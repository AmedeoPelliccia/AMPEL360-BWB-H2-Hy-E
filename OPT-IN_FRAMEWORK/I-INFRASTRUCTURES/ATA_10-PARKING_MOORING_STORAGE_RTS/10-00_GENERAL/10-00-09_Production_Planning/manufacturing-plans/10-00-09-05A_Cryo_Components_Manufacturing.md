# 10-00-09-05A Cryo Components Manufacturing

## Document Information

- **Document ID**: 10-00-09-05A
- **Title**: Cryogenic Components Manufacturing Plan
- **Version**: 1.0 (Revision A)
- **Date**: 2025-12-10
- **Status**: Draft
- **Category**: Manufacturing Plan - Cryogenic Specific
- **ATA Chapter**: 10 - Parking, Mooring, Storage & RTS

## Purpose

This document defines the specialized manufacturing processes, material requirements, and quality controls for cryogenic components used in ATA 10 Parking, Mooring, Storage, and RTS operations for the AMPEL360 BWB-H2 aircraft. These components must operate reliably at liquid hydrogen temperatures (-253°C / -423°F / 20 K) and include insulation systems, thermal breaks, vacuum-jacketed lines, and cryogenic sensors.

## Scope

### Included Components

- **Vacuum-Jacketed Lines**: Double-wall piping for cryogenic fluid transfer during ground operations
- **Thermal Breaks**: G-10 or ceramic insulating components to minimize heat leak
- **Multi-Layer Insulation (MLI)**: Reflective insulation blankets for cryogenic surfaces
- **Cryogenic Valves**: Valves rated for -253°C service
- **Cryogenic Sensors**: Temperature and pressure sensors for LH2 parking operations
- **Support Structures**: Cryogenic-rated brackets and clamps

### Exclusions

- Aircraft onboard cryogenic fuel system (covered under ATA 28)
- Ground LH2 storage tanks (covered under ATA 85)
- Cryogenic refueling equipment design (covered under ATA 03 - GSE)

## Cryogenic Material Requirements

### Material Selection Criteria

Materials for cryogenic service must exhibit:

1. **Adequate Toughness at -253°C**: No brittle fracture
2. **Low Thermal Conductivity**: Minimize heat leak (for insulation and thermal breaks)
3. **Thermal Expansion Compatibility**: Minimize thermal stresses during cool-down and warm-up
4. **Chemical Compatibility**: Resistant to LH2 and cleaning agents
5. **Vacuum Compatibility**: Low outgassing for vacuum-jacketed components

### Approved Cryogenic Materials

#### Metallic Materials

| Material | Specification | Application | Key Properties |
|----------|---------------|-------------|----------------|
| **316L Stainless Steel** | AMS 5507, AMS 5524 | Pressure vessels, piping, fittings | Excellent toughness at -253°C, FCC crystal structure |
| **304L Stainless Steel** | AMS 5511, AMS 5513 | General structures, brackets | Good toughness, lower cost than 316L |
| **5083-H321 Aluminum** | AMS 4057 | Tanks, lightweight structures | Excellent cryogenic toughness, no brittle transition |
| **Inconel 718** | AMS 5662, AMS 5663 | High-stress components | High strength retained at cryogenic temps |
| **Copper (OFHC)** | ASTM B170 | Heat sinks, high-conductivity needs | Very high thermal conductivity |
| **Titanium 6Al-4V** | AMS 4911 | Weight-critical, corrosion-resistant | Good cryogenic properties, lightweight |

**Note**: Carbon steels and ferritic stainless steels are **NOT suitable** for cryogenic service due to ductile-to-brittle transition above -253°C.

#### Non-Metallic Materials

| Material | Application | Key Properties |
|----------|-------------|----------------|
| **G-10 Fiberglass-Epoxy** | Thermal breaks, electrical insulation | Low thermal conductivity (~0.3 W/m·K), high strength |
| **G-11 Fiberglass-Epoxy** | Similar to G-10, higher temperature rating | Low thermal conductivity, dimensionally stable |
| **PTFE (Teflon)** | Seals, gaskets | Flexible at cryogenic temps, low friction |
| **PEEK** | Bushings, wear surfaces | High strength, good cryogenic properties |
| **Aerogel** | Insulation (experimental) | Ultra-low thermal conductivity (~0.015 W/m·K) |

