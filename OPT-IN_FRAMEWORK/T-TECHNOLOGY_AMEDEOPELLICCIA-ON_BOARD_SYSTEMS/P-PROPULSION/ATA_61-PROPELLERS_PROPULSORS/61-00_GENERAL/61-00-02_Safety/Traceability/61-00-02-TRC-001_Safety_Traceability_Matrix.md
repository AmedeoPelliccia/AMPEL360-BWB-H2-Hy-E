# 61-00-02-TRC-001 — Safety Traceability Matrix

## Document Information

- **Document ID**: 61-00-02-TRC-001
- **Title**: Safety Traceability Matrix — Propulsor System
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Safety / Traceability
- **ATA Chapter**: 61 — Propellers/Propulsors

---

## 1. Purpose

This document provides the **Safety Traceability Matrix** for the ATA 61 Propellers/Propulsors domain within the AMPEL360 Q100 BWB H2/Hybrid-Electric aircraft.

The matrix establishes bidirectional traceability between:

- Top-level regulatory requirements ([CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27), [14 CFR Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25))
- Hazards identified in the SFHA
- Safety requirements derived in the PSSA
- Design features and mitigations
- Verification evidence

The matrix supports compliance demonstration and change impact analysis per [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/).

---

## 2. Scope

### 2.1 Coverage

This matrix covers:

- All hazards from [61-00-02-SFHA-001](../SFHA/61-00-02-SFHA-001_Propulsor_System_Hazards.md)
- All safety requirements from [61-00-02-PSSA-001](../PSSA/61-00-02-PSSA-001_Preliminary_Safety_Assessment.md)
- Key design features implementing safety requirements
- Planned verification activities

### 2.2 Traceability Directions

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     Traceability Flow                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐ │
│   │ Regulatory │───▶│   Hazard   │───▶│   Safety   │───▶│   Design   │ │
│   │   Reqs     │    │            │    │    Reqs    │    │  Features  │ │
│   └────────────┘    └────────────┘    └────────────┘    └────────────┘ │
│         │                 │                 │                 │         │
│         └─────────────────┴─────────────────┴─────────────────┘         │
│                                     │                                   │
│                                     ▼                                   │
│                            ┌────────────────┐                           │
│                            │  Verification  │                           │
│                            │    Evidence    │                           │
│                            └────────────────┘                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Regulatory Requirements Mapping

### 3.1 CS-25 / 14 CFR Part 25 Requirements

| Reg ID | Requirement | ATA 61 Applicability | Hazard Link | Safety Req Link |
|--------|-------------|---------------------|-------------|-----------------|
| CS-25.1309(a) | Equipment and systems must function properly | Propulsor function | All | All SR-61-xxx |
| CS-25.1309(b) | Failure condition probability objectives | Loss of thrust, asymmetric thrust | H-61-001, H-61-002 | SR-61-001 to SR-61-004 |
| CS-25.1309(c) | Warning and annunciation | Propulsor failures | H-61-010 | SR-61-018 |
| CS-25.571 | Damage-tolerance and fatigue evaluation | Blade/hub fatigue | H-61-006 | SR-61-014 |
| CS-25.631 | Bird strike damage | Blade/inlet damage | H-61-006 | SR-61-007, SR-61-008 |
| CS-25.863 | Fire protection | Motor/inverter fire | H-61-005 | Fire detection/suppression |
| CS-25.1305 | Powerplant instruments | Health monitoring | H-61-010 | SR-61-018 |
| CS-25.1337 | Powerplant instruments | Speed indication | H-61-004 | SR-61-012 |
| CS-25.1141 | Powerplant controls | Thrust control | H-61-007, H-61-008 | SR-61-010 |
| CS-25.1163 | Powerplant accessories | Cooling system | H-61-012 | SR-61-016 |

---

## 4. Hazard to Safety Requirement Traceability

### 4.1 Forward Traceability (Hazard → Requirement)

