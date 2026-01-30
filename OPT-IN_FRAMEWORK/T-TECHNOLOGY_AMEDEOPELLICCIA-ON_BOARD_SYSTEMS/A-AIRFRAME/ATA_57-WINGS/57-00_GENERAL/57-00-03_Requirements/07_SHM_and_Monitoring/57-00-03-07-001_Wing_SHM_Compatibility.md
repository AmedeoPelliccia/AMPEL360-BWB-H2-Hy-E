# [57-00-03-07-001](./57-00-03-07-001_Wing_SHM_Compatibility.md): Wing SHM Compatibility

## Requirement ID
**57-00-03-07-001**

## Title
Wing Structure Compatibility with SHM Assumptions

## Category
07_SHM_and_Monitoring

## Description
The wing structural design shall be compatible with Structural Health Monitoring (SHM) system assumptions, including sensor placement, damage detection capabilities, and structural response characteristics. The wing structure shall provide adequate signal propagation and sensor accessibility for effective health monitoring of critical areas including:
- Wing-body junction (critical for BWB configuration)
- Wing carry-through structure
- Wing box primary structure
- Leading and trailing edge attachments
- Control surface hinge points

This requirement ensures alignment with parent requirement [53-00-03-01-005](../../../../ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) and extends SHM compatibility to wing-specific structures.

## Rationale
For the AMPEL360 BWB hydrogen-hybrid aircraft, wing SHM compatibility is particularly critical due to:
- **Blended Wing Body (BWB) configuration**: Wing-body junction loads are distributed over large areas requiring specialized monitoring
- **Integrated fuel storage**: Potential future integration with H2 fuel systems requires monitoring of structural interfaces
- **Advanced composites**: CFRP wing skins require specialized damage detection (delamination, disbond, BVID)
- **Extended service intervals**: SHM enables condition-based maintenance reducing scheduled inspections
- **Continuous load paths**: BWB configuration creates unique load paths requiring comprehensive coverage

## Acceptance Criteria

### Summary Table
| # | Parameter | Requirement | Verification |
|---|-----------|-------------|--------------|
| 1 | Wing-body junction coverage | 100% | Analysis + Test |
| 2 | Wing box primary structure coverage | ≥ 95% | Analysis + Test |
| 3 | Signal attenuation (CFRP) | ≤ 20 dB over 0.75 m | Test |
| 4 | Signal attenuation (titanium fittings) | ≤ 12 dB over 1.2 m | Test |
| 5 | Sensor mounting provisions | Per design requirements | Design Review |
| 6 | Access panel integration | Sensor routes defined | Design Review |

### Detailed Acceptance Criteria

#### 1. Wing-Body Junction Monitoring
| Zone | Coverage Requirement | Damage Types | Sensor Technology |
|------|---------------------|--------------|-------------------|
| Upper blend region | 100% | Fatigue, delamination | PZT + FBG |
| Lower blend region | 100% | Fatigue, delamination | PZT + FBG |
| Carry-through structure | 100% | Cracks, corrosion | PZT + ECA |
| Attachment fittings | 100% | Fatigue cracks | PZT + CVM |

#### 2. Signal Propagation Requirements (Wing-Specific)
| Material/Location | Maximum Attenuation | Monitoring Distance | Notes |
|-------------------|---------------------|---------------------|-------|
| CFRP upper skin | ≤ 20 dB | 0.75 m | Stiffener effects considered |
| CFRP lower skin | ≤ 20 dB | 0.75 m | Access panel cutouts |
| Titanium root fitting | ≤ 12 dB | 1.2 m | High load path |
| Aluminum ribs | ≤ 15 dB | 1.0 m | Fastener influence |
| BWB blend zone | ≤ 25 dB | 0.5 m | Complex geometry |

#### 3. Wave Propagation Analysis (BWB-Specific)
| Analysis Type | Purpose | Deliverable |
|--------------|---------|-------------|
| Lamb wave dispersion | Characterize modes in blended skin | Wave mode map |
| Junction transmission | Quantify signal loss at wing-body blend | Transmission coefficients |
| Stiffener interaction | Model wave behavior at stringers | Sensor placement optimization |
| Temperature compensation | Account for composite thermal effects | Compensation algorithm |

## Verification Method

| Method | Description | Deliverable |
|--------|-------------|-------------|
| **Analysis** | Wave propagation modeling, coverage analysis | Analysis Report AR-57-007 |
| **Test** | Sensor functionality on wing test articles | Test Report TR-57-007 |
| **Inspection** | Design review of sensor integration | Design Review Report DRR-57-007 |

### Verification Activities
| Activity ID | Title | Type | Status |
|-------------|-------|------|--------|
| V&V-57-071 | Wing SHM Integration Verification | Analysis + Test | Planned |
| V&V-57-072 | Wing-Body Junction Sensor Placement | Analysis | Planned |
| V&V-57-073 | BWB Signal Propagation Testing | Test | Planned |
| V&V-57-074 | Wing POD Demonstration | Test | Planned |

## Traceability

### Parent Requirements
| Requirement | Title | Source |
|-------------|-------|--------|
| [53-00-03-01-005](../../../../ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions | Primary SHM Requirement |
| [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Damage Tolerance and Fatigue Evaluation | EASA CS-25 |
| [CS-25.1529](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Instructions for Continued Airworthiness | EASA CS-25 |

### Related Requirements
| Requirement ID | Title | Relationship |
|----------------|-------|--------------|
| [53-00-03-07-001](../../../../ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/07_SHM_and_Monitoring/53-00-03-07-001_Sensor_Network_Coverage.md) | Sensor Network Coverage | Fuselage sensor requirements |
| [53-00-03-07-002](../../../../ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/07_SHM_and_Monitoring/53-00-03-07-002_Data_Acquisition_Requirements.md) | Data Acquisition Requirements | Data system interface |
| 57-00-03-01-001 | Ultimate Load Capability (Wing) | Structure performance basis |

### Interface Requirements
| Interface | Document | Content |
|-----------|----------|---------|
| Fuselage SHM | ICD-57-53-SHM-001 | Wing-body junction sensor interface |
| Electrical System | ICD-57-24-SHM-001 | Wing sensor power distribution |
| Data System | ICD-57-31-SHM-001 | Wing sensor data transmission |

## Assumptions and Constraints

### Assumptions
- Primary sensor technology: Piezoelectric (PZT) guided wave for damage detection
- Secondary technology: Fiber Bragg Grating (FBG) for strain monitoring
- Sensor system designed for 30-year service life with replaceable sensor heads
- Baseline data acquisition performed prior to aircraft entry into service

### Constraints
| Parameter | Limit | Justification |
|-----------|-------|---------------|
| Local stress concentration | ≤ 5% increase | Fatigue impact acceptable |
| Added mass (wing sensors) | ≤ 15 kg per wing | Weight budget allocation |
| Power consumption (wing) | ≤ 100 W per wing | Electrical system capacity |
| Operating temperature | -55°C to +85°C | Standard flight envelope |

## Safety Impact
**Design Assurance Level (DAL)**: C (Major)

The wing SHM compatibility requirement supports damage tolerance compliance and enables enhanced structural monitoring of the critical wing-body junction area.

## Priority
**HIGH**

## Status
**DRAFT**

## Owner
Wing Structures Team / SHM Systems Integration

## Reviewers
| Role | Name | Status | Date |
|------|------|--------|------|
| Lead Reviewer | Wing Structures Lead | Pending | — |
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
| File Path | `OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_57-WINGS/57-00_GENERAL/57-00-03_Requirements/07_SHM_and_Monitoring/` |
| Last AI Update | 2025-11-27 |

---
