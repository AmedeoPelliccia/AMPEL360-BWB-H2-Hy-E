# APPLICABILITY — Applicability Statements

## Overview

This directory contains **Applicability** definitions and cross-reference files for the Illustrated Parts Catalog (IPC). Applicability defines which parts apply to which aircraft variants, configurations, modifications, and serial numbers.

## Purpose

Applicability management provides:
- Variant-specific parts filtering
- Configuration management support
- Serial number effectivity tracking
- Optional equipment handling
- Modification state management
- Product line differentiation
- Customer-specific parts catalogs

## What is Applicability?

**Applicability** answers the question: *"Does this part apply to this specific aircraft?"*

Factors determining applicability:
- **Aircraft Model**: Q100, Q80, Q120
- **Configuration**: Standard, Extended Range, Cargo
- **Serial Number**: Effectivity ranges
- **Modification State**: Pre/post-modification
- **Optional Equipment**: Customer-selectable systems
- **Time Period**: Temporary restrictions or updates

## File Types

### Applicability Cross-Reference Table (ACT)

Primary applicability file:
```
APPLICCROSS-AMPEL360-{PROJECT}_{ISSUE}.XML
```

Example:
```
APPLICCROSS-AMPEL360-Q100_001-00.XML
```

Contains:
- Product attribute definitions
- Assignment of attributes to products
- Applicability annotation definitions

### Product Cross-Reference Table (PCT)

Product variant definitions:
```
PCT-AMPEL360-{PRODUCT_LINE}_{ISSUE}.XML
```

Example:
```
PCT-AMPEL360-Q100_001-00.XML
```

## Applicability Types

### Model Applicability

**Aircraft Models**:
```xml
<productAttribute>
  <productAttributeCode>MODEL</productAttributeCode>
  <productAttributeValue>Q100</productAttributeValue>
  <productAttributeValue>Q80</productAttributeValue>
  <productAttributeValue>Q120</productAttributeValue>
</productAttribute>
```

### Configuration Applicability

**Configurations**:
```xml
<productAttribute>
  <productAttributeCode>CONFIG</productAttributeCode>
  <productAttributeValue>STANDARD</productAttributeValue>
  <productAttributeValue>EXTENDED_RANGE</productAttributeValue>
  <productAttributeValue>CARGO</productAttributeValue>
</productAttribute>
```

### Serial Number Effectivity

**Serial Number Ranges**:
```xml
<productAttribute>
  <productAttributeCode>SERIALNO</productAttributeCode>
  <productAttributeValue>001 AND UP</productAttributeValue>
  <productAttributeValue>100-150</productAttributeValue>
  <productAttributeValue>200 TO 999</productAttributeValue>
</productAttribute>
```

### Modification Applicability

**Modification States**:
```xml
<productAttribute>
  <productAttributeCode>MOD</productAttributeCode>
  <productAttributeValue>MOD-23-001-INSTALLED</productAttributeValue>
  <productAttributeValue>MOD-23-002-NOT-INSTALLED</productAttributeValue>
</productAttribute>
```

### Optional Equipment

**Customer Options**:
```xml
<productAttribute>
  <productAttributeCode>OPTION</productAttributeCode>
  <productAttributeValue>ENHANCED_VHF</productAttributeValue>
  <productAttributeValue>HF_RADIO</productAttributeValue>
  <productAttributeValue>SATCOM</productAttributeValue>
</productAttribute>
```

## Applicability in Data Modules

### Defining Applicability

Parts Data Modules declare applicability in the identification section:

```xml
<dmStatus>
  <applic>
    <assert applicPropertyIdent="MODEL" applicPropertyType="prodattr" applicPropertyValues="Q100"/>
    <assert applicPropertyIdent="CONFIG" applicPropertyType="prodattr" applicPropertyValues="STANDARD EXTENDED_RANGE"/>
  </applic>
</dmStatus>
```

### Part-Level Applicability

Individual parts can have specific applicability:

```xml
<partRef>
  <partIdent>PN-23-001-A</partIdent>
  <applic>
    <assert applicPropertyIdent="SERIALNO" applicPropertyValues="001-099"/>
  </applic>
</partRef>
```

## Publishing with Applicability

### Filtered Publications

Generate product-specific parts catalogs:
- Filter out non-applicable parts
- Include only relevant Data Modules
- Display only applicable parts
- Custom cover sheets with effectivity

### Example: Q100 Standard Config

```bash
# Generate catalog for Q100 Standard configuration
s1000d-publish \
  --product Q100 \
  --config STANDARD \
  --serialno "001 AND UP" \
  --output IPC-Q100-STD.pdf
```

### Dynamic Electronic Publications

**IETP (Interactive Electronic Technical Publications)**:
- User selects aircraft serial number
- System filters parts automatically
- Only applicable parts displayed
- Applicability indicators shown

## Effectivity Management

### Serial Number Effectivity

**From Serial Number**:
```
S/N 001 AND UP
```
*All aircraft from serial 001 onward*

**Serial Number Range**:
```
S/N 050 TO 150
```
*Aircraft 050 through 150 only*

### Modification Effectivity

**Service Bulletin (SB)**:
```
SB-23-001 ACCOMPLISHED
```
*Aircraft with completed Service Bulletin 23-001*

**Modification Kit**:
```
MOD-23-050 INSTALLED
```
*Aircraft with Modification Kit 23-050*

## Best Practices

- **Start Simple**: Begin with basic product attributes
- **Be Specific**: Clearly define each variant
- **Consistent Codes**: Use standard codes across all content
- **Document Decisions**: Record applicability rationale
- **Test Thoroughly**: Validate filtered outputs
- **User-Friendly**: Make applicability clear to readers

## Validation

Applicability must:
- ✅ Be defined in ACT/PCT files
- ✅ Use valid product attribute codes
- ✅ Reference existing product values
- ✅ Have logically consistent rules
- ✅ Validate against BREX rules
- ✅ Produce correct filtered output

## Reporting

Generate reports for:
- Parts by product variant
- Applicability coverage
- Missing applicability statements
- Orphaned applicability codes
- Effectivity summaries

## Related Directories

- `../DM/` - Data Modules with applicability statements
- `../PM/` - Publication Modules filtered by applicability
- `../COMMON/` - Common information that may be variant-specific
- `../BREX/` - Validation rules for applicability

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-10-00 (Speech Communications)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia

## References

- S1000D Issue 5.0 Specification - Chapter 3.9.6 (Product Cross-Reference Table)
- AMPEL360 Product Variant Management Guide
- Applicability Best Practices Guide
