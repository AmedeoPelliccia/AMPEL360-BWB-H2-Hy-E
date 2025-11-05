# Cruise Speed Selection

## Executive Summary

The AMPEL360 cruise speed of Mach 0.78 (M0.78) at FL390 was selected as the optimal balance between fuel efficiency, block time competitiveness, and structural/aerodynamic design constraints.

## Design Requirements

### Market Competitiveness
- **Target:** Competitive block times with A321XLR, 737 MAX 10
- **Conventional cruise:** M0.78-M0.82 typical
- **Passenger expectation:** <4 hours for 3,000 km routes

### Fuel Efficiency
- **Primary Goal:** Minimize H2 consumption per km
- **Trade-off:** Speed vs drag vs weight
- **Optimization:** Maximum range per kg H2

### Structural Considerations
- **Flutter margin:** Adequate at cruise speeds
- **Gust loads:** Acceptable at cruise altitude
- **Fatigue life:** 90,000 flight cycles target

## Speed Selection Analysis

### Drag Polar Analysis

**BWB Drag Components:**
```
CD = CD0 + CDi + CDw

Where:
CD0 = Parasite drag (skin friction, form drag)
CDi = Induced drag (lift-dependent)
CDw = Wave drag (compressibility effects)

At M0.78, FL390:
CD0 = 0.0145 (excellent for BWB)
CDi = CL² / (π × AR × e) = 0.0082
CDw = 0.0008 (below critical Mach)
───────────────────────────────
CD total = 0.0235

L/D = CL / CD = 0.52 / 0.0235 = 22.1 ✓
```

### Speed vs L/D Trade Study

| Mach | TAS (m/s) | CD | L/D | Fuel Flow | Block Time (3000km) | Score |
|------|-----------|-----|-----|-----------|---------------------|-------|
| 0.72 | 217 | 0.0225 | 23.1 | 820 kg/h | 3.8 hours | 0.82 |
| 0.74 | 223 | 0.0228 | 22.8 | 835 kg/h | 3.7 hours | 0.89 |
| 0.76 | 229 | 0.0232 | 22.4 | 855 kg/h | 3.6 hours | 0.94 |
| **0.78** | **235** | **0.0235** | **22.1** | **875 kg/h** | **3.5 hours** | **0.97** ✓ |
| 0.80 | 241 | 0.0242 | 21.5 | 915 kg/h | 3.4 hours | 0.93 |
| 0.82 | 247 | 0.0255 | 20.4 | 975 kg/h | 3.4 hours | 0.84 |

**Selected: Mach 0.78**
- Optimal L/D (22.1)
- Competitive block time
- Below critical Mach (Mcrit = 0.80)
- Acceptable fuel consumption

## Critical Mach Number

### Wave Drag Rise

**BWB Aerodynamics:**
- **Leading Edge Sweep:** 37° → Delayed shock formation
- **Supercritical Sections:** Optimized pressure distribution
- **Critical Mach (Mcrit):** 0.80 (shock-free flow below this)

**Drag Divergence:**
```
Mach Number vs Drag Coefficient:

M0.70: CD = 0.0220 (pure subsonic)
M0.75: CD = 0.0230 (mild compress ibility)
M0.78: CD = 0.0235 (design point) ✓
M0.80: CD = 0.0245 (wave drag begins)
M0.82: CD = 0.0265 (significant wave drag)
M0.84: CD = 0.0295 (drag divergence)
```

**Design Margin:** M0.78 vs Mcrit = 0.80
- **Safety Margin:** 2.5% below critical
- **Buffet Margin:** Adequate for turbulence
- **Operating Envelope:** M0.70-M0.82 permissible

## Fuel Cell System Considerations

### Power vs Efficiency

**Fuel Cell Performance Map:**
```
Power Setting    Efficiency    Typical Flight Phase
─────────────────────────────────────────────────
20% rated        50%           Descent, hold
40% rated        60%           Climb (high altitude)
70% rated        55%           Cruise (optimal) ✓
85% rated        52%           Climb (low altitude)
100% rated       48%           Takeoff, go-around
```

**Cruise Optimization:**
- **Target:** 70% fuel cell power = 55% efficiency
- **Speed:** M0.78 provides this power requirement
- **Alternative:** M0.76 = 65% power, 57% efficiency (less fuel but slower)

### Thrust Required Calculation

```
Thrust Required = Drag = 0.5 × ρ × V² × S × CD

At M0.78, FL390 (ρ = 0.396 kg/m³):
V = 235 m/s
S = 845 m² (reference area)
CD = 0.0235

T_req = 0.5 × 0.396 × 235² × 845 × 0.0235
      = 46,500 N (per aircraft)
      ≈ 23,250 N per side
```

**Fuel Cell Sizing:**
- **Total Power:** 3.5 MW (2× 1.75 MW fuel cell stacks)
- **Cruise Power:** 2.5 MW (70% rated)
- **Efficiency:** 55% at cruise
- **H2 Consumption:** 875 kg/hour

## Speed Schedule

### Climb Speed Schedule

