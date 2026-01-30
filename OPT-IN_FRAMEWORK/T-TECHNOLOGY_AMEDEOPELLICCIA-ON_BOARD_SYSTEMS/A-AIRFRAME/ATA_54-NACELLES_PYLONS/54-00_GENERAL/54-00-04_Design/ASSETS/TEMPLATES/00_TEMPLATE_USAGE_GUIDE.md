# ATA 54 Template Usage Guide

## Purpose

This guide provides comprehensive instructions for using the ATA Chapter 54 (Nacelles & Pylons) design templates. These templates ensure consistency, completeness, and traceability across all design documentation.

## Table of Contents

- [Overview](#overview)
- [Template Categories](#template-categories)
- [Getting Started](#getting-started)
- [Naming Conventions](#naming-conventions)
- [Using Each Template](#using-each-template)
- [Field Definitions](#field-definitions)
- [Common Mistakes](#common-mistakes)
- [Examples](#examples)
- [FAQ](#faq)

---

## Overview

The ATA 54 TEMPLATES folder contains standardized templates for all major asset categories used in nacelle and pylon design documentation. Using these templates ensures:

- **Consistency**: All documents follow the same structure
- **Completeness**: Required fields ensure nothing is missed
- **Traceability**: Built-in links to requirements, safety, and test data
- **Compliance**: Templates align with certification standards
- **Quality**: Peer review and approval processes are embedded

### Template Philosophy

- **Copy, don't edit**: Always copy the template to create new documents
- **Replace placeholders**: All `<PLACEHOLDER>` values must be replaced with actual data
- **Remove unused sections**: Sections marked `[OPTIONAL]` can be removed if not applicable
- **Maintain traceability**: Always link to requirements, drawings, and related documents
- **Update indexes**: Add new documents to `INDEX.meta.yaml`

---

## Template Categories

The templates are organized into 9 categories, each in its own subfolder:

| Category | Folder | Template ID | Format | Purpose |
|----------|--------|-------------|--------|---------|
| **Assemblies** | ASSEMBLIES/ | T801 | Markdown | Define assemblies (BOM level > part) |
| **Parts** | PARTS/ | T802 | YAML | Define individual parts |
| **Drawings** | DRAWINGS/ | T803 | YAML | Document engineering drawings |
| **Installations** | INSTALLATIONS/ | T804 | YAML | Define installation procedures |
| **Models** | MODELS/ | T805 | YAML | Document analysis models (FEA, CFD, etc.) |
| **Products** | PRODUCTS/ | T806 | YAML | Define product-level documentation |
| **Data Schemas** | DATA/ | T807 | JSON | Define data structures and schemas |
| **Traceability** | DATA/ | T808 | CSV | Track requirement-to-design traceability |
| **Interfaces** | INTERFACES/ | T809 | YAML | Define interface control documents |
| **Test Procedures** | TEST/ | T810 | YAML | Document test procedures |

---

## Getting Started

### Step 1: Choose the Right Template

Determine which type of asset you need to document:

- **Creating a new part?** → Use T802 (Part Template)
- **Documenting a drawing?** → Use T803 (Drawing Template)
- **Defining an assembly?** → Use T801 (Assembly Template)
- **Planning an installation?** → Use T804 (Installation Template)
- **Creating an analysis model?** → Use T805 (Model Template)
- **Defining a product?** → Use T806 (Product Template)
- **Creating a data schema?** → Use T807 (Data Schema Template)
- **Tracking requirements?** → Use T808 (Requirements Traceability Template)
- **Defining an interface?** → Use T809 (Interface Control Template)
- **Writing a test procedure?** → Use T810 (Test Procedure Template)

### Step 2: Copy the Template

Navigate to the appropriate subfolder and copy the template file:

```bash
cd ASSETS/TEMPLATES/<CATEGORY>/
cp 54-00-04-T80X_<Template_Name>.<ext> <new_filename>.<ext>
```

### Step 3: Rename According to Convention

Follow the naming convention for your asset type (see [Naming Conventions](#naming-conventions)).

### Step 4: Fill in the Template

- Replace all `<PLACEHOLDER>` values with actual data
- Remove sections marked `[OPTIONAL]` if not applicable
- Ensure all required fields are completed
- Add traceability links to requirements, safety items, and related documents

### Step 5: Update the Index

Add your new document to `ASSETS/INDEX.meta.yaml`:

```yaml
- id: "54-00-04-<ID>"
  category: "<CATEGORY>"
  title: "<Title>"
  source: "ASSETS/<CATEGORY>/<filename>.<ext>"
  exports: []
  links:
    reqs: ["<requirement-ids>"]
    odd: []
    safety: ["<safety-item-ids>"]
  status: "<Draft|Approved|Released>"
  version: "<X.Y.Z>"
  checksum: "<filled-by-CI>"
```

---

## Naming Conventions

All asset files follow a standardized naming pattern to ensure consistency and enable automated processing.

### General Pattern

```
54-00-04-<TYPE><NNN>_<CATEGORY>_<ShortName>.<ext>
```

Where:
- `54-00-04` = ATA chapter and lifecycle folder (Design)
- `<TYPE>` = Asset type prefix (see table below)
- `<NNN>` = Sequential number (001-999)
- `<CATEGORY>` = Category name in UPPERCASE
- `<ShortName>` = Brief descriptive name in PascalCase with underscores
- `<ext>` = File extension (yaml, json, csv, md)

### Type Prefixes by Category

| Category | Type Prefix | Example ID | Example Filename |
|----------|-------------|------------|------------------|
| Assembly | T | T801 | `54-00-04-T801_Assembly_Template.md` |
| Part | P | P001 | `54-00-04-P001_PART_Nacelle_Panel.yaml` |
| Drawing | D | D001 | `54-00-04-D001_DRWG_Nacelle_GA.yaml` |
| Installation | I | I001 | `54-00-04-I001_INST_Pylon_Installation.yaml` |
| Model | M | M701 | `54-00-04-M701_MODL_Stress_Analysis.yaml` |
| Product | PR | PR001 | `54-00-04-PR001_PROD_Nacelle_System.yaml` |
| Data Schema | DS | DS001 | `54-00-04-DS001_DATA_Assembly_Schema.json` |
| Traceability | RT | RT001 | `54-00-04-RT001_Requirements_Trace.csv` |
| Interface | IC | IC001 | `54-00-04-IC001_INTFC_Pylon_Wing.yaml` |
| Test Procedure | TP | TP001 | `54-00-04-TP001_TEST_Load_Test.yaml` |

### ID Number Ranges

Different asset types use different number ranges to avoid conflicts:

- **P001-P999**: Parts
- **D001-D099**: Drawings (general/GA)
- **D100-D199**: Drawings (detail)
- **D200-D299**: Drawings (interface)
- **D300-D399**: Drawings (installation)
- **D400-D499**: Drawings (section)
- **M001-M099**: Models (data schemas)
- **M100-M199**: Models (system)
- **M700-M799**: Models (structural analysis)
- **M800-M899**: Models (thermal analysis)
- **M900-M999**: Models (aero/CFD)
- **I001-I099**: Installations
- **IC001-IC099**: Interface Control Documents
- **TP001-TP099**: Test Procedures
- **T801-T899**: Templates (reserved range)

---

## Using Each Template

### T801: Assembly Template (Markdown)

**Location**: `ASSEMBLIES/54-00-04-T801_Assembly_Template.md`

**Purpose**: Define assemblies that consist of multiple parts or sub-assemblies.

**Key Sections**:
- `assembly_metadata`: Assembly identification and version control
- `components`: List of parts and sub-assemblies
- `assembly_sequence`: Step-by-step assembly instructions
- `tooling_required`: Special tools needed
- `quality_control`: Inspection and acceptance criteria
- `links`: Traceability to requirements, models, and procedures

**When to Use**:
- Creating a Bill of Materials (BOM) for a nacelle or pylon assembly
- Documenting how parts come together
- Defining assembly sequence and tooling

**Example**:
```yaml
assembly_id: "ASM-54-NAC-001"
assembly_name: "Nacelle Primary Structure Assembly"
ata_chapter: "54"
zone: "540-560"
```

---

### T802: Part Template (YAML)

**Location**: `PARTS/54-00-04-T802_Part_Template.yaml`

**Purpose**: Define individual parts (smallest design unit).

**Key Sections**:
- `part_metadata`: Part identification and classification
- `design`: Material, dimensions, tolerances
- `manufacturing`: Process, vendor, inspection
- `installation`: Mounting method, fasteners
- `maintenance`: Inspection intervals, replacement criteria
- `traceability`: Links to requirements, safety, drawings

**When to Use**:
- Documenting a new part design
- Specifying material and manufacturing requirements
- Defining part-level inspection and maintenance

**Example**:
```yaml
id: "54-00-04-P001"
part_number: "54-NAC-1001-01"
material:
  primary: "CFRP-Epoxy"
mass_kg: 12.5
```

---

### T803: Drawing Template (YAML)

**Location**: `DRAWINGS/54-00-04-T803_Drawing_Template.yaml`

**Purpose**: Document engineering drawings and their metadata.

**Key Sections**:
- `drawing_metadata`: Drawing number, revision, type, scale
- `subject`: What the drawing depicts
- `content`: Views, dimensions, notes
- `specifications`: Materials, tolerances, GD&T
- `references`: Related drawings and documents
- `change_control`: Revision history

**When to Use**:
- Creating metadata for a new engineering drawing
- Documenting drawing relationships and dependencies
- Tracking drawing revisions

**Example**:
```yaml
id: "54-00-04-D001"
drawing_number: "54-00-0001"
drawing_type: "GA"
scale: "1:10"
```

---

### T804: Installation Template (YAML)

**Location**: `INSTALLATIONS/54-00-04-T804_Installation_Template.yaml`

**Purpose**: Define installation procedures for assemblies and systems.

**Key Sections**:
- `installation_metadata`: Installation identification
- `scope`: Components being installed
- `location_details`: Physical location coordinates
- `procedure`: Step-by-step installation instructions
- `mounting`: Attachment methods and fasteners
- `routing`: Electrical, hydraulic, pneumatic routing
- `inspection`: Post-installation checks

**When to Use**:
- Creating installation procedures for production or maintenance
- Defining mounting and routing requirements
- Specifying tooling and skill requirements

**Example**:
```yaml
id: "54-00-04-I001"
installation_id: "INST-54-PYL-001"
nomenclature: "Pylon-Wing Installation"
```

---

### T805: Model Template (YAML)

**Location**: `MODELS/54-00-04-T805_Model_Template.yaml`

**Purpose**: Document analysis models (FEA, CFD, thermal, etc.).

**Key Sections**:
- `model_metadata`: Model identification and type
- `scope`: What is being analyzed
- `description`: Governing equations, assumptions, limitations
- `geometry`: CAD source and idealization
- `mesh`: Element types, mesh quality
- `materials`: Material properties
- `boundary_conditions`: Loads, constraints, thermal/flow conditions
- `analysis_settings`: Solver, convergence criteria
- `results`: Outputs, margins of safety
- `validation`: Validation method and results

**When to Use**:
- Documenting a structural analysis (FEA)
- Recording a thermal analysis
- Defining an aerodynamic model (CFD)
- Creating a dynamics or vibration analysis

**Example**:
```yaml
id: "54-00-04-M701"
model_type: "Structural"
analysis_type: "FEA"
solver: "ANSYS Mechanical 2023R1"
```

---

### T806: Product Template (YAML)

**Location**: `PRODUCTS/54-00-04-T806_Product_Template.yaml`

**Purpose**: Define top-level product documentation (nacelle, pylon, system).

**Key Sections**:
- `product_metadata`: Product identification and classification
- `description`: Purpose, features, capabilities
- `structure`: Top-level assemblies and major components
- `specifications`: Physical, performance, environmental specs
- `interfaces`: Structural, electrical, hydraulic, data interfaces
- `quality`: Quality level, inspection, certification basis
- `maintenance`: Scheduled maintenance, spares philosophy
- `configuration`: Baseline, variants, optional equipment

**When to Use**:
- Defining a complete nacelle or pylon product
- Documenting product-level specifications
- Creating a product baseline for configuration control

**Example**:
```yaml
id: "54-00-04-PR001"
product_type: "Nacelle"
variant: "Standard"
total_mass_kg: 1250.0
```

---

### T807: Data Schema Template (JSON)

**Location**: `DATA/54-00-04-T807_Data_Schema_Template.json`

**Purpose**: Define structured data schemas using JSON Schema.

**Key Sections**:
- `metadata`: Schema identification and version
- `definitions`: Reusable schema components
- `properties`: Main schema structure
- `required`: Required fields
- `examples`: Example data instances

**When to Use**:
- Defining data structures for APIs or data exchange
- Creating validation schemas for part/assembly data
- Standardizing data formats across the project

**Example**:
```json
{
  "id": "54-00-04-DS001",
  "title": "Assembly Data Schema",
  "type": "object",
  "properties": {
    "assembly_id": {"type": "string"},
    "mass_kg": {"type": "number"}
  }
}
```

---

### T808: Requirements Traceability Template (CSV)

**Location**: `DATA/54-00-04-T808_Requirements_Traceability_Template.csv`

**Purpose**: Track requirement-to-design traceability.

**Key Columns**:
- `Requirement_ID`: Unique requirement identifier
- `Requirement_Title`: Short title
- `Requirement_Type`: Functional, Performance, Safety, etc.
- `Design_Element_ID`: ID of design element satisfying requirement
- `Design_Element_Type`: PART, DRWG, ASSY, MODL, INST, PROD
- `Verification_Method`: Analysis, Test, Inspection, Demo
- `Verification_Status`: Not-Started, In-Progress, Complete
- `Safety_Impact`: None, Minor, Major, Hazardous, Catastrophic
- `Compliance_Basis`: CS-25.xxx or other regulation

**When to Use**:
- Tracking how requirements are satisfied by design elements
- Creating a Requirements Traceability Matrix (RTM)
- Preparing for certification audits

**Example**:
```csv
Requirement_ID,Design_Element_ID,Design_Element_Type,Verification_Method,Status
54-00-03-01-001,54-00-04-P001,PART,Test,Complete
54-00-03-01-002,ASM-54-NAC-001,ASSY,Inspection,In-Progress
```

---

### T809: Interface Control Template (YAML)

**Location**: `INTERFACES/54-00-04-T809_Interface_Control_Template.yaml`

**Purpose**: Define interfaces between systems and components.

**Key Sections**:
- `interface_metadata`: Interface identification
- `parties`: Side A and Side B components
- `description`: Purpose, functional description
- `physical`: Geometry, mounting, load transfer, clearances
- `electrical`: Power, signals, connectors, grounding
- `hydraulic`: Pressure, flow, fluid type, connections
- `pneumatic`: Pressure, flow, gas type
- `data`: Protocol, data rate, message structure
- `thermal`: Heat transfer, temperatures
- `control`: Baseline, change control, verification

**When to Use**:
- Defining interfaces between nacelle/pylon and wing
- Documenting interfaces with engine or thrust reverser
- Creating Interface Control Documents (ICDs)

**Example**:
```yaml
id: "54-00-04-IC001"
interface_id: "ICD-54-PYL-001"
interface_type: "Structural"
side_a:
  component_name: "Pylon Forward Attachment"
side_b:
  component_name: "Wing Front Spar"
```

---

### T810: Test Procedure Template (YAML)

**Location**: `TEST/54-00-04-T810_Test_Procedure_Template.yaml`

**Purpose**: Document test procedures for verification and validation.

**Key Sections**:
- `test_metadata`: Test identification and type
- `objective`: Purpose, goals, success/failure criteria
- `test_article`: What is being tested
- `requirements_verified`: List of requirements verified by this test
- `setup`: Test facility, fixtures, equipment, instrumentation
- `safety`: Hazards, PPE, emergency procedures
- `prerequisites`: Pre-test checks
- `procedure`: Step-by-step test instructions
- `test_conditions`: Load cases, environmental conditions
- `acceptance`: Pass/fail criteria

**When to Use**:
- Creating test procedures for structural testing
- Documenting environmental testing procedures
- Defining functional or performance test procedures

**Example**:
```yaml
id: "54-00-04-TP001"
procedure_id: "TP-54-NAC-001"
test_type: "Qualification"
test_level: "Assembly"
test_method: "Structural"
```

---

## Field Definitions

### Common Fields Across Templates

- **id**: Unique identifier for the document (e.g., `54-00-04-P001`)
- **title**: Human-readable title
- **category**: Asset category (PART, DRWG, ASSY, MODL, INST, PROD, DATA, INTFC, TEST)
- **ata_chapter**: Always "54" for this chapter
- **status**: Document status
  - `Draft`: Under development
  - `Preliminary`: Initial review complete
  - `Released`: Officially released for use
  - `Superseded`: Replaced by newer version
  - `Obsolete`: No longer valid
- **version**: Semantic version (major.minor or major.minor.patch)
- **created_date**: Date created (YYYY-MM-DD)
- **last_updated**: Date of last update (YYYY-MM-DD)
- **author**: Person or team who created the document

### Traceability Fields

- **requirements**: List of requirement IDs (e.g., `54-00-03-01-001`)
- **safety_items**: List of safety analysis IDs (e.g., `54-00-02-20-001`)
- **drawings**: List of drawing IDs (e.g., `54-00-04-D001`)
- **test_procedures**: List of test procedure IDs (e.g., `54-00-07-01-001`)
- **certification_basis**: List of regulatory references (e.g., `CS-25.601`)

### Design Fields

- **material**: Material specification (e.g., `CFRP-Epoxy`, `Al-7075-T73`, `Ti-6Al-4V`)
- **dimensions**: Length, width, height in millimeters
- **mass_kg**: Mass in kilograms
- **tolerance**: Dimensional tolerance (e.g., `±0.1 mm`)
- **zone**: Aircraft zone designation (e.g., `540-560`)

### Quality & Compliance Fields

- **inspection_method**: Visual, NDT, CMM, Load-Test, etc.
- **quality_level**: DAL-A, DAL-B, DAL-C, DAL-D, DAL-E (per DO-178C/DO-254)
- **safety_classification**: Catastrophic, Hazardous, Major, Minor, None
- **certification_basis**: CS-25.xxx, FAR 25.xxx, etc.

---

## Common Mistakes

### 1. Not Replacing Placeholders

**Mistake**: Leaving `<PLACEHOLDER>` values in the document.

**Correct**: Replace all placeholders with actual data:
```yaml
# Wrong:
part_number: "<PART-NUMBER>"

# Right:
part_number: "54-NAC-1001-01"
```

### 2. Inconsistent ID Numbering

**Mistake**: Using conflicting or duplicate IDs.

**Correct**: Check existing IDs in `INDEX.meta.yaml` before assigning new ones:
```bash
grep "id:" ASSETS/INDEX.meta.yaml | grep "54-00-04-P"
```

### 3. Breaking Traceability Links

**Mistake**: Referencing non-existent requirements or documents.

**Correct**: Verify that all linked documents exist:
```yaml
# Ensure these IDs exist in their respective folders:
traceability:
  requirements:
    - "54-00-03-01-001"  # Must exist in 54-00-03_Requirements
  drawings:
    - "54-00-04-D001"    # Must exist in ASSETS/DRAWINGS
```

### 4. Wrong File Extension

**Mistake**: Using `.md` for YAML templates or vice versa.

**Correct**: Match the extension to the template format:
- T801 (Assembly) → `.md` (Markdown)
- T802-T806, T809-T810 → `.yaml` (YAML)
- T807 → `.json` (JSON Schema)
- T808 → `.csv` (CSV)

### 5. Not Updating INDEX.meta.yaml

**Mistake**: Creating a new document but forgetting to add it to the index.

**Correct**: Always update `ASSETS/INDEX.meta.yaml` after creating a new document.

### 6. Leaving Optional Sections Empty

**Mistake**: Leaving `[OPTIONAL]` sections with no data or comments.

**Correct**: Either fill in the optional section or remove it entirely:
```yaml
# Wrong:
thermal_analysis:  # [OPTIONAL]

# Right (if not applicable):
# Remove the entire 'thermal_analysis' section

# Right (if applicable):
thermal_analysis:
  max_temp_c: 150
  heat_flux_w_m2: 5000
```

### 7. Inconsistent Units

**Mistake**: Mixing metric and imperial units.

**Correct**: Use metric (SI) units throughout:
- Length: millimeters (mm)
- Mass: kilograms (kg)
- Pressure: pascals (Pa) or bar
- Temperature: Celsius (°C)
- Force: newtons (N)

### 8. Missing Document Control

**Mistake**: Not filling in the `document_control` section.

**Correct**: Always complete version, status, dates, and authors:
```yaml
document_control:
  version: "1.0"
  status: "Draft"
  created_date: "2026-01-07"
  last_updated: "2026-01-07"
  author: "Design Team"
```

---

## Examples

### Example 1: Creating a New Part

**Scenario**: You need to document a new nacelle panel part.

**Steps**:

1. **Copy the template**:
   ```bash
   cd ASSETS/TEMPLATES/PARTS/
   cp 54-00-04-T802_Part_Template.yaml ../../PARTS/54-00-04-P012_PART_Nacelle_Panel.yaml
   ```

2. **Edit the file**:
   ```yaml
   id: "54-00-04-P012"
   title: "Nacelle Upper Panel"
   category: "PART"
   ata_chapter: "54"
   
   part_metadata:
     part_number: "54-NAC-1012-01"
     ci_number: "CI-54-NAC-001"
     nomenclature: "Nacelle Upper Aerodynamic Panel"
     zone: "540-550"
     drawing_reference: "54-00-0012"
     revision: "A"
     status: "Preliminary"
     plm_item_id: "TC-PART-54-NAC-012"
   
   design:
     material:
       primary: "CFRP-Epoxy"
       coating: "Polyurethane Paint"
       finish: "Smooth, Ra 1.6"
     dimensions:
       length_mm: 1200.0
       width_mm: 800.0
       height_mm: 5.0
       mass_kg: 8.5
   ```

3. **Update INDEX.meta.yaml**:
   ```yaml
   - id: "54-00-04-P012"
     category: "PART"
     title: "Nacelle Upper Panel"
     source: "ASSETS/PARTS/54-00-04-P012_PART_Nacelle_Panel.yaml"
     status: "Preliminary"
     version: "1.0"
   ```

---

### Example 2: Creating a Traceability Matrix

**Scenario**: You need to track which design elements satisfy which requirements.

**Steps**:

1. **Copy the template**:
   ```bash
   cd ASSETS/TEMPLATES/DATA/
   cp 54-00-04-T808_Requirements_Traceability_Template.csv ../../DATA/54-00-04-RT001_Structural_Requirements_Trace.csv
   ```

2. **Edit the CSV** (replace example rows with actual data):
   ```csv
   Requirement_ID,Requirement_Title,Requirement_Type,Priority,Status,Parent_Requirement,Design_Element_ID,Design_Element_Type,Design_Element_Title,Verification_Method,Verification_Status,Test_Procedure_ID,Safety_Impact,Safety_Reference,Compliance_Basis,Notes
   54-00-03-01-001,Ultimate Load Capability,Performance,High,Approved,N/A,54-00-04-M701,MODL,Nacelle Stress Analysis,Analysis,Complete,N/A,Major,54-00-02-20-001,CS-25.601,FEA shows margin > 0.15
   54-00-03-01-002,Material Qualification,Regulatory,High,Approved,N/A,54-00-04-P001,PART,Primary Structure Panel,Test,In-Progress,54-00-07-01-005,Major,54-00-02-20-001,CS-25.603,Material testing underway
   ```

3. **Update INDEX.meta.yaml**.

---

### Example 3: Creating an Interface Control Document

**Scenario**: You need to define the interface between pylon and wing.

**Steps**:

1. **Copy the template**:
   ```bash
   cd ASSETS/TEMPLATES/INTERFACES/
   cp 54-00-04-T809_Interface_Control_Template.yaml ../../INTERFACES/54-00-04-IC001_INTFC_Pylon_Wing.yaml
   ```

2. **Edit the file**:
   ```yaml
   id: "54-00-04-IC001"
   title: "Pylon-Wing Interface"
   category: "INTFC"
   
   interface_metadata:
     interface_id: "ICD-54-PYL-001"
     interface_name: "Pylon-Wing Structural Interface"
     interface_type: "Structural"
     icd_number: "ICD-54-00-0001"
     revision: "A"
     status: "Preliminary"
   
   parties:
     side_a:
       component_id: "ASM-54-PYL-001"
       component_name: "Pylon Forward Attachment"
       ata_chapter: "54"
       owner: "Structures Team"
     side_b:
       component_id: "57-00-04-A001"
       component_name: "Wing Front Spar"
       ata_chapter: "57"
       owner: "Wing Structures Team"
   ```

3. **Update INDEX.meta.yaml**.

---

## FAQ

### Q1: Can I create my own templates?

**A**: Yes, but only if absolutely necessary. The provided templates cover the vast majority of use cases. If you need a custom template:
1. Discuss with the design team first
2. Base it on an existing template structure
3. Follow the same naming conventions
4. Add it to the appropriate subfolder
5. Update this guide

### Q2: What if a field doesn't apply to my document?

**A**: If a section is marked `[OPTIONAL]`, you can remove it entirely. For required fields that truly don't apply, use:
- `N/A` for text fields
- `0` or `0.0` for numeric fields where zero makes sense
- Empty array `[]` for lists

### Q3: How do I handle revisions?

**A**: Update these fields in `document_control`:
```yaml
document_control:
  version: "1.1"  # Increment version
  last_updated: "2026-01-15"  # Update date
  change_history:
    - version: "1.1"
      date: "2026-01-15"
      author: "Jane Doe"
      changes: "Updated mass calculation per test results"
    - version: "1.0"
      date: "2026-01-07"
      author: "John Smith"
      changes: "Initial release"
```

### Q4: Can I use a different format (e.g., Excel instead of CSV)?

**A**: No. The templates specify exact formats for a reason:
- **YAML**: Human-readable, version-control friendly, supports comments
- **JSON**: Machine-parsable, schema validation
- **CSV**: Universal, easy to import/export
- **Markdown**: Rich text, documentation-friendly

Changing formats breaks automated tooling and CI validation.

### Q5: What if I don't know a value yet?

**A**: Use explicit placeholders with TODO comments:
```yaml
mass_kg: 0.0  # TODO: Update after CAD model finalized
test_date: "TBD"  # TODO: Schedule with test lab
```

Never leave template `<PLACEHOLDER>` syntax in production documents.

### Q6: How do I link to external documents?

**A**: Use the appropriate ID reference system:
- Requirements: `54-00-03-XX-NNN`
- Safety items: `54-00-02-XX-NNN`
- Drawings: `54-00-04-DNNN`
- Other ATA chapters: `XX-YY-ZZ-NNN`

For truly external documents (vendor specs, standards), use full references:
```yaml
references:
  external:
    - "AMS-3850 Rev D: CFRP Material Specification"
    - "CS-25.601: Structural Design Requirements"
```

### Q7: Who approves these documents?

**A**: Depends on the document type and lifecycle stage:
- **Draft**: Author and peer reviewer
- **Preliminary**: Technical lead
- **Released**: Design authority and quality assurance
- **Certification**: Certification engineer sign-off required

Always fill in the `approver` field in `document_control`.

### Q8: How do I handle variants or configurations?

**A**: Create separate documents for significantly different variants:
```
54-00-04-P001_PART_Panel_Standard.yaml
54-00-04-P002_PART_Panel_Extended.yaml
```

For minor variations, use a single document with a `variants` or `options` section:
```yaml
variants:
  - variant: "Standard"
    mass_kg: 8.5
  - variant: "Reinforced"
    mass_kg: 9.2
```

---

## Document Control

- **Version**: 1.0
- **Status**: Active
- **Created**: 2026-01-07
- **Author**: AMPEL360 ATA 54 Design Team
- **Last Updated**: 2026-01-07
- **Standard**: AMPEL360 ASSETS Standard v1.0

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-07 | AMPEL360 Design Team | Initial release |

---

**For questions or clarifications, contact the ATA 54 Design Team.**
