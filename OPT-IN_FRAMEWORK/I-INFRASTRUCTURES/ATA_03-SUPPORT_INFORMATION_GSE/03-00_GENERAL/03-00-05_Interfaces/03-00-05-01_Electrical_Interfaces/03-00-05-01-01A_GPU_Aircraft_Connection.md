# 03-00-05-01-01A - GPU Aircraft Connection

## 1. Purpose
This document specifies the interface requirements and procedures for connecting Ground Power Units (GPU) to the AMPEL360 BWB H₂ Hy-E aircraft electrical system.

## 2. Scope
This specification covers the physical, electrical, and procedural aspects of GPU-to-aircraft connections for ground power supply during maintenance, servicing, and pre-flight operations.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ARP4754A (Guidelines for Development of Civil Aircraft and Systems)
- SAE AS50881 (Wiring Aerospace Vehicle)
- MIL-STD-704F (Aircraft Electric Power Characteristics)
- IEEE 1809 (Standard for Grounding of DC Equipment Enclosures)

## 4. Interface Description

### 4.1 Overview
The GPU interface provides external electrical power to the aircraft systems when main engines are not operating. The connection supports both 115V AC 400Hz and 28V DC power supply configurations.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Connector Type | MS3106F 28-21S (400Hz AC) | - |
| Connector Type | MS3106F 24-22S (28V DC) | - |
| Connection Location | Fuselage Station FS 125, Port Side | ±50mm |
| Access Height | 1.8m from ground level | ±100mm |
| Connector Protection | IP65 rated cover | - |
| Operating Temperature | -40°C to +55°C | - |

### 4.3 Connection Procedure
1. **Pre-Connection Checks**
   - Verify GPU output voltage and frequency within specifications
   - Inspect aircraft receptacle for damage or contamination
   - Ensure all personnel clear of connection area
   - Verify aircraft master switch is OFF

2. **Connection Steps**
   - Remove protective cover from aircraft receptacle
   - Align GPU cable connector with receptacle
   - Insert connector and rotate clockwise until locked
   - Verify visual lock indicator
   - Enable GPU output
   - Monitor aircraft electrical bus voltage

3. **Disconnection Steps**
   - Disable GPU output
   - Verify aircraft electrical load is transferred to internal power
   - Rotate connector counter-clockwise and remove
   - Install protective cover on aircraft receptacle
   - Secure GPU cable

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| GPU Unit | 90 kVA minimum, 400Hz | For AC power operations |
| GPU Unit | 1000A minimum, 28V DC | For DC power operations |
| Cable Assembly | MIL-C-27500, AWG 2/0 | Maximum length 15m |
| Cable Insulation | 600V rated minimum | Temperature rated -55°C to +200°C |
| Ground Bonding | AWG 2 minimum | Green/yellow striped |

## 6. Safety Requirements
- **Electrical Safety**
  - Always verify proper grounding before connection
  - Use insulated tools and wear appropriate PPE (electrical hazard rated gloves)
  - Never connect/disconnect under load
  - Verify voltage and frequency match before connection

- **H2 Aircraft Specific**
  - Ensure GPU equipment is rated for use in H2 environment
  - Maintain minimum 10m separation from H2 fueling operations
  - Verify bonding resistance < 1Ω to aircraft structure
  - Use spark-resistant tools and equipment
  - Monitor for static discharge hazards

- **Personnel Safety**
  - Minimum 2 qualified personnel required for connection operations
  - Maintain clear communication with flight deck during operations
  - Use spotter when operating near aircraft control surfaces

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 24 (Electrical Power)
  - ATA 28 (Fuel - H2 considerations)
  - ATA 12 (Servicing)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related GSE Subsystems: 03-20_Subsystems
- Related Interface: [03-00-05-01-04A_Electrical_Grounding](./03-00-05-01-04A_Electrical_Grounding.md)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 GSE Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
