# 03-00-05-01-03A - Voltage Standards

## 1. Purpose
This document specifies the electrical voltage standards and requirements for ground support equipment interfacing with the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope
This specification covers all voltage levels, frequency requirements, and power quality standards for GSE electrical connections to the aircraft.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ARP4754A (Guidelines for Development of Civil Aircraft and Systems)
- MIL-STD-704F (Aircraft Electric Power Characteristics)
- SAE AS50881 (Wiring Aerospace Vehicle)
- IEC 60038 (Standard Voltages)
- RTCA DO-160G (Environmental Conditions and Test Procedures)

## 4. Interface Description

### 4.1 Overview
Ground support electrical interfaces must comply with strict voltage and power quality standards to ensure safe aircraft system operation during ground servicing. This document defines acceptable voltage ranges, frequency tolerances, and power quality requirements.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| AC Voltage (3-phase) | 115V L-N, 200V L-L | ±3V steady state |
| AC Frequency | 400 Hz | ±1 Hz steady state |
| AC Voltage Transient | 130V maximum | < 1 second duration |
| DC Voltage (Main) | 28V DC | ±2V steady state |
| DC Voltage Transient | 32V maximum | < 50ms duration |
| DC Ripple | < 1.5V peak-to-peak | At rated load |
| Power Factor | > 0.85 | At full load |
| Voltage Imbalance | < 2% | Between phases |
| Total Harmonic Distortion | < 5% | THD for AC systems |

### 4.3 Connection Procedure
1. **Pre-Connection Voltage Verification**
   - Measure GPU output voltage with calibrated meter
   - Verify frequency stability (AC systems)
   - Check phase rotation for 3-phase AC (A-B-C sequence)
   - Confirm voltage within specifications before connection

2. **Connection Monitoring**
   - Monitor voltage at aircraft bus during connection
   - Verify automatic transfer switch operation
   - Check for voltage drop in cable assembly
   - Validate power quality indicators

3. **Post-Connection Validation**
   - Confirm stable voltage at all monitored points
   - Verify no fault indicators on aircraft systems
   - Document voltage readings in maintenance log

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Digital Multimeter | CAT III 600V rated, ±0.5% accuracy | For voltage verification |
| Power Quality Analyzer | IEC 61000-4-30 Class A | For THD and power factor measurement |
| Frequency Counter | ±0.01 Hz accuracy | For AC frequency verification |
| Oscilloscope | 100 MHz bandwidth minimum | For transient analysis |
| Calibration Certificate | Annual calibration required | All test equipment |

## 6. Safety Requirements
- **Electrical Power Quality**
  - Never exceed maximum transient voltage limits
  - Monitor power quality continuously during ground operations
  - Automatic disconnection if voltage exceeds limits
  - Verify neutral bonding for AC systems

- **H2 Aircraft Specific**
  - Enhanced voltage stability required during H2 fueling operations
  - Backup power available during critical H2 system operations
  - Voltage monitoring systems must be intrinsically safe rated
  - Emergency power disconnection capability within 100ms

- **Testing and Verification**
  - Perform voltage verification before each aircraft connection
  - Annual certification of GSE voltage regulation systems
  - Quarterly power quality audits for airport GSE fleet
  - Immediate removal from service if voltage standards not met

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 24 (Electrical Power)
  - ATA 42 (Integrated Modular Avionics)
  - ATA 28 (Fuel - H2 System Power Requirements)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related Interface: [03-00-05-01-01A_GPU_Aircraft_Connection](./03-00-05-01-01A_GPU_Aircraft_Connection.md)
- Related Interface: [03-00-05-01-02A_Ground_Power_Receptacles](./03-00-05-01-02A_Ground_Power_Receptacles.md)

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
