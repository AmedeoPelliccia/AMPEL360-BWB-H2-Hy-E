# Document Control Procedures

**Document ID:** AMPEL360-02-00-00-META-DCP  
**Version:** 1.0.0  
**Effective Date:** 2025-09-01

## Purpose

This document establishes the procedures for controlling all documentation within ATA 02-00-00 GENERAL to ensure:
- Document identification and traceability
- Version control and baseline management
- Distribution and access control
- Archival and retrieval

## Scope

These procedures apply to all documents including:
- Technical documentation
- Procedural documentation
- Quality records
- Interface control documents
- Training materials
- Supporting documentation

## Document Identification

### Document Numbering Scheme

Format: **ATA-Section-Subsection-Type-Sequence**

Example: `02-00-01-OVERVIEW`

Components:
- **ATA (02)**: ATA chapter number
- **Section (00)**: Section within chapter
- **Subsection (01)**: Specific subsection
- **Type (OVERVIEW)**: Document type identifier
- **Sequence**: Sequential number if multiple docs of same type

### Document Metadata

Required metadata for all documents:
- Document ID (unique identifier)
- Title (descriptive name)
- Type (Technical, Procedural, Quality, etc.)
- Version (MAJOR.MINOR.PATCH)
- Status (Draft, In Review, Approved, Released, etc.)
- Owner (responsible role/person)
- Author (creator)
- Creation Date
- Last Updated Date
- Next Review Date
- Approval Status
- Classification (Public, Internal, Confidential, etc.)

## Version Control

### Version Numbering

Format: **MAJOR.MINOR.PATCH**

- **MAJOR** (X.0.0): Significant restructuring, regulatory changes, major technical updates
- **MINOR** (0.X.0): Content updates, new sections, moderate changes
- **PATCH** (0.0.X): Editorial corrections, typos, minor clarifications

### Version Control Process

1. **Initial Creation**:
   - Document created in draft status
   - Assigned version 0.1.0
   - Stored in version control system

2. **Development**:
   - PATCH increments for each save during draft (0.1.1, 0.1.2, ...)
   - MINOR increments for significant draft milestones (0.2.0, 0.3.0, ...)

3. **Review**:
   - Version frozen during review period
   - Comments tracked separately
   - Revisions increment PATCH (0.3.1, 0.3.2, ...)

4. **Approval and Release**:
   - Upon approval, version becomes 1.0.0
   - Status changes to "Released"
   - Baseline established

5. **Maintenance**:
   - PATCH for minor updates (1.0.1, 1.0.2, ...)
   - MINOR for moderate updates (1.1.0, 1.2.0, ...)
   - MAJOR for significant changes (2.0.0, 3.0.0, ...)

### Baseline Management

**Baseline Definition**: An approved and released version of a document that serves as the reference for future changes.

**Baseline Process**:
1. Document reaches "Approved" status
2. CCB approves baseline establishment
3. Document status set to "Released"
4. Baseline registered in Baseline_Registry.csv
5. Document locked to prevent unauthorized changes
6. Changes only via CCB-approved Change Requests

**Baseline Types**:
- **Initial Baseline**: First released version (typically 1.0.0)
- **Revised Baseline**: Updated version after approved changes
- **Archived Baseline**: Superseded versions maintained for reference

## Document Status

### Status Definitions

| Status | Description | Editable | Requires Approval |
|--------|-------------|----------|------------------|
| **Draft** | Work in progress, not ready for review | Yes | No |
| **In Review** | Under technical/safety/quality review | No | No |
| **In Approval** | Awaiting final approval signatures | No | Yes |
| **Approved** | Approved but not yet released | No | Already approved |
| **Released** | Official baseline, in active use | No | N/A |
| **Superseded** | Replaced by newer version | No | N/A |
| **Obsolete** | No longer applicable, archived | No | N/A |

### Status Transitions

```
Draft → In Review → In Approval → Approved → Released
                ↑                     ↓
                └─────── Revision ────┘
                         (if rework needed)

Released → Superseded (when new version released)
Superseded → Obsolete (after retention period or by CCB decision)
```

## Document Distribution

### Distribution Matrix

All documents are distributed according to the Distribution_Matrix.csv which defines:
- Who receives each document
- Distribution method (electronic, printed, both)
- Notification requirements
- Access permissions

### Distribution Process

1. **Pre-Release**:
   - Verify document is "Approved" status
   - Check Distribution_Matrix.csv for recipients
   - Prepare distribution package
   - Generate distribution list

2. **Release**:
   - Publish to Document Management System (DMS)
   - Send notifications to distribution list
   - Update Document_Master_List.csv
   - Log distribution in Document_Distribution_Log.csv

3. **Access Control**:
   - Apply access permissions per Access_Control_List.csv
   - Enforce classification restrictions
   - Monitor document access (logged in Document_Access_Log.csv)

### Document Classification

| Classification | Access | Distribution | Example |
|---------------|--------|--------------|---------|
| **Public** | Unrestricted | Open | General information |
| **Internal** | AMPEL360 employees | Internal only | Process documents |
| **Confidential** | Need-to-know basis | Controlled | Design details |
| **Restricted** | Specific approval required | Very limited | Proprietary info |
| **Classified** | Export control applies | Highly restricted | ITAR/EAR controlled |

## Document Archival and Retention

