# 03-90-06-01A - GSE Specifications Table

## 1. Purpose

Provide a comprehensive specifications table for all Ground Support Equipment, documenting key technical parameters, ratings, and capabilities.

## 2. Scope

Master specification table covering: storage systems, transfer equipment, control systems, safety systems, and support equipment for hydrogen GSE operations.

## 3. Applicable Documents

- [ATA iSpec 2200](https://www.ata.org/resources/specifications) - Information Standards
- Equipment manufacturer datasheets and specifications

## 4. Documentation Description

### 4.1 Overview

Centralized reference for GSE technical specifications, enabling equipment selection, compatibility verification, and procurement.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Equipment List | Tabular format | Sortable by category, tag, or parameter |
| Technical Parameters | Numeric with units | SI units primary |
| Performance Data | Operating ranges | Min, nominal, max values |
| Environmental Ratings | Temperature, humidity, altitude | Operating and storage conditions |

### 4.3 Content Requirements

#### 4.3.1 GSE Equipment Categories

**LH2 Storage Systems:**

| Equipment Tag | Description | Capacity | Design Pressure | Design Temp | Insulation | Weight (empty) |
|---------------|-------------|----------|-----------------|-------------|------------|----------------|
| GSE-LH2-0001 | LH2 Storage Tank | 50,000 L | 10 bar | -253°C to +65°C | Vacuum + MLI | 15,000 kg |
| GSE-LH2-0002 | LH2 Mobile Cart | 5,000 L | 10 bar | -253°C to +65°C | Vacuum | 2,500 kg |

**Transfer Equipment:**

| Equipment Tag | Description | Type | Flow Rate | Head Pressure | Power | Material |
|---------------|-------------|------|-----------|---------------|-------|----------|
| GSE-PMP-0001 | LH2 Transfer Pump | Centrifugal | 500 L/min | 15 bar | 50 HP | 316L SS |
| GSE-PMP-0002 | LH2 Fueling Pump | Positive Disp. | 200 L/min | 8 bar | 20 HP | 316L SS |

**Vaporization Equipment:**

| Equipment Tag | Description | Capacity | Inlet/Outlet | Heating Method | Efficiency |
|---------------|-------------|----------|--------------|----------------|------------|
| GSE-VAP-0001 | Ambient Vaporizer | 100 Nm³/hr | LH2 / GH2 | Air-heated | 95% |
| GSE-VAP-0002 | Electric Vaporizer | 50 Nm³/hr | LH2 / GH2 | Electric heater | 98% |

**Control Systems:**

| Equipment Tag | Description | Type | I/O Count | Communication | Power | Redundancy |
|---------------|-------------|------|-----------|---------------|-------|------------|
| GSE-CTL-0001 | Main PLC | Modular | 256 DI, 128 DO, 64 AI, 32 AO | Ethernet/IP | 24 VDC | Dual CPU |
| GSE-CTL-0002 | Safety PLC | Compact | 32 DI, 16 DO | ProfiSafe | 24 VDC | SIL 3 |

**Safety Equipment:**

| Equipment Tag | Description | Type | Range | Response Time | Certification |
|---------------|-------------|------|-------|---------------|---------------|
| GSE-SAF-0010 | H2 Detector Zone 1 | Catalytic | 0-100% LEL | < 30 sec | ATEX Zone 1 |
| GSE-SAF-0020 | Fire Detector | UV/IR | 5m radius | < 5 sec | FM Approved |
| GSE-SAF-0030 | Emergency Stop | Push-button | N/A | Mechanical | IEC 60947-5-5 |

#### 4.3.2 Performance Specifications

**LH2 System Performance:**
- Boil-off rate: < 0.3% per day (static)
- Fueling rate: 100-300 kg/min (aircraft dependent)
- Cooldown time: < 15 minutes (piping)
- System availability: > 99% (target)

**Safety System Performance:**
- H2 detection coverage: 100% of hazardous areas
- ESD response time: < 3 seconds
- Alarm acknowledgment time: < 60 seconds (operator)
- Fire suppression activation: < 10 seconds

#### 4.3.3 Environmental Specifications

**Operating Conditions:**

| Parameter | Minimum | Maximum | Notes |
|-----------|---------|---------|-------|
| Ambient Temperature | -20°C | +45°C | Equipment derating above +40°C |
| Humidity | 0% RH | 95% RH | Non-condensing |
| Altitude | Sea level | 2000m | Pressure compensation required above |
| Wind Speed | 0 m/s | 25 m/s | Operations suspended above limit |
| Seismic | Zone 2 | Zone 4 | Per IBC seismic design |

**Storage Conditions:**
- Temperature: -40°C to +70°C
- Humidity: 0% to 100% RH
- Preservation required for storage > 6 months

#### 4.3.4 Materials and Construction

**H2-Compatible Materials:**

| Application | Material | Specification | Notes |
|-------------|----------|---------------|-------|
| LH2 Piping | 316L Stainless Steel | ASTM A312 | Austenitic, low carbon |
| GH2 Piping (high P) | 316 Stainless Steel | ASTM A312 | High strength |
| Gaskets | Spiral Wound, Graphite | ASME B16.20 | Hydrogen-compatible |
| Bolting | A193 B8M | ASTM A193 | Stainless, non-magnetic |
| Seals (dynamic) | PTFE, Peek | - | Low temperature rated |

#### 4.3.5 Electrical Specifications

**Power Requirements:**

| System | Voltage | Phase | Load (kW) | Breaker Size |
|--------|---------|-------|-----------|--------------|
| LH2 Transfer Pump | 480V | 3φ | 37 | 100A |
| GH2 Compressor | 480V | 3φ | 75 | 150A |
| Control System | 120V / 24V DC | 1φ | 5 | 20A |
| Lighting | 120V | 1φ | 2 | 20A |

## 5. Cross-References

- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-06-02A H2 Equipment Specs](./03-90-06-02A_H2_Equipment_Specs.md)
  - [03-90-01-04A Numbering Conventions](../03-90-01_GSE_Documentation_Standards/03-90-01-04A_Numbering_Conventions.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
