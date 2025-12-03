# 61-00-02-SFHA-001 — Propulsor System Hazards

## Document Information

- **Document ID**: 61-00-02-SFHA-001
- **Title**: System Functional Hazard Assessment — Propulsor System Hazards
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Safety / SFHA
- **ATA Chapter**: 61 — Propellers/Propulsors

---

## 1. Purpose

This document presents the **System Functional Hazard Assessment (SFHA)** for the ATA 61 Propellers/Propulsors domain within the AMPEL360 Q100 BWB H2/Hybrid-Electric aircraft.

The SFHA identifies and classifies hazards arising from:

- Failure or malfunction of propulsor functions
- Loss of propulsor performance or control
- Unintended propulsor behavior

The assessment follows [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) methodology and supports compliance with [EASA CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) / [FAA 14 CFR 25.1309](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25).

---

## 2. Scope

### 2.1 In-Scope Functions

The following propulsor functions are assessed:

| Function ID | Function Description |
|-------------|---------------------|
| F-61-001 | Provide commanded thrust |
| F-61-002 | Control thrust magnitude |
| F-61-003 | Control thrust direction (vectoring) |
| F-61-004 | Provide motor cooling |
| F-61-005 | Monitor propulsor health |
| F-61-006 | Provide emergency shutdown |
| F-61-007 | Communicate status to flight control |

### 2.2 Assessment Boundaries

