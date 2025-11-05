# VAL-02-10-103: Center of Gravity (CG) Location Test
## ATA 02-10-00 AIRCRAFT GENERAL DATA - Weight Validation

**Validation ID:** VAL-02-10-103  
**Test Type:** Load Test  
**Status:** 📋 Planned  
**Scheduled Date:** 2026-Q3  
**Target Completion:** 2026-Q3

---

## 1. Validation Objective

Validate that the AMPEL360 BWB H₂ Hy-E Q100 aircraft Center of Gravity (CG) remains within the certified envelope (15-42% MAC) for all operationally realistic loading configurations.

---

## 2. Specification

### 2.1 Design Requirement
- **Requirement ID:** RQ-02-10-WT-003
- **Parameter:** Center of Gravity Range
- **Certified Envelope:** 15% - 42% MAC (Mean Aerodynamic Chord)
- **MAC Reference:** As defined in Type Certificate Data Sheet
- **MAC Length:** TBD m
- **MAC Leading Edge:** TBD m aft of datum

### 2.2 CG Limits Rationale
- **Forward Limit (15% MAC):** 
  - Ensures adequate control authority (pitch up)
  - Nose gear load within limits
  - Adequate rotation capability

- **Aft Limit (42% MAC):**
  - Stability requirements (static margin)
  - Main gear load within limits
  - Controllability in all flight phases

---

## 3. Test Scope

### 3.1 Loading Configurations to Test

#### Configuration 1: Most Forward CG
**Loading:**
- Minimum fuel (H₂): 500 kg (reserves only)
- Passengers: 220 in forward cabin zones
- Cargo: All cargo in forward compartments
- **Expected CG:** ~15-17% MAC

#### Configuration 2: Most Aft CG
**Loading:**
- Maximum fuel (H₂): 8,000 kg (aft tank location)
- Passengers: 220 in aft cabin zones
- Cargo: All cargo in aft compartments
- **Expected CG:** ~38-42% MAC

#### Configuration 3: Takeoff (Typical)
**Loading:**
- Full fuel: 8,000 kg H₂
- Full passengers: 220 pax (standard seating)
- Standard cargo: 7,500 kg (mixed distribution)
- **Expected CG:** ~28-32% MAC

#### Configuration 4: Landing (Typical)
**Loading:**
- Reserve fuel: 1,000 kg H₂
- Full passengers: 220 pax (standard seating)
- Standard cargo: 7,500 kg (mixed distribution)
- **Expected CG:** ~25-29% MAC

#### Configuration 5: Ferry Flight
**Loading:**
- Full fuel: 8,000 kg H₂
- No passengers
- No cargo
- Minimal crew
- **Expected CG:** ~32-36% MAC

---

## 4. Test Method

### 4.1 Physical Load Testing
Use actual aircraft with ballast weights to simulate each configuration.

**Equipment:**
- Electronic weighing system (load cells at each gear)
- Ballast weights (total capacity 40,000 kg)
- Load distribution planning software
- Precision measurement equipment

**Procedure for Each Configuration:**
1. Start with empty aircraft (from OEW weighing)
2. Plan ballast distribution to simulate loading
3. Install ballast weights in calculated positions
4. Weigh aircraft and measure CG
5. Verify CG calculation
6. Document configuration with photographs
7. Remove ballast and proceed to next configuration

### 4.2 Analytical Validation
Supplement physical testing with analytical validation:
- Computer weight & balance calculations
- Loading computer software verification
- Monte Carlo analysis of loading variations
- Sensitivity analysis

---

## 5. CG Calculation Method

### 5.1 From Weighing Data
```
Longitudinal CG = Σ(Wheel Load × Distance from Datum) / Total Weight

Where:
- Nose Gear Load = NGL
- Main Gear Load = MGL (left + right)
- Distance Nose Gear to Datum = DNG
- Distance Main Gear to Datum = DMG

CG from Datum = (NGL × DNG + MGL × DMG) / (NGL + MGL)
```

### 5.2 Convert to % MAC
```
CG in % MAC = ((CG location - MAC leading edge) / MAC length) × 100

Where:
- MAC leading edge location from datum = LEMAC
- MAC length = MAC_L
```

### 5.3 Example Calculation
```
If:
- Total weight = 185,000 kg
- Nose gear load = 20,000 kg
- Main gear load = 165,000 kg
- Nose gear at station 5.0 m
- Main gear at station 25.0 m
- LEMAC at station 18.0 m
- MAC length = 8.0 m

Then:
CG = (20,000 × 5.0 + 165,000 × 25.0) / 185,000
CG = (100,000 + 4,125,000) / 185,000
CG = 22.84 m from datum

CG in % MAC = ((22.84 - 18.0) / 8.0) × 100
CG in % MAC = (4.84 / 8.0) × 100
CG in % MAC = 60.5% ... Wait, this would be out of envelope!
(This is example math - actual geometry TBD)
```

---

## 6. Success Criteria

### 6.1 Primary Acceptance Criteria
**All tested configurations must have CG within 15% - 42% MAC**

### 6.2 Margin Requirements
- Minimum margin to forward limit: 1% MAC
- Minimum margin to aft limit: 1% MAC
- Operational margin: 2% MAC (preferred)

### 6.3 Pass/Fail Determination
- **Pass:** All configurations within 15-42% MAC with adequate margins
- **Conditional:** One or more configurations within 0.5% of limit (requires review)
- **Fail:** Any configuration outside 15-42% MAC envelope

---

## 7. Test Schedule

