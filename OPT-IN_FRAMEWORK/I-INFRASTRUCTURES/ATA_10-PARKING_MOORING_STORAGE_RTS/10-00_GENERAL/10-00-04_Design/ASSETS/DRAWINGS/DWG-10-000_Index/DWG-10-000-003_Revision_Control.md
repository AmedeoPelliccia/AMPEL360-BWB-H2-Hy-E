# DWG-10-000-003 — Revision Control

**Document ID:** DWG-10-000-003  
**Title:** Revision Control Procedures  
**ATA Chapter:** 10 – Parking, Mooring, Storage, RTS  
**Status:** DRAFT  
**Version:** A  
**Date:** 2025-12-09

---

## 1. Purpose

This document defines the revision control procedures for ATA 10 drawings in the Q100 (AMPEL360) aircraft project.

---

## 2. Revision Numbering System

### 2.1 Draft and Preliminary Revisions

- Numeric revisions: 0, 1, 2, ... 99
- Used for internal development and review
- Not released for production use

### 2.2 Released Revisions

- Letter revisions: A, B, C, ... Z
- Used for released drawings
- Requires formal approval process

---

## 3. Revision Process

### 3.1 Initiating a Revision

1. Document change request with justification
2. Assign to drawing owner
3. Create new revision number/letter
4. Update revision date

### 3.2 Making Changes

1. Apply changes to drawing
2. Mark changed areas with revision cloud
3. Add revision triangle with identifier
4. Update title block revision field
5. Update revision history table

### 3.3 Review and Approval

1. Technical review by subject matter expert
2. Safety review (if H₂/HV/safety-critical)
3. Configuration management review
4. Final approval by authorized signatory

---

## 4. Revision Markup Requirements

### 4.1 Cloud Markup

- Draw cloud around changed area
- Use thin line weight (0.25mm)
- Include revision letter/number near cloud
- Remove clouds after two subsequent revisions

### 4.2 Revision Triangle

- Place triangle symbol at each change location
- Include revision letter inside triangle
- Position near but not obscuring critical information

---

## 5. Revision History Table

Each drawing shall maintain a revision history table including:

| Revision | Date | Description | Author | Approver |
|----------|------|-------------|--------|----------|
| 0 | YYYY-MM-DD | Initial release | Name | Name |
| A | YYYY-MM-DD | [Description] | Name | Name |

---

## 6. Supersession and Obsolescence

### 6.1 Superseding Drawings

When a drawing supersedes another:
- Note superseded drawing number in title block
- Add "SUPERSEDES: [drawing number]" note
- Update master drawing index

### 6.2 Obsolete Drawings

When a drawing becomes obsolete:
- Mark drawing status as "OBSOLETE"
- Add "SUPERSEDED BY: [drawing number]" note
- Retain in archive for traceability

---

## 7. Electronic File Management

### 7.1 File Naming Convention

```
Q100-10-[SERIES]-[SEQ]-[TYPE]_[DESCRIPTION]_Rev[X].[EXT]

Example:
Q100-10-800-001-DET_Tank_Isolation_Valve_RevA.svg
```

### 7.2 Metadata Requirements

Each drawing file shall have associated metadata in JSON format:
- Drawing number
- Revision level
- Status
- Dates (created, revised, approved)
- Authors and approvers
- Related assemblies and requirements

### 7.3 Version Control

All drawings shall be stored in version control system:
- Git repository: `AMPEL360-BWB-H2-Hy-E`
- Path: `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_10-.../ASSETS/DRAWINGS/`
- Commit messages shall reference drawing number and revision

---

## 8. Safety-Critical Drawing Reviews

Additional review requirements for safety-critical drawings:

1. **H₂ System Drawings (DWG-10-800):**
   - Cryogenic systems engineer review
   - Safety engineer review
   - Compliance with H₂ safety standards

2. **HV System Drawings (DWG-10-900):**
   - Electrical systems engineer review
   - Safety engineer review
   - Arc flash hazard analysis update

3. **Jacking Drawings (DWG-10-400):**
   - Structural engineer review
   - Load analysis verification
   - Safety factor confirmation

---

## 9. Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.**
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---
