# DPP Export v0.1 — Aircraft Baseline Digital Product Passport Export Package

## Overview

The **Aircraft Baseline DPP Export v0.1** package provides a standardized format for exporting complete Digital Product Passport (DPP) data for an aircraft baseline configuration. This package enables traceability, configuration management, and regulatory compliance throughout the aircraft lifecycle.

### Package Contents

This package defines JSON Schema draft-07 specifications and example documents for:

1. **manifest.json** — Export package manifest and file inventory
2. **baseline.json** — Aircraft baseline configuration (components, assemblies, BOMs)
3. **effectivity.json** — Component effectivity and applicability rules
4. **software_bom.json** — Software Bill of Materials for avionics and embedded systems

Additionally, the package references:
- **sbom_aircraft.spdx.json** — Aircraft-level SBOM in SPDX 2.3 JSON standard format (not redefined here; see [SPDX 2.3 specification](https://spdx.github.io/spdx-spec/v2.3/))

---

## Directory Structure

```
schemas/dpp_export/v0.1/
├── manifest.schema.json          # Manifest schema (JSON Schema draft-07)
├── baseline.schema.json          # Baseline configuration schema
├── effectivity.schema.json       # Effectivity matrix schema
└── software_bom.schema.json      # Software BOM schema

examples/dpp_export/v0.1/
├── manifest.json                 # Example manifest
├── baseline.json                 # Example baseline
├── effectivity.json              # Example effectivity
└── software_bom.json             # Example software BOM
```

---

## Schema Specifications

### 1. manifest.json

**Purpose:** Describes the complete DPP export package, including metadata and a validated file inventory.

**Key Features:**
- Unique export identification and versioning
- Complete file manifest with checksums (SHA-256)
- File type classification
- Path validation (no absolute paths allowed)
- **Hardening:** `uniqueItems` constraint on files array; path `minLength` > 0 and pattern prevents absolute paths

**Required Fields:**
- `export_id` — Unique identifier for this export
- `export_version` — Format version (semantic versioning)
- `created_at` — ISO 8601 timestamp
- `aircraft_model` — Aircraft model designation
- `baseline_id` — Reference to baseline configuration
- `files` — Array of files (must be unique)

**Schema Location:** `schemas/dpp_export/v0.1/manifest.schema.json`

---

### 2. baseline.json

**Purpose:** Defines the baseline configuration for an aircraft model, including all major components, assemblies, and part numbers organized by ATA chapter.

**Key Features:**
- Component hierarchy with parent-child relationships
- ATA iSpec 2200 chapter mapping
- Weight, criticality, and certification basis tracking
- Manufacturer and supplier information
- Change history tracking

**Required Fields:**
- `baseline_id` — Unique baseline identifier
- `baseline_version` — Version (semantic versioning)
- `aircraft_model` — Aircraft model designation
- `effective_date` — When this baseline becomes effective
- `components` — Array of components and assemblies

**Schema Location:** `schemas/dpp_export/v0.1/baseline.schema.json`

---

### 3. effectivity.json

**Purpose:** Defines which components and configurations are effective for specific aircraft serial numbers, tail numbers, or production runs.

**Key Features:**
- MSN (Manufacturer Serial Number) range applicability
- Tail number (registration) specific rules
- Production batch and configuration filtering
- Exclusion rules with mandatory identification
- **Hardening:** Exclusions require at least one of `msn` or `tail_number` (enforced via `anyOf` constraint)
- Modification and service bulletin references

**Required Fields:**
- `effectivity_id` — Unique effectivity matrix identifier
- `baseline_id` — Reference to baseline configuration
- `rules` — Array of effectivity rules

**Schema Location:** `schemas/dpp_export/v0.1/effectivity.schema.json`

---

### 4. software_bom.json

**Purpose:** Software Bill of Materials for all avionics and embedded software systems on the aircraft.

**Key Features:**
- DO-178C certification level tracking
- Binary and configuration file inventories with checksums
- Software dependency mapping
- Target hardware specification
- License and verification status tracking
- **Hardening:** Filename fields enforce basename-only (no path separators) via pattern `^[^/\\\\]+$`

**Required Fields:**
- `sbom_id` — Unique SBOM identifier
- `sbom_version` — Version (semantic versioning)
- `aircraft_model` — Aircraft model designation
- `baseline_id` — Reference to baseline configuration
- `software_components` — Array of software components

**Schema Location:** `schemas/dpp_export/v0.1/software_bom.schema.json`

---

## Validation

### Prerequisites

Install required Python dependencies:

```bash
pip install -r requirements.txt
```

This will install `jsonschema>=4.20.0` for JSON Schema validation.

### Running Validation

To validate all example JSON documents against their schemas:

```bash
python3 tools/validate_dpp_export.py
```

**Expected Output:**

```
======================================================================
DPP Export v0.1 Validation
======================================================================

Validating: manifest.json
Against:    manifest.schema.json
✓ VALID

Validating: baseline.json
Against:    baseline.schema.json
✓ VALID

Validating: effectivity.json
Against:    effectivity.schema.json
✓ VALID

Validating: software_bom.json
Against:    software_bom.schema.json
✓ VALID

======================================================================
Validation Summary
======================================================================
Total files validated: 4
Valid: 4
Invalid: 0

✓ All DPP Export v0.1 examples are valid!
```

### Validating Custom Documents

To validate your own JSON documents:

```python
import json
from jsonschema import Draft7Validator

# Load schema
with open('schemas/dpp_export/v0.1/manifest.schema.json') as f:
    schema = json.load(f)

# Load your data
with open('my_manifest.json') as f:
    data = json.load(f)

# Validate
validator = Draft7Validator(schema)
errors = list(validator.iter_errors(data))

if not errors:
    print("✓ Valid!")
else:
    for error in errors:
        print(f"✗ {error.message}")
```

---

## Hardening Features

### manifest.json
- **uniqueItems:** Files array cannot contain duplicate entries
- **path validation:** 
  - `minLength: 1` — path cannot be empty
  - `pattern: ^[^/\\\\].*$` — path cannot start with `/` or `\` (prevents absolute paths)
- **checksum format:** SHA-256 checksums must be 64 hex characters

### baseline.json
- **Part number format:** Enforced pattern `^[A-Z0-9\\-_.]+$`
- **ATA chapter format:** Pattern `^\\d{2}(-\\d{2})?(-\\d{2})?$` (e.g., "53-00", "31-20")
- **Quantity validation:** Must be greater than 0 (exclusiveMinimum)

### effectivity.json
- **Exclusions validation:** Exclusions must have at least one of:
  - `msn` array, OR
  - `tail_number` array
  - Enforced via `anyOf` JSON Schema constraint
- **Tail number format:** Pattern `^[A-Z0-9-]+$`
- **MSN validation:** Must be integers ≥ 1

### software_bom.json
- **Filename validation:** Pattern `^[^/\\\\]+$` enforces basename only (no path separators)
- **Checksum format:** SHA-256 checksums must be 64 hex characters
- **Load address format:** Pattern `^0x[0-9a-fA-F]+$` for hexadecimal addresses
- **Certification level:** Enum constraint for DO-178C DAL levels

---

## Usage Examples

### Creating a Manifest

```json
{
  "export_id": "DPP-AMPEL360-Q100-2025-001",
  "export_version": "0.1",
  "created_at": "2025-12-12T10:30:00Z",
  "aircraft_model": "AMPEL360-Q100",
  "baseline_id": "Q100-BASELINE-001",
  "files": [
    {
      "path": "baseline.json",
      "type": "baseline",
      "checksum": "a1b2c3...",
      "size_bytes": 45678
    }
  ]
}
```

### Defining Effectivity Rules

```json
{
  "rule_id": "RULE-002",
  "component_id": "PROP-61-FC-002",
  "applicability": {
    "msn_range": { "from": 51, "to": 9999 }
  },
  "exclusions": {
    "msn": [55, 72],
    "reason": "Test aircraft with experimental variant"
  }
}
```

### Software Component Entry

```json
{
  "component_id": "SW-FCC-31-001",
  "name": "Flight Control Computer Software",
  "version": "2.5.1",
  "supplier": "Avionics Systems Inc",
  "ata_chapter": "31-00",
  "certification_level": "DAL-A",
  "binary_files": [
    {
      "filename": "fcc_primary.elf",
      "checksum": "1a2b3c4d...",
      "load_address": "0x08000000"
    }
  ]
}
```

---

## Integration with AMPEL360 Repository

This DPP Export package integrates with:

- **OPT-IN Framework:** ATA chapter alignment (see `OPT-IN_FRAMEWORK/`)
- **CI/CD Pipeline:** Automated validation in `.github/workflows/`
- **Configuration Management:** Links to `tools/genccc/baseline.py`
- **SBOM Generation:** Complements existing `tools/schemas/SBOM.md`

---

## Regulatory Compliance

The DPP Export v0.1 package supports compliance with:

- **EASA Part 21** — Design Organization requirements
- **CS-25** — Certification Specifications for Large Aeroplanes
- **EU AI Act** — Digital Product Passport requirements
- **DO-178C** — Software lifecycle traceability
- **DO-254** — Hardware lifecycle traceability

---

## Version History

| Version | Date       | Description                           |
|---------|------------|---------------------------------------|
| 0.1     | 2025-12-12 | Initial stable release with hardening |

---

## References

- [JSON Schema Draft-07 Specification](https://json-schema.org/draft-07/schema)
- [SPDX 2.3 Specification](https://spdx.github.io/spdx-spec/v2.3/)
- [ATA iSpec 2200](https://www.ataebiz.org/)
- [DO-178C](https://www.rtca.org/content/standards-guidance-materials) — Software Considerations in Airborne Systems
- [AMPEL360 OPT-IN Framework](../../OPT-IN_FRAMEWORK_STANDARD.md)

---

## Support and Contributions

For questions, issues, or contributions related to the DPP Export v0.1 package:

- **Issues:** [GitHub Issues](https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/issues)
- **Discussions:** [GitHub Discussions](https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/discussions)
- **Wiki:** [Project Wiki](https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/wiki)

---

## License

Copyright © 2025 AMPEL360. Licensed under Apache License 2.0.
See [LICENSE](../../LICENSE) for details.
