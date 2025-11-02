# ATA 08: Leveling and Weighing

**PROGRAM CHAPTER STATUS:** ATA 08 establishes the procedures, equipment specifications, and calculation methods for leveling the aircraft and determining its weight and center of gravity (CG). This data is critical for flight safety, performance calculations, and regulatory compliance.

## Scope and Structure
This chapter documents all aspects of aircraft leveling and weighing operations, including:
- **Leveling Procedures:** Methods to establish aircraft reference planes
- **Weighing Procedures:** Techniques for accurate weight determination
- **CG Calculation:** Methods to determine center of gravity location
- **Equipment Requirements:** Scales, jacks, and instrumentation specifications
- **Weight and Balance Records:** Documentation and reporting requirements
- **Special Considerations:** Hydrogen fuel density, composite structure, BWB geometry

## The 14-Folder Skeleton
Every 6-digit component within this chapter represents a formal weighing procedure, calculation method, or equipment specification. Each component is managed through the full lifecycle skeleton to ensure requirements traceability, procedure validation, measurement accuracy, and regulatory compliance.

## Regulatory Framework

### Certification Requirements
- **CS-25.25:** Weight Limits (maximum weights)
- **CS-25.27:** Center of Gravity Limits
- **CS-25.1583:** Operating Limitations (Weight and CG placards)
- **CS-25.1589:** Loading Information (Weight and Balance Manual)
- **FAA AC 120-27F:** Aircraft Weight and Balance Control
- **EASA Part-M.A.306:** Aircraft Continuing Airworthiness Records

### Industry Standards
- **ATA iSpec 2200 Chapter 08:** Standard weighing procedures
- **SAE AIR1845:** Weighing and Determination of Center of Gravity of Aircraft
- **MIL-STD-1374:** Weighing and Balancing of Aircraft
- **ISO 17025:** General Requirements for Testing and Calibration Laboratories
- **ASTM E74:** Standard Practice of Calibration of Force-Measuring Instruments

## AMPEL360 Unique Characteristics

### 1. **Blended Wing Body (BWB) Geometry**
The AMPEL360 has no conventional fuselage, creating unique leveling and CG challenges:

**Reference Plane Definition:**
- **Longitudinal Reference Plane:** XZ-plane (BL 0, aircraft centerline)
- **Lateral Reference Plane:** YZ-plane (FS 0, nose apex datum)
- **Horizontal Reference Plane:** XY-plane (WL 0, ground plane)

**Leveling Challenges:**
- No conventional fuselage longitudinal axis (use BWB centerline)
- Wide center body requires multiple leveling points laterally
- Composite structure deflection affects leveling accuracy
- Large moment arms amplify small leveling errors

**Solution:**
- Digital inclinometer network (5 sensors) across airframe
- Wireless real-time monitoring during weighing
- Compensate for structural deflection under load

### 2. **Hydrogen Fuel System Impact**
Cryogenic LH₂ fuel has dramatically different weight/volume characteristics than conventional Jet-A:

**Fuel Density Comparison:**
- **LH₂ (Liquid Hydrogen):** 70.8 kg/m³ at -253°C
- **Jet-A (Conventional):** 804 kg/m³ at 15°C
- **Ratio:** Jet-A is 11.4× denser than LH₂

**Weight Impact:**
- **Full LH₂ fuel load:** 9,000 kg (13,000 L tank volume × 0.708 kg/L)
- **Equivalent Jet-A:** 102,480 kg (same mission energy)
- **Weight savings:** 93,480 kg (but requires much larger tank)

**CG Impact:**
- LH₂ tank location: FS 15,000 to FS 22,000 (center body)
- Tank CG at approximately 35% MAC (forward of typical fuel)
- As fuel burns: CG moves aft (opposite direction vs. wing tanks)
- CG travel: ~3% MAC over mission (vs. ~10% MAC for conventional aircraft)

**Weighing Considerations:**
- Empty weight includes residual H₂ (ullage gas ~0.5% tank volume)
- Boil-off during weighing: ~2 kg/hour (must correct for time)
- Cryogenic structural contraction: ±10mm dimensional change
- Tank thermal mass: 30 minutes stabilization time required

