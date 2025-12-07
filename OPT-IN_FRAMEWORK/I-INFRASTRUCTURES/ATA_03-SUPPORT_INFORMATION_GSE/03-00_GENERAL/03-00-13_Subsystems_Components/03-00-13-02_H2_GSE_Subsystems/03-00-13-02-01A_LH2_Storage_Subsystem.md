---
Title: "LH₂ Storage Subsystem — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-13-02-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Detailed specifications for the Liquid Hydrogen (LH₂) Storage Subsystem used in ground support operations for the AMPEL360 BWB H₂ Hy-E aircraft."
Keywords: ["ATA 03","GSE","LH2","Hydrogen Storage","Cryogenic","Ground Support"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968"
  - "ISO 19880-8"
  - "ASME B31.12"
Links:
  Parent: "../"
  Siblings:
    - "03-00-13-02-02A_LH2_Transfer_Subsystem.md"
    - "03-00-13-02-03A_H2_Safety_Subsystem.md"
    - "03-00-13-02-04A_Cryogenic_Control_Subsystem.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial LH₂ storage subsystem specification" }
---

# LH₂ Storage Subsystem — ATA 03 Support Information GSE

## 1. Purpose

This document specifies the **Liquid Hydrogen (LH₂) Storage Subsystem** for ground support equipment serving the AMPEL360 BWB H₂ Hy-E aircraft. The subsystem provides safe, efficient, and reliable storage of cryogenic liquid hydrogen at -253°C (20 K) for aircraft refueling operations.

## 2. Scope

### 2.1 Coverage

The LH₂ Storage Subsystem encompasses:

1. **Primary Storage Tank**
   - Vacuum-insulated cryogenic vessel
   - Inner vessel: stainless steel 316L
   - Outer vessel: carbon steel with corrosion protection
   - Capacity: 10,000 kg LH₂ (approximately 140,000 liters)

2. **Backup Storage Tank**
   - Redundant storage capacity
   - Capacity: 5,000 kg LH₂ (approximately 70,000 liters)
   - Independent operation capability

3. **Vacuum Insulation System**
   - Multi-layer insulation (MLI)
   - Vacuum pressure < 10⁻⁵ mbar
   - Thermal heat leak < 0.5 W/m²

4. **Pressure Relief and Safety Systems**
   - Primary and secondary relief valves
   - Burst discs
   - Emergency vent stack

5. **Tank Monitoring and Control**
   - Level sensors (capacitance and differential pressure)
   - Pressure sensors (cryogenic-rated)
   - Temperature sensors (RTD, Pt-100)
   - Data acquisition and control system

### 2.2 Out of Scope

- LH₂ transfer equipment (see [03-00-13-02-02A](./03-00-13-02-02A_LH2_Transfer_Subsystem.md))
- H₂ safety detection systems (see [03-00-13-02-03A](./03-00-13-02-03A_H2_Safety_Subsystem.md))
- Cryogenic control algorithms (see [03-00-13-02-04A](./03-00-13-02-04A_Cryogenic_Control_Subsystem.md))

## 3. Applicable Documents

