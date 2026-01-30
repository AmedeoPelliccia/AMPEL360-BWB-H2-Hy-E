# ICN — Illustration Control Number

## Overview

This directory contains **Illustrations and Graphics** for the Illustrated Parts Catalog (IPC), managed through the S1000D **Illustration Control Number (ICN)** system. Each graphic is assigned a unique ICN for identification and referencing.

## Purpose

The ICN directory provides:
- Centralized storage for all IPC graphical content
- Unique identification for each illustration
- Version control for graphics
- Multiple format support (SVG, PNG, JPG, etc.)
- Reusability across multiple Data Modules
- Simplified graphics management and updates

## Naming Convention

Illustrations follow the S1000D ICN structure:

```
ICN-AMPEL360-{ATA}-{SECTION}-{GRAPHIC_ID}-{VARIANT}_{SHEET}.{EXT}
```

### Components

- **Model ID**: `AMPEL360` (fixed)
- **ATA Chapter**: `23` (Communications)
- **Section**: `00-99` (per ATA SNS)
- **Graphic ID**: `0001` to `9999` (unique sequential number)
- **Variant**: `A-Z` (graphic variant for different configurations)
- **Sheet**: `000` to `999` (multi-sheet illustrations)
- **Extension**: File format (`.svg`, `.png`, `.jpg`, `.cgm`, `.tif`)

### Examples

**Exploded View (SVG)**:
```
ICN-AMPEL360-23-10-0001-A_001.SVG
```
*VHF radio assembly exploded view*

**Parts Breakdown Photo (PNG)**:
```
ICN-AMPEL360-23-10-0025-A_001.PNG
```
*Audio panel parts identification photo*

**Multi-Sheet IPB**:
```
ICN-AMPEL360-23-10-0200-A_001.SVG  (Sheet 1)
ICN-AMPEL360-23-10-0200-A_002.SVG  (Sheet 2)
ICN-AMPEL360-23-10-0200-A_003.SVG  (Sheet 3)
```
*HF antenna assembly breakdown (3 sheets)*

## Supported Formats

### Vector Graphics (Preferred)

**SVG (Scalable Vector Graphics)**:
- Recommended primary format for IPB
- Resolution-independent scaling
- Small file size
- Web and print compatible

**CGM (Computer Graphics Metafile)**:
- Legacy S1000D format
- Still widely used in aerospace
- Print-optimized

### Raster Graphics

**PNG (Portable Network Graphics)**:
- For photographs and screen captures
- Lossless compression
- Good quality at moderate file sizes

## Illustration Types

### Illustrated Parts Breakdowns (IPB)

**Exploded Views**:
- Assembly exploded views
- Subassembly breakdowns
- Mounting details

**Parts Identification**:
- Callout diagrams with item numbers
- Parts location views
- Reference designation diagrams

### Assembly Illustrations

**Assembly Drawings**:
- Component assembly views
- Installation details
- Mounting configurations

### Photographs

**Component Photos**:
- Parts identification photos
- As-manufactured condition
- Installation views

## Callouts and Labels

### In-Graphic Callouts

- Item numbers (1, 2, 3, etc.)
- Part callout lines
- Figure numbers
- Optional equipment indicators

### Parts Legend Integration

Graphics coordinate with parts lists:
- Item numbers match parts list entries
- Callouts reference specific parts
- Quantity and nomenclature in legend

## Referencing from Data Modules

Data Modules reference ICNs using the `<figure>` element:

```xml
<figure id="fig-0001">
  <title>VHF Radio Assembly</title>
  <graphic infoEntityIdent="ICN-AMPEL360-23-10-0001-A"/>
</figure>
```

## Best Practices

- **Clear Callouts**: Ensure item numbers are legible
- **Consistent Style**: Use standard exploded view conventions
- **Detailed Views**: Include insets for small parts
- **Complete Coverage**: All parts should be visible or referenced
- **Proper Orientation**: Standard viewing angles
- **File Size**: Optimize for web delivery

## Quality Checks

Before release, verify:
- ✅ Correct ICN assigned and labeled
- ✅ All parts visible and called out
- ✅ Item numbers match parts list
- ✅ Clear and readable at intended size
- ✅ Proper format and file size

## Validation

All illustrations must:
- Have valid, unique ICN codes
- Be in approved file formats
- Meet resolution and quality requirements
- Include required metadata
- Coordinate with parts lists

## Related Directories

- `../DM/` - Data Modules that reference illustrations
- `../PM/` - Publication Modules including illustrated DMs
- `../COMMON/` - Common graphics used across modules
- `../BREX/` - Validation rules for graphics

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-10-00 (Speech Communications)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
