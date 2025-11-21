# 85-00-01-002 H₂ and CO₂ Energy Infrastructure Interfaces

## Document Information

- **Document ID**: 85-00-01-002
- **Title**: H₂ and CO₂ Energy Infrastructure Interfaces
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Energy Interfaces
- **ATA Chapter**: 85 - Infrastructure Interface Standards

## Purpose

This document specifies the energy-related interfaces between the AMPEL360 BWB aircraft and ground infrastructure, focusing on hydrogen refuelling systems and CO₂ battery charge/discharge operations. These interfaces are critical for safe, efficient turnaround operations and enable the aircraft's carbon-negative operation.

## Scope

This specification covers:

- H₂ refuelling interface physical and protocol specifications
- CO₂ battery docking and thermal management interfaces
- Safety systems and interlocks for energy operations
- Data telemetry and monitoring requirements
- Cross-ATA integration with fuel, power, and energy management systems

## H₂ Refuelling Infrastructure Interface

### Physical Interface Specifications

**Refuelling Port Locations:**
- Primary port: Port side fuselage, station 12.5m (forward of wing leading edge)
- Secondary port: Starboard side fuselage, station 12.5m (mirror location)
- Emergency defuelling port: Ventral access, station 15.0m

**Connector Specifications:**
- Type: High-pressure quick-disconnect coupling (SAE AS50881 compliant)
- Operating pressure: 350-700 bar (5,000-10,000 psi)
- Flow rate capability: 4-8 kg H₂/min (typical turnaround: 15-25 minutes)
- Connection force: < 150 N for operator safety
- Leak rate requirement: < 0.01% of flow rate

**Safety Zone Requirements:**
- Minimum exclusion radius: 10m from refuelling points during active transfer
- No ignition sources within 25m during operations
- Grounding strap connection required before coupling
- Ventilation rate: minimum 0.5 m/s air movement

### H₂ Supply Infrastructure Requirements

**Ground-Side Equipment:**
- Mobile H₂ bowser (preferred for flexibility)
  - Capacity: 500-1,000 kg H₂ storage
  - On-board compression: 700 bar capability
  - Transfer rate: 4-8 kg/min sustained
- Fixed H₂ pipeline system (alternative for high-volume operations)
  - Pressure regulation: 700 bar output
  - Flow metering: ±1% accuracy
  - Emergency isolation valves: < 1 second closure time

**H₂ Quality Requirements:**
- Purity: ISO 14687 Type I Grade D (99.97% minimum)
- Water content: < 5 μmol/mol
- Total hydrocarbons: < 2 μmol/mol
- Oxygen content: < 5 μmol/mol
- Particulates: ISO 8573-1 Class 1

### Signals and Data Protocol

**Pre-Refuelling Handshake:**
1. Ground system: Presence signal (24V discrete)
2. Aircraft: Ready signal (tanks vented, pressure relieved)
3. Ground system: Pressure and temperature telemetry
4. Aircraft: Tank state-of-charge and thermal status
5. Mutual: Safety interlock enable

**During Refuelling:**
- Real-time flow rate (CAN bus, 10 Hz update)
- Tank pressure monitoring (4-20 mA analog, 1 Hz)
- Tank temperature monitoring (4-20 mA analog, 1 Hz)
- H₂ leak detection status (discrete, latching)
- Emergency stop signal (hardwired, fail-safe)

**Post-Refuelling:**
- Fill complete signal (discrete)
- Pressure stabilization confirmation
- Disconnect authorization (interlocked with pressure relief)
- Refuelling summary data (CAN message: volume, duration, quality parameters)

### Safety Interlocks

**Permissives (all must be TRUE for refuelling):**
- Aircraft electrical system: On or GPU connected
- Engines: Shut down and cooled (> 10 minutes post-shutdown)
- APU: Shut down (if equipped)
- Fire detection systems: Armed and tested
- Doors: All closed (passenger and cargo)
- Wheel chocks: In place (discrete sensor or operator confirmation)
- Grounding strap: Connected (resistance < 1 Ω)
- H₂ leak detectors: Operational and no alarms

