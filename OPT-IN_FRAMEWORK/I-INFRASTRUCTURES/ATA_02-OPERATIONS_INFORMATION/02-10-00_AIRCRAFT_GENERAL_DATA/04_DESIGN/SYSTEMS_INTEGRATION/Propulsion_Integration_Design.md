# Propulsion Integration Design

## Executive Summary

The AMPEL360 propulsion system integrates dual PEM fuel cell stacks (2× 1.75 MW) with distributed electric propulsion, leveraging the BWB configuration for optimal integration, safety, and performance.

## Propulsion Architecture

### Fuel Cell Configuration

**Primary Power Plants:**
- **Type:** Proton Exchange Membrane (PEM) fuel cells
- **Quantity:** 2 independent stacks
- **Power:** 1.75 MW each (3.5 MW total)
- **Location:** Wing roots, separated by center body
- **Redundancy:** Either stack can sustain flight

**Operating Characteristics:**
- Cruise efficiency: 55%
- Peak efficiency: 60% at 40% power
- Response time: < 1 second (instant power)
- Lifespan: 25,000 hours (15 years typical)

### Electric Motor Configuration

**Distributed Propulsion:**
- **Motors:** 8× 450 kW electric motors
- **Location:** Trailing edge, upper surface (noise shielding)
- **Propellers:** 8× 2.2m diameter, variable pitch
- **Drive:** Direct drive, no gearbox

**Advantages:**
- Boundary layer ingestion: 8-12% efficiency gain
- Noise shielding: Upper surface mounting
- Redundancy: 6 of 8 motors sufficient for cruise
- Control authority: Differential thrust capability

### Power Distribution

**Electrical Architecture:**
```
H2 Tanks → Fuel Cell Stacks → DC Bus (800V) → Inverters → Motors

Redundancy:
- Dual DC buses (independent)
- Crossfeed capability
- Battery backup (emergency)
- CAOS monitoring and control
```

## Integration Philosophy

### BWB Synergy

**Design Integration:**
- Fuel cells in wing roots: Optimal weight distribution
- Upper surface propulsion: Aerodynamic advantage
- Center body H2 tanks: Short, efficient piping
- Distributed thrust: Replaces horizontal stabilizer

**Weight and Balance:**
- Fuel cell CG: 28% MAC (aft of center)
- Motors CG: 35% MAC (furthest aft)
- Balanced with forward passenger cabin
- Dynamic balance via H2 transfer

### Safety Through Separation

**Compartmentalization:**
- H2 tanks: Upper center body
- Fuel cells: Wing roots
- Motors: Trailing edge
- Fire zones: Independent suppression

**Failure Isolation:**
- Single fuel cell failure: 80% power available
- Motor failures: 75% thrust minimum
- H2 leak: Automatic isolation
- Electrical fault: Bus switching

## Fuel Cell System Design

### Stack Construction

**PEM Technology:**
- Membrane: Nafion or equivalent
- Catalyst: Platinum (minimized, 0.05 mg/cm²)
- Operating temp: 70-80°C
- Pressure: 3 bar absolute

**Stack Specifications:**
- Cells per stack: 800
- Voltage: 640V nominal (0.8V per cell)
- Current: 2,750 A at full power
- Efficiency map: Optimized for 70% power cruise

### Thermal Management

**Cooling System:**
- Radiators: Integrated into wing structure
- Coolant: Ethylene glycol/water (50/50)
- Heat rejection: 1.4 MW per stack (at full power)
- Ram air cooling: Supplemented by forced air

**Cold Start:**
- Electric heaters: Battery powered
- Preheat time: 5 minutes to operational temp
- Ground power unit: Alternative heat source
- Operational range: -30°C to +50°C ambient

### Water Management

**Product Water:**
- Production rate: 5.8 kg H2O per kg H2
- Collection: Gravity drain + pump
- Use: Cabin humidity (partially)
- Overboard: Remaining dumped (steam at altitude)

**Humidification:**
- Required: Membrane needs moisture
- System: Evaporative from product water
- Balance: Critical for efficiency and lifespan

## Propulsion Motor Design

### Electric Motor Specifications

**Permanent Magnet Synchronous Motors (PMSM):**
- Power: 450 kW continuous, 500 kW peak (30 sec)
- Speed: 2,000 RPM nominal
- Efficiency: 97% at cruise power
- Weight: 85 kg per motor (excellent power/weight)

