# ReFuelEU Aviation Compliance Templates

**Directory:** 02-90-01-A001_Templates  
**Version:** 1.0  
**Date:** 2025-11-12  
**Status:** ACTIVE

---

## Overview

This directory contains ready-to-use templates for AMPEL360 operators to fulfill ReFuelEU Aviation (EU Regulation 2023/2405) reporting and application requirements.

---

## Template Index

| Template ID | Filename | Format | Purpose | Primary Article |
|-------------|----------|--------|---------|-----------------|
| **A001-T1** | ReFuelEU_Article8_Report_Template.csv | CSV | Annual operator reporting data | Article 8 |
| **A001-T2** | FEL_Input_Dataset_Template.csv | CSV | Flight Emissions Label application data | Article 14 |
| **A001-T3** | Exemption_Request_Form_Art5-3_TEMPLATE.md | Markdown | Temporary exemption application | Article 5(3) |

---

## Template Descriptions

### A001-T1: Article 8 Annual Report Template

**File:** `ReFuelEU_Article8_Report_Template.csv`

**Purpose:**  
Template for submitting annual operator report to competent authority (due 31 March each year).

**Usage:**
1. Copy template to new file: `Article8_Report_[YEAR]_[OPERATOR].csv`
2. Replace placeholder values (YYYY, XXX, etc.) with actual operational data
3. Add one row per Union airport operated
4. Validate using CI/CD checks ([02-90-01-007A](../02-90-01-007A_CI_Validation_Rules.md))
5. Submit to verifier for verification statement
6. Submit verified report to competent authority by **31 March**

**Data Sources:**
- Fuel logs from fuel management system
- Flight operations database (flights, hours)
- SAF procurement records and supplier certificates
- Verification body and statement

**Reference Documentation:**
- [02-90-01-002A_Data_Model_Article8.csv](../02-90-01-002A_Data_Model_Article8.csv) — Full schema with examples
- [02-90-01-001A_Regulatory_Scope.md](../02-90-01-001A_Regulatory_Scope.md) — Article 8 requirements

---

### A001-T2: FEL Input Dataset Template

**File:** `FEL_Input_Dataset_Template.csv`

**Purpose:**  
Template for preparing Flight Emissions Label (FEL) application dataset to submit to EASA.

**Usage:**
1. Copy template to new file: `FEL_Dataset_[ROUTE]_[SEASON]_[YEAR].csv`
2. Compile historical operational data (minimum 6 months)
3. Calculate average passengers, cargo, fuel consumption per flight
4. Include H₂ lifecycle emissions from supplier certificates
5. Submit to verifier for verification statement
6. Upload to EASA ReFuelEU Portal (FEL module)
7. Receive FEL certificate within 30 days

**Data Sources:**
- Flight operations database (load factors, cargo)
- Fuel management system (H₂ and SAF uplift)
- H₂ supplier lifecycle emissions certificates
- Fleet technical specifications (aircraft type, capacity)

**Reference Documentation:**
- [02-90-01-006A_FEL_Method_Art14.md](../02-90-01-006A_FEL_Method_Art14.md) — Full FEL methodology
- [02-90-01-001A_Regulatory_Scope.md](../02-90-01-001A_Regulatory_Scope.md) — Article 14 requirements

---

### A001-T3: Exemption Request Form (Article 5(3))

**File:** `Exemption_Request_Form_Art5-3_TEMPLATE.md`

**Purpose:**  
Structured form for requesting temporary exemption from 90% refuelling obligation.

**Usage:**
1. Copy template to new file: `Exemption_Request_[ROUTE]_[DATE].md`
2. Complete all sections marked with [FILL]
3. Gather and attach all required evidence (Annexes A-H)
4. Conduct internal legal/compliance review
5. Submit to competent authority **90 days before** route launch or compliance deadline
6. Await authority decision (typically 4-6 weeks)

**Required Attachments:**
- Annex A: Historical fuel uplift data (12 months)
- Annex B: Turnaround time and utilization analysis
- Annex C: Airport Article 7 H₂ infrastructure report
- Annex D: Alternative solutions assessment
- Annex E: Operational schedules and network maps
- Annex F: Airport/supplier correspondence
- Annex G: Infrastructure partnership MoUs (if applicable)
- Annex H: Other supporting evidence

**Reference Documentation:**
- [02-90-01-003A_Exemption_Workflow_Art5-3.md](../02-90-01-003A_Exemption_Workflow_Art5-3.md) — Full exemption workflow
- [02-90-01-001A_Regulatory_Scope.md](../02-90-01-001A_Regulatory_Scope.md) — Article 5(3) requirements
- **Commission Guidelines** (09 Oct 2024) — Evidence standards

