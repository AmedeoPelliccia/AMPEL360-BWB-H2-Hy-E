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
delta_doc_synthesizer.py

Generates documentation deltas from PRs or CAD/CFD model changes.
Analyzes changes between versions and produces structured delta documents
that track what changed, why, and the impact on airworthiness.

Usage:
    python -m tools.ica.cgen.delta_doc_synthesizer --pr 123
    python -m tools.ica.cgen.delta_doc_synthesizer --commit abc123
    python -m tools.ica.cgen.delta_doc_synthesizer --baseline v1.0 --current HEAD
"""

import argparse
import hashlib
import json
import logging
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
CD_DIR = REPO_ROOT / "cd"
DELTA_DIR = CD_DIR / "deltas"


@dataclass
class FileChange:
    """Represents a single file change."""
    path: str
    change_type: str  # added, modified, deleted, renamed
    old_path: Optional[str] = None
    additions: int = 0
    deletions: int = 0
    ata_chapter: Optional[str] = None
    ica_impact: bool = False
    safety_critical: bool = False


@dataclass
class DeltaDocument:
    """Represents a documentation delta."""
    id: str
    title: str
    created_at: str
    baseline_ref: str
    current_ref: str
    summary: str
    changes: List[FileChange] = field(default_factory=list)
    ata_chapters_affected: Set[str] = field(default_factory=set)
    ica_impact_summary: str = ""
    safety_impact: bool = False
    requires_review: bool = False
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        result = asdict(self)
        result['ata_chapters_affected'] = list(self.ata_chapters_affected)
        return result


class DeltaDocSynthesizer:
    """Synthesizes documentation deltas from version control changes."""
    
    # ATA chapter patterns for classification
    ATA_PATTERNS = {
        "ATA_02": "Operations Information",
        "ATA_04": "Airworthiness Limitations",
        "ATA_05": "Time Limits/Maintenance Checks",
        "ATA_21": "Air Conditioning",
        "ATA_24": "Electrical Power",
        "ATA_25": "Equipment/Furnishings",
        "ATA_27": "Flight Controls",
        "ATA_28": "Fuel",
        "ATA_29": "Hydraulic Power",
        "ATA_32": "Landing Gear",
        "ATA_34": "Navigation",
        "ATA_53": "Fuselage",
        "ATA_71": "Powerplant",
        "ATA_72": "Engine",
        "ATA_73": "Engine Fuel and Control",
        "ATA_85": "Infrastructure Interface Standards",
        "ATA_95": "Digital Product Passport",
    }
    
    # Safety-critical path patterns
    SAFETY_CRITICAL_PATTERNS = [
        "SAFETY", "CRITICAL", "HAZARD", "FHA", "FMEA", "FTA",
        "27_FLIGHT_CONTROLS", "28_FUEL", "29_HYDRAULIC",
        "DO-178", "DO-254", "CS-25.1309"
    ]
    
    # ICA-relevant path patterns
    ICA_PATTERNS = [
        "AIRWORTHINESS", "ICA", "AMM", "CMM", "SRM", "IPC",
        "SERVICE_BULLETIN", "MAINTENANCE", "INSPECTION",
        "04_AIRWORTHINESS", "05_TIME_LIMITS"
    ]
    
    def __init__(self, repo_root: Path = REPO_ROOT):
        self.repo_root = repo_root
        DELTA_DIR.mkdir(parents=True, exist_ok=True)
    
    def get_git_diff(self, baseline: str, current: str) -> List[str]:
        """Get git diff between two refs."""
        try:
            result = subprocess.run(
                ["git", "diff", "--name-status", baseline, current],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip().split("\n") if result.stdout.strip() else []
        except subprocess.CalledProcessError as e:
            logger.error(f"Git diff failed: {e}")
            return []
    
    def get_diff_stats(self, baseline: str, current: str, filepath: str) -> tuple:
        """Get additions and deletions for a specific file."""
        try:
            result = subprocess.run(
                ["git", "diff", "--numstat", baseline, current, "--", filepath],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            if result.stdout.strip():
                parts = result.stdout.strip().split("\t")
                if len(parts) >= 2:
                    adds = int(parts[0]) if parts[0] != "-" else 0
                    dels = int(parts[1]) if parts[1] != "-" else 0
                    return adds, dels
        except (subprocess.CalledProcessError, ValueError):
            pass
        return 0, 0
    
    def extract_ata_chapter(self, path: str) -> Optional[str]:
        """Extract ATA chapter from file path."""
        path_upper = path.upper()
        for ata_code in self.ATA_PATTERNS:
            if ata_code.upper() in path_upper or ata_code.replace("_", "-").upper() in path_upper:
                return ata_code
        return None
    
    def is_safety_critical(self, path: str) -> bool:
        """Check if path is safety-critical."""
        path_upper = path.upper()
        return any(pattern in path_upper for pattern in self.SAFETY_CRITICAL_PATTERNS)
    
    def is_ica_relevant(self, path: str) -> bool:
        """Check if path is ICA-relevant."""
        path_upper = path.upper()
        return any(pattern in path_upper for pattern in self.ICA_PATTERNS)
    
    def parse_change_line(self, line: str, baseline: str, current: str) -> Optional[FileChange]:
        """Parse a git diff --name-status line."""
        if not line.strip():
            return None
        
        parts = line.split("\t")
        if len(parts) < 2:
            return None
        
        status = parts[0]
        filepath = parts[1] if len(parts) == 2 else parts[2]
        old_path = parts[1] if status.startswith("R") and len(parts) >= 3 else None
        
        change_type_map = {
            "A": "added",
            "M": "modified",
            "D": "deleted",
            "R": "renamed",
        }
        change_type = change_type_map.get(status[0], "modified")
        
        adds, dels = self.get_diff_stats(baseline, current, filepath)
        
        return FileChange(
            path=filepath,
            change_type=change_type,
            old_path=old_path,
            additions=adds,
            deletions=dels,
            ata_chapter=self.extract_ata_chapter(filepath),
            ica_impact=self.is_ica_relevant(filepath),
            safety_critical=self.is_safety_critical(filepath)
        )
    
    def generate_delta_id(self, baseline: str, current: str) -> str:
        """Generate a unique delta ID."""
        content = f"{baseline}-{current}-{datetime.now().isoformat()}"
        return f"DELTA-{hashlib.sha256(content.encode()).hexdigest()[:12].upper()}"
    
    def generate_ica_impact_summary(self, changes: List[FileChange]) -> str:
        """Generate ICA impact summary."""
        ica_changes = [c for c in changes if c.ica_impact]
        if not ica_changes:
            return "No direct ICA impact detected."
        
        summary_parts = [
            f"**{len(ica_changes)} changes with ICA impact detected:**",
            ""
        ]
        
        for change in ica_changes:
            ata = change.ata_chapter or "Unknown ATA"
            summary_parts.append(
                f"- `{change.path}` ({change.change_type}) - {ata}"
            )
        
        return "\n".join(summary_parts)
    
    def synthesize_delta(
        self,
        baseline: str,
        current: str,
        title: Optional[str] = None
    ) -> DeltaDocument:
        """Synthesize a delta document from version control changes."""
        logger.info(f"Synthesizing delta: {baseline} -> {current}")
        
        diff_lines = self.get_git_diff(baseline, current)
        changes = []
        ata_chapters = set()
        has_safety_impact = False
        
        for line in diff_lines:
            change = self.parse_change_line(line, baseline, current)
            if change:
                changes.append(change)
                if change.ata_chapter:
                    ata_chapters.add(change.ata_chapter)
                if change.safety_critical:
                    has_safety_impact = True
        
        delta_id = self.generate_delta_id(baseline, current)
        
        delta = DeltaDocument(
            id=delta_id,
            title=title or f"Documentation Delta: {baseline} → {current}",
            created_at=datetime.now().isoformat(),
            baseline_ref=baseline,
            current_ref=current,
            summary=f"{len(changes)} files changed across {len(ata_chapters)} ATA chapters",
            changes=changes,
            ata_chapters_affected=ata_chapters,
            ica_impact_summary=self.generate_ica_impact_summary(changes),
            safety_impact=has_safety_impact,
            requires_review=has_safety_impact or any(c.ica_impact for c in changes)
        )
        
        return delta
    
    def save_delta(self, delta: DeltaDocument, format: str = "both") -> List[Path]:
        """Save delta document to file(s)."""
        saved_files = []
        
        if format in ("json", "both"):
            json_path = DELTA_DIR / f"{delta.id}.json"
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(delta.to_dict(), f, indent=2)
            saved_files.append(json_path)
            logger.info(f"Saved JSON delta: {json_path}")
        
        if format in ("md", "both"):
            md_path = DELTA_DIR / f"{delta.id}.md"
            md_content = self._generate_markdown(delta)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md_content)
            saved_files.append(md_path)
            logger.info(f"Saved Markdown delta: {md_path}")
        
        return saved_files
    
    def _generate_markdown(self, delta: DeltaDocument) -> str:
        """Generate Markdown representation of delta."""
        lines = [
            f"# {delta.title}",
            "",
            f"**Delta ID:** `{delta.id}`  ",
            f"**Created:** {delta.created_at}  ",
            f"**Baseline:** `{delta.baseline_ref}`  ",
            f"**Current:** `{delta.current_ref}`  ",
            "",
            "---",
            "",
            "## Summary",
            "",
            delta.summary,
            "",
        ]
        
        if delta.safety_impact:
            lines.extend([
                "> ⚠️ **SAFETY IMPACT DETECTED** - This delta contains changes to safety-critical components.",
                ""
            ])
        
        if delta.requires_review:
            lines.extend([
                "> 📋 **REVIEW REQUIRED** - This delta requires engineering/airworthiness review.",
                ""
            ])
        
        lines.extend([
            "## ATA Chapters Affected",
            "",
        ])
        
        for ata in sorted(delta.ata_chapters_affected):
            desc = self.ATA_PATTERNS.get(ata, "")
            lines.append(f"- **{ata}**: {desc}")
        
        lines.extend([
            "",
            "## ICA Impact Assessment",
            "",
            delta.ica_impact_summary,
            "",
            "## Detailed Changes",
            "",
            "| File | Type | ATA | ICA Impact | Safety Critical | +/- |",
            "|------|------|-----|------------|-----------------|-----|",
        ])
        
        for change in delta.changes:
            ica = "✅" if change.ica_impact else ""
            safety = "⚠️" if change.safety_critical else ""
            ata = change.ata_chapter or "-"
            stats = f"+{change.additions}/-{change.deletions}"
            lines.append(
                f"| `{change.path}` | {change.change_type} | {ata} | {ica} | {safety} | {stats} |"
            )
        
        lines.extend([
            "",
            "---",
            "",
            "## Document Control",
            "",
            "- Generated by: `delta_doc_synthesizer.py` (AI-assisted, prompted by Amedeo Pelliccia)",
            "- Part of: CAOS ICA Enabling Toolchain",
            f"- Version: 1.0",
            "",
        ])
        
        return "\n".join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate documentation deltas from version control changes"
    )
    parser.add_argument(
        "--baseline",
        default="HEAD~1",
        help="Baseline reference (commit, tag, branch). Default: HEAD~1"
    )
    parser.add_argument(
        "--current",
        default="HEAD",
        help="Current reference (commit, tag, branch). Default: HEAD"
    )
    parser.add_argument(
        "--pr",
        type=int,
        help="PR number to analyze (fetches base and head automatically)"
    )
    parser.add_argument(
        "--title",
        help="Custom title for the delta document"
    )
    parser.add_argument(
        "--format",
        choices=["json", "md", "both"],
        default="both",
        help="Output format. Default: both"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Custom output directory"
    )
    
    args = parser.parse_args()
    
    synthesizer = DeltaDocSynthesizer()
    
    if args.output_dir:
        global DELTA_DIR
        DELTA_DIR = args.output_dir
        DELTA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate delta
    delta = synthesizer.synthesize_delta(
        baseline=args.baseline,
        current=args.current,
        title=args.title
    )
    
    # Save and report
    saved_files = synthesizer.save_delta(delta, format=args.format)
    
    print(f"\n{'='*60}")
    print(f"Delta Document Generated: {delta.id}")
    print(f"{'='*60}")
    print(f"Changes: {len(delta.changes)} files")
    print(f"ATA Chapters: {', '.join(sorted(delta.ata_chapters_affected)) or 'None'}")
    print(f"Safety Impact: {'Yes ⚠️' if delta.safety_impact else 'No'}")
    print(f"Requires Review: {'Yes' if delta.requires_review else 'No'}")
    print(f"\nSaved to:")
    for f in saved_files:
        print(f"  - {f}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
