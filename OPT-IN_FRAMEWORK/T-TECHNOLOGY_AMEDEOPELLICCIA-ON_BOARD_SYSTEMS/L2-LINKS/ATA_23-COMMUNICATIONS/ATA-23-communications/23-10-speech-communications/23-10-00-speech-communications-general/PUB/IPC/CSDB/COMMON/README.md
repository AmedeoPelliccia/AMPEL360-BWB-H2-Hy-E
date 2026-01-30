# COMMON — Common Information Sets

## Overview

This directory contains **Common Information Sets** (also called Common Information Repositories or CIR) for the Illustrated Parts Catalog (IPC). These are reusable content fragments that can be referenced from multiple Data Modules.

## Purpose

Common Information Sets provide:
- Centralized storage for reusable parts content
- Single-source maintenance for shared information
- Consistency across parts documentation
- Efficient updates (change once, apply everywhere)
- Reduced translation costs
- Simplified content management

## What are Common Information Sets?

Common Information Sets are **reusable content fragments** such as:
- Standard notes and warnings
- Common parts information
- Vendor information
- Standard text blocks
- Abbreviation lists
- Standard legends

Instead of copying the same content into multiple Data Modules, authors **reference** common information, which is stored once and included dynamically.

## Naming Convention

Common Information files follow this structure:

```
COM-AMPEL360-{TYPE}-{ID}_{LANG}_{ISSUE}.XML
```

### Components

- **Model ID**: `AMPEL360` (fixed)
- **Type**: Category of common information
  - `NOTE` - Standard notes
  - `WARNING` - Safety warnings
  - `VENDOR` - Vendor information
  - `LEGEND` - Standard legends
  - `ABBR` - Abbreviations and acronyms
- **ID**: `00001` to `99999` (unique identifier)
- **Language**: `EN-US`, `FR-FR`, etc. (ISO language codes)
- **Issue**: `001-00` to `999-99` (issue number)

### Examples

**Standard Note**:
```
COM-AMPEL360-NOTE-00001_EN-US_001-00.XML
```
*Standard parts ordering note*

**Vendor Information**:
```
COM-AMPEL360-VENDOR-00010_EN-US_001-00.XML
```
*Common vendor contact information*

**Standard Legend**:
```
COM-AMPEL360-LEGEND-00001_EN-US_001-00.XML
```
*Standard IPB legend format*

## Content Types

### Standard Notes

**Parts Information Notes**:
```xml
<note>
  <noteIdent>COM-AMPEL360-NOTE-00001</noteIdent>
  <noteText>
    <para>
      When ordering replacement parts, specify aircraft serial number 
      and modification status.
    </para>
  </noteText>
</note>
```

### Vendor Information

**Standard Vendor Data**:
```xml
<commonInfo>
  <commonInfoIdent>COM-AMPEL360-VENDOR-00001</commonInfoIdent>
  <vendorInfo>
    <vendorCode>V12345</vendorCode>
    <vendorName>Example Vendor Inc.</vendorName>
    <vendorContact>parts@example.com</vendorContact>
  </vendorInfo>
</commonInfo>
```

### Standard Legends

**IPB Legend**:
```xml
<commonInfo>
  <commonInfoIdent>COM-AMPEL360-LEGEND-00001</commonInfoIdent>
  <legend>
    <legendEntry>
      <symbol>*</symbol>
      <meaning>Item not illustrated</meaning>
    </legendEntry>
    <legendEntry>
      <symbol>AR</symbol>
      <meaning>As Required</meaning>
    </legendEntry>
  </legend>
</commonInfo>
```

## Referencing Common Information

### From Data Modules

Reference common information using `<commonInfoRef>`:

```xml
<partsList>
  <commonInfoRef>
    <commonInfoRefIdent>
      <commonInfoCode>COM-AMPEL360-LEGEND-00001</commonInfoCode>
    </commonInfoRefIdent>
  </commonInfoRef>
  <!-- Parts list entries -->
</partsList>
```

### In-context Inclusion

Common information is included inline when document is published:
- Content appears seamlessly in output
- Authors don't duplicate content
- Updates propagate automatically

## Benefits

### Consistency

- Same legend appears identically everywhere
- Standardized vendor information
- Uniform notes and instructions

### Efficiency

- Create once, use many times
- Update once, apply everywhere
- Reduced authoring time

### Translation

- Translate common content once
- Reuse translations across all modules
- Lower translation costs

## Common Information Categories

### Parts Information

- Standard notes for ordering
- Interchangeability notes
- Supersession information

### Vendor Data

- Approved vendor lists
- Contact information
- Cage codes

### Legends and Symbols

- Standard IPB legends
- Symbol definitions
- Abbreviation lists

## Best Practices

- **Clear Identification**: Use descriptive identifiers
- **Appropriate Granularity**: Not too large, not too small
- **Context-Independence**: Design for multiple contexts
- **Proper Scope**: Ensure content is truly common
- **Documentation**: Document intended use

## Validation

Common Information must:
- Validate against S1000D schema
- Comply with BREX rules
- Be context-independent
- Have unique identifiers
- Include complete metadata

## Related Directories

- `../DM/` - Data Modules that reference common information
- `../PM/` - Publication Modules including DMs with common refs
- `../BREX/` - Validation rules for common information
- `../APPLICABILITY/` - May filter common information by variant

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

- S1000D Issue 5.0 Specification - Chapter 3.9.5 (Common Information Repositories)
- AMPEL360 Common Information Guidelines
- Reusable Content Best Practices
