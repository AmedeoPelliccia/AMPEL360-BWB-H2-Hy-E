---
Title: "Functional Requirements — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-03-002A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Functional requirements for ground support equipment and support information systems for AMPEL360 BWB H₂ Hy-E aircraft."
Keywords: ["ATA 03","Functional Requirements","GSE","Ground Support","Operations"]
Compliance:
  - "ATA iSpec 2200"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Overview: "./03-00-03-001A_Requirements_Overview.md"
  InformationModel: "./03-00-03-003A_Information_Model_Requirements.md"
  Traceability: "./03-00-03-004A_Traceability_and_Compliance_Requirements.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial functional requirements" }
---

# Functional Requirements — ATA 03 Support Information GSE

## 1. Purpose

This document defines the **functional requirements** for Ground Support Equipment (GSE) and Support Information systems necessary for the operation, maintenance, and servicing of the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope

### 2.1 Functional Categories

This document covers functional requirements across the following categories:

1. **Hydrogen Refuelling GSE** (H2-GSE)
2. **Electrical Ground Support** (ELEC-GSE)
3. **Maintenance Access Equipment** (MAINT-GSE)
4. **Ground Handling Equipment** (GH-GSE)
5. **Support Information Systems** (INFO-SYS)

### 2.2 Relationship to Other Requirements

- Performance requirements → See [03-00-03-001A_Requirements_Overview.md](./03-00-03-001A_Requirements_Overview.md)
- Information model → See [03-00-03-003A_Information_Model_Requirements.md](./03-00-03-003A_Information_Model_Requirements.md)
- Safety requirements → See [03-00-02_Safety](../03-00-02_Safety/)

## 3. Hydrogen Refuelling GSE (H2-GSE)

### 3.1 H2 Refuelling Interface

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-001 | The H2 refuelling GSE shall connect to the aircraft's LH₂ receptacle within 5 minutes of positioning. | Turnaround time efficiency | Test | MUST |
| REQ-03-00-03-FR-002 | The H2 refuelling GSE shall provide cryogenic liquid hydrogen at −253°C. | Aircraft fuel system requirements | Test | MUST |
| REQ-03-00-03-FR-003 | The H2 refuelling GSE shall deliver hydrogen at pressures between 3 and 8 bar. | Tank filling pressure envelope | Test | MUST |
| REQ-03-00-03-FR-004 | The H2 refuelling GSE shall automatically terminate fuelling upon detection of tank full condition. | Safety and operational requirement | Test | MUST |
| REQ-03-00-03-FR-005 | The H2 refuelling GSE shall provide continuous boil-off gas recovery during refuelling operations. | Environmental and safety requirement | Test | MUST |

### 3.2 H2 Safety Systems

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-006 | The H2 refuelling GSE shall incorporate automatic leak detection with ≤1 second response time. | Safety-critical function | Test | MUST |
| REQ-03-00-03-FR-007 | The H2 refuelling GSE shall provide emergency shut-off capability accessible from multiple locations. | Emergency response | Test, Inspection | MUST |
| REQ-03-00-03-FR-008 | The H2 refuelling GSE shall maintain safety exclusion zone monitoring during operations. | Personnel safety | Test | MUST |
| REQ-03-00-03-FR-009 | The H2 refuelling GSE shall provide continuous hydrogen concentration monitoring in work area. | Hazard detection | Test | MUST |

### 3.3 H2 Monitoring and Control

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-010 | The H2 refuelling GSE shall display real-time fuel quantity being transferred. | Operational awareness | Test | MUST |
| REQ-03-00-03-FR-011 | The H2 refuelling GSE shall log all refuelling events with timestamp and quantity data. | Audit and maintenance tracking | Test, Review | MUST |
| REQ-03-00-03-FR-012 | The H2 refuelling GSE shall communicate refuelling status to aircraft DPP system. | Digital integration | Test | SHOULD |

## 4. Electrical Ground Support (ELEC-GSE)

