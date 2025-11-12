# VAL-02-10-101: MTOW Validation
## ATA 02-10-00 AIRCRAFT GENERAL DATA - Weight Validation

**Validation ID:** VAL-02-10-101  
**Test Type:** Physical Weighing  
**Status:** 📋 Planned  
**Scheduled Date:** 2026-Q3  
**Target Completion:** 2026-Q3

---

## 1. Validation Objective

Validate that the AMPEL360 BWB H₂ Hy-E Q100 aircraft Maximum Takeoff Weight (MTOW) meets the certified specification of 185,000 kg and that all loading configurations remain within this limit.

---

## 2. Specification

### 2.1 Design Requirement
- **Requirement ID:** RQ-02-10-WT-001
- **Parameter:** Maximum Takeoff Weight (MTOW)
- **Target Value:** 185,000 kg
- **Regulatory Limit:** Not to exceed 185,000 kg (CS-25 certification basis)
- **Verification Method:** Actual weighing in maximum loading configuration

### 2.2 Reference Documents
- Weight & Balance Manual: WBM-02-10-2026
- Loading Manual: LM-02-10-2026
- Type Certificate Data Sheet: TCDS-AMPEL360-001
- Configuration Control: CC-02-10-2026-Q3
- Weighing Procedure: WP-WT-001

---

## 3. Validation Approach

### 3.1 Weighing Configuration
The aircraft will be weighed in the following configuration to validate MTOW:

**Aircraft Configuration:**
- Operating Empty Weight (OEW) including:
  - Airframe structure
  - Propulsion system (fuel cells, motors, propellers)
  - Systems and equipment
  - Interior furnishings
  - Operational items (crew, manuals, emergency equipment)
  
**Plus Maximum Payload:**
- Maximum passenger load: 220 passengers @ 95 kg each
- Maximum cargo load: 15,000 kg
- Crew: 2 flight crew + 4 cabin crew @ 85 kg each
  
**Plus Maximum Fuel:**
- H₂ fuel: 8,000 kg (maximum capacity)

**Expected Total:** Should not exceed 185,000 kg

---

## 4. Weighing Method

### 4.1 Equipment
- **Primary:** Electronic aircraft weighing system
  - 4x Load cells, 60,000 kg capacity each
  - Accuracy: ±0.1% of reading (±50 kg at 50,000 kg)
  - Calibration: Valid within 6 months
  - Calibration Certificate: Required before weighing
  
- **Secondary:** Backup mechanical scales (for verification)

### 4.2 Weighing Procedure
1. **Preparation Phase**
   - Verify equipment calibration
   - Position aircraft in weighing area
   - Level weighing platform
   - Install load cells under each landing gear
   - Verify aircraft level using precision spirit levels

2. **Empty Weight Measurement**
   - Weigh aircraft in OEW configuration
   - Record individual wheel loads
   - Calculate total weight and CG
   - Verify against weight & balance records

3. **Maximum Load Simulation**
   - Add ballast to simulate maximum passenger load
   - Add ballast to simulate maximum cargo load
   - Simulate maximum H₂ fuel load (water ballast in tanks or calculation)
   - Verify load distribution and CG location

4. **MTOW Measurement**
   - Measure total weight on all load cells
   - Verify level attitude maintained
   - Record environmental conditions
   - Perform redundant measurement
   - Calculate and verify CG position

5. **Verification**
   - Cross-check with independent measurement
   - Verify calculation accuracy
   - Confirm configuration control
   - Document results

### 4.3 Environmental Conditions
- Temperature: Record (for density corrections)
- Humidity: Record
- Wind: < 5 knots (weighing area should be sheltered)
- Surface: Level, solid platform

---

## 5. Success Criteria

### 5.1 Primary Acceptance Criterion
**Total Weight ≤ 185,000 kg**

The measured weight with maximum payload and fuel must not exceed the certified MTOW of 185,000 kg.

### 5.2 Secondary Criteria
- Weight measurement repeatability: ±100 kg
- CG location within certified envelope
- Weight breakdown matches weight & balance documentation
- All safety margins maintained

### 5.3 Pass/Fail Determination
- **Pass:** Total weight ≤ 185,000 kg with all margins
- **Conditional:** Weight 185,000 - 185,500 kg (engineering review required)
- **Fail:** Weight > 185,500 kg (exceeds MTOW with margin)

---

## 6. Expected Results

### 6.1 Weight Breakdown Estimate

| Component | Estimated Weight (kg) | % of MTOW |
|-----------|----------------------|-----------|
| Operating Empty Weight (OEW) | 115,000 | 62.2% |
| Maximum Passengers (220 @ 95 kg) | 20,900 | 11.3% |
| Maximum Cargo | 15,000 | 8.1% |
| Crew (6 @ 85 kg) | 510 | 0.3% |
| Maximum H₂ Fuel | 8,000 | 4.3% |
| Margin/Reserve | TBD | TBD |
| **Total (Target)** | **≤ 185,000** | **100%** |

