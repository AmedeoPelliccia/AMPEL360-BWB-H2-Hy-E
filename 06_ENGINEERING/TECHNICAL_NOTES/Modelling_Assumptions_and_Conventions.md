# Modelling Assumptions and Conventions

**Document ID:** 02-11-00-TN-001  
**Revision:** A  
**Date:** 2025-11-10  
**Status:** Draft

## 1. Purpose

This Technical Note establishes standard modelling assumptions, conventions, and practices to be followed across all engineering analyses for the AMPEL360 Q100 aircraft. It ensures consistency and traceability across structural, aerodynamic, weight & balance, performance, and certification analyses.

**All analysts must review and adhere to this document before commencing any analysis work.**

## 2. Scope

This document applies to:
- Finite Element Analysis (FEM)
- Computational Fluid Dynamics (CFD)
- Performance and mission analysis
- Weight and balance calculations
- Hand calculations and spreadsheets
- Trade studies and design evaluations

## 3. General Assumptions

### 3.1 Aircraft Configuration

**Baseline Configuration:**
- Blended Wing Body (BWB) layout
- Hydrogen fuel cell propulsion (2× fuel cell nacelles)
- Passenger capacity: 220 seats (single class)
- Design range: 8,000 km
- Design cruise Mach: 0.82
- Design cruise altitude: 41,000 ft (FL410)

**Frozen Configuration Date:** TBD  
After this date, configuration changes require formal change control and re-analysis.

### 3.2 Design Point

Unless otherwise stated, all analyses use the following design point:
- Altitude: 41,000 ft (12,497 m)
- Mach number: 0.82
- Weight: Maximum Cruise Weight (MCW) = TBD kg
- CG position: Mid-CG (TBD% MAC)
- ISA+10°C temperature deviation

### 3.3 Environmental Conditions

**Standard Atmosphere:**
- ISA (International Standard Atmosphere) per ISO 2533
- Sea level: T = 15°C, P = 101.325 kPa
- Temperature lapse rate: -6.5°C/km (troposphere)

**Design Envelopes:**
- Operating temperature: -55°C to +50°C
- Humidity: 0% to 100% RH
- Icing conditions per CS-25 Appendix C

**Extreme Temperatures (for material properties):**
- Cold Day (CD): ISA -35°C
- Hot Day (HD): ISA +35°C

### 3.4 Mass Cases

Standard mass cases for analysis (see WB-002 for detailed breakdown):

| Mass Case | Total Mass (kg) | CG (%MAC) | Use |
|-----------|-----------------|-----------|-----|
| OEW (Operating Empty Weight) | TBD | TBD | Structural baseline |
| MZFW (Max Zero Fuel Weight) | TBD | TBD | Cabin loads, ground handling |
| MLW (Max Landing Weight) | TBD | TBD | Landing loads |
| MTOW (Max Takeoff Weight) | TBD | TBD | Takeoff, maneuver loads |
| MCW (Max Cruise Weight) | TBD | TBD | Cruise performance |

**Note:** Each mass case includes appropriate fuel, payload, and consumables distributions.

## 4. Coordinate Systems

Coordinate systems are defined in detail in TN-002. Summary:

- **Aircraft Body Axes:** Origin at nose apex, X-aft, Y-right, Z-down
- **Units:** Meters (m) for lengths, kilograms (kg) for mass, newtons (N) for force
- **Right-hand rule** applies to all coordinate systems

## 5. Structural Analysis Assumptions

### 5.1 Material Properties

**Reference:** TN-004 (Materials_Allowables_Selection.md)

**Key Assumptions:**
- **Allowables:** A-basis for flight-critical structure, B-basis for non-critical
- **Knockdown Factors:** Applied per TN-004 for temperature, moisture, etc.
- **Temperature Conditions:**
  - Room Temperature Dry (RTD): 20°C, 0% RH
  - Elevated Temperature (ETW): 70°C, wet
  - Cold Temperature Dry (CTD): -55°C, 0% RH

