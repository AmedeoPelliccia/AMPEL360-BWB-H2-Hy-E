# PNR Nomenclature Standard

**Document ID:** PNR-STD-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## 1. Introduction

This document defines the nomenclature standard for the AMPEL360 Part Number Reference (PNR) system used throughout the BWB H₂ Hy-E Q100 INTEGRA aircraft operational equipment.

## 2. Nomenclature Philosophy

The AMPEL360 PNR system is designed to be:
- **Intelligent** - Embedded meaning in the part number structure
- **Scalable** - Accommodates growth and new technologies
- **Industry-Compatible** - Aligns with ATA, S1000D, and MIL-STD standards
- **Human-Readable** - Logical structure for easy interpretation
- **System-Friendly** - Parseable by automated systems

## 3. Basic Format

### 3.1 Standard Structure

```
PNR-AA-BB-CCC-DD[-EE]
│   │  │   │   │   │
│   │  │   │   │   └─ Optional: Sub-component (Alpha or Numeric)
│   │  │   │   └───── Component Level (01-99)
│   │  │   └───────── Assembly Number (001-999)
│   │  └───────────── Subsystem Code (Alphanumeric)
│   └──────────────── ATA Chapter (00-99)
└──────────────────── Prefix (PNR = Part Number Reference)
```

### 3.2 Segment Definitions

#### Segment 1: Prefix (PNR)
- **Length:** 3 characters
- **Value:** Always "PNR"
- **Purpose:** Identifies as AMPEL360 part number

#### Segment 2: ATA Chapter (AA)
- **Length:** 2 digits
- **Range:** 00-99
- **Purpose:** Primary ATA chapter classification
- **Examples:** 02 (Operations), 28 (Fuel), 52 (Doors)

#### Segment 3: Subsystem Code (BB)
- **Length:** 2-4 characters
- **Type:** Numeric or alphanumeric
- **Purpose:** Specific subsystem or equipment type
- **Examples:**
  - `32` - H₂ Refueling Equipment
  - `GSE` - Ground Support Equipment
  - `CAOS` - Computer Aided Operations System

#### Segment 4: Assembly Number (CCC)
- **Length:** 3 digits
- **Range:** 001-999
- **Purpose:** Unique assembly identifier within subsystem
- **Format:** Leading zeros required (e.g., 001, 025, 150)

#### Segment 5: Component Level (DD)
- **Length:** 2 digits
- **Range:** 01-99
- **Purpose:** Hierarchical component breakdown
- **Optional:** Only used for sub-assemblies and components

#### Segment 6: Sub-component (EE)
- **Length:** 1-2 characters
- **Type:** Alpha (A-Z) or numeric
- **Purpose:** Detailed part breakdown or revision
- **Optional:** Used for fine-grained component identification

## 4. Subsystem Code Registry

### 4.1 Numeric Codes (ATA-Based)

| Code | Subsystem | ATA Reference |
|------|-----------|---------------|
| 10 | Flight Planning Systems | 02-10-00 |
| 20 | Weight & Balance Systems | 02-20-00 |
| 30 | Operations Management | 02-30-00 |
| 32 | H₂ Refueling Equipment | 02-32-00 |
| 40 | Ground Operations | 02-40-00 |

### 4.2 Alpha Codes (Special Systems)

| Code | Subsystem | Description |
|------|-----------|-------------|
| GSE | Ground Support Equipment | Towing, power, air start |
| EMG | Emergency Equipment | Response kits, fire suppression |
| CAOS | CAOS System | AI operations hardware/software |
| EFB | Electronic Flight Bag | Tablets and software |
| PUB | Publication Systems | S1000D tools, CSDB |
| SIM | Simulator Components | Training simulators |
| TRN | Training Devices | Training equipment |

## 5. Special Designators

### 5.1 Hardware vs Software

**Hardware:** Standard PNR format
- Example: `PNR-02-32-001` (Refueling Panel Assembly)

**Software:** Add `-SW` or use CAOS-SW prefix
- Example: `PNR-CAOS-SW-001` (CAOS Core System)

### 5.2 Kits and Sets

**Kit Indicator:** Use `-KIT` suffix or note in description
- Example: `PNR-02-32-001-03` (Seal Kit)

### 5.3 Consumables

**Consumable Indicator:** Use `-CON` suffix or note in type field
- Example: `PNR-02-EMG-001-05-CON` (Consumable supplies)

## 6. Revision and Version Control

### 6.1 Hardware Revisions

**Method:** Alpha suffix (A, B, C, etc.)
- Original: `PNR-02-32-001-01`
- Revision A: `PNR-02-32-001-01A`
- Revision B: `PNR-02-32-001-01B`

### 6.2 Software Versions

**Method:** Version number in description
- Example: `PNR-CAOS-SW-001` → "CAOS Core System v2.0"

