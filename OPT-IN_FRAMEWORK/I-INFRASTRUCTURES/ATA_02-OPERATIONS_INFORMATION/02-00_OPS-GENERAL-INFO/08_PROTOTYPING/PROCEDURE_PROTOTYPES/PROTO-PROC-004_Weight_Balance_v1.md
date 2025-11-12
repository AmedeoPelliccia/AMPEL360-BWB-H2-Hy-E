# PROTO-PROC-004 - Weight and Balance Procedure v1.0

**Prototype ID:** PROTO-PROC-004  
**Version:** 1.0  
**Date:** 2025-10-05  
**Status:** Review  
**Lead:** Load Planning Team

## Overview

Weight and balance procedures specific to the BWB configuration and H2 fuel system.

## BWB-Specific Considerations

The Blended Wing Body configuration has unique weight and balance characteristics:
- Wide center of gravity range
- H2 fuel located in upper fuselage
- Passenger distribution affects CG significantly
- Different loading strategy vs. conventional aircraft

## Standard Loading Zones

### Zone A - Forward Cabin (Rows 1-8)
- Capacity: 80 passengers
- CG impact: Forward bias
- Use for: Short-range flights

### Zone B - Mid Cabin (Rows 9-16)
- Capacity: 80 passengers
- CG impact: Neutral
- Use for: Balanced loading

### Zone C - Aft Cabin (Rows 17-24)
- Capacity: 60 passengers
- CG impact: Aft bias
- Use for: Long-range flights (with forward H2 fuel)

## H2 Fuel Weight Considerations

- H2 fuel weight: 0.5-3.5 kg/kg kerosene equivalent
- Located in forward upper fuselage tanks
- CG shift during flight is minimal
- CAOS monitors CG in real-time

## Weight and Balance Calculation Procedure

### 1. Aircraft Basic Empty Weight
- Reference: Weight and Balance Manual
- Last weigh date: [Verify current]
- Basic Empty Weight: 85,000 kg
- Basic Empty CG: Station 45.2

### 2. Passenger Loading
1. Count passengers per zone
2. Use standard weights (85 kg summer / 90 kg winter)
3. Calculate moment per zone
4. Sum total passenger weight and moment

### 3. Cargo Loading
1. Forward cargo hold: Max 5,000 kg (Station 25)
2. Aft cargo hold: Max 5,000 kg (Station 65)
3. Calculate moments

### 4. H2 Fuel Loading
1. Determine required fuel (kg)
2. H2 tank location: Station 40
3. Calculate fuel moment
4. Verify tank capacity not exceeded (3,500 kg max)

### 5. Zero Fuel Weight Check
- ZFW = BEW + Passengers + Cargo
- Verify ZFW < MZFW (95,000 kg)
- Check ZFW CG within limits

### 6. Takeoff Weight Check
- TOW = ZFW + Fuel
- Verify TOW < MTOW (110,000 kg)
- Check TOW CG within limits (42.0 - 48.0)

### 7. Landing Weight Estimate
- LW = TOW - Trip Fuel
- Verify LW < MLW (100,000 kg)
- Check LW CG within limits

## CAOS Weight Monitoring

- Real-time weight calculation
- In-flight CG monitoring
- Fuel consumption tracking
- Predictive landing weight

## Evaluation Results

- **Tested By:** Load Planners (3 evaluators)
- **Result:** Draft
- **Comments:** Need to validate BWB CG envelope
- **Next Action:** FEA validation of CG limits

---

**Document Control:**
- **Next Review:** 2025-11-20
- **Approval Required:** Chief Pilot, Load Master
