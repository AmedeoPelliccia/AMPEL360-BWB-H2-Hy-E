---
document_id: 95-00-01-009
title: CCert/CVal Circuit for Body+Brain Artifacts in a Model Fleet
version: 1.1
date: 2025-12-13
status: WORKING
owner: AMPEL360 / ATA 95 Governance
classification: INTERNAL
primary_ata: "95"
related_ata: ["20","27","31","42","46","50","60","70","80","90"]
keywords:
  - CCert
  - CVal
  - AM
  - DV
  - DPP
  - IMAGE
  - SBOM
  - BOM
  - OM
  - OAV
  - DT
  - Fleet Model
---

# CCert/CVal Circuit for Body+Brain Artifacts in a Model Fleet
**A scalable epistemological model for any artifact with “Body + Brain” (embedded intelligence) across fleet family/variants/instances**

## 1. Purpose
This master document consolidates, in one coherent and certifiable framework, the **closed-loop circuit** governing the lifecycle of any **Body+Brain** artifact (embedded intelligence) deployed within a **Model Fleet**:

> **AM → DV → DPP → OM → OAV → DT → AM′**  
> (definition → design validation → predictive identity → operational manifestation → on-asset validation → ontogenetic knowledge → updated baseline)

The intent is to make evolution **verifiable**, **traceable**, and **certification-grade**, especially when the “brain” (software/ML) co-evolves with the “body” (hardware/installation/maintainability).

---

## 2. Core Axiom (Freeze)
> **AM defines DPP. DPP predicts OM. Only OAV validates (empirically, on-asset). DT accumulates truth. The loop updates AM (AM′) under controlled change.**

This is the minimum epistemological grammar required to ensure that **nothing is lost**: every change, claim, observation, validation, and learning step is captured as a state of truth.

---

## 3. Definitions (Minimal, non-ambiguous)

### 3.1 Body + Brain
- **Body**: the physical instantiation (hardware, structures, installations, maintainability).  
  Evidence typically includes **CMM**, **BOM**, installation drawings, ICDs, environmental constraints, maintainability tasks.
- **Brain**: the digital instantiation (software loadables, ML/NN models, configs, runtime monitors).  
  Evidence typically includes **IMAGE**, **SBOM**, model passports (ATA 95), configs/calibration, runtime KPIs.

**Key rule**: Body and Brain are **sovereign** (each has its own identity and lifecycle), but **fully interfaced** (contracts + evidence + telemetry mapping).

---

### 3.2 AM — At-Rest Model (Design + Maintainability)
**AM** is the baseline description of the artifact “at rest”:
- engineering definition, interfaces, maintainability, constraints, expected envelopes
- authoritative documentation and baselines
- fleet applicability at family/variant level

AM is necessary but not sufficient: AM must pass **DV**.

---

### 3.3 DV — Design Validation
**DV** is the explicit **validation-by-design layer**:
- confirms AM completeness, internal consistency, and design evidence readiness
- authorizes the creation/update of a predictive contract (DPP)

**DV is the epistemic gate between definition and prediction.**

---

### 3.4 DPP — Digital Product Passport (Predictive Identity)
**DPP** is the “ID card” of the artifact: it declares the **predictive identity** (claims, constraints, envelopes, interfaces) and references evidence.

**DPP is not a full content container by default** (it is a sovereign record with references/hashes and minimal necessary payload to be machine-auditable).  
Like an ID card: “green eyes” without embedding the entire DNA.

---

### 3.5 IMAGE — Software Image (Top-Level Loadable)
**IMAGE** is the **top-level software loadable** (container app / platform assembly):
- binary or bundle + manifest
- hashes/signatures
- compatibility constraints (platform, OS, resources)
- vendor and maintainability stack ownership as applicable
- explicit link to **SBOM** and to embedded model DPPs (if any)

**Rule**: IMAGE is the top-level digital item that operations can load, replace, roll back, and audit.

---

### 3.6 SBOM / BOM
- **SBOM**: software dependency composition (libraries, runtimes, toolchain if needed for assurance).
- **BOM**: physical composition (parts, materials, subcomponents).

---

### 3.7 OM — Ontological Mission (Operational Manifestation)
**OM** is the artifact’s *real manifestation in mission*, under a unique operational context:
- runtime behavior, transitions, performance, anomalies
- time-indexed evidence (telemetry) with context and provenance

OM is not “a manual”; it is **ontogenesis**: the artifact becoming real in context.

---

### 3.8 OAV — On Asset Validation (Generic, scalable)
**OAV** is the empirical validation gate performed **on the asset** (or an explicitly accepted representative asset) that evaluates OM evidence against DPP predictions.

- **OAV is generic**: *On Asset Validation*  
- Specializations may be used as qualifiers (non-breaking):  
  `OAV-AIR` (aircraft), `OAV-GSE`, `OAV-RIG`, `OAV-LAB`, `OAV-SIM`, `OAV-CLOUD`

**Rule**: Simulation-only evidence is *not* OAV unless representativeness is formally declared for the claim/scope.

---

### 3.9 DT — Digital Twin (Ontogenetic, truth-accumulating)
**DT** is not “a simulator output”. DT is the **accumulated validated truth** derived from OM evidence gated by OAV:
- consolidated state, validated learnings, drift knowledge, reliability and performance history
- becomes the knowledge substrate for AM′ and new baselines

