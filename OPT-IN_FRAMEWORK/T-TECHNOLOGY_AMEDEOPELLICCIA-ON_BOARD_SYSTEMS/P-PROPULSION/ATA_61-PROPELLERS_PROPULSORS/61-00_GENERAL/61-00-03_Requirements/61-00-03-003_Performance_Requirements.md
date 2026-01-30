# 61-00-03-003 Performance Requirements

**Document ID:** 61-00-03-003  
**Title:** Propulsor System Performance Requirements Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** 0.1  
**Status:** DRAFT

---

## 1. Purpose

This document defines the **quantitative performance requirements** for the Q100 Propulsor System, establishing measurable targets for power, thrust, efficiency, response, and operating conditions.

---

## 2. Scope

### 2.1 Performance Parameters

This document covers:
* Power and thrust performance
* Efficiency requirements
* Response time characteristics
* Altitude and temperature performance
* Mass and specific power targets

### 2.2 Validation Reference

Performance requirements have been validated in [[61-00-03-REF-003_Performance_Validation]].

---

## 3. Reference Documents

| ID | Title |
|----|-------|
| 61-00-03-001 | System Requirements Specification |
| 61-00-03-REF-003 | Performance Requirements Validation |
| TLARS-Q100 | Top Level Aircraft Requirements Specification |
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | EASA Certification Specifications |

---

## 4. Performance Requirements

### 4.1 Power Requirements

| Req ID | Parameter | Value | Condition | Rationale | Verification |
|--------|-----------|-------|-----------|-----------|--------------|
| PERF-61-001 | Maximum continuous power | 4.0 MW | ISA, SL (International Standard Atmosphere, Sea Level) | TLARS thrust allocation | Test |
| PERF-61-002 | Peak power (2 min rating) | 4.4 MW | ISA, SL | Takeoff/go-around | Test |
| PERF-61-003 | Cruise power | 2.5 MW | FL350, M0.5 | Mission profile | Test |
| PERF-61-004 | Idle power | ≤50 kW | All conditions | Ground operations | Test |

### 4.2 Thrust Requirements

| Req ID | Parameter | Value | Condition | Rationale | Verification |
|--------|-----------|-------|-----------|-----------|--------------|
| PERF-61-005 | Maximum thrust | 45 kN | ISA, SL, V2 | Takeoff performance | Test |
| PERF-61-006 | Cruise thrust | 12 kN | FL350, M0.5 | Drag balance | Test |
| PERF-61-007 | Reverse thrust | ≥18 kN | Landing | Stopping distance | Test |

### 4.3 Efficiency Requirements

| Req ID | Parameter | Value | Condition | Rationale | Verification |
|--------|-----------|-------|-----------|-----------|--------------|
| PERF-61-008 | Motor efficiency | ≥96% | 50-100% power | Energy optimization | Test |
| PERF-61-009 | Propulsive efficiency | ≥85% | Cruise | Mission efficiency | Test |
| PERF-61-010 | Overall efficiency | ≥81% | Cruise | System-level target | Analysis |

### 4.4 Response Requirements

| Req ID | Parameter | Value | Condition | Rationale | Verification |
|--------|-----------|-------|-----------|-----------|--------------|
| PERF-61-011 | Thrust response (idle to max) | ≤2 seconds | 0-95% thrust | Go-around performance | Test |
| PERF-61-012 | Thrust modulation bandwidth | ≥2 Hz | Flight control integration | DEP control authority | Test |
| PERF-61-013 | Thrust command latency | <100 ms | Command to response | Control loop stability | Test |

### 4.5 Altitude Performance

| Req ID | Parameter | Value | Condition | Rationale | Verification |
|--------|-----------|-------|-----------|-----------|--------------|
| PERF-61-014 | Power lapse rate (SL to FL350) | 0% | Flat rating | Electric advantage | Test |
| PERF-61-015 | Maximum operating altitude | FL410 | All flight phases | Operational envelope | Test |
| PERF-61-016 | Power derating above FL350 | ≤5% | FL350-FL410 | Cooling limitation | Test |

### 4.6 Temperature Performance

| Req ID | Parameter | Value | Condition | Rationale | Verification |
|--------|-----------|-------|-----------|-----------|--------------|
| PERF-61-017 | Full power temperature range | -40°C to +35°C | ISA deviation | Normal operations | Test |
| PERF-61-018 | Thermal derating threshold | ISA+35°C | Above which derating applies | Hot day operations | Test |
| PERF-61-019 | Thermal derating rate | ≤2%/°C | Above ISA+35°C | Performance predictability | Test |
| PERF-61-020 | Maximum thermal derating | 5% | At ISA+40°C (+55°C ambient) | Hot day limit | Test |

### 4.7 OEI Performance

| Req ID | Parameter | Value | Condition | Rationale | Verification |
|--------|-----------|-------|-----------|-----------|--------------|
| PERF-61-021 | OEI power (remaining units) | ≥105% rated | 5 minutes | OEI climb gradient | Test |
| PERF-61-022 | OEI power (continuous) | 100% rated | Unlimited | Continued operation | Test |

### 4.8 Mass Requirements

| Req ID | Parameter | Value | Condition | Rationale | Verification |
|--------|-----------|-------|-----------|-----------|--------------|
| PERF-61-023 | Propulsor unit mass | ≤450 kg | Complete unit | Weight budget | Inspection |
| PERF-61-024 | Specific power | ≥8.9 kW/kg | At rated power | Technology target | Analysis |

---

## 5. Performance Envelope

### 5.1 Power vs. Altitude

| Altitude | Power Available | Notes |
|----------|-----------------|-------|
| Sea Level | 4.0 MW (100%) | Full power |
| FL100 | 4.0 MW (100%) | Full power |
| FL200 | 4.0 MW (100%) | Full power |
| FL350 | 4.0 MW (100%) | Full power |
| FL410 | 3.8 MW (95%) | Cooling limited |

### 5.2 Power vs. Temperature

| Ambient Temp | Power Available | Notes |
|--------------|-----------------|-------|
| -40°C | 4.0 MW (100%) | Full power |
| +15°C (ISA) | 4.0 MW (100%) | Full power |
| +35°C | 4.0 MW (100%) | Full power |
| +50°C | 3.9 MW (97.5%) | 2.5% derating |
| +55°C | 3.8 MW (95%) | 5% derating |

---

## 6. Traceability

### 6.1 Upstream (Source)

| Source | Document |
|--------|----------|
| [[61-00-03-001_System_Requirements]] | System Requirements |
| TLARS-Q100 | Top Level Aircraft Requirements |
| [[61-00-03-REF-003_Performance_Validation]] | Performance Validation |

### 6.2 Downstream (Allocation)

| Target | Document |
|--------|----------|
| [[61-00-04_Design]] | Design specifications |
| [[61-00-07_V_AND_V]] | Verification plans |
| [[61-00-10_Certification]] | Compliance matrix |

---

## 7. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-Q1 | TBD | Initial draft |

---

← [[61-00-03-002_Functional_Requirements]] · [[61-00-03-004_Interface_Requirements]] →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Performance Requirements  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
