# 01_OVERVIEW - AIRCRAFT_DIMENSIONS_GEOMETRY

**Component Code:** 02-11-00  
**Component Name:** AIRCRAFT_DIMENSIONS_GEOMETRY  
**Folder:** 01_OVERVIEW

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

## Related Documents

- Parent Component: 02-11-00_AIRCRAFT_DIMENSIONS_GEOMETRY
- ATA Chapter: 02 - Operations Information
- AMPEL360 Platform: BWB H2 Hy-E Q100 INTEGRA

---

**Document Control:**
- Version: 1.0
- Status: Structure Created
- Last Updated: 2025-11-04
