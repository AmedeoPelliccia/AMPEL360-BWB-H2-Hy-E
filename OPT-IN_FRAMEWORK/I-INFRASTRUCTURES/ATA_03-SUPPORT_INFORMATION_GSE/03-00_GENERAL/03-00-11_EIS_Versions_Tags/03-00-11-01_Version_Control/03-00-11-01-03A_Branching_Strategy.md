# 03-00-11-01-03A - Branching Strategy

## 1. Purpose

This document defines the Git branching strategy for AMPEL360 BWB-H2-Hy-E development, ensuring organized parallel development, efficient collaboration, and controlled integration of changes across hardware, software, and documentation repositories.

## 2. Scope

This specification covers:
- Git branching model and workflow
- Branch naming conventions
- Branch lifecycle management
- Integration and merge procedures
- Branch protection rules

## 3. Applicable Documents

- [ATA 03-00-06 Engineering](../../03-00-06_Engineering/)
- [ATA 03-00-07 V&V](../../03-00-07_V_AND_V/)
- **Git Flow**: Vincent Driessen's branching model
- **GitHub Flow**: Simplified branching for continuous deployment
- **AS9100**: Quality Management Systems - Aerospace
- **MIL-HDBK-61A**: Configuration Management Guidance

## 4. Description

### 4.1 Overview

The AMPEL360 project adopts a modified **Git Flow** branching strategy tailored for aerospace development, balancing agile development practices with certification requirements and traceability needs.

### 4.2 Requirements

#### 4.2.1 Branch Types

The repository maintains the following branch types:

**Permanent Branches:**
- **`main`**: Production-ready, certified code only
- **`develop`**: Integration branch for ongoing development

**Temporary Branches:**
- **`feature/*`**: Individual feature development
- **`release/*`**: Release preparation and stabilization
- **`hotfix/*`**: Emergency production fixes
- **`bugfix/*`**: Non-critical bug fixes

#### 4.2.2 Branch Naming Conventions

| Branch Type | Naming Pattern | Example |
|-------------|---------------|---------|
| Main | `main` | `main` |
| Development | `develop` | `develop` |
| Feature | `feature/<issue-id>-<short-description>` | `feature/1234-h2-tank-integration` |
| Release | `release/<version>` | `release/2.1.0` |
| Hotfix | `hotfix/<version>-<issue>` | `hotfix/2.0.1-fuel-sensor-fix` |
| Bugfix | `bugfix/<issue-id>-<description>` | `bugfix/5678-ui-alignment` |

#### 4.2.3 Branch Protection Rules

**Main Branch:**
- No direct commits allowed
- Requires pull request with approvals
- Requires passing CI/CD checks
- Requires certification sign-off for production code
- Enforces linear history (no merge commits)

**Develop Branch:**
- Requires pull request with review
- Requires passing automated tests
- Allows merge commits

### 4.3 Procedures

#### 4.3.1 Feature Development Workflow

1. **Create feature branch** from `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/1234-neural-network-ecs
   ```

2. **Develop and commit** changes:
   ```bash
   git add .
   git commit -m "feat(ECS): implement neural network temperature prediction"
   ```

3. **Keep branch updated**:
   ```bash
   git fetch origin
   git rebase origin/develop
   ```

4. **Push and create pull request**:
   ```bash
   git push origin feature/1234-neural-network-ecs
   # Create PR via GitHub interface
   ```

5. **Merge after approval**:
   - Squash commits for clean history
   - Delete feature branch after merge

#### 4.3.2 Release Workflow

1. **Create release branch** from `develop`:
   ```bash
   git checkout develop
   git checkout -b release/2.1.0
   ```

2. **Stabilization phase**:
   - Bug fixes only (no new features)
   - Update version numbers
   - Update documentation
   - Run certification test suites

3. **Merge to both `main` and `develop`**:
   ```bash
   git checkout main
   git merge --no-ff release/2.1.0
   git tag -a v2.1.0 -m "Release version 2.1.0"
   
   git checkout develop
   git merge --no-ff release/2.1.0
   ```

4. **Delete release branch**:
   ```bash
   git branch -d release/2.1.0
   ```

#### 4.3.3 Hotfix Workflow

1. **Create hotfix branch** from `main`:
   ```bash
   git checkout main
   git checkout -b hotfix/2.0.1-critical-safety-fix
   ```

2. **Implement fix** and test thoroughly

3. **Merge to both `main` and `develop`**:
   ```bash
   git checkout main
   git merge --no-ff hotfix/2.0.1-critical-safety-fix
   git tag -a v2.0.1 -m "Hotfix: Critical safety issue resolved"
   
   git checkout develop
   git merge --no-ff hotfix/2.0.1-critical-safety-fix
   ```

4. **Delete hotfix branch**

#### 4.3.4 Commit Message Format

Use **Conventional Commits** specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example:**
```
feat(propulsion): add hydrogen fuel cell monitoring

Implement real-time monitoring of H2 fuel cell stack
temperature, pressure, and power output.

Relates-to: REQ-70-01-234
Tested-by: Integration Test Suite v2.3
```

## 5. Version/Tag Registry

| Branch Type | Active Branches | Purpose | Last Update |
|-------------|----------------|---------|-------------|
| main | 1 | Production baseline | 2025-12-07 |
| develop | 1 | Integration | 2025-12-07 |
| feature/* | 12 | Active development | 2025-12-07 |
| release/2.2.0 | 1 | Next release prep | 2025-12-01 |

## 6. Approval Requirements

- **Feature Branch Creation**: Developer (self-service)
- **Feature Merge to Develop**: Senior Engineer review
- **Release Branch Creation**: Release Manager
- **Merge to Main**: Chief Engineer + Certification Authority Representative
- **Hotfix Approval**: Emergency Change Control Board (ECCB)

## 7. Cross-References

- **Related ATA Chapters**:
  - [ATA 03-00-06 Engineering](../../03-00-06_Engineering/)
  - [ATA 03-00-07 V&V](../../03-00-07_V_AND_V/)
- **Parent Document**: [03-00-11_EIS_Versions_Tags](../)
- **Related Documents**:
  - [03-00-11-01-04A Merge Policies](./03-00-11-01-04A_Merge_Policies.md)
  - [03-00-11-02-02A Release Criteria](../03-00-11-02_Release_Management/03-00-11-02-02A_Release_Criteria.md)
  - [03-00-11-03-01A Tag Naming Convention](../03-00-11-03_Tagging_Standards/03-00-11-03-01A_Tag_Naming_Convention.md)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07.

---
