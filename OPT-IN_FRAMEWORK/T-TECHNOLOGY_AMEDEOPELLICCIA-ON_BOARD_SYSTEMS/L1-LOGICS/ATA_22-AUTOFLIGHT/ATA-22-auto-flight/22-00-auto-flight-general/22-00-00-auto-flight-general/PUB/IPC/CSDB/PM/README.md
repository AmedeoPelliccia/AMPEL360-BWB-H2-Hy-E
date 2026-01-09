# PM — Publication Modules

## Overview

This directory contains **Publication Modules (PM)** for the Illustrated Parts Catalog (IPC). Publication Modules define the hierarchical structure and organization of technical publications in S1000D.

## Purpose

Publication Modules:
- Define the structure and table of contents for publications
- Reference Data Modules (DM) in a specific order
- Create hierarchical document structures
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
- **ATA Chapter**: `22` (Autoflight)
- **Section**: `00-99` (per ATA SNS)
- **Publication Code**: Unique code identifying the publication type
  - `00001` - Complete AMM
  - `00010` - System Description Manual
  - `00020` - Parts Lists Manual
  - `00030` - Troubleshooting Manual
  - `00040` - Component Maintenance Manual
- **Sequence**: `XXX` (001-999)
- **Indenture**: `00` (hierarchical level)
- **Issue**: `001-00` to `999-99` (issue number and in-work revision)

### Examples

**Complete AMM Publication Module**:
```
PMC-AMPEL360-22-00-00001_001_00_001-00.XML
```
*Defines the complete ATA 22 AMM structure*

**System Description Section**:
```
PMC-AMPEL360-22-00-00010_001_00_001-00.XML
```
*System descriptions and theory of operation*

**Parts Lists Section**:
```
PMC-AMPEL360-22-00-00020_001_00_001-00.XML
```
*Maintenance task parts lists*

**Troubleshooting Section**:
```
PMC-AMPEL360-22-00-00030_001_00_001-00.XML
```
*Fault isolation and troubleshooting*

## Publication Module Types

### Primary Publication Modules

**Complete Publications**:
- Full AMM with all sections
- System-specific manuals
- Task card publications

**Section Publications**:
- Descriptive sections
- Procedural sections
- Troubleshooting sections
- Parts lists (cross-reference to IPC)

### Nested Structure

Publication Modules can reference:
- Other Publication Modules (for hierarchical organization)
- Data Modules (for actual content)
- Data Module Lists (for grouped content)

Example hierarchy:
```
PMC-AMPEL360-22-00-00001 (Complete AMM)
├── PMC-AMPEL360-22-00-00010 (Descriptions)
│   ├── DMC-...-040A-... (System overview)
│   └── DMC-...-040A-... (Component descriptions)
├── PMC-AMPEL360-22-00-00020 (Procedures)
│   ├── DMC-...-520A-... (Test parts lists)
│   └── DMC-...-520B-... (Maintenance parts lists)
└── PMC-AMPEL360-22-00-00030 (Troubleshooting)
    └── DMC-...-730A-... (Fault isolation)
```

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

### Standard AMM Structure

Typical ATA chapter AMM organization:

```
1. Introduction
   - General information
   - Abbreviations and acronyms
   - Safety precautions
   
2. Description and Operation
   - System description
   - Component descriptions
   - Theory of operation
   
3. Maintenance Practices
   - Standard practices
   - Special tools
   - Servicing
   
4. Parts Lists
   - Inspections
   - Tests
   - Adjustments
   - Removal/Installation
   
5. Troubleshooting
   - Fault isolation
   - Test parts lists
   - Fault messages
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
- **PDF**: Printable manuals
- **HTML/Web**: Interactive online documentation
- **IETP**: Interactive Electronic Technical Publications
- **Mobile Apps**: Tablet/smartphone applications

## Version Control

- Issue numbers track publication versions
- In-work revisions for draft publications
- Change markers indicate modified content
- Revision history in publication front matter

## Best Practices

- **Logical Organization**: Group related content logically
- **Consistent Structure**: Maintain standard structure across chapters
- **Clear Titles**: Use descriptive, hierarchical titles
- **Proper References**: Ensure all DM references are valid
- **Applicability**: Define applicability at appropriate level
- **Modularity**: Design for maximum reusability
- **Navigation**: Provide clear navigation path for users

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

## Tools and Software

Common tools for PM authoring:
- **Arbortext Editor**: PTC's XML editor
- **Oxygen XML Editor**: SyncRO Soft's XML editor
- **S1000D Composer**: Specialized S1000D authoring
- **Custom XSLT**: Transformation stylesheets

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 22 (Autoflight)
- **Publication Type**: AMM (Aircraft Maintenance Manual)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
