---
Title: "Common Cause Analysis — ATA 02"
Identifier: "AMPEL360-02-00-02-002A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "Safety"
CreatedAt: "2025-11-13"
ModifiedAt: "2025-11-13"
Scope: "Common Cause Analysis for ATA 02 Operations Information within I-INFRASTRUCTURES"
Abstract: "Identifies common cause conditions that can affect safety-relevant operations information under ATA 02, and defines their relationship to FHA, FMEA, and runtime monitoring."
Keywords: ["ATA 02", "Common Cause Analysis", "CCA", "Safety", "Operations Information"]
Compliance:
  - "ATA iSpec 2200"
  - "S1000D"
  - "AMPEL360 Doc Standard v1.1"
  - "Certification Safety Objectives — ATA 02"
Links:
  ParentGeneral: "../"
  SafetyObjectives: "./AMPEL360-02-00-02-001A_Certification_Safety_Objectives.md"
  FHA: "./"   # to be replaced with concrete FHA reference when available
  FMEA: "./"  # to be replaced with concrete FMEA reference when available
  RuntimeMonitoring: "../02-00-06_Engineering/"  # placeholder to runtime monitoring area
ChangeLog:
  - {version: "1.0.0", date: "2025-11-13", author: "Safety", change: "Initial creation"}
---

# Common Cause Analysis (CCA) — ATA 02

## 1. Purpose

This document captures **Common Cause Conditions (CCCs)** that can affect **safety-relevant operations information** under **ATA 02 — Operations Information**. It focuses on common information sources, infrastructure, and processes that, if degraded or misused, could simultaneously impact multiple operational products, procedures, or users.

It supports the **Certification Safety Objectives — ATA 02** by:

- Identifying shared vulnerabilities in the way operations information is produced, stored, and distributed.
- Providing inputs to FHA, FMEA, and runtime monitoring strategies.
- Guiding requirements and mitigations for information integrity, availability, and timeliness.

**Hazard generation and classification** follow [Hazard Analysis Methodology — ATA 02](./AMPEL360-02-00-02-007A_Hazard_Analysis_Methodology.md).

## 2. Scope

CCA for ATA 02 covers:

- **Information infrastructure** (data sources, networks, storage, publication systems) used to create and distribute ops information.
- **Human and process elements** (shared roles, procedures, tooling) that can introduce correlated errors.
- **Latent conditions** (e.g., configuration drift, outdated sources) that may remain undetected until multiple dependent products are affected.

System-level or hardware-specific CCCs are addressed in the owning technical ATAs and referenced where they impact ATA 02 content.

---

## 3. Common Cause Categories

### 3.1 Physical Common Cause Conditions

These are **physical or technical infrastructures** that, if degraded or failed, can affect multiple operations information products at once.

Examples for ATA 02 include:

- **Shared power and communications infrastructures**
  - Single points of failure in datacenters or on-premise facilities hosting:
    - Ops information repositories.
    - Publication/CSDB servers.
    - Distribution services (e.g., EFB sync, portal hosting).
  - Network outages affecting data replication between primary and backup sites.

- **Shared data sources**
  - Common airport or infrastructure databases (e.g., AODB, NOTAM feeds, weather feeds, airport constraints databases) used by:
    - Turnaround planning tools.
    - Ops procedure generators.
    - Capacity and slot planning.
  - Single upstream provider for critical operational parameters (e.g., runway availability, noise restrictions).

- **Co-located infrastructure**
  - Co-location of critical services (e.g., CAA-approved publication environment, safety-critical data stores) in a single facility:
    - Localized physical events (fire, flooding, building access loss) affecting multiple services.
    - Maintenance on shared hardware impacting several ops information systems simultaneously.

**Implications**

- Multiple ops products can become:
  - Unavailable (no access to procedures or limits).
  - Out-of-date (stale snapshots).
  - Inconsistent (partial updates between sites/systems).

### 3.2 Functional Common Cause Conditions

These are **shared processes, roles, or functional elements** that can introduce correlated errors across multiple documents or data sets.

Examples for ATA 02 include:

- **Shared procedures and authoring patterns**
  - Standard templates or authoring macros reused across:
    - Ops manuals, quick reference cards, line procedures.
  - A defect in a template (e.g., missing caution, wrong precondition) propagating to many documents.

- **Shared roles and responsibilities**
  - A single Ops Information Lead, Safety Engineer, or Tech Pubs specialist:
    - Misinterpreting a change request or safety constraint.
    - Applying a flawed rule across multiple publications or versions.
  - Overload or inadequate training leading to systematic mistakes in data entry or approvals.

- **Common publication pipeline**
  - A single publication workflow or toolchain for:
    - Data extraction from design tools.
    - Transformation into publication formats (iSpec 2200, S1000D, PDF, EFB formats).
    - Final distribution to operators.
  - Misconfiguration or tool defects causing:
    - Missing sections.
    - Misaligned limitations.
    - Incorrect version tagging across multiple products simultaneously.

