# H2 Storage Design Rationale

## Executive Summary

The AMPEL360 H2 storage system design leverages the BWB's thick center body to provide 6,500 kg of hydrogen fuel capacity in safe, efficient, and certifiable pressure vessels that enable 4,000 km range with zero direct emissions.

## H2 Storage Requirements

### Capacity Targets
- **Mission Fuel:** 5,500 kg H2
- **Reserve Fuel:** 750 kg H2 (15% reserve + diversion)
- **Taxi Fuel:** 250 kg H2
- **Total Capacity:** 6,500 kg H2

### Range Calculation
```
Range = 4,000 km
Cruise L/D = 21
TSFC_H2 = 0.25 kg/kW/h (fuel cell efficiency)
Average cruise thrust = 35 kN

Fuel Required = Distance × Thrust / (L/D × Efficiency × Heating Value)
              = 4,000 km × 35 kN / (21 × 0.45 × 120 MJ/kg)
              ≈ 5,500 kg H2
```

## Tank Technology Selection

### Type IV Composite Pressure Vessels

**Technology Choice Rationale:**
- **Gravimetric Efficiency:** 65% (H2 mass / total system mass)
- **Volumetric Efficiency:** 40% (H2 volume / tank volume)
- **Safety:** Proven in automotive applications (10+ years)
- **Cost:** Lower than Type III (carbon fiber liner)
- **Lifespan:** 25 years / 20,000 cycles

**Construction:**
- **Liner:** High-density polyethylene (HDPE)
- **Overwrap:** Carbon fiber composite
- **Pressure Rating:** 700 bar (10,000 psi)
- **Temperature Range:** -253°C to +85°C
- **Permeation Rate:** < 0.5% per year

### Alternative Technologies Considered

| Type | Gravimetric | Volumetric | Cost | Selected |
|------|-------------|------------|------|----------|
| Type I (Steel) | 5% | 25% | Low | No (too heavy) |
| Type II (Metal + composite) | 15% | 30% | Medium | No (heavy) |
| Type III (Metal liner + CF) | 45% | 35% | High | No (cost) |
| **Type IV (Polymer + CF)** | **65%** | **40%** | **Medium** | **Yes** ✓ |
| Liquid H2 (cryogenic) | 80% | 60% | Very High | No (boil-off) |

**Why Not Liquid H2:**
- Boil-off losses: 2-3% per day
- Complex cryogenic systems
- Greater insulation weight
- Longer ground turnaround time
- Higher operational complexity

## Tank Configuration

### Center Body Tanks (Primary)
**Quantity:** 2 tanks  
**Capacity:** 2,000 kg H2 each (4,000 kg total)  
**Dimensions:** 4.5m length × 1.8m diameter  
**Volume:** 11.5 m³ per tank  
**Pressure:** 700 bar  
**Weight (empty):** 615 kg each

**Location:**
- Station: 15.0-19.5m (longitudinal)
- Height: Upper deck, above passenger cabin
- Lateral: ±2.0m from centerline

**Mounting:**
- Cradle system with frangible links
- 9g forward, 3g aft, 4g lateral crash loads
- Thermal isolation from structure
- Anti-vibration mounts

### Wing Tanks (Trim)
**Quantity:** 2 tanks  
**Capacity:** 1,250 kg H2 each (2,500 kg total)  
**Dimensions:** 6.0m length × 1.2m diameter  
**Volume:** 6.8 m³ per tank  
**Pressure:** 700 bar  
**Weight (empty):** 385 kg each

**Location:**
- Station: Y = 10-16m (lateral)
- Height: Mid-wing height
- Integration: Wing box structure

**Mounting:**
- Wing box hard points
- 6g forward, 2g aft, 3g lateral crash loads
- Conformal to wing contour
- Load-bearing structure integration

## Tank System Design

### Pressure Management

**Operating Pressure:**
- **Full:** 700 bar (10,150 psi)
- **Normal Operations:** 200-700 bar
- **Minimum Usable:** 50 bar (fuel cell inlet pressure)
- **Relief Valve Setting:** 760 bar (108% design)

**Pressure Reduction:**
- Two-stage regulation: 700 bar → 50 bar → 10 bar
- Redundant pressure regulators
- Fail-safe to vent (upward direction)
- Pressure monitoring: 4 sensors per tank

### Thermal Management

**Insulation System:**
- Multi-layer insulation (MLI): 10 layers
- Vacuum gap: 5cm around tank
- Thermal conductivity: 0.01 W/m·K
- Heat leak: < 5W per tank

**Temperature Control:**
- Passive insulation primary
- Active heating (electric) for cold starts
- Temperature monitoring: 6 sensors per tank
- Operating range: -40°C to +55°C ambient

