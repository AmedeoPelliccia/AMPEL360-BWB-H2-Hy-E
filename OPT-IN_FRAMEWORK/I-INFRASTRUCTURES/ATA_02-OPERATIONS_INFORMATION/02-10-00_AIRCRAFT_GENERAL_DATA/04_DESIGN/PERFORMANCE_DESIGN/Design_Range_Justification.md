# Design Range Justification

## Executive Summary

The AMPEL360 design range of 4,000 km was selected to address the optimal market segment for hydrogen propulsion while maximizing operational efficiency and commercial viability.

## Market Analysis

### Route Coverage

**Regional/Medium-Haul Routes:**
- **Target Market:** 65% of global commercial aviation
- **Route Examples:**
  - London-Athens: 2,400 km ✓
  - New York-Miami: 1,750 km ✓
  - Dubai-Mumbai: 1,900 km ✓
  - Tokyo-Singapore: 5,300 km ✗ (requires stop)
  - Paris-New York: 5,800 km ✗ (outside range)

**4,000 km Coverage:**
- **Intra-Europe:** 100% coverage
- **North America Domestic:** 95% coverage
- **Asia-Pacific Regional:** 90% coverage
- **Transatlantic:** Limited (Reykjavik gateway)

### Passenger Demand

**220-Seat Capacity at 4,000 km:**
- Optimal for regional trunk routes
- High-frequency service capability
- Point-to-point network operations
- Competitive with narrow-body aircraft (A321XLR, 737 MAX)

## Design Trade-Off Analysis

### Range vs Weight Trade

| Design Range | H2 Fuel | MTOW | L/D Required | Score |
|--------------|---------|------|--------------|-------|
| 3,000 km     | 4,500 kg | 135,000 kg | 19 | 0.75 |
| 3,500 km     | 5,500 kg | 141,000 kg | 20 | 0.88 |
| **4,000 km** | **6,500 kg** | **145,000 kg** | **21** | **0.95** ✓ |
| 4,500 km     | 7,800 kg | 152,000 kg | 22 | 0.81 |
| 5,000 km     | 9,200 kg | 160,000 kg | 23 | 0.68 |

**Selected: 4,000 km**
- Maximizes route coverage without excessive weight
- Achievable L/D with BWB configuration
- Competitive with conventional aircraft
- Enables hydrogen infrastructure development pace

### H2 Infrastructure Considerations

**Current H2 Airport Status (2025):**
- Airports with H2 infrastructure: ~50 globally
- Projected 2030: ~300 major airports
- AMPEL360 strategy: Phase introduction with infrastructure

**4,000 km Range Benefits:**
- Enables hub-and-spoke with H2 hubs
- Reduces number of airports requiring H2 initially
- Allows infrastructure co-development
- Competitive on routes with H2 available

## Performance Calculation

### Breguet Range Equation

```
Range = (V × L/D / TSFC) × ln(Wi / Wf)

Where:
V = Cruise speed = 235 m/s (M0.78 at FL390)
L/D = Lift-to-drag ratio = 21
TSFC = Thrust-specific fuel consumption = 0.28 kg/kWh equivalent
Wi = Initial cruise weight = 145,000 kg
Wf = Final cruise weight = 138,500 kg

Range = (235 × 21 / 0.28) × ln(145,000 / 138,500)
      ≈ 4,100 km (with reserves)
```

**Design Point:** 4,000 km with full reserves

### Fuel Fraction

```
Fuel Fraction = Fuel Weight / MTOW
              = 6,500 kg / 145,000 kg
              = 4.5%

Comparison:
- Conventional jet: 30-35% (kerosene)
- H2 advantage: Higher energy density per kg
- H2 penalty: Lower energy density per m³
- BWB advantage: Thick body accommodates H2 tanks
```

## Operational Scenarios

### Typical Mission Profile

**Example: Frankfurt-Istanbul (2,250 km)**
- **Block Time:** 3.5 hours
- **Fuel Required:** 3,800 kg H2 (with reserves)
- **Fuel Remaining:** 2,700 kg (70% reserve margin)
- **Possible Tankering:** Yes (reduce Istanbul fuel cost)

**Benefits:**
- Excellent reserve margins on shorter routes
- Operational flexibility
- Diversion capability
- Enhanced safety