| Activity | Duration | Target Date |
|----------|----------|-------------|
| Test planning & ballast distribution calculation | 1 week | 2026-Q3 Start |
| Ballast procurement & preparation | 1 week | 2026-Q3 |
| Aircraft preparation | 2 days | 2026-Q3 |
| Configuration 1 testing | 1 day | 2026-Q3 |
| Configuration 2 testing | 1 day | 2026-Q3 |
| Configuration 3 testing | 1 day | 2026-Q3 |
| Configuration 4 testing | 1 day | 2026-Q3 |
| Configuration 5 testing | 1 day | 2026-Q3 |
| Data analysis | 1 week | 2026-Q3 |
| Report preparation | 1 week | 2026-Q3 End |

---

## 8. Resources Required

### 8.1 Personnel
- Weight & Balance Engineer (Lead)
- Loading Engineers (2)
- Load crew (6) for ballast handling
- Quality Assurance Engineer
- Safety Observer
- Photographer

### 8.2 Equipment
- Aircraft weighing system (from OEW weighing)
- Ballast weights: 40,000 kg total in various denominations
  - 500 kg weights (20x)
  - 100 kg weights (50x)
  - 50 kg weights (100x)
- Load distribution equipment (straps, nets, securing hardware)
- Forklift or crane for ballast handling
- Weight & balance calculation software
- Measurement equipment
- Photographic equipment

### 8.3 Facilities
- Weighing facility (same as OEW weighing)
- Ballast storage area
- Loading equipment access to aircraft

---

## 9. Safety Considerations

### 9.1 Load Safety
- Maximum floor loading limits not to be exceeded
- Ballast properly secured to prevent shifting
- Load distribution verified before weighing
- Structural limits monitored

### 9.2 Personnel Safety
- Ballast handling procedures (heavy loads)
- Personnel exclusion zones during weighing
- Proper lifting techniques and equipment
- Safety briefings before each configuration change

### 9.3 Aircraft Safety
- Aircraft properly supported and secured
- Landing gear load limits not exceeded
- Tipping moment calculations verified
- Continuous structural monitoring

---

## 10. Expected Results

### 10.1 CG Envelope Diagram
Will produce a diagram showing:
- Certified CG envelope (15-42% MAC)
- Tested configuration CG locations
- Operational CG range
- Margins to limits

### 10.2 Loading Limitations
May identify:
- Restricted loading combinations (if any)
- Special loading procedures required
- Ballast requirements for ferry flights
- Loading computer validation

---

## 11. Data Analysis

### 11.1 For Each Configuration
- Measured total weight
- Individual gear loads
- Calculated CG location (% MAC)
- Distance to forward limit
- Distance to aft limit
- Configuration details (payload distribution)

### 11.2 Overall Analysis
- CG travel range for typical operations
- Most critical loading scenarios
- CG control strategies
- Loading restrictions (if any)
- Comparison to design predictions

---

## 12. Deliverables

### 12.1 Test Report
- Complete test results for all configurations
- CG calculations and verification
- CG envelope diagram
- Photographic documentation
- Comparison to design predictions

### 12.2 Updated Documentation
- Weight & Balance Manual updates
- Loading Manual procedures
- Loading computer validation
- Flight manual limitations section

### 12.3 Loading Guidance
- Standard loading procedures
- CG control procedures
- Ballast requirements (if any)
- Special loading cases

---

## 13. Corrective Actions (if Required)

### 13.1 If CG Outside Envelope
**Forward CG Exceedance:**
- Move passengers aft
- Load cargo aft
- Reduce forward cargo
- Add ballast (aft location)

**Aft CG Exceedance:**
- Move passengers forward
- Load cargo forward
- Reduce aft cargo
- Add ballast (forward location)

### 13.2 If Margins Inadequate
- Revise loading procedures
- Implement loading computer controls
- Restrict certain loading combinations
- Add operational limitations

---

## 14. Risk Assessment

### 14.1 Technical Risks
- **Risk:** Unexpected CG location
  - **Mitigation:** Pre-test calculations, incremental loading

- **Risk:** CG outside envelope
  - **Mitigation:** Test planning to avoid critical combinations
  
- **Risk:** Inadequate CG control
  - **Mitigation:** Loading procedures and computer validation

### 14.2 Operational Risks
- **Risk:** Restrictive loading limitations
  - **Impact:** Operational flexibility
  - **Mitigation:** Design review, possible modifications

---

## 15. Regulatory Compliance

### 15.1 CS-25 Requirements
- CS 25.25: Weight limits
- CS 25.27: Center of gravity limits
- CS 25.29: Empty weight and CG
- CS 25.1583: Operating limitations (Weight & Balance)

### 15.2 Certification Evidence
This test provides critical evidence for:
- Type Certificate Data Sheet (TCDS)
- Flight Manual Chapter 2 (Limitations)
- Weight & Balance Manual
- Loading procedures approval

---

## 16. Approvals (Planned)

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Weight & Balance Engineer | TBD | Pending | 2026-Q3 |
| Test Engineer | TBD | Pending | 2026-Q3 |
| Structural Engineer | TBD | Pending | 2026-Q3 |
| Quality Assurance Engineer | TBD | Pending | 2026-Q3 |
| Safety Manager | TBD | Pending | 2026-Q3 |
| Chief Engineer | TBD | Pending | 2026-Q3 |
| Certification Manager | TBD | Pending | 2026-Q3 |

---

**Validation Status:** 📋 Planned  
**Scheduled:** 2026-Q3  
**Prerequisites:** OEW weighing complete, ballast available  
**Owner:** Weight & Balance Team
