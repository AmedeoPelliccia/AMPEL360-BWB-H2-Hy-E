# 53-00-01-SHM-001: SHM Architecture Overview

## Document ID
**53-00-01-SHM-001**

## Title
Structural Health Monitoring System Architecture Overview

## Purpose
Provide a comprehensive overview of the SHM system architecture for the AMPEL360 BWB aircraft fuselage structure.

## System Architecture

### Overview
The SHM system employs a distributed architecture with zone-based data acquisition and centralized processing to monitor structural health across the aircraft fuselage.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SHM SYSTEM ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│   │ Zone 1   │  │ Zone 2   │  │ Zone 3   │  │ Zone 4   │  │ Zone 5   ││
│   │ Forward  │  │ Center   │  │ Aft      │  │ Wings    │  │ H2 Zone  ││
│   │ Fuselage │  │ Fuselage │  │ Fuselage │  │          │  │          ││
│   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘│
│        │             │             │             │             │       │
│   ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐│
│   │   ZC1    │  │   ZC2    │  │   ZC3    │  │   ZC4    │  │   ZC5    ││
│   │(30W/45W) │  │(35W/50W) │  │(30W/45W) │  │(40W/60W) │  │(25W/40W) ││
│   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘│
│        │             │             │             │             │       │
│        └─────────────┼─────────────┼─────────────┼─────────────┘       │
│                      │             │             │                     │
│                      │     ┌───────┴───────┐     │                     │
│                      └────►│  AFDX NETWORK │◄────┘                     │
│                            └───────┬───────┘                           │
│                                    │                                   │
│                            ┌───────┴───────┐                           │
│                            │     CPU       │                           │
│                            │  (80W/120W)   │                           │
│                            └───────┬───────┘                           │
│                                    │                                   │
│                            ┌───────┴───────┐                           │
│                            │ Data Storage  │                           │
│                            │  (40W/60W)    │                           │
│                            └───────────────┘                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Sensor Technologies
| Technology | Application | Quantity | Data Type |
|------------|-------------|----------|-----------|
| Piezoelectric (PZT) | Guided wave damage detection | ~500 | Active pulse-echo |
| Fiber Bragg Grating (FBG) | Strain monitoring | ~200 channels | Passive strain |
| Acoustic Emission (AE) | Damage growth detection | ~50 | Passive event |
| Comparative Vacuum (CVM) | Fatigue crack detection | ~100 | Vacuum differential |

### Zone Configuration
| Zone | Location | Sensor Count | Priority Areas |
|------|----------|--------------|----------------|
| Zone 1 | Forward fuselage (Frames 1-20) | 80 PZT, 30 FBG | Pressure bulkhead, nose gear |
| Zone 2 | Center fuselage (Frames 21-50) | 120 PZT, 60 FBG | Wing-body junction, doors |
| Zone 3 | Aft fuselage (Frames 51-80) | 80 PZT, 40 FBG | Empennage attach, APU |
| Zone 4 | Wings | 120 PZT, 50 FBG | Root box, carry-through |
| Zone 5 | H2 cryogenic zone | 60 FBG, 40 PZT | Tank supports, interfaces |

### Data Flow
| Stage | Function | Output |
|-------|----------|--------|
| Acquisition | Sensor excitation/response capture | Raw waveforms |
| Preprocessing | Filtering, baseline subtraction | Normalized signals |
| Feature extraction | Damage indices calculation | Feature vectors |
| Detection algorithm | Pattern recognition, ML classification | Health assessment |
| Reporting | Alert generation, trending | Crew/maintenance messages |

## Interface Summary
| System | Interface Type | Protocol |
|--------|----------------|----------|
| Electrical (ATA 24) | Power | 28 VDC, 350W |
| IMA (ATA 42) | Processing | AFDX |
| CMS (ATA 45) | Maintenance data | ARINC 624 |
| Displays (ATA 31) | Crew alerting | ARINC 429 |
| Ground (ATA 46) | Data offload | ARINC 615A |

## Traceability
- Parent Requirement: [53-00-03-01-005](../53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md)

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
