# VAL-02-10-102: Operating Empty Weight (OEW) Weighing
## ATA 02-10-00 AIRCRAFT GENERAL DATA - Weight Validation

**Validation ID:** VAL-02-10-102  
**Test Type:** Physical Weighing  
**Status:** 📋 Planned  
**Scheduled Date:** 2026-Q3  
**Target Completion:** 2026-Q3

---

## 1. Validation Objective

Determine the actual Operating Empty Weight (OEW) and Center of Gravity (CG) of the AMPEL360 BWB H₂ Hy-E Q100 aircraft in its standard operational configuration.

---

## 2. Specification

### 2.1 Design Requirement
- **Requirement ID:** RQ-02-10-WT-002
- **Parameter:** Operating Empty Weight (OEW)
- **Target Value:** 115,000 kg (estimated)
- **Tolerance:** To be determined by actual measurement
- **Note:** OEW is basis for all weight & balance calculations

### 2.2 OEW Definition
Per CS-25 and Weight & Balance Manual, OEW includes:

**Included Items:**
- Complete airframe structure
- Propulsion system (fuel cells, electric motors, propellers)
- All permanently installed systems and equipment
- H₂ fuel system (tanks, lines, valves) - empty
- Fixed interior (seats, galleys, lavatories)
- Avionics and instruments
- Hydraulic fluid (if applicable)
- Engine oil (if applicable)
- Unusable fuel and fluids
- Emergency equipment (fixed)
- Flight manuals and documents
- Standard operational items

**Excluded Items:**
- Flight crew
- Cabin crew
- Passengers
- Cargo
- Usable H₂ fuel
- Catering supplies
- Removable emergency equipment
- Potable water (beyond minimum)

---

## 3. Weighing Method

### 3.1 Equipment
- **Primary:** Electronic aircraft weighing system
  - 4x Load cells, 60,000 kg capacity each (240,000 kg total capacity)
  - Accuracy: ±0.1% of reading
  - Calibration: Valid within 6 months
  - Calibration Certificate: CAL-2026-Q3-001
  
- **Measurement System:**
  - Digital readout with individual wheel weight display
  - Automatic CG calculation
  - Data logging capability

- **Support Equipment:**
  - Precision spirit levels (0.02° accuracy)
  - Laser alignment system
  - Weighing platform (calibrated, level surface)
  - Jacking equipment (for leveling if required)

### 3.2 Weighing Configuration

**Aircraft Configuration:**
- All doors and panels closed
- Landing gear fully extended (normal ground position)
- Control surfaces neutral
- Flaps retracted
- H₂ tanks empty and purged
- All fluids at standard levels
- Standard equipment installed
- No passengers or cargo
- No crew (except for systems operation if required)

**Environmental Conditions:**
- Indoor weighing (hangar) preferred
- Wind < 5 knots if outdoor
- Temperature: Record for documentation
- Humidity: Record for documentation
- Aircraft and equipment at thermal equilibrium

---

## 4. Weighing Procedure

### 4.1 Pre-Weighing Preparation
1. **Equipment Setup**
   - Verify load cell calibration certificates
   - Setup weighing platform
   - Position load cells at each landing gear location
   - Connect readout system
   - Verify zero reading with no load

2. **Aircraft Preparation**
   - Tow aircraft to weighing area
   - Verify configuration matches OEW definition
   - Remove all non-standard items
   - Drain H₂ tanks completely
   - Verify fluid levels (hydraulic, oil if applicable)
   - Close all doors and panels
   - Photograph configuration

3. **Configuration Documentation**
   - Complete configuration checklist
   - Record all installed equipment (by serial number)
   - Record all fluid levels
   - Note any deviations from standard configuration
   - Take comprehensive photographs

### 4.2 Weighing Execution
1. **Initial Positioning**
   - Position aircraft on weighing platform
   - Center each gear on its load cell
   - Ensure no external connections or supports
   - Verify clear of ground equipment

2. **Leveling**
   - Check aircraft level (longitudinal and lateral)
   - Use precision spirit levels at designated stations
   - If not level, record attitude for CG correction
   - Photograph level indicators

3. **Weight Measurement**
   - Allow system to stabilize (5 minutes minimum)
   - Record individual wheel loads:
     - Main gear left
     - Main gear right
     - Nose gear (or tail gear if applicable)
   - Take multiple readings (minimum 3)
   - Verify repeatability (within ±50 kg)
   - Record environmental conditions

4. **CG Calculation**
   - Measure gear positions relative to datum
   - Calculate longitudinal CG
   - Calculate lateral CG (verify symmetry)
   - Calculate vertical CG (from design data)
   - Express CG in % MAC (Mean Aerodynamic Chord)

5. **Verification**
   - Perform independent weight calculation
   - Verify against estimated weight
   - Check for any anomalies
   - Repeat measurement if questionable

### 4.3 Post-Weighing
1. **Data Recording**
   - Complete weighing data sheet
   - Record all measurements
   - Photograph all displays
   - Back up electronic data

2. **Aircraft Release**
   - Remove weighing equipment
   - Perform post-weighing inspection
   - Return aircraft to normal status

