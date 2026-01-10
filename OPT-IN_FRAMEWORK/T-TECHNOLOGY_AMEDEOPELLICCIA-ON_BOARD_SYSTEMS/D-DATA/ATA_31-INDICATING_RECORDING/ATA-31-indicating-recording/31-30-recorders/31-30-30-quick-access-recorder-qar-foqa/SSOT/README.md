# SSOT — Single Source of Truth

## Purpose

This directory contains the **Single Source of Truth** (SSOT) for **31-30-30-quick-access-recorder-qar-foqa**. All content originates here before being transformed into publication-specific formats.

## Organization

The SSOT directory should be organized by content type:

```
SSOT/
├── procedures/          # Maintenance procedures
├── descriptions/        # System descriptions
├── specifications/      # Technical specifications
├── diagrams/           # Source diagrams (before conversion to ICN)
├── data/               # Technical data and tables
└── metadata/           # Content metadata and indexes
```

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

- **SSOT**: Master content repository (format-agnostic)
- **CSDB**: Publication-ready S1000D data modules (derived from SSOT)

## Document Control

- **Subject**: 31-30-30-quick-access-recorder-qar-foqa
- **Section**: 31-30-recorders
- **Purpose**: Master content repository
- **Status**: Active
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2026-01-10
