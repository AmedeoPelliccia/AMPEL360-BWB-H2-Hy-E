# DWG-10-099-B — Drawing Register

**Document ID:** DWG-10-099-B  
**Title:** Drawing Register  
**ATA Chapter:** 10 – Parking, Mooring, Storage, RTS  
**Status:** DRAFT  
**Version:** A  
**Date:** 2025-12-09

---

## 1. Purpose

This document describes the structure of the drawing register for ATA 10 drawings.

---

## 2. Drawing Register Structure

The drawing register shall be maintained as a spreadsheet (Excel or CSV format) with the following columns:

### 2.1 Required Columns

| Column | Description | Format | Example |
|--------|-------------|--------|---------|
| Drawing Number | Full drawing number | Q100-10-XXXX-XXX-XXX | Q100-10-800-001-DET |
| Title | Drawing title | Text (max 100 char) | Tank Isolation Valve |
| Series | Drawing series | DWG-10-XXXX | DWG-10-800 |
| Type | Drawing type code | GA/DET/ASY/etc. | DET |
| Revision | Current revision | A-Z or 0-99 | A |
| Status | Drawing status | Draft/Preliminary/Released | Released |
| Date | Last revision date | YYYY-MM-DD | 2025-12-09 |
| Size | Drawing size | A0/A1/A2/A3/A4 | A3 |
| Scale | Drawing scale | 1:X or NTS | 1:2 |
| H₂ Related | H₂ system flag | Yes/No | Yes |
| HV Related | High voltage flag | Yes/No | No |
| Safety Critical | Safety critical flag | Yes/No | Yes |
| Created By | Author name | Text | J. Smith |
| Approved By | Approver name | Text | M. Johnson |
| Approved Date | Approval date | YYYY-MM-DD | 2025-12-09 |
| Supersedes | Previous drawing | Drawing number | Q100-10-800-001-DET RevA |
| Related Assembly | Assembly reference | ASM-XX-XXX | ASM-10-007-001 |
| Related Requirements | Requirement IDs | Comma-separated | REQ-10-SAF-001, REQ-10-FUN-042 |
| File Path (SVG) | SVG file path | Relative path | ./DWG-10-800/.../xxx.svg |
| File Path (PDF) | PDF file path | Relative path | ./DWG-10-800/.../xxx.pdf |

### 2.2 Optional Columns

- Keywords: Searchable keywords
- Classification: Security classification
- Export Control: Export restrictions
- Notes: Additional notes or comments
- Effectivity: Applicable serial numbers or variants
- Next Review Date: Scheduled review date

---

## 3. Register Maintenance

### 3.1 Update Frequency

The drawing register shall be updated:
- Immediately when a new drawing is created
- Immediately when a drawing is revised
- Immediately when a drawing status changes
- Weekly for any missed updates
- Monthly for verification audit

### 3.2 Responsible Party

- Configuration Management maintains the master register
- Drawing creators submit drawing information
- Approvers confirm approval information
- Quality assurance performs periodic audits

---

## 4. Register Location

The drawing register is maintained in:

**File:** `DWG-10-099-B_Drawing_Register.xlsx` (or `.csv`)  
**Location:** `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/10-00_GENERAL/10-00-04_Design/ASSETS/DRAWINGS/DWG-10-099_Index/`

---

## 5. Register Versions

### 5.1 Version Control

The drawing register itself shall be version controlled:
- Git commit for each update
- Version number in filename optional
- Revision history tracked in Git

### 5.2 Backup

- Daily automated backup
- Cloud storage synchronization
- Quarterly archival backup

---

## 6. Register Queries and Reports

### 6.1 Standard Queries

The register supports queries for:
- Drawings by series
- Drawings by status
- Drawings by safety criticality
- Drawings by revision level
- Drawings requiring approval
- Drawings due for review

### 6.2 Standard Reports

Standard reports generated from the register:
- Drawing index by series
- Revision summary
- Safety-critical drawings list
- Pending approvals list
- Effectivity matrix

---

## 7. Integration

### 7.1 Metadata Integration

The drawing register is synchronized with:
- Drawing metadata JSON files
- Configuration management database
- Document management system
- PLM system (if applicable)

### 7.2 Automated Updates

Where possible, automate:
- New drawing entry creation
- Status updates from workflow
- Approval information capture
- File path validation

---

## 8. Example Register Entry

| Drawing Number | Title | Series | Type | Rev | Status | H₂ | HV | Critical |
|----------------|-------|--------|------|-----|--------|----|----|----------|
| Q100-10-800-001-DET | Tank Isolation Valve | DWG-10-800 | DET | A | Released | Yes | No | Yes |

---

## 9. Data Quality Rules

### 9.1 Validation Rules

- Drawing number must match naming convention
- Drawing must exist in file system
- Status transitions must be valid
- Dates must be in chronological order
- Approvals required before "Released" status
- Safety flags must align with series requirements

### 9.2 Consistency Checks

- Compare register against filesystem
- Verify metadata JSON matches register
- Check for duplicate drawing numbers
- Validate cross-references exist
- Confirm required approvals present

---

## 10. Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.**
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---

## Note

The actual drawing register file (`DWG-10-099-B_Drawing_Register.xlsx` or `.csv`) will be created when drawings are added to the system. This document describes the structure and requirements for that register.

---
