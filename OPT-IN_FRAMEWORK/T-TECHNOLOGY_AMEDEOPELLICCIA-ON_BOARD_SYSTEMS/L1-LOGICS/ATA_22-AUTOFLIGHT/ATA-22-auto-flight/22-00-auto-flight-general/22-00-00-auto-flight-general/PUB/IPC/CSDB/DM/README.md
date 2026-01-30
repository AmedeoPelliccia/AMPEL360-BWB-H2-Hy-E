# DM — Data Modules (IPC)

## Overview

This directory contains **Data Modules (DM)** for the Illustrated Parts Catalog (IPC). Data Modules are the fundamental building blocks of S1000D parts catalog publications.

## Purpose

IPC Data Modules are self-contained units containing:
- Parts lists with item numbers and nomenclature
- Part number and nomenclature information
- Illustrated parts breakdowns
- Quantity and applicability information
- Reference designation and location data
- Vendor and ordering information

## Naming Convention

```
DMC-AMPEL360-{ATA}-{SECTION}-{SUBJECT}-{INFO_CODE}-{VARIANT}-{ITEM_LOCATION}_XXX_00_{LANG}_{ISSUE}.XML
```

### IPC-Specific Info Codes

| Code | Description | Use Case |
|------|-------------|----------|
| **041A** | Illustrated Parts Data | Parts lists with illustrations |
| **942A** | Illustrated Parts Data - IPL | Interactive parts lists |
| **005A** | Applicability Data | Parts applicability cross-reference |

### Examples

**Illustrated Parts List**:
```
DMC-AMPEL360-22-00-00-041A-A-A_001_00_EN-US_001-00.XML
```
*Autoflight system complete parts list*

**Subassembly Parts**:
```
DMC-AMPEL360-22-10-00-041A-A-001_001_00_EN-US_001-00.XML
```
*Autopilot controller parts breakdown*

**Component Parts List**:
```
DMC-AMPEL360-22-20-00-041A-A-002_001_00_EN-US_001-00.XML
```
*Flight director components*

## Content Structure

Each IPC Data Module typically contains:

### Illustrated Parts List (IPL)

```xml
<catalogSeqNumber>
  <catalogSeqNumberValue>C-001</catalogSeqNumberValue>
  <itemSeqNumber>
    <partRef>
      <partNumber>PN-AMPEL360-22-1000-A</partNumber>
      <partName>Autopilot Computer Unit</partName>
    </partRef>
    <quantityPerNextHigherAssy>1</quantityPerNextHigherAssy>
    <applicability>
      <assert applicPropertyIdent="MODEL" applicPropertyValues="Q100"/>
    </applicability>
  </itemSeqNumber>
</catalogSeqNumber>
```

### Key Information

Each parts entry includes:
- **Item Number**: Sequential reference number (1, 2, 3, etc.)
- **Part Number**: Full part number with revision
- **Nomenclature**: Part name/description
- **Quantity**: Units required per assembly
- **Reference Designation**: Electrical/mechanical designation
- **CAGE Code**: Commercial and Government Entity code
- **Unit of Issue**: EA (each), SET, KIT, etc.
- **Applicability**: Which aircraft/configs use this part

## Parts Data Organization

### Hierarchical Structure

**Level 1 - System**:
```
Autoflight System (ATA 22)
```

**Level 2 - Subsystem**:
```
├── Autopilot (22-10)
├── Flight Director (22-20)
└── Yaw Damper (22-30)
```

**Level 3 - Assembly**:
```
    ├── Control Panel Assembly
    ├── Computer Unit Assembly
    └── Actuator Assembly
```

**Level 4 - Components**:
```
        ├── Circuit Boards
        ├── Connectors
        └── Hardware
```

## Part Number Format

AMPEL360 part numbering:
```
PN-AMPEL360-{ATA}-{SEQUENCE}-{REV}
```

Example:
```
PN-AMPEL360-22-1000-A
```
- ATA: 22 (Autoflight)
- Sequence: 1000
- Revision: A

## Reference Designation

Electrical/electronic components:
- **A**: Assembly
- **U**: Unit (integrated circuit, module)
- **J**: Connector
- **R**: Resistor
- **C**: Capacitor
- **CR**: Diode
- **Q**: Transistor

Example: `U1`, `J5`, `A10`

## Effectivity and Applicability

### Serial Number Effectivity

```xml
<partEffectivity>
  <effectivityCode>001 AND UP</effectivityCode>
</partEffectivity>
```

### Configuration Applicability

```xml
<applicability>
  <assert applicPropertyIdent="CONFIG" applicPropertyValues="STANDARD"/>
</applicability>
```

### Optional Equipment

```xml
<applicability>
  <assert applicPropertyIdent="OPTION" applicPropertyValues="ENHANCED_AUTOPILOT"/>
</applicability>
```

## Vendor and Procurement

### Vendor Information

```xml
<manufacturerCode>VEND001</manufacturerCode>
<manufacturerName>Autopilot Systems Inc.</manufacturerName>
<cageCode>12345</cageCode>
```

### Procurement Details

- Lead time
- Minimum order quantity
- Unit price (if applicable)
- Source control drawings
- Alternate part numbers

## Illustration References

Link parts to figures:
```xml
<refs>
  <figureRef>
    <figureNumber>001</figureNumber>
    <figureTitle>Autopilot System Installation</figureTitle>
  </figureRef>
</refs>
```

## Interchangeability

### Substitute Parts

```xml
<interchangeabilityGroup>
  <primaryPart>
    <partNumber>PN-AMPEL360-22-1000-A</partNumber>
  </primaryPart>
  <substitutePart>
    <partNumber>PN-ALT-22-1000-B</partNumber>
    <substituteRestriction>Form, fit, function equivalent</substituteRestriction>
  </substitutePart>
</interchangeabilityGroup>
```

## Best Practices

- **Accuracy**: Verify all part numbers and nomenclature
- **Completeness**: Include all parts down to line-replaceable units
- **Clarity**: Use clear, unambiguous nomenclature
- **Consistency**: Maintain consistent terminology
- **Traceability**: Link to engineering drawings and specifications
- **Currency**: Keep effectivity and applicability current
- **Procurement**: Include vendor and ordering information

## Validation

IPC Data Modules must:
- Validate against S1000D schema
- Comply with BREX rules for IPC
- Have accurate part numbers
- Include all required fields
- Match illustrations (ICN files)
- Pass cross-reference checks

## Related Directories

- `../PM/` - Publication Modules organizing IPC structure
- `../ICN/` - Exploded view illustrations
- `../DML/` - Parts lists grouped by assembly
- `../APPLICABILITY/` - Product variant applicability

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 22 (Autoflight)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
