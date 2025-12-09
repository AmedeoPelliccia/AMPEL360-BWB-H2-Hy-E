# ASSEMBLIES — ATA 10 Parking, Mooring, Storage & RTS

**Path:** `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/10-00_GENERAL/10-00-04_Design/ASSETS/ASSEMBLIES/`

---

## 1. Purpose

This directory contains **assembly-level definitions** for the AMPEL360 BWB-H2-Hy-E (Q100) aircraft parking, mooring, storage, and return-to-service (RTS) systems. Each assembly represents a cohesive functional unit that:

- Integrates multiple components into a complete subsystem
- Provides standardized interfaces with the aircraft structure and other ATA chapters
- Supports ground operations, maintenance, and storage requirements
- Ensures safety for hydrogen and high-voltage systems

---

## 2. Directory Structure

```text
ASSEMBLIES/
│
├── ASM-10-001_Mooring_Points/              # 5 components
│   ├── ASM-10-001_Mooring_Points-000_Assembly_Overview.md
│   ├── ASM-10-001_Mooring_Points-DWG/     # 2D drawings (SVG)
│   ├── ASM-10-001_Mooring_Points-3D/      # 3D models (STEP, GLB)
│   ├── ASM-10-001_Mooring_Points-BOM/     # Bills of material (XLSX, CSV)
│   └── ASM-10-001_Mooring_Points-SPEC/    # Specifications (MD)
│
├── ASM-10-002_Towing_Fittings/             # 4 components
├── ASM-10-003_Jacking_Points/              # 5 components
├── ASM-10-004_Tie_Down_Hardware/           # 5 components
├── ASM-10-005_Ground_Locks/                # 5 components
├── ASM-10-006_Protective_Covers/           # 8 components
├── ASM-10-007_H2_Storage_Provisions/       # 6 components (🧊 H₂-specific)
├── ASM-10-008_HV_Isolation_Provisions/     # 6 components (⚡ HV-specific)
├── ASM-10-009_Ground_Power_Interface/      # 5 components
├── ASM-10-010_Environmental_Protection/    # 6 components
├── ASM-10-011_Monitoring_Systems/          # 6 components
├── ASM-10-012_RTS_Kit/                     # 6 components
│
├── ASM-10-090_Schemas/                     # JSON schemas for data validation
│   ├── assembly.schema.json
│   ├── drawing.schema.json
│   ├── bom.schema.json
│   ├── specification.schema.json
│   └── 3d-model.schema.json
│
└── ASM-10-099_Index/                       # Master indices
    ├── ASM-10-099-A_Assembly_Index.md
    ├── ASM-10-099-B_Drawing_Index.md
    ├── ASM-10-099-C_BOM_Index.md
    ├── ASM-10-099-D_Specification_Index.md
    ├── ASM-10-099-E_3D_Model_Index.md
    └── ASM-10-099-F_Cross_References.md
```

---

## 3. Assembly Summary

| Assembly ID | Title | Components | Q100 Specifics | Safety Criticality |
|-------------|-------|------------|----------------|-------------------|
| [ASM-10-001](ASM-10-001_Mooring_Points/) | Mooring Points | 5 | BWB configuration points | 🔴 Critical |
| [ASM-10-002](ASM-10-002_Towing_Fittings/) | Towing Fittings | 4 | High-load capacity | 🔴 Critical |
| [ASM-10-003](ASM-10-003_Jacking_Points/) | Jacking Points | 5 | BWB weight distribution | 🔴 Critical |
| [ASM-10-004](ASM-10-004_Tie_Down_Hardware/) | Tie-Down Hardware | 5 | Quick-release for ops | 🟠 High |
| [ASM-10-005](ASM-10-005_Ground_Locks/) | Ground Locks | 5 | Safety interlocks | 🔴 Critical |
| [ASM-10-006](ASM-10-006_Protective_Covers/) | Protective Covers | 8 | H₂ vent + HV covers | 🟢 Medium |
| [ASM-10-007](ASM-10-007_H2_Storage_Provisions/) | H₂ Storage Provisions | 6 | 🧊 Cryogenic-specific | 🔴 Critical |
| [ASM-10-008](ASM-10-008_HV_Isolation_Provisions/) | HV Isolation Provisions | 6 | ⚡ 800V+ systems | 🔴 Critical |
| [ASM-10-009](ASM-10-009_Ground_Power_Interface/) | Ground Power Interface | 5 | Battery charging | 🟠 High |
| [ASM-10-010](ASM-10-010_Environmental_Protection/) | Environmental Protection | 6 | Storage preservation | 🟢 Medium |
| [ASM-10-011](ASM-10-011_Monitoring_Systems/) | Monitoring Systems | 6 | H₂ + battery monitoring | 🟠 High |
| [ASM-10-012](ASM-10-012_RTS_Kit/) | RTS Kit | 6 | Return to service tools | 🟡 Low |

---

## 4. Asset Types per Assembly

Each assembly folder contains standardized subfolders:

