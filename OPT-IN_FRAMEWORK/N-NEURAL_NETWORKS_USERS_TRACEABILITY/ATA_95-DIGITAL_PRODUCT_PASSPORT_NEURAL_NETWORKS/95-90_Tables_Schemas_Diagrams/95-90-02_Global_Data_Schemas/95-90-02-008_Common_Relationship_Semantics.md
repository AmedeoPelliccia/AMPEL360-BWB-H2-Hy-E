# 95-90-02-008 — Common Relationship Semantics

**Document ID**: 95-90-02-008  
**Version**: 1.0  
**Date**: 2025-12-13  
**Status**: WORKING  
**Owner**: AMPEL360 – ATA 95 Semantics & Traceability  
**Applicability**: Global (All ATA Chapters)

---

## 1. Purpose

This document defines the **formal semantics** of the canonical relationships used across AMPEL360 for:

* Certification
* Validation
* Traceability
* Impact analysis

It ensures that relationships are **unambiguous, auditable, and epistemologically sound**.

---

## 2. Relationship Taxonomy

Relationships are classified by their epistemological nature:

| Type               | Nature                        | Example              |
|--------------------|-------------------------------|----------------------|
| **Ontological**    | Existence and composition     | HAS_BASELINE         |
| **Epistemic**      | Knowledge and validation      | VALIDATED_BY         |
| **Operational**    | Runtime execution             | EXECUTED_AS          |
| **Transformational**| State evolution              | GENERATES, UPDATES   |

---

## 3. Canonical Relationships

### 3.1 HAS_BASELINE

**Type**: Ontological  
**Direction**: SystemProduct → Baseline  
**Cardinality**: 1:N

> The system is described by this baseline at rest.

**Certification Meaning**:  
The baseline defines the *intended identity*. Multiple baselines over time represent design evolution.

**Temporal Semantics**:  
A SystemProduct may have multiple baselines across its lifecycle, but only one is "current" at any given time.

**Implementation**:
```cypher
(s:System {code: "Q100"})-[:HAS_BASELINE]->(am:AM {version: "v2.1"})
```

```sql
SELECT b.* FROM baseline b
WHERE b.system_id = 'system-uuid'
  AND b.status = 'Approved'
ORDER BY b.created_at DESC
LIMIT 1;
```

---

### 3.2 VALIDATED_BY

**Type**: Epistemic  
**Direction**: Baseline → Validation  
**Cardinality**: 1:N

> The baseline has been formally assessed against defined criteria.

**Certification Meaning**:  
Transforms description into trusted knowledge. Multiple validations may occur (DV, V&V, compliance checks).

**Epistemic Significance**:  
Without validation, a baseline is merely a claim. With validation, it becomes certifiable knowledge.

**Implementation**:
```cypher
(am:AM)-[:VALIDATED_BY]->(dv:DV {status: "Passed"})
```

**Certification Rule**:  
A baseline cannot progress to DPP generation without at least one `VALIDATED_BY` relationship to a passed Validation.

---

### 3.3 GENERATES

**Type**: Transformational  
**Direction**: Validation → DPP  
**Cardinality**: 1:1

> Validation authorizes the creation of a predictive passport.

**Certification Meaning**:  
No valid DPP without DV. This is the gate from "design definition" to "operational prediction".

**Temporal Semantics**:  
GENERATES is the moment of transformation. The timestamp of this relationship marks when design became prediction.

**Implementation**:
```cypher
(dv:DV {status: "Passed"})-[:GENERATES]->(dpp:DPP {dpp_uid: "DPP_..."})
```

**Certification Rule**:  
Once generated, the DPP inherits the immutability of its source Validation and Baseline.

---

### 3.4 PREDICTS

**Type**: Epistemic (Forward-looking)  
**Direction**: DPP → OM Event  
**Cardinality**: 1:N

> The DPP claims that the system will behave this way in operation.

**Certification Meaning**:  
This is a **promise**, not truth. The DPP makes forward-looking claims about future operational behavior.

**Epistemic Significance**:  
PREDICTS establishes the expected behavior envelope against which reality (OM) will be measured.

**Implementation**:
```cypher
(dpp:DPP)-[:PREDICTS]->(om:OM {mission_id: "FLT-042"})
```

**Validation Pattern**:  
Every OM event should trace back to a DPP that predicted its context. Unpredicted operations are anomalies.

---

### 3.5 EXECUTED_AS

**Type**: Operational  
**Direction**: SystemProduct → OM Event  
**Cardinality**: 1:N

> The system operates in a specific mission context.

**Certification Meaning**:  
This relationship links the ontological subject (SystemProduct) to its operational manifestations.

**Temporal Semantics**:  
EXECUTED_AS captures the "becoming" of the system — its ontogenesis from design to reality.

