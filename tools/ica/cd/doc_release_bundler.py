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
doc_release_bundler.py

Generates official revision bundles with ICA stamps for release.
Creates versioned documentation packages for airworthiness compliance.

Usage:
    python -m tools.ica.cd.doc_release_bundler --version 1.0.0
    python -m tools.ica.cd.doc_release_bundler --tag v1.0.0 --ata 53
"""

import argparse
import hashlib
import json
import logging
import shutil
import subprocess
import sys
import zipfile
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
BUNDLES_DIR = CD_DIR / "bundles"
PUBLICATIONS_DIR = CD_DIR / "publications"


@dataclass
class DocumentInfo:
    """Information about a document in the bundle."""
    path: str
    title: str
    ata_chapter: Optional[str]
    version: str
    last_modified: str
    checksum: str
    size_bytes: int


@dataclass
class ReleaseBundle:
    """Release bundle metadata."""
    bundle_id: str
    version: str
    release_date: str
    ica_stamp: str
    ata_chapters: List[str]
    document_count: int
    documents: List[DocumentInfo] = field(default_factory=list)
    bundle_checksum: str = ""
    manifest_path: str = ""
    archive_path: str = ""


class DocReleaseBundler:
    """Generates official revision bundles with ICA stamps."""
    
    # ATA chapters and their names
    ATA_CHAPTERS = {
        "02": "Operations Information",
        "04": "Airworthiness Limitations",
        "05": "Time Limits/Maintenance Checks",
        "21": "Air Conditioning",
        "24": "Electrical Power",
        "25": "Equipment/Furnishings",
        "27": "Flight Controls",
        "28": "Fuel",
        "29": "Hydraulic Power",
        "32": "Landing Gear",
        "34": "Navigation",
        "53": "Fuselage",
        "71": "Powerplant",
        "72": "Engine",
        "85": "Infrastructure Interface Standards",
        "95": "Digital Product Passport",
    }
    
    def __init__(self, repo_root: Path = REPO_ROOT):
        self.repo_root = repo_root
        BUNDLES_DIR.mkdir(parents=True, exist_ok=True)
        PUBLICATIONS_DIR.mkdir(parents=True, exist_ok=True)
    
    def generate_bundle_id(self, version: str) -> str:
        """Generate a unique bundle ID."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        content = f"AMPEL360-ICA-{version}-{timestamp}"
        hash_suffix = hashlib.sha256(content.encode()).hexdigest()[:8].upper()
        return f"ICA-BUNDLE-{version.replace('.', '-')}-{hash_suffix}"
    
    def generate_ica_stamp(self, version: str) -> str:
        """Generate ICA compliance stamp."""
        return f"AMPEL360-ICA-REV-{version}-{datetime.now().strftime('%Y%m%d')}"
    
    def calculate_checksum(self, filepath: Path) -> str:
        """Calculate SHA-256 checksum of a file."""
        sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def extract_ata_chapter(self, filepath: str) -> Optional[str]:
        """Extract ATA chapter from file path."""
        import re
        match = re.search(r"ATA[_-](\d{2})", filepath, re.IGNORECASE)
        if match:
            return match.group(1)
        match = re.search(r"(\d{2})-\d{2}-\d{2}", filepath)
        if match:
            return match.group(1)
        return None
    
    def extract_title(self, filepath: Path) -> str:
        """Extract document title from markdown file."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("# "):
                        return line[2:].strip()
            return filepath.stem.replace("_", " ")
        except Exception:
            return filepath.stem.replace("_", " ")
    
    def get_git_version(self) -> str:
        """Get current git version/tag."""
        try:
            result = subprocess.run(
                ["git", "describe", "--tags", "--always"],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return "0.0.0"
    
    def collect_documents(
        self,
        ata_filter: Optional[List[str]] = None,
        include_assets: bool = True
    ) -> List[DocumentInfo]:
        """Collect all documents for the bundle."""
        documents = []
        opt_in_root = self.repo_root / "OPT-IN_FRAMEWORK"
        
        if not opt_in_root.exists():
            logger.warning(f"OPT-IN_FRAMEWORK not found at {opt_in_root}")
            return documents
        
        # Collect markdown files
        for md_file in opt_in_root.rglob("*.md"):
            rel_path = str(md_file.relative_to(self.repo_root))
            ata_chapter = self.extract_ata_chapter(rel_path)
            
            # Apply ATA filter if specified
            if ata_filter and ata_chapter not in ata_filter:
                continue
            
            stat = md_file.stat()
            
            doc = DocumentInfo(
                path=rel_path,
                title=self.extract_title(md_file),
                ata_chapter=ata_chapter,
                version=self.get_git_version(),
                last_modified=datetime.fromtimestamp(stat.st_mtime).isoformat(),
                checksum=self.calculate_checksum(md_file),
                size_bytes=stat.st_size
            )
            documents.append(doc)
        
        # Optionally include CSV and JSON assets
        if include_assets:
            for ext in ["*.csv", "*.json"]:
                for asset_file in opt_in_root.rglob(ext):
                    rel_path = str(asset_file.relative_to(self.repo_root))
                    ata_chapter = self.extract_ata_chapter(rel_path)
                    
                    if ata_filter and ata_chapter not in ata_filter:
                        continue
                    
                    stat = asset_file.stat()
                    
                    doc = DocumentInfo(
                        path=rel_path,
                        title=asset_file.stem.replace("_", " "),
                        ata_chapter=ata_chapter,
                        version=self.get_git_version(),
                        last_modified=datetime.fromtimestamp(stat.st_mtime).isoformat(),
                        checksum=self.calculate_checksum(asset_file),
                        size_bytes=stat.st_size
                    )
                    documents.append(doc)
        
        return documents
    
    def create_manifest(self, bundle: ReleaseBundle) -> str:
        """Create bundle manifest."""
        manifest = {
            "bundle_info": {
                "id": bundle.bundle_id,
                "version": bundle.version,
                "release_date": bundle.release_date,
                "ica_stamp": bundle.ica_stamp,
                "aircraft_type": "AMPEL360-BWB-H₂-Hy-E",
                "document_type": "Instructions for Continued Airworthiness (ICA)",
            },
            "ata_chapters": {
                chapter: self.ATA_CHAPTERS.get(chapter, "Unknown")
                for chapter in bundle.ata_chapters
            },
            "statistics": {
                "document_count": bundle.document_count,
                "total_size_bytes": sum(d.size_bytes for d in bundle.documents),
            },
            "documents": [asdict(d) for d in bundle.documents],
            "compliance": {
                "generated_by": "CAOS ICA Enabling Toolchain",
                "generator_version": "1.0.0",
                "caos_integration": True,
                "ai_assisted": True,
                "author": "AI (prompted by Amedeo Pelliccia)",
            },
            "checksums": {
                "algorithm": "SHA-256",
                "bundle_checksum": bundle.bundle_checksum,
            }
        }
        
        return json.dumps(manifest, indent=2)
    
    def create_readme(self, bundle: ReleaseBundle) -> str:
        """Create bundle README."""
        ata_list = "\n".join([
            f"- **ATA {ch}**: {self.ATA_CHAPTERS.get(ch, 'Unknown')}"
            for ch in sorted(bundle.ata_chapters)
        ])
        
        readme = f"""# AMPEL360 ICA Documentation Bundle

