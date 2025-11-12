# ICD-02-10-71-001: Fuel Cell Power Data Interface

**From:** ATA 02-10 Aircraft General Data  
**To:** ATA 71 Power Plant (Fuel Cells)

**ICD ID:** ICD-02-10-71-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## Purpose

This Interface Control Document defines the power generation requirements and specifications for the hydrogen fuel cell propulsion system that powers the AMPEL360 BWB aircraft.

## Data Exchange

### Fuel Cell Specifications

**Provided by ATA 02-10:**

**Power Generation Requirements:**
- Total installed power: 10 MW (5 × 2 MW fuel cell stacks)
- Continuous cruise power: 8 MW
- Maximum climb power: 9.5 MW
- Emergency power: 6 MW (60% of total)
- Auxiliary power: 500 kW (for systems)

**Fuel Cell Configuration:**
- Technology: Proton Exchange Membrane (PEM)
- Number of stacks: 5 independent stacks
- Power per stack: 2 MW nominal
- Operating voltage: 600-800 VDC
- Efficiency: 55-60% @ cruise power

**Data Format:** Power specifications and performance curves  
**Update Frequency:** Static (certified values)  
**Criticality:** High

## Propulsion System Architecture

**Power Distribution:**
1. **Stack 1 & 2:** Left propulsor (4 MW combined)
2. **Stack 3 & 4:** Right propulsor (4 MW combined)
3. **Stack 5:** Center propulsor + auxiliary systems (2 MW)

**Redundancy Philosophy:**
- Any 3 stacks provide safe flight power
- Single stack failure: Continue to destination
- Dual stack failure: Divert to alternate
- Triple stack failure: Emergency landing capability

## Performance Specifications

**Operational Envelope:**
- Maximum altitude: 43,000 ft
- Minimum altitude: Sea level
- Operating temperature: -55°C to +40°C
- Maximum humidity: 95% (non-condensing at stack)

**Power Response:**
- Power increase rate: 500 kW/second
- Power decrease rate: 800 kW/second
- Cold start time: 120 seconds to 50% power
- Warm start time: 30 seconds to full power

**Fuel Consumption:**
- Cruise (8 MW): 400 kg H₂/hour
- Climb (9.5 MW): 480 kg H₂/hour
- Idle (1 MW): 55 kg H₂/hour
- APU mode (500 kW): 28 kg H₂/hour

## Integration Requirements

**Physical Installation:**
- Stack 1 & 2 Location: Station 20-25 m, -3.5 m BL
- Stack 3 & 4 Location: Station 20-25 m, +3.5 m BL
- Stack 5 Location: Station 22.5 m, centerline
- Total fuel cell system weight: 4,500 kg

**Cooling Requirements:**
- Heat rejection @ cruise: 4.5 MW
- Coolant: Ethylene glycol/water 50/50
- Coolant flow rate: 1,200 L/min total
- Radiator location: Wing surface heat exchangers

**Electrical Interface:**
- DC bus voltage: 700 VDC nominal (600-800 VDC range)
- AC conversion: 3-phase 115/200 VAC, 400 Hz
- Power quality: MIL-STD-704F compliant
- Ground power connection: 28 VDC or 115 VAC

## BWB Configuration Advantages

**Integration Benefits:**
- Center body volume accommodates stacks efficiently
- Short power cables to propulsors reduce losses
- Distributed installation improves safety
- Optimal thermal management via wing surface

**Noise and Vibration:**
- Fuel cells inherently quiet (no combustion)
- Vibration isolation: <0.1 g transmitted
- Electromagnetic compatibility: DO-160G compliant

## Operational Modes

**Normal Operation:**
- All 5 stacks online, load-shared
- Power optimization by CAOS system
- Automatic stack rotation for even wear

**Degraded Operation:**
- Single stack out: 80% power available
- Dual stack out: 60% power available (operational ceiling reduced)
- Load shedding prioritizes flight-critical systems

**Emergency Mode:**
- Minimum 3 stacks for safe flight
- Non-essential systems shed automatically
- Fuel conservation mode activated

## Dependencies

- H₂ fuel supply system (ATA 28)
- Electrical power distribution (ATA 24)
- Thermal management (ATA 21)
- Propulsion controls (ATA 76)
- CAOS power management (ATA 95)

## Responsibilities

**ATA 02-10 (Provider):**
- Define power requirements
- Specify performance envelope
- Coordinate integration requirements

**ATA 71 (Consumer):**
- Design and install fuel cell system
- Meet performance specifications
- Integrate with propulsion system
- Provide health monitoring

## Change Control

Power system changes require:
1. Performance analysis validation
2. Electrical system compatibility check
3. Thermal management revalidation
4. Flight test demonstration
5. Update to Aircraft Flight Manual

## CAOS Integration

**Real-time Monitoring:**
- Stack voltage and current per cell
- Temperature monitoring (100+ sensors)
- Hydrogen flow rates
- Efficiency optimization
- Predictive maintenance alerts
- Remaining useful life estimation

**Performance Optimization:**
- Load distribution across stacks
- Thermal management coordination
- Fuel consumption minimization
- Power quality maintenance

## Safety Systems

**Protection Features:**
- Hydrogen leak detection
- Automatic stack shutdown on fault
- Fire suppression system integration
- Emergency ventilation
- Electrical isolation on ground

**Fault Management:**
- Graceful degradation strategy
- Automatic power redistribution
- Flight crew alerting and guidance
- Maintenance diagnostic data

## References

- SAE J2578: Recommended Practice for PEM Fuel Cell Systems
- ISO 16110: Hydrogen Generators Using Fuel Processing Technologies
- DO-160G: Environmental Conditions and Test Procedures for Airborne Equipment
- MIL-STD-704F: Aircraft Electric Power Characteristics

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Review Cycle: Annual or per major change
