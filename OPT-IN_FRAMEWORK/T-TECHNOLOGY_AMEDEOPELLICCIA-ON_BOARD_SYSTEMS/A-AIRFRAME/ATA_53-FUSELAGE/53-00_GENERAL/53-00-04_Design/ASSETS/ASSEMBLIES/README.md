# ASSEMBLIES — ATA 53 Fuselage

## Purpose

This directory contains **assembly-level definitions** for the AMPEL360 BWB-H2-Hy-E fuselage structure. Each assembly sits between:

- **CI-level design** in `53-00-04_Design/02_Configuration_Items/…`
- **Detailed structural analysis** in `53-50_Structures/…`

Assemblies provide the **integration layer** that combines multiple Configuration Items (CIs) into cohesive structural units ready for manufacturing, testing, and certification.

---

## Directory Structure

```text
ASSEMBLIES/
├── README.md                          # This file
│
├── NOSE_SECTION_ASSEMBLY/             # Zone 100: Forward fuselage
│   ├── ASM-53-100-001_Forward_Bulkhead_Assembly.yaml
│   ├── ASM-53-100-002_NLG_Bay_Assembly.yaml
│   ├── ASM-53-100-003_Cockpit_Structure_Assembly.yaml
│   └── Bill_of_Materials.csv
│
├── PRESSURE_SHELL_ASSEMBLIES/         # Zones 200-300: Main cabin structure
│   ├── ASM-53-200-001_Upper_Shell_Module.yaml
│   ├── ASM-53-200-002_Lower_Shell_Module.yaml
│   ├── ASM-53-300-001_Side_Shell_Left.yaml
│   ├── ASM-53-300-002_Side_Shell_Right.yaml
│   └── Assembly_Sequence.md
│
├── FLOOR_ASSEMBLIES/                  # Cabin floor structure
│   ├── ASM-53-FLOOR-001_Primary_Beam_Grid.yaml
│   ├── ASM-53-FLOOR-002_Floor_Panels.yaml
│   ├── ASM-53-FLOOR-003_Seat_Track_Assembly.yaml
│   └── Load_Transfer_Analysis.csv
│
├── DOOR_FRAME_ASSEMBLIES/             # All door structures (12 total)
│   ├── ASM-53-200-DOOR-1L_Passenger_Door_1L.yaml
│   ├── ASM-53-200-DOOR-1R_Passenger_Door_1R.yaml
│   ├── ASM-53-200-DOOR-2L_Passenger_Door_2L.yaml
│   ├── ASM-53-200-DOOR-2R_Passenger_Door_2R.yaml
│   ├── ASM-53-300-DOOR-3L_Passenger_Door_3L.yaml
│   ├── ASM-53-300-DOOR-3R_Passenger_Door_3R.yaml
│   ├── ASM-53-300-DOOR-4L_Passenger_Door_4L.yaml
│   ├── ASM-53-300-DOOR-4R_Passenger_Door_4R.yaml
│   ├── ASM-53-400-DOOR-CRG-FL_Forward_Left_Cargo_Door.yaml
│   ├── ASM-53-400-DOOR-CRG-FR_Forward_Right_Cargo_Door.yaml
│   ├── ASM-53-400-DOOR-CRG-AL_Aft_Left_Cargo_Door.yaml
│   ├── ASM-53-400-DOOR-CRG-AR_Aft_Right_Cargo_Door.yaml
│   └── Installation_Tolerances.csv
│
├── CENTER_WING_BOX_ASSEMBLY/          # Zone 400: Wing-fuselage integration
│   ├── ASM-53-400-001_Forward_Spar_Assembly.yaml
│   ├── ASM-53-400-002_Rear_Spar_Assembly.yaml
│   ├── ASM-53-400-003_MLG_Bay_Left_Assembly.yaml
│   ├── ASM-53-400-004_MLG_Bay_Right_Assembly.yaml
│   └── Critical_Joint_Details.svg
│
├── TAIL_SECTION_ASSEMBLY/             # Zone 600: Aft fuselage
│   ├── ASM-53-600-001_Aft_Bulkhead_Assembly.yaml
│   ├── ASM-53-600-002_Empennage_Attachment_Assembly.yaml
│   ├── ASM-53-600-003_Tail_Cone_Assembly.yaml
│   └── Tail_Assembly_Bill_of_Materials.csv
│
└── ASSETS/                            # Common assembly resources
    ├── Assembly_Standards.md
    ├── Fastener_Schedules.csv
    ├── Torque_Specifications.csv
    ├── Assembly_Tooling_List.csv
    └── QC_Inspection_Points.csv
```

