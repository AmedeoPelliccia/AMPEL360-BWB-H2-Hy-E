#!/usr/bin/env python3
"""
Mass Properties Baseline Watchdog

Validates that frozen mass properties in engineering documents
match baseline_mass_properties.json. Any deviation triggers CI failure
and generates a report for ECR processing.
"""
import json
import pathlib
import re
import sys
from typing import Dict, Any, List, Tuple

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]

BASELINE_PATH = (
    REPO_ROOT
    / "OPT-IN_FRAMEWORK"
    / "I-INFRASTRUCTURES"
    / "ATA_02-OPERATIONS_INFORMATION"
    / "02-10-00_AIRCRAFT_GENERAL_DATA"
    / "01_OVERVIEW"
    / "baseline_mass_properties.json"
)

REPORT_PATH = REPO_ROOT / "cd" / "mass" / "mass_properties_deviations_report.md"

TOLERANCE_ABS = 1e-6


class CheckError(Exception):
    pass


def load_baseline() -> Dict[str, Any]:
    if not BASELINE_PATH.exists():
        raise CheckError(f"Baseline file not found: {BASELINE_PATH}")
    with BASELINE_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def read_text(path: pathlib.Path) -> str:
    if not path.exists():
        raise CheckError(f"Expected file not found: {path}")
    return path.read_text(encoding="utf-8")


def parse_float(text: str, pattern: str, key: str) -> float:
    m = re.search(pattern, text)
    if not m:
        raise CheckError(f"Could not find value for '{key}' using pattern: {pattern}")
    try:
        return float(m.group("val"))
    except ValueError as e:
        raise CheckError(f"Could not parse float for '{key}' from '{m.group('val')}'") from e


def collect_current_values() -> Dict[str, float]:
    values: Dict[str, float] = {}

    base_path = (
        REPO_ROOT
        / "OPT-IN_FRAMEWORK"
        / "I-INFRASTRUCTURES"
        / "ATA_02-OPERATIONS_INFORMATION"
        / "02-10-00_AIRCRAFT_GENERAL_DATA"
        / "06_ENGINEERING"
        / "ANALYSIS_REPORTS"
    )

    mass_path = base_path / "MASS" / "Mass_Breakdown_Analysis.md"
    mass_text = read_text(mass_path)

    values["mtow_kg"] = parse_float(
        mass_text,
        r"MTOW\s*:\s*\*\*\s*(?P<val>[0-9.]+)\s*kg",
        "mtow_kg",
    )
    values["oew_kg"] = parse_float(
        mass_text,
        r"OEW\s*:\s*\*\*\s*(?P<val>[0-9.]+)\s*kg",
        "oew_kg",
    )
    values["mzfw_kg"] = parse_float(
        mass_text,
        r"MZFW\s*:\s*\*\*\s*(?P<val>[0-9.]+)\s*kg",
        "mzfw_kg",
    )
    values["mlw_kg"] = parse_float(
        mass_text,
        r"MLW\s*:\s*\*\*\s*(?P<val>[0-9.]+)\s*kg",
        "mlw_kg",
    )
    values["max_fuel_mass_kg"] = parse_float(
        mass_text,
        r"Maximum fuel capacity\s*:\s*\*\*\s*(?P<val>[0-9.]+)\s*kg",
        "max_fuel_mass_kg",
    )
    values["max_payload_kg"] = parse_float(
        mass_text,
        r"Maximum payload capacity\s*:\s*\*\*\s*(?P<val>[0-9.]+)\s*kg",
        "max_payload_kg",
    )

    cg_path = base_path / "MASS" / "CG_Envelope_Analysis.md"
    cg_text = read_text(cg_path)

    values["cg_forward_limit_percent_mac"] = parse_float(
        cg_text,
        r"Forward limit\s*:\s*\*\*\s*(?P<val>[0-9.]+)\s*%\s*MAC",
        "cg_forward_limit_percent_mac",
    )
    values["cg_aft_limit_percent_mac"] = parse_float(
        cg_text,
        r"Aft limit\s*:\s*\*\*\s*(?P<val>[0-9.]+)\s*%\s*MAC",
        "cg_aft_limit_percent_mac",
    )

    return values


def compare_values(
    baseline: Dict[str, Any],
    current: Dict[str, float],
) -> List[Tuple[str, float, float]]:
    deviations: List[Tuple[str, float, float]] = []
    # Skip metadata keys
    metadata_keys = {"version", "last_updated"}
    for key, base_val in baseline.items():
        if key in metadata_keys:
            continue
        if key not in current:
            raise CheckError(f"Current values missing key '{key}' defined in baseline")
        cur_val = current[key]
        if abs(cur_val - float(base_val)) > TOLERANCE_ABS:
            deviations.append((key, float(base_val), cur_val))
    return deviations


def write_report(deviations: List[Tuple[str, float, float]]) -> None:
    lines = [
        "# Mass Properties Baseline Deviation Detected",
        "",
        "One or more *frozen* mass properties have changed with respect to "
        "`baseline_mass_properties.json`. This requires an **Engineering Change Request (ECR)**.",
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
    lines.append("- Raise / update the ECR document for 02-10-00 mass properties.")
    lines.append("- Assess impacts on: performance, CG envelope, loads, certification.")
    lines.append(
        "- Once the ECR is approved, update `baseline_mass_properties.json` to the new frozen values."
    )

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        baseline = load_baseline()
        current = collect_current_values()
        deviations = compare_values(baseline, current)
    except CheckError as e:
        print(f"[mass-check] ERROR: {e}", file=sys.stderr)
        write_report([(f"INTERNAL_ERROR: {type(e).__name__}", 0.0, 1.0)])
        return 1

    if deviations:
        print("[mass-check] Deviations detected:")
        for key, base, cur in deviations:
            print(f"  - {key}: baseline={base}, current={cur}")
        write_report(deviations)
        return 1

    print("[mass-check] OK – no mass property deviations vs baseline.")
    if REPORT_PATH.exists():
        REPORT_PATH.unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
