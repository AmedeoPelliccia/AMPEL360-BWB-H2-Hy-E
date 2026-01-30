# 95-90-02-002 — Common Entity Schemas

**Document ID**: 95-90-02-002  
**Version**: 1.0  
**Date**: 2025-12-13  
**Status**: WORKING  
**Owner**: AMPEL360 – ATA 95 Data Architecture  
**Applicability**: Global (All ATA Chapters)  

---

## 1. Purpose

This document defines the **Common Entity Schemas** used across the AMPEL360 Continuous Certification (**CCert**) and Continuous Validation (**CVal**) framework.

These entities represent **ontological primitives** shared by all domains (physical, digital, operational, AI), enabling:

- Cross-ATA interoperability  
- Stable database schemas  
- Traceability across AM, DPP, OM, OAV, DT  
- Long-term certification and auditability  

They are **domain-agnostic**, **ATA-neutral**, and **semantically stable**.

---

## 2. Design Principles

1. **Single definition of truth**  
   Each entity is defined once and reused everywhere.

2. **Ontological consistency**  
   Entities represent *what exists*, not how it is implemented.

3. **Versionable by nature**  
   All entities support lifecycle evolution.

4. **Certification-safe**  
   No entity definition embeds operational assumptions.

---

## 3. Core Common Entities (Canonical Set)

The following entities are mandatory and form the **minimal closed set** required to implement CCert/CVal.

---

## 3.1 ENTITY: SystemProduct

### Definition  
A **SystemProduct** is any identifiable technical subject participating in design, certification, operation, or validation.

### Examples
- Aircraft (Q100)
- LRU (FCC, Camera Unit)
- Neural Network model
- Dataset
- Ground system

### Schema (Logical)

