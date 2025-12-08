# 03-00-05-03-02A - Bleed Air Interface

## 1. Purpose
This document specifies the interface requirements for ground-based bleed air supply to the AMPEL360 BWB H₂ Hy-E aircraft environmental control and engine starting systems.

## 2. Scope
This specification covers bleed air connection interfaces, pressure and temperature requirements, and operational procedures for ground conditioning operations.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ARP4754A (Guidelines for Development of Civil Aircraft and Systems)
- SAE AS1241 (Air Start Units and Accessories)
- SAE ARP85 (Air Conditioning Equipment for Aircraft)
- MIL-STD-810 (Environmental Engineering Considerations)

## 4. Interface Description

### 4.1 Overview
The bleed air interface provides conditioned, pressurized air from ground support equipment to the aircraft's pneumatic distribution system for environmental control, engine starting, and system testing when aircraft engines are not operating.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Connector Type | MS24484-5C (3.0 inch) | - |
| Connection Location | Fuselage Station FS 200, Port Side | ±100mm |
| Supply Pressure | 40-60 psi (2.8-4.1 bar) | Operating range |
| Maximum Pressure | 75 psi (5.2 bar) | Absolute maximum |
| Air Temperature | 150°C to 200°C | At supply |
| Air Flow Rate | 150 lbs/min (68 kg/min) | Minimum |
| Maximum Temperature | 250°C | Absolute maximum |
| Coupling Material | Stainless steel 321 | High temperature rated |
| Access Height | 2.0m from ground level | ±200mm |

### 4.3 Connection Procedure
1. **Pre-Connection Setup**
   - Position bleed air cart within 10m of connection point
   - Verify unit output parameters within specifications
   - Inspect connection hose for heat damage
   - Check aircraft receptacle for cleanliness
   - Ensure protective covers removed
   - Verify area clear of personnel

2. **Connection Sequence**
   - Allow hose end to cool if hot from previous use
   - Align coupling with aircraft receptacle
   - Insert and rotate locking mechanism clockwise
   - Verify mechanical lock engagement
   - Gradually increase pressure and temperature
   - Monitor for leaks using ultrasonic detector
   - Stabilize at operating parameters

3. **Operating Monitoring**
   - Continuously monitor pressure and temperature
   - Check for unusual vibrations or noise
   - Verify aircraft system pressurization
   - Monitor GSE unit performance
   - Document any parameter excursions

4. **Disconnection Procedure**
   - Reduce temperature gradually (< 50°C per minute)
   - Decrease pressure to zero
   - Allow coupling to cool (< 80°C)
   - Rotate locking mechanism counter-clockwise
   - Remove coupling carefully (may be hot)
   - Install protective covers on both sides
   - Store equipment properly

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Bleed Air Cart | 200 lbs/min capacity | Combined heater/compressor |
| Air Compressor | 100 psi maximum | Oil-free type preferred |
| Air Heater | 250°C maximum output | Natural gas or diesel |
| Supply Hose | 3.0 inch, high-temperature | Stainless steel braided |
| Temperature Controller | ±5°C accuracy | Automatic regulation |
| Pressure Regulator | 0-100 psi range | Manual or automatic |
| Safety Relief Valve | Set at 85 psi | For overpressure protection |

## 6. Safety Requirements
- **High Temperature Safety**
  - Wear heat-resistant gloves for all connection operations
  - Verify surface temperature < 80°C before touching
  - Use thermal camera to check hot spots
  - Maintain 1m clearance from hot surfaces
  - Post high temperature warning signs
  - Fire extinguisher positioned and ready

- **Pressure Safety**
  - Never exceed 75 psi supply pressure
  - Verify pressure relief valve functionality before use
  - Monitor pressure continuously during operation
  - Automatic shutdown if pressure exceeds limits
  - Gradual pressure changes to prevent shock loads

- **H2 Aircraft Specific**
  - Ensure bleed air supply is contamination-free
  - Verify no oil mist or hydrocarbons in air supply
  - Position equipment upwind of H2 fuel areas
  - No hot work within 30m during H2 operations
  - Enhanced ventilation around bleed air connection

- **Personnel Safety**
  - Minimum 2 qualified personnel for operations
  - Communication with flight deck required
  - Heat stress precautions in warm weather
  - Proper PPE: heat-resistant gloves, face shield, safety shoes
  - Emergency shutdown procedures clearly posted

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 21 (Air Conditioning)
  - ATA 36 (Pneumatic)
  - ATA 80 (Starting)
  - ATA 30 (Ice and Rain Protection)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related Interface: [03-00-05-03-01A_Air_Start_Connection](./03-00-05-03-01A_Air_Start_Connection.md)
- Related Interface: [03-00-05-03-03A_Pneumatic_Pressure_Standards](./03-00-05-03-03A_Pneumatic_Pressure_Standards.md)
- Related Interface: [03-00-05-03-04A_Air_Conditioning_GSE](./03-00-05-03-04A_Air_Conditioning_GSE.md)

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
