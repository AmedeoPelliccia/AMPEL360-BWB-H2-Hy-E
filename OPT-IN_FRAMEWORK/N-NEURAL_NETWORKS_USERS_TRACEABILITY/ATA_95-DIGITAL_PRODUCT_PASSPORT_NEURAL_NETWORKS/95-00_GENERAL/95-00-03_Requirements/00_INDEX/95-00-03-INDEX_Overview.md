# 95-00-03 Requirements INDEX — Overview

## Purpose

This document provides a high-level overview of the **Digital Product Passport (DPP) Requirements** for ATA 95 — Neural Networks & Digital Passport system.

---

## Requirements Categories Summary

The DPP requirements are organized into **seven categories** aligned with lifecycle concerns, regulatory mandates, and operational needs:

| Category | ID Range | Count | Status | Description |
|----------|----------|-------|--------|-------------|
| **01 — Functional** | 001–099 | 10 | Active | Core DPP functionality: UUID generation, versioning, linking to artifacts |
| **02 — Non-Functional** | 100–199 | 5 | Active | Performance, availability, scalability, latency requirements |
| **03 — Safety & AAI** | 200–299 | 6 | Active | Safety assurance, ODD definition, runtime monitoring configuration |
| **04 — Regulatory Compliance** | 300–399 | 8 | Active | EU AI Act, EU DPP framework, aviation certification standards |
| **05 — Data & Metadata** | 400–499 | 7 | Active | Training data lineage, CO₂e metrics, provenance tracking |
| **06 — Toolchain & Automation** | 500–599 | 6 | Active | JSON schema validation, CI/CD integration, MCP tools |
| **07 — Governance & Audit** | 600–699 | 4 | Active | Change control, audit trails, CCB approval processes |
| **TOTAL** | — | **46** | — | — |

---

## Requirements by Category

### 01 — Functional Requirements

Core capabilities the DPP must provide to support neural network lifecycle management.

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-001 | DPP SHALL Provide Unique UUID Per Model | APPROVED |
| RQ-95-00-03-002 | DPP SHALL Support Semantic Versioning | APPROVED |
| RQ-95-00-03-003 | DPP SHALL Link To Models And Artifacts | APPROVED |
| RQ-95-00-03-004 | DPP SHALL Store Model Metadata | DRAFT |
| RQ-95-00-03-005 | DPP SHALL Track Model Lifecycle States | DRAFT |
| RQ-95-00-03-006 | DPP SHALL Support Multiple Neural Network Types | DRAFT |
| RQ-95-00-03-007 | DPP SHALL Maintain Configuration History | DRAFT |
| RQ-95-00-03-008 | DPP SHALL Support Model Comparison | DRAFT |
| RQ-95-00-03-009 | DPP SHALL Enable Model Rollback | DRAFT |
| RQ-95-00-03-010 | DPP SHALL Provide API Access | DRAFT |

### 02 — Non-Functional Requirements

Quality attributes governing system performance, reliability, and operational characteristics.

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-101 | DPP Availability ≥ 99.5% | APPROVED |
| RQ-95-00-03-102 | DPP Read Latency Under 500ms | APPROVED |
| RQ-95-00-03-103 | DPP SHALL Support Concurrent Access | DRAFT |
| RQ-95-00-03-104 | DPP SHALL Scale to 1000+ Models | DRAFT |
| RQ-95-00-03-105 | DPP Data Retention Minimum 10 Years | DRAFT |

### 03 — Safety and AAI Requirements

Safety assurance for AI systems, including Operational Design Domain and runtime monitoring.

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-201 | DPP SHALL Capture ODD Definition | FOR_REVIEW |
| RQ-95-00-03-202 | DPP SHALL Store Runtime Monitoring Config | FOR_REVIEW |
| RQ-95-00-03-203 | DPP SHALL Record Safety Assessment Results | DRAFT |
| RQ-95-00-03-204 | DPP SHALL Track Failure Modes | DRAFT |
| RQ-95-00-03-205 | DPP SHALL Store Mitigation Strategies | DRAFT |
| RQ-95-00-03-206 | DPP SHALL Link to FHA/FMEA Documents | DRAFT |

### 04 — Regulatory Compliance Requirements

Mandated by EU AI Act, EU DPP framework, and aviation certification authorities.

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-301 | DPP SHALL Support EU AI Act High-Risk Documentation | FOR_REVIEW |
| RQ-95-00-03-302 | DPP SHALL Expose EU DPP Mandatory Fields | FOR_REVIEW |
| RQ-95-00-03-303 | DPP SHALL Comply With EASA AI Requirements | DRAFT |
| RQ-95-00-03-304 | DPP SHALL Support FAA AI Certification | DRAFT |
| RQ-95-00-03-305 | DPP SHALL Enable Regulatory Inspections | DRAFT |
| RQ-95-00-03-306 | DPP SHALL Maintain Certification Evidence | DRAFT |
| RQ-95-00-03-307 | DPP SHALL Support Data Protection Regulations | DRAFT |
| RQ-95-00-03-308 | DPP SHALL Comply With Export Control Laws | DRAFT |

