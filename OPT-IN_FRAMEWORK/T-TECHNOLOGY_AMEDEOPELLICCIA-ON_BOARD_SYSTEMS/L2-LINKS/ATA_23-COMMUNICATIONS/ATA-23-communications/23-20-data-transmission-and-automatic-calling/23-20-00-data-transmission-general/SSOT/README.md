# SSOT — Single Source of Truth

## Purpose

This directory contains the **Single Source of Truth** (SSOT) for this subject. All content originates here before being transformed into publication-specific formats.

## Organization

The SSOT directory is organized by lifecycle phases:

```
SSOT/
├── LC01_Requirements/          # System and functional requirements
├── LC02_System_Requirements/   # Detailed system-level requirements
├── LC03_Design/                # Design specifications and architecture
├── LC04_Analysis/              # Engineering analysis and modeling
├── LC05_VnV/                   # Verification and validation evidence
├── LC06_Quality/               # Quality assurance documentation
├── LC07_Safety/                # Safety analysis and evidence
└── LC08_Certification/         # Certification artifacts and compliance
```

## Lifecycle Phase Guidelines

### LC01_Requirements
- Functional requirements
- Performance requirements
- Interface requirements
- Operational requirements

### LC02_System_Requirements
- Detailed system specifications
- Derived requirements
- Allocated requirements
- Requirements traceability

### LC03_Design
- System architecture
- Interface designs
- Component specifications
- Design rationale

### LC04_Analysis
- Engineering analysis
- Trade studies
- Performance analysis
- Modeling and simulation

### LC05_VnV
- Verification plans
- Validation plans
- Test procedures
- Test results and evidence

### LC06_Quality
- Quality plans
- Quality metrics
- Inspection procedures
- Quality records

### LC07_Safety
- Safety analysis (FHA, FTA, FMEA)
- Hazard analysis
- Safety requirements
- Safety verification evidence

### LC08_Certification
- Certification plans (e.g., PSAC)
- Compliance matrices
- Certification test evidence
- Certification reports

## Content Guidelines

1. **Format-Agnostic**: Store content in format-agnostic forms (Markdown, structured XML, etc.)
2. **Version Control**: All SSOT content should be version controlled
3. **Single Copy**: Each piece of information should exist in exactly one place
4. **Publication Generation**: PUB directories contain views generated from SSOT content

## Workflow

1. **Author**: Create/edit content in SSOT
2. **Transform**: Apply publication-specific transformations
3. **Publish**: Generate S1000D data modules in PUB/CSDB
4. **Export**: Create final deliverables in PUB/EXPORT

## Relationship to CSDB

- **SSOT**: Master content repository (format-agnostic, lifecycle-organized)
- **CSDB**: Publication-ready S1000D data modules (derived from SSOT)

## Document Control

- **Purpose**: Master content repository
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