| Hazard ID | Hazard Description | Severity | Safety Requirements |
|-----------|-------------------|----------|---------------------|
| H-61-001 | Loss of all propulsor thrust | CAT | SR-61-001, SR-61-002 |
| H-61-002 | Asymmetric thrust — uncontrollable | HAZ | SR-61-003, SR-61-004 |
| H-61-003 | Single propulsor failure | MAJ | (Inherent in architecture) |
| H-61-004 | Propulsor overspeed | HAZ | SR-61-005, SR-61-006, SR-61-012, SR-61-013 |
| H-61-005 | Propulsor fire | HAZ | (Fire protection per CS-25.863) |
| H-61-006 | Blade release | HAZ | SR-61-006, SR-61-007, SR-61-008, SR-61-014, SR-61-015 |
| H-61-007 | Loss of thrust control | HAZ | SR-61-010 |
| H-61-008 | Uncommanded thrust increase | HAZ | SR-61-010, SR-61-013 |
| H-61-009 | Uncommanded thrust decrease | MAJ | SR-61-010 |
| H-61-010 | Loss of health monitoring | MAJ | SR-61-018 |
| H-61-011 | Motor overtemperature | MAJ | SR-61-016, SR-61-017 |
| H-61-012 | Cooling system failure | MAJ | SR-61-016 |

### 4.2 Reverse Traceability (Requirement → Hazard)

| Req ID | Requirement | Source Hazards |
|--------|-------------|----------------|
| SR-61-001 | No single failure causes loss of all thrust | H-61-001 |
| SR-61-002 | Two independent power sources | H-61-001 |
| SR-61-003 | Physical separation prevents multi-unit damage | H-61-002 |
| SR-61-004 | Controllability with any two propulsors inoperative | H-61-002 |
| SR-61-005 | Two independent overspeed protections | H-61-004 |
| SR-61-006 | Blades contain failures up to 120% overspeed | H-61-004, H-61-006 |
| SR-61-007 | Nacelle contains blade fragments at max speed | H-61-006 |
| SR-61-008 | Blade release affects max one propulsor | H-61-006 |
| SR-61-010 | PCU dual-channel with cross-monitoring | H-61-007, H-61-008, H-61-009 |
| SR-61-011 | Motor phase winding isolation | H-61-001 |
| SR-61-012 | Triplicated speed sensors with voting | H-61-004 |
| SR-61-013 | Hardware overspeed independent of software | H-61-004, H-61-008 |
| SR-61-014 | Blade safe-life requirements per CS-25.571 | H-61-006 |
| SR-61-015 | Containment validated by rig test | H-61-006 |
| SR-61-016 | Cooling failure triggers power reduction | H-61-011, H-61-012 |
| SR-61-017 | Redundant motor temperature monitoring | H-61-011 |
| SR-61-018 | Health monitoring detects impending failures | H-61-010 |

---

## 5. Safety Requirement to Design Feature Traceability

| Req ID | Requirement | Design Feature(s) | Component Ref |
|--------|-------------|-------------------|---------------|
| SR-61-001 | No single failure causes loss of all thrust | 4 independent propulsor units | 61-20-xx |
| SR-61-002 | Two independent power sources | FC1 + FC2 + Battery feeds | ATA 24 |
| SR-61-003 | Physical separation | Propulsors on separate pylons (5m+ separation) | ATA 54 |
| SR-61-004 | N-2 controllability | Flight control authority sizing | ATA 22 |
| SR-61-005 | Two independent overspeed protections | HW trip circuit + SW monitor | 61-20-04 PCU |
| SR-61-006 | Blade containment at 120% overspeed | Blade design, material selection | 61-20-03 |
| SR-61-007 | Nacelle blade containment | Kevlar/composite containment ring | 61-50 Structures |
| SR-61-008 | Single propulsor damage limit | Separation distance, containment | 61-50, 54 |
| SR-61-010 | PCU dual-channel | Channel A + Channel B architecture | 61-20-04 |
| SR-61-011 | Motor winding isolation | Independent phase connections | 61-20-01 |
| SR-61-012 | Triplicated speed sensors | 3× Hall effect / resolver sensors | 61-20-06 |
| SR-61-013 | Hardware overspeed trip | Dedicated comparator circuit | 61-20-04 |
| SR-61-014 | Blade safe-life design | Fatigue analysis, inspection intervals | 61-20-03 |
| SR-61-015 | Containment rig test | Test article, spin pit facility | V&V |
| SR-61-016 | Cooling failure response | Temperature-based power limiting | 61-20-05, 61-40 |
| SR-61-017 | Redundant temperature sensors | 2× motor temp sensors per unit | 61-20-06 |
| SR-61-018 | Health monitoring | Vibration, current, temp trending | 61-20-06, 61-40 |

