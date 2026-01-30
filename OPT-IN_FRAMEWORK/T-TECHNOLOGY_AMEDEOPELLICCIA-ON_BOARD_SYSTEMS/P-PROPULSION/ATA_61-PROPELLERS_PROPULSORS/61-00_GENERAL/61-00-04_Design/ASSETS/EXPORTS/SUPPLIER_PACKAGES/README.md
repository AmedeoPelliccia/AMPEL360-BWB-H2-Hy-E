# SUPPLIER_PACKAGES — Supplier Data Packages

This directory contains data packages prepared for external suppliers involved in the manufacturing and assembly of ATA 61 propulsion system components.

## Purpose

Supplier packages enable:

- Controlled data sharing with external partners
- Consistent package structure across suppliers
- Traceability of released supplier data
- Compliance with export control requirements
- Efficient supplier onboarding and communication

## Directory Structure

```
SUPPLIER_PACKAGES/
├── README.md           # This file
└── [Supplier packages placed here]
```

## Package Structure

Each supplier package SHALL follow this structure:

```
Q100-61-SUP-[SUPPLIER]-[COMPONENT]-R[rev].zip
├── MANIFEST.yaml                    # Package manifest (required)
├── COVER_LETTER.pdf                 # Package cover letter
├── TECHNICAL/                       # Technical data
│   ├── DRAWINGS/                    # Drawing package
│   ├── MODELS/                      # CAD models (neutral formats)
│   └── SPECIFICATIONS/              # Technical specifications
├── QUALITY/                         # Quality requirements
│   ├── INSPECTION_REQUIREMENTS.pdf  # Inspection criteria
│   └── ACCEPTANCE_CRITERIA.pdf      # Acceptance standards
├── COMMERCIAL/                      # Commercial documents
│   └── PURCHASE_ORDER.pdf           # PO reference (if applicable)
└── COMPLIANCE/                      # Compliance documentation
    ├── EXPORT_CLASSIFICATION.pdf    # Export control classification
    └── NDA_REFERENCE.pdf            # NDA reference (not actual NDA)
```

## Manifest Requirements

Every supplier package MUST include a `MANIFEST.yaml` with the following structure:

```yaml
# Supplier Package Manifest
package_id: Q100-61-SUP-[SUPPLIER]-[COMPONENT]-R[rev]
package_version: R01
created_date: YYYY-MM-DD
expiration_date: YYYY-MM-DD  # Data validity period

supplier:
  name: "[Supplier Company Name]"
  code: "[Internal supplier code]"
  contact: "[Supplier contact name]"
  email: "[Contact email]"

program:
  name: "AMPEL360-BWB-H2-Hy-E"
  designation: "Q100"
  ata_chapter: "61"

component:
  name: "[Component name]"
  part_number: "[Part number]"
  revision: "[Revision]"
  quantity_required: [Number]

classification:
  export_control: "[ECCN or EAR99]"
  data_rights: "[Data rights category]"
  confidentiality: "[Confidentiality level]"

contents:
  - path: "TECHNICAL/DRAWINGS/..."
    description: "Engineering drawings"
    revision: "A"
    
  - path: "TECHNICAL/MODELS/..."
    description: "CAD model (STEP AP242)"
    revision: "A"

approvals:
  prepared_by: "[Name]"
  reviewed_by: "[Name]"
  approved_by: "[Name]"
  export_control_officer: "[Name]"

change_log:
  - version: R01
    date: YYYY-MM-DD
    description: "Initial release"
```

## Naming Convention

Supplier packages follow:

```
Q100-61-SUP-[SUPPLIER]-[COMPONENT]-R[rev].zip
```

### Components

| Component    | Description                              |
|--------------|------------------------------------------|
| Q100-61      | Program and ATA chapter identifier       |
| SUP          | Supplier package type code               |
| [SUPPLIER]   | Supplier code (3-6 characters)           |
| [COMPONENT]  | Component identifier                     |
| R[rev]       | Release revision (R01, R02, etc.)        |

### Examples

```
Q100-61-SUP-ACME-GBX-HOUSING-R01.zip     → Gearbox housing package to ACME
Q100-61-SUP-FLYCO-FAN-BLADE-R02.zip      → Fan blade package to FLYCO (rev 2)
Q100-61-SUP-MOTEX-EMD-STATOR-R01.zip     → Motor stator package to MOTEX
Q100-61-SUP-AEROTECH-NAC-SHELL-R01.zip   → Nacelle shell package to AEROTECH
```

## Package Creation Process

1. **Scope Definition**
   - Define package contents based on supplier scope of work
   - Identify required drawings, models, and specifications
   - Determine quality and inspection requirements

2. **Export Control Review**
   - Classify all technical data
   - Verify supplier eligibility (country, license status)
   - Document export control classification

3. **Content Assembly**
   - Collect approved drawings and models
   - Convert models to neutral formats (STEP, JT)
   - Prepare specifications and requirements

4. **Manifest Creation**
   - Complete manifest with all required fields
   - List all package contents
   - Document approvals and classifications

5. **Quality Review**
   - Verify all files present and correct
   - Validate manifest accuracy
   - Check for sensitive data

6. **Approval**
   - Engineering approval
   - Export control officer approval
   - Program management approval

7. **Distribution**
   - Secure transfer to supplier
   - Document distribution record
   - Archive package in RELEASE_HISTORY

## Data Rights and Classification

### Data Rights Categories

| Category     | Description                              |
|--------------|------------------------------------------|
| Unlimited    | No restrictions on use                   |
| Limited      | Restricted to contract scope             |
| Proprietary  | Company proprietary, NDA required        |
| Restricted   | Special handling required                |

### Export Control

All supplier packages MUST include export classification:

- **ECCN**: Export Control Classification Number (if controlled)
- **EAR99**: Not controlled under EAR
- **ITAR**: International Traffic in Arms Regulations (if applicable)

## Supplier Package Register

Maintain a register of all released supplier packages:

| Package ID | Supplier | Component | Rev | Release Date | Status |
|------------|----------|-----------|-----|--------------|--------|
| Example    | ACME     | GBX-HSG   | R01 | 2025-12-05   | Active |

## Related Documentation

- [Q100-61-EXPORT-SETTINGS.yaml](../Q100-61-EXPORT-SETTINGS.yaml) - Export settings
- [../README.md](../README.md) - EXPORTS overview
- [../RELEASE_HISTORY/README.md](../RELEASE_HISTORY/README.md) - Release archive

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
