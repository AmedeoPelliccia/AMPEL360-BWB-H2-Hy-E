# Range-Payload Trade

## Executive Summary

The AMPEL360 range-payload trade analysis defines the operational envelope balancing passenger capacity, cargo volume, H2 fuel, and mission requirements to optimize for regional/medium-haul markets.

## Design Point Selection

### Baseline Mission

**Design Mission:**
- **Passengers:** 220 (100% load factor)
- **Cargo:** 15,000 kg
- **Range:** 4,000 km
- **Reserves:** Full IFR + ETOPS
- **MTOW:** 145,000 kg

**Key Parameters:**
- **OEW:** 66,500 kg
- **Payload:** 35,900 kg (20,900 kg pax + 15,000 kg cargo)
- **Fuel:** 6,500 kg H2
- **MZFW:** 118,000 kg (OEW + payload)
- **MLW:** 130,000 kg

## Range-Payload Diagram

### Trade Curve

```
Payload (kg)
  40,000 │         Design Point (220 pax + 15 T cargo)
         │              ●
  35,000 │           ╱   ╲
         │         ╱       ╲
  30,000 │       ╱           ╲
         │     ╱               ╲  Max Fuel
  25,000 │   ╱                   ╲
         │ ╱                       ╲
  20,000 │●─────────────────────────●
         │ MZFW                  Max Fuel
         │ Limited                Limited
         └────────────────────────────── Range (km)
           0    1,000  2,000 3,000 4,000  5,000

Key Points:
A: Max payload, no fuel (ferry range only)
B: 220 pax + 15T cargo, 4,000 km (design point) ✓
C: 220 pax, no cargo, 4,500 km (max pax range)
D: No pax, max cargo, 3,000 km (cargo mission)
E: No payload, max fuel, 6,500 km (ferry range)
```

## Operational Scenarios

### Scenario 1: Full Passenger + Full Cargo (Design Point)

**Configuration:**
- Passengers: 220 (20,900 kg)
- Cargo: 15,000 kg
- Total payload: 35,900 kg
- Fuel: 6,500 kg H2
- **Range: 4,000 km** ✓

**Routes:**
- London-Istanbul: 2,500 km (comfortable)
- New York-Miami: 1,750 km (excellent margin)
- Frankfurt-Dubai: 4,200 km (requires slight reduction or stop)

**Load Factor Sensitivity:**
- 85% LF: 187 pax, 17,750 kg, +280 km range
- 100% LF: 220 pax, 20,900 kg, design range
- Over-booking: Not possible (MZFW limit)

### Scenario 2: Max Passengers, Reduced Cargo

**Configuration:**
- Passengers: 220 (20,900 kg)
- Cargo: 10,000 kg (reduced)
- Total payload: 30,900 kg
- Fuel: 7,400 kg H2 (increased)
- **Range: 4,500 km**

**Routes:**
- London-Dubai: 4,500 km ✓ (possible!)
- Paris-Cairo: 3,200 km (excellent)
- Tokyo-Mumbai: 5,800 km (still requires stop)

**Trade-off:**
- +500 km range
- -5,000 kg cargo revenue (~ -$5,000/flight)
- Use case: Long thin routes, low cargo demand

### Scenario 3: Reduced Passengers, Max Cargo

**Configuration:**
- Passengers: 150 (14,250 kg)
- Cargo: 20,900 kg (increased)
- Total payload: 35,150 kg
- Fuel: 6,600 kg H2
- **Range: 4,100 km**

**Use Case:**
- Cargo charter
- Off-peak passenger demand
- High cargo rates

**Economics:**
- Lost pax revenue: 70 pax × $300 = -$21,000
- Gained cargo: 5,900 kg × $1.50/kg = +$8,850
- Net: -$12,150 (not economical unless cargo rate higher)

### Scenario 4: All-Cargo Configuration

**Configuration:**
- Passengers: 0
- Cargo: 45,000 kg (convertible variant)
- Total payload: 45,000 kg
- Fuel: 5,800 kg H2 (reduced for weight)
- **Range: 3,000 km**

**Market:**
- Express cargo (FedEx, UPS)
- Night operations
- Conversion: 8-hour quick-change

**Economics:**
- Revenue: 45,000 kg × $1.50/kg = $67,500
- vs pax: 220 pax × $300 = $66,000
- Competitive if cargo rates good

### Scenario 5: Ferry / Positioning Flight

**Configuration:**
- Passengers: 0
- Cargo: 0
- Total payload: 0
- Fuel: 8,900 kg H2 (maximum tankage)
- **Range: 6,500 km**

**Use Case:**
- Aircraft delivery
- Maintenance ferry
- Positioning between bases

**Note:** Rarely used; design based on revenue missions

## MTOW and MLW Limitations

### Maximum Takeoff Weight (MTOW): 145,000 kg

**Limit Cases:**
- Full payload + full fuel: 66,500 + 35,900 + 6,500 = 108,900 kg ✓ (within MTOW)
- Overload not possible: Aircraft designed for max efficiency at MTOW

**Performance at MTOW:**
- Takeoff distance: 2,300 m (sea level, ISA)
- Initial climb: 2,000 fpm
- Cruise altitude: FL370 initial

### Maximum Zero Fuel Weight (MZFW): 118,000 kg

**Structural Limit:**
- OEW + payload ≤ 118,000 kg
- 66,500 + payload ≤ 118,000
- **Max payload: 51,500 kg**

