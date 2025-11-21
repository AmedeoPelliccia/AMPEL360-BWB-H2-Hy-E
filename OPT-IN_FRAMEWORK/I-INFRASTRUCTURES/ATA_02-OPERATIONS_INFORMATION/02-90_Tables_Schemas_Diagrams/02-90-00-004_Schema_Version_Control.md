# 02-90-00-004: Schema Version Control

## 1. Purpose

This document describes the version control strategy for schemas and tables in ATA 02-90, including branching, tagging, deprecation rules, change control boards, and compatibility requirements.

## 2. Version Control Principles

### 2.1 Semantic Versioning

All schemas follow [Semantic Versioning 2.0.0](https://semver.org/) (SemVer):

```
MAJOR.MINOR.PATCH
```

- **MAJOR** version: Incompatible API/schema changes (breaking changes)
- **MINOR** version: Backward-compatible functionality additions
- **PATCH** version: Backward-compatible bug fixes and clarifications

#### Examples

- `1.0.0` → Initial stable release
- `1.1.0` → Added new optional fields (backward-compatible)
- `1.1.1` → Fixed documentation typo (no functional change)
- `2.0.0` → Removed deprecated fields (breaking change)

### 2.2 Pre-Release Versions

For schemas under development:

```
MAJOR.MINOR.PATCH-LABEL.BUILD
```

Labels:
- `alpha` – Early development, unstable
- `beta` – Feature-complete, testing phase
- `rc` – Release candidate, final testing

Examples:
- `1.0.0-alpha.1` – First alpha release
- `1.0.0-beta.2` – Second beta release
- `1.0.0-rc.1` – First release candidate
- `1.0.0` – Production release

## 3. Git Branching Strategy

### 3.1 Branch Structure

```
main (production-ready schemas)
├── develop (integration branch)
│   ├── feature/schema-name-description
│   ├── feature/api-name-description
│   └── bugfix/issue-number-description
└── release/vX.Y.Z (release preparation)
```

### 3.2 Branch Naming Conventions

| Branch Type | Pattern | Example | Purpose |
|-------------|---------|---------|---------|
| Main | `main` | `main` | Production-ready schemas |
| Develop | `develop` | `develop` | Integration branch |
| Feature | `feature/<schema>-<description>` | `feature/flight-ops-schema-v2` | New schemas or features |
| Bugfix | `bugfix/<issue>-<description>` | `bugfix/123-fix-timestamp-type` | Bug fixes |
| Release | `release/v<version>` | `release/v2.0.0` | Release preparation |
| Hotfix | `hotfix/v<version>` | `hotfix/v1.2.1` | Critical production fixes |

### 3.3 Branch Lifecycle

1. **Feature Development**
   ```bash
   git checkout develop
   git checkout -b feature/new-energy-schema
   # Make changes
   git commit -m "Add energy monitoring schema v1.0.0"
   git push origin feature/new-energy-schema
   # Create pull request to develop
   ```

2. **Release Preparation**
   ```bash
   git checkout develop
   git checkout -b release/v2.0.0
   # Update version numbers, finalize docs
   git commit -m "Prepare release v2.0.0"
   # Create pull request to main
   ```

3. **Production Release**
   ```bash
   git checkout main
   git merge release/v2.0.0
   git tag -a v2.0.0 -m "Release version 2.0.0"
   git push origin main --tags
   git checkout develop
   git merge main  # Sync develop with main
   ```

## 4. Tagging Strategy

### 4.1 Git Tags

All production releases must be tagged:

```bash
git tag -a v<MAJOR>.<MINOR>.<PATCH> -m "Release version <MAJOR>.<MINOR>.<PATCH>"
```

Tag naming:
- Format: `v<MAJOR>.<MINOR>.<PATCH>`
- Examples: `v1.0.0`, `v1.5.2`, `v2.0.0`

### 4.2 Tag Metadata

Tags must include:
- **Version number**: SemVer format
- **Release date**: ISO 8601 format
- **Changelog**: Summary of changes
- **Breaking changes**: If MAJOR version bump
- **Migration guide**: If breaking changes present

### 4.3 Tag Protection

- Tags are **immutable** once pushed to remote
- Production tags (`v*.*.*`) require approval
- Pre-release tags may be moved during development

## 5. Change Control Process

### 5.1 Change Categories

| Change Type | Approval Required | Review Board | Version Impact |
|-------------|------------------|--------------|----------------|
| **Breaking** | Yes | Architecture + Change Control | MAJOR |
| **Non-breaking addition** | Yes (expedited) | Technical Lead | MINOR |
| **Bug fix** | No (peer review only) | Peer Reviewer | PATCH |
| **Documentation** | No | Peer Reviewer | None |

### 5.2 Change Control Board (CCB)

#### Composition
- **Chair**: Data Architecture Lead
- **Members**: 
  - Domain SMEs (Operations, Energy, Propulsion)
  - Security representative
  - Integration architect
  - Quality assurance representative

#### Responsibilities
- Review and approve schema changes
- Assess impact on existing systems
- Approve deprecation and migration plans
- Maintain schema compatibility matrix

#### Meeting Cadence
- **Regular**: Bi-weekly
- **Emergency**: As needed for critical issues

### 5.3 Change Request Process

1. **Initiator** creates change request (GitHub Issue or formal document)
2. **Technical Lead** performs impact analysis
3. **CCB** reviews and approves/rejects/requests modifications
4. **Implementer** makes changes in feature branch
5. **Peer Reviewer** reviews code and documentation
6. **CCB** approves merge to develop
7. **Release Manager** includes in next release

## 6. Compatibility Requirements

### 6.1 Backward Compatibility

**MINOR and PATCH versions MUST maintain backward compatibility:**

#### Allowed Changes (Backward-Compatible)
- ✅ Add new optional fields
- ✅ Add new tables/collections
- ✅ Add new API endpoints
- ✅ Expand enumeration values
- ✅ Relax validation constraints
- ✅ Add indexes (performance optimization)
- ✅ Improve documentation

#### Prohibited Changes (Breaking)
- ❌ Remove or rename fields
- ❌ Change field data types
- ❌ Change field semantics
- ❌ Make optional fields required
- ❌ Remove API endpoints
- ❌ Change API request/response formats
- ❌ Remove enumeration values

### 6.2 Forward Compatibility

Systems should be designed to **gracefully handle unknown fields:**

- **SQL**: Ignore additional columns in SELECT results
- **JSON/MongoDB**: Ignore unrecognized fields
- **APIs**: Accept and preserve unknown fields in PATCH operations

### 6.3 Compatibility Matrix

Maintain a compatibility matrix in release notes:

| Schema Version | Compatible API Versions | Compatible Database Versions | Notes |
|----------------|-------------------------|------------------------------|-------|
| v2.0.0 | v2.x.x | PostgreSQL 13+, MongoDB 5+ | Breaking: Removed deprecated fields |
| v1.5.0 | v1.x.x, v2.0.0+ | PostgreSQL 12+, MongoDB 4.4+ | Added energy monitoring fields |
| v1.4.2 | v1.x.x | PostgreSQL 12+, MongoDB 4.4+ | Bug fix: Corrected timestamp default |

## 7. Deprecation Policy

### 7.1 Deprecation Process

1. **Announcement**: Mark as deprecated in version X.Y.0
2. **Grace Period**: Maintain for minimum of 2 MAJOR versions or 12 months
3. **Removal**: Remove in next MAJOR version after grace period

### 7.2 Deprecation Markers

#### SQL
```sql
-- @deprecated since v1.5.0, use new_field_name instead
-- Will be removed in v3.0.0
old_field_name VARCHAR(50);
```

#### JSON Schema
```json
{
  "old_field": {
    "type": "string",
    "deprecated": true,
    "description": "Deprecated since v1.5.0. Use new_field instead. Will be removed in v3.0.0."
  }
}
```

#### OpenAPI
```yaml
properties:
  old_field:
    type: string
    deprecated: true
    description: "Deprecated since v1.5.0. Use new_field instead. Will be removed in v3.0.0."
```

### 7.3 Migration Guides

For breaking changes, provide:

1. **What changed**: Clear description of the change
2. **Why it changed**: Rationale for the change
3. **How to migrate**: Step-by-step migration instructions
4. **Code examples**: Before/after examples
5. **Timeline**: Deprecation and removal dates

## 8. Schema Validation

### 8.1 Automated Validation

All schemas must pass automated validation before merge:

#### SQL Schemas
- **SQLFluff**: Linting and style checking
- **Schema Validator**: Custom validation rules
- **Breaking Change Detector**: Compares with previous version

#### JSON Schemas
- **JSON Schema Validator**: Against Draft 7+
- **Breaking Change Detector**: Field removal/type change detection

#### OpenAPI Specifications
- **OpenAPI Validator**: Against OpenAPI 3.1
- **Spectral**: Custom linting rules
- **Breaking Change Detector**: API contract compatibility

### 8.2 CI/CD Integration

```yaml
# Example GitHub Actions workflow
name: Schema Validation
on: [pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Validate SQL Schemas
        run: sqlfluff lint 02-90-01_Database_Schemas/
      - name: Validate OpenAPI
        run: spectral lint 02-90-02_API_Specifications/
      - name: Detect Breaking Changes
        run: ./tools/detect-breaking-changes.sh
```

## 9. Release Process

### 9.1 Release Checklist

- [ ] All changes merged to develop
- [ ] Version numbers updated in all schemas
- [ ] Changelog updated with all changes
- [ ] Migration guide created (if breaking changes)
- [ ] Documentation updated
- [ ] Automated tests passing
- [ ] Peer review completed
- [ ] CCB approval obtained (if required)
- [ ] Release branch created
- [ ] Final validation in staging environment
- [ ] Merge to main approved
- [ ] Git tag created
- [ ] Release notes published

### 9.2 Release Artifacts

Each release must include:

1. **Tagged Git commit** on main branch
2. **Release notes** (GitHub Release)
3. **Changelog** (CHANGELOG.md)
4. **Migration guide** (if breaking changes)
5. **Compatibility matrix** updated
6. **Archived schemas** (ZIP file of all schemas)

### 9.3 Communication

- **Internal**: Notify development teams via Slack/email
- **External**: Update documentation portal
- **Deprecations**: Highlight in release notes and send targeted notifications

## 10. Emergency Hotfix Process

For critical production issues:

1. **Create hotfix branch** from main: `hotfix/v1.2.1`
2. **Fix issue** with minimal changes
3. **Fast-track review** by on-call technical lead
4. **Merge to main** and tag
5. **Merge back to develop**
6. **Document** in post-incident review

## 11. Schema Archival

### 11.1 Archival Policy

- **Current version**: Available in main repository
- **Previous MAJOR versions**: Maintained in `archive/` directory
- **End-of-life versions**: Removed from active repository, preserved in Git history

### 11.2 Archive Structure

```
02-90_Tables_Schemas_Diagrams/
└── archive/
    ├── v1.x/  (Schemas from version 1.x)
    ├── v2.x/  (Schemas from version 2.x)
    └── README.md  (Archive index)
```

## 12. References

- [Semantic Versioning](https://semver.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [JSON Schema](https://json-schema.org/)
- [02-90-00-001 Tables Schemas Overview](./02-90-00-001_Tables_Schemas_Overview.md)
- [02-90-00-002 Data Dictionary Master](./02-90-00-002_Data_Dictionary_Master.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