### 3. **Composite Structure Weight Distribution**
Carbon fiber composite structure has different weight distribution than aluminum:

**Material Density:**
- **CFRP (Carbon Fiber):** 1,550 kg/m³ (laminate density)
- **Aluminum 2024-T3:** 2,780 kg/m³ (conventional aircraft skin)
- **Weight Ratio:** Aluminum is 1.8× heavier by volume

**Structural Weight Breakdown (Estimated):**
| Component | Weight (kg) | % of OEW | Material |
|-----------|-------------|----------|----------|
| BWB Airframe Structure | 18,500 | 26.4% | CFRP composite |
| Landing Gear | 4,200 | 6.0% | Steel/Titanium |
| Propulsion System | 8,600 | 12.3% | Mixed metals/CFRP |
| LH₂ Fuel System | 3,800 | 5.4% | Al-Li/Inconel |
| Fuel Cell System | 2,400 | 3.4% | Stainless steel/Graphite |
| Systems (Hydraulic, ECS, etc.) | 6,800 | 9.7% | Mixed |
| Avionics | 1,200 | 1.7% | Electronics |
| Interior/Furnishings | 12,500 | 17.9% | Mixed |
| Propulsors (2×) | 6,000 | 8.6% | Titanium/CFRP |
| Operational Items | 6,000 | 8.6% | Fluids, crew, catering |
| **Operating Empty Weight (OEW)** | **70,000** | **100%** | — |

**CG Distribution:**
- Composite structure shifts weight distribution forward (lighter aft fuselage)
- Heavy components: Landing gear (aft), propulsors (aft-upper), fuel cells (center)
- Result: OEW CG at ~38% MAC (typical for BWB configuration)

### 4. **Weight and CG Limits**

**Design Weights:**
| Weight Condition | Value (kg) | Description |
|------------------|------------|-------------|
| **Manufacturer's Empty Weight (MEW)** | 64,000 | As-built aircraft, no operational items |
| **Operating Empty Weight (OEW)** | 70,000 | MEW + crew, catering, unusable fuel |
| **Maximum Zero Fuel Weight (MZFW)** | 96,000 | Max weight without fuel |
| **Maximum Taxi Weight (MTW)** | 121,000 | Max weight for ground operations |
| **Maximum Takeoff Weight (MTOW)** | 120,000 | Max weight at brake release |
| **Maximum Landing Weight (MLW)** | 105,000 | Max weight at touchdown |

**Center of Gravity Limits:**
| Configuration | Forward CG Limit | Aft CG Limit | Reference |
|---------------|------------------|--------------|-----------|
| Takeoff | 25% MAC | 40% MAC | CS-25.25 |
| Landing | 20% MAC | 45% MAC | CS-25.25 |
| Zero Fuel | 30% MAC | 65% MAC | Structural limit |
| Flight (All) | 20% MAC | 40% MAC | Envelope corner |

**MAC Reference:**
- **Leading Edge MAC (LEMAC):** FS 18,000
- **MAC Length:** 17,000 mm (17.0 meters)
- **Trailing Edge MAC (TEMAC):** FS 35,000

**CG Calculation:**
```
CG % MAC = [(CG Station - LEMAC) / MAC] × 100
Example: CG at FS 24,500 = [(24,500 - 18,000) / 17,000] × 100 = 38.2% MAC
```

### 5. **Upper-Surface Propulsor Weight Distribution**
Twin propulsors mounted above BWB affect weight and CG:

**Propulsor Weight Breakdown (Each):**
| Component | Weight (kg) | Total (2×) |
|-----------|-------------|------------|
| Open-fan rotor assembly | 1,200 | 2,400 |
| Nacelle structure | 450 | 900 |
| Electric drive motor | 600 | 1,200 |
| Gearbox | 380 | 760 |
| Pylon structure | 270 | 540 |
| Controls/accessories | 100 | 200 |
| **Total per propulsor** | **3,000** | **6,000** |

