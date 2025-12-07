# 03-00-08-06-03A - Configuration Control

## 1. Purpose

This document defines configuration management practices for prototypes within the AMPEL360-BWB-H2-Hy-E program, ensuring traceability and version control throughout iterative development.

## 2. Scope

This specification covers configuration identification, change control, status accounting, and audits for all prototype hardware, software, and documentation.

## 3. Applicable Documents

- ATA 03-00-08-01-01A_Prototyping_Strategy
- ATA 03-00-11_EIS_Versions_Tags
- AS9100 - Quality Management Systems
- ISO 10007 - Configuration Management

## 4. Description

### 4.1 Overview

Configuration control for prototypes balances the need for rapid iteration with traceability and reproducibility. While less rigid than production configuration management, prototype CM ensures that the "as-built" and "as-tested" configurations are known and documented.

### 4.2 Requirements

**Configuration Management Elements:**

**Configuration Identification:**
- Unique identifier for each prototype version
- Part numbering scheme
- Drawing and document revision control
- Software version control
- Test configuration identification

**Configuration Control:**
- Change request process
- Change evaluation and approval
- Implementation verification
- Configuration updates

**Configuration Status Accounting:**
- Current configuration baseline
- Change history
- As-built vs. as-designed differences
- Test history by configuration

**Configuration Audits:**
- Physical configuration audits (PCA)
- Functional configuration audits (FCA)
- Documentation verification

### 4.3 Methodology

**Prototype Numbering Scheme:**

```
AMPEL-[ATA]-[SYS]-[PROTO]-[VER]

Example: AMPEL-28-H2TANK-P01-V3
- ATA: 28 (Fuel Systems)
- SYS: H2TANK (Hydrogen Tank)
- PROTO: P01 (Prototype 1)
- VER: V3 (Version 3)
```

**Configuration Baseline:**

**Initial Baseline (Ver 1.0):**
- Initial design released for fabrication
- Drawings and specs approved
- Bill of materials (BOM) established
- Software version (if applicable) baselined

**Subsequent Versions:**
- Incremental version numbers (1.1, 1.2, ...)
- Major changes = integer increment (2.0, 3.0)
- Minor changes = decimal increment (1.1, 1.2)

**Change Control Process:**

1. **Initiate Change Request**
   - Fill out change request form (CR-XXXX)
   - Describe proposed change
   - Provide rationale
   - Identify affected items

2. **Evaluate Change**
   - Technical review
   - Impact assessment (cost, schedule, performance)
   - Risk assessment
   - Recommend approval/rejection

3. **Approve Change**
   - Configuration Control Board (CCB) review
   - Obtain approvals
   - Assign implementation owner
   - Update schedule

4. **Implement Change**
   - Update design documentation
   - Fabricate/modify prototype
   - Verify implementation
   - Update as-built records

5. **Update Configuration**
   - Increment version number
   - Update BOM and drawings
   - Record change in database
   - Notify stakeholders

**Configuration Documentation:**

**Design Documentation:**
- CAD models (versioned)
- Drawings (revision letters)
- Specifications (version numbers)
- Analysis reports

**Build Documentation:**
- As-built drawings (redlines)
- Manufacturing travelers
- Inspection reports
- Material certifications
- Deviation records

**Test Documentation:**
- Test configuration sheets
- Instrumentation lists
- Software versions used
- Test data files

**Configuration Baseline Review:**

Hold configuration reviews at key milestones:
- Before first test (Baseline V1.0)
- After major design changes
- Before transition to production
- Quarterly for long-running programs

**Configuration Audit:**

**Physical Configuration Audit (PCA):**
- Verify as-built matches documentation
- Check part numbers and serial numbers
- Inspect for deviations
- Update as-built records

**Functional Configuration Audit (FCA):**
- Verify functionality per specifications
- Check test results
- Confirm performance requirements
- Document any waivers or deviations

## 5. Deliverables

| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Configuration Management Plan | Document | CM Manager | Program start |
| Prototype Configuration Baseline | Document Package | CM Manager | Per version |
| Change Request Form | Form | Requester | As needed |
| Change Log | Spreadsheet | CM Manager | Ongoing |
| Configuration Audit Report | Report | CM Manager | Per audit |

## 6. Quality Criteria

**CM Quality:**
- All prototypes uniquely identified
- Current configuration documented
- Change history complete
- As-built documentation accurate
- Traceability maintained

**Audit Quality:**
- Physical config matches documentation
- Functional performance verified
- Deviations documented
- Corrective actions identified

## 7. Cross-References

- Related ATA Chapters: ATA 03-00-11 (EIS Versions Tags)
- Parent Document: 03-00-08_Prototyping
- Related Engineering Docs: 03-00-06_Engineering
- Related V&V Docs: 03-00-07_V_AND_V

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation WG | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
