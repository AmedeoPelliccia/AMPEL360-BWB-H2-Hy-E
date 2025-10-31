# Design: 04-50-01 - LH₂ Tank Inner Vessel Life Limit

## 1.0 Component Design Overview

### 1.1 Tank Configuration
**Type:** Double-wall vacuum-insulated cryogenic pressure vessel

**Inner Vessel (Subject to Life Limit):**
- **Material:** Al-Li 2195-T8 alloy
- **Design Pressure:** 5.5 bar (operating), 8.25 bar (design), 13.2 bar (burst)
- **Operating Temperature:** -253°C (20K) for LH₂ storage
- **Geometry:** Cylindrical body with ellipsoidal domes
- **Dimensions:** 8.5m length × 2.2m diameter
- **Wall Thickness:** 6.5mm (cylinder), 8.0mm (domes)
- **Capacity:** 2,850 kg LH₂ (40,000 liters)

**Outer Vessel:**
- **Material:** Aluminum 6061-T6
- **Function:** Vacuum containment for MLI insulation
- **Design:** Not subject to life limit (damage tolerance design)

### 1.2 Critical Design Features

#### Dome-to-Cylinder Weld
**Configuration:** Full-penetration butt weld with backing strip
- **Weld Material:** ER2319 filler (Al-Cu-Li system)
- **Process:** Automated GTAW (Gas Tungsten Arc Welding)
- **Critical Stress Location:** Weld toe radius (identified in FSFT)
- **Design Mitigation:** 
  - Minimum toe radius: 3mm (reduces stress concentration)
  - Post-weld heat treatment (PWHT) to relieve residual stress
  - 100% radiographic + ultrasonic inspection

#### Tank Support Lugs (4 locations)
**Configuration:** Machined integral lugs with clevis pins
- **Material:** Same as vessel (Al-Li 2195-T8)
- **Load Path:** Reacts vertical (9g), lateral (3g), and longitudinal (12g) loads
- **Design Feature:** Spherical bearing allows thermal contraction without constraint

#### Fill/Drain Penetration
**Configuration:** Welded boss with mechanical fitting
- **Size:** DN50 (2-inch nominal)
- **Reinforcement:** Doubler plate on internal surface
- **Sealing:** Metal C-ring gasket (Inconel 718)

### 1.3 Material Properties at Cryogenic Temperature

**Al-Li 2195-T8 at -253°C:**
- **Yield Strength (σ_y):** 420 MPa (ambient: 345 MPa)
- **Ultimate Strength (σ_u):** 510 MPa (ambient: 455 MPa)
- **Fracture Toughness (K_IC):** 45 MPa√m (initial)
- **Coefficient of Thermal Expansion:** 22.5×10⁻⁶ /°C (20°C), 18.1×10⁻⁶ /°C (-253°C)
- **Modulus of Elasticity:** 78 GPa (both temperatures)

**Material Selection Rationale:**
- High strength-to-weight ratio (density: 2.7 g/cm³)
- Excellent cryogenic toughness (no ductile-to-brittle transition)
- Proven spaceflight heritage (Space Shuttle external tank, SLS)
- Weldable with proper procedures

## 2.0 Life Limit Design Basis

### 2.1 Design Service Goal (DSG)
**Target:** 50,000 flight cycles (15 years at 3,333 FC/year average utilization)

**Mission Profile per Flight Cycle:**
1. Pre-flight: Ambient temperature (+20°C), 1 bar internal
2. LH₂ fill: Cool-down to -253°C over 45 minutes
3. Taxi/takeoff: Pressurize to 5.5 bar, fuel consumption begins
4. Cruise: 4.0 bar average (fuel burn reduces pressure)
5. Descent/landing: 2.5 bar residual
6. Post-flight: Drain residual H₂, warm-up to ambient

**Critical Stress Cycle:**
- **Mechanical:** 0 MPa → 285 MPa → 190 MPa → 0 MPa (pressure variation)
- **Thermal:** 200 MPa (thermal stress during cool-down/warm-up)
- **Combined:** Equivalent stress range = 340 MPa

### 2.2 Fatigue Analysis Method

**Approach:** Linear-elastic fracture mechanics (LEFM)

**Assumptions:**
- Initial flaw size: 0.5mm (detection limit of manufacturing NDT)
- Stress intensity factor: K_I = σ√(πa) × F_geometry
- Paris Law crack growth: da/dN = C(ΔK)^m
  - Material constants (Al-Li 2195 at -253°C): C = 1.2×10⁻¹¹, m = 3.1
- Critical crack size: a_c = 45mm (when K_I reaches K_IC)

**Analysis Result:**
- Crack initiation: 50,000 cycles (0.5mm → 1.0mm)
- Crack propagation: 97,000 cycles (1.0mm → 45mm)
- **Total life:** 147,000 cycles to failure
- **Design life (÷3 safety factor):** 49,000 cycles → **rounded to 50,000 FC**

### 2.3 Thermal Cycle Contribution

**Thermal Cycling Damage:**
- Each fill/drain cycle induces plastic strain at dome radius: ε_p = 0.08%
- Low-cycle fatigue (LCF) damage per thermal cycle: D_LCF = 1.33×10⁻⁵
- Equivalent high-cycle fatigue (HCF) damage: D_HCF = 2.0×10⁻⁵
- **Ratio:** 1 thermal cycle = 0.67 flight cycle (Palmgren-Miner rule)

**Thermal Cycle Limit:**
- 50,000 FC ÷ 0.67 = 74,627 thermal cycles → **rounded to 75,000 TC**

### 2.4 Calendar Life Determination