- **System boundary**: Propulsor unit from electrical power input to thrust output
- **Operational phases**: All flight phases (taxi, takeoff, climb, cruise, descent, approach, landing)
- **Environmental conditions**: Per [DO-160G](https://www.rtca.org/content/standards-guidance-documents) operating envelopes

---

## 3. Hazard Classification Criteria

### 3.1 Severity Categories

Per [CS-25.1309(a)](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):

| Category | Effect on Aircraft | Effect on Occupants |
|----------|-------------------|---------------------|
| **Catastrophic (CAT)** | Hull loss | Multiple fatalities |
| **Hazardous (HAZ)** | Large reduction in safety margins | Serious injury / fatalities (small number) |
| **Major (MAJ)** | Significant reduction in safety margins | Physical distress / possible injury |
| **Minor (MIN)** | Slight reduction in safety margins | Slight inconvenience |
| **No Safety Effect (NSE)** | No effect on safety | No effect |

### 3.2 Probability Objectives

| Severity | Probability Objective |
|----------|----------------------|
| Catastrophic | < 1×10⁻⁹ per flight hour |
| Hazardous | < 1×10⁻⁷ per flight hour |
| Major | < 1×10⁻⁵ per flight hour |
| Minor | No specific requirement |

---

## 4. Propulsor Hazard Identification

### 4.1 Hazard Summary Table

| Hazard ID | Hazard Description | Failure Condition | Phase | Severity | Probability Objective |
|-----------|-------------------|-------------------|-------|----------|----------------------|
| H-61-001 | Loss of all propulsor thrust | Complete loss of thrust from all 4 propulsors | Any | CAT | < 1×10⁻⁹ |
| H-61-002 | Asymmetric thrust — uncontrollable | Loss of 2+ propulsors on same side, beyond control authority | Takeoff, Cruise | HAZ | < 1×10⁻⁷ |
| H-61-003 | Single propulsor failure | Loss of thrust from one propulsor | Any | MAJ | < 1×10⁻⁵ |
| H-61-004 | Propulsor overspeed | Motor/fan exceeds maximum rated speed | Any | HAZ | < 1×10⁻⁷ |
| H-61-005 | Propulsor fire | Uncontained thermal event in motor/controller | Any | HAZ | < 1×10⁻⁷ |
| H-61-006 | Blade release | Fan blade separates from hub | Any | HAZ | < 1×10⁻⁷ |
| H-61-007 | Loss of thrust control | Unable to modulate thrust on command | Any | HAZ | < 1×10⁻⁷ |
| H-61-008 | Uncommanded thrust increase | Propulsor delivers more thrust than commanded | Approach, Landing | HAZ | < 1×10⁻⁷ |
| H-61-009 | Uncommanded thrust decrease | Propulsor delivers less thrust than commanded | Takeoff, Climb | MAJ | < 1×10⁻⁵ |
| H-61-010 | Loss of propulsor health monitoring | No warning of degradation or impending failure | Any | MAJ | < 1×10⁻⁵ |
| H-61-011 | Motor overtemperature | Motor temperature exceeds safe limits | Any | MAJ | < 1×10⁻⁵ |
| H-61-012 | Cooling system failure | Loss of motor cooling capacity | Any | MAJ | < 1×10⁻⁵ |

---

## 5. Hazard Analysis Details

### 5.1 H-61-001: Loss of All Propulsor Thrust

**Classification**: Catastrophic

**Description**: Complete loss of thrust from all four propulsor units simultaneously, resulting in total loss of propulsive power.

**Potential Causes**:

- Common-mode failure of power electronics
- Complete loss of electrical power (ATA 24)
- Common-mode software failure in all PCUs
- Catastrophic damage to all propulsors (e.g., bird strike, foreign object damage)

**Mitigation Strategies**:

- Distributed propulsion architecture with independent power feeds
- Redundant electrical power sources (fuel cells + battery)
- Dissimilar software in PCU channels
- Physical separation of propulsor units
- Containment structures for blade/motor failures

**Safety Requirements Derived**:

- SR-61-001: The propulsion system shall be designed such that no single failure causes loss of all thrust
- SR-61-002: Electrical power to propulsors shall be provided from at least two independent sources

---

### 5.2 H-61-002: Asymmetric Thrust — Uncontrollable

**Classification**: Hazardous

**Description**: Loss of two or more propulsors on the same side of the aircraft, creating asymmetric thrust beyond the control system's ability to compensate.

**Potential Causes**:

- Zonal event (fire, explosion) affecting multiple units
- Common power bus failure
- Nacelle/pylon structural failure affecting multiple units

**Mitigation Strategies**:

- Propulsor physical separation exceeding damage tolerance requirements
- Independent power distribution to left/right propulsor groups
- Control system authority sufficient for asymmetric thrust up to N-2 configuration

**Safety Requirements Derived**:

- SR-61-003: Propulsor units shall be physically separated to prevent single-event damage to more than one unit per side
- SR-61-004: The flight control system shall maintain controllability with any two propulsors inoperative

---

### 5.3 H-61-004: Propulsor Overspeed

**Classification**: Hazardous

**Description**: Electric motor and/or fan exceeds maximum rated rotational speed, risking mechanical failure and blade release.

**Potential Causes**:

- PCU control logic failure
- Loss of speed feedback
- Electrical fault causing uncontrolled motor acceleration

**Mitigation Strategies**:

- Redundant speed sensing (min. 3 sensors per propulsor)
- Independent overspeed protection circuit (hardware-based)
- Mechanical overspeed trip mechanism
- Motor design with inherent speed limiting

**Safety Requirements Derived**:

- SR-61-005: Each propulsor shall have at least two independent overspeed protection mechanisms
- SR-61-006: Propulsor fan blades shall be designed to contain failures up to 120% overspeed

---

### 5.4 H-61-006: Blade Release

**Classification**: Hazardous

**Description**: One or more fan blades separate from the hub during operation, potentially causing secondary damage.

**Potential Causes**:

- Fatigue failure
- Foreign object damage
- Manufacturing defect
- Overspeed event

**Mitigation Strategies**:

- Blade containment structure (nacelle)
- Damage-tolerant blade design
- Blade health monitoring (vibration, strain)
- Safe-life or fail-safe blade design philosophy

**Safety Requirements Derived**:

- SR-61-007: The nacelle shall contain any blade fragment resulting from blade release at maximum rated speed
- SR-61-008: Blade release shall not result in loss of more than one propulsor

---

## 6. Hazard Log

| Hazard ID | Status | Open Items | Owner | Target Date |
|-----------|--------|------------|-------|-------------|
| H-61-001 | Open | Complete CCA for common-mode failures | Safety Lead | TBD |
| H-61-002 | Open | Validate control authority analysis | Flight Controls | TBD |
| H-61-003 | Open | Define single-engine performance | Performance | TBD |
| H-61-004 | Open | Design overspeed protection | Propulsion Design | TBD |
| H-61-005 | Open | Define fire detection/suppression | Systems Safety | TBD |
| H-61-006 | Open | Blade containment analysis | Structures | TBD |
| H-61-007 | Open | Control system FMEA | Avionics | TBD |
| H-61-008 | Open | Uncommanded thrust analysis | Controls | TBD |
| H-61-009 | Open | Thrust degradation analysis | Performance | TBD |
| H-61-010 | Open | Health monitoring architecture | Diagnostics | TBD |
| H-61-011 | Open | Thermal analysis | Thermal | TBD |
| H-61-012 | Open | Cooling system FMEA | Thermal | TBD |

---

## 7. References

### Internal References

- [61-00-02-000 Safety README](../README.md)
- [61-00-02-PSSA-001 Preliminary Safety Assessment](../PSSA/61-00-02-PSSA-001_Preliminary_Safety_Assessment.md)
- [61-00-02-FTA-001 Propulsor Failure Trees](../FTA/61-00-02-FTA-001_Propulsor_Failure_Trees.md)
- [61-00-02-TRC-001 Safety Traceability Matrix](../Traceability/61-00-02-TRC-001_Safety_Traceability_Matrix.md)
- [61-00-01-001 ATA 61 Domain Description](../../61-00-01_Overview/61-00-01-001_ATA_61_Domain_Description.md)

### External Standards

- [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) — Guidelines and Methods for Conducting the Safety Assessment Process
- [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/) — Guidelines for Development of Civil Aircraft and Systems
- [EASA CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) — Equipment, Systems, and Installations
- [FAA AC 25.1309-1A](https://www.faa.gov/regulations_policies/advisory_circulars) — System Design and Analysis

---

## 8. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
