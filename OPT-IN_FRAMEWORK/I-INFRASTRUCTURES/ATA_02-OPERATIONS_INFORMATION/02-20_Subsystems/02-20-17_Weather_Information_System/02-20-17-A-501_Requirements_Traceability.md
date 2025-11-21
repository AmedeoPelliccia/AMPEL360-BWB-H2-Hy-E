# 02-20-17-A-501: Requirements Traceability

> **ID:** 02-20-17-A-501  
> **Title:** WIS Requirements Traceability Matrix  
> **Type:** Traceability Document  
> **Status:** DRAFT  

---

## 1. Purpose

This document provides traceability between Weather Information System (WIS) requirements and their implementation in design documents, code modules, and test cases.

---

## 2. Regulatory Requirements

| Req ID | Source | Requirement | Implementation | Verification |
|:---|:---|:---|:---|:---|
| **REG-WIS-001** | [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) | System must not present misleading information | QC algorithms in 02-20-17-003 | Test: T-002 |
| **REG-WIS-002** | [DO-178C](https://en.wikipedia.org/wiki/DO-178C) | Software must be traceable and auditable | ATA 95 NN Registry | Audit logs |
| **REG-WIS-003** | [DO-200A](https://www.rtca.org/) | Aeronautical data must be quality-checked | CAOS-QC pipeline | Test: T-001 |
| **REG-WIS-004** | [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | AI predictions must be explainable | NN model documentation | ATA 95 |

---

## 3. Functional Requirements

| Req ID | Requirement | Priority | Implementation | Test Case |
|:---|:---|:---|:---|:---|
| **FR-WIS-001** | Ingest data from multiple sources (SAT, GND, AC) | HIGH | 02-20-17-002 | T-001 |
| **FR-WIS-002** | Fuse heterogeneous data into 4D voxel grid | HIGH | 02-20-17-003 | T-002 |
| **FR-WIS-003** | Generate thermal risk maps for ground ops | HIGH | 02-20-17-004 | T-003 |
| **FR-WIS-004** | Predict CO₂ plumes for capture optimization | MEDIUM | 02-20-17-005 (Chem-Net) | T-004 |
| **FR-WIS-005** | Predict contrail formation risk | HIGH | 02-20-17-005 (Cirrus-Net) | T-004 |
| **FR-WIS-006** | Provide nowcasts (0-2h) for terminal ops | MEDIUM | 02-20-17-004 | T-003 |
| **FR-WIS-007** | Interface with Dispatch System | HIGH | 02-20-17-006 (IF-WIS-001) | Integration test |
| **FR-WIS-008** | Interface with Flight Planning | HIGH | 02-20-17-006 (IF-WIS-002) | Integration test |
| **FR-WIS-009** | Interface with Ground Ops | HIGH | 02-20-17-006 (IF-WIS-003) | Integration test |
| **FR-WIS-010** | Display weather overlays on EFB | MEDIUM | 02-20-17-A-002 | UI test |

---

## 4. Non-Functional Requirements

| Req ID | Requirement | Target | Implementation | Verification |
|:---|:---|:---|:---|:---|
| **NFR-WIS-001** | API latency (strategic mode) | < 5 sec | 02-20-17-A-001 | Performance test |
| **NFR-WIS-002** | API latency (tactical mode) | < 500 ms | Edge compute (IMA) | Performance test |
| **NFR-WIS-003** | System availability | 99.9% | Multi-region deployment | SLA monitoring |
| **NFR-WIS-004** | Data freshness (tactical) | < 5 min | Real-time ingestion | Monitoring |
| **NFR-WIS-005** | Contrail prediction accuracy | F1 > 0.90 | Cirrus-Net training | Model eval |
| **NFR-WIS-006** | CO₂ prediction error | MAE < 15 ppm | Chem-Net training | Model eval |
| **NFR-WIS-007** | Temperature forecast error | RMSE < 2°C | Boil-Net training | Model eval |
| **NFR-WIS-008** | Data quality score | > 80% | QC algorithms | Monitoring |

---

## 5. Interface Requirements

| Req ID | Interface | Data Flow | Protocol | Implementation |
|:---|:---|:---|:---|:---|
| **IF-WIS-001** | WIS → Dispatch | Thermal forecasts | REST/JSON | 02-20-17-006 |
| **IF-WIS-002** | WIS → Flight Planning | CO₂ maps, contrail zones | REST/JSON | 02-20-17-006 |
| **IF-WIS-003** | WIS → Ground Ops | Stand temperatures | WebSocket/JSON | 02-20-17-006 |
| **IF-WIS-004** | WIS → EFB | Weather overlays | GeoJSON | 02-20-17-006 |
| **IF-WIS-005** | WIS → Predictive NN | Weather features | Message Queue | 02-20-17-006 |
| **IF-WIS-006** | CO₂ Sensors → WIS | In-situ CO₂ | ARINC 429 | 02-20-17-006 |
| **IF-WIS-007** | Navigation → WIS | OAT, Lidar | ARINC 429 | 02-20-17-006 |
| **IF-WIS-008** | WIS → IMA | NN inference | IMA API | 02-20-17-006 |
| **IF-WIS-009** | WIS → ATA 95 | Prediction logs | S3/Parquet | 02-20-17-006 |

---

## 6. Test Coverage Matrix

| Test ID | Test Type | Requirements Covered | Status |
|:---|:---|:---|:---|
| **T-001** | Unit | FR-WIS-001, NFR-WIS-004 | Planned |
| **T-002** | Unit | FR-WIS-002, REG-WIS-001 | Planned |
| **T-003** | Integration | FR-WIS-003, FR-WIS-006 | Planned |
| **T-004** | Integration | FR-WIS-004, FR-WIS-005 | Planned |
| **IT-001** | System | FR-WIS-007, IF-WIS-001 | Planned |
| **IT-002** | System | FR-WIS-008, IF-WIS-002 | Planned |
| **IT-003** | System | FR-WIS-009, IF-WIS-003 | Planned |
| **PT-001** | Performance | NFR-WIS-001, NFR-WIS-002 | Planned |
| **MT-001** | Model Eval | NFR-WIS-005, NFR-WIS-006, NFR-WIS-007 | Planned |

---

## 7. Change Log

| Version | Date | Change | Impacted Requirements |
|:---|:---|:---|:---|
| 0.1 | 2025-11-21 | Initial traceability matrix | All |

---

## 8. Related Documents

*   [02-20-17-001: System Overview](02-20-17-001_Weather_System_Overview.md)
*   [02-20-17-002: Data Sources](02-20-17-002_Meteo_Data_Sources_and_Ingestion.md)
*   [02-20-17-003: Data Fusion & QC](02-20-17-003_Weather_Data_Fusion_and_Quality_Control.md)
*   [02-20-17-004: Operational Products](02-20-17-004_Operational_Weather_Products_for_Ops.md)
*   [02-20-17-005: NN Integration](02-20-17-005_Weather_Prediction_NN_Integration.md)
*   [02-20-17-006: Interfaces](02-20-17-006_Interfaces_with_Other_02-20_Subsystems.md)
*   [ATA 95 Neural Networks](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95_NEURAL_NETWORKS/)

---

## 9. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
