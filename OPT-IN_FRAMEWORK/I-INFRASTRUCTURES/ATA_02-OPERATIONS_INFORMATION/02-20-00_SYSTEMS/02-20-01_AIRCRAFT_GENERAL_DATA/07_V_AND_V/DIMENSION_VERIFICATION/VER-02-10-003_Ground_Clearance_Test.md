# VER-02-10-003: Ground Clearance Test
## ATA 02-10-00 AIRCRAFT GENERAL DATA - Dimension Verification

**Verification ID:** VER-02-10-003  
**Verification Method:** Physical Measurement  
**Status:** 📋 Planned  
**Scheduled Date:** 2026-Q2  
**Verified By:** Dimensional Metrology Team (Assigned)

---

## 1. Verification Objective

Verify that the AMPEL360 BWB H₂ Hy-E Q100 aircraft ground clearance meets design specifications at various loading conditions to ensure adequate clearance for ground operations and prevent tail strike during takeoff rotation.

---

## 2. Specification

### 2.1 Design Requirements
- **Requirement ID:** RQ-02-10-DIM-003
- **Parameter:** Ground Clearance
- **Critical Measurements:**
  - Main gear clearance (static): ≥ 0.8 m
  - Tail clearance at MTOW (static): ≥ 0.35 m
  - Tail clearance during rotation (takeoff): ≥ 0.15 m at rotation angle
  - Engine/nacelle clearance: ≥ 0.6 m
  - Wingtip clearance: ≥ 1.2 m

### 2.2 Reference Documents
- Design Drawing: DWG-02-10-003 (Ground Clearance Diagram)
- Loading Manual: LM-02-10-2026
- Configuration Control: CC-02-10-2026-Q2
- Measurement Procedure: MP-DIM-003

---

## 3. Test Conditions

### 3.1 Loading Configurations to Test
1. **Empty Weight Configuration**
   - Aircraft empty (OEW)
   - No fuel, no payload
   - Maximum clearances

2. **Maximum Taxi Weight**
   - Full fuel
   - Maximum payload
   - Forward CG

3. **Maximum Takeoff Weight (MTOW)**
   - Takeoff fuel
   - Maximum payload
   - Aft CG (critical for tail clearance)

4. **Landing Weight**
   - Landing fuel reserves
   - Full payload
   - Various CG positions

### 3.2 Measurement Points
- Tail trailing edge (lowest point)
- Engine nacelle (lowest point)
- Wingtips (lowest point)
- Center fuselage (lowest point)
- Main gear attachment points
- Auxiliary gear attachment points

---

## 4. Measurement Plan

### 4.1 Equipment to be Used
- **Laser measurement system** for precise height measurements
- **Mechanical height gauges** for verification
- **Spirit levels** for aircraft attitude verification
- **Load cells** for weight and CG verification
- **Rotation simulator** (hydraulic jacks for rotation testing)
- **Photographic/video equipment** for documentation

### 4.2 Measurement Procedure

#### Phase 1: Static Measurements
1. Position aircraft on level surface
2. Load aircraft to test configuration
3. Verify weight and CG position
4. Measure ground clearances at all critical points
5. Record aircraft attitude (pitch and roll)
6. Document with photographs
7. Repeat for each loading configuration

#### Phase 2: Rotation Test
1. Position aircraft at MTOW, aft CG
2. Install rotation simulator under tail
3. Gradually increase pitch angle to rotation angle
4. Measure tail clearance throughout rotation
5. Verify adequate clearance at critical angles
6. Document rotation envelope

### 4.3 Environmental Requirements
- Level, hard surface (concrete or asphalt)
- Dry conditions (no ice, snow, standing water)
- Wind: < 10 knots for measurement accuracy
- Temperature: Record for data correlation
- Lighting: Adequate for measurements

---

## 5. Success Criteria

### 5.1 Acceptance Criteria - Static Clearances

| Measurement Point | Minimum Clearance | Target Clearance |
|-------------------|-------------------|------------------|
| Tail (MTOW, static) | 0.35 m | 0.40 m |
| Tail (rotation) | 0.15 m | 0.20 m |
| Engine nacelle | 0.60 m | 0.70 m |
| Wingtips | 1.20 m | 1.30 m |
| Main gear | 0.80 m | 0.90 m |

### 5.2 Pass/Fail Criteria
- **Pass:** All clearances meet or exceed minimum values
- **Conditional:** Clearances within 5% of minimum (engineering review)
- **Fail:** Any clearance below minimum value

