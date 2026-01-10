# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>

# PUB — Publication Views

## Overview

This directory contains publication-specific views for BITE Data Export to CMS (ATA 45) (32-60-50).

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

## S1000D Data Module Naming

Data modules follow the standard S1000D naming convention:

```
DMC-<ModelIdentCode>-<SystemDiffCode>-<SystemCode>-<SubSystemCode>-<SubSubSystemCode>-<InfoCode>-<InfoCodeVariant>-<ItemLocationCode>_<LearnCode>_<LearnEventCode>_<LanguageIsoCode>-<CountryIsoCode>_<IssueNumber>-<InWork>.XML
```

Example for AMPEL360AT model:
```
DMC-AMPEL360AT-32-60-50-040A-A-A_001_00_EN-US_001-00.XML
```

## Document Control

- **Subject**: 32-60-50
- **Type**: PUB (Publication Views)
- **Standard**: S1000D Issue 5.0 / ATA iSpec 2200
- **Model**: AMPEL360AT
- **Last Updated**: 2026-01-10