### Retention Policy

| Document Type | Active Period | Archive Period | Disposition |
|--------------|---------------|----------------|-------------|
| **Technical** | Until superseded | 10 years | Review for permanent archival |
| **Quality Records** | Until obsolete | 10 years (minimum) | Permanent archival |
| **Procedural** | Until superseded | 7 years | Destroy after review |
| **Training** | Until superseded | 7 years | Destroy after review |
| **Meeting Minutes** | Indefinite | N/A | Permanent archival |
| **Change Records** | Indefinite | N/A | Permanent archival |

### Archival Process

1. **Superseded Documents**:
   - Status changed to "Superseded"
   - Moved to archive repository
   - Read-only access maintained
   - Linked to superseding document
   - Recorded in archive index

2. **Obsolete Documents**:
   - CCB decision required
   - Status changed to "Obsolete"
   - Moved to deep archive
   - Access restricted to administrators
   - Retention period applied

3. **Disposal**:
   - After retention period expires
   - CCB approval required for disposal
   - Secure destruction (shredding, data wiping)
   - Disposal logged and audited
   - Traceability maintained

## Document Retrieval

### Retrieval Methods

1. **Active Documents**:
   - Search Document Management System (DMS)
   - Browse by ATA chapter/section
   - Search by metadata (title, author, date, etc.)
   - Instant access for authorized users

2. **Archived Documents**:
   - Request via Document Control
   - Search archive index
   - Approval may be required
   - Retrieval within 24-48 hours

3. **Off-site Archives**:
   - Formal request process
   - Justification required
   - Management approval
   - Retrieval within 5-10 business days

### Document Master List

The Document_Master_List.csv is the authoritative index of all documents:
- Updated in real-time as documents are created/modified
- Includes all metadata
- Shows current status and version
- Links to document location
- Tracks review dates
- Identifies document owner

## Access Control

### Role-Based Access Control (RBAC)

Access permissions defined by role:

| Role | Read | Create | Edit | Approve | Delete |
|------|------|--------|------|---------|--------|
| **Author** | ✓ | ✓ | ✓ (own docs) | ✗ | ✗ |
| **Reviewer** | ✓ | ✗ | ✗ | ✗ | ✗ |
| **Approver** | ✓ | ✗ | ✗ | ✓ | ✗ |
| **Document Controller** | ✓ | ✓ | ✓ | ✗ | ✗ |
| **Quality Manager** | ✓ | ✓ | ✓ | ✓ | ✗ |
| **CCB Member** | ✓ | ✓ | ✓ | ✓ | ✗ |
| **Administrator** | ✓ | ✓ | ✓ | ✓ | ✓ |

### Access Control List (ACL)

The Access_Control_List.csv defines:
- User/role to document mapping
- Permission level for each user/role
- Effective dates
- Approval authority
- Exceptions and special cases

### Audit Trail

All document access and modifications logged:
- User ID and timestamp
- Action performed (view, edit, approve, etc.)
- Document ID and version
- IP address and system
- Success/failure status

Logs maintained in:
- Document_Access_Log.csv (viewing)
- Document_Modification_Log.csv (changes)
- Document_Approval_Log.csv (approvals)
- Document_Distribution_Log.csv (distribution)

## Change Control Integration

All document changes must follow the Change Management process:

1. Change Request (CR) submitted
2. Impact assessment performed
3. CCB reviews and decides
4. If approved, change implemented
5. Document version updated
6. Distribution notification sent
7. Change logged in Changes_to_Documents.csv

See CHANGE_MANAGEMENT/ folder for detailed procedures.

## Quality Assurance

### Document Quality Checks

Before release, all documents must pass:
- ✅ Template compliance check
- ✅ Metadata completeness check
- ✅ Standards compliance check (ATA, S1000D)
- ✅ Cross-reference validation
- ✅ Traceability verification
- ✅ Approval authority confirmation
- ✅ Classification appropriate

### Periodic Reviews

All documents subject to periodic review:
- Review frequency defined by document type
- Owner notified 30 days before review due
- Review assesses currency, accuracy, completeness
- Updates initiated via change process if needed
- Review date updated in Document_Master_List.csv

### Audits

Document control processes audited:
- Quarterly internal audits
- Annual external audits (ISO, regulatory)
- Audit findings tracked and resolved
- Corrective actions implemented

## Training

All personnel working with documents must be trained:
- Document control procedures (this document)
- Document management system (DMS) usage
- Version control system operations
- Standards compliance (ATA, S1000D)
- Role-specific responsibilities

Training tracked in TRAINING_COMPETENCY/ folder.

## References

- Documentation Governance Plan
- Configuration Control Board Charter
- Quality Management System
- ATA iSpec 2200 Information Standards
- S1000D International Specification for Technical Publications

## Appendices

### Appendix A: Document Templates

See DOCUMENT_CONTROL/Document_Templates/

### Appendix B: Document Master List

See DOCUMENT_CONTROL/Document_Master_List.csv

### Appendix C: Numbering Schemes

See DOCUMENT_CONTROL/Numbering_Systems/

---

**Document Control:**
- Document ID: AMPEL360-02-00-00-META-DCP
- Version: 1.0.0
- Status: Released
- Owner: Documentation Manager
- Last Updated: 2025-09-01
- Next Review: 2026-09-01
