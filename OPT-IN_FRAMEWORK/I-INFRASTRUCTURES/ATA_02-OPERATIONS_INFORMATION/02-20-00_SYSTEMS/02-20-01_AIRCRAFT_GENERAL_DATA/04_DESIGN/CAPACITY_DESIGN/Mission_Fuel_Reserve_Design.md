# Mission Fuel Reserve Design

## Executive Summary

The AMPEL360 mission fuel and reserve design ensures safe operations with adequate reserves for diversion, holding, and contingencies while optimizing the unique characteristics of hydrogen fuel systems.

## Regulatory Requirements

### CS-25 / FAR 121 Reserve Fuel Requirements

**IFR Operations:**
1. **Destination Fuel:** Fuel to destination airport
2. **Approach/Landing:** 300 kg H2 (conservative)
3. **Missed Approach:** 150 kg H2
4. **Diversion:** Fuel to alternate (200 km assumed)
5. **Hold at Alternate:** 30 minutes at 1,500 ft
6. **Final Reserve:** 45 minutes at holding speed
7. **Contingency:** 5% of trip fuel or 5 minutes (greater)

### ETOPS Reserve Requirements

**ETOPS-120 (Target Certification):**
- All IFR reserves above, plus:
- **ETOPS Critical Fuel:** Fuel to nearest suitable airport
- **ETOPS Hold:** 30 minutes holding at alternate
- **ETOPS Additional:** Weather contingency (10% of ETOPS segment)

## Fuel Planning Calculation

### Typical Mission Profile (3,500 km)

**Flight Phases:**
```
1. Taxi Out:           250 kg H2   (20 minutes)
2. Takeoff:            180 kg H2   (2 minutes)
3. Climb:              850 kg H2   (25 minutes to FL390)
4. Cruise:           3,200 kg H2   (4.5 hours at M0.78)
5. Descent:            120 kg H2   (25 minutes)
6. Approach/Land:      100 kg H2   (15 minutes)
   ───────────────────────────────────────────
   TRIP FUEL:        4,700 kg H2
```

**Reserve Fuel:**
```
7. Contingency:        235 kg H2   (5% of trip fuel)
8. Alternate:          450 kg H2   (200 km + approach)
9. Hold (alternate):   320 kg H2   (30 min at 1500 ft)
10. Final Reserve:     480 kg H2   (45 min holding)
    ───────────────────────────────────────────
    RESERVE FUEL:    1,485 kg H2
```

**Total Fuel Required:** 4,700 + 1,485 = **6,185 kg H2**

**Available Capacity:** 6,500 kg H2  
**Margin:** 315 kg (5% of required, 2% of capacity)

### Fuel Planning Conservatism

**Built-in Margins:**
- Cruise fuel: Based on ISA +10°C, 95% probability winds
- Climb fuel: Worst case weight (MTOW)
- Contingency: 5% minimum (typically plan 10%)
- Alternate selection: Suitable weather requirements
- Final reserve: Not planned to be used

**Statistical Diversion Rate:**
- Historical data: 2.5% of flights divert
- Reserve usage: < 0.5% of flights use final reserve
- System design: Reserves protect 99.9% of scenarios

## H2 Fuel Characteristics

### Fuel Cell Performance Considerations

**Variable Efficiency:**
- Peak efficiency: 60% at 40% power
- Cruise efficiency: 55% at 70% power
- Descent efficiency: 50% at 20% power (less optimal)
- Ground idle: 45% (fuel cell minimum power)

**Reserve Fuel Efficiency:**
- Hold power: 30% rated (good efficiency ~57%)
- Final reserve calculation: Conservative 50% efficiency
- Actual performance: Typically better than planned

### Hydrogen Pressure Management

**Tank Pressure vs Range:**
- Full tanks: 700 bar (all fuel usable)
- End of cruise: 200 bar (still usable)
- Minimum usable: 50 bar (fuel cell inlet pressure)
- **Trapped fuel:** < 2% below 50 bar (acceptable)

**Pressure-Based Gauging:**
- Primary: Mass flow integration (totalizer)
- Secondary: Pressure-temperature calculation (PVT)
- Tertiary: Ullage volume estimation
- Accuracy: ±2% of capacity (better than conventional)

### Temperature Effects

**Fuel Temperature Management:**
- Tank temperature: Monitored continuously
- Warming during flight: Minimal (good insulation)
- Fuel density impact: Accounted in PVT calculation
- Reserve calculation: Conservative temperature assumed

## Reserve Fuel Strategy

### Minimum Fuel Advisory

**Fuel States (kg H2 remaining):**
- **Bingo Fuel:** 1,800 kg (must divert or land immediately)
- **Minimum Fuel:** 1,200 kg (declare emergency if cannot land within 30 min)
- **Emergency Fuel:** 750 kg (final reserve only remaining)

**CAOS Fuel Monitoring:**
- Continuous fuel calculation
- Prediction of fuel at destination
- Alert at contingency fuel consumption
- Advisory at minimum fuel state
- Emergency declaration recommendation

### Alternate Airport Selection

