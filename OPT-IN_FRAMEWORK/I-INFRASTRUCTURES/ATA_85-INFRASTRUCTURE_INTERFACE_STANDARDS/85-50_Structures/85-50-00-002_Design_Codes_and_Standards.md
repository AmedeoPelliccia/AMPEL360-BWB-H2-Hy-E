# 85-50-00-002: Design Codes and Standards

## Document Information

- **Document ID**: 85-50-00-002  
- **Title**: Design Codes and Standards  
- **Version**: 1.0  
- **Status**: DRAFT  
- **Date**: 2025-11-22  

---

## 1. Purpose

This document establishes the **mandatory design codes and standards** for all infrastructure structures supporting the AMPEL360 BWB-H2-Hy-E aircraft. It provides:

- **Primary design standards** for structural, mechanical, and safety systems
- **Regulatory requirements** for aviation infrastructure
- **H₂-specific codes** for safe hydrogen handling
- **International harmonization** guidance for multi-region deployment

Compliance with these standards is required for all infrastructure projects documented in [ATA 85-50](85-50-00-001_Infrastructure_Structures_Overview.md).

---

## 2. Hierarchy of Standards

### 2.1 Precedence Order

When conflicts arise between standards, the following precedence applies:

1. **Local regulatory requirements** (mandatory)
2. **Aviation-specific standards** ([ICAO](https://www.icao.int/), [EASA](https://www.easa.europa.eu/), [FAA](https://www.faa.gov/))
3. **H₂ safety codes** ([NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code), [ISO 19880](https://www.iso.org/standard/71940.html))
4. **International structural codes** ([Eurocode](https://eurocodes.jrc.ec.europa.eu/), [ASCE](https://www.asce.org/))
5. **Industry best practices** (technical guidelines)

*Note*: Project-specific Basis of Design (BOD) documents shall explicitly state any deviations or clarifications.

---

## 3. Building and Structural Codes

### 3.1 International Building Codes

| **Standard** | **Title** | **Application** | **Link** |
|-------------|-----------|----------------|----------|
| **IBC** | [International Building Code](https://codes.iccsafe.org/content/IBC2021P1) | General building design (US) | [IBC 2021](https://codes.iccsafe.org/content/IBC2021P1) |
| **Eurocode 0** | [Basis of Structural Design](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=130) | Design philosophy (EU) | [EN 1990](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=130) |
| **Eurocode 1** | [Actions on Structures](https://eurocodes.jrc.ec.europa.eu/) | Load definitions (EU) | [EN 1991](https://eurocodes.jrc.ec.europa.eu/) |
| **ASCE 7** | [Minimum Design Loads](https://www.asce.org/publications-and-news/asce-7) | Load combinations (US) | [ASCE 7-22](https://www.asce.org/publications-and-news/asce-7) |

### 3.2 Concrete Structures

| **Standard** | **Title** | **Application** | **Link** |
|-------------|-----------|----------------|----------|
| **ACI 318** | [Building Code Requirements for Structural Concrete](https://www.concrete.org/) | Reinforced concrete design (US) | [ACI 318-19](https://www.concrete.org/store/productdetail.aspx?ItemID=31814) |
| **Eurocode 2** | [Design of Concrete Structures](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=132) | Concrete design (EU) | [EN 1992](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=132) |
| **ACI 376** | [Code Requirements for Design and Construction of Concrete Structures for Containment of Refrigerated Liquefied Gases](https://www.concrete.org/) | Cryogenic concrete (LH₂ tanks) | [ACI 376-10](https://www.concrete.org/) |

### 3.3 Steel Structures

| **Standard** | **Title** | **Application** | **Link** |
|-------------|-----------|----------------|----------|
| **AISC 360** | [Specification for Structural Steel Buildings](https://www.aisc.org/) | Steel building design (US) | [AISC 360-22](https://www.aisc.org/publications/steel-construction-manual-resources/) |
| **Eurocode 3** | [Design of Steel Structures](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=133) | Steel design (EU) | [EN 1993](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=133) |
| **AISC 341** | [Seismic Provisions for Structural Steel Buildings](https://www.aisc.org/) | Seismic steel design (US) | [AISC 341-22](https://www.aisc.org/) |

### 3.4 Foundations

| **Standard** | **Title** | **Application** | **Link** |
|-------------|-----------|----------------|----------|
| **Eurocode 7** | [Geotechnical Design](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=137) | Foundation design (EU) | [EN 1997](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=137) |
| **ACI 336.3R** | [Design and Construction of Drilled Piers](https://www.concrete.org/) | Deep foundations | [ACI 336.3R-93](https://www.concrete.org/) |

---

## 4. Load Standards

### 4.1 General Loads

| **Load Type** | **Standard** | **Application** |
|---------------|-------------|----------------|
| **Dead Loads** | ASCE 7, Eurocode 1-1 | Self-weight, permanent fixtures |
| **Live Loads** | ASCE 7-22 Table 4.3-1, EN 1991-1-1 | Occupancy, equipment, vehicles |
| **Snow Loads** | ASCE 7 Ch. 7, EN 1991-1-3 | Roof snow, drift, sliding |
| **Rain Loads** | ASCE 7 Ch. 8, EN 1991-1-3 | Ponding, drainage |

### 4.2 Wind Loads

| **Standard** | **Application** | **Key Features** |
|-------------|----------------|------------------|
| **[ASCE 7-22 Ch. 26-31](https://www.asce.org/publications-and-news/asce-7)** | Directional procedure (US) | Risk categories, exposure, topography |
| **[EN 1991-1-4](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=131)** | Wind actions (EU) | Peak velocity pressure, structural factor |
| **ISO 4354** | [Wind actions on structures](https://www.iso.org/standard/10140.html) | International harmonization |

### 4.3 Seismic Loads

| **Standard** | **Application** | **Key Features** |
|-------------|----------------|------------------|
| **[ASCE 7-22 Ch. 11-22](https://www.asce.org/publications-and-news/asce-7)** | Seismic design (US) | Response spectrum, site class, Seismic Design Categories |
| **[Eurocode 8](https://eurocodes.jrc.ec.europa.eu/showpage.php?id=138)** | Earthquake design (EU) | Ground acceleration, behavior factors |
| **[ASCE 41-17](https://www.asce.org/)** | Seismic evaluation of existing buildings | Retrofit and upgrade |

### 4.4 Thermal Loads

| **Application** | **Standard** | **Reference** |
|----------------|-------------|---------------|
| **Cryogenic tanks (LH₂)** | [API 620 Appendix Q](https://www.api.org/products-and-services/standards) | Thermal stress, material embrittlement |
| **General thermal effects** | Eurocode 1-5, ASCE 7 | Temperature ranges, expansion joints |

### 4.5 Blast and Explosion Loads

| **Standard** | **Application** | **Link** |
|-------------|----------------|----------|
| **[UFC 3-340-02](https://www.wbdg.org/ffc/dod/unified-facilities-criteria-ufc/ufc-3-340-02)** | Structures to Resist the Effects of Accidental Explosions | DoD blast design (US) |
| **[NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code)** | Hydrogen Technologies Code | H₂ explosion scenarios |
| **ISO 16852** | Explosion consequence analysis | International guidance |

---

## 5. H₂-Specific Standards and Codes

### 5.1 Hydrogen Safety Codes

| **Standard** | **Title** | **Application** | **Link** |
|-------------|-----------|----------------|----------|
| **NFPA 2** | [Hydrogen Technologies Code](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code) | Comprehensive H₂ safety requirements | [NFPA 2 (2023)](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code) |
| **ISO 19880-1** | [Gaseous hydrogen — Fueling stations — Part 1: General requirements](https://www.iso.org/standard/71940.html) | H₂ fueling station design | [ISO 19880-1:2020](https://www.iso.org/standard/71940.html) |
| **ISO 13984** | [Liquid hydrogen — Land vehicle fuel tanks](https://www.iso.org/standard/23419.html) | LH₂ tank design and testing | [ISO 13984:1999](https://www.iso.org/standard/23419.html) |
| **CGA G-5.4** | Standard for Hydrogen Vent Systems | Safe venting and dispersion | [CGA G-5.4-2022](https://www.cganet.com/) |

### 5.2 Cryogenic Storage Standards

| **Standard** | **Application** | **Link** |
|-------------|----------------|----------|
| **[API 620](https://www.api.org/products-and-services/standards)** | Design and Construction of Large, Welded, Low-Pressure Storage Tanks | LH₂ storage tanks | [API 620 12th Ed.](https://www.api.org/products-and-services/standards) |
| **[API 625](https://www.api.org/)** | Tank Systems for Refrigerated Liquefied Gas Storage | Tank system design | [API 625-2015](https://www.api.org/) |
| **[EN 14620](https://standards.iteh.ai/catalog/standards/cen/fc9e8a27-d70e-4f5a-9a0f-6c4e9f9d8b7a/en-14620-1-2006)** | Design and manufacture of site built, vertical, cylindrical, flat-bottomed steel tanks for the storage of refrigerated, liquefied gases | EU cryogenic tank standard | EN 14620 series |

### 5.3 H₂ Fuel Quality

| **Standard** | **Application** |
|-------------|----------------|
| **[ISO 14687](https://www.iso.org/standard/69539.html)** | Hydrogen fuel quality — Product specification |
| **SAE J2719** | Hydrogen fuel quality for fuel cell vehicles |

---

## 6. Aviation Infrastructure Standards

### 6.1 Aerodrome Design

| **Standard** | **Title** | **Application** | **Link** |
|-------------|-----------|----------------|----------|
| **ICAO Annex 14** | [Aerodrome Design and Operations](https://www.icao.int/safety/pages/annex-14.aspx) | International airport standards | [ICAO Annex 14 Vol. I](https://www.icao.int/safety/pages/annex-14.aspx) |
| **FAA AC 150/5300-13B** | [Airport Design](https://www.faa.gov/airports/resources/advisory_circulars/) | Airport pavement and geometry (US) | [AC 150/5300-13B](https://www.faa.gov/airports/resources/advisory_circulars/) |
| **CS-ADR-DSN** | [EASA Certification Specifications for Aerodrome Design](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-adr-dsg-issue-4) | Aerodrome design (EU) | [CS-ADR-DSN Issue 4](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-adr-dsg-issue-4) |

### 6.2 Apron and Pavement Design

| **Standard** | **Application** |
|-------------|----------------|
| **FAA AC 150/5320-6G** | Airport pavement design for Boeing and Airbus aircraft |
| **ICAO Airport Services Manual Part 3** | Pavement design and evaluation |
| **ACN-PCN method** | Aircraft Classification Number / Pavement Classification Number |

### 6.3 Aircraft Ground Support

| **Standard** | **Application** |
|-------------|----------------|
| **ISO 6966** | Aircraft ground support equipment — General requirements |
| **SAE AS36100** | Performance Standard for Aircraft Ground Support Equipment |

---

## 7. Fire Protection and Safety

### 7.1 Fire Codes

| **Standard** | **Title** | **Application** | **Link** |
|-------------|-----------|----------------|----------|
| **NFPA 1** | Fire Code | General fire safety | [NFPA 1 (2021)](https://www.nfpa.org/codes-and-standards/1/fire-code) |
| **NFPA 30** | Flammable and Combustible Liquids Code | Fuel storage safety | [NFPA 30 (2021)](https://www.nfpa.org/codes-and-standards/30/flammable-and-combustible-liquids-code) |
| **NFPA 409** | Aircraft Hangars | Hangar fire protection | [NFPA 409 (2022)](https://www.nfpa.org/codes-and-standards/409/aircraft-hangars) |
| **NFPA 502** | Standard for Road Tunnels, Bridges, and Other Limited Access Highways | Tunnel fire safety (underground H₂ piping) | [NFPA 502 (2020)](https://www.nfpa.org/) |

### 7.2 Fire Resistance

| **Standard** | **Application** |
|-------------|----------------|
| **ASTM E119** | Standard Test Methods for Fire Tests of Building Construction and Materials |
| **UL 263** | Fire Tests of Building Construction and Materials |
| **EN 1363-1** | Fire resistance tests — Part 1: General requirements |

---

## 8. Electrical and Mechanical Systems

### 8.1 Electrical Systems

| **Standard** | **Title** | **Application** |
|-------------|-----------|----------------|
| **IEC 61936-1** | Power installations exceeding 1 kV AC | Substation design |
| **IEEE 80** | Guide for Safety in AC Substation Grounding | Grounding and earthing |
| **NEC (NFPA 70)** | National Electrical Code | Electrical installations (US) |
| **IEC 60364** | Low-voltage electrical installations | Electrical design (international) |

### 8.2 HVAC and Ventilation

| **Standard** | **Application** |
|-------------|----------------|
| **ASHRAE 90.1** | Energy Standard for Buildings Except Low-Rise Residential Buildings |
| **ISO 16890** | Air filters for general ventilation |
| **CGA G-5.4** | Hydrogen ventilation and dispersion |

---

## 9. Materials and Testing

### 9.1 Material Specifications

| **Material** | **Standard** | **Application** |
|--------------|-------------|----------------|
| **Structural steel** | ASTM A36, ASTM A992, EN 10025 | Building frames, supports |
| **Stainless steel** | ASTM A240 (304, 316), EN 10088 | H₂-compatible components |
| **9% Ni steel** | ASTM A553, EN 10028-4 | Cryogenic tanks (LH₂) |
| **Aluminum** | ASTM B209, EN 573-3 | Lightweight structures |
| **Concrete** | ASTM C150, EN 197-1 | Foundations, pavements |
| **Reinforcement** | ASTM A615, EN 10080 | Rebar for concrete |

### 9.2 Welding Standards

| **Standard** | **Application** |
|-------------|----------------|
| **AWS D1.1** | Structural Welding Code — Steel |
| **AWS D1.6** | Structural Welding Code — Stainless Steel |
| **EN ISO 3834** | Quality requirements for fusion welding of metallic materials |

### 9.3 Non-Destructive Testing (NDT)

| **Standard** | **Application** |
|-------------|----------------|
| **ASME Section V** | Nondestructive Examination |
| **EN ISO 17636** | Radiographic testing of welds |
| **ASTM E165** | Liquid penetrant testing |

---

## 10. Environmental and Sustainability

### 10.1 Environmental Standards

| **Standard** | **Application** |
|-------------|----------------|
| **ISO 14001** | Environmental management systems |
| **ISO 14040/14044** | Life cycle assessment (LCA) |
| **[ISO 14067](https://www.iso.org/standard/71206.html)** | Carbon footprint of products |

### 10.2 Sustainable Construction

| **Standard** | **Application** |
|-------------|----------------|
| **LEED v4.1** | Leadership in Energy and Environmental Design |
| **BREEAM** | Building Research Establishment Environmental Assessment Method |
| **ISO 15392** | Sustainability in building construction — General principles |

---

## 11. Quality Assurance and Certification

### 11.1 Quality Management

| **Standard** | **Application** |
|-------------|----------------|
| **ISO 9001** | Quality management systems |
| **ISO 19011** | Guidelines for auditing management systems |
| **AS9100** | Quality management systems — Requirements for aviation, space, and defense organizations |

### 11.2 Inspection and Testing

| **Standard** | **Application** |
|-------------|----------------|
| **ACI 318 Ch. 26** | Inspection and testing requirements for concrete |
| **AISC 360 Ch. N** | Quality control and quality assurance for steel |

---

## 12. Regional Code Adaptations

### 12.1 United States

- **IBC** (International Building Code)
- **ASCE 7** (loads)
- **ACI 318** (concrete), **AISC 360** (steel)
- **NFPA codes** (fire and H₂ safety)
- **FAA Advisory Circulars** (airport design)

### 12.2 European Union

- **Eurocode series** (structural design)
- **EN standards** (materials, testing, fire)
- **EASA CS-ADR-DSN** (aerodrome design)
- **National Annexes** for country-specific requirements

### 12.3 Other Regions

- **Canada**: National Building Code of Canada (NBCC), CSA standards
- **Australia**: AS/NZS standards (Australian/New Zealand)
- **Middle East**: Local codes with reference to international standards
- **Asia**: Country-specific codes (e.g., GB codes in China, IS codes in India)

---

## 13. Compliance Documentation

All infrastructure structures require:

1. **Basis of Design (BOD)** document stating applicable codes
2. **Design calculations** stamped by licensed professional engineer
3. **Material certifications** and mill test reports
4. **Inspection and testing reports** per code requirements
5. **As-built drawings** reflecting actual construction
6. **Occupancy/completion certificates** from authorities having jurisdiction (AHJ)

See [ASSETS/Standards_and_Codes/85-50-00-A-005_Certification_Requirements.md](ASSETS/Standards_and_Codes/) for detailed certification process.

---

## 14. Standards Updates and Maintenance

### 14.1 Version Control

- **Track standard editions** used for each project
- **Monitor updates** to key codes (annual review cycle)
- **Evaluate impact** of new editions on existing designs
- **Document deviations** if older editions are retained

### 14.2 Continuous Improvement

- **Lessons learned** from project implementations
- **Industry feedback** integration
- **Regulatory changes** monitoring
- **Harmonization efforts** across regions

---

## 15. Cross-References

### 15.1 Internal (ATA 85-50)

- [85-50-00-001_Infrastructure_Structures_Overview.md](85-50-00-001_Infrastructure_Structures_Overview.md): Overall structures overview
- [85-50-00-003_Material_Selection_Strategy.md](85-50-00-003_Material_Selection_Strategy.md): Material specifications
- [85-50-00-004_Safety_and_H2_Considerations.md](85-50-00-004_Safety_and_H2_Considerations.md): Safety design criteria
- [ASSETS/Standards_and_Codes/](ASSETS/Standards_and_Codes/): Standards library and code summaries

### 15.2 External (Other ATAs)

- [85-00-10_Certification](../85-00_GENERAL/85-00-10_Certification/): Certification artifacts
- [ATA 99 – Circularity & Carbon](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_99-CIRCULARITY_CARBON/): Sustainability compliance

### 15.3 Regulatory

- [EASA CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27): Certification Specifications for Large Aeroplanes
- [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx): Aerodrome Design and Operations
- [NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code): Hydrogen Technologies Code

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22.

---

**End of Document**
