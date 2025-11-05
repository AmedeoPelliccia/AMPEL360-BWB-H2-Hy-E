# Passenger Distribution Design

## Executive Summary

The AMPEL360 BWB's 38-meter-wide cabin requires careful passenger distribution strategy to maintain CG within limits while maximizing comfort and operational flexibility.

## Cabin Layout

### Seating Zones

**Zone A (Forward) - Stations 8-13m**
- **Capacity:** 60 passengers (6 rows × 10 seats)
- **CG Impact:** Forward of datum (18% MAC)
- **Configuration:** Business class (2-3-2-3 layout)

**Zone B (Center) - Stations 13-18m**
- **Capacity:** 100 passengers (10 rows × 10 seats)
- **CG Impact:** Near datum (25% MAC)
- **Configuration:** Economy plus (2-4-4-4-2 layout)

**Zone C (Aft) - Stations 18-23m**
- **Capacity:** 60 passengers (6 rows × 10 seats)
- **CG Impact:** Aft of datum (32% MAC)
- **Configuration:** Economy (3-5-5-3 layout)

**Total Capacity:** 220 passengers

## CG Control Strategy

### Loading Principles

**Balanced Loading (Target: 27% MAC)**
- Fill Zones A and C proportionally
- Zone B serves as buffer
- Minimize CG shift during boarding

**Forward CG Scenarios (< 25% MAC)**
- Load Zone A to capacity first
- Fill Zone B forward-to-aft
- Limit Zone C to maintain forward CG
- Use case: Heavy aft cargo

**Aft CG Scenarios (> 30% MAC)**
- Load Zone C to capacity first
- Fill Zone B aft-to-forward
- Limit Zone A to maintain aft CG
- Use case: Heavy forward cargo or H2 in wing tanks

### Load Planning Algorithm

```
Target CG = 27% MAC

If (Passenger Load < 50%):
  - Load Zone B only (natural balance)
  
If (Passenger Load 50-80%):
  - Load Zones A + C proportionally
  - Fill Zone B center-out
  
If (Passenger Load > 80%):
  - Optimize with cargo and fuel distribution
  - CAOS calculates optimal seat assignments
```

## Operational Procedures

### Boarding Process

**Check-In Assignment**
- CAOS pre-calculates seat assignments
- Zone assignments based on:
  - Passenger count
  - Cargo load
  - H2 fuel quantity
  - Target CG (27% MAC)

**Boarding Sequence**
1. Zone B center (establish base CG)
2. Zones A and C simultaneously (maintain balance)
3. Zone B outer seats (fine tuning)

**CG Monitoring**
- Real-time weight updates from boarding bridge sensors
- CAOS recalculates CG every 30 seconds
- Alerts crew if deviating from plan

### In-Flight Considerations

**Passenger Movement**
- Expected CG shift: ±1% MAC
- Lavatory distribution: 4 forward, 6 center, 4 aft (balanced)
- Galley locations: Balanced at 15% and 35% MAC

**Emergency Scenarios**
- CG impact analysis for passenger evacuation
- Preferred exit usage to maintain balance
- CAOS guides crew for safe egress

## Weight Calculations

### Per Zone Weight Summary

| Zone | Passengers | Pax Weight | Baggage | Seats | Total | CG (% MAC) |
|------|------------|-----------|---------|-------|-------|------------|
| A    | 60         | 5,700 kg  | 900 kg  | 480 kg| 7,080 kg | 18% |
| B    | 100        | 9,500 kg  | 1,500 kg| 750 kg| 11,750 kg| 25% |
| C    | 60         | 5,700 kg  | 900 kg  | 480 kg| 7,080 kg | 32% |
| **Total** | **220** | **20,900 kg** | **3,300 kg** | **1,710 kg** | **25,910 kg** | **25%** |

### Standard Passenger Assumptions
- Adult: 95 kg (including carry-on)
- Child: 70 kg
- Infant: 10 kg
- Checked baggage: 15 kg per pax (loaded in cargo)

## Design Validation

### CG Sensitivity Analysis

**Maximum Forward Loading**
- All Zone A full, Zone C empty
- CG: 21% MAC
- Within limits (15% forward limit)

**Maximum Aft Loading**
- All Zone C full, Zone A empty  
- CG: 31% MAC
- Within limits (42% aft limit)

**Critical Combinations**
- Full pax + forward cargo + aft H2: 19% MAC ✓
- Full pax + aft cargo + forward H2: 35% MAC ✓
- Half pax + unbalanced cargo: CAOS optimizes seating

### Operational Flexibility

**Load Factor Scenarios**
- 50% LF: Zone B only (perfect balance)
- 70% LF: A+C balanced, some B
- 85% LF: Optimized distribution
- 95% LF: All zones, cargo/fuel balanced

**Charter Configurations**
- All-business: 120 pax in Zones A+B (CG: 22% MAC)
- High-density: 240 pax (requires cargo balancing)
- Cargo conversion: Passenger floor reinforced for freight

## Integration with Systems

### CAOS Integration
- Pre-flight load optimization
- Real-time boarding monitoring
- In-flight CG tracking
- Post-flight load analysis for fleet learning

### Ground Systems
- Check-in system interfaces with CAOS
- Automated seat assignment
- Load sheet generation
- Boarding pass zone printing

### Flight Deck Interface
- Weight & balance display
- CG position indicator
- Loading progress monitoring
- Alert system for limit approach

---

**References:**
- Cabin Layout Drawing: DWG-CABIN-001
- Weight & Balance Manual: WBM-004 Passenger Distribution
- CAOS Load Planning: ATA 45-00-00
- CS-25.27 Compliance: CRT-WB-2025-001