---

## Additional Templates (To Be Developed)

### Planned Templates

| Template | Filename | Status | Target Date |
|----------|----------|--------|-------------|
| **SAF Difficulty Report** | SAF_Access_Difficulty_Report_Template.md | Planned | Q1 2025 |
| **H₂ Infrastructure Readiness Tracker** | H2_Airport_Readiness_Tracker.xlsx | Planned | Q1 2025 |
| **Article 8 Verification Workbook** | Article8_Verification_Workbook.xlsx | Planned | Q2 2025 |
| **FEL Display Code Snippets** | FEL_Display_HTML_Templates.zip | Planned | Q2 2025 |

**Note:** Excel (.xlsx) and Word (.docx) versions of templates will be generated from CSV/Markdown sources using automated conversion scripts.

---

## Template Usage Best Practices

### 1. Version Control
- **Never edit template files directly**
- Always copy template to new file with descriptive name
- Include date/version in filename: `Article8_Report_2024_v1.csv`
- Track changes using git or document management system

### 2. Data Quality
- **Validate early and often** using CI/CD scripts ([02-90-01-007A](../02-90-01-007A_CI_Validation_Rules.md))
- Cross-check with source systems (fuel logs, flight ops database)
- Conduct peer review before submission
- Retain supporting documentation for 3 years (EU ETS requirement)

### 3. Collaboration
- **Assign ownership:** Each template has responsible team/person
- Example: Article 8 → Compliance Team; FEL → Operations/Marketing
- Use shared drive/repository for templates and completed submissions
- Establish approval workflow (preparer → reviewer → authorizer)

### 4. Automation
- **Integrate with AMPEL360 systems:**
  - Auto-populate from fuel management system
  - Pull load factors from flight ops database
  - Fetch H₂ lifecycle data from supplier API
  - Link to DPP/CAOS (ATA 95) for analytics

### 5. Confidentiality
- **Protect sensitive data:**
  - Supplier contracts and pricing (SAF, H₂)
  - Operational details (routes, frequencies)
  - Verification statements (contain proprietary methods)
- Restrict access to compliance team and authorized personnel
- Encrypt when transmitting to external parties

---

## Template Maintenance

### Update Triggers

Templates will be updated when:
- **Regulatory changes:** Commission implementing acts, EASA guidance updates
- **Operator feedback:** Usability improvements, clarifications needed
- **System integration:** New data sources or automation capabilities
- **Lessons learned:** Post-submission reviews identify gaps

### Change Process

1. **Propose Change:** Compliance team drafts update with justification
2. **Review:** Legal, IV&V, and affected business units review
3. **Version Control:** Update template version number and change log
4. **Communicate:** Notify all users via email/portal announcement
5. **Archive Old Version:** Retain for reference (especially if used in prior submissions)
6. **Update Documentation:** Cross-reference updates in main compliance pack

### Version History

| Template | Current Version | Last Updated | Next Review Due |
|----------|-----------------|--------------|-----------------|
| A001-T1 | 1.0 | 2025-11-12 | 2026-01-15 |
| A001-T2 | 1.0 | 2025-11-12 | 2026-01-15 |
| A001-T3 | 1.0 | 2025-11-12 | 2026-01-15 |

---

## Support & Contact

### Internal Support

**AMPEL360 Compliance Team:**
- **Email:** compliance@ampel360.aero
- **Portal:** Internal SharePoint / Confluence
- **Office Hours:** Mon-Fri 08:00-17:00 CET
- **Emergency Contact:** +XX XXX XXX XXXX

### External Resources

**Competent Authority:**
- Contact details per operating license (varies by Member State)
- ReFuelEU Aviation Portal: [National CAA website]

**EASA:**
- General inquiries: info@easa.europa.eu
- FEL support: fel@easa.europa.eu
- Portal technical support: [EASA portal help desk]

**Verifier:**
- Accredited verification body per EU ETS framework
- Contact per service contract

---

## Related Documents

- **[02-90-01-000A_README.md](../02-90-01-000A_README.md):** Overall ReFuelEU compliance pack
- **[02-90-01-001A to 007A]:** Detailed compliance workflows and methodologies
- **AMPEL360_DOCUMENTATION_STANDARD.md:** Repository documentation structure
- **ATA 95 (DPP/CAOS):** Digital Product Passport integration for automation

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-12 | AMPEL360 Compliance Team | Initial templates directory README |

---

**End of Templates README**

For questions or template requests, contact: compliance@ampel360.aero
