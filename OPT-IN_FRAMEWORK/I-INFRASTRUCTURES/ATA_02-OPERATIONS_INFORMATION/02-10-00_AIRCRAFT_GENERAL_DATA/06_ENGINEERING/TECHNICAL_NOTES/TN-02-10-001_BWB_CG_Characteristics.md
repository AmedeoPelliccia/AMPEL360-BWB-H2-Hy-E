# TN-02-10-001: BWB Center of Gravity Characteristics

**Document ID:** TN-02-10-001  
**Title:** BWB Configuration CG Behavior and Management  
**Project:** AMPEL360 BWB H₂ Hy-E Q100 INTEGRA  
**Date:** 2025-11-05  
**Author:** AMPEL360 Engineering Team  
**Classification:** Technical Note

---

## Summary

This technical note describes the unique center of gravity characteristics of the Blended Wing Body configuration and provides guidance for CG management during design and operations.

---

## 1. BWB CG Fundamentals

### 1.1 Key Differences from Conventional Aircraft

**Conventional Tube-and-Wing:**
- CG typically 25-30% MAC
- Narrow CG range (5-8% MAC)
- Limited by wing-fuselage geometry
- Cargo/fuel in wings

**AMPEL360 BWB:**
- CG typically 20-32% MAC (operational)
- Wider CG envelope (27% MAC range, 15-42% allowed)
- Flexible due to distributed geometry
- Cargo/fuel in center body
- **8.5 m longitudinal control range through fuel management**

### 1.2 BWB Advantages

1. **Larger CG Envelope:** More design flexibility
2. **Better Control Authority:** Wide body allows strategic placement
3. **Fuel CG Management:** H₂ tanks provide active control
4. **Payload Flexibility:** Wide cabin enables load distribution

---

## 2. CG Control Strategy

### 2.1 Load Configuration Planning

**Critical Load Cases:**

| Configuration | Condition | CG Position | % MAC | Control Method |
|---------------|-----------|-------------|-------|----------------|
| **Most Forward** | Full forward pax + aft cargo | 16.40 m | 19.2% | Use forward H₂ tank |
| **Most Aft** | Full aft pax + forward cargo | 18.02 m | 32.5% | Use aft H₂ tank (CRITICAL) |
| **Nominal** | Balanced loading | 17.50 m | 27.0% | All tanks equally |

**Design Validation:** All cases within 15-42% MAC limits ✓

### 2.2 Fuel Management for CG Control

**H₂ Tank Positions:**
- Forward tank: 21.0 m (19.2% MAC equivalent)
- Center tank: 24.0 m (27.0% MAC equivalent)
- Aft tank: 29.0 m (35.3% MAC equivalent)

**Active CG Control:**
- Select tank draw sequence based on load configuration
- Maintain CG in optimal 22-30% MAC range for cruise
- Minimize trim drag (saves 2-3% fuel)

---

## 3. Loading Guidelines

### 3.1 Passenger Seating Strategy

**Forward CG Risk Scenarios:**
- Heavy forward cargo + light aft seating
- Empty aft cabin (less than 50% aft occupancy)

**Mitigation:**
- Close aft rows first during boarding
- Balance cargo between forward/aft holds
- Use forward H₂ tank first (moves CG aft)

**Aft CG Risk Scenarios:**
- Full aft seating + heavy forward cargo
- **Most critical: All aft rows full + maximum forward cargo**

**Mitigation:**
- Limit forward cargo when aft cabin is full
- Open forward rows first
- Use aft H₂ tank first (moves CG forward)

### 3.2 Cargo Loading Strategy

**Standard Practice:**
- Balance cargo fore/aft: 50/50 split nominal
- Maximum forward: 8,000 kg
- Maximum aft: 7,000 kg
- Total: 15,000 kg available

**CG Impact:**
- Forward cargo: -0.24 m CG shift per 1,000 kg
- Aft cargo: +0.35 m CG shift per 1,000 kg

---

## 4. In-Flight CG Management

### 4.1 Fuel Burn Sequence

**Optimal Cruise CG: 24-28% MAC** (minimizes trim drag)

**Example Mission Profile:**

| Phase | Start CG | Fuel Action | End CG | Trim Benefit |
|-------|----------|-------------|--------|--------------|
| Takeoff | 27.0% | Balanced | 27.0% | Neutral |
| Climb | 27.0% | Use center tank | 26.5% | Slight forward |
| Cruise 1-4h | 26.5% | Use forward tank | 28.0% | Moving aft |
| Cruise 4-8h | 28.0% | Use aft tank | 26.0% | Optimizing |
| Descent | 26.0% | Minimal use | 25.5% | Good for landing |

