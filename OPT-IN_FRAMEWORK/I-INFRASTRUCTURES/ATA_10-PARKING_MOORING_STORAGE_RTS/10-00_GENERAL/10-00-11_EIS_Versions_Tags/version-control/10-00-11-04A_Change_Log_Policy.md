# 10-00-11-04A: Change Log Policy

## Document Information
- **Document ID**: 10-00-11-04A
- **Title**: Change Log Policy
- **Version**: 1.0.0
- **Date**: 2025-12-11
- **Status**: DRAFT
- **Document Type**: policy

## Purpose

This policy defines requirements and guidelines for maintaining change logs throughout the AMPEL360-BWB-H2 aircraft program, ensuring complete traceability of changes across all versions, baselines, and configuration items.

## Scope

This policy applies to change logs for:
- Master program change log
- Design change history
- H2 system change history
- Certification change history
- Software change logs
- Configuration item change records
- Baseline change documentation

## Policy Statements

### 1. Mandatory Change Logging

**POLICY 1.1**: All versioned items MUST maintain a change log.

**POLICY 1.2**: All changes affecting configuration items MUST be logged.

**POLICY 1.3**: Change logs MUST be updated before version release.

**POLICY 1.4**: Change logs MUST be version controlled alongside their artifacts.

### 2. Change Log Format

