# Requirements: 06-10-01 - Overall Dimensions

## Purpose
This folder documents all requirements for the overall dimensions of the AMPEL360 aircraft, including certification requirements, operational requirements, and interface requirements.

## Certification Requirements

### CS-25 (Large Aeroplanes)
- **[CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):** Door dimensions (minimum dimensions, emergency egress)
- **[CS-25.803](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):** Emergency evacuation (90-second requirement)
- **[CS-25.109](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):** Accelerate-stop distance (affected by length)
- **[CS-25.1359](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):** Electrical system fire protection (compartment dimensions)

### ICAO Standards
- **[ICAO Annex 14](https://www.icao.int/safety/airnavigation/nationalitymarks/annexes_booklet_en.pdf):** Aerodromes (aerodrome reference code)
- **[ICAO Doc 9157](https://www.icao.int/publications/Pages/catalogue.aspx):** Aerodrome Design Manual

### FAA Regulations
- **[FAA AC 150/5300-13B](https://www.faa.gov/airports/resources/advisory_circulars/index.cfm/go/document.current/documentNumber/150_5300-13):** Airport Design
- **[FAA AC 25.783-1A](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/22876):** Fuselage Doors and Hatches

## Operational Requirements

### Airport Compatibility
- Gate compatibility: ≤55m length for 85% of international gates
- Code E apron: wingspan 52-65m
- Hangar compatibility: width ≤70m, height ≤13m

### Performance Requirements
- Cruise L/D ≥23 (wingspan optimization)
- Takeoff field length ≤2,500m (wing loading)
- Landing field length ≤2,200m

### Capacity Requirements
- 300 passengers (3-class configuration)
- 18 LD-3 containers (cargo capacity)
- 7,500 nm range (fuel volume requirement)

## Requirements Traceability Matrix
| Req ID | Requirement | Source | Verification Method | Status |
|--------|-------------|--------|---------------------|--------|
| DIM-001 | Wingspan ≤65m | ICAO Code E | Measurement | Verified |
| DIM-002 | Length ≤55m | Gate Compatibility | CAD Analysis | Verified |
| DIM-003 | Height ≤13m | Hangar Compatibility | CAD Analysis | Verified |
| DIM-004 | Emergency exits ≤18m spacing | CS-25.803 | Analysis | Verified |
| DIM-005 | Propulsor ground clearance ≥3.5m | Safety Requirement | CAD Analysis | Verified |

## Interface Requirements
- **ATA 07:** Jack point locations for lifting
- **ATA 08:** Datum references for weighing
- **ATA 09:** Tow bar attachment coordinates
- **ATA 28:** Fuel tank volume and placement

## Document Status
**Status:** Approved  
**Last Review:** 2025-11-01  
**Next Review:** 2026-05-01
