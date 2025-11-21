# 85-00-10-002 Regulatory Framework and Applicability

## Document Information

- **Document ID**: 85-00-10-002
- **Title**: Regulatory Framework and Applicability for Infrastructure Interfaces
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Certification
- **ATA Chapter**: 85 - Infrastructure Interface Standards

## Purpose

This document identifies and assesses the applicability of regulations, certification specifications, and industry standards relevant to **ATA 85 – Infrastructure Interface Standards**. It provides the regulatory foundation for the certification strategy and compliance demonstration approach.

---

## Scope

This document covers regulatory frameworks applicable to:

1. **Aviation domain**: Aircraft certification requirements for ground interface systems
2. **Hydrogen infrastructure**: H₂ production, storage, and fuelling regulations
3. **Electrical infrastructure**: CO₂ battery charging and power systems
4. **Building and fire safety**: Airport terminal, ramp, and evacuation infrastructure
5. **Environmental**: Emissions, noise, and sustainability requirements

---

## Aviation Regulations

### EASA Certification Specifications

#### CS-25: Large Aeroplanes

Primary certification basis for the AMPEL360 BWB aircraft:

**[CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) – Equipment, Systems and Installations**
- **Applicability**: HIGH
- **Interface Impact**: All infrastructure interface systems (H₂, electrical, data)
- **Requirements**:
  - § 1309(b): Systems and associated components must be designed to ensure that catastrophic failure conditions are extremely improbable
  - § 1309(c): Warning information must be provided to alert crew to unsafe system operating conditions
  - § 1309(d): Compliance shown by analysis, tests, or combination
- **ATA 85 Application**: 
  - H₂ refuelling interface safety systems
  - CO₂ battery charging monitoring and protection
  - GSE power and data interface fault detection

**[CS-25.807](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) – Emergency Exits**
- **Applicability**: HIGH
- **Interface Impact**: Passenger boarding and evacuation interfaces
- **Requirements**:
  - Emergency exit types, number, and distribution
  - Opening mechanisms and markings
  - Exit access and evacuation routes
- **ATA 85 Application**:
  - Novel BWB boarding bridge interfaces
  - Multiple-level evacuation slide deployment
  - Compatibility with airport terminal infrastructure

**[CS-25.853](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) – Compartment Interiors**
- **Applicability**: MEDIUM
- **Interface Impact**: Fire safety at boarding/evacuation interfaces
- **Requirements**: Material flammability, smoke, and toxicity
- **ATA 85 Application**: Boarding interface materials and finishes

**[CS-25.981](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) – Fuel Tank Ignition Prevention**
- **Applicability**: HIGH (by analogy)
- **Interface Impact**: H₂ storage and fuelling systems
- **Requirements**: Prevention of ignition sources in fuel tanks
- **ATA 85 Application**: 
  - H₂ tank venting and pressure relief interfaces
  - Electrostatic discharge prevention at refuelling points
  - Bonding and grounding of H₂ systems

#### CS-E: Engines

