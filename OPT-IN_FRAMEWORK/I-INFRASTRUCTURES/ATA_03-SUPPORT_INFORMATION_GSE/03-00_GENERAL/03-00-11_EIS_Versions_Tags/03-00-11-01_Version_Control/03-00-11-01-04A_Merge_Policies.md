# 03-00-11-01-04A - Merge Policies

## 1. Purpose

This document defines merge policies and procedures for AMPEL360 BWB-H2-Hy-E repositories, ensuring code quality, maintaining traceability, and preventing integration issues during collaborative development.

## 2. Scope

This specification covers:
- Merge approval requirements
- Automated checks and gates
- Conflict resolution procedures
- Code review standards
- Merge commit strategies

## 3. Applicable Documents

- [ATA 03-00-06 Engineering](../../03-00-06_Engineering/)
- [ATA 03-00-07 V&V](../../03-00-07_V_AND_V/)
- **AS9100**: Quality Management Systems - Aerospace
- **DO-178C**: Software Considerations in Airborne Systems and Equipment Certification
- **MIL-HDBK-61A**: Configuration Management Guidance

## 4. Description

### 4.1 Overview

Merge policies establish the rules and quality gates that must be satisfied before code can be integrated into protected branches. These policies ensure that all integrated changes maintain system integrity, safety, and certification compliance.

### 4.2 Requirements

#### 4.2.1 Merge to `develop` Branch

**Prerequisites:**
- [ ] Pull request created with clear description
- [ ] At least one peer review approval
- [ ] All automated tests pass (unit, integration, system)
- [ ] No merge conflicts
- [ ] Commit messages follow conventions
- [ ] Documentation updated (if applicable)
- [ ] Linked to issue/requirement ID

**Automated Checks:**
- Continuous Integration (CI) build success
- Code coverage ≥ 80% (for software components)
- Linting and style checks pass
- Security vulnerability scan clean
- License compliance check pass

**Review Requirements:**
- Minimum one senior engineer approval
- For safety-critical components: two approvals required
- For certification artifacts: additional safety engineer review

#### 4.2.2 Merge to `main` Branch

**Prerequisites (in addition to develop requirements):**
- [ ] Release branch stabilization complete
- [ ] All certification test suites pass
- [ ] Documentation package complete and reviewed
- [ ] Configuration Control Board (CCB) approval
- [ ] Chief Engineer sign-off
- [ ] Certification Authority Representative review (if required)
- [ ] Version number assigned and tagged

**Additional Checks:**
- Full regression test suite pass
- Performance benchmarks met
- Memory leak analysis clean
- Static code analysis (MISRA C, DO-178C compliance for software)
- Hardware-in-the-loop (HIL) testing complete (if applicable)

#### 4.2.3 Hotfix Merge

**Prerequisites:**
- [ ] Emergency Change Control Board (ECCB) approval
- [ ] Root cause analysis documented
- [ ] Fix verified in isolated environment
- [ ] Risk assessment completed
- [ ] Rollback plan prepared
- [ ] Customer notification drafted (if required)

**Expedited Review:**
- Fast-track review process for critical safety issues
- Minimum two senior engineers plus safety authority
- Post-implementation review within 48 hours

### 4.3 Procedures

#### 4.3.1 Creating a Merge Request

1. **Prepare branch for merge:**
   ```bash
   git checkout feature/1234-my-feature
   git rebase origin/develop
   git push -f origin feature/1234-my-feature
   ```

2. **Create pull request** with template:
   ```markdown
   ## Description
   [Brief description of changes]
   
   ## Related Issues
   Fixes #1234
   Relates-to: REQ-03-00-234
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update
   
   ## Testing
   - [ ] Unit tests added/updated
   - [ ] Integration tests pass
   - [ ] Manual testing performed
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] No merge conflicts
   ```

3. **Request reviews** from appropriate team members

4. **Address review comments** iteratively

5. **Obtain approvals** and verify all checks pass

6. **Merge** using appropriate strategy

#### 4.3.2 Merge Strategies

**Squash and Merge** (Default for feature branches):
- Combines all commits into a single commit
- Creates clean, linear history
- Use for: Feature branches, bug fixes

**Merge Commit** (For release branches):
- Preserves branch history
- Creates merge commit
- Use for: Release branches, hotfixes

**Rebase and Merge** (For simple changes):
- Replays commits on target branch
- No merge commit created
- Use for: Documentation updates, simple fixes

#### 4.3.3 Conflict Resolution

When merge conflicts occur:

1. **Communicate** with other developers involved
2. **Understand both changes** thoroughly
3. **Resolve conflicts locally:**
   ```bash
   git checkout feature/my-branch
   git fetch origin
   git rebase origin/develop
   # Resolve conflicts in files
   git add <resolved-files>
   git rebase --continue
   ```
4. **Test thoroughly** after resolution
5. **Request re-review** if significant changes made
6. **Document resolution** in merge commit message

#### 4.3.4 Failed Merge Handling

If automated checks fail:

1. **Review failure logs** to identify root cause
2. **Fix issues** in feature branch
3. **Re-run checks** to verify resolution
4. **Do not bypass checks** without CCB approval
5. **Document exceptions** if checks are waived

#### 4.3.5 Post-Merge Verification

After successful merge:

1. **Verify target branch** builds successfully
2. **Run smoke tests** on integrated code
3. **Monitor CI/CD pipeline** for downstream effects
4. **Update related documentation** and traceability matrices
5. **Close related issues** and update project board
6. **Notify stakeholders** of significant changes

## 5. Version/Tag Registry

| Policy Item | Requirement Level | Enforcement | Last Review |
|-------------|------------------|-------------|-------------|
| Peer Review | Mandatory | Automated | 2025-12-07 |
| CI Pass | Mandatory | Automated | 2025-12-07 |
| Code Coverage | Advisory (≥80%) | Automated | 2025-12-07 |
| CCB Approval (main) | Mandatory | Manual | 2025-12-07 |

## 6. Approval Requirements

- **Merge Policy Updates**: Configuration Control Board (CCB)
- **Policy Exceptions**: Chief Engineer
- **Emergency Override**: Program Manager (with post-event review)
- **Tool Configuration**: DevOps Lead with CCB approval

## 7. Cross-References

- **Related ATA Chapters**:
  - [ATA 03-00-06 Engineering](../../03-00-06_Engineering/)
  - [ATA 03-00-07 V&V](../../03-00-07_V_AND_V/)
  - [ATA 03-00-10 Certification](../../03-00-10_Certification/)
- **Parent Document**: [03-00-11_EIS_Versions_Tags](../)
- **Related Documents**:
  - [03-00-11-01-03A Branching Strategy](./03-00-11-01-03A_Branching_Strategy.md)
  - [03-00-11-06-01A Change Request Process](../03-00-11-06_Change_Control/03-00-11-06-01A_Change_Request_Process.md)
  - [03-00-11-06-03A Change Review Board](../03-00-11-06_Change_Control/03-00-11-06-03A_Change_Review_Board.md)

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
