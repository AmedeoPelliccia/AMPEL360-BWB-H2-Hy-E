# 85-70-02-001: H₂ Fuel Cell Tugs

## Document Information

- **Document ID**: 85-70-02-001
- **Title**: Hydrogen Fuel Cell Tugs
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

---

## 1. Purpose

This document defines the specifications, requirements, and operational guidelines for hydrogen fuel cell-powered tugs used in ground handling operations for the AMPEL360 BWB-H2-Hy-E aircraft.

---

## 2. Scope

### 2.1 In Scope

- H₂ fuel cell pushback tractors
- Fuel cell-powered towbarless aircraft tugs
- H₂ storage systems for tug operations
- Refueling procedures and interfaces
- Performance criteria and operational parameters
- Safety systems and hydrogen handling

### 2.2 Out of Scope

- Battery-electric tugs (see [85-70-01-001](../85-70-01_Electric_GSE_Propulsion/85-70-01-001_Battery_Electric_Tugs.md))
- Hybrid tugs (see [85-70-03](../85-70-03_Hybrid_Propulsion_Systems/))

---

## 3. Technical Requirements

### 3.1 Towing Capacity

- **Maximum Towing Weight**: 650 metric tons (BWB-H2-Hy-E MTOW)
- **Pushback Force**: Minimum 150 kN
- **Operating Speed**: 0-30 km/h
- **Slope Capability**: Up to 3% gradient fully loaded
- **Range**: 300-400 km per refueling

### 3.2 Fuel Cell System

- **Fuel Cell Type**: PEM (Proton Exchange Membrane)
- **Power Output**: 150-250 kW continuous
- **Peak Power**: 300-400 kW (with battery buffer)
- **System Efficiency**: 50-60% (H₂ to electric)
- **Operating Temperature**: -30°C to +40°C ambient
- **Cooling System**: Liquid cooling with deionized water/glycol

### 3.3 Hydrogen Storage

- **Storage Type**: Type IV composite cylinders (700 bar)
- **H₂ Capacity**: 40-60 kg hydrogen
- **Tank Configuration**: 4-6 cylinders under vehicle chassis
- **Refueling Time**: 5-10 minutes
- **Tank Certification**: [ISO 19881](https://www.iso.org/standard/66787.html), [UN ECE R134](https://unece.org/transport/standards/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-121)

### 3.4 Electric Drivetrain

- **Motor Type**: Permanent magnet synchronous motor (PMSM)
- **Motor Power**: 200-300 kW continuous
- **Battery Buffer**: 20-30 kWh (lithium-ion for peak power)
- **Regenerative Braking**: Energy captured to battery buffer
- **Efficiency**: >85% system efficiency (fuel cell to wheels)

### 3.5 Environmental Requirements

- **Operating Temperature**: -30°C to +50°C
- **Humidity**: 0-95% non-condensing
- **Ingress Protection**: IP54 for electrical components
- **Altitude**: Operation up to 2,500m AMSL

---

## 4. Safety Requirements

### 4.1 Hydrogen Safety

- **Leak Detection**: Multiple H₂ sensors with automatic ventilation
- **Ventilation**: Forced ventilation in fuel cell compartment
- **Emergency Shutdown**: Automatic H₂ supply cutoff on leak detection
- **Fire Detection**: Flame and heat detectors
- **Grounding**: Bonding to prevent static discharge
- **Pressure Relief**: PRD (Pressure Relief Device) on H₂ tanks

### 4.2 Operational Safety

- **Emergency Stop**: Dual-circuit emergency stop system
- **Dead Man Switch**: Operator presence detection
- **Anti-collision**: 360° proximity sensors and cameras
- **Collision Mitigation**: Automatic braking on obstacle detection

### 4.3 Maintenance Safety

- **Lockout/Tagout**: H₂ system isolation for maintenance
- **Purging**: Inert gas purging procedures
- **Training**: Specialized training for H₂ handling
- **PPE**: Personal protective equipment requirements

---

## 5. Standards and Compliance

### 5.1 Hydrogen Standards

- [ISO 19880-1](https://www.iso.org/standard/71940.html) – Gaseous hydrogen fueling stations
- [ISO 19881](https://www.iso.org/standard/66787.html) – Land vehicle fuel containers
- [SAE J2579](https://www.sae.org/standards/content/j2579_201808/) – Fuel systems safety requirements
- [ISO 14687](https://www.iso.org/standard/69539.html) – Hydrogen fuel quality

### 5.2 Fuel Cell Standards

- [IEC 62282-2](https://webstore.iec.ch/publication/6735) – Fuel cell modules
- [SAE J2615](https://www.sae.org/standards/content/j2615_201612/) – Fuel cell performance testing

### 5.3 Pressure Vessel Standards

- [UN ECE R134](https://unece.org/transport/standards/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-121) – Hydrogen vehicles
- [ISO 11439](https://www.iso.org/standard/44087.html) – Gas cylinders for vehicle storage

---

## 6. Cross-References

### 6.1 Internal (ATA 85)

- [85-70-02-A-001_Fuel_Cell_Specs.csv](./ASSETS/85-70-02-A-001_Fuel_Cell_Specs.csv) – Fuel cell specifications
- [85-70-02-A-002_H2_Tank_Integration.md](./ASSETS/85-70-02-A-002_H2_Tank_Integration.md) – H₂ tank design
- [85-70-02-005_Refueling_Interface.md](./85-70-02-005_Refueling_Interface.md) – Refueling procedures
- [85-60_Storages](../../85-60_Storages/) – H₂ infrastructure
- [85-70-06](../85-70-06_Maintenance_and_Diagnostics/) – Maintenance

### 6.2 External (Other ATAs)

- [ATA 03 – Support Information GSE](../../../ATA_03-SUPPORT_INFORMATION_GSE/)
- [ATA 09 – Towing and Taxiing](../../../../P-PROGRAM/ATA_09-TOWING_AND_TAXIING/)

---

## 7. Status and Next Steps

- **Current Phase**: Technology evaluation and pilot programs
- **Next Phase**: Fleet trials at H₂-equipped airports
- **Dependencies**: Airport H₂ refueling infrastructure, fuel cell cost reduction

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