---

### 3.10 CCert / CVal
- **CVal**: continuous empirical validation (OM + OAV) as an operational truth pipeline.
- **CCert**: continuous certification as a controlled evolution of certified states (AM/DPP) supported by validated truth (DT).

---

## 4. The Circuit (Canonical, scalable)

```mermaid
flowchart LR
  A[AM\nAt-Rest Model] --> B[DV\nDesign Validation]
  B --> C[DPP\nPredictive Identity]
  C --> D[OM\nOperational Manifestation]
  D --> E[OAV\nOn Asset Validation]
  E --> F[DT\nOntogenetic Digital Twin]
  F --> A2[AM'\nUpdated Baseline]
  A2 --> B2[DV'\nRe-Validation]
  B2 --> C2[DPP'\nRe-Prediction]
````

### 4.1 What each edge means (in one line)

* **AM → DV**: definition becomes admissible knowledge
* **DV → DPP**: authorization to publish predictive claims
* **DPP → OM**: prediction confronted with reality
* **OM → OAV**: empirical evaluation under explicit criteria
* **OAV → DT**: validated truth consolidated as knowledge
* **DT → AM′**: controlled baseline update (closing the loop)

---

## 5. Artifact Model: The “Body+Brain” Minimum Set

### 5.1 Minimum evidence for Body

* CMM (maintainability & testability)
* BOM (composition)
* installation / structural constraints (where relevant)
* ICDs (interfaces)
* environmental constraints (DO-160 class evidence as applicable)

### 5.2 Minimum evidence for Brain

* IMAGE manifest (top-level loadable)
* SBOM (dependencies)
* configuration/calibration and parameter sets
* runtime monitoring signals and thresholds
* model passports (ATA 95) for embedded intelligence, if applicable

### 5.3 Interfacing rule (non-negotiable)

Every DPP claim that matters must map to:

* **telemetry signals** (time-series) and
* **derived metrics** and
* **OAV acceptance criteria**

Otherwise it is not a certifiable claim.

---

## 6. Fleet Model: Family → Variant → Instance

### 6.1 Three truth layers

1. **Family baseline (AM-FAMILY)**: common architecture and invariants
2. **Variant baseline (AM-VARIANT)**: controlled deviations and certified config rules
3. **Instance truth (per serial)**: OM/OAV/DT states, unique operational history

### 6.2 Why the loop scales

Because the grammar is invariant:

* the same entity and relationship semantics apply to one unit and to a fleet
* only the multiplicity changes (more OM events, more OAV campaigns, richer DT)

---

## 7. Where things “live” (ATA reality, without over-personalization)

* **Brain sovereignty**: ATA 95 is the canonical house for DPP and embedded intelligence governance.
* **Body sovereignty**: the physical system remains under its appropriate ATA physical home.
* **Example note (correct placement)**: camera/recording assets are typically better aligned under **ATA 31** than ATA 33 (lights), while their embedded intelligence and DPP governance remain in **ATA 95**.

This preserves both:

* traditional ATA discipline (physical homes), and
* modern traceability discipline (digital sovereignty under ATA 95).

---

## 8. Canonical relationships (Certification lives here)

These relationships are the certifiable narrative:

* `HAS_BASELINE` (System → AM)
* `VALIDATED_BY` (AM → DV)
* `GENERATES` (DV → DPP)
* `EXECUTED_AS` (System → OM)
* `PREDICTS` (DPP → OM)
* `VALIDATED_IN` (OM → OAV)
* `FEEDS` (OAV → DT)
* `UPDATES` (DT → AM′)

**Forbidden shortcut**:

* OM does not rewrite DPP directly
* OAV does not rewrite AM directly
* raw telemetry does not rewrite baselines
  All feedback must pass through DT and controlled change.

---

## 9. Time-series, telemetry, and “truth extraction”

Telemetry is not logging. Telemetry is the instrument by which:

* prediction becomes falsifiable,
* falsifiability becomes validation,
* validation becomes knowledge.

Minimum telemetry attributes (must exist):

* time base, provenance/source, quality flags
* context binding to OM event
* mapping to DPP claim IDs / envelopes

---

## 10. Epistemological storage (what the DB actually stores)

The system of record does not store “data”; it stores **states of truth**:

* AM baselines and their DV gates
* DPP predictive states (versioned)
* OM operational realizations (append-only)
* OAV decisions and evidence packages
* DT snapshots (knowledge accumulation)
* transitions as auditable state evolution

This is the implementation substrate for CCert/CVal.

---

## 11. Operational consequence (why this prevents loss)

Working alone becomes sustainable because the circuit forces crystallization:

* every insight becomes a state (AM/DPP/DT) or evidence (OM/OAV)
* every change is versioned
* every claim is testable against operational truth
* every improvement becomes AM′ + DPP′ under governance

Nothing remains “in the head”; everything becomes an auditable artifact.

---

## 12. Internal References (ATA 95)

* `95-90-02-002_Common_Entity_Schemas.md`
* `95-90-02-003_TimeSeries_and_Telemetry_Schemas.md`
* `95-90-02-006_CCert_CVal_Database_Schema.md`
* `95-90-02-008_Common_Relationship_Semantics.md`
* `95-90-02-005_Links_to_95-00-05_Interfaces_and_95-60_Storages.md`

---

```
::contentReference[oaicite:0]{index=0}
```
