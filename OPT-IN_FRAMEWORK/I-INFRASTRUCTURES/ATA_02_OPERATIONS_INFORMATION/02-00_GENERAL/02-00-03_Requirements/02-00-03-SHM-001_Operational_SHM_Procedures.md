# 02-00-03-SHM-001: Operational SHM Procedures (Enhanced)

| Field | Value |
|-------|-------|
| **Document ID** | 02-00-03-SHM-001 |
| **Version** | 2.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | OPERATIONS / PROCEDURES |
| **ATA Chapter** | 02 (Operations Information) |
| **Aircraft** | AMPEL360 BWB H2 Hy-E Q100 |

---

## Title
Operational Procedures for Structural Health Monitoring

## Purpose
Define operational procedures for flight crews and ground personnel regarding the SHM system during normal operations, abnormal conditions, and maintenance activities.

## Flight Crew Procedures

### Pre-Flight
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify SHM status on EICAS | SHM READY displayed |
| 2 | Check for SHM messages in CMC | No active faults |
| 3 | Review last flight SHM summary | No structural alerts |
| 4 | Verify sensor BITE status | All zones green |

### In-Flight Monitoring
| Display | Location | Update Rate |
|---------|----------|-------------|
| SHM status | EICAS synoptic | 1 Hz |
| Zone health | MFD status page | 1 Hz |
| Active alerts | EICAS message | Immediate |
| Trend data | Not displayed | Ground only |

### Alert Response
| Alert Level | Indication | Crew Action |
|-------------|------------|-------------|
| Advisory | Blue SHM message | Log and monitor |
| Caution | Amber SHM CAUTION | Run QRH checklist |
| Warning | Red SHM WARN | Follow emergency procedure |

### QRH Checklist: SHM CAUTION
```
SHM CAUTION
1. Verify structural integrity via other means (vibration, noise)
2. If abnormal indications confirmed:
   - Reduce airspeed to VA max
   - Limit altitude to FL350
   - Plan diversion if severe
3. Contact dispatch for engineering assessment
4. Log all observations for maintenance
```

## Ground Operations

### Post-Flight Download
| Step | Action | Responsibility |
|------|--------|----------------|
| 1 | Connect ground data loader | Line maintenance |
| 2 | Initiate SHM data download | Automatic |
| 3 | Verify download complete | Ground crew |
| 4 | Review quick-look summary | Maintenance control |
| 5 | Forward for engineering analysis | If required |

### Scheduled Checks
| Check | Interval | Actions |
|-------|----------|---------|
| Transit | Each flight | Visual BITE check |
| Daily | 24 hours | Full BITE execution |
| Weekly | 7 days | Baseline validation |
| A-Check | Per MPD | Sensor inspection |
| C-Check | Per MPD | Full system test |

## Dispatch Procedures

### MEL Provisions
| Item | Relief | Dispatch Condition |
|------|--------|---------------------|
| SHM system inoperative | 10 days | Per normal inspection program |
| Single zone inoperative | 30 days | Remaining zones operative |
| Single sensor failed | No limit | Coverage maintained |
| Data link inoperative | 3 days | On-board storage available |

### Engineering Consultation
| Condition | Contact | Response Time |
|-----------|---------|---------------|
| Structural alert (flight) | OCC Engineering | Immediate |
| Structural alert (ground) | Maintenance control | 2 hours |
| System degradation | Engineering support | 24 hours |
| Data quality issue | SHM support | 48 hours |

## Abnormal Procedures

### Suspected Structural Event
1. Flight crew reports unusual vibration or noise
2. Maintenance reviews SHM data for corresponding events
3. Engineering assesses data against detection thresholds
4. If positive: initiate detailed inspection
5. If negative: document and continue monitoring

### SHM False Alarm Management
1. Identify alert source (sensor, zone, algorithm)
2. Review environmental conditions at time of alert
3. Compare with historical baselines
4. Classify as confirmed damage or false positive
5. Update false alarm database for algorithm tuning

## Training Requirements

| Role | Training Module | Recurrency |
|------|-----------------|------------|
| Flight crew | SHM awareness | Initial + annual |
| Dispatch | SHM MEL procedures | Initial + biennial |
| Line maintenance | SHM BITE operations | Initial + annual |
| Heavy maintenance | Full SHM maintenance | Initial + biennial |

## Traceability
- Parent Requirement: [53-00-03-01-005](../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md)

---

## Document Control

| Field | Value |
|-------|-------|
| Version | 2.0 |
| Classification | OPERATIONS / PROCEDURES |
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| Last AI Update | 2025-11-27 |

---
