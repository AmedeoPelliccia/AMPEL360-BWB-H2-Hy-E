---
title: ATA 02-10-00 AIRCRAFT GENERAL DATA / 01_OVERVIEW
identifier: 02-20-01-001A
version: 0.1
author: Amedeo Pelliccia
status: Draft
classification: Technical
scope: Operations Information architecture and integration with related subsystems
created_at: 2025-11-13
next_review: 2026-05-12
compliance:
  - ATA iSpec 2200
  - S1000D
  - AMPEL360 OPT-IN Framework
---

<!-- GENCCC_STATUS: pending -->
<!-- GENCCC_SCOPE: system_description, architecture, integration -->


> 🔗 **Linked Verification Matrix:** [../../07_V_AND_V/02-20-01-001A_Traceability_Matrix.csv](../../07_V_AND_V/02-20-01-001A_Traceability_Matrix.csv)

# ATA 02-10-00 AIRCRAFT GENERAL DATA / 01_OVERVIEW

## Overview

This folder contains comprehensive aircraft general data and operational information for the **AMPEL360 BWB H₂ Hy-E Q100 INTEGRA** aircraft. It serves as the primary reference for all operational personnel, maintenance crews, and flight planning systems.

## Folder Structure

```
01_OVERVIEW/
├── README.md
├── Aircraft_General_Description.md
├── Principal_Dimensions.md
├── Weight_Limits.md
├── Capacities_Summary.md
├── Performance_Summary.md
├── Systems_Overview.md
│
├── ASSETS/
│   ├── Three_View_Drawing.svg
│   ├── General_Arrangement_Drawing.pdf
│   ├── Aircraft_Silhouette.svg
│   └── Comparison_Chart_Conventional.svg
│
└── TABLES/
    ├── Aircraft_Data_Summary.csv
    ├── Weight_Balance_Limits.csv
    ├── Performance_Envelope.csv
    └── Systems_List.csv
```

## Key Documents

### Aircraft_General_Description.md
Complete aircraft type description, key features, configuration, certification basis, and operational highlights for the revolutionary Blended Wing Body hydrogen fuel cell aircraft.

### Principal_Dimensions.md
Comprehensive dimensional data including overall dimensions, BWB-specific geometry, ground clearances, and airport compatibility information.

### Weight_Limits.md
Structural weight limits, fuel capacity data, payload specifications, and center of gravity limits with BWB-specific considerations.

### Capacities_Summary.md
Passenger capacity, cargo volume, fuel capacity, and other capacity-related operational data.

### Performance_Summary.md
Key performance data including range, speed, altitude capabilities, and efficiency metrics.

### Systems_Overview.md
High-level overview of all major aircraft systems including propulsion, fuel, environmental control, CAOS AI, and flight controls.

## Data Tables (TABLES/ Folder)

### Aircraft_Data_Summary.csv
Master table containing all key aircraft parameters, values, units, and notes for quick reference.

### Weight_Balance_Limits.csv
Detailed weight and balance limitations for all operational conditions.

### Performance_Envelope.csv
Performance envelope data across various flight regimes and conditions.

### Systems_List.csv
Complete list of aircraft systems with ATA chapter references and status.

## Visual Assets (ASSETS/ Folder)

### Three_View_Drawing.svg
Standard three-view drawing showing front, side, and top views of the BWB configuration.

### General_Arrangement_Drawing.pdf
Detailed general arrangement drawing with cabin layout, systems locations, and dimensions.

### Aircraft_Silhouette.svg
Simple aircraft silhouette for documentation and training materials.

### Comparison_Chart_Conventional.svg
Visual comparison chart showing AMPEL360 BWB advantages versus conventional aircraft.

## Aircraft Specifications Summary

| Parameter | Value | Unit |
|-----------|-------|------|
| **Manufacturer** | AMPEL360 | — |
| **Model** | BWB H₂ Hy-E Q100 INTEGRA | — |
| **Type Certificate** | Pending (Target 2028) | — |
| **Configuration** | Blended Wing Body | — |
| **Crew** | 2 pilots | — |
| **Passenger Capacity** | 220 pax | Single class |
| **MTOW** | 185,000 kg | — |
| **Maximum Fuel** | 8,000 kg | H₂ cryogenic |
| **Design Range** | 6,500 km | 3,500 NM |
| **Cruise Speed** | 470 kt | Mach 0.82 |
| **Service Ceiling** | 13,700 m | FL450 |
| **Wingspan** | 80 m | Code F |
| **Propulsion** | Hydrogen Fuel Cells | 4 × 2.5 MW |

## Unique Features

- **Zero Direct Emissions**: PEM fuel cells with hydrogen fuel (water vapor only byproduct)
- **Carbon Negative**: Active atmospheric CO₂ capture during flight
- **30% More Efficient**: BWB aerodynamics vs conventional tube-and-wing
- **CAOS AI System**: Computer Aided Operations & Services for predictive maintenance

## Cross-References

- **Related Folders**: 02_SAFETY, 03_REQUIREMENTS, 04_DESIGN, 05_INTERFACES
- **Related ATA Chapters**: 
  - ATA 05 - Time Limits & Maintenance Checks
  - ATA 06 - Dimensions and Areas
  - ATA 07 - Lifting and Shoring
  - ATA 08 - Leveling and Weighing
  - ATA 28 - Fuel (H₂ System)
  - ATA 71 - Power Plant (Fuel Cells)
  - ATA 95 - Neural Networks & Digital Passport

## Document Control

- **Version**: 1.0.0
- **Status**: Complete
- **Last Updated**: 2025-11-05
- **Classification**: Operations Critical
- **Approval**: Pending Type Certificate
- **Next Review**: 2026-Q1

---

**© 2025 AMPEL360 Project | All Rights Reserved**
