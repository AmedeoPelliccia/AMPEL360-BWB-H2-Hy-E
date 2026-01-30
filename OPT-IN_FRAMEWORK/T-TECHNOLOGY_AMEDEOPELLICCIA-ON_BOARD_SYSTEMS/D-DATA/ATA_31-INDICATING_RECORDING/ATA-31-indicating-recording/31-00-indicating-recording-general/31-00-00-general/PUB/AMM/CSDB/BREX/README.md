# BREX Directory - ATA 31-00-00

## Purpose

Contains **Business Rules Exchange (BREX)** - validation rules and constraints for ATA 31 (Indicating/Recording) AMM data modules.

This BREX layer constrains how ATA 31 AMM DMs are authored, not how they are rendered. It enforces structure, semantics, info-code usage, and cross-ATA discipline.

## S1000D BREX Files

### Master BREX
- **DMC-AMPEL360AT-31-00-00-022A-A-001_001_00_EN-US_001-00.XML**
  - Master BREX for ATA 31-00-00 AMM data modules
  - Controls: Applicable info codes, mandatory sectioning, allowed DM types, prohibited constructs

### Structural Rules BREX
- **DMC-AMPEL360AT-31-00-00-022B-A-001_001_00_EN-US_001-00.XML**
  - Structural and content model rules
  - Enforces: Proper use of `<descr>`, `<proceduralStep>`, `<warning>`, `<caution>`, content separation

### Safety & Operational Constraints BREX
- **DMC-AMPEL360AT-31-00-00-022C-A-001_001_00_EN-US_001-00.XML**
  - Safety, warnings, and operational constraints
  - Enforces: Mandatory warnings for live displays and data recording, standardized safety phrasing

### Cross-ATA Interface BREX
- **DMC-AMPEL360AT-31-00-00-022D-A-001_001_00_EN-US_001-00.XML**
  - Cross-ATA interface constraints and discipline
  - Controls: References to ATA 24, 42, 45, 23, 22, 46; prevents responsibility redefinition

### Graphics & ICN Usage BREX
- **DMC-AMPEL360AT-31-00-00-022E-A-001_001_00_EN-US_001-00.XML**
  - Rules for ICN/SVG usage in AMM
  - Enforces: Referenced ICNs only, proper naming, no illustration-only DMs, explanatory scope

## Naming Convention

Data Module Code format: `DMC-AMPEL360AT-31-00-00-022[A-E]-A-001_001_00_EN-US_001-00.XML`

Where:
- **022A** = Master BREX
- **022B** = Structural Rules
- **022C** = Safety & Operational
- **022D** = Cross-ATA Interface
- **022E** = Graphics & ICN Usage

## Key Principles

1. **BREX applies to DM only**, never to PM
2. **PDF/HTML/IETP** are downstream products, not governed here
3. **Inheritance-safe**: Program BREX → ATA 31 BREX → sub-ATA BREX (31-xx-yy)

## Document Control

- **Directory**: BREX
- **Subject**: 31-00-00-general (Indicating/Recording - General)
- **Publication**: AMM (Aircraft Maintenance Manual)
- **Model**: AMPEL360AT
- **Standard**: S1000D Issue 5.0
- **Status**: Active
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2026-01-10
