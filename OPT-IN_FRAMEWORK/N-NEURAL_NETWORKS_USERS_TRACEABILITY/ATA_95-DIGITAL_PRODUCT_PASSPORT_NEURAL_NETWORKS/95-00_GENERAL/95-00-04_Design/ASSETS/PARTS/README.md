# PARTS - Design Layer

**Purpose**: This directory contains individual part-level documentation for hardware components and discrete software modules within the DPP+NN system.

## Structure

### 01_SYSTEM_LEVEL
System-level part definitions (e.g., complete IMA module, NPU accelerator card)

### 02_SUBSYSTEM_LEVEL
Subsystem-level parts organized by functional domain:
- Hardware components (sensors, processors, memory modules)
- Software modules (libraries, drivers, firmware)

### 03_INTERFACE_VIEWS
Part-level interface specifications:
- Connector pinouts
- Software APIs
- Communication protocols

### 04_VARIANTS
Variant-specific part configurations:
- **Q100**: Baseline parts list
- **Q80**: Cost-optimized parts
- **Q120**: Enhanced capability parts

### 99_ARCHIVE
Deprecated parts and obsolete components

## Naming Convention

All part documents follow this pattern:
```
95-00-04-P<nnn>_<Part_Name>.md
```

Where:
- `95-00-04`: ATA 95, chapter 00, section 04 (Design)
- `P<nnn>`: Part number (e.g., P001, P010, P020)
- `<Part_Name>`: Descriptive name using underscores

## Parts Hierarchy

Parts are related to assemblies via Bill of Materials (BOM) structures:
- Each assembly document references its constituent parts
- Parts may be shared across multiple assemblies
- Part substitution and alternates are documented

## Usage Guidelines

1. **Part Selection**: Choose parts based on assembly requirements
2. **Compatibility**: Verify part compatibility with target assemblies
3. **Procurement**: Link to approved vendor list and part numbers
4. **Quality**: Document certification and quality standards
5. **Lifecycle**: Track part obsolescence and replacement paths

## Traceability

All parts must trace to:
- **Assemblies**: Which assemblies use this part
- **Requirements**: Functional and performance requirements
- **Suppliers**: Approved vendors and manufacturers
- **Certification**: Compliance with aviation standards

## Document Control

- **Standard**: AMPEL360 Assets Standard
- **Owner**: AMPEL360 Design WG
- **Review Frequency**: Annual or upon part change
- **Status**: Active development

## Related Documents

- [ASSEMBLIES](../ASSEMBLIES/README.md) - Assembly-level documentation
- [INSTALLATIONS](../INSTALLATIONS/README.md) - Installation procedures
