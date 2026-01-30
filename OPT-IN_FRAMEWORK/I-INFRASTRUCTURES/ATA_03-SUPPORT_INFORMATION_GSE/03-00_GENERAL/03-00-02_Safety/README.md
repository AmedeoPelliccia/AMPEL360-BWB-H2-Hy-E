# 03-00-02_Safety — Ground Support Equipment (GSE) Safety Framework

## 1. Purpose

This folder defines the **safety framework, operational rules, and risk management methods** for **Ground Support Equipment (GSE)** under [ATA 03 – Support Information GSE](https://www.ata.org/resources/specifications/ispec2200).

It establishes:

- Overall safety management framework for GSE operations
- Hazard identification and risk assessment methodologies
- Operational safety rules and procedures for GSE
- Hydrogen-specific safety considerations for GSE handling H₂ refuelling and support
- Training, competency, and audit requirements
- Incident reporting and lessons-learned processes
- Safety interfaces with flight operations, maintenance, and airport authorities

---

## 2. Scope

This folder is part of the **03-00_GENERAL** layer, which provides governance and lifecycle management for [ATA Chapter 03](https://www.ata.org/resources/specifications/ispec2200).

The 03-00-02_Safety layer covers:

- **Safety Management System (SMS)** for GSE operations, including policy, roles, responsibilities, and KPIs
- **Hazard Identification and Risk Assessment** (HAZID, bow-tie analysis, FMEA, risk matrices)
- **Operational Safety Rules** for GSE (speed limits, exclusion zones, PPE, traffic management, marshalling)
- **Hydrogen-Specific Safety** considerations (H₂ refuelling bowsers, leak detection, ignition source control, zoning, monitoring)
- **Training and Competency** requirements for GSE operators, supervisors, and maintenance personnel
- **Incident Reporting** workflows, classification, investigation, and lessons-learned feedback loops
- **Safety Interfaces** with flight operations ([ATA 02-20 ground operations](../../ATA_02-OPERATIONS_INFORMATION/02-20_Ground_Operations/)), maintenance, and airport authorities
- **Safety Audits and Inspections**, including periodic audits, checklists, and compliance follow-up

It does **not** cover aircraft-specific safety analyses (handled by T-TECHNOLOGY axis) but focuses on **ground infrastructure and GSE operational safety**.

---

## 3. Folder Structure

```text
03-00-02_Safety/
├── README.md (this file)
├── 03-00-02-001_Safety_Management_Framework.md
├── 03-00-02-002_Hazard_Identification_and_Risk_Assessment.md
├── 03-00-02-003_Operational_Safety_Rules_GSE.md
├── 03-00-02-004_H2_Specific_Safety_Considerations.md
├── 03-00-02-005_Safety_Training_and_Competency.md
├── 03-00-02-006_Safety_Incident_Reporting_and_Lessons_Learned.md
├── 03-00-02-007_Safety_Interfaces_with_Ops_and_Maintenance.md
├── 03-00-02-008_Safety_Audits_and_Inspections.md
└── ASSETS/
    ├── README.md
    ├── 03-00-02-A-001_Safety_Architecture_GSE.drawio
    ├── 03-00-02-A-002_Safety_Architecture_GSE.svg
    ├── 03-00-02-A-003_BowTie_Analysis_H2_Refuelling.svg
    ├── 03-00-02-A-004_FMEA_Template.xlsx
    ├── 03-00-02-A-005_Risk_Register_Template.xlsx
    └── 03-00-02-A-006_Safety_Checklist_GSE_Operations.pdf
```

### Document Roles

* **[03-00-02-001_Safety_Management_Framework.md](./03-00-02-001_Safety_Management_Framework.md)**
  Describes the overall safety management framework for GSE & ground support (policy, roles, processes, KPIs).

* **[03-00-02-002_Hazard_Identification_and_Risk_Assessment.md](./03-00-02-002_Hazard_Identification_and_Risk_Assessment.md)**
  Defines methods for hazard identification (HAZID) and risk assessment (bow-tie, FMEA, risk matrix) for GSE operations.

* **[03-00-02-003_Operational_Safety_Rules_GSE.md](./03-00-02-003_Operational_Safety_Rules_GSE.md)**
  Captures core operational safety rules for GSE (speed limits, exclusion zones, PPE, traffic rules, marshalling).

* **[03-00-02-004_H2_Specific_Safety_Considerations.md](./03-00-02-004_H2_Specific_Safety_Considerations.md)**
  Details hydrogen-specific safety constraints for GSE (refuelling bowsers, leaks, ignition sources, zoning, monitoring).

* **[03-00-02-005_Safety_Training_and_Competency.md](./03-00-02-005_Safety_Training_and_Competency.md)**
  Defines training, competency and recurrent checks for GSE operators, supervisors and maintenance staff.

* **[03-00-02-006_Safety_Incident_Reporting_and_Lessons_Learned.md](./03-00-02-006_Safety_Incident_Reporting_and_Lessons_Learned.md)**
  Describes incident/near-miss reporting workflow, classification, investigation and lessons-learned loop.

* **[03-00-02-007_Safety_Interfaces_with_Ops_and_Maintenance.md](./03-00-02-007_Safety_Interfaces_with_Ops_and_Maintenance.md)**
  Explains interfaces between GSE safety, flight operations, turnaround, maintenance and airport authorities.

* **[03-00-02-008_Safety_Audits_and_Inspections.md](./03-00-02-008_Safety_Audits_and_Inspections.md)**
  Defines periodic safety audits, inspections, checklists, and compliance follow-up for GSE.

---

## 4. Relationship with Other Sections

* **[03-00-01_Overview](../03-00-01_Overview/)**
  Provides the general ATA 03 GSE concept; 03-00-02_Safety specialises it for **safety management and operational safety**.

* **[03-00-03_Requirements](../03-00-03_Requirements/)**
  Safety requirements defined here feed into the overall GSE requirements baseline.

* **[ATA 02-20 Ground Operations](../../ATA_02-OPERATIONS_INFORMATION/02-20_Ground_Operations/)**
  GSE safety interfaces with flight operations ground handling procedures.

* **Other Safety / Certification Artefacts**
  This section is designed to align with:
  - [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Equipment, Systems, and Installations)
  - [Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012) (Design Organisation Approval)
  - Ground handling safety standards ([IATA AHM](https://www.iata.org/en/publications/manuals/airport-handling-manual/), [ICAO Annex 14](https://www.icao.int/safety/airnavigation/Annexes/Pages/annex-14.aspx))
  - Hydrogen safety standards ([ISO 19880-8](https://www.iso.org/standard/71940.html), [SAE J2601](https://www.sae.org/standards/content/j2601/))

---

## 5. Usage

* Use this folder as the **reference** when:
  - Defining GSE safety policies and operational rules
  - Conducting hazard analyses and risk assessments for GSE operations
  - Developing training programs for GSE operators
  - Investigating safety incidents and implementing lessons learned
  - Preparing for safety audits and regulatory inspections

* Any change to safety objectives, requirements, or processes that affects GSE operations must be reflected in the relevant `03-00-02-xxx_*.md` files and captured in ATA 03 change control.

---

## 6. Status

- **Phase**: Safety
- **Lifecycle Position**: 02 of 14
- **Status**: Active
- **Last Updated**: 2025-11-21

---

## 7. Related Folders

Part of the canonical 14-folder lifecycle:
1. [Overview](../03-00-01_Overview/) → 2. **Safety** → 3. [Requirements](../03-00-03_Requirements/) → 4. [Design](../03-00-04_Design/) → 5. [Interfaces](../03-00-05_Interfaces/) → 6. [Engineering](../03-00-06_Engineering/) → 7. [V&V](../03-00-07_V_AND_V/) → 8. [Prototyping](../03-00-08_Prototyping/) → 9. [Production Planning](../03-00-09_Production_Planning/) → 10. [Certification](../03-00-10_Certification/) → 11. [EIS/Versions/Tags](../03-00-11_EIS_Versions_Tags/) → 12. [Services](../03-00-12_Services/) → 13. [Subsystems/Components](../03-00-13_Subsystems_Components/) → 14. [Ops/Std/Sustain](../03-00-14_Ops_Std_Sustain/)

---

## 8. Document Control

- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template)
- **Owner**: AMPEL360 Documentation WG
- **Status**: `WORKING` / `FOR_REVIEW` / `APPROVED`
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
