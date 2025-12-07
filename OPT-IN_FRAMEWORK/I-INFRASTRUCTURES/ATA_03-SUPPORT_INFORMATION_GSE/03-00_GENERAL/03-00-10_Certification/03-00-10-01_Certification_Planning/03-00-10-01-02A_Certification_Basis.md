---
Title: "Certification Basis — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-10-01-02A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Certification Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Definition of certification basis for ATA 03 Ground Support Equipment and support information systems."
Keywords: ["ATA 03","GSE","Certification Basis","Regulatory Requirements"]
Compliance:
  - "EASA CS-25"
  - "FAA Part 25"
  - "EASA Part 21"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentCertification: "../"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Certification Team", change: "Initial certification basis" }
---

# 03-00-10-01-02A - Certification Basis

## 1. Purpose

This document establishes the **certification basis** for ATA Chapter 03 — Support Information and Ground Support Equipment (GSE). It defines the specific regulations, standards, and special conditions that apply to certification of GSE and support information systems for the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope

### 2.1 Coverage

The certification basis defines regulatory requirements for:

1. **Ground Support Equipment**
   - Hydrogen refuelling systems and equipment
   - Electrical ground power systems
   - Maintenance access and servicing equipment
   - Ground handling and towing equipment

2. **Support Information**
   - Technical documentation and manuals
   - Maintenance procedures and instructions
   - Training materials and programs
   - Digital integration systems

3. **Interface Requirements**
   - Aircraft-to-GSE physical interfaces
   - Data and communication interfaces
   - Safety and emergency systems

## 3. Applicable Documents

### 3.1 EASA Regulations

- **[EASA CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)** — Certification Specifications for Large Aeroplanes
  - CS-25.1581 — General (Manuals, markings, and placards)
  - CS-25.1583 — Operating limitations
  - CS-25.981 — Fuel tank explosion prevention
  - CS-25.1309 — Equipment, systems, and installations

