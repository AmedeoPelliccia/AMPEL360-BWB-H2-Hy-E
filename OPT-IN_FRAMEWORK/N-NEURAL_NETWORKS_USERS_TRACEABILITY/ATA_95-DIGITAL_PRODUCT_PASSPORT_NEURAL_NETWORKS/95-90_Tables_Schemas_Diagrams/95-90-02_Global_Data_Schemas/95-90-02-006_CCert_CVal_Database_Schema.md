# 95-90-02-006 — CCert/CVal Database Schema

## 1. Purpose

This document defines the **central database schema** for the AMPEL360 CCert/CVal framework. It formalizes the ontological lifecycle concepts (AM, DV, DPP, OM, OAV, DT) into concrete data models supporting both **relational (PostgreSQL)** and **graph (Neo4j)** implementations.

The schema serves as the backbone for tracking the continuous certification loop: AM → DV → DPP → OM → OAV → DT → AM'.

## 2. Conceptual Model

### 2.1 Core Entities

From the [CCert/CVal Glossary](../95-90-01_Global_Reference_Taxonomies/95-90-01-005_CCert_CVal_Glossary.md), we derive these master entities:

| Entity | Purpose | Key Attributes |
|--------|---------|----------------|
| **SYSTEM_PRODUCT** | Generic "what I am" (Q100, WTCU, FCC, NN model, dataset) | id, code, name, type, primary_ata |
| **AM_BASELINE** | At-rest model/manual version | id, system_id, version, status, document_ref |
| **DESIGN_VALIDATION** | Design validation evidence for AM version | id, am_id, status, report_ref, metrics |
| **DPP_RECORD** | Sovereign identity + predictive ontology | id, dpp_id, system_id, am_id, dv_id, dpp_json |
| **OM_EVENT** | Real operational mission instances | id, system_id, dpp_id, flight_id, om_data |
| **OAV_CAMPAIGN** | On-aircraft validation campaign grouping | id, dpp_id, name, status, objectives, result |
| **DT_SNAPSHOT** | Digital twin state at a point in time | id, system_id, dpp_id, oav_id, dt_state |
| **GLOSSARY_ENTRY** | Terms, acronyms, taxonomies | id, term, full_name, category, description |
| **ENTITY_LINK** | Explicit relationships between entities | id, from_type, from_id, to_type, to_id, relation_type |

### 2.2 Ontological Loop Encoding

The schema encodes the complete CCert/CVal loop:

```
system_product → am_baseline → design_validation → dpp_record → 
om_event → oav_campaign → dt_snapshot → (feedback to next am_baseline')
```

---

## 3. Relational Model (PostgreSQL)

### 3.1 Core Tables

#### 3.1.1 system_product

The foundational entity representing any system, component, model, or dataset.

```sql
CREATE TABLE system_product (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code VARCHAR(64) UNIQUE NOT NULL,   -- Q100, WTCU01, FCC01, FC_PitchStab_NN
  name VARCHAR(256) NOT NULL,
  type VARCHAR(64) NOT NULL,          -- aircraft, lru, nn_model, dataset, subsystem
  primary_ata VARCHAR(16),            -- 95-20-27, 27, etc.
  description TEXT,
  parent_system_id UUID REFERENCES system_product(id),
  metadata JSONB,                     -- flexible additional data
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by VARCHAR(128),
  
  CONSTRAINT valid_type CHECK (type IN (
    'aircraft', 'lru', 'nn_model', 'dataset', 'subsystem', 
    'component', 'software', 'hardware', 'document'
  ))
);

CREATE INDEX idx_system_product_code ON system_product(code);
CREATE INDEX idx_system_product_type ON system_product(type);
CREATE INDEX idx_system_product_ata ON system_product(primary_ata);
```

**Purpose**: Central registry of all identifiable products and systems in AMPEL360.

---

#### 3.1.2 am_baseline

Static design baseline / Aircraft Manual version.

