# 85-00-13-H2-002: H₂ Infrastructure Components Index

## Document Information

- **Document ID**: 85-00-13-H2-002
- **Title**: H₂ Infrastructure Components Index
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

---

## 1. Introduction

This document provides a detailed catalog of all **components** within H₂ infrastructure interface subsystems. Components are organized by family (receptacles, connectors, sensors, valves, etc.).

---

## 2. Component Summary

| Part Number | Name | Family | Subsystem | Status | Criticality |
|-------------|------|--------|-----------|--------|-------------|
| 85-RCPT-H2F-001-A | H₂ Fueling Receptacle | RCPT | 85-H2-FUEL-001 | Active | Critical |
| 85-CONN-H2V-001-A | H₂ Vent Coupling | CONN | 85-H2-VENT-001 | Active | Important |
| 85-SENS-H2S-010 | H₂ Leak Sensor | SENS | 85-H2-SFTY-001 | Active | Critical |
| 85-VALVE-H2F-005 | H₂ Shutoff Valve | VALVE | 85-H2-FUEL-001 | Active | Critical |
| 85-CTRL-H2F-020 | H₂ Fueling Controller | CTRL | 85-H2-FUEL-001 | Active | Important |

_(See complete listing in [MASTER/85-00-13-M-002_Master_Component_List.csv](../MASTER/85-00-13-M-002_Master_Component_List.csv))_

---

## 3. Component Details by Family

### 3.1 Receptacles (RCPT)

#### 85-RCPT-H2F-001-A: H₂ Fueling Receptacle Assembly

- **Manufacturer**: AeroConnect Systems (AC-H2R-350-001)
- **Material**: Stainless steel 316L body, PTFE seals
- **Weight**: 2.45 kg
- **Specifications**:
  - Pressure rating: 700 bar (10,150 psi)
  - Temperature range: -40°C to +85°C
  - Flow rate: Up to 10 kg/min H₂
  - Coupling: Quarter-turn bayonet with safety lock
  - Sealing: Metal-to-metal primary, elastomer backup
- **Safety Features**: Integrated pressure relief, breakaway coupling
- **Certifications**: EASA CS-25, SAE AS50881, ISO 19881
- **DPP Required**: Yes
- **Circularity Rating**: A (90%+ recyclable)
- **Maintenance**: Seal replacement every 5 years or 10,000 cycles

---

### 3.2 Connectors (CONN)

#### 85-CONN-H2V-001-A: H₂ Vent Coupling

- **Manufacturer**: AeroConnect Systems (AC-H2V-100-001)
- **Material**: Aluminum alloy 6061-T6, Viton seals
- **Weight**: 0.85 kg
- **Specifications**:
  - Pressure rating: 10 bar (145 psi)
  - Temperature range: -40°C to +85°C
  - Flow rate: Up to 50 L/min H₂ vapor
  - Coupling: Cam-lock quick-disconnect
- **Safety Features**: Flame arrestor, static bonding
- **Certifications**: EASA CS-25, SAE ARP5433
- **Maintenance**: Annual inspection, 7-year replacement

---

### 3.3 Sensors (SENS)

#### 85-SENS-H2S-010: H₂ Leak Detection Sensor

- **Manufacturer**: SafeSense Technologies (SS-H2-ECM-001)
- **Type**: Electrochemical H₂ sensor
- **Weight**: 0.35 kg
- **Specifications**:
  - Detection range: 0-4% H₂ by volume
  - Response time: <2 seconds to 50% LEL
  - Accuracy: ±5% of reading
  - Output: 4-20 mA analog + CAN-FD digital
  - Power: 12-28V DC, <500 mA
  - Environmental: IP67, -40°C to +85°C
- **Certifications**: ATEX Zone 1, IECEx, EASA CS-25.1309
- **Maintenance**: Quarterly functional test, 3-year replacement

---

### 3.4 Valves (VALVE)

#### 85-VALVE-H2F-005: H₂ Shutoff Valve

- **Manufacturer**: FlowControl Aerospace (FC-H2SV-700-001)
- **Type**: Pneumatic shutoff valve with manual override
- **Material**: Stainless steel 316L, PTFE seals
- **Weight**: 3.20 kg
- **Specifications**:
  - Pressure rating: 700 bar
  - Port size: 1/2" NPT
  - Actuation: Pneumatic (60-120 psi), manual override
  - Response time: <1 second full closure
  - Leak rate: <1×10⁻⁶ mbar·L/s (closed position)
- **Maintenance**: Annual calibration, 10-year overhaul

---

### 3.5 Controllers (CTRL)

#### 85-CTRL-H2F-020: H₂ Fueling Controller

