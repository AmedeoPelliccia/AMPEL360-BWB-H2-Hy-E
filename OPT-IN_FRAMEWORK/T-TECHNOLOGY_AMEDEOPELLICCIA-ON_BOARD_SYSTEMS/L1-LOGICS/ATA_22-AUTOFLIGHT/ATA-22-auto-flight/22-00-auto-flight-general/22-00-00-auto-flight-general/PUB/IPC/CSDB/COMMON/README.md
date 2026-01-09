# COMMON — Common Information Sets

## Overview

This directory contains **Common Information Sets** (also called Common Information Repositories or CIR) for the Illustrated Parts Catalog (IPC). These are reusable content fragments that can be referenced from multiple Data Modules.

## Purpose

Common Information Sets provide:
- Centralized storage for reusable content
- Single-source maintenance for shared information
- Consistency across documentation
- Efficient updates (change once, apply everywhere)
- Reduced translation costs
- Simplified content management

## What are Common Information Sets?

Common Information Sets are **reusable content fragments** such as:
- Standard warnings and cautions
- Safety precautions
- Common procedural steps
- Standard definitions
- Boilerplate text
- Abbreviation lists
- Tool descriptions
- Parts information

Instead of copying the same content into multiple Data Modules, authors **reference** common information, which is stored once and included dynamically.

## Naming Convention

Common Information files follow this structure:

```
COM-AMPEL360-{TYPE}-{ID}_{LANG}_{ISSUE}.XML
```

### Components

- **Model ID**: `AMPEL360` (fixed)
- **Type**: Category of common information
  - `WARNING` - Safety warnings
  - `CAUTION` - Caution statements
  - `PROC` - Common procedures
  - `DEF` - Standard definitions
  - `TOOL` - Tool descriptions
  - `ABBR` - Abbreviations and acronyms
- **ID**: `00001` to `99999` (unique identifier)
- **Language**: `EN-US`, `FR-FR`, etc. (ISO language codes)
- **Issue**: `001-00` to `999-99` (issue number)

### Examples

**Standard Warning**:
```
COM-AMPEL360-WARNING-00001_EN-US_001-00.XML
```
*High voltage warning*

**Common Caution**:
```
COM-AMPEL360-CAUTION-00005_EN-US_001-00.XML
```
*Static electricity precaution*

**Standard Procedure**:
```
COM-AMPEL360-PROC-00100_EN-US_001-00.XML
```
*Lockout/tagout procedure*

**Tool Description**:
```
COM-AMPEL360-TOOL-00250_EN-US_001-00.XML
```
*Multimeter usage instructions*

## Content Types

### Safety Notices

**Warnings** (danger, potential injury/death):
```xml
<warning>
  <warningIdent>COM-AMPEL360-WARNING-00001</warningIdent>
  <warningText>
    <para>
      HIGH VOLTAGE - LETHAL POTENTIAL. Ensure power is disconnected 
      and locked out before performing maintenance.
    </para>
  </warningText>
</warning>
```

**Cautions** (equipment damage):
```xml
<caution>
  <cautionIdent>COM-AMPEL360-CAUTION-00001</cautionIdent>
  <cautionText>
    <para>
      Do not apply excessive torque. Over-tightening can damage threads.
    </para>
  </cautionText>
</caution>
```

**Notes** (important information):
```xml
<note>
  <noteIdent>COM-AMPEL360-NOTE-00001</noteIdent>
  <noteText>
    <para>
      Record all test results in aircraft maintenance log.
    </para>
  </noteText>
</note>
```

### Common Procedures

**Standard Tasks**:
- Safety lockout/tagout
- Contamination control
- Cleaning procedures
- Sealing and bonding
- Torque specifications
- Test equipment setup

Example:
```xml
<commonInfo>
  <commonInfoIdent>COM-AMPEL360-PROC-00001</commonInfoIdent>
  <procedure>
    <title>Lockout/Tagout Procedure</title>
    <proceduralStep>
      <para>Identify all energy sources...</para>
    </proceduralStep>
    <!-- Additional steps -->
  </procedure>
</commonInfo>
```

### Definitions and Terminology

**Standard Definitions**:
```xml
<commonInfo>
  <commonInfoIdent>COM-AMPEL360-DEF-00001</commonInfoIdent>
  <definitionList>
    <definitionListItem>
      <term>BITE</term>
      <definition>
        <para>Built-In Test Equipment</para>
      </definition>
    </definitionListItem>
  </definitionList>
</commonInfo>
```

### Tool Descriptions

