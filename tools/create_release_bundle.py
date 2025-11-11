#!/usr/bin/env python3
"""
Release Bundle Creator

Creates deployment-ready release bundles for AMPEL360 documentation and data.
Supports versioned releases with automatic file collection and manifest generation.

Output goes to cd/publications/ directory.
"""
import argparse
import json
import pathlib
import tarfile
import time

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "cd" / "publications"

MASS_BASELINE = (
    REPO_ROOT
    / "OPT-IN_FRAMEWORK"
    / "I-INFRASTRUCTURES"
    / "ATA_02-OPERATIONS_INFORMATION"
    / "02-10-00_AIRCRAFT_GENERAL_DATA"
    / "01_OVERVIEW"
    / "baseline_mass_properties.json"
)


def build_manifest() -> dict:
    """Create manifest for the release bundle."""
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    manifest = {
        "generated_at": ts,
        "geometry_package": None,
        "mass_baseline_present": MASS_BASELINE.exists(),
    }
    return manifest


def create_release_bundle(output_dir: pathlib.Path) -> pathlib.Path:
    """Create the release bundle as a tar.gz file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    bundle = output_dir / f"ampel360_release_{ts}.tar.gz"

    manifest = build_manifest()
    manifest_path = output_dir / f"release_manifest_{ts}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    with tarfile.open(bundle, "w:gz") as tf:
        if MASS_BASELINE.exists():
            tf.add(MASS_BASELINE, arcname=str(MASS_BASELINE.relative_to(REPO_ROOT)))
        tf.add(manifest_path, arcname=str(manifest_path.relative_to(REPO_ROOT)))

    return bundle


def main() -> int:
    parser = argparse.ArgumentParser(description="Create AMPEL360 release bundle.")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=pathlib.Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for the bundle",
    )
    args = parser.parse_args()

    bundle = create_release_bundle(args.output_dir)
    print(f"[release-bundle] Created {bundle}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