**Result:** Maintain 25-28% MAC throughout, optimal trim

### 4.2 Fuel Management Computer

**Automated System:**
- Monitors real-time CG position
- Calculates optimal tank for next fuel draw
- Provides pilot advisory displays
- Can operate fully automatic or manual override

**Pilot Interface:**
- Current CG position display
- Fuel remaining each tank
- Recommended tank selection
- Manual override capability

---

## 5. CG Envelope Characteristics

### 5.1 Forward CG Limit (15% MAC)

**Aerodynamic Implications:**
- Increased static stability
- Reduced elevator effectiveness
- Higher control forces
- May limit maneuverability

**Structural Implications:**
- Higher nose-up moment in cruise
- Increased elevator deflection
- Higher trim drag penalty

**Critical Cases:**
- OEW + minimum fuel + forward cargo only
- Never occurs in normal operations ✓

### 5.2 Aft CG Limit (42% MAC)

**Aerodynamic Implications:**
- Reduced static stability
- Enhanced elevator effectiveness
- Lighter control forces
- Risk of pitch instability

**Structural Implications:**
- Lower trim drag (if not excessive)
- Reduced elevator authority required
- Better L/D if within optimal range

**Critical Case:**
- Full aft seating + full forward cargo + aft fuel loading
- CG = 32.5% MAC (within limits but requires attention)

---

## 6. Stability and Control

### 6.1 Static Stability

**CG Position vs Stability Margin:**

| CG Position | Static Margin | Handling | Trim Drag |
|-------------|---------------|----------|-----------|
| 15-20% MAC | +15% to +10% | Heavy | Moderate |
| 20-25% MAC | +10% to +5% | Good | Low |
| 25-30% MAC | +5% to 0% | Neutral | Optimal ✓ |
| 30-35% MAC | 0% to -5% | Light | Low |
| 35-42% MAC | -5% to -10% | Very Light | Moderate |

**Design Target:** 24-28% MAC for cruise (neutral-stable, optimal trim)

### 6.2 Control Authority

**Elevator Sizing:**
- Sized for 15% MAC forward limit
- Provides adequate authority to 42% aft limit
- 60 m² total elevon area
- ±25° deflection range

**Fly-by-Wire Benefits:**
- Artificial stability augmentation
- Allows wider CG envelope
- Maintains consistent handling across CG range
- Automatic load alleviation

---

## 7. Design Recommendations

### 7.1 Component Placement Guidelines

**For Equipment/Systems:**
- Heavy items (batteries, fuel cells): Place near design CG (24-26% MAC)
- Variable items (cargo): Distribute fore/aft
- Fixed items (structure): Optimize for all load cases

**Weight Distribution Targets:**
- 40% forward of 20% MAC
- 35% between 20-30% MAC
- 25% aft of 30% MAC

### 7.2 Future Modifications

**CG Impact Assessment Required For:**
- Passenger capacity changes
- Cargo configuration modifications
- H₂ tank capacity increases
- Major equipment relocations
- Structural reinforcements

**Process:**
1. Calculate new component CG
2. Update weight and balance database
3. Verify all load cases within envelope
4. Update loading manual if required

---

## 8. Operational Considerations

### 8.1 Loading Manual

**Pilot Responsibilities:**
- Verify load sheet before flight
- Confirm CG within envelope
- Select appropriate fuel management strategy
- Monitor CG during flight

**Load Planner Responsibilities:**
- Balance passenger distribution
- Optimize cargo placement
- Calculate accurate CG position
- Provide fuel loading recommendation

### 8.2 Abnormal Situations

**CG Out of Limits:**
- Do not dispatch aircraft
- Redistribute load or off-load
- Recalculate and verify

**In-Flight CG Excursion:**
- Immediate fuel redistribution (if able)
- Reduce speed if necessary
- Land at nearest suitable airport

---

## 9. Conclusions

The BWB configuration provides excellent CG management flexibility through:
- Wide 27% MAC envelope (vs 5-8% conventional)
- 8.5 m fuel CG control range
- Distributed passenger/cargo placement options
- Automated fuel management system

**Key Takeaway:** Active management of H₂ fuel distribution enables optimal CG throughout flight, reducing trim drag by 2-3% and enhancing handling qualities.

---

**References:**
1. CALC-02-10-002: CG Calculation Matrix
2. SIM-02-10-101: CG Envelope Validation
3. AR-02-10-002: Weight Estimation Analysis
4. TS-02-10-003: H₂ Tank Location Trade Study

---

**Document Control:**
- **Version:** 1.0
- **Date:** 2025-11-05
- **Next Review:** 2026-02-05

*END OF TECHNICAL NOTE*
