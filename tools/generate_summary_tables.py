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
Summary Table Generator

Parses selected analysis outputs and generates consolidated markdown
summary tables for documentation.
"""
import argparse
import csv
import pathlib
from typing import Iterable

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT
    / "OPT-IN_FRAMEWORK"
    / "I-INFRASTRUCTURES"
    / "ATA_02-OPERATIONS_INFORMATION"
    / "02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY"
    / "01_OVERVIEW"
    / "TABLES"
    / "Generated_Summaries"
)


def csv_to_markdown_table(csv_path: pathlib.Path) -> str:
    """Convert a CSV file to a markdown table."""
    rows = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    if not rows:
        return ""

    header = rows[0]
    data = rows[1:]

    lines = []
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join("---" for _ in header) + " |")
    for r in data:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def generate_for_files(csv_files: Iterable[pathlib.Path], output_dir: pathlib.Path) -> None:
    """Generate markdown summary tables from CSV files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    for p in csv_files:
        if not p.exists():
            print(f"[summary] WARNING: {p} does not exist, skipping")
            continue
        md = csv_to_markdown_table(p)
        if not md:
            continue
        rel_name = p.stem + ".md"
        out_path = output_dir / rel_name
        out_path.write_text(md + "\n", encoding="utf-8")
        print(f"[summary] Generated {out_path}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate markdown summary tables from CSV files."
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        type=pathlib.Path,
        help="CSV files to process (defaults to key results CSVs if omitted)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=pathlib.Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for generated tables",
    )
    args = parser.parse_args()

    if args.inputs:
        csv_files = args.inputs
    else:
        # default: key results CSVs
        csv_files = [
            REPO_ROOT
            / "OPT-IN_FRAMEWORK"
            / "I-INFRASTRUCTURES"
            / "ATA_02-OPERATIONS_INFORMATION"
            / "02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY"
            / "07_V_AND_V"
            / "DIMENSION_VERIFICATION"
            / "Dimension_Verification_Results.csv",
            # Add more CSVs here as needed
        ]

    generate_for_files(csv_files, args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