- **[EASA Part 21](https://www.easa.europa.eu/document-library/regulations/easa-part-21)** — Certification Procedures
  - Subpart B — Type-certificates
  - Subpart D — Design organisation approval

### 3.2 FAA Regulations

- **[FAA Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25)** — Transport Category Airplanes
  - §25.1581 — General
  - §25.1583 — Operating limitations
  - §25.981 — Fuel tank ignition prevention
  - §25.1309 — Equipment, systems, and installations

### 3.3 Industry Standards

- **[ISO 19880-8:2019](https://www.iso.org/standard/71940.html)** — Hydrogen fuelling stations
- **[SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/)** — Development of Civil Aircraft and Systems
- **[SAE ARP4761](https://www.sae.org/standards/content/arp4761/)** — Safety Assessment Process
- **[ATA iSpec 2200](https://www.ata.org/resources/specifications)** — Information Standards for Aviation Maintenance

### 3.4 Related AMPEL360 Documents

- [03-00-10-01-01A_Certification_Strategy](./03-00-10-01-01A_Certification_Strategy.md)
- [03-00-10-04_Airworthiness_Requirements](../03-00-10-04_Airworthiness_Requirements/)
- [03-00-10-05_Safety_Assessment](../03-00-10-05_Safety_Assessment/)

## 4. Description

### 4.1 Overview

The certification basis provides the regulatory foundation for demonstrating compliance with applicable airworthiness requirements. For the AMPEL360 aircraft, the certification basis includes both standard transport category requirements and special conditions specific to hydrogen propulsion and BWB configuration.

### 4.2 Regulatory Requirements

#### 4.2.1 CS-25 / Part 25 Requirements

| Section | Title | Applicability to GSE | Compliance Method |
|---------|-------|----------------------|-------------------|
| CS-25.1581 / §25.1581 | General | Ground service procedures and interface documentation | Documentation + Review |
| CS-25.1583 / §25.1583 | Operating limitations | GSE operating limitations and procedures | Documentation + Testing |
| CS-25.981 / §25.981 | Fuel tank explosion prevention | Hydrogen refuelling safety systems | Safety Assessment + Testing |
| CS-25.1309 / §25.1309 | Equipment, systems, installations | GSE equipment qualification | Analysis + Testing |

#### 4.2.2 Special Conditions for Hydrogen Systems

Due to the novel use of liquid hydrogen (LH₂) as aircraft fuel, the following special conditions are anticipated:

1. **SC-H2-001: Cryogenic Hydrogen Ground Handling**
   - Safety requirements for LH₂ transfer operations
   - Personnel protection and training requirements
   - Emergency response procedures

2. **SC-H2-002: Hydrogen Leak Detection and Mitigation**
   - Ground-based leak detection systems
   - Ventilation and dispersion requirements
   - Automatic shutdown systems

3. **SC-H2-003: Refuelling Equipment Safety**
   - Fail-safe refuelling connections
   - Pressure relief and venting systems
   - Static electricity dissipation

4. **SC-H2-004: Ground Service Interface Standards**
   - Physical interface specifications for H₂ systems
   - Data interface requirements
   - Compatibility with airport infrastructure

### 4.3 Compliance Approach

#### 4.3.1 Means of Compliance

Each requirement in the certification basis will be addressed through one or more of the following means:

| Method | Description | Application |
|--------|-------------|-------------|
| **Analysis** | Engineering analysis and calculations | Safety analysis, interface compatibility |
| **Testing** | Physical testing of equipment and systems | Functional testing, environmental testing |
| **Inspection** | Design review and manufacturing inspection | Quality assurance, conformity verification |
| **Demonstration** | Operational demonstrations | Procedures validation, training effectiveness |

#### 4.3.2 Equivalent Level of Safety (ELOS)

Where compliance with specific regulations cannot be achieved through standard means, Equivalent Level of Safety (ELOS) findings will be pursued. Anticipated ELOS areas include:

- Novel hydrogen safety systems
- BWB-specific ground servicing procedures
- Digital integration and automation systems

## 5. Compliance Matrix

| Requirement ID | Regulation | Description | Means of Compliance | Status |
|----------------|------------|-------------|---------------------|--------|
| CB-001 | CS-25.1581 | Ground service interface documentation | Documentation + Review | Planned |
| CB-002 | CS-25.1583 | GSE operating limitations | Documentation + Testing | Planned |
| CB-003 | CS-25.981 | Fuel system safety (hydrogen) | Safety Assessment + Testing | Planned |
| CB-004 | CS-25.1309 | Equipment qualification | Analysis + Testing | Planned |
| CB-005 | SC-H2-001 | Cryogenic hydrogen handling | Special Condition + Testing | Planned |
| CB-006 | SC-H2-002 | Hydrogen leak detection | Special Condition + Testing | Planned |
| CB-007 | SC-H2-003 | Refuelling equipment safety | Special Condition + Testing | Planned |
| CB-008 | SC-H2-004 | Ground service interfaces | Special Condition + Analysis | Planned |
| CB-009 | ISO 19880-8 | Hydrogen fuel quality | Testing + Analysis | Planned |
| CB-010 | ATA iSpec 2200 | Technical documentation standards | Documentation Review | Planned |

## 6. Evidence Requirements

### 6.1 Documentation

- Type Certificate Data Sheet (TCDS)
- Aircraft Flight Manual (AFM) — Ground servicing sections
- Maintenance Manual — GSE procedures
- Service Bulletins and Instructions
- Training program documentation

### 6.2 Safety Assessment

- Functional Hazard Assessment (FHA)
- Preliminary System Safety Assessment (PSSA)
- System Safety Assessment (SSA)
- Common Cause Analysis (CCA)

### 6.3 Test Evidence

- GSE functional test reports
- Interface compatibility test reports
- Safety system validation reports
- Environmental test reports

## 7. Cross-References

- Related ATA Chapters: ATA 03 (Support Information/GSE), ATA 28 (Fuel System), ATA 85 (Infrastructure)
- Parent Document: 03-00-10_Certification
- Related V&V Docs: 03-00-07_V_AND_V
- Related Engineering Docs: 03-00-04_Design

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Certification Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-10-01-02A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Certification & Ground Support WG

---
