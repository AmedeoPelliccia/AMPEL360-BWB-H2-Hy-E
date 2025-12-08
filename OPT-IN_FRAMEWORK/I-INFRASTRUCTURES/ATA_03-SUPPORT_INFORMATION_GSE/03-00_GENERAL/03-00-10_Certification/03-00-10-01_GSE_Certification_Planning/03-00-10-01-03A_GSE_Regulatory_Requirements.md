---
Title: "GSE Regulatory Requirements — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-10-01-03A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Comprehensive compilation of regulatory requirements applicable to GSE certification for AMPEL360 aircraft."
Keywords: ["ATA 03","GSE","Regulatory","Requirements","Compliance"]
Compliance:
  - "EASA Regulation (EU) 2018/1139"
  - "FAA 14 CFR Part 139"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentPlanning: "./"
  Siblings:
    - "03-00-10-01-01A_GSE_Certification_Strategy.md"
    - "03-00-10-01-02A_GSE_Certification_Roadmap.md"
    - "03-00-10-01-04A_GSE_Certification_Schedule.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial regulatory requirements compilation" }
---

# 03-00-10-01-03A - GSE Regulatory Requirements

## 1. Purpose

This document compiles and interprets the **regulatory requirements** applicable to Ground Support Equipment (GSE) certification for the AMPEL360 BWB H₂ Hy-E aircraft. It serves as the regulatory foundation for GSE design, testing, and approval activities.

## 2. Scope

This document covers regulatory requirements from:

- European Union Aviation Safety Agency (EASA)
- Federal Aviation Administration (FAA)
- National Aviation Authorities (NAAs)
- International standards organizations
- Airport authority requirements

## 3. Applicable Documents

### 3.1 Primary Regulations