**Boil-off Management:**
- Compressed gas, no boil-off in normal ops
- Pressure relief to vent system if over-temp
- Ground cooling available via external chiller

### Safety Features

**Burst Pressure:**
- Design: 1,050 bar (150% operating)
- Test: 875 bar (125% operating)
- Safety Factor: 2.25 (per ISO-19881)

**Fire Protection:**
- Thermally-activated pressure relief devices (TPRD)
- Vent upward through upper fuselage
- Fire detection: Smoke + heat
- Halon alternative suppression system

**Crash Resistance:**
- Frangible couplings auto-disconnect
- Pressure relief activated
- Tank integrity maintained to 10g
- Post-crash inspection requirements

**Leak Detection:**
- Hydrogen sensors: 4 ppm threshold
- 8 sensors per tank (redundant pairs)
- Automatic valve closure on leak
- Crew alerting via EICAS

## Fuel Management System

### Fill System
- **Fill Port:** Underwing, both sides
- **Fill Rate:** 150 kg/min (45 minute full fill)
- **Coupling:** Break-away safety coupling
- **Grounding:** Automatic static discharge
- **Interlocks:** Door closed, APU off, passengers clear

### Transfer System
- **Transfer Pumps:** Hydrogen gas compressors
- **Transfer Rate:** 50 kg/min between tanks
- **Control:** CAOS automated or crew manual
- **Purpose:** CG optimization during flight

### Feed System
- **Priority:** Center tanks first (CG stability)
- **Crossfeed:** Capability to feed any fuel cell from any tank
- **Emergency:** Any tank can feed any fuel cell
- **Monitoring:** Mass flow meters, temperature, pressure

### Venting System
- **Normal Vent:** Relief valves to upper fuselage vent
- **Vent Capacity:** 200 kg/min (emergency)
- **Vent Location:** Upper surface, aft of tanks
- **Dispersion:** High altitude release, rapid dilution
- **Monitoring:** Flow sensors, concentration monitoring

## Weight and Volume Summary

### System Weight Breakdown
| Component | Weight (kg) |
|-----------|-------------|
| Center Tanks (2×) | 1,230 |
| Wing Tanks (2×) | 770 |
| Piping and Valves | 450 |
| Insulation | 280 |
| Sensors and Controls | 120 |
| Venting System | 180 |
| Safety Equipment | 90 |
| **Empty System Weight** | **3,120 kg** |
| H2 Fuel (full) | 6,500 kg |
| **Gross System Weight** | **9,620 kg** |

### Gravimetric Efficiency
- **System:** 6,500 / 9,620 = 67.6%
- **Comparison:** 
  - Jet-A tank system: 98% (much heavier fuel though)
  - LH2 system: ~75% (but operational penalties)

### Volume Utilization
- **Total H2 Volume:** 9.1 m³ (at 700 bar)
- **Total Tank Volume:** 48.4 m³
- **Volumetric Efficiency:** 18.8% (gaseous H2)
- **BWB Advantage:** Thick center body accommodates tanks

## Certification and Standards

### Applicable Standards
- **ISO 19881:** Gaseous hydrogen pressure vessels
- **ISO 19882:** Hydrogen refueling interface
- **SAE J2579:** Fuel cell vehicle safety
- **CS-25 Special Conditions:** Novel fuel system
- **EASA/FAA:** Coordination on H2 aircraft standards

### Testing Requirements
- Pressure cycling: 20,000 cycles to 125% pressure
- Burst testing: Samples to 225% pressure
- Fire testing: Engulfed in flames, TPRD activation
- Crash testing: 10g deceleration, no leak
- Environmental: -55°C to +85°C operation
- Permeation: Long-term leak rate validation

### Maintenance Program
- Visual inspections: Every 100 flight hours
- Pressure test: Every 2,500 flight hours
- Ultrasonic inspection: Every 10,000 flight hours
- Tank replacement: 25 years or 20,000 cycles
- CAOS predictive monitoring: Continuous

## Operational Advantages

### Compared to Conventional Fuel
- **Zero Emissions:** Only H2O produced
- **Energy Density:** 120 MJ/kg vs 43 MJ/kg Jet-A (2.8× by mass)
- **Refuel Time:** 45 min vs 30 min (acceptable trade)
- **Range:** 4,000 km with current capacity

### Compared to Battery Electric
- **Energy Density:** 100× better than Li-ion batteries
- **Weight Savings:** 90,000 kg saved vs battery electric
- **Range:** 4,000 km vs 800 km battery electric
- **Refuel Time:** 45 min vs 4-8 hours battery charge

---

**References:**
- H2 System Specification: ATA 28-00-00
- Tank Design: ISO-19881 Compliance Report
- Safety Analysis: SHA-H2-2025-001
- Weight Breakdown: WBS-H2-001
- Certification Plan: CP-H2-2025-001