---

## 6. Safety Considerations

### 6.1 Test Hazards
- Aircraft movement during loading
- Hydraulic jack failure during rotation test
- Personnel in hazard zones
- Load shifting during test

### 6.2 Safety Measures
- Aircraft properly chocked and secured
- Safety factor 2:1 on all jacks and supports
- Personnel exclusion zones established
- Emergency procedures briefed
- Safety observer assigned
- Continuous monitoring during rotation test

---

## 7. Test Schedule

| Activity | Duration | Target Date |
|----------|----------|-------------|
| Test preparation | 3 days | 2026-Q2 Start |
| Static clearance tests | 2 days | 2026-Q2 |
| Rotation test setup | 1 day | 2026-Q2 |
| Rotation test execution | 1 day | 2026-Q2 |
| Data analysis | 2 days | 2026-Q2 |
| Report preparation | 2 days | 2026-Q2 End |

---

## 8. Resources Required

### 8.1 Personnel
- Test Engineer (Lead)
- Measurement Technicians (3)
- Structural Engineer (for rotation test)
- Safety Observer (2)
- Loading crew (4)

### 8.2 Equipment
- Laser measurement system
- Mechanical height gauges
- Hydraulic jacks (4x 50-ton capacity)
- Load cells and scales
- Spirit levels (precision)
- Safety chocks and supports
- Ballast weights (for loading)
- Photographic equipment

### 8.3 Facilities
- Outdoor test area with level concrete pad
- Loading equipment (forklift, crane if needed)
- Weather protection (tent/hangar if available)

---

## 9. Test Data

### 9.1 Data to be Collected
- Clearance measurements (all points, all configurations)
- Aircraft weight and CG for each configuration
- Aircraft attitude (pitch, roll) for each configuration
- Rotation angle vs. tail clearance curve
- Environmental conditions
- Time-stamped photographs/video

### 9.2 Data Analysis
- Compare measured clearances to requirements
- Identify most critical loading condition
- Verify adequate margin for operations
- Identify any potential operational limitations
- Create clearance envelope diagram

---

## 10. Expected Results

Based on design analysis:
- Static tail clearance (MTOW): ~0.40 m (exceeds 0.35 m requirement)
- Rotation clearance: ~0.20 m at 12° rotation (exceeds 0.15 m requirement)
- Engine clearance: ~0.75 m (exceeds 0.60 m requirement)
- Adequate margins expected in all configurations

---

## 11. Risk Assessment

### 11.1 Technical Risks
- **Risk:** Clearance below minimum at aft CG
  - **Likelihood:** Low (design margins included)
  - **Mitigation:** Limit aft CG if necessary
  
- **Risk:** Tail strike during rotation test
  - **Likelihood:** Very low (controlled test)
  - **Mitigation:** Incremental rotation, continuous monitoring

### 11.2 Schedule Risks
- **Risk:** Weather delays
  - **Mitigation:** Schedule buffer, alternative test dates
  
- **Risk:** Equipment availability
  - **Mitigation:** Early equipment reservation

---

## 12. Post-Test Actions

### 12.1 If PASS
- Update flight manual with clearance data
- Establish operational limitations (if any)
- Define loading procedures and CG limits
- Close verification activity
- Archive test evidence

### 12.2 If FAIL
- Initiate nonconformance report
- Engineering analysis of impact
- Determine corrective actions (possible solutions):
  - Adjust landing gear geometry
  - Limit aft CG range
  - Modify operating procedures
  - Structural modifications if necessary
- Re-test after corrections

---

## 13. Deliverables

1. Complete test report with all measurements
2. Clearance envelope diagram
3. Photographic/video evidence
4. Loading configuration data
5. Rotation test data and curves
6. Recommendations for flight manual
7. Operational limitations (if any)

---

## 14. Approvals (Planned)

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Engineer | TBD | Pending | 2026-Q2 |
| Structural Engineer | TBD | Pending | 2026-Q2 |
| Quality Engineer | TBD | Pending | 2026-Q2 |
| Safety Manager | TBD | Pending | 2026-Q2 |
| Chief Engineer | TBD | Pending | 2026-Q2 |

---

**Verification Status:** 📋 Planned  
**Scheduled:** 2026-Q2  
**Dependencies:** Aircraft assembly complete, loading equipment available  
**Owner:** Test Engineering Team
