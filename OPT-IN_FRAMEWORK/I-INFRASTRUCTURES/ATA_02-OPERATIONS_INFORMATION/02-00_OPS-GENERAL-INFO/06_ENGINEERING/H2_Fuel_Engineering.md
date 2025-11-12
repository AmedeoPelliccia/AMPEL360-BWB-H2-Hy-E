# H₂ Fuel Engineering
**Component Code:** 02-00-00  
**Component Name:** GENERAL  
**Document Type:** Hydrogen Fuel System Engineering

---

## Overview

This document defines the engineering principles, analysis methods, and operational considerations for the AMPEL360 BWB H₂ Hy-E Q100 aircraft's liquid hydrogen fuel system. This revolutionary propulsion approach requires specialized engineering analysis and operational procedures.

---

## H₂ System Architecture

### Primary Components

| Component | Specification | Location |
|-----------|--------------|----------|
| **Main H₂ Tanks** | 2 × 29.65 m³ | Center fuselage |
| **Total Capacity** | 59.3 m³ (4,200 kg) | Station 500-800 |
| **Tank Type** | Vacuum-insulated composite | Type IV COPV |
| **Operating Pressure** | 5-8 bar | Cryogenic liquid |
| **Operating Temp** | -253°C (20 K) | Liquid hydrogen |
| **Fuel Cell Stacks** | 4 × 625 kW PEM | Aft fuselage |
| **Total Power** | 2.5 MW | Distributed architecture |

---

## Fuel Properties

### Liquid Hydrogen Characteristics

**Physical Properties:**
```
Density (liquid):        70.8 kg/m³ at -253°C
Boiling Point:          -253°C at 1 atm
Energy Density (mass):   120 MJ/kg (33.3 kWh/kg)
Energy Density (volume): 8.5 MJ/L (2.4 kWh/L)
Specific Energy:         3× Jet-A by weight
Volume Ratio:           4× Jet-A for equivalent energy
```

**Advantages Over Conventional Fuel:**
- Zero carbon emissions (only H₂O byproduct)
- Superior energy per unit mass
- Abundant and renewable
- No particulate emissions
- No sulfur or aromatics

**Challenges:**
- Low volumetric energy density
- Cryogenic storage requirements
- Boil-off losses
- Infrastructure requirements
- Material compatibility

---

## Fuel Planning

### Range Calculation

**Basic Range Equation (H₂ Modified):**
```
Range = (L/D) × (Energy Density) × η × ln(W₀/W₁)

Where:
L/D = 20 (BWB advantage: +30% vs conventional)
Energy Density = 120 MJ/kg (H₂)
η = 0.60 (fuel cell efficiency, 8-15% CAOS boost)
W₀ = Takeoff weight
W₁ = Landing weight
```

**Design Range:** 4,000 km with reserves

### Fuel Consumption Rates

| Flight Phase | Consumption Rate | Duration | Fuel Used |
|--------------|-----------------|----------|-----------|
| **Taxi** | 15 kg/hr | 15 min | 4 kg |
| **Takeoff** | 280 kg/hr | 2 min | 9 kg |
| **Climb** | 185 kg/hr | 25 min | 77 kg |
| **Cruise** | 650 kg/hr | Variable | Mission dependent |
| **Descent** | 95 kg/hr | 20 min | 32 kg |
| **Landing** | 45 kg/hr | 10 min | 8 kg |
| **Reserves** | - | 45 min | 488 kg |

**Typical Mission (4,000 km):**
- Mission fuel: 3,200 kg
- Reserves (45 min): 488 kg
- Alternate (200 km): 325 kg
- Total required: 4,013 kg
- Tankage capacity: 4,200 kg
- Margin: 187 kg (4.4%)

Documentation: CALC-02-00-201_H2_Fuel_Planning.csv

---

## Cryogenic Storage

### Tank System Design

