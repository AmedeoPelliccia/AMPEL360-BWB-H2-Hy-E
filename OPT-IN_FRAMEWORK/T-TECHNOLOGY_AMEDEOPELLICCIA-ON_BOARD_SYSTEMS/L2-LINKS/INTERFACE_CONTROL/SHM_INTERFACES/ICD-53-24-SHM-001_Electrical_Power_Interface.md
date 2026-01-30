# ICD-53-24-SHM-001: SHM Electrical Power Interface

## Document ID
**ICD-53-24-SHM-001**

## Title
Interface Control Document - SHM System to Electrical Power System

## Revision
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-11-27 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial release |

## Purpose
Define the electrical power interface between the Structural Health Monitoring (SHM) system (ATA 53) and the Electrical Power System (ATA 24).

## Scope
This ICD covers:
- Power supply requirements and allocation
- Bus assignments and distribution
- Circuit protection and load shedding
- Wiring and connector specifications

## Interface Participants

| Role | System | ATA | Owner |
|------|--------|-----|-------|
| Consumer | SHM System | 53 | SHM Systems |
| Provider | Electrical Power | 24 | Electrical Systems |

## Power Requirements

### Summary
| Parameter | Value |
|-----------|-------|
| Nominal power | 350 W |
| Peak power | 500 W |
| Voltage | 28 VDC |
| Primary bus | ESS1 |
| Backup bus | ESS2 |

### Load Distribution
| SHM Component | Nominal (W) | Peak (W) | Bus | Circuit |
|---------------|-------------|----------|-----|---------|
| Zone Controller 1 | 30 | 45 | ESS1 | CB-SHM-01 |
| Zone Controller 2 | 35 | 50 | ESS1 | CB-SHM-02 |
| Zone Controller 3 | 30 | 45 | ESS2 | CB-SHM-03 |
| Zone Controller 4 | 40 | 60 | ESS2 | CB-SHM-04 |
| Zone Controller 5 (H2) | 25 | 40 | ESS1 | CB-SHM-05 |
| Central Processing Unit | 80 | 120 | ESS1/ESS2 | CB-SHM-06/07 |
| Data Storage Module | 40 | 60 | ESS2 | CB-SHM-08 |
| Sensor Excitation | 50 | 60 | Distributed | CB-SHM-09 |
| BITE | 20 | 20 | ESS1 | CB-SHM-10 |

## Electrical Interface Specifications

### Power Input
| Parameter | Min | Nominal | Max | Unit |
|-----------|-----|---------|-----|------|
| Voltage (normal) | 26 | 28 | 30 | VDC |
| Voltage (emergency) | 22 | 24 | 28 | VDC |
| Ripple voltage | — | — | 1.5 | Vpp |
| Inrush current | — | — | 15 | A |
| Steady-state current | — | 12.5 | 18 | A |

### Power Quality
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Steady-state voltage | Per DO-160G Cat A | DO-160G §16 |
| Voltage transients | ≤ 80 V, ≤ 0.15 s | DO-160G §16 |
| Voltage spikes | ≤ 600 V, ≤ 10 μs | DO-160G §16 |
| Power interruption | ≤ 50 ms | DO-160G §16 |

## Bus Transfer Logic

### Automatic Transfer
| Condition | Action | Transfer Time |
|-----------|--------|---------------|
| ESS1 undervoltage (< 22 VDC) | Transfer to ESS2 | ≤ 50 ms |
| ESS1 overcurrent | Transfer to ESS2 | ≤ 20 ms |
| ESS2 undervoltage (< 22 VDC) | Maintain ESS1 | N/A |
| Both buses failed | Backup battery | ≤ 10 ms |

### Load Shedding
| Category | Shed Priority | Condition |
|----------|---------------|-----------|
| SHM continuous | Not shed | Normal operations |
| SHM acquisition | Category 3 | Emergency only |
| SHM BITE | Category 4 | Electrical emergency |

## Circuit Protection

### Circuit Breakers
| Circuit | Rating | Type | Panel Location |
|---------|--------|------|----------------|
| CB-SHM-01 | 3 A | Push-pull | P6 |
| CB-SHM-02 | 3 A | Push-pull | P6 |
| CB-SHM-03 | 3 A | Push-pull | P6 |
| CB-SHM-04 | 3 A | Push-pull | P6 |
| CB-SHM-05 | 3 A | Push-pull | P6 |
| CB-SHM-06 | 5 A | Push-pull | P6 |
| CB-SHM-07 | 5 A | Push-pull | P6 |
| CB-SHM-08 | 3 A | Push-pull | P6 |
| CB-SHM-09 | 5 A | Push-pull | P6 |
| CB-SHM-10 | 2 A | Push-pull | P6 |

## Wiring Specifications

### Wire Types
| Application | Wire Type | Gauge | Notes |
|-------------|-----------|-------|-------|
| Power mains | MIL-W-22759/16 | 16 AWG | High temp |
| Branch circuits | MIL-W-22759/16 | 20 AWG | High temp |
| Sensor power | MIL-W-22759/18 | 22 AWG | Shielded |

### Connectors
| Location | Type | Pin Count | Keying |
|----------|------|-----------|--------|
| Zone Controller (all) | MS3116F | 19 | Position A |
| CPU Power Input | MS3116F | 37 | Position B |
| Sensor Junction | MS3116F | 12 | Position C |

## Grounding Requirements

| Requirement | Specification |
|-------------|---------------|
| Ground reference | Aircraft structure |
| Ground path impedance | ≤ 2.5 mΩ per joint |
| Shield grounding | Single-point at CPU |
| Equipment bonding | Per MIL-B-5087B |

## EMI/EMC Requirements

| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Conducted emissions | Per DO-160G Cat L | DO-160G §21 |
| Conducted susceptibility | Per DO-160G Cat R | DO-160G §18 |
| Lightning protection | Per DO-160G Level 3 | DO-160G §22 |

## Traceability

### Parent Requirements
| Requirement | Title |
|-------------|-------|
| [53-00-03-01-005](../../A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md) | Compatibility with SHM Assumptions |
| [24-00-03-SHM-001](../../E2-ENERGY/ATA_24-ELECTRICAL_POWER/24-00_GENERAL/24-00-03_Requirements/SHM_Interface/24-00-03-SHM-001_SHM_Power_Requirements.md) | SHM Power Requirements |

## Verification

| Test | Method | Responsibility |
|------|--------|----------------|
| Power quality | Measurement | Electrical Systems |
| Bus transfer | Functional test | Systems Integration |
| Load shedding | Simulation | Systems Integration |
| EMI/EMC | DO-160G test | SHM Systems |

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
