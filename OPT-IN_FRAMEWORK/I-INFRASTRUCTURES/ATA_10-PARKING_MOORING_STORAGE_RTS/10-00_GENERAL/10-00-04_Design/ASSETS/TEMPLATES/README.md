# TEMPLATES — ATA 10 Parking, Mooring, Storage & RTS

## Overview

This directory contains **master templates** for documentation, specifications, checklists, and work formats related to **ATA Chapter 10: Parking, Mooring, Storage & Return to Service (RTS)** for the AMPEL360-BWB-H2 aircraft.

These templates provide standardized structures to ensure consistency, completeness, and compliance across all ATA 10 documentation.

## Purpose

The TEMPLATES directory serves to:

- **Standardize** document structure and content across ATA 10
- **Accelerate** creation of new documentation with pre-defined formats
- **Ensure completeness** by providing comprehensive section structures
- **Maintain consistency** across different authors and teams
- **Support traceability** with built-in metadata and cross-reference sections
- **Integrate H2 safety** and BWB-specific considerations in all relevant templates

## Subdirectories

### 1. **document-templates/**
Standard templates for formal technical documents:
- Specifications
- Procedures
- Technical notes
- Engineering changes
- Design reviews

### 2. **drawing-templates/**
Templates for engineering drawings and schematics:
- Drawing title blocks
- Assembly drawings
- Detail drawings
- Installation drawings
- Schematics

### 3. **checklist-templates/**
Operational and verification checklists:
- Design review checklists
- Installation checklists
- Verification checklists
- H2 safety checklists
- Release checklists

### 4. **report-templates/**
Templates for analysis and reporting:
- Analysis reports
- Test reports
- Validation reports
- Incident reports

### 5. **h2-specific-templates/**
Specialized templates for hydrogen systems:
- H2 safety assessments
- Cryogenic hazard analysis
- H2 compatibility checklists
- LH2 procedures

### 6. **bwb-specific-templates/**
Specialized templates for Blended Wing Body configuration:
- BWB clearance analysis
- BWB ground handling
- BWB configuration documentation

### 7. **metadata-schemas/**
JSON schemas for structured metadata:
- Document metadata
- Drawing metadata
- Part metadata
- Product metadata

### 8. **style-guides/**
Documentation standards and conventions:
- Documentation style guide
- Naming convention guide
- Terminology glossary

## Template Usage Guidelines

### How to Use These Templates

1. **Select the appropriate template** for your document type
2. **Copy the template** to your target location (do not edit templates directly)
3. **Rename** following AMPEL360 naming conventions
4. **Fill in all sections**, removing or adapting as needed for your specific use case
5. **Preserve Document Control** sections with proper metadata
6. **Update cross-references** to related documents and requirements
7. **Review against applicable standards** (ATA iSpec 2200, CS-25, etc.)

### Template Naming Convention

All templates follow this pattern:

```
10-TPL-<TYPE>-<nnn>_<Descriptive_Name>.<ext>
```

Where:
- `10` = ATA Chapter
- `TPL` = Template identifier
- `<TYPE>` = Template category (DOC, DWG, CHK, RPT, H2, BWB, STY)
- `<nnn>` = Sequential 3-digit number (001-999)
- `<Descriptive_Name>` = Purpose in PascalCase
- `<ext>` = File extension (.md, .json, etc.)

### Customization Guidelines

When adapting templates:

- **Preserve required sections** (Document Control, Safety, References)
- **Add project-specific sections** as needed
- **Maintain consistent formatting** within your document set
- **Document deviations** from standard template in Document Control
- **Keep original template reference** in Document Control block

### H2 and BWB Integration

All general templates include sections for:
- **H2 Safety Considerations**: Addressing hydrogen-specific hazards
- **BWB Configuration Impact**: Addressing Blended Wing Body specifics
- **Cryogenic Considerations**: For LH2 systems at -253°C

Use specialized H2 and BWB templates when these aspects are the primary focus.

## Version Control for Templates

Templates are version-controlled as part of this repository:

- **Template updates** must be reviewed by ATA 10 documentation lead
- **Version history** is maintained in git commit history
- **Breaking changes** (structure modifications) require notification to all users
- **Backward compatibility** should be maintained where possible

### Template Lifecycle

| Stage | Action | Approval Required |
|-------|--------|-------------------|
| Draft | Initial template creation | Technical review |
| Active | Released for general use | Documentation lead |
| Deprecated | Template superseded by newer version | Documentation lead |
| Archived | No longer in use | Configuration management |

## Document Control

Templates themselves include Document Control sections. When using a template:

1. **Update all metadata fields** (document ID, version, date, author)
2. **Set initial status** to "Draft" or "In Review"
3. **Track revisions** in the Revision History table
4. **Obtain required approvals** before setting status to "Released"

## Standards Compliance

These templates are designed to support compliance with:

- **ATA iSpec 2200**: Aircraft maintenance documentation
- **ATA 100**: Standard numbering system
- **S1000D**: Technical publications specification
- **CS-25 / FAR 25**: Certification specifications for large aircraft
- **SAE AS6968**: Hydrogen aircraft systems
- **NFPA 2**: Hydrogen Technologies Code
- **ISO 19880-8**: Gaseous hydrogen — Fueling protocols

## Related Documentation

For complete context and requirements:

- [ATA 10 Overview](../../10-00-01_Overview/README.md)
- [ATA 10 Safety Framework](../../10-00-02_Safety/README.md)
- [ATA 10 Requirements](../../10-00-03_Requirements/README.md)
- [AMPEL360 Documentation Standard](../../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)
- [AMPEL360 Assets Standard](../../../../../../../AMPEL360_ASSETS_STANDARD.md)
- [OPT-IN Framework Standard](../../../../../../../OPT-IN_FRAMEWORK_STANDARD.md)

## Template Index

For a complete categorized list of all templates, see [00_INDEX.md](./00_INDEX.md).

## Support and Feedback

For questions or suggestions regarding templates:

- **Technical questions**: Contact ATA 10 technical lead
- **Template requests**: Submit via project issue tracking
- **Template updates**: Create pull request with proposed changes

---

## Document Control

- **Document ID**: 10-00-04-README-TPL
- **Version**: 1.0
- **Status**: Active
- **Date**: 2025-12-09
- **Author**: AMPEL360 Documentation Team
- **Repository**: AMPEL360-BWB-H2-Hy-E
- **Path**: `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/10-00_GENERAL/10-00-04_Design/ASSETS/TEMPLATES/`

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-09 | AMPEL360 Docs | Initial template directory structure |

---

*Generated with assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia*
