---
Title: "H2 GSE Materials Selection — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-06-02-04A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Material selection criteria and requirements for hydrogen Ground Support Equipment to prevent embrittlement and ensure long-term compatibility."
Keywords: ["ATA 03","GSE","Hydrogen","Materials","Embrittlement","Compatibility"]
Compliance:
  - "NASA-STD-8719.17"
  - "ASME B31.12"
  - "ASTM G142"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Parent: "../00_INDEX.md"
  Related: "./03-00-06-02-02A_Cryogenic_GSE_Requirements.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-00-06-02-04A — H2 GSE Materials Selection

## 1. Purpose

This document defines **material selection criteria** for hydrogen Ground Support Equipment to ensure long-term compatibility with gaseous and liquid hydrogen. Improper material selection can lead to hydrogen embrittlement, resulting in unexpected failures with catastrophic consequences.

## 2. Scope

Material requirements for:
- **Pressure-containing components** (tanks, piping, valves)
- **Structural components** (supports, frames, fasteners)
- **Sealing materials** (gaskets, O-rings, packings)
- **Non-metallic components** (hoses, insulators, coatings)

Addresses both:
- **Gaseous Hydrogen (GH2)** at elevated pressures and temperatures
- **Liquid Hydrogen (LH2)** at cryogenic temperatures (-253°C)

## 3. Applicable Documents

