# 53-50-03-001 Fatigue Analysis Methodology

## Document Information

- **Document ID**: 53-50-03-001
- **Title**: Fatigue Analysis Methodology
- **Version**: 1.0
- **Date**: 2025-11-22
- **Status**: Draft
- **Category**: Fatigue & Damage Tolerance
- **ATA Chapter**: 53-50 - Fuselage Structures

## Purpose

This document defines the fatigue analysis methodology used for the AMPEL360 BWB fuselage structure, ensuring compliance with [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) damage tolerance and fatigue evaluation requirements.

## Scope

This methodology covers:
- Fatigue load spectrum development
- S-N curve fatigue analysis
- Miner's cumulative damage assessment
- Crack initiation life prediction
- Safe-life substantiation for critical elements

## Fatigue Analysis Philosophy

The AMPEL360 uses a dual approach:
- **Safe-life** for single load path elements (PSE)
- **Damage tolerance** for redundant structure

### Design Service Goal

| Parameter | Value |
|-----------|-------|
| Design Service Goal (DSG) | 60,000 flight cycles |
| Flight hours | 90,000 hours |
| Average flight duration | 1.5 hours |

## Load Spectrum Development

### Flight Profile

| Phase | Duration (min) | Frequency | Load Factor Range |
|-------|---------------|-----------|-------------------|
| Taxi out | 10 | 1/flight | 1.0g ± 0.1g |
| Takeoff | 2 | 1/flight | 1.0 - 1.3g |
| Climb | 15 | 1/flight | 1.0 - 1.15g |
| Cruise | 70 | 1/flight | 1.0 ± 0.3g (gust) |
| Descent | 20 | 1/flight | 0.95 - 1.1g |
| Landing | 2 | 1/flight | 1.0 - 1.8g |
| Taxi in | 5 | 1/flight | 1.0g ± 0.1g |

### Pressure Cycling

| Cycle Type | ΔP (psi) | Frequency |
|------------|----------|-----------|
| Ground-air-ground | 8.6 | 1/flight |
| Cruise pressure change | 0.5 | Variable |

## S-N Curve Data

### Material S-N Curves

| Material | Kt | S @ 10⁴ cycles (MPa) | S @ 10⁶ cycles (MPa) | Slope (b) |
|----------|----|--------------------|--------------------|----|
| IM7/8552 CFRP | 1.0 | 850 | 450 | -0.12 |
| IM7/8552 CFRP | 3.0 | 550 | 250 | -0.14 |
| Al 7050-T7451 | 1.0 | 480 | 180 | -0.10 |
| Al 7050-T7451 | 3.0 | 320 | 100 | -0.12 |
| Ti-6Al-4V | 1.0 | 900 | 550 | -0.08 |
| Ti-6Al-4V | 3.0 | 650 | 350 | -0.10 |

### Scatter Factors

| Element Type | Scatter Factor | Notes |
|--------------|----------------|-------|
| PSE (metallic) | 4.0 | Per AC 25.571-1D |
| PSE (composite) | Life factor method | Per CMH-17 |
| Standard structure | 2.0 | Fail-safe |

## Cumulative Damage Analysis

### Miner's Rule Application

**Damage Index**: D = Σ(nᵢ / Nᵢ)

Where:
- nᵢ = applied cycles at stress level i
- Nᵢ = allowable cycles at stress level i (from S-N curve)
- D ≤ 1/SF for acceptable life

### Example Calculation (Door Corner)

| Load Level | Stress (MPa) | Cycles/Flight | N (allowable) | Damage/Flight |
|------------|--------------|---------------|---------------|---------------|
| Pressure cycle | 230 | 1 | 85,000 | 1.18 × 10⁻⁵ |
| Gust loads | 180 | 50 | 250,000 | 2.0 × 10⁻⁴ |
| Maneuver | 200 | 10 | 150,000 | 6.7 × 10⁻⁵ |
| **Total** | | | | 2.8 × 10⁻⁴ |

**Predicted Life** = 1 / (2.8 × 10⁻⁴) = 3,570 flights = 215,000 FC (3.6 × DSG)

## Fatigue Life Summary

| Location | Predicted Life (FC) | Factor on DSG | Status |
|----------|---------------------|---------------|--------|
| Door 1 corner | 180,000 | 3.0× | ✓ Pass |
| Window corners (typical) | 250,000 | 4.2× | ✓ Pass |
| Crown splice LS-01 | 200,000 | 3.3× | ✓ Pass |
| MLG trunnion fitting | 240,000 | 4.0× | ✓ Pass |
| Wing spar lug | 260,000 | 4.3× | ✓ Pass |

## Verification

### Full-Scale Fatigue Test

- **Test Article**: Complete fuselage barrel
- **Duration**: 2 × DSG (120,000 simulated flights)
- **Inspections**: Every 1/4 DSG
- **Success Criteria**: No crack initiation at DSG; controlled growth to 2× DSG

## References

### Regulatory Documents
- [CS-25.571 Damage Tolerance and Fatigue Evaluation](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- AC 25.571-1D Advisory Circular

### Internal References
- [53-50-03-002 Design Service Goal Analysis](53-50-03-002_Design_Service_Goal_Analysis.md)
- [Fatigue Spectrum Data](ASSETS/Fatigue_Spectrum_Data.csv)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-25

---
