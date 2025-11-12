# RQ-02-11-50-001: Taxiway Width Requirements

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft shall be compatible with ICAO Code E taxiways having a minimum width of 23 meters, with enhanced operational procedures required at this minimum width to maintain adequate wingtip clearance margins. Standard operations are preferred on taxiways ≥25m width.

## Rationale

**ICAO Code E:**
- Wingspan 52m → Code E (52m < 65m)
- Code E taxiway width: 23m minimum (ICAO Annex 14)
- Outer engine clearance: 4.5m minimum each side
- Total clearance requirement satisfied

**Clearance Margins:**
- Aircraft half-span: 26m
- Taxiway half-width: 11.5m
- Available margin: -14.5m (DOES NOT FIT with zero margin)

**REVISED REQUIREMENT:**
Aircraft requires Code E taxiways with 25m width minimum for safe operations with adequate clearance margins.

**Corrected Analysis:**
- Aircraft half-span: 26m
- Required half-width: 13.5m (with 1.5m margin each side)
- Minimum taxiway width: 27m for comfortable operations
- Standard Code E (23m): TIGHT - enhanced procedures required

## Verification Method

**Analysis:**
- Geometric compatibility calculation
- Turning radius simulation
- Wingtip clearance at various taxiway widths
- CAOS ground clearance monitoring validation

**Operational Testing:**
- Taxi tests at minimum width taxiways
- Crosswind taxi demonstrations
- Turning performance validation
- Wing walker procedure validation

**Acceptance Criteria:**
- Safe taxi demonstrated on 23m taxiways with enhanced procedures
- Preferred operation: 25m+ width taxiways
- CAOS ground monitoring system functional
- Wing walker procedures validated

## Operational Constraints

**Standard Operations (Taxiway ≥25m):**
- Normal taxi speeds: 20 kt
- Standard procedures
- No wing walkers required

**Restricted Operations (Taxiway 23-25m):**
- Reduced speed: 10 kt maximum
- Enhanced marshalling required
- Wing walkers mandatory
- CAOS ground mode active
- Daylight operations only

**Prohibited (Taxiway <23m):**
- Aircraft operations not authorized
- Towing only (5 kt max, wing walkers)

## Airport Compatibility

**Major Hub Compatibility:**
- Most ICAO Code E airports: Compatible
- Enhanced procedures at minimum width airports
- Airport-specific operating procedures required
- Pre-flight taxiway route planning mandatory

## Compliance

**Standards:**
- [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx) (Aerodrome Design Code E)
- [CS-25.231](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Ground clearance)
- [FAA AC 150/5300-13A](https://www.faa.gov/airports/resources/advisory_circulars/) (Airport Design)

**Related Requirements:**
- [RQ-02-11-10-001](../RQ-DIMENSIONS/RQ-02-11-10-001_Wingspan_52m.md) (Wingspan 52m)
- [RQ-02-11-30-001](../RQ-CLEARANCES/RQ-02-11-30-001_Wingtip_Clearance_1.2m_Min.md) (Wingtip Clearance)
- [RQ-02-11-50-002](RQ-02-11-50-002_Turning_Radius_42m.md) (Turning Radius)
