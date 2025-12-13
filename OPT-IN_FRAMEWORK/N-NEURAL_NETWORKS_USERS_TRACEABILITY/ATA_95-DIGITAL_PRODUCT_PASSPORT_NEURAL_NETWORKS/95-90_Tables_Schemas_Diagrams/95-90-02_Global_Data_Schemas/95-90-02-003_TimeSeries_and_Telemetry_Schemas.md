# 95-90-02-003 — TimeSeries and Telemetry Schemas

**Document ID**: 95-90-02-003  
**Version**: 1.0  
**Date**: 2025-12-13  
**Status**: WORKING  
**Owner**: AMPEL360 – ATA 95 Data Architecture  
**Applicability**: Global (All ATA Chapters)

---

## 1. Purpose

This document defines the **canonical schemas for time-series and telemetry data** used to support:

* Ontological Mission execution (**OM**)
* On-Aircraft Validation (**OAV**)
* Continuous Validation (**CVal**)
* Digital Twin ontogenetic construction (**DT**)

It ensures that **operational reality is captured in a certifiable, replayable, and analyzable form**, independent of system domain.

---

## 2. Design Principles

1. **Append-only truth**  
   Telemetry is never overwritten.

2. **Time as a first-class dimension**  
   All operational truth is time-indexed.

3. **Contextual integrity**  
   Telemetry is meaningless without mission context.

4. **Prediction comparability**  
   Data must be directly comparable with DPP predictions.

---

## 3. Core Concepts

### 3.1 Telemetry Stream

A **Telemetry Stream** is a logical grouping of homogeneous time-series signals emitted by a SystemProduct during OM.

**Examples:**
* Flight control loop signals
* Neural network inference metrics
* Energy flow measurements
* Structural strain gauges

**Characteristics:**
* Bound to a specific OM event
* Homogeneous sampling rate
* Consistent units and semantics
* Traceable to source (sensor, software, model)

---

### 3.2 TimeSeries Event

A **TimeSeries Event** is an immutable measurement at a precise time.

**Properties:**
* Timestamp (ISO-8601 with microsecond precision)
* Value (typed: numeric, boolean, categorical, or structured)
* Quality indicator
* Source attribution

---

## 4. Canonical Telemetry Schema (Logical)

```json
{
  "telemetry_id": "UUID",
  "system_id": "UUID",
  "dpp_id": "UUID",
  "om_event_id": "UUID",
  "stream_name": "string",
  "signal_name": "string",
  "timestamp": "ISO-8601",
  "value": "number | string | boolean | object",
  "unit": "string",
  "quality_flag": "OK | DEGRADED | INVALID",
  "source": "sensor | software | model | estimator"
}
```

### Field Definitions

| Field          | Type     | Description                                    | Mandatory |
|----------------|----------|------------------------------------------------|-----------|
| telemetry_id   | UUID     | Unique event identifier                        | Yes       |
| system_id      | UUID     | Reference to SystemProduct                     | Yes       |
| dpp_id         | UUID     | DPP making predictions about this telemetry    | Yes       |
| om_event_id    | UUID     | Mission context                                | Yes       |
| stream_name    | string   | Logical grouping (e.g., "FC_Pitch_Loop")      | Yes       |
| signal_name    | string   | Specific signal (e.g., "pitch_rate_actual")   | Yes       |
| timestamp      | ISO-8601 | Precise measurement time                       | Yes       |
| value          | variant  | Measured or computed value                     | Yes       |
| unit           | string   | Physical unit (SI preferred)                   | Yes       |
| quality_flag   | enum     | Data quality assessment                        | Yes       |
| source         | enum     | Origin of the measurement                      | Yes       |

---

## 5. Time-Series Storage Model (Physical)

### 5.1 PostgreSQL (Certification Store)

Used for:
* Aggregated metrics
* Events triggering certification actions
* Long-term archival with immutability guarantees