```json
{
  "id": "UUID",
  "code": "string",
  "name": "string",
  "system_type": "aircraft | lru | subsystem | nn_model | dataset | platform",
  "primary_ata": "string",
  "description": "string",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

### Ontological Role

**Subject of existence** — everything else attaches to this.

### Certification Significance

The SystemProduct code is the sovereign identifier that persists across all lifecycle stages, from initial design through retirement. It is the anchor for all traceability.

---

## 3.2 ENTITY: Baseline

### Definition

A **Baseline** is a frozen description of a SystemProduct at rest.

### Specializations

* AM Baseline
* Architecture Baseline
* Configuration Baseline

### Schema

```json
{
  "id": "UUID",
  "system_id": "UUID",
  "baseline_type": "AM | ARCH | CONFIG",
  "version": "string",
  "status": "Draft | Approved | Retired",
  "reference": "string",
  "metadata": "object",
  "created_at": "timestamp"
}
```

### Ontological Role

**Static identity** — what the system *is supposed to be*.

### Certification Significance

Approved baselines are immutable. They represent the authoritative definition against which all predictions and validations are measured.

---

## 3.3 ENTITY: Validation

### Definition

A **Validation** represents formal evidence that a Baseline satisfies defined criteria.

### Types

* Design Validation (DV)
* Verification Validation (V&V)
* Compliance Validation

### Schema

```json
{
  "id": "UUID",
  "baseline_id": "UUID",
  "validation_type": "DV | VV | Compliance",
  "status": "Passed | Conditional | Failed",
  "criteria": "object",
  "evidence_ref": "string",
  "validated_at": "timestamp",
  "validated_by": "string"
}
```

### Ontological Role

**Epistemic gate** — transforms description into trusted knowledge.

### Certification Significance

Validation is the formal gate that permits progression from static design (Baseline) to predictive identity (DPP). No DPP may exist without passing Validation.

---

## 3.4 ENTITY: DigitalProductPassport (DPP)

### Definition

A **Digital Product Passport** is the **predictive identity** of a SystemProduct.

It states **what the system claims it will do**, under which constraints.

### Schema

```json
{
  "id": "UUID",
  "dpp_uid": "string",
  "system_id": "UUID",
  "baseline_id": "UUID",
  "validation_id": "UUID",
  "primary_ata": "string",
  "related_ata": ["string"],
  "status": "Draft | Certified | InService | Retired",
  "lifecycle_stage": "Design | InService | Deprecated",
  "payload": "object",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

### Ontological Role

**Predictive contract** — declares future behaviour.

### Certification Significance

The DPP is a promise. It predicts operational behavior before that behavior occurs. Certified DPPs are immutable commitments that can only be superseded by new versions with full traceability.

---

## 3.5 ENTITY: MissionEvent (OM)

### Definition

A **MissionEvent** is a concrete instantiation of a SystemProduct operating in a unique real-world context.

### Schema

```json
{
  "id": "UUID",
  "system_id": "UUID",
  "dpp_id": "UUID",
  "mission_id": "string",
  "context": "object",
  "observed_metrics": "object",
  "started_at": "timestamp",
  "ended_at": "timestamp"
}
```

### Ontological Role

**Reality manifestation** — where predictions meet the world.

### Certification Significance

MissionEvents are the empirical truth. They are append-only and immutable, forming the evidentiary basis for all validation activities. Each event captures what the system *actually did* in a specific context.

---

## 3.6 ENTITY: OperationalValidation (OAV)

### Definition

An **OperationalValidation** aggregates MissionEvents to validate a DPP against real operational evidence.

### Schema

```json
{
  "id": "UUID",
  "dpp_id": "UUID",
  "name": "string",
  "scope": "string",
  "acceptance_criteria": "object",
  "result": "Passed | Partial | Failed",
  "evidence": "object",
  "started_at": "timestamp",
  "closed_at": "timestamp"
}
```

### Ontological Role

**Truth extraction** — establishes verifiable reality.

### Certification Significance

OAV campaigns compare DPP predictions against OM reality. They answer the fundamental certification question: "Did the system behave as predicted?" Acceptance criteria must be defined before data collection to prevent post-hoc rationalization.

---

## 3.7 ENTITY: DigitalTwinSnapshot (DT)

### Definition

A **Digital Twin Snapshot** is a consolidated state derived from validated operational evidence.

### Schema

```json
{
  "id": "UUID",
  "system_id": "UUID",
  "dpp_id": "UUID",
  "source_oav_id": "UUID",
  "dt_version": "string",
  "state": "object",
  "created_at": "timestamp"
}
```

### Ontological Role

**Accumulated truth** — memory of what the system truly is.

### Certification Significance

The Digital Twin is ontogenetic: it learns from operation. It represents the synthesis of design intent (DPP) and validated reality (OAV). DT snapshots must reference their source OAV to maintain traceability to evidence.

---

## 4. Common Relationship Types

These relationships are **canonical** and reused everywhere.

| Relationship   | Meaning                     | Semantic Direction      |
| -------------- | --------------------------- | ----------------------- |
| `HAS_BASELINE` | System → Baseline           | Composition             |
| `VALIDATED_BY` | Baseline → Validation       | Epistemic transformation|
| `GENERATES`    | Validation → DPP            | Creation                |
| `PREDICTS`     | DPP → MissionEvent          | Forward projection      |
| `VALIDATED_IN` | MissionEvent → OAV          | Evidence aggregation    |
| `FEEDS`        | OAV → DigitalTwin           | Knowledge consolidation |
| `UPDATES`      | DigitalTwin → Baseline′     | Loop closure            |

### Semantic Clarity

* **Forward relationships** (HAS, GENERATES, PREDICTS): Design-to-operation flow
* **Backward relationships** (VALIDATED_BY, VALIDATED_IN): Evidence-to-knowledge flow
* **Circular relationships** (FEEDS, UPDATES): Continuous learning loop

---

## 5. Alignment with CCert / CVal Loop

```text
SystemProduct
   ↓ HAS_BASELINE
Baseline
   ↓ VALIDATED_BY
Validation
   ↓ GENERATES
DigitalProductPassport
   ↓ PREDICTS
MissionEvent (OM)
   ↓ VALIDATED_IN
OperationalValidation (OAV)
   ↓ FEEDS
DigitalTwinSnapshot
   ↓ UPDATES
Baseline′
```

This entity set is **closed, sufficient, and minimal**.

**Closed**: No external entities are needed to express the full lifecycle.  
**Sufficient**: All certification states can be represented.  
**Minimal**: No entity can be removed without breaking the loop.

---

## 6. Usage Rules

### 6.1 Entity Purity

1. **No ATA-specific extensions inside common entities**
   * Domain-specific attributes live in `payload`, `context`, or `state` fields
   * Core schema remains stable across all ATAs

2. **All certified states are immutable**
   * Approved Baselines cannot be modified
   * Certified DPPs cannot be altered
   * MissionEvents cannot be edited or deleted

3. **Operational data is append-only**
   * MissionEvents accumulate
   * OAV campaigns build incrementally
   * DT snapshots represent points in time, never replace history

### 6.2 Versioning Strategy

* Baselines use semantic versioning: `vMAJOR.MINOR.PATCH`
* DPPs inherit baseline version and add lifecycle suffix: `DPP_v1.2_InService`
* DT snapshots use timestamp or sequence: `DT_2025-12-13_001`

### 6.3 Status Transitions

**Baseline:**
```
Draft → InReview → Approved → [Superseded | Retired]
```

**DPP:**
```
Draft → UnderReview → Certified → InService → [Suspended | Retired]
```

**OAV Campaign:**
```
Planned → Running → [Paused] → Completed → Closed
```

---

## 7. Entity Cardinalities

| Relationship                  | Cardinality |
| ----------------------------- | ----------- |
| SystemProduct → Baseline      | 1:N         |
| Baseline → Validation         | 1:N         |
| Validation → DPP              | 1:1         |
| DPP → MissionEvent            | 1:N         |
| MissionEvent → OAV            | N:M         |
| OAV → DigitalTwinSnapshot     | 1:N         |
| DigitalTwinSnapshot → Baseline| N:1         |

---

## 8. Ontological Guarantees

This entity set guarantees:

1. **Traceability**: Every operational truth traces back to design intent
2. **Auditability**: Every certification claim has timestamped evidence
3. **Reproducibility**: The loop can be reconstructed from persistent data
4. **Evolvability**: New versions maintain links to predecessors
5. **Accountability**: All transformations are attributed and timestamped

---

## 9. Cross-References

### 9.1 Related Documents

* [95-90-02-007_CCert_CVal_Core_Data_Model.md](./95-90-02-007_CCert_CVal_Core_Data_Model.md) — Logical data model
* [95-90-02-006_CCert_CVal_Database_Schema.md](./95-90-02-006_CCert_CVal_Database_Schema.md) — Physical implementation
* [95-90-01-005_CCert_CVal_Glossary.md](../95-90-01_Global_Reference_Taxonomies/95-90-01-005_CCert_CVal_Glossary.md) — Terminology
* [95-00-01-007_DPP_Data_Model_and_Identifiers.md](../../95-00_GENERAL/95-00-01_Overview/) — DPP details

### 9.2 Future Documents

* **95-90-02-008_Common_Relationship_Semantics.md** — Formalization of relationship meanings in certification context
* **95-90-02-009_Entity_Lifecycle_Management.md** — Rules for entity state transitions

---

## 10. Version History

| Version | Date       | Author                          | Description                           |
| ------- | ---------- | ------------------------------- | ------------------------------------- |
| 1.0     | 2025-12-13 | AMPEL360 ATA 95 Data Architecture| Initial definition of common entities |

---

## 11. Document Control

- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by [Approver]
- **Status**: WORKING – Subject to formal review and approval
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **Sub-bucket**: 02_Global_Data_Schemas
- **Document ID**: 95-90-02-002
- **Last AI update**: 2025-12-13
- **Criticality**: FOUNDATIONAL

---

## 12. Final Note

This is not "another specification."  
**This is the ontological alphabet of AMPEL360.**

If this document exists and is respected, **nothing is lost**, even working alone.

Every system, every prediction, every validation, every truth — all expressed in this common language.

**This is the grammar of continuous certification.**

---

**End of Document**
