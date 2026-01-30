# 61-00-03-004 Interface Requirements

**Document ID:** 61-00-03-004  
**Title:** Propulsor System Interface Requirements Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** 0.1  
**Status:** DRAFT

---

## 1. Purpose

This document defines the **interface requirements** for the Q100 Propulsor System, establishing the electrical, mechanical, data, and thermal interfaces with other aircraft systems.

---

## 2. Scope

### 2.1 Interface Categories

This document covers:
* Electrical power interfaces (ATA 24)
* Flight control interfaces (ATA 27)
* Structural/mechanical interfaces (ATA 54)
* Thermal management interfaces (ATA 21)
* Data communication interfaces
* Maintenance interfaces

### 2.2 Interface Partners

| ATA Chapter | System | Interface Type |
|-------------|--------|----------------|
| ATA 24 | Electrical Power | Power supply |
| ATA 27 | Flight Controls | Command/feedback |
| ATA 54 | Nacelles/Pylons | Structural mounting |
| ATA 21 | Air Conditioning | Thermal management |
| ATA 45 | Central Maintenance | Diagnostics |
| ATA 77 | Engine Indicating | Monitoring |

---

## 3. Reference Documents

| ID | Title |
|----|-------|
| 61-00-03-001 | System Requirements Specification |
| ICD-24-61 | Electrical Power Interface Control Document |
| ICD-27-61 | Flight Controls Interface Control Document |
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | EASA Certification Specifications |
| SAE AS6968 | High-Voltage Aerospace Applications |

---

## 4. Interface Requirements

### 4.1 Electrical Power Interface (ATA 24)

| Req ID | Requirement | Value/Spec | Rationale | Verification |
|--------|-------------|------------|-----------|--------------|
| IFC-61-001 | The propulsor shall interface with 800 VDC power bus. | 800 VDC ±10% | Electrical architecture | Test |
| IFC-61-002 | Maximum power draw per propulsor shall not exceed 4.5 MW. | 4.5 MW peak | Power budget | Test |
| IFC-61-003 | Power interface shall comply with SAE AS6968 for high-voltage aerospace. | SAE AS6968 | Electrical safety | Analysis |
| IFC-61-004 | Power connectors shall support hot disconnect capability. | — | Maintenance safety | Test |
| IFC-61-005 | Power cables shall be routed with minimum 50mm separation from fuel lines. | 50mm min | Safety segregation | Inspection |

### 4.2 Flight Controls Interface (ATA 27)

| Req ID | Requirement | Value/Spec | Rationale | Verification |
|--------|-------------|------------|-----------|--------------|
| IFC-61-006 | Thrust commands shall be received via AFDX network. | ARINC 664 Part 7 | Avionics standard | Test |
| IFC-61-007 | Command update rate shall be ≥100 Hz. | 100 Hz min | Control bandwidth | Test |
| IFC-61-008 | Thrust feedback shall be provided to flight controls. | Actual thrust ±2% | Closed-loop control | Test |
| IFC-61-009 | Propulsor status shall be transmitted to flight controls. | Discrete status | Fault management | Test |
| IFC-61-010 | Interface latency shall be <10 ms end-to-end. | <10 ms | Control stability | Test |
| IFC-61-011 | The propulsor control system shall provide thrust differential commands to flight control for yaw control augmentation. | — | DEP yaw control | Analysis, Test |

### 4.3 Structural Interface (ATA 54)

| Req ID | Requirement | Value/Spec | Rationale | Verification |
|--------|-------------|------------|-----------|--------------|
| IFC-61-012 | Propulsor shall mount to nacelle via standardized flange interface. | Per ICD-54-61 | Interchangeability | Inspection |
| IFC-61-013 | Mount interface shall transfer maximum thrust loads of 50 kN. | 50 kN limit | Structural integrity | Test |
| IFC-61-014 | Mount interface shall accommodate thermal expansion of ±5mm. | ±5mm | Thermal growth | Analysis |
| IFC-61-015 | Vibration isolation mounts shall limit transmitted vibration to nacelle. | Per DO-160G | Structural fatigue | Test |

### 4.4 Thermal Management Interface (ATA 21)

| Req ID | Requirement | Value/Spec | Rationale | Verification |
|--------|-------------|------------|-----------|--------------|
| IFC-61-016 | The propulsor shall interface with aircraft thermal management system for heat rejection. | Up to 200 kW/unit | Thermal integration | Test |
| IFC-61-017 | Coolant interface shall use standard quick-disconnect fittings. | Per SAE AS5877 | Maintainability | Inspection |
| IFC-61-018 | Coolant flow rate requirement shall be ≤10 L/min per propulsor. | 10 L/min max | System sizing | Test |
| IFC-61-019 | Coolant inlet temperature shall be ≤45°C. | 45°C max | Cooling effectiveness | Test |

### 4.5 Data Communication Interface

| Req ID | Requirement | Value/Spec | Rationale | Verification |
|--------|-------------|------------|-----------|--------------|
| IFC-61-020 | Health data shall be transmitted via AFDX to aircraft systems. | ARINC 664 | Data integration | Test |
| IFC-61-021 | Maintenance data shall be accessible via maintenance data bus. | ARINC 429 | Ground support | Test |
| IFC-61-022 | Real-time monitoring data rate shall be ≥10 Hz. | 10 Hz min | Health monitoring | Test |
| IFC-61-023 | Interface shall support digital twin data synchronization. | Per 61-00-03-008 | Digital integration | Test |

### 4.6 Maintenance Interface

| Req ID | Requirement | Value/Spec | Rationale | Verification |
|--------|-------------|------------|-----------|--------------|
| IFC-61-024 | Propulsor shall support on-wing LRU replacement. | — | Maintainability | Demonstration |
| IFC-61-025 | All electrical connectors shall be keyed to prevent mis-mating. | — | Error prevention | Inspection |
| IFC-61-026 | Test port shall be provided for ground checkout. | Per ICD | Troubleshooting | Inspection |

---

## 5. Interface Diagram

```
                    ┌─────────────────┐
                    │   ATA 24        │
                    │ Electrical Power│
                    │   800 VDC       │
                    └────────┬────────┘
                             │
                             ▼
┌─────────────┐      ┌───────────────┐      ┌─────────────┐
│  ATA 27     │◄────►│               │◄────►│  ATA 21     │
│ Flight      │      │   PROPULSOR   │      │ Thermal     │
│ Controls    │      │   SYSTEM      │      │ Management  │
│ (AFDX)      │      │   (ATA 61)    │      │ (Coolant)   │
└─────────────┘      └───────┬───────┘      └─────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   ATA 54        │
                    │ Nacelle/Pylon   │
                    │ (Structural)    │
                    └─────────────────┘
```

---

## 6. Traceability

### 6.1 Upstream (Source)

| Source | Document |
|--------|----------|
| [[61-00-03-001_System_Requirements]] | System Requirements |
| ARC-Q100 | Aircraft Requirements Cascade |
| ICD-XX-61 | Interface Control Documents |

### 6.2 Downstream (Allocation)

| Target | Document |
|--------|----------|
| [[61-00-05_Interfaces]] | Detailed ICDs |
| [[61-00-04_Design]] | Design specifications |
| [[61-00-07_V_AND_V]] | Interface verification plans |

---

## 7. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-Q1 | TBD | Initial draft |

---

← [[61-00-03-003_Performance_Requirements]] · [[61-00-03-005_Safety_and_Certification_Requirements]] →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Interface Requirements  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
