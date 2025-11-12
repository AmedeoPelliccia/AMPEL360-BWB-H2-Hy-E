# Version Control Policy

**Document ID:** AMPEL360-02-00-00-META-VCP  
**Version:** 1.0.0  
**Effective Date:** 2025-09-01

## Purpose

This policy establishes the version control standards and practices for all ATA 02-00-00 documentation to ensure:
- Consistent version numbering
- Complete version history
- Baseline integrity
- Change traceability
- Recovery capability

## Version Numbering Standard

### Format

All documents use **Semantic Versioning**: `MAJOR.MINOR.PATCH`

### Version Components

**MAJOR (X.0.0)**: Incremented for:
- Significant restructuring of document
- Regulatory-driven major changes
- Certification milestone updates
- Complete rewrite or major revision
- Breaking changes to interfaces or procedures

**MINOR (0.X.0)**: Incremented for:
- New sections or chapters added
- Substantial content updates
- Moderate technical changes
- Enhanced procedures or processes
- Non-breaking interface changes

**PATCH (0.0.X)**: Incremented for:
- Editorial corrections
- Typo fixes
- Minor clarifications
- Formatting improvements
- Reference updates
- Minor wording changes

### Pre-Release Versions

During development, documents use `0.X.X` versioning:
- `0.1.0`: Initial draft
- `0.2.0`, `0.3.0`, etc.: Major draft milestones
- `0.X.1`, `0.X.2`, etc.: Minor draft iterations

Upon approval and release, version becomes `1.0.0`.

### Version Incrementing Rules

1. **Only one component increments at a time**
   - When MAJOR increments, MINOR and PATCH reset to 0
   - When MINOR increments, PATCH resets to 0

2. **Example progression**:
   - Initial: 0.1.0
   - Draft updates: 0.2.0, 0.3.0, 0.3.1
   - First release: 1.0.0
   - Editorial fix: 1.0.1
   - Content update: 1.1.0
   - Major revision: 2.0.0

## Version Control System

### Git-Based Version Control

All documents are maintained in Git repository:
- **Repository**: AMPEL360-BWB-H2-Hy-E
- **Branch Structure**:
  - `main`: Released versions only
  - `develop`: Integration branch for approved changes
  - `feature/*`: Individual change branches
  - `hotfix/*`: Emergency fixes to released versions

### Branching Strategy

**Feature Branches**:
```
feature/CR-02-00-XXX-description
```
- Created from `develop`
- One branch per Change Request
- Merged back to `develop` after review
- Deleted after merge

**Hotfix Branches**:
```
hotfix/v1.0.1-critical-fix
```
- Created from `main` for urgent fixes
- Merged to both `main` and `develop`
- Tagged with new version number
- Deleted after merge

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New content or feature
- `fix`: Correction or bug fix
- `docs`: Documentation updates
- `style`: Formatting, no content change
- `refactor`: Content reorganization
- `test`: Test-related changes
- `chore`: Maintenance tasks

**Example**:
```
feat(safety): Add H2 emergency procedures

- Added emergency shutdown procedure
- Added leak response procedure
- Updated safety checklist

Refs: CR-02-00-123
```

### Tags and Releases

