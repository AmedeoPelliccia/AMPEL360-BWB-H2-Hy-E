#!/usr/bin/env python3
"""
Geometry Baseline Watchdog

This script validates that frozen geometry dimensions in engineering documents
match the baseline_dimensions.json file. Any deviation triggers a CI failure
and generates a report for ECR (Engineering Change Request) processing.
"""
import json
import pathlib
import re
import sys
from typing import Dict, Any, List, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

# Update path to match actual repository structure
BASELINE_PATH = (
    REPO_ROOT / "OPT-IN_FRAMEWORK" / "I-INFRASTRUCTURES" / "ATA_02-OPERATIONS_INFORMATION"
    / "02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY" / "01_OVERVIEW" / "baseline_dimensions.json"
)
REPORT_PATH = REPO_ROOT / "geometry_deviations_report.md"

TOLERANCE_ABS = 1e-6  # strict: any numerical change is detected


class CheckError(Exception):
    pass


def load_baseline() -> Dict[str, Any]:
    if not BASELINE_PATH.exists():
        raise CheckError(f"Baseline file not found: {BASELINE_PATH}")
    with BASELINE_PATH.open() as f:
        return json.load(f)


def read_text(path: pathlib.Path) -> str:
    if not path.exists():
        raise CheckError(f"Expected file not found: {path}")
    return path.read_text(encoding="utf-8")


def parse_float_from_regex(text: str, pattern: str, key: str) -> float:
    m = re.search(pattern, text)
    if not m:
        raise CheckError(f"Could not find value for '{key}' using pattern: {pattern}")
    try:
        return float(m.group("val"))
    except ValueError as e:
        raise CheckError(f"Could not parse float for '{key}' from '{m.group('val')}'") from e


def collect_current_values() -> Dict[str, float]:
    """
    Parse key geometry values from existing markdown reports.
    Extend this function as needed to watch more dimensions.
    """
    values: Dict[str, float] = {}

    base_path = (
        REPO_ROOT / "OPT-IN_FRAMEWORK" / "I-INFRASTRUCTURES" / "ATA_02-OPERATIONS_INFORMATION"
        / "02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY" / "06_ENGINEERING" / "ANALYSIS_REPORTS"
    )

    # 1) Aerodynamic geometry from Lift_Distribution_Analysis.md
    lift_dist_path = base_path / "AERODYNAMIC" / "Lift_Distribution_Analysis.md"
    text = read_text(lift_dist_path)

    values["wingspan_m"] = parse_float_from_regex(
        text,
        r"Wingspan\s*\(b\):\s*\*\*\s*(?P<val>[0-9.]+)\s*m",
        "wingspan_m",
    )
    values["wing_area_m2"] = parse_float_from_regex(
        text,
        r"Wing area\s*\(S\):\s*\*\*\s*(?P<val>[0-9.]+)\s*m²",
        "wing_area_m2",
    )
    values["aspect_ratio"] = parse_float_from_regex(
        text,
        r"Aspect ratio\s*\(AR\):\s*\*\*\s*(?P<val>[0-9.]+)",
        "aspect_ratio",
    )
    values["cruise_sweep_deg"] = parse_float_from_regex(
        text,
        r"Sweep\s*\(Λ\):\s*\*\*\s*(?P<val>[0-9.]+)°",
        "cruise_sweep_deg",
    )

    # 2) Pressure vessel geometry from Pressure_Vessel_Analysis.md
    pv_path = base_path / "STRUCTURAL" / "Pressure_Vessel_Analysis.md"
    pv_text = read_text(pv_path)

    values["pressure_vessel_equiv_radius_m"] = parse_float_from_regex(
        pv_text,
        r"Equivalent radius:\s*\*\*\s*(?P<val>[0-9.]+)\s*m",
        "pressure_vessel_equiv_radius_m",
    )
    values["overall_length_m"] = parse_float_from_regex(
        pv_text,
        r"Length:\s*\*\*\s*(?P<val>[0-9.]+)\s*m",
        "overall_length_m",
    )
    values["center_body_depth_m"] = parse_float_from_regex(
        pv_text,
        r"Depth:\s*\*\*\s*(?P<val>[0-9.]+)\s*m",
        "center_body_depth_m",
    )

    # 3) Gear geometry from Ground_Clearance_Calculations.md
    clr_path = base_path / "CLEARANCE" / "Ground_Clearance_Calculations.md"
    clr_text = read_text(clr_path)

    values["mlg_height_m"] = parse_float_from_regex(
        clr_text,
        r"Main landing gear\s*\(MLG\)\s*height:\s*\*\*\s*(?P<val>[0-9.]+)\s*m",
        "mlg_height_m",
    )
    values["nlg_height_m"] = parse_float_from_regex(
        clr_text,
        r"Nose landing gear\s*\(NLG\)\s*height:\s*\*\*\s*(?P<val>[0-9.]+)\s*m",
        "nlg_height_m",
    )
    values["wheelbase_m"] = parse_float_from_regex(
        clr_text,
        r"Wheelbase:\s*\*\*\s*(?P<val>[0-9.]+)\s*m",
        "wheelbase_m",
    )
    values["mlg_track_m"] = parse_float_from_regex(
        clr_text,
        r"Main gear track:\s*\*\*\s*(?P<val>[0-9.]+)\s*m",
        "mlg_track_m",
    )

    return values


def compare_values(
    baseline: Dict[str, Any],
    current: Dict[str, float],
) -> List[Tuple[str, float, float]]:
    deviations: List[Tuple[str, float, float]] = []
    for key, base_val in baseline.items():
        if key not in current:
            raise CheckError(f"Current values missing key '{key}' defined in baseline")
        cur_val = current[key]
        if abs(cur_val - float(base_val)) > TOLERANCE_ABS:
            deviations.append((key, float(base_val), cur_val))
    return deviations


def write_report(deviations: List[Tuple[str, float, float]]) -> None:
    lines = [
        "# Geometry Baseline Deviation Detected",
        "",
        "One or more *frozen* geometry parameters have changed with respect to "
        "`baseline_dimensions.json`. This requires an **Engineering Change Request (ECR)**.",
        "",
        "## Deviations",
        "",
        "| Parameter | Baseline | Current | Δ |",
        "|-----------|----------|---------|---|",
    ]
    for key, base, cur in deviations:
        delta = cur - base
        lines.append(f"| `{key}` | {base:.6g} | {cur:.6g} | {delta:.6g} |")

    lines.append("")
    lines.append("## Next Actions")
    lines.append("")
    lines.append("- Raise / update the ECR document for 02-11-00 geometry.")
    lines.append("- Assess impacts on: FEM global model, ground clearance, CG envelope, performance, certification.")
    lines.append("- Once the ECR is approved, update `baseline_dimensions.json` to the new frozen values.")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        baseline = load_baseline()
        current = collect_current_values()
        deviations = compare_values(baseline, current)
    except CheckError as e:
        print(f"[geometry-check] ERROR: {e}", file=sys.stderr)
        # Treat missing data / parsing issues as hard failure
        write_report([(f"INTERNAL_ERROR: {type(e).__name__}", 0.0, 1.0)])
        return 1

    if deviations:
        print("[geometry-check] Deviations detected:")
        for key, base, cur in deviations:
            print(f"  - {key}: baseline={base}, current={cur}")
        write_report(deviations)
        return 1

    print("[geometry-check] OK – no geometry deviations vs baseline.")
    # If a previous report exists, it's now obsolete; optional cleanup
    if REPORT_PATH.exists():
        REPORT_PATH.unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
