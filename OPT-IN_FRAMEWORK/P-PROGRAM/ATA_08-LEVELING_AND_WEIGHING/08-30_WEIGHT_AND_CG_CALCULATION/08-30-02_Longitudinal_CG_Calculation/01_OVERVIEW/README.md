# Overview: 08-30-02 - Longitudinal CG Calculation

## 1.0 Purpose
This component establishes the method for calculating the longitudinal center of gravity (CG) position of the AMPEL360 aircraft from weighing data. The longitudinal CG position is critical for flight safety, as it affects aircraft stability, control authority, and performance.

## 2.0 Calculation Method

### 2.1 Basic Principle
The longitudinal CG is calculated using the moment arm principle:

**Total Moment = Sum of (Weight × Arm)**

Where:
- **Weight** = Force measured at each weighing point (kg)
- **Arm** = Distance from reference datum to weighing point (mm)
- **Moment** = Weight × Arm (kg·mm)

### 2.2 Standard Formula
For the AMPEL360 three-point weighing configuration:

```
CG_X = [W_nose × X_nose + W_main_left × X_main + W_main_right × X_main] / W_total
```

**Where:**
- `CG_X` = Longitudinal CG position (fuselage station in mm)
- `W_nose` = Weight measured at nose landing gear (kg)
- `W_main_left` = Weight measured at left main landing gear (kg)
- `W_main_right` = Weight measured at right main landing gear (kg)
- `X_nose` = Longitudinal position of nose gear (FS 6,500 mm)
- `X_main` = Longitudinal position of main gear (FS 23,800 mm)
- `W_total` = Total aircraft weight (kg)

### 2.3 AMPEL360-Specific Parameters

**Landing Gear Positions (Body Reference System):**
| Landing Gear | Fuselage Station (FS) | Butt Line (BL) | Water Line (WL) |
|--------------|------------------------|----------------|-----------------|
| Nose Gear | 6,500 mm | 0 mm | 2,800 mm |
| Left Main Gear | 23,800 mm | -7,800 mm | 2,600 mm |
| Right Main Gear | 23,800 mm | +7,800 mm | 2,600 mm |

**Reference Datum:**
- **FS 0:** Nose apex (forward-most point of aircraft)
- All measurements are positive aft from FS 0

## 3.0 Calculation Procedure

### Step 1: Record Scale Readings
Record weight at each landing gear position:
```
W_nose = [Scale Reading] kg
W_main_left = [Scale Reading] kg
W_main_right = [Scale Reading] kg
```

### Step 2: Correct for Tare Weight
Subtract scale platform weights:
```
W_nose_corrected = W_nose - W_tare_nose
W_main_left_corrected = W_main_left - W_tare_main_left
W_main_right_corrected = W_main_right - W_tare_main_right
```

### Step 3: Calculate Total Weight
```
W_total = W_nose_corrected + W_main_left_corrected + W_main_right_corrected
```

### Step 4: Calculate Moments
```
M_nose = W_nose_corrected × X_nose
M_main_left = W_main_left_corrected × X_main
M_main_right = W_main_right_corrected × X_main
M_total = M_nose + M_main_left + M_main_right
```

### Step 5: Calculate Longitudinal CG Position
```
CG_X = M_total / W_total
```

### Step 6: Convert to % MAC
```
CG_% MAC = [(CG_X - LEMAC) / MAC] × 100
```

Where:
- `LEMAC` = Leading Edge MAC = FS 18,000 mm
- `MAC` = Mean Aerodynamic Chord = 17,000 mm

## 4.0 Example Calculation

### Given Data (Operating Empty Weight Configuration):
```
W_nose = 21,850 kg (scale reading)
W_main_left = 49,320 kg (scale reading)
W_main_right = 49,180 kg (scale reading)
W_tare_total = 350 kg (all three scales)
```

### Calculation:
```
Step 1: Tare correction (assuming equal tare per scale)
W_tare_per_scale = 350 / 3 = 117 kg

W_nose_corrected = 21,850 - 117 = 21,733 kg
W_main_left_corrected = 49,320 - 117 = 49,203 kg
W_main_right_corrected = 49,180 - 117 = 49,063 kg

Step 2: Total weight
W_total = 21,733 + 49,203 + 49,063 = 119,999 kg ≈ 120,000 kg

Step 3: Calculate moments
M_nose = 21,733 × 6,500 = 141,264,500 kg·mm
M_main_left = 49,203 × 23,800 = 1,171,031,400 kg·mm
M_main_right = 49,063 × 23,800 = 1,167,699,400 kg·mm
M_total = 141,264,500 + 1,171,031,400 + 1,167,699,400 = 2,479,995,300 kg·mm

Step 4: Calculate CG position
CG_X = 2,479,995,300 / 119,999 = 20,667 mm = FS 20,667

Step 5: Convert to % MAC
CG_% MAC = [(20,667 - 18,000) / 17,000] × 100 = 15.7% MAC
```

