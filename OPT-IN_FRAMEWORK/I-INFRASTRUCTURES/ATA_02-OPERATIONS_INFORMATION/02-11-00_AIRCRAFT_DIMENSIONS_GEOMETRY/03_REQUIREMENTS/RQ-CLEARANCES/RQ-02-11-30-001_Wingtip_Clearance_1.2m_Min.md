# RQ-02-11-30-001: Wingtip Ground Clearance

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The minimum wingtip ground clearance shall be 1.2 meters at Maximum Takeoff Weight (MTOW) with landing gear extended in level attitude on a flat, paved surface.

## Rationale

**Safety Margin:**
- Prevents wingtip strike during normal operations
- Accounts for wing flex under load
- Provides margin for uneven surfaces
- Supports operational safety requirements

**Operational Constraints:**
- Taxi on uneven surfaces: 0.8m practical minimum
- Wing droop at MTOW: 150mm maximum
- Safety margin: 300mm above absolute minimum
- CS-25.231 compliance

**BWB Considerations:**
- Low aspect ratio (3.2) reduces tip clearance issues vs high AR
- Wide wingspan (52m) requires careful ground operations
- Wing walker procedures for tight clearances

## Verification Method

**Static Test:**
- Aircraft at MTOW (185,000 kg)
- Level attitude on calibrated platform
- Landing gear properly extended
- Measurement at lowest wingtip point

**Dynamic Validation:**
- Taxi tests on representative surfaces
- Crosswind taxi validation
- Turning radius verification
- CAOS ground clearance monitoring validation

**Acceptance Criteria:**
- Static clearance ≥ 1.2m ±0.05m
- Dynamic clearance ≥ 1.0m (with monitoring)
- No contact during maximum deflection tests

## Monitoring Requirements

**CAOS Integration:**
- Real-time ground clearance calculation
- Crew advisory below 1.5m
- Crew warning below 1.0m
- Ground mode activation mandatory

**Ground Crew:**
- Visual inspection procedures
- Wing walker deployment criteria (<2m clearance)
- Enhanced marshalling for restricted areas

## Compliance

**Regulatory:**
- [CS-25.231](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Ground clearance)
- [CS-25.25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Weight limits)
- [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx) (Operations)

**Operational:**
- Company ground handling procedures
- Airport compatibility requirements
- Emergency response planning

## Related Requirements

- [RQ-02-11-30-002](RQ-02-11-30-002_Belly_Clearance_1.8m_Min.md) (Belly Clearance)
- [RQ-02-11-50-001](../RQ-AIRPORT-COMPATIBILITY/RQ-02-11-50-001_Taxiway_Width_23m_Min.md) (Taxiway Width)
- [RQ-02-11-60-003](../RQ-TOLERANCES/RQ-02-11-60-003_Operational_Deflections.md) (Operational Deflections)
