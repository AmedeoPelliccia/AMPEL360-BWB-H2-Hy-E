# CFD Cruise Analysis Setup - Mach 0.82 at FL410

**Analysis:** AMPEL360 Q100 Cruise Performance  
**Software:** ANSYS Fluent  
**Status:** Setup Template

## Flight Condition

- **Mach:** 0.82
- **Altitude:** 41,000 ft (12,497 m)
- **Temperature:** ISA (-56.5°C, 216.65 K)
- **Pressure:** 18.75 kPa
- **Reynolds number:** 45 million (based on MAC)

## Computational Setup

### Mesh
- **Type:** Hybrid unstructured (tetrahedra + prism layers)
- **Cells:** ~25 million
- **y+:** < 1 (wall-resolved)
- **Domain:** 20× aircraft length

### Solver Settings
- **Solver:** Pressure-based, coupled
- **Turbulence:** k-ω SST
- **Discretization:** 2nd order upwind
- **Convergence:** Residuals < 10⁻⁶

## Expected Results

- Lift coefficient: CL ~0.52
- Drag coefficient: CD < 0.022
- L/D > 23
- Shock wave location and strength on upper surface

## Files Location

Case files stored in: `case_files/cruise_m082_41000ft/`