| Subfolder | Content | Formats | Purpose |
|-----------|---------|---------|---------|
| `ASM-10-XXX-DWG/` | 2D Engineering Drawings | SVG, PDF | Manufacturing, inspection, assembly |
| `ASM-10-XXX-3D/` | 3D CAD Models | STEP, GLB, GLTF | Design analysis, visualization, tooling |
| `ASM-10-XXX-BOM/` | Bills of Material | XLSX, CSV, JSON | Procurement, cost tracking, inventory |
| `ASM-10-XXX-SPEC/` | Technical Specifications | Markdown | Requirements, test procedures, interfaces |

---

## 5. Naming Conventions

### 5.1 Drawing Naming

```
Q100-10-[ASM]-[ITEM]-[TYPE]-[SEQ]_[DESCRIPTION].[EXT]

Where:
  Q100    = Aircraft model (AMPEL360 BWB-H2-Hy-E)
  10      = ATA Chapter
  ASM     = Assembly number (001-012)
  ITEM    = Item number within assembly (001-999)
  TYPE    = Asset type (DWG, 3D, BOM, SPEC)
  SEQ     = Sequential number (001-999)
  EXT     = File extension (svg, pdf, step, glb, xlsx, md, etc.)

Examples:
  Q100-10-001-001-DWG-001_Fwd_Mooring_Assy.svg
  Q100-10-007-002-3D-001_Vent_Management.step
  Q100-10-008-BOM-001_HV_Isolation_BOM.xlsx
  Q100-10-011-SPEC-002_H2_Detection_Sensitivity.md
```

### 5.2 Assembly Identifier Format

```
ASM-10-XXX

Where:
  ASM = Assembly designation
  10  = ATA Chapter 10
  XXX = Three-digit assembly number (001-012, 090=schemas, 099=indices)
```

---

## 6. Q100-Specific Assemblies

### 6.1 🧊 ASM-10-007: H₂ Storage Provisions

**Critical for hydrogen-hybrid aircraft storage**

| Component | Purpose | Safety Criticality |
|-----------|---------|-------------------|
| Tank Isolation System | Isolate LH₂ tank during storage | 🔴 Critical |
| Vent Management System | Controlled boil-off release | 🔴 Critical |
| Pressure Relief Interface | Overpressure protection | 🔴 Critical |
| Leak Detection Provisions | H₂ leak monitoring | 🔴 Critical |
| Boil-Off Management | Minimize fuel loss | 🟠 High |
| Ground Vent Connection | External venting during storage | 🟠 High |

**Key Design Considerations:**
- Cryogenic temperature compatibility (-253°C)
- Fail-safe isolation mechanisms
- Redundant leak detection
- Remote monitoring capability
- Ground crew safety zones

---

### 6.2 ⚡ ASM-10-008: HV Isolation Provisions

**Essential for 800V+ electrical system safety**

| Component | Purpose | Safety Criticality |
|-----------|---------|-------------------|
| Main HV Disconnect | Primary system isolation | 🔴 Critical |
| Battery Isolation Switch | Battery pack isolation | 🔴 Critical |
| Fuel Cell Isolation | FC stack isolation | 🔴 Critical |
| Motor Isolation Contactors | Propulsion motor isolation | 🔴 Critical |
| Ground Fault Interrupter | Fault protection | 🔴 Critical |
| LOTO Provisions | Maintenance lockout/tagout | 🟠 High |

**Key Design Considerations:**
- Verified zero-energy state capability
- Arc flash boundary markings
- Multi-point isolation architecture
- Visual and electrical status indication
- NFPA 70E compliance

---

### 6.3 🔋 ASM-10-009: Ground Power Interface

**Unique charging requirements for hybrid-electric architecture**

| Component | Purpose | Specification |
|-----------|---------|---------------|
| External Power Receptacle | Ground power connection | 400Hz AC / High-power DC |
| Power Transfer Switch | Power source switching | Automatic/Manual modes |
| Ground Power Controller | Power management | Smart charging algorithms |
| Battery Charging Interface | Li-ion charging port | CCS2 / MCS compatible |
| Shore Power Connector | Long-term storage power | 3-phase AC input |

**Key Design Considerations:**
- Dual-mode operation (AC + DC)
- Future-proof charging standards
- Compatibility with airport GSE
- Rapid charging capability (up to 350 kW DC)

---

## 7. Cross-References

### 7.1 Related ATA Chapters

| ATA | Chapter | Interface | Assembly Link |
|-----|---------|-----------|---------------|
| [ATA 07](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/) | Lifting & Shoring | Jacking point load paths | ASM-10-003 |
| [ATA 09](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/) | Towing & Taxiing | Towing lug interfaces | ASM-10-002 |
| [ATA 24](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/) | Electrical Power | Ground power, HV isolation | ASM-10-008, ASM-10-009 |
| [ATA 28](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/) | Fuel Systems | H₂ storage interface | ASM-10-007 |
| [ATA 32](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/) | Landing Gear | Ground lock interfaces, jacking | ASM-10-003, ASM-10-005 |
| [ATA 73](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/) | Engine Fuel Systems | H₂ tank isolation valves | ASM-10-007 |

