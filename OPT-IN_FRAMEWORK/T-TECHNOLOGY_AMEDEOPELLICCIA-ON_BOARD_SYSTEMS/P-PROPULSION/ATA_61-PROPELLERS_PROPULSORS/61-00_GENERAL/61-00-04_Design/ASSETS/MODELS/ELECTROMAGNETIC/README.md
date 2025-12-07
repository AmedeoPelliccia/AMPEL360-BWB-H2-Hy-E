# ELECTROMAGNETIC Models

**Purpose**: Electromagnetic analysis models for the high power-density permanent magnet synchronous motor (PMSM) used in the propulsor drivetrain.

---

## Overview

This directory contains electromagnetic analysis models supporting:

- Motor sizing and performance prediction
- Efficiency mapping across the torque-speed envelope
- Loss calculation for thermal analysis inputs
- Magnet demagnetization assessment
- Inductance and flux linkage computation

---

## Subdirectories

### MOTOR/

Electric motor electromagnetic models:

| Model ID | Description | Analysis Type |
|----------|-------------|---------------|
| Q100-61-MDL-EM-MOTOR-2D | 2D cross-section EM analysis | 2D FEA |
| Q100-61-MDL-EM-MOTOR-3D | 3D end-region effects | 3D FEA |

#### Q100-61-MDL-EM-MOTOR-2D/

Primary electromagnetic model for motor performance:

- `geometry/` — 2D cross-section geometry
- `materials/` — B-H curves, conductivity data
- `windings/` — Winding layout and connections
- `results/` — Flux density, torque, losses

#### Q100-61-MDL-EM-MOTOR-3D/

Extended model for end-winding and 3D effects:

- `end_effects/` — End-winding inductance, losses

---

## Analysis Methods

### 2D Finite Element Magnetics

- **Software**: ANSYS Maxwell, JMAG, MotorCAD, FEMM
- **Analysis Types**:
  - Magnetostatic (flux density, torque)
  - Transient (cogging, ripple, harmonics)
  - AC loss (eddy currents in windings/magnets)
- **Mesh**: Adaptive refinement in air gap region
- **Post-Processing**: FFT of torque, efficiency maps

### 3D Finite Element Magnetics

- **Software**: ANSYS Maxwell 3D, JMAG
- **Focus**: End-winding inductance, axial flux leakage
- **Use Case**: Refined loss and inductance values

---

## Key Inputs

1. **Geometry**:
   - Stator/rotor dimensions
   - Slot/pole count
   - Air gap length
   - Magnet dimensions and grade

2. **Materials**:
   - Silicon steel laminations (B-H curve, core loss)
   - NdFeB magnets (Br, Hc, temperature coefficients)
   - Copper (resistivity at operating temperature)

3. **Operating Points**:
   - Current magnitude and phase angle
   - Speed range (0 to max RPM)
   - Temperature (for material property adjustment)

---

## Key Outputs

1. **Torque-Speed Characteristic**: Peak and continuous torque vs. speed
2. **Efficiency Map**: η = f(torque, speed) including:
   - Copper losses (DC + AC)
   - Iron losses (hysteresis + eddy current)
   - Magnet losses
   - Stray load losses
3. **Flux Density Plots**: B-field in teeth, yoke, air gap
4. **Cogging Torque**: Amplitude and spatial frequency
5. **Torque Ripple**: Percentage of rated torque
6. **Inductances**: Ld, Lq for control model
7. **Back-EMF Waveform**: Harmonic content

---

## Material References

See `MODEL_LIBRARY/MATERIALS/` for:

- Q100-61-MAT-SILICON-STEEL (laminations)
- Q100-61-MAT-NDFEB-MAGNET (permanent magnets)
- Q100-61-MAT-COPPER-WINDING (stator windings)

---

## Integration with Other Models

- **Thermal Models**: Loss maps → heat sources for Q100-61-MDL-THM-MOTOR
- **Control Models**: Inductances → plant model for Q100-61-MDL-DYN-MOTOR-CONTROL
- **Performance Models**: Efficiency maps → Q100-61-MDL-PERF-PROPULSOR

---

## Traceability

- Requirements: See `61-00-03_Requirements/`
- Motor Subsystem: See `61-20-01_Electric_Motor/`
- Certification: CS-25.1309 (continued safe operation)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-05
