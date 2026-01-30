# 31-00-03-07-001: SHM Display Requirements

## Requirement ID
**31-00-03-07-001**

## Title
SHM Display and Recording Integration Requirements

## Category
07_SHM_Integration

## Description
The indicating and recording system shall provide crew display interface for SHM status and alerts, and shall record SHM data for maintenance and trend analysis.

## Display Requirements

### EICAS Integration
| Function | Display Location | Format |
|----------|------------------|--------|
| System status | SYNOPTIC page | Graphic icon |
| Zone health | STATUS page | Zone status tiles |
| Active alerts | Message area | Text messages |
| BITE status | MAINTENANCE page | Status list |

### Message Format
| Alert Level | Color | Format |
|-------------|-------|--------|
| Advisory | Blue | "SHM: [Zone] [Status]" |
| Caution | Amber | "SHM CAUTION: [Description]" |
| Warning | Red | "SHM WARNING: [Description]" |

### Status Indications
| State | Symbol | Color | Description |
|-------|--------|-------|-------------|
| Normal | ● | Green | All sensors operative, no damage |
| Degraded | ◐ | Amber | Partial sensor failure |
| Alert | ◉ | Amber | Potential damage detected |
| Failed | ○ | Red | Zone inoperative |

## Recording Requirements

### Flight Data Recording
| Parameter | Sample Rate | Resolution |
|-----------|-------------|------------|
| SHM system status | 1 Hz | Discrete |
| Zone health status | 1 Hz | Discrete (5 zones) |
| Active alert count | 1 Hz | Integer |
| Damage index (max) | 1 Hz | Float, 0-100 |
| Sensor count active | 0.1 Hz | Integer |

### Quick Access Recorder (QAR)
| Data | Recording Rate | Format |
|------|----------------|--------|
| Processed health summary | 1 Hz | Structured data |
| Alert history | Event-driven | Log entries |
| Sensor statistics | Per flight | Summary file |
| Baseline quality | Per flight | Quality metrics |

### Maintenance Data Recording
| Data | Storage Location | Retention |
|------|------------------|-----------|
| Raw sensor data | Onboard SSD | 30 days |
| Processed results | Onboard SSD | 1 year |
| Alert log | Nonvolatile | Permanent |
| BITE log | Nonvolatile | 90 days |

## Interface Specifications

### ARINC 429 Output (to EICAS)
| Label | Parameter | Rate |
|-------|-----------|------|
| 270 | SHM status word 1 | 12.5 Hz |
| 271 | SHM status word 2 | 12.5 Hz |
| 272 | Alert word | 12.5 Hz |
| 273 | Zone 1 DI | 12.5 Hz |
| 274 | Zone 2 DI | 12.5 Hz |
| 275 | Zone 3 DI | 12.5 Hz |
| 276 | Zone 4 DI | 12.5 Hz |
| 277 | Zone 5 DI | 12.5 Hz |

### AFDX Output (to FDR/QAR)
| VL | Data | Rate |
|----|------|------|
| VL-SHM-10 | Status summary | 1 Hz |
| VL-SHM-11 | Alert data | Event-driven |
| VL-SHM-12 | Processed results | 0.1 Hz |

## Acceptance Criteria

| # | Parameter | Requirement | Verification |
|---|-----------|-------------|--------------|
| 1 | Status update rate | ≤1 second | Test |
| 2 | Alert display latency | ≤500 ms | Test |
| 3 | Recording integrity | 100% | Test |
| 4 | Data retention | Per specification | Analysis |

## Traceability

### Parent Requirements
| Requirement | Title | Source |
|-------------|-------|--------|
| [53-00-03-01-005](../../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions | Primary SHM Requirement |
| CS-25.1301 | Function and Installation | EASA CS-25 |
| CS-25.1541 | General (Markings and Placards) | EASA CS-25 |

## Priority
**HIGH**

## Status
**DRAFT**

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
