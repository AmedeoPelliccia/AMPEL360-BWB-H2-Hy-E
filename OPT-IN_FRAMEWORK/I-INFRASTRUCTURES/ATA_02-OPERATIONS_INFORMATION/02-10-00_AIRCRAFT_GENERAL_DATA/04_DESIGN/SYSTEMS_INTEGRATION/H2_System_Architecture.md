# H2 System Architecture

## Executive Summary

The AMPEL360 H2 system architecture provides safe, efficient storage, distribution, and utilization of hydrogen fuel across all phases of operation from ground refueling to in-flight consumption.

## System Overview

### Major Components

**Storage Subsystem:**
- 4 composite pressure vessels (Type IV, 700 bar)
- Multi-layer insulation and vacuum gaps
- Temperature and pressure monitoring
- Emergency relief and vent system

**Distribution Subsystem:**
- Dual-stage pressure reduction (700→50→3 bar)
- Redundant distribution manifolds
- Mass flow measurement and control
- Leak detection throughout

**Safety Subsystem:**
- H2 sensors (4 ppm threshold)
- Automatic isolation valves
- Fire suppression (Halon alternative)
- Vent system to upper surface

**Control Subsystem:**
- CAOS-integrated fuel management
- Automated tank sequencing
- CG optimization via fuel transfer
- Crew interface and monitoring

## Ground Operations

### Refueling Interface

**Underwing Refueling Points:**
- Location: Both wings, station Y=5m
- Coupling: Break-away safety type
- Flow rate: 150 kg/min (45 min full fill)
- Pressure: Truck at 750 bar, aircraft to 700 bar

**Safety Procedures:**
- Aircraft grounded: Static discharge
- 15m safety zone: Enforced
- Fire services: Standing by
- Passengers: Clear of aircraft
- APU: Shutdown required

### Pre-Flight Checks

**Automated Systems:**
- Tank pressure verification
- Leak check (automatic sniff test)
- Sensor functional check
- Valve position verification

**Crew Actions:**
- Fuel quantity verification
- CG position check
- System status review (EICAS)
- Load sheet confirmation

## In-Flight Operations

### Normal Operations

**Fuel Consumption Sequence:**
1. Wing tanks depleted first (CG forward shift)
2. Center tanks provide cruise fuel
3. Automated transfer maintains CG 26-28% MAC
4. Reserve fuel in center tanks (landing)

**Monitoring:**
- CAOS: Real-time consumption tracking
- Crew display: Fuel quantity, CG position
- Predictive: Fuel at destination
- Alerting: Approaching reserve fuel

### Fuel Transfer System

**Transfer Logic:**
- Trigger: CG deviation > 3% from optimal
- Rate: 50 kg/min between tanks
- Control: CAOS automated, crew override available
- Purpose: Optimize L/D, maintain stability

**Emergency Transfer:**
- Rapid rebalancing if CG approaching limits
- Priority override of normal operations
- Crew alerts and guidance

### Emergency Procedures

**H2 Leak Detection:**
- Alert: EICAS warning + crew procedures
- Action: Isolate affected tank
- Ventilation: Maximum flow
- Diversion: Land at nearest suitable airport

**Fuel Cell Failure:**
- Remaining power: Adequate for flight
- Fuel consumption: Optimized for single stack
- Performance: Reduced but safe
- Diversion: May be required depending on distance

## Safety Features

### Leak Detection

**Sensor Network:**
- 8 sensors per tank (redundant pairs)
- 4 ppm threshold (well below combustible limit)
- Continuous monitoring
- Self-test capability

**Response:**
- Automatic valve closure (isolate leak source)
- Ventilation activation
- Crew alerting (EICAS)
- CAOS guidance for crew actions

### Fire Protection

**Detection:**
- Smoke detectors: Optical type
- Heat detectors: Rate-of-rise and fixed temp
- H2 sensors: Hydrogen-specific
- Redundant coverage

**Suppression:**
- Halon 1301 alternative (HFC-125)
- Automatic discharge on confirmed fire
- Manual discharge capability
- Coverage: All H2 compartments

### Ventilation

**Normal Ventilation:**
- Continuous air flow through H2 compartments
- Exhaust to upper surface (away from intakes)
- Dilutes any minor leaks
- Pressure monitoring

**Emergency Ventilation:**
- High-flow mode on leak detection
- Powered by ram air + blowers
- Ensures H2 below combustible concentration
- Manual override available

### Vent System

**Pressure Relief:**
- Thermally-activated pressure relief devices (TPRD)
- Relief valves at 760 bar (108% design)
- Vent routing to upper surface
- Disperses safely at altitude

**Emergency Dump:**
- Capability to empty tanks if required
- Controlled vent rate: 200 kg/min
- Safety: High altitude preferred
- Procedure: Crew-initiated only

## Integration with Other Systems

### Electrical System

**Power for H2 System:**
- Pumps: Transfer system
- Valves: Actuation
- Sensors: Monitoring
- Heaters: Cold start, line heating

**Backup Power:**
- Essential H2 systems: Battery backed up
- Emergency: Minimum safe operation
- Duration: 30 minutes

### CAOS System

**Functions:**
- Real-time fuel management
- Predictive consumption
- CG optimization
- Health monitoring
- Crew decision support

**Data:**
- Tank pressures and temperatures
- Flow rates
- Fuel quantity (mass)
- CG position
- System status

### Flight Control System

**Integration:**
- CG position input to flight computers
- Affects control laws (trim, stability augmentation)
- Fuel transfer coordinated with maneuvers
- Weight changes accounted in performance calculations

### Environmental Control System

**H2 Compartment Conditioning:**
- Temperature control (heating if cold)
- Ventilation air supply
- Humidity control (prevent condensation)
- Integration with cabin ECS

## Certification Basis

### Novel Fuel System

**Special Conditions:**
- EASA/FAA: Equivalent level of safety to Jet-A
- Additional requirements for H2 specific hazards
- Demonstration of safety systems
- Testing beyond conventional fuel

### Compliance Strategy

**Analysis:**
- System safety assessment (SSA)
- Failure modes and effects analysis (FMEA)
- Fault tree analysis (FTA)
- Hazard analysis (SHA)

**Testing:**
- Leak testing: All components
- Fire testing: Suppression effectiveness
- Crash testing: No leak after impact
- Environmental: -55°C to +85°C

### Operational Approval

**H2 Operations Manual:**
- Refueling procedures
- Normal operations
- Emergency procedures
- Maintenance procedures
- Training requirements

**Airport Requirements:**
- H2 refueling infrastructure
- Fire/rescue capabilities
- Personnel training
- Emergency response plan

---

**References:**
- H2 Fuel System: ATA 28-00-00
- Safety Analysis: SHA-H2-2025-001
- CAOS Integration: ATA 45-00-00
- Fire Protection: ATA 26-00-00
- Certification Plan: CP-H2-2025-001