| Standard | Application | Link |
|----------|-------------|------|
| **[SAE AS6968](https://www.sae.org/standards/content/as6968/)** | Hydrogen Aircraft Refueling | Overall GSE requirements |
| **[ISO 19880-8](https://www.iso.org/standard/71940.html)** | Gaseous Hydrogen Fueling Stations | Safety and operational requirements |
| **[ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines)** | Hydrogen Piping and Pipelines | Cryogenic piping design |
| **[ASME Section VIII Div. 1](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-rules-construction-pressure-vessels-division-1)** | Pressure Vessel Code | Tank design and fabrication |
| **[EN 13458-2](https://standards.cen.eu/)** | Cryogenic Vessels | Static vacuum insulated vessels |

## 4. Subsystem Description

### 4.1 Overview

The LH₂ Storage Subsystem consists of two vacuum-insulated cryogenic storage tanks (primary and backup) with integrated safety, monitoring, and control systems. The primary tank provides sufficient capacity for refueling multiple AMPEL360 aircraft without intermediate refilling, while the backup tank ensures operational continuity.

```
┌──────────────────────────────────────────────────────────────┐
│              LH₂ Storage Subsystem Architecture               │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌────────────────┐            ┌────────────────┐            │
│  │  Primary Tank  │            │  Backup Tank   │            │
│  │  10,000 kg LH₂ │            │  5,000 kg LH₂  │            │
│  │  -253°C / 20 K │            │  -253°C / 20 K │            │
│  │  1-5 bar       │            │  1-5 bar       │            │
│  └───────┬────────┘            └───────┬────────┘            │
│          │                             │                      │
│          │    ┌──────────────────┐     │                      │
│          └────┤ Manifold & Valves├─────┘                      │
│               └─────────┬────────┘                            │
│                         │                                     │
│                         ▼                                     │
│              ┌──────────────────┐                             │
│              │  To Transfer     │                             │
│              │  Subsystem       │                             │
│              └──────────────────┘                             │
│                                                                │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Safety Systems:                                       │    │
│  │ - Pressure Relief Valves (PRV)                       │    │
│  │ - Burst Discs                                        │    │
│  │ - Emergency Vent Stack                               │    │
│  │ - Overpressure Interlocks                            │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                                │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Monitoring & Control:                                 │    │
│  │ - Level Sensors (Capacitance, ΔP)                   │    │
│  │ - Pressure Sensors (0-10 bar)                        │    │
│  │ - Temperature Sensors (20-300 K)                     │    │
│  │ - Vacuum Sensors (MLI)                               │    │
│  │ - PLC Control System                                  │    │
│  └──────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

### 4.2 Specifications

#### 4.2.1 Primary Storage Tank

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Storage Capacity** | 10,000 kg LH₂ | ~140,000 liters at 71 kg/m³ density |
| **Inner Vessel Material** | Stainless Steel 316L | Cryogenic compatibility, ASTM A240 |
| **Outer Vessel Material** | Carbon Steel A516 Grade 70 | Painted with epoxy coating |
| **Design Pressure (Inner)** | 10 bar | ASME Section VIII Div. 1 |
| **Operating Pressure** | 1-5 bar absolute | Normal range |
| **Design Temperature** | -270°C to +50°C | Inner vessel |
| **Insulation Type** | Vacuum + Multi-Layer Insulation (MLI) | 30-60 layers aluminized Mylar |
| **Vacuum Level** | < 10⁻⁵ mbar | Maintained by getter pumps |
| **Heat Leak** | < 0.5 W/m² | Thermal performance |
| **Boil-Off Rate** | < 0.1% per day | At steady-state |
| **Overall Dimensions** | Ø 3.5 m × L 15 m | Horizontal orientation |
| **Weight (Empty)** | ~25,000 kg | Approximate |
| **Weight (Full)** | ~35,000 kg | Including LH₂ |

#### 4.2.2 Backup Storage Tank

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Storage Capacity** | 5,000 kg LH₂ | ~70,000 liters |
| **Material & Construction** | Same as primary tank | Standardized design |
| **Design Pressure** | 10 bar | ASME Section VIII Div. 1 |
| **Operating Pressure** | 1-5 bar absolute | Normal range |
| **Insulation** | Vacuum + MLI | Same as primary |
| **Boil-Off Rate** | < 0.1% per day | At steady-state |
| **Overall Dimensions** | Ø 3.0 m × L 10 m | Horizontal orientation |

### 4.3 Part Number Information

| Component | Part Number | Description | Supplier | Interchangeability |
|-----------|-------------|-------------|----------|-------------------|
| Primary Tank Assembly | GSE-H2-01-001-A | 10,000 kg LH₂ storage tank | Chart Industries | None (custom) |
| Backup Tank Assembly | GSE-H2-01-002-A | 5,000 kg LH₂ storage tank | Chart Industries | None (custom) |
| Vacuum Insulation Panel | GSE-H2-01-003-A | MLI panel set for primary tank | Lydall Thermal/Acoustical | Non-interchangeable |
| Primary Relief Valve | GSE-H2-01-004-A | Cryogenic PRV, 6 bar set | Herose GmbH | Model 06450 series |
| Burst Disc | GSE-H2-01-005-A | Rupture disc, 8 bar burst | Fike Corporation | Model SRD series |
| Level Sensor (Capacitance) | GSE-H2-01-006-A | 0-100% range, cryogenic | Endress+Hauser | Model FMI51 |
| Pressure Transmitter | GSE-H2-01-007-A | 0-10 bar, cryogenic | Rosemount | Model 3051C |
| Temperature Sensor | GSE-H2-01-008-A | RTD Pt-100, 20-300 K | Lake Shore Cryotronics | Model PT-103 |

See [03-00-13-03_GSE_Part_Number_Registry](../03-00-13-03_GSE_Part_Number_Registry/) for complete PNR.

## 5. Spare Parts Information

### 5.1 Critical Spare Parts

| Part Number | Description | Criticality | Lead Time | Min Stock |
|-------------|-------------|-------------|-----------|-----------|
| GSE-H2-01-004-A | Primary Relief Valve | **Critical** | 8 weeks | 2 units |
| GSE-H2-01-005-A | Burst Disc | **Critical** | 4 weeks | 4 units |
| GSE-H2-01-006-A | Level Sensor | **Essential** | 6 weeks | 1 unit |
| GSE-H2-01-007-A | Pressure Transmitter | **Essential** | 4 weeks | 2 units |
| GSE-H2-01-008-A | Temperature Sensor | **Essential** | 3 weeks | 3 units |
| GSE-H2-01-009-A | Vacuum Pump Cartridge | **Standard** | 6 weeks | 1 unit |
| GSE-H2-01-010-A | Gasket Kit (Cryogenic) | **Standard** | 2 weeks | 3 kits |

See [03-00-13-04_GSE_Spare_Parts_Management](../03-00-13-04_GSE_Spare_Parts_Management/) for complete spare parts strategy.

## 6. Safety Features

### 6.1 Overpressure Protection

| Protection Device | Set Point | Capacity | Discharge Location |
|-------------------|-----------|----------|-------------------|
| Primary PRV (PSV-001) | 6.0 bar | 100 kg/hr | Vent stack |
| Secondary PRV (PSV-002) | 6.5 bar | 100 kg/hr | Vent stack |
| Burst Disc (BD-001) | 8.0 bar | Full tank venting | Vent stack |

### 6.2 Emergency Venting

- **Vent Stack Height**: 10 meters above ground level
- **Vent Stack Diameter**: DN 200 (8 inches)
- **Emergency Vent Capacity**: 500 kg/hour (entire tank in < 20 hours)
- **Dispersion Zone**: 50-meter radius maintained clear

### 6.3 Vacuum Loss Detection

- **Vacuum Sensors**: Pirani gauge in annular space
- **Alarm Threshold**: > 10⁻³ mbar
- **Response**: Activate getter pumps, notify operator

## 7. Operational Parameters

### 7.1 Normal Operation

| Parameter | Operating Range | Alarm Threshold | Trip Threshold |
|-----------|-----------------|-----------------|----------------|
| Tank Pressure | 1.5-4.0 bar | < 1.2 or > 4.5 bar | < 1.0 or > 5.5 bar |
| LH₂ Temperature | 20-22 K | > 24 K | > 26 K |
| Liquid Level | 10-95% | < 5% or > 98% | < 2% or > 99% |
| Vacuum Pressure (MLI) | < 10⁻⁵ mbar | > 10⁻³ mbar | > 10⁻² mbar |

### 7.2 Fill and Withdrawal Rates

| Operation | Rate | Notes |
|-----------|------|-------|
| **Tank Filling** | 2,000 kg/hour max | From LH₂ delivery truck |
| **Aircraft Refueling** | 500 kg/hour nominal | To aircraft via transfer subsystem |
| **Emergency Defuel** | 1,000 kg/hour max | From aircraft back to storage |

## 8. Maintenance Requirements

### 8.1 Routine Inspections

| Inspection | Frequency | Procedure |
|------------|-----------|-----------|
| Visual inspection (exterior) | Daily | Check for frost, damage, leaks |
| Pressure gauge verification | Weekly | Compare gauges, verify readings |
| Relief valve inspection | Monthly | Visual check, no operational test |
| Vacuum level check | Monthly | Record vacuum pressure |
| Level sensor calibration | Quarterly | 3-point calibration check |
| Relief valve functional test | Annually | Lift test per manufacturer procedure |
| Pressure vessel inspection | 5 years | Per ASME Section VIII requirements |

### 8.2 Preventive Maintenance

| Task | Frequency | Estimated Duration |
|------|-----------|-------------------|
| Vacuum pump getter replacement | 3 years | 8 hours |
| Instrumentation calibration | Annually | 16 hours |
| Relief valve overhaul | 5 years | Send to OEM |
| Tank external coating inspection/repair | 5 years | Variable |

## 9. Cross-References

### 9.1 Related ATA Chapters

- [ATA 02 — Operations Information](../../../../../ATA_02-OPERATIONS_INFORMATION/) — Ground operations
- [ATA 85 — Infrastructure Interface Standards](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/) — H₂ infrastructure

### 9.2 Related Documents

- [03-00-13-01-01A_GSE_Subsystem_Overview](../03-00-13-01_GSE_Subsystem_Architecture/03-00-13-01-01A_GSE_Subsystem_Overview.md)
- [03-00-13-02-02A_LH2_Transfer_Subsystem](./03-00-13-02-02A_LH2_Transfer_Subsystem.md)
- [03-00-13-02-03A_H2_Safety_Subsystem](./03-00-13-02-03A_H2_Safety_Subsystem.md)
- [03-00-13-02-04A_Cryogenic_Control_Subsystem](./03-00-13-02-04A_Cryogenic_Control_Subsystem.md)
- [03-00-02_Safety](../../03-00-02_Safety/) — Safety assessments
- [03-00-06_Engineering](../../03-00-06_Engineering/) — Engineering standards

### 9.3 Parent Document

- [03-00-13_Subsystems_Components](../) — Top-level subsystems directory

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-13-02-01A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Ground Support Equipment WG

---
