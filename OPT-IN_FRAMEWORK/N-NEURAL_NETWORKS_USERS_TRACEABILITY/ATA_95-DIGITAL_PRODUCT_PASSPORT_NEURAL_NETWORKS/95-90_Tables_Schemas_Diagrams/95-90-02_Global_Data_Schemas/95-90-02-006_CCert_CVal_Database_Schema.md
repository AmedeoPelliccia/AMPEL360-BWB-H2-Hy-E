# 95-90-02-006 — CCert / CVal Database Schema

**Detailed PostgreSQL & Neo4j Implementation**

**Document ID**: 95-90-02-006  
**Version**: 1.0  
**Date**: 2025-12-13  
**Status**: WORKING  
**Owner**: AMPEL360 – ATA 95 Data & Certification Architecture  
**Scope**: Global (All ATA via references)

---

## 1. Purpose

This document specifies the **physical database schema** supporting the **Continuous Certification (CCert)** and **Continuous Validation (CVal)** loop:

> **AM → DV → DPP → OM → OAV → DT → AM′**

It translates the **ontological and conceptual model** defined in:

* [95-90-02-007_CCert_CVal_Core_Data_Model.md](./95-90-02-007_CCert_CVal_Core_Data_Model.md)

into:

* **PostgreSQL** (authoritative, auditable, transactional store)
* **Neo4j** (traceability, dependency, impact-analysis graph)

This schema is **certification-grade**, traceable, and designed to sustain long-lived aerospace programs.

---

## 2. Architectural Principles

### 2.1 Separation of Concerns

| Layer            | Technology | Role                               |
| ---------------- | ---------- | ---------------------------------- |
| Truth & Evidence | PostgreSQL | Immutable, auditable records       |
| Traceability     | Neo4j      | Semantic and cross-ATA reasoning   |
| Payloads         | JSONB      | Extensibility without schema churn |
| Identity         | UUID       | Global, sovereign identifiers      |

---

### 2.2 Certification-Driven Design Rules

1. **No destructive updates** on certified data
2. **Versioned entities only** (AM, DPP, DT)
3. **Operational truth (OM/OAV) is append-only**
4. **Prediction ≠ Validation** (explicitly separated)

---

## 3. PostgreSQL Schema (Authoritative Store)

### 3.1 SYSTEM_PRODUCT

```sql
CREATE TABLE system_product (
  id UUID PRIMARY KEY,
  code VARCHAR(64) UNIQUE NOT NULL,
  name VARCHAR(256) NOT NULL,
  system_type VARCHAR(64) NOT NULL,
  primary_ata VARCHAR(16),
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

CREATE INDEX idx_system_product_code ON system_product(code);
CREATE INDEX idx_system_product_type ON system_product(system_type);
CREATE INDEX idx_system_product_ata ON system_product(primary_ata);
```

**Meaning**  
Defines the *ontological subject*: aircraft, LRU, NN, dataset, platform.

**Certification Rule**  
Every system must have a unique, immutable `code` that serves as its sovereign identifier across all lifecycle stages.

---

### 3.2 AM_BASELINE (At-Rest Definition)

```sql
CREATE TABLE am_baseline (
  id UUID PRIMARY KEY,
  system_id UUID NOT NULL REFERENCES system_product(id),
  am_version VARCHAR(32) NOT NULL,
  status VARCHAR(32) NOT NULL,
  document_ref TEXT NOT NULL,
  document_hash VARCHAR(64),
  metadata JSONB,
  created_at TIMESTAMP NOT NULL,
  
  CONSTRAINT unique_system_am_version UNIQUE (system_id, am_version),
  CONSTRAINT valid_am_status CHECK (status IN (
    'Draft', 'InReview', 'Approved', 'Retired', 'Superseded'
  ))
);

CREATE INDEX idx_am_baseline_system ON am_baseline(system_id);
CREATE INDEX idx_am_baseline_status ON am_baseline(status);
```

**Certification Rule**  
Approved AM baselines are **immutable**. Changes require a new version with complete traceability to the previous baseline.

**Meaning**  
The AM represents the static ontology: "what the system is" before it operates. It is the authoritative design definition.

---

### 3.3 DESIGN_VALIDATION (DV)

