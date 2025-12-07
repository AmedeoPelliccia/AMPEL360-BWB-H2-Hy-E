# Template Versioning Standard

<!-- Template ID: Q100-61-TPL-STD-VERSIONING -->

## 1. Purpose

This document defines version control practices for templates.

---

## 2. Version Numbering

### 2.1 Format

```
MAJOR.MINOR
```

| Component | When to Increment |
|-----------|-------------------|
| MAJOR | Significant structure changes |
| MINOR | Content updates, clarifications |

### 2.2 Examples

| Version | Change |
|---------|--------|
| 1.0 | Initial release |
| 1.1 | Minor corrections |
| 1.2 | Added optional field |
| 2.0 | Restructured template |

---

## 3. Version Tracking

### 3.1 Template Version Block

Each template must include:

```yaml
template_id: "Q100-61-TPL-XXX-NAME"
version: "1.0"
date: "YYYY-MM-DD"
```

### 3.2 Changelog

Major templates should maintain a changelog:

```markdown
## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-01 | [Name] | Initial release |
| 1.1 | 2025-02-15 | [Name] | Added field XYZ |
```

---

## 4. Compatibility

### 4.1 Backward Compatibility

- MINOR version changes must be backward compatible
- MAJOR version changes may break compatibility
- Document breaking changes clearly

### 4.2 Migration

When templates change significantly:
1. Create migration guide
2. Allow transition period
3. Archive old version

---

## 5. Release Process

### 5.1 Release Steps

1. Finalize template changes
2. Update version number
3. Update changelog
4. Get approval per STD-APPROVAL
5. Release to repository

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
