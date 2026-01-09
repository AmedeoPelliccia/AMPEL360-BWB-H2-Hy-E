# APPLICABILITY — Applicability Statements

## Overview

This directory contains **Applicability** definitions and cross-reference files for the Illustrated Parts Catalog (IPC). Applicability defines which technical content applies to which aircraft variants, configurations, modifications, and serial numbers.

## Purpose

Applicability management provides:
- Variant-specific content filtering
- Configuration management support
- Serial number effectivity tracking
- Optional equipment handling
- Modification state management
- Product line differentiation
- Customer-specific documentation

## What is Applicability?

**Applicability** answers the question: *"Does this content apply to this specific aircraft?"*

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
  <productAttributeValue>MOD-22-001-INSTALLED</productAttributeValue>
  <productAttributeValue>MOD-22-002-NOT-INSTALLED</productAttributeValue>
</productAttribute>
```

### Optional Equipment

**Customer Options**:
```xml
<productAttribute>
  <productAttributeCode>OPTION</productAttributeCode>
  <productAttributeValue>ENHANCED_AUTOPILOT</productAttributeValue>
  <productAttributeValue>AUTOLAND</productAttributeValue>
  <productAttributeValue>CATIIIB</productAttributeValue>
</productAttribute>
```

## Applicability in Data Modules

### Defining Applicability

Data Modules declare applicability in the identification section:

```xml
<dmStatus>
  <applic>
    <assert applicPropertyIdent="MODEL" applicPropertyType="prodattr" applicPropertyValues="Q100"/>
    <assert applicPropertyIdent="CONFIG" applicPropertyType="prodattr" applicPropertyValues="STANDARD EXTENDED_RANGE"/>
  </applic>
</dmStatus>
```

### Complex Applicability

**AND Logic** (all conditions must be true):
```xml
<applic>
  <assert applicPropertyIdent="MODEL" applicPropertyValues="Q100"/>
  <assert applicPropertyIdent="SERIALNO" applicPropertyValues="100 AND UP"/>
</applic>
```

**OR Logic** (any condition true):
```xml
<applic>
  <evaluate andOr="or">
    <assert applicPropertyIdent="CONFIG" applicPropertyValues="STANDARD"/>
    <assert applicPropertyIdent="CONFIG" applicPropertyValues="EXTENDED_RANGE"/>
  </evaluate>
</applic>
```

**NOT Logic** (exclusion):
```xml
<applic>
  <evaluate andOr="and">
    <assert applicPropertyIdent="MODEL" applicPropertyValues="Q100"/>
    <assert applicPropertyIdent="MOD" applicPropertyValues="MOD-22-001-NOT-INSTALLED"/>
  </evaluate>
</applic>
```

## Applicability Annotation

### In-content Applicability

Mark specific paragraphs or steps:

```xml
<para>
  <applic>
    <assert applicPropertyIdent="OPTION" applicPropertyValues="ENHANCED_AUTOPILOT"/>
  </applic>
  This step applies only to aircraft with Enhanced Autopilot option.
</para>
```

### Visual Indicators

Publishing systems can display:
- Icons indicating applicable variants
- Shading for optional content
- Brackets or markers for effectivity
- Tooltips with applicability details

## Product Variants

### AMPEL360 Q-Series

**Q100 (100-passenger baseline)**:
- Standard configuration
- Extended range variant
- Primary development focus

**Q80 (80-passenger compact)**:
- Shorter fuselage
- Reduced range
- Shares most systems with Q100

**Q120 (120-passenger extended)**:
- Extended fuselage
- Increased capacity
- Modified fuel system

### Configuration Variants

**Standard**:
- Baseline systems
- Standard range (3,500 km)
- Standard passenger capacity

**Extended Range**:
- Additional fuel capacity
- Modified fuel management
- Range: 4,200 km

**Cargo**:
- No passenger seats
- Cargo loading system
- Modified cabin configuration

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

**Before Serial Number**:
```
S/N 001 TO 099
```
*Early production aircraft*

### Modification Effectivity

**Service Bulletin (SB)**:
```
SB-22-001 ACCOMPLISHED
```
*Aircraft with completed Service Bulletin 22-001*

**Modification Kit**:
```
MOD-22-050 INSTALLED
```
*Aircraft with Modification Kit 22-050*

**Pre-Mod / Post-Mod**:
```
BEFORE MOD-22-025
AFTER MOD-22-025
```

## Publishing with Applicability

### Filtered Publications

Generate product-specific manuals:
- Filter out non-applicable content
- Include only relevant Data Modules
- Display only applicable procedures
- Custom cover sheets with effectivity

### Example: Q100 Standard Config

```bash
# Generate manual for Q100 Standard configuration
s1000d-publish \
  --product Q100 \
  --config STANDARD \
  --serialno "001 AND UP" \
  --output AMM-Q100-STD.pdf
