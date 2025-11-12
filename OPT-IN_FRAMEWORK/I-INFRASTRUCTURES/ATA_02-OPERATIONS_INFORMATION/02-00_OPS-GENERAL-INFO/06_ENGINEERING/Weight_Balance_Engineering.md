# Weight & Balance Engineering
**Component Code:** 02-00-00  
**Component Name:** GENERAL  
**Document Type:** Weight & Balance Engineering Analysis

---

## Overview

This document establishes the weight and balance engineering methodology for the AMPEL360 BWB H₂ Hy-E Q100 aircraft. The unique BWB configuration requires specialized analysis for center of gravity (CG) management and balance optimization.

---

## Weight Categories

### Design Weights

| Weight Category | Value (kg) | Description |
|----------------|-----------|-------------|
| **MTOW** | 95,000 | Maximum Takeoff Weight |
| **MLW** | 85,000 | Maximum Landing Weight |
| **MZFW** | 72,000 | Maximum Zero Fuel Weight |
| **OEW** | 48,000 | Operating Empty Weight |
| **Max Payload** | 24,000 | 220 passengers + cargo |
| **Max H₂ Fuel** | 4,200 | Liquid hydrogen capacity |

---

## Center of Gravity (CG) Envelope

### BWB CG Characteristics

The Blended Wing Body configuration provides unique advantages:
- **Wider CG Range:** 25-42% MAC (vs 15-35% conventional)
- **Better stability:** Distributed load across entire body
- **Reduced trim drag:** Natural aerodynamic balance
- **Fuel tank placement:** Optimal for CG control

### CG Limits

```
Forward CG Limit:  25% MAC (most restrictive in landing)
Aft CG Limit:      42% MAC (most restrictive at MTOW)
Typical CG Range:  28-38% MAC (normal operations)
```

### CG Envelope Analysis
- Detailed calculations in: CALC-02-00-101_CG_Envelope_BWB.csv
- Loading scenarios: CALC-02-00-102_Loading_Analysis.csv
- Fuel effects: CALC-02-00-103_Fuel_Weight_Effects.csv

---

## Weight Distribution

### Longitudinal Distribution

1. **Forward Section (Stations 0-400)**
   - Flight deck equipment: 1,200 kg
   - Avionics: 800 kg
   - Forward cargo: 3,500 kg
   - Nose gear: 450 kg

2. **Center Section (Stations 400-1200)**
   - Passenger cabin: 220 pax (18,700 kg with bags)
   - H₂ fuel tanks: 4,200 kg (full)
   - Main landing gear: 3,200 kg
   - Systems: 2,800 kg

3. **Aft Section (Stations 1200-1600)**
   - Aft cargo: 2,000 kg
   - Empennage: 1,200 kg
   - APU: 450 kg
   - Fuel cell systems: 2,500 kg

### Lateral Distribution

BWB configuration considerations:
- **Symmetric loading:** Required for lateral stability
- **Fuel tank symmetry:** Automatic sequencing
- **Passenger distribution:** Managed by CAOS
- **Cargo loading:** Side-to-side balance requirements

Analysis documented in: CALC-02-00-106_Lateral_Balance.csv

---

## Loading Analysis

### Passenger Loading

**Seating Configuration:**
- Total seats: 220 (all-economy configuration)
- Aisle configuration: 2-4-2 or 3-3-3 depending on section
- Average passenger weight: 85 kg (standard)
- Baggage allowance: 23 kg per passenger

**Loading Sequences:**
1. Forward loading (preferred for CG)
2. Aft loading (backup method)
3. Distributed loading (CAOS optimized)

Documentation: CALC-02-00-104_Passenger_Distribution.csv

### Cargo Loading

**Cargo Compartments:**
- Forward hold: 12 m³ (max 3,500 kg)
- Main hold: 18 m³ (max 5,000 kg)
- Aft hold: 8 m³ (max 2,000 kg)
- Bulk cargo: 4 m³ (max 800 kg)

**Loading Restrictions:**
- Heavy cargo forward for CG control
- Dangerous goods: Specific positions
- Live animals: Pressurized/heated zones
- Special cargo: Case-by-case analysis

Documentation: CALC-02-00-105_Cargo_Distribution.csv

---

## Fuel Weight Effects

### H₂ Fuel Characteristics

**Mass Properties:**
- Liquid H₂ density: 70.8 kg/m³ (at -253°C)
- Tank capacity: 59.3 m³
- Maximum fuel mass: 4,200 kg
- Fuel CG location: Station 650 (near aircraft CG)

**Fuel Burn Effects:**
- CG shift during flight: 2-5% MAC typical
- Tank sequencing strategy: Minimize CG travel
- Boil-off consideration: 0.3-0.5% per hour
- Emergency jettison: Not available (H₂ system)

### Fuel Management Strategy

