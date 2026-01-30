# 10-00-09-04A H2 Components Manufacturing

## Document Information

- **Document ID**: 10-00-09-04A
- **Title**: Hydrogen Components Manufacturing Plan
- **Version**: 1.0 (Revision A)
- **Date**: 2025-12-10
- **Status**: Draft
- **Category**: Manufacturing Plan - H2 Specific
- **ATA Chapter**: 10 - Parking, Mooring, Storage & RTS

## Purpose

This document defines the specialized manufacturing processes, controls, and quality requirements for hydrogen (H2) system components used in ATA 10 Parking, Mooring, Storage, and RTS operations for the AMPEL360 BWB-H2 aircraft. These components include H2 detectors, safety equipment, valves, sensors, and associated hardware that interface with the aircraft's hydrogen systems during ground operations.

## Scope

### Included Components

- **H2 Detection Systems**: Fixed and portable H2 detectors for parking areas
- **Safety Equipment**: Emergency shutdown valves, pressure relief devices
- **H2 Sensors**: Temperature, pressure, and flow sensors for ground operations
- **H2 Connectors**: Ground supply quick-disconnect fittings (parking interface)
- **Purge Equipment**: N2 purge valves and manifolds for ground safety

### Exclusions

- Aircraft onboard H2 fuel system (covered under ATA 28)
- Ground H2 production and storage infrastructure (covered under ATA 85)
- H2 refueling equipment design (covered under ATA 03 - GSE)

## H2 Manufacturing Requirements

### Material Selection

All materials in contact with hydrogen must be H2-compatible to prevent:
- **Hydrogen Embrittlement**: Loss of ductility and strength in metals
- **Permeation**: Diffusion of H2 through materials
- **Compatibility Issues**: Chemical reactions or degradation

#### Approved H2-Compatible Materials

| Material | Specification | Application | Notes |
|----------|---------------|-------------|-------|
| **316L Stainless Steel** | AMS 5507, AMS 5524 | Valves, fittings, pressure vessels | Solution annealed, low carbon to prevent sensitization |
| **Inconel 625** | AMS 5666, AMS 5599 | High-temperature components, springs | Excellent H2 resistance, high strength |
| **Inconel 718** | AMS 5662, AMS 5663 | High-stress components | Age-hardenable, requires controlled heat treatment |
| **Elgiloy** | AMS 5876 | Springs, bellows | Cobalt-based alloy with excellent H2 compatibility |
| **Monel 400** | AMS 4674, AMS 4675 | Corrosion-resistant components | Nickel-copper alloy |
| **Aluminum 5083-H321** | AMS 4057 | Low-pressure housings | Strain-hardened, corrosion resistant |
| **PTFE (Teflon)** | AMS 3651 | Seals, gaskets | Virgin PTFE, no fillers |
| **Kalrez** | DuPont Spec | High-performance seals | Perfluoroelastomer, extreme environments |
| **PEEK** | AMS 3667 | Electrical insulation, bushings | High-performance thermoplastic |

#### Prohibited Materials

- **High-carbon steels** (>0.30% C): Susceptible to hydrogen embrittlement
- **Cast iron**: Brittle, poor H2 compatibility
- **Copper and brass** (except specific alloys): Hydrogen embrittlement concern
- **Zinc-plated components**: Hydrogen absorption and embrittlement
- **Soft elastomers** (NBR, EPDM): High permeation rates

### Cleanliness Requirements

H2 components require exceptional cleanliness to prevent ignition sources and ensure proper function.

#### Cleaning Process

**Level 1: Standard Cleaning** (Low-pressure, non-critical components)
- Solvent cleaning (isopropyl alcohol or approved equivalent)
- Ultrasonic cleaning for complex geometries
- Hot water rinse and compressed air dry
- Visual inspection for cleanliness

**Level 2: Precision Cleaning** (Medium-pressure, control components)
- Alkaline cleaning (pH 10-11)
- Ultrasonic cleaning with filtered solution
- DI water rinse (5 stages)
- Cleanroom drying (ISO Class 6)
- Particulate count verification (<100 particles >10μm per 100 mL)

**Level 3: Oxygen Cleaning** (High-pressure, H2 service)
- Per ASTM G93 or CGA G-4.1
- Alkaline cleaning with ultrasonic agitation
- Acid passivation (for stainless steel)
- DI water rinse (7 stages, final rinse <0.5 μS/cm conductivity)
- Cleanroom drying (ISO Class 5)
- Particle count: <25 particles >5μm per 100 mL
- Hydrocarbon residue: <1 mg/100 cm²
- Package in sealed clean bags with inert gas purge

