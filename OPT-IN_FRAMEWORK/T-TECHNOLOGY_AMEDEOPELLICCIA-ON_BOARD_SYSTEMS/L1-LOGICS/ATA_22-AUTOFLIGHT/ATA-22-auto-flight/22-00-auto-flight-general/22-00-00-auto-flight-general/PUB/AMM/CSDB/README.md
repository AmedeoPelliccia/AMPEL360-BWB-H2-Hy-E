# S1000D Common Source Database (CSDB)

## Overview

This directory contains the S1000D Common Source Database for ATA 22-00-00 Auto Flight General documentation.

## Directory Structure

- **DM/**: Data Modules - Individual documentation units (procedures, descriptions, etc.)
- **PM/**: Publication Modules - Define the structure of publications
- **DML/**: Data Module Lists - Organize and reference groups of data modules
- **ICN/**: Illustrations/Graphics - All graphical content (ICN = Illustration Control Number)
- **BREX/**: Business Rules Exchange - Validation rules and constraints
- **COMMON/**: Common Information Sets - Reusable content snippets
- **APPLICABILITY/**: Applicability Statements - Product variant and configuration applicability

## S1000D Naming Convention

Data modules follow the S1000D naming convention:
```
DMC-<modelIdentCode>-<systemDiffCode>-<systemCode>-<subSystemCode><subSubSystemCode>-<assyCode>-<disassyCode><disassyCodeVariant>-<infoCode><infoCodeVariant>-<itemLocationCode>
```

Example:
```
DMC-AMPEL360-22-00-00-00A-00A-D
```

## Usage

1. Create data modules in the **DM/** directory following S1000D schema
2. Reference illustrations from the **ICN/** directory
3. Define publication structure in **PM/** directory
4. Organize data modules using **DML/** directory
5. Apply business rules from **BREX/** for validation
6. Reuse common content from **COMMON/** directory
7. Apply applicability from **APPLICABILITY/** directory

## References

- S1000D Specification Issue 5.0
- ATA iSpec 2200 for chapter/section/subject codes
- AMPEL360 CSDB Guidelines (see repository documentation)

## Document Control

- **Location**: ATA 22-00-00 AMM CSDB
- **Standard**: S1000D Issue 5.0
- **Last Updated**: 2026-01-08
