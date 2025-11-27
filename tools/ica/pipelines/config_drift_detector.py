#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2025 AMPEL360 Project Contributors

"""
config_drift_detector.py

Compares aircraft configuration vs. documentation baselines to detect drift.
Identifies discrepancies between as-designed, as-built, and as-documented states.

Usage:
    python -m tools.ica.pipelines.config_drift_detector --aircraft MSN001
    python -m tools.ica.pipelines.config_drift_detector --baseline v1.0.0 --current HEAD
"""

import argparse
import hashlib
import json
import logging
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
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
BASELINES_DIR = REPO_ROOT / "cd" / "baselines"


class DriftType(str, Enum):
    """Types of configuration drift."""
    ADDED = "added"
    REMOVED = "removed"
    MODIFIED = "modified"
    VERSION_MISMATCH = "version_mismatch"
    CHECKSUM_MISMATCH = "checksum_mismatch"


class DriftSeverity(str, Enum):
    """Severity levels for configuration drift."""
    CRITICAL = "critical"  # Safety-critical component drift
    HIGH = "high"          # ICA-relevant component drift
    MEDIUM = "medium"      # Standard component drift
    LOW = "low"            # Documentation-only drift
    INFO = "info"          # Informational drift


@dataclass
class DriftItem:
    """A single configuration drift item."""
    component_id: str
    component_name: str
    drift_type: DriftType
    severity: DriftSeverity
    baseline_value: Optional[str]
    current_value: Optional[str]
    ata_chapter: Optional[str]
    description: str
    requires_action: bool = True
    recommended_action: str = ""


@dataclass
class DriftReport:
    """Complete configuration drift report."""
    report_id: str
    generated_at: str
    baseline_ref: str
    current_ref: str
    aircraft_msn: Optional[str]
    total_components: int
    drifts_detected: int
    drift_items: List[DriftItem] = field(default_factory=list)
    critical_count: int = 0
    high_count: int = 0
    medium_count: int = 0
    low_count: int = 0
    requires_ica_update: bool = False


