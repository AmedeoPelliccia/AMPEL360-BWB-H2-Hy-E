# ATA 54 Templates Index

## Overview

This folder contains standardized templates for all asset categories in ATA Chapter 54 (Nacelles & Pylons) design documentation. Templates ensure consistency, completeness, and traceability across the project.

**Location**: `54-00-04_Design/ASSETS/TEMPLATES/`

---

## Quick Links

- **[Template Usage Guide](00_TEMPLATE_USAGE_GUIDE.md)** - Comprehensive instructions for using templates
- **[Parent ASSETS Folder](../)** - Main assets directory
- **[INDEX.meta.yaml](../INDEX.meta.yaml)** - Authoritative asset catalog

---

## Folder Structure

```
TEMPLATES/
├── 00_INDEX.md                          # This file
├── 00_TEMPLATE_USAGE_GUIDE.md           # Comprehensive usage guide
├── ASSEMBLIES/                          # Assembly templates
│   └── 54-00-04-T801_Assembly_Template.md
├── PARTS/                               # Part templates
│   └── 54-00-04-T802_Part_Template.yaml
├── DRAWINGS/                            # Drawing templates
│   └── 54-00-04-T803_Drawing_Template.yaml
├── INSTALLATIONS/                       # Installation templates
│   └── 54-00-04-T804_Installation_Template.yaml
├── MODELS/                              # Model templates
│   └── 54-00-04-T805_Model_Template.yaml
├── PRODUCTS/                            # Product templates
│   └── 54-00-04-T806_Product_Template.yaml
├── DATA/                                # Data & traceability templates
│   ├── 54-00-04-T807_Data_Schema_Template.json
│   └── 54-00-04-T808_Requirements_Traceability_Template.csv
├── INTERFACES/                          # Interface control templates
│   └── 54-00-04-T809_Interface_Control_Template.yaml
└── TEST/                                # Test procedure templates
    └── 54-00-04-T810_Test_Procedure_Template.yaml
```

---

## Template Register

### Summary

| Template ID | Category | Format | Status | Version | Last Updated |
|-------------|----------|--------|--------|---------|--------------|
| T801 | Assembly | Markdown | Active | 1.0 | 2026-01-02 |
| T802 | Part | YAML | Active | 1.0 | 2026-01-07 |
| T803 | Drawing | YAML | Active | 1.0 | 2026-01-07 |
| T804 | Installation | YAML | Active | 1.0 | 2026-01-07 |
| T805 | Model | YAML | Active | 1.0 | 2026-01-07 |
| T806 | Product | YAML | Active | 1.0 | 2026-01-07 |
| T807 | Data Schema | JSON | Active | 1.0 | 2026-01-07 |
| T808 | Requirements Traceability | CSV | Active | 1.0 | 2026-01-07 |
| T809 | Interface Control | YAML | Active | 1.0 | 2026-01-07 |
| T810 | Test Procedure | YAML | Active | 1.0 | 2026-01-07 |

**Total Templates**: 10

---

## Detailed Template Information

### T801: Assembly Template

- **ID**: 54-00-04-T801
- **File**: `ASSEMBLIES/54-00-04-T801_Assembly_Template.md`
- **Format**: Markdown
- **Category**: ASSY
- **Purpose**: Define assemblies consisting of multiple parts or sub-assemblies
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-02
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Assembly metadata and identification
- Component list with quantities and specifications
- Assembly sequence and tooling requirements
- Quality control and inspection criteria
- Traceability to requirements and drawings

**Use Cases**:
- Creating Bill of Materials (BOM)
- Documenting assembly procedures
- Defining tooling and quality checkpoints

---

### T802: Part Template

- **ID**: 54-00-04-T802
- **File**: `PARTS/54-00-04-T802_Part_Template.yaml`
- **Format**: YAML
- **Category**: PART
- **Purpose**: Define individual parts (smallest design unit)
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Part identification and classification
- Material, dimensions, and tolerances
- Manufacturing process and vendor info
- Installation and mounting details
- Maintenance intervals and lifecycle
- Comprehensive traceability

**Use Cases**:
- Documenting new part designs
- Specifying material requirements
- Defining inspection and maintenance criteria

---

### T803: Drawing Template

- **ID**: 54-00-04-T803
- **File**: `DRAWINGS/54-00-04-T803_Drawing_Template.yaml`
- **Format**: YAML
- **Category**: DRWG
- **Purpose**: Document engineering drawings and their metadata
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Drawing identification (number, revision, type)
- Content description (views, dimensions, notes)
- Material callouts and GD&T specifications
- Related drawings and references
- Change control and revision history

**Use Cases**:
- Creating drawing metadata
- Documenting drawing relationships
- Tracking revisions and changes

---

### T804: Installation Template