**Insulation System:**
- Multi-layer vacuum insulation (MLVI)
- 15-20 layers of aluminized mylar
- Vacuum pressure: <10⁻⁴ mbar
- Effective thermal conductivity: 0.0001 W/(m·K)

**Structural Design:**
- Inner vessel: Aluminum 2219-T87
- Outer vessel: Carbon fiber composite
- Support system: Low-conductivity struts
- Burst pressure: 15 bar (2× operating)
- Test pressure: 12 bar

**Boil-Off Management:**
- Boil-off rate: 0.3-0.5% per hour (ground)
- Boil-off rate: 0.1-0.2% per hour (flight)
- Boil-off recovery: Fuel cell feed or vent
- Maximum ground hold: 48 hours without venting

Analysis: CALC-02-00-203_Boiloff_Rate.csv

---

## Refueling Operations

### Refueling Procedure

**Pre-Refueling:**
1. Aircraft grounding verification
2. Tank pressure and temperature check
3. Connection of cryogenic transfer line
4. Purge of transfer system
5. Cooling of transfer line (pre-cooling)

**Refueling Sequence:**
1. Tank A fill (0-50% capacity)
2. Tank B fill (0-50% capacity)
3. Tank A top-off (50-100%)
4. Tank B top-off (50-100%)
5. System pressure stabilization

**Post-Refueling:**
1. Disconnect and purge transfer line
2. Verify tank quantity and pressure
3. System leak check
4. Documentation completion

**Refueling Time:**
- Full tank (4,200 kg): 45-60 minutes
- Partial refuel: Pro-rated
- Fast refuel capability: 30 minutes (future)

Documentation: CALC-02-00-202_Refueling_Time.csv

### Tank Sequencing

**Normal Operations:**
- Symmetric tank usage for lateral balance
- Tank A/B alternating feed to fuel cells
- CAOS-optimized sequencing for CG control
- Manual override capability

**Tank Sequencing Strategy:**
```
Phase 1 (Takeoff/Climb):   Both tanks feeding equally
Phase 2 (Cruise):          Optimized for CG control
Phase 3 (Descent):         Both tanks feeding equally
Phase 4 (Landing):         Maintain minimum levels
```

Documentation: CALC-02-00-204_Tank_Sequencing.csv

---

## Safety Considerations

### H₂ Safety Properties

**Physical Hazards:**
- Extremely cold (cryogenic burns)
- High pressure (potential rupture)
- Rapid expansion (gaseous phase)
- Asphyxiation (oxygen displacement)

**Chemical Hazards:**
- Highly flammable (wide flammability range: 4-75%)
- Low ignition energy (0.02 mJ)
- Invisible flame
- High flame speed

**Safety Features:**
- Automatic leak detection system
- Emergency vent system
- Pressure relief valves
- Fire suppression system
- Sensor redundancy (triple redundant)

### Emergency Defueling

**Defuel Scenarios:**
- Maintenance requirement
- Tank inspection
- Emergency defuel (rare)
- System malfunction

**Defuel Procedure:**
1. Transfer to ground storage
2. Tank warming (controlled)
3. Pressure reduction
4. Purge with inert gas
5. Safety verification

**Defuel Rate:** 50-70 kg/min (slower than refuel)  
**Time for Full Defuel:** 60-84 minutes

Documentation: CALC-02-00-205_Emergency_Defuel.csv

---

## Heat Transfer Analysis

### Thermal Management

**Heat Leak Sources:**
1. Conduction through support struts
2. Radiation from outer shell
3. Residual gas conduction
4. Penetrations (fill/vent/sensors)

**Heat Leak Rate:**
- Design target: 8-12 W total
- Actual performance: 10 W typical
- Boil-off equivalent: 0.3%/hr ground, 0.15%/hr flight

**Cooling Strategies:**
- Passive insulation (primary)
- Active cooling (not required in normal ops)
- Boil-off gas utilization
- Pre-cooling of feed lines

Documentation: CALC-02-00-206_Cryogenic_Heat_Transfer.csv

