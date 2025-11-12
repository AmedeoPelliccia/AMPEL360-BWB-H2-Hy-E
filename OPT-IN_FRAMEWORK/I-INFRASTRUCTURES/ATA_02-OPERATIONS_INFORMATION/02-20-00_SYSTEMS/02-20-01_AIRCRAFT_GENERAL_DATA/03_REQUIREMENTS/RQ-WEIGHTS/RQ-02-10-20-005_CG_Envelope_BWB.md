# RQ-02-10-20-005: Center of Gravity Envelope

**Requirement ID:** RQ-02-10-20-005  
**Category:** Weights  
**Priority:** Critical  
**Status:** Approved

## Requirement

BWB aircraft shall maintain CG within 15% to 42% MAC for all loading conditions.

**Forward Limit:** 15.0% MAC  
**Aft Limit:** 42.0% MAC  
**Normal Range:** 25-38% MAC  
**Lateral Limit:** ±500 kg imbalance

## Rationale

BWB configuration requires wider CG range than conventional (27% vs 20%) due to distributed payload and fuel storage.

## CG Envelope Details

### Longitudinal CG Limits

The center of gravity envelope is defined by the following boundaries:

| Weight (kg) | Forward Limit (%MAC) | Aft Limit (%MAC) |
|-------------|---------------------|------------------|
| 95,000 (OEW) | 28.0 | 35.0 |
| 117,000 (Typical ZFW) | 25.0 | 38.0 |
| 135,000 (MZFW) | 20.0 | 40.0 |
| 155,000 (MLW) | 17.0 | 41.0 |
| 185,000 (MTOW) | 15.0 | 42.0 |

### Critical Loading Cases

1. **Most Forward CG:**
   - Empty aircraft + crew forward
   - Minimal fuel
   - CG at 15.0% MAC

2. **Most Aft CG:**
   - Full passenger load aft
   - Cargo aft
   - H₂ tanks aft depleted first
   - CG at 42.0% MAC

3. **Normal Operations:**
   - Standard passenger distribution
   - Balanced cargo loading
   - CG typically 25-38% MAC

### Lateral CG Limits

**Maximum Lateral Imbalance:** ±500 kg  
**Typical Lateral CG:** Within ±200 kg

Lateral imbalance controlled by:
- Symmetrical passenger seating
- Balanced cargo loading
- Fuel management system
- CAOS monitoring and alerts

## BWB-Specific Considerations

The wider CG range for BWB configuration is driven by:

1. **Distributed Payload Volume:**
   - Passenger cabin spans 32m width
   - Cargo holds distributed across wing-body
   - Greater longitudinal and lateral distribution

2. **H₂ Fuel Distribution:**
   - Multiple tank locations (4 primary tanks)
   - Tank-to-tank fuel transfer capability
   - CG management through fuel sequencing

3. **Aerodynamic Characteristics:**
   - Integrated lift generation across body
   - Natural pitch stability from configuration
   - Reduced horizontal tail size/weight

4. **Control Authority:**
   - Enhanced pitch control from configuration
   - Distributed control surfaces
   - Fly-by-wire with CG compensation

## CG Management System

**CAOS Integration:**
- Real-time CG calculation and monitoring
- Predictive CG for fuel burn planning
- Loading optimization recommendations
- Automated fuel transfer scheduling
- Crew alerting for out-of-limits conditions

**Manual Procedures:**
- Load and trim sheet calculations
- Pre-flight CG verification
- In-flight fuel management procedures
- Abnormal CG recovery procedures

## Verification

- **Analysis:** Stability derivatives validated across envelope
- **Test:** Ground balance tests with extreme loading
- **Demonstration:** Flight test validation

### Verification Methods

1. **Stability Analysis:**
   - Static margin ≥ 5% at all CG positions
   - Dynamic stability modes acceptable
   - Control authority sufficient at all CG positions

2. **Ground Tests:**
   - Weighing with ballast at extreme CG positions
   - Landing gear load distribution verified
   - Fuel transfer system operation validated

3. **Flight Tests:**
   - Handling qualities evaluation at CG extremes
   - Stall characteristics at forward and aft CG
   - Autopilot performance across CG range
   - Emergency procedures validation

## Compliance

- CS-25.27: Center of gravity limits
- CS-25.143: General (controllability and maneuverability)
- CS-25.147: Directional and lateral control
- CS-25.161: Trim
- CS-25.173: Static longitudinal stability
- CS-25.175: Demonstration of static longitudinal stability

## Operational Procedures

### Pre-Flight:
1. Calculate actual CG from load manifest
2. Verify CG within limits for takeoff weight
3. Plan fuel burn sequence for CG control
4. Brief crew on CG management procedures

### In-Flight:
1. Monitor CG through CAOS system
2. Execute fuel transfer per flight plan
3. Respond to CG alerts/warnings
4. Adjust flight plan if CG limits threatened

### Emergency:
1. Emergency fuel dump procedures (if installed)
2. Passenger redistribution procedures
3. Cargo jettison procedures (if applicable)
4. Abnormal CG recovery procedures

## Related Requirements

- RQ-02-10-20-001: MTOW Specification
- RQ-02-10-20-002: MLW Specification
- RQ-02-10-20-003: MZFW Specification
- RQ-02-10-20-004: OEW Specification
- RQ-02-10-30-003: H2 Fuel Capacity
- RQ-02-10-50-003: CAOS Integration

---

**Document Control:**
- Version: 1.0
- Status: Approved
- Last Updated: 2025-11-05
- Approved By: Flight Dynamics Lead Engineer
- Reviewed By: Flight Test Chief, Certification Specialist