#### Insulation Materials

| Material | Application | Thermal Conductivity | Notes |
|----------|-------------|----------------------|-------|
| **Multi-Layer Insulation (MLI)** | Vacuum-jacketed surfaces | <0.001 W/m·K (in vacuum) | Alternating layers of aluminized mylar and spacer |
| **Polyurethane Foam** | Low-performance insulation | ~0.025 W/m·K | For non-critical areas |
| **Perlite** | Bulk insulation (powder in vacuum) | ~0.003 W/m·K (in vacuum) | Used in large storage tanks |

### Material Testing and Qualification

All cryogenic materials must be tested and qualified for -253°C service:

1. **Charpy V-Notch Impact Test** (per ASTM E23):
   - Test temperature: -196°C (liquid nitrogen) as a minimum
   - Acceptance criteria: ≥20 ft-lbs (27 J) absorbed energy typical for structural components
   - Higher toughness required for pressure vessels per ASME Section VIII

2. **Tensile Test at Cryogenic Temperature** (per ASTM E8):
   - Test at -196°C or -253°C depending on application criticality
   - Verify yield strength, ultimate strength, and elongation meet or exceed specifications

3. **Thermal Cycling Test**:
   - Cycle component between ambient (+20°C) and cryogenic (-253°C)
   - Typical: 10-100 cycles depending on application
   - Inspect for cracks, delamination, dimensional changes

## Manufacturing Processes

### Fabrication and Machining

**General Requirements**:
- Use appropriate cutting tools and speeds/feeds for cryogenic materials
- Avoid work-hardening of austenitic stainless steels (can reduce toughness)
- Deburr and radius all edges to avoid stress concentrations

**Critical Dimensions**:
- Vacuum sealing surfaces: ≤16 μin Ra (0.4 μm Ra)
- O-ring grooves: Per AS568 or Parker O-Ring Handbook
- Thread engagement: Full thread engagement required (no partial threads in load path)

### Welding for Cryogenic Service

All welds on cryogenic components must comply with:
- AWS D17.1 (Aerospace Fusion Welding)
- ASME Section VIII or IX (Pressure Vessels and Piping)
- ISO 13984 (Liquid Hydrogen - Land Vehicle Fuel Tanks)

See detailed cryogenic material processing: [10-00-09-14A_Cryo_Material_Processing.md](../process-specifications/10-00-09-14A_Cryo_Material_Processing.md)

#### Welding Process Summary

**Preferred Welding Methods**:

1. **TIG (GTAW)**: Most common for stainless steel and aluminum
   - Austenitic stainless steels (316L, 304L): ER316L or ER308L filler
   - Aluminum alloys (5083): ER5183 or ER5356 filler
   - Full penetration welds for pressure boundaries
   - Inert gas purge (argon) on back side to prevent oxidation

2. **Electron Beam Welding (EBW)**: For thick sections or dissimilar materials
   - Vacuum environment prevents contamination
   - Deep penetration with narrow heat-affected zone (HAZ)
   - Used for vacuum jackets and complex joints

3. **Laser Welding**: Precision welds, minimal heat input
   - Controlled depth and bead geometry
   - Good for thin-wall components

**Welding Consumables**:
- 316L filler wire (ER316L per AWS A5.9)
- 308L filler wire (ER308L per AWS A5.9)
- Aluminum filler (ER5183 or ER5356 per AWS A5.10)
- Shielding gas: Argon (99.999% purity)

**Post-Weld Treatment**:
- Solution annealing (for austenitic stainless steels): 1900-2100°F, water quench
- Stress relief (for aluminum): 300-350°F for 1-2 hours
- Post-weld cleaning and passivation (per ASTM A380)

#### Weld Inspection

**100% Inspection Required**:
- Visual inspection (per AWS D17.1)
- Liquid penetrant testing (PT) - all accessible weld surfaces
- Radiographic testing (RT) - 100% of pressure boundary welds
- Helium leak testing - all vacuum jackets and pressure boundaries

