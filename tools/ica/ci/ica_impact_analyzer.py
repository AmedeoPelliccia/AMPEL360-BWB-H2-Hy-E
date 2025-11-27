# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python3

"""
ica_impact_analyzer.py

Analyzes commits and PRs to flag changes that impact airworthiness intents.
Detects modifications to CS-25 references, safety documents, ICA content,
and other certification-relevant materials.

Usage:
    python -m tools.ica.ci.ica_impact_analyzer --check
    python -m tools.ica.ci.ica_impact_analyzer --pr 123
    python -m tools.ica.ci.ica_impact_analyzer --commit abc123
"""

import argparse
import json
import logging
import re
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Repository root
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
REPORTS_DIR = REPO_ROOT / "cd" / "reports"


@dataclass
class ICAImpact:
    """Represents an ICA impact finding."""
    file_path: str
    impact_type: str
    severity: str  # critical, high, medium, low
    description: str
    line_numbers: List[int] = field(default_factory=list)
    cs25_references: List[str] = field(default_factory=list)
    requires_review: bool = True


@dataclass
class ICAAnalysisResult:
    """Complete ICA impact analysis result."""
    analyzed_at: str
    commit_ref: str
    total_files_analyzed: int
    files_with_impact: int
    impacts: List[ICAImpact] = field(default_factory=list)
    critical_count: int = 0
    high_count: int = 0
    medium_count: int = 0
    low_count: int = 0
    requires_ica_review: bool = False
    requires_safety_review: bool = False