### 6.2 Weight Contingency
- Design target OEW: 115,000 kg
- Maximum allowable OEW: 120,000 kg (5,000 kg contingency)
- If OEW > 120,000 kg: Requires payload or fuel reduction

---

## 7. Risk Assessment

### 7.1 Weight Growth Risks
- **Risk:** OEW exceeds estimate
  - **Impact:** Reduced payload or fuel capacity
  - **Likelihood:** Moderate (first prototype)
  - **Mitigation:** Weight reduction program, payload adjustment
  
- **Risk:** Systems heavier than designed
  - **Impact:** Certification basis affected
  - **Mitigation:** Component weight tracking during assembly

### 7.2 Operational Risks
- **Risk:** MTOW exceeded
  - **Impact:** Cannot carry full payload and full fuel simultaneously
  - **Mitigation:** Define reduced range or reduced payload missions
  
### 7.3 Measurement Risks
- **Risk:** Measurement uncertainty
  - **Mitigation:** Use calibrated equipment, multiple measurements
  
- **Risk:** Load cell failure
  - **Mitigation:** Backup measurement system available

---

## 8. Test Schedule

| Activity | Duration | Target Date |
|----------|----------|-------------|
| Equipment preparation | 1 week | 2026-Q3 Start |
| Equipment calibration | 2 days | 2026-Q3 |
| Aircraft positioning | 1 day | 2026-Q3 |
| OEW weighing | 1 day | 2026-Q3 |
| Load simulation setup | 2 days | 2026-Q3 |
| MTOW weighing | 1 day | 2026-Q3 |
| Data analysis | 3 days | 2026-Q3 |
| Report preparation | 5 days | 2026-Q3 End |

---

## 9. Resources Required

### 9.1 Personnel
- Test Engineer (Lead)
- Weighing Technicians (4)
- Weight & Balance Engineer
- Quality Assurance Engineer
- Structural Engineer (for load distribution)
- Configuration Manager

### 9.2 Equipment
- Electronic aircraft weighing system (load cells, readout)
- Calibration weights (for verification)
- Ballast weights (20+ tons)
- Precision spirit levels
- Survey equipment
- Data acquisition system
- Lifting/positioning equipment

### 9.3 Facilities
- Weighing facility with level platform
- Ballast storage and handling equipment
- Environmental protection (hangar preferred)

---

## 10. Corrective Actions (if MTOW Exceeded)

### 10.1 Weight Reduction Options
1. **Reduce OEW:**
   - Material substitution
   - Component optimization
   - Non-essential items removal

2. **Operational Restrictions:**
   - Reduced passenger capacity on long-range missions
   - Reduced fuel load for short-range missions
   - Cargo limitations

3. **Performance Trade-offs:**
   - Accept reduced range
   - Accept reduced payload
   - Combination of above

### 10.2 Re-certification Considerations
If weight significantly exceeds MTOW, may require:
- Revised Type Certificate Data Sheet (TCDS)
- Performance re-analysis
- Regulatory authority approval

---

## 11. Data Management

### 11.1 Data to be Collected
- Individual wheel loads (main gear, nose gear)
- Total aircraft weight
- CG location (longitudinal, lateral, vertical)
- Environmental conditions
- Ballast configuration and weights
- Photographic documentation
- Equipment calibration data

### 11.2 Data Analysis
- Weight comparison to estimate
- CG envelope verification
- Weight breakdown analysis
- Margin analysis
- Trend analysis (for future aircraft)

---

## 12. Deliverables

1. **Weight & Balance Report**
   - Measured OEW
   - Measured MTOW with full load
   - CG location data
   - Weight breakdown

2. **Validation Report**
   - Test procedure used
   - Results and analysis
   - Comparison to requirements
   - Pass/fail determination
   - Recommendations

3. **Updated Weight & Balance Manual**
   - Actual aircraft data
   - Loading procedures
   - CG envelope

---

## 13. Approvals (Planned)

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Engineer | TBD | Pending | 2026-Q3 |
| Weight & Balance Engineer | TBD | Pending | 2026-Q3 |
| Quality Engineer | TBD | Pending | 2026-Q3 |
| Chief Engineer | TBD | Pending | 2026-Q3 |
| Certification Manager | TBD | Pending | 2026-Q3 |

---

**Validation Status:** 📋 Planned  
**Scheduled:** 2026-Q3  
**Dependencies:** Aircraft assembly complete, weighing equipment available  
**Owner:** Weight & Balance Team
