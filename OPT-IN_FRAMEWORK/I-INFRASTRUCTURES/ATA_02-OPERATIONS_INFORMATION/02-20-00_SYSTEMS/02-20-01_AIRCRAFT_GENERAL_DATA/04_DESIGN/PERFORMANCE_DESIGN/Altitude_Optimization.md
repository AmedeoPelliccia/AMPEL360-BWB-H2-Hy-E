# Altitude Optimization

## Executive Summary

The AMPEL360 optimal cruise altitude band of FL370-FL410 (37,000-41,000 ft) was selected based on aerodynamic efficiency, fuel cell performance, and operational flexibility.

## Altitude Selection Rationale

### Aerodynamic Performance

**L/D vs Altitude:**
| Altitude | Density | L/D | Score |
|----------|---------|-----|-------|
| FL310 | 0.530 kg/m³ | 19.5 | 0.72 |
| FL350 | 0.455 kg/m³ | 21.2 | 0.88 |
| FL370 | 0.413 kg/m³ | 21.8 | 0.95 |
| **FL390** | **0.396 kg/m³** | **22.1** | **1.00** ✓ |
| FL410 | 0.365 kg/m³ | 22.0 | 0.98 |
| FL430 | 0.336 kg/m³ | 21.5 | 0.91 |

**Optimal: FL390**
- Maximum L/D = 22.1
- Thinner air reduces parasite drag
- Still adequate dynamic pressure for control

### Fuel Cell Efficiency

**Altitude Effects on Fuel Cells:**
- Lower air density → Less cooling drag
- Lower temperature → Better thermal management
- Lower pressure → Minimal impact (H2 is pressurized)

**Optimal Band:** FL370-FL410
- Fuel cell efficiency: 54-56% throughout
- Cooling requirements: Reduced by 15% vs FL310
- Thermal management: Optimal

### Temperature Considerations

**ISA Temperature Profile:**
```
FL310: -44°C (ISA)
FL350: -54°C
FL370: -57°C
FL390: -57°C (tropopause)
FL410: -57°C
FL430: -57°C
```

**H2 System Benefits:**
- Colder ambient → Better tank insulation efficiency
- Reduced heat leak to H2 tanks
- Fuel cell cooling: Easier

## Step Climb Strategy

### Weight-Optimized Profile

**Typical Mission:**
```
Takeoff Weight: 145,000 kg
├─ FL370: 0-500 NM (heavy)
├─ FL390: 500-1,500 NM (optimal)
└─ FL410: 1,500-2,000 NM (light)
```

**Fuel Burn Optimization:**
- FL370 start: Best L/D for heavy weight
- FL390 mid-cruise: Optimal for most of flight
- FL410 final: Best L/D for light weight

**Fuel Savings:** 2-3% vs constant altitude

### ATC Considerations

**Altitude Assignment:**
- Westbound: FL350, FL370, FL390, FL410 (even + 10)
- Eastbound: FL360, FL380, FL400 (odd)
- RVSM: 1,000 ft separation above FL290

**Step Climb Requests:**
- Timing: Every 45-60 minutes typical
- Coordination: CAOS calculates optimal time
- Fuel savings: Justifies potential routing

## Altitude vs Range

### Breguet Range Equation at Altitude

```
Range ∝ (V × L/D) / TSFC

At FL390:
- V = 235 m/s (TAS)
- L/D = 22.1
- TSFC equivalent = 0.28 kg/kWh
- Range = 4,100 km ✓

At FL310:
- V = 235 m/s (same Mach)
- L/D = 19.5
- TSFC equivalent = 0.30 kg/kWh
- Range = 3,650 km (11% less)
```

**Altitude Impact:** Each 2,000 ft = ~1.5% range change

## Cabin Altitude and Pressure

### Pressurization System

**BWB Advantage:**
- Structural efficiency → Lower cabin altitude possible
- Design cabin altitude: 6,500 ft at FL390
- Conventional: 8,000 ft typical

**Differential Pressure:**
```
FL390: Pa = 2.1 psi (ambient)
Cabin: Pc = 10.9 psi (6,500 ft)
ΔP = 8.8 psi differential ✓

CS-25 Limit: 9.0 psi (within limit)
```

**Passenger Benefits:**
- Reduced fatigue
- Better oxygen saturation
- Less jet lag effect
- Competitive advantage

## Weather Avoidance

### Cruise Altitude Benefits

**Weather Considerations:**
- Most turbulence: Below FL350
- Jet stream: FL300-FL380 typically
- Thunderstorms: Tops < FL450 usually

**FL390 Advantages:**
- Above most weather
- Smooth ride quality
- Less ATC deviations
- Predictable routing

### Wind Optimization

**CAOS Wind Analysis:**
- Optimizes altitude for winds aloft
- Trade-off: Headwind vs altitude penalty
- Typical adjustment: ±2,000 ft from optimal
- Fuel savings: 1-2% on average

## Environmental Considerations

### Contrail Formation

**Contrail Altitude:**
- Forms when: T < -40°C and humidity > threshold
- Typical: FL300-FL410
- AMPEL360: Water vapor only (no soot nuclei)
- Impact: Contrails likely but cleaner

**Mitigation Strategy:**
- CAOS contrail prediction
- Altitude adjustment capability: ±2,000 ft
- Environmental mode: Reduces contrail formation
- Trade-off: 0.5% fuel penalty acceptable

### NOx Impact Minimization

**Fuel Cell Advantage:**
- Zero NOx production (no combustion)
- High altitude: No NOx climate impact
- Conventional jets: NOx worse at high altitude
- AMPEL360: Environmental advantage

## Operational Ceiling

### Maximum Altitude

**Absolute Ceiling:** FL450
- Defined: Rate of climb = 100 fpm
- Weight dependent
- Light weight only

**Service Ceiling:** FL430
- Defined: Rate of climb = 500 fpm
- Practical maximum
- Rarely used (ATC, efficiency)

**Optimum Ceiling:** FL390-FL410
- Best L/D range
- Fuel cell efficiency
- ATC standard altitudes

### Buffet Considerations

**Coffin Corner at High Altitude:**
- Low speed buffet: Stall warning
- High speed buffet: Shock-induced
- Margin at FL410: 40 knots (adequate)
- BWB advantage: Wide speed margin

## Certification Compliance

### CS-25 Requirements

**CS-25.1527:** Maximum Operating Altitude
- **Limit:** FL430 (certified ceiling)
- **Typical Operations:** FL370-FL410
- **Margin:** Adequate

**CS-25.841:** Pressurization
- Cabin altitude: 8,000 ft max at certified ceiling
- AMPEL360: 6,500 ft (better than required)

**CS-25.1581:** Oxygen Equipment
- Required if: Cabin altitude > 10,000 ft possible
- Emergency descent: Cabin to 10,000 ft in 10 minutes
- System: Adequate for FL430 depressurization

---

**References:**
- Altitude Performance: PA-ALT-2025-001
- Pressurization System: ATA 21-10-00
- Flight Planning: FCOM Section 03.06
- CS-25 Compliance: CRT-ALT-2025-001
