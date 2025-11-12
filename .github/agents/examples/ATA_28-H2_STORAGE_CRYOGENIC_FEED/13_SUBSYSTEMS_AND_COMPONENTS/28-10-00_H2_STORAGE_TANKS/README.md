# ATA 28-10-00: H₂ Storage Tanks (4-digit Level)

**Parent System:** 28-00-00 - Hydrogen Storage and Cryogenic Feed System  
**ATA Code:** 28-10-00  
**Level:** Subsystem (4-digit)  
**Classification:** Safety Critical - DAL A

---

## Subsystem Description

The H₂ Storage Tanks subsystem provides safe, efficient containment of liquid hydrogen at cryogenic temperatures (-253°C / 20K) for the AMPEL360 aircraft propulsion system. The subsystem includes primary and secondary tanks, mounting structures, insulation systems, and all associated safety equipment.

### Key Performance Requirements

| Parameter | Specification | Verification Method |
|-----------|---------------|---------------------|
| Total Storage Capacity | [TBD] kg LH₂ | Design calculation + fill test |
| Operating Pressure | [TBD] bar | Pressure test |
| Design Pressure | 1.5 × MEOP minimum | Burst test |
| Boil-off Rate | < 0.5% per day | Thermal performance test |
| Empty Weight | < [TBD] kg | Weigh test |
| Lifetime Cycles | > 10,000 fill/drain | Fatigue test |
| Vacuum Insulation | < 10⁻⁵ mbar | Vacuum decay test |

---

## 6-Digit Subsystem Breakdown

### 28-10-10: Primary Storage Tank
- **Function:** Main hydrogen storage for normal operations
- **Capacity:** [TBD] kg LH₂ (majority of total capacity)
- **Type:** Type IV COPV with MLVI
- **Redundancy:** Dual pressure relief, multiple sensors
- **Location:** Fuselage center section, above main spar

### 28-10-20: Secondary Storage Tank
- **Function:** Backup/reserve hydrogen storage
- **Capacity:** [TBD] kg LH₂ (emergency reserve)
- **Type:** Type IV COPV with MLVI
- **Redundancy:** Independent from primary system
- **Location:** Fuselage aft section

### 28-10-30: Tank Mounting Structure
- **Function:** Secure attachment to airframe structure
- **Material:** Titanium alloy (Ti-6Al-4V)
- **Design:** Load-distributing cradle design
- **Features:** Thermal isolation, vibration damping
- **Interface:** ATA 53 (Fuselage structure)

### 28-10-40: Vacuum Insulation System
- **Function:** Minimize heat leak to stored LH₂
- **Type:** Multi-layer vacuum insulation (MLVI)
- **Performance:** Effective thermal conductivity < [TBD] W/m·K
- **Maintenance:** Vacuum monitoring, getter replacement
- **Design Life:** 20 years minimum

### 28-10-50: Pressure Relief System
- **Function:** Overpressure protection
- **Components:** Primary relief valve, secondary relief valve, burst disk
- **Set Pressures:** [TBD] bar (primary), [TBD] bar (secondary)
- **Flow Capacity:** [TBD] kg/min gaseous H₂
- **Discharge:** Vented overboard through safe discharge path

### 28-10-60: Tank Filling Interface
- **Function:** Ground service connection for hydrogen refueling
- **Type:** Quick-disconnect coupling (hydrogen-rated)
- **Location:** Accessible ground service panel
- **Safety Features:** Grounding verification, leak detection
- **Interface:** ATA 12 (Ground servicing)

---

## Interfaces

### Mechanical Interfaces
- **ATA 53 (Fuselage):** Structural mounting points, load paths
- **ATA 28-20-00 (Feed Lines):** Outlet connections, thermal expansion

### Thermal Interfaces
- **Cryogenic Environment:** Tank operates at -253°C
- **Ambient Environment:** External surface at ambient
- **Heat Leak Management:** Insulation system, boil-off control

### Electrical Interfaces
- **ATA 24 (Electrical Power):** Sensor power, valve actuation
- **ATA 31 (Instrumentation):** Level, pressure, temperature signals
- **ATA 42 (IMA):** Data acquisition and CAOS integration

### Fluid Interfaces
- **28-20-00 (Feed Lines):** LH₂ outlet to fuel cells
- **28-50-00 (Boil-Off Recovery):** Gaseous H₂ return
- **Atmosphere:** Pressure relief discharge

---

## Safety Analysis Summary

### Critical Hazards (from 02_SAFETY)
1. **Catastrophic hydrogen leak** → Multiple leak detection, auto-isolation
2. **Tank rupture (overpressure)** → Redundant pressure relief, burst disk
3. **Cryogenic exposure** → Personnel protection, ground handling procedures
4. **Hydrogen embrittlement** → Material selection, inspection protocols
5. **Fire/explosion** → Inerting, ventilation, ignition source control

### Failure Modes (FMEA Summary)
- **Single tank failure:** Redundant secondary tank available (degraded ops)
- **Insulation failure:** Increased boil-off, reduced range (detectable)
- **Relief valve failure:** Redundant relief + burst disk (safe)
- **Sensor failure:** Multiple redundant sensors per parameter

---

## CAOS Integration (ATA 40)

### Predictive Maintenance
- **Insulation degradation:** Monitors boil-off rate trends
- **Pressure cycling fatigue:** Tracks fill/drain cycles vs. design life
- **Sensor health:** Calibration drift detection, cross-comparison
- **Vacuum integrity:** Real-time vacuum pressure monitoring