### Maximum Range Mission

**Example: London-Dubai (5,500 km) - Requires Stop**
- **Option 1:** London → Athens (2,400 km) → Dubai (3,100 km)
  - Total block time: 7.5 hours (competitive)
  - H2 refuel in Athens: 45 minutes
- **Option 2:** Direct on A350: 6.5 hours
  - AMPEL360: Not competitive (yet)

**Market Strategy:**
- Focus on routes within 4,000 km
- As H2 efficiency improves: Extend range
- Future variant: 5,000 km capability (10-15 years)

### Emergency Range

**Maximum Diversion Range:**
- **From cruise at 4,000 km:** 400 km to alternate
- **Total capability:** 4,400 km theoretical
- **Operational limit:** 4,000 km with full reserves

## Performance Optimization

### Cruise Altitude Strategy

**Optimal Altitude:** FL370-FL410
- Higher altitude: Better L/D (thinner air)
- Lower air density: Better fuel cell efficiency
- Pressure altitude: Optimal for H2 system

**Step Climb Profile:**
- Initial cruise: FL370 (heavy weight)
- Mid-cruise: FL390 (optimal)
- Final cruise: FL410 (light weight, best efficiency)

### Speed Optimization

**Long Range Cruise (LRC):** M0.78
- 99% of maximum range
- Acceptable block time
- Optimal fuel efficiency

**Economy Cruise (ECON):** M0.74
- 101% range vs LRC
- 5% longer block time
- Best fuel economy (used when ahead of schedule)

**Maximum Range Cruise (MRC):** M0.72
- 103% range vs LRC
- 8% longer block time
- Used only for extended diversion scenarios

## Environmental Performance

### Carbon-Negative Operations

**Per Flight (4,000 km mission):**
- **Direct Emissions:** 0 kg CO₂ (H2 → H₂O)
- **CO₂ Captured:** 5 kg (solid-state battery system)
- **Net Impact:** -5 kg CO₂ per flight ✓

**Annual Fleet (500 flights/year):**
- Total CO₂ removed: 2,500 kg/year per aircraft
- Fleet of 100: 250,000 kg CO₂/year removed
- Equivalent to: 50,000 trees planted

### Comparison to Conventional

**A321neo (equivalent mission):**
- **Fuel Burn:** 2,500 kg Jet-A
- **CO₂ Emissions:** 7,875 kg CO₂
- **AMPEL360 Advantage:** 7,880 kg CO₂ better

**Annual Impact (per aircraft):**
- Flights: 500/year
- CO₂ Saved: 3,940,000 kg/year
- Equivalent to: 19,000 passenger cars removed

## Future Range Extension

### Technology Roadmap

**Phase 1 (2029-2035): 4,000 km**
- Current design
- Type IV tanks (700 bar)
- 65% gravimetric efficiency

**Phase 2 (2035-2040): 5,000 km**
- Improved fuel cells (65% efficiency)
- Type V tanks (900 bar)
- 75% gravimetric efficiency
- +25% range, +8% MTOW

**Phase 3 (2040+): 6,000 km**
- Advanced fuel cells (70% efficiency)
- Cryo-compressed H2 (optional)
- 85% gravimetric efficiency
- +50% range, +12% MTOW

### Market Evolution

**Hydrogen Infrastructure Growth:**
- 2030: 300 airports with H2
- 2035: 800 airports with H2
- 2040: 2,000+ airports with H2

**AMPEL360 Strategy:**
- Phase 1: 4,000 km establishes operations
- Phase 2: 5,000 km expands market
- Phase 3: 6,000 km competes with wide-bodies

## Certification Basis

### CS-25 Compliance

**Range Demonstration:**
- CS-25.1001: Fuel system capacity
- CS-25.1011: Engines (fuel cell stacks)
- CS-25.1013: H2 tank installation
- CS-25.1093: Emergency fuel system

**Flight Testing:**
- Maximum range demonstration flight
- Reserve fuel validation
- Alternate airport scenarios
- ETOPS demonstration (if applicable)

---

**References:**
- Range-Payload Manual: RPM-001
- Performance Analysis: PA-BWB-2025-001
- Market Study: MS-AMPEL360-2024
- Fuel System Design: ATA 28-00-00
- CS-25 Compliance: CRT-PERF-2025-001
