# 95-90-00-005 — Naming and Versioning Rules

## 1. Purpose

This document provides detailed **naming patterns and versioning strategies** for all artifacts in the 95-90 bucket, ensuring consistency and discoverability.

## 2. Naming Patterns

### 2.1 Document Files

**Pattern**: `{ATA}-{BUCKET}-{SECTION}-{ID}_{DESCRIPTION}.md`

**Components**:
- `{ATA}`: Always `95` for this chapter
- `{BUCKET}`: Always `90` for this bucket
- `{SECTION}`: Two-digit section code (`00`, `01`, `02`, etc.)
- `{ID}`: Three-digit sequential ID (`001`, `002`, `003`, etc.)
- `{DESCRIPTION}`: Snake_case descriptive name

**Examples**:
```
95-90-00-001_Tables_Schemas_Diagrams_Overview.md
95-90-01-001_Global_Taxonomies_Overview.md
95-90-02-002_Common_Entity_Schemas.md
95-90-28-001_H2_and_Fuel_Tables_Schemas_Overview.md
```

### 2.2 Asset Files

**Pattern**: `{ATA}-{BUCKET}-{SECTION}-A-{ID}_{DESCRIPTION}.{ext}`

The `A` designates an asset file (data, diagram, etc.) as opposed to documentation.

**Examples**:
```
95-90-01-A-001_Functional_Taxonomy_Table.csv
95-90-02-A-001_Aircraft_and_Flight_Schema.json
95-90-06-A-004_Example_Diagrams_Pack.drawio
95-90-28-A-003_H2_PandID_Diagram.drawio
```

### 2.3 Directory Names

**Pattern**: `{SECTION}_{DESCRIPTION}/`

Where:
- `{SECTION}`: Two-digit code or special name (e.g., `00_META`, `ASSETS`)
- `{DESCRIPTION}`: Snake_case description

**Examples**:
```
00_META/
95-90-01_Global_Reference_Taxonomies/
95-90-28_H2_and_Fuel_Tables_Schemas_Diagrams/
ASSETS/
```

### 2.4 Schema Identifiers

**Pattern**: `{domain}_{entity}_{schema_type}`

Used within schema files as the schema ID:

**Examples**:
```
glb_aircraft_entity
glb_telemetry_timeseries
h2_tank_entity
ima_partition_config
```

## 3. Versioning Strategy

### 3.1 Semantic Versioning

All schemas, tables, and diagrams use **Semantic Versioning 2.0.0**:

```
vMAJOR.MINOR.PATCH
```

**Version Components**:
- **MAJOR**: Incompatible API changes (breaking changes)
- **MINOR**: Backward-compatible new features
- **PATCH**: Backward-compatible bug fixes

**Initial Versions**:
- First release: `v1.0.0`
- Pre-release: `v0.1.0`, `v0.2.0`, etc.

### 3.2 Version Increment Rules

#### MAJOR Version Increment

Increment when making **breaking changes**:
- Removing required fields
- Changing field types incompatibly
- Changing API signatures
- Removing endpoints or operations

**Example**: `v1.5.2` → `v2.0.0`

#### MINOR Version Increment

Increment when adding **backward-compatible features**:
- Adding optional fields
- Adding new endpoints
- Adding new enum values
- Deprecating fields (but not removing)

**Example**: `v1.5.2` → `v1.6.0`

#### PATCH Version Increment

Increment for **backward-compatible fixes**:
- Fixing typos in descriptions
- Clarifying field meanings
- Updating examples
- Fixing validation constraints

**Example**: `v1.5.2` → `v1.5.3`

### 3.3 Pre-Release Versions

For schemas under development:

```
v0.1.0        # Initial draft
v0.2.0        # First review
v0.9.0        # Release candidate
v1.0.0        # Production release
```

Pre-release versions (v0.x.x) may have breaking changes between MINOR versions.

### 3.4 Version in Filenames

For versioned assets, append version to filename:

```
95-90-02-A-001_Aircraft_Schema_v1.2.0.json
95-90-28-A-002_H2_Safety_Sensor_Map_v2.0.0.json
```

Alternatively, use directories:
```
ASSETS/
├── v1.0/
│   └── 95-90-02-A-001_Aircraft_Schema.json
├── v1.1/
│   └── 95-90-02-A-001_Aircraft_Schema.json
└── v2.0/
    └── 95-90-02-A-001_Aircraft_Schema.json
```

## 4. Changelog Management

### 4.1 Changelog Format

Every versioned artifact must include a changelog:

```json
{
  "changelog": {
    "2.0.0": {
      "date": "2025-11-17",
      "changes": [
        "BREAKING: Removed deprecated 'legacy_id' field",
        "Added 'hydrogen_capacity' field to aircraft schema"
      ]
    },
    "1.2.0": {
      "date": "2025-10-15",
      "changes": [
        "Added optional 'icao_type' field",
        "Deprecated 'legacy_id' field (use 'uuid' instead)"
      ]
    },
    "1.1.0": {
      "date": "2025-09-01",
      "changes": [
        "Added 'registration_country' field"
      ]
    },
    "1.0.0": {
      "date": "2025-08-01",
      "changes": [
        "Initial release"
      ]
    }
  }
}
```

### 4.2 Change Categories

Prefix changes with category:
- `BREAKING:` — Breaking change
- `FEATURE:` — New feature
- `FIX:` — Bug fix
- `DOCS:` — Documentation update
- `DEPRECATED:` — Deprecation notice

## 5. Deprecation Policy

### 5.1 Deprecation Process

1. **Mark as deprecated**: Add deprecation notice in schema
2. **Document migration**: Provide migration guide
3. **Maintain for one MINOR version**: Keep deprecated field functional
4. **Remove in next MAJOR version**: Remove in breaking change release

### 5.2 Deprecation Notice Format

```json
{
  "properties": {
    "legacy_id": {
      "type": "string",
      "deprecated": true,
      "deprecationMessage": "Use 'uuid' field instead. This field will be removed in v2.0.0",
      "deprecatedSince": "v1.2.0",
      "removedIn": "v2.0.0",
      "migrationGuide": "Replace 'legacy_id' with 'uuid'. No data transformation needed."
    }
  }
}
```

## 6. Compatibility Matrix

### 6.1 Forward Compatibility

Older clients should work with newer schemas (within same MAJOR version):
- `v1.0.0` client can consume `v1.5.0` schema (ignores new fields)
- `v1.5.0` client may not work with `v1.0.0` schema (missing fields)

### 6.2 Backward Compatibility

Newer clients should work with older schemas (within same MAJOR version):
- `v1.5.0` client can consume `v1.0.0` schema (uses defaults for new fields)

### 6.3 Breaking Compatibility

MAJOR version changes break compatibility:
- `v1.x.x` and `v2.x.x` are incompatible
- Migration required
- Document migration path

## 7. Naming Constraints

### 7.1 Character Restrictions

- **Alphanumeric**: `a-z`, `A-Z`, `0-9`
- **Separators**: `-`, `_`
- **No spaces**: Use `_` instead
- **No special characters**: Avoid `@`, `#`, `$`, etc.

### 7.2 Length Limits

- **File names**: Maximum 255 characters
- **Directory names**: Maximum 255 characters
- **Schema IDs**: Maximum 64 characters
- **Descriptions**: Maximum 100 characters (in filenames)

### 7.3 Case Conventions

- **Files and directories**: `Snake_case` (lowercase with underscores)
- **Schema IDs**: `snake_case` (lowercase with underscores)
- **JSON properties**: `snake_case` (lowercase with underscores)
- **Constants**: `UPPER_SNAKE_CASE`

## 8. Registry Integration

### 8.1 Registry Entry

Every named artifact must be registered:

```json
{
  "id": "aircraft_schema",
  "name": "Aircraft Entity Schema",
  "file": "95-90-02_Global_Data_Schemas/ASSETS/95-90-02-A-001_Aircraft_and_Flight_Schema.json",
  "version": "1.2.0",
  "type": "entity_schema",
  "domain": "GLB",
  "status": "APPROVED",
  "lastUpdated": "2025-11-17",
  "owner": "Data Architecture WG",
  "changelog_url": "95-90-02-A-001_Aircraft_Schema_Changelog.md"
}
```

### 8.2 Version History

Registry maintains version history:

```json
{
  "id": "aircraft_schema",
  "current_version": "1.2.0",
  "versions": [
    {"version": "1.2.0", "date": "2025-11-17", "status": "APPROVED"},
    {"version": "1.1.0", "date": "2025-10-15", "status": "ARCHIVED"},
    {"version": "1.0.0", "date": "2025-08-01", "status": "ARCHIVED"}
  ]
}
```

## 9. Validation

### 9.1 Naming Validation

Automated checks verify:
- Naming pattern compliance
- Character restrictions
- Length limits
- No duplicates

### 9.2 Versioning Validation

Automated checks verify:
- Semantic versioning format
- Version increment validity
- Changelog presence
- Backward compatibility (within MAJOR version)

## 10. Status

- **Document ID**: 95-90-00-005
- **Version**: 1.0
- **Status**: ACTIVE
- **Last Updated**: 2025-11-17
- **Owner**: AMPEL360 Data Architecture WG

---

## Document Control

- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
