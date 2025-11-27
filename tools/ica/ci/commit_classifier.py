#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2025 AMPEL360 Project Contributors

"""
commit_classifier.py

Classifies commits by type and impact for ICA workflow management.
Categories: Safety, Ops, Design, MRO, ICA, Documentation, Delta-Only.

Usage:
    python -m tools.ica.ci.commit_classifier --commit HEAD
    python -m tools.ica.ci.commit_classifier --range HEAD~10..HEAD
"""

import argparse
import json
import logging
import re
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


class CommitCategory(str, Enum):
    """Commit classification categories."""
    SAFETY = "Safety"
    OPS = "Operations"
    DESIGN = "Design"
    MRO = "MRO"
    ICA = "ICA"
    DOCUMENTATION = "Documentation"
    DELTA_ONLY = "Delta-Only"
    INFRASTRUCTURE = "Infrastructure"
    TEST = "Test"
    UNKNOWN = "Unknown"


@dataclass
class CommitClassification:
    """Classification result for a single commit."""
    sha: str
    short_sha: str
    author: str
    date: str
    message: str
    primary_category: CommitCategory
    secondary_categories: List[CommitCategory] = field(default_factory=list)
    affected_ata_chapters: List[str] = field(default_factory=list)
    files_changed: int = 0
    requires_ica_review: bool = False
    requires_safety_review: bool = False
    confidence: float = 1.0


