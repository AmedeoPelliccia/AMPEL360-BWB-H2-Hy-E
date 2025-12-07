# 03-00-08-07-01A - Build Records

## 1. Purpose

This document defines requirements and standards for build records documentation for prototypes within the AMPEL360-BWB-H2-Hy-E program, ensuring traceability and quality.

## 2. Scope

This specification covers build documentation requirements, manufacturing travelers, inspection records, and material certifications for all prototype fabrication activities.

## 3. Applicable Documents

- ATA 03-00-08-01-01A_Prototyping_Strategy
- ATA 03-00-08-06-03A_Configuration_Control
- ATA 03-00-09_Production_Planning
- AS9100 - Quality Management Systems

## 4. Description

### 4.1 Overview

Build records document the fabrication history of each prototype, providing traceability from raw materials through final assembly. Complete build records are essential for understanding prototype configuration, supporting test data interpretation, and transitioning to production.

### 4.2 Requirements

**Build Record Components:**

**Manufacturing Traveler:**
- Unique traveler number
- Prototype identification
- Build sequence steps
- Sign-off for each step
- Inspection hold points
- Quality stamps/signatures

**Material Certifications:**
- Material test reports (MTR)
- Certificate of conformance (CoC)
- Heat/lot traceability
- Special process certifications

**Process Records:**
- Welding procedure specifications (WPS)
- Welding procedure qualification records (WPQR)
- Welder qualifications
- Heat treatment records
- Composite cure records
- NDI reports

**Inspection Records:**
- First article inspection (FAI)
- In-process inspections
- Final inspection reports
- Dimensional inspection data
- Non-conformance reports (NCR)
- Deviation approvals

**Assembly Records:**
- Sub-assembly records
- Torque specifications and actuals
- Witness marks/safety wire
- Cleanliness verification
- Leak test results (if applicable)

### 4.3 Methodology

**Build Documentation Process:**

1. **Pre-Build Preparation**
   - Generate manufacturing traveler from BOM and drawings
   - Procure materials with certifications
   - Verify special process qualifications
   - Prepare inspection points

2. **During Build**
   - Follow traveler sequence
   - Sign off each completed step
   - Perform in-process inspections
   - Document deviations immediately
   - Take photos at key stages

3. **Quality Inspections**
   - Perform inspections per traveler
   - Record measurements
   - Generate inspection reports
   - Disposition any non-conformances
   - Obtain quality stamps

4. **Post-Build**
   - Compile complete build record package
   - Verify all signatures and stamps
   - Scan/digitize records
   - Archive in document management system
   - Assign to prototype serial number

5. **Handoff to Test**
   - Transfer build records to test team
   - Review as-built configuration
   - Brief on any deviations or special notes
   - Maintain records with prototype

**Build Record Package Contents:**

```
Prototype Build Record
├── Cover Sheet (ID, dates, approvals)
├── Manufacturing Traveler (signed)
├── Material Certifications
│   ├── MTRs
│   ├── CoCs
│   └── Traceability records
├── Process Records
│   ├── Weld records
│   ├── Heat treatment records
│   ├── Composite cure records
│   └── Special process certs
├── Inspection Records
│   ├── FAI report
│   ├── In-process inspections
│   ├── Final inspection
│   └── Dimensional data
├── Non-Conformance Records
│   ├── NCRs
│   ├── Deviation requests
│   └── Dispositions
├── Assembly Records
│   ├── Torque sheets
│   ├── Leak test results
│   └── Cleanliness verification
└── Photos
    ├── Key build stages
    ├── Final configuration
    └── Special features
```

**Digital Records Management:**

- Scan paper records to PDF
- Store in PLM/PDM system
- Link to prototype serial number
- Enable search by part number, serial number, material lot
- Maintain backup copies
- Control access (read-only for most users)

## 5. Deliverables

| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Manufacturing Traveler | Document | Manufacturing Engineer | Before build |
| Completed Traveler (signed) | Document | Manufacturing | After build |
| Build Record Package | Document Package | Quality | After build |
| Material Certifications | Certificates | Procurement / Supplier | Before use |
| Inspection Reports | Reports | Quality Inspector | During/After build |

## 6. Quality Criteria

**Build Record Quality:**
- Complete (all required elements present)
- Accurate (matches as-built configuration)
- Traceable (material lots, processes linked)
- Signed/stamped per requirements
- Legible (readable scans)

**Compliance:**
- All steps completed and signed
- All inspections performed and recorded
- All NCRs dispositioned
- Material certifications on file
- Special process certifications current

## 7. Cross-References

- Related ATA Chapters: ATA 03-00-09 (Production Planning)
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