**Bundle ID:** `{bundle.bundle_id}`  
**Version:** {bundle.version}  
**Release Date:** {bundle.release_date}  
**ICA Stamp:** `{bundle.ica_stamp}`

---

## Contents

This bundle contains Instructions for Continued Airworthiness (ICA) documentation
for the AMPEL360-BWB-H₂-Hy-E aircraft.

**Documents:** {bundle.document_count}  
**ATA Chapters Included:**

{ata_list}

---

## Verification

Bundle Checksum (SHA-256): `{bundle.bundle_checksum}`

To verify bundle integrity:
```bash
sha256sum -c CHECKSUMS.txt
```

---

## Usage

This documentation bundle is intended for:
- Type Certificate Holders (TCH)
- Design Approval Holders (DAH)
- Maintenance, Repair, and Overhaul (MRO) organizations
- Operators and flight crews
- Regulatory authorities (EASA, FAA, etc.)

---

## Compliance

- **Aircraft Type:** AMPEL360-BWB-H₂-Hy-E
- **Regulatory Basis:** CS-25, EASA Part 21
- **ICA Requirements:** Per CS-25.1529 and Appendix H

---

## Document Control

- Generated by: CAOS ICA Enabling Toolchain
- AI-assisted (prompted by Amedeo Pelliccia)
- Status: Official Release
- Last Updated: {bundle.release_date}

---

## Contact

For questions regarding this documentation bundle:
- Repository: `AMPEL360-BWB-H2-Hy-E`
- CAOS Integration: Enabled