---

## 5. Data Analysis

### 5.1 Weight Calculation
```
OEW = Main Gear Left + Main Gear Right + Nose Gear
```

### 5.2 CG Calculation
```
Longitudinal CG = Σ(Wheel Load × Distance from Datum) / OEW
CG in % MAC = ((CG location - MAC leading edge) / MAC length) × 100
```

### 5.3 Comparison Analysis
- Compare to design estimate (115,000 kg target)
- Calculate weight margin remaining
- Analyze weight breakdown if possible
- Identify any weight growth areas

---

## 6. Success Criteria

### 6.1 Measurement Quality
- Repeatability: ±50 kg between measurements
- Balance: Left/right symmetry within 1%
- CG location: Within certified envelope
- Data quality: Complete and accurate

### 6.2 Weight Acceptance
- **Target:** OEW ≤ 120,000 kg
- **Acceptable:** OEW ≤ 122,000 kg (allows reduced payload/fuel)
- **Marginal:** OEW 122,000 - 125,000 kg (requires weight reduction program)
- **Unacceptable:** OEW > 125,000 kg (exceeds viable limits)

---

## 7. Expected Results

### 7.1 Estimated OEW Breakdown

| Component Group | Estimated Weight (kg) | % of OEW |
|-----------------|----------------------|----------|
| Airframe structure | 45,000 | 39.1% |
| Propulsion system | 25,000 | 21.7% |
| H₂ fuel system (empty) | 15,000 | 13.0% |
| Systems & equipment | 18,000 | 15.7% |
| Interior | 8,000 | 7.0% |
| Operational items | 4,000 | 3.5% |
| **Total (Target)** | **115,000** | **100%** |

### 7.2 Expected CG Location
- Longitudinal CG: Approximately 30% MAC
- Within certified envelope: 15% - 42% MAC
- Adequate margin for all loading conditions

---

## 8. Test Schedule

| Activity | Duration | Date |
|----------|----------|------|
| Equipment preparation | 3 days | 2026-Q3 Start |
| Equipment calibration verification | 1 day | 2026-Q3 |
| Aircraft preparation | 2 days | 2026-Q3 |
| Weighing execution | 1 day | 2026-Q3 |
| Data analysis | 2 days | 2026-Q3 |
| Report preparation | 3 days | 2026-Q3 End |

---

## 9. Resources Required

### 9.1 Personnel
- Weight & Balance Engineer (Lead)
- Weighing Technicians (2)
- Configuration Manager
- Quality Assurance Engineer
- Photographer/Documentarian

### 9.2 Equipment
- Aircraft weighing system with load cells
- Precision leveling equipment
- Measuring equipment (for CG calculation)
- Data recording system
- Photographic equipment

### 9.3 Facilities
- Weighing facility (hangar with level floor preferred)
- Towing equipment
- Jacking equipment (if leveling required)

---

## 10. Deliverables

### 10.1 Weight & Balance Report
- Measured OEW: [Value] kg
- CG location: [Value] % MAC
- Individual wheel weights
- Aircraft configuration at time of weighing
- Photographic documentation

### 10.2 Updated Documentation
- Aircraft Weight & Balance Record
- Weight & Balance Manual (update with actual data)
- Configuration deviation list (if any)

### 10.3 Validation Report
- Complete test procedure
- All measurement data
- Analysis and comparison to estimate
- Recommendations

---

## 11. Quality Assurance

### 11.1 Measurement Verification
- Multiple measurements for repeatability
- Independent calculation check
- Calibration verification
- Configuration control

### 11.2 Documentation Control
- Photographs of configuration
- Photographs of measurements
- Witnessed by QA
- Traceability to requirements

---

## 12. Risk Management

### 12.1 Technical Risks
- **Measurement error:** Use calibrated equipment, multiple readings
- **Configuration error:** Detailed checklist, photographic documentation
- **Weight growth:** Already built into contingency planning

### 12.2 Schedule Risks
- **Aircraft availability:** Coordinate with assembly schedule
- **Equipment failure:** Backup measurement capability
- **Weather (if outdoor):** Schedule flexibility

---

## 13. Post-Weighing Actions

### 13.1 Documentation Updates
- Update aircraft logbook with official OEW
- Update Weight & Balance Manual
- Update loading computer software
- Distribute data to operations and maintenance

### 13.2 Configuration Control
- Establish official weight baseline
- Track all future modifications affecting weight
- Establish re-weighing schedule (per regulations)

---

## 14. Approvals (Planned)

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Weight & Balance Engineer | TBD | Pending | 2026-Q3 |
| Configuration Manager | TBD | Pending | 2026-Q3 |
| Quality Assurance Engineer | TBD | Pending | 2026-Q3 |
| Chief Engineer | TBD | Pending | 2026-Q3 |
| Certification Manager | TBD | Pending | 2026-Q3 |

---

**Validation Status:** 📋 Planned  
**Scheduled:** 2026-Q3  
**Prerequisites:** Aircraft assembly complete, systems installed  
**Owner:** Weight & Balance Team