```sql
CREATE TABLE am_baseline (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  system_id UUID NOT NULL REFERENCES system_product(id) ON DELETE CASCADE,
  version VARCHAR(32) NOT NULL,       -- v1.0, v2.1-alpha, etc.
  status VARCHAR(32) NOT NULL,        -- Draft, Approved, InReview, Retired
  document_ref TEXT,                  -- repo path, URL, S1000D DMRef
  document_hash VARCHAR(64),          -- SHA256 or similar for integrity
  baseline_date DATE,
  metadata JSONB,                     -- architecture, interfaces, limits
  notes TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by VARCHAR(128),
  
  CONSTRAINT unique_system_version UNIQUE (system_id, version),
  CONSTRAINT valid_am_status CHECK (status IN (
    'Draft', 'InReview', 'Approved', 'Retired', 'Deprecated'
  ))
);

CREATE INDEX idx_am_baseline_system ON am_baseline(system_id);
CREATE INDEX idx_am_baseline_status ON am_baseline(status);
```

**Purpose**: Version control for static design definitions (the "at-rest" state).

---

#### 3.1.3 design_validation

Evidence that AM baseline has passed design validation.

```sql
CREATE TABLE design_validation (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  am_id UUID NOT NULL REFERENCES am_baseline(id) ON DELETE CASCADE,
  dv_status VARCHAR(32) NOT NULL,     -- Passed, ConditionallyPassed, Failed, InProgress
  dv_report_ref TEXT,                 -- path to DV report/evidence
  dv_metrics JSONB,                   -- {coverage: 98, completeness: 100, checks_passed: 245}
  findings TEXT,                      -- open issues, observations
  performed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  performed_by VARCHAR(128),
  approved_by VARCHAR(128),
  approval_date DATE,
  
  CONSTRAINT valid_dv_status CHECK (dv_status IN (
    'InProgress', 'Passed', 'ConditionallyPassed', 'Failed', 'Waived'
  ))
);

CREATE INDEX idx_dv_am ON design_validation(am_id);
CREATE INDEX idx_dv_status ON design_validation(dv_status);
```

**Purpose**: Track validation of design coherence, completeness, and certifiability.

---

#### 3.1.4 dpp_record

The Digital Product Passport - sovereign identity and predictive ontology.

```sql
CREATE TABLE dpp_record (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  dpp_id VARCHAR(128) UNIQUE NOT NULL, -- DPP_95-20_FC_PitchStability_v1.2
  system_id UUID NOT NULL REFERENCES system_product(id),
  am_id UUID REFERENCES am_baseline(id),
  dv_id UUID REFERENCES design_validation(id),
  primary_ata VARCHAR(16),
  related_ata_chapters TEXT[],        -- ARRAY['27', '31', '70']
  status VARCHAR(32) NOT NULL,        -- Draft, Certified, InService, Retired
  lifecycle_stage VARCHAR(32),        -- Design, Testing, InService, Deprecated
  dpp_json JSONB NOT NULL,            -- complete DPP envelope + payload
  odd_conditions JSONB,               -- Operational Design Domain constraints
  sbom JSONB,                         -- Software Bill of Materials
  capabilities TEXT[],                -- declared capabilities
  limitations TEXT[],                 -- known limitations
  certification_basis TEXT,           -- CS-25, DO-178C DAL B, etc.
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by VARCHAR(128),
  approved_by VARCHAR(128),
  approval_date DATE,
  
  CONSTRAINT valid_dpp_status CHECK (status IN (
    'Draft', 'UnderReview', 'Certified', 'InService', 'Suspended', 'Retired'
  ))
);

CREATE INDEX idx_dpp_system ON dpp_record(system_id);
CREATE INDEX idx_dpp_status ON dpp_record(status);
CREATE INDEX idx_dpp_ata ON dpp_record(primary_ata);
CREATE INDEX idx_dpp_json ON dpp_record USING gin(dpp_json);
```

**Purpose**: Authoritative digital identity declaring expected behavior and operational limits.

---

#### 3.1.5 om_event

Operational Mission events - real-world system behavior.

