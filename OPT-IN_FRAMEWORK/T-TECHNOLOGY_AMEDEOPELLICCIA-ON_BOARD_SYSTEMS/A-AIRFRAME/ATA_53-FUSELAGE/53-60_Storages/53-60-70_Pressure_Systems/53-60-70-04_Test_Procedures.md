# 53-60-70-04 Pressure Test Procedures

## Document Information

- **Document ID**: 53-60-70-04
- **Title**: Pressure Test Procedures
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Pressure Systems
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the pressure test procedures for storage system verification and acceptance.

## Scope

This specification covers:
- Proof pressure testing
- Leak testing
- Burst testing (qualification)
- In-service testing

## Test Categories

### Test Level Summary

| Test Type | Purpose | Frequency | Reference |
|-----------|---------|-----------|-----------|
| Proof pressure | Acceptance | 100% production | REQ-TST-001 |
| Leak test | Acceptance | 100% production | REQ-TST-002 |
| Burst test | Qualification | Sample | REQ-TST-003 |
| In-service leak | Maintenance | Per AMM | REQ-TST-004 |

## Proof Pressure Test

### Test Parameters by System

| System | Operating | Proof | Duration | Criteria |
|--------|-----------|-------|----------|----------|
| Battery coolant | 3.0 bar | 6.0 bar | 5 min | No leak, no deformation |
| CO₂ cartridge | 2.0 bar | 4.0 bar | 5 min | No leak, no deformation |
| Water tank | 0.5 bar | 1.5 bar | 5 min | No leak, no deformation |
| Thermal system | 3.0 bar | 6.0 bar | 5 min | No leak, no deformation |

### Procedure

| Step | Action | Acceptance |
|------|--------|------------|
| 1 | Install test fixtures | Secure connection |
| 2 | Fill with test medium | No air pockets |
| 3 | Pressurize to 50% proof | No leaks |
| 4 | Hold 1 minute | Stable pressure |
| 5 | Pressurize to 100% proof | No leaks |
| 6 | Hold 5 minutes | Pressure drop ≤ 1% |
| 7 | Depressurize | Controlled rate |
| 8 | Visual inspection | No deformation |

## Leak Test

### Test Parameters

| Method | Pressure | Detection Limit | Application |
|--------|----------|-----------------|-------------|
| Bubble test | Operating | Visible bubble | General |
| Helium mass spec | Operating | 10⁻⁶ mbar·L/s | Critical joints |
| Pressure decay | Operating | 1% / hour | System level |

### Bubble Test Procedure

| Step | Action |
|------|--------|
| 1 | Pressurize to operating pressure |
| 2 | Apply leak detection fluid |
| 3 | Observe for 5 minutes |
| 4 | Record any bubble formation |

## Burst Test (Qualification)

### Test Requirements

| System | Design Burst | Test Burst | Quantity |
|--------|--------------|------------|----------|
| Battery coolant | 12.0 bar | 12.0 bar | 3 samples |
| CO₂ cartridge | 8.0 bar | 8.0 bar | 3 samples |
| Water tank | 3.0 bar | 3.0 bar | 2 samples |
| Thermal system | 12.0 bar | 12.0 bar | 3 samples |

### Criteria

| Requirement | Acceptance |
|-------------|------------|
| Burst pressure | ≥ design burst |
| Failure mode | Ductile (no fragmentation) |
| Location | Not at joints or welds |

## In-Service Testing

### Periodic Leak Check

| System | Interval | Method |
|--------|----------|--------|
| Battery coolant | 500 FH | Pressure decay |
| CO₂ | 500 FH | Pressure decay |
| Thermal | 500 FH | Pressure decay |
| Water | 1000 FH | Visual |

## Test Equipment

| Equipment | Specification | Calibration |
|-----------|---------------|-------------|
| Pressure gauge | ±1% FS | Annual |
| Pressure source | 0-15 bar | — |
| Leak detector | 10⁻⁶ mbar·L/s | Annual |
| Test fixtures | System-specific | Before use |

## References

### Internal Documents
- [53-60-00-04 Safety Requirements](../53-60-00_General/53-60-00-04_Safety_Requirements.md)

### External Standards
- [CS-25.1435](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Hydraulic Systems

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---