| Authority | Regulation | Title | Link |
|-----------|------------|-------|------|
| **EASA** | Regulation (EU) 2018/1139 | Common rules in the field of civil aviation | [EASA Reg](https://www.easa.europa.eu/document-library/regulations/regulation-eu-20181139) |
| **EASA** | CS-25 Amendment 27 | Certification Specifications for Large Aeroplanes | [CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) |
| **FAA** | 14 CFR Part 139 | Certification of Airports | [Part 139](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-139) |
| **FAA** | 14 CFR Part 25 | Airworthiness Standards: Transport Category Airplanes | [Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) |

### 3.2 Standards and Guidelines

| Organization | Standard | Title | Link |
|--------------|----------|-------|------|
| **SAE** | AS6968 | Hydrogen Aircraft Refueling | [SAE AS6968](https://www.sae.org/standards/content/as6968/) |
| **ISO** | ISO 19880-8 | Gaseous hydrogen fueling stations | [ISO 19880-8](https://www.iso.org/standard/71940.html) |
| **IEC** | IEC 60079 | Explosive atmospheres (ATEX) | [IEC 60079](https://webstore.iec.ch/publication/632) |
| **CEN** | EN 1915 | Ground support equipment — General requirements | CEN Standards |
| **ISO** | ISO 9001 | Quality management systems | [ISO 9001](https://www.iso.org/iso-9001-quality-management.html) |

## 4. Certification Requirements

### 4.1 EASA Requirements

#### 4.1.1 Aircraft Interface Requirements

**CS-25.1581 — General**

GSE must not compromise aircraft systems or structures during normal or abnormal operations.

**Interpretation for GSE**:
- GSE design must prevent damage to aircraft systems
- Interface forces and loads must be within aircraft design limits
- Electrical GSE must not cause electromagnetic interference
- Fueling GSE must comply with aircraft fuel system protection requirements

**CS-25.1583 — Operating Limitations and Information**

Aircraft manuals must include GSE interface requirements.

**Interpretation for GSE**:
- GSE must provide interface specifications for inclusion in Aircraft Maintenance Manual
- GSE operating procedures must be compatible with aircraft procedures
- GSE limitations must be clearly documented

#### 4.1.2 Regulation (EU) 2018/1139 Applicability

**Article 47 — Ground handling services**

Ground support equipment used in ground handling operations must ensure safe aircraft operations.

**Interpretation for GSE**:
- GSE must undergo safety assessment
- Operators must demonstrate competence
- Maintenance procedures must be established

### 4.2 FAA Requirements

#### 4.2.1 Part 139 — Airport Certification

**§139.319 — Aircraft rescue and firefighting: Operational requirements**

Airports must have adequate firefighting equipment, including for H₂ aircraft.

**Interpretation for H₂ GSE**:
- H₂ GSE must be compatible with airport firefighting equipment
- Emergency response procedures must address H₂ hazards
- Personnel training must include H₂ safety

**§139.321 — Handling and storing of hazardous substances and materials**

Airports must establish procedures for hazardous materials, including cryogenic hydrogen.

**Interpretation for H₂ GSE**:
- H₂ GSE must include leak detection and containment
- Storage and handling procedures must comply with airport hazardous materials protocols
- Spill response procedures must be defined

#### 4.2.2 Part 25 — Airworthiness Standards

**§25.1581 — General**

Instructions for continued airworthiness must include servicing information.

**Interpretation for GSE**:
- GSE manuals must be compatible with aircraft service procedures
- GSE-related aircraft inspection requirements must be defined

**§25.1583 — Operating limitations**

Aircraft limitations related to GSE must be documented.

**Interpretation for GSE**:
- Environmental limits for GSE operation must align with aircraft limits
- GSE operational restrictions must be documented

### 4.3 Hydrogen-Specific Requirements

#### 4.3.1 SAE AS6968 — Hydrogen Aircraft Refueling

**Key Requirements**:

| Section | Requirement | GSE Application |
|---------|-------------|-----------------|
| 4.1 | Safety philosophy | Fail-safe design, leak detection, automatic shutdown |
| 4.2 | Equipment design | Cryogenic compatibility, pressure management, material selection |
| 4.3 | Operating procedures | Pre-fueling checks, fueling sequence, emergency procedures |
| 4.4 | Training | Personnel qualification, emergency response training |
| 4.5 | Maintenance | Inspection intervals, leak testing, component replacement |

#### 4.3.2 ISO 19880-8 — Gaseous Hydrogen Fueling

**Key Requirements**:

- Hydrogen purity standards (SAE J2719)
- Leak detection sensitivity (10 ppm)
- Pressure vessel certification (UN TPED, ASME BPVC)
- Grounding and bonding (static discharge prevention)
- Safety interlocks and emergency stops

#### 4.3.3 IEC 60079 — ATEX Requirements

**Zone Classification**:

| Zone | Definition | GSE Requirements |
|------|------------|------------------|
| Zone 0 | Explosive atmosphere continuously present | Not applicable (enclosed systems) |
| Zone 1 | Explosive atmosphere likely in normal operations | Explosion-proof electrical systems, intrinsically safe circuits |
| Zone 2 | Explosive atmosphere unlikely but possible | Non-sparking equipment, protected enclosures |

**GSE Design**:
- Electrical systems in H₂ zones must be ATEX-certified
- Temperature classification: T1 (450°C max surface temp)
- Equipment group: IIC (hydrogen)

### 4.4 Environmental and Sustainability Requirements

#### 4.4.1 EU Regulations

- **EU Green Deal**: GSE must support zero-emission operations
- **EU Taxonomy Regulation**: GSE lifecycle emissions tracking

#### 4.4.2 Noise Requirements

- **ICAO Annex 16 Vol 1**: Ground noise limits
- Airport-specific noise restrictions

### 4.5 Quality and Production Requirements

#### 4.5.1 ISO 9001 — Quality Management

GSE manufacturers must demonstrate:

- Quality management system certification
- Design control processes
- Supplier quality oversight
- Traceability and configuration management
- Continuous improvement processes

## 5. Certification Evidence

### 5.1 Required Evidence by Regulation

| Regulation | Required Evidence |
|------------|-------------------|
| CS-25.1581/1583 | Interface specifications, compatibility testing, manual excerpts |
| Part 139 | Operational procedures, training materials, emergency response plans |
| SAE AS6968 | Design compliance checklist, test reports, operational procedures |
| ISO 19880-8 | Purity verification, leak test reports, pressure vessel certificates |
| IEC 60079 | ATEX certificates, zone classification drawings, electrical system design |
| ISO 9001 | QMS certificate, design reviews, supplier audits, production control plan |

## 6. Safety Requirements

### 6.1 Safety Assessment Requirements

Per EASA and FAA guidance:

- **Functional Hazard Assessment (FHA)**: Identify potential hazards
- **Preliminary System Safety Assessment (PSSA)**: Assess safety impact
- **System Safety Assessment (SSA)**: Demonstrate acceptable safety
- **Common Cause Analysis (CCA)**: Address common mode failures

### 6.2 Safety Objectives

| Failure Condition | Classification | Probability Target |
|-------------------|----------------|-------------------|
| Catastrophic (aircraft loss) | Not applicable | N/A (GSE design precludes) |
| Hazardous (serious injury) | Major | < 10⁻⁵ per flight hour |
| Major (crew workload) | Major | < 10⁻⁵ per flight hour |
| Minor (inconvenience) | Minor | < 10⁻³ per flight hour |

## 7. Cross-References

### 7.1 Related ATA 03 Documents

- [03-00-10-01-01A_GSE_Certification_Strategy](./03-00-10-01-01A_GSE_Certification_Strategy.md) — Certification strategy
- [03-00-10-03_GSE_Regulatory_Compliance](../03-00-10-03_GSE_Regulatory_Compliance/) — Detailed regulatory compliance
- [03-00-10-04_GSE_Safety_Certification](../03-00-10-04_GSE_Safety_Certification/) — Safety certification
- [03-00-10-06-01A_GSE_Compliance_Matrix](../03-00-10-06_GSE_Compliance_Documentation/03-00-10-06-01A_GSE_Compliance_Matrix.md) — Compliance matrix

### 7.2 Cross-ATA References

- [ATA 28 — Fuel System](../../../ATA_28-FUEL_SYSTEM/) — Aircraft fuel system interfaces
- [ATA 02 — Operations Information](../../ATA_02-OPERATIONS_INFORMATION/) — Operational procedures

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-10-01-03A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Certification Team

---
