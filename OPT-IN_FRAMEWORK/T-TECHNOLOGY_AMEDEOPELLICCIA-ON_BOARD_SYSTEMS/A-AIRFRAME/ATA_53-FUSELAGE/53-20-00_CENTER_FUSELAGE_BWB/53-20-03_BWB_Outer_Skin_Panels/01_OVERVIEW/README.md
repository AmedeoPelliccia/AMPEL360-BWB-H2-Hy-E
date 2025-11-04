# 53-20-03 BWB Outer Skin Panels

## Component Overview

The BWB outer skin panels form the primary aerodynamic and pressure-containing surface of the AMPEL360 center body. These large-area composite panels are critical for structural integrity, cabin pressurization, and aerodynamic performance.

### Key Functions
- Aerodynamic surface continuity (smooth outer mold line)
- Cabin pressure containment (8.5 psi differential)
- Load distribution to circumferential frames and stringers
- Environmental protection (moisture, thermal, acoustic)
- Electromagnetic interference (EMI) shielding
- Attachment for windows, doors, and systems penetrations

### Configuration
- **Coverage Area:** 450 m² (total outer skin surface)
- **Panel Size:** Typical 3m × 2m (optimized for manufacturing and transport)
- **Construction:** Carbon fiber sandwich with honeycomb core
- **Curvature:** Variable radius (8m to 20m) following BWB contour

### Design Characteristics
- **Material:** T800/M21 CFRP prepreg
- **Face Sheet Thickness:** 4 plies (2mm) inner and outer
- **Core:** Nomex honeycomb 25mm thick (48 kg/m³)
- **Total Thickness:** 29mm
- **Weight:** 4.67 kg/m² (2,100 kg total for all panels)

### Critical Interfaces
- **Circumferential Frames (53-20-04):** Bonded and fastened joints every 500mm
- **Longitudinal Stringers (53-20-05):** Co-bonded or secondarily bonded
- **Window Cutouts (ATA 56):** Reinforced doubler frames
- **Door Cutouts (ATA 52):** Heavy reinforcement and fail-safe design
- **Wing Blend (53-50):** Smooth transition to wing structure

### Operational Environment
- **Temperature Range:** -55°C to +85°C (outer surface)
- **Pressure Differential:** 8.5 psi nominal, 17 psi ultimate
- **Acoustic Environment:** 140 dB OASPL (takeoff/landing)
- **Thermal Cycling:** 2 cycles per flight
- **Moisture Exposure:** Rain, humidity, condensation

## CAOS Integration

### Distributed Sensing Network
- **Fiber Optic Sensors:** 2 km total length, distributed strain sensing
- **Coverage:** All critical panel areas and joints
- **Sampling:** 0.1m spatial resolution, 10 Hz temporal
- **Damage Detection:** Delamination, disbonding, crack detection

### Digital Twin Capabilities
- **Load Reconstruction:** Derive applied loads from strain measurements
- **Fatigue Tracking:** Cumulative damage at every sensor location
- **Anomaly Detection:** Machine learning identifies abnormal patterns
- **Fleet Analytics:** Compare degradation across aircraft

### Predictive Maintenance
- **Inspection Optimization:** Risk-based NDT scheduling
- **Repair Planning:** Predict optimal repair timing
- **Spare Parts:** Automated ordering based on fleet trends
- **Downtime Minimization:** Coordinate maintenance with operations

## Structural Health Monitoring

### Damage Tolerance Philosophy
- **Two-Bay Crack Criterion:** Cracks shall not propagate beyond two frame bays before detection
- **Inspection Intervals:** Based on crack growth analysis
- **Residual Strength:** Maintain ultimate load capability with damage
- **Fail-Safe Design:** Multiple load paths, crack arrestors

### Inspection Methods
- **Visual:** Daily walk-around (external surface)
- **Ultrasonic:** C-Check intervals (delamination detection)
- **Thermography:** Specialized inspection (moisture, disbonds)
- **Fiber Optic:** Continuous CAOS monitoring

## Manufacturing Considerations

### Panel Fabrication
- **Process:** Autoclave cure of prepreg layups
- **Quality Control:** Ultrasonic C-scan (100% coverage)
- **Tolerances:** ±0.5mm thickness, ±2mm contour
- **Surface Quality:** Ra < 3.2 μm (aerodynamic requirement)

### Assembly
- **Frame Attachment:** Bonded + mechanical fasteners
- **Stringer Integration:** Co-bonded during panel manufacture
- **Sealant:** Polysulfide sealant at all joints (pressure tight)
- **Inspection:** Leak test at 8.5 psi after assembly

## Related Documents
- **Design:** 04_DESIGN/bwb_skin_panel_design_specification.md
- **Analysis:** 06_ENGINEERING/panel_buckling_analysis.pdf
- **Manufacturing:** 09_PRODUCTION_PLANNING/panel_fabrication_plan.md
- **Certification:** 10_CERTIFICATION/damage_tolerance_substantiation.pdf

## Status
- **Design Phase:** Critical Design Review (CDR) complete
- **Analysis:** Panel sizing complete, MS > 0.15 all locations
- **Manufacturing:** Tool design in progress
- **Certification:** Substantiation in work
