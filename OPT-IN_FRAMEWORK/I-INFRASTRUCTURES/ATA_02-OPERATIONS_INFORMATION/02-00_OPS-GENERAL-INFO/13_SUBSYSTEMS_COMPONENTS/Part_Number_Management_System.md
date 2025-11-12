# Part Number Management System

**Document ID:** PNR-SYS-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## 1. Overview

The AMPEL360 Part Number (PNR) Management System provides a comprehensive, intelligent part numbering scheme for all operational equipment, components, and systems used in the BWB H₂ Hy-E Q100 INTEGRA aircraft operations.

## 2. Purpose

This system ensures:
- **Unique identification** of all parts, assemblies, and systems
- **Traceability** throughout the product lifecycle
- **Interoperability** with industry standards (ATA, S1000D, MIL-STD-130)
- **Configuration management** and change control
- **Supply chain integration** with manufacturer CAGE codes

## 3. Part Number Structure

### 3.1 Standard Format

**General Format:** `PNR-AA-BB-CCC-DD`

| Segment | Description | Length | Example |
|---------|-------------|--------|---------|
| **PNR** | Part Number Reference (prefix) | 3 chars | PNR |
| **AA** | ATA chapter code | 2 digits | 02 |
| **BB** | Subsystem/category code | 2-3 chars | 32, GSE, EFB |
| **CCC** | Sequential assembly number | 3 digits | 001 |
| **DD** | Component level (optional) | 2 digits | 01 |

### 3.2 Subsystem Codes

| Code | Subsystem | Example |
|------|-----------|---------|
| **32** | H₂ Refueling Equipment | PNR-02-32-001 |
| **GSE** | Ground Support Equipment | PNR-02-GSE-001 |
| **EMG** | Emergency Equipment | PNR-02-EMG-001 |
| **CAOS-HW** | CAOS Hardware | PNR-CAOS-HW-001 |
| **CAOS-SW** | CAOS Software | PNR-CAOS-SW-001 |
| **EFB** | Electronic Flight Bag | PNR-02-EFB-001 |
| **PUB** | Publication Systems | PNR-02-PUB-001 |
| **SIM** | Simulator Components | PNR-02-SIM-001 |
| **TRN** | Training Devices | PNR-02-TRN-001 |

### 3.3 Component Hierarchy Levels

- **Level 1 (System):** PNR-02-32-000 (H₂ Refueling System)
- **Level 2 (Subsystem):** PNR-02-32-001 (Refueling Panel Assembly)
- **Level 3 (Assembly):** PNR-02-32-001-01 (Panel Door)
- **Level 4 (Component):** PNR-02-32-001-01A (Door Hinge)

## 4. Part Number Categories

### 4.1 By Type

| Type | Description | Example |
|------|-------------|---------|
| **Assembly** | Multi-component assembly | PNR-02-32-001 |
| **Component** | Individual part | PNR-02-32-001-01 |
| **Software** | Software module/package | PNR-CAOS-SW-001 |
| **Kit** | Collection of parts | PNR-02-32-001-03 (Seal Kit) |
| **Consumable** | Single-use items | PNR-02-EMG-001-05 |

### 4.2 By Status

| Status | Description | Usage |
|--------|-------------|-------|
| **Active** | Current production/use | Standard parts |
| **Superseded** | Replaced by newer part | Cross-referenced to new PNR |
| **Obsolete** | No longer available | Documented for legacy |
| **Developmental** | In design/testing | Pre-production |
| **Discontinued** | Manufacturer stopped production | Seek alternatives |

## 5. CAGE Code Integration

All parts include Commercial and Government Entity (CAGE) codes:

**Format:** 5-character alphanumeric code identifying manufacturer

**Examples:**
- **A3MP0** - AMPEL360 (in-house design)
- **AC123** - AeroComposite (external supplier)
- **HT789** - H2Tech (H₂ equipment specialist)
- **NV001** - NVIDIA (computing hardware)

## 6. Master Part Number Registry

The Master Part Number Registry (Master_Part_Number_Registry.csv) contains:

| Field | Description |
|-------|-------------|
| Part_Number | Unique PNR identifier |
| Description | Full part description |
| Type | Assembly/Component/Software/Kit |
| Category | System category |
| Manufacturer | Company name |
| CAGE_Code | 5-character manufacturer code |
| Status | Active/Superseded/Obsolete |
| Unit_Cost_USD | Current unit cost |
| Lead_Time_Days | Standard lead time |

## 7. Part Number Assignment Process

### 7.1 New Part Number Request

1. **Requester** submits PNR request via engineering system
2. **Engineering** reviews for existing similar parts
3. **PNR Administrator** assigns next available number
4. **Quality** verifies compliance with standards
5. **Configuration Management** publishes to registry

### 7.2 Assignment Rules

- Sequential numbering within each category
- No reuse of retired part numbers
- Minimum 5-year hold on superseded numbers
- Document all cross-references

## 8. Revision and Change Control

### 8.1 Revision Designators

- **Numeric versions** for software (v1.0, v2.0)
- **Alpha suffixes** for hardware (01A, 01B)
- Major changes require new part number
- Minor changes use revision suffix

### 8.2 Engineering Change Orders (ECO)

All part number changes tracked via ECO system:
- ECO number assigned
- Reason for change documented
- Effectivity specified (serial numbers, dates)
- Cross-references maintained

## 9. Interchangeability

### 9.1 Types of Interchangeability

| Type | Description | Example |
|------|-------------|---------|
| **Direct** | Exact replacement, no modifications | PNR-02-32-001-01 → 01A |
| **Form-Fit-Function** | Different manufacturer, same specs | PNR-02-EFB-001 → 001B |
| **Conditional** | Requires modification/update | PNR-CAOS-HW-001-02 → 02C |

### 9.2 Interchangeability Matrix

Maintained in `Interchangeability_Matrix.csv` with:
- Primary and alternate part numbers
- Interchange type and approval status
- Any restrictions or requirements
- Engineering approval documentation

## 10. Integration with Other Systems

### 10.1 S1000D Data Modules

Each part number maps to S1000D Data Module Codes (DMC) for technical publications.

### 10.2 ERP/PLM Systems

PNR system interfaces with:
- Enterprise Resource Planning (ERP) for procurement
- Product Lifecycle Management (PLM) for engineering
- Maintenance Management System (MMS) for operations

### 10.3 Digital Product Passport

Each part number linked to Digital Product Passport (ATA 95) containing:
- Complete lifecycle history
- Certification documentation
- Maintenance records
- Sustainability metrics

## 11. Quality and Compliance

### 11.1 Standards Compliance

- **ATA iSpec 2200** - Technical data standards
- **S1000D Issue 6.0** - Technical publications
- **ISO 9001:2015** - Quality management
- **AS9100D** - Aerospace quality
- **MIL-STD-130** - Identification marking

### 11.2 Audit Trail

All part number activities logged:
- Creation date and author
- All revisions and changes
- ECO references
- Usage in assemblies

## 12. Training and Access

### 12.1 User Roles

| Role | Permissions |
|------|-------------|
| **PNR Administrator** | Create, modify, retire part numbers |
| **Engineer** | Request new PNRs, propose changes |
| **Quality** | Review and approve PNRs |
| **Supply Chain** | View, export data |
| **Read-Only** | View only access |

### 12.2 Training Requirements

- All engineers: PNR system overview (2 hours)
- PNR Administrators: Full system training (8 hours)
- Annual refresher training required

## 13. Continuous Improvement

### 13.1 Metrics

Track and report:
- Number of part numbers created per month
- Time to assign new part numbers
- Number of obsolete parts
- Interchangeability utilization rate

### 13.2 System Reviews

- Quarterly system audits
- Annual process review
- Continuous feedback from users

## 14. References

- Component_Breakdown_Structure.md
- Master_Part_Number_Registry.csv
- PART_NUMBER_STRUCTURE/Intelligent_Part_Numbering_Scheme.md
- CONFIGURATION_CONTROL/Configuration_Management_Plan.md

---

**Document Control:**
- **Version:** 1.0
- **Status:** Active
- **Approved By:** Engineering Manager
- **Next Review Date:** 2026-05-05
- **Owner:** Configuration Management
