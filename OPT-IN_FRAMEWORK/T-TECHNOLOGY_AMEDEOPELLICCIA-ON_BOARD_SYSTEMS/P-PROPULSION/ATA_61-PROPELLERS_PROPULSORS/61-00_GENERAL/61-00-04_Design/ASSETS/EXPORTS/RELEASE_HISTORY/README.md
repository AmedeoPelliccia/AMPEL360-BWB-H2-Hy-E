# RELEASE_HISTORY — Release Versioning and Archive

This directory tracks the release history of all exports from the ATA 61 propulsion system design and provides archival storage for superseded releases.

## Purpose

Release history management enables:

- Version control of all released exports
- Change tracking across releases
- Archival of superseded versions
- Audit trail for certification
- Rollback capability when needed

## Directory Structure

```
RELEASE_HISTORY/
├── README.md           # This file
└── ARCHIVE/            # Archived superseded releases
```

## Release Versioning

### Version Numbering Convention

Releases follow semantic versioning with release designator:

```
Q100-61-REL-[COMPONENT]-V[major].[minor].[patch]
```

| Component | Description                                  |
|-----------|----------------------------------------------|
| major     | Breaking changes, major redesign             |
| minor     | New features, significant updates            |
| patch     | Bug fixes, minor corrections                 |

### Examples

```
Q100-61-REL-FPS-V1.0.0     → Initial release of Full Propulsor System
Q100-61-REL-FPS-V1.1.0     → Added cooling system updates
Q100-61-REL-FPS-V1.1.1     → Minor drawing corrections
Q100-61-REL-FPS-V2.0.0     → Major gearbox redesign
```

### Release Package Structure

```
Q100-61-REL-[COMPONENT]-V[version].zip
├── RELEASE_MANIFEST.yaml      # Release manifest
├── RELEASE_NOTES.md           # Detailed release notes
├── CHANGE_LOG.csv             # Structured change log
├── EXPORTS/                   # All export files for this release
│   ├── NEUTRAL_FORMATS/
│   ├── VISUALIZATION/
│   ├── MANUFACTURING/
│   ├── ANALYSIS/
│   └── DOCUMENTATION/
└── VALIDATION/                # Release validation evidence
    ├── EXPORT_VALIDATION.md
    └── CHECKSUMS.sha256
```

## Release Manifest

Every release MUST include a `RELEASE_MANIFEST.yaml`:

```yaml
# Release Manifest
release_id: Q100-61-REL-[COMPONENT]-V[version]
release_date: YYYY-MM-DD
release_type: "[Major|Minor|Patch|Initial]"

program:
  name: "AMPEL360-BWB-H2-Hy-E"
  designation: "Q100"
  ata_chapter: "61"

component:
  name: "[Component name]"
  identifier: "[Component ID]"

version:
  current: "V[major].[minor].[patch]"
  previous: "V[previous version]"  # null for initial release

status:
  current: "Released"
  classification: "[Internal|Supplier|Customer|Public]"

contents:
  neutral_formats:
    - Q100-61-EXP-[COMPONENT].step
    - Q100-61-EXP-[COMPONENT].jt
  visualization:
    - Q100-61-VIS-[COMPONENT].glb
  manufacturing:
    - Q100-61-MFG-[COMPONENT].step
  analysis:
    - Q100-61-FEA-[COMPONENT].bdf
  documentation:
    - Q100-61-PKG-[COMPONENT]-R[rev].zip

validation:
  export_check: "PASS"
  geometry_validation: "PASS"
  completeness_check: "PASS"

approvals:
  design_engineer: "[Name]"
  design_lead: "[Name]"
  project_engineer: "[Name]"
  quality_engineer: "[Name]"
  release_date: YYYY-MM-DD

dependencies:
  source_cad_version: "[CAD system and version]"
  source_file_revision: "[Revision]"
  configuration: "[Configuration name]"
```

## Change Log Format

Maintain change logs in CSV format:

```csv
change_id,version,date,category,affected_items,description,author,reference
CHG-001,V1.1.0,2025-12-05,Enhancement,FAN-BLADE,Updated blade airfoil profile,J. Smith,REQ-61-123
CHG-002,V1.1.0,2025-12-05,Correction,GBX-HOUSING,Fixed mounting hole location,A. Jones,NCR-001
CHG-003,V1.1.1,2025-12-10,Documentation,ALL,Updated drawing title blocks,M. Brown,DOC-UPDATE
```

### Change Categories

| Category      | Description                              |
|---------------|------------------------------------------|
| Enhancement   | New feature or improvement               |
| Correction    | Fix to existing design                   |
| Documentation | Documentation-only change                |
| Optimization  | Performance or weight optimization       |
| Compliance    | Regulatory compliance update             |
| Safety        | Safety-related modification              |

## Release Notes Template

```markdown
# Release Notes: Q100-61-REL-[COMPONENT]-V[version]

## Release Information

- **Release Date:** YYYY-MM-DD
- **Release Type:** [Major|Minor|Patch]
- **Previous Version:** V[previous]

## Summary

[Brief summary of what's included in this release]

## Changes in This Release

### New Features
- [Feature 1]
- [Feature 2]

### Improvements
- [Improvement 1]
- [Improvement 2]

### Bug Fixes
- [Fix 1]
- [Fix 2]

### Known Issues
- [Issue 1]
- [Issue 2]

## Affected Systems

[List systems/components affected by this release]

## Compatibility

[Compatibility notes with other systems/versions]

## Installation/Usage Notes

[Special instructions for using this release]

## Validation

[Summary of validation performed]

## Approval

| Role               | Name    | Date       |
|--------------------|---------|------------|
| Design Engineer    | TBD     | YYYY-MM-DD |
| Quality Engineer   | TBD     | YYYY-MM-DD |
| Project Engineer   | TBD     | YYYY-MM-DD |
```

## Archive Policy

### When to Archive

Releases are moved to ARCHIVE/ when:

- A new version supersedes the release
- The release is deprecated or withdrawn
- Per retention policy requirements

### Archive Structure

```
ARCHIVE/
├── Q100-61-REL-FPS-V1.0.0.zip
├── Q100-61-REL-FPS-V1.0.0_ARCHIVE_RECORD.yaml
├── Q100-61-REL-FPS-V1.1.0.zip
└── Q100-61-REL-FPS-V1.1.0_ARCHIVE_RECORD.yaml
```

### Archive Record

Each archived release includes an archive record:

```yaml
archive_id: Q100-61-REL-[COMPONENT]-V[version]_ARCHIVE
original_release_date: YYYY-MM-DD
archive_date: YYYY-MM-DD
archive_reason: "[Superseded|Deprecated|Withdrawn]"
superseded_by: "Q100-61-REL-[COMPONENT]-V[new_version]"
retention_period: "[Duration or 'Permanent']"
archived_by: "[Name]"
notes: "[Additional notes]"
```

### Retention Periods

| Release Type      | Retention Period                         |
|-------------------|------------------------------------------|
| Certification     | Permanent (aircraft lifetime + 5 years)  |
| Manufacturing     | 10 years after last production           |
| Development       | 5 years                                  |
| Prototype         | 3 years                                  |

## Release Register

Maintain a master register of all releases:

| Release ID | Component | Version | Date | Status | Notes |
|------------|-----------|---------|------|--------|-------|
| Example    | FPS       | V1.0.0  | 2025-12-05 | Archived | Superseded by V1.1.0 |
| Example    | FPS       | V1.1.0  | 2025-12-15 | Current | Active release |

## Related Documentation

- [../README.md](../README.md) - EXPORTS overview
- [Q100-61-EXPORT-SETTINGS.yaml](../Q100-61-EXPORT-SETTINGS.yaml) - Export settings
- [../SUPPLIER_PACKAGES/README.md](../SUPPLIER_PACKAGES/README.md) - Supplier packages

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
