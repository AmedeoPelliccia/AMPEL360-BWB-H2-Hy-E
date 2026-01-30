# ICD-53-45-SHM-001: SHM CMS Maintenance Interface

## Document ID
**ICD-53-45-SHM-001**

## Title
Interface Control Document - SHM System to Central Maintenance System

## Revision
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-11-27 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial release |

## Purpose
Define the data interface between the Structural Health Monitoring (SHM) system (ATA 53) and the Central Maintenance System (CMS) (ATA 45).

## Scope
This ICD covers:
- Status and fault message interface
- Maintenance data transfer
- Ground data loading interface
- BITE integration

## Interface Participants

| Role | System | ATA | Owner |
|------|--------|-----|-------|
| Data Provider | SHM System | 53 | SHM Systems |
| Data Consumer | Central Maintenance System | 45 | Maintenance Systems |

## Message Interface

### Message Categories
| Category | Direction | Protocol | Rate |
|----------|-----------|----------|------|
| Status messages | SHM → CMS | ARINC 624 | 1 Hz |
| Fault messages | SHM → CMS | ARINC 624 | On event |
| Configuration data | CMS → SHM | ARINC 615A | On demand |
| Diagnostic requests | CMS → SHM | ARINC 624 | On demand |
| Trend data | SHM → CMS | ARINC 624 | 0.1 Hz |

### Status Message Format (ARINC 624)
| Field | Size | Description |
|-------|------|-------------|
| Message ID | 2 bytes | SHM-STATUS-001 |
| Timestamp | 4 bytes | UTC seconds |
| System status | 1 byte | Overall health (0-3) |
| Zone status[5] | 5 bytes | Per-zone health |
| Sensor count active | 2 bytes | Number of active sensors |
| Sensor count failed | 2 bytes | Number of failed sensors |
| Last damage event | 4 bytes | Timestamp of last detection |
| CRC | 2 bytes | Data integrity |

### Fault Message Format (ARINC 624)
| Field | Size | Description |
|-------|------|-------------|
| Message ID | 2 bytes | SHM-FAULT-XXX |
| Timestamp | 4 bytes | UTC seconds |
| Fault code | 4 bytes | Per fault code table |
| Fault location | 4 bytes | Zone/sensor ID |
| Fault severity | 1 byte | 1=Advisory, 2=Caution, 3=Warning |
| Fault data | 16 bytes | Context-dependent |
| Recommended action | 4 bytes | Action code |
| CRC | 2 bytes | Data integrity |

### Fault Code Table
| Range | Category | Example |
|-------|----------|---------|
| 1000-1999 | Sensor faults | 1001 = PZT sensor open |
| 2000-2999 | DAQ faults | 2001 = Zone controller comm loss |
| 3000-3999 | Processing faults | 3001 = Algorithm timeout |
| 4000-4999 | Power faults | 4001 = Undervoltage |
| 5000-5999 | Communication faults | 5001 = Network timeout |
| 6000-6999 | Structural alerts | 6001 = Damage detected |

## Maintenance Action Interface

### Action Codes
| Code | Action | Urgency |
|------|--------|---------|
| MA-SHM-001 | Inspect sensor installation | Next A-check |
| MA-SHM-002 | Replace sensor | Next C-check |
| MA-SHM-003 | Recalibrate sensor network | Within 10 flights |
| MA-SHM-004 | Download diagnostic data | Before next flight |
| MA-SHM-005 | Verify structural integrity | Immediate |
| MA-SHM-006 | Update baseline | After repair |

### Troubleshooting Tree Reference
| Fault Category | TSM Reference |
|----------------|---------------|
| Sensor faults | TSM-53-80-00 |
| DAQ faults | TSM-53-80-10 |
| Processing faults | TSM-53-80-20 |
| Power faults | TSM-53-80-30 |
| Communication faults | TSM-53-80-40 |

## Ground Data Interface

### Data Download (ARINC 615A)
| Data Type | Size (typical) | Format |
|-----------|----------------|--------|
| Sensor raw data | 500 MB/flight | Binary |
| Processed results | 10 MB/flight | XML |
| Trend data | 1 MB/flight | CSV |
| Configuration | 100 KB | XML |
| BITE logs | 5 MB | Text |

### Data Upload (ARINC 615A)
| Data Type | Size (typical) | Format |
|-----------|----------------|--------|
| Baseline update | 200 MB | Binary |
| Algorithm update | 50 MB | Binary |
| Configuration | 100 KB | XML |
| Threshold tables | 10 KB | XML |

### Transfer Specifications
| Parameter | Requirement |
|-----------|-------------|
| Transfer rate | ≥ 10 Mbps |
| Protocol | ARINC 615A Part 3 |
| Security | Encrypted (AES-256) |
| Authentication | Certificate-based |
| Integrity | SHA-256 checksum |

## BITE Integration

### BITE Levels
| Level | Scope | Trigger |
|-------|-------|---------|
| Continuous | Power, comm, sensor response | Automatic |
| Initiated | Full self-test | Crew/maintenance |
| Ground | Extended diagnostics | Maintenance only |

### BITE Status to CMS
| Status | CMS Display | Action |
|--------|-------------|--------|
| BITE Pass | Green | None |
| BITE Degraded | Amber | Review at next check |
| BITE Fail | Red | Troubleshoot |
| BITE Not Complete | Gray | Initiate test |

## Physical Interface

### Network Connection
| Parameter | Specification |
|-----------|---------------|
| Physical | AFDX port |
| Speed | 100 Mbps |
| VL assignment | VL-SHM-01 through VL-SHM-05 |
| Connector | M12 (D-coded) |

### Discrete Signals
| Signal | Direction | Function |
|--------|-----------|----------|
| SHM_VALID | SHM → CMS | Data validity |
| SHM_FAIL | SHM → CMS | System failure indication |
| BITE_REQ | CMS → SHM | BITE initiation request |

## Traceability

### Parent Requirements
| Requirement | Title |
|-------------|-------|
| [53-00-03-01-005](../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions |
| [45-00-03-SHM-001](../../I-INFORMATION_INTELLIGENCE_INTERFACES/ATA_45-ONBOARD_MAINTENANCE_SYSTEMS/45-00_GENERAL/45-00-03_Requirements/SHM_Integration/45-00-03-SHM-001_SHM_CMS_Integration.md) | SHM CMS Integration Requirements |

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Human Approver | _[to be completed]_ |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| Last AI Update | 2025-11-27 |

---