```sql
CREATE TABLE design_validation (
  id UUID PRIMARY KEY,
  am_id UUID NOT NULL REFERENCES am_baseline(id),
  dv_status VARCHAR(32) NOT NULL,
  dv_report_ref TEXT,
  dv_metrics JSONB,
  findings TEXT,
  validated_at TIMESTAMP NOT NULL,
  validated_by VARCHAR(128),
  approved_by VARCHAR(128),
  approval_date DATE,
  
  CONSTRAINT valid_dv_status CHECK (dv_status IN (
    'InProgress', 'Passed', 'ConditionallyPassed', 'Failed', 'Waived'
  ))
);

CREATE INDEX idx_dv_am ON design_validation(am_id);
CREATE INDEX idx_dv_status ON design_validation(dv_status);
CREATE INDEX idx_dv_validated_at ON design_validation(validated_at DESC);
```

**Role**  
Formal gate between *definition* (AM) and *prediction* (DPP).

**Certification Rule**  
No DPP may be generated without a passed DV. Failed or conditional DV must be resolved or waived with documented justification.

**Meaning**  
DV is the "ontological compiler" that validates design coherence, completeness, and certifiability before prediction.

---

### 3.4 DPP_RECORD (Predictive Identity)

```sql
CREATE TABLE dpp_record (
  id UUID PRIMARY KEY,
  dpp_uid VARCHAR(128) UNIQUE NOT NULL,
  system_id UUID NOT NULL REFERENCES system_product(id),
  am_id UUID REFERENCES am_baseline(id),
  dv_id UUID REFERENCES design_validation(id),
  status VARCHAR(32) NOT NULL,
  lifecycle_stage VARCHAR(32),
  primary_ata VARCHAR(16),
  related_ata_chapters TEXT[],
  dpp_payload JSONB NOT NULL,
  odd_conditions JSONB,
  certification_basis TEXT,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL,
  certified_at TIMESTAMP,
  certified_by VARCHAR(128),
  
  CONSTRAINT valid_dpp_status CHECK (status IN (
    'Draft', 'UnderReview', 'Certified', 'InService', 'Suspended', 'Retired'
  )),
  CONSTRAINT dpp_must_have_dv CHECK (
    status IN ('Draft', 'UnderReview') OR dv_id IS NOT NULL
  )
);

CREATE INDEX idx_dpp_system ON dpp_record(system_id);
CREATE INDEX idx_dpp_status ON dpp_record(status);
CREATE INDEX idx_dpp_ata ON dpp_record(primary_ata);
CREATE INDEX idx_dpp_payload ON dpp_record USING gin(dpp_payload);
CREATE INDEX idx_dpp_lifecycle ON dpp_record(lifecycle_stage);
```

**Key Concept**  
The **DPP predicts OM**, it does not validate itself. The DPP is a promise about future behavior.

**Certification Rule**  
Certified DPPs are **immutable**. Updates require retirement and creation of a new DPP version with full traceability.

**Meaning**  
The DPP is the predictive ontology: it declares what the system *will be* when operating, establishing the expected behavior envelope.

---

### 3.5 OM_EVENT (Ontological Mission Instance)

```sql
CREATE TABLE om_event (
  id UUID PRIMARY KEY,
  system_id UUID NOT NULL REFERENCES system_product(id),
  dpp_id UUID REFERENCES dpp_record(id),
  mission_id VARCHAR(64),
  mission_type VARCHAR(64),
  context JSONB,
  metrics JSONB,
  anomalies JSONB,
  started_at TIMESTAMP NOT NULL,
  ended_at TIMESTAMP,
  duration_seconds INTEGER,
  created_at TIMESTAMP NOT NULL,
  
  CONSTRAINT valid_duration CHECK (
    duration_seconds IS NULL OR duration_seconds >= 0
  )
);

CREATE INDEX idx_om_system ON om_event(system_id);
CREATE INDEX idx_om_dpp ON om_event(dpp_id);
CREATE INDEX idx_om_mission ON om_event(mission_id);
CREATE INDEX idx_om_started_at ON om_event(started_at DESC);
CREATE INDEX idx_om_metrics ON om_event USING gin(metrics);
```

**Rule**  
OM is **truth manifestation**, never overwritten. Each OM_EVENT is an immutable record of reality.

**Meaning**  
OM is the enacted ontology: "what the system actually was" during a specific operational context. It is empirical truth.