- **Manufacturer**: AvionicsTech (AT-IFC-H2-001)
- **Type**: Embedded controller for fueling sequence
- **Material**: PCB, aluminum housing
- **Weight**: 1.15 kg
- **Specifications**:
  - Processor: ARM Cortex-M7 (400 MHz)
  - Memory: 2 MB Flash, 512 KB RAM
  - Interfaces: CAN-FD (5 Mbps), Ethernet (1 Gbps)
  - I/O: 16× digital input, 8× digital output, 8× analog input (4-20 mA)
  - Power: 12-28V DC, <5W
  - Environmental: -40°C to +85°C, IP65
- **Software**: Certified to DO-178C Level C
- **Maintenance**: Software updates per service bulletin

---

### 3.6 Seals & Consumables (SEAL)

#### 85-SEAL-H2F-001: H₂ Receptacle Seal Kit

- **Manufacturer**: SealTech (ST-H2SK-001)
- **Contents**: Primary seal (PTFE), backup seal (Viton), O-rings, lubricant
- **Weight**: 0.15 kg per kit
- **Specifications**:
  - Material: PTFE (primary), Viton (backup)
  - Temperature range: -40°C to +150°C
  - Pressure rating: 800 bar (design margin)
- **Replacement Interval**: 5 years or 10,000 cycles
- **Storage**: Cool, dry location; 10-year shelf life

---

### 3.7 Cables & Harnesses (CABL)

#### 85-CABL-H2F-050: H₂ System Wiring Harness

- **Manufacturer**: WirePro Aerospace (WP-WH-H2-001)
- **Type**: Shielded wiring harness for H₂ fueling interface
- **Material**: Copper conductors, PTFE insulation, braided shield
- **Weight**: 3.50 kg
- **Specifications**:
  - Conductor size: 16-22 AWG
  - Voltage rating: 600V
  - Temperature rating: -55°C to +200°C
  - Shield effectiveness: >60 dB (10 kHz - 1 GHz)
- **Connectors**: MIL-DTL-38999 (controller end), various (sensor ends)
- **Maintenance**: Visual inspection annually, 15-year service life

---

### 3.8 Mounting Hardware (MNTS)

#### 85-MNTS-H2F-100: Receptacle Mounting Bracket

- **Manufacturer**: StructureTech (ST-MB-H2R-001)
- **Material**: Aluminum alloy 7075-T6, anodized
- **Weight**: 1.20 kg
- **Specifications**:
  - Load capacity: 500 kg static, 200 kg dynamic
  - Mounting: 8× M8 bolts to fuselage structure
  - Finish: Type III hard anodize (black)
- **Certifications**: AS9100 certified manufacturing
- **Maintenance**: Visual inspection during C-check

---

## 4. Component Interchangeability

### Approved Alternates

| Primary Part | Alternate Part | Notes |
|--------------|----------------|-------|
| 85-RCPT-H2F-001-A | 85-RCPT-H2F-001-B | Variant B: Enhanced cold-weather performance |
| 85-SENS-H2S-010 | 85-SENS-H2S-011 | Alternate manufacturer (equivalent spec) |

All alternates require engineering approval and configuration management update.

---

## 5. Spare Parts Recommendations

Recommended spare parts inventory per 10 aircraft:

| Part Number | Description | Qty |
|-------------|-------------|-----|
| 85-SEAL-H2F-001 | H₂ Receptacle Seal Kit | 20 |
| 85-SENS-H2S-010 | H₂ Leak Sensor | 10 |
| 85-CONN-H2V-001-A | H₂ Vent Coupling | 5 |
| 85-VALVE-H2F-005 | H₂ Shutoff Valve | 3 |

See [85-00-13-005_Configurable_Packages_and_Kits.md](../85-00-13-005_Configurable_Packages_and_Kits.md) for spare kits.

---

## 6. References

### Internal

- [85-00-13-003_Component_Taxonomy_and_Coding.md](../85-00-13-003_Component_Taxonomy_and_Coding.md)
- [85-00-13-004_Interface_Hardware_Catalog.md](../85-00-13-004_Interface_Hardware_Catalog.md)
- [85-00-13-H2-001_H2_Infrastructure_Subsystems_Index.md](./85-00-13-H2-001_H2_Infrastructure_Subsystems_Index.md)
- [MASTER/85-00-13-M-002_Master_Component_List.csv](../MASTER/85-00-13-M-002_Master_Component_List.csv)

### External Standards

- **[SAE AS50881](https://www.sae.org/)** – H₂ fuel system components
- **[DO-178C](https://www.rtca.org/)** – Software certification
- **[AS9100](https://www.sae.org/)** – Quality management for aerospace

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
