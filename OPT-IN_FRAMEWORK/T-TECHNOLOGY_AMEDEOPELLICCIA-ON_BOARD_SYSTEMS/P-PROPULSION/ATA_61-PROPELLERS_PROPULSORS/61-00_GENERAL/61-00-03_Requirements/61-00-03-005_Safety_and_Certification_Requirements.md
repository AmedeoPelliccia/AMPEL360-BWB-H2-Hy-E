# 61-00-03-005 Safety and Certification Requirements

**Document ID:** 61-00-03-005  
**Title:** Propulsor System Safety and Certification Requirements Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** 0.1  
**Status:** DRAFT

---

## 1. Purpose

This document defines the **safety and certification requirements** for the Q100 Propulsor System, derived from Functional Hazard Assessment (FHA), Preliminary System Safety Assessment (PSSA), and regulatory certification requirements.

---

## 2. Scope

### 2.1 Safety Scope

This document covers:
* Safety-derived requirements from FHA/PSSA
* Development Assurance Level (DAL) allocations
* Certification basis requirements
* Special conditions for novel technologies

### 2.2 Certification Basis

| Authority | Regulation | Notes |
|-----------|------------|-------|
| EASA | [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | Large Aeroplanes |
| FAA | 14 CFR Part 25 | Transport Category |
| EASA | Special Conditions | DEP, H₂, Batteries |

---

## 3. Reference Documents

| ID | Title |
|----|-------|
| 61-00-03-001 | System Requirements Specification |
| 61-00-02-001 | Functional Hazard Assessment |
| 61-00-02-002 | Preliminary System Safety Assessment |
| 61-00-03-REF-002 | Gap Closure Response |
| [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | Equipment, Systems, and Installations |
| ARP4761A | Safety Assessment Process |
| ARP4754A | Development Assurance |

---

## 4. Safety Requirements

### 4.1 Failure Probability Requirements

| Req ID | Requirement | DAL | Failure Condition | Source | Verification |
|--------|-------------|-----|-------------------|--------|--------------|
| SAFE-61-001 | Uncontained propulsor failure probability shall be < 10⁻⁹ per flight hour. | A | Catastrophic | FHA | Analysis |
| SAFE-61-002 | Loss of all thrust probability shall be < 10⁻⁹ per flight hour. | A | Catastrophic | FHA | Analysis |
| SAFE-61-003 | Loss of thrust control (single propulsor) probability shall be < 10⁻⁷ per flight hour. | B | Hazardous | FHA | Analysis |
| SAFE-61-004 | Uncommanded thrust reversal probability shall be < 10⁻⁹ per flight hour. | A | Catastrophic | FHA | Analysis |

### 4.2 Redundancy Requirements

| Req ID | Requirement | DAL | Rationale | Verification |
|--------|-------------|-----|-----------|--------------|
| SAFE-61-005 | The propulsor control system shall implement dual-channel motor control. | A | SPOF prevention | Analysis, Test |
| SAFE-61-006 | Each control channel shall be capable of independent operation. | A | Fail-operational | Test |
| SAFE-61-007 | Propulsor architecture shall prevent single points of failure for critical functions per CS-25.1309. | A | Safety architecture | Analysis |

### 4.3 Fire Protection Requirements

| Req ID | Requirement | DAL | Rationale | Verification |
|--------|-------------|-----|-----------|--------------|
| SAFE-61-008 | Fire detection shall be provided in the propulsor nacelle. | B | [CS-25.1181](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | Test |
| SAFE-61-009 | Fire suppression capability shall be provided. | B | [CS-25.1195](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | Test |
| SAFE-61-010 | Fire zones shall be isolated from adjacent structure. | B | Fire containment | Inspection |

### 4.4 Hydrogen Safety Requirements

| Req ID | Requirement | DAL | Rationale | Verification |
|--------|-------------|-----|-----------|--------------|
| SAFE-61-011 | Hydrogen leak detection shall be provided with automatic fuel shutoff within 2 seconds. | A | FAA H₂ Roadmap | Test |
| SAFE-61-012 | Hydrogen venting shall prevent accumulation in enclosed spaces. | A | Explosion prevention | Analysis |
| SAFE-61-013 | Electrical components in hydrogen zones shall be rated for hazardous atmospheres. | A | Ignition prevention | Inspection |

### 4.5 Battery Safety Requirements

| Req ID | Requirement | DAL | Rationale | Verification |
|--------|-------------|-----|-----------|--------------|
| SAFE-61-014 | Battery thermal runaway detection and containment shall be provided per RTCA DO-311A. | A | Battery safety | Test |
| SAFE-61-015 | Battery fire shall not propagate to adjacent cells or systems. | A | Fire containment | Test |
| SAFE-61-016 | Battery venting shall be directed overboard. | B | Toxic fume protection | Analysis |

### 4.6 Electrical Safety Requirements

| Req ID | Requirement | DAL | Rationale | Verification |
|--------|-------------|-----|-----------|--------------|
| SAFE-61-017 | 800 VDC electrical interface shall comply with SAE AS6968. | B | High-voltage safety | Analysis |
| SAFE-61-018 | High-voltage circuits shall be protected against arc flash. | B | Personnel safety | Test |
| SAFE-61-019 | Ground fault protection shall disconnect within 100 ms. | B | Electrical safety | Test |

### 4.7 Containment Requirements

| Req ID | Requirement | DAL | Rationale | Verification |
|--------|-------------|-----|-----------|--------------|
| SAFE-61-020 | Fan blade failure shall be contained within the nacelle. | A | Uncontained failure | Test |
| SAFE-61-021 | Motor rotor failure shall be contained. | A | Uncontained failure | Test |

---

## 5. Development Assurance Level Allocation

### 5.1 DAL Summary

| Component | DAL | Justification |
|-----------|-----|---------------|
| Motor Control Software | A | Loss of control = Catastrophic |
| Motor Control Hardware | A | Loss of control = Catastrophic |
| Health Monitoring | C | Advisory function |
| Thrust Reverser Control | B | Uncommanded reversal = Hazardous |
| Fire Detection | B | Delayed detection = Hazardous |

### 5.2 Software Assurance

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| SAFE-61-022 | Control software shall be developed to DO-178C DAL A. | Software assurance | Analysis |
| SAFE-61-023 | Control software shall achieve MC/DC test coverage. | DO-178C objective | Test |

### 5.3 Hardware Assurance

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| SAFE-61-024 | Control hardware shall be developed to DO-254 DAL A. | Hardware assurance | Analysis |
| SAFE-61-025 | Hardware shall meet SEU tolerance requirements. | Cosmic ray immunity | Test |

---

## 6. Certification Compliance Matrix

| CS-25 Requirement | Propulsor Requirement | Status |
|-------------------|----------------------|--------|
| CS-25.901 | SYS-61-005 | Covered |
| CS-25.903 | PERF-61-001, PERF-61-021 | Covered |
| CS-25.1181 | SAFE-61-008 | Covered |
| CS-25.1195 | SAFE-61-009 | Covered |
| CS-25.1309 | SAFE-61-001 through SAFE-61-007 | Covered |
| Special Condition (H₂) | SAFE-61-011 through SAFE-61-013 | Covered |
| Special Condition (Battery) | SAFE-61-014 through SAFE-61-016 | Covered |

---

## 7. Traceability

### 7.1 Upstream (Source)

| Source | Document |
|--------|----------|
| [[61-00-02_Safety]] | FHA, PSSA |
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | Certification Specifications |
| ARP4761A | Safety Assessment Process |

### 7.2 Downstream (Allocation)

| Target | Document |
|--------|----------|
| [[61-00-04_Design]] | Safety-critical design |
| [[61-00-07_V_AND_V]] | Safety verification |
| [[61-00-10_Certification]] | Certification evidence |

---

## 8. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-Q1 | TBD | Initial draft |

---

← [[61-00-03-004_Interface_Requirements]] · [[61-00-03-006_Environmental_and_Noise_Requirements]] →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Safety and Certification Requirements  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
