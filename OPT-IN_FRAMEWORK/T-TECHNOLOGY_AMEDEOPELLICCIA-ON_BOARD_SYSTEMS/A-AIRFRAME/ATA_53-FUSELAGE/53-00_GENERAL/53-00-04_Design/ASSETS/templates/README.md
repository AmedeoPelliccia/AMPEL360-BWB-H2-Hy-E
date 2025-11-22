# ASSETS/templates – Design Documentation Templates

## Purpose

This folder contains standard templates for design documentation in the 53-00-04_Design folder. Using these templates ensures consistency and completeness across all design documentation.

## Available Templates

### CI-Level Templates

1. **[53-00-04-A-001_CI_Definition_Template.yaml](53-00-04-A-001_CI_Definition_Template.yaml)**
   - Metadata template for Configuration Item definitions
   - YAML format for machine-readable configuration
   - Copy to each CI folder as `CI_Definition.yaml`

2. **[53-00-04-A-002_Design_Description_Template.md](53-00-04-A-002_Design_Description_Template.md)**
   - Narrative design description for each CI
   - Covers requirements, concept, detailed design, interfaces, analysis
   - Copy to each CI folder as `Design_Description.md`

3. **53-00-04-A-003_Analysis_Report_Template.md** _(to be created)_
   - Template for analysis reports
   - Standardized structure for stress, fatigue, and other analyses

4. **53-00-04-A-004_Manufacturing_Plan_Template.md** _(to be created)_
   - Manufacturing and production planning template
   - Process steps, tooling, quality requirements

## Usage Guidelines

### When to Use Templates

**Always use templates for**:
- New Configuration Item documentation
- Design reports for design reviews
- Analysis reports for critical components
- Manufacturing plans for released CIs

**Templates may be customized for**:
- Unique component types not covered by standard structure
- Simplified documentation for low-criticality components
- Integration with existing documentation systems

### How to Use Templates

1. **Copy the template** to your target location
2. **Rename** according to naming conventions
3. **Fill in all sections**, delete sections marked as optional if not needed
4. **Do not delete required sections** even if "TBD" or "N/A"
5. **Update Document Control** section with proper version, date, author
6. **Review and approve** per standard process

### Template Maintenance

**Responsibility**: Configuration Manager

**Update Process**:
1. Identify need for template update
2. Draft updated template
3. Review with Chief Design Engineer
4. Communicate changes to team
5. Update template files
6. Archive previous versions

**Version Control**:
- Templates are version controlled in this repository
- Changes logged in commit messages
- Major updates communicated via team meetings

## Template Standards

### Format Standards
- **Markdown (.md)** for text documents
- **YAML (.yaml)** for structured metadata
- **CSV (.csv)** for data tables

### Section Numbering
- Use hierarchical numbering (1, 1.1, 1.1.1)
- Consistent depth (typically 3 levels max)

### Required Sections
- Overview/Purpose
- Requirements (where applicable)
- Design/Description
- Interfaces (where applicable)
- Document Control

### Optional Sections
- May vary by component type
- Marked as "[Optional]" in templates
- Delete if not applicable

### Document Control Section
**Always include**:
- Document ID
- Title
- Version
- Date
- Author
- Approval (name and date)
- Status (Draft, Released, Obsolete)

**For AI-assisted documents, include**:
```markdown
---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _YYYY-MM-DD_.
```

## Related Standards

- **OPT-IN Framework Standard**: [../../../../OPT-IN_FRAMEWORK_STANDARD.md](../../../../../../../../OPT-IN_FRAMEWORK_STANDARD.md)
- **Documentation Standard**: [../../../../AMPEL360_DOCUMENTATION_STANDARD.md](../../../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)
- **CI Structure and Governance**: [../../02_Configuration_Items/53-00-04-02-004_CI_Structure_and_Governance.md](../../02_Configuration_Items/53-00-04-02-004_CI_Structure_and_Governance.md)

---

## Document Control

- **Folder**: `ASSETS/templates`
- **Version**: 1.0
- **Date**: 2025-11-22
- **Owner**: Configuration Manager
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
