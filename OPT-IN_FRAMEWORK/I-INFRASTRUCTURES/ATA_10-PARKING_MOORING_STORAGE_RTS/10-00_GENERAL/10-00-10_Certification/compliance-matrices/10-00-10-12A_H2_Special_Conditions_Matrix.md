# 10-00-10-12A H2 Special Conditions Matrix

## Document Information

- **Document ID**: 10-00-10-12A
- **Title**: Hydrogen Special Conditions Compliance Matrix
- **Revision**: A
- **Version**: 1.0
- **Status**: Draft
- **Date**: 2025-12-10
- **Owner**: AMPEL360 H2 Systems Certification Team
- **ATA Chapter**: 10 - Parking, Mooring, Storage & RTS
- **Section**: 10-00-10 Certification

## Purpose

This matrix tracks compliance with proposed Special Conditions for hydrogen (H2) and liquid hydrogen (LH2) systems during parking, mooring, storage, and return to service operations.

## Scope

Special Conditions required because CS-25/FAR 25 do not adequately address:
- Hydrogen fuel safety during ground operations
- Cryogenic LH2 system management (-253°C)
- H2 leak detection and emergency response
- Safety zones for H2 aircraft

## Reference Documents

- H2 Special Conditions: [10-00-10-30A](../special-conditions/10-00-10-30A_H2_Special_Conditions.md)
- LH2 Special Conditions: [10-00-10-31A](../special-conditions/10-00-10-31A_LH2_Fuel_Special_Conditions.md)
- H2 Certification Plan: [10-00-10-03A](../certification-plans/10-00-10-03A_H2_Certification_Plan.md)
- NFPA 2 Matrix: [10-00-10-14A](./10-00-10-14A_NFPA2_Compliance_Matrix.md)

## Special Conditions Compliance Matrix

### SC-H2-01: Hydrogen Leak Detection

| Requirement | Acceptance Criteria | MOC | Status | Evidence | Authority Status |
|-------------|---------------------|-----|--------|----------|------------------|
| Detection sensitivity | ≥ 25% LEL | Testing | In Progress | Sensor specs, test data | Draft submitted |
| Response time | < 2 seconds | Testing | In Progress | Response time tests | Draft submitted |
| Coverage | All potential leak points | Analysis, Testing | In Progress | Coverage map | Draft submitted |
| Ground crew warning | Automatic audible/visual | Demo | Planned | System demo | Draft submitted |
| Emergency shutdown integration | Automatic or manual | Testing | Planned | Integration tests | Draft submitted |

**MOC Reference**: [10-00-10-24A_H2_Safety_MOC.md](../means-of-compliance/10-00-10-24A_H2_Safety_MOC.md)

### SC-H2-02: Safety Zones During Parking

| Zone | Distance | Requirements | MOC | Status | Evidence |
|------|----------|--------------|-----|--------|----------|
| Zone 1 (Restricted) | 0-3m | No ignition sources, trained personnel only | Analysis | In Progress | CFD dispersion modeling |
| Zone 2 (Controlled) | 3-8m | Limited ignition sources, qualified personnel | Analysis | In Progress | Hazard analysis |
| Zone 3 (Monitored) | 8-15m | Standard ops with awareness | Analysis | Planned | Risk assessment |
| Indoor parking | Modified zones | Enhanced ventilation required | Analysis, Testing | Planned | Ventilation study |

**MOC Reference**: [10-00-10-24A_H2_Safety_MOC.md](../means-of-compliance/10-00-10-24A_H2_Safety_MOC.md)

**Basis**: 
- NFPA 2 Section 6.3.2 (adapted for aviation)
- ISO 13984 principles
- Worst-case leak scenario analysis

### SC-H2-03: Venting and Defueling Requirements

| Requirement | Acceptance Criteria | MOC | Status | Evidence |
|-------------|---------------------|-----|--------|----------|
| Continuous boiloff venting | < 1% per day | Testing | Planned | Boiloff rate tests |
| Emergency venting capacity | Full tank in < 30 min | Analysis, Testing | Planned | Vent system sizing |
| Venting height | > 3m above aircraft | Design | In Progress | Design drawings |
| Venting direction | Away from ignition sources | Design, Analysis | In Progress | Dispersion analysis |
| Wind considerations | Operational limitations | Analysis | Planned | Operational limits |
| Controlled defueling | Safe procedure | Procedure | Planned | Procedure validation |

**MOC Reference**: [10-00-10-25A_Cryo_Systems_MOC.md](../means-of-compliance/10-00-10-25A_Cryo_Systems_MOC.md)

### SC-H2-04: Cryogenic System Management

| Requirement | Acceptance Criteria | MOC | Status | Evidence |
|-------------|---------------------|-----|--------|----------|
| Boiloff rate | < 1% per day normal parking | Testing | Planned | Long-duration tests |
| Thermal protection | Effective at -253°C | Analysis, Testing | In Progress | Thermal analysis |
| No external ice formation | Surface temp > 0°C | Testing | Planned | Environmental tests |
| Ground crew protection | PPE requirements, procedures | Analysis, Procedure | In Progress | Training materials |
| Material compatibility | Certified to -253°C | Analysis, Testing | In Progress | Material tests |