**Certification Significance**  
OM events are the primary evidence for validation. They cannot be deleted or modified once recorded (append-only).

---

### 3.6 OAV_CAMPAIGN (On-Aircraft Validation)

```sql
CREATE TABLE oav_campaign (
  id UUID PRIMARY KEY,
  dpp_id UUID NOT NULL REFERENCES dpp_record(id),
  name VARCHAR(256) NOT NULL,
  validation_scope TEXT,
  objectives TEXT,
  acceptance_criteria JSONB,
  result JSONB,
  findings TEXT,
  recommendation TEXT,
  status VARCHAR(32) NOT NULL,
  planned_start_date DATE,
  actual_start_date DATE,
  planned_end_date DATE,
  closed_at TIMESTAMP,
  created_at TIMESTAMP NOT NULL,
  lead_engineer VARCHAR(128),
  
  CONSTRAINT valid_oav_status CHECK (status IN (
    'Planned', 'Running', 'Paused', 'Completed', 'Closed', 'Cancelled'
  ))
);

CREATE INDEX idx_oav_dpp ON oav_campaign(dpp_id);
CREATE INDEX idx_oav_status ON oav_campaign(status);
CREATE INDEX idx_oav_created_at ON oav_campaign(created_at DESC);
```

#### OM ↔ OAV Link

```sql
CREATE TABLE oav_event_link (
  oav_id UUID NOT NULL REFERENCES oav_campaign(id) ON DELETE CASCADE,
  om_event_id UUID NOT NULL REFERENCES om_event(id) ON DELETE CASCADE,
  relevance_score NUMERIC(3, 2),
  notes TEXT,
  added_at TIMESTAMP NOT NULL,
  
  PRIMARY KEY (oav_id, om_event_id),
  
  CONSTRAINT valid_relevance CHECK (
    relevance_score IS NULL OR (relevance_score >= 0.00 AND relevance_score <= 1.00)
  )
);

CREATE INDEX idx_oav_link_oav ON oav_event_link(oav_id);
CREATE INDEX idx_oav_link_event ON oav_event_link(om_event_id);
```

**Meaning**  
OAV is the validation layer that compares DPP predictions against OM reality. It answers: "Did the system behave as predicted?"

**Certification Rule**  
OAV campaigns must document acceptance criteria *before* data collection begins. Post-hoc criteria changes invalidate the campaign.

---

### 3.7 DT_SNAPSHOT (Ontogenetic Digital Twin)

```sql
CREATE TABLE dt_snapshot (
  id UUID PRIMARY KEY,
  system_id UUID NOT NULL REFERENCES system_product(id),
  dpp_id UUID REFERENCES dpp_record(id),
  source_oav_id UUID REFERENCES oav_campaign(id),
  dt_version VARCHAR(64),
  dt_state JSONB NOT NULL,
  performance_metrics JSONB,
  health_indicators JSONB,
  accumulated_hours NUMERIC(10, 2),
  accumulated_cycles INTEGER,
  confidence_level NUMERIC(3, 2),
  notes TEXT,
  created_at TIMESTAMP NOT NULL,
  created_by VARCHAR(128),
  
  CONSTRAINT valid_confidence CHECK (
    confidence_level IS NULL OR (confidence_level >= 0.00 AND confidence_level <= 1.00)
  )
);

CREATE INDEX idx_dt_system ON dt_snapshot(system_id);
CREATE INDEX idx_dt_dpp ON dt_snapshot(dpp_id);
CREATE INDEX idx_dt_oav ON dt_snapshot(source_oav_id);
CREATE INDEX idx_dt_created_at ON dt_snapshot(created_at DESC);
CREATE INDEX idx_dt_confidence ON dt_snapshot(confidence_level DESC);
```

**Meaning**  
DT is **accumulated verified truth**, not simulation. It is the synthesis of design (AM/DPP) and validated operation (OM/OAV).

**Certification Rule**  
DT snapshots must reference their source OAV campaign. Unsourced or speculative twin states are not certification evidence.

**Key Insight**  
The DT is ontogenetic: it accumulates the system's operational history, learning what the system *has been*, not just what it was designed to be.

---

## 4. Neo4j Graph Model (Traceability Layer)

### 4.1 Node Types

