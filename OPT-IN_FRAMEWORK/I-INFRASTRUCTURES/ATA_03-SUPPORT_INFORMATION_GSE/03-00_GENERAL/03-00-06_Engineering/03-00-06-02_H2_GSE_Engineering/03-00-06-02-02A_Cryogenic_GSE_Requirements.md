---
Title: "Cryogenic GSE Requirements — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-06-02-02A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Cryogenic engineering requirements for Ground Support Equipment handling Liquid Hydrogen (LH2) at -253°C."
Keywords: ["ATA 03","GSE","Cryogenic","LH2","Hydrogen","Thermal","Insulation"]
Compliance:
  - "ATA iSpec 2200"
  - "ASME B31.12"
  - "NASA-STD-8719.17"
  - "CGA G-5.4"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Parent: "../00_INDEX.md"
  Related: "./03-00-06-02-01A_LH2_Fueling_GSE_Design.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-00-06-02-02A — Cryogenic GSE Requirements

## 1. Purpose

This document defines the **cryogenic engineering requirements** for Ground Support Equipment (GSE) that handles Liquid Hydrogen (LH2) at its boiling point of -253°C (20 Kelvin, -423°F). Operating at this extreme temperature requires specialized design considerations for thermal management, material selection, and safety.

## 2. Scope

This document covers:

- **Thermal design**: insulation, heat leak calculations, boil-off management
- **Material behavior at cryogenic temperatures**
- **Thermal stress and contraction**
- **Vacuum systems for insulation**
- **Cryogenic component selection**: valves, seals, instrumentation
- **Safety considerations specific to cryogenic operations**

This applies to all LH2 GSE including refueling trucks, hydrant systems, transfer lines, and storage vessels.

## 3. Applicable Documents

