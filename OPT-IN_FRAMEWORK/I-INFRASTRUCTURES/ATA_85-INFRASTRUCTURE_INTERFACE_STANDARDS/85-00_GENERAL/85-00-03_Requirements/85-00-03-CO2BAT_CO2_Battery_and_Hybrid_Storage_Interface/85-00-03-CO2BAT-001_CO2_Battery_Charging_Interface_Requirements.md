# 85-00-03-CO2BAT-001 — CO₂ Battery Charging Interface Requirements

## 1. Requirement Statement

The AMPEL360 aircraft **SHALL** be equipped with a ground charging interface for the CO₂ battery system supporting:
- **DC Charging**: 800V DC at up to 200 kW power
- **Thermal Management**: Integrated cooling during charging (liquid cooling interface)
- **Charge Time**: Full charge in ≤ 30 minutes

## 2. Rationale

The CO₂ battery system requires high-power charging infrastructure to support rapid turnaround times and thermal management to prevent battery degradation.

## 3. Category

- **Requirement Type**: Interface — Electrical and Thermal
- **Domain**: CO₂ Battery and Hybrid Storage
- **ATA**: 85-00-03_Requirements / CO2BAT

## 4. Source(s)

- Battery system design (ATA 24, ATA 47)
- Turnaround time targets

## 5. Acceptance Criteria

- [ ] DC charging interface: 800V ±50V, up to 200 kW
- [ ] Thermal management: cooling flow rate 20 L/min, coolant temp 15-25°C
- [ ] Charge time ≤ 30 minutes (0-80% SOC)
- [ ] Safety interlocks prevent charging during flight operations

## 6. Verification Method

- **Method**: Test
- **Evidence**: Charging interface test, thermal management validation, charge time measurement

## 7. Status

- **Lifecycle State**: `FOR_REVIEW`
- **Owner**: Energy Systems Team
- **Last Updated**: 2025-11-21

---

## Document Control

- **Document ID**: RQ-85-00-03-CO2BAT-001
- **Version**: 1.0
- **Status**: FOR_REVIEW
- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21