#### Cleanroom Assembly

Critical H2 components are assembled in controlled environments:

**ISO Class 5 (Class 100)**:
- H2 valves (internal assembly)
- Sensor elements
- Sealed electronics enclosures

**ISO Class 6 (Class 1000)**:
- H2 detector assemblies
- Quick-disconnect fittings (final assembly)
- Pressure regulators

## Manufacturing Processes

### Welding for H2 Service

All welds on H2 components must comply with:
- AWS D17.1 (Aerospace Fusion Welding)
- ASME B31.12 (Hydrogen Piping)
- SAE AS6968 (Hydrogen Aircraft Systems)

See detailed welding specification: [10-00-09-13A_H2_Compatible_Welding.md](../process-specifications/10-00-09-13A_H2_Compatible_Welding.md)

#### Welding Process Summary

**Preferred Welding Methods**:

1. **Orbital TIG (GTAW)**: Tube-to-fitting welds
   - Automatic process for repeatability
   - Inert gas purge (argon or helium) on both sides
   - Full penetration welds required
   - Weld parameters monitored and recorded

2. **Manual TIG (GTAW)**: Repair and complex geometry
   - Qualified welders per AWS D17.1
   - Controlled environment (low humidity, no drafts)
   - Pre-weld and post-weld cleaning

3. **Electron Beam (EBW)**: Thick sections, dissimilar materials (outsourced)
   - Vacuum environment (prevents contamination)
   - Deep penetration with minimal heat-affected zone
   - Used for critical joints where EB is advantageous

**Welding Consumables**:
- 316L filler wire (ER316L per AWS A5.9)
- Inconel 625 filler (ERNiCrMo-3 per AWS A5.14)
- Argon or helium shielding gas (99.999% purity)

**Post-Weld Treatment**:
- Stress relief (optional, depends on material and application)
- Solution annealing (for austenitic stainless steels to prevent sensitization)
- Pickling and passivation (per ASTM A380)

#### Weld Inspection

**100% Inspection Required**:
- Visual inspection (per AWS D17.1)
- Radiographic testing (RT) - 100% of H2 service welds
- Liquid penetrant testing (PT) - all accessible surfaces
- Helium leak testing - ≤1×10⁻⁹ std cc/sec

### Machining

**General Requirements**:
- Use cutting fluids compatible with H2 service (synthetic, water-soluble, or none)
- Final cleaning after machining to remove all residues
- Inspection of machined surfaces for defects (scratches, gouges, burrs)

**Critical Dimensions**:
- Sealing surfaces: ≤32 μin Ra (0.8 μm Ra)
- Threaded connections: Class 2A/2B minimum
- O-ring grooves: Per AS568 or AS5857

### Heat Treatment

Heat treatment of H2 components must be performed per:
- AMS 2750 (Pyrometry requirements)
- NADCAP AC7102 (Heat Treatment)

**Common Heat Treatments**:

| Material | Treatment | Purpose | Temperature | Atmosphere |
|----------|-----------|---------|-------------|------------|
| 316L SS | Solution Anneal | Remove sensitization, restore corrosion resistance | 1900-2100°F | Inert or vacuum |
| Inconel 718 | Age Hardening | Increase strength | 1325°F + 1150°F | Air or inert |
| Inconel 625 | Stress Relief | Reduce residual stresses | 1600-1800°F | Inert |

**Heat Treatment Controls**:
- Furnace qualification per AMS 2750 (Class and Type per application)
- Thermocouple calibration (NIST-traceable)
- Load thermocouples to verify part temperature
- Time-temperature recording for traceability

### Surface Treatment

**Passivation** (Stainless Steel):
- Per ASTM A380 or AMS 2700
- Removes free iron, enhances corrosion resistance
- Nitric acid or citric acid bath
- Post-treatment rinse and drying

**Electropolishing** (Optional for critical surfaces):
- Removes surface imperfections
- Creates smooth, passive surface
- Reduces particle generation

**Prohibited Surface Treatments**:
- Cadmium plating (banned in many jurisdictions, H2 incompatible)
- Zinc plating (hydrogen embrittlement risk)
- Chrome plating (cracks can trap hydrogen)

## Quality Control for H2 Components

