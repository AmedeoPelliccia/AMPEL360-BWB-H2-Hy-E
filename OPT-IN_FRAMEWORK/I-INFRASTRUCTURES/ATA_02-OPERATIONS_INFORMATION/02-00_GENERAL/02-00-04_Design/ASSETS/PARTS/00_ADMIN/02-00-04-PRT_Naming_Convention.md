# PARTS Naming Convention (ATA 02-00-04)

## 1. Part Folder Naming

### Pattern

```text
[ATA]-PRT-[Category]-[PartCode]_[ShortName]/
```

### Components

* **[ATA]** = ATA chapter reference = `02-00-04`
* **PRT** = Part artifact type identifier
* **[Category]** = Part category code (see section 2)
* **[PartCode]** = Unique numeric or alphanumeric code within category
* **[ShortName]** = Concise English descriptor using CamelCase or underscores

### Examples

* `02-00-04-PRT-MECH-0001_ConsoleSideBracket/`
* `02-00-04-PRT-ELEC-0100_PowerPanelMainBreaker/`
* `02-00-04-PRT-IT-0200_ServerChassis_2U/`
* `02-00-04-PRT-GSE-0300_PowerCart_Chassis/`
* `02-00-04-PRT-STD-9001_M8_Bolt_A2/`

---

## 2. Part Categories

| Category Code | Description | Example Parts |
|--------------|-------------|---------------|
| **MECH** | Mechanical parts | Brackets, frames, housings, panels, fabricated items |
| **ELEC** | Electrical/Electronic | Breakers, panels, connectors, harnesses, cables |
| **IT** | IT and Network | Racks, servers, chassis, network modules, COTS IT hardware |
| **GSE** | Ground Support Equipment & Infrastructure | Power carts, support structures, enclosures |
| **STD** | Fasteners and Standard Parts | Bolts, nuts, washers, screws, standardized hardware |

---

## 3. Part Code Assignment

### Guidelines

* **Sequential numbering** within each category
* **Leading zeros** for alignment (e.g., `0001`, `0100`)
* **Ranges** can be reserved for subsystems:
  * `MECH-0001` to `MECH-0099`: Console components
  * `MECH-0100` to `MECH-0199`: Frame structures
  * `ELEC-0100` to `ELEC-0199`: Power distribution
  * `ELEC-0200` to `ELEC-0299`: Control panels
  * `IT-0200` to `IT-0299`: Server equipment
  * `GSE-0300` to `GSE-0399`: Power carts
  * `STD-9000+`: Standard fasteners

---

## 4. File Naming Within Part Folders

### 4.1 3D CAD Files

**Neutral format (STEP):**

```text
[ATA]-PRT-[Category]-[PartCode]_[ShortName].step
```

Example: `02-00-04-PRT-MECH-0001_ConsoleSideBracket.step`

**Native CAD format:**

```text
[ATA]-PRT-[Category]-[PartCode]_[ShortName].[ext]
```

Examples:
* `02-00-04-PRT-MECH-0001_ConsoleSideBracket.prt` (Creo/Pro-E)
* `02-00-04-PRT-MECH-0001_ConsoleSideBracket.sldprt` (SolidWorks)
* `02-00-04-PRT-MECH-0001_ConsoleSideBracket.f3d` (Fusion 360)

### 4.2 2D Detail Drawings

**Pattern:**

```text
[ATA]-DWG-DET-PRT-[Category]-[PartCode]-[ShortName]-SHT[nn]-R[yy].[ext]
```

**Components:**
* **DWG** = Drawing artifact type
* **DET** = Detail drawing (vs. ASM for assembly)
* **SHT[nn]** = Sheet number (01, 02, etc.)
* **R[yy]** = Revision number (01, 02, etc.)

