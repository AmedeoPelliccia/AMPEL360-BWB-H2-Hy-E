# 95-90-00-002 — Usage Rules and Conventions

## 1. Purpose

This document defines the **naming conventions, versioning rules, and usage guidelines** for all tables, schemas, and diagrams in the 95-90 bucket.

## 2. Naming Conventions

### 2.1 File Naming Pattern

All files follow the pattern:
```
{ATA}-{BUCKET}-{SECTION}-{ID}_{DESCRIPTION}.{ext}
```

Where:
- **{ATA}**: `95` (ATA chapter)
- **{BUCKET}**: `90` (Tables, Schemas, Diagrams bucket)
- **{SECTION}**: `00` (meta), `01` (taxonomies), `02` (data), etc.
- **{ID}**: `001`, `002`, `003`, etc. (sequential)
- **{DESCRIPTION}**: Snake_case description
- **{ext}**: `.md`, `.json`, `.csv`, `.yaml`, `.drawio`, `.svg`, `.png`

**Examples:**
```
95-90-00-001_Tables_Schemas_Diagrams_Overview.md
95-90-01-A-001_Functional_Taxonomy_Table.csv
95-90-02-A-002_Telemetry_Timeseries_Schema.json
95-90-06-A-004_Example_Diagrams_Pack.drawio
```

### 2.2 Directory Naming Pattern

Directories follow:
```
{SECTION}_{DESCRIPTION}/
```

**Examples:**
```
00_META/
95-90-01_Global_Reference_Taxonomies/
95-90-28_H2_and_Fuel_Tables_Schemas_Diagrams/
ASSETS/
```

### 2.3 Asset Naming Pattern

Assets stored in `ASSETS/` subdirectories use the pattern:
```
{ATA}-{BUCKET}-{SECTION}-A-{ID}_{DESCRIPTION}.{ext}
```

The `A` indicates "Asset" to distinguish from documentation files.

## 3. Versioning Rules

### 3.1 Semantic Versioning

All schemas and tables use **semantic versioning**: `vMAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (incompatible with previous version)
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes and minor updates (backward compatible)

**Examples:**
```
v1.0.0 → Initial release
v1.1.0 → Added new optional fields
v1.1.1 → Fixed field description
v2.0.0 → Changed required fields (breaking)
```

### 3.2 Version Documentation

Each versioned file must include a header with:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Aircraft Schema",
  "version": "1.2.0",
  "lastUpdated": "2025-11-17",
  "changelog": {
    "1.2.0": "Added hydrogen tank capacity field",
    "1.1.0": "Added ICAO aircraft type",
    "1.0.0": "Initial release"
  }
}
```

### 3.3 Backward Compatibility

- **MINOR** and **PATCH** versions must be backward compatible
- **MAJOR** versions may break compatibility but must document migration path
- Deprecated fields must be marked for at least one MINOR version before removal

## 4. Schema Formats

### 4.1 JSON Schemas

Use **JSON Schema Draft-07** for all data schemas:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Entity Name",
  "version": "1.0.0",
  "type": "object",
  "properties": {
    "field_name": {
      "type": "string",
      "description": "Field purpose and usage"
    }
  },
  "required": ["field_name"]
}
```

### 4.2 CSV Tables

CSV files must include:
- **Header row**: Field names
- **UTF-8 encoding**
- **Comma separator**
- **Quote strings** containing commas or newlines

**Example:**
```csv
Field_Name,Type,Required,Description
aircraft_id,UUID,Yes,"Unique identifier for aircraft"
registration,String,Yes,"Aircraft registration number"
model,String,Yes,"Aircraft model designation"
```

### 4.3 YAML Configurations

Use YAML for configuration files:
```yaml
---
title: Configuration Name
version: 1.0.0
lastUpdated: 2025-11-17
config:
  setting_name: value
  nested_setting:
    sub_setting: value
```

## 5. Diagram Standards

### 5.1 Diagram Tools

- **Primary tool**: draw.io (diagrams.net)
- **Export formats**: `.drawio`, `.svg`, `.png`
- **Resolution**: Minimum 300 DPI for raster images

### 5.2 Diagram Types

| Type | Extension | Use Case |
|------|-----------|----------|
| Architecture | `.drawio` | System architecture, component diagrams |
| Process | `.drawio` | P&ID, flowcharts, state machines |
| ER Diagram | `.drawio` | Entity-relationship, data models |
| Interface | `.drawio` | API contracts, message flows |

### 5.3 Layer Conventions

All diagrams should use layers:
- **Layer 0**: Background (grid, borders)
- **Layer 1**: Main content (components, connections)
- **Layer 2**: Annotations (labels, notes)
- **Layer 3**: Overlay (highlights, change indicators)

## 6. Cross-Reference Format

### 6.1 Internal References

Use relative paths for internal references:
```markdown
[Schema Definition](95-90-02_Global_Data_Schemas/95-90-02-001_Global_Data_Schemas_Overview.md)
[Asset File](95-90-02_Global_Data_Schemas/ASSETS/95-90-02-A-001_Aircraft_and_Flight_Schema.json)
```

### 6.2 External References

Reference other ATA chapters using absolute paths from OPT-IN_FRAMEWORK:
```markdown
[Requirements](../95-00_GENERAL/95-00-03_Requirements/)
[Software Implementation](../95-40_Software/)
```

### 6.3 Traceability Links

All schemas and tables must link to:
```markdown
## Traceability
- **Requirements**: RQ-95-00-03-XXX
- **Design**: 95-00-04-XXX
- **Implementation**: 95-40-YYY
- **V&V**: TC-95-00-07-XXX
```

## 7. Registry Management

### 7.1 Schema Registration

All schemas must be registered in:
```
00_META/95-90-00-006_Tables_Schemas_Registry.json
```

Registry entry format:
```json
{
  "schema_id": "aircraft_schema",
  "name": "Aircraft Schema",
  "version": "1.2.0",
  "file": "95-90-02_Global_Data_Schemas/ASSETS/95-90-02-A-001_Aircraft_and_Flight_Schema.json",
  "category": "data_schema",
  "status": "active",
  "owner": "Data Architecture WG",
  "lastUpdated": "2025-11-17"
}
```

### 7.2 Update Process

When creating or updating schemas:
1. Create/update schema file with new version
2. Update registry entry
3. Update index in parent directory README
4. Document changes in changelog
5. Notify dependent teams

## 8. Documentation Requirements

### 8.1 Markdown Files

All markdown documentation must include:
- **Title**: H1 header with file ID
- **Sections**: Purpose, Scope, Content, Cross-references
- **Status block**: Version, owner, last updated
- **Document Control**: Standard, ATA chapter, bucket

### 8.2 Code Comments

JSON schemas must include:
- **Description** field for each property
- **Examples** for complex types
- **Constraints** documented (min, max, pattern)

## 9. Quality Standards

### 9.1 Validation

- **JSON schemas**: Must validate against JSON Schema Draft-07
- **CSV files**: Must parse without errors
- **Diagrams**: Must open without errors in draw.io

### 9.2 Completeness

- All mandatory fields must be present
- All cross-references must be valid
- All ASSETS must have corresponding documentation

## 10. Status

- **Document ID**: 95-90-00-002
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-11-17
- **Owner**: AMPEL360 Data Architecture WG

---

## Document Control

- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
