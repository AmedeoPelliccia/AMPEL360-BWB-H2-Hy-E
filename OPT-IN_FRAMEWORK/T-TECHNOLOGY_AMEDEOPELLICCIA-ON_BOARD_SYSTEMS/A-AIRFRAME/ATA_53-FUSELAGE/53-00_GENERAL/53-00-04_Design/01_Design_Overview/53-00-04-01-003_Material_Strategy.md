# 53-00-04-01-003: Material Strategy – AMPEL360 BWB Fuselage

## 1. Overview

This document defines the material selection strategy for the AMPEL360 BWB fuselage structure. The strategy balances structural performance, weight efficiency, manufacturability, cost, and sustainability.

## 2. Material Selection Philosophy

### 2.1 Guiding Principles
- **Proven Materials**: Use materials with established aerospace qualification
- **Right Material, Right Place**: Match material properties to load requirements
- **Weight Optimization**: Minimize structural weight while meeting safety requirements
- **Manufacturability**: Consider production constraints in material selection
- **Sustainability**: Prefer recyclable and environmentally friendly materials
- **Cost-Effectiveness**: Balance performance with lifecycle cost

### 2.2 Material Selection Process
1. Define functional requirements (loads, environment, durability)
2. Identify candidate materials
3. Evaluate performance vs. weight vs. cost
4. Consider manufacturing and assembly
5. Assess availability and supply chain
6. Verify certification basis
7. Document selection rationale

## 3. Primary Structural Materials

### 3.1 Carbon Fiber Reinforced Polymer (CFRP)

**Applications**:
- Primary structure skins (upper and lower shells)
- Wing spars and ribs
- Primary frames and bulkheads
- Doors and access panels

**Material Systems**:
- **IM7/8552**: High-strength, toughened epoxy system
  - Use: Primary load-bearing structure
  - Fiber: Intermediate modulus carbon
  - Resin: Toughened epoxy (improved damage tolerance)
  - Form: Unidirectional tape, fabric
  
- **T800/3900**: High-performance system for critical areas
  - Use: Wing spars, critical fittings
  - Fiber: High-strength carbon
  - Resin: Toughened epoxy
  - Form: Unidirectional tape

**Properties**:
- High specific strength and stiffness
- Excellent fatigue resistance
- Low thermal expansion
- Corrosion resistance

**Considerations**:
- Moisture absorption (requires environmental conditioning)
- Lightning strike protection (copper mesh/foil)
- Impact damage susceptibility (design for)
- Quality control in manufacturing (critical)

**Standards**:
- ASTM D3039 (Tensile testing)
- ASTM D7137/D7136 (CAI - Compression After Impact)
- Qualified per EASA/FAA requirements

### 3.2 Glass Fiber Reinforced Polymer (GFRP)

**Applications**:
- Secondary structure
- Fairings and non-load-bearing panels
- Radome structure
- Interior panels

**Material Systems**:
- **S-Glass/Epoxy**: For higher-performance secondary structure
- **E-Glass/Epoxy**: Cost-effective for non-critical components

**Properties**:
- Lower cost than CFRP
- Good electrical insulation (radome applications)
- Moderate specific strength
- Excellent corrosion resistance

**Considerations**:
- Heavier than CFRP for same strength
- Lower stiffness
- Good for electromagnetic transparency

### 3.3 Aluminum Alloys

**Applications**:
- Floor beams and subfloor structure
- Seat tracks
- Secondary fittings and brackets
- Cargo liner panels
- Access panels

**Alloy Systems**:
- **7075-T6**: High-strength applications
  - Ultimate tensile strength: ~570 MPa
  - Use: Fittings, high-load attachments
  
- **2024-T3**: Good fatigue resistance
  - Use: Floor beams, subfloor structure
  - Ultimate tensile strength: ~470 MPa
  
- **6061-T6**: Moderate strength, excellent formability
  - Use: Brackets, clips, secondary structure
  - Ultimate tensile strength: ~310 MPa

