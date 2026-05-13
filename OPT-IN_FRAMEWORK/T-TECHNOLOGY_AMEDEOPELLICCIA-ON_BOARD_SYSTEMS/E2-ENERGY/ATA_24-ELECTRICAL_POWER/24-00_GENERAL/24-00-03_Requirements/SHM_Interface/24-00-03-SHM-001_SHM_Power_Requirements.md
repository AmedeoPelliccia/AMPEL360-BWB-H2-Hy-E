# 24-00-03-SHM-001 — SHM Power Requirements

## Requirement ID
**24-00-03-SHM-001**

## Title
Electrical Power Requirements for SHM System

## Category
SHM_Interface

## Description
The electrical power system shall provide dedicated, reliable power supply to the Structural Health Monitoring (SHM) system to support continuous structural monitoring operations. This includes power for:
- Sensor excitation (piezoelectric, strain gauge, fiber optic interrogators)
- Data acquisition units (zone controllers)
- Central processing unit
- Data storage and transmission equipment
- Built-In Test Equipment (BITE)

This requirement ensures the SHM system receives stable, high-quality power to enable accurate damage detection in accordance with parent requirement [53-00-03-01-005](../../../../../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md).

## Rationale
The SHM system requires dedicated electrical power for:
- **Continuous monitoring**: 24/7 operation during flight and ground phases
- **Signal quality**: Clean power essential for sensitive sensor measurements
- **Data integrity**: Uninterrupted power for data acquisition and processing
- **Safety criticality**: Power reliability commensurate with SHM DAL requirements
- **Certification credit**: Reliable power supports SHM certification approach

For the AMPEL360 BWB hydrogen-hybrid aircraft:
- **Distributed architecture**: Power distribution to fuselage zones, wings, and empennage
- **H2 cryogenic zones**: Specialized power provisions for extreme temperature sensors
- **High power efficiency**: Integration with aircraft electrical load management

## Acceptance Criteria

### Summary Table
| # | Parameter | Requirement | Verification |
|---|-----------|-------------|--------------|
| 1 | Total SHM power allocation | 350 W nominal, 500 W peak | Analysis |
| 2 | Power quality | Per DO-160G Section 16 | Test |
| 3 | Bus assignment | Essential bus (2 sources) | Design Review |
| 4 | Voltage regulation | 28 VDC ± 2% | Test |
| 5 | Power interruption tolerance | ≤ 50 ms | Test |
| 6 | Emergency power | 30 min battery backup | Test |

### Detailed Acceptance Criteria

#### 1. Power Budget Allocation
| SHM Component | Nominal Power | Peak Power | Bus Assignment |
|---------------|---------------|------------|----------------|
| Zone Controller 1 (Forward) | 30 W | 45 W | ESS1 |
| Zone Controller 2 (Center) | 35 W | 50 W | ESS1 |
| Zone Controller 3 (Aft) | 30 W | 45 W | ESS2 |
| Zone Controller 4 (Wings) | 40 W | 60 W | ESS2 |
| Zone Controller 5 (H2) | 25 W | 40 W | ESS1 |
| Central Processing Unit | 80 W | 120 W | ESS1/ESS2 (dual) |
| Data Storage Module | 40 W | 60 W | ESS2 |
| Sensor Excitation | 50 W | 60 W | Distributed |
| BITE and Diagnostics | 20 W | 20 W | ESS1 |
| **TOTAL** | **350 W** | **500 W** | — |

#### 2. Power Quality Requirements
| Parameter | Requirement | Standard Reference |
|-----------|-------------|-------------------|
| Steady-state voltage | 28 VDC ± 2 VDC | DO-160G Section 16 |
| Voltage transient | ≤ 80 V, ≤ 0.15 s | DO-160G Section 16 |
| Voltage spike | ≤ 600 V, ≤ 10 μs | DO-160G Section 16 |
| Ripple voltage | ≤ 1.5 Vpp | DO-160G Section 16 |
| Ground fault protection | Per DO-160G | DO-160G Section 16 |