**Implementation**:
```cypher
(s:System)-[:EXECUTED_AS]->(om:OM {started_at: "2025-01-15T10:30:00Z"})
```

---

### 3.6 VALIDATED_IN

**Type**: Epistemic (Empirical)  
**Direction**: OM Event → OAV  
**Cardinality**: N:M

> Operational evidence is aggregated and evaluated in a validation campaign.

**Certification Meaning**:  
Reality confronts prediction. Multiple OM events contribute to a single OAV campaign, and a single OM event may be used in multiple campaigns.

**Epistemic Significance**:  
VALIDATED_IN is where empirical truth is extracted from operational data.

**Implementation**:
```cypher
(om:OM)-[:VALIDATED_IN]->(oav:OAV {name: "Phase1_Validation"})
```

```sql
SELECT om.*, oav.name, oav.result
FROM om_event om
JOIN oav_event_link link ON link.om_event_id = om.id
JOIN oav_campaign oav ON oav.id = link.oav_id
WHERE oav.dpp_id = 'specific-dpp-uuid';
```

---

### 3.7 FEEDS

**Type**: Transformational  
**Direction**: OAV → DigitalTwin  
**Cardinality**: 1:N

> Validated evidence updates the digital twin's accumulated knowledge.

**Certification Meaning**:  
FEEDS is the knowledge consolidation step. OAV results are not just pass/fail — they inform the DT's understanding of the system.

**Epistemic Significance**:  
The DT is ontogenetic: it learns from validated operational evidence. FEEDS is how that learning occurs.

**Implementation**:
```cypher
(oav:OAV {result: "Passed"})-[:FEEDS]->(dt:DT {dt_version: "v1.3"})
```

**Certification Rule**:  
Only completed OAV campaigns with documented results may FEED a DT snapshot.

---

### 3.8 UPDATES

**Type**: Transformational  
**Direction**: DigitalTwin → Baseline′  
**Cardinality**: N:1

> Accumulated truth informs the next design iteration.

**Certification Meaning**:  
Enables Continuous Certification. The DT's accumulated knowledge drives design evolution.

**Temporal Semantics**:  
UPDATES closes the loop. It represents the moment when operational learnings become design inputs.

**Implementation**:
```cypher
(dt:DT)-[:UPDATES]->(am:AM {version: "v2.2"})
```

**Certification Rule**:  
UPDATES must document what changed and why. Traceability from DT findings to baseline updates is mandatory.

---

## 4. Forbidden Relationships

The following are **explicitly forbidden** as they violate epistemological integrity:

| Forbidden Relationship | Reason                                                    |
|------------------------|-----------------------------------------------------------|
| OM → DPP               | Reality cannot redefine prediction                        |
| OAV → DPP (direct)     | Validation must pass through DT before informing design   |
| Telemetry → Baseline   | Raw data cannot directly alter design                     |
| DPP → AM               | Prediction cannot retroactively change its basis          |
| Baseline → OM          | Design cannot directly create operational reality         |

**Rationale**:  
These forbidden paths would create epistemological contradictions or bypass necessary validation gates.

---

## 5. Relationship Constraints

### 5.1 Temporal Constraints

1. **All relationships are time-bound**  
   Every relationship has a `created_at` timestamp

2. **Temporal ordering must be preserved**  
   `AM.created_at < DV.validated_at < DPP.created_at < OM.started_at`

3. **No retroactive relationships**  
   A relationship cannot point to an entity created after it

### 5.2 Version Awareness

1. **Relationships are version-specific**  
   `AM v1.0 -[:GENERATES]-> DPP v1.0`, not just `AM -> DPP`

2. **Version evolution is traceable**  
   `DPP v1.0 -[:SUPERSEDED_BY]-> DPP v1.1`

### 5.3 Immutability

1. **Certified relationships are immutable**  
   Once a DPP is certified, its `VALIDATED_BY` and `GENERATES` relationships cannot change

2. **Append-only operational relationships**  
   `EXECUTED_AS`, `VALIDATED_IN` accumulate; they are never deleted

### 5.4 Authority Requirements

1. **Relationship creation requires authority**  
   `VALIDATED_BY` requires validator credentials  
   `GENERATES` requires DV approval  
   `UPDATES` requires change authority

2. **All authority is logged**  
   Every relationship stores `created_by` and optional `approved_by`

---

## 6. Neo4j Encoding Examples

### 6.1 Complete Lifecycle Path

```cypher
MATCH path = (s:System)-[:HAS_BASELINE]->(am:AM)
             -[:VALIDATED_BY]->(dv:DV)
             -[:GENERATES]->(dpp:DPP)
             -[:PREDICTS]->(om:OM)
             -[:VALIDATED_IN]->(oav:OAV)
             -[:FEEDS]->(dt:DT)
             -[:UPDATES]->(am_next:AM)
WHERE s.code = 'Q100'
RETURN path
```