### Interpretation:
- **CG Position:** FS 20,667 (20.667 meters aft of nose)
- **CG % MAC:** 15.7% MAC
- **Status:** Forward of takeoff forward limit (25% MAC) - requires loading

## 5.0 Hydrogen System Corrections

### 5.1 Residual LH₂ Correction
If residual hydrogen remains in the tank after defueling:

```
W_residual_H2 = [measured via tank level sensor] kg
X_H2_tank_CG = FS 18,500 (approximate LH₂ tank CG)

M_H2 = W_residual_H2 × X_H2_tank_CG

Corrected calculation:
W_total_empty = W_total - W_residual_H2
M_total_empty = M_total - M_H2
CG_X_empty = M_total_empty / W_total_empty
```

### 5.2 Boil-Off Correction
If hydrogen boils off during weighing:

```
W_boiloff = Boil-off_rate × Time_elapsed
W_boiloff = 4.8 kg/hr × [Time in hours]

Corrected weight:
W_total_corrected = W_total_measured + W_boiloff
```

Note: Boil-off affects weight but has minimal effect on CG since hydrogen is lost from the same location (center tank).

## 6.0 Accuracy and Uncertainty

### 6.1 Sources of Error
1. **Scale accuracy:** ±25 kg per main scale, ±10 kg nose scale
2. **Leveling error:** ±0.05° creates ±150 mm CG error
3. **Landing gear position tolerance:** ±10 mm manufacturing tolerance
4. **Structural deflection:** ±5 mm under weighing load
5. **Tare weight uncertainty:** ±5 kg per scale

### 6.2 Total Uncertainty
Using root-sum-square method:

```
σ_CG = √(σ_scales² + σ_leveling² + σ_position² + σ_deflection²)
σ_CG ≈ ±180 mm (±1.1% MAC)
```

### 6.3 Acceptance Criteria
- **Single weighing:** CG within expected range (±2% MAC from previous weighing)
- **Repeat weighing:** Two consecutive weighings agree within ±0.5% MAC
- **Lateral balance:** Left/right main gear weight difference <2% of total weight

## 7.0 Validation Checks

### 7.1 Pre-Calculation Checks
- [ ] All three scale readings recorded
- [ ] Tare weights documented
- [ ] Aircraft properly leveled (±0.05° tolerance verified)
- [ ] Environmental conditions acceptable (wind <10 knots)
- [ ] Landing gear strut pressures correct

### 7.2 Post-Calculation Checks
- [ ] Total weight within expected range (compare to previous weighing)
- [ ] CG position reasonable (typical BWB: 30-40% MAC for OEW)
- [ ] Left/right main gear balance acceptable (difference <2%)
- [ ] CG within certified envelope
- [ ] Calculation reviewed by second qualified person

## 8.0 Special Considerations for BWB Configuration

### 8.1 Wide Main Gear Spacing
- Main gear separation: 15,600 mm (BL ±7,800)
- Wide spacing improves lateral stability during weighing
- Reduces sensitivity to lateral CG offset

### 8.2 Forward CG Location
- BWB configuration typically has forward CG (35-40% MAC)
- Due to heavy nose section (cockpit, nose gear)
- Balanced by aft-mounted propulsors

### 8.3 Composite Structure Effects
- CFRP structure lighter than aluminum
- Shifts weight distribution forward
- Reduces overall structural weight fraction

## 9.0 Documentation Requirements

### 9.1 Required Records
For each weighing, document:
- Date, time, location
- Aircraft serial number and registration
- Configuration (equipment list status)
- Environmental conditions
- Scale calibration certificates
- Raw scale readings (with timestamps)
- Tare weights
- Calculated CG position
- Signature of qualified weighing personnel

### 9.2 Traceability
- Link to previous weighing records
- Reference to equipment list
- Note any configuration changes since last weighing

## 10.0 Software Tools

### 10.1 Approved Calculation Methods
1. **Manual calculation:** Using approved worksheet (Form 08-30-02-WS-001)
2. **Spreadsheet:** Excel template (File: ATA_08_CG_Calc_v2.xlsx)
3. **Weight & Balance software:** (e.g., CAMP, ULTRAMAIN)

### 10.2 Software Validation
- All software tools must be validated against known test cases
- Annual verification required
- Version control maintained

## 11.0 Related Documents
- **08-30-01:** Weight Calculation Method
- **08-30-03:** Lateral CG Calculation
- **08-20-04:** Weighing Execution Procedure
- **08-40-01:** Residual LH₂ Measurement
- **08-60-02:** CG Envelope Definition
- **08-90-05:** Data Verification Procedures

## 12.0 Revision History
| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-02 | ATA 08 Team | Initial release |

## 13.0 Contacts
- **Weight & Balance Engineer:** TBD
- **Certification Specialist:** TBD
- **Quality Assurance:** TBD
