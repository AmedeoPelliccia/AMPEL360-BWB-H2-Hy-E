# 42-00-20-001 — GenCCC & gpt-5.1-codex Partitioned SW Development

## 1. Purpose and Scope

This document defines the integrated development framework for safety-critical partitioned software in IMA (Integrated Modular Avionics) environments. It establishes:

* The role of **GenCCC** as the governance and traceability orchestrator for partitioned software
* The positioning of **gpt-5.1-codex** as an AI assistance tool (non-qualified, T0 classification)
* The development lifecycle for DO-178C compliant software within ARINC 653 and CAST-32A contexts

### 1.1 Applicable Standards

| Standard | Applicability |
|----------|---------------|
| [DO-178C](https://www.rtca.org/) | Software Considerations in Airborne Systems |
| [DO-254](https://www.rtca.org/) | Design Assurance for Airborne Electronic Hardware |
| [ARINC 653](https://www.arinc.com/) | Avionics Application Software Standard Interface |
| CAST-32A | Multi-core Processor Software Certification |
| [CS-25.1309](https://www.easa.europa.eu/en/regulations/certification-specifications/cs-25-large-aeroplanes) | Equipment, Systems, and Installations |
| [EU AI Act](https://artificialintelligenceact.eu/) | Regulation on Artificial Intelligence |

---

## 2. Roles and Responsibilities

### 2.1 GenCCC — Governance and Traceability Engine

GenCCC serves as the **deterministic, auditable orchestrator** for configuration and coverage management across all software partitions.

**Key Functions:**

1. **Partition Catalog Management**
   * Maintain registry of all partitions (P-FCS, P-GNC, P-MAINT, P-ADS, etc.)
   * Track DO-178C level assignment (A/B/C/D/E) per partition
   * Record platform/IMA slot, ARINC 653 partition ID, M-core affinity (CAST-32A)

2. **Traceability Matrix Generation**
   * REQ → DESIGN → CODE → TEST → HAZARD/SAFETY → CERT artefacts
   * Automatic gap detection (requirements without tests, modules without partition justification)
   * Coverage reports (requirements, tests, code)

3. **Certification Evidence**
   * Deterministic scripts (Python) for matrix generation
   * Auditable CSV outputs for certification audits
   * Aspires to TQL-4/TQL-5 qualification as a traceability tool

**Certification Positioning:**

> GenCCC is positioned as a **qualified tool (TQL-4/5)** for traceability and coverage.
> Its logic is deterministic and fully auditable.

### 2.2 gpt-5.1-codex — AI Development Assistant

gpt-5.1-codex is positioned as an **unqualified development support tool (T0)** per DO-178C tool qualification guidelines.

**Key Constraints:**

* **All outputs require 100% human/automated verification**
* No direct credit toward certification objectives
* Used strictly as a productivity aid, not a decision authority

**Permitted Functions:**

1. **Code Generation**
   * Stubs and skeletons for C/Ada/SPARK modules per partition
   * Drivers, wrappers, glue code between partitions
   * Unit test and integration test templates

2. **Refactoring Suggestions**
   * MISRA-C compliance improvements
   * Coding standard alignment (but always human-reviewed)

3. **Test Derivation**
   * Suggest test cases from formal requirements
   * Propose boundary conditions and edge cases

4. **Documentation Generation**
   * SDD (Software Design Document) content
   * SRS (Software Requirements Specification) content
   * Code comments and annotations

**AI Assistance Metadata:**

All AI-generated content must be tagged in GenCCC with:

```yaml
ai_assist:
  model: gpt-5.1-codex
  prompt_owner: "Amedeo Pelliccia"
  generated_at: "YYYY-MM-DDTHH:MM:SSZ"
  partition: "P-XXX"
  safety_level: "A|B|C|D|E"
  verification_required: true
```

### 2.3 Human Engineers

Human engineers retain **full authority and accountability** for:

* All certification decisions
* Final review and approval of all artifacts
* Safety assessments and hazard analysis
* Sign-off on certification evidence packages

---

## 3. Partition Model

### 3.1 Partition Types

| Partition ID | Description | DO-178C Level | ARINC 653 Type | CAST-32A Affinity |
|--------------|-------------|---------------|----------------|-------------------|
| P-FCS | Flight Control System | A | System | Core 0 |
| P-GNC | Guidance, Navigation, Control | A | System | Core 0 |
| P-ADS | Air Data System | B | Application | Core 1 |
| P-MAINT | Maintenance Functions | D | Application | Core 2 |
| P-DIAG | Diagnostics | C | Application | Core 2 |

### 3.2 Partition Configuration Profiles

Partition-specific configuration profiles are maintained in:

* [`PROFILES/level_A_partition.yaml`](./PROFILES/level_A_partition.yaml)
* [`PROFILES/level_B_partition.yaml`](./PROFILES/level_B_partition.yaml)

### 3.3 Traceability Matrices

Per-partition traceability matrices are maintained in:

* [`MATRICES/P-FCS_Traceability.csv`](./MATRICES/P-FCS_Traceability.csv)
* [`MATRICES/P-MAINT_Traceability.csv`](./MATRICES/P-MAINT_Traceability.csv)

---

## 4. Development Lifecycle by Partition

### 4.1 Phase 1: Design

1. **Requirements Capture**
   * Partition requirements documented in [`42-00-22_SW_Requirements/`](../42-00-22_SW_Requirements/)
   * GenCCC ensures all REQ assigned to 1..N modules
   * GenCCC validates verification strategy for each REQ

2. **AI-Assisted Design**
   * gpt-5.1-codex generates design skeletons (headers, interfaces)
   * gpt-5.1-codex generates SPARK/ACSL contracts for formal verification
   * All outputs tagged with AI metadata and queued for review

### 4.2 Phase 2: Implementation

1. **Development Environment**
   * Partition modules organized in [`42-00-23_SW_Code/`](../42-00-23_SW_Code/)
   * Example: `P-FCS/src/fcs_control.c`

2. **AI-Assisted Coding**
   * gpt-5.1-codex generates initial code conforming to coding standard
   * gpt-5.1-codex proposes optimizations for determinism and WCET
   * All changes versioned in Git, indexed in GenCCC (REQ ↔ FILE ↔ FUNC)

3. **Traceability**
   * GenCCC maintains REQ → CODE → FILE mapping
   * Automatic detection of untraced code

### 4.3 Phase 3: Verification

1. **AI-Assisted Test Generation**
   * gpt-5.1-codex proposes unit tests
   * gpt-5.1-codex suggests boundary conditions
   * gpt-5.1-codex generates partition isolation harnesses (ARINC 653)

2. **GenCCC Coverage**
   * REQ-TEST-RESULT matrices generated
   * Structural coverage reports (via external tool integration)
   * Gap reports: REQ without TEST, TEST without REQ

3. **Test Artifacts**
   * Test cases stored in [`42-00-24_SW_Tests/`](../42-00-24_SW_Tests/)

---

## 5. Certification Positioning

### 5.1 Key Message for Certification Authority

> "AI (gpt-5.1-codex) does not make certifiable decisions.
> What is certifiable is the **traceability and verification** governed by GenCCC."

### 5.2 Tool Qualification Strategy

| Tool | TQL Target | Justification |
|------|------------|---------------|
| GenCCC | TQL-4 or TQL-5 | Deterministic logic, auditable outputs, Python scripts, CSV matrices |
| gpt-5.1-codex | T0 (Unqualified) | Non-deterministic AI; all output verified by qualified process |

### 5.3 Evidence Package

For each partition, GenCCC generates:

1. Requirements Traceability Matrix
2. Test Coverage Report
3. Code Coverage Report (via external tool)
4. Gap Analysis Report
5. AI Assistance Log (all gpt-5.1-codex contributions)

---

## 6. AI Usage Rules

### 6.1 Permitted Uses

* Code stub generation
* Test case suggestion
* Documentation drafting
* Refactoring proposals
* Requirements clarification

### 6.2 Prohibited Uses

* **No** direct certification decisions
* **No** safety assessment conclusions
* **No** unverified code in safety-critical partitions
* **No** modification of certification evidence without human review

### 6.3 AI Assistance Logging

All AI interactions are logged in [`42-00-25_AI_Assistance_Log/`](../42-00-25_AI_Assistance_Log/) with:

* Prompt content
* Model response
* Human reviewer
* Verification status
* Integration decision

---

## 7. Integration with CGen Pipeline

GenCCC integrates with the CGen CI/CD pipeline to:

1. Automatically regenerate traceability matrices on commit
2. Detect and report gaps in real-time
3. Generate coverage dashboards
4. Archive AI assistance logs with version control

**Pipeline Hooks:**

```bash
# Example CGen integration
cgen lane:trace --partition P-FCS --output MATRICES/P-FCS_Traceability.csv
cgen lane:gaps --partition P-FCS --report gaps_report.md
```

---

## 8. Related Documents

| Document | Location | Description |
|----------|----------|-------------|
| GenCCC SW Model | [`42-00-20-001_GenCCC_SW_Model.md`](./42-00-20-001_GenCCC_SW_Model.md) | Detailed SW configuration model |
| Partition Catalog | [`42-00-21_Partition_Catalog/`](../42-00-21_Partition_Catalog/) | Registry of all partitions |
| SW Requirements | [`42-00-22_SW_Requirements/`](../42-00-22_SW_Requirements/) | Partition requirements |
| SW Code | [`42-00-23_SW_Code/`](../42-00-23_SW_Code/) | Partition source code |
| SW Tests | [`42-00-24_SW_Tests/`](../42-00-24_SW_Tests/) | Test artifacts |
| AI Assistance Log | [`42-00-25_AI_Assistance_Log/`](../42-00-25_AI_Assistance_Log/) | AI interaction records |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-04.

---
