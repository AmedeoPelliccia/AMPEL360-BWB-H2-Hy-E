# 85-70: Propulsion Systems for Ground Support Equipment

## Document Information

- **Document ID**: 85-70
- **Title**: Propulsion Systems for Ground Support Equipment
- **Version**: 1.0
- **Status**: ACTIVE
- **Date**: 2025-11-22

---

## 1. Purpose

This section provides comprehensive documentation for propulsion systems used in Ground Support Equipment (GSE) at airports supporting the AMPEL360 BWB-H2-Hy-E aircraft. It covers electric, hydrogen fuel cell, and hybrid propulsion technologies for zero-emission or low-emission airport operations.

---

## 2. Scope

### 2.1 In Scope

- Battery-electric GSE propulsion systems
- Hydrogen fuel cell GSE propulsion systems
- Hybrid propulsion systems (battery-diesel, battery-H₂)
- Charging infrastructure for electric GSE
- Motor and drivetrain specifications
- Maintenance and diagnostic systems
- Integration with airport energy infrastructure
- Performance monitoring and optimization

### 2.2 Out of Scope

- Aircraft propulsion systems (covered in ATA 70-79 series in T-TECHNOLOGY)
- Airport ground power units (covered in [ATA 85-80_Energy](../85-80_Energy/))
- Static hydrogen storage (covered in [ATA 85-60_Storages](../85-60_Storages/))

---

## 3. Document Structure

This section is organized into the following subsections:

### 3.1 [85-70-01_Electric_GSE_Propulsion](./85-70-01_Electric_GSE_Propulsion/)

Battery-electric propulsion systems for GSE including:
- Battery Electric Tugs
- Electric Belt Loaders
- Electric Baggage Tractors
- Electric Cargo Loaders
- Power Electronics (BMS, inverters, converters)

### 3.2 [85-70-02_H2_Fuel_Cell_GSE](./85-70-02_H2_Fuel_Cell_GSE/)

Hydrogen fuel cell propulsion systems for GSE including:
- H₂ Fuel Cell Tugs
- H₂ Heavy Duty Equipment
- Fuel Cell Stack Design
- H₂ Storage Onboard GSE
- Refueling Interface

### 3.3 [85-70-03_Hybrid_Propulsion_Systems](./85-70-03_Hybrid_Propulsion_Systems/)

Hybrid propulsion systems combining multiple power sources:
- Battery-Diesel Hybrid
- Battery-H₂ Hybrid
- Energy Management Strategy

### 3.4 [85-70-04_Charging_Infrastructure](./85-70-04_Charging_Infrastructure/)

Charging infrastructure for electric GSE:
- Fast Charging Stations
- Opportunity Charging
- Smart Charging Management
- Battery Swapping Systems

### 3.5 [85-70-05_Motor_and_Drivetrain](./85-70-05_Motor_and_Drivetrain/)

Electric motor and drivetrain specifications:
- Electric Motors
- Transmission Systems
- Regenerative Braking
- Thermal Management

### 3.6 [85-70-06_Maintenance_and_Diagnostics](./85-70-06_Maintenance_and_Diagnostics/)

Maintenance procedures and diagnostic systems:
- Predictive Maintenance
- Battery Health Monitoring
- Motor Diagnostics

### 3.7 [ASSETS/](./ASSETS/)

Supporting data and integration documents:
- GSE Fleet Specifications
- Energy Consumption Analysis
- Lifecycle Cost Models
- Carbon Footprint Tracking
- Integration with ATA 85-40 Software

---

## 4. Strategic Context

### 4.1 Zero-Emission Airport Operations

The AMPEL360 program aims to achieve zero-emission aircraft operations, which requires a comprehensive transition of airport ground support equipment from diesel to electric or hydrogen fuel cell propulsion. This section provides the technical foundation for this transition.

### 4.2 Hydrogen Ecosystem Integration

The BWB-H2-Hy-E aircraft utilizes hydrogen as its primary fuel. Airport GSE powered by hydrogen fuel cells creates operational synergy by:
- Sharing hydrogen refueling infrastructure
- Demonstrating hydrogen safety protocols
- Building hydrogen operational experience
- Maximizing return on hydrogen infrastructure investment

### 4.3 Battery-Electric Foundation

Battery-electric GSE provides the near-term solution for most airport ground handling operations with:
- Proven technology and mature supply chain
- Lower initial cost compared to fuel cell systems
- Suitable for light to medium-duty applications
- Excellent energy efficiency (70-80% well-to-wheel)

---

## 5. Key Standards and Regulations

### 5.1 Aviation Standards

