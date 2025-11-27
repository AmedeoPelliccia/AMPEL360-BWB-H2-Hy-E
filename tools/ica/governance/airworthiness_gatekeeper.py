#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2025 AMPEL360 Project Contributors

"""
airworthiness_gatekeeper.py

Blocks PRs affecting ICA without proper delta documentation.
Enforces airworthiness documentation requirements before merge.

Usage:
    python -m tools.ica.governance.airworthiness_gatekeeper --check
    python -m tools.ica.governance.airworthiness_gatekeeper --pr 123
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


class GateResult:
    """Gate check result."""
    PASS = "pass"
    WARN = "warn"
    BLOCK = "block"


@dataclass
class GateCheck:
    """Individual gate check result."""
    check_id: str
    name: str
    result: str  # pass, warn, block
    description: str
    details: List[str] = field(default_factory=list)
    remediation: str = ""


@dataclass
class GatekeeperReport:
    """Complete gatekeeper report."""
    report_id: str
    checked_at: str
    commit_ref: str
    overall_result: str  # pass, warn, block
    checks: List[GateCheck] = field(default_factory=list)
    pass_count: int = 0
    warn_count: int = 0
    block_count: int = 0
    ica_documentation_required: bool = False
    delta_documentation_present: bool = False


class AirworthinessGatekeeper:
    """Enforces airworthiness documentation requirements."""
    
    # ICA-relevant path patterns
    ICA_PATTERNS = [
        r"AIRWORTHINESS", r"ICA", r"SAFETY", r"CERTIFICATION",
        r"04_AIRWORTHINESS", r"05_TIME_LIMITS", r"10_CERTIFICATION",
        r"FHA", r"FMEA", r"FTA", r"SSA", r"PSSA",
        r"CS[-\s]?25", r"DO-178", r"DO-254",
    ]
    
    # Safety-critical ATA chapters
    SAFETY_CRITICAL_ATA = ["27", "28", "29", "32", "71", "72", "73"]
    
    # Required documentation patterns for ICA changes
    REQUIRED_DOC_PATTERNS = {
        "delta_document": r"cd/deltas/DELTA-.*\.(md|json)",
        "impact_analysis": r"cd/reports/ica_impact.*\.(md|json)",
        "change_summary": r"CHANGELOG|CHANGES|REVISION",
    }
    
    def __init__(self, repo_root: Path = REPO_ROOT):
        self.repo_root = repo_root
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    def get_changed_files(self, ref: str = "HEAD") -> List[str]:
        """Get changed files."""
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
            return []
    
    def extract_ata_chapter(self, filepath: str) -> Optional[str]:
        """Extract ATA chapter from path."""
        match = re.search(r"ATA[_-](\d{2})", filepath, re.IGNORECASE)
        if match:
            return match.group(1)
        match = re.search(r"(\d{2})-\d{2}-\d{2}", filepath)
        if match:
            return match.group(1)
        return None
    
    def is_ica_relevant(self, filepath: str) -> bool:
        """Check if file is ICA-relevant."""
        filepath_upper = filepath.upper()
        
        # Check patterns
        for pattern in self.ICA_PATTERNS:
            if re.search(pattern, filepath_upper):
                return True
        
        # Check ATA chapters
        ata = self.extract_ata_chapter(filepath)
        if ata in self.SAFETY_CRITICAL_ATA:
            return True
        
        return False
    
    def check_ica_relevance(self, changed_files: List[str]) -> GateCheck:
        """Check if changes affect ICA-relevant content."""
        ica_files = [f for f in changed_files if self.is_ica_relevant(f)]
        
        if not ica_files:
            return GateCheck(
                check_id="ICA-001",
                name="ICA Relevance Check",
                result=GateResult.PASS,
                description="No ICA-relevant changes detected",
                details=[]
            )
        
        return GateCheck(
            check_id="ICA-001",
            name="ICA Relevance Check",
            result=GateResult.WARN,
            description=f"Found {len(ica_files)} ICA-relevant file(s) modified",
            details=ica_files[:10],  # Limit to first 10
            remediation="Ensure proper ICA documentation is included"
        )
    
    def check_delta_documentation(self, changed_files: List[str]) -> GateCheck:
        """Check if delta documentation is present."""
        delta_files = [
            f for f in changed_files
            if re.match(self.REQUIRED_DOC_PATTERNS["delta_document"], f)
        ]
        
        if delta_files:
            return GateCheck(
                check_id="ICA-002",
                name="Delta Documentation Check",
                result=GateResult.PASS,
                description="Delta documentation present",
                details=delta_files
            )
        
        # Check if ICA-relevant changes exist
        ica_files = [f for f in changed_files if self.is_ica_relevant(f)]
        
        if ica_files:
            return GateCheck(
                check_id="ICA-002",
                name="Delta Documentation Check",
                result=GateResult.BLOCK,
                description="ICA changes detected but no delta documentation found",
                details=ica_files[:5],
                remediation="Run delta_doc_synthesizer.py to generate delta documentation"
            )
        
        return GateCheck(
            check_id="ICA-002",
            name="Delta Documentation Check",
            result=GateResult.PASS,
            description="No ICA changes requiring delta documentation",
            details=[]
        )
    
    def check_impact_analysis(self, changed_files: List[str]) -> GateCheck:
        """Check if impact analysis is present for ICA changes."""
        impact_files = [
            f for f in changed_files
            if re.match(self.REQUIRED_DOC_PATTERNS["impact_analysis"], f)
        ]
        
        if impact_files:
            return GateCheck(
                check_id="ICA-003",
                name="Impact Analysis Check",
                result=GateResult.PASS,
                description="Impact analysis present",
                details=impact_files
            )
        
        # Check for safety-critical changes
        safety_files = [
            f for f in changed_files
            if self.extract_ata_chapter(f) in self.SAFETY_CRITICAL_ATA
        ]
        
        if safety_files:
            return GateCheck(
                check_id="ICA-003",
                name="Impact Analysis Check",
                result=GateResult.BLOCK,
                description="Safety-critical changes detected but no impact analysis found",
                details=safety_files[:5],
                remediation="Run ica_impact_analyzer.py to generate impact analysis"
            )
        
        return GateCheck(
            check_id="ICA-003",
            name="Impact Analysis Check",
            result=GateResult.PASS,
            description="No safety-critical changes requiring impact analysis",
            details=[]
        )
    
    def check_document_control(self, changed_files: List[str]) -> GateCheck:
        """Check if modified documents have proper document control sections."""
        md_files = [f for f in changed_files if f.endswith(".md")]
        missing_control = []
        
        for filepath in md_files:
            full_path = self.repo_root / filepath
            if full_path.exists():
                try:
                    content = full_path.read_text(encoding="utf-8")
                    if "Document Control" not in content and "Generated by" not in content:
                        missing_control.append(filepath)
                except Exception:
                    pass
        
        if missing_control:
            return GateCheck(
                check_id="ICA-004",
                name="Document Control Check",
                result=GateResult.WARN,
                description=f"{len(missing_control)} document(s) missing Document Control section",
                details=missing_control[:5],
                remediation="Add Document Control section to modified documents"
            )
        
        return GateCheck(
            check_id="ICA-004",
            name="Document Control Check",
            result=GateResult.PASS,
            description="All documents have proper Document Control sections",
            details=[]
        )
    
    def check_cs25_references(self, changed_files: List[str]) -> GateCheck:
        """Check for CS-25 reference modifications."""
        cs25_files = []
        
        for filepath in changed_files:
            full_path = self.repo_root / filepath
            if full_path.exists() and filepath.endswith(".md"):
                try:
                    content = full_path.read_text(encoding="utf-8")
                    if re.search(r"CS[-\s]?25\.\d+", content):
                        cs25_files.append(filepath)
                except Exception:
                    pass
        
        if cs25_files:
            return GateCheck(
                check_id="ICA-005",
                name="CS-25 Reference Check",
                result=GateResult.WARN,
                description=f"{len(cs25_files)} file(s) contain CS-25 references",
                details=cs25_files[:5],
                remediation="Verify CS-25 compliance requirements are met"
            )
        
        return GateCheck(
            check_id="ICA-005",
            name="CS-25 Reference Check",
            result=GateResult.PASS,
            description="No CS-25 references detected in changes",
            details=[]
        )
    
    def run_all_checks(self, ref: str = "HEAD") -> GatekeeperReport:
        """Run all gatekeeper checks."""
        logger.info(f"Running airworthiness gatekeeper checks for {ref}")
        
        changed_files = self.get_changed_files(ref)
        
        checks = [
            self.check_ica_relevance(changed_files),
            self.check_delta_documentation(changed_files),
            self.check_impact_analysis(changed_files),
            self.check_document_control(changed_files),
            self.check_cs25_references(changed_files),
        ]
        
        # Count results
        pass_count = sum(1 for c in checks if c.result == GateResult.PASS)
        warn_count = sum(1 for c in checks if c.result == GateResult.WARN)
        block_count = sum(1 for c in checks if c.result == GateResult.BLOCK)
        
        # Determine overall result
        if block_count > 0:
            overall = GateResult.BLOCK
        elif warn_count > 0:
            overall = GateResult.WARN
        else:
            overall = GateResult.PASS
        
        # Check for ICA documentation requirement
        ica_files = [f for f in changed_files if self.is_ica_relevant(f)]
        delta_present = any(
            re.match(self.REQUIRED_DOC_PATTERNS["delta_document"], f)
            for f in changed_files
        )
        
        report = GatekeeperReport(
            report_id=f"GATE-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            checked_at=datetime.now().isoformat(),
            commit_ref=ref,
            overall_result=overall,
            checks=checks,
            pass_count=pass_count,
            warn_count=warn_count,
            block_count=block_count,
            ica_documentation_required=len(ica_files) > 0,
            delta_documentation_present=delta_present
        )
        
        return report
    
    def generate_markdown_report(self, report: GatekeeperReport) -> str:
        """Generate markdown report."""
        result_icon = {
            GateResult.PASS: "✅",
            GateResult.WARN: "⚠️",
            GateResult.BLOCK: "🛑",
        }
        
        lines = [
            "# Airworthiness Gatekeeper Report",
            "",
            f"**Report ID:** `{report.report_id}`  ",
            f"**Checked:** {report.checked_at}  ",
            f"**Commit:** `{report.commit_ref}`  ",
            f"**Overall Result:** {result_icon.get(report.overall_result, '❓')} {report.overall_result.upper()}",
            "",
            "---",
            "",
            "## Summary",
            "",
            f"| Result | Count |",
            f"|--------|-------|",
            f"| ✅ Pass | {report.pass_count} |",
            f"| ⚠️ Warn | {report.warn_count} |",
            f"| 🛑 Block | {report.block_count} |",
            "",
        ]
        
        if report.overall_result == GateResult.BLOCK:
            lines.extend([
                "> 🛑 **MERGE BLOCKED** - Required documentation or checks are missing.",
                ""
            ])
        
        lines.extend([
            "## Check Details",
            "",
        ])
        
        for check in report.checks:
            icon = result_icon.get(check.result, "❓")
            lines.extend([
                f"### {icon} {check.name}",
                "",
                f"**ID:** `{check.check_id}`  ",
                f"**Result:** {check.result}  ",
                f"**Description:** {check.description}",
                "",
            ])
            
            if check.details:
                lines.append("**Affected files:**")
                for detail in check.details:
                    lines.append(f"- `{detail}`")
                lines.append("")
            
            if check.remediation:
                lines.extend([
                    f"**Remediation:** {check.remediation}",
                    ""
                ])
        
        lines.extend([
            "---",
            "",
            "## Document Control",
            "",
            "- Generated by: `airworthiness_gatekeeper.py` (AI-assisted, prompted by Amedeo Pelliccia)",
            "- Part of: CAOS ICA Enabling Toolchain",
            "",
        ])
        
        return "\n".join(lines)
    
    def save_report(self, report: GatekeeperReport) -> tuple:
        """Save gatekeeper report."""
        # Save JSON
        json_path = REPORTS_DIR / f"{report.report_id}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(asdict(report), f, indent=2)
        
        # Save Markdown
        md_path = REPORTS_DIR / f"{report.report_id}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(self.generate_markdown_report(report))
        
        logger.info(f"Reports saved: {json_path}, {md_path}")
        return json_path, md_path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Airworthiness gatekeeper for ICA documentation"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Run gatekeeper checks"
    )
    parser.add_argument(
        "--commit",
        default="HEAD",
        help="Commit to check"
    )
    parser.add_argument(
        "--pr",
        type=int,
        help="PR number to check"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Custom output directory"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with error on any warning or block"
    )
    
    args = parser.parse_args()
    
    gatekeeper = AirworthinessGatekeeper()
    
    if args.output_dir:
        global REPORTS_DIR
        REPORTS_DIR = args.output_dir
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Run checks
    report = gatekeeper.run_all_checks(args.commit)
    
    # Save reports
    json_path, md_path = gatekeeper.save_report(report)
    
    # Print summary
    result_icon = {
        GateResult.PASS: "✅",
        GateResult.WARN: "⚠️",
        GateResult.BLOCK: "🛑",
    }
    
    print(f"\n{'='*60}")
    print("Airworthiness Gatekeeper Check Complete")
    print(f"{'='*60}")
    print(f"Report ID: {report.report_id}")
    print(f"Overall Result: {result_icon.get(report.overall_result, '❓')} {report.overall_result.upper()}")
    print(f"\nCheck Results:")
    
    for check in report.checks:
        icon = result_icon.get(check.result, "❓")
        print(f"  {icon} {check.name}: {check.result}")
        if check.result != GateResult.PASS and check.remediation:
            print(f"     └─ {check.remediation}")
    
    print(f"\nReports saved:")
    print(f"  - {json_path}")
    print(f"  - {md_path}")
    
    # Determine exit code
    if report.overall_result == GateResult.BLOCK:
        return 1
    if args.strict and report.overall_result == GateResult.WARN:
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
