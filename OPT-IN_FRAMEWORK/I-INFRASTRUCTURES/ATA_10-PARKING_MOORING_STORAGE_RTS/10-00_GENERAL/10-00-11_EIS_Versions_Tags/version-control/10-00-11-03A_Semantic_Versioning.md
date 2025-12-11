# 10-00-11-03A: Semantic Versioning

## Document Information
- **Document ID**: 10-00-11-03A
- **Title**: Semantic Versioning
- **Version**: 1.0.0
- **Date**: 2025-12-11
- **Status**: DRAFT
- **Document Type**: policy

## Purpose

This document provides detailed guidance on applying Semantic Versioning 2.0.0 (SemVer) to the AMPEL360-BWB-H2 aircraft program, ensuring consistent and predictable version numbering across all software, systems, and configuration items.

## Scope

Semantic Versioning applies to:
- Software components and modules
- System configurations
- API interfaces
- Data schemas
- Configuration baselines
- Release packages

## Semantic Versioning Specification

### Version Format

**Format**: `MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]`

Where:
- **MAJOR**: Incompatible API/interface changes
- **MINOR**: Backward-compatible functionality additions
- **PATCH**: Backward-compatible bug fixes
- **PRERELEASE**: Optional pre-release identifier
- **BUILD**: Optional build metadata

### Examples

```
0.1.0          - Initial development release
0.5.0-alpha    - Alpha pre-release
0.9.0-beta.1   - First beta pre-release
1.0.0-rc.1     - First release candidate
1.0.0          - First public release (EIS)
1.0.1          - Patch release
1.1.0          - Minor update
2.0.0          - Major update (breaking changes)
```

## Version Number Rules

### Rule 1: Initial Development (0.y.z)

During initial development:
- MAJOR version 0 (0.y.z) indicates development/pre-release
- MINOR version increments for feature additions
- PATCH version increments for fixes
- Public API is not considered stable
- Breaking changes are permitted

**Example Progression**:
```
0.1.0 - Initial alpha
0.2.0 - Added parking procedures
0.2.1 - Fixed mooring calculations
0.3.0 - Added H2 venting integration
0.5.0 - Beta release
```

### Rule 2: First Public Release (1.0.0)

Version 1.0.0 defines the public API/interface:
- Marks Entry Into Service (EIS) for aircraft systems
- Public API is now stable
- All subsequent versioning based on this baseline
- Compatibility rules now apply

### Rule 3: PATCH Version (x.x.Z)

Increment PATCH version when:
- Making backward-compatible bug fixes
- Fixing defects without changing functionality
- Correcting documentation errors
- Improving performance without interface changes
- Internal refactoring without external impact

**Examples**:
- `1.0.0` → `1.0.1`: Fixed parking brake calculation error
- `1.2.3` → `1.2.4`: Corrected H2 vent timing in documentation

**DO NOT increment PATCH for**:
- New features
- Deprecations
- Interface changes
- Breaking changes

### Rule 4: MINOR Version (x.Y.z)

Increment MINOR version when:
- Adding backward-compatible functionality
- Introducing new features
- Deprecating functionality (mark for future removal)
- Substantial new functionality in private code
- Adding new optional parameters
- Enhancing capabilities without breaking existing usage

Reset PATCH to 0 when incrementing MINOR.

**Examples**:
- `1.0.0` → `1.1.0`: Added automated mooring sequence
- `1.5.2` → `1.6.0`: Added BWB-specific clearance checks

**MINOR Changes Include**:
- New optional parameters
- New methods/functions
- New configuration options
- Performance improvements with interface additions
- New H2 safety features (if backward-compatible)

### Rule 5: MAJOR Version (X.y.z)

Increment MAJOR version when:
- Making incompatible API/interface changes
- Breaking backward compatibility
- Removing deprecated features
- Changing fundamental behavior
- Major system redesign
- Certification re-baseline required

Reset MINOR and PATCH to 0 when incrementing MAJOR.

**Examples**:
- `1.9.5` → `2.0.0`: Changed H2 venting API (breaking change)
- `2.3.1` → `3.0.0`: Redesigned parking system architecture

**MAJOR Changes Include**:
- Required parameter changes
- Removed functionality
- Changed method signatures
- Modified data schemas (non-compatible)
- Changed system interfaces
- New certification requirements

### Rule 6: Pre-release Versions

Pre-release identifier format: `-<identifier>[.<number>]`

**Identifiers**:
- `alpha`: Early development, unstable
- `beta`: Feature complete, testing in progress
- `rc`: Release candidate, final testing

**Examples**:
```
1.0.0-alpha
1.0.0-alpha.1
1.0.0-beta
1.0.0-beta.2
1.0.0-rc.1
1.0.0
```