class CommitClassifier:
    """Classifies commits by type and impact."""
    
    # Category detection patterns (message and file paths)
    CATEGORY_PATTERNS = {
        CommitCategory.SAFETY: {
            "message": [
                r"\bsafety\b", r"\bhazard\b", r"\bfha\b", r"\bfmea\b", r"\bfta\b",
                r"\bcritical\b.*\bfailure\b", r"\bssa\b", r"\bpssa\b", r"\basa\b",
                r"\bcs[-\s]?25\.1309\b", r"\bsafety assessment\b"
            ],
            "paths": [
                r"SAFETY", r"HAZARD", r"FHA", r"FMEA", r"FTA", r"02_SAFETY",
                r"CRITICAL", r"SSA", r"PSSA"
            ]
        },
        CommitCategory.OPS: {
            "message": [
                r"\bops\b", r"\boperations?\b", r"\bprocedure\b", r"\boperating\b",
                r"\bflight ops\b", r"\bground ops\b", r"\bcrew\b"
            ],
            "paths": [
                r"14_OPS", r"OPERATIONS", r"PROCEDURES", r"OPS_STD",
                r"ATA_02", r"53-10"
            ]
        },
        CommitCategory.DESIGN: {
            "message": [
                r"\bdesign\b", r"\barchitecture\b", r"\bspecification\b",
                r"\brequirement\b", r"\bicd\b", r"\binterface\b", r"\bschematic\b"
            ],
            "paths": [
                r"04_DESIGN", r"03_REQUIREMENTS", r"05_INTERFACES",
                r"06_ENGINEERING", r"DESIGN", r"ICD"
            ]
        },
        CommitCategory.MRO: {
            "message": [
                r"\bmro\b", r"\bmaintenance\b", r"\brepair\b", r"\boverhaul\b",
                r"\binspection\b", r"\bservice bulletin\b", r"\bsb\b",
                r"\bcmm\b", r"\bamm\b", r"\bipc\b", r"\bsrm\b"
            ],
            "paths": [
                r"MAINTENANCE", r"MRO", r"CMM", r"AMM", r"IPC", r"SRM",
                r"SERVICE_BULLETIN", r"12_SERVICES"
            ]
        },
        CommitCategory.ICA: {
            "message": [
                r"\bica\b", r"\bairworthiness\b", r"\bcertification\b",
                r"\btype certificate\b", r"\btc\b.*\bholder\b",
                r"\bairworthiness directive\b", r"\bad\b"
            ],
            "paths": [
                r"ICA", r"AIRWORTHINESS", r"10_CERTIFICATION",
                r"04_AIRWORTHINESS", r"CERT"
            ]
        },
        CommitCategory.DOCUMENTATION: {
            "message": [
                r"\bdoc(?:s|umentation)?\b", r"\breadme\b", r"\bmanual\b",
                r"\bguide\b", r"\bindex\b", r"\btable of contents\b"
            ],
            "paths": [
                r"README", r"DOCUMENTATION", r"DOCS", r"01_OVERVIEW",
                r"\.md$", r"INDEX"
            ]
        },
        CommitCategory.INFRASTRUCTURE: {
            "message": [
                r"\bci\b", r"\bcd\b", r"\bpipeline\b", r"\bworkflow\b",
                r"\binfrastructure\b", r"\bconfig\b", r"\bsetup\b"
            ],
            "paths": [
                r"\.github", r"workflows?", r"tools/ci", r"tools/cd",
                r"Dockerfile", r"\.yml$", r"\.yaml$"
            ]
        },
        CommitCategory.TEST: {
            "message": [
                r"\btest\b", r"\bvalidat\w+\b", r"\bverif\w+\b",
                r"\bcheck\b", r"\bqa\b"
            ],
            "paths": [
                r"test", r"07_V_AND_V", r"VERIFICATION", r"VALIDATION",
                r"_test\.py$", r"_spec\."
            ]
        },
    }
    
    # ATA chapter extraction pattern
    ATA_PATTERN = re.compile(r"ATA[_-](\d{2})|(\d{2})-\d{2}-\d{2}")
    
    def __init__(self, repo_root: Path = REPO_ROOT):
        self.repo_root = repo_root
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    def get_commit_info(self, sha: str) -> Dict:
        """Get commit information."""
        try:
            # Get commit details
            result = subprocess.run(
                ["git", "log", "-1", "--format=%H|%h|%an|%aI|%s", sha],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            parts = result.stdout.strip().split("|", 4)
            
            # Get changed files
            files_result = subprocess.run(
                ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", sha],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            files = [f for f in files_result.stdout.strip().split("\n") if f]
            
            return {
                "sha": parts[0],
                "short_sha": parts[1],
                "author": parts[2],
                "date": parts[3],
                "message": parts[4] if len(parts) > 4 else "",
                "files": files
            }
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to get commit info for {sha}: {e}")
            return {}
    
    def extract_ata_chapters(self, files: List[str]) -> List[str]:
        """Extract ATA chapters from file paths."""
        chapters = set()
        for filepath in files:
            matches = self.ATA_PATTERN.findall(filepath)
            for match in matches:
                chapter = match[0] or match[1]
                if chapter:
                    chapters.add(chapter)
        return sorted(list(chapters))
    
    def match_category(
        self,
        message: str,
        files: List[str],
        category: CommitCategory
    ) -> tuple:
        """Check if commit matches a category. Returns (matches, confidence)."""
        patterns = self.CATEGORY_PATTERNS.get(category, {})
        message_patterns = patterns.get("message", [])
        path_patterns = patterns.get("paths", [])
        
        message_lower = message.lower()
        message_matches = 0
        path_matches = 0
        
        # Check message patterns
        for pattern in message_patterns:
            if re.search(pattern, message_lower):
                message_matches += 1
        
        # Check path patterns
        for filepath in files:
            filepath_upper = filepath.upper()
            for pattern in path_patterns:
                if re.search(pattern, filepath_upper, re.IGNORECASE):
                    path_matches += 1
                    break  # Count each file once
        
        total_matches = message_matches + path_matches
        if total_matches == 0:
            return False, 0.0
        
        # Calculate confidence based on matches
        confidence = min(1.0, total_matches * 0.25 + 0.5)
        return True, confidence
    
    def classify_commit(self, sha: str) -> Optional[CommitClassification]:
        """Classify a single commit."""
        info = self.get_commit_info(sha)
        if not info:
            return None
        
        message = info.get("message", "")
        files = info.get("files", [])
        
        # Score each category
        category_scores = {}
        for category in CommitCategory:
            if category in (CommitCategory.UNKNOWN, CommitCategory.DELTA_ONLY):
                continue
            matches, confidence = self.match_category(message, files, category)
            if matches:
                category_scores[category] = confidence
        
        # Determine primary and secondary categories
        if not category_scores:
            # Check if it's a delta-only (minor) change
            if all(f.endswith(('.md', '.txt', '.json', '.csv')) for f in files):
                primary = CommitCategory.DELTA_ONLY
            else:
                primary = CommitCategory.UNKNOWN
            secondary = []
            confidence = 0.5
        else:
            sorted_categories = sorted(
                category_scores.items(),
                key=lambda x: x[1],
                reverse=True
            )
            primary = sorted_categories[0][0]
            confidence = sorted_categories[0][1]
            secondary = [cat for cat, _ in sorted_categories[1:3]]
        
        # Determine review requirements
        requires_safety = primary == CommitCategory.SAFETY or CommitCategory.SAFETY in secondary
        requires_ica = primary in (CommitCategory.ICA, CommitCategory.MRO, CommitCategory.SAFETY)
        
        return CommitClassification(
            sha=info["sha"],
            short_sha=info["short_sha"],
            author=info["author"],
            date=info["date"],
            message=message,
            primary_category=primary,
            secondary_categories=secondary,
            affected_ata_chapters=self.extract_ata_chapters(files),
            files_changed=len(files),
            requires_ica_review=requires_ica,
            requires_safety_review=requires_safety,
            confidence=confidence
        )
    
    def classify_range(self, range_spec: str) -> List[CommitClassification]:
        """Classify a range of commits."""
        try:
            result = subprocess.run(
                ["git", "log", "--format=%H", range_spec],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            shas = [s for s in result.stdout.strip().split("\n") if s]
        except subprocess.CalledProcessError:
            return []
        
        classifications = []
        for sha in shas:
            classification = self.classify_commit(sha)
            if classification:
                classifications.append(classification)
        
        return classifications
    
    def generate_report(self, classifications: List[CommitClassification]) -> str:
        """Generate markdown report from classifications."""
        lines = [
            "# Commit Classification Report",
            "",
            f"**Generated:** {datetime.now().isoformat()}  ",
            f"**Commits Analyzed:** {len(classifications)}  ",
            "",
            "---",
            "",
            "## Summary by Category",
            "",
            "| Category | Count |",
            "|----------|-------|",
        ]
        
        # Count by category
        category_counts = {}
        for classification in classifications:
            cat = classification.primary_category.value
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        for cat, count in sorted(category_counts.items()):
            lines.append(f"| {cat} | {count} |")
        
        lines.extend([
            "",
            "## Commits Requiring Review",
            "",
        ])
        
        safety_commits = [c for c in classifications if c.requires_safety_review]
        ica_commits = [c for c in classifications if c.requires_ica_review and not c.requires_safety_review]
        
        if safety_commits:
            lines.extend([
                "### ⚠️ Safety Review Required",
                "",
                "| Commit | Author | Category | Message |",
                "|--------|--------|----------|---------|",
            ])
            for c in safety_commits:
                lines.append(f"| `{c.short_sha}` | {c.author} | {c.primary_category.value} | {c.message[:50]}... |")
            lines.append("")
        
        if ica_commits:
            lines.extend([
                "### 📋 ICA Review Required",
                "",
                "| Commit | Author | Category | Message |",
                "|--------|--------|----------|---------|",
            ])
            for c in ica_commits:
                lines.append(f"| `{c.short_sha}` | {c.author} | {c.primary_category.value} | {c.message[:50]}... |")
            lines.append("")
        
        lines.extend([
            "## Detailed Classifications",
            "",
            "| Commit | Category | ATA Chapters | Files | Confidence |",
            "|--------|----------|--------------|-------|------------|",
        ])
        
        for c in classifications:
            ata = ", ".join(c.affected_ata_chapters) if c.affected_ata_chapters else "-"
            lines.append(
                f"| `{c.short_sha}` | {c.primary_category.value} | {ata} | {c.files_changed} | {c.confidence:.0%} |"
            )
        
        lines.extend([
            "",
            "---",
            "",
            "## Document Control",
            "",
            "- Generated by: `commit_classifier.py` (AI-assisted, prompted by Amedeo Pelliccia)",
            "- Part of: CAOS ICA Enabling Toolchain",
            "",
        ])
        
        return "\n".join(lines)
    
    def save_report(self, classifications: List[CommitClassification]) -> tuple:
        """Save classification report."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save JSON
        json_path = REPORTS_DIR / f"commit_classification_{timestamp}.json"
        data = [asdict(c) for c in classifications]
        for d in data:
            d["primary_category"] = d["primary_category"].value if hasattr(d["primary_category"], "value") else d["primary_category"]
            d["secondary_categories"] = [
                c.value if hasattr(c, "value") else c 
                for c in d.get("secondary_categories", [])
            ]
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        
        # Save Markdown
        md_path = REPORTS_DIR / f"commit_classification_{timestamp}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(self.generate_report(classifications))
        
        return json_path, md_path


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Classify commits by type and impact"
    )
    parser.add_argument(
        "--commit",
        default="HEAD",
        help="Single commit to classify"
    )
    parser.add_argument(
        "--range",
        help="Range of commits to classify (e.g., HEAD~10..HEAD)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Custom output directory"
    )
    
    args = parser.parse_args()
    
    classifier = CommitClassifier()
    
    if args.output_dir:
        global REPORTS_DIR
        REPORTS_DIR = args.output_dir
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Classify commits
    if args.range:
        classifications = classifier.classify_range(args.range)
    else:
        classification = classifier.classify_commit(args.commit)
        classifications = [classification] if classification else []
    
    if not classifications:
        print("No commits found or classified.")
        return 1
    
    # Save reports
    json_path, md_path = classifier.save_report(classifications)
    
    # Print summary
    print(f"\n{'='*60}")
    print("Commit Classification Complete")
    print(f"{'='*60}")
    print(f"Commits Classified: {len(classifications)}")
    
    for c in classifications:
        icon = "⚠️" if c.requires_safety_review else "📋" if c.requires_ica_review else "✅"
        print(f"\n{icon} {c.short_sha}: {c.primary_category.value}")
        print(f"   Message: {c.message[:60]}...")
        if c.affected_ata_chapters:
            print(f"   ATA: {', '.join(c.affected_ata_chapters)}")
    
    print(f"\nReports saved:")
    print(f"  - {json_path}")
    print(f"  - {md_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
