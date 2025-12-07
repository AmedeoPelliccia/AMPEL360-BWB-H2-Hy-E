# MODEL_LIBRARY

**Purpose**: Shared resources for analytical models including material properties, airfoil definitions, and standard operating conditions.

---

## Overview

The Model Library provides reusable, validated data for use across all domain models:

- **MATERIALS/** — Material property definitions (mechanical, thermal, electromagnetic)
- **AIRFOILS/** — Airfoil coordinate and performance data
- **STANDARD_CONDITIONS/** — Reference atmospheric and operating conditions

---

## Subdirectories

### MATERIALS/

Material property YAML files for structural, thermal, and electromagnetic analysis:

| File | Material | Primary Use |
|------|----------|-------------|
| Q100-61-MAT-COMPOSITE-CFRP.yaml | Carbon fiber reinforced polymer | Fan blades |
| Q100-61-MAT-TITANIUM-TI6AL4V.yaml | Titanium Ti-6Al-4V | Disk, hub |
| Q100-61-MAT-ALUMINUM-7075.yaml | Aluminum 7075-T6 | Housing, nacelle |
| Q100-61-MAT-STEEL-4340.yaml | AISI 4340 steel | Gears, shafts |
| Q100-61-MAT-COPPER-WINDING.yaml | Electrolytic copper | Motor windings |
| Q100-61-MAT-NDFEB-MAGNET.yaml | NdFeB N48SH | Permanent magnets |
| Q100-61-MAT-SILICON-STEEL.yaml | M19 electrical steel | Motor laminations |

### AIRFOILS/

Airfoil definitions for blade aerodynamic analysis:

| File | Airfoil | Application |
|------|---------|-------------|
| Q100-61-AFL-FAN-ROOT.yaml | Fan blade root section | 20-40% span |
| Q100-61-AFL-FAN-MID.yaml | Fan blade mid section | 40-70% span |
| Q100-61-AFL-FAN-TIP.yaml | Fan blade tip section | 70-100% span |
| Q100-61-AFL-PROP-FWD.yaml | Forward propeller blade | Open-fan forward |
| Q100-61-AFL-PROP-AFT.yaml | Aft propeller blade | Open-fan aft |

### STANDARD_CONDITIONS/

Reference operating conditions for analysis:

| File | Condition | Description |
|------|-----------|-------------|
| Q100-61-COND-SEA-LEVEL.yaml | ISA Sea Level | Standard day at SL |
| Q100-61-COND-CRUISE-FL350.yaml | Cruise FL350 | Design cruise point |
| Q100-61-COND-HOT-DAY.yaml | ISA+15°C Hot Day | High temperature ops |
| Q100-61-COND-COLD-DAY.yaml | ISA-30°C Cold Day | Low temperature ops |

---

## YAML File Structure

### Material Properties Template

```yaml
material_id: Q100-61-MAT-XXX
material_name: Material Name
category: STRUCTURAL | THERMAL | ELECTROMAGNETIC
specification: Industry specification (e.g., AMS 4911)

mechanical:
  density_kg_m3: 0000
  youngs_modulus_GPa: 000
  poissons_ratio: 0.00
  yield_strength_MPa: 000
  ultimate_strength_MPa: 000
  elongation_percent: 00
  fatigue_limit_MPa: 000

thermal:
  conductivity_W_mK: 00.0
  specific_heat_J_kgK: 000
  expansion_coeff_1_K: 0.0e-6
  max_service_temp_C: 000

electromagnetic:  # if applicable
  resistivity_ohm_m: 0.0e-8
  relative_permeability: 1.0
  
source: Reference standard or test data
status: Approved | Draft
```

### Airfoil Template

```yaml
airfoil_id: Q100-61-AFL-XXX
airfoil_name: Airfoil Name
family: Fan | Propeller
span_location: root | mid | tip

geometry:
  chord_m: 0.000
  max_thickness_percent: 00.0
  max_camber_percent: 0.0
  coordinates_file: coordinates.csv  # x/c, y_upper/c, y_lower/c

performance:
  design_cl: 0.0
  design_aoa_deg: 0.0
  design_mach: 0.0
  cl_max: 0.0
  cd_min: 0.0000
  
source: Design optimization or reference airfoil
status: Approved | Draft
```

### Standard Conditions Template

```yaml
condition_id: Q100-61-COND-XXX
condition_name: Condition Name
isa_deviation_C: 0

atmosphere:
  altitude_m: 0000
  pressure_Pa: 00000
  temperature_K: 000.0
  density_kg_m3: 0.000
  speed_of_sound_m_s: 000.0
  viscosity_Pa_s: 0.00e-5

flight:
  mach: 0.00
  true_airspeed_m_s: 000.0
  
source: ISA model, test conditions
status: Approved
```

---

## Usage Guidelines

1. **Referencing Library Elements**:
   - In model_definition.yaml, reference by ID:
     ```yaml
     materials:
       - ref: Q100-61-MAT-COMPOSITE-CFRP
         component: fan_blade
     ```

2. **Adding New Materials**:
   - Create YAML file following naming convention
   - Include all relevant property categories
   - Cite source standards or test reports
   - Set status to Draft until approved

3. **Validation**:
   - Material properties must trace to specifications
   - Airfoil data must be validated against CFD/test
   - Conditions must comply with ISA model

---

## Traceability

- Requirements: See `61-00-03_Requirements/`
- Material Specifications: See vendor/standards references in each file
- Test Data: See `61-00-07_V_AND_V/` for material test reports

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
