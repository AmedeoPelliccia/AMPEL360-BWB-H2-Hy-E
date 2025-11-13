#!/usr/bin/env python3
# Copyright (c) 2025 AMPEL360 Project Contributors
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

Output goes to cd/publications/ directory.
"""
import argparse
import pathlib
import tarfile
import time

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

GEOM_ROOT = (
    REPO_ROOT
    / "OPT-IN_FRAMEWORK"
    / "I-INFRASTRUCTURES"
    / "ATA_02-OPERATIONS_INFORMATION"
    / "02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY"
)

DEFAULT_OUTPUT_DIR = REPO_ROOT / "cd" / "publications"


def collect_geometry_files() -> list:
    """Collect all relevant geometry files for packaging."""
    files = []
    
    # Add baseline dimensions
    baseline = GEOM_ROOT / "01_OVERVIEW" / "baseline_dimensions.json"
    if baseline.exists():
        files.append(baseline)
    
    # Add analysis reports
    analysis_reports_dir = GEOM_ROOT / "06_ENGINEERING" / "ANALYSIS_REPORTS"
    if analysis_reports_dir.exists():
        for report in analysis_reports_dir.rglob("*.md"):
            files.append(report)
    
    # Add requirements
    requirements_dir = GEOM_ROOT / "03_REQUIREMENTS"
    if requirements_dir.exists():
        for req in requirements_dir.rglob("*.md"):
            files.append(req)
    
    # Add overview documentation
    overview_dir = GEOM_ROOT / "01_OVERVIEW"
    if overview_dir.exists():
        for doc in overview_dir.glob("*.md"):
            files.append(doc)
    
    return [p for p in files if p.exists()]


def make_archive(output_dir: pathlib.Path, suffix: str = None) -> pathlib.Path:
    """Create a tar.gz archive with the geometry data."""
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    name = f"geometry_baseline_{ts}"
    if suffix:
        name += f"_{suffix}"
    archive_path = output_dir / f"{name}.tar.gz"

    files = collect_geometry_files()
    with tarfile.open(archive_path, "w:gz") as tf:
        for p in files:
            arcname = p.relative_to(REPO_ROOT)
            tf.add(p, arcname=str(arcname))
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
    args = parser.parse_args()

    archive = make_archive(args.output_dir, args.suffix)
    print(f"[geometry-package] Created {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