**Fatigue and Damage Tolerance:**
- S-N curves from material handbooks (MMPDS, CMH-17)
- Crack growth data from NASGRO database
- Initial flaw sizes per AC 25.571-1D

### 5.2 Load Factors

**Flight Load Factors (per CS-25.337):**
- Positive limit: +2.5g at VC (clean), +2.0g (flaps extended)
- Negative limit: -1.0g at VC (clean)
- Positive ultimate: +3.8g at VA
- Negative ultimate: -1.5g at VA

**Ground Load Factors:**
- Level landing: nz = TBD (per CS-25.479)
- Tail-down landing: nz = TBD (per CS-25.481)
- Emergency landing: nx = ±9g, ny = ±3g, nz = -3g (per CS-25.561)

**Factor of Safety:** 1.5 (Ultimate = 1.5 × Limit per CS-25.303)

### 5.3 Load Cases

**Reference:** TN-003 (Load_Case_Definition_and_Combinations.md)

**Standard Combinations:**
- Flight loads = Maneuver OR Gust + Pressurization
- Ground loads = Landing/Taxi reactions + Inertia relief
- Emergency = Crash loads per CS-25.561

**Load Case Numbering:**
- LC-F-xxx: Flight loads
- LC-G-xxx: Ground loads
- LC-P-xxx: Pressurization loads
- LC-E-xxx: Emergency loads

### 5.4 Boundary Conditions

**Symmetric Models:**
- Y = 0 plane: Uy = Rx = Rz = 0 (symmetry)

**Landing Gear:**
- Represented as spring elements with appropriate stiffness
- Main gear stiffness: TBD kN/mm (vertical)
- Nose gear stiffness: TBD kN/mm (vertical)

**Fuel Cell Nacelles:**
- Modeled as lumped masses at attachment points
- Nacelle mass per unit: TBD kg

### 5.5 Failure Criteria

**Metallic Materials:**
- von Mises stress ≤ Fty (yield) for limit load
- von Mises stress ≤ Ftu (ultimate) for ultimate load
- Maximum principal stress ≤ Ftu (for brittle failure modes)

**Composite Materials:**
- Tsai-Wu failure criterion
- Maximum strain criterion: ε ≤ 0.004 (0.4%)
- Delamination: Quadratic stress criterion

**Margin of Safety:**
```
MS = (Allowable / Applied) - 1
```
- MS ≥ 0: Pass
- MS < 0: Fail (redesign required)

## 6. Aerodynamic Analysis Assumptions

### 6.1 CFD Assumptions

**Solver Settings:**
- Turbulence model: k-ω SST (Shear Stress Transport)
- Compressible flow: Ideal gas law
- Transition model: γ-Reθ (if transition effects significant)

**Boundary Conditions:**
- Far-field: Pressure far-field (Mach, AoA, T specified)
- Surface: No-slip wall, adiabatic (unless thermal analysis)
- Symmetry: XZ plane for symmetric cases

**Mesh Quality:**
- y+ < 1 for first cell (wall-resolved LES/RANS)
- Growth ratio: ≤ 1.2
- Aspect ratio: ≤ 100 in boundary layer, ≤ 5 in wake

**Convergence Criteria:**
- Residuals: < 10⁻⁶ for continuity, momentum, energy
- Forces: Variation < 0.1% over 500 iterations

### 6.2 Aerodynamic Coefficients

**Sign Conventions (per TN-002):**
- CL: Positive lift upward
- CD: Positive drag aft
- CM: Positive pitch-up
- Cy: Positive side force right
- Cl: Positive roll right-wing-down
- Cn: Positive yaw nose-right

**Reference Values:**
- Reference area (Sref): TBD m²
- Reference chord (cref = MAC): TBD m
- Reference span (bref): TBD m

**Typical Values (for validation):**
- Cruise: CL ≈ 0.52, CD ≈ TBD, L/D ≈ TBD
- Max L/D: CL ≈ TBD, L/D_max ≈ TBD

### 6.3 High-Lift Devices