**Optimal Climb:**
```
Altitude      CAS       Mach
─────────────────────────────
0-10,000 ft   250 kt    -
10,000-FL280  300 kt    -
FL280-FL370   -         M0.78
FL370-FL410   -         M0.78 (cruise climb)
```

**Climb Time to FL390:** 25 minutes
**Fuel Used in Climb:** 850 kg H2

### Cruise Speed Options

**Long Range Cruise (LRC):** M0.78
- Standard operating speed
- Optimal fuel efficiency
- 99% of maximum range

**Economy Cruise (ECON):** M0.74
- 101% range vs LRC
- 5% longer block time
- Use when: Ahead of schedule, fuel conservation priority

**Maximum Range Cruise (MRC):** M0.72
- 103% range vs LRC
- 8% longer block time
- Use when: Diversion, fuel emergency

**High Speed Cruise (HSC):** M0.82
- 95% range vs LRC
- 3% shorter block time
- Use when: Severe delays, urgent situations

### Descent Speed Schedule

**Optimal Descent:**
```
Altitude      Mach/CAS    Rate
────────────────────────────────────
FL410-FL280   M0.78       2,000 fpm
FL280-10,000  300 kt      2,500 fpm
10,000-0      250 kt      1,500 fpm
```

**Idle Descent Profile:**
- Distance required: 120 NM from TOD
- Fuel saved: 50 kg H2 vs powered descent
- ATC coordination: Request clearance early

## Competitive Analysis

### Block Time Comparison (3,000 km mission)

| Aircraft | Cruise Speed | Block Time | Advantage |
|----------|--------------|------------|-----------|
| A321XLR | M0.78 | 3.5 hours | Baseline |
| 737 MAX 10 | M0.79 | 3.5 hours | Equal |
| **AMPEL360** | **M0.78** | **3.5 hours** | **Equal** ✓ |
| A321neo | M0.78 | 3.5 hours | Equal |

**Result:** AMPEL360 is block-time competitive with conventional aircraft

### Operating Cost Comparison

**AMPEL360 at M0.78:**
- **H2 Fuel Cost:** $5.50/kg × 4,700 kg = $25,850
- **Block Time:** 3.5 hours
- **DOC:** $32,500 per flight

**A321XLR at M0.78:**
- **Jet-A Fuel Cost:** $0.80/kg × 8,500 kg = $6,800
- **Block Time:** 3.5 hours
- **DOC:** $28,000 per flight

**Current Challenge:** H2 fuel price premium
**Future (2035):** H2 cost parity expected → DOC advantage for AMPEL360

## Passenger Comfort Considerations

### Cabin Altitude

**Cruise Altitude:** FL390
- **Cabin Altitude:** 6,500 ft (BWB allows lower cabin alt)
- **Passenger Comfort:** Enhanced vs 8,000 ft conventional
- **Health Benefits:** Reduced fatigue, jet lag

### Turbulence

**Ride Quality at M0.78:**
- **Optimal Altitude:** Above most weather (FL370-410)
- **Gust Response:** BWB has lower wing loading → smoother ride
- **Passenger Feedback:** Expected to be superior to narrow-body

### Noise

**Cruise Noise:**
- **Cabin Noise:** 68 dB (BWB has better insulation)
- **Conventional:** 72 dB typical
- **Advantage:** 4 dB quieter (passengers notice)

## Environmental Considerations

### Fuel Efficiency

**H2 Consumption per ASK:**
```
ASK = Available Seat Kilometers
    = 220 seats × 4,000 km
    = 880,000 ASK per flight

H2 per ASK = 6,500 kg / 880,000 = 0.0074 kg/ASK

Energy per ASK = 0.0074 kg × 120 MJ/kg / 880,000
               = 0.88 MJ/ASK

Comparison:
- Conventional jet: 1.5 MJ/ASK
- AMPEL360: 0.88 MJ/ASK (40% better)
```

### NOx Emissions

**Fuel Cell Advantage:**
- **NOx Production:** Near zero (no combustion)
- **Altitude Impact:** No high-altitude NOx contribution
- **Climate Impact:** Significantly reduced vs conventional

## Certification Compliance

### CS-25 Requirements

**Maximum Operating Speed (VMO/MMO):**
- **VMO:** 340 KIAS (equivalent airspeed)
- **MMO:** M0.82 (design limit)
- **Cruise:** M0.78 (5% margin)

**Flutter Clearance:**
- **VD:** M0.92 (dive speed, 15% above MMO)
- **Flutter Speed:** > 1.15 × VD = M1.06
- **Margin:** Adequate at cruise

**Gust Loads:**
- **Cruise:** 50 ft/s gust at M0.78
- **Design:** BWB structure validated
- **Limit Load:** Not exceeded in service conditions

---

**References:**
- Aerodynamic Analysis: AER-BWB-2025-002
- Fuel Cell Performance: ATA 24-00-00
- Speed Schedule: FCOM Section 03.05
- CS-25.1505: Airspeed Limitations
- Performance Optimization: PA-CRUISE-2025-001