```sql
CREATE TABLE om_event (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  system_id UUID NOT NULL REFERENCES system_product(id),
  dpp_id UUID REFERENCES dpp_record(id),
  context_id UUID,                    -- FK to operational_context if needed
  flight_id VARCHAR(64),              -- tail number + flight, or campaign ID
  mission_type VARCHAR(64),           -- test_flight, revenue_service, validation
  timestamp_start TIMESTAMP NOT NULL,
  timestamp_end TIMESTAMP,
  duration_seconds INTEGER,
  om_data JSONB,                      -- metrics, logs summary, KPIs
  anomalies JSONB,                    -- detected deviations
  environment JSONB,                  -- weather, altitude, config
  notes TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  
  CONSTRAINT valid_duration CHECK (
    duration_seconds IS NULL OR duration_seconds >= 0
  )
);

CREATE INDEX idx_om_system ON om_event(system_id);
CREATE INDEX idx_om_dpp ON om_event(dpp_id);
CREATE INDEX idx_om_flight ON om_event(flight_id);
CREATE INDEX idx_om_timestamps ON om_event(timestamp_start, timestamp_end);
CREATE INDEX idx_om_data ON om_event USING gin(om_data);
```

**Purpose**: Capture enacted ontology - what the system actually does in operation.

---

#### 3.1.6 oav_campaign

On-Aircraft Validation campaigns comparing OM reality to DPP predictions.

```sql
CREATE TABLE oav_campaign (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  dpp_id UUID NOT NULL REFERENCES dpp_record(id),
  name VARCHAR(256) NOT NULL,
  status VARCHAR(32) NOT NULL,        -- Planned, Running, Completed, Closed
  objectives TEXT,
  criteria JSONB,                     -- what constitutes "validated"
  result JSONB,                       -- {passed: true, findings: [...], metrics: {...}}
  findings TEXT,                      -- detailed observations
  recommendation TEXT,                -- actions, updates needed
  planned_start_date DATE,
  actual_start_date DATE,
  planned_end_date DATE,
  completed_at TIMESTAMP,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by VARCHAR(128),
  lead_engineer VARCHAR(128),
  
  CONSTRAINT valid_oav_status CHECK (status IN (
    'Planned', 'Running', 'Paused', 'Completed', 'Closed', 'Cancelled'
  ))
);

CREATE INDEX idx_oav_dpp ON oav_campaign(dpp_id);
CREATE INDEX idx_oav_status ON oav_campaign(status);
```

**Purpose**: Organize validation activities that verify DPP predictions against operational reality.

---

#### 3.1.7 oav_event_link

Links OM events to OAV campaigns (many-to-many).

```sql
CREATE TABLE oav_event_link (
  oav_id UUID NOT NULL REFERENCES oav_campaign(id) ON DELETE CASCADE,
  om_event_id UUID NOT NULL REFERENCES om_event(id) ON DELETE CASCADE,
  relevance_score NUMERIC(3, 2),      -- 0.00 to 1.00
  notes TEXT,
  added_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  
  PRIMARY KEY (oav_id, om_event_id)
);

CREATE INDEX idx_oav_link_oav ON oav_event_link(oav_id);
CREATE INDEX idx_oav_link_event ON oav_event_link(om_event_id);
```

**Purpose**: Associate operational events with validation campaigns.

---

#### 3.1.8 dt_snapshot

Digital Twin state snapshots accumulated from OM + OAV.

```sql
CREATE TABLE dt_snapshot (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  system_id UUID NOT NULL REFERENCES system_product(id),
  dpp_id UUID REFERENCES dpp_record(id),
  source_oav_id UUID REFERENCES oav_campaign(id),
  version_tag VARCHAR(64),            -- DT_v1.3, snapshot_20250115
  dt_state JSONB NOT NULL,            -- condensed twin state
  performance_metrics JSONB,          -- aggregated performance data
  health_indicators JSONB,            -- system health state
  predictive_models JSONB,            -- trained models, coefficients
  accumulated_hours NUMERIC(10, 2),   -- operational time
  accumulated_cycles INTEGER,         -- operational cycles
  confidence_level NUMERIC(3, 2),     -- 0.00 to 1.00
  notes TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by VARCHAR(128)
);

CREATE INDEX idx_dt_system ON dt_snapshot(system_id);
CREATE INDEX idx_dt_dpp ON dt_snapshot(dpp_id);
CREATE INDEX idx_dt_oav ON dt_snapshot(source_oav_id);
CREATE INDEX idx_dt_created ON dt_snapshot(created_at DESC);
```

**Purpose**: Ontogenetic accumulation - living synthesis of design + validated operation.

---

#### 3.1.9 glossary_entry

Terms, acronyms, and taxonomy definitions.