---

## Safety Margins

### Design Safety Factors

**Structural:**
- Ultimate load factor: 1.5 × limit load
- Burst pressure: 2.0 × MEOP (Maximum Expected Operating Pressure)
- Fatigue life: 3 × design life
- Leak-before-burst: Verified by test

**Operational:**
- Fuel reserves: 11.7% of mission fuel
- Pressure margins: 20% below MEOP
- Temperature margins: ±10°C operating band
- CG limits: Conservative envelope

**System Redundancy:**
- Dual fuel cell stacks per side
- Triple redundant sensors
- Dual refueling connections
- Emergency power systems

Documentation: CALC-02-00-207_Safety_Margins.csv

---

## Fuel Cell Integration

### Power Management

**Fuel Cell Stack Configuration:**
- 4 stacks × 625 kW = 2.5 MW total
- PEM (Proton Exchange Membrane) technology
- Operating temperature: 80°C
- H₂ consumption: 0.06 kg/kWh
- Efficiency: 60% (electrical)

**Load Distribution:**
- Each stack independently controlled
- Automatic load balancing
- Graceful degradation (N-1 capability)
- CAOS optimization for efficiency

Detailed analysis in separate document: Fuel Cell Engineering

---

## Regulatory Compliance

### Standards and Certification

**Applicable Standards:**
- ISO 19881: Gaseous hydrogen — Land vehicle fuel containers
- SAE AS8534: Minimum Performance Standard for Fuel Cell Power System
- EASA Special Condition: H₂ propulsion system (in development)
- CS-25 Amendments: Fuel system requirements adapted for H₂

**Certification Requirements:**
- Tank structural testing
- Pressure cycling (10× expected life)
- Extreme temperature testing
- Crash worthiness demonstration
- Fire safety testing

---

## Operational Considerations

### Airport Infrastructure

**Required Facilities:**
- H₂ production or delivery system
- Cryogenic storage tanks (20+ tons capacity)
- Refueling vehicles/equipment
- Safety equipment and PPE
- Trained ground personnel

**Network Development:**
- Initial: 10 hub airports
- Phase 2: 50 airports (2030)
- Full network: 200+ airports (2035)

### Flight Planning

**Additional Considerations:**
- H₂ availability at destination/alternate
- Boil-off during ground delays
- Temperature effects on range
- Emergency landing options
- Defuel capability at airports

---

## Performance Benefits

### H₂ Propulsion Advantages

**Environmental:**
- Zero CO₂ emissions
- Zero NOx, SOx, PM emissions
- Only byproduct: Pure water vapor
- Carbon-negative with CO₂ capture system

**Operational:**
- 68% better fuel efficiency (kg/km basis)
- Lower noise (fuel cell vs turbine)
- Reduced maintenance (fewer moving parts)
- CAOS optimization potential

**Economic:**
- 33% lower operating cost per ASK
- Reduced fuel cost volatility
- Government incentives
- Future-proof technology

---

## Digital Twin Integration

### CAOS Monitoring

**Real-Time Parameters:**
- Tank pressure and temperature
- Fuel quantity and CG
- Boil-off rate
- Fuel cell performance
- System health status

**Predictive Functions:**
- Remaining range calculation
- Optimal tank sequencing
- Refuel time estimation
- Maintenance predictions
- Emergency planning

---

## Related Calculations

All H₂ system calculations maintained in:
- `CALCULATIONS/H2_System_Calculations/`
- Standards: CALC-02-00-201 through CALC-02-00-207

---

## Related Documents

- Performance Engineering
- Weight & Balance Engineering
- BWB Operations Engineering
- CAOS Integration Engineering
- Safety Engineering Analysis
- Environmental Engineering

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-05 | H₂ Systems Engineering Team | Initial release |

---

**Status:** Active  
**Next Review:** 2026-02-05  
**Owner:** AMPEL360 H₂ Systems Engineering

**Classification:** Technical - Proprietary