| Node     | Meaning                 | Properties                    |
| -------- | ----------------------- | ----------------------------- |
| `System` | Ontological subject     | code, name, type, primary_ata |
| `AM`     | Design definition       | version, status, document_ref |
| `DV`     | Design validation       | dv_status, validated_at       |
| `DPP`    | Predictive passport     | dpp_uid, status, lifecycle    |
| `OM`     | Mission realization     | mission_id, started_at        |
| `OAV`    | Validation evidence     | name, status, result          |
| `DT`     | Verified digital twin   | dt_version, confidence_level  |

---

### 4.2 Relationships (The Ontological Loop)

```cypher
// Primary CCert/CVal loop
(System)-[:HAS_AM]->(AM)
(AM)-[:VALIDATED_BY]->(DV)
(DV)-[:GENERATES]->(DPP)
(DPP)-[:PREDICTS]->(OM)
(OM)-[:VALIDATED_IN]->(OAV)
(OAV)-[:FEEDS]->(DT)
(DT)-[:UPDATES]->(AM)

// Supporting relationships
(System)-[:HAS_DPP]->(DPP)
(System)-[:HAS_DT]->(DT)
(DPP)-[:BASED_ON]->(AM)
(OM)-[:OPERATES]->(System)
(DT)-[:SYNTHESIZES]->(OM)
```

**Semantic Meaning**

* `PREDICTS`: Forward-looking relationship (design to operation)
* `VALIDATED_IN`: Backward-looking relationship (operation to validation)
* `FEEDS`: Knowledge transfer (validation to twin)
* `UPDATES`: Loop closure (twin to next design)

---

### 4.3 Example Queries

#### Query 1: Impact Analysis

> *Which certified systems are invalidated if a DV rule changes?*

```cypher
MATCH (dv:DV)<-[:VALIDATED_BY]-(am:AM)<-[:HAS_AM]-(s:System)
WHERE dv.dv_status <> 'Passed'
RETURN s.code AS system_code, 
       am.version AS am_version,
       dv.dv_status AS validation_status
ORDER BY s.code
```

#### Query 2: Traceability Path

> *Show complete lifecycle for a specific DPP*

```cypher
MATCH path = (s:System)-[:HAS_AM]->(am:AM)
             -[:VALIDATED_BY]->(dv:DV)
             -[:GENERATES]->(dpp:DPP)
             -[:PREDICTS]->(om:OM)
             -[:VALIDATED_IN]->(oav:OAV)
             -[:FEEDS]->(dt:DT)
WHERE dpp.dpp_uid = 'DPP_95-20-27_FC_PitchStability_v1.2'
RETURN path
```

#### Query 3: Dependency Analysis

> *Find all systems dependent on a specific AM baseline*

```cypher
MATCH (am:AM {version: 'v2.1'})<-[:HAS_AM]-(s:System)
OPTIONAL MATCH (s)-[:HAS_DPP]->(dpp:DPP)
WHERE dpp.status IN ['Certified', 'InService']
RETURN s.code, 
       count(dpp) AS active_dpps,
       collect(dpp.dpp_uid) AS dpp_list
```

---

## 5. Data Governance Rules

| Area          | Rule                                                 | Rationale                             |
| ------------- | ---------------------------------------------------- | ------------------------------------- |
| Certification | No UPDATE on certified DPP                           | Immutability ensures audit trail      |
| Validation    | OM/OAV append-only                                   | Operational truth cannot be rewritten |
| Traceability  | Every DPP must link to AM + DV                       | Prediction must be grounded in design |
| Audit         | All timestamps mandatory                             | Complete temporal traceability        |
| Security      | JSON payload signed externally                       | Non-repudiation of data               |
| Versioning    | AM/DPP/DT use semantic versioning                    | Clear evolution tracking              |
| Retention     | Retired entities never deleted, marked as Superseded | Historical record preservation        |

---

## 6. Alignment with ATA 95 Buckets

| Bucket           | DB Role                          | Example                         |
| ---------------- | -------------------------------- | ------------------------------- |
| 95-20 Subsystems | `system_product` type=subsystem  | FC_PitchStab_NN, ECS_TempCtrl   |
| 95-30 Anchors    | Graph relationships              | Cross-ATA dependencies          |
| 95-40 Software   | `dpp_payload.sbom`               | Software bill of materials      |
| 95-50 Structures | Hardware references in metadata  | Structural component IDs        |
| 95-60 Storages   | OM data stores (time-series)     | Telemetry, logs                 |
| 95-90 Tables     | This schema definition           | The meta-schema                 |