```sql
CREATE TABLE glossary_entry (
  id SERIAL PRIMARY KEY,
  term VARCHAR(64) UNIQUE NOT NULL,
  full_name VARCHAR(256),
  category VARCHAR(64),               -- acronym, concept, process, standard, ata_chapter
  description TEXT,
  layer_domain VARCHAR(64),           -- Design, Operation, Validation, etc.
  language VARCHAR(8) DEFAULT 'en',
  related_terms TEXT[],               -- cross-references
  source_document TEXT,               -- reference to defining document
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_glossary_term ON glossary_entry(term);
CREATE INDEX idx_glossary_category ON glossary_entry(category);
```

**Purpose**: Central glossary aligned with [95-90-01-005_CCert_CVal_Glossary.md](../95-90-01_Global_Reference_Taxonomies/95-90-01-005_CCert_CVal_Glossary.md).

---

#### 3.1.10 entity_link

Generic relationship tracking between any entities.

```sql
CREATE TABLE entity_link (
  id SERIAL PRIMARY KEY,
  from_type VARCHAR(32) NOT NULL,     -- am_baseline, dpp_record, om_event, etc.
  from_id UUID NOT NULL,
  to_type VARCHAR(32) NOT NULL,
  to_id UUID NOT NULL,
  relation_type VARCHAR(64) NOT NULL, -- predicts, validated_by, derived_to, updates, etc.
  metadata JSONB,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_by VARCHAR(128),
  
  CONSTRAINT valid_entity_types CHECK (
    from_type IN ('system_product', 'am_baseline', 'design_validation', 'dpp_record', 
                  'om_event', 'oav_campaign', 'dt_snapshot') AND
    to_type IN ('system_product', 'am_baseline', 'design_validation', 'dpp_record', 
                'om_event', 'oav_campaign', 'dt_snapshot')
  )
);

CREATE INDEX idx_entity_link_from ON entity_link(from_type, from_id);
CREATE INDEX idx_entity_link_to ON entity_link(to_type, to_id);
CREATE INDEX idx_entity_link_relation ON entity_link(relation_type);
```

**Purpose**: Flexible graph-like relationships within the relational model.

---

### 3.2 Initialization Script

```sql
-- Initialize glossary from CCert/CVal glossary document
INSERT INTO glossary_entry (term, full_name, category, description, layer_domain) VALUES
  ('AM', 'Aircraft Manual / At-Rest Model', 'acronym', 'Static ontology describing system at rest', 'Design'),
  ('DV', 'Design Validation', 'acronym', 'Validates AM and enables DPP creation', 'Design Validation'),
  ('DPP', 'Digital Product Passport', 'acronym', 'Predictive ontology with sovereign identity', 'Identity + Prediction'),
  ('OM', 'Ontological Mission', 'acronym', 'Enacted ontology - real operational behavior', 'Operation'),
  ('OAV', 'On-Aircraft Validation', 'acronym', 'Empirical truth validation against DPP', 'On-Aircraft Validation'),
  ('DT', 'Digital Twin (Ontogenetic)', 'acronym', 'Living synthesis of design + operation', 'Digital Twin'),
  ('CCert', 'Continuous Certification', 'acronym', 'Continuous loop keeping system certifiable', 'Certification Loop'),
  ('CVal', 'Continuous Validation', 'acronym', 'Continuous validation from operational evidence', 'Validation Loop'),
  ('ATA 95', 'Digital Product Passport & Neural Networks', 'ata_chapter', 'ATA chapter for DPP, NN, and AI systems', 'ATA Chapter'),
  ('UTCS', 'Universal Traceability & Circularity Standard', 'acronym', 'Backbone for traceability and circularity', 'Traceability');
```

---

## 4. Graph Model (Neo4j)

### 4.1 Node Labels

```cypher
// Core entity nodes
(:System {id, code, name, type, primary_ata})
(:AM {id, version, status, document_ref})
(:DV {id, dv_status, performed_at})
(:DPP {id, dpp_id, status, lifecycle_stage})
(:OMEvent {id, flight_id, timestamp_start, mission_type})
(:OAV {id, name, status, objectives})
(:DTSnapshot {id, version_tag, confidence_level})
(:GlossaryTerm {term, full_name, category})
```

### 4.2 Relationship Types