---

## Naming Convention

### Assembly ID Format

All assemblies follow the pattern:

```
ASM-53-[ZONE]-[SUBTYPE]-[SEQUENCE]_[Descriptive_Name]
```

**Components:**
- `ASM` — Assembly identifier prefix
- `53` — ATA Chapter 53 (Fuselage)
- `[ZONE]` — Structural zone (100, 200, 300, 400, 600)
  - `100` = Nose section
  - `200` = Upper pressure shell
  - `300` = Lower/side pressure shell
  - `400` = Center wing box
  - `600` = Tail section
- `[SUBTYPE]` — Optional subtype (e.g., DOOR, FLOOR)
- `[SEQUENCE]` — Sequential number (001, 002, etc.)
- `[Descriptive_Name]` — Human-readable name in PascalCase or Snake_Case

**Examples:**
- `ASM-53-100-001` — Forward Bulkhead Assembly (Nose, sequence 1)
- `ASM-53-200-DOOR-1L` — Passenger Door 1 Left (Upper shell, door subtype)
- `ASM-53-400-003` — MLG Bay Left Assembly (Center wing box, sequence 3)

---

## YAML Template Structure

Each assembly YAML file contains:

1. **assembly_metadata** — Core identification and traceability
   - `assembly_id` — Unique assembly identifier (ASM-53-…)
   - `assembly_name` — Descriptive name
   - `parent_ci` — Primary Configuration Item
   - `related_cis` — List of all CIs in this assembly
   - `structure_classification` — Primary or Secondary structure
   - `plm_item_id` — PLM system reference (Teamcenter, ENOVIA, etc.)
   - `cad_master_drawing` — Drawing number reference
   - `version` — Design version, status, update history

2. **components** — Bill of Materials
   - Part numbers with CI linkage
   - Material specifications
   - Quantities
   - Primary load path identification

3. **assembly_sequence** — Step-by-step assembly instructions
   - Tooling setup
   - Component positioning
   - Fastening and bonding procedures
   - Quality checkpoints

4. **tooling_required** — Assembly tooling catalog
   - Jigs, fixtures, alignment systems
   - Torque tools and calibration requirements

5. **quality_control** — Inspection and acceptance criteria
   - Dimensional tolerances
   - NDT requirements
   - Fastener verification
   - Acceptance criteria

6. **links** — Traceability to related documentation
   - Requirements traceability matrices
   - Stress analysis reports
   - FEA model descriptions
   - Manufacturing plans
   - Quality control plans

---

## CI-to-Assembly Mapping

Assemblies integrate multiple Configuration Items (CIs):

| Assembly Zone | CI Zone Range | Example CIs |
|---------------|---------------|-------------|
| 100 (Nose) | CI-53-100-xxx | Forward bulkhead, NLG bay, cockpit frame |
| 200 (Upper Shell) | CI-53-200-xxx | Upper shell panels, stringers, frames |
| 300 (Lower/Side Shell) | CI-53-300-xxx | Side shell panels, floor supports |
| 400 (Center Wing Box) | CI-53-400-xxx | Wing spars, MLG bays, keel beam |
| 600 (Tail) | CI-53-600-xxx | Aft bulkhead, empennage attach, tail cone |

**Reference:** CI definitions are maintained in `53-00-04_Design/02_Configuration_Items/Zone_[XXX]_[Name]/`

---

## Bill of Materials (BOM) Generation

### From CI Database

Each assembly folder contains a `Bill_of_Materials.csv` or equivalent that can be generated from the CI database:

```bash
# Example: Generate BOM for nose section
python tools/generate_bom.py --zone 100 --output NOSE_SECTION_ASSEMBLY/Bill_of_Materials.csv
```

### BOM Structure

Standard BOM CSV format:

```csv
Item,Part_Number,CI_Number,Description,Quantity,Material,Unit_Weight_kg,Total_Weight_kg,Primary_Structure
1,53-100-1001-01,CI-53-100-BHD-FWD,Forward Bulkhead Web,1,CFRP,45.2,45.2,Yes
2,53-100-1002-01,CI-53-100-NLG-BAY,NLG Bay Frame,1,Al-7075-T6,32.8,32.8,Yes
...
```

---

## Assembly ID Rules

### Creating New Assembly IDs

