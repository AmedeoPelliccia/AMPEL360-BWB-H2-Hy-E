# Engineering Analysis: 06-10-01 - Overall Dimensions

## Purpose
This folder contains engineering analysis, calculations, and simulation results related to the overall dimensions of the AMPEL360 aircraft.

## Analysis Areas

### 1. Structural Analysis
- Wing deflection under aerodynamic loads (FEA)
- Center body pressurization stress analysis
- Thermal expansion/contraction analysis (LH₂ effects)
- Manufacturing tolerance stack-up analysis

### 2. Aerodynamic Analysis
- Lift-to-drag ratio optimization (CFD)
- Aspect ratio trade studies
- Ground effect analysis
- Propulsor inlet flow quality

### 3. Performance Analysis
- Mission performance calculations (range, payload)
- Takeoff/landing field length calculations
- Fuel burn optimization
- Weight vs. performance trade-offs

### 4. Manufacturing Analysis
- Dimensional tolerance analysis
- Assembly jig design verification
- Transportation constraints (road, rail, barge)
- Tooling compatibility assessment

## Analysis Tools
- **CATIA V6:** CAD geometry and digital mockup
- **ANSYS Mechanical:** Structural FEA
- **MSC Nastran:** Detailed stress analysis
- **STAR-CCM+:** Computational Fluid Dynamics
- **MATLAB:** Performance calculations and optimization

## Key Analysis Results

### Wing Deflection
- +2.5g: 850mm upward wingtip deflection (1.3% span)
- -1.0g: 320mm downward wingtip deflection
- Ultimate load test: No permanent deformation up to 1.5× limit load

### Thermal Effects
- +50°C ambient: +12mm wingspan expansion
- -20°C cruise: -8mm wingspan contraction
- LH₂ tank region: -10mm local contraction at -253°C

### Tolerance Stack-Up
- Overall dimensions: ±50mm manufacturing tolerance
- Critical interfaces: ±5mm tolerance
- As-built measurement: ±2mm laser tracker accuracy

## Analysis Reports
- **AR-06-001:** Wing Structural Analysis
- **AR-06-002:** Aerodynamic Performance Analysis (CFD)
- **AR-06-003:** Thermal Expansion Analysis
- **AR-06-004:** Manufacturing Tolerance Analysis
- **AR-06-005:** Mission Performance Calculations

## Document Status
**Status:** Approved  
**Last Review:** 2025-11-01  
**Next Review:** 2026-05-01