The ontological loop is encoded in relationships:

```cypher
// Primary CCert/CVal loop relationships
(System)-[:HAS_AM]->(AM)
(AM)-[:VALIDATED_BY]->(DV)
(DV)-[:GENERATES]->(DPP)
(DPP)-[:PREDICTS]->(OMEvent)              // type-level prediction
(OMEvent)-[:INCLUDED_IN]->(OAV)
(OAV)-[:VALIDATES]->(DPP)
(OAV)-[:FEEDS]->(DTSnapshot)
(DTSnapshot)-[:UPDATES]->(AM)              // feedback loop to next AM version

// Supporting relationships
(System)-[:HAS_DPP]->(DPP)
(System)-[:HAS_DT]->(DTSnapshot)
(DPP)-[:BASED_ON]->(AM)
(DPP)-[:VALIDATED_BY]->(DV)
(OMEvent)-[:OPERATES]->(System)
(DTSnapshot)-[:SYNTHESIZES]->(OMEvent)     // many events contribute
```

### 4.3 Example Queries

#### 4.3.1 Trace complete lifecycle for a system

```cypher
MATCH path = (s:System {code: 'FC_PitchStab_NN'})-[:HAS_AM]->(am:AM)
             -[:VALIDATED_BY]->(dv:DV)
             -[:GENERATES]->(dpp:DPP)
             -[:PREDICTS]->(om:OMEvent)
             -[:INCLUDED_IN]->(oav:OAV)
             -[:FEEDS]->(dt:DTSnapshot)
RETURN path
```

#### 4.3.2 Find all DPPs validated by recent OAV campaigns

```cypher
MATCH (oav:OAV)-[:VALIDATES]->(dpp:DPP)
WHERE oav.status = 'Completed' 
  AND oav.completed_at > datetime() - duration({days: 90})
RETURN dpp.dpp_id, oav.name, oav.result
```

#### 4.3.3 Identify systems needing AM updates from DT feedback

```cypher
MATCH (dt:DTSnapshot)-[:UPDATES]->(am:AM)<-[:HAS_AM]-(s:System)
WHERE dt.confidence_level > 0.90
  AND am.status = 'Approved'
  AND NOT EXISTS((am)-[:SUPERSEDED_BY]->(:AM))
RETURN s.code, am.version, dt.version_tag, dt.created_at
ORDER BY dt.created_at DESC
```

---

## 5. Entity-Relationship Diagram

```
┌──────────────────┐
│ SYSTEM_PRODUCT   │
│ (Q100, FCC, NN)  │
└────────┬─────────┘
         │
         │ 1:N
         ↓
┌──────────────────┐      ┌──────────────────┐
│  AM_BASELINE     │──1:N→│ DESIGN_VALIDATION│
│  (static design) │←─────│  (DV evidence)   │
└────────┬─────────┘      └──────────────────┘
         │                          │
         │ 1:N                      │ 1:N
         ↓                          ↓
┌──────────────────────────────────────────┐
│           DPP_RECORD                      │
│  (sovereign identity + prediction)        │
└────────┬─────────────────────────────────┘
         │
         │ 1:N
         ↓
┌──────────────────┐      ┌──────────────────┐
│    OM_EVENT      │──N:M→│  OAV_CAMPAIGN    │
│ (real operation) │←─────│   (validation)   │
└──────────────────┘      └────────┬─────────┘
         │                         │
         │ N:1                     │ 1:N
         ↓                         ↓
┌──────────────────────────────────────────┐
│         DT_SNAPSHOT                       │
│  (ontogenetic accumulation)               │
│  ───────────────────────────────────────→ │
│  (feeds back to next AM_BASELINE')        │
└───────────────────────────────────────────┘

Supporting entities:
- GLOSSARY_ENTRY (terms/acronyms)
- ENTITY_LINK (flexible relationships)
```

---

## 6. Concrete Example: Flight Control Pitch Stability NN

### 6.1 System Product

```sql
INSERT INTO system_product (code, name, type, primary_ata) VALUES
  ('FC_PitchStab_NN', 'Flight Control Pitch Stability Neural Network', 'nn_model', '95-20-27');
```

### 6.2 AM Baseline

