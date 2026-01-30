# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>

# CSDB — Common Source Database

## Overview

This is the S1000D Common Source Database for Rigging Adjustment And Calibration (27-50-40-rigging-adjustment-and-calibration).

## S1000D Structure

### Data Modules (DM/)

Data modules contain the actual technical content:

- **040A**: Description and Operation
- **520A**: Test and Checkout Procedures
- **720A**: Removal and Installation
- **730A**: Fault Isolation
- **940A**: Software Configuration (if applicable)

### Publication Modules (PM/)

Publication modules define how data modules are organized into publications.

### Data Module Lists (DML/)

Data module lists group related data modules together.

### Illustrations (ICN/)

Technical illustrations in SVG format following S1000D naming conventions.

### Business Rules (BREX/)

BREX files define validation rules and business rules for the content.

### Common Information (COMMON/)

Reusable content such as:
- Standard warnings
- Standard cautions
- Standard notes
- Common procedures

### Applicability (APPLICABILITY/)

Applicability cross-reference tables defining which content applies to which product variants.

## Naming Conventions

### Data Module Codes

Format: `DMC-AMPEL360AT-27-50-40-<InfoCode>-<Variant>-<ItemLoc>_<Learn>_<LearnEvent>_<Lang>-<Country>_<Issue>-<InWork>.XML`

### Illustration Codes

Format: `ICN-AMPEL360AT-27-50-40-<Seq>-<Variant>_<Issue>.<ext>`

## Document Control

- **Subject**: 27-50-40-rigging-adjustment-and-calibration
- **Model**: AMPEL360AT
- **Standard**: S1000D Issue 5.0
- **Last Updated**: 2026-01-09
