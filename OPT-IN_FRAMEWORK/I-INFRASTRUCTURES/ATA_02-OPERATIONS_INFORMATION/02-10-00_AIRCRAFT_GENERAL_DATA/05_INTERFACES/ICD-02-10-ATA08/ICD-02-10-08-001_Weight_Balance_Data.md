# ICD-02-10-08-001: Weight and Balance Data Interface

**From:** ATA 02-10 Aircraft General Data  
**To:** ATA 08 Leveling and Weighing

**ICD ID:** ICD-02-10-08-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## Purpose

This Interface Control Document defines the critical weight and balance data exchange required for accurate aircraft weight determinations, center of gravity calculations, and loading procedures.

## Data Exchange

### Aircraft Weight Parameters

**Provided by ATA 02-10:**
- **MTOW (Maximum Takeoff Weight):** 185,000 kg
- **MLW (Maximum Landing Weight):** 155,000 kg
- **MZFW (Maximum Zero Fuel Weight):** 145,000 kg
- **Operating Empty Weight:** 105,000 kg
- **Maximum Fuel Weight:** 40,000 kg (H₂)
- **Maximum Payload:** 40,000 kg (220 passengers + cargo)

**Data Format:** Weight statement with detailed breakdown  
**Update Frequency:** Static (updated with major modifications)  
**Criticality:** Critical

### Center of Gravity Limits

**CG Envelope:**
- **Forward Limit:** 15% MAC
- **Aft Limit:** 42% MAC
- **MAC Location:** Station 18.5 m (from nose datum)
- **MAC Length:** 8.2 m

**Loading Stations:**
- Cabin zones: 7 zones (Station 8.0 to Station 48.0 m)
- Cargo compartments: 3 compartments
- H₂ fuel tanks: 4 tanks (symmetrical)

### BWB-Specific Considerations

The Blended Wing Body configuration presents unique weight and balance characteristics:
- Wide CG range due to distributed passenger seating
- Fuel distribution affects CG significantly
- Center tank provides CG control capability
- Non-traditional moment arm calculations

## Interface Specifications

**Data Exchange Method:** 
- Master weight statement (Excel/CSV)
- CG calculation worksheets
- Loading charts and tables

**Coordinate System:** 
- Reference: Nose datum (Station 0)
- Positive aft along aircraft centerline
- CG expressed in % MAC and Station

**Accuracy Requirements:**
- Weight measurements: ±0.5% MTOW
- CG position: ±0.5% MAC
- Loading calculations: ±50 kg per zone

## H₂ System Weight Impact

**Hydrogen Fuel Density Considerations:**
- Liquid H₂ density: 71 kg/m³ @ -253°C
- Tank structure weight fraction: 15%
- Boil-off margin: 2% per 24 hours
- CG shift with fuel consumption: Managed by tank sequencing

## Dependencies

- H₂ fuel system capacity (ATA 28)
- Structural design loads (ATA 20)
- Cabin configuration (ATA 25)
- Cargo compartment volumes (ATA 50)

## Responsibilities

**ATA 02-10 (Provider):**
- Maintain accurate weight statement
- Define CG limits
- Update with configuration changes
- Coordinate weighing events

**ATA 08 (Consumer):**
- Conduct aircraft weighing
- Validate weight and balance data
- Generate loading manuals
- Train load planners

## Change Control

Weight and balance data changes require:
1. Structural analysis validation
2. Flight test verification (if CG limits change)
3. Update to Aircraft Flight Manual
4. Operator training on new limits

## Critical Monitoring

**Real-time CG monitoring required for:**
- H₂ fuel transfer operations
- Cargo loading/unloading
- Passenger distribution (BWB-specific)
- In-flight fuel consumption

Interface with CAOS (ATA 95) provides real-time weight and balance monitoring.

## References

- EASA CS-25.23 to 25.27: Load Distribution Limits
- FAA AC 120-27F: Aircraft Weight and Balance Control
- SAE AIR1168: Aircraft Weight and Balance Control

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Review Cycle: Annual or per modification
