# 13_SUBSYSTEMS_AND_COMPONENTS - ATA 28 Hierarchical Breakdown

**ATA Chapter:** 28-00-00  
**Document Type:** Subsystem Decomposition  
**Classification:** Technical Structure  

---

## ATA Numbering Hierarchy

This document demonstrates the complete ATA chapter hierarchical structure from 2 digits down to 8-9 digits, following aerospace industry standards (ATA iSpec 2200).

### Hierarchical Levels

- **2-digit (ATA Chapter)**: 28 = Fuel Systems (adapted for hydrogen)
- **4-digit (System Level)**: 28-XX-00 = Major subsystems
- **6-digit (Subsystem Level)**: 28-XX-YY = Functional assemblies
- **8-digit (Component Level)**: 28-XX-YY-ZZ = Individual components
- **9-digit (Part Level)**: 28-XX-YY-ZZZ = Specific parts/configurations

---

## Level 1: ATA 28 (2-digit) - Fuel/Hydrogen Systems

**Full Code:** 28  
**Description:** Complete hydrogen storage and distribution system for AMPEL360 aircraft

---

## Level 2: Subsystems (4-digit - 28-XX-00)

### 28-10-00: H₂ Storage Tanks
Primary and secondary liquid hydrogen storage vessels with cryogenic insulation

### 28-20-00: Cryogenic Feed Lines
Vacuum-jacketed transfer lines connecting tanks to fuel cells

### 28-30-00: Pressure Control System
Pumps, compressors, and regulators maintaining system pressure

### 28-40-00: Tank Instrumentation
Sensors, transducers, and monitoring equipment

### 28-50-00: Boil-Off Recovery System
Gaseous hydrogen capture and recirculation

### 28-60-00: Safety and Isolation System
Emergency shutdown, leak detection, and fire suppression

---

## Level 3: Functional Assemblies (6-digit - 28-XX-YY)

### 28-10-00: H₂ Storage Tanks Breakdown

#### 28-10-10: Primary Storage Tank
- **Capacity:** [TBD] kg LH₂
- **Type:** Type IV composite overwrapped pressure vessel (COPV)
- **Insulation:** Multi-layer vacuum insulation (MLVI)
- **Operating Pressure:** [TBD] bar
- **Design Pressure:** [TBD] bar (1.5× MEOP minimum)

#### 28-10-20: Secondary Storage Tank
- **Capacity:** [TBD] kg LH₂ (backup/reserve)
- **Type:** Type IV COPV
- **Redundancy:** Provides flight-critical redundancy
- **Configuration:** Isolated system with independent feed

#### 28-10-30: Tank Mounting Structure
- Structural interface to airframe (ATA 53)
- Load distribution framework
- Thermal isolation mounts
- Vibration damping system

#### 28-10-40: Vacuum Insulation System
- Multi-layer insulation (MLI) blankets
- Vacuum maintenance system
- Getter materials (hydrogen absorption)
- Vacuum monitoring sensors

#### 28-10-50: Pressure Relief System
- Primary relief valve (PRV)
- Secondary/redundant PRV
- Burst disk backup
- Vent line to atmosphere

#### 28-10-60: Tank Filling Interface
- Ground service coupling
- Quick-disconnect fittings
- Fill rate control valve
- Backflow prevention

---

### 28-20-00: Cryogenic Feed Lines Breakdown

#### 28-20-10: Main Feed Line (Tank to Fuel Cell)
- **Diameter:** [TBD] mm
- **Material:** Stainless steel 316L (cryogenic grade)
- **Insulation:** Vacuum-jacketed
- **Length:** [TBD] meters

#### 28-20-20: Return Line (Boil-off recirculation)
- Return path for gaseous hydrogen
- Integrated with boil-off recovery (28-50-00)
- Pressure balancing function

#### 28-20-30: Distribution Manifold
- Splits flow to multiple fuel cell stacks
- Flow balancing between cells
- Individual cell isolation valves

#### 28-20-40: Thermal Expansion Joints
- Accommodates thermal contraction (ambient to -253°C)
- Bellows-type expansion compensators
- Maintains pressure seal integrity