**Flap Settings:**
- Clean (cruise): 0°
- Takeoff (TO): TBD° (LE slat + TE flap)
- Landing (LDG): TBD° (LE slat + TE flap)

**CLmax Targets:**
- Clean: CLmax ≈ 1.2
- TO config: CLmax ≈ 2.0
- LDG config: CLmax ≈ 2.5

## 7. Weight and Balance Assumptions

### 7.1 Mass Properties

**Reference:** WB-002 (Weight_Distribution.md)

**Weight Breakdown:**
- Per ATA chapter
- Including systems, structure, propulsion, furnishings, operational items

**CG Calculation:**
- Component-level CG positions from CAD or estimates
- Total CG = Σ(mi × ri) / Σ(mi)

**Inertia Calculation:**
- Principal moments of inertia (Ixx, Iyy, Izz)
- Products of inertia (Ixy, Ixz, Iyz) if significant
- Parallel axis theorem for component contributions

### 7.2 Fuel Density

**Liquid Hydrogen (LH₂):**
- Density: 70.8 kg/m³ at 20 K, 1 atm
- Boil-off rate: TBD% per hour (depends on insulation)
- Usable fuel: 95% of tank volume (5% ullage)

**Sustainable Aviation Fuel (SAF) - if used:**
- Density: 800 kg/m³ (typical)

### 7.3 Payload Assumptions

**Passenger Weight:**
- Per passenger (including baggage): 100 kg
- Seat pitch: 32 inches (0.813 m)
- Seats abreast: TBD

**Cargo:**
- Cargo density: 160 kg/m³ (typical mixed cargo)

## 8. Performance Analysis Assumptions

### 8.1 Propulsion System

**Fuel Cell Performance:**
- Maximum power per nacelle: TBD kW
- Fuel cell efficiency: TBD% (varies with power setting)
- Specific fuel consumption (SFC): TBD kg/kWh

**Thrust Model:**
- Thrust = f(altitude, Mach, power setting)
- Data source: Fuel cell manufacturer / preliminary design

### 8.2 Mission Profile

**Standard Mission:**
1. Taxi: 10 min
2. Takeoff: To 1,500 ft AGL
3. Climb: To cruise altitude (FL410)
4. Cruise: At M0.82, constant altitude or step climb
5. Descent: To 1,500 ft AGL at destination
6. Landing and taxi: 10 min

**Reserves:**
- Alternate: 200 NM at cruise
- Hold: 30 min at 1,500 ft AGL
- Final reserve: 5% of trip fuel

### 8.3 Drag Polar

**Form:** CD = CD0 + K × CL²

Where:
- CD0: Zero-lift drag coefficient (from CFD or estimation)
- K: Induced drag factor = 1 / (π × AR × e)
- AR: Aspect ratio ≈ TBD
- e: Oswald efficiency factor ≈ TBD (BWB typically 0.85-0.95)

**Drag Breakdown:** See AERO-003 for detailed component drag.

## 9. Simulation Tool Conventions

### 9.1 FEM (Finite Element Method)

**Software:** NASTRAN (MSC or NX) or ANSYS Mechanical

**Standard Practices:**
- Use SOL 101 (Linear Statics) for most load cases
- Use SOL 103 (Normal Modes) for flutter pre-analysis
- Use SOL 106 (Nonlinear Statics) for large deflections, if needed

**Verification:**
- Check model mass vs expected mass (±1%)
- Check CG location vs expected (±50 mm)
- Run simple hand-check load cases

### 9.2 CFD (Computational Fluid Dynamics)

**Software:** ANSYS Fluent or OpenFOAM

**Standard Practices:**
- Double precision solver
- Second-order spatial discretization (minimum)
- Coupled pressure-velocity solver for compressible flow

**Post-Processing:**
- Extract forces and moments (CL, CD, CM)
- Check residuals and force convergence
- Generate surface Cp plots and streamline visualizations

### 9.3 Performance Simulations

**Software:** MATLAB/Simulink or Python

**Standard Practices:**
- ODE solver: ode45 or equivalent
- Time step: Adaptive, max TBD seconds
- Integration tolerance: 10⁻⁶