**Implications**

- Errors can be **systematic** rather than isolated, affecting:
  - Entire families of procedures.
  - Multiple operator fleets or configurations.
  - Several releases/EIS tags at once.

### 3.3 Latent Common Cause Conditions

These are **hidden or time-lagged conditions** that may remain undetected until triggered by an event or by multiple dependent changes.

Examples for ATA 02 include:

- **Configuration errors**
  - Incorrect mapping between:
    - Design baselines and ops information versions.
    - EIS tags and operator-specific configurations.
  - Misassigned applicability ranges (e.g., wrong aircraft or configuration tags), causing:
    - Ops information to be used outside its valid domain.
    - Valid information not being delivered where needed.

- **Stale data ingestion**
  - Automated ingestion pipelines from external or internal sources (airport data, weather, infrastructure constraints) that:
    - Fail silently.
    - Are disabled without proper notice.
  - Ops content continuing to rely on **outdated assumptions** about airport layouts, procedures, or limitations.

- **Publication delays or partial roll-out**
  - Approved safety-critical changes:
    - Not published in time.
    - Published in one channel (e.g., central portal) but not another (e.g., EFB, printed copies).
  - Lack of confirmation that operators have received and acknowledged critical updates.

**Implications**

- Hazards triggered when:
  - A latent issue aligns with specific operational conditions (e.g., particular airport, weather, traffic pattern).
  - Multiple dependent documents are assumed to be synchronized but are not.

---

## 4. Interfaces with Other Safety Artefacts

This CCA is **not standalone**; it feeds and is fed by other safety analyses and monitoring activities.

### 4.1 FHA (Functional Hazard Assessment)

- FHA identifies **hazards and operational failure conditions** involving ATA 02 information.  
- CCA provides:
  - Candidate common causes to be included in FHA scenarios (e.g., global mis-tagging of limitations).
- FHA results in:
  - Severity assessments and safety objectives that may require additional mitigations for CCA-identified conditions.

**Reference:** Link to FHA artefacts once established (see `Links.FHA` in front-matter).

### 4.2 FMEA / FTA

- **FMEA**:
  - Uses CCA categories as potential shared failure modes (e.g., “shared template defect,” “stale data source”).
- **FTA**:
  - Incorporates CCA as **common cause events** in fault trees (e.g., single database failure causing multiple procedure errors).

**Reference:** Link to FMEA and FTA artefacts once established (see `Links.FMEA` and safety folder structure).

### 4.3 Runtime Monitoring

CCA informs **runtime monitoring strategies** to detect and mitigate common causes in operation, e.g.:

- Monitoring for:
  - Inconsistent versions across channels (portal vs. EFB vs. printed).
  - Unexpected stagnation in data refresh cycles.
  - Anomalous patterns in ops usage or incidents pointing to shared information defects.

- Defining triggers for:
  - Emergency publication workflows.
  - Safety reviews of common assets (templates, shared data tables, tooling).

**Reference:** Runtime monitoring concepts are typically maintained under `../02-00-06_Engineering/` or `../02-00-10_Certification/` depending on program conventions.

---

## 5. Mitigation and Requirements Hooks

For each CCC category, programs should derive **mitigations and requirements**, for example:

- **Technical mitigations**
  - Redundant data sources or cross-checks (e.g., multiple airport data feeds).
  - Health monitoring of pipelines and publication systems.
  - Automated consistency checks across versions and channels.

- **Process mitigations**
  - Independent checks for template or macro changes.
  - Segregation of duties for safety-critical approvals.
  - Formal go/no-go criteria for publication with safety changes.

- **Organizational mitigations**
  - Training and competency requirements for key roles (Ops Information Lead, Safety Engineer, Tech Pubs).
  - Clear escalation paths for detected CCA-related anomalies.

These should be instantiated as **requirements** in `../02-00-03_Requirements/` and **MoC/evidence** in `../02-00-10_Certification/`, with traceability to the Certification Safety Objectives and this CCA.

---

## 6. Usage Guidelines

When performing safety or certification work on ATA 02:

1. **Use this CCA as a checklist**  
   - For FHA, FMEA, and FTA sessions, systematically review:
     - Physical CCCs.
     - Functional CCCs.
     - Latent CCCs.
   - Add program-specific CCCs where relevant (new tools, new data flows, new roles).

2. **Record explicit CCC references**  
   - When a hazard, failure mode, or fault tree event is driven by a common cause, reference:
     - This document’s identifier (`AMPEL360-02-00-02-002A`) and the corresponding section.

3. **Feed runtime monitoring design**  
   - Use the identified CCCs to:
     - Define monitoring points and KPIs.
     - Identify where alerts or dashboards should be implemented.

4. **Maintain alignment with objectives and requirements**  
   - Ensure:
     - CCA entries map to safety objectives in `Certification Safety Objectives — ATA 02`.  
     - Derived requirements in `../02-00-03_Requirements/` are kept in sync when CCC understanding evolves.

---