#### 28-20-50: Emergency Shutoff Valves
- Solenoid-actuated isolation valves
- Fail-safe (fail-closed) design
- Redundant actuation (electrical + pneumatic)
- Response time: < 100ms

#### 28-20-60: Flow Measurement Stations
- Coriolis mass flow meters
- Temperature compensation
- Digital output to FADEC and CAOS

---

### 28-30-00: Pressure Control System Breakdown

#### 28-30-10: Cryogenic Pumps
- Centrifugal pump design for LH₂
- Variable speed drive
- Minimum NPSH requirement
- Redundant pump capability

#### 28-30-20: Pressure Regulators
- Primary regulator: Tank to feed line
- Secondary regulator: Fine pressure control
- Pilot-operated relief valve integration

#### 28-30-30: Vaporizer/Heat Exchanger (if required)
- Converts LH₂ to gaseous H₂ if needed
- Heat source from APU or waste heat
- Flow rate capacity matching

#### 28-30-40: Pressure Accumulator
- Dampens pressure fluctuations
- Emergency pressure reserve
- Bladder or piston type

---

## Level 4: Components (8-digit - 28-XX-YY-ZZ)

### Example: 28-10-10 Primary Storage Tank Components

#### 28-10-10-01: Tank Shell (Composite)
- Inner liner: Aluminum or polymer
- Carbon fiber overwrap (T700 or equivalent)
- Filament winding pattern: Hoop + helical
- Thickness: [TBD] mm

#### 28-10-10-02: Tank End Domes
- Forward dome assembly
- Aft dome assembly
- Boss penetrations for fittings

#### 28-10-10-03: Internal Baffles
- Anti-slosh baffles
- Liquid stratification prevention
- Thermosiphon enhancement

#### 28-10-10-04: Liquid Level Sensor Assembly
- Capacitive probe technology
- Multiple measurement points
- Temperature-compensated readings
- Digital output: 0-100% level

#### 28-10-10-05: Temperature Sensor Array
- Type T thermocouples (cryogenic rated)
- Multiple zones: Top, middle, bottom, wall
- 8-channel monitoring per tank
- CAOS integration for thermal mapping

#### 28-10-10-06: Pressure Transducer
- Range: 0-[TBD] bar absolute
- Accuracy: ±0.25% FS
- Temperature compensation: -270°C to +85°C
- Output: 4-20mA + digital (ARINC 429)

#### 28-10-10-07: Safety Valve (Primary)
- Set pressure: [TBD] bar
- Flow capacity: [TBD] kg/min H₂ gas
- Certification: ASME Section VIII
- Re-seat pressure: 90% of set

#### 28-10-10-08: Safety Valve (Secondary)
- Independent redundant valve
- Set pressure: [TBD] bar (10% above primary)
- Same specifications as primary

#### 28-10-10-09: Burst Disk Assembly
- Ultimate overpressure protection
- Rupture pressure: [TBD] bar
- One-time use (requires replacement)
- Includes telltale indicator

---

### Example: 28-20-10 Main Feed Line Components

#### 28-20-10-01: Inner Transfer Tube
- Material: SS 316L seamless
- Wall thickness: [TBD] mm
- Surface finish: Electropolished

#### 28-20-10-02: Outer Vacuum Jacket
- Material: Stainless steel or aluminum
- Vacuum level: < 10⁻⁵ mbar
- Leak rate: < [TBD] mbar·L/s

#### 28-20-10-03: Spacers and Supports
- Low thermal conductivity material (G-10 or similar)
- Minimize heat conduction to inner tube
- Maintain concentricity

#### 28-20-10-04: MLI Blanket Layers
- 20-40 layers of aluminized mylar
- Crinkled for spacing
- Thermal performance: k_eff < [TBD] W/m·K

#### 28-20-10-05: Vacuum Port and Getter
- Valve for initial evacuation
- Activated charcoal getter (hydrogen adsorption)
- Vacuum monitoring tap

#### 28-20-10-06: End Fittings (Flanges)
- Conflat (CF) or VCR fittings (cryogenic rated)
- Metal gasket seals
- Torque specifications per manufacturer

---

## Level 5: Part Numbers (9-digit - 28-XX-YY-ZZZ)

### Example: 28-10-10-04 Liquid Level Sensor - Part Variants