Every released version is tagged:
```
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

Tag format: `vMAJOR.MINOR.PATCH`

## Version History

### Version History Log

Every document maintains version history in:
- Document header/footer
- Separate Version_History_Log.csv
- Git commit history

### Version History Entry

Each entry includes:
- Version number
- Date
- Author
- Change summary
- Approval authority
- Related Change Request (if applicable)

### Example Version History Table

| Version | Date | Author | Changes | Approved By |
|---------|------|--------|---------|-------------|
| 1.0.0 | 2025-09-01 | J. Smith | Initial release | CCB |
| 1.0.1 | 2025-09-15 | J. Smith | Fixed typos in Section 3 | Doc Control |
| 1.1.0 | 2025-10-01 | M. Garcia | Added H₂ safety procedures | CCB |
| 2.0.0 | 2025-11-01 | J. Smith | Major restructure per CR-002 | CCB |

## Baseline Management

### Baseline Definition

A **baseline** is an approved and released version that serves as the official reference. All baselines are:
- Registered in Baseline_Registry.csv
- Tagged in version control
- Immutable (no direct edits)
- Traceable to approval

### Establishing a Baseline

1. Document reaches "Approved" status
2. CCB approves baseline establishment
3. Version number assigned (typically X.0.0)
4. Document merged to `main` branch
5. Git tag created
6. Baseline registered
7. Status changed to "Released"

### Baseline Types

**Initial Baseline**: First production release (v1.0.0)
**Updated Baseline**: Revised after approved changes (v1.1.0, v2.0.0, etc.)
**Configuration Baseline**: Complete set of related documents at a specific milestone

### Baseline Registry

The Baseline_Registry.csv records:
- Baseline ID
- Document ID
- Version
- Date established
- Approval authority
- Related Change Requests
- Supersedes (previous baseline)

## Change Control Integration

### Controlled Documents

All baselined documents are **controlled** and can only be changed through:
1. Change Request (CR) submitted
2. Impact assessment performed
3. CCB review and approval
4. Change implemented
5. New version released

### Change Traceability

Every version change is linked to:
- Change Request ID
- Impact assessment
- CCB decision
- Implementation verification
- Related test results

Recorded in Changes_to_Documents.csv in TRACEABILITY folder.

## Recovery and Backup

### Backup Strategy

- **Git Repository**: Primary version control, inherently backed up
- **Daily Backup**: Git repository backed up daily
- **Weekly Snapshot**: Full repository snapshot
- **Monthly Archive**: Long-term archive storage
- **Off-site Backup**: Encrypted backup to cloud storage

### Recovery Procedures

**Single Document Recovery**:
```bash
git checkout <version-tag> -- path/to/document.md
```

**Full Repository Recovery**:
1. Restore from daily backup
2. Verify integrity
3. Test access
4. Notify users

**Point-in-Time Recovery**:
```bash
git checkout <commit-hash>
```

### Disaster Recovery

- **Recovery Time Objective (RTO)**: 4 hours
- **Recovery Point Objective (RPO)**: 24 hours (last daily backup)
- **Tested**: Quarterly disaster recovery drills

## Version Comparison

### Comparing Versions

Tools available for version comparison:
- `git diff`: Command-line comparison
- Git GUI tools: Visual diff
- Document management system: Side-by-side comparison

### Change Tracking

Track what changed between versions:
```bash
git diff v1.0.0 v1.1.0 -- path/to/document.md
```

View changes by author, date, or file.

## Archival of Old Versions

### Retention Policy

- **Released Versions**: Retained for 10 years minimum
- **Superseded Versions**: Retained for 10 years
- **Draft Versions**: Retained for 2 years after release
- **Obsolete Versions**: Retained for 10 years after obsolescence

### Archive Access

- **Active Versions**: Full access for authorized users
- **Superseded Versions**: Read-only access
- **Obsolete Versions**: Restricted access, requires approval

## Quality Assurance

### Version Control Audits

Quarterly audits verify:
- ✅ All documents under version control
- ✅ Version numbering correct
- ✅ Version history complete
- ✅ Tags match releases
- ✅ Branches cleaned up
- ✅ Backups current and tested

### Metrics

Track version control metrics:
- Average time between versions
- Number of versions per document
- Frequency of major/minor/patch updates
- Time to baseline establishment
- Recovery test success rate

## Training

All document authors and controllers must be trained on:
- Version numbering policy
- Git usage for documentation
- Branching and merging
- Commit message standards
- Baseline procedures
- Recovery procedures

## References

- Documentation Governance Plan
- Document Control Procedures
- Change Management Process
- Git Documentation: https://git-scm.com/doc

## Appendices

### Appendix A: Quick Reference

**Creating a new version**:
1. Create feature branch
2. Make changes
3. Commit with proper message
4. Submit for review
5. Merge to develop
6. Tag if release

**Emergency hotfix**:
1. Create hotfix branch from main
2. Make critical fix
3. Test thoroughly
4. Merge to main and develop
5. Tag new version
6. Deploy immediately

### Appendix B: Git Commands Cheatsheet

```bash
# Create feature branch
git checkout -b feature/CR-02-00-123-description develop

# Commit changes
git add path/to/file
git commit -m "feat(scope): description"

# Push to remote
git push origin feature/CR-02-00-123-description

# Tag a release
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0

# View history
git log --oneline --graph --all

# Compare versions
git diff v1.0.0 v1.1.0
```

---

**Document Control:**
- Document ID: AMPEL360-02-00-00-META-VCP
- Version: 1.0.0
- Status: Released
- Owner: Documentation Manager
- Last Updated: 2025-09-01
- Next Review: 2026-09-01