```sql
INSERT INTO am_baseline (system_id, version, status, document_ref) VALUES
  (
    (SELECT id FROM system_product WHERE code = 'FC_PitchStab_NN'),
    'v1.0',
    'Approved',
    'OPT-IN_FRAMEWORK/.../95-20-27-...AM_v1.0.md'
  );
```

### 6.3 Design Validation

```sql
INSERT INTO design_validation (am_id, dv_status, dv_metrics, performed_by) VALUES
  (
    (SELECT id FROM am_baseline WHERE version = 'v1.0' LIMIT 1),
    'Passed',
    '{"coverage": 98, "completeness": 100, "checks_passed": 245}'::jsonb,
    'DV Team Lead'
  );
```

### 6.4 DPP Record

```sql
INSERT INTO dpp_record (dpp_id, system_id, am_id, dv_id, primary_ata, status, dpp_json) VALUES
  (
    'DPP_95-20-27_FC_PitchStab_v1.0',
    (SELECT id FROM system_product WHERE code = 'FC_PitchStab_NN'),
    (SELECT id FROM am_baseline WHERE version = 'v1.0' LIMIT 1),
    (SELECT id FROM design_validation WHERE dv_status = 'Passed' LIMIT 1),
    '95-20-27',
    'Certified',
    '{
      "capabilities": ["pitch_rate_prediction", "stability_augmentation"],
      "odd": {"altitude_min_m": 0, "altitude_max_m": 15000, "speed_max_mach": 0.85},
      "model_type": "LSTM",
      "input_dim": 12,
      "output_dim": 3
    }'::jsonb
  );
```

### 6.5 OM Event (Test Flight)

```sql
INSERT INTO om_event (system_id, dpp_id, flight_id, mission_type, timestamp_start, timestamp_end, om_data) VALUES
  (
    (SELECT id FROM system_product WHERE code = 'FC_PitchStab_NN'),
    (SELECT id FROM dpp_record WHERE dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0'),
    'Q100-001-FLT-042',
    'test_flight',
    '2025-01-15 10:30:00',
    '2025-01-15 12:45:00',
    '{
      "avg_pitch_error_deg": 0.12,
      "max_pitch_error_deg": 0.45,
      "stability_margin": 0.92,
      "anomalies": []
    }'::jsonb
  );
```

### 6.6 OAV Campaign

```sql
INSERT INTO oav_campaign (dpp_id, name, status, objectives, result) VALUES
  (
    (SELECT id FROM dpp_record WHERE dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0'),
    'FC_PitchStab_Initial_Validation_Q1_2025',
    'Completed',
    'Validate pitch stability NN predictions against flight test data',
    '{
      "passed": true,
      "metrics": {"prediction_accuracy": 0.96, "false_positive_rate": 0.02},
      "findings": ["Excellent performance within ODD", "Minor degradation above 12000m"]
    }'::jsonb
  );

-- Link OM event to OAV campaign
INSERT INTO oav_event_link (oav_id, om_event_id, relevance_score) VALUES
  (
    (SELECT id FROM oav_campaign WHERE name = 'FC_PitchStab_Initial_Validation_Q1_2025'),
    (SELECT id FROM om_event WHERE flight_id = 'Q100-001-FLT-042'),
    0.95
  );
```

### 6.7 DT Snapshot

```sql
INSERT INTO dt_snapshot (system_id, dpp_id, source_oav_id, version_tag, dt_state, confidence_level) VALUES
  (
    (SELECT id FROM system_product WHERE code = 'FC_PitchStab_NN'),
    (SELECT id FROM dpp_record WHERE dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0'),
    (SELECT id FROM oav_campaign WHERE name = 'FC_PitchStab_Initial_Validation_Q1_2025'),
    'DT_v1.0_post_Q1_validation',
    '{
      "operational_envelope": {"altitude_validated_max_m": 14500},
      "performance_drift": 0.02,
      "recommended_recalibration_hours": 5000,
      "health_status": "nominal"
    }'::jsonb,
    0.94
  );
```

---

## 7. Query Examples

### 7.1 Find all DPPs for a system with their validation status