**Examples:**
* `02-00-04-DWG-DET-PRT-MECH-0001-ConsoleSideBracket-SHT01-R01.dwg`
* `02-00-04-DWG-DET-PRT-MECH-0001-ConsoleSideBracket-SHT01-R01.pdf`
* `02-00-04-DWG-DET-PRT-ELEC-0100-PowerPanelMainBreaker-SHT01-R02.dwg`

**Accompanying description file (optional):**

```text
[ATA]-DWG-DET-PRT-[Category]-[PartCode]-[ShortName]-SHT[nn]-R[yy].md
```

Example: `02-00-04-DWG-DET-PRT-MECH-0001-ConsoleSideBracket-SHT01-R01.md`

### 4.3 Datasheets and Specifications

**For COTS parts:**

```text
[ATA]-PRT-[Category]-[PartCode]_[ShortName]-Datasheet-R[yy].pdf
```

Example: `02-00-04-PRT-IT-0200_ServerChassis_2U-Datasheet-R01.pdf`

**For specifications:**

```text
[ATA]-PRT-[Category]-[PartCode]_[ShortName]-Specification-R[yy].pdf
```

Example: `02-00-04-PRT-ELEC-0100_PowerPanelMainBreaker-Specification-R01.pdf`

### 4.4 Part Metadata Sidecar

**Optional markdown file for rich metadata:**

```text
[ATA]-PRT-[Category]-[PartCode]_[ShortName].md
```

Example: `02-00-04-PRT-MECH-0001_ConsoleSideBracket.md`

**Content should include:**
* Material specifications
* Surface finish requirements
* Manufacturing notes
* Tolerances
* Mass properties
* Related assemblies
* Supplier information (for COTS)

---

## 5. Internal Part Folder Structure

Each part folder should maintain this structure:

```text
02-00-04-PRT-[Category]-[PartCode]_[ShortName]/
├── README.md                           # Part overview and metadata
├── 3D/                                 # 3D CAD files
│   ├── [PartID].step                   # Neutral format
│   └── [PartID].[native_ext]           # Native CAD (optional)
├── 2D/                                 # 2D detail drawings
│   ├── [DrawingID]-SHT01-R01.dwg
│   ├── [DrawingID]-SHT01-R01.pdf
│   └── [DrawingID]-SHT01-R01.md
├── DATASHEETS/                         # Specifications and datasheets
│   ├── [PartID]-Datasheet-R01.pdf
│   └── [PartID]-Specification-R01.pdf
├── TEST/                               # Test reports (optional)
│   └── [PartID]-TestReport-R01.pdf
└── CERTS/                              # Certifications (optional)
    └── [PartID]-MaterialCert-R01.pdf
```

---

## 6. Archive Naming

When archiving parts:

```text
99_ARCHIVE/
└── 02-00-04-PRT-ARCHIVE_YYYY-MM-DD_[Tag]/
    └── [Archived part folder with original name]
```

Example:

```text
99_ARCHIVE/
└── 02-00-04-PRT-ARCHIVE_2025-11-17_Superseded-by-0002/
    └── 02-00-04-PRT-MECH-0001_ConsoleSideBracket/
```

---

## 7. Naming Best Practices

### DO:
* Use consistent CamelCase or underscores for `[ShortName]`
* Keep `[ShortName]` concise (max 40 characters)
* Use standard units in names (e.g., `_2U`, `_M8`, `_100A`)
* Include key distinguishing features (e.g., `_Left`, `_Right`, `_A`, `_B`)
* Update revision numbers when drawings change
* Maintain descriptive README.md files

### DON'T:
* Use spaces in file or folder names
* Use special characters except `-`, `_`
* Abbreviate excessively (maintain readability)
* Change `[PartCode]` once assigned
* Duplicate part codes across categories

---

## 8. Document Control

* **Version:** 1.0.0
* **Status:** WORKING
* **Last Updated:** 2025-11-17
* **Author:** AMPEL360 Design Team (AI-assisted by Amedeo Pelliccia)
* **Approver:** [To be assigned]

**Notes:**
* This naming convention was generated by AI and requires human review and approval before official adoption.
