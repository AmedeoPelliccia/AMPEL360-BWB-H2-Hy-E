# 42-00-03-07-001: IMA Resource Allocation for SHM

## Requirement ID
**42-00-03-07-001**

## Title
Integrated Modular Avionics Resource Allocation for SHM

## Category
07_SHM_Integration

## Description
The Integrated Modular Avionics (IMA) system shall provide computing resources and network connectivity for hosting SHM processing applications per ARINC 653 partitioning requirements.

## Resource Allocation

### Computing Resources
| Resource | Allocation | Notes |
|----------|------------|-------|
| CPU time | 40% of partition | SHM_CORE + SHM_PROC |
| RAM | 512 MB | Static allocation |
| Non-volatile storage | 1 GB | Configuration, baselines |
| I/O channels | 6 AFDX ports | Network interfaces |

### Partition Configuration
| Partition | MAF (ms) | Budget (ms) | Priority |
|-----------|----------|-------------|----------|
| SHM_MAIN | 20 | 8 | High |
| SHM_PROC | 50 | 15 | Medium |
| SHM_DISP | 100 | 5 | Low |
| SHM_BITE | 1000 | 10 | Background |

### Memory Allocation
| Segment | Size | Type | Access |
|---------|------|------|--------|
| Code | 64 MB | Flash | Execute |
| Static data | 128 MB | RAM | Read/Write |
| Dynamic data | 256 MB | RAM | Read/Write |
| I/O buffers | 64 MB | RAM | Read/Write |
| Configuration | 256 MB | NVM | Read/Write |

## Network Requirements

### AFDX Virtual Links
| VL ID | Source | Destination | BAG (ms) | Lmax (bytes) |
|-------|--------|-------------|----------|--------------|
| VL-SHM-01 | SHM | EICAS | 32 | 512 |
| VL-SHM-02 | SHM | FDR | 64 | 1024 |
| VL-SHM-03 | SHM | CMS | 64 | 2048 |
| VL-SHM-04 | ZC1 | SHM | 16 | 4096 |
| VL-SHM-05 | ZC2 | SHM | 16 | 4096 |
| VL-SHM-06 | ZC3 | SHM | 16 | 4096 |
| VL-SHM-07 | ZC4 | SHM | 16 | 4096 |
| VL-SHM-08 | ZC5 | SHM | 16 | 4096 |

### Network Redundancy
| Network | Function | Backup |
|---------|----------|--------|
| Network A | Primary data path | Automatic failover |
| Network B | Redundant path | Active standby |

## Software Hosting

### ARINC 653 Compliance
| Requirement | Implementation |
|-------------|----------------|
| Partition isolation | Hardware MMU + RTOS |
| Time partitioning | Cyclic scheduler |
| Health monitoring | Partition-level BITE |
| Inter-partition communication | Sampling/queuing ports |

### DO-178C Integration
| DAL | Application | Objectives |
|-----|-------------|------------|
| C | SHM_MAIN | Table A-4 |
| C | SHM_PROC | Table A-4 |
| D | SHM_DISP | Table A-5 |
| D | SHM_BITE | Table A-5 |

## Interface Specifications

### Sampling Ports (Input)
| Port | Data | Period (ms) |
|------|------|-------------|
| SP_ZC1_DATA | Zone 1 sensor data | 20 |
| SP_ZC2_DATA | Zone 2 sensor data | 20 |
| SP_ZC3_DATA | Zone 3 sensor data | 20 |
| SP_ZC4_DATA | Zone 4 sensor data | 20 |
| SP_ZC5_DATA | Zone 5 sensor data | 20 |
| SP_TEMP | Temperature data | 1000 |

### Sampling Ports (Output)
| Port | Data | Period (ms) |
|------|------|-------------|
| SP_STATUS | System status | 100 |
| SP_HEALTH | Health summary | 1000 |
| SP_ALERT | Active alerts | 100 |

### Queuing Ports
| Port | Direction | Message Size | Queue Depth |
|------|-----------|--------------|-------------|
| QP_CMD | Input | 64 bytes | 10 |
| QP_LOG | Output | 256 bytes | 100 |
| QP_EVENT | Output | 128 bytes | 50 |

## Acceptance Criteria

| # | Parameter | Requirement | Verification |
|---|-----------|-------------|--------------|
| 1 | CPU utilization | ≤40% | Test |
| 2 | Memory utilization | ≤512 MB | Analysis |
| 3 | Network bandwidth | ≤10% of VL capacity | Test |
| 4 | Partition deadline | 100% met | Test |
| 5 | Startup time | ≤30 seconds | Test |

## Traceability

### Parent Requirements
| Requirement | Title | Source |
|-------------|-------|--------|
| [53-00-03-01-005](../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions | Primary SHM Requirement |
| ARINC 653 | Avionics Application Software Standard Interface | IMA Standard |

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