**Emergency Stop Triggers:**
- Manual E-stop activation (ground or cockpit)
- H₂ leak detection (> 1% LEL)
- Fire detection in vicinity
- Loss of grounding connection
- Seismic event detection (> 0.1g acceleration)
- Loss of communication link (> 2 seconds)

## CO₂ Battery Infrastructure Interface

### Physical Interface Specifications

**Battery Pack Configuration:**
- Type: Containerized solid-state CO₂ battery modules
- Quantity: 4 modules per aircraft (2 port, 2 starboard)
- Location: Ventral bays, stations 18-22m
- Mounting: Quick-release docking system with guide rails

**Docking Interface:**
- Mechanical: Kinematic coupling with 3-point contact
- Electrical: High-current connector (500A continuous, 800V DC)
- Thermal: Liquid cooling quick-disconnect (50 L/min coolant flow)
- Data: Ethernet (1000BASE-T) + discrete I/O

**Access Requirements:**
- Clearance height: 2.5m under aircraft for battery cart
- Side clearance: 1.0m for operator access
- Docking alignment tolerance: ±10mm lateral, ±5mm vertical

### Charge/Discharge Operations

**Charging Infrastructure:**
- Power source: Airport grid or dedicated renewable energy (wind/solar)
- Charging rate: 100-200 kW per module (400-800 kW total)
- Voltage range: 600-850V DC
- Duration: 2-4 hours for 80% charge (during overnight parking)

**Discharge for CO₂ Regeneration:**
- Energy recovery: 80-90% round-trip efficiency
- Discharge rate: Up to 150 kW per module (when actively capturing CO₂)
- Thermal management: Integrated with aircraft thermal management system

### Thermal Management Interface

**Cooling Requirements:**
- Coolant type: Propylene glycol 50/50 mix (freeze point: -37°C)
- Flow rate: 30-50 L/min per module
- Supply temperature: 10-15°C
- Return temperature: 25-35°C (ΔT = 15-20°C nominal)

**Ground Cooling System:**
- Mobile cooling cart or fixed ground loop
- Heat rejection: 50-100 kW per module
- Temperature control: ±2°C stability
- Emergency backup: Air cooling (reduced capacity)

### Battery Monitoring and Telemetry

**Real-Time Data (1 Hz):**
- State of charge (SOC): 0-100%
- Cell voltages: Individual cell monitoring
- Temperature distribution: 12 points per module
- Internal pressure (for CO₂ containment integrity)
- Coolant flow rate and temperatures

**Event Logging:**
- Charge/discharge cycles
- Thermal excursions
- Fault conditions
- Connection/disconnection timestamps
- Energy throughput totals

## Cross-ATA Integration

### ATA 28 - Fuel (H₂) Systems

**Interface Points:**
- Tank pressure and temperature sensors → 85 ground monitoring
- H₂ quality verification data → 85 ground supply tracking
- Refuelling valve control signals ↔ 85 ground interlock system
- Flow meter data → ATA 28 consumption tracking and 85 billing

**Procedures:**
- Refuelling authorization from ATA 28 fuel management system
- Emergency defuelling commands routed through ATA 28
- Fuel quantity reconciliation (aircraft vs. ground measurements)

### ATA 71 - Power Plant (Fuel Cell Systems)

**Interface Points:**
- Fuel cell temperature status → 85 refuelling permissive
- Stack conditioning state → 85 timeline planning
- Performance data → 85 H₂ quality feedback loop

### ATA 80 - Energy Management (CO₂ Battery Owner)

**Interface Points:**
- Battery SOC and health → 85 charge scheduling
- Thermal management requests → 85 cooling system control
- Energy flow commands ↔ 85 ground power distribution
- CO₂ capture metrics → 85 environmental reporting

**Procedures:**
- Charge scheduling coordination with turnaround timeline
- Battery swap procedures (if rapid exchange is implemented)
- Thermal preconditioning before flight (cold weather operations)

### ATA 24 - Electrical Power