```sql
CREATE TABLE telemetry_event (
  id UUID PRIMARY KEY,
  system_id UUID NOT NULL REFERENCES system_product(id),
  dpp_id UUID REFERENCES dpp_record(id),
  om_event_id UUID NOT NULL REFERENCES om_event(id),
  stream_name VARCHAR(128) NOT NULL,
  signal_name VARCHAR(128) NOT NULL,
  ts TIMESTAMP NOT NULL,
  value JSONB NOT NULL,
  unit VARCHAR(32),
  quality_flag VARCHAR(16) NOT NULL,
  source VARCHAR(32) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  
  CONSTRAINT valid_quality_flag CHECK (
    quality_flag IN ('OK', 'DEGRADED', 'INVALID', 'ESTIMATED')
  ),
  CONSTRAINT valid_source CHECK (
    source IN ('sensor', 'software', 'model', 'estimator', 'derived')
  )
);

CREATE INDEX idx_telemetry_om_event ON telemetry_event(om_event_id);
CREATE INDEX idx_telemetry_stream ON telemetry_event(stream_name);
CREATE INDEX idx_telemetry_timestamp ON telemetry_event(ts);
CREATE INDEX idx_telemetry_system ON telemetry_event(system_id);
```

**Certification Rule:**  
Raw telemetry in PostgreSQL serves as the authoritative record for audit and certification evidence.

---

### 5.2 Time-Series Engine (Optional)

For high-frequency data (kHz–MHz), a dedicated TSDB may be used:

* **TimescaleDB** (PostgreSQL extension)
* **InfluxDB**
* **OpenTelemetry-compatible backend**

**Rule:**  
Certification decisions are always based on **derived evidence stored in PostgreSQL**. High-frequency TSDB is for operational monitoring and analysis only.

**Integration Pattern:**
```
Raw Sensors → TSDB (operational) → Aggregator → PostgreSQL (certification)
```

---

## 6. Derived Metrics Schema

Derived metrics are **certification-relevant abstractions** of raw telemetry.

```json
{
  "metric_id": "UUID",
  "om_event_id": "UUID",
  "dpp_id": "UUID",
  "metric_name": "string",
  "value": "number",
  "unit": "string",
  "aggregation_window": "string",
  "aggregation_method": "mean | max | min | stddev | count | percentile",
  "derived_from": ["signal_name"],
  "timestamp": "ISO-8601",
  "confidence": "number"
}
```

### Examples

| Metric Name                  | Derived From                           | Aggregation Method |
|------------------------------|----------------------------------------|--------------------|
| mean_pitch_error_deg         | pitch_angle_predicted, pitch_angle_actual | mean              |
| max_envelope_exceedance      | altitude, speed, temperature           | max                |
| inference_latency_p99_ms     | inference_start_time, inference_end_time | percentile(99)   |
| prediction_accuracy_ratio    | prediction, ground_truth               | mean(abs(error))   |

**Certification Significance:**  
Derived metrics are the bridge between raw operational data and DPP validation. They must be:
* Reproducible from raw telemetry
* Defined before OAV campaign execution
* Traceable to specific DPP claims

---

## 7. Alignment with DPP Predictions

Every telemetry stream **shall be mappable** to one of:

* **DPP constraint** (e.g., "altitude_max_m: 15000")
* **DPP performance claim** (e.g., "prediction_accuracy > 0.95")
* **DPP operational envelope** (e.g., "valid within ODD")

### Mapping Table Schema

```sql
CREATE TABLE dpp_telemetry_mapping (
  id UUID PRIMARY KEY,
  dpp_id UUID NOT NULL REFERENCES dpp_record(id),
  stream_name VARCHAR(128) NOT NULL,
  signal_name VARCHAR(128) NOT NULL,
  dpp_claim_type VARCHAR(64) NOT NULL,
  dpp_claim_path VARCHAR(256),
  comparison_operator VARCHAR(16),
  threshold_value NUMERIC,
  notes TEXT,
  
  CONSTRAINT valid_claim_type CHECK (
    dpp_claim_type IN ('constraint', 'performance_claim', 'envelope', 'capability')
  )
);
```

**Purpose:**  
This mapping enables automated validation: for each OM event, telemetry can be automatically compared against DPP predictions to generate validation evidence.

---

## 8. Certification Rules

1. **Immutability**  
   Raw telemetry is **never deleted** during active lifecycle. Archival only after retirement.

2. **Reproducibility**  
   Derived metrics must be reproducible from raw telemetry using documented algorithms.

