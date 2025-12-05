# Q100-61-PRT-STD-REVISION — Part Revision Control Standard

## Purpose

This document defines the revision control procedures for parts used in the Q100 program propulsion system (ATA 61 - Propellers/Propulsors).

## Revision Identifier

Parts use a single-letter revision identifier:

| Revision | Meaning |
|----------|---------|
| - | Initial release (dash or blank) |
| A | First revision |
| B | Second revision |
| C | Third revision |
| ... | Continue alphabetically |

### Excluded Letters

The following letters are **not used** to avoid confusion:
- I (looks like 1)
- O (looks like 0)
- Q (looks like O)
- S (looks like 5)
- X (reserved for obsolete)
- Z (reserved for prototype)

## Revision Levels

### Prototype (Z-prefix)

Pre-production parts use Z-prefix revisions:
- Z1, Z2, Z3, ... (prototype iterations)

Prototype parts are not released for production.

### Production

Production parts start with revision A (or dash for initial):
- A, B, C, D, E, F, G, H, J, K, L, M, N, P, R, T, U, V, W, Y

### Obsolete (X-suffix)

Obsoleted revisions are marked with X-suffix:
- AX = Revision A, obsolete
- BX = Revision B, obsolete

## Revision History

Each part definition YAML includes a revision history:

```yaml
revision_history:
  - revision: "A"
    date: "2025-12-05"
    author: "Engineering"
    description: "Initial release"
    ecn: "ECN-61-001"

  - revision: "B"
    date: "2025-12-15"
    author: "Engineering"
    description: "Updated material specification"
    ecn: "ECN-61-015"
```

## Engineering Change Notice (ECN)

All revisions must be documented via ECN:

| Field | Description |
|-------|-------------|
| ECN Number | Sequential identifier (ECN-61-XXX) |
| Part ID | Affected part identifier |
| From Revision | Current revision |
| To Revision | New revision |
| Description | Summary of changes |
| Reason | Reason for change |
| Effectivity | Serial number or date effectivity |
| Approvals | Required signatures |

## CAD File Revision

CAD files include revision in file properties:
- Document property: "Revision" = current letter
- Filename does NOT include revision

## Interchangeability

| Change Type | Revision | Interchangeable? |
|-------------|----------|------------------|
| Form/Fit change | New letter | No |
| Material upgrade | New letter | Per engineering |
| Drawing clarification | Same letter | Yes |
| Documentation only | Same letter | Yes |

## Supersession

When a part is redesigned with a new part number:
1. Old part revision marked obsolete (X-suffix)
2. Old part definition updated with supersession reference
3. New part created with revision A

```yaml
supersession:
  superseded_by: "Q100-61-PRT-FAN-BLADE-V2"
  supersession_date: "2025-12-20"
  reason: "Redesigned for improved aerodynamics"
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