### 05 — Data and Metadata Requirements

Data lineage, provenance, environmental impact metrics, and metadata management.

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-401 | DPP SHALL Store Training Data Lineage | APPROVED |
| RQ-95-00-03-402 | DPP SHALL Record CO₂e Metrics | APPROVED |
| RQ-95-00-03-403 | DPP SHALL Track Data Provenance | DRAFT |
| RQ-95-00-03-404 | DPP SHALL Store Hyperparameter History | DRAFT |
| RQ-95-00-03-405 | DPP SHALL Record Validation Dataset Info | DRAFT |
| RQ-95-00-03-406 | DPP SHALL Track Model Performance Metrics | DRAFT |
| RQ-95-00-03-407 | DPP SHALL Store Bias Assessment Results | DRAFT |

### 06 — Toolchain and Automation Requirements

Integration with CI/CD pipelines, automated validation, and developer tooling.

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-501 | DPP SHALL Be Validated By JSON Schema | APPROVED |
| RQ-95-00-03-502 | DPP SHALL Be Auto-Generated From CI Pipeline | APPROVED |
| RQ-95-00-03-503 | DPP SHALL Use Doc-Meta-Enforcer MCP | APPROVED |
| RQ-95-00-03-504 | DPP SHALL Integrate With Model Registry | DRAFT |
| RQ-95-00-03-505 | DPP SHALL Support Git-Based Versioning | DRAFT |
| RQ-95-00-03-506 | DPP SHALL Enable Automated Testing | DRAFT |

### 07 — Governance and Audit Requirements

Change control, audit trails, and configuration control board processes.

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-601 | DPP Changes SHALL Require CCB Approval | APPROVED |
| RQ-95-00-03-602 | DPP SHALL Support Audit Trail | APPROVED |
| RQ-95-00-03-603 | DPP SHALL Log All Modifications | DRAFT |
| RQ-95-00-03-604 | DPP SHALL Enable Access Control | DRAFT |

---

## Requirements Lifecycle States

| State | Definition | Transition Criteria |
|-------|------------|---------------------|
| **DRAFT** | Initial capture, under development | None (starting state) |
| **FOR_REVIEW** | Ready for stakeholder review | Complete template filled, acceptance criteria defined |
| **APPROVED** | Reviewed and approved by stakeholders | Review complete, CCB approval obtained |
| **IMPLEMENTED** | Implemented in design/code | Design complete, implementation verified |
| **VERIFIED** | Verification complete | Test cases executed, evidence collected |
| **CLOSED** | Requirement satisfied and closed | Verification complete, certification accepted |

---

## Requirements Traceability Matrix (RTM)

The full RTM is maintained in `95-00-03-RTM_DPP_Requirements.xlsx` and provides:

- **Horizontal Traceability**: Linking requirements to their sources (regulations, standards, parent requirements)
- **Vertical Traceability**: Linking requirements to downstream artifacts (design, implementation, test, certification)

### RTM Columns

| Column | Description |
|--------|-------------|
| Requirement ID | Unique identifier (RQ-95-00-03-XXX) |
| Title | Short descriptive title |
| Category | Requirement category (01–07) |
| Status | Current lifecycle state |
| Source | Originating document/regulation |
| Design | Link to design specification |
| Implementation | Link to implementation (code, config) |
| Test | Link to test case(s) |
| Certification | Link to means of compliance |
| DPP Field(s) | Corresponding fields in DPP JSON schema |

---

## Usage

### For Requirements Engineers

1. Review this overview to understand the requirements landscape
2. Consult the detailed requirement files in category folders (01–07)
3. Use the RTM to trace requirements through the lifecycle
4. Update `95-00-03-REQ_List.csv` when adding/modifying requirements

### For Designers

1. Review requirements in relevant categories
2. Link design artifacts to requirements in RTM
3. Ensure all APPROVED requirements are addressed in design

### For Testers

1. Review requirements with verification method = "Test"
2. Create test cases covering all testable requirements
3. Link test results to requirements in RTM

### For Certification

1. Review regulatory compliance requirements (Category 04)
2. Collect evidence for all requirements
3. Populate certification column in RTM

---

## Document Control

- **Document ID**: 95-00-03-INDEX-001
- **Version**: 1.0
- **Status**: APPROVED
- **Last Updated**: 2025-11-17
- **Owner**: AMPEL360 Requirements WG
- **Standard**: OPT-IN Framework v1.4

---

## References

- `95-00-03-README.md` — Requirements framework overview
- `95-00-03-REQ_List.csv` — Machine-readable requirements list
- `95-00-03-RTM_DPP_Requirements.xlsx` — Full traceability matrix

---

**For questions or suggestions, contact: requirements@ampel360.aero**