---

## 6. Verification Matrix

### 6.1 Verification Methods

| Method Code | Description |
|-------------|-------------|
| A | Analysis (calculation, simulation) |
| T | Test (ground, flight, rig) |
| I | Inspection (review, audit) |
| D | Demonstration (functional demo) |

### 6.2 Safety Requirement Verification

| Req ID | Requirement Summary | V&V Method | V&V Activity | Status |
|--------|---------------------|------------|--------------|--------|
| SR-61-001 | No single failure loss of all thrust | A, T | FTA, Ground test | Open |
| SR-61-002 | Independent power sources | A, I | Power distribution analysis, design review | Open |
| SR-61-003 | Physical separation | A, I | Zonal analysis, drawing review | Open |
| SR-61-004 | N-2 controllability | A, T | Flight dynamics simulation, flight test | Open |
| SR-61-005 | Independent overspeed protections | A, T | FMEA, functional test | Open |
| SR-61-006 | Blade containment at 120% | A, T | Stress analysis, spin pit test | Open |
| SR-61-007 | Nacelle blade containment | A, T | Finite element analysis, blade-off test | Open |
| SR-61-008 | Single propulsor damage limit | A, I | Damage analysis, design review | Open |
| SR-61-010 | PCU dual-channel | A, T, I | Architecture analysis, FMEA, channel test | Open |
| SR-61-011 | Motor winding isolation | I, T | Design inspection, HiPot test | Open |
| SR-61-012 | Triplicated speed sensors | A, T | FMEA, sensor fault injection test | Open |
| SR-61-013 | Hardware overspeed trip | T | Functional test, failure injection | Open |
| SR-61-014 | Blade safe-life | A, I | Fatigue analysis, material review | Open |
| SR-61-015 | Containment rig test | T | Spin pit blade release test | Open |
| SR-61-016 | Cooling failure response | A, T | Thermal simulation, functional test | Open |
| SR-61-017 | Redundant temperature sensors | I, T | Design review, sensor test | Open |
| SR-61-018 | Health monitoring capability | A, T, D | Algorithm development, demo | Open |

---

## 7. Analysis Document Traceability

### 7.1 Safety Analysis Documents

| Doc ID | Document Title | Hazards Covered | Requirements Verified |
|--------|---------------|-----------------|----------------------|
| 61-00-02-SFHA-001 | [Propulsor System Hazards](../SFHA/61-00-02-SFHA-001_Propulsor_System_Hazards.md) | H-61-001 to H-61-012 | — |
| 61-00-02-PSSA-001 | [Preliminary Safety Assessment](../PSSA/61-00-02-PSSA-001_Preliminary_Safety_Assessment.md) | H-61-001 to H-61-012 | SR-61-001 to SR-61-018 |
| 61-00-02-FTA-001 | [Propulsor Failure Trees](../FTA/61-00-02-FTA-001_Propulsor_Failure_Trees.md) | H-61-001, H-61-002, H-61-004 | SR-61-001, SR-61-005 |
| 61-00-02-FMEA-001 | [Component Failure Modes](../FMEA/61-00-02-FMEA-001_Component_Failure_Modes.md) | H-61-003 to H-61-012 | Multiple |
| 61-00-02-CCA-001 | [Common Cause Analysis](../CCA/61-00-02-CCA-001_Common_Cause_Analysis.md) | H-61-001, H-61-002 | SR-61-001, SR-61-003 |

### 7.2 External Analysis References

| Analysis Type | External Document | ATA 61 Interface |
|--------------|-------------------|------------------|
| Power loss probability | ATA 24 FTA | Input to H-61-001 analysis |
| Control authority | ATA 22 Analysis | Supports SR-61-004 verification |
| Structural containment | ATA 54 Stress Analysis | Supports SR-61-007, SR-61-008 |
| Thermal analysis | ATA 21/28 Interface | Supports SR-61-016 verification |

---

## 8. Compliance Matrix Summary

### 8.1 CS-25.1309 Compliance