### 6.2 Impact Analysis Query

> Find all OM events that would be invalidated if a DPP is retired

```cypher
MATCH (dpp:DPP {dpp_uid: 'specific-dpp'})-[:PREDICTS]->(om:OM)
WHERE dpp.status = 'Retired'
RETURN om.mission_id, om.started_at
ORDER BY om.started_at DESC
```

### 6.3 Traceability Query

> Trace a DT snapshot back to its design origins

```cypher
MATCH path = (dt:DT {dt_version: 'v1.3'})-[:FEEDS*0..1]-(oav:OAV)
             -[:VALIDATED_IN*0..]-(om:OM)
             -[:PREDICTS*0..1]-(dpp:DPP)
             -[:GENERATES*0..1]-(dv:DV)
             -[:VALIDATED_BY*0..1]-(am:AM)
             -[:HAS_BASELINE*0..1]-(s:System)
RETURN path
```

---

## 7. Alignment with CCert / CVal

| Relationship   | Loop Phase                 | CCert/CVal Role                       |
|----------------|----------------------------|---------------------------------------|
| HAS_BASELINE   | Definition                 | Establishes design baseline           |
| VALIDATED_BY   | DV                         | Gates design validity                 |
| GENERATES      | Prediction                 | Creates operational promise           |
| PREDICTS       | Future claim               | Establishes expected behavior         |
| EXECUTED_AS    | Reality manifestation      | Records actual operation              |
| VALIDATED_IN   | Empirical truth            | Compares prediction vs reality        |
| FEEDS          | Knowledge consolidation    | Builds ontogenetic understanding      |
| UPDATES        | Certification continuity   | Closes loop for next design iteration |

---

## 8. Relationship Lifecycle States

Relationships themselves have states:

| State      | Meaning                                                  |
|------------|----------------------------------------------------------|
| **Draft**  | Proposed but not yet approved                            |
| **Active** | Currently valid and in use                               |
| **Deprecated** | Superseded by newer relationship but retained for history |
| **Invalid** | Determined to be erroneous; marked for investigation     |

**Example**: A `VALIDATED_BY` relationship may become **Deprecated** if the validation is superseded by a more comprehensive assessment.

---

## 9. Key Epistemological Principle

> **Relationships are where certification actually lives.  
> Data without semantics is not certifiable.**

* A Baseline without `VALIDATED_BY` is just a document
* A DPP without `PREDICTS` connections is just metadata
* An OM event without `VALIDATED_IN` is just telemetry
* A DT without `FEEDS` is just a model

**The relationships ARE the certification narrative.**

---

## 10. Cross-References

### 10.1 Related Documents

* [95-90-02-002_Common_Entity_Schemas.md](./95-90-02-002_Common_Entity_Schemas.md) — Entity definitions
* [95-90-02-003_TimeSeries_and_Telemetry_Schemas.md](./95-90-02-003_TimeSeries_and_Telemetry_Schemas.md) — Telemetry semantics
* [95-90-02-006_CCert_CVal_Database_Schema.md](./95-90-02-006_CCert_CVal_Database_Schema.md) — Physical implementation
* [95-90-02-007_CCert_CVal_Core_Data_Model.md](./95-90-02-007_CCert_CVal_Core_Data_Model.md) — Logical model
* [95-90-01-005_CCert_CVal_Glossary.md](../95-90-01_Global_Reference_Taxonomies/95-90-01-005_CCert_CVal_Glossary.md) — Terminology

### 10.2 Future Documents

* **95-90-02-009_CCert_CVal_Event_Model.md** — Event sourcing for relationship creation
* **95-90-02-010_CCert_CVal_Query_Cookbook.md** — Standard relationship queries

---

## 11. Version History

| Version | Date       | Author                               | Changes                                    |
|---------|------------|--------------------------------------|--------------------------------------------|
| 1.0     | 2025-12-13 | AMPEL360 ATA 95 Semantics Architecture| Initial relationship semantics definition |

---

## 12. Document Control

- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by [Approver]
- **Status**: WORKING – Subject to formal review and approval
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **Sub-bucket**: 02_Global_Data_Schemas
- **Document ID**: 95-90-02-008
- **Last AI update**: 2025-12-13
- **Criticality**: FOUNDATIONAL

---

## 13. Final Note

This document is not about database foreign keys.  
**This document is about how knowledge flows through the certification process.**

Every relationship type defined here carries epistemological weight:
* **HAS_BASELINE**: Identity
* **VALIDATED_BY**: Trust
* **GENERATES**: Authorization
* **PREDICTS**: Promise
* **EXECUTED_AS**: Reality
* **VALIDATED_IN**: Truth
* **FEEDS**: Learning
* **UPDATES**: Evolution

Without understanding these semantics, you have tables and links.  
With these semantics, you have **certifiable epistemology**.

---

**End of Document**
