# 85-00-13-H2-001: H₂ Infrastructure Subsystems Index

## Document Information

- **Document ID**: 85-00-13-H2-001
- **Title**: H₂ Infrastructure Subsystems Index
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

---

## 1. Introduction

This document provides a comprehensive index of all **hydrogen (H₂) infrastructure interface subsystems** for the AMPEL360 BWB aircraft. Each subsystem is documented with its purpose, components, interfaces, and integration points.

---

## 2. Subsystem Summary

| Subsystem ID | Name | Category | Status | ATA Chapters | Components |
|--------------|------|----------|--------|--------------|-----------|
| 85-H2-FUEL-001 | H₂ Fueling Interface | FUEL | Active | 28, 85 | 12 |
| 85-H2-VENT-001 | H₂ Vent Interface | VENT | Active | 28, 85 | 8 |
| 85-H2-SFTY-001 | H₂ Safety Monitoring | SFTY | Active | 26, 28, 85 | 15 |
| 85-H2-PURGE-001 | H₂ Purge Interface | PURGE | Active | 28, 85 | 6 |

---

## 3. Subsystem Details

### 3.1 H₂ Fueling Interface Subsystem (85-H2-FUEL-001)

**Purpose**: Provide safe, efficient interface for ground-based H₂ refueling.

**Key Components**:
- 85-RCPT-H2F-001-A: H₂ Fueling Receptacle (×2)
- 85-VALVE-H2F-005: H₂ Shutoff Valve (×2)
- 85-CTRL-H2F-020: Fueling Controller (×1)
- 85-SENS-H2F-030: Pressure Sensor (×2)
- 85-CABL-H2F-050: Wiring Harness (×1)

**Interfaces**:
- **ATA 28**: Connection to aircraft H₂ fuel tanks
- **ATA 24**: Electrical power for heaters, controls
- **ATA 45**: Fueling status telemetry
- **Ground**: H₂ fueling truck/dispenser

**Operational Requirements**:
- Fueling rate: Up to 10 kg/min per receptacle
- Pressure: 700 bar (10,150 psi) max
- Temperature range: -40°C to +85°C
- Safety interlocks: Grounding, leak detection, pressure monitoring

**Location**: Fwd Fuselage Station 450, starboard and port sides

**Related Documents**:
- [85-00-13-004_Interface_Hardware_Catalog.md](../85-00-13-004_Interface_Hardware_Catalog.md)
- [85-00-13-005_Configurable_Packages_and_Kits.md](../85-00-13-005_Configurable_Packages_and_Kits.md)

---

### 3.2 H₂ Vent Interface Subsystem (85-H2-VENT-001)

**Purpose**: Safely vent H₂ boil-off gas to atmosphere during ground operations.

**Key Components**:
- 85-CONN-H2V-001-A: H₂ Vent Coupling (×2)
- 85-VALVE-H2V-010: Vent Control Valve (×2)
- 85-SENS-H2V-020: Flow Sensor (×2)
- 85-FLTR-H2V-030: Flame Arrestor (×2)

**Interfaces**:
- **ATA 28**: Connection to H₂ tank vent lines
- **ATA 26**: Fire detection system
- **Ground**: Vent gas capture/dispersion system

**Operational Requirements**:
- Flow rate: Up to 50 L/min per vent
- Pressure: 10 bar (145 psi) max
- Flame arrestor rating: Prevents flashback
- Automatic closure on disconnect

**Location**: Aft Fuselage Station 850, starboard and port sides

---

### 3.3 H₂ Safety Monitoring Subsystem (85-H2-SFTY-001)

**Purpose**: Monitor for H₂ leaks and provide safety interlocks during ground operations.

**Key Components**:
- 85-SENS-H2S-010: H₂ Leak Sensor (×8)
- 85-SENS-SFTY-001: Fire/Smoke Detector (×4)
- 85-CTRL-H2S-040: Safety Controller (×2)
- 85-ALRM-H2S-050: Visual/Audible Alarm (×4)

**Interfaces**:
- **ATA 26**: Fire protection system integration
- **ATA 28**: Fuel system safety interlocks
- **ATA 45**: Safety telemetry and alerts
- **Ground**: Ground crew notification systems

**Operational Requirements**:
- H₂ detection: 0-4% by volume, <2s response time
- Alarm thresholds: 25% LEL (warning), 50% LEL (critical)
- Redundancy: Dual sensor coverage at critical points
- Fail-safe: System defaults to safe state on failure

**Location**: Multiple locations around H₂ receptacles and vent points

---

### 3.4 H₂ Purge Interface Subsystem (85-H2-PURGE-001)

**Purpose**: Enable pre-flight and post-flight purging of H₂ fuel system with inert gas.

**Key Components**:
- 85-CONN-H2P-001-A: Purge Gas Coupling (×2)
- 85-VALVE-H2P-010: Purge Control Valve (×2)
- 85-SENS-H2P-020: Purity Sensor (×2)

**Interfaces**:
- **ATA 28**: H₂ fuel system purge ports
- **Ground**: Nitrogen/helium purge gas supply

**Operational Requirements**:
- Purge gas: Nitrogen or helium (>99.9% purity)
- Pressure: 5 bar (73 psi) typical
- Purge verification: Oxygen content <0.5%, H₂ content <0.1%

**Location**: Adjacent to fueling receptacles, Station 450

---

## 4. Integration Matrix

| Subsystem | ATA 28 | ATA 24 | ATA 26 | ATA 45 | Ground Equipment |
|-----------|--------|--------|--------|--------|------------------|
| 85-H2-FUEL-001 | High | Medium | Low | Medium | H₂ Dispenser |
| 85-H2-VENT-001 | High | Low | Medium | Low | Vent Capture |
| 85-H2-SFTY-001 | Medium | Low | High | High | Safety Monitoring |
| 85-H2-PURGE-001 | High | Low | Low | Low | Purge Gas Supply |

---

## 5. Configuration Management

All H₂ infrastructure subsystems are tracked in:
- **Master Subsystem List**: [MASTER/85-00-13-M-001_Master_Subsystem_List.csv](../MASTER/85-00-13-M-001_Master_Subsystem_List.csv)
- **DPP System**: Each subsystem has unique DPP identifier
- **Digital Twin**: Real-time operational status and telemetry

---

## 6. References

### Internal

- [85-00-13-001_Subsystems_Components_Overview.md](../85-00-13-001_Subsystems_Components_Overview.md)
- [85-00-13-002_Subsystem_Master_Register.md](../85-00-13-002_Subsystem_Master_Register.md)
- [85-00-13-H2-002_H2_Infrastructure_Components_Index.md](./85-00-13-H2-002_H2_Infrastructure_Components_Index.md)

### External Standards

- **[SAE AS50881](https://www.sae.org/)** – Hydrogen fuel system components
- **[ISO 19881](https://www.iso.org/standard/66482.html)** – Gaseous hydrogen land vehicle fuel containers
- **[EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)** – Certification specifications

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
