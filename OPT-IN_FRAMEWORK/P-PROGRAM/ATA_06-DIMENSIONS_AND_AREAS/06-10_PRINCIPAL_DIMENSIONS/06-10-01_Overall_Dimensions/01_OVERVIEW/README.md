# Overview: 06-10-01 - Overall Dimensions

## 1.0 Purpose
This component establishes the official principal dimensions of the AMPEL360 aircraft, serving as the master reference for airport planning, ground handling, hangar design, and regulatory compliance.

## 2.0 Principal Dimensions Summary

### 2.1 Overall Dimensions (Nominal)
**Reference Condition:** Aircraft on level ground, landing gear static, empty weight, standard day (ISA)

| Dimension | Value | Tolerance | Measurement Point |
|-----------|-------|-----------|-------------------|
| **Wingspan** | 65.0 m | ±50 mm | Wingtip to wingtip (lateral extremes) |
| **Overall Length** | 52.5 m | ±50 mm | Nose apex to aft-most point |
| **Overall Height** | 11.2 m | ±50 mm | Ground to propulsor nacelle top |
| **Cabin Width (Max)** | 22.5 m | ±50 mm | Maximum BWB center body width |
| **Fuselage Width (Nose)** | 8.2 m | ±50 mm | Forward fuselage at cockpit |

### 2.2 Ground Contact Dimensions

| Dimension | Value | Reference |
|-----------|-------|-----------|
| **Wheelbase** | 23.8 m | Nose gear to main gear centerline |
| **Main Gear Track** | 15.6 m | Left to right main gear centerline |
| **Nose Gear Height** | 3.2 m | Ground to nose gear attach point |
| **Main Gear Height** | 4.1 m | Ground to main gear attach point |

### 2.3 Propulsor Dimensions

| Dimension | Value | Reference |
|-----------|-------|-----------|
| **Propulsor Diameter** | 5.2 m | Blade tip to tip (static) |
| **Propulsor Ground Clearance** | 3.8 m | Lowest blade tip to ground (static) |
| **Nacelle Length** | 4.5 m | Inlet lip to exhaust nozzle |
| **Propulsor Lateral Spacing** | 18.0 m | Left to right propulsor centerline |
| **Propulsor Vertical Position** | 1.8 m | Above BWB upper surface |

### 2.4 Comparison with Conventional Aircraft

**AMPEL360 vs. Boeing 787-9 (similar passenger capacity):**

| Parameter | AMPEL360 (BWB) | Boeing 787-9 | Difference |
|-----------|----------------|--------------|------------|
| Wingspan | 65.0 m | 60.1 m | +8.2% |
| Length | 52.5 m | 62.8 m | -16.4% |
| Height | 11.2 m | 17.0 m | -34.1% |
| Cabin Width (Max) | 22.5 m | 5.7 m | +295% |
| Wetted Area | 2,850 m² | 3,200 m² | -10.9% |

**Key Advantage:** BWB configuration provides 11% less wetted area (drag reduction) despite larger wingspan.

## 3.0 BWB Reference System (BRS)