**Properties**:
- Well-established material database
- Good damage tolerance
- Easy inspection and repair
- Established manufacturing processes

**Considerations**:
- Corrosion protection required (anodizing, primer, paint)
- Galvanic corrosion risk with CFRP (require isolation)
- Higher density than composites

**Standards**:
- AMS specifications (e.g., AMS 4045 for 2024-T3)
- ASTM B557 (Tensile testing)

### 3.4 Titanium Alloys

**Applications**:
- Landing gear attachment fittings
- High-load transfer fittings
- Gear bay structure (fire resistance)
- CFRP-to-metal transition joints
- High-temperature areas

**Alloy Systems**:
- **Ti-6Al-4V (Grade 5)**: Primary titanium alloy
  - Ultimate tensile strength: ~900 MPa (annealed)
  - Use: Fittings, bushings, high-load attachments
  - Excellent strength-to-weight ratio
  
- **Ti-6Al-2Sn-4Zr-2Mo (Ti-6242)**: Elevated temperature applications
  - Use: Areas with higher operating temperatures

**Properties**:
- Excellent specific strength
- Corrosion resistance (no treatment needed)
- Compatible with CFRP (no galvanic issues)
- High melting point
- Good fatigue resistance

**Considerations**:
- High material and machining cost
- Specialized manufacturing processes
- Requires careful machining (work hardening)

**Standards**:
- AMS 4928 (Ti-6Al-4V bar)
- ASTM B265 (Ti sheet)

### 3.5 Steel Alloys

**Applications**:
- High-load fasteners (bolts, nuts)
- Landing gear trunnion pins
- Selected bushings and inserts

**Alloy Systems**:
- **300M Steel**: Ultra-high-strength steel
  - Ultimate tensile strength: ~1900 MPa
  - Use: Landing gear fittings
  
- **PH 13-8 Mo (Stainless)**: Corrosion-resistant high-strength
  - Use: Bushings, pins
  - Ultimate tensile strength: ~1500 MPa

**Properties**:
- Very high strength
- Cost-effective for small components
- Established fastener supply chain

**Considerations**:
- High density
- Corrosion protection (except stainless)
- Limited to small, high-load components

## 4. Hybrid and Sandwich Materials

### 4.1 Composite Sandwich Panels

**Applications**:
- Floor panels
- Interior panels
- Access doors
- Non-primary structure panels

**Configuration**:
- **Facesheets**: CFRP or GFRP
- **Core**: Honeycomb (Nomex, aluminum) or foam

**Advantages**:
- High bending stiffness with low weight
- Good impact resistance
- Sound and thermal insulation

**Considerations**:
- Core crushing under compression
- Moisture ingress (require edge sealing)
- Facesheet-to-core debonding
- Damage inspection more complex

### 4.2 Hybrid Metal-Composite Joints

**Applications**:
- Wing-to-fuselage attachment
- Landing gear beam connections
- High-load transfer areas

**Concepts**:
- **CFRP + Titanium**: Load introduction fittings
- **Co-bonded/Co-cured**: Metal inserts in composite structure
- **Mechanically Fastened**: Bolted metal fittings to composite

**Advantages**:
- Optimal load transfer
- Exploit benefits of both materials
- Proven in Boeing 787, Airbus A350

## 5. Material Allocation by Zone

### 5.1 Zone 100: Nose Section
| Component | Primary Material | Secondary Option |
|-----------|------------------|------------------|
| Frames | CFRP (IM7/8552) | Aluminum 7075 |
| Skins | CFRP (IM7/8552) | N/A |
| Forward bulkhead | CFRP (IM7/8552) | N/A |
| Floor beams | Aluminum 2024-T3 | CFRP |
| Fittings | Titanium Ti-6Al-4V | Steel 300M |

### 5.2 Zone 200: Forward Cabin
| Component | Primary Material | Secondary Option |
|-----------|------------------|------------------|
| Frames | CFRP (IM7/8552) | N/A |
| Skins | CFRP (IM7/8552) | N/A |
| Floor beams | Aluminum 2024-T3 | CFRP |
| Door frames | CFRP + Ti fittings | Aluminum 7075 |
| Seat tracks | Aluminum 6061-T6 | N/A |

