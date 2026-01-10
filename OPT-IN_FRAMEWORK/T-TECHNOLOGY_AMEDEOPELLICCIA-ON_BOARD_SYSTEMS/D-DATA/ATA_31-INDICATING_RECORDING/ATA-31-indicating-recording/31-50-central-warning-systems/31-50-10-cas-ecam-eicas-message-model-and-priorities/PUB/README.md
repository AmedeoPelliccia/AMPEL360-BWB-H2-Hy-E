# PUB — Publications

## Overview

This directory contains S1000D-compliant technical publications for ATA 31-50-10 (CAS/ECAM/EICAS Message Model and Priorities).

## Structure

### CSDB — Common Source Database

The Common Source Database (CSDB) is the master repository for all S1000D data modules:

- **DM/**: Data Modules (descriptive, procedural, and fault isolation content)
- **PM/**: Publication Modules (define publication structures like AMM, IPC, WDM, TSM)
- **ICN/**: Illustrations (SVG graphics and images)
- **BREX/**: Business Rules Exchange (validation rules for content)
- **DML/**: Data Module Lists
- **COMMON/**: Common information elements (warnings, cautions, notes)
- **APPLICABILITY/**: Applicability statements and conditions

### EXPORT — Multi-Format Publications

Exported publications in multiple formats for different use cases:

- **AMM/**: Aircraft Maintenance Manual (PDF, HTML)
- **IPC/**: Illustrated Parts Catalog (PDF, HTML)
- **WDM/**: Wiring Diagram Manual (PDF, HTML)
- **TSM/**: Troubleshooting Manual (PDF, HTML)

### IETP — Interactive Electronic Technical Publication

Modern interactive viewer and runtime environment:

- **RUNTIME/**: IETP viewer software and runtime environment
- **PKG/**: Versioned IETP packages with manifests, SBOM, and checksums
- **DEPLOY/**: Deployment configurations (Docker Compose, Kubernetes, installers)

## S1000D Compliance

All publications conform to:

- **S1000D Issue 5.0** specification
- **BREX** (Business Rules Exchange) for project-specific rules
- **ATA iSpec 2200** chapter numbering
- **DO-178C** software documentation requirements (where applicable)

## Publication Workflow

1. **Author**: Create/edit data modules in CSDB/DM/
2. **Review**: Validate against BREX rules
3. **Approve**: Quality assurance and technical approval
4. **Publish**: Generate publication modules (PM)
5. **Export**: Create PDF/HTML outputs in EXPORT/
6. **Package**: Bundle for IETP distribution in PKG/
7. **Deploy**: Distribute to aircraft, ground stations, or cloud platforms

## Document Control

- **Owner**: AMPEL360 Technical Publications
- **Standard**: S1000D Issue 5.0, ATA iSpec 2200
- **Generated with AI assistance**: GitHub Copilot, prompted by **Amedeo Pelliccia**
- **Last Updated**: 2026-01-09
