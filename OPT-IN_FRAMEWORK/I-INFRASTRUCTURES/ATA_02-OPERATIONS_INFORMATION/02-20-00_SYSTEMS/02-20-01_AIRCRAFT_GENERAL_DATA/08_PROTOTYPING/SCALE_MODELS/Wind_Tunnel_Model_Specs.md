# Wind Tunnel Model Specifications
# 1:10 Scale BWB Model Technical Specifications

**Document ID:** WTM-02-10-001  
**Version:** 2.0  
**Date:** 2025-09-15  
**Status:** As-Built  
**Classification:** Engineering Reference

---

## 1. Model Overview

### 1.1 General Information

**Model Designation:** AMPEL360-BWB-WT-001  
**Scale Ratio:** 1:10  
**Purpose:** Low-speed aerodynamic validation, geometry verification  
**Fabrication:** CNC Technologies GmbH, Munich  
**Delivery Date:** 2025-09-30  
**Cost:** €45,000

### 1.2 Design Requirements

| Requirement | Specification | Verification |
|-------------|--------------|--------------|
| Geometric Accuracy | ±0.5 mm from nominal | ✅ Photogrammetry |
| Surface Finish | Ra < 1.6 μm (smooth) | ✅ Surface profiler |
| Structural Integrity | 1.5 × max wind load | ✅ Load test |
| Instrumentation | 256 pressure taps minimum | ✅ 256 installed |
| Weight Target | 48 kg ± 2 kg | ✅ 47.5 kg |

---

## 2. Geometric Specifications

### 2.1 Overall Dimensions (Model Scale)

| Parameter | Value | Tolerance | Unit |
|-----------|-------|-----------|------|
| **Wingspan** | 6400 | ±2 | mm |
| **Overall Length** | 5200 | ±2 | mm |
| **Overall Height** | 1150 | ±1 | mm |
| **Wing Area** | 7.50 | ±0.02 | m² |
| **Mean Aerodynamic Chord (MAC)** | 1374 | ±1 | mm |
| **Wing Root Chord** | 3200 | ±2 | mm |
| **Wing Tip Chord** | 240 | ±0.5 | mm |

### 2.2 Reference Points

**Coordinate System:** Right-handed, X forward, Y right, Z up
- **Origin:** Nose apex
- **X-Reference:** 0.25 MAC = 3120 mm aft of nose
- **Y-Reference:** Centerline (Y = 0)
- **Z-Reference:** Fuselage bottom at X = 0

### 2.3 Control Surfaces

| Surface | Span Location | Chord % | Deflection Range | Actuated |
|---------|--------------|---------|------------------|----------|
| **Inboard Elevon** | 20-45% | 25% | ±25° | Yes |
| **Outboard Elevon** | 55-85% | 25% | ±25° | Yes |
| **Winglet Rudder** | 95-98% | 30% | ±30° | Yes |

**Actuation System:** 
- Type: Digital servo motors (Futaba S9352HV)
- Control: Wireless receiver (lab computer interface)
- Position accuracy: ±0.1°
- Update rate: 50 Hz

---

## 3. Construction Details

### 3.1 Core Structure

**Material:** Polyurethane foam (Ureol FC 80)
- Density: 80 kg/m³
- Compressive strength: 1.2 MPa
- Working temperature: -40°C to +100°C

**Manufacturing:**
- 5-axis CNC milling from solid block
- Toolpath tolerance: ±0.05 mm
- Surface finish: 2000 grit equivalent
- Assembly: 3 major sections (center, left wing, right wing)

### 3.2 Skin Laminate

**Composite Layup:**
- Prepreg: Toray T700SC carbon fiber / epoxy
- Layup: [0/90]s (2 plies, symmetric)
- Ply thickness: 0.25 mm
- Fiber volume fraction: 60%
- Cured thickness: 0.5 mm

**Mechanical Properties:**
- Tensile modulus: 70 GPa
- Tensile strength: 600 MPa
- Flexural stiffness: EI = 1200 N·m²/m (spanwise)

### 3.3 Surface Finish

**Process:**
1. Primer coat (epoxy-based)
2. Wet sanding: 400, 800, 1200, 2000 grit progression
3. Polishing compound
4. Final gelcoat (white, RAL 9016)

