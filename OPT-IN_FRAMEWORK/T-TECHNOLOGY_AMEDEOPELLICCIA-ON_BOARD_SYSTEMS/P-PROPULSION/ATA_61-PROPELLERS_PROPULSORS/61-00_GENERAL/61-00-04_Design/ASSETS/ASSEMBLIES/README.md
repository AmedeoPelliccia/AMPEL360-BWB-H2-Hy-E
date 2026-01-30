# ASSEMBLIES — ATA 61 Propellers/Propulsors Design Assets

**Purpose**: This directory contains hierarchical CAD assembly structures for the AMPEL360 BWB H2 Hy-E hybrid electric propulsion system, organized by product category.

## Project Context

The AMPEL360-BWB-H2-Hy-E is a hybrid Blended Wing Body aircraft featuring:

- **H₂ PEM Fuel Cells** — Primary power source
- **Open-Fan Propulsors** — High bypass ratio for efficiency
- **Closed-Loop CO₂ Battery** — Peak-power buffering system
- **SAF Compatibility** — Sustainable Aviation Fuel ready

This assembly structure reflects the electric/hybrid propulsion architecture.

## Structure

### OPEN_FAN_PROPULSOR/

Open-fan propulsor system assemblies including:

- **FAN_ASSEMBLY/** — Fan blades, hub, and spinner assembly
- **NACELLE_ASSEMBLY/** — Nacelle structure and acoustic liners
- **GEARBOX_ASSEMBLY/** — Reduction gearbox (if applicable)
- **PROPULSOR_INTEGRATION/** — Integration of all propulsor components

### ELECTRIC_MOTOR_DRIVE/

Electric motor drive system assemblies:

- **MOTOR_ASSEMBLY/** — High-power electric motor
- **CONTROLLER_ASSEMBLY/** — Motor controller and inverter
- **POWER_DISTRIBUTION_ASSEMBLY/** — HV/LV power distribution

### PROPELLER_VARIANTS/

Alternative propeller configurations:

- **COUNTER_ROTATING_ASSEMBLY/** — Counter-rotating propeller design
- **VARIABLE_PITCH_ASSEMBLY/** — Variable-pitch mechanism assembly

### MOUNTING_ASSEMBLY/

Structural mounting and attachment:

- Engine/propulsor mounting structure
- Pylon interfaces
- Vibration isolation systems

### FULL_PROPULSOR_SYSTEM/

Top-level integrated propulsion system:

- Complete propulsor system assembly
- DMU (Digital Mock-Up) for clash detection and clearance verification

## CAD Directory Structure

Each assembly contains a `CAD/` directory with:

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # .CATProduct files
│   ├── SOLIDWORKS/   # .sldasm files
│   └── NX/           # .prt assembly files
├── NEUTRAL/          # Exchange formats (.step, .jt)
├── VISUALIZATION/    # Lightweight viewing (.stl, .3dpdf)
├── RENDERS/          # Visual documentation (.png, .gif)
└── DMU/              # Digital Mock-Up (top-level only)
```

## Naming Convention for CAD Products

All CAD files follow the pattern:

```
[SYSTEM]_[SUBSYSTEM]_ASSY.[extension]
```

### Examples

| CAD System   | Extension     | Example                              |
|--------------|---------------|--------------------------------------|
| CATIA V5/V6  | .CATProduct   | FAN_ASSY.CATProduct                 |
| SOLIDWORKS   | .sldasm       | MOTOR_ASSY.sldasm                   |
| Siemens NX   | .prt          | GEARBOX_ASSY.prt                    |
| STEP         | .step/.stp    | PROPULSOR_SYSTEM_TOP_ASSY.step      |
| JT           | .jt           | NACELLE_ASSY.jt                     |
| STL          | .stl          | FAN_BLADE_VIZ.stl                   |
| 3D PDF       | .3dpdf        | MOTOR_DRIVE_3D.3dpdf                |

## Part References

Individual parts are stored separately in the PARTS directory:

```
../PARTS/
```

Assemblies reference parts using relative paths. When working with assemblies, ensure the PARTS directory is accessible in your CAD system's search paths.

## Assembly Hierarchy

```
FULL_PROPULSOR_SYSTEM (A400)
├── OPEN_FAN_PROPULSOR (A401)
│   ├── FAN_ASSEMBLY (A410)
│   ├── NACELLE_ASSEMBLY (A420)
│   ├── GEARBOX_ASSEMBLY (A430)
│   └── PROPULSOR_INTEGRATION (A440)
├── ELECTRIC_MOTOR_DRIVE (A450)
│   ├── MOTOR_ASSEMBLY (A451)
│   ├── CONTROLLER_ASSEMBLY (A452)
│   └── POWER_DISTRIBUTION_ASSEMBLY (A453)
├── PROPELLER_VARIANTS (A460)
│   ├── COUNTER_ROTATING_ASSEMBLY (A461)
│   └── VARIABLE_PITCH_ASSEMBLY (A462)
└── MOUNTING_ASSEMBLY (A470)
```

## Export Settings

### STEP Export (AP214/AP242)

- **Format**: AP242 Managed Model-Based 3D Engineering (preferred)
- **Fallback**: AP214 Automotive Design
- **Include**: Assembly structure, colors, PMI (if supported)

### JT Export

- **Version**: JT 10.5 or later
- **LOD Levels**: Include at least 2 LOD levels for visualization

### STL Export

- **Resolution**: Fine (chord deviation ≤ 0.01mm for visualization)
- **Format**: Binary (for smaller file size)

### 3D PDF Export

- **Include**: Assembly tree, cross-sections, annotations
- **Template**: Use AMPEL360 standard 3D PDF template

## Traceability

All assemblies must trace to:

- **Requirements**: In `../../../61-00-03_Requirements/`
- **Verification**: In `../../../61-00-07_V_AND_V/`
- **Interfaces**: In `../../../61-00-05_Interfaces/`
- **Drawings**: In `../DRAWINGS/`

## Related Documents

- [Design Principles](../../README.md)
- [AMPEL360 Assets Standard](../../../../../../../AMPEL360_ASSETS_STANDARD.md)
- [Parts Directory](../PARTS/README.md)
- [Drawings Directory](../DRAWINGS/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
