# DOCUMENTATION — Document Packages and Publications

This directory contains packaged document exports including drawing packages, data sheets, and technical publications for ATA 61 propulsion system components.

## Purpose

Documentation exports enable:

- Controlled drawing package releases
- Component data sheet distribution
- Technical publication generation (CMM, IPC, AMM)
- Regulatory submission packages
- Customer and supplier documentation

## Directory Structure

```
DOCUMENTATION/
├── README.md                   # This file
├── DRAWING_PACKAGES/           # Packaged drawing releases
│   └── MANIFESTS/              # Package manifest files
├── DATA_SHEETS/                # Component data sheets
└── TECHNICAL_PUBLICATIONS/     # CMM, IPC, AMM publications
```

## Format Specifications

### Drawing Packages (DRAWING_PACKAGES/)

**Controlled release packages of engineering drawings**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | ZIP archive containing PDF drawings      |
| Manifest             | YAML manifest in MANIFESTS/              |
| Drawing Format       | PDF/A-1b (archival quality)              |
| Revision Control     | Include revision letter in filename      |
| Naming               | `Q100-61-PKG-[COMPONENT]-R[rev].zip`     |

**Package Contents:**

```
Q100-61-PKG-FAN-ASSY-R01.zip
├── MANIFEST.yaml
├── Q100-61-DWG-FAN-ASSY-001-A.pdf
├── Q100-61-DWG-FAN-BLADE-002-A.pdf
├── Q100-61-DWG-FAN-HUB-003-A.pdf
├── Q100-61-BOM-FAN-ASSY-001.csv
└── RELEASE_NOTES.md
```

**Manifest Format (MANIFESTS/):**

```yaml
package_id: Q100-61-PKG-FAN-ASSY-R01
release_date: 2025-12-05
revision: R01
status: Released
classification: Company Confidential

contents:
  - file: Q100-61-DWG-FAN-ASSY-001-A.pdf
    type: assembly_drawing
    revision: A
    part_number: Q100-61-ASSY-FAN-001
    
  - file: Q100-61-DWG-FAN-BLADE-002-A.pdf
    type: detail_drawing
    revision: A
    part_number: Q100-61-PART-FAN-BLADE-002

approvals:
  design_engineer: TBD
  checker: TBD
  stress_engineer: TBD
  project_engineer: TBD
  
change_summary: |
  Initial release of fan assembly drawing package.
```

**Use Cases:**

- Manufacturing release packages
- Supplier data packages
- Certification submissions
- Customer deliverables

### Data Sheets (DATA_SHEETS/)

**Component and system data sheets**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Format               | Markdown (.md) or PDF                    |
| Template             | Use standard data sheet template         |
| Content              | Specifications, performance, interfaces  |
| Naming               | `Q100-61-DS-[COMPONENT].[ext]`           |

**Data Sheet Contents:**

- General description
- Physical specifications (dimensions, weight)
- Performance specifications
- Environmental limits
- Interface definitions
- Installation requirements
- Compliance and certification references

**Template Structure:**

```markdown
# Q100-61-DS-[COMPONENT] Data Sheet

## 1. General Description
[Component overview and purpose]

## 2. Physical Specifications
| Parameter | Value | Unit |
|-----------|-------|------|
| Length    | xxx   | mm   |
| Width     | xxx   | mm   |
| Height    | xxx   | mm   |
| Mass      | xxx   | kg   |

## 3. Performance Specifications
[Key performance parameters]

## 4. Environmental Limits
[Temperature, altitude, vibration, etc.]

## 5. Interface Definitions
[Mechanical, electrical, fluid interfaces]

## 6. Compliance
[Applicable standards and certifications]
```

**Use Cases:**

- Component specifications
- System interface documentation
- Procurement specifications
- Technical reference

### Technical Publications (TECHNICAL_PUBLICATIONS/)

**Maintenance and operational publications**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Standards            | ATA iSpec 2200, S1000D                   |
| Format               | SGML/XML source, PDF/HTML output         |
| Structure            | Per ATA chapter organization             |
| Naming               | `Q100-61-TP-[TYPE]-[COMPONENT].[ext]`    |

**Publication Types:**

| Code | Type                              | Description                          |
|------|-----------------------------------|--------------------------------------|
| CMM  | Component Maintenance Manual      | Component overhaul and repair        |
| IPC  | Illustrated Parts Catalog         | Parts identification and ordering    |
| AMM  | Aircraft Maintenance Manual       | Aircraft-level maintenance           |
| SRM  | Structural Repair Manual          | Structural damage repair             |
| ESPM | Engine Shop Manual                | Engine/propulsor shop procedures     |

**Publication Contents:**

- **CMM (Component Maintenance Manual):**
  - Description and operation
  - Removal and installation
  - Disassembly and assembly
  - Cleaning and inspection
  - Repair procedures
  - Testing and calibration
  - Illustrated parts breakdown

- **IPC (Illustrated Parts Catalog):**
  - System breakdown
  - Part number cross-reference
  - Effectivity information
  - Vendor/supplier data
  - Illustrated figures

**Use Cases:**

- Airline maintenance operations
- MRO facility procedures
- Spare parts ordering
- Regulatory compliance

## Naming Convention

All documentation exports follow:

```
Q100-61-[TYPE]-[COMPONENT]-[VARIANT].[ext]
```

### Documentation Type Codes

| Code | Type                    |
|------|-------------------------|
| PKG  | Drawing Package         |
| DS   | Data Sheet              |
| TP   | Technical Publication   |
| DWG  | Individual Drawing      |
| BOM  | Bill of Materials       |

### Examples

```
Q100-61-PKG-FPS-ASSY-R01.zip            → Full propulsor drawing package
Q100-61-DS-EMD-MOTOR-SPEC.md            → Motor specification data sheet
Q100-61-TP-CMM-GBX.xml                  → Gearbox component maintenance manual
Q100-61-TP-IPC-FAN.xml                  → Fan illustrated parts catalog
Q100-61-DWG-NAC-ASSY-001-A.pdf          → Nacelle assembly drawing
```

## Export Procedures

### Drawing Package Release

1. **Drawing Review**: Verify all drawings are checked and approved
2. **Manifest Creation**: Create YAML manifest in MANIFESTS/
3. **Package Assembly**: Collect drawings, BOMs, and notes
4. **Archive Creation**: Create ZIP with consistent structure
5. **Quality Check**: Verify package contents and manifest
6. **Release Notes**: Document changes from previous release

### Data Sheet Creation

1. **Template Selection**: Use standard data sheet template
2. **Content Population**: Fill in all specification sections
3. **Review**: Technical review for accuracy
4. **Approval**: Engineering approval
5. **Release**: Place in DATA_SHEETS/

### Technical Publication

1. **Source Preparation**: Create SGML/XML source per standard
2. **Illustration Preparation**: Create technical illustrations
3. **Validation**: Validate against DTD/schema
4. **Output Generation**: Generate PDF/HTML outputs
5. **Review Cycle**: Technical and editorial review
6. **Approval**: Publication approval per process

## Related Documentation

- [Q100-61-EXPORT-SETTINGS.yaml](../Q100-61-EXPORT-SETTINGS.yaml) - Export settings
- [../README.md](../README.md) - EXPORTS overview
- ATA iSpec 2200 - Technical publication standards
- S1000D - International specification for technical publications

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
