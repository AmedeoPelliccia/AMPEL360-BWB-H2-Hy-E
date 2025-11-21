# 85-00-03-H2-002 — H₂ Supply Capacity and Pressure Requirements

## 1. Requirement Statement

The ground-based hydrogen refuelling infrastructure **SHALL** provide:
- **Supply Pressure**: 700 bar ±50 bar (adjustable based on aircraft tank conditions)
- **Flow Rate**: Sufficient to refuel aircraft H₂ tanks (target capacity: 1,500 kg) in ≤ 15 minutes
- **Fuel Quality**: Hydrogen purity ≥ 99.97% per [ISO 14687](https://www.iso.org/standard/69539.html) Type I Grade D

## 2. Rationale

High-pressure, high-purity hydrogen supply is essential for:
- Efficient fuel cell operation (impurities reduce performance and lifetime)
- Rapid refuelling to support 45-minute turnaround time target
- Maximizing aircraft range (high-pressure storage increases volumetric energy density)

## 3. Category

- **Requirement Type**: Performance — Supply Specifications
- **Domain**: Hydrogen Refuelling Infrastructure
- **ATA**: 85-00-03_Requirements / H2

## 4. Source(s)

- **[ISO 14687](https://www.iso.org/standard/69539.html)** — Hydrogen fuel quality specification
- **[ISO 19880-8](https://www.iso.org/standard/71940.html)** — Fuelling station fuel quality control
- **Aircraft Performance Requirements** — Range, fuel capacity, turnaround time targets

## 5. Acceptance Criteria

- [ ] Supply pressure: 700 bar ±50 bar
- [ ] Refuelling time ≤ 15 minutes for full tanks (1,500 kg H₂)
- [ ] H₂ purity ≥ 99.97% (ISO 14687 Type I Grade D)
- [ ] Maximum contaminant levels per ISO 14687 (H₂O, O₂, CO, CO₂, hydrocarbons)
- [ ] Temperature control during refuelling (-40°C to +85°C)

## 6. Verification Method

- **Method**: Test + Analysis
- **Evidence**: Fuel quality test reports, refuelling time measurements, pressure and flow rate validation

## 7. Traceability

- **Upstream**: ATA 28 (Fuel Systems), fuel cell specifications
- **Horizontal**: ICD-85-H2-001 (H₂ supply specifications)
- **Downstream**: TC-85-03-H2-002-A (fuel quality test), TC-85-03-H2-002-B (refuelling time test)

## 8. Status

- **Lifecycle State**: `FOR_REVIEW`
- **Owner**: Propulsion & Hydrogen Systems Team
- **Last Updated**: 2025-11-21

---

## Document Control

- **Document ID**: RQ-85-00-03-H2-002
- **Version**: 1.0
- **Status**: FOR_REVIEW
- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21
