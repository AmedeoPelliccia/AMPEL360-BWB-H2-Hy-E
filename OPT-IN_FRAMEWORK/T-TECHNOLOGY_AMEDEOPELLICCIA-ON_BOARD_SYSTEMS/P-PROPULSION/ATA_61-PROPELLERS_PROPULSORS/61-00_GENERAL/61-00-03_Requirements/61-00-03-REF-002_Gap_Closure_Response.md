# 61-00-03-REF-002 Gap Closure Response

**Document ID:** 61-00-03-REF-002  
**Title:** Requirements Gap Closure — Independent Evaluation Response  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** 0.1  
**Status:** DRAFT  
**Reference:** Independent Evaluation Report (Dec 2025)

---

## 1. Purpose

This document provides a **formal response** to the independent evaluation of Q100 Propulsor System Requirements, addressing each identified gap with specific requirement additions or clarifications.

---

## 2. Gap Summary Matrix

| Gap ID | Finding | Severity | Status | Closure Document |
|--------|---------|----------|--------|------------------|
| GAP-01 | Hydrogen leak detection & shutdown | Critical | **CLOSED** | This document |
| GAP-02 | Battery thermal runaway protection | Critical | **CLOSED** | This document |
| GAP-03 | Single Point of Failure (SPOF) prevention | Critical | **CLOSED** | This document |
| GAP-04 | Emergency/OEI power compensation | Major | **CLOSED** | This document |
| GAP-05 | Thrust response time quantification | Major | **CLOSED** | This document |
| GAP-06 | Regenerative braking control | Major | **CLOSED** | This document |
| GAP-07 | Thermal derating specification | Major | **CLOSED** | This document |
| GAP-08 | Cooling system integration | Major | **CLOSED** | This document |
| GAP-09 | Feathering/drag mitigation | Moderate | **CLOSED** | This document |
| GAP-10 | Yaw control coordination | Major | **CLOSED** | This document |
| GAP-11 | 800V DC architecture validation | Moderate | **CLOSED** | This document |
| GAP-12 | Mass budget clarification | Moderate | **CLOSED** | REF-001 (confirmed) |
| GAP-13 | Certification traceability matrix | Administrative | **CLOSED** | Annex A |

---

## 3. New Requirements — Gap Closures

### 3.1 GAP-01: Hydrogen Leak Detection and Shutdown

**Finding:** Requirement for hydrogen leak detection and automatic shutoff not explicitly stated.

**Reference:** FAA Hydrogen Roadmap, [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) Special Conditions

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| SAFE-61-010 | The propulsor system shall include hydrogen leak detection with automatic fuel shutoff capability within 2 seconds of detection. | FAA Hydrogen Roadmap compliance | Test, Analysis |

---

### 3.2 GAP-02: Battery Thermal Runaway Protection

**Finding:** Battery thermal runaway protection requirements not specified.

**Reference:** RTCA DO-311A, CS-25 Amendment 27

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| SAFE-61-011 | The battery system shall incorporate thermal runaway detection and containment per RTCA DO-311A. | Battery safety compliance | Test, Analysis |

---

### 3.3 GAP-03: Single Point of Failure (SPOF) Prevention

**Finding:** SPOF analysis and prevention requirements not explicit.

**Reference:** CS-25.1309, ARP4761A

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| SAFE-61-012 | The propulsor control architecture shall be designed to prevent single points of failure for critical functions per CS-25.1309. | Safety architecture | Analysis |

---

### 3.4 GAP-04: Emergency/OEI Power Compensation

**Finding:** One Engine Inoperative (OEI) power compensation not quantified.

**Reference:** CS-25.121, CS-25.123

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| PERF-61-010 | With one propulsor inoperative, remaining propulsors shall provide ≥105% rated power for 5 minutes to maintain OEI climb performance. | OEI climb gradient compliance | Test |

---

### 3.5 GAP-05: Thrust Response Time Quantification

**Finding:** Thrust response time not quantified for flight control integration.

**Reference:** CS-25.143, Flight Control Interface Requirements

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| PERF-61-011 | Thrust response from idle to maximum shall be ≤2 seconds (0-95% thrust). | Go-around performance | Test |
| PERF-61-012 | Thrust modulation bandwidth shall be ≥2 Hz for flight control integration. | DEP control authority | Test |

---

### 3.6 GAP-06: Regenerative Braking Control

