# 10-00-09-14A Cryogenic Material Processing Specification

## Document Information

- **Document ID**: 10-00-09-14A
- **Title**: Cryogenic Material Processing Specification
- **Version**: 1.0 (Revision A)
- **Date**: 2025-12-10
- **Status**: Draft
- **Category**: Process Specification - Material Processing
- **ATA Chapter**: 10 - Parking, Mooring, Storage & RTS

## Purpose

This specification defines material selection, processing, and quality requirements for components intended for cryogenic service at liquid hydrogen temperatures (-253°C / -423°F / 20 K).

## Scope

Covers all metallic and non-metallic materials used in cryogenic components including:
- Pressure vessels and piping
- Structural supports and brackets
- Thermal breaks and insulators
- Seals and gaskets

## Material Selection Criteria

### Metallic Materials for -253°C Service

Materials must meet these criteria:
1. **No Ductile-to-Brittle Transition** above -253°C
2. **Adequate Fracture Toughness**: Charpy impact ≥20 ft-lbs at -196°C minimum
3. **Weldability**: Can be welded without loss of cryogenic properties
4. **Thermal Expansion**: Compatible with mating materials

### Approved Metallic Materials

| Material | Specification | Min. Charpy at -196°C | Typical Applications |
|----------|---------------|------------------------|----------------------|
| 316L SS | AMS 5507 | 35 ft-lbs (47 J) | Piping, vessels, fittings |
| 304L SS | AMS 5511 | 30 ft-lbs (41 J) | General structure |
| 5083-H321 Al | AMS 4057 | 20 ft-lbs (27 J) | Tanks, lightweight structure |
| Inconel 718 | AMS 5662 | 15 ft-lbs (20 J) | High-stress components |
| Copper (OFHC) | ASTM B170 | N/A (ductile FCC) | Heat sinks, high conductivity |

**Prohibited Materials**:
- Carbon steels (ferritic, martensitic - brittle at cryogenic temps)
- Cast iron (brittle at room temperature, worse at cryo)
- Brass (some compositions brittle at cryo)

### Non-Metallic Materials

| Material | Max Service Temp | Thermal Conductivity | Applications |
|----------|------------------|----------------------|--------------|
| G-10 Fiberglass-Epoxy | -269°C | 0.3 W/m·K | Thermal breaks, electrical insulation |
| PTFE (Teflon) | -270°C | 0.25 W/m·K | Seals, gaskets |
| PEEK | -250°C | 0.25 W/m·K | Bushings, wear surfaces |

## Material Testing and Qualification

### Charpy V-Notch Impact Test

**Standard**: ASTM E23

**Test Requirements**:
- **Test Temperature**: -196°C (liquid nitrogen bath) minimum
  - For critical applications, test at -253°C (liquid hydrogen/helium)
- **Specimen**: Standard Charpy V-notch (10 mm × 10 mm × 55 mm)
- **Number of Tests**: Minimum 3 specimens per heat lot
- **Acceptance Criteria**: 
  - Structural components: ≥20 ft-lbs (27 J)
  - Pressure vessels per ASME: Varies by code, typically ≥15 ft-lbs (20 J)

**Test Procedure**:
1. Machine test specimens per ASTM E23
2. Immerse in liquid nitrogen (-196°C) for ≥5 minutes
3. Transfer specimen to test machine within 5 seconds
4. Perform impact test
5. Record absorbed energy and fracture appearance

### Tensile Test at Cryogenic Temperature

**Standard**: ASTM E8 (Tension Testing of Metallic Materials)

**Test Requirements**:
- **Test Temperature**: -196°C or -253°C
- **Specimens**: Per ASTM E8 (round or flat tensile specimens)
- **Number of Tests**: Minimum 2 specimens per heat lot
- **Measurements**: Yield strength, ultimate strength, elongation, reduction of area

**Acceptance Criteria**:
- Yield and ultimate strength meet or exceed specification
- Elongation ≥10% (austenitic SS typically >30%)

### Thermal Cycling Test

**Purpose**: Verify material can withstand repeated thermal cycling without degradation

**Test Procedure**:
1. Cool specimen to -253°C (liquid hydrogen or helium bath)
2. Hold for 15-30 minutes
3. Warm to ambient temperature (+20°C)
4. Repeat for specified cycles (typically 10-100 cycles)
5. Inspect for cracks, delamination, dimensional changes
6. Perform Charpy impact test on cycled specimens vs. non-cycled (compare)

**Acceptance Criteria**:
- No visible cracks or delamination
- Dimensional changes <0.1%
- Impact energy >90% of non-cycled specimens

## Material Processing

### Machining

**Tool Selection**:
- Carbide or high-speed steel tools
- Sharp cutting edges (dull tools work-harden austenitic stainless steels)