### 5.3 Zone 300: Mid Cabin
| Component | Primary Material | Secondary Option |
|-----------|------------------|------------------|
| Frames | CFRP (IM7/8552) | N/A |
| Skins | CFRP (IM7/8552) | N/A |
| Floor beams | Aluminum 2024-T3 | CFRP sandwich |
| Emergency exit frames | CFRP + Ti fittings | N/A |

### 5.4 Zone 400: Center Wing Box (Critical)
| Component | Primary Material | Secondary Option |
|-----------|------------------|------------------|
| Wing spars | CFRP (T800/3900) | IM7/8552 |
| Spar caps | CFRP (T800/3900) | N/A |
| Skins | CFRP (IM7/8552) | N/A |
| Ribs | CFRP (IM7/8552) | N/A |
| Gear bay structure | CFRP + Ti fittings | Titanium |
| Main fittings | Titanium Ti-6Al-4V | Steel 300M |

### 5.5 Zone 500: Aft Cabin
| Component | Primary Material | Secondary Option |
|-----------|------------------|------------------|
| Frames | CFRP (IM7/8552) | N/A |
| Skins | CFRP (IM7/8552) | N/A |
| Floor beams | Aluminum 2024-T3 | CFRP |

### 5.6 Zone 600: Tail Section
| Component | Primary Material | Secondary Option |
|-----------|------------------|------------------|
| Frames | CFRP (IM7/8552) | Aluminum 7075 |
| Skins | CFRP (IM7/8552) | N/A |
| Aft bulkhead | CFRP (IM7/8552) | N/A |
| APU bay structure | Titanium (fire zone) | Aluminum |
| Empennage fittings | Titanium Ti-6Al-4V | Steel |

## 6. Material Properties Database

Detailed material properties are maintained in:
- [../04_Design_Analysis/Global_FEA_Model/53-00-04-04-003_Material_Properties.csv](../04_Design_Analysis/Global_FEA_Model/53-00-04-04-003_Material_Properties.csv)
- Company Materials Handbook
- Supplier material data sheets

## 7. Environmental and Durability Considerations

### 7.1 Operating Environment
- Temperature range: -54°C to +71°C
- Humidity: Up to 100% RH
- Salt spray (coastal operations)
- UV exposure
- Fuel and hydraulic fluid exposure

### 7.2 Material Response
| Material | Key Environmental Factor | Mitigation |
|----------|-------------------------|------------|
| CFRP | Moisture absorption | Protective coatings, design allowables |
| Aluminum | Corrosion | Anodizing, primer, paint |
| Titanium | None (excellent) | N/A |
| Steel | Corrosion | Cadmium plating, stainless alloys |

### 7.3 Fatigue and Damage Tolerance
- CFRP: Excellent fatigue resistance, design for impact damage
- Aluminum: Good fatigue (2024-T3), slow crack growth
- Titanium: Excellent fatigue and crack resistance
- Steel: Very good fatigue in high-strength alloys

## 8. Lightning Strike Protection

### 8.1 CFRP Structure Protection
- **Expanded copper foil** (ECF): 0.005" to 0.010" thick
- **Aluminum mesh**: Bonded to surface
- **Conductive paint**: For non-critical areas
- **Diverter strips**: At panel joints

### 8.2 Design Zones
- **Zone 1A** (initial attachment): Maximum protection (heavy ECF)
- **Zone 1B/C** (swept stroke): Medium protection
- **Zone 2** (intermediate): Light protection
- **Zone 3** (low probability): Minimal protection