| Paragraph | Requirement | ATA 61 Evidence | Status |
|-----------|-------------|-----------------|--------|
| (a) | Proper function | SFHA shows all functions identified | Open |
| (b)(1) | CAT < 10⁻⁹ | FTA TE-61-001 | Open |
| (b)(2) | HAZ < 10⁻⁷ | FTA TE-61-002, TE-61-003 | Open |
| (b)(3) | MAJ < 10⁻⁵ | FMEA severity III analysis | Open |
| (c) | Warning information | Health monitoring requirements | Open |
| (d) | Crew action feasibility | TBD | Open |

### 8.2 Hazard Closure Status

| Hazard ID | Severity | Analysis Complete | Requirements Defined | Design Verified | Closed |
|-----------|----------|-------------------|---------------------|-----------------|--------|
| H-61-001 | CAT | Partial | Yes | No | No |
| H-61-002 | HAZ | Partial | Yes | No | No |
| H-61-003 | MAJ | Yes | Yes (inherent) | No | No |
| H-61-004 | HAZ | Partial | Yes | No | No |
| H-61-005 | HAZ | Partial | TBD | No | No |
| H-61-006 | HAZ | Partial | Yes | No | No |
| H-61-007 | HAZ | Partial | Yes | No | No |
| H-61-008 | HAZ | Partial | Yes | No | No |
| H-61-009 | MAJ | Partial | Yes | No | No |
| H-61-010 | MAJ | Partial | Yes | No | No |
| H-61-011 | MAJ | Partial | Yes | No | No |
| H-61-012 | MAJ | Partial | Yes | No | No |

---

## 9. Change Impact Matrix

When a change occurs, use this matrix to identify affected items:

### 9.1 If a Hazard Changes

| Changed Hazard | Update Required |
|----------------|-----------------|
| Severity change | Re-evaluate safety requirements, DAL allocation |
| New hazard | Add to SFHA, derive requirements, update FTA/FMEA |
| Hazard removed | Document justification, update traceability |

### 9.2 If a Requirement Changes

| Changed Requirement | Update Required |
|--------------------|-----------------|
| New requirement | Identify design feature, plan verification |
| Requirement deleted | Update hazard analysis, justify removal |
| Requirement modified | Re-verify affected design features |

### 9.3 If Design Changes

| Design Change | Update Required |
|---------------|-----------------|
| Architecture change | Re-run FTA, CCA |
| Component change | Update FMEA, re-verify requirements |
| Interface change | Assess impact on other ATA chapters |

---

## 10. Open Items and Action Tracking

| Item ID | Description | Owner | Status | Target Date |
|---------|-------------|-------|--------|-------------|
| TRC-OI-001 | Complete FTA probability calculations | Safety | Open | TBD |
| TRC-OI-002 | Define fire protection requirements | Systems | Open | TBD |
| TRC-OI-003 | Confirm power distribution independence | Electrical | Open | TBD |
| TRC-OI-004 | Define containment test plan | V&V | Open | TBD |
| TRC-OI-005 | Complete FMEA for all components | Safety | Open | TBD |
| TRC-OI-006 | Document CCA conclusions | Safety | Open | TBD |

---

## 11. References

### Internal References

- [61-00-02-SFHA-001 Propulsor System Hazards](../SFHA/61-00-02-SFHA-001_Propulsor_System_Hazards.md)
- [61-00-02-PSSA-001 Preliminary Safety Assessment](../PSSA/61-00-02-PSSA-001_Preliminary_Safety_Assessment.md)
- [61-00-02-FTA-001 Propulsor Failure Trees](../FTA/61-00-02-FTA-001_Propulsor_Failure_Trees.md)
- [61-00-02-FMEA-001 Component Failure Modes](../FMEA/61-00-02-FMEA-001_Component_Failure_Modes.md)
- [61-00-02-CCA-001 Common Cause Analysis](../CCA/61-00-02-CCA-001_Common_Cause_Analysis.md)

### External Standards

- [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/) — Guidelines for Development of Civil Aircraft and Systems
- [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) — Guidelines and Methods for Conducting the Safety Assessment Process
- [EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) — Certification Specifications for Large Aeroplanes
- [FAA 14 CFR Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) — Airworthiness Standards: Transport Category Airplanes

---

## 12. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
