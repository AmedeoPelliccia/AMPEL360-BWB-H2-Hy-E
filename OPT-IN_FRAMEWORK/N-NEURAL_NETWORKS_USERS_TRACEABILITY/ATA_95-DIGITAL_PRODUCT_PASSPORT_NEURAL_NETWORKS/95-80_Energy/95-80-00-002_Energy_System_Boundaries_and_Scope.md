# 95-80-00-002 Energy System Boundaries and Scope

**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**ATA Chapter:** 95-80 (Energy)

---

## 1. Purpose

This document defines the boundaries and scope of the Energy (95-80) module, clarifying what is included and excluded, and establishing interfaces with other systems.

---

## 2. System Boundaries

### 2.1 Physical Boundaries

#### Included:
- LH₂ tank outlets to fuel cell inlets
- Fuel cell stacks and power conditioning units
- Electrical distribution network (buses, contactors, protection)
- Electric motor drive systems
- Hydraulic pumps and distribution
- Pneumatic compressors and distribution
- APU electrical generation
- Battery energy storage systems
- Energy management system (EMS) hardware and software
- Thermal management interfaces for waste heat

#### Excluded:
- LH₂ tank internal systems (covered in ATA 28 fuel storage)
- Propulsion motor mechanical interfaces (covered in ATA 70-79 propulsion)
- Avionics power supplies (covered in ATA 42)
- Individual consumer loads (covered in respective ATA chapters)
- External charging/refueling infrastructure (covered in I-INFRASTRUCTURES)

### 2.2 Functional Boundaries

#### Included:
- Energy generation (fuel cells, APU, regeneration)
- Energy conversion (DC/DC, DC/AC, AC/DC)
- Energy distribution (electrical, hydraulic, pneumatic)
- Energy storage management (batteries, accumulators)
- Power quality management (filtering, conditioning)
- Load management and prioritization
- Energy monitoring and diagnostics
- Fault detection and isolation
- Emergency power modes

#### Excluded:
- Aircraft flight control laws (covered in ATA 27)
- Mission planning algorithms (covered in ATA 02 operations)
- Structural integration of energy systems (covered in respective structural ATA)
- Software application logic (covered in ATA 42 IMA applications)

---

## 3. Energy Domain Scope

### 3.1 Electrical Domain

**Scope:**
- Voltage levels: 270 VDC primary bus, 28 VDC secondary, 115/200 VAC
- Frequency: 400 Hz AC where applicable
- Power generation: Fuel cells (2.5 MW continuous), APU (350 kW), batteries (500 kW peak)
- Distribution architecture: Multi-bus with cross-ties
- Protection: Circuit breakers, solid-state power controllers (SSPCs)

**Boundaries:**
- From fuel cell DC bus output to final consumer input terminals
- Includes power management and control units
- Excludes individual consumer internal power supplies

### 3.2 Chemical Domain (H₂)

**Scope:**
- H₂ energy content and flow rates
- Conversion efficiency tracking
- Energy balance from tank to fuel cell
- Boil-off and loss accounting

**Boundaries:**
- From tank outlet pressure/temperature measurement to fuel cell inlet
- Excludes tank internal design (ATA 28)
- Excludes downstream fuel cell electrochemistry details

### 3.3 Hydraulic Domain

**Scope:**
- Hydraulic system pressure: 5000 psi
- Flow rate monitoring
- Accumulator energy storage
- Pump efficiency and power consumption

**Boundaries:**
- From electric pump input to hydraulic consumer actuators
- Includes accumulators and pressure management
- Excludes actuator internal design (ATA 27, 29, 32)

### 3.4 Pneumatic Domain

**Scope:**
- Compressed air pressure: 50-200 psi depending on application
- Compressor power consumption
- Air storage energy
- Distribution to ECS, anti-ice, and other consumers

**Boundaries:**
- From compressor inlet to pneumatic consumer inlet
- Includes air reservoirs and pressure regulation
- Excludes consumer internal pneumatics (ATA 21, 30, 36)

### 3.5 Thermal Domain

**Scope:**
- Waste heat generation tracking
- Cooling loads and thermal management
- Heat recovery opportunities
- Thermal energy storage (if applicable)

**Boundaries:**
- Energy content of heat flows
- Interface temperatures and flow rates
- Excludes detailed thermal system design (ATA 21)

---

## 4. Temporal Scope

### 4.1 Mission Phases

The Energy module addresses all flight mission phases:

1. **Ground operations**: Pre-flight, post-flight, maintenance
2. **Engine start**: APU and main power-up sequence
3. **Taxi**: Low power, ground maneuvering
4. **Takeoff**: Maximum power demand (3.5 MW peak)
5. **Climb**: High continuous power (2.8 MW)
6. **Cruise**: Optimized efficiency (2.0 MW)
7. **Descent**: Regenerative energy capture
8. **Approach/Landing**: Variable power management
9. **Emergency**: Degraded modes, essential power only

