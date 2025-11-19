# 95-60-00-001 Storages Overview

**Document ID:** 95-60-00-001  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

---

## 1. Purpose

This document provides a comprehensive overview of all storage systems within the AMPEL360 BWB H₂ Hy-E aircraft. Storages encompass physical vessels, reservoirs, tanks, accumulators, buffers, and digital/data storage facilities critical to aircraft operations.

---

## 2. Scope

The 95-60 Storages chapter documents all storage systems across multiple ATA chapters, including:

- **Physical Storages**: Tanks, reservoirs, vessels, accumulators, and buffers for fluids, gases, thermal energy, and mechanical energy
- **Energy Storages**: Electrical batteries, hydrogen storage, hydraulic accumulators, and CO₂ battery systems
- **Data Storages**: Flight data recorders (FDR), cockpit voice recorders (CVR), onboard data hubs, and digital infrastructure
- **Service Storages**: Water/waste tanks, APU fuel storages, and other auxiliary systems

---

## 3. Storage Categories

### 3.1 Energy Storages

| Storage Type | ATA | Primary Function | Typical Capacity |
|-------------|-----|------------------|------------------|
| Electrical (Battery/Supercaps) | 24, 80 | DC bus energy buffer | 500+ kWh |
| Hydrogen (LH₂ tanks) | 28 | Primary fuel storage | 1,000+ kg H₂ |
| Hydraulic (Accumulators) | 29 | Pressure buffering | 5-20 L @ 3000 psi |
| Thermal (ECS) | 21 | Temperature regulation | Variable |
| CO₂ Battery System | 80 | Closed-loop energy storage | 500+ kWh |

### 3.2 Fluid and Gas Storages

| Storage Type | ATA | Primary Function | Typical Capacity |
|-------------|-----|------------------|------------------|
| Potable Water | 38 | Passenger/crew water supply | 200-400 L |
| Waste Water (grey/black) | 38 | Waste collection | 150-300 L |
| Hydraulic Fluid Reservoirs | 29 | System fluid supply | 10-50 L |
| Thermal Fluid Buffers | 21 | ECS thermal management | Variable |

### 3.3 Data and Digital Storages

| Storage Type | ATA | Primary Function | Typical Capacity |
|-------------|-----|------------------|------------------|
| FDR/CVR | 31 | Flight data recording | 25+ hours |
| Onboard Data Hubs | 31 | Operational data buffering | 1-10 TB |
| Digital Infrastructure | 46 | Data lake/warehouse/registry | 100+ TB |
| Model Artifacts | 46 | AI/ML model storage | Variable |

### 3.4 Propulsion and Auxiliary Storages

| Storage Type | ATA | Primary Function | Typical Capacity |
|-------------|-----|------------------|------------------|
| APU Fuel Storage | 49 | APU fuel supply | 50-100 L |
| APU Oil Storage | 49 | Lubrication | 5-10 L |
| Propulsion Energy Buffers | 70 | Spool/mechanical buffering | Variable |

---

## 4. Cross-ATA Integration

Storage systems integrate across multiple ATA chapters:

```
95-60_Storages (This Chapter)
     ├── Links to Physical Systems (ATA 21, 24, 28, 29, 31, 38, 49, 70, 80)
     ├── Links to 95-20_Subsystems (component-level details)
     ├── Links to 95-30_Circularity (lifecycle, maintenance, reuse)
     ├── Links to 95-50_Structures (mounting, integration)
     └── Links to 95-40_Software (monitoring, control, CAOS integration)
```

---

## 5. Traceability and Monitoring

All storage systems are monitored through:

- **Health Monitoring**: SOH (State of Health), SOE (State of Energy), SOC (State of Charge)
- **Safety Limits**: Pressure, temperature, level, contamination thresholds
- **CAOS Integration**: AI-powered predictive maintenance and optimization
- **Digital Twin**: Real-time monitoring and simulation

---

## 6. Storage Registry

A comprehensive storage registry is maintained at:
- **File**: `00_META/95-60-00-006_Storages_Registry.json`
- **Contents**: ID, ATA chapter, location, capacity, criticality, monitoring points

---

## 7. Naming Convention

Storage documentation follows the pattern:

```
95-60-{ATA}-{SEQ}_{Description}.md
```

Where:
- `95-60`: Storage chapter identifier
- `{ATA}`: Two-digit ATA chapter (21, 24, 28, 29, 31, 38, 46, 49, 70, 80)
- `{SEQ}`: Three-digit sequence number (001, 002, etc.)
- `{Description}`: Descriptive name in PascalCase

---

## 8. Related Documents

- **[95-60-00-002](95-60-00-002_Storage_Taxonomy_and_Scope.md)**: Storage taxonomy and classification
- **[95-60-00-003](95-60-00-003_Cross_ATA_Storages_Map.csv)**: Cross-ATA storage mapping
- **[00_META](00_META/)**: Metadata, registries, and traceability matrices

---

## 9. Maintenance and Updates

This document is maintained by the AMPEL360 Documentation Working Group and updated as storage systems evolve throughout the aircraft lifecycle.

**Last Review:** 2025-11-17  
**Next Review:** 2026-05-17  
**Owner:** AMPEL360 Systems Engineering

---

**Document Control**
- **Standard**: OPT-IN Framework v1.5
- **Classification**: Technical Documentation
- **Distribution**: Unrestricted (Open Source)