#### 3. Bus Architecture Requirements
| Requirement | Specification |
|-------------|---------------|
| Primary supply | Essential Bus 1 (ESS1) |
| Backup supply | Essential Bus 2 (ESS2) |
| Automatic transfer | ≤ 50 ms switchover |
| Load shedding priority | Category 3 (maintained during normal operations) |
| Emergency operation | 30 minutes on backup battery |
| Ground power compatibility | Compatible with ground power unit (GPU) |

#### 4. Wiring and Distribution
| Parameter | Requirement |
|-----------|-------------|
| Wire gauge | 16-20 AWG per load (sized per current) |
| Cable shielding | Shielded twisted pair for sensor data |
| EMI protection | Per DO-160G Section 21 |
| Routing separation | Minimum 2 inches from high power cables |
| Connector type | MIL-DTL-38999 or equivalent |
| Wire identification | Per aircraft wiring standards |

## Verification Method

| Method | Description | Deliverable |
|--------|-------------|-------------|
| **Analysis** | Power budget analysis, load flow analysis | Analysis Report AR-24-SHM-001 |
| **Test** | Power quality testing, bus transfer testing | Test Report TR-24-SHM-001 |
| **Inspection** | Wiring installation inspection | Inspection Report IR-24-SHM-001 |

### Verification Activities
| Activity ID | Title | Type | Status |
|-------------|-------|------|--------|
| V&V-24-SHM-001 | SHM Power Budget Verification | Analysis | Planned |
| V&V-24-SHM-002 | Power Quality Testing | Test | Planned |
| V&V-24-SHM-003 | Bus Transfer Test | Test | Planned |
| V&V-24-SHM-004 | Emergency Power Endurance | Test | Planned |

## Traceability

### Parent Requirements
| Requirement | Title | Source |
|-------------|-------|--------|
| [53-00-03-01-005](../../../../../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions | Primary SHM Requirement |
| [CS-25.1351](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | General (Electrical Systems) | EASA CS-25 |
| [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Equipment, Systems, and Installations | EASA CS-25 |

### Related Requirements
| Requirement ID | Title | Relationship |
|----------------|-------|--------------|
| [53-00-03-07-002](../../../../../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/07_SHM_and_Monitoring/53-00-03-07-002_Data_Acquisition_Requirements.md) | Data Acquisition Requirements | Data system power needs |
| 24-00-03-01-001 | Electrical Load Analysis | System-wide load management |
| 24-00-03-02-001 | Essential Bus Requirements | Bus architecture |

### Interface Requirements
| Interface | Document | Content |
|-----------|----------|---------|
| SHM System | ICD-24-53-SHM-001 | Power interface specification |
| Avionics | ICD-24-42-001 | IMA power allocation |
| Maintenance System | ICD-24-45-001 | BITE power requirements |

## Assumptions and Constraints

### Assumptions
- SHM system operates continuously during flight and on ground (when power available)
- Power quality meets DO-160G Category A/B requirements
- Ground power unit provides equivalent power quality
- Battery backup sized for 30-minute emergency operation

### Constraints
| Parameter | Limit | Justification |
|-----------|-------|---------------|
| Total power allocation | 500 W maximum | Electrical load budget |
| Essential bus loading | ≤ 5% of bus capacity | System redundancy |
| Startup inrush current | ≤ 150% of nominal | Circuit breaker sizing |
| Operating temperature | -55°C to +70°C (equipment) | Standard avionics bay |

## Safety Impact
**Design Assurance Level (DAL)**: C (Major)

Loss of SHM power results in loss of continuous structural monitoring capability. The aircraft reverts to conventional inspection program, which is an acceptable degraded mode.

## Priority
**HIGH**

## Status
**DRAFT**

## Owner
Electrical Systems Engineering / SHM Integration

## Reviewers
| Role | Name | Status | Date |
|------|------|--------|------|
| Lead Reviewer | Electrical Systems Lead | Pending | — |
| SHM Integration | SHM Systems Lead | Pending | — |
| Power Management | Power Systems Engineer | Pending | — |

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
| File Path | `OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_24-ELECTRICAL_POWER/24-00_GENERAL/24-00-03_Requirements/SHM_Interface/` |
| Last AI Update | 2025-11-27 |

---
