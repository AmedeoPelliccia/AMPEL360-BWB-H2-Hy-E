# 95-00-14-00-003_Ops_Standards_Taxonomy

## Document Information
- **Document ID**: 95-00-14-00-003
- **Title**: Operational Standards Taxonomy
- **Version**: 1.0
- **Date**: 2025-11-17
- **Status**: Active
- **Author**: AMPEL360 Documentation Team

## Purpose

This document defines the taxonomy and classification scheme for operational standards within the 95-00-14 module, ensuring consistent categorization, discoverability, and traceability of operational documentation.

## Taxonomy Structure

### Level 1: Primary Domains

1. **OPERATIONAL_STANDARDS** - Core operational procedures and limits
2. **GOVERNANCE** - Decision-making, accountability, oversight
3. **RISK_COMPLIANCE** - Risk management, regulatory compliance
4. **SUSTAINABILITY** - Environmental, circularity, ESG
5. **IMPROVEMENT** - Continuous learning and enhancement
6. **INCIDENT** - Anomaly detection and response
7. **TRAINING** - Competence and human factors
8. **KNOWLEDGE** - Documentation and information management
9. **VENDOR** - Partner and supplier governance
10. **ETHICS** - Data privacy and ethical operations
11. **ANALYTICS** - KPIs, dashboards, reporting
12. **COMMUNICATION** - Stakeholder engagement
13. **REGULATORY** - ESG and regulatory reporting
14. **STRATEGY** - Long-term planning and maturity

### Level 2: Sub-Domains

Each primary domain contains specific sub-domains as defined in folder structure (e.g., 01_OPERATIONAL_STANDARDS contains SOPs, Limits, Interfaces, etc.).

### Level 3: Document Types

Standard document types across all domains:
- **Policy**: High-level principles and requirements
- **Standard**: Detailed specifications and criteria
- **Procedure**: Step-by-step operational instructions
- **Guideline**: Recommendations and best practices
- **Template**: Reusable document frameworks
- **Checklist**: Verification and compliance tools
- **Register**: Inventory and tracking documents
- **Report**: Analysis and status documentation
- **Diagram**: Visual representations and flows

## Classification Scheme

### Document Classification Tags

**Format**: `[DOMAIN]-[SUBDOMAIN]-[TYPE]-[LIFECYCLE]`

**Examples**:
- `OPS-SOP-PROC-ACTIVE` - Operational SOP procedure in active use
- `RISK-REGISTER-REGISTER-REVIEW` - Risk register under review
- `SUSTAIN-KPI-REPORT-ARCHIVED` - Archived sustainability KPI report

### Lifecycle States

- **DRAFT**: Under development
- **REVIEW**: In review process
- **ACTIVE**: Currently in force
- **SUPERSEDED**: Replaced by newer version
- **ARCHIVED**: Historical record only

### Priority Levels

- **CRITICAL**: Safety-critical or regulatory requirement
- **HIGH**: Significant operational impact
- **MEDIUM**: Standard operational importance
- **LOW**: Reference or supporting information

## Metadata Schema

All documents shall include standardized metadata:

```yaml
document_id: "95-00-14-XX-YYY"
title: "Document Title"
version: "MAJOR.MINOR.PATCH"
date: "YYYY-MM-DD"
status: "[DRAFT|REVIEW|ACTIVE|SUPERSEDED|ARCHIVED]"
author: "Author Name/Team"
owner: "Role/Department"
classification: "[DOMAIN]-[SUBDOMAIN]-[TYPE]-[LIFECYCLE]"
priority: "[CRITICAL|HIGH|MEDIUM|LOW]"
related_ata: ["ATA XX", "ATA YY"]
related_docs: ["95-00-14-XX-YYY", "95-00-14-ZZ-AAA"]
keywords: ["keyword1", "keyword2", "keyword3"]
review_cycle: "Monthly|Quarterly|Annually"
next_review: "YYYY-MM-DD"
```

## Indexing & Search

### Primary Index Fields
- Document ID
- Title
- Domain/Sub-domain
- Document Type
- Keywords
- Related ATA chapters

### Search Facets
- By domain
- By document type
- By lifecycle state
- By owner/author
- By date range
- By priority level

## Relationships & Dependencies

### Document Relationships

**Types**:
- **PARENT_OF**: Higher-level document
- **CHILD_OF**: Detailed implementation
- **SUPERSEDES**: Replaces older document
- **SUPERSEDED_BY**: Replaced by newer document
- **REFERENCES**: Informative link
- **REFERENCED_BY**: Cited by another document
- **DEPENDS_ON**: Prerequisite document
- **SUPPORTS**: Provides supporting information

### Dependency Matrix

Maintained in: `95-00-14-00-005_Ops_Traceability_Matrix.csv`

## Governance Taxonomy

### Decision Types
- **STRATEGIC**: Board-level, long-term direction
- **TACTICAL**: Management-level, operational planning
- **OPERATIONAL**: Day-to-day execution decisions

### Approval Authorities
- **BOARD**: Governance Board
- **COMMITTEE**: Standards/Sustainability Committee
- **MANAGER**: Module/Domain Manager
- **OWNER**: Document Owner
- **PEER**: Peer review only

## Naming Conventions

### File Naming

**Format**: `95-00-14-[FOLDER]-[NUM]_[Title].[ext]`

**Components**:
- `95-00-14`: Fixed prefix (ATA 95, Section 00, Folder 14)
- `[FOLDER]`: Two-digit folder code (00-14)
- `[NUM]`: Three-digit sequential number (001-999)
- `[Title]`: Descriptive title with underscores
- `[ext]`: File extension

**Examples**:
- `95-00-14-01-001_Operational_Standards_Overview.md`
- `95-00-14-03-A-001_Ops_Risk_Register.xlsx`
- `95-00-14-11-A-002_Analytics_Dashboard_Wireframes.svg`

### Asset Naming

**Format**: `95-00-14-[FOLDER]-A-[NUM]_[Description].[ext]`

**Note**: `-A-` indicates ASSETS folder content

## Integration Points

### ATA Chapter Mapping

| 95-00-14 Domain | Primary ATA | Secondary ATA |
|----------------|-------------|---------------|
| OPERATIONAL_STANDARDS | 02, 92 | 31, 45 |
| GOVERNANCE | 00, 01 | 04, 05 |
| RISK_COMPLIANCE | 04, 05 | 02, 95-00-07 |
| SUSTAINABILITY | 95 | 28, 21-80 |
| IMPROVEMENT | 92 | 45, 95-00-07 |
| INCIDENT | 02, 45 | 31, 92 |
| TRAINING | 02, 15 | 95-00-07 |
| KNOWLEDGE | 00 | All |
| VENDOR | 00, 03 | 95 |
| ETHICS | 95 | 31, 45 |
| ANALYTICS | 31, 45 | 92, 95 |
| COMMUNICATION | 00 | All |
| REGULATORY | 00, 95 | 02, 04 |
| STRATEGY | 00 | All |

## Related Documents

- 95-00-14-00-001: Ops Std Sustain Strategy
- 95-00-14-00-002: Scope and Alignment with ATA Operations
- 95-00-14-00-004: Governance and Sustainability Index
- 95-00-14-00-005: Ops Traceability Matrix
- 95-00-14-00-006: Stakeholders and Roles Registry

## Document Control

| Version | Date | Author | Changes | Approved By |
|---------|------|--------|---------|-------------|
| 1.0 | 2025-11-17 | AMPEL360 Doc Team | Initial taxonomy | Pending |

---

**END OF DOCUMENT**