**POLICY 2.1**: Change logs SHALL follow the "Keep a Changelog" format (https://keepachangelog.com/).

**POLICY 2.2**: Change logs SHALL be written in Markdown format.

**POLICY 2.3**: Change logs SHALL use reverse chronological order (newest first).

**POLICY 2.4**: Change logs SHALL group changes by version number.

## Change Log Structure

### Standard Format

```markdown
# Changelog

All notable changes to [PROJECT/COMPONENT] will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature descriptions

### Changed
- Changes to existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security fixes

## [1.0.0] - 2025-12-11

### Added
- Initial release
- Feature 1
- Feature 2

[Unreleased]: https://github.com/user/repo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/user/repo/releases/tag/v1.0.0
```

### Change Categories

**POLICY 3.1**: Changes SHALL be categorized as:

- **Added**: New features, capabilities, or components
- **Changed**: Changes to existing functionality
- **Deprecated**: Features marked for future removal
- **Removed**: Removed features or capabilities
- **Fixed**: Bug fixes and corrections
- **Security**: Security-related changes and fixes

**POLICY 3.2**: Each category SHALL be a level 3 heading (`### Category`).

**POLICY 3.3**: Empty categories SHALL be omitted.

### Entry Format

**POLICY 4.1**: Each change entry SHALL:
- Start with a verb (Added, Fixed, Changed, etc.)
- Be concise but descriptive
- Reference issue/change request numbers where applicable
- Include impact assessment for breaking changes

**Example Entries**:
```markdown
### Added
- Added automated H2 vent monitoring during storage (CR-1234)
- Implemented BWB-specific clearance checks for parking positions

### Fixed
- Fixed mooring load calculation for high wind conditions (BUG-567)
- Corrected H2 detector placement in documentation

### Changed
- **BREAKING**: Changed parking position API to include BWB clearance parameters (CR-890)
- Updated mooring procedure sequence timing
```

## Change Log Maintenance

### 5. Update Requirements

**POLICY 5.1**: Change log updates SHALL occur:
- With every version increment
- Before release approval
- When merging significant feature branches

**POLICY 5.2**: Unreleased section SHALL accumulate changes between releases.

**POLICY 5.3**: Upon release, Unreleased changes move to versioned section with release date.

### 6. Review and Approval

**POLICY 6.1**: Change logs SHALL be reviewed as part of version review.

**POLICY 6.2**: Change logs for MAJOR versions require CCB approval.

**POLICY 6.3**: Inaccurate or incomplete change logs are grounds for release rejection.

## Special Requirements

### 7. H2 System Changes

**POLICY 7.1**: H2 safety-critical changes MUST be clearly marked in change logs.

**POLICY 7.2**: H2 system changes SHALL include:
- Safety impact assessment
- Certification impact
- Compatibility notes with aircraft versions

**Example**:
```markdown
### Added
- **H2 SAFETY**: Added redundant H2 leak detection in Zone 200 (CR-H2-123)
  - Impact: Requires certification amendment
  - Compatible with aircraft v1.2.0+
  - Addresses safety finding SF-H2-045
```

### 8. BWB Configuration Changes

**POLICY 8.1**: BWB-specific changes SHALL be tagged with `[BWB]`.

**POLICY 8.2**: BWB changes affecting ground handling SHALL include operator notification requirements.

**Example**:
```markdown
### Changed
- **[BWB]** Updated wingtip clearance requirements for narrow aprons (CR-BWB-067)
  - Operator notification required
  - Ground crew training update needed
```

### 9. Breaking Changes

**POLICY 9.1**: Breaking changes MUST be marked with `**BREAKING**`.

**POLICY 9.2**: Breaking changes SHALL include:
- Description of incompatibility
- Migration guidance
- Affected components/systems

**Example**:
```markdown
### Changed
- **BREAKING**: Changed mooring point identification scheme from alphanumeric to numeric-only (CR-456)
  - Migration: Update all mooring procedures and software interfaces
  - Affects: Ground handling software v2.x and earlier
  - Migration guide: See DOC-10-MIG-001
```

### 10. Security Changes

**POLICY 10.1**: Security fixes MUST use the `### Security` category.

**POLICY 10.2**: Security entries SHALL include:
- Severity level (Critical, High, Medium, Low)
- CVE number if applicable
- Affected versions
- Mitigation if patch not immediately available

**Example**:
```markdown
### Security
- **HIGH**: Fixed SQL injection in parking position query interface (CVE-2025-XXXX)
  - Affects: v1.0.0 through v1.5.2
  - Fixed in: v1.5.3, v1.6.0
  - Workaround: Sanitize all user inputs (see SECURITY-ADVISORY-001)
```

### 11. Certification Changes

**POLICY 11.1**: Changes affecting certification SHALL be tagged with `[CERT]`.

**POLICY 11.2**: Certification changes SHALL reference:
- Certification document updates
- Authority coordination status
- Compliance demonstration method

**Example**:
```markdown
### Changed
- **[CERT]** Updated H2 vent system compliance demonstration for CS-25.1309 (CR-CERT-234)
  - Updated: Certification Plan CP-10-001 Rev C
  - Authority: EASA coordination complete
  - Method: Analysis + ground test
```

## Change Log Templates

### 12. Standard Templates

**POLICY 12.1**: Project SHALL provide change log templates for:
- Master change log
- Component change logs
- H2 system change logs
- Certification change logs

Templates are located in: `eis-templates/change-log-template.md`

### 13. Automated Tools

**POLICY 13.1**: Automated tools MAY be used to generate change log drafts from commit messages.

**POLICY 13.2**: Auto-generated change logs MUST be reviewed and edited before release.

**POLICY 13.3**: Conventional Commits format is RECOMMENDED for commit messages to aid automation.

## Change Log Links

### 14. Version Links

**POLICY 14.1**: Change logs SHALL include links to:
- Version comparison URLs (git diff)
- Release tag URLs
- Unreleased changes comparison

**Example**:
```markdown
[Unreleased]: https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/releases/tag/v1.0.0
```

### 15. Cross-References

**POLICY 15.1**: Change entries SHALL link to:
- Change requests (CR-XXX)
- Bug reports (BUG-XXX)
- Requirements (REQ-XXX)
- Design documents as applicable

## Quality Standards

### 16. Completeness

**POLICY 16.1**: Change logs SHALL include all user-visible changes.

**POLICY 16.2**: Internal refactoring without external impact MAY be omitted.

**POLICY 16.3**: Documentation-only changes SHALL be logged.

### 17. Clarity

**POLICY 17.1**: Change descriptions SHALL be written for the target audience (operators, maintainers, developers).

**POLICY 17.2**: Technical jargon SHALL be minimized or explained.

**POLICY 17.3**: Acronyms SHALL be defined on first use in each version section.

## Audit and Compliance

### 18. Audit Trail

**POLICY 18.1**: Change logs provide the primary audit trail for version history.

**POLICY 18.2**: Change logs SHALL be included in certification evidence packages.

**POLICY 18.3**: Change log accuracy is subject to configuration audits.

### 19. Retention

**POLICY 19.1**: Change logs SHALL be retained for the life of the aircraft program plus 10 years.

**POLICY 19.2**: Archived change logs remain accessible for audit purposes.

## Standards and References

This policy aligns with:
- **Keep a Changelog**: https://keepachangelog.com/
- **Semantic Versioning**: https://semver.org/
- **Conventional Commits**: https://www.conventionalcommits.org/
- **ATA iSpec 2200**: Configuration Management
- **ISO 10007**: Configuration Management

## Related Documents

- 10-00-11-01A: Version Control Plan
- 10-00-11-02A: Versioning Policy
- 10-00-11-03A: Semantic Versioning
- 10-00-11-60A: Master Change Log
- eis-templates/change-log-template.md

## Document Control

- **Author**: AMPEL360 Configuration Management Team
- **Reviewer**: [To be assigned]
- **Approver**: [To be assigned]
- **Next Review**: 2026-12-11
- **Revision History**:
  - Rev A (v1.0.0) - 2025-12-11 - Initial release

---

**END OF DOCUMENT**