**Standard**: [SAE ARP5414](https://www.sae.org/standards/content/arp5414b/) (Lightning Strike Protection)

## 9. Manufacturing Compatibility

### 9.1 CFRP Manufacturing
- **Hand layup**: Small quantities, complex shapes
- **Automated Fiber Placement (AFP)**: Large panels, high production rate
- **Out-of-autoclave (OOA)**: Large components, lower cost
- **Autoclave cure**: Highest quality, existing large autoclaves

### 9.2 Metal Manufacturing
- **Machining**: Aluminum and titanium components
- **Forming**: Aluminum sheet and extrusions
- **Casting**: Titanium fittings (investment casting)

### 9.3 Joining Methods
- **Co-curing**: CFRP to CFRP (primary method)
- **Bonding**: Secondary bonding with adhesives (e.g., FM 300)
- **Mechanical fastening**: Bolts, Hi-Loks, rivets
- **Welding**: Titanium and steel (limited use)

## 10. Sustainability and Recyclability

### 10.1 Material Lifecycle
- **CFRP**: Currently limited recycling; research ongoing
  - Pyrolysis to recover fibers
  - Energy recovery as last resort
- **Aluminum**: Highly recyclable (95% energy savings vs. primary)
- **Titanium**: Recyclable, high scrap value
- **Steel**: Fully recyclable

### 10.2 Sustainable Practices
- Material utilization optimization (minimize scrap)
- Use of recycled aluminum where possible
- Design for disassembly at end-of-life
- Tracking of hazardous materials (REACH, RoHS compliance)

## 11. Supply Chain and Qualification

### 11.1 Material Suppliers (Examples)
- **CFRP Prepreg**: Hexcel, Cytec/Solvay, Toray
- **Aluminum**: Alcoa, Constellium, Kaiser
- **Titanium**: VSMPO-AVISMA, TIMET, ATI
- **Fasteners**: Alcoa Fastening Systems, Arconic

### 11.2 Material Qualification
- All materials qualified per [EASA CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) and [FAA Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25)
- Material specifications: AMS, ASTM, company specs
- Quality control: Incoming inspection, test coupons, certifications
- Traceability: Batch tracking, material certificates

## 12. Cost Considerations

### 12.1 Material Cost Comparison (Relative)
| Material | Raw Material Cost | Processing Cost | Total Cost Index |
|----------|-------------------|-----------------|------------------|
| Aluminum | 1.0 | 1.0 | 1.0 |
| CFRP (prepreg) | 15-20 | 3-5 | 10-15 |
| Titanium | 8-12 | 5-8 | 8-12 |
| GFRP | 3-5 | 2-3 | 2-4 |

**Note**: Cost index is relative to aluminum baseline. CFRP cost justified by weight savings and performance.

### 12.2 Lifecycle Cost
- Include: Material, processing, assembly, inspection, maintenance, disposal
- CFRP higher initial cost, lower maintenance (corrosion resistance)
- Aluminum lower initial cost, periodic corrosion inspection required
- Titanium high cost, but essential for critical fittings

## 13. Future Material Technologies

### 13.1 Under Evaluation
- **Thermoplastic composites**: Faster processing, better damage tolerance
- **Nano-enhanced resins**: Improved toughness
- **3D-printed titanium**: Complex fittings, reduced lead time
- **Variable-stiffness composites**: Optimized fiber paths

### 13.2 Technology Roadmap
- Continuous monitoring of material developments
- Collaboration with material suppliers
- Coupon testing of promising materials
- Potential insertion in later aircraft batches

## 14. Conclusion

The material strategy for the AMPEL360 BWB fuselage leverages proven aerospace materials while optimizing for the unique characteristics of the BWB configuration. CFRP composites form the backbone of the primary structure, with strategic use of aluminum, titanium, and steel for specific applications.

This strategy balances structural performance, weight efficiency, manufacturability, and cost to achieve program objectives while maintaining the highest safety standards.

---

## Document Control

- **Document ID**: 53-00-04-01-003
- **Title**: Material Strategy – AMPEL360 BWB Fuselage
- **Version**: 1.0
- **Date**: 2025-11-22
- **Author**: ATA 53 Chief Design Engineer / Materials Engineering
- **Approval**: _[to be completed]_
- **Status**: DRAFT
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