- **ID**: 54-00-04-T804
- **File**: `INSTALLATIONS/54-00-04-T804_Installation_Template.yaml`
- **Format**: YAML
- **Category**: INST
- **Purpose**: Define installation procedures for assemblies and systems
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Installation scope and location details
- Step-by-step installation procedures
- Mounting and attachment specifications
- Routing (electrical, hydraulic, pneumatic)
- Tooling requirements and skill levels
- Inspection and testing requirements

**Use Cases**:
- Creating installation procedures
- Defining mounting requirements
- Specifying routing and connections

---

### T805: Model Template

- **ID**: 54-00-04-T805
- **File**: `MODELS/54-00-04-T805_Model_Template.yaml`
- **Format**: YAML
- **Category**: MODL
- **Purpose**: Document analysis models (FEA, CFD, thermal, etc.)
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Model identification and analysis type
- Geometry, mesh, and material properties
- Boundary conditions and loads
- Analysis settings and solver configuration
- Results, margins of safety
- Validation and verification

**Use Cases**:
- Documenting structural analyses (FEA)
- Recording thermal analyses
- Defining aerodynamic models (CFD)
- Creating dynamics/vibration analyses

---

### T806: Product Template

- **ID**: 54-00-04-T806
- **File**: `PRODUCTS/54-00-04-T806_Product_Template.yaml`
- **Format**: YAML
- **Category**: PROD
- **Purpose**: Define top-level product documentation (nacelle, pylon, system)
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Product identification and classification
- Key features and capabilities
- Top-level structure (assemblies, components)
- Physical, performance, and environmental specs
- Interface definitions (structural, electrical, hydraulic, data)
- Quality, certification, and maintenance
- Configuration management and variants

**Use Cases**:
- Defining complete nacelle or pylon products
- Documenting product-level specifications
- Creating configuration baselines

---

### T807: Data Schema Template

- **ID**: 54-00-04-T807
- **File**: `DATA/54-00-04-T807_Data_Schema_Template.json`
- **Format**: JSON (JSON Schema Draft 07)
- **Category**: DATA
- **Purpose**: Define structured data schemas for validation and data exchange
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- JSON Schema format (machine-readable)
- Reusable definitions section
- Type definitions and constraints
- Required vs. optional fields
- Validation rules
- Example data instances

**Use Cases**:
- Defining data structures for APIs
- Creating validation schemas for part/assembly data
- Standardizing data formats

---

### T808: Requirements Traceability Template

- **ID**: 54-00-04-T808
- **File**: `DATA/54-00-04-T808_Requirements_Traceability_Template.csv`
- **Format**: CSV
- **Category**: DATA
- **Purpose**: Track requirement-to-design traceability
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Requirement identification and classification
- Design element mapping (PART, DRWG, ASSY, MODL, etc.)
- Verification method and status tracking
- Safety impact classification
- Compliance basis (CS-25, etc.)
- Comprehensive field definitions

**Use Cases**:
- Creating Requirements Traceability Matrices (RTM)
- Tracking requirement satisfaction
- Preparing for certification audits

---

### T809: Interface Control Template

- **ID**: 54-00-04-T809
- **File**: `INTERFACES/54-00-04-T809_Interface_Control_Template.yaml`
- **Format**: YAML
- **Category**: INTFC
- **Purpose**: Define interfaces between systems and components
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Interface identification and parties (Side A, Side B)
- Physical interface (geometry, mounting, loads)
- Electrical interface (power, signals, connectors)
- Hydraulic/pneumatic interfaces
- Data interface (protocols, messages)
- Thermal interface
- Change control and verification

**Use Cases**:
- Creating Interface Control Documents (ICDs)
- Defining interfaces between nacelle/pylon and wing
- Documenting interfaces with engine or thrust reverser

---

### T810: Test Procedure Template

- **ID**: 54-00-04-T810
- **File**: `TEST/54-00-04-T810_Test_Procedure_Template.yaml`
- **Format**: YAML
- **Category**: TEST
- **Purpose**: Document test procedures for verification and validation
- **Status**: Active
- **Version**: 1.0
- **Last Updated**: 2026-01-07
- **Owner**: AMPEL360 ATA 54 Design Team

**Key Features**:
- Test identification and objectives
- Test article description
- Requirements being verified
- Test setup (facility, equipment, instrumentation)
- Safety precautions and personnel
- Step-by-step test procedure
- Data recording and acceptance criteria
- Post-test actions and analysis

**Use Cases**:
- Creating structural test procedures
- Documenting environmental test procedures
- Defining functional/performance test procedures

---

## Template Coverage Matrix

| Asset Category | Template ID | Folder | Completeness | Notes |
|----------------|-------------|--------|--------------|-------|
| Assemblies | T801 | ASSEMBLIES/ | ✅ Complete | Markdown format, established template |
| Parts | T802 | PARTS/ | ✅ Complete | YAML format, comprehensive fields |
| Drawings | T803 | DRAWINGS/ | ✅ Complete | YAML format, supports all drawing types |
| Installations | T804 | INSTALLATIONS/ | ✅ Complete | YAML format, routing and tooling |
| Models | T805 | MODELS/ | ✅ Complete | YAML format, FEA/CFD/thermal/aero |
| Products | T806 | PRODUCTS/ | ✅ Complete | YAML format, product-level specs |
| Data Schemas | T807 | DATA/ | ✅ Complete | JSON Schema format, validation ready |
| Traceability | T808 | DATA/ | ✅ Complete | CSV format, RTM support |
| Interfaces | T809 | INTERFACES/ | ✅ Complete | YAML format, ICD support |
| Test Procedures | T810 | TEST/ | ✅ Complete | YAML format, V&V procedures |

