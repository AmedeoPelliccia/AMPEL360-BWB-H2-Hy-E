# PM — Publication Modules

## Overview

This directory contains **Publication Modules (PM)** for the Illustrated Parts Catalog (IPC). Publication Modules define the hierarchical structure and organization of technical publications in S1000D.

## Purpose

Publication Modules:
- Define the structure and table of contents for IPC publications
- Reference Data Modules (DM) in a specific order
- Create hierarchical parts catalog structures
- Enable multiple publication views from the same content
- Support dynamic publication generation
- Manage applicability filtering for different aircraft variants

## Naming Convention

Publication Modules follow the S1000D Publication Module Code (PMC) structure:

```
PMC-AMPEL360-{ATA}-{SECTION}-{PUBLICATION_CODE}_XXX_00_{ISSUE}.XML
```

### Components

- **Model ID**: `AMPEL360` (fixed)
- **ATA Chapter**: `23` (Communications)
- **Section**: `00-99` (per ATA SNS)
- **Publication Code**: Unique code identifying the publication type
  - `00001` - Complete IPC
  - `00010` - System Parts Overview
  - `00020` - Illustrated Parts Breakdowns
  - `00030` - Parts Cross-Reference
- **Sequence**: `XXX` (001-999)
- **Indenture**: `00` (hierarchical level)
- **Issue**: `001-00` to `999-99` (issue number and in-work revision)

### Examples

**Complete IPC Publication Module**:
```
PMC-AMPEL360-23-10-00001_001_00_001-00.XML
```
*Defines the complete ATA 23-10 IPC structure*

**System Parts Overview**:
```
PMC-AMPEL360-23-10-00010_001_00_001-00.XML
```
*Speech communications parts overview*

**Illustrated Parts Breakdowns**:
```
PMC-AMPEL360-23-10-00020_001_00_001-00.XML
```
*Detailed IPB sections*

## Publication Module Types

### Primary Publication Modules

**Complete Publications**:
- Full IPC with all parts
- System-specific catalogs
- Component breakdowns

**Section Publications**:
- Parts lists by system
- Illustrated breakdowns
- Cross-reference sections

### Nested Structure

Publication Modules can reference:
- Other Publication Modules (for hierarchical organization)
- Data Modules (for actual parts content)
- Data Module Lists (for grouped content)

## File Structure

Each Publication Module XML file contains:

1. **Identification and Status Section**
   - Publication module code
   - Title and security classification
   - Issue information

2. **Content Section**
   - Hierarchical structure definition
   - References to child PMs or DMs
   - Applicability statements

3. **Publication Module Entry**
   - Reference to included modules
   - Entry title and navigation labels
   - Sequencing information

## Content Organization

### Standard IPC Structure

Typical ATA chapter IPC organization:

```
1. Introduction
   - General information
   - How to use this catalog
   - Abbreviations
   
2. System Overview
   - System description
   - Component locations
   
3. Illustrated Parts Breakdowns
   - Major assemblies
   - Subassemblies
   - Detail parts
   
4. Parts Lists
   - Tabular parts lists
   - Quantities
   - Part numbers
   
5. Cross-Reference
   - Vendor cross-reference
   - Interchangeability
```

## Applicability Management

Publication Modules support:
- **Product variants**: Different aircraft configurations
- **Effectivity**: Serial number or modification state
- **Optional equipment**: Customer-selectable systems
- **Time-based applicability**: Temporary restrictions

## Publishing Workflow

1. **Structure Definition**: Create PM hierarchy
2. **Content Assembly**: Reference DMs in logical order
3. **Applicability Filter**: Apply product/effectivity filters
4. **Validation**: Verify structure and references
5. **Transformation**: Generate output (PDF, HTML, XML)
6. **Quality Check**: Review final publication
7. **Release**: Distribute to field organization

## Output Formats

Publication Modules can be transformed to:
- **PDF**: Printable catalogs
- **HTML/Web**: Interactive online catalogs
- **IETP**: Interactive Electronic Technical Publications
- **Mobile Apps**: Tablet/smartphone applications

## Best Practices

- **Logical Organization**: Group parts by assembly
- **Consistent Structure**: Maintain standard structure across chapters
- **Clear Titles**: Use descriptive, hierarchical titles
- **Proper References**: Ensure all DM references are valid
- **Applicability**: Define applicability at appropriate level

## Validation

All Publication Modules must:
- Validate against S1000D Issue 5.0 schema
- Reference only valid Data Modules
- Comply with AMPEL360 BREX rules
- Have unique publication codes
- Include all required metadata

## Related Directories

- `../DM/` - Data Modules referenced by publication modules
- `../DML/` - Data Module Lists that can be referenced
- `../BREX/` - Validation rules for publication modules
- `../APPLICABILITY/` - Applicability cross-reference tables

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 23 (Communications)
- **Section**: 23-10-00 (Speech Communications)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
