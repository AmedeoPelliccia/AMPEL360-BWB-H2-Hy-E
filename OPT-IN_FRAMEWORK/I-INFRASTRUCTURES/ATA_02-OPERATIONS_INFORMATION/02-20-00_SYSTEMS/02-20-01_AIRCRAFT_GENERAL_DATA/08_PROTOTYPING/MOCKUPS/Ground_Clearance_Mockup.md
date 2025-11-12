# Ground Clearance Mockup
# Landing Gear and Fuselage Clearance Validation

**Mockup ID:** GCM-02-10-002  
**Scale:** 1:1 (Full Scale)  
**Date:** 2026-Q2 (Planned)  
**Status:** Design Phase  
**Classification:** Engineering Validation

---

## 1. Overview

### 1.1 Purpose

Validate ground clearance requirements for the AMPEL360 BWB configuration to ensure:
- Compliance with CS-25.231 (Tail down landing conditions)
- Adequate clearance for rotation during takeoff
- Protection of critical components during ground operations
- Compatibility with standard ground service equipment

### 1.2 Unique BWB Challenge

**Challenge:** Blended Wing Body has no traditional fuselage
- Entire aft body is part of lifting surface
- Risk of tail strike during rotation is unique geometry
- Ground clearance must be verified with full-scale physical mockup
- CFD/CAD alone insufficient due to gear deflection, tire deformation

---

## 2. Mockup Scope

### 2.1 Physical Representation

**Included Components:**

1. **Aft Fuselage Section**
   - From aft pressure bulkhead to tail cone (FS 40,000 to 52,000 mm)
   - Lower surface geometry accurate to ±5 mm
   - Includes auxiliary power unit (APU) bay
   - Aft cargo door clearance

2. **Main Landing Gear**
   - Full-scale main gear leg (functional extension/retraction)
   - Actual tires (nose and main, proper inflation)
   - Shock strut with representative travel (±150 mm)
   - Gear attachment structure

3. **Nose Landing Gear**
   - Full-scale nose gear (steering range ±75°)
   - Tire and wheel assembly
   - Extension/retraction mechanism

4. **Reference Datum**
   - Fixed ground plane (concrete pad, level within 1 mm/m)
   - Articulated platform for simulated runway slope
   - Load cells for weight distribution measurement

### 2.2 Excluded Components (Not Critical for Clearance)

- Wing tips (beyond 90% span)
- Forward fuselage (FS 0 to 15,000 mm)
- Empennage details (simplified geometry)

---

## 3. Test Scenarios

### 3.1 Static Ground Clearance

**Test Conditions:**

| Load Case | MTOW (kg) | CG Location (%MAC) | Gear Compression | Target Clearance |
|-----------|----------|-------------------|------------------|------------------|
| Empty + Crew | 45,000 | 28% | Minimal | - |
| MTOW Forward CG | 95,000 | 20% | Full static | ≥ 400 mm |
| MTOW Aft CG | 95,000 | 35% | Full static | ≥ 350 mm |
| MLW Forward CG | 82,000 | 22% | Full static | ≥ 420 mm |
| MLW Aft CG | 82,000 | 33% | Full static | ≥ 370 mm |

**Measurement Points:**
- Lowest fuselage point (typically aft belly, FS ~48,000 mm)
- APU exhaust
- Aft cargo door lower edge
- Tail skid or bumper (if installed)

**Instrumentation:**
- 20× laser distance sensors (Keyence LK-H082, ±10 μm accuracy)
- Hydraulic load cells on each gear leg (50,000 kg capacity, ±0.1% FS)
- Inclinometers (pitch and roll, ±0.01° accuracy)

### 3.2 Dynamic Rotation Simulation

**Objective:** Simulate takeoff rotation to verify no tail strike

**Method:**
1. Position mockup at static MTOW condition
2. Hydraulically rotate aft section (simulates pitch increase during liftoff)
3. Monitor clearance continuously during rotation
4. Stop rotation when clearance reaches minimum (200 mm residual)

**Test Matrix:**

| CG Location | Takeoff Rotation Rate | Max Pitch Angle | Min Clearance Target |
|-------------|----------------------|----------------|---------------------|
| Forward (20% MAC) | 3°/sec | 12° | ≥ 400 mm |
| Nominal (28% MAC) | 3°/sec | 10° | ≥ 350 mm |
| Aft (35% MAC) | 3°/sec | 8° | ≥ 300 mm |