**Cutting Parameters** (for austenitic SS):
- Low speeds, high feeds (to minimize work hardening)
- Ample coolant (to control temperature)

**Surface Finish**:
- Critical sealing surfaces: ≤16 μin Ra (0.4 μm Ra)
- Structural surfaces: ≤63 μin Ra (1.6 μm Ra)

### Stress Relief

**Purpose**: Reduce residual stresses from forming, machining, or welding

**Procedure** (for austenitic stainless steel):
- **Temperature**: 1600-1800°F (870-980°C)
- **Time**: 30 minutes to 2 hours (depends on section thickness)
- **Atmosphere**: Inert (argon) or vacuum (to prevent oxidation)
- **Cooling**: Furnace cool or air cool (slow cooling preferred)

**Note**: Stress relief does NOT restore toughness lost by sensitization; use solution annealing for that.

### Solution Annealing

**Purpose**: Restore corrosion resistance and cryogenic toughness in austenitic stainless steels

**Procedure**:
- **Temperature**: 1900-2100°F (1040-1150°C)
- **Time**: 5-15 minutes at temperature (depends on section thickness)
- **Atmosphere**: Inert or vacuum
- **Cooling**: **Rapid quench** in water or polymer quench (critical to prevent sensitization)

**Effect**:
- Dissolves chromium carbides (eliminates sensitization)
- Restores uniform microstructure
- Maximizes corrosion resistance and cryogenic toughness

### Forming and Bending

**Austenitic Stainless Steels**:
- Can be cold-formed (work hardening occurs)
- For tight radii, may need to solution anneal after forming

**Aluminum Alloys**:
- 5083 in H321 temper can be formed with moderate bends
- Sharp bends may require annealing to O-temper first, then re-temper

**Avoid**:
- Cold working below -50°C (risk of cracking)

## Welding for Cryogenic Service

See detailed specification: [10-00-09-13A_H2_Compatible_Welding.md](10-00-09-13A_H2_Compatible_Welding.md)

**Key Requirements**:
- Weld procedure qualified with Charpy impact test of weld and HAZ at -196°C
- Post-weld solution annealing recommended for austenitic SS (to restore toughness)
- 100% radiographic and leak testing of pressure boundaries

## Surface Treatment

### Passivation (Stainless Steel)

**Purpose**: Remove free iron, enhance corrosion resistance

**Procedure**: Per ASTM A380 or AMS 2700
- Nitric acid or citric acid bath
- Post-treatment DI water rinse and dry

### Cleaning

**Cryogenic Cleanliness**:
- Remove all oils, greases, and particulates
- Solvent cleaning (isopropyl alcohol or approved cleaner)
- Ultrasonic cleaning for complex geometries
- Verify cleanliness before assembly

## Quality Control

### Material Certification

**Required Documentation**:
- Mill test reports (MTRs) with:
  - Chemical composition
  - Mechanical properties (room temperature)
  - Heat treatment history
  - Heat lot number
- **Cryogenic Impact Data**: Charpy impact at -196°C for each heat lot

### Traceability

- **Heat Lot Traceability**: Each component marked with heat lot number
- **Material Certifications**: Retained permanently
- **Cryogenic Test Data**: Retained permanently

### Inspection

- **Visual Inspection**: 100% for surface defects, cleanliness
- **Dimensional Inspection**: Per drawing requirements
- **NDT**: Liquid penetrant or magnetic particle for high-stress areas
- **Cryogenic Performance Testing**: Thermal cycling and/or heat leak testing (for assemblies)

## Safety Requirements

### Cryogenic Handling Hazards

- **Extreme Cold**: -253°C causes instant frostbite
- **Asphyxiation**: Vaporized cryogen displaces oxygen
- **Material Embrittlement**: Many materials become brittle
- **Pressure Build-Up**: Vaporization creates high pressure in closed systems

### Personal Protective Equipment

- Cryo gloves (loose-fitting for quick removal)
- Face shield over safety glasses
- Insulated apron or lab coat
- Closed-toe shoes, long pants

### Work Area Controls

- Adequate ventilation
- Oxygen monitoring (<19.5% O2 is IDLH)
- Eyewash/safety shower within 10 seconds
- Warning signs posted

## References

- [10-00-09-01A_Master_Manufacturing_Plan.md](../manufacturing-plans/10-00-09-01A_Master_Manufacturing_Plan.md)
- [10-00-09-05A_Cryo_Components_Manufacturing.md](../manufacturing-plans/10-00-09-05A_Cryo_Components_Manufacturing.md)
- [10-00-09-13A_H2_Compatible_Welding.md](10-00-09-13A_H2_Compatible_Welding.md)
- ASTM E23: Charpy Impact Testing
- ASTM E8: Tensile Testing
- ISO 13984: Liquid Hydrogen - Land Vehicle Fuel Tanks
- ASME Section VIII: Pressure Vessel Code

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-10

---