### 4.2 Lifecycle Phases

1. **Design**: Energy requirements definition, architecture selection
2. **Development**: Component testing, integration, validation
3. **Production**: Calibration, quality assurance
4. **Operation**: Real-time monitoring, optimization
5. **Maintenance**: Diagnostics, prognostics, repair
6. **Disposal**: Energy system decommissioning, recycling

---

## 5. Data Scope

### 5.1 Real-Time Data

- Power generation (fuel cells, APU, batteries)
- Power consumption by bus and major loads
- Voltage, current, frequency on all buses
- Energy storage state (battery SoC, accumulator pressure)
- Thermal conditions (temperatures, cooling flows)
- System health and status indicators

### 5.2 Accumulated Data

- Total energy produced/consumed per mission
- Fuel cell cumulative runtime and cycling
- Battery charge/discharge cycles
- Energy efficiency trends
- Maintenance trigger counters

### 5.3 Metadata

- System configuration
- Component serial numbers and versions
- Calibration data
- Operating limits and thresholds
- Traceability to design requirements

---

## 6. Interfaces

### 6.1 Physical Interfaces

| Interface | Type | Description |
|-----------|------|-------------|
| LH₂ supply | Fluid | From ATA 28 fuel tanks |
| Electrical buses | Electrical | To all aircraft systems |
| Hydraulic lines | Fluid | To actuation systems |
| Pneumatic ducts | Fluid | To ECS and anti-ice |
| Cooling loops | Thermal | To thermal management system |
| Control signals | Digital | CAN, ARINC 429, Ethernet |

### 6.2 Functional Interfaces

| System | Interface Description |
|--------|----------------------|
| **Flight Control (ATA 27)** | Power demand, emergency mode triggers |
| **Avionics (ATA 42)** | Data exchange, health monitoring |
| **ECS (ATA 21)** | Pneumatic/electrical power, waste heat |
| **Landing Gear (ATA 32)** | Hydraulic power for extension/retraction |
| **CAOS (ATA 40/92)** | Energy optimization, predictive maintenance |
| **Propulsion (ATA 70-79)** | Primary power distribution, regeneration |

---

## 7. Exclusions and Clarifications

### 7.1 What This Module Does NOT Cover

- **Detailed fuel cell electrochemistry**: Vendor-specific, covered in ATA 24 subsystem docs
- **Individual consumer load internal design**: Each consumer's power supply is in its own ATA
- **Fuel tank structural design**: Covered in ATA 28 and structural chapters
- **Ground power carts and GSE**: Covered in I-INFRASTRUCTURES
- **Airport charging infrastructure**: External to aircraft, covered in I-INFRASTRUCTURES
- **Software application logic**: Covered in ATA 42/45/46 software chapters

### 7.2 Clarifications

- **Energy vs. Power**: This module tracks both instantaneous power (kW) and integrated energy (kWh)
- **Efficiency definitions**: Clearly defined in `00_META/95-80-00-006_Energy_Balances_and_KPI_Definitions.md`
- **Cross-ATA coordination**: Energy impacts all systems; coordination managed through Digital Product Passport and traceability matrix
- **CAOS integration**: Energy module provides data to CAOS; CAOS provides optimization commands

---

## 8. Assumptions and Constraints

### 8.1 Assumptions

1. Fuel cells operate within manufacturer specifications
2. Electrical loads follow predicted demand profiles
3. Battery degradation follows standard models
4. Environmental conditions within aircraft operating envelope
5. Proper maintenance intervals are followed

### 8.2 Constraints

1. **Regulatory**: EASA CS-25, FAA Part 25, RTCA DO-160, DO-254, DO-178C
2. **Safety**: DAL A for critical power paths, redundancy requirements
3. **Weight**: Total energy system <4,500 kg including H₂
4. **Volume**: Fit within BWB center body envelope
5. **Thermal**: Waste heat must be dissipated without exceeding structural limits
6. **Cost**: Target <30% of total aircraft cost

---

## 9. Related Documents

| Document | Description |
|----------|-------------|
| [95-80-00-001](95-80-00-001_Energy_Overview.md) | Energy module overview |
| [95-80-00-003](95-80-00-003_Cross_ATA_Energy_Map.csv) | Cross-ATA interfaces |
| [00_META/95-80-00-004](00_META/95-80-00-004_Energy_Taxonomy.md) | Energy terminology |
| [00_META/95-80-00-005](00_META/95-80-00-005_Energy_Traceability_Matrix.csv) | Requirements traceability |

---

## 10. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Energy WG | Initial version |

---

**Document Control**
- **Standard**: OPT-IN Framework v1.5
- **Owner**: AMPEL360 Documentation WG
- **Classification**: Technical Reference