### 6.3 Major Changes

**New Part Number Required When:**
- Form, fit, or function changes significantly
- Not interchangeable with previous version
- Different manufacturing process
- Significant cost impact

**Revision Suffix Used When:**
- Minor improvements
- Backward compatible
- Same form, fit, and function
- Interchangeable without modification

## 7. Special Cases

### 7.1 Multi-Use Components

For components used across multiple systems:
- Assign to primary system
- Document cross-references in registry
- Include in multiple PBS structures

### 7.2 Commercial Off-The-Shelf (COTS)

**Approach:**
- Assign AMPEL360 PNR
- Reference manufacturer part number in registry
- Include manufacturer CAGE code

**Example:**
- PNR: `PNR-CAOS-HW-001-01`
- Mfr P/N: NVIDIA A100-80GB
- CAGE: NV001

### 7.3 Assemblies with Options

**Method:** Use base PNR with configuration code
- Base: `PNR-02-EFB-001`
- With WiFi: `PNR-02-EFB-001-CFG-A`
- With WiFi+4G: `PNR-02-EFB-001-CFG-B`

## 8. Naming Conventions

### 8.1 Description Format

**Structure:** `[Component Type] [Specific Name] [Key Feature/Size]`

**Examples:**
- "Refueling Panel Assembly"
- "CPU Module 128GB"
- "Temperature Sensor Type-K"
- "Fire Extinguisher 5lb Halon"

### 8.2 Abbreviations

**Approved Abbreviations:**
- Assy - Assembly
- Comp - Component
- Sys - System
- Temp - Temperature
- Press - Pressure
- Ctrl - Control/Controller
- Mech - Mechanism
- Elect - Electrical/Electronic

### 8.3 Avoid

- Manufacturer-specific jargon
- Marketing names
- Ambiguous terms
- Special characters (except hyphen)

## 9. Data Management

### 9.1 Master Registry

All PNRs maintained in:
- `Master_Part_Number_Registry.csv`
- PLM system database
- ERP system

### 9.2 Required Fields

- Part_Number (unique)
- Description (full text)
- Type (Assembly/Component/Software/Kit)
- Category (system classification)
- Manufacturer (company name)
- CAGE_Code (5-char)
- Status (Active/Superseded/Obsolete)
- Unit_Cost_USD
- Lead_Time_Days

### 9.3 Optional Fields

- Manufacturer_Part_Number
- Drawing_Number
- Specification_Reference
- Weight
- Material
- Finish
- Shelf_Life

## 10. Quality Control

### 10.1 Validation Rules

1. Format compliance check
2. Duplicate number prevention
3. Sequence gap detection
4. CAGE code verification
5. Description completeness

### 10.2 Audit Trail

All PNR assignments logged with:
- Date and time
- Requesting engineer
- Approving authority
- ECO reference (if applicable)
- Reason for assignment

## 11. Integration with Standards

### 11.1 ATA iSpec 2200

PNR system aligns with ATA numbering:
- Chapter codes match ATA chapters
- Subsystem codes follow ATA breakdown
- Component hierarchy consistent with ATA levels

### 11.2 S1000D

PNR maps to Data Module Code (DMC):
- PNR used as reference in `<dmIdent>`
- Supports applicability cross-reference
- Enables publication integration

### 11.3 MIL-STD-130

Physical marking requirements:
- Human-readable PNR on label
- 2D barcode/QR code optional
- Tamper-evident marking for critical parts

## 12. References

- ATA iSpec 2200 - Air Transport Association Standard
- S1000D Issue 6.0 - International Technical Publications
- MIL-STD-130 - Identification Marking
- ISO 9001:2015 - Quality Management
- AS9100D - Aerospace Quality

## 13. Appendices

### Appendix A: Quick Reference Chart

| What | Example | Notes |
|------|---------|-------|
| Assembly | PNR-02-32-001 | Level 3 |
| Component | PNR-02-32-001-01 | Level 4 |
| Sub-component | PNR-02-32-001-01A | Level 5 |
| Software | PNR-CAOS-SW-001 | Version in description |
| Kit | PNR-02-32-001-03 | Type = Kit |
| Revision | -01A, -01B | Alpha suffix |

### Appendix B: Common Mistakes

1. ❌ Skipping leading zeros: `PNR-02-32-1` should be `PNR-02-32-001`
2. ❌ Inconsistent codes: Mixing numeric and alpha in same segment
3. ❌ Too specific descriptions: Avoid including temporary info
4. ❌ Missing CAGE codes: Always include manufacturer identifier
5. ❌ Reusing numbers: Never reuse retired PNRs

---

**Document Control:**
- **Version:** 1.0
- **Status:** Active
- **Approved By:** Configuration Management Lead
- **Next Review Date:** 2026-05-05
- **Owner:** Systems Engineering
