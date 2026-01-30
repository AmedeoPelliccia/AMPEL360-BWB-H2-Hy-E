# ICD-53-31-SHM-001: SHM Display Recording Interface

## Document ID
**ICD-53-31-SHM-001**

## Title
Interface Control Document - SHM System to Indicating/Recording Systems

## Revision
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-11-27 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial release |

## Purpose
Define the interface between the SHM system (ATA 53) and the Indicating/Recording systems (ATA 31) for crew display and flight data recording.

## Interface Participants

| Role | System | ATA | Owner |
|------|--------|-----|-------|
| Data Provider | SHM System | 53 | SHM Systems |
| Display Consumer | EICAS | 31 | Avionics |
| Recording Consumer | FDR/QAR | 31 | Avionics |

## Display Interface

### ARINC 429 Bus Assignment
| Bus | Function | Direction |
|-----|----------|-----------|
| SHM_A429_1 | Status to EICAS L | SHM → EICAS |
| SHM_A429_2 | Status to EICAS R | SHM → EICAS |

### Label Definitions
| Label (Octal) | Parameter | SSM | SDI | Bits | Units |
|---------------|-----------|-----|-----|------|-------|
| 270 | SHM Status Word 1 | Normal | ALL | 11-29 | Discrete |
| 271 | SHM Status Word 2 | Normal | ALL | 11-29 | Discrete |
| 272 | Alert Status | Normal | ALL | 11-29 | Discrete |
| 273 | Zone 1 Damage Index | Normal | ALL | 11-29 | 0-100 |
| 274 | Zone 2 Damage Index | Normal | ALL | 11-29 | 0-100 |
| 275 | Zone 3 Damage Index | Normal | ALL | 11-29 | 0-100 |
| 276 | Zone 4 Damage Index | Normal | ALL | 11-29 | 0-100 |
| 277 | Zone 5 Damage Index | Normal | ALL | 11-29 | 0-100 |

### Status Word 1 Bit Assignments
| Bit | Parameter | 0 State | 1 State |
|-----|-----------|---------|---------|
| 11 | System power | Off | On |
| 12 | Zone 1 status | Failed | Operative |
| 13 | Zone 2 status | Failed | Operative |
| 14 | Zone 3 status | Failed | Operative |
| 15 | Zone 4 status | Failed | Operative |
| 16 | Zone 5 status | Failed | Operative |
| 17 | BITE status | Fail | Pass |
| 18-21 | Active fault count | Binary (0-15) | |
| 22-29 | Reserved | | |

### Status Word 2 Bit Assignments
| Bit | Parameter | 0 State | 1 State |
|-----|-----------|---------|---------|
| 11 | Advisory active | No | Yes |
| 12 | Caution active | No | Yes |
| 13 | Warning active | No | Yes |
| 14 | Structural alert | No | Yes |
| 15 | Sensor degraded | No | Yes |
| 16 | Baseline valid | Invalid | Valid |
| 17 | Temperature comp active | No | Yes |
| 18-29 | Reserved | | |

## Recording Interface

### AFDX to FDR/QAR
| VL ID | Content | BAG (ms) | Lmax |
|-------|---------|----------|------|
| VL-SHM-10 | Status summary | 1000 | 256 |
| VL-SHM-11 | Alert data | 100 | 512 |
| VL-SHM-12 | Processed results | 1000 | 1024 |

### Data Frame Format (VL-SHM-10)
| Byte | Content | Format |
|------|---------|--------|
| 0-3 | Timestamp | UTC seconds |
| 4 | System status | Bit field |
| 5-9 | Zone status (5 bytes) | Per zone |
| 10-11 | Active sensor count | Uint16 |
| 12-13 | Failed sensor count | Uint16 |
| 14-17 | Max damage index | Float32 |
| 18-21 | Last alert time | UTC seconds |
| 22-255 | Reserved | |

### Recording Requirements
| Parameter | Sample Rate | Retention |
|-----------|-------------|-----------|
| System status | 1 Hz | FDR: 25 hours |
| Zone status | 1 Hz | FDR: 25 hours |
| Damage index | 1 Hz | FDR: 25 hours |
| Alert events | Event | FDR: 25 hours |
| Raw data | Per flight | QAR: 30 days |

## Message Interface

### Alert Message Format
| Field | Size | Description |
|-------|------|-------------|
| Message ID | 2 | Unique alert identifier |
| Timestamp | 4 | UTC seconds |
| Alert level | 1 | 1=Advisory, 2=Caution, 3=Warning |
| Zone ID | 1 | 1-5 |
| Location | 8 | X, Y coordinates |
| Damage index | 4 | Float, 0-100 |
| Message text | 64 | Alert description |

### Standard Alert Messages
| ID | Level | Text |
|----|-------|------|
| 0001 | Advisory | "SHM: Zone [X] sensor degraded" |
| 0002 | Advisory | "SHM: Baseline update required" |
| 0010 | Caution | "SHM CAUTION: Potential damage Zone [X]" |
| 0011 | Caution | "SHM CAUTION: Zone [X] multiple alerts" |
| 0020 | Warning | "SHM WARNING: Structural damage detected" |

## Verification

| Test | Method | Pass Criteria |
|------|--------|---------------|
| Label transmission | Bus analyzer | All labels present at rate |
| Data accuracy | Simulation | Values match source |
| Alert display | Demonstration | Correct format and timing |
| Recording integrity | Playback | 100% data recovery |

## Traceability

### Parent Requirements
| Requirement | Title |
|-------------|-------|
| [31-00-03-07-001](../../D-DATA/ATA_31-INDICATING_RECORDING/31-00_GENERAL/31-00-03_Requirements/07_SHM_Integration/31-00-03-07-001_SHM_Display_Requirements.md) | SHM Display Requirements |
| [53-00-03-01-005](../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions |

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| Last AI Update | 2025-11-27 |

---