**MOC Reference**: [10-00-10-25A_Cryo_Systems_MOC.md](../means-of-compliance/10-00-10-25A_Cryo_Systems_MOC.md)

### SC-H2-05: Emergency Response Procedures

| Scenario | Procedure Required | Acceptance Criteria | MOC | Status |
|----------|-------------------|---------------------|-----|--------|
| H2 leak detection alarm | Emergency response | Shutdown < 30 sec | Demo | Planned |
| Fire involving H2 | Firefighting approach | Coordinated with airport | Procedure | In Progress |
| Loss of safety systems | Backup procedures | Safe state achieved | Analysis | Planned |
| Overpressure condition | Pressure relief | Relief < critical pressure | Testing | Planned |
| Emergency defueling | Rapid defueling | Complete in < X hours | Procedure | Planned |

**MOC Reference**: [10-00-10-24A_H2_Safety_MOC.md](../means-of-compliance/10-00-10-24A_H2_Safety_MOC.md)

## NFPA 2 Alignment

| NFPA 2 Requirement | H2 Special Condition | Compliance Approach |
|-------------------|---------------------|---------------------|
| 6.3.1 - Aircraft applications | SC-H2-01 to SC-H2-05 | Special conditions based on NFPA 2 |
| 6.3.2 - Safety distances | SC-H2-02 | CFD-validated safety zones |
| 6.3.3 - Ventilation | SC-H2-03 | Venting system design |
| 6.3.4 - Emergency procedures | SC-H2-05 | Comprehensive emergency procedures |

**Reference**: [10-00-10-14A_NFPA2_Compliance_Matrix.md](./10-00-10-14A_NFPA2_Compliance_Matrix.md)

## Compliance Status Summary

| Special Condition | Overall Status | Target Approval | Critical Path |
|------------------|----------------|-----------------|---------------|
| SC-H2-01 (Leak Detection) | In Progress | Month 12 | Sensor validation |
| SC-H2-02 (Safety Zones) | In Progress | Month 12 | CFD analysis |
| SC-H2-03 (Venting) | Planned | Month 18 | System design |
| SC-H2-04 (Cryogenic) | In Progress | Month 18 | Thermal testing |
| SC-H2-05 (Emergency) | In Progress | Month 15 | Procedure validation |

## Evidence Package Organization

```
/H2_Special_Conditions_Evidence/
├── SC-H2-01_Leak_Detection/
│   ├── Sensor_Specifications.pdf
│   ├── Coverage_Analysis.pdf
│   ├── Response_Time_Test_Results.pdf
│   └── Integration_Test_Report.pdf
├── SC-H2-02_Safety_Zones/
│   ├── CFD_Dispersion_Analysis.pdf
│   ├── Worst_Case_Leak_Scenario.pdf
│   ├── Risk_Assessment.pdf
│   └── Indoor_Parking_Ventilation_Study.pdf
├── SC-H2-03_Venting/
│   ├── Vent_System_Design.pdf
│   ├── Boiloff_Rate_Analysis.pdf
│   ├── Emergency_Vent_Sizing.pdf
│   └── Dispersion_Modeling.pdf
├── SC-H2-04_Cryogenic/
│   ├── Thermal_Analysis.pdf
│   ├── Insulation_Performance_Tests.pdf
│   ├── Material_Compatibility_Tests.pdf
│   └── Long_Duration_Parking_Tests.pdf
└── SC-H2-05_Emergency/
    ├── Emergency_Procedures_Manual.pdf
    ├── Shutdown_Time_Tests.pdf
    ├── Airport_Coordination_Records.pdf
    └── Training_Materials.pdf
```

## Open Items

### Critical
1. **OI-H2-01**: EASA/FAA acceptance of safety zone distances
   - Status: Issue paper in preparation
   - Target: Month 6

2. **OI-H2-02**: Cryogenic system boiloff rate validation
   - Status: Test planning
   - Target: Month 18

### Important
3. **OI-H2-03**: Emergency defueling procedure validation
4. **OI-H2-04**: Ground crew training program approval

## Related Documents

- H2 Special Conditions: [10-00-10-30A](../special-conditions/10-00-10-30A_H2_Special_Conditions.md)
- H2 Safety MOC: [10-00-10-24A](../means-of-compliance/10-00-10-24A_H2_Safety_MOC.md)
- Cryo Systems MOC: [10-00-10-25A](../means-of-compliance/10-00-10-25A_Cryo_Systems_MOC.md)

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**
- **Status**: DRAFT – Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-10

### Revision History

| Revision | Date | Author | Description | Approved By |
|----------|------|--------|-------------|-------------|
| A | 2025-12-10 | AMPEL360 H2 Cert Team | Initial draft | Pending |

---

*This document is part of the ATA 10 Certification documentation suite for the AMPEL360-BWB-H2 aircraft.*