```sql
SELECT 
  sp.code AS system_code,
  dpp.dpp_id,
  dpp.status AS dpp_status,
  dv.dv_status,
  COUNT(DISTINCT om.id) AS om_events_count,
  COUNT(DISTINCT oav.id) AS oav_campaigns_count
FROM system_product sp
JOIN dpp_record dpp ON dpp.system_id = sp.id
LEFT JOIN design_validation dv ON dv.id = dpp.dv_id
LEFT JOIN om_event om ON om.dpp_id = dpp.id
LEFT JOIN oav_campaign oav ON oav.dpp_id = dpp.id
WHERE sp.code = 'FC_PitchStab_NN'
GROUP BY sp.code, dpp.dpp_id, dpp.status, dv.dv_status;
```

### 7.2 Trace the complete lifecycle for a DPP

```sql
WITH lifecycle AS (
  SELECT 
    'AM' AS stage, am.version AS identifier, am.status, am.created_at AS timestamp
  FROM am_baseline am
  WHERE am.id = (SELECT am_id FROM dpp_record WHERE dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0')
  
  UNION ALL
  
  SELECT 
    'DV' AS stage, dv.id::text AS identifier, dv.dv_status AS status, dv.performed_at AS timestamp
  FROM design_validation dv
  WHERE dv.id = (SELECT dv_id FROM dpp_record WHERE dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0')
  
  UNION ALL
  
  SELECT 
    'DPP' AS stage, dpp.dpp_id AS identifier, dpp.status, dpp.created_at AS timestamp
  FROM dpp_record dpp
  WHERE dpp.dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0'
  
  UNION ALL
  
  SELECT 
    'OM' AS stage, om.flight_id AS identifier, om.mission_type AS status, om.timestamp_start AS timestamp
  FROM om_event om
  WHERE om.dpp_id = (SELECT id FROM dpp_record WHERE dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0')
  
  UNION ALL
  
  SELECT 
    'OAV' AS stage, oav.name AS identifier, oav.status, oav.created_at AS timestamp
  FROM oav_campaign oav
  WHERE oav.dpp_id = (SELECT id FROM dpp_record WHERE dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0')
  
  UNION ALL
  
  SELECT 
    'DT' AS stage, dt.version_tag AS identifier, dt.confidence_level::text AS status, dt.created_at AS timestamp
  FROM dt_snapshot dt
  WHERE dt.dpp_id = (SELECT id FROM dpp_record WHERE dpp_id = 'DPP_95-20-27_FC_PitchStab_v1.0')
)
SELECT * FROM lifecycle ORDER BY timestamp;
```

### 7.3 Identify systems requiring AM updates based on DT feedback

```sql
SELECT 
  sp.code,
  am.version AS current_am_version,
  dt.version_tag AS dt_version,
  dt.confidence_level,
  dt.dt_state->>'recommended_recalibration_hours' AS recalibration_hours,
  dt.created_at AS dt_snapshot_date
FROM dt_snapshot dt
JOIN system_product sp ON dt.system_id = sp.id
JOIN am_baseline am ON am.system_id = sp.id
WHERE dt.confidence_level > 0.90
  AND am.status = 'Approved'
  AND dt.created_at > am.created_at
  AND dt.dt_state ? 'recommended_recalibration_hours'
ORDER BY dt.created_at DESC;
```

---

## 8. Implementation Guidelines

### 8.1 PostgreSQL Setup

1. **Install PostgreSQL 14+** with UUID and JSONB support
2. **Run schema creation scripts** in order:
   - Core tables (system_product → am_baseline → ... → entity_link)
   - Indexes
   - Glossary initialization
3. **Set up triggers** for `updated_at` timestamps:

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

4. **Configure backup and archival** for audit trail

### 8.2 Neo4j Setup

1. **Install Neo4j 5.x** with APOC and GDS plugins
2. **Create constraints** for uniqueness:

```cypher
CREATE CONSTRAINT system_code_unique IF NOT EXISTS
FOR (s:System) REQUIRE s.code IS UNIQUE;

CREATE CONSTRAINT dpp_id_unique IF NOT EXISTS
FOR (d:DPP) REQUIRE d.dpp_id IS UNIQUE;
```

3. **Import data from PostgreSQL** using Neo4j ETL or custom scripts
4. **Create indexes** for performance:

