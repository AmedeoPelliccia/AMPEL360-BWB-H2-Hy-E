# [RQ-02-00-01-015](./RQ-02-00-01-015_*.md): [ISO 19881](https://www.iso.org/standard/66482.html) H₂ Compliance

## Requirement Details

**ID:** [RQ-02-00-01-015](./RQ-02-00-01-015_*.md)  
**Category:** Regulatory  
**Subcategory:** H2  
**Title:** [ISO 19881](https://www.iso.org/standard/66482.html) H₂ Fuel Container Compliance  
**Priority:** Critical  
**Status:** Approved

## Description

The hydrogen fuel storage system shall comply with [ISO 19881:2018](https://www.iso.org/standard/66482.html) "Gaseous hydrogen — Land vehicle fuel containers" requirements for design, construction, testing, and marking of compressed gaseous hydrogen fuel containers.

## Rationale

[ISO 19881:2018](https://www.iso.org/standard/66482.html) is the international standard for hydrogen fuel containers in vehicles. Compliance ensures safety and enables international operations with hydrogen refueling infrastructure.

## Source

- **Document:** [ISO 19881:2018](https://www.iso.org/standard/66482.html)
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
- **Design Implementation:** [ATA 28-10-00](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENIC_SYSTEMS/ATA_28-FUEL_SAF_AND_CRYOGENIC/) H₂ Storage Tanks
- **Verification Doc:** VER-28-10-001
- **Validation Doc:** VAL-28-10-001

## Related Requirements

- [RQ-02-00-01-016](./RQ-02-00-01-016_*.md): [SAE J2719](https://www.sae.org/standards/content/j2719_202009/) Fuel Quality
- [RQ-02-00-01-017](./RQ-02-00-01-017_*.md): [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) H₂ Code
- [RQ-02-00-05-001](../RQ-H2-OPERATIONS/RQ-02-00-05-001_*.md): H₂ Capacity 8000 kg
- [RQ-02-00-05-003](../RQ-H2-OPERATIONS/RQ-02-00-05-003_*.md): H₂ Temperature -253°C
- [RQ-02-00-05-004](../RQ-H2-OPERATIONS/RQ-02-00-05-004_*.md): H₂ Pressure 2.8-3.2 bar

## Impact Areas

- Tank design and materials
- Testing and qualification program
- Maintenance procedures
- Ground handling procedures
- Refueling operations

## Risks

- **Risk:** Cryogenic operation adds complexity beyond [ISO 19881](https://www.iso.org/standard/66482.html) scope
- **Mitigation:** Apply additional cryogenic standards (ASME Section VIII), special approval from authorities

## Notes

[ISO 19881](https://www.iso.org/standard/66482.html) is primarily designed for compressed gas at ambient temperature. Adaptation for cryogenic liquid hydrogen storage requires additional analysis and special conditions to certification basis.

The requirement is met through combination of:
- [ISO 19881](https://www.iso.org/standard/66482.html) for general hydrogen safety principles
- [ASME Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-rules-construction-pressure-vessels) for cryogenic pressure vessels
- Special Conditions from [EASA](https://www.easa.europa.eu/)/[FAA](https://www.faa.gov/) for aircraft application

---

**Document Control**  
**Version:** 1.0  
**Last Updated:** 2025-11-04  
**Owner:** H₂ Systems Engineering  
**Approved By:** Chief H₂ Systems Engineer