- [ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines) — Hydrogen Piping and Pipelines
- [CGA G-5.4](https://www.cganet.com/) — Standard for Hydrogen Piping Systems at Consumer Locations
- [NASA-STD-8719.17](https://standards.nasa.gov/) — Safety Standard for Hydrogen and Hydrogen Systems
- [CGA P-12](https://www.cganet.com/) — Safe Handling of Cryogenic Liquids
- [ISO 21013](https://www.iso.org/standard/73699.html) — Cryogenic Vessels (Parts 1-3)
- [ASME Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-rules-construction-pressure-vessels) — Pressure Vessel Code

## 4. Cryogenic Properties of Liquid Hydrogen

### 4.1 Physical Properties

| Property | Value | Notes |
|----------|-------|-------|
| **Boiling Point** | -253°C (20.28 K, -423°F) at 1 atm | Coldest cryogenic fuel except helium |
| **Density (Liquid)** | 70.8 kg/m³ at NBP | Very low density (cf. LNG 423 kg/m³, Jet-A 804 kg/m³) |
| **Latent Heat of Vaporization** | 445.6 kJ/kg | High energy required to vaporize |
| **Specific Heat (Liquid)** | 9.7 kJ/(kg·K) | Temperature change per unit energy |
| **Thermal Conductivity (Liquid)** | 0.1 W/(m·K) | Low, but still conducts heat |
| **Viscosity (Liquid)** | 13 μPa·s | Very low viscosity (flows easily) |
| **Thermal Expansion Coefficient** | 0.016 /K | Volume change with temperature |

### 4.2 Comparison with Other Cryogens

| Cryogen | Boiling Point | Density (kg/m³) | Typical Application |
|---------|---------------|-----------------|---------------------|
| **Helium (He)** | -269°C (4 K) | 124.8 | Scientific research, superconductors |
| **Hydrogen (H2)** | -253°C (20 K) | 70.8 | Rocket fuel, aircraft fuel (AMPEL360) |
| **Neon (Ne)** | -246°C (27 K) | 1,207 | Specialty applications |
| **Nitrogen (N2)** | -196°C (77 K) | 808 | Industrial, food freezing |
| **Oxygen (O2)** | -183°C (90 K) | 1,141 | Medical, industrial |
| **Natural Gas (LNG)** | -162°C (111 K) | 423 | Energy, shipping fuel |

**Key Insight**: LH2 is second only to helium in coldness, requiring the most extreme cryogenic engineering.

## 5. Thermal Design and Insulation

### 5.1 Heat Leak Sources

Heat leak into LH2 systems causes boil-off (evaporation), which:
- Reduces fuel inventory
- Increases tank pressure
- Wastes energy

| Heat Leak Path | Contribution | Mitigation |
|----------------|--------------|------------|
| **Conduction** (through supports, piping) | 30-50% | Use low-conductivity materials (G10 fiberglass, stainless steel vs. aluminum); minimize cross-section |
| **Radiation** (from warm surfaces) | 30-40% | Multi-layer insulation (MLI) or reflective surfaces |
| **Convection** (gas flow in insulation space) | 10-20% | Evacuate insulation space to high vacuum (< 10⁻⁴ mbar) |
| **Conduction through Liquid/Gas** | 10-20% (in vacuum loss) | Maintain vacuum integrity |

### 5.2 Insulation Types

| Insulation Type | Description | Performance (W/m²) | Application |
|-----------------|-------------|---------------------|-------------|
| **Multi-Layer Insulation (MLI)** | 30-60 layers of aluminized Mylar or Dacron with spacer material (fiberglass or silk net) | 0.1-0.5 W/m² | LH2 tanks, vacuum-jacketed piping |
| **Vacuum Insulation (no MLI)** | Evacuated space only (mirror finish surfaces) | 1-3 W/m² | Simple systems, short-term storage |
| **Foam Insulation** | Polyurethane or polyisocyanurate foam + vapor barrier | 5-10 W/m² | Non-vacuum systems (less efficient, but simpler) |
| **Perlite Powder** | Evacuated perlite (silicate mineral) | 2-5 W/m² | Large storage tanks (lower cost than MLI) |

**AMPEL360 Standard**: Use MLI with high vacuum for mobile refueling trucks and aircraft tanks; foam insulation acceptable for short-term transfer lines if vacuum maintenance is impractical.

### 5.3 Heat Leak Calculation

Heat leak (Q) is calculated using:

**Q = (k · A · ΔT) / L**

Where:
- **k** = thermal conductivity of insulation or support material (W/(m·K))
- **A** = cross-sectional area (m²)
- **ΔT** = temperature difference (K) (typically 273K from ambient to LH2)
- **L** = insulation thickness or length (m)

**Example**: 40,000 L LH2 tank with surface area 50 m², MLI insulation 50mm thick, k = 0.001 W/(m·K):

Q = (0.001 × 50 × 273) / 0.05 = **273 W** = **23.6 MJ/day**

Boil-off rate = Q / (ρ × V × Lv) = 23.6 MJ/day / (70.8 kg/m³ × 40 m³ × 445.6 kJ/kg) = **0.47% per day**

**Target**: Boil-off < 0.5% per day for mobile tanks, < 0.2% per day for stationary bulk storage.

## 6. Material Behavior at Cryogenic Temperatures

### 6.1 Material Selection Criteria

| Property | Requirement at -253°C | Test Method |
|----------|------------------------|-------------|
| **Ductility** | > 20% elongation at fracture | ASTM E8 (tensile test at -196°C or -253°C) |
| **Fracture Toughness** | > 50 MPa√m (KIC) | ASTM E399 (fracture toughness at cryogenic temp) |
| **Thermal Contraction** | Coefficient of thermal expansion (CTE) known and accounted for in design | ASTM E831 |
| **Hydrogen Compatibility** | No embrittlement after H2 exposure | ASTM G142 (slow strain rate tensile test) |

### 6.2 Approved Materials for LH2 Service

#### 6.2.1 Metallic Materials

| Material | Application | Advantages | Disadvantages |
|----------|-------------|------------|---------------|
| **Austenitic Stainless Steel (304, 304L, 316, 316L)** | Tanks, piping, valves, fittings | Excellent ductility at cryogenic temp, non-magnetic, widely available | Higher cost than carbon steel |
| **Aluminum Alloys (5083, 6061)** | Tanks, structural supports (aerospace heritage) | Lightweight, good cryogenic properties, higher thermal conductivity than SS | Lower strength than SS, requires thicker walls |
| **Nickel Alloys (Inconel 718, Monel 400)** | High-stress components, seals | Exceptional cryogenic toughness | Expensive, heavy |
| **Copper** | Heat exchangers, electrical conductors | High thermal and electrical conductivity | Soft, limited structural use |

**Avoid**: Carbon steel (brittle at -253°C), cast iron, most plastics (except specific cryogenic grades).

#### 6.2.2 Non-Metallic Materials

| Material | Application | Notes |
|----------|-------------|-------|
| **PTFE (Teflon)** | Seals, gaskets, valve seats | Remains flexible at -253°C |
| **PCTFE (Kel-F)** | Seals, O-rings | Better mechanical properties than PTFE at cryogenic temp |
| **PEEK (Polyetheretherketone)** | Bushings, insulators | Maintains strength at -253°C |
| **G-10 Fiberglass Epoxy** | Insulating supports, structural | Low thermal conductivity, high strength |
| **Graphite (Spiral-Wound)** | Gaskets (high-pressure flanges) | Flexible, conformable, cryogenic compatible |
| **Aramid Fiber (Kevlar)** | Reinforcement in composite tanks | High strength-to-weight ratio |

### 6.3 Thermal Contraction

All materials contract when cooled. Thermal contraction from ambient (20°C) to LH2 temperature (-253°C) is approximately:

| Material | Linear Contraction (ΔL/L) | Example: 10m pipe contracts by: |
|----------|----------------------------|----------------------------------|
| **Stainless Steel 316** | 0.42% | 42 mm (1.65 inches) |
| **Aluminum 6061** | 0.59% | 59 mm (2.3 inches) |
| **G-10 Fiberglass (axial)** | 0.25% | 25 mm (1 inch) |

**Design Implications**:
- Piping must have expansion joints, bellows, or flexible sections
- Flange bolt-up must allow for differential contraction
- Supports must accommodate movement (sliding supports or flexible hangers)

## 7. Vacuum Systems for Insulation

### 7.1 Vacuum Requirements

| System | Vacuum Level | Purpose |
|--------|--------------|---------|
| **MLI Effectiveness** | < 10⁻⁴ mbar (< 0.1 Pa) | Eliminate convective heat transfer, maximize MLI performance |
| **Simple Vacuum** | 10⁻² - 10⁻³ mbar | Adequate for short-term or less critical applications |
| **Degraded Vacuum** | > 10⁻³ mbar | Reduced insulation performance, increased boil-off |

### 7.2 Vacuum System Components

| Component | Function | Specification |
|-----------|----------|---------------|
| **Vacuum Pump** | Evacuate insulation space during manufacturing | Turbomolecular or diffusion pump, backed by roughing pump |
| **Getter Material** | Absorb residual gases over time (maintain vacuum) | Activated charcoal or metal getters (Ba, Ti) at cryogenic temp |
| **Vacuum Gauge** | Monitor vacuum level | Pirani or cold cathode gauge, 10⁻⁶ to 10⁰ mbar range |
| **Seal-Off Port** | Seal vacuum space after evacuation | Pinch-off tube welded shut or valve with metal seal |

### 7.3 Vacuum Loss Detection

| Symptom | Cause | Action |
|---------|-------|--------|
| **Increased Boil-Off Rate** | Vacuum degradation (leak or outgassing) | Monitor vacuum gauge; re-evacuate if > 10⁻³ mbar |
| **Frost on Outer Jacket** | Vacuum lost, moisture condensing | Immediate re-evacuation or tank withdrawal from service |
| **Tank Pressure Rise Faster Than Expected** | Insulation failure | Investigate, repair, and pressure test |

## 8. Cryogenic Component Selection

### 8.1 Valves

| Valve Type | Application | Cryogenic Design Features |
|------------|-------------|---------------------------|
| **Ball Valve** | Isolation, on/off service | Extended bonnet to keep stem seal above cryogenic zone; austenitic SS or Al body |
| **Globe Valve** | Throttling, flow control | Long bonnet, bellows seal to prevent leakage |
| **Check Valve** | Prevent backflow | Spring-loaded or swing check; materials compatible with -253°C |
| **Relief Valve** | Overpressure protection | Stainless steel body, PTFE or metal seats, set pressure per ASME Section VIII |

**Key Requirement**: All valves must be tested at cryogenic temperature (liquid nitrogen bath at -196°C minimum) before LH2 service.

### 8.2 Seals and Gaskets

| Seal Type | Application | Temperature Range |
|-----------|-------------|-------------------|
| **PTFE (Teflon)** | Valve stem seals, static seals | -253°C to +260°C |
| **PCTFE (Kel-F)** | O-rings, dynamic seals | -240°C to +200°C |
| **Metal C-Ring** | High-pressure flanges | -269°C to +800°C (most robust) |
| **Spiral-Wound Graphite** | Flange gaskets | -200°C to +800°C (conformable) |
| **Indium Wire** | Ultra-high vacuum seals | -269°C to +150°C (soft metal, re-usable) |

### 8.3 Instrumentation

| Instrument | Cryogenic Requirement | Example |
|------------|------------------------|---------|
| **Temperature Sensor** | Platinum RTD (Pt-100 or Pt-1000) or Silicon diode | Calibrated for -253°C |
| **Pressure Gauge** | Diaphragm seal with glycerin fill; or strain gauge | Bourdon tube not suitable (freezes) |
| **Level Gauge** | Differential pressure or capacitance probe | Submerged sensor must withstand thermal cycling |
| **Flow Meter** | Coriolis or turbine meter (cryogenic version) | Wetted parts in stainless steel |

## 9. Thermal Stress and Design for Thermal Cycling

### 9.1 Thermal Stress Analysis

Thermal stress arises from:
1. **Temperature gradients** during cool-down or warm-up
2. **Constrained contraction** (components fixed at both ends)
3. **Differential contraction** between dissimilar materials

Thermal stress (σ) is approximately:

**σ = E × α × ΔT**

Where:
- **E** = Young's modulus (GPa) (e.g., 193 GPa for SS 316 at -253°C)
- **α** = coefficient of thermal expansion (/K) (e.g., 16×10⁻⁶ /K for SS 316 avg from 20°C to -253°C)
- **ΔT** = temperature change (K)

**Example**: SS 316 pipe constrained at both ends, cooled from 20°C to -253°C:

σ = 193 × 10⁹ Pa × 16×10⁻⁶ /K × 273 K = **842 MPa**

This exceeds yield strength (~200 MPa at -253°C), so the pipe will yield or buckle unless free to contract.

**Solution**: Use expansion joints, bellows, or sliding supports.

### 9.2 Design for Thermal Cycling

LH2 GSE undergoes repeated thermal cycles (ambient → cryogenic → ambient).

| Design Feature | Purpose |
|----------------|---------|
| **Expansion Joints** | Accommodate thermal contraction in piping (bellows-type, rated for cryogenic) |
| **Flexible Hoses** | Allow for movement and misalignment |
| **Sliding Supports** | Permit pipe movement while supporting weight |
| **Low-Cycle Fatigue Analysis** | Ensure welds and high-stress areas survive 10,000+ cycles (per ASME VIII-2) |

## 10. Safety Considerations for Cryogenic Operations

### 10.1 Cryogenic Hazards

| Hazard | Risk | Protection |
|--------|------|------------|
| **Skin/Eye Contact** | Instant frostbite, severe tissue damage | Cryogenic gloves (cryo-rated to -253°C), face shield, long sleeves |
| **Cold Burn from Metal** | Touching cold metal causes instant freeze injury | Insulate or cover all accessible cold surfaces; warning labels |
| **Embrittlement of Materials** | Non-cryogenic materials become brittle and fracture | Use only approved cryogenic materials |
| **Oxygen Enrichment** | If LH2 vents in enclosed space, air liquefies and O2 concentration increases (fire risk) | Vent to well-ventilated area; O2 monitors in confined spaces |
| **Asphyxiation** | Hydrogen displaces oxygen | H2 is lighter than air, rises; ensure ventilation |

### 10.2 Personal Protective Equipment (PPE)

| PPE Item | Specification | Application |
|----------|---------------|-------------|
| **Cryogenic Gloves** | Insulated to -253°C, loose-fitting (can be quickly removed if liquid spills inside) | Mandatory when handling LH2 connections |
| **Face Shield** | Full-face polycarbonate shield | Protect against LH2 splash during connect/disconnect |
| **Safety Glasses** | Underneath face shield | Secondary eye protection |
| **Long Sleeves and Pants** | Cotton or Nomex (not synthetic, which melts) | Cover all skin |
| **Steel-Toe Boots** | With metatarsal guard | Protect from dropped cryogenic components |
| **Apron** | Cryogenic-rated (aluminized or Kevlar) | For high-splash-risk tasks |

### 10.3 Operating Procedures

| Procedure | Safety Requirement |
|-----------|---------------------|
| **Pre-Cool Slowly** | Cool equipment gradually (10-20°C/min) to avoid thermal shock |
| **Vent Safely** | Vent hydrogen releases to >3m above equipment, away from ignition sources |
| **No Water Contact** | Never spray water on cryogenic equipment (causes violent boiling and ice formation) |
| **Monitor Oxygen** | Use O2 monitors in enclosed areas; evacuate if O2 < 19.5% by volume |

## 11. Cryogenic Testing and Qualification

### 11.1 Component Qualification Tests

All cryogenic components shall be tested:

| Test | Method | Acceptance Criteria |
|------|--------|---------------------|
| **Cryogenic Cycle Test** | Cycle component 10 times: ambient → LN2 (-196°C) → ambient | No cracks, leaks, or loss of function |
| **Pressure Test at Cryogenic Temp** | Pressurize to 1.5× MAWP with LN2 or cold GHe | No leakage, deformation, or failure |
| **Leak Test** | Helium leak test at ambient and cryogenic temp | < 10⁻⁶ mbar·L/s (for critical components) |
| **Insulation Performance Test** | Measure boil-off rate over 48 hours | Meet design boil-off target (e.g., < 0.5%/day) |

### 11.2 System-Level Tests

| Test | Description | Purpose |
|------|-------------|---------|
| **Cool-Down Test** | Fill empty tank with LH2, measure cool-down time and initial boil-off | Validate thermal design |
| **Hold Time Test** | Fill tank, seal, and measure pressure rise rate over 7 days | Confirm insulation performance and leak tightness |
| **Thermal Cycling** | Perform 50 fill/empty cycles, inspect for cracks and leaks | Demonstrate durability |

## 12. Cross-References

- **Parent Document**: [03-00-06_Engineering](../00_INDEX.md)
- **Related H2 GSE Engineering**: 
  - [03-00-06-02-01A_LH2_Fueling_GSE_Design](./03-00-06-02-01A_LH2_Fueling_GSE_Design.md)
  - [03-00-06-02-03A_H2_Safety_Systems_Design](./03-00-06-02-03A_H2_Safety_Systems_Design.md)
  - [03-00-06-02-04A_H2_GSE_Materials](./03-00-06-02-04A_H2_GSE_Materials.md)
- **Environmental Requirements**: [03-00-06-01-03A_Environmental_Requirements](../03-00-06-01_GSE_Design_Requirements/03-00-06-01-03A_Environmental_Requirements.md)
- **GSE Safety**: [03-00-02_Safety](../../03-00-02_Safety/)

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-06-02-02A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Engineering & Certification WG

---