- [EASA CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-large-aeroplanes) – Large Aeroplanes Certification
- [FAA Part 21](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-21) – Certification Procedures
- [IATA AHM](https://www.iata.org/en/publications/manuals/airport-handling-manual/) – Airport Handling Manual

### 5.2 Electric Vehicle Standards

- [IEC 61851](https://webstore.iec.ch/publication/6035) – Electric vehicle conductive charging system
- [ISO 15118](https://www.iso.org/standard/55366.html) – Vehicle-to-grid communication
- [IEC 62196](https://webstore.iec.ch/publication/6614) – Plugs, socket-outlets, vehicle connectors

### 5.3 Hydrogen Safety Standards

- [ISO 19880-1](https://www.iso.org/standard/71940.html) – Gaseous hydrogen fueling stations
- [ISO 19881](https://www.iso.org/standard/66787.html) – Land vehicle fuel containers
- [SAE J2579](https://www.sae.org/standards/content/j2579_201808/) – Fuel systems safety requirements

### 5.4 Battery Safety Standards

- [UN 38.3](https://unece.org/transportdangerous-goods/un-manual-tests-and-criteria-rev6-2015) – Lithium battery testing
- [UL 2580](https://www.ul.com/resources/ul-2580-standard-safety) – Batteries for electric vehicles
- [IEC 62619](https://webstore.iec.ch/publication/7299) – Secondary batteries for industrial applications

### 5.5 Functional Safety

- [ISO 26262](https://www.iso.org/standard/68383.html) – Road vehicles - Functional safety
- [IEC 61508](https://webstore.iec.ch/publication/5515) – Functional safety of systems

---

## 6. Cross-References

### 6.1 Internal (ATA 85)

- [85-00-03_Requirements](../85-00_GENERAL/85-00-03_Requirements/) – System requirements
- [85-00-04_Design](../85-00_GENERAL/85-00-04_Design/) – Design specifications
- [85-10_Operations](../85-10_Operations/) – Operational procedures
- [85-40_Software](../85-40_Software/) – Fleet management software
- [85-60_Storages](../85-60_Storages/) – H₂ storage infrastructure
- [85-80_Energy](../85-80_Energy/) – Energy management systems

### 6.2 External (Other ATAs)

- [ATA 02 – Operations Information](../../ATA_02-OPERATIONS_INFORMATION/)
- [ATA 03 – Support Information GSE](../../ATA_03-SUPPORT_INFORMATION_GSE/)
- [ATA 09 – Towing and Taxiing](../../../P-PROGRAM/ATA_09-TOWING_AND_TAXIING/)
- [ATA 12 – Servicing](../../../P-PROGRAM/ATA_12-SERVICING/)
- [ATA 95 – Digital Product Passport](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)

---

## 7. Technology Comparison

| Technology | Advantages | Disadvantages | Best Application |
|------------|------------|---------------|------------------|
| **Battery-Electric** | Mature technology, high efficiency, lower cost | Long charging time, range anxiety | Light-medium duty, frequent cycling |
| **H₂ Fuel Cell** | Fast refueling, long range, high power | Higher cost, lower efficiency, infrastructure | Heavy duty, long range operations |
| **Hybrid** | Flexibility, optimal efficiency | Complexity, higher maintenance | Transition technology, extreme duty cycles |

---

## 8. Implementation Roadmap

### 8.1 Phase 1 (2024-2026)

- Deploy battery-electric GSE for light to medium-duty operations
- Establish AC Level 2 and DC fast charging infrastructure
- Pilot hydrogen fuel cell tugs at selected airports

### 8.2 Phase 2 (2026-2028)

- Scale battery-electric fleet to 60-70% of GSE
- Deploy H₂ fuel cell GSE for heavy-duty applications
- Implement smart charging and energy management systems

### 8.3 Phase 3 (2028-2030)

- Achieve 90%+ zero-emission GSE fleet
- Integrate V2G (vehicle-to-grid) capabilities
- Optimize hydrogen and electric infrastructure utilization

---

## 9. Naming Convention

Items within this bucket follow the pattern:
- **85-70-XX_DESCRIPTION**
  - 85 = ATA chapter
  - 70 = Bucket number (Propulsion)
  - XX = Sequential number (00, 01, 02, etc.)
  - DESCRIPTION = Descriptive name

---

## 10. Status and Next Steps

- **Current Phase**: Documentation framework complete
- **Next Phase**: Pilot programs and vendor selection
- **Dependencies**: Airport infrastructure investment, technology cost reduction, regulatory approvals

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: ACTIVE – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.
- **Standard**: OPT-IN Framework v1.1
- **Owner**: AMPEL360 Documentation WG

---

**End of Document**