## 10. Uncertainty and Sensitivity

### 10.1 Uncertainty Factors

When performing sensitivity studies, consider:
- Structural: Material properties ±10%, mass ±5%
- Aerodynamic: CD ±5%, CL ±3%
- Propulsion: SFC ±10%, thrust ±5%
- Weight: OEW ±3%, payload as required

### 10.2 Validation and Verification

**Reference:** TN-005 (Verification_and_Validation_Strategy.md)

**Standard Checks:**
- **V&V Plan:** Each analysis includes verification and validation plan
- **Independent Check:** All analyses peer-reviewed by independent engineer
- **Benchmarking:** Compare against known solutions, test data, or handbook methods

## 11. Documentation Standards

### 11.1 Analysis Reports

All analysis reports shall include:
1. Executive summary
2. Scope and objectives
3. Methodology and assumptions
4. Results with tables and figures
5. Compliance statement (if certification-related)
6. References

**Format:** Markdown (.md) for easy version control and readability

### 11.2 Calculation Sheets

**Format:** CSV for data tables, Excel for complex calculations with checks

**Required Information:**
- Input parameters with units
- Calculation steps with intermediate results
- Output summary with units
- Verification check (hand-check or benchmark)

### 11.3 Units

**Primary Units:**
- Length: meters (m), millimeters (mm)
- Mass: kilograms (kg)
- Force: newtons (N), kilonewtons (kN)
- Pressure: pascals (Pa), megapascals (MPa)
- Stress: megapascals (MPa)
- Temperature: degrees Celsius (°C) or Kelvin (K)

**Conversions:**
- 1 kN = 1,000 N
- 1 MPa = 1 N/mm² = 145 psi
- 1 m/s = 1.944 knots

**Always explicitly state units in all calculations and results.**

### 11.4 Significant Figures

- Input data: Use as many digits as provided
- Intermediate calculations: Maintain at least 4 significant figures
- Final results: Round to appropriate precision (typically 3-4 significant figures)
- Margins of safety: Report to 2 decimal places (e.g., MS = 0.15)

## 12. Change Control and Deviations

### 12.1 Deviations from This Document

Any deviation from these standard assumptions must be:
1. **Documented:** State deviation clearly in analysis report
2. **Justified:** Provide technical rationale
3. **Approved:** By discipline lead and chief engineer
4. **Tracked:** In deviation log (TBD location)

### 12.2 Updates to This Document

This document is living and will be updated as the design matures.

**Update Process:**
1. Propose change via technical note revision request
2. Review by all discipline leads
3. Approval by chief engineer
4. Issue new revision with revision history updated
5. Notify all analysts of change

## 13. Traceability

### 13.1 Related Documents

This Technical Note is referenced by:
- All documents in ANALYSIS_REPORTS/
- All documents in CALCULATIONS/
- All documents in SIMULATIONS/
- TN-002 through TN-005

### 13.2 Upstream References

- 03_REQUIREMENTS/ - System requirements
- 04_DESIGN/ - Design definition
- TRADE_STUDIES/ - Design decisions

## 14. Compliance with Standards

This Technical Note ensures compliance with:
- CS-25: Load definitions, factor of safety, material properties
- ARP-4754A: Development assurance
- Company quality procedures

See Analysis_Standards_Applied.csv for full standards list.

## 15. Required Visualizations

The following PNG visualization should be created:

- **02-11-00-TN-001-FIG-01_Assumptions_VModel.png**
  - V-model style diagram showing: Assumptions → Models → Results
  - Verification and validation loops
  - Traceability flow

## 16. Revision History

| Revision | Date | Author | Description |
|----------|------|--------|-------------|
| A | 2025-11-10 | Engineering Team | Initial release |

---

**APPROVAL:**
- **Prepared by:** TBD - Methods & Tools Lead
- **Reviewed by:** TBD - All Discipline Leads
- **Approved by:** TBD - Chief Engineer

**END OF DOCUMENT**
