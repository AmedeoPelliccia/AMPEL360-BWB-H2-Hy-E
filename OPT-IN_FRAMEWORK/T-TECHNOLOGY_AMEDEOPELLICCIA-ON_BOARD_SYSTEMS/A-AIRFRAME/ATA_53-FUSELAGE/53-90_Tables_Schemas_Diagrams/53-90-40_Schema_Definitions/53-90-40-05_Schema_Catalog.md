# 53-90-40-05 Schema Catalog

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-40-05 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / DATA |
| **ATA Chapter** | 53-90-40 |

---

## 1. Purpose

This document provides a catalog of all schemas defined for the ANCHORS system, including JSON schemas, XML schemas, and data format specifications.

## 2. Schema Inventory

### 2.1 JSON Schemas

| Schema ID | File | Version | Purpose | Status |
|-----------|------|---------|---------|--------|
| SIG-SCH-001 | `53-90-40-01_Signal_Schema.json` | 1.0 | Signal definitions | ✅ Active |
| PAR-SCH-001 | `53-90-40-02_Parameter_Schema.json` | 1.0 | Parameter definitions | ✅ Active |
| DPP-SCH-001 | `53-90-40-03_DPP_Event_Schema.json` | 1.0 | DPP lifecycle events | ✅ Active |

### 2.2 XML Schemas

| Schema ID | File | Version | Purpose | Status |
|-----------|------|---------|---------|--------|
| DMC-SCH-001 | `53-90-40-04_DMC_Schema.xsd` | 1.0 | S1000D DMC codes | ✅ Active |

### 2.3 CSV Templates

| Template ID | Location | Version | Purpose |
|-------------|----------|---------|---------|
| SIG-CSV-001 | `53-90-10-01_Signal_Catalog.csv` | 1.0 | Signal catalog |
| PAR-CSV-001 | `53-90-20-01_Parameter_Catalog.csv` | 1.0 | Parameter catalog |
| VL-CSV-001 | `53-90-30-01_AFDX_VL_Definitions.csv` | 1.0 | AFDX VL definitions |
| CAN-CSV-001 | `53-90-30-02_CAN_Message_Definitions.csv` | 1.0 | CAN message definitions |

## 3. Schema Details

### 3.1 Signal Schema (SIG-SCH-001)

**Purpose**: Validate signal definitions in the ANCHORS signal dictionary

**Required Fields**:
- `signal_id` — Pattern: `^ANCH_[A-Z0-9]+_[TPFLVIWSDACX]_[A-Z0-9_]+$`
- `name` — Max 64 characters
- `type` — Enum: T, P, F, L, V, I, W, S, D, A, C, X
- `range` — Object with min/max
- `units` — String
- `source` — Source LRU
- `destination` — Destination LRU(s)
- `rate_hz` — 0.001 to 1000
- `dal` — Enum: A, B, C, D, E

**Optional Fields**:
- `description`
- `scaling`
- `fault_handling`
- `traceability`

### 3.2 Parameter Schema (PAR-SCH-001)

**Purpose**: Validate parameter definitions in the ANCHORS parameter database

**Required Fields**:
- `param_id` — Pattern: `^P_[A-Z0-9]+_[A-Z0-9_]+$`
- `name` — Max 64 characters
- `category` — Enum: Fixed, Tunable, Configurable, Adaptive
- `default` — Number
- `units` — String
- `bucket` — Pattern: `^53-(0[0-9]|[1-8][0-9]|90)$`

**Optional Fields**:
- `min`, `max` — (null for Fixed)
- `description`
- `data_type`
- `persistence`
- `modification`
- `validation`
- `traceability`

### 3.3 DPP Event Schema (DPP-SCH-001)

**Purpose**: Validate Digital Product Passport lifecycle events

**Required Fields**:
- `event_id` — UUID format
- `event_type` — Enum of lifecycle events
- `timestamp` — ISO 8601 datetime
- `component_id` — Pattern: `^ANCH-[A-Z]{3}-[0-9]{6}$`

**Conditional Requirements**:
- INSTALLATION: requires `msn`, `location`
- REMOVAL: requires `reason`, `condition`
- FAULT: requires `fault_code`, `severity`
- SWAP: requires `old_component_id`, `new_component_id`

### 3.4 DMC Schema (DMC-SCH-001)

**Purpose**: Validate S1000D Data Module Codes for technical publications

**Pattern**: `DMC-AMPEL-[A-Z]-53-[0-9]{2}-[0-9]{2}-[0-9]{2}[A-Z]-[0-9]{3}-[A-Z]`

**Info Codes**:
| Code | Description |
|------|-------------|
| A | Description and operation |
| C | Parts data |
| D | Maintenance procedures |
| F | Fault isolation |
| G | Structural data |
| S | Safety data |

## 4. Validation Procedures

### 4.1 Automated Validation

```bash
# Validate JSON file against schema
jsonschema --instance data.json 53-90-40-01_Signal_Schema.json

# Validate XML against XSD
xmllint --schema 53-90-40-04_DMC_Schema.xsd document.xml
```

### 4.2 CI/CD Integration

| Stage | Tool | Schema | Action |
|-------|------|--------|--------|
| Pre-commit | jsonschema | All JSON | Block on error |
| PR Review | ajv | All JSON | Report warnings |
| Release | Full suite | All | Block release |

## 5. Schema Versioning

### 5.1 Version Policy

| Change Type | Version Bump | Compatibility |
|-------------|--------------|---------------|
| Breaking | Major (X.0.0) | Not backward compatible |
| New Field | Minor (x.Y.0) | Backward compatible |
| Clarification | Patch (x.y.Z) | No functional change |

### 5.2 Version History

| Schema | Version | Date | Changes |
|--------|---------|------|---------|
| Signal | 1.0 | 2025-11-27 | Initial release |
| Parameter | 1.0 | 2025-11-27 | Initial release |
| DPP Event | 1.0 | 2025-11-27 | Initial release |
| DMC | 1.0 | 2025-11-27 | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
