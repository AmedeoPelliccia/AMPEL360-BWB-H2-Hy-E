# [28-00-03-SHM-001](./28-00-03-SHM-001_H2_Tank_Structure_Monitoring.md): H2 Tank Structure Monitoring Requirements

## Requirement ID
**28-00-03-SHM-001**

## Title
Hydrogen Tank Structure Monitoring via SHM Integration

## Category
SHM_H2_Interface

## Description
The SHM system shall monitor the structural integrity of hydrogen fuel tank support structures, cryogenic zone interfaces, and tank-fuselage attachments. The monitoring system shall operate effectively across the extreme temperature range associated with liquid hydrogen storage (-253°C to ambient).

This requirement addresses the unique challenges of SHM in cryogenic environments and ensures compliance with parent requirement [53-00-03-01-005](../../../../../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md).

## Rationale
Hydrogen tank structure monitoring is critical for:
- **Cryogenic stress monitoring**: Thermal cycling creates unique fatigue loading on support structures
- **Leak prevention**: Early detection of micro-cracks before hydrogen permeation
- **Safety assurance**: H2 tank failure consequences are catastrophic (DAL A consideration)
- **Novel design validation**: First-generation aircraft requires enhanced monitoring
- **Certification credit**: SHM may provide alternative compliance for damage tolerance

For the AMPEL360 BWB hydrogen-hybrid aircraft:
- **Integrated tank design**: Tank support structure is integral with fuselage
- **Thermal gradients**: Extreme temperature differences between tank and cabin
- **Material challenges**: Specialized materials at cryogenic temperatures
- **Limited access**: Tank locations restrict conventional inspection

## Acceptance Criteria

### Summary Table
| # | Parameter | Requirement | Verification |
|---|-----------|-------------|--------------|
| 1 | Tank support coverage | 100% of critical joints | Analysis + Test |
| 2 | Cryogenic sensor operation | -253°C to +40°C | Test |
| 3 | Thermal gradient compensation | Validated algorithm | Analysis + Test |
| 4 | Crack detection (cryogenic) | ≥ 3.0 mm at 90/95 POD | Test |
| 5 | Monitoring frequency | Continuous during ops | Design Review |
| 6 | Hydrogen embrittlement detection | Per specification | Test |

### Detailed Acceptance Criteria

#### 1. Monitoring Zone Coverage
| Zone | Coverage | Damage Types | Priority |
|------|----------|--------------|----------|
| Tank forward attachment | 100% | Fatigue cracks, embrittlement | Critical |
| Tank aft attachment | 100% | Fatigue cracks, embrittlement | Critical |
| Tank lateral supports | 100% | Thermal fatigue, disbond | Critical |
| Thermal insulation interface | ≥ 95% | Disbond, moisture ingress | High |
| Fuselage transition zone | ≥ 95% | Thermal stress, fatigue | High |
| Vent line attachments | 100% | Vibration fatigue | Medium |

#### 2. Cryogenic Sensor Requirements
| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| Operating temperature | -253°C to +40°C | LH2 tank to ambient |
| Thermal cycling endurance | 10,000 cycles | -253°C to +20°C |
| Temperature compensation | Automatic | Real-time correction |
| Sensor type (primary) | Fiber Bragg Grating (FBG) | Cryogenic-rated |
| Sensor type (secondary) | Piezoelectric (cryo-rated) | Specialized formulation |
| Signal stability | ≤ 2% drift across temperature | Per sensor specification |

#### 3. Detection Requirements (Cryogenic Zone)
| Damage Type | Minimum Detectable Size | POD | Environment |
|-------------|------------------------|-----|-------------|
| Fatigue crack (Ti-6Al-4V) | 3.0 mm | ≥ 90% @ 95% conf | -253°C |
| Fatigue crack (Inconel) | 3.0 mm | ≥ 90% @ 95% conf | -253°C |
| Disbond (insulation) | 50 mm diameter | ≥ 90% @ 95% conf | -253°C |
| Hydrogen embrittlement | Per HE criteria | ≥ 85% @ 95% conf | -253°C |

#### 4. Thermal Gradient Management
| Parameter | Requirement |
|-----------|-------------|
| Temperature measurement | ≤ ±2°C accuracy |
| Gradient mapping | Real-time thermal profile |
| Baseline compensation | Temperature-indexed baselines |
| Transition zone monitoring | Enhanced density in gradient zones |
| Thermal event detection | Anomaly detection for insulation failure |