**Success Criterion:** Clearance ≥ 200 mm at maximum pitch angle (CS-25.231 compliance)

### 3.3 Ground Service Equipment Clearance

**Scenarios:**

1. **Catering Truck Access**
   - Truck positioning at forward and aft galley doors
   - Verify no interference with gear or fuselage contour
   - Clearance: ≥ 100 mm

2. **Baggage Loader**
   - Cargo door height validation (Type C cargo door, 1,370 mm × 1,676 mm)
   - Belt loader clearance under fuselage
   - Clearance: ≥ 200 mm

3. **Ground Power Unit**
   - GPU connection point accessibility
   - Cable routing clearance

4. **Tow Bar Attachment**
   - Tow bar angle range (±60°)
   - Clearance during tightest turn radius

**Documentation:** Photo/video of each scenario, clearance measurements

---

## 4. Design Specifications

### 4.1 Mockup Construction

**Structure:**
- Steel space frame (welded 150×150 mm SHS)
- Fuselage contour: Aluminum sheet metal forming (3 mm)
- No aerodynamic accuracy required (ground clearance only)

**Adjustability:**
- Hydraulic jacks at each gear location (load capacity 50,000 kg each)
- Manual adjustment of CG location (movable ballast weights, 500 kg increments)
- Pitch articulation: ±15° range (hydraulic actuator, 100 kN capacity)

**Gear Assemblies:**
- Procure surplus Airbus A320 main landing gear (modified mounting)
- Actual AMPEL360 tires (Michelin or Goodyear, 52×21.0 R22)
- Representative shock strut travel (±150 mm stroke)

### 4.2 Instrumentation

**Clearance Measurement:**
- 20× laser distance sensors (ground to fuselage)
- Sampling rate: 100 Hz
- Data logging: LabVIEW system

**Load Monitoring:**
- 3× load cells (nose and 2× main gear)
- Weight distribution calculation (real-time)

**Geometry Capture:**
- 4× high-speed cameras (240 fps) for rotation event
- Photogrammetry targets (50× on fuselage lower surface)

---

## 5. Validation Criteria

### 5.1 Regulatory Compliance (CS-25.231)

**CS-25.231(a) - Tail Down Landing:**
- Airplane contacts ground with aft fuselage (most critical attitude)
- All landing gear extended and fully compressed
- Flaps in landing position
- **Required Ground Clearance:** Not less than that required by CS-25.231(b)

**CS-25.231(b) - Ground Clearance:**
- Aft fuselage structure must withstand tail-down landing loads
- No damage to structure, systems, or equipment
- **AMPEL360 Target:** 200 mm minimum at most aft point (conservative vs. regulation)

### 5.2 Operational Requirements

**Takeoff Rotation:**
- Clearance at VR (rotation speed): ≥ 300 mm
- Clearance at VLOF (liftoff speed): ≥ 200 mm
- No ground contact during normal takeoff (pilot technique variation ±2°)

**Ground Handling:**
- Static clearance (MTOW): ≥ 400 mm
- Clearance with gear on pothole (-50 mm depression): ≥ 350 mm
- Service equipment access: No interference

### 5.3 Test Acceptance

**Pass Criteria:**
- ✅ All clearances meet or exceed targets
- ✅ No interference with ground service equipment
- ✅ Rotation to 15° pitch without ground contact
- ✅ Load distribution within ±5% of predicted
- ✅ Gear deflection matches analysis (±10 mm)

**Failure Modes (Require Design Iteration):**
- ❌ Clearance < 200 mm at tail-down attitude
- ❌ Aft fuselage contacts ground during rotation test
- ❌ Gear load imbalance > 10%
- ❌ Service equipment interference discovered

---

## 6. Risk Mitigation

### 6.1 Design Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Insufficient clearance at aft CG | Medium | High | Aft fuselage redesign, tail bumper |
| Gear sinkage greater than predicted | Low | Medium | Tire pressure optimization |
| Uneven weight distribution | Low | Medium | CG location adjustment, ballast |
| Mockup inaccuracy | Low | High | Laser scan verification pre-test |

### 6.2 Test Risks