- [NASA-STD-8719.17](https://standards.nasa.gov/) — Safety Standard for Hydrogen and Hydrogen Systems
- [ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines) — Hydrogen Piping and Pipelines
- [ASTM G142](https://www.astm.org/g0142-98r16.html) — Standard Test Method for Determination of Susceptibility of Metals to Embrittlement in Hydrogen
- [ISO 11114-4](https://www.iso.org/standard/50507.html) — Transportable Gas Cylinders — Compatibility of Cylinder and Valve Materials with Gas Contents (Part 4: Hydrogen)
- [CGA G-5.4](https://www.cganet.com/) — Standard for Hydrogen Piping Systems

## 4. Hydrogen Embrittlement Mechanism

### 4.1 Definition

**Hydrogen Embrittlement**: Degradation of mechanical properties (ductility, fracture toughness) when atomic hydrogen diffuses into the material's crystal lattice, causing:
- **Reduced ductility** (lower elongation at fracture)
- **Reduced fracture toughness** (lower resistance to crack propagation)
- **Susceptibility to cracking** under tensile stress (delayed failure)

### 4.2 Factors Affecting Embrittlement

| Factor | Effect | Notes |
|--------|--------|-------|
| **Hydrogen Pressure** | Higher pressure → greater H absorption → more embrittlement | Especially critical above 10 MPa (100 bar, 1,450 psi) |
| **Temperature** | Peak embrittlement at -50°C to +150°C; reduced at cryogenic temps | LH2 at -253°C is less prone to embrittlement than GH2 at ambient |
| **Stress Level** | Higher tensile stress → faster crack growth | Design for lower stress levels in H2 service |
| **Exposure Time** | Embrittlement can develop over hours to years | Long-term exposure testing required |
| **Material Microstructure** | FCC metals (austenitic SS, Al, Cu, Ni) resist embrittlement; BCC metals (ferritic steel, Ti) susceptible | Material selection is critical |

### 4.3 Testing for Embrittlement

| Test Method | Description | Standard |
|-------------|-------------|----------|
| **Slow Strain Rate Tensile Test (SSRT)** | Apply slow tensile strain (10⁻⁵ to 10⁻⁶ s⁻¹) in H2 environment; compare ductility to air | ASTM G142 |
| **Fracture Mechanics Test** | Measure fracture toughness (KIC) in H2 vs. air | ASTM E1681 |
| **Notched Tensile Test** | Tensile test with notched specimen in H2 | ISO 11114-4 |

**Acceptance Criterion**: Reduction in ductility or fracture toughness < 10% in H2 environment vs. air (per NASA-STD-8719.17).

## 5. Material Selection Guidelines

### 5.1 General Principles

| Principle | Description |
|-----------|-------------|
| **Prefer FCC Crystal Structure** | Face-centered cubic (FCC) metals have low hydrogen diffusivity and resist embrittlement |
| **Avoid BCC and HCP** | Body-centered cubic (BCC) and hexagonal close-packed (HCP) metals are susceptible |
| **Use Proven Materials** | Rely on materials with documented hydrogen service history |
| **Perform Qualification Testing** | Test new or unproven materials per ASTM G142 before use |
| **Design for Low Stress** | Reduce stress concentrations; use generous fillets and radii |

### 5.2 Material Crystal Structures

| Crystal Structure | Examples | H2 Compatibility |
|-------------------|----------|------------------|
| **FCC** | Austenitic stainless steel (304, 316), aluminum alloys, copper, nickel alloys | Excellent (low H diffusivity) |
| **BCC** | Ferritic/martensitic steels, carbon steel, alloy steels (4340, 4130), titanium alloys | Poor (high susceptibility to embrittlement) |
| **HCP** | Titanium, magnesium, zinc | Poor to fair (depends on alloy) |

## 6. Approved Metallic Materials

### 6.1 Austenitic Stainless Steels (Preferred)

| Alloy | UNS Number | Applications | Advantages | Disadvantages |
|-------|------------|--------------|------------|---------------|
| **304** | S30400 | General piping, tanks, valves | Excellent H2 compatibility, widely available, weldable | Lower corrosion resistance than 316 |
| **304L** | S30403 | Same as 304 | Lower carbon (< 0.03%) reduces sensitization in welds | Slightly lower strength |
| **316** | S31600 | Marine environment, higher corrosion resistance | Better corrosion resistance (Mo addition) | Higher cost than 304 |
| **316L** | S31603 | Critical welds, marine, chemical exposure | Lower carbon for improved weldability | Higher cost |
| **321** | S32100 | High-temperature applications (stabilized with Ti) | Resists sensitization without low carbon | Limited availability |

**AMPEL360 Standard**: Use **316L** for LH2 wetted components; **304L** acceptable for non-critical or low-corrosion environments.

### 6.2 Aluminum Alloys

| Alloy | Temper | Applications | Advantages | Disadvantages |
|-------|--------|--------------|------------|---------------|
| **5083** | H116 (marine grade) | LH2 tanks, structures | Excellent cryogenic properties, non-heat-treatable, weldable | Lower strength than 6061 |
| **6061** | T6 | Structural frames, brackets | Good strength-to-weight, widely available | Slight reduction in toughness at -253°C |
| **2219** | T87 | Aerospace applications (high-strength) | High strength, excellent cryogenic properties | Expensive, limited availability |

**AMPEL360 Standard**: Use **5083-H116** for LH2 tanks; **6061-T6** for non-pressure structures.

### 6.3 Nickel Alloys (High-Performance)

| Alloy | UNS Number | Applications | Advantages | Disadvantages |
|-------|------------|--------------|------------|---------------|
| **Inconel 718** | N07718 | High-stress components (e.g., pump shafts, bolts) | High strength at cryogenic temps, excellent H2 compatibility | Expensive, difficult to machine |
| **Monel 400** | N04400 | Valve seats, seals | Corrosion resistance, good H2 compatibility | Expensive |

**Use Case**: Reserve for critical, high-stress applications where SS or Al insufficient.

### 6.4 Copper Alloys

| Alloy | Applications | Notes |
|-------|-------------|-------|
| **Copper (C11000)** | Electrical conductors, heat exchangers | Excellent H2 compatibility, high thermal/electrical conductivity; soft (low strength) |
| **Beryllium Copper (C17200)** | Springs, electrical contacts | Higher strength than pure copper; excellent H2 compatibility |

### 6.5 Avoid or Restrict

| Material | H2 Compatibility | Restriction |
|----------|------------------|-------------|
| **Carbon Steel** | Poor (embrittlement) | **NOT APPROVED** for H2 pressure vessels or piping at pressure > 1 bar |
| **Low-Alloy Steel (4130, 4340)** | Poor (embrittlement) | **NOT APPROVED** for H2 service |
| **Titanium Alloys** | Fair to Poor (depends on alloy and pressure) | **RESTRICTED**: Only use Ti-6Al-4V or Ti-5Al-2.5Sn with qualification testing; avoid pressures > 35 MPa (5,000 psi) |
| **Magnesium Alloys** | Poor | **NOT APPROVED** (fire risk, poor H2 compatibility) |
| **Cast Iron** | Poor | **NOT APPROVED** (brittle at cryogenic temps) |

## 7. Non-Metallic Materials

### 7.1 Elastomers and Seals

| Material | Temperature Range | H2 Permeability | Applications |
|----------|-------------------|-----------------|-------------|
| **PTFE (Teflon)** | -253°C to +260°C | Low | Primary seal material; valve seats, gaskets, O-rings |
| **PCTFE (Kel-F)** | -240°C to +200°C | Very Low | Higher mechanical strength than PTFE; O-rings, seals |
| **Kalrez (perfluoroelastomer)** | -25°C to +260°C | Low | High-performance seals (expensive) |
| **Viton (FKM)** | -40°C to +200°C | Moderate | Acceptable for low-pressure GH2; NOT for LH2 (too brittle) |
| **Buna-N (NBR)** | -40°C to +120°C | High | NOT RECOMMENDED (high permeability, incompatible with LH2) |

**AMPEL360 Standard**: Use **PTFE** or **PCTFE** for all LH2 seals; Viton acceptable for GH2 < 10 bar and T > -40°C.

### 7.2 Plastics and Composites

| Material | Applications | Notes |
|----------|-------------|-------|
| **PEEK (Polyetheretherketone)** | Bushings, insulators, structural | Maintains properties at -253°C; low H2 permeability |
| **G-10 Fiberglass Epoxy** | Structural supports, electrical insulation | Low thermal conductivity, high strength, cryogenic-compatible |
| **UHMW Polyethylene** | Wear surfaces, low-friction components | Good at cryogenic temps, but high H2 permeability (avoid pressure boundaries) |
| **Epoxy Resins** | Adhesives, composite matrix | Select cryogenic-rated formulations |

### 7.3 Coatings and Surface Treatments

| Coating | Purpose | Compatibility |
|---------|---------|---------------|
| **Electroless Nickel** | Corrosion protection, wear resistance | Compatible; avoid high-phosphorus formulations (embrittlement risk) |
| **Hard Anodizing (Aluminum)** | Corrosion and wear protection | Compatible (Type III per MIL-A-8625) |
| **Zinc Galvanizing** | Corrosion protection (carbon steel structures not in H2 contact) | Compatible for external use; NOT for H2-wetted surfaces |
| **Paint (Epoxy, Polyurethane)** | Corrosion protection | Select low-temperature-rated paints for cryogenic surfaces |
| **PTFE Coating** | Low-friction surfaces | Compatible |

## 8. Fasteners and Joining

### 8.1 Bolts and Nuts

| Application | Material | Standard |
|-------------|----------|----------|
| **General Structural** | 316 SS or A286 (high-strength stainless) | ASTM A193 Grade B8M (316 SS), A286 |
| **Critical High-Stress** | Inconel 718 or A286 | Aerospace bolting standards |
| **Aluminum Structures** | Al 7075-T73 or 2024-T4 (cadmium-plated or anodized) | Match structure material to avoid galvanic corrosion |

**Avoid**: Carbon steel bolts in H2 pressure boundary (embrittlement risk).

### 8.2 Welding

| Material | Welding Process | Filler Material | Notes |
|----------|-----------------|-----------------|-------|
| **316L SS** | GTAW (TIG), GMAW (MIG) | ER316L | Use low-carbon filler to minimize sensitization |
| **304L SS** | GTAW, GMAW | ER308L | Lower carbon than 308 |
| **5083 Al** | GTAW, GMAW | ER5183 or ER5356 | Prevent cracking with proper preheat and technique |
| **Inconel 718** | GTAW | ERNiCrFe-7 (IN 718) | Requires PWHT (post-weld heat treatment) for strength |

**Weld Qualification**: All pressure-boundary welds require:
- Welder certification per ASME Section IX
- Procedure Qualification Record (PQR)
- Non-destructive testing (RT, UT, or PT) per code

### 8.3 Brazing and Soldering

| Method | Filler Material | Application | Notes |
|--------|-----------------|-------------|-------|
| **Brazing** | Silver-based (BAg alloys) or nickel-based | Joining dissimilar metals, complex assemblies | Acceptable for non-critical joints; avoid in high-stress areas |
| **Soldering** | Tin-lead or tin-silver | Electrical connections only | NOT for pressure boundaries |

## 9. Material Qualification and Testing

### 9.1 New Material Approval Process

Before using a new material in H2 service:

| Step | Activity | Responsible Party |
|------|----------|-------------------|
| 1. **Literature Review** | Check NASA, ASME, and industry databases for H2 compatibility data | Engineering |
| 2. **Preliminary Selection** | Select candidate materials based on properties and cost | Engineering |
| 3. **Testing** | Perform ASTM G142 (SSRT in H2) or equivalent | Testing Laboratory |
| 4. **Analysis** | Compare mechanical properties in H2 vs. air; accept if degradation < 10% | Engineering |
| 5. **Approval** | Document in Approved Materials List (AML) | Chief Engineer |

### 9.2 Approved Materials List (AML)

AMPEL360 shall maintain an AML for H2 GSE, listing:
- Material designation and specification
- Approved applications (e.g., LH2 piping, GH2 seals)
- Restrictions (e.g., pressure limits, temperature limits)
- Test data reference

**Update Frequency**: Review AML annually and after any material failure investigation.

## 10. Material Inspection and Traceability

### 10.1 Material Certification

All pressure-boundary materials shall have:
- **Certified Material Test Report (CMTR)** or **Mill Test Certificate (MTC)** documenting:
  - Heat number
  - Chemical composition
  - Mechanical properties (yield, tensile, elongation)
  - Heat treatment
- **Traceability**: Mark each component with heat number (stamping, engraving, or tags)

### 10.2 Receiving Inspection

| Inspection | Method | Acceptance |
|------------|--------|------------|
| **Visual** | Check for defects (cracks, corrosion, dents) | No visible defects |
| **Dimensional** | Verify dimensions per drawing | Within tolerances |
| **Material Verification** | Positive Material Identification (PMI) using XRF or OES | Matches CMTR |
| **Certification Review** | Verify CMTR against specification | Complete and accurate |

## 11. Material Selection Summary Table

| Component | Preferred Material | Alternate Material | Avoid |
|-----------|-------------------|-------------------|-------|
| **LH2 Tanks** | 316L SS, 5083 Al | 304L SS | Carbon steel, cast iron |
| **LH2 Piping** | 316L SS | 304L SS, 5083 Al | Carbon steel, Ti alloys |
| **GH2 Piping (< 35 MPa)** | 316L SS, 304L SS | 6061 Al | Carbon steel |
| **Valves (Body)** | 316 SS | CF8M (cast 316 SS) | Carbon steel |
| **Valve Seats** | PTFE, PCTFE | Monel 400 | Viton (for LH2) |
| **Gaskets** | Spiral-wound graphite, PTFE | Metal C-ring | Fiber-based |
| **Fasteners** | 316 SS, A286 | Inconel 718 | Carbon steel |
| **Hoses (Inner)** | 316L SS corrugated | PTFE-lined | Rubber (for LH2) |
| **Seals/O-Rings** | PTFE, PCTFE | Kalrez | Viton (for LH2), Buna-N |
| **Structural Supports** | 6061 Al, 304 SS | G-10 fiberglass | Carbon steel (if H2-exposed) |

## 12. Cross-References

- **Parent Document**: [03-00-06_Engineering](../00_INDEX.md)
- **Related H2 GSE Engineering**: 
  - [03-00-06-02-01A_LH2_Fueling_GSE_Design](./03-00-06-02-01A_LH2_Fueling_GSE_Design.md)
  - [03-00-06-02-02A_Cryogenic_GSE_Requirements](./03-00-06-02-02A_Cryogenic_GSE_Requirements.md)
  - [03-00-06-02-03A_H2_Safety_Systems_Design](./03-00-06-02-03A_H2_Safety_Systems_Design.md)
- **GSE Design Standards**: [03-00-06-01-01A_GSE_Design_Standards](../03-00-06-01_GSE_Design_Requirements/03-00-06-01-01A_GSE_Design_Standards.md)

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-06-02-04A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Engineering & Certification WG

---
