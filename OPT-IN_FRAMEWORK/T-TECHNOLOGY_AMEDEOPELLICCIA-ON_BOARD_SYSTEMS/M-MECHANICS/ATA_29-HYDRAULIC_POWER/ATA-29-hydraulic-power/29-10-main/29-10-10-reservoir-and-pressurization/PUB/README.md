# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>

# PUB — Publication Views

## Overview

This directory contains publication-specific views for Reservoir and Pressurization (29-10-10).

## Structure

### AMM — Aircraft Maintenance Manual

The AMM contains maintenance procedures, troubleshooting, and service information.

#### CSDB — Common Source Database (S1000D)

The CSDB follows the S1000D Issue 5.0 standard:

- **DM/**: Data Modules
  - Descriptive (040A): System descriptions and overviews
  - Procedural (520A): Test and checkout procedures
  - Procedural (720A): Removal and installation procedures
  - Procedural (730A): Fault isolation procedures
  - Procedural (940A): Software loading and configuration (if applicable)

- **PM/**: Publication Modules
  - Define the structure and organization of publications

- **DML/**: Data Module Lists
  - Organize and group related data modules

- **ICN/**: Illustrations (SVG format)
  - Technical illustrations and diagrams
  - Follow S1000D ICN naming conventions

- **BREX/**: Business Rules Exchange
  - Validation rules and business rules for content

- **COMMON/**: Common Information
  - Reusable content snippets (warnings, cautions, notes)

- **APPLICABILITY/**: Applicability Statements
  - Product variant and configuration applicability

### EXPORT — Rendered Outputs

Rendered outputs in various formats:
- **PDF/**: PDF format exports
- **HTML/**: HTML format exports

### IETP — Interactive Electronic Technical Publication

IETP package structure:
- **RUNTIME/**: Viewer and server components
- **PKG/**: Packaged artifacts and manifests
- **DEPLOY/**: Deployment configurations

## S1000D Data Module Naming

Data modules follow the standard S1000D naming convention:

```
DMC-<ModelIdentCode>-<SystemDiffCode>-<SystemCode>-<SubSystemCode>-<SubSubSystemCode>-<AssyCode>-<DisassyCode>-<DisassyCodeVariant>-<InfoCode>-<InfoCodeVariant>-<ItemLocationCode>_<LearnCode>_<LearnEventCode>_<LanguageIsoCode>-<CountryIsoCode>_<IssueNumber>-<InWork>.XML
```

Example for AMPEL360AT model:
```
DMC-AMPEL360AT-29-10-10-040A-A-A_001_00_EN-US_001-00.XML
```

## Configuration Files

### csdb.profile.yaml

CSDB profile configuration for this subject.

## Document Control

- **Subject**: 29-10-10
- **Type**: PUB (Publication Views)
- **Standard**: S1000D Issue 5.0 / ATA iSpec 2200
- **Model**: AMPEL360AT
- **Last Updated**: 2026-01-09