### 4.1 Ground Power Unit

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-013 | The electrical GSE shall provide 115V AC 400Hz power to aircraft. | Standard aircraft electrical interface | Test | MUST |
| REQ-03-00-03-FR-014 | The electrical GSE shall provide 28V DC power to aircraft systems. | Aircraft battery charging and system power | Test | MUST |
| REQ-03-00-03-FR-015 | The electrical GSE shall deliver minimum 90 kVA power capacity. | Aircraft ground power requirements | Test | MUST |
| REQ-03-00-03-FR-016 | The electrical GSE shall connect to aircraft via standard NATO-compatible connector. | Interface standardization | Test, Inspection | MUST |

### 4.2 Battery Charging Systems

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-017 | The battery charging GSE shall support charging of 800V DC battery system. | Aircraft battery architecture | Test | MUST |
| REQ-03-00-03-FR-018 | The battery charging GSE shall provide charging power up to 500 kW. | Rapid turnaround charging | Test | MUST |
| REQ-03-00-03-FR-019 | The battery charging GSE shall communicate with aircraft Battery Management System (BMS). | Safe and efficient charging | Test | MUST |
| REQ-03-00-03-FR-020 | The battery charging GSE shall automatically adjust charging profile based on BMS input. | Battery health optimization | Test | MUST |

## 5. Maintenance Access Equipment (MAINT-GSE)

### 5.1 Access Platforms and Stands

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-021 | The maintenance platform GSE shall provide access to all aircraft doors and access panels. | Maintenance accessibility | Test, Inspection | MUST |
| REQ-03-00-03-FR-022 | The maintenance platform GSE shall accommodate BWB non-standard fuselage geometry. | Aircraft configuration requirement | Test, Analysis | MUST |
| REQ-03-00-03-FR-023 | The maintenance platform GSE shall support working loads up to 500 kg per platform. | Maintenance operations requirement | Test | MUST |
| REQ-03-00-03-FR-024 | The maintenance platform GSE shall provide fall protection systems compliant with local regulations. | Personnel safety | Test, Inspection | MUST |

### 5.2 Specialized Maintenance Equipment

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-025 | Specialized GSE shall be provided for LH₂ tank inspection and servicing. | Cryogenic system maintenance | Review, Inspection | MUST |
| REQ-03-00-03-FR-026 | Specialized GSE shall be provided for fuel cell stack removal and installation. | Propulsion system maintenance | Review, Inspection | MUST |
| REQ-03-00-03-FR-027 | Tooling shall be provided for composite structure repair compatible with CFRP materials. | Structural repair capability | Test, Inspection | MUST |

## 6. Ground Handling Equipment (GH-GSE)

### 6.1 Towing and Pushback

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-028 | The towing equipment shall connect to aircraft nose landing gear tow fitting. | Ground movement requirement | Test, Inspection | MUST |
| REQ-03-00-03-FR-029 | The towing equipment shall provide minimum 35,000 kg drawbar pull. | Aircraft MTOW towing capability | Test | MUST |
| REQ-03-00-03-FR-030 | The pushback tug shall provide clearance for BWB wing-body blend geometry. | Aircraft configuration requirement | Analysis, Test | MUST |

### 6.2 Passenger Boarding

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-031 | Passenger boarding bridges shall accommodate aircraft door sill heights ranging from 2.5m to 4.5m. | BWB door location variability | Test, Inspection | MUST |
| REQ-03-00-03-FR-032 | Passenger boarding equipment shall provide accessibility for passengers with reduced mobility. | Regulatory compliance (EU 1107/2006) | Test, Inspection | MUST |

## 7. Support Information Systems (INFO-SYS)