**Degradation Mechanisms:**
1. **Hydrogen Embrittlement:** K_IC reduction rate = 0.45% per year
   - Critical threshold: K_IC < 32 MPa√m (residual strength insufficient)
   - Time to critical: 28.9 years
   - **Safety factor (÷1.5):** 19.3 years → **rounded to 20 years**

2. **Corrosion:** Localized pitting reduces effective wall thickness
   - Corrosion rate: 0.004 mm/year (coastal environment)
   - Time to critical (t_min - 0.5mm): 125 years (not limiting)

3. **Vacuum Degradation:** MLI performance loss
   - Boil-off rate increase: 1.2% per year
   - Time to 2× boil-off: 83 years (not limiting)

**Conclusion:** Hydrogen embrittlement is limiting factor for calendar life.

## 3.0 Design Verification

### 3.1 Stress Analysis (FEA)
**Model Details:**
- Software: ANSYS Mechanical 2024 R1
- Element type: SOLID186 (20-node hexahedral)
- Mesh density: 4mm global, 1mm refined at welds
- Total elements: 2.3 million
- Contact elements: 50,000 (support lugs)

**Load Cases:**
1. **Internal Pressure:** 5.5 bar (operating), 8.25 bar (design), 13.2 bar (ultimate)
2. **Thermal:** -253°C internal, +70°C external (desert hot day)
3. **Inertial:** 9g crash loads (per CS-25.561)
4. **Combined:** Pressure + thermal + inertial (load factor 1.0)

**Results Summary:**
| Location | Stress (MPa) | Margin of Safety |
|----------|--------------|------------------|
| Dome-cylinder weld | 285 | +0.47 |
| Support lug | 310 | +0.35 |
| Fill valve boss | 265 | +0.58 |

**All Margins Positive:** Design meets CS-25.305 ultimate load requirements

### 3.2 Design Optimization Studies

**Trade Studies Conducted:**
1. **Material Selection:** Al-Li 2195 vs. Al 2219 vs. Ti-6Al-4V
   - **Winner:** Al-Li 2195 (best strength/weight, cost-effective)

2. **Dome Shape:** Ellipsoidal vs. torispherical vs. hemispherical
   - **Winner:** Ellipsoidal (2:1 ratio optimizes stress distribution)

3. **Wall Thickness:** 5mm vs. 6.5mm vs. 8mm
   - **Winner:** 6.5mm (minimum weight meeting fatigue life)

4. **Weld Configuration:** Butt weld vs. lap weld vs. friction stir weld
   - **Winner:** Butt weld (highest fatigue resistance, proven process)

### 3.3 Design for Inspectability
**Access Provisions:**
- External visual inspection: 360° access via removable insulation panels
- Internal inspection: DN600 manhole at aft dome (entry for borescope)
- NDT access: Ultrasonic transducer ports at 12 locations

**Inspection Capability:**
- Detectable flaw size: 3mm (visual), 1mm (ultrasonic), 0.5mm (eddy current)
- Inspection interval: NOT APPLICABLE (safe-life component)

## 4.0 Interface Design

### 4.1 Mechanical Interfaces
**Support Structure:**
- 4× clevis mounts to fuselage frames
- Kinematic mount (1 fixed, 3 floating) accommodates thermal contraction
- Load path: Tank → lugs → clevises → frames → keel beam

**Piping Connections:**
- Fill/drain: DN50 (2-inch) at forward dome
- Vent/relief: DN25 (1-inch) at aft dome
- Fuel feed: DN40 (1.5-inch) at aft dome (to fuel cells)

### 4.2 Instrumentation Interfaces
**Sensors Integrated:**
- Pressure transducer: 0-10 bar range, ±0.1% accuracy
- Temperature sensor (×4): Pt100 RTD, -270°C to +50°C
- Level sensor: Capacitance type, 0-100% range
- Vacuum pressure sensor: 10⁻⁶ to 10⁻² torr range
- Leak detector: H₂ concentration sensor, 0-1000 ppm

**Data Interfaces:**
- ACMS: Flight cycle count (ARINC 429)
- FMS: Fuel quantity and thermal cycle count (ARINC 429)
- EICAS: Caution/warning messages (ARINC 429)

### 4.3 Electrical Bonding
**Lightning Protection:**
- Conductive path: Tank → support lugs → airframe
- Bonding resistance: < 2.5 milliohms per CS-25.581
- Diverter strips: Installed on external surface (aluminum foil tape)

## 5.0 Design Standards and Codes

**Pressure Vessel Codes:**
- ASME Section VIII Division 2: Alternative Rules (design by analysis)
- EN 13445: Unfired Pressure Vessels (European standard)

**Aerospace Standards:**
- CS-25.963: Fuel Tank Tests
- CS-25.981: Fuel Tank Ignition Prevention
- NASA-STD-5001B: Structural Design and Test Factors (adapted)

**Material Standards:**
- AMS 4331: Al-Li 2195 Plate and Sheet
- AWS D17.1: Fusion Welding for Aerospace Applications

**Quality Standards:**
- AS9100 Rev D: Quality Management System
- NADCAP: Welding and NDT accreditation

## 6.0 Design Documentation

**Released Drawings:**
- AMPEL-28-100-001: Tank assembly
- AMPEL-28-100-010: Inner vessel detail
- AMPEL-28-100-020: Outer vessel detail
- AMPEL-28-100-030: Support lug detail
- AMPEL-28-100-100: Installation assembly

**Specifications:**
- AMPEL-SPEC-MAT-001: Material specification (Al-Li 2195)
- AMPEL-SPEC-WELD-002: Welding procedure specification
- AMPEL-SPEC-NDT-003: Non-destructive testing requirements

**Configuration Control:**
- All drawings maintained in Windchill PLM system
- Change control per AMPEL-PROC-CM-001
- Current revision: D (all production tanks)
