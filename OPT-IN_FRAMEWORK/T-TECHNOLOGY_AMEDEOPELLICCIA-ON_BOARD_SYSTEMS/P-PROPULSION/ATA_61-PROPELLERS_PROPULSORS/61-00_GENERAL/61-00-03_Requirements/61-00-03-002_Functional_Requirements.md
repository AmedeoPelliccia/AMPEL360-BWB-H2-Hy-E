# 61-00-03-002 Functional Requirements

**Document ID:** 61-00-03-002  
**Title:** Propulsor System Functional Requirements Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** 0.1  
**Status:** DRAFT

---

## 1. Purpose

This document defines the **functional requirements** for the Q100 Propulsor System, establishing the functional decomposition and allocation of propulsor capabilities to system components.

---

## 2. Scope

### 2.1 Functional Scope

This document covers the following propulsor functions:
* Thrust generation from electrical power
* Thrust modulation and control
* Thrust reversal
* Regenerative braking
* Health monitoring and diagnostics

### 2.2 Exclusions

* Power generation functions (ATA 24)
* Flight control law functions (ATA 27)
* Structural functions (ATA 54)

---

## 3. Reference Documents

| ID | Title |
|----|-------|
| 61-00-03-001 | System Requirements Specification |
| TLARS-Q100 | Top Level Aircraft Requirements Specification |
| ARC-Q100 | Aircraft Requirements Cascade |
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | EASA Certification Specifications |

---

## 4. Functional Requirements

### 4.1 Thrust Generation

| Req ID | Requirement | Rationale | Verification | Allocation |
|--------|-------------|-----------|--------------|------------|
| FUNC-61-001 | The propulsor system shall generate thrust from electrical power input. | Primary function | Test | Motor, Fan |
| FUNC-61-002 | The propulsor system shall convert 800 VDC electrical power to mechanical shaft power. | Electrical architecture | Test | Motor |
| FUNC-61-003 | The propulsor system shall accelerate air mass through the fan stage to produce thrust. | Propulsion physics | Test | Fan |

### 4.2 Thrust Modulation

| Req ID | Requirement | Rationale | Verification | Allocation |
|--------|-------------|-----------|--------------|------------|
| FUNC-61-004 | The propulsor system shall modulate thrust per flight control commands. | Flight control integration | Test | Controller |
| FUNC-61-005 | The propulsor system shall accept thrust commands via AFDX interface from the flight control system. | Interface standardization | Test | Controller |
| FUNC-61-006 | The propulsor system shall provide continuous thrust modulation from idle to maximum. | Operational flexibility | Test | Controller, Motor |

### 4.3 Thrust Reversal

| Req ID | Requirement | Rationale | Verification | Allocation |
|--------|-------------|-----------|--------------|------------|
| FUNC-61-007 | The propulsor system shall provide thrust reversal capability. | Landing performance | Test | Reverser |
| FUNC-61-008 | The propulsor system shall transition from forward to reverse thrust within 2 seconds. | Operational requirement | Test | Reverser, Controller |
| FUNC-61-009 | The propulsor system shall provide at least 40% of maximum forward thrust in reverse mode. | Stopping distance | Test | Reverser |

### 4.4 Regenerative Braking

| Req ID | Requirement | Rationale | Verification | Allocation |
|--------|-------------|-----------|--------------|------------|
| FUNC-61-010 | The propulsor system shall support regenerative braking mode during descent. | Energy efficiency | Test | Motor, Controller |
| FUNC-61-011 | The propulsor system shall recover up to 500 kW per unit during regenerative braking. | Energy recovery target | Test | Motor |
| FUNC-61-012 | Regenerative braking shall be automatically disabled when battery SOC exceeds 95%. | Battery protection | Test | Controller |

### 4.5 Health Monitoring

| Req ID | Requirement | Rationale | Verification | Allocation |
|--------|-------------|-----------|--------------|------------|
| FUNC-61-013 | The propulsor system shall continuously monitor motor temperature. | Thermal protection | Test | Health Monitoring |
| FUNC-61-014 | The propulsor system shall continuously monitor bearing vibration levels. | Predictive maintenance | Test | Health Monitoring |
| FUNC-61-015 | The propulsor system shall provide fault codes to the aircraft maintenance system. | Troubleshooting | Test | Health Monitoring |

### 4.6 Windmilling and Feathering

| Req ID | Requirement | Rationale | Verification | Allocation |
|--------|-------------|-----------|--------------|------------|
| FUNC-61-016 | The propulsor shall incorporate a windmill brake or feathering capability to minimize drag with motor failure. | Failed engine drag | Test | Fan, Controller |

---

## 5. Functional Allocation Matrix

| Function | Motor | Fan | Controller | Reverser | Health Mon. |
|----------|-------|-----|------------|----------|-------------|
| Thrust generation | ● | ● | ○ | — | — |
| Thrust modulation | ● | — | ● | — | — |
| Thrust reversal | ○ | — | ● | ● | — |
| Regenerative braking | ● | — | ● | — | — |
| Health monitoring | ○ | ○ | ○ | ○ | ● |

Legend: ● Primary, ○ Supporting, — Not applicable

---

## 6. Traceability

### 6.1 Upstream (Source)

| Source | Document |
|--------|----------|
| [[61-00-03-001_System_Requirements]] | System Requirements |
| TLARS-Q100 | Top Level Aircraft Requirements |
| ARC-Q100 | Aircraft Requirements Cascade |

### 6.2 Downstream (Allocation)

| Target | Document |
|--------|----------|
| [[61-00-04_Design]] | Design specifications |
| [[61-00-05_Interfaces]] | Interface control documents |
| [[61-00-07_V_AND_V]] | Verification plans |

---

## 7. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-Q1 | TBD | Initial draft |

---

← [[61-00-03-001_System_Requirements]] · [[61-00-03-003_Performance_Requirements]] →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Functional Requirements  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