1. **Identify the structural zone** (100, 200, 300, 400, 600)
2. **Check existing sequence numbers** in that zone
3. **Use next available number** within the zone
4. **Add subtype if needed** (DOOR, FLOOR, etc.)
5. **Follow naming convention** exactly

### Zone-Based Allocation

- **100-series**: Nose section components (001-099)
- **200-series**: Upper pressure shell components (001-099, DOOR-1L through DOOR-2R)
- **300-series**: Lower/side shell components (001-099, DOOR-3L through DOOR-4R)
- **400-series**: Center wing box components (001-099, DOOR-CRG-xx for cargo doors)
- **600-series**: Tail section components (001-099)

### Special Subtypes

- **DOOR**: Door frame assemblies (8 passenger + 4 cargo = 12 total)
- **FLOOR**: Floor structural assemblies
- **No subtype**: Primary structural assemblies

---

## Integration with Other Systems

### CI/CD Pipeline

Assembly YAML files are validated in the CI/CD pipeline:
- Schema validation against assembly template
- Link verification (all referenced CIs must exist)
- BOM completeness checks
- Traceability matrix validation

### PLM Integration

- `plm_item_id` provides linkage to PLM systems (Teamcenter, ENOVIA)
- `cad_master_drawing` links to CAD drawing management
- Version control synchronized between Git and PLM

### 53-50 Structures Integration

Assembly definitions link to detailed structural analysis:
- Stress analysis reports in `53-50_Structures/53-50-[XX]_[Topic]/`
- FEA model descriptions and results
- Load case documentation
- Material test data

### GenCCC Traceability

- `parent_ci` and `related_cis` enable automatic traceability graph generation
- Links to requirements via CI-level traceability matrices
- Supports impact analysis for design changes

---

## Quality Assurance

### Assembly Standards

All assemblies must comply with:
- [CS-25 Certification Specifications](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)
- [DO-178C](https://www.rtca.org/) (for software-controlled assembly processes)
- [DO-254](https://www.rtca.org/) (for electronic assembly elements)
- Internal standards in `ASSETS/Assembly_Standards.md`

### Inspection Points

Critical inspection points are defined in:
- `ASSETS/QC_Inspection_Points.csv` — Global QC checkpoints
- Individual assembly YAML `quality_control` sections
- Assembly sequence step validations

### Documentation Requirements

Each assembly must have:
- Complete YAML definition with all required fields
- Bill of Materials (CSV format)
- Assembly sequence documentation
- Quality control plan
- Traceability to parent CIs

---

## Usage Examples

### Viewing an Assembly Definition

```bash
# View a specific assembly
cat NOSE_SECTION_ASSEMBLY/ASM-53-100-001_Forward_Bulkhead_Assembly.yaml
```

### Validating Assembly Definitions

```bash
# Validate all assemblies in this directory
python tools/validate_assemblies.py ASSEMBLIES/

# Validate a specific assembly
python tools/validate_assemblies.py ASSEMBLIES/NOSE_SECTION_ASSEMBLY/ASM-53-100-001_Forward_Bulkhead_Assembly.yaml
```

### Generating Traceability Reports

```bash
# Generate CI-to-Assembly traceability matrix
python tools/generate_traceability.py --type assembly --zone 400 --output traceability_report.csv
```

---

## Maintenance Guidelines

### Adding a New Assembly

1. Create YAML file in appropriate subdirectory
2. Follow naming convention strictly
3. Copy and adapt template from this README or existing assembly
4. Fill in all required metadata sections
5. Add to parent folder's Bill_of_Materials.csv
6. Update CI linkages
7. Commit with descriptive message

### Updating an Assembly

1. Increment `version.design_version` in YAML
2. Update `version.last_update` date
3. Document changes in version control commit message
4. Update dependent BOMs if components changed
5. Notify downstream systems (PLM, manufacturing)

### Deprecating an Assembly

1. Set `version.status` to "Obsolete"
2. Document reason in commit message
3. Update traceability matrices
4. Archive assembly definition (do not delete)

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status**: DRAFT – Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22

---

## References

- [CS-25 Certification Specifications](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)
- [AMPEL360 Assets Standard](../../../../../../AMPEL360_ASSETS_STANDARD.md)
- [OPT-IN Framework Documentation](../../../../../../OPT-IN_FRAMEWORK_STANDARD.md)
- [ATA Chapter 53 Overview](../../../README.md)

---

**For questions or issues with assembly definitions, contact the Fuselage Structures Team.**