**Selection Criteria:**
- **Distance:** < 400 km from destination
- **H2 Refueling:** Available (critical requirement)
- **Weather:** Above minimums at ETA +/- 1 hour
- **Runway:** Adequate length for MLW landing
- **Facilities:** Fire/rescue, H2 emergency response

**Pre-Designated Alternates:**
- Listed in flight plan
- H2 infrastructure verified
- Weather checked before departure
- Communicated to ATC

### Contingency Fuel

**5% Contingency Rationale:**
- Accounts for weather variations
- Covers ATC routing changes
- Allows for minor system inefficiencies
- Typical usage rate: 3% on average

**10% Enhanced Contingency (Optional):**
- Used for winter operations
- High wind route segments
- Limited alternate availability
- ETOPS operations
- Reduces payload but increases safety margin

## ETOPS Fuel Planning

### ETOPS-120 Mission Profile

**Critical Scenarios:**
1. **Single Fuel Cell Failure:**
   - Remaining fuel cells: Adequate power
   - Fuel flow increase: ~8% (less efficient distribution)
   - Additional fuel required: Accounted in ETOPS planning

2. **Diversion from ETOPS Entry:**
   - Fuel to entry point: Calculated
   - Fuel to suitable airport: Max 120 min
   - Hold + final reserve: As standard
   - Weather contingency: +10% of ETOPS segment

3. **Depressurization Scenario:**
   - Descent to FL100: Higher fuel flow
   - Increased drag: 35% more fuel burn
   - ETOPS planning: Includes depressurization scenario

**ETOPS Fuel Calculation:**
```
ETOPS Fuel = MAX(
  Normal reserves,
  [Fuel to ETOPS alternate + Hold + Final + Weather],
  [Fuel to ETOPS alternate + Hold + Final + Depressurization scenario]
)
```

**Typical ETOPS Penalty:** +15% fuel vs non-ETOPS

### ETOPS Alternate Requirements
- **Suitable Airport:** H2 infrastructure mandatory
- **Weather Mins:** Above operator minimums by 400 ft/2 km
- **Availability:** > 95% probability at ETA
- **Distance:** < 120 minutes single fuel cell

## In-Flight Fuel Management

### Fuel Optimization

**CAOS Functions:**
- Real-time fuel flow monitoring
- Performance comparison to flight plan
- Re-calculation of reserves continuously
- Optimal altitude recommendations
- Speed optimization for fuel conservation

**Fuel Conservation Techniques:**
- Optimal cruise altitude (FL370-FL410)
- Speed management (LRC vs ECON)
- Route optimization (winds aloft)
- Early descent planning
- Single fuel cell operation (if ahead on fuel)

### Fuel Transfer for CG

**Transfer Logic:**
- Primary goal: Maintain CG 26-28% MAC (best L/D)
- Secondary goal: Balanced fuel cell loading
- Transfer rate: 50 kg/min
- Minimize transfers: Reduces system wear

**Transfer Scenarios:**
- Passenger movement: Automated compensation
- Cargo shift (rare): Automated compensation
- Performance optimization: Crew-initiated
- Emergency rebalancing: Automated priority

### Fuel Monitoring and Alerting

**EICAS Messages:**
- `FUEL QTY LOW`: At contingency fuel state
- `FUEL DIVERSION ADVISED`: At minimum fuel state
- `FUEL EMERGENCY`: At emergency fuel state (auto declared to ATC)

**Flight Deck Display:**
- Current fuel quantity (kg)
- Fuel flow rate (kg/hour)
- Fuel at destination (predicted)
- Reserve remaining (color coded: Green/Amber/Red)
- Time to minimum fuel (if applicable)

## Ground Fuel Management

### Fuel Loading Procedures

**Pre-Flight Fuel Order:**
- CAOS generates fuel requirement
- Dispatcher reviews and approves
- Fuel order sent to H2 supplier
- Load sheet prepared with CG calculation

**Fueling Sequence:**
1. Aircraft chocked and grounded
2. Safety zone established (15m radius)
3. APU shutdown, passengers clear
4. Fuel truck connection (underwing)
5. Automated fill sequence (45 minutes)
6. Pressure stabilization (5 minutes)
7. Disconnect and safety check
8. Load sheet verification

**Defueling Procedures:**
- Rarely required (plan for full tanks)
- If required: Vent to storage tanks
- Time: 60 minutes
- Safety: Same as fueling

### Tankering Decision

**Economic Tankering:**
- H2 price differential: > $2/kg variance
- Payload penalty: 15 pax per 500 kg extra fuel
- MTOW limit: Restricts tankering
- CAOS calculation: Recommends optimal tankering

**Operational Tankering:**
- Destination fuel unavailable: Full tanks
- Price/availability uncertain: Conservative fill
- Return flight same day: Tank for round trip

---

**References:**
- Fuel Planning Manual: FPM-001
- ETOPS Operations Manual: EOM-001
- CS-25.1001: Fuel System Requirements
- H2 Fuel Management: ATA 28-00-00
- CAOS Fuel Optimization: ATA 45-00-00