See comprehensive QC plan: [10-00-09-23A_H2_Component_QC.md](../quality-control/10-00-09-23A_H2_Component_QC.md)

### Inspection Requirements

**Receiving Inspection**:
- Material certifications (mill certs with chemical and mechanical properties)
- Heat lot traceability
- Visual inspection for damage or contamination
- Dimensional check (sample or 100% depending on risk)

**In-Process Inspection**:
- Dimensional checks at defined hold points
- Visual inspection after each major operation
- Cleanliness verification before assembly
- Welding inspection (visual, PT, RT as required)

**Final Inspection**:
- 100% dimensional inspection per drawing
- 100% visual inspection
- Functional testing (pressurization, actuation, etc.)
- Leak testing (pressure decay and/or helium mass spectrometer)
- Cleanliness verification (if Level 2 or 3 required)

### Non-Destructive Testing (NDT)

**Visual Inspection (VT)**:
- 100% of all components
- Trained inspectors per NAS-410 Level I or II

**Liquid Penetrant Testing (PT)**:
- All weld seams and high-stress areas
- Per ASTM E1417 or AMS 2644
- Technician certification: NAS-410 Level II

**Radiographic Testing (RT)**:
- 100% of all H2 service welds
- Per ASTM E1742 or AMS 2647
- Film or digital radiography
- Technician certification: NAS-410 Level II
- Acceptance criteria: No cracks, incomplete fusion, or porosity >5% wall thickness

**Ultrasonic Testing (UT)**:
- Thick sections or suspected subsurface defects
- Per ASTM E164 or equivalent
- Technician certification: NAS-410 Level II

### Leak Testing

Leak testing is **mandatory** for all H2 components with pressure boundaries.

**Pressure Decay Test** (Initial screening):
- Pressurize to 1.5× design pressure with nitrogen or helium
- Hold for 10 minutes minimum
- Measure pressure drop (<1% allowed)

**Helium Mass Spectrometer Leak Test** (Final verification):
- **Sensitivity**: ≤1×10⁻⁹ std cc/sec (standard cubic centimeters per second)
- **Method**: External sniffing or chamber method
- **Procedure**:
  1. Evacuate component and backfill with helium
  2. Pressurize to design pressure or higher
  3. Use mass spectrometer detector to scan all joints and welds
  4. Document leak rate (must be below spec)

**Acceptance Criteria**:
- No detectable leaks at ≤1×10⁻⁹ std cc/sec sensitivity
- For larger assemblies, ≤1×10⁻⁸ std cc/sec may be acceptable (with engineering approval)

### Functional Testing

**H2 Detectors**:
- Calibration with known H2 concentrations (e.g., 1%, 2%, 4% H2 in air or N2)
- Response time verification (<5 seconds typical)
- Alarm threshold verification
- Environmental testing (temperature, humidity per spec)

**Valves**:
- Actuation force or pressure measurement
- Cycle testing (typically 100-1000 cycles depending on application)
- Leak testing in both open and closed positions
- Fail-safe verification (if applicable)

**Sensors**:
- Calibration against reference standards
- Accuracy and repeatability verification
- Environmental testing (temperature cycling)
- Output signal verification

## Traceability Requirements

### Material Traceability

**Required Documentation**:
- Material certifications (mill certs) with heat lot numbers
- Chemical composition analysis
- Mechanical property test results
- Heat treatment records (if applicable)

**Marking**:
- Permanent marking on each component (laser etching, electro-etching, or stamping)
- Marking includes: Part number, serial number, heat lot, and date code

### Process Traceability

**Manufacturing Traveler** (routing sheet) accompanies each component:
- Lists all manufacturing operations in sequence
- Inspection and test hold points
- Operator and inspector sign-offs
- Traceability to work instructions, process specs, and tooling

**Records Retention**:
- Manufacturing travelers: Permanent (life of aircraft +5 years minimum)
- Inspection and test records: Permanent
- Nonconformance reports and corrective actions: Permanent
- Weld records: Permanent

## Safety Requirements

### Hydrogen Safety

**Designated H2 Work Areas**:
- H2 detection and monitoring (continuous)
- Explosion-proof electrical equipment (Class I, Division 2)
- Ventilation (>10 air changes per hour)
- No-ignition-source policy (no sparks, flames, static)

**Personal Protective Equipment (PPE)**:
- Safety glasses with side shields (minimum)
- Static-dissipative clothing and shoes
- Insulated gloves for cryogenic H2 (if applicable)
- Hearing protection (if high-pressure venting occurs)

