# Template Customization Rules

<!-- Template ID: Q100-61-TPL-STD-CUSTOMIZATION -->

## 1. Purpose

This document defines rules for customizing templates for specific use cases.

---

## 2. Customization Levels

### 2.1 Level 1: No Modification

Use template as-is. Recommended for:
- Standard documents
- Common use cases
- Initial deployment

### 2.2 Level 2: Field Customization

Modify field values only. Allowed for:
- Adding project-specific fields
- Adjusting default values
- Adding optional sections

### 2.3 Level 3: Structure Modification

Modify template structure. Requires:
- Approval per STD-APPROVAL
- New template version
- Documentation of changes

---

## 3. Customization Guidelines

### 3.1 Allowed Customizations

✅ **Allowed:**
- Add optional fields
- Modify examples
- Expand tables
- Add clarifying notes
- Customize for subsystem

### 3.2 Restricted Customizations

⚠️ **Requires Approval:**
- Remove required fields
- Change field names
- Alter structure
- Modify validation rules

### 3.3 Prohibited Customizations

❌ **Not Allowed:**
- Remove Document Control section
- Change template ID format
- Remove traceability fields
- Alter safety-related sections

---

## 4. Creating Derived Templates

### 4.1 When to Create

Create a derived template when:
- Frequent customization is needed
- Subsystem has unique needs
- Standard template is insufficient

### 4.2 Derived Template Naming

```
Q100-61-TPL-[CATEGORY]-[NAME]-[VARIANT].[ext]
```

Example:
- Base: `Q100-61-TPL-RPT-ANALYSIS.md`
- Derived: `Q100-61-TPL-RPT-ANALYSIS-CFD.md`

---

## 5. Customization Documentation

Record customizations in:
1. Template header notes
2. Changelog
3. Usage documentation

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
