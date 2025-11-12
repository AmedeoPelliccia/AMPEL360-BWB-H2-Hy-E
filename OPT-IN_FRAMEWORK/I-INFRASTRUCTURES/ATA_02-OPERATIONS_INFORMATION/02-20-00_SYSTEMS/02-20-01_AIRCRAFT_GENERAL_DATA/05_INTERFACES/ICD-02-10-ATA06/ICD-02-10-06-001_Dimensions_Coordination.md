# ICD-02-10-06-001: Dimensions Coordination Interface

**From:** ATA 02-10 Aircraft General Data  
**To:** ATA 06 Dimensions and Areas

**ICD ID:** ICD-02-10-06-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## Purpose

This Interface Control Document defines the coordination between Aircraft General Data and Dimensions & Areas to ensure consistent geometric specifications across all documentation and systems.

## Data Exchange

### BWB Geometry Specifications

**Provided by ATA 02-10:**
- Overall aircraft length: 54.5 m
- Maximum wingspan: 65.0 m
- Maximum height: 15.2 m
- Cabin length (internal): 42.0 m
- Maximum cabin width: 12.5 m
- Wing area: 750 m²
- Mean Aerodynamic Chord (MAC): 8.2 m

**Data Format:** CAD reference geometry + dimensional tables  
**Update Frequency:** Static (updated with design changes only)  
**Criticality:** Medium

### Airport Compatibility Data

**Critical Dimensions:**
- Wingspan for gate compatibility: 65.0 m (Code E)
- Height clearance for hangars: 15.2 m
- Door sill heights: L1 Forward 4.2 m, L3 Aft 3.8 m
- Cargo door height: 3.5 m

## Interface Specifications

**Data Exchange Method:**
- Primary: CAD model (STEP format)
- Secondary: Dimensional drawings (PDF)
- Tertiary: Tabular data (CSV)

**Coordinate System:** Aircraft datum at nose, X-axis aft, Y-axis right, Z-axis up

**Tolerance Standards:**
- Critical dimensions: ±5 mm
- General dimensions: ±10 mm
- Reference dimensions: ±25 mm

## BWB-Specific Considerations

The Blended Wing Body design requires special attention to:
- Continuously varying cross-sections
- Non-traditional fuselage reference lines
- Integration of wing and body coordinate systems
- Passenger cabin floor curvature

## Dependencies

- Structural design (ATA 53, 57)
- Door locations (ATA 52)
- Systems installation envelopes (various ATAs)

## Responsibilities

**ATA 02-10 (Provider):**
- Maintain master geometry definition
- Issue controlled CAD models
- Coordinate geometry changes

**ATA 06 (Consumer):**
- Generate dimensional drawings
- Maintain areas and volume calculations
- Support ground operations planning

## Change Control

Dimensional changes require:
1. Engineering Change Order (ECO)
2. Impact assessment on airport operations
3. Update to Type Certificate Data Sheet
4. Notification to operators

## References

- ISO 1151: Flight Dynamics - Concepts, Quantities and Symbols
- SAE AS755: Aircraft Reference Axes and Sections
- ICAO Annex 14: Aerodrome Design Standards

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Review Cycle: Per design change