**Standard Tools**:
```xml
<commonInfo>
  <commonInfoIdent>COM-AMPEL360-TOOL-00001</commonInfoIdent>
  <toolDescription>
    <toolIdent>T-12345-A</toolIdent>
    <toolName>Digital Multimeter</toolName>
    <toolSpec>
      <para>Accuracy: ±0.5%, Range: 0-1000V DC</para>
    </toolSpec>
  </toolDescription>
</commonInfo>
```

## Referencing Common Information

### From Data Modules

Reference common information using `<commonInfoRef>`:

```xml
<proceduralStep>
  <para>Before starting work, apply lockout/tagout procedure:</para>
  <commonInfoRef>
    <commonInfoRefIdent>
      <commonInfoCode>COM-AMPEL360-PROC-00001</commonInfoCode>
    </commonInfoRefIdent>
  </commonInfoRef>
</proceduralStep>
```

### In-context Inclusion

Common information is included inline when document is published:
- Content appears seamlessly in output
- Authors don't duplicate content
- Updates propagate automatically

## Benefits

### Consistency

- Same warning appears identically everywhere
- Standardized terminology across manuals
- Uniform procedure descriptions

### Efficiency

- Create once, use many times
- Update once, apply everywhere
- Reduced authoring time

### Translation

- Translate common content once
- Reuse translations across all modules
- Lower translation costs

### Quality

- Expert-reviewed standard content
- Reduced errors from copy/paste
- Easier to maintain accuracy

## Common Information Categories

### Safety (High Priority)

- Electrical hazard warnings
- Mechanical hazard warnings
- Chemical hazard warnings
- Environmental hazards
- PPE requirements

### Procedures (Standard Tasks)

- Lockout/tagout
- Contamination control
- FOD prevention
- Cleanliness requirements
- Sealing and bonding
- Torque application

### Tools and Equipment

- Standard tool descriptions
- Special tool procedures
- Test equipment specifications
- Ground support equipment

### Definitions

- Technical terminology
- Abbreviations and acronyms
- System-specific terms
- Regulatory terms

### Administrative

- Record-keeping requirements
- Documentation references
- Approval requirements
- Certification statements

## Creating Common Information

### Identification Process

1. **Analyze Content**: Review multiple Data Modules
2. **Identify Patterns**: Find repeated content
3. **Assess Suitability**: Determine if content is truly common
4. **Create Common Info**: Extract to common information file
5. **Update DMs**: Replace duplicated content with references

### Criteria for Common Information

Content should be common if:
- ✅ Used in 3+ Data Modules
- ✅ Identical or nearly identical
- ✅ Changes need to be synchronized
- ✅ Subject to regulatory requirements
- ✅ Benefits from centralized control

Content should NOT be common if:
- ❌ Context-specific variations needed
- ❌ Rarely used (1-2 instances)
- ❌ Frequently customized
- ❌ Module-specific details

## Maintenance

### Update Process

1. **Identify Change**: Determine need for update
2. **Impact Analysis**: Find all references
3. **Update Common Info**: Modify master file
4. **Validate**: Check all referencing DMs
5. **Issue New Version**: Release updated file
6. **Notify Authors**: Alert to changes

### Version Control

- Track all changes with issue numbers
- Maintain change history
- Coordinate with Data Module updates
- Test references after updates

## Best Practices

- **Clear Identification**: Use descriptive identifiers
- **Appropriate Granularity**: Not too large, not too small
- **Context-Independence**: Design for multiple contexts
- **Proper Scope**: Ensure content is truly common
- **Documentation**: Document intended use
- **Review Process**: Expert review before release
- **Change Control**: Formal process for updates

## Validation

Common Information must:
- Validate against S1000D schema
- Comply with BREX rules
- Be context-independent
- Have unique identifiers
- Include complete metadata
- Pass technical review

## Workflow Integration

### Authoring

1. Check if common information exists
2. Reference existing or create new
3. Validate references
4. Preview in context

### Publishing

1. Resolve common information references
2. Include content in output
3. Maintain change markers
4. Generate cross-reference reports

## Related Directories

- `../DM/` - Data Modules that reference common information
- `../PM/` - Publication Modules including DMs with common refs
- `../BREX/` - Validation rules for common information
- `../APPLICABILITY/` - May filter common information by variant

## Tools

Software supporting common information:
- **Arbortext Editor**: Native common info support
- **Oxygen XML Editor**: Reusable content features
- **CCMS**: Content component management systems
- **S1000D Tools**: Specialized common info managers

## Document Control

- **Standard**: S1000D Issue 5.0
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 22 (Autoflight)
- **Publication Type**: IPC (Illustrated Parts Catalog)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia

## References

- S1000D Issue 5.0 Specification - Chapter 3.9.5 (Common Information Repositories)
- AMPEL360 Common Information Guidelines
- Reusable Content Best Practices