```cypher
CREATE INDEX system_type IF NOT EXISTS FOR (s:System) ON (s.type);
CREATE INDEX dpp_status IF NOT EXISTS FOR (d:DPP) ON (d.status);
CREATE INDEX om_flight IF NOT EXISTS FOR (o:OMEvent) ON (o.flight_id);
```

### 8.3 Synchronization Strategy

- **PostgreSQL as source of truth** for transactional data
- **Neo4j for analytics and graph queries** (read-optimized)
- **CDC (Change Data Capture)** or scheduled ETL to sync PostgreSQL → Neo4j
- **Event-driven updates** using message queue (e.g., Kafka, RabbitMQ)

---

## 9. Integration with ATA 95 Framework

This database schema directly supports:

- **[95-20 Subsystems](../../95-20_Subsystems/)** - Each subsystem NN has entries in system_product, DPP, etc.
- **[95-40 Software](../../95-40_Software/)** - Software lifecycle tracking via AM/DPP/DT
- **[95-90-01 Taxonomies](../95-90-01_Global_Reference_Taxonomies/)** - glossary_entry table
- **[95-90-04 Traceability](../95-90-04_Global_Traceability_Tables/)** - entity_link for UTCS compliance

---

## 10. Security and Compliance

### 10.1 Access Control

- **Row-Level Security (RLS)** in PostgreSQL for multi-tenant or role-based access
- **Audit logging** for all mutations (INSERT/UPDATE/DELETE)
- **Encryption at rest** for sensitive DPP payload data

### 10.2 Data Retention

- **Soft deletes** preferred over hard deletes (status = 'Retired')
- **Archival policy** for old AM versions and OM events (>5 years)
- **GDPR/Privacy compliance** for any personal data in om_event

### 10.3 Backup Strategy

- **Continuous archival** (PostgreSQL WAL archiving)
- **Point-in-time recovery** capability
- **Geo-redundant backups** for disaster recovery

---

## 11. Future Extensions

1. **Time-series optimization** - Consider TimescaleDB extension for om_event
2. **Vector search** - Add pgvector for NN embedding searches
3. **Blockchain integration** - Immutable DPP versions via distributed ledger
4. **ML model versioning** - Extend dt_snapshot with MLflow-style model registry
5. **Real-time streaming** - Kafka Connect for live OM event ingestion

---

## 12. Cross-References

### 12.1 Related Documents

- [95-90-01-005 — CCert/CVal Glossary](../95-90-01_Global_Reference_Taxonomies/95-90-01-005_CCert_CVal_Glossary.md) (terminology source)
- [95-90-04 — Global Traceability Tables](../95-90-04_Global_Traceability_Tables/) (UTCS implementation)
- [95-40 — Software Lifecycle](../../95-40_Software/) (software DPP tracking)
- [AM_Q100.json](../../../../../../examples/am_aircraft_model/AM_Q100.json) (example AM artifact)

### 12.2 Standards References

- **DO-178C** (Software): [RTCA DO-178C](https://www.rtca.org/content/standards-guidance-materials)
- **ED-324** (AI Trustworthiness): EUROCAE ED-324 (Learning Assurance)
- **ISO 19650** (BIM/Digital Twins): [ISO 19650 Series](https://www.iso.org/standard/68078.html)
- **ATA iSpec 2200**: [ATA Specifications](https://www.ata.org/resources/specifications)

---

## 13. Version History

| Version | Date       | Author         | Changes                                  |
|---------|------------|----------------|------------------------------------------|
| 1.0     | 2025-12-13 | GitHub Copilot | Initial database schema definition       |

---

## 14. Document Control

- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by [Approver]
- **Status**: DRAFT – Subject to human review and DBA approval
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **Sub-bucket**: 02_Global_Data_Schemas
- **Document ID**: 95-90-02-006
- **Last AI update**: 2025-12-13
- **Target DBMS**: PostgreSQL 14+, Neo4j 5.x

---

## 15. Notes

This schema is the **operational backbone** of the AMPEL360 CCert/CVal framework. It transforms the conceptual ontological loop (AM → DV → DPP → OM → OAV → DT → AM') into concrete, queryable data structures.

**Key principle**: The database IS the living embodiment of continuous certification—every insert, update, and query reflects the system's ontogenesis from design through operation to validated twin.

For implementation questions, contact the AMPEL360 Data Architecture Working Group or Database Administration team.

---

**End of Document**