**Propulsor CG Location:**
- Longitudinal: FS 28,000 (28m aft of nose, ~59% MAC)
- Lateral: BL ±9,000 (9m left/right of centerline)
- Vertical: WL 7,400 (7.4m above ground, ~3.2m above BWB surface)

**Effect on Aircraft CG:**
- Propulsors are aft and high → moves aircraft CG aft and up
- Balances forward weight of nose landing gear and cockpit
- Vertical CG elevation: 4.5m above ground (lower than conventional due to BWB)

## Weighing Methods

### 1. **Standard Weighing (On Scales)**
**Method:** Aircraft positioned on calibrated platform scales at each landing gear

**Equipment Required:**
- 3× calibrated platform scales (2× main gear, 1× nose gear)
- Digital inclinometer system (5 sensors)
- Calibration weights (verification)
- Environmental monitoring (temperature, wind)

**Procedure Overview:**
1. Tow aircraft onto scales
2. Level aircraft using spirit levels + inclinometers
3. Record scale readings (correct for tare weight)
4. Calculate total weight and CG position
5. Verify results against previous weighing (±0.5% tolerance)

**Accuracy:** ±0.1% of total weight (±120 kg for AMPEL360)

**Duration:** 4-6 hours (including setup and leveling)

### 2. **Jack Weighing (On Jacks)**
**Method:** Aircraft lifted on jacks equipped with load cells

**Equipment Required:**
- 3× hydraulic jacks with integrated load cells (600 kN capacity)
- Digital inclinometer system
- Load cell calibration equipment
- Safety stands (installed after initial lift)

**Procedure Overview:**
1. Jack aircraft per ATA 07 procedures
2. Level aircraft using jack height adjustments
3. Record load cell readings at each jack point
4. Calculate total weight and CG position
5. Lower aircraft and verify scale readings (if possible)

**Accuracy:** ±0.2% of total weight (±240 kg for AMPEL360)

**Duration:** 6-8 hours (longer due to jacking setup)

**Advantages:**
- Can be performed in maintenance hangar
- Allows simultaneous maintenance access
- Useful for weight checks during heavy maintenance

### 3. **Computational Weighing (Future)**
**Method:** Weight estimation from installed sensors and digital twin model

**Equipment Required:**
- Strain gauges at critical structure locations (200+ sensors)
- Digital twin model (real-time FEA)
- Machine learning algorithm (trained on historical weighing data)

**Concept:**
- Strain sensors measure structural deflection under load
- Digital twin correlates strain to weight distribution
- AI algorithm refines estimate based on operational data

**Accuracy (Target):** ±0.5% of total weight (±600 kg for AMPEL360)

**Status:** Under development (ATA 92 integration), pilot program 2026

## Leveling Procedures

### Three-Point Leveling Method
**Primary Method:** Spirit level measurements at defined leveling points

**Leveling Points:**
| Point | Location (BRS) | Reference Surface |
|-------|----------------|-------------------|
| **LP-1 (Nose)** | FS 8,000 / BL 0 / WL 5,200 | Forward cabin floor rail |
| **LP-2 (Left)** | FS 25,000 / BL -8,000 / WL 5,400 | Center body floor rail |
| **LP-3 (Right)** | FS 25,000 / BL +8,000 / WL 5,400 | Center body floor rail |

**Leveling Procedure:**
1. Position aircraft on level surface (floor verified ±0.1°)
2. Place precision spirit levels at each leveling point
3. Adjust aircraft attitude using jacks (if scale weighing) or jack height (if jack weighing)
4. Iterate until all three points show level (±0.05° tolerance)
5. Verify with digital inclinometers (wireless real-time display)

**Leveling Tolerance:**
- **Longitudinal (Pitch):** ±0.05° (±0.87 mrad)
- **Lateral (Roll):** ±0.05° (±0.87 mrad)

**CG Error from Leveling Error:**
- 0.1° pitch error → ±150mm CG error (±0.9% MAC) at 50m aircraft length
- Critical to achieve tight leveling tolerance

### Digital Inclinometer System
**Equipment:** 5× wireless MEMS inclinometers (±0.01° accuracy)

