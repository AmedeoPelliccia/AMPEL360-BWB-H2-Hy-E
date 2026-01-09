# ICN — Illustration Control Number

## Overview

This directory contains **Illustrations and Graphics** for the Aircraft Maintenance Manual (AMM), managed through the S1000D **Illustration Control Number (ICN)** system. Each graphic is assigned a unique ICN for identification and referencing.

## Purpose

The ICN directory provides:
- Centralized storage for all graphical content
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

**System Diagram (SVG)**:
```
ICN-AMPEL360-23-10-0001-A_001.SVG
```
*Speech communications system block diagram*

**Component Photo (PNG)**:
```
ICN-AMPEL360-23-10-0025-A_001.PNG
```
*VHF radio control panel photograph*

**Wiring Diagram (SVG)**:
```
ICN-AMPEL360-23-10-0100-A_001.SVG
```
*Audio distribution wiring schematic*

**Multi-Sheet Drawing**:
```
ICN-AMPEL360-23-10-0200-A_001.SVG  (Sheet 1)
ICN-AMPEL360-23-10-0200-A_002.SVG  (Sheet 2)
ICN-AMPEL360-23-10-0200-A_003.SVG  (Sheet 3)
```
*HF antenna installation (3 sheets)*

## Supported Formats

### Vector Graphics (Preferred)

**SVG (Scalable Vector Graphics)**:
- Recommended primary format
- Resolution-independent scaling
- Small file size
- Web and print compatible
- Editable with standard tools

**CGM (Computer Graphics Metafile)**:
- Legacy S1000D format
- Still widely used in aerospace
- Requires specialized viewers
- Print-optimized

### Raster Graphics

**PNG (Portable Network Graphics)**:
- For photographs and screen captures
- Lossless compression
- Transparency support
- Good quality at moderate file sizes

**JPG/JPEG**:
- For photographs only
- Lossy compression
- Smaller file sizes
- Not suitable for line drawings

**TIFF**:
- High-quality raster format
- Large file sizes
- Archive and print quality

## Illustration Types

### Technical Drawings

**System Diagrams**:
- Block diagrams
- Functional flow diagrams
- System interconnection diagrams

**Schematic Diagrams**:
- Electrical schematics
- RF distribution diagrams
- Audio signal flow diagrams

**Installation Drawings**:
- Component location diagrams
- Installation details
- Antenna routing diagrams

### Exploded Views

**Assembly Illustrations**:
- Exploded part views
- Assembly sequence diagrams
- Subassembly breakdowns

**Parts Identification**:
- Callout diagrams
- Parts location views
- Reference designation diagrams

### Photographs

**Component Photos**:
- Installed component views
- Component identification
- As-removed condition documentation

**Maintenance Actions**:
- Procedure step illustrations
- Tool usage demonstrations
- Access panel locations

### Procedures

**Flowcharts**:
- Troubleshooting logic
- Procedure decision trees
- Test sequence flows

**Step-by-Step**:
- Maintenance task illustrations
- Installation sequences
- Adjustment procedures

## Hotspot Graphics

Interactive graphics with clickable areas:
- Area definitions for IETP
- Link targets within graphic
- Hotspot coordinates and actions

Example hotspot file:
```
ICN-AMPEL360-23-10-0001-A_001.SVG       (Base graphic)
ICN-AMPEL360-23-10-0001-A_001_HS.XML    (Hotspot definitions)
```

## Callouts and Labels

### In-Graphic Text

- Item numbers for parts
- Reference designations
- Warnings and cautions
- Dimensional information

### External Callouts

Separate callout files for translation:
```
ICN-AMPEL360-23-10-0001-A_001.SVG           (Base graphic)
ICN-AMPEL360-23-10-0001-A_001_EN-US.XML     (English callouts)
ICN-AMPEL360-23-10-0001-A_001_FR-FR.XML     (French callouts)
```

## Graphic Specifications

### SVG Requirements

- **Viewbox**: Properly defined for scaling
- **Layers**: Organized logical layer structure
- **Text**: Converted to paths or embedded fonts
- **Colors**: Standard palette for consistency
- **Line weights**: Appropriate for output medium
- **Size**: Optimized for web and print

### Resolution Guidelines

- **Screen Graphics**: 96-150 DPI
- **Print Graphics**: 300 DPI minimum
- **Photos**: 300 DPI for print quality
- **Maximum Dimensions**: 8.5" × 11" for standard pages

## Referencing from Data Modules

Data Modules reference ICNs using the `<figure>` element:

```xml
<figure id="fig-0001">
  <title>Speech Communications System Block Diagram</title>
  <graphic infoEntityIdent="ICN-AMPEL360-23-10-0001-A"/>
</figure>
```

## Version Control

### Variant Management

- Use variant code for configuration differences
- Example: `-A` for baseline, `-B` for modified system

### Issue Tracking

- Maintain illustration history
- Track changes in illustration metadata
- Coordinate with Data Module revisions

## Workflow

### Creation

1. **Plan**: Define illustration requirements from DM
2. **Create**: Develop graphic using approved tools
3. **Review**: Technical accuracy review
4. **Approve**: Sign-off on final artwork
5. **Assign ICN**: Allocate unique identifier
6. **Store**: Place in CSDB ICN directory

### Modification

1. **Identify Need**: Change requirement from DM update
2. **Edit**: Modify existing graphic
3. **Review**: Verify technical accuracy
4. **Version**: Update issue or create new variant
5. **Update References**: Ensure DMs reference correct version

## Best Practices

- **Consistent Style**: Use standard symbology and conventions
- **Clarity**: Prioritize clarity over artistic complexity
- **Labels**: Clear, unambiguous callouts and labels
- **Simplicity**: Include only necessary details
- **Reusability**: Design for use in multiple contexts
- **Accessibility**: Consider colorblind users (avoid red/green alone)
- **File Size**: Optimize for web delivery
- **Standards**: Follow industry standards (e.g., ISO 1219 for hydraulics)

## Quality Checks

Before release, verify:
- ✅ Correct ICN assigned and labeled
- ✅ Technical accuracy validated
- ✅ Clear and readable at intended size
- ✅ Proper format and file size
- ✅ Correct file naming
- ✅ Metadata complete
- ✅ Copyright and source information included

## Validation

All illustrations must:
- Have valid, unique ICN codes
- Be in approved file formats
- Meet resolution and quality requirements
- Include required metadata
- Pass technical accuracy review
- Comply with AMPEL360 graphic standards

## Related Directories

- `../DM/` - Data Modules that reference illustrations
- `../PM/` - Publication Modules including illustrated DMs
- `../COMMON/` - Common graphics used across modules
- `../BREX/` - Validation rules for graphics

## Tools

Graphics creation and management tools:
- **Adobe Illustrator**: Professional vector graphics
- **Inkscape**: Open-source SVG editor
- **CorelDRAW**: Technical illustration software
- **Arbortext IsoDraw**: CAD-to-SVG conversion
- **IsoView**: CGM viewer and converter

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-10-00 (Speech Communications)
- **Publication Type**: AMM (Aircraft Maintenance Manual)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
