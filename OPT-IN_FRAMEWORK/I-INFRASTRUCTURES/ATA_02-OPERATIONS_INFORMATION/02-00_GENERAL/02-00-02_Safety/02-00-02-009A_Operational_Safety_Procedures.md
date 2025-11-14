---
Title: "Human Factors Safety — ATA 02"
Identifier: "AMPEL360-02-00-02-008A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "HF Lead"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Human Factors safety approach for ATA 02 Operations Information within I-INFRASTRUCTURES"
Abstract: "Defines Human Factors safety considerations, assessment methods, and procedural/training expectations for ATA 02 operations information."
Keywords: ["ATA 02", "Human Factors", "HF", "Safety", "Operations Information"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Doc Standard v1.1"
  - "Certification Safety Objectives — ATA 02"
Links:
  ParentGeneral: "../"
  SafetyObjectives: "./AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md"
  ERP: "./AMPEL360-02-00-02-003A_Emergency_Response_Procedures.md"
  HazardMethodology: "./AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md"
  TrainingMaterials: "../../02-90_Tables_Schemas_Diagrams/"
  Requirements: "../02-00-03_Requirements/"
  VAndV: "../02-00-07_V_AND_V/"
  RolesResponsibilities: "../02-00-01-004A_Roles_Responsibilities.md"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "HF Lead", change: "Initial creation"}
---

# Human Factors Safety — ATA 02

## 1. Purpose

This document defines the **Human Factors (HF) safety approach** for **ATA 02 — Operations Information**. It specifies:

- HF dimensions to be considered when designing, reviewing, and validating operations information.
- Expectations for HF assessment techniques and evidence.
- Requirements for the **clarity and handling of change notices**.
- Linkage to **training materials** and HF-related requirements and verification.

It complements the **Certification Safety Objectives — ATA 02** and the **Hazard Analysis Methodology**, focusing on workload, situation awareness, error resilience, and information usability.

---

## 2. Human Factors Focus Areas

HF assessment for ATA 02 operations information must consider at least the following dimensions:

### 2.1 Crew and Operator Workload

- Use structured workload assessment methods (e.g. **NASA-TLX** or equivalent) where appropriate to evaluate:
  - Additional workload imposed by interacting with ops information (manual lookups, multiple systems, complex tables).
  - Workload during **time-critical** phases (e.g., turnarounds, irregular operations, degraded conditions).
- Objectives:
  - Avoid excessive or poorly distributed workload caused by information design.
  - Ensure critical information is accessible with minimal cognitive and physical effort.

### 2.2 Situation Awareness (SA)

- Use methods such as **SAGAT** (Situation Awareness Global Assessment Technique) or equivalent to assess:
  - Whether operators can easily understand:
    - Current operational status and constraints.
    - Applicability of procedures/limits to their aircraft, airport, and configuration.
  - Whether information presentation supports maintaining SA during:
    - Rapid changes (e.g., NOTAM updates, gate changes, weather deterioration).
    - Abnormal and degraded situations.
- Objectives:
  - Minimize SA loss due to ambiguous or poorly structured information.
  - Ensure critical changes are clearly visible and contextualized.

### 2.3 Error Traps and Error Tolerance

- Identify **error traps**, such as:
  - Look-alike/sound-alike values or codes.
  - Crowded tables with similar entries.
  - Layouts that encourage slips (e.g., off-by-one line selection, misaligned columns).
- Design for **error tolerance**, including:
  - Cross-checks and confirmation steps where high-risk selections are involved.
  - Clear fallbacks and recovery paths (e.g., how to verify suspect information).
- Objectives:
  - Reduce the likelihood of human error induced by the structure or content of operations information.
  - Ensure that when errors occur, they are detectable and recoverable.

### 2.4 Display and Information Clarity

- Assess **display clarity** for all published formats:
  - EFB screens, portals, PDFs, printed manuals, dashboards.
- Consider:
  - Readability (font size, contrast, color usage).
  - Consistent terminology, symbols, and iconography.
  - Logical grouping and hierarchy (headings, sections, tables).
  - Distinct visual emphasis for **warnings, cautions, limitations**, and applicability.
- Objectives:
  - Make key safety-critical information immediately recognizable.
  - Avoid visual clutter and misinterpretation.

---

## 3. Procedures for Change Notices

Ops information change notices (including emergency changes) must be HF-informed.

### 3.1 Unambiguous Content

Change notices must:

- Clearly state:
  - **What** is changing (e.g., specific tables, procedures, airports, fleets).
  - **Why** it is changing (safety, performance, regulatory, operational rationale).
  - **From–to** differences (old vs. new values or steps).
- Avoid:
  - Ambiguous timing (“soon”, “as possible”).
  - Vague scope (e.g., “some airports” instead of explicit identifiers).

### 3.2 Time-Boxed Validity and Actions

Change notices must:

- Include **explicit timing information**:
  - Effective date/time and time zone.
  - Applicability periods (temporary vs. permanent).
- Define **clear actions**:
  - What crews/operators must do **before**, **during**, and **after** the change becomes effective.
  - Any required confirmation (e.g., acknowledgement or training completion).

### 3.3 Auditability and Traceability

Change notice procedures must be:

- **Auditable**:
  - Records of which notices were issued, when, and to whom.
  - Proof of distribution and, where necessary, acknowledgement.
- **Traceable**:
  - Linked to:
    - Hazards and safety objectives.
    - Requirements (in `../02-00-03_Requirements/`).
    - ERP activations (where applicable).
    - V&V and certification evidence.

Where possible, change notice templates should be **standardized** and stored with training and communication materials (see Section 4).

---

## 4. Training and Materials

HF safety depends on appropriate training for users of ATA 02 operations information.

### 4.1 Training Content

Training materials should cover:

- How to **interpret and navigate** operations information structures (ATA 02 hierarchy, key buckets).
- How to understand **limits, warnings, and applicability tags**.
- How to respond to:
  - **Change notices** (including emergency ones).
  - ERP bulletins and special instructions.
- Typical **error traps** and recommended cross-checks.

### 4.2 Training Material Location

HF-relevant training artefacts (slides, e-learning references, checklists, scenarios) should be stored under:

- `../../02-90_Tables_Schemas_Diagrams/`

with clear subfolders or naming conventions indicating:

- `Training_*` for general HF and operations information training sets.
- Program-specific training variants where needed.

These artefacts should be:

- Referenced from this document and from program safety/certification documents.
- Kept consistent with the latest **requirements**, **procedures**, and **ERP** content.

### 4.3 HF in Training Evaluation

Where appropriate:

- Evaluate training effectiveness using:
  - Knowledge checks and scenario-based exercises.
  - Feedback on clarity and usability of materials.
- Feed results back into:
  - HF design of ops information.
  - Hazard and risk assessments.

---

## 5. Requirements and Verification Hooks

### 5.1 Requirements

HF-related safety expectations should be translated into explicit **requirements** under:

- `../02-00-03_Requirements/`

Examples (to be formalized as requirements):

- HF-01: “Ops information affecting safety-critical tasks shall be assessed for crew workload impact using an accepted HF method where justified (e.g., NASA-TLX).”
- HF-02: “Change notices for safety-relevant information shall include explicit effective date/time, scope, and required actions, and be auditable.”
- HF-03: “Hazard mitigations relying on human detection or action shall be supported by HF assessment and training materials.”

### 5.2 Verification

Verification of HF-related requirements may include:

- **Analytical reviews**:
  - HF expert review of procedures, layouts, and change notices.
- **Empirical evaluations**:
  - Usability tests, simulations, SAGAT or NASA-TLX studies where justified.
- **Operational monitoring**:
  - Incident/feedback analysis related to information use, misunderstandings, or workload issues.

Evidence should be stored and referenced via:

- `../02-00-07_V_AND_V/` and `../02-00-10_Certification/`.

---

## 6. Roles & Responsibilities

HF responsibilities dovetail with roles defined in:

- `../02-00-01-004A_Roles_Responsibilities.md`

In particular:

- **HF Lead**:
  - Owns this document and HF assessment strategy for ATA 02.
  - Provides HF input to hazard analysis, FTA, FMEA, ERP, and training.
- **Safety Engineer (Ops)**:
  - Ensures HF hazards and mitigations are included in safety artefacts and objectives.
- **Ops Information Lead**:
  - Ensures HF considerations are applied in the design and governance of ATA 02 documents.
- **Technical Publications**:
  - Implements HF-driven layout and clarity requirements in all publication formats.
- **Training/Operations**:
  - Develops and maintains HF-aligned training materials and ensures delivery to relevant users.

---

## 7. Usage Guidelines

When designing or changing ATA 02 operations information:

1. **Identify HF-relevant tasks**  
   - Focus on time-critical, high-workload, or safety-critical tasks (e.g., turnarounds, abnormal operations).

2. **Apply HF assessment methods**  
   - Use NASA-TLX, SAGAT, expert review, or other appropriate techniques to evaluate workload, SA, and error traps.

3. **Design for clarity and resilience**  
   - Ensure content structure, layout, and language support easy, correct use and recovery from potential errors.

4. **Define clear change notices and training impacts**  
   - Ensure changes to ops information are accompanied by:
     - Clear notices.
     - Updated training materials, where necessary.

5. **Maintain traceability**  
   - Link HF findings to:
     - Hazards and safety objectives.
     - Requirements and verification.
     - Training content in `../../02-90_Tables_Schemas_Diagrams/`.

---

## 8. What to do next / how to approach this

1. **Add HF requirements**  
   - Create a small HF requirements cluster in `../02-00-03_Requirements/` and tag them clearly (e.g., `Category: HF`).

2. **Seed training content structure**  
   - Under `../../02-90_Tables_Schemas_Diagrams/`, create a minimal `Training_HF_ATA02` folder or file set with placeholders for:
     - HF overview.
     - Navigation of ATA 02.
     - Change notice handling.

3. **Integrate HF checks into workflow**  
   - In ops content and safety review checklists, add explicit HF checkpoints:
     - “HF impact assessed?”  
     - “Change notice HF criteria met (unambiguous, time-boxed, auditable)?”

4. **Connect HF to hazards and ERP**  
   - For hazards like H-02-001 (turnaround data errors), explicitly note HF aspects:
     - Workload, SA, error traps.  
   - Ensure ERP templates include HF guidance for writing clear, operator-friendly bulletins.
