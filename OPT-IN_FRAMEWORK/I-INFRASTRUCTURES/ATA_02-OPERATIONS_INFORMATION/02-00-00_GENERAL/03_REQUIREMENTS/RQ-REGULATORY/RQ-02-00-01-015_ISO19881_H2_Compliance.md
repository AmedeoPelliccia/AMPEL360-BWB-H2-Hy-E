# RQ-02-00-01-015: ISO 19881 H₂ Compliance

## Requirement Details

**ID:** RQ-02-00-01-015  
**Category:** Regulatory  
**Subcategory:** H2  
**Title:** ISO 19881 H₂ Fuel Container Compliance  
**Priority:** Critical  
**Status:** Approved

## Description

The hydrogen fuel storage system shall comply with ISO 19881:2018 "Gaseous hydrogen — Land vehicle fuel containers" requirements for design, construction, testing, and marking of compressed gaseous hydrogen fuel containers.

## Rationale

ISO 19881:2018 is the international standard for hydrogen fuel containers in vehicles. Compliance ensures safety and enables international operations with hydrogen refueling infrastructure.

## Source

- **Document:** ISO 19881:2018
- **Section:** All sections applicable to aircraft use
- **Effective Date:** 2018

## Acceptance Criteria

1. Tank design pressure rating complies with Section 5
2. Material selection per Section 6 requirements
3. Leak-before-break design verified
4. Pressure cycling test completed (15,000 cycles minimum)
5. Burst pressure test at 2.35x design pressure
6. Fire resistance test passed
7. Gunfire penetration test completed
8. Permeation rate below specified limits
9. Marking and labeling per Section 10

## Verification Method

**Method:** Test  
**Procedure:** TP-H2-TANK-001  
**Status:** Verified  
**Date:** 2025-08-20

## Traceability

- **Parent ATA:** 02-30-00 (Hydrogen Fuel Data)
- **Design Implementation:** ATA 28-10-00 H₂ Storage Tanks
- **Verification Doc:** VER-28-10-001
- **Validation Doc:** VAL-28-10-001

## Related Requirements

- RQ-02-00-01-016: SAE J2719 Fuel Quality
- RQ-02-00-01-017: NFPA 2 H₂ Code
- RQ-02-00-05-001: H₂ Capacity 8000 kg
- RQ-02-00-05-003: H₂ Temperature -253°C
- RQ-02-00-05-004: H₂ Pressure 2.8-3.2 bar

## Impact Areas

- Tank design and materials
- Testing and qualification program
- Maintenance procedures
- Ground handling procedures
- Refueling operations

## Risks

- **Risk:** Cryogenic operation adds complexity beyond ISO 19881 scope
- **Mitigation:** Apply additional cryogenic standards (ASME Section VIII), special approval from authorities

## Notes

ISO 19881 is primarily designed for compressed gas at ambient temperature. Adaptation for cryogenic liquid hydrogen storage requires additional analysis and special conditions to certification basis.

The requirement is met through combination of:
- ISO 19881 for general hydrogen safety principles
- ASME Section VIII for cryogenic pressure vessels
- Special Conditions from EASA/FAA for aircraft application

---

**Document Control**  
**Version:** 1.0  
**Last Updated:** 2025-11-04  
**Owner:** H₂ Systems Engineering  
**Approved By:** Chief H₂ Systems Engineer