| Risk | Mitigation |
|------|------------|
| Hydraulic failure during rotation | Redundant hydraulic system, manual lockout |
| Overload of gear during test | Load limiters, real-time monitoring |
| Instrumentation failure | Redundant sensors, manual measurement backup |
| Damage to mockup | Controlled test procedure, incremental pitch increase |

---

## 7. Schedule and Budget

### 7.1 Timeline

| Phase | Duration | Dates | Status |
|-------|----------|-------|--------|
| Design Complete | 2 months | Nov-Dec 2025 | ✅ |
| Procurement (Gear, Materials) | 3 months | Jan-Mar 2026 | 📋 |
| Fabrication | 2 months | Mar-Apr 2026 | 📋 |
| Assembly & Instrumentation | 1 month | May 2026 | 📋 |
| Testing Campaign | 2 weeks | Jun 2026 | 📋 |
| Data Analysis & Report | 1 month | Jun-Jul 2026 | 📋 |

**Critical Path:** Gear procurement (long-lead item, 12 weeks)

### 7.2 Budget

| Item | Cost (€) |
|------|---------|
| Design Engineering | 15,000 |
| Landing Gear (surplus A320, modified) | 45,000 |
| Steel Structure & Skin | 35,000 |
| Hydraulic System | 25,000 |
| Instrumentation | 20,000 |
| Assembly Labor | 12,000 |
| Facility Rental | 8,000 |
| Contingency (15%) | 24,000 |
| **Total** | **184,000** |

**Funding Status:** Approved, allocated from Phase 2A budget

---

## 8. Deliverables

### 8.1 Test Reports

1. **Ground Clearance Validation Report (GCVR-02-10-001)**
   - Summary of all test scenarios
   - Clearance measurements vs. requirements
   - Load distribution data
   - Photographic evidence

2. **Compliance Demonstration (CS-25.231)**
   - Formal demonstration of regulatory compliance
   - Signed by DER (Designated Engineering Representative)
   - Submitted to EASA as part of certification plan

3. **Lessons Learned Document**
   - Design optimization recommendations
   - Operational considerations (pilot technique, field length)

### 8.2 Data Package

- 3D scan of mockup (as-built geometry)
- Video recordings of rotation tests
- Load cell data (time history, all test points)
- Clearance sensor data (CSV format, 100 Hz sampling)

---

## 9. Follow-On Actions

### 9.1 Design Optimization

**If Clearance Issues Identified:**
- Adjust main gear length (+50 to +100 mm strut extension)
- Modify aft fuselage contour (local reshaping, ±20 mm)
- Install tail bumper or skid (retractable or fixed)

**If Clearance Margin Excessive (> 500 mm):**
- Consider shorter gear (weight reduction)
- Optimize gear attachment structure

### 9.2 Operational Procedures

**Flight Crew:**
- Define rotation technique in Flight Crew Operating Manual (FCOM)
- Specify rotation rate (3°/sec nominal, 5°/sec maximum)
- Aft CG limitations (VR speed adjustment)

**Ground Crew:**
- Service equipment positioning procedures
- Clearance markings on fuselage (visual reference for GSE operators)

---

## 10. Success Metrics

**Mockup Evaluation Successful If:**
- ✅ CS-25.231 compliance demonstrated (≥ 200 mm clearance)
- ✅ Operational margin confirmed (≥ 300 mm at rotation)
- ✅ No redesign required (or minor adjustments only)
- ✅ Test data accuracy validated (±10 mm vs. predictions)
- ✅ Schedule and budget maintained

**Decision Gate:** Proceed to detailed landing gear design (Q3 2026)

---

## 11. References

1. CS-25.231: Tail Down Landing Condition
2. CS-25.479: Level Landing Conditions
3. AMPEL360 Landing Gear Design Specification (LGDS-32-00-001)
4. A320 Landing Gear Maintenance Manual (Reference for mockup gear)
5. Ground Clearance Best Practices (Boeing D6-54446, Airbus ABD0100)

---

**Document Owner:** Landing Gear Design Lead  
**Approval:**
- [ ] Chief Engineer - Aircraft General Data
- [ ] Landing Gear System Engineer
- [ ] Flight Test Engineer
- [ ] Quality Assurance

**Status:** Design Complete / Procurement Phase  
**Next Review:** 2026-03-01 (Fabrication Kickoff)