**Sensor Locations:**
- Forward fuselage: FS 8,000 / BL 0
- Left wing: FS 25,000 / BL -8,000
- Right wing: FS 25,000 / BL +8,000
- Center body: FS 18,000 / BL 0
- Aft fuselage: FS 40,000 / BL 0

**Real-Time Display:**
- Tablet display shows all sensor readings simultaneously
- Color-coded: Green (in tolerance), Yellow (approaching limit), Red (out of tolerance)
- Historical tracking: Logs leveling convergence over time

## Weight and Balance Calculation

### Weight Calculation
**Formula:**
```
Total Weight (W) = W_nose + W_main_left + W_main_right - W_tare
```

Where:
- W_nose = Nose gear scale reading
- W_main_left = Left main gear scale reading
- W_main_right = Right main gear scale reading
- W_tare = Combined tare weight of scales/jacks

**Example Calculation (OEW Weighing):**
```
W_nose = 21,850 kg (scale reading)
W_main_left = 49,320 kg
W_main_right = 49,180 kg
W_tare = 350 kg (3 scales)

Total Weight = 21,850 + 49,320 + 49,180 - 350 = 119,980 kg

Correction for residual H₂ = -45 kg (ullage gas)
Correction for boil-off during weighing = +12 kg (2.5 hours × 4.8 kg/hr)

Final OEW = 119,980 - 45 + 12 = 119,947 kg ≈ 120,000 kg (MTOW check)
```

### CG Calculation (Longitudinal)
**Formula:**
```
CG_X = [W_nose × X_nose + W_main_left × X_main + W_main_right × X_main] / W_total
```

Where:
- X_nose = FS 6,500 (nose gear position)
- X_main = FS 23,800 (main gear position)

**Example Calculation:**
```
CG_X = [21,850 × 6,500 + 49,320 × 23,800 + 49,180 × 23,800] / 120,000
CG_X = [142,025,000 + 1,173,816,000 + 1,170,484,000] / 120,000
CG_X = 2,486,325,000 / 120,000 = 20,719 mm = FS 20,719

CG % MAC = [(20,719 - 18,000) / 17,000] × 100 = 16.0% MAC
```

**Verification:** 16.0% MAC is forward of takeoff limit (25% MAC) → requires loading to achieve forward CG limit

### CG Calculation (Lateral)
**Formula:**
```
CG_Y = [W_main_left × (-7,800) + W_main_right × (+7,800)] / W_total
```

**Example Calculation:**
```
CG_Y = [49,320 × (-7,800) + 49,180 × (+7,800)] / 120,000
CG_Y = [-384,696,000 + 383,604,000] / 120,000
CG_Y = -1,092,000 / 120,000 = -9.1 mm = BL -9.1

Lateral offset = 9.1mm left of centerline (negligible, <0.01% of span)
```

**Acceptance:** Lateral CG within ±50mm of centerline (meets requirement)

### CG Calculation (Vertical)
**Not typically calculated for flight operations** (not a certification requirement for transport category aircraft), but important for landing gear load distribution and structural analysis.

**Formula:**
```
CG_Z = Σ(component weight × component Z-coordinate) / W_total
```

**AMPEL360 Estimated Vertical CG:** WL 4,500 (4.5m above ground)

## Weight and Balance Documentation

### Required Records
**Per EASA Part-M.A.306 and CS-25.1589:**

1. **Aircraft Weighing Report:**
   - Serial number, registration
   - Date of weighing, location
   - Environmental conditions (temperature, humidity, wind)
   - Scale/jack calibration data
   - Raw scale readings
   - Tare weights
   - Calculated total weight and CG
   - Signature of authorized person

2. **Weight and Balance Manual:**
   - Empty weight and CG (as-weighed)
   - Loading instructions
   - CG envelope diagram
   - Sample load sheets
   - Equipment list (removable items)

3. **Equipment List:**
   - Standard items (included in OEW)
   - Optional items (added/removed, affect weight/CG)
   - Configuration management

