# Change Log Template

All notable changes to [PROJECT/COMPONENT NAME] will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- [New features or capabilities to be released]

### Changed
- [Changes to existing functionality]

### Deprecated
- [Features marked for future removal]

### Removed
- [Removed features or capabilities]

### Fixed
- [Bug fixes and corrections]

### Security
- [Security-related changes and fixes]

---

## [X.Y.Z] - YYYY-MM-DD

### Added
- [Feature description] ([CR-XXX])
- [Component addition] 
- **[H2]** [H2-related feature] ([CR-H2-XXX])
- **[BWB]** [BWB-specific feature] ([CR-BWB-XXX])

### Changed
- [Change description] ([CR-XXX])
- Updated [component] to improve [aspect]
- **BREAKING**: [Breaking change description] ([CR-XXX])
  - Migration: [Migration guidance]
  - Affects: [Affected systems/versions]

### Deprecated
- [Feature] is now deprecated and will be removed in v[X+1].0.0
- Use [alternative] instead

### Removed
- Removed [obsolete feature] (deprecated in v[X-1].Y.Z)
- Removed support for [legacy component]

### Fixed
- Fixed [bug description] ([BUG-XXX])
- Corrected [calculation/behavior] in [component]
- **[H2 SAFETY]** Fixed [safety-related issue] ([BUG-H2-XXX])

### Security
- **[SEVERITY]**: [Security issue description] ([CVE-YYYY-XXXX])
  - Affects: v[X.Y.Z] through v[A.B.C]
  - Fixed in: v[X.Y.Z+1]
  - Workaround: [If applicable]

---

## [X.Y.Z-1] - YYYY-MM-DD

[Previous version entries...]

---

## Version Links

[Unreleased]: https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/compare/v[LATEST]...HEAD
[X.Y.Z]: https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/compare/v[X.Y.Z-1]...v[X.Y.Z]
[X.Y.Z-1]: https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E/releases/tag/v[X.Y.Z-1]

---

## Change Log Guidelines

### When to Update

- Update this file with **every significant change**
- Update before creating a new version release
- Move Unreleased items to versioned section upon release

### Change Categories

Use these categories in this order:
1. **Added** - New features, capabilities, or components
2. **Changed** - Changes to existing functionality
3. **Deprecated** - Soon-to-be removed features
4. **Removed** - Removed features or capabilities
5. **Fixed** - Bug fixes and corrections
6. **Security** - Security-related changes

### Entry Format

- Start with a verb (Added, Fixed, Changed, etc.)
- Be concise but descriptive
- Reference issue/CR numbers in parentheses: (CR-XXX), (BUG-XXX)
- For breaking changes, use **BREAKING**: prefix and include migration guidance

### Special Markers

- **[H2]** or **[H2 SAFETY]**: H2 system changes
- **[BWB]**: BWB-specific changes
- **[CERT]**: Certification-affecting changes
- **BREAKING**: Breaking/incompatible changes
- **[SEVERITY]**: For security issues (CRITICAL, HIGH, MEDIUM, LOW)

### Examples

Good entries:
```markdown
### Added
- Added automated H2 vent monitoring during storage (CR-1234)
- **[H2 SAFETY]** Implemented redundant H2 leak detection in Zone 200 (CR-H2-567)

### Fixed
- Fixed mooring load calculation for high wind conditions (BUG-890)
- Corrected H2 detector placement coordinates in documentation

### Changed
- **BREAKING**: Changed parking position API to include BWB clearance parameters (CR-456)
  - Migration: Update all API calls to include `bwb_clearance` parameter
  - Affects: Ground handling software v2.x and earlier
  - Migration guide: See DOC-10-MIG-001

### Security
- **HIGH**: Fixed unauthorized access to H2 vent controls (CVE-2025-12345)
  - Affects: v1.0.0 through v1.5.2
  - Fixed in: v1.5.3
  - Workaround: Restrict network access to control interface
```

### Version Numbering

Follow Semantic Versioning:
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- Increment MAJOR for incompatible changes
- Increment MINOR for backward-compatible additions
- Increment PATCH for backward-compatible fixes

Pre-release versions:
- **X.Y.Z-alpha**: Alpha releases
- **X.Y.Z-beta.N**: Beta releases
- **X.Y.Z-rc.N**: Release candidates

### Links

- Update version comparison links at the bottom
- Link to GitHub releases, commits, or tags
- Use consistent link format

---

## Template Notes

1. Copy this template for new change logs
2. Replace [PROJECT/COMPONENT NAME] with actual name
3. Update version links with correct repository URLs
4. Delete this "Template Notes" section in actual change logs
5. Keep template formatting and structure consistent