1. **Takeoff Configuration**
   - Full tanks: CG at ~32% MAC
   - Reduced fuel: Forward CG shift
   - Trim setting optimization

2. **Cruise Configuration**
   - Continuous CG monitoring by CAOS
   - Tank sequencing for CG control
   - Optimum CG for best L/D ratio

3. **Landing Configuration**
   - Minimum fuel requirement: 500 kg
   - CG range verification
   - Emergency fuel planning

Detailed analysis: CALC-02-00-103_Fuel_Weight_Effects.csv

---

## CG Shift During Flight

### Normal Operations

**Flight Phase CG Changes:**
```
Taxi:        CG = 32.0% MAC (full fuel, full pax)
Takeoff:     CG = 31.8% MAC (fuel burn during taxi)
Climb:       CG = 31.5% MAC (fuel burn)
Cruise:      CG = 30.5% MAC (mid-cruise)
Descent:     CG = 29.8% MAC (minimum fuel)
Landing:     CG = 29.5% MAC (landing config)
```

### Maximum CG Shift Rate
- Normal operations: 0.5% MAC per hour
- Maximum rate: 2% MAC per hour
- CAOS monitoring: Real-time tracking
- Alert thresholds: ±5% from planned

Documentation: CALC-02-00-107_CG_Shift_Flight.csv

---

## Balance Calculations

### Moment Calculation Method

```
Moment = Weight × Arm
Total Moment = Σ(Individual Moments)
CG Position = Total Moment / Total Weight
CG % MAC = (CG Position - MAC Leading Edge) / MAC × 100
```

### Verification Methods
1. **Pre-flight calculation:** Load sheet preparation
2. **In-flight monitoring:** CAOS digital twin
3. **Post-flight analysis:** Actual vs. planned
4. **Periodic validation:** Scale weighing

---

## BWB-Specific Considerations

### Aerodynamic Effects

**CG Impact on Performance:**
- Forward CG: Higher stability, increased drag
- Aft CG: Lower stability, reduced drag
- Optimum CG: 33-35% MAC for cruise efficiency
- BWB advantage: Wider acceptable range

**Trim Requirements:**
- Elevator deflection vs. CG position
- Trim drag penalty
- Control authority margins
- Flutter considerations

### Structural Considerations

**Load Paths:**
- Wing-body integration
- Distributed loads across BWB
- Main spar location and CG
- Landing gear attachment points

---

## Weight Control Program

### Weight Monitoring

**Throughout Development:**
- Design weight targets
- Weight growth tracking
- Weight reduction initiatives
- Final weight verification

**In Service:**
- Operational empty weight (OEW) updates
- Equipment change tracking
- Modification impact assessment
- Annual/bi-annual weighing

### Weight Reduction Strategies
1. Material optimization (composites)
2. Systems integration (CAOS efficiency)
3. H₂ system lightweighting
4. Manufacturing process improvements

---

## Regulatory Compliance

### Certification Requirements

**CS-25 / FAR Part 25:**
- CG limits establishment (§25.25)
- CG range (§25.27)
- Static longitudinal stability (§25.173)
- Loading information (§25.1583)

**Special Conditions:**
- BWB configuration approval
- H₂ fuel system weight effects
- CAOS automated balance management

---

## Operational Procedures

### Load Planning

**Pre-Flight:**
1. Calculate planned CG for all flight phases
2. Verify CG within limits
3. Determine trim setting
4. Brief crew on any restrictions

**Load Sheet Preparation:**
- CAOS automated generation
- Manual verification required
- Pilot acknowledgment
- Ground crew confirmation

### In-Flight Management

**CAOS Functions:**
- Real-time CG calculation
- Fuel sequencing optimization
- Passenger movement tracking (if significant)
- Predictive CG for destination

**Crew Procedures:**
- Monitor CG display
- Verify automated systems
- Manual override capability
- Non-normal procedures

---

## Emergency Procedures

### CG Exceedance

**Out of Forward Limit:**
- Increased elevator authority required
- Higher stall speed
- Reduced maneuverability
- Landing considerations

**Out of Aft Limit:**
- Reduced stability
- Pitch sensitivity
- Control difficulty
- Dangerous flight regime

**Recovery Actions:**
- Fuel management (if possible)
- Passenger/cargo redistribution (ground only)
- Emergency landing planning
- Consult with CAOS recommendations

---

## Related Calculations

All weight and balance calculations maintained in:
- `CALCULATIONS/Weight_Balance_Calculations/`
- Standards: CALC-02-00-101 through CALC-02-00-107

---

## Related Documents

- Performance Engineering
- H2 Fuel Engineering
- BWB Operations Engineering
- Safety Engineering Analysis
- Flight Envelope Analysis

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-05 | Weight & Balance Team | Initial release |

---

**Status:** Active  
**Next Review:** 2026-02-05  
**Owner:** AMPEL360 Weight & Balance Engineering