"""
        return readme
    
    def create_checksums_file(self, bundle: ReleaseBundle) -> str:
        """Create checksums verification file."""
        lines = ["# SHA-256 Checksums", f"# Bundle: {bundle.bundle_id}", ""]
        for doc in bundle.documents:
            lines.append(f"{doc.checksum}  {doc.path}")
        return "\n".join(lines)
    
    def create_bundle(
        self,
        version: str,
        ata_filter: Optional[List[str]] = None,
        include_assets: bool = True
    ) -> ReleaseBundle:
        """Create a complete documentation bundle."""
        logger.info(f"Creating ICA bundle version {version}")
        
        # Collect documents
        documents = self.collect_documents(ata_filter, include_assets)
        
        # Get unique ATA chapters
        ata_chapters = sorted(set(
            d.ata_chapter for d in documents if d.ata_chapter
        ))
        
        # Create bundle metadata
        bundle = ReleaseBundle(
            bundle_id=self.generate_bundle_id(version),
            version=version,
            release_date=datetime.now().isoformat(),
            ica_stamp=self.generate_ica_stamp(version),
            ata_chapters=ata_chapters,
            document_count=len(documents),
            documents=documents
        )
        
        return bundle
    
    def save_bundle(self, bundle: ReleaseBundle, create_archive: bool = True) -> Path:
        """Save bundle to disk."""
        bundle_dir = BUNDLES_DIR / bundle.bundle_id
        bundle_dir.mkdir(parents=True, exist_ok=True)
        
        # Save manifest
        manifest_path = bundle_dir / "MANIFEST.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            f.write(self.create_manifest(bundle))
        bundle.manifest_path = str(manifest_path)
        
        # Save README
        readme_path = bundle_dir / "README.md"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(self.create_readme(bundle))
        
        # Save checksums
        checksums_path = bundle_dir / "CHECKSUMS.txt"
        with open(checksums_path, "w", encoding="utf-8") as f:
            f.write(self.create_checksums_file(bundle))
        
        # Copy documents to bundle
        docs_dir = bundle_dir / "documents"
        for doc in bundle.documents:
            src = self.repo_root / doc.path
            if src.exists():
                dst = docs_dir / doc.path
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        
        # Create archive if requested
        if create_archive:
            archive_path = BUNDLES_DIR / f"{bundle.bundle_id}.zip"
            with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for file_path in bundle_dir.rglob("*"):
                    if file_path.is_file():
                        arcname = file_path.relative_to(bundle_dir)
                        zf.write(file_path, arcname)
            
            bundle.archive_path = str(archive_path)
            bundle.bundle_checksum = self.calculate_checksum(archive_path)
            
            # Update manifest with final checksum
            with open(manifest_path, "w", encoding="utf-8") as f:
                f.write(self.create_manifest(bundle))
            
            logger.info(f"Created archive: {archive_path}")
        
        logger.info(f"Bundle saved to: {bundle_dir}")
        return bundle_dir


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate official ICA revision bundles"
    )
    parser.add_argument(
        "--version",
        help="Bundle version (e.g., 1.0.0)"
    )
    parser.add_argument(
        "--tag",
        help="Use git tag as version"
    )
    parser.add_argument(
        "--ata",
        nargs="+",
        help="Filter by ATA chapters (e.g., 53 85)"
    )
    parser.add_argument(
        "--no-assets",
        action="store_true",
        help="Exclude CSV/JSON assets from bundle"
    )
    parser.add_argument(
        "--no-archive",
        action="store_true",
        help="Don't create ZIP archive"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Custom output directory"
    )
    
    args = parser.parse_args()
    
    bundler = DocReleaseBundler()
    
    if args.output_dir:
        global BUNDLES_DIR
        BUNDLES_DIR = args.output_dir
        BUNDLES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Determine version
    version = args.version or args.tag or bundler.get_git_version()
    
    # Create bundle
    bundle = bundler.create_bundle(
        version=version,
        ata_filter=args.ata,
        include_assets=not args.no_assets
    )
    
    # Save bundle
    bundle_dir = bundler.save_bundle(
        bundle,
        create_archive=not args.no_archive
    )
    
    # Print summary
    print(f"\n{'='*60}")
    print("ICA Documentation Bundle Created")
    print(f"{'='*60}")
    print(f"Bundle ID: {bundle.bundle_id}")
    print(f"Version: {bundle.version}")
    print(f"ICA Stamp: {bundle.ica_stamp}")
    print(f"Documents: {bundle.document_count}")
    print(f"ATA Chapters: {', '.join(bundle.ata_chapters)}")
    print(f"\nBundle Location: {bundle_dir}")
    if bundle.archive_path:
        print(f"Archive: {bundle.archive_path}")
        print(f"Checksum: {bundle.bundle_checksum}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