**Cooling:**
- Type: Liquid cooled (glycol/water)
- Heat rejection: 13 kW per motor
- Integrated into wing cooling system

### Variable Pitch Propellers

**Propeller Design:**
- Diameter: 2.2 m
- Blades: 5-blade composite
- Pitch: Variable (0° to 45°)
- Speed: Constant 2,000 RPM (electric motor control)
- Efficiency: 85% at cruise

**Operating Modes:**
- Takeoff: Fine pitch, high thrust
- Cruise: Coarse pitch, high efficiency
- Descent: Windmill, regenerative braking (optional)
- Ground: Feathered (minimal drag)

### Thrust Vectoring

**Differential Thrust:**
- Yaw control: Independent motor power
- Roll assistance: Outboard motor differential
- Redundancy: Replaces some flight control surface area

## Power Management System

### CAOS Integration

**Functions:**
- Power distribution optimization
- Fuel cell load balancing
- Motor health monitoring
- Thermal management
- Emergency power prioritization

**Algorithms:**
- Predictive power demand
- Optimal fuel cell loading (efficiency)
- Battery state-of-charge management
- Fault detection and isolation

### Emergency Power

**Battery Backup:**
- Capacity: 250 kWh lithium-ion
- Purpose: Emergency power (30 minutes flight)
- Location: Center body, isolated
- Uses: Essential systems, emergency descent

**Priority Shedding:**
- Level 1: Full power (normal)
- Level 2: Non-essential systems shed (minor fault)
- Level 3: Essential only (major fault)
- Level 4: Emergency descent power (critical fault)

## H2 Delivery System

### Feed System Design

**From Tank to Fuel Cell:**
```
H2 Tanks (700 bar) 
  → Pressure Regulators (50 bar)
  → Distribution Manifold
  → Fuel Cell Inlet Regulators (3 bar)
  → Fuel Cell Stacks
```

**Safety Features:**
- Redundant regulators
- Automatic shutoff valves
- Leak detection throughout
- Vent system to upper surface
- Crash-resistant couplings

### Mass Flow Control

**Requirements:**
- Cruise: 875 kg/h total (437.5 kg/h per stack)
- Takeoff: 1,200 kg/h total (600 kg/h per stack)
- Idle: 150 kg/h total (75 kg/h per stack)

**Control:**
- CAOS demand calculation
- Flow meters: Coriolis type (high accuracy)
- Valve response: < 100 ms
- Balance: Equal to both stacks (normally)

## Integration Testing

### Ground Testing

**Component Tests:**
- Fuel cell endurance: 5,000 hour qualification
- Motor testing: Full power, thermal cycling
- Propeller testing: Blade loads, fatigue
- Electrical system: Fault injection, redundancy

**System Integration:**
- Iron bird test rig: Full electrical system
- Thermal management: Hot/cold chamber tests
- Emergency scenarios: Power loss, system failures

### Flight Testing

**Validation:**
- Fuel cell performance: All power settings
- Motor performance: Takeoff to cruise
- Thermal management: Worst case conditions
- Emergency procedures: Single stack operation

**Certification:**
- CS-25.1309: Systems safety analysis
- Novel propulsion: EASA/FAA special conditions
- Endurance demonstration: 300 flight cycles

## Maintenance Design

### Fuel Cell Maintenance

**Scheduled Maintenance:**
- Visual inspection: Every 100 FH
- Performance check: Every 500 FH
- Stack replacement: 25,000 FH (15 years)
- CAOS monitoring: Continuous degradation tracking

**Health Monitoring:**
- Voltage per cell: Identifies weak cells
- Efficiency trending: Predictive maintenance
- Membrane resistance: Early fault detection

### Motor/Propeller Maintenance

**Scheduled:**
- Propeller inspection: Every 1,000 FH
- Motor winding inspection: Every 5,000 FH
- Bearing replacement: Every 10,000 FH
- Prop blade replacement: 15,000 FH or damage

**Condition Monitoring:**
- Vibration analysis: Bearing health
- Temperature monitoring: Winding condition
- Current analysis: Rotor/stator condition

---

**References:**
- Fuel Cell System: ATA 71-00-00
- Electric Propulsion: ATA 61-00-00
- Power Management: ATA 24-00-00
- H2 Fuel System: ATA 28-00-00
- Safety Analysis: SHA-PROP-2025-001
