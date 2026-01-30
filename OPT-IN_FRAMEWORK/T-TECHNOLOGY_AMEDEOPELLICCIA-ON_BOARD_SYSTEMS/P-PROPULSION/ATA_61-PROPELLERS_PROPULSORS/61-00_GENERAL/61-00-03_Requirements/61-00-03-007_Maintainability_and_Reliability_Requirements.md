# 61-00-03-007 Maintainability and Reliability Requirements

**Document ID:** 61-00-03-007  
**Title:** Propulsor System Maintainability and Reliability Requirements Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** 0.1  
**Status:** DRAFT

---

## 1. Purpose

This document defines the **maintainability and reliability requirements** for the Q100 Propulsor System, establishing targets for MTBF, MTTR, maintenance philosophy, and supportability.

---

## 2. Scope

### 2.1 M&R Scope

This document covers:
* Reliability requirements (MTBF, failure rates)
* Maintainability requirements (MTTR, accessibility)
* Maintenance philosophy (on-condition, MSG-3)
* Supportability requirements
* LRU/SRU definitions

### 2.2 Applicable Standards

| Standard | Title |
|----------|-------|
| MSG-3 | Maintenance Program Development |
| ATA iSpec 2200 | Information Standards |
| SAE ARP4761A | Safety Assessment Process |
| MIL-HDBK-470A | Designing and Developing Maintainable Products |

---

## 3. Reference Documents

| ID | Title |
|----|-------|
| 61-00-03-001 | System Requirements Specification |
| MSG-3 | Maintenance Program Development |
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | EASA Certification Specifications |

---

## 4. Reliability Requirements

### 4.1 System Reliability

| Req ID | Parameter | Value | Condition | Verification |
|--------|-----------|-------|-----------|--------------|
| MNT-61-001 | Propulsor MTBF | >10,000 FH | All failure modes | Analysis |
| MNT-61-002 | Propulsor MTBUR | >5,000 FH | Unscheduled removal | Analysis |
| MNT-61-003 | Dispatch reliability | ≥99.5% | Per propulsor | Analysis |
| MNT-61-004 | Mission reliability | ≥99.9% | 4-engine dispatch | Analysis |

### 4.2 Component Reliability

| Req ID | Component | MTBF Target | Critical | Verification |
|--------|-----------|-------------|----------|--------------|
| MNT-61-005 | Electric motor | >20,000 FH | Yes | Analysis |
| MNT-61-006 | Motor controller (PMU) | >15,000 FH | Yes | Analysis |
| MNT-61-007 | Fan assembly | >15,000 FH | Yes | Analysis |
| MNT-61-008 | Thrust reverser | >10,000 FH | No | Analysis |
| MNT-61-009 | Bearings | >25,000 FH | Yes | Analysis |
| MNT-61-010 | Sensors/harnesses | >30,000 FH | No | Analysis |

### 4.3 Failure Rate Allocation

| Req ID | Failure Mode | Max Rate (per FH) | Verification |
|--------|--------------|-------------------|--------------|
| MNT-61-011 | Propulsor shutdown (uncommanded) | <10⁻⁵ | Analysis |
| MNT-61-012 | Loss of thrust control | <10⁻⁶ | Analysis |
| MNT-61-013 | Uncontained failure | <10⁻⁹ | Analysis |

---

## 5. Maintainability Requirements

### 5.1 Time Requirements

| Req ID | Parameter | Value | Condition | Verification |
|--------|-----------|-------|-----------|--------------|
| MNT-61-014 | MTTR (LRU replacement) | <2 hours | Line maintenance | Demonstration |
| MNT-61-015 | MTTR (propulsor removal) | <4 hours | Line maintenance | Demonstration |
| MNT-61-016 | Fault isolation time | <30 minutes | With BITE | Demonstration |
| MNT-61-017 | Inspection access time | <15 minutes | Borescope ports | Demonstration |

### 5.2 Accessibility Requirements

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| MNT-61-018 | All LRUs shall be accessible without special tooling. | Maintainability | Demonstration |
| MNT-61-019 | LRU removal/installation shall require no more than 2 technicians. | Labor efficiency | Demonstration |
| MNT-61-020 | Inspection ports shall be provided for fan blade and bearing inspection. | On-condition maintenance | Inspection |
| MNT-61-021 | Test ports shall be provided for ground checkout without LRU removal. | Troubleshooting | Inspection |

