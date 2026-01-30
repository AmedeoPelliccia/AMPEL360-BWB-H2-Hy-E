# ICD-53-57-SHM-001: Wing-Body Junction SHM Interface

## Document ID
**ICD-53-57-SHM-001**

## Title
Interface Control Document - Fuselage to Wing SHM at Wing-Body Junction

## Revision
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-11-27 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial release |

## Purpose
Define the structural health monitoring interface at the wing-body junction (WBJ), which is critical for the AMPEL360 Blended Wing Body (BWB) configuration.

## Scope
This ICD covers:
- Sensor network continuity across WBJ
- Signal routing and conditioning
- Data acquisition responsibility boundaries
- Physical interface specifications

## Interface Participants

| Role | System | ATA | Owner |
|------|--------|-----|-------|
| Fuselage SHM | Zone Controller 2 | 53 | SHM Systems |
| Wing SHM | Zone Controller 4 | 57 | SHM Systems |

## BWB Wing-Body Junction Characteristics

### Structural Definition
| Parameter | Value |
|-----------|-------|
| Junction type | Blended transition (no discrete joint) |
| Span location | ±3.5 m to ±8.0 m from centerline |
| Blend zone depth | 1.5 m chord transition |
| Primary material | CFRP (fuselage) to CFRP (wing) |
| Critical load path | Continuous skin + integrated stringers |

### Monitoring Zones
| Zone ID | Location | Responsibility |
|---------|----------|----------------|
| WBJ-UB | Upper blend (upper skin) | Shared 53/57 |
| WBJ-LB | Lower blend (lower skin) | Shared 53/57 |
| WBJ-FS | Forward spar carrythrough | ATA 53 |
| WBJ-RS | Rear spar carrythrough | ATA 53 |
| WBJ-WR | Wing root box | ATA 57 |

## Sensor Network Interface

### Sensor Continuity
| Sensor Type | Fuselage Side | Junction | Wing Side |
|-------------|---------------|----------|-----------|
| PZT guided wave | 5 sensors | 3 bridge sensors | 5 sensors |
| FBG strain | 4 channels | 2 bridge channels | 4 channels |

### Physical Layout
```
          FUSELAGE (ATA 53)                    WING (ATA 57)
   ┌─────────────────────────┐        ┌─────────────────────────┐
   │  P1  P2  P3  P4  P5     │◄──────►│     P6  P7  P8  P9  P10│
   │                         │  WBJ   │                         │
   │  F1  F2  F3  F4         │        │     F5  F6  F7  F8     │
   └─────────────────────────┘        └─────────────────────────┘
         Zone Controller 2                   Zone Controller 4

   P = PZT sensor
   F = FBG fiber
```

### Signal Path Allocation
| Signal Path | Sensors | Controller | Network Segment |
|-------------|---------|------------|-----------------|
| Path A (Upper) | P1-P5, F1-F2 | ZC2 | Fuselage network |
| Path B (Junction) | Bridge sensors | ZC2/ZC4 | Shared |
| Path C (Lower) | P6-P10, F5-F8 | ZC4 | Wing network |

## Data Acquisition Boundaries

### Responsibility Matrix
| Function | ATA 53 | Shared | ATA 57 |
|----------|--------|--------|--------|
| Sensor excitation (fuselage) | ● | | |
| Sensor excitation (wing) | | | ● |
| Junction monitoring | | ● | |
| Data collection (fuselage) | ● | | |
| Data collection (wing) | | | ● |
| Cross-boundary correlation | | ● | |
| Damage localization (blend zone) | | ● | |

### Data Exchange
| Data Type | Direction | Rate | Protocol |
|-----------|-----------|------|----------|
| Raw sensor data | ZC2 ↔ ZC4 | 1 MHz bursts | Time-synchronized |
| Processed health status | ZC2 → CPU | 1 Hz | AFDX |
| Processed health status | ZC4 → CPU | 1 Hz | AFDX |
| Cross-correlation data | ZC2 ↔ ZC4 | On-demand | Direct fiber |

## Physical Interface Specifications

### Wiring Harness
| Harness ID | Function | Conductors | Route |
|------------|----------|------------|-------|
| SHM-WBJ-01 | PZT excitation | 4 pair shielded | Junction forward |
| SHM-WBJ-02 | FBG interrogation | 2 fiber | Junction aft |
| SHM-WBJ-03 | Data sync | 2 pair + shield | Direct ZC-ZC |
| SHM-WBJ-04 | Power distribution | 4 wire | Via main harness |

### Connector Interface
| Connector ID | Type | Location | Pinout |
|--------------|------|----------|--------|
| J-WBJ-P01 | MS3116F-14S | Frame 34 | Per drawing |
| J-WBJ-P02 | MS3116F-10S | Frame 36 | Per drawing |
| J-WBJ-F01 | FC/APC optical | Frame 35 | N/A |

### Harness Break Points
| Break Point | Location | Access | Purpose |
|-------------|----------|--------|---------|
| BP-WBJ-01 | Frame 34 | Access panel | Maintenance |
| BP-WBJ-02 | Frame 36 | Access panel | Maintenance |
| BP-WBJ-03 | Wing root | Wing removal | Assembly |

## Signal Quality Requirements

### At Interface Boundary
| Parameter | Requirement |
|-----------|-------------|
| PZT signal attenuation | ≤ 6 dB across junction |
| PZT crosstalk | ≤ -40 dB between channels |
| FBG wavelength accuracy | ≤ 10 pm |
| Time synchronization | ≤ 1 μs |

### Temperature Effects
| Parameter | Compensation Method |
|-----------|---------------------|
| Material expansion | Temperature-indexed baseline |
| Sensor drift | Real-time temperature correction |
| Fiber wavelength | Thermal reference FBG |

## Verification Requirements

| Test | Description | Pass Criteria |
|------|-------------|---------------|
| Continuity test | End-to-end signal path | < 2 Ω per conductor |
| Signal transmission | PZT pulse response | ≤ 6 dB attenuation |
| Data sync | Time correlation | ≤ 1 μs difference |
| Coverage validation | Damage detection | Per POD requirements |

## Traceability

### Parent Requirements
| Requirement | Title |
|-------------|-------|
| [53-00-03-01-005](../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions |
| [57-00-03-07-001](../../A-AIRFRAME/ATA_57-WINGS/57-00_GENERAL/57-00-03_Requirements/07_SHM_and_Monitoring/57-00-03-07-001_Wing_SHM_Compatibility.md) | Wing SHM Compatibility |

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