**Why MZFW Limits Payload:**
- Wing bending relief: Fuel in wing reduces loads
- Without fuel: Structure must carry full payload → Stress limit
- Design: Ensures structure not overloaded

**Example:**
- 220 pax + 30,600 kg cargo = 51,500 kg payload (MZFW limited)
- Fuel: Reduced to 5,500 kg H2
- Range: 3,200 km (reduced but acceptable for cargo-heavy missions)

### Maximum Landing Weight (MLW): 130,000 kg

**Limit:**
- Landing gear: Structural design limit
- Typical: 90% of MTOW (AMPEL360: 130,000 / 145,000 = 90% ✓)

**Operational Impact:**
- Normal landing: < 130,000 kg (after fuel burn)
- Emergency landing: May require fuel dump if > MLW
- Fuel dump rate: 1,500 kg/min (10 min to MLW from MTOW)

## H2 Fuel Load Flexibility

### Tank Capacity vs Mission Fuel

**Total Capacity:** 6,500 kg H2 (full tanks)

**Fuel Loading Strategy:**
| Mission Range | Fuel Required | Tanks Filled | Flexibility |
|---------------|---------------|--------------|-------------|
| 1,500 km | 2,800 kg | 43% | High ✓ |
| 2,500 km | 4,000 kg | 62% | Good |
| 3,500 km | 5,400 kg | 83% | Limited |
| 4,000 km | 6,200 kg | 95% | Minimal |
| 4,500 km | 7,000 kg | 108% | Not possible |

**Operational Flexibility:**
- Short missions: Reduced fuel → More payload or faster turnaround
- Tankering: Carry extra fuel if destination H2 expensive
- Diversion: Extra fuel for weather alternates

### Fuel vs Payload Trade

```
Additional fuel weight = Lost payload capacity (1:1 trade)

Example:
+500 kg H2 = +300 km range = -500 kg payload = -5 passengers
```

**Economic Decision:**
- Value of range extension vs value of payload
- CAOS optimization: Calculates optimal fuel load per flight

## Operational Constraints

### Airport Runway Length

**Takeoff Distance Sensitivity:**
- Heavy (MTOW): 2,300 m required
- Medium (130,000 kg): 1,950 m required
- Light (120,000 kg): 1,750 m required

**Runway-Limited Takeoff:**
- Short runway: Reduce MTOW (less payload or fuel)
- Example: 2,000 m runway → Max TOW 135,000 kg
- Payload reduction: 10,000 kg or range reduction: 800 km

### Climb Performance

**MTOW Climb:**
- Initial: 2,000 fpm (adequate)
- Continued: FL370 in 25 minutes
- Obstacle clearance: 4.5% gradient (exceeds 2.4% requirement)

**Weight Reduction Benefit:**
- -10,000 kg: +400 fpm climb rate
- Better obstacle clearance
- Quicker to cruise altitude (fuel savings)

## Economic Optimization

### Revenue Optimization

**CAOS Algorithm:**
```
For each flight:
  1. Calculate demand (passenger + cargo)
  2. Calculate fuel required for mission range
  3. Check limits (MTOW, MZFW, MLW)
  4. Optimize:
     - Max revenue = (Pax × Fare) + (Cargo × Rate)
     - Subject to: Weight limits, range requirements
  5. Generate load plan
```

**Typical Result:**
- Short range (<2,500 km): Maximize payload
- Medium range (2,500-3,500 km): Balance payload and range
- Long range (>3,500 km): Sacrifice cargo for fuel

### Cargo Tankering Decision

**Question:** Carry cargo or extra fuel for long mission?

**Analysis:**
- Cargo value: $1.50/kg
- Fuel cost: $5.50/kg (but enables mission)
- Decision: Cargo more valuable unless mission not possible

**Example:**
- 3,800 km mission: Requires 6,000 kg H2
- Option A: 220 pax, 15,000 kg cargo, 6,000 kg fuel ✓
- Option B: 220 pax, 10,000 kg cargo, 7,000 kg fuel (unnecessary)
- Choose A: Maximize cargo revenue

## Future Growth Options

### Uprated Version (AMPEL360-250)

**Concept:**
- MTOW: 160,000 kg (+10%)
- Passengers: 250 (+14%)
- Range: 3,800 km (similar)
- Fuel cells: 4.0 MW (+14%)

**Market:**
- High-density routes
- Further efficiency improvements (2035+)

### Extended Range Version (AMPEL360-220ER)

**Concept:**
- MTOW: 150,000 kg (+3%)
- Passengers: 220 (same)
- Range: 5,000 km (+25%)
- Fuel: 7,800 kg H2

**Market:**
- Thin long-haul routes
- Improved fuel cell efficiency (2035+)

## Conclusion

### Optimal Operating Point

**AMPEL360 Design Point:**
- 220 passengers + 15,000 kg cargo
- 4,000 km range
- Covers 65% of global aviation demand
- Economics: Competitive with conventional

**Flexibility:**
- Can trade range for payload (and vice versa)
- CAOS optimizes per-flight
- Adaptable to market variations

**Future:**
- Variant family: Different range/payload points
- Technology improvements: Extend capability
- Market expansion: As H2 infrastructure grows

---

**References:**
- Range-Payload Analysis: RPA-2024-001
- Weight & Balance Manual: WBM-001
- Performance Manual: PM-001 Section 3
- Economic Model: EM-PAYLOAD-2024-003
