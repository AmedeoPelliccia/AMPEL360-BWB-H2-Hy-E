# ICD-53-42-SHM-001: IMA Processing Interface

## Document ID
**ICD-53-42-SHM-001**

## Title
Interface Control Document - SHM System to IMA Processing

## Revision
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-11-27 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial release |

## Purpose
Define the interface between the SHM system and the Integrated Modular Avionics (IMA) platform for hosted application processing.

## Interface Participants

| Role | System | ATA | Owner |
|------|--------|-----|-------|
| Application | SHM Application | 53 | SHM Systems |
| Host Platform | IMA Cabinet | 42 | Avionics |

## ARINC 653 Interface

### Partition Configuration
| Partition | ID | Period (ms) | Duration (ms) |
|-----------|-----|-------------|---------------|
| SHM_MAIN | 0x10 | 20 | 8 |
| SHM_PROC | 0x11 | 50 | 15 |
| SHM_DISP | 0x12 | 100 | 5 |
| SHM_BITE | 0x13 | 1000 | 10 |

### Health Monitoring
| Level | Timeout | Action |
|-------|---------|--------|
| Partition | 100 ms | Restart partition |
| Process | 50 ms | Restart process |
| Deadline | 10 ms | Log and continue |

## Port Definitions

### Sampling Ports
| Port Name | Direction | Max Size | Period |
|-----------|-----------|----------|--------|
| SP_ZC1_IN | SOURCE | 4096 | 20 ms |
| SP_ZC2_IN | SOURCE | 4096 | 20 ms |
| SP_ZC3_IN | SOURCE | 4096 | 20 ms |
| SP_ZC4_IN | SOURCE | 4096 | 20 ms |
| SP_ZC5_IN | SOURCE | 4096 | 20 ms |
| SP_STATUS_OUT | DESTINATION | 256 | 100 ms |
| SP_HEALTH_OUT | DESTINATION | 512 | 1000 ms |

### Queuing Ports
| Port Name | Direction | Max Size | Queue Depth |
|-----------|-----------|----------|-------------|
| QP_CMD_IN | SOURCE | 64 | 10 |
| QP_ALERT_OUT | DESTINATION | 256 | 50 |
| QP_LOG_OUT | DESTINATION | 512 | 100 |

### Channel Definitions
| Channel | Source Partition | Dest Partition | Type |
|---------|------------------|----------------|------|
| CH_ZC_DATA | External | SHM_MAIN | Sampling |
| CH_STATUS | SHM_MAIN | External | Sampling |
| CH_ALERT | SHM_MAIN | SHM_DISP | Queuing |
| CH_PROC | SHM_MAIN | SHM_PROC | Queuing |

## AFDX Interface

### Virtual Link Configuration
| VL ID | BAG (ms) | Jitter (μs) | Lmax (bytes) |
|-------|----------|-------------|--------------|
| 1001 | 16 | 500 | 4096 |
| 1002 | 16 | 500 | 4096 |
| 1003 | 16 | 500 | 4096 |
| 1004 | 16 | 500 | 4096 |
| 1005 | 16 | 500 | 4096 |
| 1010 | 32 | 500 | 512 |
| 1011 | 64 | 500 | 2048 |

### End System Configuration
| ES ID | Network A | Network B | Partitions |
|-------|-----------|-----------|------------|
| ES_SHM | A1 | B1 | SHM_MAIN, SHM_PROC |

## Data Structures

### Zone Data Input
```c
typedef struct {
    uint32_t timestamp;           // UTC seconds
    uint16_t sensor_count;        // Active sensors
    uint16_t sample_count;        // Samples per sensor
    float    sample_rate;         // Hz
    uint8_t  data[4000];          // Sensor waveforms
} ZoneDataInput_t;
```

### Status Output
```c
typedef struct {
    uint32_t timestamp;           // UTC seconds
    uint8_t  system_status;       // 0=OK, 1=Degraded, 2=Failed
    uint8_t  zone_status[5];      // Per-zone status
    float    damage_index[5];     // Per-zone DI
    uint16_t active_alerts;       // Alert count
    uint16_t sensor_active;       // Active sensor count
    uint16_t sensor_failed;       // Failed sensor count
} StatusOutput_t;
```

### Alert Message
```c
typedef struct {
    uint32_t timestamp;           // UTC seconds
    uint16_t alert_id;            // Unique identifier
    uint8_t  alert_level;         // 1=Advisory, 2=Caution, 3=Warning
    uint8_t  zone_id;             // 1-5
    float    location_x;          // mm
    float    location_y;          // mm
    float    damage_index;        // 0-100
    char     description[64];     // Text description
} AlertMessage_t;
```

## Timing Requirements

| Parameter | Requirement |
|-----------|-------------|
| Data input latency | ≤ 10 ms |
| Processing time | ≤ 100 ms |
| Status output latency | ≤ 20 ms |
| Alert generation | ≤ 500 ms |
| End-to-end latency | ≤ 1 second |

## Error Handling

| Error | Detection | Response |
|-------|-----------|----------|
| Port timeout | Deadline monitor | Use stale data, set flag |
| Data corruption | CRC check | Discard, request retransmit |
| Partition failure | Health monitor | Restart, log event |
| Network failure | VL monitor | Switch to backup network |

## Verification

| Test | Method | Pass Criteria |
|------|--------|---------------|
| Port communication | Loopback test | All ports functional |
| Timing compliance | Timestamp analysis | Within requirements |
| Partition isolation | Fault injection | No cross-partition effect |
| Network redundancy | Failover test | Seamless switchover |

## Traceability

### Parent Requirements
| Requirement | Title |
|-------------|-------|
| [42-00-03-07-001](../../O-OPERATING_SYSTEMS/ATA_42-IMA_GOVERNANCE/42-00_GENERAL/42-00-03_Requirements/07_SHM_Integration/42-00-03-07-001_IMA_Resource_Allocation.md) | IMA Resource Allocation |
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
