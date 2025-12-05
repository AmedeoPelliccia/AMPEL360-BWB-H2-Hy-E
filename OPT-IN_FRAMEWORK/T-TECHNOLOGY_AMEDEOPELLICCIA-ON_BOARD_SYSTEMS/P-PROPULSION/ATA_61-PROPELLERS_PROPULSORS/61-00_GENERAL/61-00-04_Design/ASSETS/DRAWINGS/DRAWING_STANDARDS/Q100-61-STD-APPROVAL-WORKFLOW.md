# Q100-61-STD-APPROVAL-WORKFLOW — Approval Workflow Standard

## Purpose

This document defines the review and approval workflow for ATA 61 engineering drawings in the AMPEL360-BWB-H2-Hy-E project.

## Scope

Applies to all drawing types and drawing sets under ATA 61.

---

## 1. Workflow States

### 1.1 State Definitions

| State | Code | Description |
|-------|------|-------------|
| Draft | DRAFT | Initial creation, work in progress |
| In Review | REVIEW | Submitted for technical review |
| Pending Approval | PENDING | Technical review complete, awaiting approval |
| Approved | APPROVED | Formally approved for release |
| Released | RELEASED | Published and distributed |
| Obsolete | OBSOLETE | Superseded or withdrawn |

### 1.2 State Diagram

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  DRAFT   │────▶│  REVIEW  │────▶│ PENDING  │
└──────────┘     └──────────┘     └──────────┘
     │                │                 │
     │                │                 │
     │                ▼                 ▼
     │           ┌──────────┐     ┌──────────┐
     │           │  (reject)│     │ APPROVED │
     │           └──────────┘     └──────────┘
     │                │                 │
     ◀────────────────┘                 │
                                        ▼
                                  ┌──────────┐
                                  │ RELEASED │
                                  └──────────┘
                                        │
                                        ▼
                                  ┌──────────┐
                                  │ OBSOLETE │
                                  └──────────┘
```

---

## 2. Roles and Responsibilities

### 2.1 Role Definitions

| Role | Responsibility |
|------|----------------|
| Author | Creates and updates drawings |
| Checker | Verifies technical accuracy |
| Lead Engineer | Reviews design adequacy |
| Quality Assurance | Verifies compliance with standards |
| Design Authority | Final approval authority |
| Certification (if applicable) | Certifies safety-critical drawings |

### 2.2 Approval Matrix

| Drawing Type | Author | Checker | Lead | QA | DA | Cert |
|--------------|:------:|:-------:|:----:|:--:|:--:|:----:|
| Part Drawing | ✓ | ✓ | ✓ | ✓ | - | - |
| Assembly Drawing | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| Interface Control | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| Safety-Critical | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Schematic | ✓ | ✓ | ✓ | - | - | - |
| Diagram | ✓ | ✓ | - | - | - | - |

---

## 3. Review Process

### 3.1 Technical Review

**Checker** verifies:
- Dimensional accuracy
- Material specifications
- Manufacturing feasibility
- Standards compliance
- Reference accuracy

### 3.2 Lead Engineer Review

**Lead Engineer** verifies:
- Design intent
- System integration
- Performance requirements
- Interface compatibility

### 3.3 Quality Review

**Quality Assurance** verifies:
- Standard compliance (ASME, ISO)
- Drawing requirements per [Q100-61-STD-DRAWING-REQUIREMENTS.md](./Q100-61-STD-DRAWING-REQUIREMENTS.md)
- Naming convention per [Q100-61-STD-NAMING-CONVENTION.md](./Q100-61-STD-NAMING-CONVENTION.md)
- Revision control per [Q100-61-STD-REVISION-CONTROL.md](./Q100-61-STD-REVISION-CONTROL.md)

---

## 4. Approval Process

### 4.1 Approval Actions

Each approver must:
1. Review the drawing against their checklist
2. Document any findings
3. Either:
   - Approve (sign/initial with date)
   - Request changes (provide comments)
   - Reject (provide justification)

### 4.2 Digital Signature

For digital workflows:
- Use Git commit signatures
- Record approver name and timestamp
- Reference approval in commit message

### 4.3 Approval Record

```yaml
approval:
  author:
    name: "Engineer Name"
    date: "2025-12-04"
    action: "Created"
  checker:
    name: "Checker Name"
    date: "2025-12-05"
    action: "Checked"
  lead:
    name: "Lead Name"
    date: "2025-12-06"
    action: "Approved"
  qa:
    name: "QA Name"
    date: "2025-12-07"
    action: "Approved"
```

---

## 5. Timeline Requirements

### 5.1 Standard Review Times

| Activity | Maximum Duration |
|----------|------------------|
| Technical Check | 3 working days |
| Lead Review | 2 working days |
| QA Review | 2 working days |
| DA Approval | 3 working days |
| Total | 10 working days |

### 5.2 Expedited Reviews

For urgent drawings:
- Notify all reviewers in advance
- Reduce timelines by 50%
- Document reason for expediting

---

## 6. Change Requests

### 6.1 During Review

If changes required:
1. Document findings in review form
2. Return to Author
3. Author updates drawing
4. Re-submit for review

### 6.2 After Release

If changes required:
1. Create Engineering Change Notice (ECN)
2. Follow full approval workflow
3. Increment revision per [Q100-61-STD-REVISION-CONTROL.md](./Q100-61-STD-REVISION-CONTROL.md)

---

## 7. References

- AS9100D — Document Control
- [Q100-61-STD-DRAWING-REQUIREMENTS.md](./Q100-61-STD-DRAWING-REQUIREMENTS.md)
- [Q100-61-STD-NAMING-CONVENTION.md](./Q100-61-STD-NAMING-CONVENTION.md)
- [Q100-61-STD-REVISION-CONTROL.md](./Q100-61-STD-REVISION-CONTROL.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
