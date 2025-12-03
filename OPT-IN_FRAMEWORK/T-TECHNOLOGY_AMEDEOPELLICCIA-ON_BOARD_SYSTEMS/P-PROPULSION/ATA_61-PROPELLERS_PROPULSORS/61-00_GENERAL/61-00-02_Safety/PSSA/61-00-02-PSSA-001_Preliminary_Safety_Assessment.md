# 61-00-02-PSSA-001 — Preliminary System Safety Assessment

## Document Information

- **Document ID**: 61-00-02-PSSA-001
- **Title**: Preliminary System Safety Assessment — Propulsor System
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Safety / PSSA
- **ATA Chapter**: 61 — Propellers/Propulsors

---

## 1. Purpose

This document presents the **Preliminary System Safety Assessment (PSSA)** for the ATA 61 Propellers/Propulsors domain within the AMPEL360 Q100 BWB H2/Hybrid-Electric aircraft.

The PSSA:

- Derives safety requirements from the SFHA hazards
- Allocates Design Assurance Levels (DAL) to system functions and items
- Identifies architectural features required to meet safety objectives
- Provides input to the system design process

The assessment follows [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) methodology and supports compliance with [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/).

---

## 2. Scope

### 2.1 System Description

The propulsor system comprises four Electric Ducted Fan (EDF) units, each containing:

- 4 MW-class electric motor
- Ducted fan assembly (rotor/stator)
- Propulsor Control Unit (PCU)
- Cooling system interface
- Health sensing suite

### 2.2 PSSA Boundaries

This PSSA covers the propulsor system from:

- **Input**: Electrical power interface (DC bus), control commands from flight control
- **Output**: Thrust force applied to aircraft structure

---

## 3. Safety Requirements Derivation

### 3.1 Top-Level Safety Requirements

Derived from SFHA hazards documented in [61-00-02-SFHA-001](../SFHA/61-00-02-SFHA-001_Propulsor_System_Hazards.md):

| Req ID | Requirement Text | Source Hazard | DAL |
|--------|------------------|---------------|-----|
| SR-61-001 | The propulsion system shall be designed such that no single failure causes loss of all thrust | H-61-001 | A |
| SR-61-002 | Electrical power to propulsors shall be provided from at least two independent sources | H-61-001 | A |
| SR-61-003 | Propulsor units shall be physically separated to prevent single-event damage to more than one unit per side | H-61-002 | A |
| SR-61-004 | The flight control system shall maintain controllability with any two propulsors inoperative | H-61-002 | A |
| SR-61-005 | Each propulsor shall have at least two independent overspeed protection mechanisms | H-61-004 | A |
| SR-61-006 | Propulsor fan blades shall be designed to contain failures up to 120% overspeed | H-61-004 | A |
| SR-61-007 | The nacelle shall contain any blade fragment resulting from blade release at maximum rated speed | H-61-006 | A |
| SR-61-008 | Blade release shall not result in loss of more than one propulsor | H-61-006 | A |

### 3.2 Derived Safety Requirements

| Req ID | Requirement Text | Parent Req | DAL |
|--------|------------------|------------|-----|
| SR-61-010 | The PCU shall implement dual-channel control with cross-monitoring | SR-61-001 | A |
| SR-61-011 | Each propulsor motor shall have independent phase winding isolation | SR-61-001 | B |
| SR-61-012 | Motor speed sensors shall be triplicated with voting logic | SR-61-005 | A |
| SR-61-013 | Hardware overspeed trip shall be independent of software control | SR-61-005 | A |
| SR-61-014 | Blade structural design shall meet safe-life requirements per [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) | SR-61-006 | A |
| SR-61-015 | Nacelle containment design shall be validated by rig test | SR-61-007 | A |
| SR-61-016 | Propulsor cooling failure shall trigger automatic power reduction | H-61-012 | B |
| SR-61-017 | Motor temperature monitoring shall be redundant with independent sensors | H-61-011 | B |
| SR-61-018 | Propulsor health monitoring shall detect impending failures with sufficient warning time | H-61-010 | C |

---

