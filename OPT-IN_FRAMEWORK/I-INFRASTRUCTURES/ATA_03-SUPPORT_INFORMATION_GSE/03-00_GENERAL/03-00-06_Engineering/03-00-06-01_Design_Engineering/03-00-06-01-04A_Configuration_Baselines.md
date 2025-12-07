# 03-00-06-01-04A - Configuration Baselines

## 1. Purpose
Define the process for establishing, documenting, and managing configuration baselines throughout the AMPEL360 BWB-H2-Hy-E aircraft development, ensuring controlled evolution of design and maintaining traceability of changes.

## 2. Scope
This document covers:
- Configuration baseline types and definitions
- Baseline establishment criteria and process
- Configuration control board (CCB) operations
- Change request and approval workflows
- Baseline documentation and release procedures
- Impact analysis for configuration changes
- Configuration audits and compliance verification

## 3. Applicable Documents
- [EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012) - Certification of Aircraft and Related Products, Subpart J - Design Organization Approval
- [ISO 10007](https://www.iso.org/standard/70400.html) - Quality Management - Guidelines for Configuration Management
- [SAE EIA-649](https://www.sae.org/standards/content/eia649c/) - Configuration Management Standard
- [MIL-STD-973](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36026) - Configuration Management (reference)

## 4. Description

### 4.1 Overview
Configuration management ensures that the aircraft design is properly identified, controlled, and documented throughout its lifecycle. For the BWB-H2-Hy-E aircraft, configuration baselines provide reference points for design evolution, change impact assessment, and certification compliance, addressing both the innovative airframe configuration and advanced hydrogen propulsion systems.

### 4.2 Requirements
**Baseline Types:**
1. **Functional Baseline** - Approved system requirements and specifications
2. **Allocated Baseline** - Requirements allocated to system elements
3. **Design Baseline** - Detailed design documentation and models
4. **Product Baseline** - Approved production configuration
5. **Operational Baseline** - As-maintained aircraft configuration

**Baseline Requirements:**
- Each baseline shall be formally reviewed and approved
- Baseline documents shall be version-controlled and archived
- Changes to baselines shall require CCB approval
- Impact analysis shall be performed for all proposed changes
- Traceability shall be maintained between baseline levels
- Baseline deviations shall be documented and justified
- Configuration audits shall verify baseline compliance

### 4.3 Methodology
**Baseline Establishment Process:**
1. **Preparation**
   - Compile baseline documentation package
   - Verify completeness and quality
   - Prepare baseline description document

2. **Review and Approval**
   - Technical review by engineering teams
   - CCB evaluation and discussion
   - Formal approval and signature
   - Baseline release and communication

3. **Configuration Control**
   - Monitor and control changes
   - Process change requests through CCB
   - Update baseline documentation
   - Maintain configuration status accounting

**Configuration Control Board (CCB):**
- **Membership:** Chief Engineer (Chair), Technical Leads, Safety Rep, Certification Rep, Quality Rep
- **Frequency:** Weekly during active development, monthly during maintenance
- **Authority:** Approve/reject changes affecting baselines
- **Documentation:** Meeting minutes, decision records, action items

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Configuration Management Plan | Markdown/PDF | Configuration Manager | Project start |
| Baseline Description Documents | Markdown | Systems Engineering | Per baseline |
| Change Request Forms | Markdown Template | Configuration Manager | Initial release |
| CCB Meeting Minutes | Markdown | CCB Secretary | Weekly |
| Configuration Status Report | CSV/Markdown | Configuration Manager | Monthly |
| Configuration Audit Reports | Markdown/PDF | Quality Assurance | Quarterly |

## 6. Verification & Validation
**Acceptance Criteria:**
- Baseline documentation complete and approved
- All baseline items under version control
- CCB operational with defined procedures
- Change process functioning effectively
- Traceability matrix maintained and current
- Configuration audits pass with no major findings
- Certification authority acceptance of CM process

**Audit Types:**
- Functional Configuration Audit (FCA)
- Physical Configuration Audit (PCA)
- Configuration Management Audit (CMA)

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 05](https://en.wikipedia.org/wiki/ATA_100) - Time Limits/Maintenance Checks
  - [ATA 24](https://en.wikipedia.org/wiki/ATA_100) - Electrical Power
  - [ATA 28](https://en.wikipedia.org/wiki/ATA_100) - Fuel System
  - [ATA 95](https://en.wikipedia.org/wiki/ATA_100) - Digital Product Passport
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-01-02A CAD Models Management](./03-00-06-01-02A_CAD_Models_Management.md)
  - [03-00-06-02-01A Requirements Management](../03-00-06-02_Systems_Engineering/03-00-06-02-01A_Requirements_Management.md)
  - [03-00-06-02-04A Traceability Matrix](../03-00-06-02_Systems_Engineering/03-00-06-02-04A_Traceability_Matrix.md)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AI (GitHub Copilot) | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