#### 5. Data Acquisition (H2 Zone)
| Parameter | Requirement |
|-----------|-------------|
| Sampling rate | ≥ 500 kHz (guided wave) |
| Data resolution | 16-bit minimum |
| Noise floor | ≤ 30 dB SNR |
| Data integrity | CRC validation |
| Storage | 7-day local buffer |

## Verification Method

| Method | Description | Deliverable |
|--------|-------------|-------------|
| **Analysis** | Thermal modeling, coverage analysis | Analysis Report AR-28-SHM-001 |
| **Test** | Cryogenic sensor validation, POD demonstration | Test Report TR-28-SHM-001 |
| **Inspection** | Sensor installation review | Inspection Report IR-28-SHM-001 |

### Verification Activities
| Activity ID | Title | Type | Status |
|-------------|-------|------|--------|
| V&V-28-SHM-001 | Cryogenic Sensor Qualification | Test | Planned |
| V&V-28-SHM-002 | Tank Support Coverage Analysis | Analysis | Planned |
| V&V-28-SHM-003 | Thermal Compensation Validation | Test | Planned |
| V&V-28-SHM-004 | POD Demonstration (Cryogenic) | Test | Planned |

## Traceability

### Parent Requirements
| Requirement | Title | Source |
|-------------|-------|--------|
| [53-00-03-01-005](../../../../../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions | Primary SHM Requirement |
| [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Damage Tolerance and Fatigue Evaluation | EASA CS-25 |
| CS-25.981 | Fuel Tank Ignition Prevention | EASA CS-25 |
| EASA SC H2-001 | Hydrogen Fuel Systems (anticipated) | Special Condition |

### Related Requirements
| Requirement ID | Title | Relationship |
|----------------|-------|--------------|
| [53-00-03-07-001](../../../../../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/07_SHM_and_Monitoring/53-00-03-07-001_Sensor_Network_Coverage.md) | Sensor Network Coverage | System integration |
| 28-00-03-01-001 | H2 Tank Structural Requirements | Structure design basis |
| 73-00-03-SHM-001 | H2 System Interface SHM | Fuel system interface |

### Interface Requirements
| Interface | Document | Content |
|-----------|----------|---------|
| Fuselage SHM | ICD-28-53-SHM-001 | Tank-fuselage interface |
| Fuel System | ICD-28-73-001 | Fuel system sensors |
| Thermal Management | ICD-28-21-001 | Temperature data sharing |

## Assumptions and Constraints

### Assumptions
- Fiber Bragg Grating sensors available for -253°C operation
- Cryogenic piezoelectric sensors qualified for application
- Tank support structure accessible during manufacturing for sensor installation
- Thermal insulation system design finalized

### Constraints
| Parameter | Limit | Justification |
|-----------|-------|---------------|
| Sensor installation temperature | Ambient only | Cryogenic bonding not feasible |
| Sensor replacement access | Major maintenance | Tank location |
| Power dissipation (cryogenic zone) | ≤ 2 W per sensor | Heat leak minimization |
| EMI emissions | Per DO-160G | H2 safety |
| Cable penetrations | Hermetic sealed | Pressure/vacuum boundary |

## Safety Impact
**Design Assurance Level (DAL)**: B (Hazardous)

H2 tank structural failure could result in hazardous conditions. SHM provides enhanced monitoring capability but is not sole means of compliance. Conventional inspection program remains as backup.

## Priority
**CRITICAL**

## Status
**DRAFT**

## Owner
Hydrogen Systems Engineering / Structures / SHM Integration

## Reviewers
| Role | Name | Status | Date |
|------|------|--------|------|
| Lead Reviewer | H2 Systems Lead | Pending | — |
| Structures | Cryogenic Structures Lead | Pending | — |
| SHM Integration | SHM Systems Lead | Pending | — |
| Certification | Certification Engineer | Pending | — |

## Change History
| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-27 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial draft |

## Last Updated
2025-11-27

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Human Approver | _[to be completed]_ |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| File Path | `OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/28-00_GENERAL/28-00-03_Requirements/SHM_H2_Interface/` |
| Last AI Update | 2025-11-27 |

---

## Notes for Reviewers

1. **Cryogenic sensor technology**: FBG sensors are the primary technology for cryogenic zones due to temperature stability
2. **Hydrogen embrittlement**: Detection requirements need coordination with materials engineering
3. **Special Condition**: Anticipate EASA Special Condition for H2 systems requiring SHM justification
4. **DAL B consideration**: May need to elevate DAL based on safety assessment outcomes
5. **Thermal management interface**: Coordination with ATA 21 for thermal data sharing

---