## 4. Design Assurance Level Allocation

### 4.1 DAL Assignment Rationale

Per [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/), DAL is assigned based on failure condition severity and independence of backup:

| Failure Condition Severity | Single Function (no backup) | Function with Independent Backup |
|---------------------------|----------------------------|----------------------------------|
| Catastrophic | DAL A | DAL B (each path) |
| Hazardous | DAL B | DAL C (each path) |
| Major | DAL C | DAL D (each path) |
| Minor | DAL D | No requirement |

### 4.2 Propulsor System DAL Summary

| Item | Function | Failure Condition | Backup/Redundancy | Assigned DAL |
|------|----------|------------------|-------------------|--------------|
| Propulsor Control Unit — Channel A | Thrust control | Loss of thrust control (HAZ) | Channel B | B |
| Propulsor Control Unit — Channel B | Thrust control | Loss of thrust control (HAZ) | Channel A | B |
| Speed Sensor 1 | Speed measurement | Erroneous speed (HAZ) | Sensors 2, 3 | C |
| Speed Sensor 2 | Speed measurement | Erroneous speed (HAZ) | Sensors 1, 3 | C |
| Speed Sensor 3 | Speed measurement | Erroneous speed (HAZ) | Sensors 1, 2 | C |
| Overspeed Protection (HW) | Prevent overspeed | Undetected overspeed (HAZ) | SW protection | B |
| Overspeed Protection (SW) | Prevent overspeed | Undetected overspeed (HAZ) | HW protection | B |
| Electric Motor (per unit) | Thrust generation | Loss of single propulsor (MAJ) | 3 other propulsors | C |
| Blade Assembly (per unit) | Thrust generation | Blade release (HAZ) | Containment | A (structure) |
| Cooling System Controller | Thermal management | Motor overtemp (MAJ) | Backup cooling mode | C |
| Health Monitoring System | Fault detection | Loss of monitoring (MAJ) | Backup monitoring | C |

---

## 5. Architectural Features for Safety

### 5.1 Redundancy Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     Propulsor Redundancy Architecture                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Power Sources                     Propulsor Units                     │
│   ┌───────────────┐                                                     │
│   │ Fuel Cell     │──┬──┬──┬──┬──▶ ┌─────────────┐                     │
│   │ System 1      │  │  │  │  │    │ Propulsor 1 │ (Port)              │
│   └───────────────┘  │  │  │  │    │ ├─ PCU Ch A │                     │
│                      │  │  │  │    │ ├─ PCU Ch B │                     │
│   ┌───────────────┐  │  │  │  │    │ └─ Motor    │                     │
│   │ Fuel Cell     │──┤  │  │  │    └─────────────┘                     │
│   │ System 2      │  │  │  │  │                                        │
│   └───────────────┘  │  │  │  ├──▶ ┌─────────────┐                     │
│                      │  │  │  │    │ Propulsor 2 │ (Port Inboard)      │
│   ┌───────────────┐  │  │  │  │    └─────────────┘                     │
│   │ Battery       │──┤  │  │  │                                        │
│   │ System        │  │  │  │  ├──▶ ┌─────────────┐                     │
│   └───────────────┘  │  │  │  │    │ Propulsor 3 │ (Stbd Inboard)      │
│                      │  │  │  │    └─────────────┘                     │
│                      │  │  │  │                                        │
│                      └──┴──┴──┴──▶ ┌─────────────┐                     │
│                                    │ Propulsor 4 │ (Starboard)         │
│                                    └─────────────┘                     │
│                                                                         │
│   Independence: Each propulsor can operate from any power source       │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Separation and Isolation

- **Physical separation**: Propulsors located on separate pylons with defined separation distance
- **Electrical isolation**: Independent power feeds with galvanic isolation
- **Control isolation**: Each PCU operates independently with defined command interfaces
- **Thermal isolation**: Separate cooling circuits per propulsor

### 5.3 Monitoring and Detection

- Triplicated speed sensing with voting
- Dual temperature monitoring per motor
- Vibration monitoring for blade health
- Current/voltage monitoring for electrical faults
- Cross-channel comparison in PCU for latent fault detection

