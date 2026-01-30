# 53-60-70-02 Burst Disc Specification

## Document Information

- **Document ID**: 53-60-70-02
- **Title**: Burst Disc Specification
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Pressure Systems
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the burst disc (rupture disc) specifications for storage system ultimate pressure protection.

## Scope

This specification covers:
- Burst disc types and applications
- Performance requirements
- Installation requirements
- Replacement criteria

## Burst Disc Applications

### Application Summary

| System | Burst Pressure | Material | Size | Reference |
|--------|----------------|----------|------|-----------|
| Battery coolant | 6.0 bar | Stainless 316L | DN15 | REQ-BD-001 |
| CO₂ cartridge | 4.0 bar | Stainless 316L | DN15 | REQ-BD-002 |
| Thermal accumulator | 5.0 bar | Stainless 316L | DN12 | REQ-BD-003 |

## General Requirements

### Performance

| Parameter | Requirement | Reference |
|-----------|-------------|-----------|
| Burst accuracy | ±5% | REQ-BD-010 |
| Response time | ≤ 10 ms | REQ-BD-011 |
| Non-fragmenting | Required | REQ-BD-012 |
| Operating ratio | ≥ 0.7 | REQ-BD-013 |

### Environmental

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Temperature range | -40 to +120°C | REQ-BD-020 |
| Fatigue resistance | ≥ 10⁶ cycles at 70% | REQ-BD-021 |
| Corrosion resistance | Per medium | REQ-BD-022 |

## Disc Specifications by Application

### Battery Coolant (BD-BAT-001)

| Parameter | Value | Unit |
|-----------|-------|------|
| Burst pressure | 6.0 ± 0.3 | bar |
| Temperature range | -40 to +100 | °C |
| Size | DN15 | — |
| Material | Stainless 316L | — |
| Type | Forward-acting, scored | — |

### CO₂ System (BD-CO2-001)

| Parameter | Value | Unit |
|-----------|-------|------|
| Burst pressure | 4.0 ± 0.2 | bar |
| Temperature range | -40 to +100 | °C |
| Size | DN15 | — |
| Material | Stainless 316L | — |
| Type | Forward-acting, scored | — |

## Burst Indicator

| Feature | Description | Reference |
|---------|-------------|-----------|
| Visual indicator | Pop-up telltale | REQ-BD-030 |
| Electrical indication | Discrete 28 VDC | REQ-BD-031 |
| BITE integration | Status to CMC | REQ-BD-032 |

## Replacement Criteria

| Condition | Action |
|-----------|--------|
| Burst | Mandatory replacement |
| Calendar | Replace at 10 years |
| Damage | Replace if any defect |
| Temperature exceedance | Replace if >120°C |

## Testing Requirements

| Test | Criteria | Frequency |
|------|----------|-----------|
| Burst pressure | ±5% | Sample (1 per lot) |
| Visual inspection | No defects | 100% |
| Pressure cycling | No degradation at 70% | Qualification |

## References

### Internal Documents
- [53-60-70-01 Relief Valve Specification](53-60-70-01_Relief_Valve_Spec.md)
- [53-60-70-03 Vent Routing](53-60-70-03_Vent_Routing.md)

### External Standards
- ASME Code Section VIII - Pressure Vessels

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