**Achieved Roughness:**
- Average: Ra = 0.8 μm
- Maximum: Rz = 4.2 μm
- Equivalent sand grain: ks < 10 μm (hydraulically smooth at test Re)

---

## 4. Instrumentation

### 4.1 Pressure Measurement System

**Pressure Taps:**
- Total quantity: 256
- Type: Stainless steel hypodermic tubing (1.2 mm OD, 0.8 mm ID)
- Installation: Flush mounted, smoothly blended
- Distribution: 12 spanwise sections × ~21 chordwise per section

**Spanwise Sections (% semi-span):**
0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95

**Chordwise Distribution:**
- Leading edge region: 6 points (0-5% chord)
- Mid-chord: 10 points (5-80% chord)
- Trailing edge: 5 points (80-100% chord)

**Pressure Scanner:**
- Model: Pressure Systems Inc. ESP-32HD
- Channels: 4 modules × 64 channels = 256 total
- Range: ±10 psi (±68.9 kPa)
- Accuracy: ±0.05% FS = ±34 Pa
- Response time: < 1 ms
- Temperature compensation: Active (±0.01%/°C)

### 4.2 Force Balance

**Type:** 6-component internal strain gauge balance
- Manufacturer: ABLE Co. (Japan)
- Model: MK-40A

**Load Ranges:**
| Component | Range | Accuracy |
|-----------|-------|----------|
| Normal Force (FN) | ±200 N | ±0.2 N |
| Axial Force (FA) | ±50 N | ±0.05 N |
| Side Force (FS) | ±100 N | ±0.1 N |
| Pitching Moment (My) | ±40 N·m | ±0.04 N·m |
| Rolling Moment (Mx) | ±30 N·m | ±0.03 N·m |
| Yawing Moment (Mz) | ±25 N·m | ±0.025 N·m |

**Calibration:**
- Full 6×6 interaction matrix determined
- Calibration date: 2025-09-25
- Next calibration due: 2026-03-25
- Calibration certificate: ABLE-CAL-2025-0847

### 4.3 Additional Sensors

**Temperature Monitoring:**
- Type: K-type thermocouples
- Locations: 8 (model surface, balance, tunnel ambient)
- Accuracy: ±0.5°C

**Accelerometers:**
- Type: Piezoelectric (PCB 356A15)
- Locations: 3 (model center, wing tips)
- Purpose: Vibration monitoring, flutter detection
- Range: ±500 g, frequency 0.5-10,000 Hz

---

## 5. Mounting System

### 5.1 Sting Configuration

**Sting Type:** Rear sting support
- Material: Steel (S355J2)
- Diameter: 80 mm
- Length: 1200 mm
- Pitch angle range: -5° to +25°
- Yaw angle range: ±15°

**Connection:**
- Model side: M20 bolts (8×) to internal hardpoint
- Tunnel side: Automated angle-of-attack mechanism
- Stiffness: > 5000 N/mm (bending)

### 5.2 Sting Interference Correction

**Base Pressure Measurement:**
- 16 static taps on model base (aft of balance cavity)
- Used for sting drag correction per AGARD-AR-304

**Estimated Correction:** ΔCD = -0.0008 (based on base Cp measurements)

---

## 6. Model Fidelity

### 6.1 Full-Scale Feature Representation

| Feature | Full-Scale | Model | Fidelity |
|---------|-----------|-------|----------|
| **Outer Mold Line** | Complete | 1:10 exact | 100% |
| **Control Surfaces** | Functional | Functional | 100% |
| **Landing Gear** | Retractable | Faired (clean config) | 0% |
| **Engine Nacelles** | Present | Omitted (TPC) | 0% |
| **Surface Details** | Rivets, panels | Smooth | 50% |

**TPC:** Through-flow powered condition (no propulsion simulation in this phase)

### 6.2 Reynolds Number Scaling

**Full-Scale Cruise:**
- Velocity: 242 m/s (M = 0.72)
- Altitude: 11,000 m
- Reynolds number (MAC): 52 × 10⁶

**Wind Tunnel:**
- Velocity: 60 m/s
- Sea level conditions
- Reynolds number (MAC): 5.5 × 10⁶

**Re Ratio:** 1:9.5 (close to geometric scale 1:10)

**Implications:**
- Boundary layer transition: Earlier on model (turbulence stimulation required)
- Separation: More prone on model (conservative)
- Drag coefficient: 5-10% higher on model (correction applied)

