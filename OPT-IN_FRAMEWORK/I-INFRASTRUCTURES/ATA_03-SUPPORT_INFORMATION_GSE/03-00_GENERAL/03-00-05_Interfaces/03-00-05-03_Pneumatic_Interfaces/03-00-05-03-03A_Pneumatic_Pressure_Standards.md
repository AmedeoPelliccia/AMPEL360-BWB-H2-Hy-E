# 03-00-05-03-03A - Pneumatic Pressure Standards

## 1. Purpose
This document specifies the pneumatic pressure standards and requirements for ground support equipment interfacing with the AMPEL360 BWB H₂ Hy-E aircraft pneumatic systems.

## 2. Scope
This specification covers pressure ranges, regulation requirements, testing procedures, and safety standards for all pneumatic GSE connections.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ARP4754A (Guidelines for Development of Civil Aircraft and Systems)
- SAE AS1241 (Air Start Units and Accessories)
- ISO 4126 (Safety Devices for Protection Against Excessive Pressure)
- ASME B31.3 (Process Piping)
- CGA G-7.1 (Commodity Specification for Air)

## 4. Interface Description

### 4.1 Overview
Pneumatic pressure standards ensure safe and effective operation of ground support equipment connected to aircraft pneumatic systems. Proper pressure regulation prevents system damage and ensures reliable operation.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Engine Start Pressure | 30-50 psi (2.0-3.4 bar) | Operating range |
| Engine Start Maximum | 65 psi (4.5 bar) | Absolute maximum |
| Bleed Air Pressure | 40-60 psi (2.8-4.1 bar) | Operating range |
| Bleed Air Maximum | 75 psi (5.2 bar) | Absolute maximum |
| Air Conditioning Pressure | 35-45 psi (2.4-3.1 bar) | Operating range |
| Test Pressure | 1.5 × maximum operating | Hydrostatic test |
| Pressure Relief Setting | 110% of maximum operating | Safety valve |
| Pressure Gauge Accuracy | ±2% of full scale | Digital preferred |
| Pressure Transient Limit | 120% of maximum | < 1 second duration |

### 4.3 Connection Procedure
1. **Pre-Connection Pressure Verification**
   - Verify GSE pressure regulator calibration current
   - Set regulator to mid-range of operating pressure
   - Perform pressure gauge zero check
   - Test pressure relief valve operation
   - Verify pressure transducer functionality
   - Document pre-operation pressure readings

2. **Pressure Ramp-Up Procedure**
   - Begin with supply pressure at minimum
   - Increase pressure gradually (< 10 psi per 10 seconds)
   - Monitor aircraft system response
   - Stabilize at target operating pressure
   - Verify no leaks at all connections
   - Document stabilized pressure readings

3. **Operating Pressure Monitoring**
   - Continuous pressure monitoring required
   - Sample rate: minimum 1 Hz
   - Alarm if pressure exceeds operating range
   - Automatic shutdown if maximum exceeded
   - Record pressure data for post-operation analysis

4. **Pressure Reduction and Disconnection**
   - Reduce pressure gradually (< 10 psi per 10 seconds)
   - Allow system to stabilize at each step
   - Confirm zero pressure before physical disconnection
   - Verify pressure relief valve not stuck open
   - Document final pressure readings

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Pressure Regulator | 0-100 psi range | Precision type, ±1 psi |
| Digital Pressure Gauge | 0-150 psi range | ±0.5% accuracy |
| Pressure Relief Valve | ASME rated | Set per system requirement |
| Pressure Transducer | 0-10V output, 0-100 psi | For data logging |
| Calibration Certificate | Annual calibration | All pressure instruments |
| Pressure Test Kit | 0-200 psi capability | For GSE verification |

## 6. Safety Requirements
- **Pressure Regulation Safety**
  - All systems must have pressure relief protection
  - Dual redundancy for critical pressure controls
  - Automatic shutdown on overpressure
  - Manual pressure override requires authorization
  - Pressure gauge visible from operator position
  - Audible alarm for pressure excursions

- **Testing and Verification**
  - Daily pressure calibration check before first use
  - Weekly pressure relief valve functional test
  - Monthly regulator performance verification
  - Annual complete system pressure test
  - Immediate removal from service if out of specification
  - Document all testing and calibration

- **Operational Limits**
  - Never exceed absolute maximum pressure
  - Maintain pressure within operating range
  - Slow pressure changes to prevent shock loads
  - Verify system compatibility before connection
  - Monitor for pressure drift during operation
  - Emergency depressurization capability required

- **H2 Aircraft Considerations**
  - Enhanced pressure monitoring near H2 systems
  - Pressure-related sparks could ignite hydrogen
  - Pressure relief discharge directed away from H2 areas
  - Additional safety factor for H2 zone operations
  - Pressure testing prohibited during H2 fueling

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 36 (Pneumatic)
  - ATA 80 (Starting)
  - ATA 21 (Air Conditioning)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related Interface: [03-00-05-03-01A_Air_Start_Connection](./03-00-05-03-01A_Air_Start_Connection.md)
- Related Interface: [03-00-05-03-02A_Bleed_Air_Interface](./03-00-05-03-02A_Bleed_Air_Interface.md)
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
