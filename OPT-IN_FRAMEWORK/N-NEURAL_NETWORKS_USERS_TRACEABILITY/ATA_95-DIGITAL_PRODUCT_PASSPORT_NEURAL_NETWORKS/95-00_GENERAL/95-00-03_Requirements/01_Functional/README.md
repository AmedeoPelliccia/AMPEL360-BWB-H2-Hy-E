# 01_Functional — Functional Requirements

## Purpose

This folder contains **functional requirements** for the DPP system — requirements that define **what the system must do**.

## Scope

### ID Range: RQ-95-00-03-001 to RQ-95-00-03-099

Functional requirements in this category address:
- **Core DPP capabilities**: UUID generation, versioning, artifact linking
- **Data management**: Storage, retrieval, update operations
- **Lifecycle tracking**: Model states, transitions, history
- **API functionality**: CRUD operations, query capabilities
- **Integration points**: Interfaces with external systems

## Requirements Summary

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-001 | DPP SHALL Provide Unique UUID Per Model | APPROVED |
| RQ-95-00-03-002 | DPP SHALL Support Semantic Versioning | APPROVED |
| RQ-95-00-03-003 | DPP SHALL Link To Models And Artifacts | APPROVED |
| RQ-95-00-03-004 | DPP SHALL Store Model Metadata | DRAFT |
| RQ-95-00-03-005 | DPP SHALL Track Model Lifecycle States | DRAFT |
| ... | (Additional requirements as defined) | ... |

---

## What Belongs Here

**Functional requirements** define system capabilities and behaviors. Examples:
- "The system SHALL generate a unique UUID for each model"
- "The system SHALL support semantic versioning"
- "The system SHALL provide an API for DPP access"

## What Doesn't Belong Here

- **Performance requirements** → 02_NonFunctional
- **Safety requirements** → 03_Safety_and_AAI
- **Regulatory mandates** → 04_Regulatory_Compliance
- **Data quality requirements** → 05_Data_and_Metadata

---

## Document Control

- **Folder**: 01_Functional
- **ID Range**: 001-099
- **Owner**: Requirements WG / Functional Architecture
- **Last Updated**: 2025-11-17
