# 61-00-02-FMEA-001 — Component Failure Modes

## Document Information

- **Document ID**: 61-00-02-FMEA-001
- **Title**: Failure Modes and Effects Analysis — Propulsor Components
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Safety / FMEA
- **ATA Chapter**: 61 — Propellers/Propulsors

---

## 1. Purpose

This document presents the **Failure Modes and Effects Analysis (FMEA)** for the ATA 61 Propellers/Propulsors components within the AMPEL360 Q100 BWB H2/Hybrid-Electric aircraft.

The FMEA:

- Identifies potential failure modes for each propulsor component
- Analyzes local, system, and aircraft-level effects
- Determines failure detection methods and compensating provisions
- Supports the PSSA and FTA analyses

The analysis follows [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) and [SAE J1739](https://www.sae.org/standards/content/j1739_200901/) methodology.

---

## 2. Scope

### 2.1 Components Analyzed

The FMEA covers the following ATA 61 components:

| Component ID | Component Name | Reference |
|--------------|----------------|-----------|
| 61-20-01 | Electric Motor | [61-20-01 Subsystem](../../61-20_Subsystems/61-20-01_Electric_Motor/) |
| 61-20-02 | Ducted Fan Assembly | [61-20 Subsystems](../../61-20_Subsystems/) |
| 61-20-03 | Blade System | [61-20-03 Blade System](../../61-20_Subsystems/61-20-03_Blade_System/) |
| 61-20-04 | Propulsor Control Unit | [61-20-04 PCU](../../61-20_Subsystems/61-20-04_Propulsor_Control_Unit/) |
| 61-20-05 | Cooling Loop | [61-20-05 Cooling](../../61-20_Subsystems/61-20-05_Cooling_Loop/) |
| 61-20-06 | Health Sensing | [61-20-06 Sensing](../../61-20_Subsystems/61-20-06_Health_Sensing/) |

### 2.2 FMEA Level

- **Level**: Component-level FMEA (Item-level)
- **Depth**: Major component failure modes

---

## 3. FMEA Methodology

### 3.1 Severity Classification

| Severity | Description | Classification |
|----------|-------------|----------------|
| I | Catastrophic — May cause death or loss of aircraft | CAT |
| II | Critical — May cause severe injury or major system damage | HAZ |
| III | Marginal — May cause minor injury or system degradation | MAJ |
| IV | Minor — May cause inconvenience or non-mission impact | MIN |

### 3.2 Probability Levels

| Level | Description | Probability Range |
|-------|-------------|------------------|
| A | Frequent | > 1×10⁻³ /FH |
| B | Reasonably Probable | 1×10⁻⁵ to 1×10⁻³ /FH |
| C | Remote | 1×10⁻⁷ to 1×10⁻⁵ /FH |
| D | Extremely Remote | 1×10⁻⁹ to 1×10⁻⁷ /FH |
| E | Extremely Improbable | < 1×10⁻⁹ /FH |

### 3.3 Risk Priority

| Risk | Severity I | Severity II | Severity III | Severity IV |
|------|-----------|-------------|--------------|-------------|
| Prob A | 1 | 3 | 7 | 13 |
| Prob B | 2 | 5 | 9 | 16 |
| Prob C | 4 | 6 | 11 | 18 |
| Prob D | 8 | 10 | 14 | 19 |
| Prob E | 12 | 15 | 17 | 20 |

---

## 4. Electric Motor (61-20-01) FMEA

### 4.1 Stator Failures

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-EM-001 | Open circuit in stator winding | Insulation breakdown, thermal damage | Loss of motor phase | Reduced motor power | Reduced thrust from one propulsor | III | C | Current monitoring, torque ripple | Remaining 3 propulsors |
| FM-EM-002 | Short circuit in stator winding | Insulation failure | Motor overheating | Motor shutdown | Loss of one propulsor | III | C | Overcurrent protection | Remaining 3 propulsors |
| FM-EM-003 | Ground fault | Insulation degradation | Current path to ground | Motor shutdown | Loss of one propulsor | III | C | Ground fault detection | Remaining 3 propulsors |

### 4.2 Rotor Failures

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-EM-010 | Rotor imbalance | Magnet detachment, wear | Vibration | Motor degradation | Reduced propulsor life | IV | C | Vibration monitoring | Maintenance action |
| FM-EM-011 | Rotor demagnetization | Thermal overload | Reduced torque | Reduced motor power | Reduced thrust | III | D | Torque monitoring | Power management |
| FM-EM-012 | Rotor seizure | Bearing failure | Motor locked | Complete motor failure | Loss of one propulsor | III | D | Speed sensing, current spike | Remaining 3 propulsors |

### 4.3 Bearing Failures

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-EM-020 | Bearing wear | Normal wear, contamination | Increased friction | Motor overheating | Reduced efficiency | IV | B | Temperature, vibration | Scheduled replacement |
| FM-EM-021 | Bearing seizure | Lubrication failure | Rotor locked | Motor failure | Loss of one propulsor | III | D | Speed monitoring | Remaining 3 propulsors |
| FM-EM-022 | Bearing cage failure | Fatigue, overload | Vibration, noise | Potential motor damage | Reduced propulsor life | III | D | Vibration monitoring | Maintenance action |

---

## 5. Ducted Fan Assembly (61-20-02) FMEA

### 5.1 Fan Failures

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-FAN-001 | Blade tip rub | Thermal expansion, assembly error | Efficiency loss, heating | Reduced thrust | Performance reduction | IV | C | Temperature monitoring | Maintenance action |
| FM-FAN-002 | Stator vane damage | FOD, erosion | Aerodynamic loss | Reduced efficiency | Minor thrust reduction | IV | B | Visual inspection | Scheduled maintenance |
| FM-FAN-003 | Hub crack | Fatigue, overload | Potential blade release | Fan failure | Loss of one propulsor | II | D | Inspection, strain sensors | Containment, 3 propulsors |

### 5.2 Nacelle Failures

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-NAC-001 | Nacelle inlet damage | FOD, bird strike | Flow distortion | Reduced efficiency | Minor performance loss | IV | B | Visual inspection | Continue operation |
| FM-NAC-002 | Acoustic liner degradation | Wear, contamination | Increased noise | Regulatory concern | Noise limit exceedance | IV | B | Noise monitoring | Maintenance |
| FM-NAC-003 | Nacelle structural failure | Overload, fatigue | Loss of containment | Potential cascading damage | Possible damage to adjacent systems | II | D | Structural monitoring | Design margin |

---

## 6. Blade System (61-20-03) FMEA

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-BLD-001 | Blade erosion | Rain, sand, FOD | Reduced efficiency | Thrust reduction | Performance degradation | IV | B | Visual inspection | Maintenance |
| FM-BLD-002 | Blade crack | Fatigue, FOD | Potential blade release | Containment challenge | HAZ if uncontained | II | D | NDI, strain sensing | Safe-life design |
| FM-BLD-003 | Blade separation | Fatigue, overload, FOD | Blade release | Containment activation | HAZ if uncontained | II | D | NDI, health monitoring | Containment design |
| FM-BLD-004 | Blade delamination | Manufacturing defect, fatigue | Structural weakness | Potential failure | Depends on progression | III | D | NDI, strain sensing | Damage tolerance |
| FM-BLD-005 | Blade foreign object damage | Bird strike, debris | Surface damage | Possible failure | Depends on severity | III | B | Visual, vibration | Inspection, replacement |

---

## 7. Propulsor Control Unit (61-20-04) FMEA

### 7.1 Channel A Failures

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-PCU-001 | Channel A processor failure | Hardware fault | Loss of channel A | Channel B takeover | No immediate effect | IV | C | Built-in test, cross-check | Channel B active |
| FM-PCU-002 | Channel A power supply failure | Component failure | Channel A inoperative | Channel B takeover | No immediate effect | IV | C | Voltage monitoring | Channel B active |
| FM-PCU-003 | Channel A software halt | Software error | Channel A inoperative | Channel B takeover | No immediate effect | IV | C | Watchdog timer | Channel B active |

### 7.2 Common Mode Failures

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-PCU-010 | Both channels fail | CCF, power loss | PCU inoperative | Propulsor shutdown | Loss of one propulsor | III | D | System monitoring | Remaining 3 propulsors |
| FM-PCU-011 | Erroneous speed command | Software error | Wrong thrust | Potential overspeed/underspeed | Safety concern | II | D | Range checking, cross-compare | Overspeed protection |
| FM-PCU-012 | Loss of communication | Bus failure | No commands received | Propulsor to safe state | Loss of one propulsor | III | D | Communication timeout | Remaining 3 propulsors |

### 7.3 Power Electronics Failures

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-PE-001 | Inverter IGBT short | Thermal, overvoltage | Phase short | Motor damage | Loss of one propulsor | III | C | Overcurrent detection | Remaining 3 propulsors |
| FM-PE-002 | Inverter IGBT open | Wear, thermal | Phase loss | Reduced power | Reduced thrust | III | C | Current monitoring | Power derating |
| FM-PE-003 | DC link capacitor failure | Thermal, overvoltage | Voltage ripple | Power instability | Performance reduction | III | D | Voltage monitoring | Derating, maintenance |

---

## 8. Cooling Loop (61-20-05) FMEA

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-CL-001 | Coolant pump failure | Mechanical wear | Loss of coolant flow | Motor overheating | Power reduction | III | C | Flow sensor, pressure | Backup pump, power limit |
| FM-CL-002 | Coolant leak | Seal failure, damage | Loss of coolant | Gradual overheating | Power reduction | III | C | Level sensor, temp rise | Top-up, maintenance |
| FM-CL-003 | Heat exchanger fouling | Contamination | Reduced cooling | Higher temperatures | Efficiency loss | IV | B | Temperature differential | Maintenance |
| FM-CL-004 | Coolant contamination | System breach | Reduced heat transfer | Overheating risk | Power reduction | III | D | Coolant analysis | Coolant replacement |
| FM-CL-005 | Cooling control failure | Sensor/valve fault | Wrong coolant flow | Temperature excursion | Power reduction | III | C | Temperature monitoring | Backup control mode |

---

## 9. Health Sensing (61-20-06) FMEA

| ID | Failure Mode | Cause | Local Effect | System Effect | Aircraft Effect | Severity | Prob | Detection | Compensating Provision |
|----|--------------|-------|--------------|---------------|-----------------|----------|------|-----------|----------------------|
| FM-HS-001 | Speed sensor failure | Wear, contamination | No speed signal | Reliance on remaining sensors | Reduced redundancy | IV | C | Cross-compare, BIT | Triplicated sensors |
| FM-HS-002 | Temperature sensor failure | Drift, open circuit | No/wrong temp signal | Thermal protection affected | Potential overtemp | III | C | Range check, redundancy | Multiple sensors |
| FM-HS-003 | Vibration sensor failure | Mechanical damage | No vibration data | Loss of health monitoring | No early warning | III | C | Signal quality check | Periodic inspection |
| FM-HS-004 | Current sensor failure | Drift, saturation | Wrong current reading | Power control affected | Performance impact | III | C | Cross-compare | Redundant sensing |
| FM-HS-005 | All sensors CCF | Common power, common board | Loss of all sensing | No health data | Safety concern | II | D | Independent supplies | Hardware diversity |

---

## 10. FMEA Summary

### 10.1 Failure Mode Count by Severity

| Component | Severity I | Severity II | Severity III | Severity IV | Total |
|-----------|-----------|-------------|--------------|-------------|-------|
| Electric Motor | 0 | 0 | 6 | 3 | 9 |
| Ducted Fan | 0 | 2 | 0 | 4 | 6 |
| Blade System | 0 | 2 | 2 | 1 | 5 |
| PCU | 0 | 1 | 5 | 6 | 12 |
| Cooling Loop | 0 | 0 | 4 | 1 | 5 |
| Health Sensing | 0 | 1 | 3 | 1 | 5 |
| **Total** | **0** | **6** | **20** | **16** | **42** |

### 10.2 Critical Failure Modes

Failure modes with Severity II requiring special attention:

| ID | Failure Mode | Mitigation |
|----|--------------|------------|
| FM-FAN-003 | Hub crack | Safe-life design, inspection program |
| FM-NAC-003 | Nacelle structural failure | Design margin, structural monitoring |
| FM-BLD-002 | Blade crack | NDI program, strain monitoring |
| FM-BLD-003 | Blade separation | Containment design, health monitoring |
| FM-PCU-011 | Erroneous speed command | Range checking, overspeed protection |
| FM-HS-005 | All sensors CCF | Hardware diversity, independent supplies |

---

## 11. Recommendations

1. **Design improvements**:
   - Implement sensor redundancy with diversity
   - Ensure PCU channels are truly independent
   - Design robust containment for blade release

2. **Monitoring enhancements**:
   - Add continuous blade health monitoring
   - Implement predictive maintenance algorithms
   - Enhance temperature monitoring coverage

3. **Maintenance considerations**:
   - Define inspection intervals based on failure modes
   - Establish on-condition monitoring requirements
   - Develop troubleshooting procedures for each failure mode

---

## 12. References

### Internal References

- [61-00-02-SFHA-001 Propulsor System Hazards](../SFHA/61-00-02-SFHA-001_Propulsor_System_Hazards.md)
- [61-00-02-PSSA-001 Preliminary Safety Assessment](../PSSA/61-00-02-PSSA-001_Preliminary_Safety_Assessment.md)
- [61-00-02-FTA-001 Propulsor Failure Trees](../FTA/61-00-02-FTA-001_Propulsor_Failure_Trees.md)
- [61-20 Subsystems](../../61-20_Subsystems/)

### External Standards

- [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) — Guidelines and Methods for Conducting the Safety Assessment Process
- [SAE J1739](https://www.sae.org/standards/content/j1739_200901/) — Potential Failure Mode and Effects Analysis
- [MIL-STD-1629A](https://quicksearch.dla.mil/) — Procedures for Performing a Failure Mode, Effects and Criticality Analysis

---

## 13. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