**Cryogenic Qualification**:
- Weld procedure qualification (WPQ) includes Charpy impact test of weld and HAZ at -196°C
- Production welds use qualified procedures only

### Heat Treatment

Heat treatment of cryogenic components must be performed per:
- AMS 2750 (Pyrometry requirements)
- NADCAP AC7102 (Heat Treatment)

**Common Heat Treatments for Cryogenic Materials**:

| Material | Treatment | Purpose | Temperature | Quench |
|----------|-----------|---------|-------------|--------|
| 316L SS | Solution Anneal | Restore toughness, remove sensitization | 1900-2100°F | Water |
| 304L SS | Solution Anneal | Restore toughness | 1900-2050°F | Water |
| 5083 Al | Stress Relief | Reduce residual stresses | 300-350°F | Air |
| Inconel 718 | Age Hardening | Increase strength | 1325°F + 1150°F | Air |

**Heat Treatment Controls**:
- Furnace qualification per AMS 2750 (typically Class 2, Type C for critical work)
- Thermocouple calibration (NIST-traceable, annual)
- Load thermocouples to verify part temperature uniformity
- Time-temperature recording for traceability

### Multi-Layer Insulation (MLI) Fabrication

MLI is critical for minimizing heat leak in cryogenic systems.

**MLI Construction**:
- **Reflective Layers**: Double-aluminized mylar (typically 0.00025" thick)
- **Spacer Layers**: Polyester netting or fiberglass paper (low contact conductance)
- **Number of Layers**: 10-40 layers depending on application (more layers = better insulation, but diminishing returns)

**Fabrication Process**:
1. **Pattern Development**: Create patterns for complex geometries using templates
2. **Layer Cutting**: Cut reflective and spacer layers to pattern
3. **Assembly**: Layer alternating reflective and spacer materials
4. **Attachment**: Secure MLI with fiberglass tape or low-conductance fasteners
5. **Cleanliness**: Minimize contamination (oils, particulates) that can degrade vacuum

**Quality Control**:
- Layer count verification (count and record layers)
- Wrinkle and gap inspection (wrinkles create conduction paths)
- Attachment inspection (ensure no metal-to-metal contact through MLI)

### Vacuum Jacketing

Vacuum-jacketed components provide insulation by evacuating the space between an inner and outer wall.

**Design Features**:
- **Inner Wall**: Contains cryogenic fluid (316L SS or aluminum)
- **Outer Wall**: Provides structural support and vacuum containment (316L SS)
- **Spacers**: G-10 or ceramic spacers maintain annular gap, minimize conduction
- **Getter**: Activated charcoal or barium getter to absorb residual gases
- **Vacuum Port**: Evacuation and backfill port with pinch-off valve

**Fabrication Process**:
1. **Inner Component Assembly**: Weld inner piping or vessel
2. **Spacer Installation**: Install G-10 or ceramic spacers at regular intervals
3. **Outer Shell Assembly**: Weld outer jacket around inner component
4. **Leak Testing**: Helium leak test all welds (inner and outer) before evacuation
5. **Evacuation**: Evacuate to ≤1×10⁻⁵ torr (or lower for best performance)
6. **Getter Activation**: Heat getter to activate (if used)
7. **Pinch-Off**: Seal vacuum port (pinch-off or weld-seal valve)
8. **Final Leak Test**: Verify vacuum integrity (≤1×10⁻⁸ torr-L/sec leak rate)

**Vacuum Requirements**:
- Initial vacuum: ≤1×10⁻⁵ torr
- Operating vacuum (after getter activation and thermal cycling): ≤1×10⁻⁶ torr
- Leak rate: ≤1×10⁻⁸ torr-L/sec

## Quality Control for Cryogenic Components

See comprehensive QC plan: [10-00-09-24A_Cryo_Component_QC.md](../quality-control/10-00-09-24A_Cryo_Component_QC.md)

### Inspection Requirements

**Receiving Inspection**:
- Material certifications with Charpy impact data at -196°C or -253°C
- Chemical composition and mechanical properties
- Visual inspection for surface defects
- Dimensional check (sample or 100% per criticality)

**In-Process Inspection**:
- Dimensional checks at hold points
- Weld inspection (visual, PT, RT)
- Heat treatment verification (hardness, microstructure)
- Cleanliness verification

**Final Inspection**:
- 100% dimensional inspection per drawing
- 100% visual inspection
- Leak testing (pressure and/or helium mass spectrometer)
- Functional testing (thermal performance, vacuum integrity)

### Non-Destructive Testing (NDT)

**Visual Inspection (VT)**:
- 100% of all components
- Look for cracks, surface defects, weld quality

**Liquid Penetrant Testing (PT)**:
- All weld seams and high-stress areas
- Per ASTM E1417 or AMS 2644
- Technician: NAS-410 Level II

**Radiographic Testing (RT)**:
- 100% of pressure boundary welds
- Per ASTM E1742 or AMS 2647
- Acceptance: No cracks, incomplete fusion, porosity >5% wall thickness

**Ultrasonic Testing (UT)**:
- Thick sections (>0.5" wall) or suspected defects
- Per ASTM E164
- Technician: NAS-410 Level II

### Cryogenic Performance Testing

**Thermal Cycling Test**:
- Cool component to -253°C (liquid hydrogen or helium bath)
- Hold for specified time (typically 15-30 minutes)
- Warm to ambient temperature
- Repeat for specified number of cycles (10-100)
- Inspect for cracks, leaks, dimensional changes after cycling

**Heat Leak Measurement** (for insulated components):
- Cool component to -253°C
- Measure heat input to maintain temperature (boil-off rate)
- Calculate effective thermal conductivity
- Compare to design specification

**Vacuum Integrity Test** (for vacuum-jacketed components):
- Evacuate component and seal
- Monitor vacuum level over time (typically 24-48 hours)
- Acceptable: Pressure rise <10× over test period
- Perform helium leak test if vacuum integrity is questionable

### Leak Testing

**Pressure Decay Test** (Initial screening):
- Pressurize to 1.5× design pressure with nitrogen or helium
- Hold for 10 minutes minimum
- Measure pressure drop (<1% allowed)

**Helium Mass Spectrometer Leak Test** (Final verification):
- **Sensitivity**: ≤1×10⁻⁹ std cc/sec for pressure boundaries
- **Sensitivity**: ≤1×10⁻⁸ torr-L/sec for vacuum jackets
- **Method**: External sniffing or chamber method
- Document leak rate (must be below specification)

## Safety Requirements

### Cryogenic Safety Hazards

1. **Extreme Cold Burns**: Contact with -253°C surfaces or fluids causes instant frostbite
2. **Asphyxiation**: Vaporized cryogens displace oxygen (1 L LH2 → 850 L gaseous H2 at STP)
3. **Material Embrittlement**: Most materials become brittle at cryogenic temps
4. **Pressure Build-Up**: Vaporization in closed containers creates extreme pressure
5. **Explosion**: Rapid phase transition if LH2 contacts water or other incompatible materials

### Personal Protective Equipment (PPE)

**Minimum PPE for Cryogenic Work**:
- **Cryo Gloves**: Insulated gloves rated for -253°C (loose-fitting for quick removal)
- **Face Shield**: Full-face shield over safety glasses
- **Apron or Lab Coat**: Insulated, non-porous (prevents liquid pooling on clothing)
- **Closed-Toe Shoes**: No sandals or open-toe shoes
- **Long Pants**: No shorts (liquid can splash)

**Additional PPE for Prolonged Exposure**:
- Insulated boots
- Hearing protection (if venting high-pressure cryogens)

### Work Area Requirements

- **Ventilation**: Adequate ventilation to prevent oxygen deficiency (<19.5% O2 is IDLH)
- **Oxygen Monitoring**: Continuous O2 monitoring in enclosed areas (alarm at <19.5%)
- **Cryogen Detectors**: For enclosed areas (H2 detection if working with LH2)
- **Emergency Eyewash/Shower**: Within 10 seconds of any cryogenic work area
- **Warning Signs**: "Cryogenic Hazard" signs posted

### Training Requirements

- **Cryogenic Safety Awareness**: All personnel in cryogenic work areas
- **Cryogenic Handling**: Personnel directly handling cryogens
- **First Aid for Cold Burns**: Supervisors and safety personnel
- **Emergency Response**: Spill response, oxygen deficiency rescue

## Work Instructions

Detailed work instructions for critical cryogenic operations:

- [10-00-09-53A_Cryo_Insulation_Install_WI.md](../work-instructions/10-00-09-53A_Cryo_Insulation_Install_WI.md)

## Supplier Management

### Cryogenic Material Suppliers

See: [10-00-09-43A_Cryo_Material_Suppliers.md](../supplier-management/10-00-09-43A_Cryo_Material_Suppliers.md)

**Supplier Requirements**:
- AS9100D certified
- NADCAP accredited for welding, heat treatment, NDT
- Cryogenic experience (references required)
- Capability to provide Charpy impact data at -196°C or -253°C
- On-site audit approval for critical suppliers

## Production Schedule

### Lead Times

| Component Type | Typical Lead Time | Critical Path Items |
|----------------|-------------------|---------------------|
| Vacuum-Jacketed Lines | 14-20 weeks | Welding, evacuation, thermal cycling |
| Thermal Breaks (G-10) | 6-8 weeks | Material procurement, machining |
| MLI Blankets | 4-6 weeks | Pattern development, assembly |
| Cryogenic Valves | 16-22 weeks | Machining, assembly, cryogenic testing |
| Cryogenic Sensors | 10-14 weeks | Sensor element, calibration, cryo testing |

### Schedule Integration

See: [10-00-09-62A_H2_System_Schedule.md](../production-schedules/10-00-09-62A_H2_System_Schedule.md)  
(H2 and cryogenic schedules are often combined due to overlap in LH2 systems)

## Cost Drivers and Optimization

**Primary Cost Drivers**:
1. **Material Costs**: Cryogenic-grade materials (316L SS, 5083 Al) with impact testing
2. **Special Processes**: Vacuum brazing, electron beam welding (outsourced)
3. **Testing**: Cryogenic thermal cycling and performance testing
4. **Insulation**: MLI fabrication is labor-intensive
5. **Quality**: Extensive inspection and documentation

**Cost Reduction Opportunities**:
- Standardize components to amortize NRE (non-recurring engineering) costs
- In-house thermal cycling capability (reduce outsourcing)
- Optimize MLI layer count (balance performance vs. cost)
- Design for manufacturability (minimize complex geometries)
- Continuous improvement to reduce fabrication and test cycle times

## References

### Internal Documentation

- [10-00-09-01A_Master_Manufacturing_Plan.md](10-00-09-01A_Master_Manufacturing_Plan.md)
- [10-00-09-14A_Cryo_Material_Processing.md](../process-specifications/10-00-09-14A_Cryo_Material_Processing.md)
- [10-00-09-24A_Cryo_Component_QC.md](../quality-control/10-00-09-24A_Cryo_Component_QC.md)
- [10-00-09-33A_Cryo_Testing_Equipment.md](../tooling-equipment/10-00-09-33A_Cryo_Testing_Equipment.md)
- [10-00-09-43A_Cryo_Material_Suppliers.md](../supplier-management/10-00-09-43A_Cryo_Material_Suppliers.md)
- [10-00-09-73A_Cryo_Material_Storage.md](../logistics/10-00-09-73A_Cryo_Material_Storage.md)

### External Standards

- **ISO 13984**: Liquid Hydrogen - Land Vehicle Fuel Tanks
- **ASME Section VIII**: Rules for Construction of Pressure Vessels (Division 1, 2, or 3)
- **AWS D17.1**: Specification for Fusion Welding for Aerospace Applications
- **ASTM E23**: Standard Test Methods for Notched Bar Impact Testing of Metallic Materials
- **ASTM E8**: Standard Test Methods for Tension Testing of Metallic Materials
- **AMS 2750**: Pyrometry
- **NADCAP**: National Aerospace and Defense Contractors Accreditation Program
- **NAS-410**: Certification and Qualification of Nondestructive Test Personnel
- **AS9100D**: Quality Management Systems - Aerospace Requirements

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-10

### Revision History

| Revision | Date | Author | Description | Approved By |
|----------|------|--------|-------------|-------------|
| A | 2025-12-10 | AI (GitHub Copilot) / A. Pelliccia | Initial release | TBD |

---

**End of Document**