---

## 7. Key Epistemological Insight

> **This database does not store data.  
> It stores epistemological states of truth.**

The schema captures:

1. **Design** (AM) → What we *define* the system to be
2. **Prediction** (DPP) → What we *expect* it will be
3. **Reality** (OM) → What it *actually was*
4. **Verification** (OAV) → Whether reality matched expectation
5. **Knowledge** (DT) → What we *know* from accumulated truth
6. **Redesign** (AM′) → Updated definition informed by knowledge

That is **CCert / CVal implemented as data**.

---

## 8. Implementation Triggers and Automation

### 8.1 Timestamp Triggers

```sql
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_system_product_updated_at 
  BEFORE UPDATE ON system_product
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_dpp_record_updated_at 
  BEFORE UPDATE ON dpp_record
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### 8.2 Certification State Enforcement

```sql
CREATE OR REPLACE FUNCTION enforce_dpp_immutability()
RETURNS TRIGGER AS $$
BEGIN
  IF OLD.status = 'Certified' AND NEW.status <> OLD.status THEN
    RAISE EXCEPTION 'Cannot modify status of certified DPP. Create new version instead.';
  END IF;
  IF OLD.status = 'Certified' AND NEW.dpp_payload <> OLD.dpp_payload THEN
    RAISE EXCEPTION 'Cannot modify payload of certified DPP. Create new version instead.';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER enforce_dpp_immutability_trigger
  BEFORE UPDATE ON dpp_record
  FOR EACH ROW EXECUTE FUNCTION enforce_dpp_immutability();
```

---

## 9. Cross-References

### 9.1 Related Documents

* [95-90-01-005 — CCert/CVal Glossary](../95-90-01_Global_Reference_Taxonomies/95-90-01-005_CCert_CVal_Glossary.md) — Terminology definitions
* [95-90-02-007 — CCert/CVal Core Data Model](./95-90-02-007_CCert_CVal_Core_Data_Model.md) — Logical entity definitions
* [95-00-03 — Requirements](../../95-00_GENERAL/95-00-03_Requirements/) — Traceability to requirements
* [95-00-07 — V&V](../../95-00_GENERAL/95-00-07_V_AND_V/) — Verification and validation framework

### 9.2 Standards References

* **DO-178C** (Software Considerations): [RTCA DO-178C](https://www.rtca.org/)
* **DO-254** (Hardware Design Assurance): [RTCA DO-254](https://www.rtca.org/)
* **CS-25** (Large Aeroplanes): [EASA CS-25](https://www.easa.europa.eu/)
* **ED-324** (AI Learning Assurance): EUROCAE ED-324

---

## 10. Next Logical Documents

Future extensions to this schema foundation:

* **95-90-02-008_CCert_CVal_Query_Patterns.md**
  * Standard query patterns for certification evidence
  * Performance optimization strategies
  * Example reports and dashboards

* **95-90-02-009_CCert_CVal_Data_Governance_and_Retention.md**
  * Data retention policies
  * Archival strategies
  * Compliance with regulations (GDPR, etc.)

* **95-90-02-010_CCert_CVal_API_and_Event_Model.md**
  * RESTful API specification
  * Event sourcing patterns
  * Real-time data streaming

---

## 11. Version History

| Version | Date       | Author                              | Changes                                         |
| ------- | ---------- | ----------------------------------- | ----------------------------------------------- |
| 1.0     | 2025-12-13 | AMPEL360 ATA 95 Data Architecture   | Initial formal baseline specification           |

---

## 12. Document Control

- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by [Approver]
- **Status**: WORKING – Subject to formal review and DBA approval
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **Sub-bucket**: 02_Global_Data_Schemas
- **Document ID**: 95-90-02-006
- **Last AI update**: 2025-12-13
- **Target DBMS**: PostgreSQL 14+, Neo4j 5.x
- **Certification Grade**: Yes
- **Baseline Candidate**: Yes

---

## 13. Final Note

This is not infrastructure.  
**This is epistemological architecture.**

The difference:

* Infrastructure stores *what happened*.
* Epistemology stores *how we know what happened*.

The CCert/CVal database is the latter.

It is the **canonical record of certification as a continuous process of knowing**, not a one-time event of approving.

---

**End of Document**
