#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 AMPEL360 Project Contributors
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Geometry Data Packaging Tool

This script packages geometry data and analysis reports for deployment or
external delivery. It creates a structured archive containing baseline
dimensions, analysis reports, and documentation.

Output goes to cd/publications/ directory by default.

Usage:
    python tools/package_geometry_data.py [--output-dir OUT] [--suffix SFX] [--dry-run] [--verbose]
"""
from __future__ import annotations

import argparse
import tarfile
import time
import pathlib
from typing import List

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

GEOM_ROOT = (
    REPO_ROOT
    / "OPT-IN_FRAMEWORK"
    / "I-INFRASTRUCTURES"
    / "ATA_02-OPERATIONS_INFORMATION"
    / "02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY"
)

DEFAULT_OUTPUT_DIR = REPO_ROOT / "cd" / "publications"


def collect_geometry_files(verbose: bool = False) -> List[pathlib.Path]:
    """Collect all relevant geometry files for packaging.

    Returns a sorted, unique list of existing file paths.
    """
    files: List[pathlib.Path] = []

    # Add baseline dimensions
    baseline = GEOM_ROOT / "01_OVERVIEW" / "baseline_dimensions.json"
    if baseline.exists():
        files.append(baseline)
        if verbose:
            print(f"[collect] added baseline: {baseline}")

    # Add analysis reports
    analysis_reports_dir = GEOM_ROOT / "06_ENGINEERING" / "ANALYSIS_REPORTS"
    if analysis_reports_dir.exists():
        for report in sorted(analysis_reports_dir.rglob("*.md")):
            files.append(report)
            if verbose:
                print(f"[collect] added analysis report: {report}")

    # Add requirements
    requirements_dir = GEOM_ROOT / "03_REQUIREMENTS"
    if requirements_dir.exists():
        for req in sorted(requirements_dir.rglob("*.md")):
            files.append(req)
            if verbose:
                print(f"[collect] added requirement: {req}")

    # Add overview documentation (top-level .md files)
    overview_dir = GEOM_ROOT / "01_OVERVIEW"
    if overview_dir.exists():
        for doc in sorted(overview_dir.glob("*.md")):
            files.append(doc)
            if verbose:
                print(f"[collect] added overview doc: {doc}")

    # Deduplicate and ensure existence
    unique_files = sorted({p.resolve() for p in files})
    existing_files = [p for p in unique_files if p.exists()]

    if verbose:
        print(f"[collect] total files collected: {len(existing_files)}")

    return existing_files


def make_archive(output_dir: pathlib.Path, suffix: str | None = None, verbose: bool = False) -> pathlib.Path:
    """Create a tar.gz archive with the geometry data.

    Returns the path to the created archive.
    Raises RuntimeError if no files found to archive.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    name = f"geometry_baseline_{ts}"
    if suffix:
        safe_suffix = "".join(c for c in suffix if c.isalnum() or c in ("-", "_")).strip()
        if safe_suffix:
            name += f"_{safe_suffix}"
    archive_path = output_dir / f"{name}.tar.gz"

    files = collect_geometry_files(verbose=verbose)
    if not files:
        raise RuntimeError(f"No geometry files found under {GEOM_ROOT}; nothing to archive.")

    if verbose:
        print(f"[archive] creating archive {archive_path} with {len(files)} files")

    # create tar.gz archive; store paths relative to repo root
    with tarfile.open(archive_path, "w:gz") as tf:
        for p in files:
            try:
                arcname = p.relative_to(REPO_ROOT)
            except Exception:
                arcname = p.name
            if verbose:
                print(f"[archive] adding {p} as {arcname}")
            tf.add(p, arcname=str(arcname))

    if verbose:
        print(f"[archive] created {archive_path} ({archive_path.stat().st_size} bytes)")

    return archive_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Package geometry baseline data.")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=pathlib.Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for the archive",
    )
    parser.add_argument(
        "--suffix",
        help="Optional suffix for the archive name",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not create archive; list files that would be packaged",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose diagnostic output",
    )
    args = parser.parse_args()

    try:
        files = collect_geometry_files(verbose=args.verbose)
        if args.dry_run:
            print("[dry-run] Files that would be archived:")
            for p in files:
                print(f"  - {p.relative_to(REPO_ROOT)}")
            return 0

        archive = make_archive(args.output_dir, args.suffix, verbose=args.verbose)
        print(f"[geometry-package] Created {archive}")
        return 0
    except Exception as e:
        print(f"[geometry-package] ERROR: {e}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