**Finding:** Regenerative braking during descent not addressed.

**Reference:** Electrical Architecture Specification

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| FUNC-61-010 | The propulsor system shall support regenerative braking mode during descent, recovering up to 500 kW per unit. | Energy efficiency | Test |
| FUNC-61-011 | Regenerative braking shall be automatically disabled when battery SOC exceeds 95%. | Battery protection | Test |

---

### 3.7 GAP-07: Thermal Derating Specification

**Finding:** Thermal derating curves not specified.

**Reference:** Motor thermal design requirements

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| PERF-61-013 | The propulsor shall maintain full power output up to ambient temperature of ISA+35°C. | Hot day operations | Test |
| PERF-61-014 | Above ISA+35°C, power derating shall not exceed 2% per °C. | Performance predictability | Test |

---

### 3.8 GAP-08: Cooling System Integration

**Finding:** Cooling system interface requirements not specified.

**Reference:** ATA 21 Interface, Thermal Management System

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| IFC-61-010 | The propulsor shall interface with aircraft thermal management system (ATA 21) for heat rejection of up to 200 kW per unit. | Thermal integration | Analysis, Test |

---

### 3.9 GAP-09: Feathering/Drag Mitigation

**Finding:** Windmilling/feathering requirements for failed propulsor not specified.

**Reference:** CS-25.147

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| FUNC-61-012 | The propulsor shall incorporate a windmill brake or feathering capability to minimize drag with motor failure. | Failed engine drag | Test |

---

### 3.10 GAP-10: Yaw Control Coordination

**Finding:** Yaw control coordination with asymmetric thrust not addressed.

**Reference:** CS-25.147, Flight Control Interface

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| IFC-61-011 | The propulsor control system shall provide thrust differential commands to flight control (ATA 27) for yaw control augmentation. | DEP yaw control | Analysis, Test |

---

### 3.11 GAP-11: 800V DC Architecture Validation

**Finding:** 800V DC architecture validation requirements not explicit.

**Reference:** SAE AS6968, DO-160G Section 16

**New Requirement:**

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| ENV-61-010 | The 800 VDC electrical interface shall comply with SAE AS6968 for high-voltage aerospace applications. | Electrical safety | Analysis, Test |

---

### 3.12 GAP-12: Mass Budget Clarification

**Status:** CLOSED — Confirmed in REF-001

The 450 kg per propulsor unit mass budget is confirmed as inclusive of:
- Electric motor: 280 kg
- Fan/propulsor stage: 85 kg
- Motor controller (PMU): 45 kg
- Structural interfaces: 40 kg

---

### 3.13 GAP-13: Certification Traceability Matrix

**Status:** CLOSED — See Annex A

---

## 4. Requirements Traceability Update

The following requirements are added to the baseline:

| Category | New Req IDs | Count |
|----------|-------------|-------|
| Safety (SAFE-61) | SAFE-61-010, SAFE-61-011, SAFE-61-012 | 3 |
| Performance (PERF-61) | PERF-61-010, PERF-61-011, PERF-61-012, PERF-61-013, PERF-61-014 | 5 |
| Functional (FUNC-61) | FUNC-61-010, FUNC-61-011, FUNC-61-012 | 3 |
| Interface (IFC-61) | IFC-61-010, IFC-61-011 | 2 |
| Environmental (ENV-61) | ENV-61-010 | 1 |
| **Total New Requirements** | | **14** |

---

## 5. Annex A: Certification Traceability Matrix

| CS-25 Requirement | Propulsor Requirement | Status |
|-------------------|----------------------|--------|
| CS-25.901 | SYS-61-005 | Covered |
| CS-25.903 | SYS-61-001, PERF-61-010 | Covered |
| CS-25.1309 | SAFE-61-012 | Covered |
| CS-25.121 | PERF-61-010 | Covered |
| CS-25.123 | PERF-61-010 | Covered |
| CS-25.143 | PERF-61-011, PERF-61-012 | Covered |
| CS-25.147 | FUNC-61-012, IFC-61-011 | Covered |
| Special Condition (H2) | SAFE-61-010 | Covered |
| Special Condition (Battery) | SAFE-61-011 | Covered |

---

## 6. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-Q1 | TBD | Initial draft responding to independent evaluation |

---

← [[61-00-03-001_System_Requirements]] · [[00_INDEX]] →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Gap Closure Response  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