---

## 7. Quality Assurance

### 7.1 As-Built Inspection

**Method:** Laser photogrammetry (GOM ATOS Core 135)
- Measurement volume: 135 mm × 100 mm
- Point spacing: 0.1 mm
- Total points measured: 2,534,872
- Scan date: 2025-09-28

**Results:**
- RMS deviation: 0.18 mm
- Maximum deviation: +0.42 mm (upper surface, Y = 2.1 m, X = 3.5 m)
- Minimum deviation: -0.38 mm (lower surface, Y = 1.8 m, X = 2.9 m)
- 99.7% of surface within ±0.5 mm tolerance

**Conclusion:** ✅ Model meets geometric accuracy requirements

### 7.2 Weight & Balance

**Measured Values:**
- Total weight: 47.5 kg
- CG location: X = 3115 mm, Y = 0 mm, Z = 142 mm (from nose)
- Target CG: X = 3120 mm (0.25 MAC)
- Deviation: ΔX = -5 mm (-0.36% MAC) - Acceptable

**Moments of Inertia:**
| Axis | Value | Unit |
|------|-------|------|
| Ixx | 18.2 | kg·m² |
| Iyy | 85.4 | kg·m² |
| Izz | 96.8 | kg·m² |

### 7.3 Structural Load Test

**Test Procedure:**
- Applied 1.5× maximum expected wind load
- Load cases: Normal force, side force, combined
- Duration: 5 minutes per case
- Monitoring: Strain gauges, photogrammetry

**Results:**
- Maximum strain: 1850 με (< 3000 με allowable)
- Permanent deformation: < 0.1 mm (within measurement noise)
- No damage or cracks observed

**Conclusion:** ✅ Structure adequate for testing

---

## 8. Test Readiness

### 8.1 Pre-Test Checklist

- [x] Geometric verification complete
- [x] Surface finish acceptable
- [x] Weight & balance within limits
- [x] All pressure taps leak-checked
- [x] Force balance calibrated
- [x] Control surface actuation functional
- [x] Data acquisition system tested
- [x] Safety review approved

### 8.2 Operational Limits

**Wind Speed:**
- Maximum: 80 m/s (Re = 7.3 × 10⁶)
- Typical cruise: 60 m/s (Re = 5.5 × 10⁶)

**Angle of Attack:**
- Range: -5° to +25° (hard limit ±30° mechanical)
- Never exceed α > 22° above 70 m/s (model flutter risk)

**Load Limits (Balance):**
- Normal force: ±200 N (corresponds to CL = ±1.85 at 60 m/s)
- All balance components rated to 150% overload

---

## 9. Documentation Package

### 9.1 Delivered Items

1. **Model Hardware**
   - Main model assembly (3 sections)
   - Sting adapter hardware
   - Transport case

2. **Technical Documentation**
   - As-built CAD models (STEP, IGES)
   - Photogrammetry inspection report
   - Balance calibration certificate
   - Material test certificates
   - Quality assurance records

3. **Software**
   - Pressure tap location database (CSV)
   - Data reduction scripts (MATLAB)
   - Control surface calibration curves

### 9.2 Storage & Handling

**Storage Conditions:**
- Temperature: 15-25°C
- Humidity: 30-60% RH
- Storage case: Climate-controlled foam-lined

**Handling:**
- Always use soft slings or lifting frame
- Protect leading edges (most vulnerable)
- No contact with skin surface finish
- Clean after testing (isopropanol, microfiber cloth)

---

## 10. References

1. AMPEL360 Wind Tunnel Test Plan, WTP-02-10-001, Rev. 2
2. TU Delft LST Facility Handbook, Version 3.2, 2024
3. AGARD-AR-304: Experimental Data Base for Computer Program Assessment
4. ISO 1940-1: Balance Quality Requirements
5. Model Fabrication Contract, CNC-Tech-2025-0123

---

**Approved By:**

**Model Designer:** Senior Aerodynamics Engineer, AMPEL360  
**QA Inspector:** CNC Technologies GmbH  
**Test Engineer:** Dr. Maria Schmidt, TU Delft  

**Date:** 2025-09-30  
**Status:** ✅ Ready for Testing

---

**Next Review:** Post-test inspection (2025-10-20)