**[CS-E 20](https://www.easa.europa.eu/document-library/certification-specifications/cs-e-amendment-6) – Design and Construction (Hydrogen Propulsion)**
- **Applicability**: HIGH
- **Interface Impact**: H₂ fuel system interfaces to propulsion
- **Requirements**: Applicable by analogy for hydrogen propulsion systems
- **ATA 85 Application**: H₂ supply interface to propulsion system

### EASA Part 21: Certification Procedures

**[Part 21](https://www.easa.europa.eu/document-library/regulations/commission-regulation-eu-no-7482012) – Certification of Aircraft and Related Products**
- **Applicability**: HIGH
- **Interface Impact**: Overall certification process and evidence requirements
- **Key Sections**:
  - Subpart B: Type-Certificates and Restricted Type-Certificates
  - Subpart D: Design Organisation Approval (DOA)
  - Subpart F: Production Organisation Approval (POA)
- **ATA 85 Application**: 
  - Interface Control Documents as part of Type Design
  - Production conformity for certified interface components

### FAA Regulations

#### 14 CFR Part 25: Airworthiness Standards

**[§ 25.1309](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-F/section-25.1309) – Equipment, Systems, and Installations**
- **Applicability**: HIGH
- **Harmonization**: Harmonized with CS-25.1309
- **ATA 85 Application**: Same as CS-25.1309 above

**[§ 25.807](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-D/section-25.807) – Emergency Exits**
- **Applicability**: HIGH
- **Harmonization**: Harmonized with CS-25.807
- **ATA 85 Application**: Same as CS-25.807 above

**[§ 25.981](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-E/section-25.981) – Fuel System Ignition Prevention**
- **Applicability**: HIGH (by analogy)
- **Harmonization**: Harmonized with CS-25.981
- **ATA 85 Application**: Same as CS-25.981 above

#### 14 CFR Part 21: Certification Procedures

**[Part 21](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-21) – Certification Procedures for Products and Articles**
- **Applicability**: HIGH
- **Harmonization**: Broadly harmonized with EASA Part 21
- **ATA 85 Application**: Type certificate process including interface standards

---

## Hydrogen Infrastructure Standards and Regulations

### International Standards

**ISO 19880 Series – Gaseous Hydrogen Fuelling Stations**

**[ISO 19880-1:2020](https://www.iso.org/standard/71940.html) – General Requirements**
- **Applicability**: HIGH
- **Interface Impact**: H₂ refuelling infrastructure design and safety
- **Requirements**:
  - Fuelling station design and construction
  - Safety systems and interlocks
  - Operational procedures and maintenance
- **ATA 85 Application**: Airport H₂ fuelling station interface requirements

**[ISO 19880-3:2018](https://www.iso.org/standard/66997.html) – Valves**
- **Applicability**: MEDIUM
- **Interface Impact**: H₂ refuelling connector valves
- **ATA 85 Application**: Aircraft-side and ground-side valve specifications

**[ISO 19880-5:2019](https://www.iso.org/standard/68522.html) – Dispenser Hoses and Hose Assemblies**
- **Applicability**: HIGH
- **Interface Impact**: H₂ refuelling hose connections
- **ATA 85 Application**: Aircraft receptacle and hose coupling standards

**[ISO 19880-8:2019](https://www.iso.org/standard/67651.html) – Fuel Quality Control**
- **Applicability**: MEDIUM
- **Interface Impact**: H₂ fuel quality assurance at delivery
- **ATA 85 Application**: Fuel quality verification interface

### SAE Standards for Aviation

**SAE AS6858 – Hydrogen Fuel Servicing for Aircraft**
- **Status**: Under development
- **Applicability**: HIGH (when published)
- **Interface Impact**: Aviation-specific H₂ refuelling interfaces
- **Expected Coverage**:
  - Aircraft H₂ receptacle specifications
  - Ground service equipment requirements
  - Operational procedures for aircraft refuelling
- **ATA 85 Application**: Primary standard for aircraft H₂ interface design

**SAE AIR6464 – Aircraft Hydrogen Fuel System Safety**
- **Status**: Under development
- **Applicability**: HIGH
- **Interface Impact**: Safety requirements for aircraft H₂ systems
- **ATA 85 Application**: Safety case for H₂ interface systems

### Regional Regulations

**European Union**
- **[EU Hydrogen Strategy](https://energy.ec.europa.eu/topics/energy-systems-integration/hydrogen_en)** – Policy framework for hydrogen deployment
- **[EU Alternative Fuels Infrastructure Regulation (AFIR)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1804)** – Infrastructure deployment requirements
- **Applicability**: MEDIUM (policy context, not certification requirement)

**United States**
- **[DOE Hydrogen Safety Program](https://www.energy.gov/eere/fuelcells/hydrogen-safety)** – Best practices and guidelines
- **OSHA regulations** for H₂ handling in occupational settings
- **Applicability**: MEDIUM (operational context)

---

## Electrical Infrastructure Standards

### IEC Standards

**IEC 62196 Series – Plugs, Socket-Outlets, Vehicle Connectors**
- **Applicability**: MEDIUM (by analogy)
- **Interface Impact**: CO₂ battery charging connectors
- **Requirements**: Electrical and mechanical interface specifications
- **ATA 85 Application**: Baseline for aircraft charging connector design

**IEC 61851 Series – Electric Vehicle Conductive Charging Systems**
- **Applicability**: MEDIUM (by analogy)
- **Interface Impact**: Battery charging protocols and safety
- **Requirements**:
  - Charging modes and control pilot signals
  - Ground fault protection
  - Communication protocols
- **ATA 85 Application**: CO₂ battery charging system architecture

### SAE Standards

**SAE J1772 – Electric Vehicle Connector**
- **Applicability**: LOW (reference only)
- **Interface Impact**: Connector design principles
- **ATA 85 Application**: Design reference for aircraft charging connectors

**SAE AS50881 – Wiring Aerospace Vehicle**
- **Applicability**: HIGH
- **Interface Impact**: Aircraft-side wiring for ground power interfaces
- **ATA 85 Application**: GSE power interface wiring standards

### Airport Ground Power Standards

**SAE ARP 5015 – 270 VDC Aircraft Ground Power Connector**
- **Applicability**: MEDIUM
- **Interface Impact**: Traditional ground power interfaces
- **ATA 85 Application**: Baseline for enhanced GSE power interfaces

**ISO 6858 – Aircraft Ground Support Equipment – Electrical Ground Power Units**
- **Applicability**: MEDIUM
- **Interface Impact**: GSE power unit specifications
- **ATA 85 Application**: Compatibility requirements for enhanced GSE

---

## Building and Fire Safety Codes

### NFPA Codes

**[NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies) – Hydrogen Technologies Code**
- **Applicability**: HIGH
- **Interface Impact**: H₂ system installation and operation at airports
- **Requirements**:
  - H₂ storage and piping systems
  - Separation distances and ventilation
  - Fire protection and emergency response
- **ATA 85 Application**: Airport H₂ infrastructure safety requirements

**[NFPA 101](https://www.nfpa.org/codes-and-standards/101) – Life Safety Code**
- **Applicability**: MEDIUM
- **Interface Impact**: Passenger boarding and evacuation routes
- **Requirements**:
  - Means of egress
  - Emergency lighting and signage
  - Accessibility
- **ATA 85 Application**: Terminal interface design for boarding/evacuation

**[NFPA 409](https://www.nfpa.org/codes-and-standards/409) – Aircraft Hangars**
- **Applicability**: MEDIUM
- **Interface Impact**: Maintenance facility H₂ safety
- **Requirements**: Fire protection in aircraft maintenance facilities
- **ATA 85 Application**: H₂ servicing in hangars

### International Building Code (IBC)

**[IBC Chapter 4](https://codes.iccsafe.org/content/IBC2021P2) – Special Detailed Requirements Based on Use and Occupancy**
- **Applicability**: MEDIUM
- **Interface Impact**: Airport terminal modifications for boarding interfaces
- **ATA 85 Application**: Structural and fire safety for terminal interface modifications

---

## Environmental Regulations

### Emissions

**[ICAO Annex 16, Volume II](https://www.icao.int/environmental-protection/Pages/Standards.aspx) – Aircraft Engine Emissions**
- **Applicability**: MEDIUM (context)
- **Interface Impact**: H₂ and CO₂ battery systems support zero-emission operations
- **ATA 85 Application**: Verification of zero-emission claims at infrastructure interface

### Sustainability

**[EU Taxonomy Regulation](https://finance.ec.europa.eu/sustainable-finance/tools-and-standards/eu-taxonomy-sustainable-activities_en)**
- **Applicability**: MEDIUM (policy context)
- **Interface Impact**: Sustainability claims for H₂ and battery systems
- **ATA 85 Application**: Support for ATA 99 circularity and sustainability documentation

**[Corporate Sustainability Reporting Directive (CSRD)](https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/company-reporting-and-auditing/company-reporting/corporate-sustainability-reporting_en)**
- **Applicability**: LOW (corporate reporting)
- **Interface Impact**: Reporting on sustainable infrastructure interfaces
- **ATA 85 Application**: Data provision for corporate sustainability reporting

---

## Airport and Operator Standards

### IATA Standards

**IATA Airport Handling Manual (AHM)**
- **Applicability**: MEDIUM
- **Interface Impact**: Ground handling procedures and equipment
- **ATA 85 Application**: Operational procedures for novel interfaces

**IATA Ground Operations Manual (IGOM)**
- **Applicability**: MEDIUM
- **Interface Impact**: Standard ground operations practices
- **ATA 85 Application**: Integration of H₂ and battery servicing into ground ops

### ICAO Standards

**[ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx) – Aerodromes**
- **Applicability**: MEDIUM
- **Interface Impact**: Aerodrome design and operations
- **Requirements**:
  - Aircraft stand design
  - Fuelling area specifications
  - Fire fighting and rescue services
- **ATA 85 Application**: Airport infrastructure requirements for AMPEL360 operations

---

## Applicability Matrix Summary

| Regulation/Standard | Domain | Applicability | Primary ATA 85 Impact |
|---------------------|--------|---------------|----------------------|
| CS-25.1309 / §25.1309 | Aviation | HIGH | All interface systems safety |
| CS-25.807 / §25.807 | Aviation | HIGH | Boarding/evacuation interfaces |
| CS-25.981 / §25.981 | Aviation | HIGH | H₂ fuel system safety |
| Part 21 (EASA/FAA) | Aviation | HIGH | Certification process |
| ISO 19880 series | H₂ Infrastructure | HIGH | H₂ refuelling stations |
| SAE AS6858 | H₂ Aviation | HIGH | Aircraft H₂ interfaces |
| IEC 62196/61851 | Electrical | MEDIUM | Battery charging (by analogy) |
| SAE AS50881 | Aviation Electrical | HIGH | GSE power wiring |
| NFPA 2 | Fire Safety | HIGH | Airport H₂ safety |
| NFPA 101 | Building Safety | MEDIUM | Boarding/evacuation routes |
| ICAO Annex 14 | Airports | MEDIUM | Aerodrome infrastructure |
| IATA AHM/IGOM | Operations | MEDIUM | Ground handling procedures |

Detailed traceability from regulations to ATA 85 requirements is maintained in [ASSETS/Matrices/85-00-10-A-001_Regulatory_Compliance_Matrix.xlsx](./ASSETS/Matrices/).

---

## Gaps and Special Conditions

### Identified Regulatory Gaps

1. **Hydrogen Aviation Certification**  
   - Gap: No comprehensive aviation certification standard for H₂ aircraft
   - Approach: Develop issue papers, leverage CS-25.981 by analogy, engage with ongoing SAE AS6858 development
   - Status: Active engagement with EASA and FAA on Special Conditions

2. **Novel Boarding Configurations**  
   - Gap: BWB multi-level boarding not explicitly covered by CS-25.807
   - Approach: Equivalency demonstration, analysis of evacuation performance
   - Status: Pre-application discussions with authorities

3. **CO₂ Battery Infrastructure**  
   - Gap: No aviation-specific standard for CO₂ battery ground charging
   - Approach: Adapt EV charging standards (IEC 61851), develop aircraft-specific requirements
   - Status: Industry standards development (via SAE)

### Proposed Special Conditions

Special Conditions may be required for:
1. Hydrogen fuel system certification basis
2. Multi-level passenger evacuation for BWB configuration
3. CO₂ battery safety and charging systems
4. Novel ground interface communication protocols

Development and submission of Special Condition proposals is managed under [85-00-10-006_Authority_Engagement_and_Issue_Papers.md](./85-00-10-006_Authority_Engagement_and_Issue_Papers.md).

---

## Compliance Strategy

### Means of Compliance (MoC)

For each applicable regulation, compliance will be demonstrated through:
- **Analysis**: Safety analysis, thermal/electrical modeling, structural analysis
- **Test**: Laboratory tests, ground tests, operational trials
- **Inspection**: Design review, manufacturing inspection
- **Similarity**: Reference to existing certified systems where applicable

The complete compliance demonstration plan is documented in [85-00-10-004_Conformity_Demonstration_Plan.md](./85-00-10-004_Conformity_Demonstration_Plan.md).

### Compliance Matrix

A comprehensive compliance matrix mapping regulations to requirements to verification methods to evidence is maintained in [ASSETS/Matrices/85-00-10-A-001_Regulatory_Compliance_Matrix.xlsx](./ASSETS/Matrices/).

---

## References

### Internal Documents
- [85-00-10-001_Certification_Strategy_Interface_Standards.md](./85-00-10-001_Certification_Strategy_Interface_Standards.md)
- [85-00-10-003_Compliance_Matrix_Overview.md](./85-00-10-003_Compliance_Matrix_Overview.md)
- [85-00-10-004_Conformity_Demonstration_Plan.md](./85-00-10-004_Conformity_Demonstration_Plan.md)
- [85-00-10-006_Authority_Engagement_and_Issue_Papers.md](./85-00-10-006_Authority_Engagement_and_Issue_Papers.md)

### External References
- [EASA CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)
- [FAA 14 CFR Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25)
- [EASA Part 21](https://www.easa.europa.eu/document-library/regulations/commission-regulation-eu-no-7482012)
- [ISO 19880-1:2020](https://www.iso.org/standard/71940.html)
- [NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies)
- [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---

**End of Document**
