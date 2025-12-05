# Q100-61-STD-REVISION-CONTROL — Revision Control Standard

## Purpose

This document defines the revision control procedures for ATA 61 engineering drawings in the AMPEL360-BWB-H2-Hy-E project.

## Scope

Applies to all drawing types and drawing sets under ATA 61.

---

## 1. Revision Identification

### 1.1 Revision Letter Scheme

| Revision | Status | Description |
|----------|--------|-------------|
| - | Initial | First release (no letter) |
| A | First revision | First engineering change |
| B–Y | Subsequent | Incremental revisions |
| Z | Reserved | Do not use |

### 1.2 Preliminary Revisions

For pre-release drawings:

| Revision | Status |
|----------|--------|
| P1, P2, P3... | Preliminary drafts |
| PA, PB, PC... | Preliminary reviews |

### 1.3 Examples

```
Q100-61-DRW-OFP-BLADE-001.svg           (Initial release)
Q100-61-DRW-OFP-BLADE-001_A.svg         (Rev A)
Q100-61-DRW-OFP-BLADE-001_P1.svg        (Preliminary 1)
```

---

## 2. Revision Block Content

### 2.1 Required Information

Each revision block entry shall include:

| Field | Description |
|-------|-------------|
| Rev | Revision letter |
| Date | Date of revision (YYYY-MM-DD) |
| Author | Name or initials of author |
| Description | Brief description of change |
| ECN | Engineering Change Notice number |

### 2.2 Format

```
| REV | DATE       | BY   | DESCRIPTION                | ECN      |
|-----|------------|------|----------------------------|----------|
| -   | 2025-12-04 | AP   | Initial release            | -        |
| A   | 2025-12-15 | AP   | Updated blade dimensions   | ECN-0001 |
```

---

## 3. Change Categories

### 3.1 Major Changes

Require new revision letter:

- Dimensional changes
- Material changes
- Functional changes
- Interface changes
- Safety-critical changes

### 3.2 Minor Changes

May use same revision with note:

- Typographical corrections
- Clarifications (no change to design)
- Format/style updates
- Reference updates

---

## 4. Git Version Control

### 4.1 Commit Messages

Use structured commit messages:

```
[ATA-61] [REV-X] Brief description

- Detailed change 1
- Detailed change 2

ECN: ECN-XXXX
Approved-by: Name
```

### 4.2 Branching Strategy

```
main
├── develop
│   └── feature/ata61-drawing-update
└── release/v1.0.0
```

### 4.3 Tags

Tag releases:
```
Q100-61-v1.0.0
Q100-61-v1.1.0
```

---

## 5. Approval Requirements

### 5.1 Revision Approval Matrix

| Change Type | Engineer | Lead | Quality | Certification |
|-------------|:--------:|:----:|:-------:|:-------------:|
| Initial Release | ✓ | ✓ | ✓ | - |
| Minor Revision | ✓ | ✓ | - | - |
| Major Revision | ✓ | ✓ | ✓ | - |
| Safety-Critical | ✓ | ✓ | ✓ | ✓ |

### 5.2 Approval Workflow

See [Q100-61-STD-APPROVAL-WORKFLOW.md](./Q100-61-STD-APPROVAL-WORKFLOW.md) for detailed workflow.

---

## 6. Superseded Drawings

### 6.1 Marking

Superseded drawings shall be marked:
- Watermark: "SUPERSEDED BY [new drawing number]"
- Status field: "OBSOLETE"

### 6.2 Retention

Superseded drawings retained for:
- Traceability
- Historical reference
- Audit purposes

---

## 7. References

- AS9100D — Configuration Management
- ISO 10007 — Configuration Management Guidelines
- [Q100-61-STD-APPROVAL-WORKFLOW.md](./Q100-61-STD-APPROVAL-WORKFLOW.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
