# Changelog

All notable changes to ATA Chapter 10 design exports will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Initial EXPORTS directory structure
- Export manifest schema (exports-manifest.schema.json)
- Tooling scripts for package management
- CI/CD workflow for automated exports
- Access control policies
- Cryptographic signing infrastructure

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- Implemented GPG signing for all external releases
- Added SHA256 checksum verification
- Established access control policies

---

## Template for Future Releases

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- New features or capabilities

### Changed
- Changes in existing functionality

### Deprecated
- Features marked for removal in future versions

### Removed
- Features removed in this release

### Fixed
- Bug fixes

### Security
- Security-related changes
```

---

## Version History Template

When creating a new release, copy the template above and fill in:

1. **Version number** — Follow semantic versioning (MAJOR.MINOR.PATCH)
2. **Release date** — ISO format (YYYY-MM-DD)
3. **Changes** — List all changes by category

### Version Numbering Guidelines

- **MAJOR** (X.0.0): Incompatible changes, major architectural changes
- **MINOR** (0.Y.0): New features, backward-compatible additions
- **PATCH** (0.0.Z): Bug fixes, documentation updates

### Example Entry

```markdown
## [1.0.0] - 2025-12-15

### Added
- Complete H2 system design package (ATA 10-800 series)
- 247 engineering drawings with BOMs
- Assembly instructions and installation guides
- 3D STEP models for all major components

### Changed
- Updated drawing metadata format to v2.0
- Improved manifest validation checks

### Fixed
- Corrected part numbering in ASM-10-800-025
- Fixed checksum mismatch in previous release

### Security
- Upgraded GPG key to RSA 4096
- Added multi-signature requirement for RESTRICTED releases
```

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status**: DRAFT – Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-09
- **Owner**: AMPEL360 Configuration Management WG
- **Version**: 1.0.0