**Coverage**: 10/10 categories (100%)

---

## How to Use Templates

### Quick Start

1. **Choose the right template** for your asset type
2. **Copy the template** to the appropriate asset folder (not the TEMPLATES folder)
3. **Rename** following the naming convention
4. **Fill in** all required fields, replacing `<PLACEHOLDER>` values
5. **Remove** sections marked `[OPTIONAL]` if not applicable
6. **Add traceability** links to requirements, safety items, and related documents
7. **Update** `../INDEX.meta.yaml` with the new asset entry

### Detailed Instructions

See **[00_TEMPLATE_USAGE_GUIDE.md](00_TEMPLATE_USAGE_GUIDE.md)** for:
- Step-by-step instructions
- Naming conventions
- Field definitions
- Common mistakes to avoid
- Complete examples

### Example Workflow

```bash
# 1. Navigate to templates
cd ASSETS/TEMPLATES/PARTS/

# 2. Copy template
cp 54-00-04-T802_Part_Template.yaml ../../PARTS/54-00-04-P012_PART_Nacelle_Panel.yaml

# 3. Edit the file
vim ../../PARTS/54-00-04-P012_PART_Nacelle_Panel.yaml

# 4. Update index
vim ../../INDEX.meta.yaml
```

---

## Naming Conventions

### General Pattern

```
54-00-04-<TYPE><NNN>_<CATEGORY>_<ShortName>.<ext>
```

### Type Prefixes

- **T**: Template (T801-T899)
- **P**: Part (P001-P999)
- **D**: Drawing (D001-D499)
- **M**: Model (M001-M999)
- **I**: Installation (I001-I099)
- **PR**: Product (PR001-PR099)
- **DS**: Data Schema (DS001-DS099)
- **RT**: Requirements Traceability (RT001-RT099)
- **IC**: Interface Control (IC001-IC099)
- **TP**: Test Procedure (TP001-TP099)

### File Extensions

- **`.yaml`**: YAML format (most templates)
- **`.json`**: JSON Schema format (T807)
- **`.csv`**: CSV format (T808)
- **`.md`**: Markdown format (T801)

---

## Maintenance & Updates

### Template Maintenance

- **Owner**: AMPEL360 ATA 54 Design Team
- **Review Cycle**: Quarterly
- **Change Control**: All template changes require design team approval
- **Version Control**: Templates use semantic versioning (major.minor.patch)

### Requesting Template Updates

To request an update or new template:

1. Submit an issue to the documentation team
2. Include:
   - Reason for change/addition
   - Affected use cases
   - Proposed changes
3. Design team will review and approve/reject
4. If approved, update this index and the usage guide

### Template Deprecation

When deprecating a template:

1. Update status to "Deprecated"
2. Add deprecation notice with alternative template
3. Keep template file for historical reference
4. Remove from "Active Templates" list
5. Update usage guide

---

## Related Documents

- **[ASSETS README](../README.md)** - Main assets folder documentation
- **[INDEX.meta.yaml](../INDEX.meta.yaml)** - Authoritative asset catalog
- **[AMPEL360 ASSETS Standard](../../../../../../../AMPEL360_ASSETS_STANDARD.md)** - Organization-wide asset standard
- **[54-00-04 Design README](../../README.md)** - Design folder overview

---

## Support & Contacts

### Questions About Templates

- **Design Team**: ata54-design@ampel360.com
- **Documentation Team**: docs@ampel360.com

### Reporting Issues

- **Template Errors**: Submit issue with "Template" label
- **Usage Questions**: Contact design team or consult usage guide
- **Feature Requests**: Submit enhancement request

---

## Statistics

- **Total Templates**: 10
- **Active Templates**: 10
- **Deprecated Templates**: 0
- **Template Coverage**: 100%
- **Last Inventory**: 2026-01-07

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-07 | AMPEL360 Design Team | Initial template set with all 10 templates |
| 0.1 | 2026-01-02 | AMPEL360 Design Team | Initial structure with T801 only |

---

## Document Control

- **Document ID**: 54-00-04-TMPL-INDEX
- **Version**: 1.0
- **Status**: Active
- **Created**: 2026-01-07
- **Last Updated**: 2026-01-07
- **Author**: AMPEL360 ATA 54 Design Team
- **Owner**: AMPEL360 Documentation WG
- **Standard**: AMPEL360 ASSETS Standard v1.0

---

**END OF TEMPLATES INDEX**
