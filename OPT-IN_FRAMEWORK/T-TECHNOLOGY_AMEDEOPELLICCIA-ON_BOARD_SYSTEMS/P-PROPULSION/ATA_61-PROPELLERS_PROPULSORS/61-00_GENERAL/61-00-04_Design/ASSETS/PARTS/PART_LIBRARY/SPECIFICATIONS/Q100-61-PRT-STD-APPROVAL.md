# Q100-61-PRT-STD-APPROVAL — Part Approval Workflow

## Purpose

This document defines the approval workflow for parts used in the Q100 program propulsion system (ATA 61 - Propellers/Propulsors).

## Part Status Lifecycle

```
DRAFT → REVIEW → APPROVED → RELEASED → (OBSOLETE)
```

| Status | Description | Actions Allowed |
|--------|-------------|-----------------|
| DRAFT | Initial creation, in development | Edit, Delete |
| REVIEW | Submitted for approval | Comment, Approve, Reject |
| APPROVED | Design approved, not released | Minor edits, Release |
| RELEASED | Available for production | No edits (new revision required) |
| OBSOLETE | No longer valid | Reference only |

## Approval Roles

| Role | Responsibilities |
|------|------------------|
| Author | Create part definition, request review |
| Design Engineer | Technical accuracy, analysis verification |
| Stress Engineer | Structural adequacy (load-bearing parts) |
| Materials Engineer | Material specification, process |
| Manufacturing Engineer | Producibility, cost |
| Quality Engineer | Inspection requirements, QA |
| Chief Engineer | Final design approval |
| Configuration Manager | Release to production |

## Approval Matrix

| Part Category | Required Approvals |
|---------------|-------------------|
| All parts | Author, Design Engineer |
| Structural parts | + Stress Engineer |
| Composite parts | + Materials Engineer |
| Fabricated parts | + Manufacturing Engineer |
| Flight-critical | + Chief Engineer |

## Workflow Steps

### 1. Draft Creation

- Author creates part definition YAML
- Author creates/updates CAD model
- Author completes specification documents

### 2. Review Request

Author sets status to REVIEW and notifies reviewers:

```yaml
approval:
  status: "REVIEW"
  requested_by: "Author Name"
  requested_date: "2025-12-05"
  reviewers:
    - role: "Design Engineer"
      name: "TBD"
      status: "Pending"
```

### 3. Technical Review

Each reviewer:
1. Reviews part definition and CAD
2. Verifies analysis and specifications
3. Provides comments or approval

### 4. Approval Recording

```yaml
approval:
  status: "APPROVED"
  approvals:
    - role: "Design Engineer"
      name: "Engineer Name"
      date: "2025-12-06"
      signature: "TBD"

    - role: "Chief Engineer"
      name: "Chief Name"
      date: "2025-12-07"
      signature: "TBD"
```

### 5. Release

Configuration Manager:
1. Verifies all approvals complete
2. Assigns release number
3. Updates status to RELEASED
4. Archives released version

## Approval Documentation

### Digital Signatures

Approvals are recorded with:
- Role and name
- Date
- Digital signature or unique identifier

### Approval Form

For formal releases, use the Part Approval Form:
- Form Q100-61-FORM-PART-APPROVAL
- Attach to part definition package
- Retain in configuration management system

## Rejection and Rework

If a reviewer rejects:
1. Status returns to DRAFT
2. Rejection comments recorded
3. Author addresses comments
4. New review cycle initiated

```yaml
rejection:
  date: "2025-12-06"
  reviewer: "Stress Engineer"
  reason: "Stress analysis incomplete for fatigue case"
  action_required: "Complete fatigue analysis per spec"
```

## Emergency Release

For urgent production needs:
1. Chief Engineer may issue conditional release
2. Document limitations and conditions
3. Complete full approval within 30 days
4. Track as open action item

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
