# 02-20-19 — Crew Resource Management

**Subsystem ID:** 02-20-19_Crew_Resource_Management  
**Parent Group:** [02-20-00 SYSTEMS](../README.md)  
**Axis:** I — Infrastructures  
**Status:** PROTOTYPE  
**Owner:** Flight Operations / Human Factors Domain  

---

## 1. Purpose

The **Crew Resource Management (CRM)** subsystem provides tools and interfaces for:
*   **Crew Coordination:** Task allocation, workload distribution, and communication.
*   **Fatigue Management:** Monitoring crew duty hours and rest requirements per regulatory limits.
*   **Situational Awareness:** Real-time status of crew tasks and aircraft state.
*   **Human Factors:** Integrating cognitive workload models to prevent task saturation.

---

## 2. Scope

### 2.1 Included
*   **Rostering Integration:** Interface with crew scheduling systems.
*   **Task Management:** Dynamic task allocation based on flight phase and crew workload.
*   **Alert Prioritization:** Intelligent filtering of alerts to prevent information overload.
*   **Fatigue Monitoring:** Real-time assessment of crew fatigue risk.

### 2.2 Excluded
*   **Crew Training Records:** Managed by HR systems.
*   **Medical Certification:** Handled by aviation medical authorities.

---

## 3. Key Interfaces

| Interface ID | Target System | Description |
|:---|:---|:---|
| **IF-CRM-001** | HR/Rostering Systems | Crew availability and duty hours |
| **IF-CRM-002** | [02-20-23 Predictive NN](../02-20-23_Predictive_Operations_NN/) | Workload prediction models |
| **IF-CRM-003** | ATA 42 IMA | Alert management and display |

---

## 4. Document Map

*   **[02-20-19-001: CRM Overview](02-20-19-001_CRM_Overview.md)**
*   **[02-20-19-002: Rostering Integration](02-20-19-002_Crew_Rostering_Integration.md)**
*   **[02-20-19-003: Task & Workload Model](02-20-19-003_Task_and_Workload_Model.md)**
*   **[02-20-19-004: Crew Alerts](02-20-19-004_Crew_Alerts_and_Notifications.md)**
*   **[02-20-19-005: Human Factors](02-20-19-005_Human_Factors_and_Fatigue_Constraints.md)**

### Architecture
*   **[02-20-19-A-001: System Architecture](02-20-19-A-001_CRM_System_Architecture.md)**
*   **[02-20-19-A-501: Requirements Traceability](02-20-19-A-501_Requirements_Traceability.md)**

### Test Data
*   [TEST_DATA/02-20-19-T-001_Crew_Task_Allocation_Scenarios.json](TEST_DATA/02-20-19-T-001_Crew_Task_Allocation_Scenarios.json)
*   [TEST_DATA/02-20-19-T-002_Crew_Workload_and_Fatigue_Cases.json](TEST_DATA/02-20-19-T-002_Crew_Workload_and_Fatigue_Cases.json)

---

## 5. Regulatory References

*   **[CS-OPS Subpart Q](https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-air-operations)** - Flight and Duty Time Limitations (EASA)
*   **[Part 117](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-117)** - Flight and Duty Limitations and Rest Requirements (FAA)

---

## 6. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
