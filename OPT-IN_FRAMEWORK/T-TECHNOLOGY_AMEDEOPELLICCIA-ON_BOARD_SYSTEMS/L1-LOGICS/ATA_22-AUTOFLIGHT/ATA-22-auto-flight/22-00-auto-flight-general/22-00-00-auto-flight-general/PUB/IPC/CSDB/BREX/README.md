# BREX — Business Rules Exchange

## Overview

This directory contains **Business Rules Exchange (BREX)** files for the Illustrated Parts Catalog (IPC). BREX files define project-specific validation rules that extend and constrain the base S1000D specification.

## Purpose

BREX files provide:
- Project-specific validation rules beyond S1000D schema
- Consistency enforcement across all data modules
- Quality assurance automation
- Compliance verification
- Configuration management support
- Corporate standards enforcement

## What is BREX?

**Business Rules Exchange (BREX)** is an S1000D mechanism for defining and sharing:
- Allowed and required XML elements and attributes
- Valid value ranges and enumerations
- Mandatory metadata
- Naming conventions
- Structure rules
- Content constraints

BREX rules are **machine-readable**, enabling automated validation tools to verify compliance before publication.

## Naming Convention

BREX files follow a standard structure:

```
BREX-AMPEL360-{PROJECT}-{VERSION}.XML
```

### Components

- **Model ID**: `AMPEL360` (fixed)
- **Project**: Identifier for rule set scope
  - `GLOBAL` - Rules for all AMPEL360 publications
  - `AMM` - Rules specific to maintenance manuals
  - `ATA22` - Rules specific to ATA 22 Autoflight
- **Version**: `v1-0`, `v1-1`, `v2-0` (version identifier)

### Examples

**Global AMPEL360 BREX**:
```
BREX-AMPEL360-GLOBAL-v1-0.XML
```
*Project-wide rules for all technical publications*

**AMM-Specific BREX**:
```
BREX-AMPEL360-AMM-v1-0.XML
```
*Rules specific to maintenance manual format*

**ATA 22-Specific BREX**:
```
BREX-AMPEL360-ATA22-v1-0.XML
```
*Rules specific to autoflight system documentation*

## BREX Structure

Each BREX file contains:

1. **Identification Section**
   - BREX code and title
   - Responsible organization
   - Issue and version information

2. **Context Rules**
   - Specify where rules apply
   - Define scope (DM, PM, ICN, etc.)

3. **Structure Rules**
   - Required and allowed elements
   - Element nesting constraints
   - Attribute requirements

4. **Notation Rules**
   - Naming conventions
   - Code patterns
   - Value formats

5. **Object Rules**
   - Whole-object constraints
   - Cross-element dependencies
   - Business logic validation

## Rule Categories

### Structure Rules

**Element Requirements**:
- Which elements are required
- Which elements are forbidden
- Valid child element combinations

Example:
```xml
<!-- Require safety warning in all procedures -->
<structureRule>
  <ruleContext>procedureStep</ruleContext>
  <ruleAction>mandatory</ruleAction>
  <element>warning</element>
</structureRule>
```

### Notation Rules

**Naming Patterns**:
- Data Module Code format
- ICN numbering sequences
- Publication Module codes

Example:
```xml
<!-- Enforce AMPEL360 DMC prefix -->
<notationRule>
  <ruleContext>dmCode</ruleContext>
  <pattern>AMPEL360-22-\d{2}-\d{2}-\d{3}[A-Z]-[A-Z]-[A-Z]{1,3}</pattern>
</notationRule>
```

### Value Rules

**Allowed Values**:
- Restricted enumerations
- Value ranges
- Controlled vocabularies

Example:
```xml
<!-- Restrict security classification values -->
<valueRule>
  <ruleContext>securityClassification</ruleContext>
  <allowedValue>01</allowedValue>  <!-- Unclassified -->
  <allowedValue>02</allowedValue>  <!-- Restricted -->
</valueRule>
```

## Rule Hierarchy

BREX files can be layered:

1. **S1000D Base Schema** (most general)
   ↓
2. **AMPEL360 Global BREX** (company-wide)
   ↓
3. **AMM BREX** (manual type-specific)
   ↓
4. **ATA 22 BREX** (system-specific)

Each layer adds more specific constraints.

## Validation Process

### Authoring Time

- **Real-time validation**: Editors validate against BREX as you type
- **Save validation**: Check compliance before saving
- **Warnings/Errors**: Immediate feedback on violations

### Check-in Time

- **Repository validation**: Automatic check on content commit
- **Quality gate**: Prevent non-compliant content from entering CSDB
- **Reporting**: Log violations for correction

### Publication Time

- **Pre-publication validation**: Final compliance check
- **Publication blocking**: Prevent release of non-compliant content
- **Audit trail**: Record validation results

## Common AMPEL360 BREX Rules

### Metadata Requirements

- Responsible Partner Company must be specified
- Issue date must be present and valid
- Security classification required
- Applicability statement mandatory for variant-specific content

### Coding Conventions

- DMC must start with "AMPEL360"
- ATA chapter must match directory structure
- ICN must follow sequential numbering
- Language codes must be ISO 639/3166

### Content Rules

- All procedures must include warning or caution if applicable
- Figures must have titles
- References must point to valid objects
- Abbreviations must be defined before use

### Quality Standards

- Descriptive titles required (minimum length)
- Technical names must match approved terminology
- Part numbers must follow format standards
- Units of measure must be SI or approved alternatives

## BREX Customization

### Creating Custom Rules

1. **Identify Requirement**: Document business rule need
2. **Define Scope**: Determine where rule applies
3. **Write Rule**: Create BREX XML structure
4. **Test**: Validate against sample content
5. **Deploy**: Add to BREX file and distribute
6. **Document**: Update BREX documentation

### Rule Maintenance

- **Version Control**: Track BREX changes over time
- **Impact Analysis**: Assess effect of rule changes
- **Backward Compatibility**: Manage legacy content
- **Migration**: Update content to meet new rules

## Tools and Validation

### Authoring Tools

Tools with BREX support:
- **Arbortext Editor**: Native BREX validation
- **Oxygen XML Editor**: Configurable BREX checking
- **S1000D Composer**: Built-in BREX support

### Validation Tools

Standalone validators:
- **S1000D Validator**: Command-line validation
- **CSDB Management Tools**: Batch validation
- **CI/CD Integration**: Automated pipeline checks

### Configuration

Configure tools to use project BREX:
```xml
<brexReference>
  <dmRef>
    <dmRefIdent>
      <dmCode>BREX-AMPEL360-GLOBAL-v1-0</dmCode>
    </dmRefIdent>
  </dmRef>
</brexReference>
```

## Best Practices

- **Clear Rules**: Write unambiguous, testable rules
- **Documentation**: Document the purpose of each rule
- **Minimal Constraints**: Only add rules that add value
- **Testing**: Validate BREX files themselves for correctness
- **Communication**: Inform authors of rule changes
- **Versioning**: Maintain backward compatibility when possible
- **Exceptions**: Define clear process for rule exceptions

## Compliance Reporting

Generate reports showing:
- Validation status by Data Module
- Rule violation frequency
- Compliance trends over time
- Non-compliant objects requiring correction

## Exception Handling

When content cannot meet BREX rules:
1. **Document Justification**: Why exception is needed
2. **Request Approval**: Obtain waiver from authority
3. **Track Exception**: Maintain exception register
4. **Review Periodically**: Reassess exception validity

## Related Directories

- `../DM/` - Data Modules validated against BREX
- `../PM/` - Publication Modules validated against BREX
- `../ICN/` - Illustrations subject to BREX rules
- `../COMMON/` - Common content validated against BREX

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 22 (Autoflight)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia

## References

- S1000D Issue 5.0 Specification - Chapter 3.3 (BREX)
- AMPEL360 BREX Development Guidelines
- S1000D User Guide - BREX Best Practices