### 5.3 Built-In Test Equipment (BITE)

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| MNT-61-022 | BITE shall detect ≥95% of LRU-level faults. | Fault detection | Analysis |
| MNT-61-023 | BITE shall isolate faults to LRU level ≥90% of the time. | Fault isolation | Analysis |
| MNT-61-024 | BITE shall not generate false alarms >1% of flight cycles. | Nuisance avoidance | Analysis |
| MNT-61-025 | BITE results shall be stored for download. | Troubleshooting | Test |

---

## 6. Maintenance Philosophy

### 6.1 MSG-3 Compliance

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| MNT-61-026 | Maintenance program shall be developed per MSG-3 methodology. | Industry standard | Analysis |
| MNT-61-027 | On-condition maintenance shall be the primary maintenance strategy. | Cost optimization | Analysis |
| MNT-61-028 | Hard-time limits shall be established only for safety-critical items. | Regulatory compliance | Analysis |

### 6.2 Scheduled Maintenance

| Req ID | Task | Interval | Type | Verification |
|--------|------|----------|------|--------------|
| MNT-61-029 | Visual inspection | A-check (500 FH) | On-condition | Analysis |
| MNT-61-030 | BITE download and analysis | A-check | On-condition | Analysis |
| MNT-61-031 | Borescope inspection | C-check (5000 FH) | On-condition | Analysis |
| MNT-61-032 | Bearing health assessment | C-check | On-condition | Analysis |
| MNT-61-033 | Motor winding insulation test | C-check | On-condition | Analysis |

### 6.3 Unscheduled Maintenance

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| MNT-61-034 | Troubleshooting procedures shall be provided for all fault codes. | Maintainability | Analysis |
| MNT-61-035 | Unscheduled removal rate shall not exceed 0.02 per 1000 FH. | Operational availability | Analysis |

---

## 7. Supportability Requirements

### 7.1 Spare Parts

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| MNT-61-036 | LRU spares shall be available within 24 hours to major hubs. | Operational support | Analysis |
| MNT-61-037 | Recommended spare parts list shall be provided at EIS. | Airline readiness | Analysis |
| MNT-61-038 | Propulsor shall be designed for modular spare parts. | Inventory optimization | Inspection |

### 7.2 Special Tools and Equipment

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| MNT-61-039 | Special tools shall be minimized (<5 per propulsor). | Maintainability | Inspection |
| MNT-61-040 | All special tools shall be commercially available or provided by OEM. | Supportability | Analysis |
| MNT-61-041 | Ground support equipment shall interface with aircraft standard connectors. | Standardization | Inspection |

### 7.3 Documentation

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| MNT-61-042 | Maintenance documentation shall comply with ATA iSpec 2200. | Industry standard | Analysis |
| MNT-61-043 | Illustrated Parts Catalog shall be provided at EIS. | Parts identification | Analysis |
| MNT-61-044 | Fault Isolation Manual shall cover all BITE fault codes. | Troubleshooting | Analysis |

---

## 8. LRU/SRU Definition

### 8.1 Line Replaceable Units (LRUs)

| LRU | Part Number | Removal Time | Weight |
|-----|-------------|--------------|--------|
| Motor Controller (PMU) | 61-PMU-001 | 45 min | 45 kg |
| Sensor Module | 61-SNS-001 | 30 min | 5 kg |
| Harness Assembly | 61-HRN-001 | 60 min | 8 kg |
| Cooling Pump | 61-CLP-001 | 45 min | 12 kg |
| Thrust Reverser Actuator | 61-TRA-001 | 90 min | 25 kg |

### 8.2 Shop Replaceable Units (SRUs)

| SRU | Parent LRU | Shop Repair |
|-----|------------|-------------|
| Power Stage Module | PMU | Yes |
| Control Card | PMU | Yes |
| Bearing Assembly | Motor | Yes |
| Winding Assembly | Motor | Yes |

---

## 9. Traceability

### 9.1 Upstream (Source)

| Source | Document |
|--------|----------|
| [[61-00-03-001_System_Requirements]] | System Requirements |
| MSG-3 | Maintenance Program Development |
| ATA iSpec 2200 | Documentation Standards |

### 9.2 Downstream (Allocation)

| Target | Document |
|--------|----------|
| [[61-00-04_Design]] | Maintainability design |
| [[61-00-12_Services]] | Support planning |
| [[61-00-14_Ops_Std_Sustain]] | Maintenance program |

---

## 10. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-Q1 | TBD | Initial draft |

---

← [[61-00-03-006_Environmental_and_Noise_Requirements]] · [[61-00-03-008_Digital_and_AI_Requirements]] →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Maintainability and Reliability Requirements  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