---

## 6. Failure Analysis Summary

### 6.1 Quantitative Targets

| Failure Condition | Target Probability | Required Architecture |
|------------------|-------------------|----------------------|
| Loss of all thrust | < 1×10⁻⁹ | 4 independent propulsors + multiple power sources |
| Uncontrollable asymmetric thrust | < 1×10⁻⁷ | Physical separation + N-2 controllability |
| Undetected overspeed | < 1×10⁻⁷ | Dual independent protection + containment |

### 6.2 Fault Tolerance Requirements

| Number of Propulsors Lost | Aircraft Capability |
|--------------------------|---------------------|
| 0 | Full performance |
| 1 | Continued safe flight and landing; minor performance reduction |
| 2 (balanced) | Continued safe flight and landing; reduced performance |
| 2 (asymmetric) | Controllable; significant performance reduction |
| 3 | Minimum safe flight to nearest suitable airport |
| 4 | Not acceptable; design prevents this combination |

---

## 7. Interface with Other Analyses

### 7.1 Supporting Analyses

| Analysis | Document Reference | Purpose |
|----------|-------------------|---------|
| Fault Tree Analysis | [61-00-02-FTA-001](../FTA/61-00-02-FTA-001_Propulsor_Failure_Trees.md) | Quantify probability of top-level hazards |
| FMEA | [61-00-02-FMEA-001](../FMEA/61-00-02-FMEA-001_Component_Failure_Modes.md) | Identify component failure modes and effects |
| Common Cause Analysis | [61-00-02-CCA-001](../CCA/61-00-02-CCA-001_Common_Cause_Analysis.md) | Validate independence assumptions |
| Zonal Safety Analysis | TBD | Assess zonal threats to multiple propulsors |

### 7.2 Design Data Required

- Motor failure rate data
- PCU hardware failure rates
- Sensor failure rates
- Blade fatigue data
- Containment test results

---

## 8. Open Items and Assumptions

### 8.1 Assumptions

| ID | Assumption | Validation Method |
|----|------------|-------------------|
| A-61-001 | Motor failure rate < 1×10⁻⁵ per flight hour | Supplier data + test |
| A-61-002 | PCU channel failure rate < 1×10⁻⁵ per flight hour | DO-254 analysis |
| A-61-003 | Blade containment effective at max speed | Rig test |
| A-61-004 | Propulsors are sufficiently separated for independence | Zonal analysis |

### 8.2 Open Items

| ID | Item | Owner | Target Date |
|----|------|-------|-------------|
| OI-61-001 | Obtain motor failure rate data from supplier | Propulsion Lead | TBD |
| OI-61-002 | Complete FTA for loss of all thrust | Safety Lead | TBD |
| OI-61-003 | Define blade containment test plan | Structures Lead | TBD |
| OI-61-004 | Complete PCU architecture definition | Avionics Lead | TBD |

---

## 9. References

### Internal References

- [61-00-02-SFHA-001 Propulsor System Hazards](../SFHA/61-00-02-SFHA-001_Propulsor_System_Hazards.md)
- [61-00-02-FTA-001 Propulsor Failure Trees](../FTA/61-00-02-FTA-001_Propulsor_Failure_Trees.md)
- [61-00-02-CCA-001 Common Cause Analysis](../CCA/61-00-02-CCA-001_Common_Cause_Analysis.md)
- [61-00-02-TRC-001 Safety Traceability Matrix](../Traceability/61-00-02-TRC-001_Safety_Traceability_Matrix.md)

### External Standards

- [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) — Guidelines and Methods for Conducting the Safety Assessment Process
- [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/) — Guidelines for Development of Civil Aircraft and Systems
- [RTCA DO-178C](https://www.rtca.org/content/standards-guidance-documents) — Software Considerations in Airborne Systems
- [RTCA DO-254](https://www.rtca.org/content/standards-guidance-documents) — Design Assurance Guidance for Airborne Electronic Hardware
- [EASA CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) — Equipment, Systems, and Installations

---

## 10. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
