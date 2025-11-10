# ATA 02-11-00 Aircraft Dimensions & Geometry - Overview

**Document ID:** AMPEL360-02-11-00-OVW-README  
**Version:** 1.0.0  
**Status:** Released

## Purpose

This folder contains overview documentation and the **frozen geometry baseline** for the AMPEL360 BWB H₂ Hy-E Q100 INTEGRA aircraft configuration.

## Contents

### baseline_dimensions.json

**Single source of truth for frozen geometry dimensions.**

This file contains the type-design baseline dimensions that are monitored by the Geometry Baseline Watchdog CI system. Any deviation from these values requires an Engineering Change Request (ECR).

**Monitored parameters:**
- Aerodynamic geometry (wingspan, wing area, aspect ratio, sweep)
- Structural geometry (overall length, center body depth, pressure vessel radius)
- Landing gear geometry (MLG/NLG heights, wheelbase, gear track)

**⚠️ IMPORTANT**: Changes to this file must be accompanied by:
1. An approved ECR document
2. Updates to all affected engineering analysis documents
3. Impact assessment on FEM, clearance, CG envelope, and performance analyses

The CI watchdog automatically verifies that values in engineering documents match this baseline. Deviations trigger automatic ECR issue creation.

For more information, see: `tools/README.md`

## Status

✅ **Baseline Established** - Geometry baseline file created and CI watchdog active.

| Document | Purpose | Status |
|----------|---------|--------|
| Dimensions_Overview.md | General dimensional data | Released |
| BWB_Geometry_Description.md | BWB-specific geometry | Released |
| Reference_Systems.md | Coordinate systems | Released |
| Measurement_Standards.md | Measurement procedures | Released |

## BWB Configuration Highlights

- **Wingspan:** 52.0 m (ICAO Code E)
- **Length:** 38.2 m (BWB chord)
- **Center Body:** 38.0 m width × 28.5 m length
- **Aspect Ratio:** 3.2 (typical for BWB)
- **Wing Sweep:** 37° leading edge

## Coordinate System

**Body Axis System:**
- X: Forward positive (nose to tail)
- Y: Right wing positive (left to right)
- Z: Down positive (top to bottom)

**Reference Point:** Nose apex (Station 0)

## Directory Structure

```
01_OVERVIEW/
├── README.md
├── Dimensions_Overview.md
├── BWB_Geometry_Description.md
├── Reference_Systems.md
├── Measurement_Standards.md
│
├── PRINCIPAL_DIMENSIONS/
│   ├── Overall_Dimensions.md
│   ├── Wingspan_Specifications.md
│   ├── Length_Specifications.md
│   ├── Height_Specifications.md
│   └── Principal_Dimensions_Table.csv
│
├── BWB_GEOMETRY/
│   ├── Planform_Geometry.md
│   ├── Cross_Section_Geometry.md
│   ├── Wing_Geometry.md
│   ├── Center_Body_Geometry.md
│   └── Geometry_Parameters.csv
│
├── REFERENCE_SYSTEMS/
│   ├── Body_Axis_System.md
│   ├── Station_System.md
│   ├── Waterline_System.md
│   ├── Buttline_System.md
│   └── Reference_Points.csv
│
├── DRAWINGS/
│   ├── Three_View_Drawing.svg
│   ├── Planform_Drawing.svg
│   ├── Cross_Sections_Drawing.svg
│   └── Geometry_Layout.svg
│
└── TABLES/
    ├── Dimension_Summary.csv
    ├── Station_Locations.csv
    ├── Critical_Clearances.csv
    └── Airport_Compatibility.csv
```

---

**Document Control:**
- Version: 1.0.0
- Status: Complete ✅
- Last Updated: 2025-11-06
- Classification: Operations Critical
