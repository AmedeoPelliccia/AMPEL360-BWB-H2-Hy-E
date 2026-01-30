# 85-60-01-005 — Pressure Management

## Document Metadata

```yaml
document_id: "85-60-01-005"
title: "Pressure_Management"
parent_system: "85-60-01 H2 Storage Systems"
category: "Compression and Pressure Control"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-22"
```

## Purpose

This document defines the requirements, design specifications, and operational procedures for pressure management systems including compression, regulation, and safety relief for hydrogen storage and dispensing supporting the AMPEL360 BWB-H2-Hy-E aircraft.

## Pressure Management Overview

### Pressure Levels in H2 System

1. **LH2 Storage:** 1-10 bar
2. **Vaporization:** 1-50 bar (output from vaporizer)
3. **Compression:** 50-500 bar (intermediate and final stages)
4. **Cascade Storage:** 150-500 bar (three banks for efficient dispensing)
5. **Aircraft Refueling:** 350 bar (target for AMPEL360 BWB)

### Key Functions

- **Compression:** Increase pressure from vaporizer outlet to cascade storage or directly to aircraft
- **Regulation:** Control pressure for safe and efficient refueling
- **Safety Relief:** Protect equipment from over-pressure
- **Pressure Monitoring:** Continuous surveillance of system pressures

## Hydrogen Compressors

### Compressor Types

#### Reciprocating (Piston) Compressors

**Principle:** Positive displacement using pistons in cylinders

**Advantages:**
- High pressure capability (>700 bar)
- Good efficiency (70-85% isentropic)
- Proven technology

**Disadvantages:**
- Pulsating flow (requires dampeners)
- Higher maintenance (seals, valves, piston rings)
- Vibration and noise

**Applications:** Primary compressors for 350-700 bar cascade systems

#### Diaphragm Compressors

**Principle:** Reciprocating action with flexible diaphragm (no contact between H2 and lubrication)

**Advantages:**
- Oil-free compression (no contamination)
- Hermetic sealing (minimal H2 leakage)
- High pressure capability (>500 bar)

**Disadvantages:**
- Lower flow rate than piston compressors
- Higher cost
- Diaphragm fatigue (limited life)

**Applications:** High-purity H2 compression, where contamination is critical

#### Ionic Liquid Compressors

**Principle:** H2 absorbed in ionic liquid, liquid pressurized, H2 released at high pressure

**Advantages:**
- Oil-free, near-isothermal compression (high efficiency)
- Low noise and vibration
- High reliability (few moving parts)

**Disadvantages:**
- Emerging technology (limited commercial availability)
- Higher capital cost

**Applications:** Future technology for H2 refueling stations

### Compressor Sizing

**Capacity:** Based on peak refueling demand + safety margin

**Example:**
- Aircraft refueling rate: 2 kg H2/min (average)
- Peak demand: 3 aircraft simultaneously = 6 kg/min
- Compressor capacity: 8 kg/min (33% margin)

**Pressure Ratio:** Total pressure ratio = (final pressure / inlet pressure)

**Staging:** Multi-stage compression required for high pressure ratios

**Example:**
- Inlet: 5 bar (from vaporizer)
- Outlet: 500 bar (cascade high bank)
- Pressure ratio: 100:1
- Staging: 4 stages (pressure ratio per stage: 100^(1/4) ≈ 3.16:1)

**Intercooling:** Cool H2 between stages to improve efficiency and reduce final temperature

### Compression Energy

**Theoretical Energy:** Based on isentropic compression

**Example (simplified):**
- Compress 1 kg H2 from 5 bar to 500 bar
- Theoretical energy: ~2.2 kWh/kg (isothermal), ~2.8 kWh/kg (isentropic, γ=1.4)

**Actual Energy:** Divide by compressor efficiency (70-85%)
- Actual energy: 2.8 kWh / 0.75 ≈ **3.7 kWh/kg H2**

**Power Requirement:**
- For 8 kg/min compressor: 8 kg/min × 3.7 kWh/kg × (60 min/h) ≈ **30 kW continuous**

**Peak Power:** Higher during startup and transient conditions (size motor for peak, typically 1.5x continuous)

See: [85-80_Energy](../../85-80_Energy/README.md) for electrical power supply integration

### Compressor Design Features

**Oil-Free Design Preferred:**
- Prevents oil contamination of H2 (critical for fuel cell applications)
- Diaphragm compressors (inherently oil-free)
- Oil-lubricated compressors with oil separators (less preferred)

**Materials:**
- Cylinder and head: Stainless steel (300 series) or aluminum alloy
- Valves: Stainless steel with PTFE or PEEK seals
- Diaphragms: PTFE-coated or metal (for high pressure)

**Cooling:**
- Intercoolers between stages (water-cooled or air-cooled)
- After-cooler at final stage (cool to ambient temperature before storage)

**Instrumentation:**
- Pressure transmitters (suction and discharge, each stage)
- Temperature sensors (suction, interstage, discharge)
- Vibration sensors (for condition monitoring)

## Pressure Regulation

### Pressure Regulators

