#!/usr/bin/env python3
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

"""
generate-manifest.py

Generate JSON manifest from packages directory.
Validates against exports-manifest.schema.json.

Usage:
    python tooling/generate-manifest.py --dir packages/full-release --out manifests/exports-manifest-20251201-143022.json
    python tooling/generate-manifest.py --dir packages/full-release --model Q100 --ata 10 --version 1.0.0
"""

import argparse
import hashlib
import json
import logging
import os
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Script directory
SCRIPT_DIR = Path(__file__).resolve().parent
EXPORTS_DIR = SCRIPT_DIR.parent
SCHEMA_PATH = EXPORTS_DIR / "manifests" / "exports-manifest.schema.json"


def calculate_sha256(filepath: Path) -> str:
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_package_type(filename: str) -> str:
    """Infer package type from filename."""
    filename_lower = filename.lower()
    
    if "full-release" in filename_lower or "export" in filename_lower:
        return "full-release"
    elif "drawing" in filename_lower:
        return "drawings"
    elif "assembly" in filename_lower or "asm" in filename_lower:
        return "assemblies"
    elif "3d" in filename_lower or "model" in filename_lower:
        return "3d-models"
    elif "bom" in filename_lower:
        return "boms"
    elif "spec" in filename_lower:
        return "specs"
    else:
        return "full-release"  # Default


def load_package_index(package_dir: Path, filename: str) -> Optional[Dict]:
    """Load package index file if it exists."""
    base_name = filename.rsplit(".", 2)[0] if filename.endswith(".tar.gz") else filename.rsplit(".", 1)[0]
    index_file = package_dir / f"{base_name}.index.json"
    
    if index_file.exists():
        try:
            with open(index_file, "r") as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Could not load index file {index_file}: {e}")
    
    return None


def scan_packages(package_dir: Path) -> List[Dict]:
    """Scan directory for package files and generate package objects."""
    packages = []
    
    # Find all package files
    for ext in ["*.tar.gz", "*.zip", "*.tar", "*.7z"]:
        for package_file in package_dir.glob(ext):
            logger.info(f"Processing package: {package_file.name}")
            
            # Calculate hash
            sha256 = calculate_sha256(package_file)
            
            # Get file size
            size_bytes = package_file.stat().st_size
            
            # Check for signature
            sig_file = package_file.with_suffix(package_file.suffix + ".sig")
            signed = sig_file.exists()
            
            # Load index if available
            index_data = load_package_index(package_dir, package_file.name)
            
            # Build package object
            package = {
                "filename": package_file.name,
                "package_type": get_package_type(package_file.name),
                "size_bytes": size_bytes,
                "sha256": sha256,
                "signed": signed
            }
            
            # Add optional fields from index
            if index_data:
                if "file_count" in index_data:
                    package["included_files_count"] = index_data["file_count"]
                if "related_requirements" in index_data:
                    package["related_requirements"] = index_data["related_requirements"]
                if "related_assemblies" in index_data:
                    package["related_assemblies"] = index_data["related_assemblies"]
            
            # Add signature file if present
            if signed:
                package["signature_file"] = sig_file.name
            
            packages.append(package)
    
    return packages


def generate_manifest(
    package_dir: Path,
    model: str,
    ata_chapter: str,
    version: str,
    created_by: str,
    release_tag: Optional[str] = None
) -> Dict:
    """Generate complete manifest."""
    
    # Scan packages
    packages = scan_packages(package_dir)
    
    if not packages:
        logger.warning(f"No packages found in {package_dir}")
    
    # Build manifest
    manifest = {
        "manifest_id": str(uuid.uuid4()),
        "created_at": datetime.utcnow().isoformat() + "Z",
        "created_by": created_by,
        "model": model,
        "ata_chapter": ata_chapter,
        "version": version,
        "packages": packages,
        "validators": [],
        "approvals": [],
        "notes": f"Auto-generated manifest for {len(packages)} package(s)"
    }
    
    # Add optional release tag
    if release_tag:
        manifest["release_tag"] = release_tag
    
    return manifest


def validate_manifest(manifest: Dict) -> bool:
    """Validate manifest against schema."""
    try:
        import jsonschema
    except ImportError:
        logger.warning("jsonschema not installed. Skipping validation.")
        logger.info("Install with: pip install jsonschema")
        return True
    
    if not SCHEMA_PATH.exists():
        logger.warning(f"Schema file not found: {SCHEMA_PATH}")
        return True
    
    try:
        with open(SCHEMA_PATH, "r") as f:
            schema = json.load(f)
        
        jsonschema.validate(instance=manifest, schema=schema)
        logger.info("✓ Manifest validation passed")
        return True
    
    except jsonschema.ValidationError as e:
        logger.error(f"✗ Manifest validation failed: {e.message}")
        logger.error(f"  Failed at: {' -> '.join(str(p) for p in e.path)}")
        return False
    except Exception as e:
        logger.error(f"✗ Validation error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate export manifest from packages directory"
    )
    parser.add_argument(
        "--dir",
        type=Path,
        required=True,
        help="Directory containing packages"
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Output manifest file path (default: auto-generated)"
    )
    parser.add_argument(
        "--model",
        default="Q100",
        help="Aircraft model (default: Q100)"
    )
    parser.add_argument(
        "--ata",
        default="10",
        help="ATA chapter (default: 10)"
    )
    parser.add_argument(
        "--version",
        required=True,
        help="Version string (e.g., 1.0.0)"
    )
    parser.add_argument(
        "--release-tag",
        help="Optional release tag (e.g., v1.0.0-ATA10)"
    )
    parser.add_argument(
        "--created-by",
        default=f"{os.getenv('USER', 'automation')}@ampel360.aero",
        help="Creator email (default: $USER@ampel360.aero)"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate manifest against schema"
    )
    
    args = parser.parse_args()
    
    # Validate package directory
    if not args.dir.exists():
        logger.error(f"Directory not found: {args.dir}")
        sys.exit(1)
    
    # Generate output filename if not provided
    if not args.out:
        timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        manifests_dir = EXPORTS_DIR / "manifests"
        manifests_dir.mkdir(exist_ok=True)
        args.out = manifests_dir / f"exports-manifest-{timestamp}.json"
    
    logger.info(f"Scanning packages in: {args.dir}")
    logger.info(f"Output manifest: {args.out}")
    
    # Generate manifest
    manifest = generate_manifest(
        package_dir=args.dir,
        model=args.model,
        ata_chapter=args.ata,
        version=args.version,
        created_by=args.created_by,
        release_tag=args.release_tag
    )
    
    # Validate if requested
    if args.validate:
        if not validate_manifest(manifest):
            logger.error("Manifest validation failed")
            sys.exit(1)
    
    # Write manifest
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(manifest, f, indent=2)
    
    logger.info(f"✓ Manifest generated: {args.out}")
    logger.info(f"  Packages: {len(manifest['packages'])}")
    logger.info(f"  Manifest ID: {manifest['manifest_id']}")
    
    # Print summary
    print("\n" + "=" * 60)
    print(f"Manifest Generated: {args.out}")
    print("=" * 60)
    print(f"Model:        {manifest['model']}")
    print(f"ATA Chapter:  {manifest['ata_chapter']}")
    print(f"Version:      {manifest['version']}")
    print(f"Packages:     {len(manifest['packages'])}")
    print(f"Manifest ID:  {manifest['manifest_id']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