**Interface Points:**
- Ground power connection status → 85 energy interface permissives
- Electrical load distribution during charging → 85 capacity planning
- Power quality monitoring → 85 grid interface protection

## Safety Systems Integration

### H₂ Safety

**Leak Detection:**
- Technology: Catalytic bead sensors and infrared spectroscopy
- Coverage: 100% of refuelling zone (10m radius)
- Sensitivity: 0.1% LEL (Lower Explosive Limit)
- Response time: < 1 second detection to alarm

**Fire Suppression:**
- Type: Water deluge system (H₂ fires are cooled, not smothered)
- Activation: Automatic on fire detection or manual
- Coverage: 15m radius around refuelling points
- Flow rate: 10 L/m²/min for 30 minutes minimum

**Ventilation:**
- Outdoor refuelling: Natural ventilation, wind speed monitoring
- Indoor facilities (future): Forced ventilation, 12 air changes/hour minimum

### CO₂ Battery Safety

**Pressure Monitoring:**
- CO₂ containment integrity verified before docking
- Maximum safe pressure: 100 bar (at 50°C)
- Relief valve setting: 110 bar (vented to atmosphere)

**Thermal Runaway Protection:**
- Cell temperature limits: -20°C to +60°C operating range
- Shutdown threshold: +55°C with 2°C/min rise rate
- Emergency cooling: Expanded coolant flow + ambient air backup

## Operational Scenarios

### Normal Turnaround (60-90 minutes)

```
T+0:    Aircraft arrives at stand, engines shut down
T+5:    Wheel chocks, grounding, GPU connected
T+10:   H₂ leak detectors confirmed operational
T+12:   H₂ refuelling initiated (primary port)
T+27:   H₂ refuelling complete (15 min @ 6 kg/min, 90 kg transferred)
T+30:   CO₂ battery modules docked for top-up charge
T+60:   Batteries charged +20% SOC (fast charge mode)
T+75:   All ground services disconnected
T+85:   Aircraft ready for pushback
```

### Extended Turnaround / Overnight (4-8 hours)

```
T+0:    Aircraft secured at stand
T+15:   H₂ refuelling (if required)
T+30:   CO₂ battery modules in full charge mode
T+4h:   Batteries reach 90% SOC (slow, efficient charge)
T+8h:   All systems fully recharged, aircraft pre-flighted
```

### Emergency Defuelling Scenario

```
T+0:    Emergency declared (e.g., H₂ leak in aircraft tank)
T+1:    Emergency defuelling initiated (ventral port)
T+1:    Fire services on standby, exclusion zone established
T+15:   Controlled venting to atmosphere (when safe) or transfer to ground storage
T+30:   Aircraft H₂ tanks depressurized, secured for maintenance
```

## Future Infrastructure Evolution

### Hydrogen Infrastructure

- **Phase 1 (EIS)**: Mobile H₂ bowsers, 2-4 units per airport
- **Phase 2 (5 years)**: Fixed pipeline systems at major hubs
- **Phase 3 (10 years)**: On-site green H₂ production (electrolysis from renewables)

### CO₂ Battery Infrastructure

- **Phase 1 (EIS)**: Battery charging at stand, modules remain on aircraft
- **Phase 2 (3 years)**: Rapid battery swap capability for 15-minute turnarounds
- **Phase 3 (7 years)**: Integrated CO₂ regeneration facilities at airports (close the loop)

## Standards and Regulations

- **SAE AS50881**: Hydrogen Aircraft Refuelling Interface
- **ISO 14687**: Hydrogen fuel — Product specification
- **ISO 19881**: Gaseous hydrogen — Land vehicle fuel containers
- **NFPA 2**: Hydrogen Technologies Code
- **SAE ARP6490**: Aircraft Ground Support Equipment Electromagnetic Compatibility Requirements
- **EN 17127**: Hydrogen refuelling stations - Safety requirements
- **EASA CS-25**: Certification Specifications for Large Aeroplanes (Appendix F for fuel systems, extended for H₂)
- **FAA Part 25**: Airworthiness Standards (parallel to EASA CS-25)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