### 7.2 Related ATA 10 Folders

| Folder | Content | Relationship |
|--------|---------|--------------|
| [10-00-03_Requirements](../../10-00-03_Requirements/) | System requirements | Derives assembly specs |
| [10-00-06_Engineering](../../10-00-06_Engineering/) | Engineering analysis | Validates assembly designs |
| [10-00-07_V_AND_V](../../10-00-07_V_AND_V/) | Verification & Validation | Tests assembly compliance |
| [10-20_Subsystems](../../../../10-20_Subsystems/) | Functional subsystems | Assembly integration |
| [10-50_Structures](../../../../10-50_Structures/) | Structural design | Mounting and load paths |
| [10-80_Energy](../../../../10-80_Energy/) | Energy systems | HV and H₂ interfaces |

---

## 8. Standards and Schemas

### 8.1 JSON Schemas

All structured data (BOMs, specifications, model metadata) can be validated against schemas in [`ASM-10-090_Schemas/`](ASM-10-090_Schemas/):

- **assembly.schema.json** — Assembly definition structure
- **drawing.schema.json** — Drawing metadata
- **bom.schema.json** — Bill of materials format
- **specification.schema.json** — Specification document structure
- **3d-model.schema.json** — 3D model metadata

### 8.2 Applicable Standards

| Standard | Title | Applicability |
|----------|-------|---------------|
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Large Aeroplanes | All assemblies |
| SAE AS8015 | Jacking and Shoring Pads | ASM-10-003 |
| SAE AS8016 | Towing Provisions | ASM-10-002 |
| SAE AIR7558 | Hydrogen Aviation Fuel Safety | ASM-10-007, ASM-10-011 |
| NFPA 70E | Electrical Safety in Workplace | ASM-10-008 |
| ISO 21013-1 | Cryogenic Vessels | ASM-10-007 |

---

## 9. Usage Guidelines

### 9.1 For Design Engineers

1. **Navigate to the relevant assembly folder** (e.g., `ASM-10-007_H2_Storage_Provisions/`)
2. **Review the Assembly Overview** (`ASM-10-XXX-000_Assembly_Overview.md`)
3. **Access asset subfolders**:
   - `*-DWG/` for drawings
   - `*-3D/` for CAD models
   - `*-BOM/` for part lists
   - `*-SPEC/` for specifications
4. **Follow naming conventions** when adding new files
5. **Validate structured data** against JSON schemas in `ASM-10-090_Schemas/`

### 9.2 For Procurement/Manufacturing

1. **Use BOM files** (`ASM-10-XXX-BOM/`) for procurement planning
2. **Reference drawings** for manufacturing specifications
3. **Consult specifications** for quality acceptance criteria
4. **Track critical items** (long-lead components marked in BOMs)

### 9.3 For Certification Engineers

1. **Review assembly safety criticality** classifications (table in Section 3)
2. **Trace to requirements** via cross-references (Section 7)
3. **Gather compliance evidence** from specifications and test reports
4. **Reference applicable standards** (Section 8.2)

---

## 10. Development Status

| Assembly | Overview | Drawings | 3D Models | BOM | Specifications | Status |
|----------|----------|----------|-----------|-----|----------------|--------|
| ASM-10-001 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-002 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-003 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-004 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-005 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-006 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-007 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-008 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-009 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-010 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-011 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |
| ASM-10-012 | Stub | Pending | Pending | Pending | Pending | 📝 Planned |

**Legend:**  
📝 Planned | 🚧 In Progress | ✅ Complete | 🔍 Under Review

---

## 11. Contributing

When adding or modifying assembly definitions:

1. **Follow the directory structure** exactly as shown
2. **Use the naming conventions** (Section 5)
3. **Validate JSON/CSV data** against schemas
4. **Update cross-references** in both directions
5. **Document design decisions** in `10-00-04-004_Design_Decisions.md`
6. **Link to verification evidence** in `10-00-07_V_AND_V/`
7. **Maintain traceability** to requirements in `10-00-03_Requirements/`

---

## 12. Index Files

For comprehensive indices of all assets across assemblies, see:

- [`ASM-10-099-A_Assembly_Index.md`](ASM-10-099_Index/ASM-10-099-A_Assembly_Index.md) — Master assembly list
- [`ASM-10-099-B_Drawing_Index.md`](ASM-10-099_Index/ASM-10-099-B_Drawing_Index.md) — All drawings
- [`ASM-10-099-C_BOM_Index.md`](ASM-10-099_Index/ASM-10-099-C_BOM_Index.md) — All BOMs
- [`ASM-10-099-D_Specification_Index.md`](ASM-10-099_Index/ASM-10-099-D_Specification_Index.md) — All specifications
- [`ASM-10-099-E_3D_Model_Index.md`](ASM-10-099_Index/ASM-10-099-E_3D_Model_Index.md) — All 3D models
- [`ASM-10-099-F_Cross_References.md`](ASM-10-099_Index/ASM-10-099-F_Cross_References.md) — Cross-references and traceability

---

## Document Control

- **Generated with assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT – Subject to human review and approval
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---