```

### Dynamic Electronic Publications

**IETP (Interactive Electronic Technical Publications)**:
- User selects aircraft serial number
- System filters content automatically
- Only applicable content displayed
- Applicability indicators shown

## Workflow

### Content Creation

1. **Define Products**: Establish product attributes
2. **Create ACT**: Build cross-reference table
3. **Author Content**: Create Data Modules
4. **Assign Applicability**: Tag content appropriately
5. **Validate**: Check applicability logic
6. **Publish**: Generate variant-specific outputs

### Maintenance

1. **Track Changes**: Monitor product variants
2. **Update ACT**: Add new products/modifications
3. **Review Content**: Verify applicability accuracy
4. **Revalidate**: Check logic after changes
5. **Republish**: Generate updated manuals

## Best Practices

- **Start Simple**: Begin with basic product attributes
- **Be Specific**: Clearly define each variant
- **Consistent Codes**: Use standard codes across all content
- **Document Decisions**: Record applicability rationale
- **Test Thoroughly**: Validate filtered outputs
- **User-Friendly**: Make applicability clear to readers
- **Future-Proof**: Design for product expansion

## Common Applicability Patterns

### New Optional Equipment

```xml
<!-- Aircraft with new option -->
<applic>
  <assert applicPropertyIdent="OPTION" applicPropertyValues="NEW_FEATURE"/>
</applic>
```

### Retrofit Modification

```xml
<!-- Can be pre-mod or post-mod -->
<applic>
  <evaluate andOr="or">
    <assert applicPropertyIdent="MOD" applicPropertyValues="BEFORE_MOD_22_100"/>
    <assert applicPropertyIdent="MOD" applicPropertyValues="AFTER_MOD_22_100"/>
  </evaluate>
</applic>
```

### Serial Number Cutover

```xml
<!-- Production change at specific S/N -->
<applic>
  <evaluate andOr="or">
    <assert applicPropertyIdent="SERIALNO" applicPropertyValues="001-199"/>
    <!-- Old design -->
    <assert applicPropertyIdent="SERIALNO" applicPropertyValues="200 AND UP"/>
    <!-- New design -->
  </evaluate>
</applic>
```

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
- Content by product variant
- Applicability coverage
- Missing applicability statements
- Orphaned applicability codes
- Effectivity summaries

## Related Directories

- `../DM/` - Data Modules with applicability statements
- `../PM/` - Publication Modules filtered by applicability
- `../COMMON/` - Common information that may be variant-specific
- `../BREX/` - Validation rules for applicability

## Tools

Software supporting applicability:
- **S1000D Publishing Tools**: Filter by product attributes
- **IETP Systems**: Dynamic applicability filtering
- **CMS**: Applicability-aware content management
- **Validation Tools**: Check applicability logic

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 22 (Autoflight)
- **Publication Type**: AMM (Aircraft Maintenance Manual)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia

## References

- S1000D Issue 5.0 Specification - Chapter 3.9.6 (Product Cross-Reference Table)
- AMPEL360 Product Variant Management Guide
- Applicability Best Practices Guide