### 3.1 Coordinate System Definition
The AMPEL360 uses a Body-Fixed Reference System per [SAE AS8015](https://www.sae.org/standards/content/as8015c/):

**Origin:** Nose apex (intersection of nose cone with forward pressure bulkhead)

**Axes:**
- **X-axis (Longitudinal):** Positive aft, parallel to aircraft centerline
- **Y-axis (Lateral):** Positive right (from pilot perspective)
- **Z-axis (Vertical):** Positive up, perpendicular to X-Y plane

**Datum Plane:** X=0 plane at nose apex (all fuselage stations forward of this are negative)

### 3.2 Station Numbering
- **Fuselage Stations (FS):** Longitudinal distance from datum (X-axis), measured in millimeters
  - Example: FS 12,500 = 12.5 meters aft of nose apex
- **Buttock Lines (BL):** Lateral distance from centerline (Y-axis)
  - Example: BL 1000 = 1.0 meter right of centerline
  - BL 0 = aircraft centerline
- **Water Lines (WL):** Vertical distance from ground datum (Z-axis)
  - WL 0 = ground plane (aircraft at zero pitch/roll on level surface)
  - Example: WL 4500 = 4.5 meters above ground

### 3.3 Key Reference Points (BRS Coordinates)

| Feature | X (FS) | Y (BL) | Z (WL) | Description |
|---------|--------|--------|--------|-------------|
| Nose Apex | 0 | 0 | 3200 | Origin / nose tip |
| Cockpit Floor | 3500 | 0 | 3800 | Pilot seat reference |
| Main Gear Axle | 23800 | ±7800 | 0 | Landing gear contact |
| LH₂ Tank Center | 18500 | 0 | 5200 | Fuel tank CG |
| Propulsor CL (Left) | 28000 | -9000 | 7400 | Left propulsor axis |
| Propulsor CL (Right) | 28000 | +9000 | 7400 | Right propulsor axis |
| Aft Pressure Bulkhead | 48000 | 0 | 4500 | End of pressurized cabin |
| Tail Cone Aft Point | 52500 | 0 | 3800 | Aft-most point |

## 4.0 Dimensional Tolerances and Variations

### 4.1 Manufacturing Tolerances
**Nominal dimensions are subject to manufacturing variations:**

| Feature | Tolerance |
|---------|-----------|
| Overall Dimensions (length, span, height) | ±50 mm |
| Critical Interfaces (door frames, attach points) | ±5 mm |
| Structural Jig Points | ±2 mm |
| Control Surface Gaps | ±1 mm |

### 4.2 Operational Variations
**Dimensions vary with operational conditions:**

**Fuel Loading:**
- LH₂ at -253°C causes local structure contraction (~10mm in tank region)
- Full fuel load (9,000 kg H₂) increases main gear stance by ~15mm (strut compression)

**Temperature:**
- Composite structure thermal expansion: +50°C (desert hot day) = +12mm wingspan
- Cryogenic cold soak: -20°C (cruise @ FL410) = -8mm wingspan

**Pressurization:**
- Cabin pressurization (0.8 bar differential) causes ~5mm outward bulge in center body width

**Aerodynamic Loading:**
- Wing deflection under +2.5g load: ~850mm upward wingtip deflection
- Wing deflection under -1.0g load: ~320mm downward wingtip deflection

### 4.3 As-Built Measurement
**Every production aircraft measured at final assembly:**

**Measurement Method:**
- Full-aircraft laser scan (Leica Absolute Tracker AT960, ±2mm 3D accuracy)
- 500+ measurement points distributed across airframe
- Compared to CAD master geometry (tolerance stack-up analysis)

**Acceptance Criteria:**
- All critical dimensions within ±5mm of nominal
- Overall dimensions within ±50mm of nominal
- No single deviation >100mm (requires engineering disposition)

**Documentation:**
- As-built report generated for each aircraft serial number
- Deviations tracked in Manufacturing Execution System (MES)
- Service Bulletin issued if fleet-wide trend identified

## 5.0 Airport Planning Implications

### 5.1 ICAO Aerodrome Reference Code
**AMPEL360 Classification:**
- **Code Letter:** E (wingspan 52m - 65m)
- **Code Number:** 4 (Reference Field Length ≥1800m)
- **Designation:** 4E (per [ICAO Annex 14](https://www.icao.int/safety/airnavigation/nationalitymarks/annexes_booklet_en.pdf))

**Airport Requirements:**
- **Runway Width:** Minimum 45m (typically 60m for Code E)
- **Taxiway Width:** Minimum 23m (typically 25m)
- **Taxiway Separation:** 182.5m centerline to parallel taxiway centerline
- **Apron Clearance:** Minimum 7.5m between wingtips of adjacent aircraft

### 5.2 Gate Compatibility
**Jetway Compatibility:**
- **Door L1 (Forward Left):** FS 8,500 / BL -3,200 / WL 5,200
- **Door L2 (Aft Left):** FS 38,000 / BL -3,200 / WL 5,200
- **Jetway Height Range:** 3.5m - 6.5m (standard)
- **Jetway Reach:** Minimum 15m (AMPEL360 fuselage width 8.2m at doors)

**Ramp Space:**
- **Parking Stand:** Minimum 75m × 80m
- **Wingtip Clearance:** 7.5m to adjacent objects
- **Tail Clearance:** 15m to behind aircraft (propulsor safety zone)

### 5.3 Hangar Compatibility
**Hangar Door Requirements:**
- **Width:** Minimum 70m (65m wingspan + 5m clearance)
- **Height:** Minimum 13m (11.2m height + 1.8m clearance)
- **Depth:** Minimum 60m (52.5m length + 7.5m clearance)

**Hangar Floor Loading:**
- **Main Gear Point Load:** 450 kN per strut (pavement design)
- **Nose Gear Point Load:** 180 kN
- **Pavement Classification Number (PCN):** 75 / F / B / W / T

## 6.0 Special Dimensional Considerations

### 6.1 Hydrogen System Safety Zones
**Exclusion Zones During Fueling:**
- **Hot Work Prohibited:** 10m radius from LH₂ fill port
- **Vehicle Exclusion:** 5m radius from fill port
- **Personnel Limit:** Only certified H₂ technicians within 5m

**Permanent Safety Markings:**
- Yellow hatched markings on ground around fill port (FS 22,000 / BL 0)
- "NO SMOKING / NO OPEN FLAMES" signage
- H₂ sensor locations marked with blue triangles

### 6.2 Propulsor Safety Zone
**Engine Running Envelope:**
- **Forward Danger Zone:** 25m forward of inlet (FOD ingestion risk)
- **Aft Danger Zone:** 50m aft of propulsor (blade tip velocity ~280 m/s)
- **Lateral Danger Zone:** ±15m from propulsor centerline

**Ground Crew Restrictions:**
- No personnel within safety zone when propulsors operating
- Ground equipment positioned outside lateral danger zone
- Hearing protection mandatory within 50m of operating propulsor

### 6.3 BWB Ground Handling Challenges
**Tail Strike Risk:**
- **Tail Strike Angle:** 11.5° pitch up (aft fuselage contacts ground)
- **Rotation Angle (Takeoff):** 8.5° (adequate clearance)
- **Over-Rotation Protection:** Tail bumper at FS 51,000 / WL 500 (ground contact at 12° pitch)

**Tipback Risk:**
- **Critical CG Position:** 65% MAC (aircraft tips aft if CG behind this point, empty aircraft)
- **Tail Stand Required:** Mandatory if CG >62% MAC during loading/unloading
- **Tail Stand Attachment:** FS 50,000 / BL 0 / WL 1,500 (reinforced hard point)

## 7.0 Dimensional Verification Procedures

### 7.1 Production Acceptance
**Final Assembly Dimensional Inspection:**
1. Aircraft positioned on level jig (±0.01° levelness)
2. Laser tracker setup with reference targets (±0.5mm accuracy)
3. Measure 500+ feature points (automatically compared to CAD)
4. Generate as-built report with deviation analysis
5. Engineering review and acceptance (deviations >±5mm require disposition)

### 7.2 In-Service Monitoring
**Periodic Dimensional Checks:**
- **C-Check (9,000 FH):** Wingspan measurement (detect permanent deformation)
- **D-Check (36,000 FH):** Full aircraft laser scan (compare to original as-built)

**Damage Detection:**
- Post-hard landing: Fuselage length/height measurement (detect buckle)
- Post-overweight landing: Wing dihedral measurement (detect permanent set)
- Post-lightning strike: Local dimensional check (detect composite delamination bulge)

## 8.0 Interfaces
- **ATA 00-10:** Aircraft General Information (summary dimensions in TCDS)
- **ATA 02-30:** Airport Facilities Requirements (ground handling dimensions)
- **ATA 05-30:** Zonal Inspection (zone boundary coordinates)
- **ATA 07-10:** Jack Point Locations (lifting interface dimensions)
- **ATA 08-10:** Weighing Reference Points (CG calculation datum)
- **ATA 09-10:** Tow Bar Attachment (towing interface dimensions)
- **ATA 51-57:** Structural Drawings (detailed component dimensions)
