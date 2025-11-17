# Part Metadata Sheet Template (Excel)

## Purpose

This document describes the structure of the Excel metadata sheet template for parts.
The actual Excel file should be created with the following structure.

---

## Sheet 1: Part Information

| Field | Column | Type | Description | Example |
|-------|--------|------|-------------|---------|
| Part ID | A | Text | Full part identifier | 02-00-04-PRT-MECH-0001 |
| Part Code | B | Text | Numeric code | 0001 |
| Category | C | Text | Part category | MECH, ELEC, IT, GSE, STD |
| Short Name | D | Text | Concise identifier | ConsoleSideBracket |
| Full Name | E | Text | Complete descriptive name | Console Side Mounting Bracket |
| Description | F | Text | Detailed description | Mounting bracket for console side panel attachment |
| Type | G | Text | COTS or CUSTOM | COTS / CUSTOM |
| Status | H | Text | Current status | WORKING, FOR_REVIEW, APPROVED, OBSOLETE |
| Created Date | I | Date | Creation date | 2025-11-17 |
| Modified Date | J | Date | Last modification | 2025-11-17 |

---

## Sheet 2: Physical Properties

| Field | Column | Type | Description | Example |
|-------|--------|------|-------------|---------|
| Part ID | A | Text | Reference to Part Info | 02-00-04-PRT-MECH-0001 |
| Material | B | Text | Primary material | Aluminum 6061-T6 |
| Material Standard | C | Text | Material spec standard | ASTM B209 |
| Surface Finish | D | Text | Finish specification | Anodized Clear per MIL-A-8625 |
| Mass (kg) | E | Number | Part mass in kilograms | 0.245 |
| Length (mm) | F | Number | Bounding box length | 150 |
| Width (mm) | G | Number | Bounding box width | 75 |
| Height (mm) | H | Number | Bounding box height | 25 |
| CoG X (mm) | I | Number | Center of gravity X | 75.0 |
| CoG Y (mm) | J | Number | Center of gravity Y | 37.5 |
| CoG Z (mm) | K | Number | Center of gravity Z | 12.5 |

---

## Sheet 3: Manufacturing & Procurement

| Field | Column | Type | Description | Example |
|-------|--------|------|-------------|---------|
| Part ID | A | Text | Reference to Part Info | 02-00-04-PRT-MECH-0001 |
| Manufacturing Process | B | Text | Primary process | CNC Machining |
| Special Operations | C | Text | Additional operations | Deburring, Anodizing |
| General Tolerance | D | Text | Default tolerance | ±0.1 mm |
| Critical Tolerances | E | Text | Special callouts | 2x Ø8.0 +0.05/-0.00 |
| Supplier | F | Text | Supplier name | MachineShop Co. |
| Manufacturer | G | Text | Manufacturer name | (same as supplier for custom) |
| Manufacturer P/N | H | Text | Mfr part number | (blank for custom) |
| Lead Time (days) | I | Number | Procurement lead time | 14 |
| MOQ | J | Number | Minimum order quantity | 10 |
| Unit Cost | K | Number | Cost per unit | (optional) |

---

## Sheet 4: Files & Documentation

| Field | Column | Type | Description | Example |
|-------|--------|------|-------------|---------|
| Part ID | A | Text | Reference to Part Info | 02-00-04-PRT-MECH-0001 |
| 3D File (STEP) | B | Text | Path to STEP file | 3D/02-00-04-PRT-MECH-0001_ConsoleSideBracket.step |
| 3D File (Native) | C | Text | Path to native CAD | 3D/02-00-04-PRT-MECH-0001_ConsoleSideBracket.prt |
| 2D Drawing (CAD) | D | Text | Path to drawing file | 2D/02-00-04-DWG-DET-PRT-MECH-0001-ConsoleSideBracket-SHT01-R01.dwg |
| 2D Drawing (PDF) | E | Text | Path to PDF | 2D/02-00-04-DWG-DET-PRT-MECH-0001-ConsoleSideBracket-SHT01-R01.pdf |
| Datasheet | F | Text | Path to datasheet | DATASHEETS/02-00-04-PRT-MECH-0001-Datasheet-R01.pdf |
| Specification | G | Text | Path to specification | DATASHEETS/02-00-04-PRT-MECH-0001-Specification-R01.pdf |
| Material Cert | H | Text | Path to cert | CERTS/02-00-04-PRT-MECH-0001-MaterialCert-R01.pdf |
| Test Report | I | Text | Path to test report | TEST/02-00-04-PRT-MECH-0001-TestReport-R01.pdf |

---

## Sheet 5: Traceability

| Field | Column | Type | Description | Example |
|-------|--------|------|-------------|---------|
| Part ID | A | Text | Reference to Part Info | 02-00-04-PRT-MECH-0001 |
| Related Assemblies | B | Text | Comma-separated list | 02-00-04-ASSY-A310, 02-00-04-ASSY-A311 |
| Related BoMs | C | Text | Comma-separated list | 02-00-04-A310_BOM, 02-00-04-A311_BOM |
| Related BIM Models | D | Text | Comma-separated list | BIM-MODEL-001 |
| Related Drawings | E | Text | Comma-separated list | 02-00-04-DWG-ASM-A310 |
| Requirements | F | Text | Comma-separated REQ IDs | REQ-02-001, REQ-02-015 |
| ODD References | G | Text | Comma-separated ODD IDs | ODD-01 |
| Safety/Hazards | H | Text | Comma-separated HZ IDs | HZ-02-0007 |
| Standard Reference | I | Text | ISO/DIN/ANSI standard | (if applicable) |

---

## Sheet 6: Maintenance & Notes

| Field | Column | Type | Description | Example |
|-------|--------|------|-------------|---------|
| Part ID | A | Text | Reference to Part Info | 02-00-04-PRT-MECH-0001 |
| Special Handling | B | Text | Handling requirements | Handle with care - anodized surface |
| Inspection Points | C | Text | Critical inspections | Check mounting hole alignment |
| Maintenance | D | Text | Maintenance schedule | Visual inspection every 6 months |
| Design Notes | E | Text | Design considerations | Optimized for weight reduction |
| Revision History | F | Text | Change history | R01: Initial release (2025-11-17) |

---

## Sheet 7: Document Control

| Field | Column | Type | Description | Example |
|-------|--------|------|-------------|---------|
| Part ID | A | Text | Reference to Part Info | 02-00-04-PRT-MECH-0001 |
| Originator | B | Text | Creator name/role | Jane Smith / Mechanical Engineer |
| Checker | C | Text | Reviewer name/role | John Doe / Senior Engineer |
| Approver | D | Text | Approver name/role | [To be assigned] |
| Created Date | E | Date | Initial creation | 2025-11-17 |
| Last Modified | F | Date | Last update | 2025-11-17 |
| Status | G | Text | Document status | WORKING |
| Notes | H | Text | Additional notes | AI-generated template requires human review |

---

## Usage Instructions

1. **Create Excel file** using this structure with named sheets
2. **Use data validation** for dropdown fields (Category, Type, Status)
3. **Apply cell formatting**:
   - Dates: YYYY-MM-DD format
   - Numbers: Appropriate decimal places
   - Text: Left-aligned
4. **Protect sheets** if needed to prevent accidental edits
5. **Use formulas** to link Part ID across sheets
6. **Add conditional formatting** for status indicators

---

## Notes

* This template provides a comprehensive metadata structure
* Not all fields are required for every part
* COTS parts may have fewer custom manufacturing details
* Standard parts (fasteners) may have simplified metadata
* Export to CSV for integration with other systems
