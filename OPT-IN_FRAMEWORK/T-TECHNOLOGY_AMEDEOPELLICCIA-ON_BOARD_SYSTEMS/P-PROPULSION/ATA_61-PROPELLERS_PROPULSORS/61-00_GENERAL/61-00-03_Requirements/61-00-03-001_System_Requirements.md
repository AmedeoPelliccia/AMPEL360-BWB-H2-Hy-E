# 61-00-03-001 System Requirements

**Document ID:** 61-00-03-001  
**Title:** Propulsor System Requirements Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** 0.1  
**Status:** DRAFT

---

## 1. Purpose

This document defines the **top-level system requirements** for the Q100 Propulsor System, establishing the technical baseline for design, verification, and certification activities.

---

## 2. Scope

### 2.1 System Boundary

The Propulsor System includes:

* Electric motor assembly
* Fan/propulsor stage
* Motor controller (PMU)
* Thrust reverser mechanism
* Propulsor health monitoring
* Structural interfaces to nacelle

### 2.2 Exclusions

* Electrical power generation (ATA 24)
* Nacelle structure (ATA 54)
* Flight control laws (ATA 27)

---

## 3. Reference Documents

| ID | Title |
|----|-------|
| TLARS-Q100 | Top Level Aircraft Requirements Specification |
| ARC-Q100 | Aircraft Requirements Cascade |
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | EASA Certification Specifications |
| 14 CFR 25 | FAA Airworthiness Standards |

---

## 4. System Requirements

### 4.1 General

| Req ID | Requirement | Rationale | Verification |
|--------|-------------|-----------|--------------|
| SYS-61-001 | The propulsor system shall provide continuous thrust power of 4 MW per unit under ISA sea level conditions. | TLARS thrust allocation | Test |
| SYS-61-002 | The propulsor system shall integrate with the H₂ fuel cell electrical power system (ATA 24). | Hybrid-electric architecture | Analysis, Test |
| SYS-61-003 | The aircraft shall be equipped with four (4) propulsor units in a distributed electric propulsion (DEP) configuration. | Redundancy, BLI optimization | Inspection |
| SYS-61-004 | The propulsor system shall operate across the full flight envelope from ground to FL410. | Operational requirement | Test |
| SYS-61-005 | The propulsor system shall comply with EASA [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) and FAA 14 CFR Part 25 requirements. | Certification basis | Analysis |

### 4.2 Configuration

_TBD — To be completed with detailed configuration requirements._

---

## 5. Traceability

### 5.1 Upstream (Source)

| Source | Document |
|--------|----------|
| TLARS | Top Level Aircraft Requirements |
| ARC | Aircraft Requirements Cascade |

### 5.2 Downstream (Allocation)

| Target | Document |
|--------|----------|
| [[61-00-03-002_Functional_Requirements]] | Functional Requirements |
| [[61-00-03-003_Performance_Requirements]] | Performance Requirements |
| [[61-00-03-004_Interface_Requirements]] | Interface Requirements |
| [[61-00-03-005_Safety_and_Certification_Requirements]] | Safety Requirements |
| [[61-00-04_Design]] | Design specifications |

---

## 6. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-Q1 | TBD | Initial draft |

---

← [[00_INDEX]] · [[61-00-03-002_Functional_Requirements]] →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — System Requirements  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