**Precedence**:
```
1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-beta < 1.0.0-rc.1 < 1.0.0
```

**Usage Guidelines**:
- **Alpha**: Internal development, APIs unstable, breaking changes expected
- **Beta**: APIs stable, features complete, bug fixes only
- **RC**: Production-ready candidate, final verification

### Rule 7: Build Metadata

Build metadata format: `+<identifier>`

**Examples**:
```
1.0.0+20251211
1.0.0+exp.sha.5114f85
1.0.0-beta+exp.sha.5114f85.20251211
```

**Usage**:
- Build metadata does NOT affect version precedence
- Used for build identifiers, commit hashes, timestamps
- Ignored in version comparisons

## AMPEL360-BWB-H2 Specific Guidelines

### H2 System Versioning

**Guideline H2-1**: H2 safety-critical changes increment MAJOR version even if interface-compatible, due to certification impact.

**Guideline H2-2**: Cryo system configuration changes follow SemVer based on interface compatibility:
- Temperature range changes (interface): MAJOR
- New monitoring parameters (backward-compatible): MINOR
- Calculation improvements: PATCH

**Example**:
```
H2 Vent System:
1.0.0 - EIS baseline
1.0.1 - Fixed flow calculation
1.1.0 - Added pressure monitoring
2.0.0 - Changed vent valve control interface (breaking)
```

### BWB Configuration Versioning

**Guideline BWB-1**: BWB-specific configurations maintain separate version lineage.

**Guideline BWB-2**: Clearance requirement changes:
- New clearance zones: MINOR
- Changed existing clearances: MAJOR
- Corrected clearance documentation: PATCH

**Example**:
```
BWB Ground Handling Config:
1.0.0 - Initial BWB configuration
1.1.0 - Added wingtip clearance monitoring
1.1.1 - Fixed clearance calculation
2.0.0 - Changed tiedown point locations (breaking)
```

### Baseline Versioning

**Guideline BL-1**: Baselines use milestone-tagged versions:
```
1.0.0-PDR     - Preliminary Design Review baseline
1.5.0-CDR     - Critical Design Review baseline
2.0.0-TRR     - Test Readiness Review baseline
2.5.0-FAI     - First Article Inspection baseline
3.0.0-EIS     - Entry Into Service baseline
```

**Guideline BL-2**: Post-baseline changes increment from baseline version.

## Version Comparison and Precedence

### Comparison Rules

1. Compare MAJOR, MINOR, PATCH numerically left to right
2. Pre-release versions have lower precedence than normal versions
3. Pre-release identifiers compared lexically (ASCII sort)
4. Build metadata ignored in precedence

### Examples

```
Ascending Order:
0.1.0
0.2.0
0.2.1
1.0.0-alpha
1.0.0-alpha.1
1.0.0-beta
1.0.0-rc.1
1.0.0
1.0.1
1.1.0
2.0.0
```

## Version Declaration

### In Documentation

```markdown
## Document Information
- **Version**: 1.2.3
- **Date**: 2025-12-11
- **Status**: RELEASED
```

### In Software

```python
__version__ = "1.2.3"
```

```json
{
  "version": "1.2.3"
}
```

### In Configuration Files

```yaml
version: 1.2.3
release_date: 2025-12-11
```

## FAQ and Common Scenarios

### Q1: When should I increment to 1.0.0?

**A**: At Entry Into Service (EIS) when the system is ready for production use and the public interface is stable.

### Q2: Can I skip version numbers?

**A**: No. Version numbers must increment sequentially without gaps.

### Q3: What if I accidentally release a breaking change as MINOR?

**A**: Issue a PATCH to revert the change and release the breaking change as a new MAJOR version.

### Q4: How do I handle security fixes?

**A**: Security fixes increment PATCH version. If the fix breaks compatibility, increment MAJOR with clear release notes.

### Q5: Can different components have different versions?

**A**: Yes. Each component maintains its own version. Use a compatibility matrix to track relationships.

## Standards and References

- **Semantic Versioning 2.0.0**: https://semver.org/
- **ATA iSpec 2200**: Configuration Management
- **ISO/IEC 19505-1**: Software and System Versioning

## Related Documents

- 10-00-11-01A: Version Control Plan
- 10-00-11-02A: Versioning Policy
- 10-00-11-04A: Change Log Policy

## Document Control

- **Author**: AMPEL360 Configuration Management Team
- **Reviewer**: [To be assigned]
- **Approver**: [To be assigned]
- **Next Review**: 2026-12-11
- **Revision History**:
  - Rev A (v1.0.0) - 2025-12-11 - Initial release

---

**END OF DOCUMENT**