class ConfigDriftDetector:
    """Detects configuration drift between baselines."""
    
    # ATA chapters with safety-critical components
    SAFETY_CRITICAL_ATA = {
        "27": "Flight Controls",
        "28": "Fuel",
        "29": "Hydraulic Power",
        "32": "Landing Gear",
        "71": "Powerplant",
        "72": "Engine",
    }
    
    # ICA-relevant ATA chapters
    ICA_RELEVANT_ATA = {
        "04": "Airworthiness Limitations",
        "05": "Time Limits/Maintenance Checks",
        "24": "Electrical Power",
        "53": "Fuselage",
        "85": "Infrastructure Interface Standards",
        "95": "Digital Product Passport",
    }
    
    def __init__(self, repo_root: Path = REPO_ROOT):
        self.repo_root = repo_root
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        BASELINES_DIR.mkdir(parents=True, exist_ok=True)
    
    def generate_report_id(self) -> str:
        """Generate unique report ID."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        content = f"DRIFT-{timestamp}"
        hash_suffix = hashlib.sha256(content.encode()).hexdigest()[:8].upper()
        return f"DRIFT-{timestamp}-{hash_suffix}"
    
    def calculate_checksum(self, filepath: Path) -> str:
        """Calculate SHA-256 checksum."""
        if not filepath.exists():
            return ""
        sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()[:16]
    
    def extract_ata_chapter(self, path: str) -> Optional[str]:
        """Extract ATA chapter from path."""
        import re
        match = re.search(r"ATA[_-](\d{2})", path, re.IGNORECASE)
        if match:
            return match.group(1)
        match = re.search(r"(\d{2})-\d{2}-\d{2}", path)
        if match:
            return match.group(1)
        return None
    
    def determine_severity(self, ata_chapter: Optional[str], drift_type: DriftType) -> DriftSeverity:
        """Determine drift severity based on ATA chapter and drift type."""
        if ata_chapter in self.SAFETY_CRITICAL_ATA:
            return DriftSeverity.CRITICAL if drift_type != DriftType.MODIFIED else DriftSeverity.HIGH
        elif ata_chapter in self.ICA_RELEVANT_ATA:
            return DriftSeverity.HIGH if drift_type != DriftType.MODIFIED else DriftSeverity.MEDIUM
        else:
            return DriftSeverity.MEDIUM if drift_type != DriftType.MODIFIED else DriftSeverity.LOW
    
    def get_file_list(self, ref: str) -> Dict[str, str]:
        """Get list of files and their checksums at a specific ref."""
        files = {}
        try:
            # Get file list at ref
            result = subprocess.run(
                ["git", "ls-tree", "-r", "--name-only", ref],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            
            for filepath in result.stdout.strip().split("\n"):
                if filepath and not filepath.startswith("."):
                    # Get file content hash
                    hash_result = subprocess.run(
                        ["git", "rev-parse", f"{ref}:{filepath}"],
                        cwd=self.repo_root,
                        capture_output=True,
                        text=True
                    )
                    if hash_result.returncode == 0:
                        files[filepath] = hash_result.stdout.strip()[:16]
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to get file list for {ref}: {e}")
        
        return files
    
    def compare_configurations(
        self,
        baseline_ref: str,
        current_ref: str
    ) -> List[DriftItem]:
        """Compare configurations between two refs."""
        baseline_files = self.get_file_list(baseline_ref)
        current_files = self.get_file_list(current_ref)
        
        drift_items = []
        
        # Check for added files
        for filepath in current_files:
            if filepath not in baseline_files:
                ata = self.extract_ata_chapter(filepath)
                severity = self.determine_severity(ata, DriftType.ADDED)
                
                drift_items.append(DriftItem(
                    component_id=filepath,
                    component_name=Path(filepath).name,
                    drift_type=DriftType.ADDED,
                    severity=severity,
                    baseline_value=None,
                    current_value=current_files[filepath],
                    ata_chapter=ata,
                    description=f"New file added: {filepath}",
                    requires_action=severity in (DriftSeverity.CRITICAL, DriftSeverity.HIGH),
                    recommended_action="Review new component and update ICA documentation"
                ))
        
        # Check for removed files
        for filepath in baseline_files:
            if filepath not in current_files:
                ata = self.extract_ata_chapter(filepath)
                severity = self.determine_severity(ata, DriftType.REMOVED)
                
                drift_items.append(DriftItem(
                    component_id=filepath,
                    component_name=Path(filepath).name,
                    drift_type=DriftType.REMOVED,
                    severity=severity,
                    baseline_value=baseline_files[filepath],
                    current_value=None,
                    ata_chapter=ata,
                    description=f"File removed: {filepath}",
                    requires_action=severity in (DriftSeverity.CRITICAL, DriftSeverity.HIGH),
                    recommended_action="Verify removal and update ICA documentation"
                ))
        
        # Check for modified files
        for filepath in baseline_files:
            if filepath in current_files:
                if baseline_files[filepath] != current_files[filepath]:
                    ata = self.extract_ata_chapter(filepath)
                    severity = self.determine_severity(ata, DriftType.MODIFIED)
                    
                    drift_items.append(DriftItem(
                        component_id=filepath,
                        component_name=Path(filepath).name,
                        drift_type=DriftType.MODIFIED,
                        severity=severity,
                        baseline_value=baseline_files[filepath],
                        current_value=current_files[filepath],
                        ata_chapter=ata,
                        description=f"File modified: {filepath}",
                        requires_action=severity in (DriftSeverity.CRITICAL, DriftSeverity.HIGH),
                        recommended_action="Review changes and update related documentation"
                    ))
        
        return drift_items
    
    def detect_drift(
        self,
        baseline_ref: str = "HEAD~1",
        current_ref: str = "HEAD",
        aircraft_msn: Optional[str] = None
    ) -> DriftReport:
        """Detect configuration drift between refs."""
        logger.info(f"Detecting drift: {baseline_ref} -> {current_ref}")
        
        drift_items = self.compare_configurations(baseline_ref, current_ref)
        
        # Count by severity
        critical = sum(1 for d in drift_items if d.severity == DriftSeverity.CRITICAL)
        high = sum(1 for d in drift_items if d.severity == DriftSeverity.HIGH)
        medium = sum(1 for d in drift_items if d.severity == DriftSeverity.MEDIUM)
        low = sum(1 for d in drift_items if d.severity == DriftSeverity.LOW)
        
        # Get total component count
        current_files = self.get_file_list(current_ref)
        
        report = DriftReport(
            report_id=self.generate_report_id(),
            generated_at=datetime.now().isoformat(),
            baseline_ref=baseline_ref,
            current_ref=current_ref,
            aircraft_msn=aircraft_msn,
            total_components=len(current_files),
            drifts_detected=len(drift_items),
            drift_items=drift_items,
            critical_count=critical,
            high_count=high,
            medium_count=medium,
            low_count=low,
            requires_ica_update=critical > 0 or high > 0
        )
        
        return report
    
    def generate_markdown_report(self, report: DriftReport) -> str:
        """Generate markdown report."""
        lines = [
            "# Configuration Drift Report",
            "",
            f"**Report ID:** `{report.report_id}`  ",
            f"**Generated:** {report.generated_at}  ",
            f"**Baseline:** `{report.baseline_ref}`  ",
            f"**Current:** `{report.current_ref}`  ",
        ]
        
        if report.aircraft_msn:
            lines.append(f"**Aircraft MSN:** {report.aircraft_msn}  ")
        
        lines.extend([
            "",
            "---",
            "",
            "## Summary",
            "",
            f"**Total Components:** {report.total_components}  ",
            f"**Drifts Detected:** {report.drifts_detected}  ",
            "",
            "| Severity | Count |",
            "|----------|-------|",
            f"| 🔴 Critical | {report.critical_count} |",
            f"| 🟠 High | {report.high_count} |",
            f"| 🟡 Medium | {report.medium_count} |",
            f"| 🟢 Low | {report.low_count} |",
            "",
        ])
        
        if report.requires_ica_update:
            lines.extend([
                "> ⚠️ **ICA UPDATE REQUIRED** - Critical or high-severity drift detected.",
                ""
            ])
        
        if report.drift_items:
            lines.extend([
                "## Detailed Drift Items",
                "",
            ])
            
            # Group by severity
            for severity in [DriftSeverity.CRITICAL, DriftSeverity.HIGH, DriftSeverity.MEDIUM, DriftSeverity.LOW]:
                items = [d for d in report.drift_items if d.severity == severity]
                if items:
                    icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}[severity.value]
                    lines.extend([
                        f"### {icon} {severity.value.capitalize()} Severity",
                        "",
                        "| Component | Type | ATA | Description | Action Required |",
                        "|-----------|------|-----|-------------|-----------------|",
                    ])
                    
                    for item in items:
                        ata = item.ata_chapter or "-"
                        action = "Yes" if item.requires_action else "No"
                        lines.append(
                            f"| `{item.component_name}` | {item.drift_type.value} | {ata} | {item.description[:50]}... | {action} |"
                        )
                    
                    lines.append("")
        else:
            lines.extend([
                "## Findings",
                "",
                "✅ No configuration drift detected.",
                ""
            ])
        
        lines.extend([
            "---",
            "",
            "## Document Control",
            "",
            "- Generated by: `config_drift_detector.py` (AI-assisted, prompted by Amedeo Pelliccia)",
            "- Part of: CAOS ICA Enabling Toolchain",
            "",
        ])
        
        return "\n".join(lines)
    
    def save_report(self, report: DriftReport) -> tuple:
        """Save drift report."""
        # Save JSON
        json_path = REPORTS_DIR / f"{report.report_id}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            data = asdict(report)
            # Convert enums to strings
            for item in data.get("drift_items", []):
                item["drift_type"] = item["drift_type"].value if hasattr(item["drift_type"], "value") else item["drift_type"]
                item["severity"] = item["severity"].value if hasattr(item["severity"], "value") else item["severity"]
            json.dump(data, f, indent=2)
        
        # Save Markdown
        md_path = REPORTS_DIR / f"{report.report_id}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(self.generate_markdown_report(report))
        
        logger.info(f"Reports saved: {json_path}, {md_path}")
        return json_path, md_path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Detect configuration drift between baselines"
    )
    parser.add_argument(
        "--baseline",
        default="HEAD~1",
        help="Baseline reference"
    )
    parser.add_argument(
        "--current",
        default="HEAD",
        help="Current reference"
    )
    parser.add_argument(
        "--aircraft",
        help="Aircraft MSN for tracking"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Custom output directory"
    )
    parser.add_argument(
        "--fail-on-critical",
        action="store_true",
        help="Exit with error if critical drift detected"
    )
    
    args = parser.parse_args()
    
    detector = ConfigDriftDetector()
    
    if args.output_dir:
        global REPORTS_DIR
        REPORTS_DIR = args.output_dir
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Detect drift
    report = detector.detect_drift(
        baseline_ref=args.baseline,
        current_ref=args.current,
        aircraft_msn=args.aircraft
    )
    
    # Save reports
    json_path, md_path = detector.save_report(report)
    
    # Print summary
    print(f"\n{'='*60}")
    print("Configuration Drift Detection Complete")
    print(f"{'='*60}")
    print(f"Report ID: {report.report_id}")
    print(f"Components Analyzed: {report.total_components}")
    print(f"Drifts Detected: {report.drifts_detected}")
    print(f"\nSeverity Breakdown:")
    print(f"  🔴 Critical: {report.critical_count}")
    print(f"  🟠 High: {report.high_count}")
    print(f"  🟡 Medium: {report.medium_count}")
    print(f"  🟢 Low: {report.low_count}")
    
    if report.requires_ica_update:
        print("\n⚠️  ICA UPDATE REQUIRED")
    
    print(f"\nReports saved:")
    print(f"  - {json_path}")
    print(f"  - {md_path}")
    
    if args.fail_on_critical and report.critical_count > 0:
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
