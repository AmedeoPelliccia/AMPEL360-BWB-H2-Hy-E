# PROCEDURES — Administration

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / PROCEDURES / 00_ADMIN  
**Purpose:** Administrative files, metadata, and change tracking for installation procedures

---

## Contents

This folder contains:

- **README.md** - This file, describing the PROCEDURES structure
- **CHANGELOG.md** - Revision history of all procedures in this folder tree
- **02-00-04-PRC_Index.csv** - Master index of all procedures with metadata

---

## PROCEDURES Structure

```
PROCEDURES/
├── 00_ADMIN/                      # Administrative files (this folder)
├── 05_TEMPLATES/                  # Reusable procedure templates
├── 10_INSTALLATION/               # Installation procedures
├── 20_COMMISSIONING/              # Commissioning and acceptance procedures
├── 30_OPERATION/                  # Operational procedures
├── 40_MAINTENANCE/                # Maintenance procedures
├── 50_EMERGENCY/                  # Emergency response procedures
├── 60_CHECKLISTS_FORMS/           # Checklists and forms
├── 70_TRAINING_AIDS/              # Training materials and quick reference
└── 99_ARCHIVE/                    # Archived/superseded procedures
```

---

## Important Note on Maintenance Procedures

**Maintenance procedures** in this folder (40_MAINTENANCE) are **design-side** procedures covering:
- Design-phase maintenance planning
- Maintainability design considerations
- Maintenance access requirements
- Tooling and equipment specifications

**Operational maintenance procedures** for the production aircraft/system should be placed in:
- **ATA Chapter 11** (Maintenance/Placards) folders
- **02-00-14_Ops_Std_Sustain** (Operations & Sustainment lifecycle folder)

This distinction keeps design documentation separate from operational documentation.

---

## Procedure Categories

### 05_TEMPLATES

Standard procedure templates:
- Installation procedure template
- Commissioning procedure template
- Operation procedure template
- Maintenance procedure template
- Emergency procedure template

**Formats:** `.md`, `.docx`, `.xlsx`

### 10_INSTALLATION

Installation procedures for physical installations:
- Equipment installation steps
- Console and workstation installation
- Rack installation procedures
- Cabling and connectivity procedures
- Initial power-up procedures

**Purpose:** Guide installation contractors and technicians

**Formats:** `.md`, `.pdf`, `.docx`

### 20_COMMISSIONING

Commissioning and acceptance test procedures:
- System commissioning procedures
- Integrated system testing
- Acceptance test procedures (ATP)
- Factory acceptance test (FAT) procedures
- Site acceptance test (SAT) procedures
- Performance verification

**Purpose:** Ensure systems are correctly installed and functional

**Formats:** `.md`, `.pdf`, `.docx`, `.xlsx`

### 30_OPERATION

Operational procedures for installed systems:
- Startup procedures
- Shutdown procedures
- Normal operations
- Mode changes
- System configuration procedures

**Purpose:** Guide operators in day-to-day use

**Formats:** `.md`, `.pdf`, `.docx`

### 40_MAINTENANCE

Design-side maintenance procedures:
- Preventive maintenance schedules
- Component replacement procedures
- Periodic inspection procedures
- Calibration procedures
- Cleaning and servicing procedures

**Purpose:** Guide maintenance planning during design phase

**Formats:** `.md`, `.pdf`, `.docx`

### 50_EMERGENCY

Emergency response procedures:
- Loss of power procedures
- System failure responses
- Fire emergency procedures
- Evacuation procedures
- Emergency shutdown procedures

**Purpose:** Ensure safe response to emergency situations

**Formats:** `.md`, `.pdf`, `.docx`

### 60_CHECKLISTS_FORMS

Checklists and forms supporting procedures:
- Pre-installation checklists
- Commissioning checklists
- Daily/weekly/monthly inspection checklists
- Maintenance logs
- Incident report forms

**Purpose:** Standardize and document procedural compliance

**Formats:** `.xlsx`, `.pdf`, `.docx`

### 70_TRAINING_AIDS

Training materials and quick reference:
- Operator training guides
- Quick reference cards
- Training presentations
- Video training materials
- Job aids and decision trees

**Purpose:** Support training and knowledge transfer

**Formats:** `.pdf`, `.pptx`, `.docx`, `.mp4`

---

## File Naming Convention

All procedures follow the pattern:

```
02-00-04-PRC-<TYPE>-<FACILITY>-<PROCEDURE>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `PRC` = Procedure category code
- `TYPE` = INST (Installation), COMM (Commissioning), OPR (Operation), MAINT (Maintenance), EMERG (Emergency), CHK (Checklist), TRNG (Training)
- `FACILITY` = OPSCTR (Operations Center), DATACENTER, etc.
- `PROCEDURE` = Specific procedure name
- `R<nn>` = Revision number (R01, R02, etc.)
- `ext` = File extension (.md, .pdf, .docx, .xlsx, etc.)

### Examples

**Installation:**
- `02-00-04-PRC-INST-OPSCTR-ConsolesInstall-R01.md`
- `02-00-04-PRC-INST-DATACENTER-RacksInstall-R01.md`

**Commissioning:**
- `02-00-04-PRC-COMM-OPSCTR-ControlRoomCommissioning-R01.md`
- `02-00-04-PRC-COMM-DATACENTER-SystemsCommissioning-R01.md`

**Operation:**
- `02-00-04-PRC-OPR-OPSCTR-StartUpShutdown-R01.md`
- `02-00-04-PRC-OPR-DATACENTER-NormalOps-R01.md`

**Maintenance:**
- `02-00-04-PRC-MAINT-OPSCTR-PeriodicInspection-R01.md`
- `02-00-04-PRC-MAINT-DATACENTER-FilterReplacement-R01.md`

**Emergency:**
- `02-00-04-PRC-EMERG-OPSCTR-LossOfPower-R01.md`
- `02-00-04-PRC-EMERG-DATACENTER-SmokeInRoom-R01.md`

**Checklists:**
- `02-00-04-PRC-CHK-OPSCTR-CommissioningChecklist-R01.xlsx`
- `02-00-04-PRC-CHK-DATACENTER-MaintLog-R01.xlsx`

**Training:**
- `02-00-04-PRC-TRNG-OPSCTR-OperatorGuide-R01.pdf`
- `02-00-04-PRC-TRNG-OPSCTR-QuickRefCards-R01.pdf`

---

## Usage Guidelines

### Creating a New Procedure

1. **Select appropriate category** folder (10-70)
2. **Use template** from `05_TEMPLATES/` if available
3. **Follow naming convention** strictly
4. **Write in clear, step-by-step format**
5. **Include safety warnings** and cautions
6. **Add diagrams/photos** where helpful
7. **Review with SMEs** (Subject Matter Experts)
8. **Update CHANGELOG.md** with revision entry
9. **Update index** in `00_ADMIN/02-00-04-PRC_Index.csv`

### Procedure Writing Standards

**Structure:**
1. **Purpose** - Why this procedure exists
2. **Scope** - What is covered/not covered
3. **Prerequisites** - Required conditions before starting
4. **Required Tools/Equipment** - What you need
5. **Safety Warnings** - Critical safety information
6. **Procedure Steps** - Numbered, sequential steps
7. **Verification** - How to verify successful completion
8. **Troubleshooting** - Common issues and solutions
9. **References** - Related documents

**Style:**
- Use **imperative mood** ("Connect the cable" not "The cable should be connected")
- Use **numbered steps** for sequential actions
- Use **bullet points** for non-sequential information
- **Bold** critical safety information
- Include **clear warnings** before hazardous steps
- Add **notes** for helpful information
- Use **simple language** avoiding jargon where possible

### Safety Warnings Format

Use standard warning levels:

**DANGER:** Immediate hazards that will result in severe injury or death
**WARNING:** Hazards that could result in severe injury or death
**CAUTION:** Hazards that could result in minor or moderate injury
**NOTICE:** Situations that could result in equipment damage

### Revision Control

- Increment revision number for each significant change
- Document changes in CHANGELOG.md
- Keep revision history section in procedure
- Archive previous revision to `99_ARCHIVE/` if major change

### Coordination

Procedures must coordinate with:
- **BIM_CAD_MODELS/** - 3D models showing physical context
- **DIAGRAMS/** - System diagrams referenced in procedures
- **LAYOUTS/** - Space layouts showing equipment locations
- **Requirements/** - `02-00-03_Requirements` (functional requirements)
- **Safety/** - `02-00-02_Safety` (safety requirements)

---

## Review and Approval

All procedures should undergo:

1. **Technical review** - Subject matter expert validation
2. **Safety review** - Safety team review for hazards
3. **Quality review** - Quality assurance review for completeness
4. **Pilot test** - Test procedure with actual personnel
5. **Final approval** - Authorized approver sign-off

Document approvals in CHANGELOG.md

---

## Related Documentation

- [INSTALLATIONS README](../README.md)
- [BIM_CAD_MODELS README](../BIM_CAD_MODELS/00_ADMIN/README.md)
- [DIAGRAMS README](../DIAGRAMS/00_ADMIN/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)
- Safety Standards - see `02-00-02_Safety`
- Operational Procedures - see `02-00-14_Ops_Std_Sustain`
- Maintenance Procedures - see ATA Chapter 11

---

**Last Updated:** 2025-11-14  
**Owner:** AMPEL360 Procedures & Training Team
