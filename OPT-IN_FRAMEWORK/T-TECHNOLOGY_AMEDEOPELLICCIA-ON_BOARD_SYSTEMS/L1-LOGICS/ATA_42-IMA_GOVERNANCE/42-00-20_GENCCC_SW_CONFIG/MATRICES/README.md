# MATRICES

## Purpose

Traceability matrices for partitioned software development.

## Contents

| Matrix | Description | Partition |
|--------|-------------|-----------|
| [`P-FCS_Traceability.csv`](./P-FCS_Traceability.csv) | Flight Control System traceability | P-FCS (Level A) |
| [`P-MAINT_Traceability.csv`](./P-MAINT_Traceability.csv) | Maintenance Functions traceability | P-MAINT (Level D) |

## Matrix Columns

| Column | Description |
|--------|-------------|
| REQ_ID | Requirement identifier |
| REQ_Title | Requirement title |
| DO178C_Level | Design Assurance Level (A/B/C/D/E) |
| Design_ID | Linked design element |
| Code_Module | Implementing source file |
| Code_Function | Implementing function |
| Test_ID | Verification test case |
| Test_Result | Test execution result |
| Hazard_ID | Related hazard (if safety-critical) |
| CERT_Evidence | Certification evidence reference |
| AI_Assisted | Flag for AI-generated artifacts |
| Verification_Status | Current verification status |
| Last_Updated | Last modification date |

## Gap Detection

GenCCC analyzes these matrices to detect:

* Requirements without tests
* Code modules without requirements
* AI-generated artifacts without verification
* Missing hazard links for safety-critical requirements

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Status**: Active
- **Owner**: AMPEL360 SW WG
- **Last Updated**: 2025-12-04

---