### 7.1 Technical Publications

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-033 | Technical publications shall be provided in [S1000D](https://www.s1000d.org/) format. | Industry standard compliance | Review | MUST |
| REQ-03-00-03-FR-034 | Interactive Electronic Technical Publications (IETP) shall be accessible via mobile devices. | Operational efficiency | Test | SHOULD |
| REQ-03-00-03-FR-035 | Technical publications shall be available in English, with translations as required by operators. | Operator requirements | Review | MUST |

### 7.2 Maintenance Management System

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-036 | The maintenance management system shall integrate with aircraft [Digital Product Passport (DPP)](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/). | Digital lifecycle management | Test | MUST |
| REQ-03-00-03-FR-037 | The maintenance management system shall provide predictive maintenance alerts based on aircraft health data. | Proactive maintenance | Test | SHOULD |
| REQ-03-00-03-FR-038 | The maintenance management system shall track GSE utilization and maintenance status. | GSE fleet management | Test | SHOULD |

### 7.3 Training Systems

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-039 | Training materials shall be provided for all GSE operations and maintenance procedures. | Personnel qualification | Review | MUST |
| REQ-03-00-03-FR-040 | Training programs shall include hydrogen safety training compliant with [ISO 19880-8](https://www.iso.org/standard/71940.html). | Safety-critical training | Review | MUST |
| REQ-03-00-03-FR-041 | Computer-based training (CBT) modules shall be provided for ground crew certification. | Training efficiency | Test, Review | SHOULD |

## 8. Digital Integration Requirements

### 8.1 Data Exchange

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-042 | GSE shall support data exchange with aircraft via secure wireless protocol. | Operational data integration | Test | SHOULD |
| REQ-03-00-03-FR-043 | GSE operational data shall be logged and transmitted to operator's ground operations system. | Fleet management and analytics | Test | SHOULD |

### 8.2 Cybersecurity

| Req ID | Requirement | Rationale | Verification | Priority |
|--------|-------------|-----------|--------------|----------|
| REQ-03-00-03-FR-044 | All GSE-to-aircraft data interfaces shall implement encryption and authentication per [DO-326A](https://www.rtca.org/content/standards-documents). | Cybersecurity requirement | Test, Review | MUST |
| REQ-03-00-03-FR-045 | GSE software shall be protected against unauthorized modification. | System integrity | Test, Inspection | MUST |

## 9. Functional Allocation Matrix

| Function | H2-GSE | ELEC-GSE | MAINT-GSE | GH-GSE | INFO-SYS |
|----------|--------|----------|-----------|--------|----------|
| Hydrogen refuelling | ● | — | — | — | ○ |
| Ground power supply | — | ● | — | — | ○ |
| Battery charging | — | ● | — | — | ○ |
| Maintenance access | — | — | ● | — | ○ |
| Specialized maintenance | — | — | ● | — | ○ |
| Towing and pushback | — | — | — | ● | ○ |
| Passenger boarding | — | — | — | ● | ○ |
| Technical publications | — | — | — | — | ● |
| Maintenance management | — | — | — | — | ● |
| Training systems | — | — | — | — | ● |
| Digital integration | ○ | ○ | ○ | ○ | ● |

Legend: ● Primary, ○ Supporting, — Not applicable

## 10. Traceability

### 10.1 Upstream (Source Requirements)

| Source | Document/Regulation |
|--------|---------------------|
| Aircraft-level requirements | Top-level Aircraft Requirements Specification (TLARS) |
| Safety requirements | [03-00-02_Safety](../03-00-02_Safety/) |
| Regulatory requirements | [EASA CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27), [FAA Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) |
| Operator requirements | Operator stakeholder requirements documents |

### 10.2 Downstream (Allocated To)

| Target | Document |
|--------|----------|
| Design specifications | [03-00-04_Design](../03-00-04_Design/) |
| Interface definitions | [03-00-05_Interfaces](../03-00-05_Interfaces/) |
| Verification plans | [03-00-07_V_AND_V](../03-00-07_V_AND_V/) |
| Certification evidence | [03-00-10_Certification](../03-00-10_Certification/) |

## 11. Compliance Matrix

| Requirement Category | Count | Verification Method | Status |
|---------------------|-------|---------------------|--------|
| H2 Refuelling | 12 | Test, Inspection | Draft |
| Electrical Support | 8 | Test | Draft |
| Maintenance Access | 7 | Test, Inspection, Analysis | Draft |
| Ground Handling | 5 | Test, Inspection, Analysis | Draft |
| Information Systems | 11 | Test, Review | Draft |
| Digital Integration | 4 | Test, Review | Draft |
| **Total** | **47** | — | **Draft** |

## 12. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-12-07 | AMPEL360 Documentation Team | Initial functional requirements |

---

## Document Control

- **Document ID**: 03-00-03-002A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Ground Operations & Support Equipment WG

---