### Reweighing Requirements
**Mandatory Reweighing Events:**
- **Initial certification:** As-built aircraft before first flight
- **Major modification:** Structural changes >0.5% OEW or CG change >1% MAC
- **Periodic:** Every 4 years (or 48 months / 10,000 FH, whichever first)
- **Cumulative changes:** When sum of changes exceeds 0.5% OEW

**Example Triggers for Reweighing:**
- Interior reconfiguration (seat changes >10 seats)
- Fuel system modification (affects H₂ tank capacity)
- Avionics upgrade (weight >50 kg)
- Structural repair (composite patch >5 m²)

## Hydrogen System Considerations for Weighing

### Pre-Weighing LH₂ System Preparation
**Mandatory Steps:**
1. **Defuel to minimum:** Drain LH₂ tank to <5% capacity (target: empty)
2. **Depressurize:** Reduce tank pressure to atmospheric (0 bar gauge)
3. **Vent ullage gas:** Connect vent line, safely disperse residual H₂
4. **Thermal stabilization:** Wait 60 minutes for structure to warm
5. **Measure residual H₂:** Use tank level sensor to determine remaining mass

**Residual H₂ Correction:**
- Tank "empty" state: ~0.5% volume ullage gas (65 L × 0.708 kg/m³ × 0.005 = 0.46 kg)
- Residual liquid holdup: ~10 L in sump and lines (10 L × 0.708 kg/L = 7.1 kg)
- **Total residual H₂:** ~7.5 kg (must be subtracted from weighed empty weight)

### Boil-Off Correction
**H₂ Boil-Off Rate:** 4.8 kg/hour (from tank heat leak)

**Correction Formula:**
```
Weight_corrected = Weight_measured + (Boil-off_rate × Time_elapsed)
```

**Example:**
Weighing duration: 2.5 hours  
Boil-off correction: 4.8 kg/hr × 2.5 hr = 12 kg  
Add 12 kg to measured weight to correct for H₂ lost during weighing

**Best Practice:** Complete weighing quickly (<3 hours) to minimize correction

## Scale and Load Cell Requirements

### Scale Specifications
**Nose Gear Scale:**
- Capacity: 25,000 kg (250 kN)
- Resolution: 5 kg (0.02% of capacity)
- Accuracy: ±10 kg (0.04% of capacity)
- Platform size: 1.2m × 1.2m
- Calibration interval: 12 months

**Main Gear Scales (2×):**
- Capacity: 60,000 kg (600 kN)
- Resolution: 10 kg (0.017% of capacity)
- Accuracy: ±25 kg (0.042% of capacity)
- Platform size: 1.5m × 2.0m
- Calibration interval: 12 months

**Total System Capacity:** 145,000 kg (adequate for MTOW 120,000 kg with 21% margin)

### Load Cell Specifications (Jack Weighing)
**Nose Jack Load Cell:**
- Capacity: 250 kN
- Accuracy: ±0.1% full scale (±250 N = ±25 kg)
- Output: Digital (RS-485)
- Calibration: 6 months

**Main Jack Load Cells (2×):**
- Capacity: 600 kN
- Accuracy: ±0.1% full scale (±600 N = ±60 kg)
- Output: Digital (RS-485)
- Calibration: 6 months

### Calibration Requirements
**Pre-Use Verification:**
- Apply known calibration weights (1,000 kg, 5,000 kg, 10,000 kg)
- Verify scale reading within ±0.1% of calibration weight
- Record results in calibration log

**Annual Calibration:**
- Performed by accredited calibration laboratory (ISO 17025)
- Traceable to national standards (NIST in USA, PTB in Germany)
- Certificate of calibration maintained in quality records

## Integration with Other Chapters

### Data Flows
```
ATA 08 (Leveling/Weighing)
    ↓ Weight Data → ATA 00 (General - TCDS)
    ↓ CG Limits → ATA 00-50 (Limitations)
    ↓ Loading Info → ATA 09 (Towing - CG considerations)
    ↓ Jack Setup → ATA 07 (Lifting/Shoring)
    ↓ H₂ Fuel Weight → ATA 28 (Fuel System)
    ↓ Balance Calculation → Flight Operations (Load Sheet)
```