**Training Requirements**:
- H2 safety awareness (all personnel in H2 areas)
- H2 leak response and emergency procedures
- Use of H2 detectors and monitoring equipment
- Annual refresher training

### Emergency Procedures

- **H2 Leak Detection**: Evacuate area, activate ventilation, isolate source, call emergency response
- **H2 Fire**: Evacuate, call fire department (specialized H2 firefighting)
- **High-Pressure Release**: Evacuate, hearing protection, assess for injuries
- **Emergency Contacts**: Posted in all H2 work areas

## Work Instructions

Detailed work instructions are provided for critical operations:

- [10-00-09-52A_H2_Valve_Assembly_WI.md](../work-instructions/10-00-09-52A_H2_Valve_Assembly_WI.md)
- [10-00-09-54A_H2_Detector_Assembly_WI.md](../work-instructions/10-00-09-54A_H2_Detector_Assembly_WI.md)

## Supplier Management

### H2 Component Suppliers

See: [10-00-09-42A_H2_Component_Suppliers.md](../supplier-management/10-00-09-42A_H2_Component_Suppliers.md)

**Supplier Requirements**:
- AS9100D certified
- NADCAP accredited for applicable special processes (welding, heat treatment, NDT)
- H2 experience (demonstrated with references)
- Audit approval (on-site audit for critical suppliers)

## Production Schedule

### Lead Times

| Component Type | Typical Lead Time | Critical Path Items |
|----------------|-------------------|---------------------|
| H2 Detectors | 12-14 weeks | Sensor calibration, environmental testing |
| H2 Valves | 14-18 weeks | Machining, welding, leak testing |
| H2 Sensors | 10-12 weeks | Sensor element, calibration |
| Quick-Disconnect Fittings | 8-10 weeks | Machining, plating/coating, testing |

### Schedule Integration

See: [10-00-09-62A_H2_System_Schedule.md](../production-schedules/10-00-09-62A_H2_System_Schedule.md)

## Cost Drivers and Optimization

**Primary Cost Drivers**:
1. **Material Costs**: H2-compatible materials (Inconel, 316L SS) are expensive
2. **Special Processes**: NADCAP welding, heat treatment, and NDT require certified suppliers
3. **Leak Testing**: Helium mass spectrometer testing is time-intensive
4. **Cleanliness**: Cleanroom assembly and precision cleaning add cost
5. **Traceability**: Documentation and record-keeping overhead

**Cost Reduction Opportunities**:
- Standardize designs to reduce unique parts
- Volume purchasing of H2-compatible materials
- In-house capability for high-volume processes
- Design for manufacturability (DFM) to simplify fabrication
- Continuous improvement to reduce cycle times

## References

### Internal Documentation

- [10-00-09-01A_Master_Manufacturing_Plan.md](10-00-09-01A_Master_Manufacturing_Plan.md)
- [10-00-09-13A_H2_Compatible_Welding.md](../process-specifications/10-00-09-13A_H2_Compatible_Welding.md)
- [10-00-09-23A_H2_Component_QC.md](../quality-control/10-00-09-23A_H2_Component_QC.md)
- [10-00-09-32A_H2_Handling_Equipment.md](../tooling-equipment/10-00-09-32A_H2_Handling_Equipment.md)
- [10-00-09-42A_H2_Component_Suppliers.md](../supplier-management/10-00-09-42A_H2_Component_Suppliers.md)
- [10-00-09-72A_H2_Component_Handling.md](../logistics/10-00-09-72A_H2_Component_Handling.md)

### External Standards

- **SAE AS6968**: Hydrogen Aircraft Systems Requirements
- **ASME B31.12**: Hydrogen Piping and Pipelines
- **AWS D17.1**: Specification for Fusion Welding for Aerospace Applications
- **ASTM G93**: Standard Practice for Cleaning Methods and Cleanliness Levels for Material and Equipment Used in Oxygen-Enriched Environments (applicable to H2 by analogy)
- **CGA G-4.1**: Cleaning Equipment for Oxygen Service
- **ISO/TR 15916**: Basic Considerations for the Safety of Hydrogen Systems
- **AS9100D**: Quality Management Systems - Aerospace Requirements
- **NADCAP**: National Aerospace and Defense Contractors Accreditation Program
- **NAS-410**: Certification and Qualification of Nondestructive Test Personnel

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