3. **Traceability**  
   All telemetry is traceable to:
   * SystemProduct (what emitted it)
   * DPP (what predicted it)
   * OM Event (when it occurred)

4. **Time Synchronization**  
   Time synchronization method and accuracy must be documented and auditable. GPS time or certified time source required for certification-grade telemetry.

5. **Quality Assessment**  
   Every telemetry point must carry a quality flag. INVALID data may be recorded but never used for certification decisions.

6. **Source Attribution**  
   The source of every measurement must be known and traceable to calibration records.

---

## 9. Query Patterns

### 9.1 Retrieve Telemetry for OM Event

```sql
SELECT stream_name, signal_name, ts, value, unit, quality_flag
FROM telemetry_event
WHERE om_event_id = 'specific-uuid'
  AND quality_flag IN ('OK', 'DEGRADED')
ORDER BY ts;
```

### 9.2 Compare DPP Prediction vs Actual

```sql
WITH dpp_claims AS (
  SELECT dpp_claim_path, threshold_value, comparison_operator
  FROM dpp_telemetry_mapping
  WHERE dpp_id = 'specific-dpp-uuid'
),
actual_telemetry AS (
  SELECT signal_name, AVG((value->>'value')::numeric) as avg_value
  FROM telemetry_event
  WHERE om_event_id = 'specific-om-uuid'
    AND quality_flag = 'OK'
  GROUP BY signal_name
)
SELECT d.dpp_claim_path, d.threshold_value, a.avg_value,
       CASE 
         WHEN d.comparison_operator = '<=' AND a.avg_value <= d.threshold_value THEN 'PASS'
         WHEN d.comparison_operator = '>=' AND a.avg_value >= d.threshold_value THEN 'PASS'
         ELSE 'FAIL'
       END as validation_result
FROM dpp_claims d
JOIN actual_telemetry a ON d.dpp_claim_path LIKE '%' || a.signal_name || '%';
```

---

## 10. Assets

Recommended assets in `ASSETS/`:

* **95-90-02-003-A-001_Telemetry_Signal_Catalog.csv**  
  Master catalog of all telemetry signals with units, ranges, sampling rates

* **95-90-02-003-A-002_TimeSeries_Flow_Diagram.drawio**  
  Data flow from sensors through TSDB to certification store

* **95-90-02-003-A-003_Metric_Derivation_Map.json**  
  JSON schema defining how derived metrics are computed from raw signals

* **95-90-02-003-A-004_DPP_Telemetry_Mapping_Examples.csv**  
  Example mappings between DPP claims and telemetry signals

---

## 11. Cross-References

### 11.1 Related Documents

* [95-90-02-002_Common_Entity_Schemas.md](./95-90-02-002_Common_Entity_Schemas.md) — Entity definitions
* [95-90-02-006_CCert_CVal_Database_Schema.md](./95-90-02-006_CCert_CVal_Database_Schema.md) — Physical schema
* [95-90-02-007_CCert_CVal_Core_Data_Model.md](./95-90-02-007_CCert_CVal_Core_Data_Model.md) — Logical model
* [95-90-02-008_Common_Relationship_Semantics.md](./95-90-02-008_Common_Relationship_Semantics.md) — Relationship meanings

### 11.2 Future Documents

* **95-90-02-009_CCert_CVal_Event_Model.md** — Event sourcing for the CCert/CVal loop
* **95-90-02-010_CCert_CVal_Query_Cookbook.md** — Standard certification queries

---

## 12. Version History

| Version | Date       | Author                            | Changes                              |
|---------|------------|-----------------------------------|--------------------------------------|
| 1.0     | 2025-12-13 | AMPEL360 ATA 95 Data Architecture | Initial time-series schema definition|

---

## 13. Document Control

- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by [Approver]
- **Status**: WORKING – Subject to formal review and approval
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **Sub-bucket**: 02_Global_Data_Schemas
- **Document ID**: 95-90-02-003
- **Last AI update**: 2025-12-13
- **Criticality**: FOUNDATIONAL

---

## 14. Final Note

Telemetry is not just data.  
**Telemetry is the voice of operational truth.**

Without proper time-series capture and structuring, there is no OAV, no CVal, no DT, and no CCert.

This schema ensures that operational reality speaks clearly and traceably to the certification process.

---

**End of Document**
