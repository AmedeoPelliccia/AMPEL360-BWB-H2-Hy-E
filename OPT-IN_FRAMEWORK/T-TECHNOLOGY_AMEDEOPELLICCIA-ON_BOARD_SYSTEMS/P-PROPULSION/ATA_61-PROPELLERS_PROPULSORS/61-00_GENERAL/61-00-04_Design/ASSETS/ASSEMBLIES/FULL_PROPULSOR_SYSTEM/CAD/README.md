# CAD Directory — FULL_PROPULSOR_SYSTEM

**Parent Assembly**: 61-00-04-A400 (FULL_PROPULSOR_SYSTEM)

## Directory Structure

This is the top-level assembly CAD directory and includes a **DMU** (Digital Mock-Up) subdirectory for system-level studies.

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # .CATProduct files
│   ├── SOLIDWORKS/   # .sldasm files
│   └── NX/           # .prt assembly files
├── NEUTRAL/          # Exchange formats
├── VISUALIZATION/    # Lightweight viewing formats
├── RENDERS/          # Visual documentation
└── DMU/              # Digital Mock-Up studies
    ├── CLASH_STUDIES/         # Interference detection results
    ├── CLEARANCE_CHECKS/      # Clearance verification
    └── INSTALLATION_SEQUENCES/ # Assembly sequence studies
```

## Naming Convention

```
PROPULSOR_SYSTEM_[VARIANT]_ASSY.[extension]
```

### Expected Files

| File Name | Description |
|-----------|-------------|
| PROPULSOR_SYSTEM_TOP_ASSY.* | Complete propulsor system assembly |
| PROPULSOR_SYSTEM_Q100_ASSY.* | Q100 variant configuration |
| PROPULSOR_SYSTEM_Q120_ASSY.* | Q120 variant configuration |

## DMU Studies

The DMU directory contains digital mock-up studies for:

### Clash Studies

- Interference detection between assemblies
- Dynamic clash during operation
- Tool access verification

### Clearance Checks

- Minimum clearances to structure
- Thermal expansion allowances
- Service access verification

### Installation Sequences

- Build sequence animation
- Tooling requirements
- Removal/replacement procedures

## Export Settings

### STEP Export (AP242)

- **Format**: AP242 Managed Model-Based 3D Engineering
- **Include**: Full assembly structure, colors, PMI
- **File**: `PROPULSOR_SYSTEM_TOP_ASSY.step`

### JT Export

- **Version**: JT 10.5+
- **LOD**: Multiple levels for DMU visualization
- **File**: `PROPULSOR_SYSTEM_TOP_ASSY.jt`

## Part References

All parts and sub-assemblies are linked from:

```
../../../../PARTS/
../OPEN_FAN_PROPULSOR/
../ELECTRIC_MOTOR_DRIVE/
../PROPELLER_VARIANTS/
../MOUNTING_ASSEMBLY/
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
