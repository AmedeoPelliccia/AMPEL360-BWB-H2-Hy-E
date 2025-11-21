# 85-00-03-H2-001 — H₂ Refuelling Interface Requirements

## 1. Requirement Statement

The AMPEL360 BWB H₂ Hy-E aircraft **SHALL** be equipped with hydrogen refuelling interfaces that comply with [SAE J2601](https://www.sae.org/standards/content/j2601/) fuelling protocols (adapted for aviation applications) and support high-pressure refuelling at pressures up to **700 bar** (70 MPa).

## 2. Rationale

Standardized refuelling interfaces ensure compatibility with emerging hydrogen refuelling infrastructure while enabling:
- Safe, leak-free hydrogen transfer at high pressures
- Automated safety interlocks to prevent unsafe refuelling conditions
- Compatibility with ground-based H₂ supply equipment
- Rapid refuelling to support target turnaround times (15 minutes)

## 3. Category

- **Requirement Type**: Interface — Physical and Safety
- **Domain**: Hydrogen Refuelling Infrastructure
- **ATA**: 85-00-03_Requirements / H2

## 4. Source(s)

- **[SAE J2601](https://www.sae.org/standards/content/j2601/)** — Fueling Protocols for Light Duty Gaseous Hydrogen Surface Vehicles
- **[ISO 19880-8](https://www.iso.org/standard/71940.html)** — Gaseous hydrogen — Fuelling stations — Part 8
- **Aircraft H₂ Fuel System Design** — ATA 28 fuel system specifications
- **Safety Analyses** — Hydrogen hazard assessments (ATA 85-00-02_Safety)

## 5. Acceptance Criteria

- [ ] Refuelling connector design complies with SAE J2601 (or aviation-adapted equivalent)
- [ ] Maximum operating pressure: 700 bar (70 MPa)
- [ ] Leak rate < 1×10⁻⁶ mbar·L/s at maximum pressure
- [ ] Automated breakaway coupling in case of vehicle movement
- [ ] Safety interlocks prevent refuelling when aircraft systems are energized
- [ ] Temperature monitoring during refuelling (prevent over-temperature)
- [ ] Compatible with ground-based H₂ dispensers at target airports

## 6. Verification Method

- **Method**: Test + Inspection
- **Evidence**: Pressure test reports, leak test results, interface compatibility validation, safety interlock tests

## 7. Traceability

- **Upstream**: ATA 28 (Fuel Systems), H₂ fuel system design requirements
- **Horizontal**: ICD-85-H2-001 (H₂ Refuelling Interface Control Document)
- **Downstream**: TC-85-03-H2-001-A (pressure test), TC-85-03-H2-001-B (leak test), TC-85-03-H2-001-C (safety interlock test)

## 8. Status

- **Lifecycle State**: `FOR_REVIEW`
- **Owner**: Propulsion & Hydrogen Systems Team
- **Last Updated**: 2025-11-21

---

## Document Control

- **Document ID**: RQ-85-00-03-H2-001
- **Version**: 1.0
- **Status**: FOR_REVIEW
- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21