**Purpose:** Reduce pressure from cascade storage to safe and controlled refueling pressure

**Types:**

#### Dome-Loaded Regulators

**Principle:** Diaphragm-actuated valve, pressure in dome opposes inlet pressure

**Advantages:**
- Simple and reliable
- No external power required
- Fast response

**Disadvantages:**
- Limited accuracy (±5-10% of setpoint)
- Droop (outlet pressure decreases as flow increases)

**Applications:** General pressure reduction, where precise control not critical

#### Pilot-Operated Regulators

**Principle:** Small pilot regulator controls main valve actuator

**Advantages:**
- High accuracy (±1-2% of setpoint)
- Low droop (maintains outlet pressure under varying flow)
- High flow capacity

**Disadvantages:**
- More complex than dome-loaded
- Requires minimum flow for stability

**Applications:** Precision pressure control for aircraft refueling

#### Electronic Pressure Regulators

**Principle:** Electronic controller + electromechanical valve (e.g., motor-operated or solenoid)

**Advantages:**
- Very high accuracy (±0.1-0.5% of setpoint)
- Programmable setpoints and ramp rates
- Remote control and monitoring

**Disadvantages:**
- Requires electrical power
- Higher cost
- More complex (potential failure modes)

**Applications:** Advanced refueling systems with precise pressure profiling per [SAE J2601](https://www.sae.org/standards/content/j2601/) protocol

### Pressure Control Strategy for Refueling

**Goal:** Fill aircraft tank to target pressure (e.g., 350 bar) safely and efficiently

**Typical Profile per SAE J2601 (adapted for aircraft):**

1. **Ramp-Up Phase:** Gradually increase pressure (0 → 70% target pressure in 1-2 minutes)
   - Prevents thermal shock to aircraft tank
   - Allows time for safety system verification

2. **Fast-Fill Phase:** High flow rate at constant pressure differential (70% → 95% target pressure)
   - Maximum flow rate limited by aircraft tank heat dissipation
   - Typically 1-3 kg H2/min for automotive (may be higher for larger aircraft tanks)

3. **Top-Off Phase:** Reduce flow rate, approach target pressure slowly (95% → 100%)
   - Prevents over-filling
   - Allows aircraft tank temperature to stabilize

**Control Implementation:**
- Electronic pressure regulator (preferred)
- Manual adjustment with real-time monitoring (backup)

**Safety Interlocks:**
- Maximum pressure limit (prevents over-pressurization of aircraft tank)
- Maximum temperature limit (monitors aircraft tank temperature if available)
- H2 detection interlock (stops refueling if leak detected)

See: [85-20-01 H2 Refueling Interface Subsystem](../../85-20_Subsystems/85-20-01_H2_Refueling_Interface_Subsystem/README.md)

## Pressure Safety Systems

### Pressure Relief Valves (PRV)

**Purpose:** Protect vessels and piping from over-pressure

**Installation Locations:**
- LH2 storage tanks
- GH2 cascade vessels
- Compressor stages (suction and discharge)
- Vaporizers and heat exchangers
- Piping sections that can be isolated (thermal expansion)

**Sizing:**
- Capacity to relieve worst-case scenario (e.g., external fire, thermal expansion, runaway reaction)
- Per [ASME Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-division-1-rules-construction-pressure-vessels) or [API 520](https://www.api.org/products-and-services/oil-and-natural-gas/refining/api-520)

**Set Pressure:**
- Typically design pressure of protected equipment
- Multiple PRVs: Stagger set pressures (primary at design pressure, backup at 105% design pressure)

**Discharge:**
- Vent to safe location (minimum 3m above grade, away from ignition sources and air intakes)
- If large relief flows expected, vent to flare stack for controlled combustion

### Burst Discs

**Purpose:** Ultimate over-pressure protection (fail-safe)

**Installation:**
- In series with PRV (protects PRV from corrosion or fouling)
- Parallel with PRV (backup if PRV fails)

**Set Pressure:** Slightly above PRV set pressure (e.g., 110% design pressure)

**Limitation:** Single-use device (must be replaced after burst)

### Pressure Switches and Alarms

**High-Pressure Alarms:**
- Warn operators of abnormal pressure rise
- Typical setpoint: 90-95% of PRV set pressure
- Actions: Investigate cause, reduce pressure, prepare for potential relief event

**Low-Pressure Alarms:**
- Indicate insufficient supply pressure (e.g., compressor failure, tank empty)
- Actions: Switch to backup supply, notify operations

**Pressure Transmitters:**
- Continuous pressure monitoring
- Logged for trending and predictive maintenance

## Pressure Monitoring and Control System

### Instrumentation

**Pressure Transmitters:**
- Strategic locations: LH2 tank, vaporizer outlet, compressor stages, cascade banks, refueling hose
- Accuracy: ±0.5% full scale or better
- Output: 4-20 mA or digital (Modbus, Profibus, etc.)

**Pressure Gauges:**
- Local indication for operators
- Liquid-filled (glycerin) for vibration damping
- Ranges appropriate for location (0-10 bar for LH2 tank, 0-600 bar for cascade)

### Control System

**PLC or DCS:**
- Programmable Logic Controller (PLC) or Distributed Control System (DCS)
- Functions:
  - Compressor sequencing and load management
  - Cascade bank selection for refueling
  - Pressure regulation control (for electronic regulators)
  - Safety interlocks and emergency shutdown

**HMI (Human-Machine Interface):**
- Graphical display of system pressures
- Trend charts (historical pressure data)
- Alarm annunciation
- Manual control overrides (for maintenance or emergency)

**Data Logging:**
- Record all pressures, temperatures, flow rates
- Minimum resolution: 1 sample per second during refueling
- Retention: Minimum 3 years (for incident investigation and compliance)

## Operational Procedures

### Compressor Startup

1. Verify all valves in correct position (suction open, discharge closed initially)
2. Check oil level (if oil-lubricated compressor)
3. Check cooling water flow (if water-cooled)
4. Start compressor (allow warm-up period, no load)
5. Gradually open discharge valve (load compressor slowly)
6. Monitor suction and discharge pressures, temperatures, vibration
7. When pressures stabilized, place in automatic mode (if applicable)

### Normal Operation

**Continuous Monitoring:**
- Compressor pressures and temperatures (all stages)
- Cascade bank pressures
- H2 detection system status

**Automatic Functions:**
- Compressor load/unload based on cascade pressure
- Cascade bank selection for refueling (start with low bank, progress to high bank)
- Pressure regulation during refueling

**Operator Actions:**
- Periodic inspection (visual and auditory check of compressor)
- Log readings (pressures, temperatures, cycle counts)
- Respond to alarms and abnormal conditions

### Compressor Shutdown

**Normal Shutdown:**
1. Unload compressor (close suction or reduce load)
2. Allow compressor to run at idle (purge and cool down)
3. Stop compressor
4. Close isolation valves (if extended shutdown)

**Emergency Shutdown:**
1. ESD button (immediately stops compressor and closes valves)
2. Triggered by: High pressure, high temperature, H2 detection, fire alarm, manual activation

### Emergency Procedures

**Compressor High Pressure:**
1. Verify pressure reading (check if sensor error or actual)
2. If actual high pressure, unload compressor or stop
3. Check PRV (should relieve if at set pressure)
4. Investigate cause (downstream blockage, regulator failure, control system error)

**H2 Leak at Compressor:**
1. Activate ESD (stop compressor, close isolation valves)
2. Evacuate personnel upwind
3. Notify ARFF (establish safety perimeter)
4. Monitor H2 concentration (safe approach after H2 dispersed)
5. Isolate leaking component (if possible from safe distance)

## Maintenance

### Preventive Maintenance

**Daily:**
- Check compressor operation (listen for unusual noise, vibration)
- Verify pressures and temperatures normal
- Check for leaks (visual inspection)

**Weekly:**
- Check oil level (oil-lubricated compressors)
- Inspect cooling system (water flow, heat exchanger cleanliness)

**Monthly:**
- Change oil and filter (oil-lubricated compressors)
- Inspect valves and seals (reciprocating compressors)
- Test PRVs (manual lift test, if so equipped)

**Quarterly:**
- Vibration analysis (trending for bearing wear)
- Leak test of piping and fittings (soap solution or sniffer)

**Annual:**
- Major overhaul (reciprocating compressors): Replace piston rings, valves, seals
- Diaphragm replacement (diaphragm compressors, or per manufacturer recommendation)
- PRV recertification (remove and bench test)
- Pressure vessel inspection (cascade vessels, per ASME or ISO standards)

### Condition Monitoring

**Trending:**
- Compressor discharge pressure vs. inlet pressure (indicates efficiency)
- Intercooler outlet temperatures (indicates heat exchanger fouling)
- Vibration levels (indicates bearing wear or misalignment)

**Predictive Maintenance:**
- Schedule overhauls based on condition indicators, not just time
- Reduce unplanned downtime

## Standards and References

### Compressor Design

- [API 618](https://www.api.org/products-and-services/oil-and-natural-gas/refining/api-618) — Reciprocating Compressors for Petroleum, Chemical, and Gas Industry Services
- [ISO 13707](https://www.iso.org/standard/66179.html) — Petroleum and natural gas industries — Reciprocating positive-displacement compressors

### Pressure Relief

- [ASME BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-division-1-rules-construction-pressure-vessels) — Pressure Vessel Code (PRV sizing and installation)
- [API 520](https://www.api.org/products-and-services/oil-and-natural-gas/refining/api-520) — Sizing, Selection, and Installation of Pressure-Relieving Devices

### Safety and Operations

- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code
- [SAE J2601](https://www.sae.org/standards/content/j2601/) — Fueling protocols for light duty gaseous hydrogen surface vehicles (adapted for aircraft)
- [ISO 19880-1](https://www.iso.org/standard/71940.html) — Gaseous hydrogen — Fueling stations — Part 1: General requirements

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

*Reference: [85-60-01 H2 Storage Systems README](./README.md)*