#### 28-10-10-041: Level Sensor - Primary Tank Configuration
- Length: [TBD] mm (matches primary tank height)
- Part Number: AMPEL-LLS-P001-A
- Manufacturer: [TBD]
- Serial Number Format: YYMMDDSSSS

#### 28-10-10-042: Level Sensor - Secondary Tank Configuration
- Length: [TBD] mm (matches secondary tank height)
- Part Number: AMPEL-LLS-S001-A
- Otherwise identical to -041

#### 28-10-10-043: Level Sensor - Spare/Service Unit
- Universal length (field-trimmable)
- Part Number: AMPEL-LLS-U001-A
- Includes calibration certificate

---

## Recursive 14-Folder Structure

Each level (4-digit, 6-digit, 8-digit) can have its own 14-folder lifecycle documentation:

```
28-10-00_H2_STORAGE_TANKS/
├── 01_OVERVIEW/
├── 02_SAFETY/
├── ...
├── 13_SUBSYSTEMS_AND_COMPONENTS/
│   ├── 28-10-10_PRIMARY_TANK/
│   │   ├── 01_OVERVIEW/
│   │   ├── 02_SAFETY/
│   │   ├── ...
│   │   └── 13_SUBSYSTEMS_AND_COMPONENTS/
│   │       ├── 28-10-10-01_TANK_SHELL/
│   │       ├── 28-10-10-02_END_DOMES/
│   │       ├── 28-10-10-04_LEVEL_SENSOR/
│   │       │   ├── 01_OVERVIEW/
│   │       │   ├── 04_DESIGN/
│   │       │   ├── 06_ENGINEERING/
│   │       │   └── ... (14-folder structure)
│   │       └── ...
│   ├── 28-10-20_SECONDARY_TANK/
│   └── ...
└── 14_META_GOVERNANCE/
```

---

## Digital Product Passport (DPP) Integration

Each component level (8-digit and below) has individual DPP tracking:

### Example: 28-10-10-04-042 Instance Tracking

```json
{
  "ata_code": "28-10-10-04",
  "part_variant": "042",
  "serial_number": "25112401234",
  "installation": {
    "aircraft_msn": "AMPEL-001",
    "position": "Secondary Tank",
    "installed_date": "2025-11-12",
    "installed_by": "Technician #1234"
  },
  "lifecycle": {
    "manufacture_date": "2025-10-15",
    "first_calibration": "2025-10-20",
    "operating_hours": 0,
    "cycles": 0,
    "next_calibration_due": "2027-10-20"
  },
  "traceability": {
    "material_lot": "CF-T700-20251001",
    "manufacturer": "SensorTech Inc.",
    "certification": "EASA-Form1-20251015-001"
  }
}
```

---

## CAOS Monitoring Hierarchy

### System Level (28-00-00)
- Overall hydrogen system health
- Fleet-wide performance comparison
- Predictive maintenance scheduling

### Subsystem Level (28-10-00)
- Primary tank performance trends
- Boil-off rate analysis
- Pressure stability monitoring

### Component Level (28-10-10-04)
- Individual sensor health
- Calibration drift detection
- Failure prediction (MTTF tracking)

---

## Cross-References

- **Parent System**: ATA 28-00-00 (top level)
- **Related Systems**: 
  - ATA 73 (Fuel Cell - hydrogen consumer)
  - ATA 24 (Electrical - power for pumps)
  - ATA 26 (Fire Protection - safety integration)
- **Digital Product Passport**: ATA 95 (component serialization)
- **CAOS Integration**: ATA 40 (predictive analytics)

---

## Certification Requirements by Level

### 4-Digit (System)
- System Safety Assessment (SSA)
- EASA/FAA Type Certification

### 6-Digit (Subsystem)
- Preliminary System Safety Assessment (PSSA)
- Design approval

### 8-Digit (Component)
- Component qualification testing
- Material/process specifications

### 9-Digit (Part)
- Manufacturing approval
- Individual serialization and traceability

---

**Document Owner:** Systems Engineering  
**Hierarchy Standards:** ATA iSpec 2200  
**Folder Schema:** /14_META_GOVERNANCE/schemas/13_subsystems_schema.json  
**Generated by:** AMPEL360 Documentation Expert Agent