### Cross-References
- **ATA 00-40:** Weight and Balance Data (summary)
- **ATA 06-10:** Dimensions and Reference System (datum definition)
- **ATA 07-20:** Jacking Procedures (jack weighing method)
- **ATA 09-30:** CG Limits for Towing
- **ATA 12-31:** H₂ Defueling for Weighing
- **ATA 25-20:** Equipment List (removable items)
- **ATA 28-10:** Fuel System (residual H₂ measurement)

## Special Weighing Scenarios

### 1. **Wing-Off Weighing (Major Repair)**
**Scenario:** Wing removed for structural repair

**Procedure:**
- Weigh center body with nose gear and main gear
- Weigh wing separately on fixture
- Calculate combined weight and CG
- Verify against previous whole-aircraft weighing

**Challenge:** CG calculation more complex (component CG must be known)

### 2. **Fuel Cell Stack Weighing (Component Change)**
**Scenario:** Fuel cell stack replaced (3,000 kg component)

**Procedure:**
- Weigh old fuel cell on calibrated platform scale
- Weigh new fuel cell before installation
- Calculate weight change and CG shift
- Update equipment list (if different model installed)

**Criteria for Reweighing:** If weight change >100 kg or CG change >50mm

### 3. **Interior Reconfiguration Weighing**
**Scenario:** Seat layout changed (300-seat → 350-seat high-density)

**Procedure:**
- Remove old seats and weigh
- Install new seats and weigh
- Measure seat row positions (calculate CG change)
- Update Weight and Balance Manual

**Simplified Method:** If seat manufacturer provides certified weight data, calculation may be acceptable (reweighing not mandatory)

## Quality Assurance

### Pre-Weighing Checklist
- [ ] Aircraft towed to weighing area (level floor verified ±0.1°)
- [ ] LH₂ tank defueled to minimum (residual H₂ measured)
- [ ] All removable equipment in standard configuration (per equipment list)
- [ ] Landing gear struts serviced to correct pressure
- [ ] Fuel cells shut down (no electrical loads)
- [ ] Scales/load cells calibrated (current certificate verified)
- [ ] Environmental conditions recorded (temperature, wind speed)
- [ ] Digital inclinometers installed and verified

### During Weighing Monitoring
- **Leveling:** Continuous monitoring (inclinometers green light)
- **Stability:** Scale readings stable (±5 kg) for 60 seconds before recording
- **Environmental:** Wind speed <10 knots (5 m/s)
- **Time:** Record start/stop time (for boil-off correction)

### Post-Weighing Documentation
- [ ] Weighing report completed and signed
- [ ] Results compared to previous weighing (±0.5% tolerance)
- [ ] Weight and Balance Manual updated
- [ ] Aircraft logbook entry: "Aircraft weighed per ATA 08. OEW = XXX kg, CG = XX.X% MAC. No discrepancies."
- [ ] Type Certificate Data Sheet (TCDS) updated if initial certification
- [ ] Operator notification if CG limits or loading procedures change

## Document Hierarchy
```
ATA 08 (This Chapter)
├── Weighing Procedures Manual (WPM)
├── Leveling Point Identification Drawing
├── Weight and Balance Manual (AFM Supplement)
├── Equipment List
├── Weighing Report Template
├── Scale/Load Cell Calibration Certificates
├── CG Envelope Diagram
└── Sample Load Sheets
```

## Revision Control
Changes to ATA 08 procedures require:
1. **Engineering Analysis:** CG limits affected by design changes
2. **Flight Test:** CG envelope expansion requires flight test validation
3. **Regulatory Approval:** EASA/FAA approval for TCDS amendment (weight/CG limits)
4. **Operator Training:** Flight crew and load planning staff updated
5. **Service Bulletin:** Formal notification to all operators

## Future Enhancements
- **Automated Weighing:** Drive-on scales (aircraft tows onto platform, automatic reading)
- **Continuous Weight Monitoring:** Embedded strain sensors + digital twin (real-time weight/CG)
- **Blockchain Records:** Immutable weight and balance records (tamper-proof certification)
- **AI Load Planning:** Machine learning optimizes cargo/passenger distribution for CG control