class ICAImpactAnalyzer:
    """Analyzes changes for ICA (Instructions for Continued Airworthiness) impact."""
    
    # CS-25 reference patterns
    CS25_PATTERNS = [
        r"CS[-\s]?25\.(\d+)",
        r"25\.(\d+)\([a-z]\)",
        r"AMC\s+25\.(\d+)",
        r"GM\s+25\.(\d+)",
    ]
    
    # Safety-critical section references
    SAFETY_SECTIONS = {
        "25.1309": "Equipment, Systems, and Installations",
        "25.1301": "Function and Installation",
        "25.1302": "Installed Systems and Equipment for Use by the Crew",
        "25.1307": "Miscellaneous Equipment",
        "25.1322": "Flightcrew Alerting",
        "25.1329": "Flight Guidance System",
        "25.1333": "Instrument Systems",
        "25.671": "General (Flight Controls)",
        "25.672": "Stability Augmentation and Automatic Systems",
        "25.1435": "Hydraulic Systems",
    }
    
    # ICA-relevant keywords
    ICA_KEYWORDS = [
        "airworthiness", "ica", "amm", "cmm", "srm", "ipc",
        "service bulletin", "airworthiness directive", "ad",
        "maintenance", "inspection", "overhaul", "repair",
        "life limit", "time limit", "interval", "check",
        "mrbr", "mpd", "fha", "fmea", "fta", "ssa", "pssa",
        "safety assessment", "hazard", "failure mode",
        "critical", "essential", "dah", "certification"
    ]
    
    # File path patterns indicating ICA relevance
    ICA_PATH_PATTERNS = [
        r"SAFETY", r"CERTIFICATION", r"AIRWORTHINESS",
        r"MAINTENANCE", r"SERVICE", r"INSPECTION",
        r"04_AIRWORTHINESS", r"05_TIME_LIMITS",
        r"10_CERTIFICATION", r"DO-178", r"DO-254",
        r"FHA", r"FMEA", r"FTA", r"SSA",
    ]
    
    # Critical ATA chapters (safety-critical systems)
    CRITICAL_ATA_CHAPTERS = {
        "27": "Flight Controls",
        "28": "Fuel",
        "29": "Hydraulic Power",
        "32": "Landing Gear",
        "49": "Airborne Auxiliary Power",
        "71": "Powerplant",
        "72": "Engine",
        "73": "Engine Fuel and Control",
        "74": "Ignition",
        "75": "Air",
        "76": "Engine Controls",
        "77": "Engine Indicating",
        "78": "Exhaust",
        "79": "Oil",
        "80": "Starting",
    }
    
    def __init__(self, repo_root: Path = REPO_ROOT):
        self.repo_root = repo_root
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    def get_changed_files(self, ref: str = "HEAD") -> List[str]:
        """Get list of changed files compared to base."""
        try:
            result = subprocess.run(
                ["git", "diff", "--name-only", f"{ref}~1", ref],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            return [f for f in result.stdout.strip().split("\n") if f]
        except subprocess.CalledProcessError:
            # Fallback: get all files in current diff
            try:
                result = subprocess.run(
                    ["git", "diff", "--name-only", "--cached"],
                    cwd=self.repo_root,
                    capture_output=True,
                    text=True
                )
                return [f for f in result.stdout.strip().split("\n") if f]
            except subprocess.CalledProcessError:
                return []
    
    def get_file_diff(self, filepath: str, ref: str = "HEAD") -> str:
        """Get diff content for a specific file."""
        try:
            result = subprocess.run(
                ["git", "diff", f"{ref}~1", ref, "--", filepath],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            return ""
    
    def extract_cs25_references(self, content: str) -> List[str]:
        """Extract CS-25 references from content."""
        references = []
        for pattern in self.CS25_PATTERNS:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                ref = f"25.{match}" if not match.startswith("25.") else match
                if ref not in references:
                    references.append(ref)
        return references
    
    def extract_ata_chapter(self, filepath: str) -> Optional[str]:
        """Extract ATA chapter from file path."""
        match = re.search(r"ATA[_-](\d{2})", filepath, re.IGNORECASE)
        if match:
            return match.group(1)
        match = re.search(r"(\d{2})-\d{2}-\d{2}", filepath)
        if match:
            return match.group(1)
        return None
    
    def is_safety_critical_path(self, filepath: str) -> bool:
        """Check if file path indicates safety-critical content."""
        filepath_upper = filepath.upper()
        
        # Check path patterns
        for pattern in self.ICA_PATH_PATTERNS:
            if re.search(pattern, filepath_upper):
                return True
        
        # Check ATA chapter
        ata = self.extract_ata_chapter(filepath)
        if ata and ata in self.CRITICAL_ATA_CHAPTERS:
            return True
        
        return False
    
    def analyze_content_impact(self, content: str, filepath: str) -> List[ICAImpact]:
        """Analyze content for ICA impact."""
        impacts = []
        content_lower = content.lower()
        
        # Check for CS-25 references
        cs25_refs = self.extract_cs25_references(content)
        if cs25_refs:
            safety_refs = [r for r in cs25_refs if r in self.SAFETY_SECTIONS]
            
            severity = "critical" if safety_refs else "high"
            impacts.append(ICAImpact(
                file_path=filepath,
                impact_type="cs25_reference_modified",
                severity=severity,
                description=f"Changes affect CS-25 referenced content: {', '.join(cs25_refs)}",
                cs25_references=cs25_refs,
                requires_review=True
            ))
        
        # Check for ICA keywords
        found_keywords = []
        for keyword in self.ICA_KEYWORDS:
            if keyword in content_lower:
                found_keywords.append(keyword)
        
        if found_keywords:
            severity = "high" if any(k in ["safety", "critical", "hazard", "failure"] for k in found_keywords) else "medium"
            impacts.append(ICAImpact(
                file_path=filepath,
                impact_type="ica_content_modified",
                severity=severity,
                description=f"Changes affect ICA-relevant content containing: {', '.join(found_keywords[:5])}",
                requires_review=True
            ))
        
        # Check for maintenance interval changes
        interval_patterns = [
            r"interval[:\s]+\d+",
            r"every\s+\d+\s+(hours|cycles|days|months)",
            r"time limit[:\s]+\d+",
            r"life limit[:\s]+\d+",
        ]
        
        for pattern in interval_patterns:
            if re.search(pattern, content_lower):
                impacts.append(ICAImpact(
                    file_path=filepath,
                    impact_type="maintenance_interval_modified",
                    severity="high",
                    description="Changes affect maintenance intervals or time limits",
                    requires_review=True
                ))
                break
        
        return impacts
    
    def analyze_file(self, filepath: str, ref: str = "HEAD") -> List[ICAImpact]:
        """Analyze a single file for ICA impact."""
        impacts = []
        
        # Check if path itself indicates ICA relevance
        if self.is_safety_critical_path(filepath):
            ata = self.extract_ata_chapter(filepath)
            ata_desc = self.CRITICAL_ATA_CHAPTERS.get(ata, "")
            
            impacts.append(ICAImpact(
                file_path=filepath,
                impact_type="safety_critical_file_modified",
                severity="critical" if ata in self.CRITICAL_ATA_CHAPTERS else "high",
                description=f"Modification to safety-critical file path{f' (ATA {ata} - {ata_desc})' if ata_desc else ''}",
                requires_review=True
            ))
        
        # Get and analyze diff content
        diff_content = self.get_file_diff(filepath, ref)
        if diff_content:
            content_impacts = self.analyze_content_impact(diff_content, filepath)
            impacts.extend(content_impacts)
        
        return impacts
    
    def analyze_changes(self, ref: str = "HEAD") -> ICAAnalysisResult:
        """Analyze all changes for ICA impact."""
        logger.info(f"Analyzing changes at ref: {ref}")
        
        changed_files = self.get_changed_files(ref)
        all_impacts = []
        files_with_impact = set()
        
        for filepath in changed_files:
            impacts = self.analyze_file(filepath, ref)
            if impacts:
                all_impacts.extend(impacts)
                files_with_impact.add(filepath)
        
        # Count by severity
        critical = sum(1 for i in all_impacts if i.severity == "critical")
        high = sum(1 for i in all_impacts if i.severity == "high")
        medium = sum(1 for i in all_impacts if i.severity == "medium")
        low = sum(1 for i in all_impacts if i.severity == "low")
        
        result = ICAAnalysisResult(
            analyzed_at=datetime.now().isoformat(),
            commit_ref=ref,
            total_files_analyzed=len(changed_files),
            files_with_impact=len(files_with_impact),
            impacts=all_impacts,
            critical_count=critical,
            high_count=high,
            medium_count=medium,
            low_count=low,
            requires_ica_review=high > 0 or critical > 0,
            requires_safety_review=critical > 0
        )
        
        return result
    
    def generate_report(self, result: ICAAnalysisResult) -> str:
        """Generate markdown report from analysis result."""
        lines = [
            "# ICA Impact Analysis Report",
            "",
            f"**Analyzed:** {result.analyzed_at}  ",
            f"**Commit:** `{result.commit_ref}`  ",
            f"**Files Analyzed:** {result.total_files_analyzed}  ",
            f"**Files with Impact:** {result.files_with_impact}  ",
            "",
            "---",
            "",
            "## Summary",
            "",
            f"| Severity | Count |",
            f"|----------|-------|",
            f"| 🔴 Critical | {result.critical_count} |",
            f"| 🟠 High | {result.high_count} |",
            f"| 🟡 Medium | {result.medium_count} |",
            f"| 🟢 Low | {result.low_count} |",
            "",
        ]
        
        if result.requires_safety_review:
            lines.extend([
                "> ⚠️ **SAFETY REVIEW REQUIRED** - Critical safety-related changes detected.",
                ""
            ])
        
        if result.requires_ica_review:
            lines.extend([
                "> 📋 **ICA REVIEW REQUIRED** - Changes may affect airworthiness documentation.",
                ""
            ])
        
        if result.impacts:
            lines.extend([
                "## Detailed Findings",
                "",
                "| File | Impact Type | Severity | Description |",
                "|------|-------------|----------|-------------|",
            ])
            
            for impact in result.impacts:
                severity_icon = {
                    "critical": "🔴",
                    "high": "🟠",
                    "medium": "🟡",
                    "low": "🟢"
                }.get(impact.severity, "⚪")
                
                lines.append(
                    f"| `{impact.file_path}` | {impact.impact_type} | {severity_icon} {impact.severity} | {impact.description} |"
                )
            
            lines.append("")
            
            # CS-25 references summary
            all_cs25 = set()
            for impact in result.impacts:
                all_cs25.update(impact.cs25_references)
            
            if all_cs25:
                lines.extend([
                    "## CS-25 References Affected",
                    "",
                ])
                for ref in sorted(all_cs25):
                    desc = self.SAFETY_SECTIONS.get(ref, "")
                    lines.append(f"- **{ref}**: {desc}" if desc else f"- **{ref}**")
                lines.append("")
        else:
            lines.extend([
                "## Findings",
                "",
                "✅ No ICA impact detected in analyzed changes.",
                ""
            ])
        
        lines.extend([
            "---",
            "",
            "## Document Control",
            "",
            "- Generated by: `ica_impact_analyzer.py` (AI-assisted, prompted by Amedeo Pelliccia)",
            "- Part of: CAOS ICA Enabling Toolchain",
            "",
        ])
        
        return "\n".join(lines)
    
    def save_report(self, result: ICAAnalysisResult) -> tuple:
        """Save analysis report in multiple formats."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save JSON
        json_path = REPORTS_DIR / f"ica_impact_{timestamp}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(asdict(result), f, indent=2, default=str)
        
        # Save Markdown
        md_path = REPORTS_DIR / f"ica_impact_{timestamp}.md"
        md_content = self.generate_report(result)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        logger.info(f"Reports saved: {json_path}, {md_path}")
        return json_path, md_path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze changes for ICA impact"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check mode - analyze HEAD and report"
    )
    parser.add_argument(
        "--commit",
        help="Specific commit to analyze"
    )
    parser.add_argument(
        "--pr",
        type=int,
        help="PR number to analyze"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Custom output directory for reports"
    )
    parser.add_argument(
        "--fail-on-critical",
        action="store_true",
        help="Exit with error code if critical issues found"
    )
    parser.add_argument(
        "--fail-on-high",
        action="store_true",
        help="Exit with error code if high or critical issues found"
    )
    
    args = parser.parse_args()
    
    analyzer = ICAImpactAnalyzer()
    
    if args.output_dir:
        global REPORTS_DIR
        REPORTS_DIR = args.output_dir
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Determine ref to analyze
    ref = args.commit if args.commit else "HEAD"
    
    # Run analysis
    result = analyzer.analyze_changes(ref)
    
    # Save reports
    json_path, md_path = analyzer.save_report(result)
    
    # Print summary
    print(f"\n{'='*60}")
    print("ICA Impact Analysis Complete")
    print(f"{'='*60}")
    print(f"Files Analyzed: {result.total_files_analyzed}")
    print(f"Files with Impact: {result.files_with_impact}")
    print(f"\nImpact Summary:")
    print(f"  🔴 Critical: {result.critical_count}")
    print(f"  🟠 High: {result.high_count}")
    print(f"  🟡 Medium: {result.medium_count}")
    print(f"  🟢 Low: {result.low_count}")
    
    if result.requires_safety_review:
        print("\n⚠️  SAFETY REVIEW REQUIRED")
    if result.requires_ica_review:
        print("📋 ICA REVIEW REQUIRED")
    
    print(f"\nReports saved:")
    print(f"  - {json_path}")
    print(f"  - {md_path}")
    
    # Determine exit code
    if args.fail_on_critical and result.critical_count > 0:
        return 1
    if args.fail_on_high and (result.critical_count > 0 or result.high_count > 0):
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