### Digital Twin
- **Physics-based model:** Thermal simulation of tank and insulation
- **Real-time synchronization:** Actual sensor data updates twin
- **Predictive simulation:** Forecast behavior under future conditions

### Fleet Intelligence
- **Performance benchmarking:** Compare tank performance across fleet
- **Failure pattern recognition:** Identify early warning signatures
- **Optimization:** Share best practices for boil-off minimization

---

## Certification Evidence

### EASA CS-25 Compliance
- **CS-25.981:** Fuel tank ignition prevention (adapted for H₂)
- **CS-25.1183:** Flammable fluid fire protection
- **CS-25.1309:** System safety assessment (DAL A)

### Special Conditions
- **SC-H2-001:** Cryogenic hydrogen storage requirements
- **SC-H2-002:** Material compatibility with liquid hydrogen
- **SC-H2-003:** Pressure relief sizing for hydrogen

### Testing Requirements
- **Pressure cycle test:** 1.5× design life (15,000 cycles minimum)
- **Burst test:** > 2.25 × MEOP (certification requirement)
- **Thermal performance:** Validate boil-off rate specification
- **Leak test:** Helium leak detection < [TBD] mbar·L/s
- **Drop test:** Survival of [TBD]g impact (crashworthiness)

---

## Maintenance Plan (from 11_OPERATIONS_AND_MAINTENANCE)

### Daily Inspections
- Visual inspection for frost, leaks, damage
- Leak detector system functional test

### 500 Flight Hours
- Vacuum pressure check (insulation integrity)
- Pressure relief valve operation test
- Sensor calibration verification

### 2000 Flight Hours
- Internal inspection (borescope)
- Non-destructive testing (ultrasonic, radiography)

### 5000 Flight Hours / 5 Years
- Hydrostatic pressure re-test
- Vacuum system refurbishment
- Consider tank replacement or life extension

---

## Example: 6-Digit Recursive Structure

Each 6-digit subsystem (e.g., 28-10-10) contains its own 14-folder structure:

```
28-10-10_PRIMARY_TANK/
├── 01_OVERVIEW/          # Tank architecture, key dimensions
├── 02_SAFETY/            # Tank-specific safety analysis
├── 03_REQUIREMENTS/      # Tank performance requirements
├── 04_DESIGN/            # Tank CAD models, drawings
├── 05_INTERFACES/        # Mounting, fluid, electrical ICDs
├── 06_ENGINEERING/       # FEA stress analysis, thermal modeling
├── 07_V_AND_V/           # Tank qualification test plans
├── 08_PROTOTYPING/       # Prototype tank test results
├── 09_PRODUCTION_PLANNING/ # Tank manufacturing process
├── 10_CERTIFICATION/     # Tank certification deliverables
├── 11_OPERATIONS_AND_MAINTENANCE/ # Tank-specific procedures
├── 12_ASSETS_MANAGEMENT/ # Tank spare parts, tooling
├── 13_SUBSYSTEMS_AND_COMPONENTS/ # 8-digit components breakdown
└── 14_META_GOVERNANCE/   # Tank metadata, traceability
```

---

## Digital Product Passport (ATA 95)

### Tank-Level Tracking
Each tank assembly has a unique DPP entry:

```json
{
  "ata_code": "28-10-10",
  "assembly_serial": "AMPEL-PT-001-00042",
  "aircraft_msn": "AMPEL-BWB-001",
  "manufacture": {
    "manufacturer": "Composite Tanks Inc.",
    "date": "2025-08-15",
    "location": "Facility A, Country"
  },
  "certification": {
    "pressure_test_date": "2025-08-20",
    "burst_pressure": "[TBD] bar",
    "certificates": ["EASA-Form1-2025-001"]
  },
  "lifecycle": {
    "installation_date": "2025-10-01",
    "total_cycles": 127,
    "total_hours": 456.3,
    "last_inspection": "2025-11-10",
    "next_inspection_due": "2026-01-10"
  },
  "components": [
    "28-10-10-01-12345",  # Tank shell S/N
    "28-10-10-04-67890",  # Level sensor S/N
    "28-10-10-06-24680"   # Pressure transducer S/N
  ]
}
```

---

## Weight Breakdown (Preliminary)

| Component | Quantity | Unit Weight (kg) | Total Weight (kg) |
|-----------|----------|------------------|-------------------|
| 28-10-10: Primary Tank | 1 | [TBD] | [TBD] |
| 28-10-20: Secondary Tank | 1 | [TBD] | [TBD] |
| 28-10-30: Mounting Structure | 1 | [TBD] | [TBD] |
| 28-10-40: Insulation System | - | [TBD] | [TBD] |
| 28-10-50: Relief System | - | [TBD] | [TBD] |
| 28-10-60: Fill Interface | 1 | [TBD] | [TBD] |
| **Total (Empty)** | | | **[TBD]** |
| **With LH₂ (Full)** | | | **[TBD]** |

---

## Next Level Documentation

For detailed component-level documentation (8-digit), see:
- `28-10-10_PRIMARY_TANK/13_SUBSYSTEMS_AND_COMPONENTS/`
- `28-10-20_SECONDARY_TANK/13_SUBSYSTEMS_AND_COMPONENTS/`

Each component folder contains full 14-folder lifecycle documentation.

---

**Subsystem Owner:** Propulsion Systems Engineering  
**Safety Classification:** DAL A (Design Assurance Level A - Most Critical)  
**Last Update:** 2025-11-12  
**Generated by:** AMPEL360 Documentation Expert Agent
