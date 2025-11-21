# 02-20-18 — Operational Data Recording

**Subsystem ID:** 02-20-18_Operational_Data_Recording  
**Parent Group:** [02-20-00 SYSTEMS](../README.md)  
**Axis:** I — Infrastructures  
**Status:** PROTOTYPE  
**Owner:** Operations / Data Governance Domain  

---

## 1. Purpose

The **Operational Data Recording (ODR)** subsystem captures, processes, and stores operational events and data streams for:
*   **Regulatory Compliance:** Integration with Flight Data Recorder (FDR) per ATA 31.
*   **Digital Product Passport (DPP):** Maintaining complete data lineage for certification.
*   **Analytics:** Supporting predictive operations and continuous improvement.
*   **Audit Trail:** Ensuring traceability for safety and environmental claims.

---

## 2. Scope

### 2.1 Included
*   **Event Logging Model:** Standardized event taxonomy and schema.
*   **FDR Integration:** Bidirectional data exchange with ATA 31 recording systems.
*   **DPP Support:** Data lineage tracking for carbon credits and environmental certification.
*   **Privacy Controls:** GDPR-compliant data retention and anonymization.

### 2.2 Excluded
*   **Cockpit Voice Recorder (CVR):** Managed separately under ATA 31.
*   **Real-time Streaming Analytics:** Handled by [02-20-23 Predictive Ops NN](../02-20-23_Predictive_Operations_NN/).

---

## 3. Key Interfaces

| Interface ID | Target System | Description |
|:---|:---|:---|
| **IF-ODR-001** | ATA 31 FDR | Flight data synchronization |
| **IF-ODR-002** | [02-20-23 Predictive NN](../02-20-23_Predictive_Operations_NN/) | Historical data for model training |
| **IF-ODR-003** | [ATA 95 Digital Passport](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95_NEURAL_NETWORKS/) | DPP data lineage |
| **IF-ODR-004** | CAOS Event Bus | Real-time event ingestion |

---

## 4. Document Map

*   **[02-20-18-001: System Overview](02-20-18-001_Operational_Data_Recording_Overview.md)** - Architecture and data flows.
*   **[02-20-18-002: Event & Logging Model](02-20-18-002_Event_and_Logging_Model.md)** - Event taxonomy and schema.
*   **[02-20-18-003: FDR Integration](02-20-18-003_FDR_and_ATA31_Integration.md)** - Flight Data Recorder interfacing.
*   **[02-20-18-004: DPP & Data Lineage](02-20-18-004_DPP_and_Data_Lineage.md)** - Digital Product Passport support.
*   **[02-20-18-005: Privacy & Retention](02-20-18-005_Privacy_and_Retention_Policies.md)** - GDPR compliance and data lifecycle.

### Architecture Documents

*   **[02-20-18-A-001: Architecture](02-20-18-A-001_Operational_Data_Recording_Architecture.md)**
*   **[02-20-18-A-002: Data Flow View](02-20-18-A-002_Operational_Data_Flow_View.md)**
*   **[02-20-18-A-501: Requirements Traceability](02-20-18-A-501_Requirements_Traceability.md)**

### Test Data

*   [TEST_DATA/02-20-18-T-001_Event_Logging_Cases.json](TEST_DATA/02-20-18-T-001_Event_Logging_Cases.json)
*   [TEST_DATA/02-20-18-T-002_FDR_Synchronisation_Cases.json](TEST_DATA/02-20-18-T-002_FDR_Synchronisation_Cases.json)
*   [TEST_DATA/02-20-18-T-003_DPP_Lineage_Cases.json](TEST_DATA/02-20-18-T-003_DPP_Lineage_Cases.json)

---

## 5. Regulatory & Standards References

*   **[CS-25.1459](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)** - Flight Data Recorders (EASA)
*   **[Part 121.344](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-121/subpart-N/section-121.344)** - Digital Flight Data Recorder (FAA)
*   **[GDPR](https://gdpr.eu/)** - General Data Protection Regulation
*   **[ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)** - Information Security Management

---

## 6. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
