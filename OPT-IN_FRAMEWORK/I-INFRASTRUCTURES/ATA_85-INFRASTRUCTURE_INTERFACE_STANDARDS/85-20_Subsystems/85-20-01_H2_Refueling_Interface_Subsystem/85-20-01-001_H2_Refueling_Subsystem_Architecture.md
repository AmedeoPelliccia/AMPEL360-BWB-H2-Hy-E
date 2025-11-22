# 85-20-01-001 — H2 Refueling Subsystem Architecture

## Document Metadata

```yaml
document_id: "85-20-01-001"
title: "H2 Refueling Subsystem Architecture"
parent_system: "85-20-01 H2 Refueling Interface Subsystem"
category: "Architecture"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

This document defines the high-level architecture of the H2 Refueling Interface Subsystem, establishing system boundaries, functional decomposition, and integration with aircraft and ground infrastructure systems.

## System Boundaries

### Aircraft Interface Boundary

**Interface Point:** Aircraft H2 fuel receptacle (part of [ATA 28 Fuel System](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/ATA_28-FUEL/README.md))

**Aircraft-Side Responsibilities:**
- H2 fuel receptacle with standardized coupling interface
- H2 tank fill/vent valves and controls
- Aircraft-side H2 quantity indication
- Fueling interlock signals to ground system
- Aircraft grounding/bonding provisions

**Ground-Side Responsibilities (This Subsystem):**
- H2 refueling dispenser and hose assembly
- Coupling mechanism and sealing
- Ground-side flow control, metering, and safety systems
- Data interface for refueling authorization and status
- Ground-side grounding/bonding equipment

### Ground Infrastructure Boundary

**Interface Point:** H2 refueling station or mobile H2 tanker

**Ground Infrastructure Responsibilities:**
- H2 storage (compressed gas or liquid)
- Primary H2 compression and pressure regulation
- Bulk H2 supply line to dispenser
- Ground infrastructure safety systems (beyond aircraft vicinity)

**This Subsystem Responsibilities:**
- Final H2 pressure regulation for aircraft
- Flow control and metering specific to aircraft refueling
- Safety monitoring in aircraft vicinity
- Data exchange with aircraft and operations center

## Functional Architecture

The H2 Refueling Interface Subsystem comprises five functional blocks:

```
┌─────────────────────────────────────────────────────────────┐
│         H2 Refueling Interface Subsystem (85-20-01)         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  1. H2 Coupling and Connection System (85-20-01-002)  │ │
│  │     - Mechanical coupling                             │ │
│  │     - Sealing and leak prevention                     │ │
│  │     - Breakaway protection                            │ │
│  └───────────────────────────────────────────────────────┘ │
│                           │                                 │
│  ┌────────────────────────┴────────────────────────────┐   │
│  │  2. H2 Safety Monitoring Subsystem (85-20-01-003)   │   │
│  │     - H2 leak detection                             │   │
│  │     - Safety interlocks                             │   │
│  │     - Emergency shutdown                            │   │
│  │     - Grounding/bonding verification                │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│  ┌────────────────────────┴────────────────────────────┐   │
│  │  3. H2 Flow Control and Metering (85-20-01-004)     │   │
│  │     - Flow rate control                             │   │
│  │     - Pressure management                           │   │
│  │     - Quantity measurement                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│  ┌────────────────────────┴────────────────────────────┐   │
│  │  4. H2 Data Interface and Communications            │   │
│  │     (85-20-01-005)                                  │   │
│  │     - Refueling authorization                       │   │
│  │     - Status reporting                              │   │
│  │     - Audit logging                                 │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
         │                                  │
         ▼                                  ▼
    Aircraft H2                      Ground Data Link
    Fuel System                       (85-20-06)
    (ATA 28)
```

## Architectural Principles

### 1. Defense in Depth

**Multiple Independent Safety Layers:**

- **Primary Protection:** Physical design (fail-safe valves, breakaway couplings)
- **Secondary Protection:** Active monitoring (H2 detection, pressure sensors)
- **Tertiary Protection:** Procedural safeguards (checklists, training, inspections)

### 2. Fail-Safe Design

All safety-critical components default to safe state on failure:

- **Valves:** Fail closed (stop H2 flow)
- **Sensors:** Fail to warn state (assume unsafe condition)
- **Interlocks:** Fail to inhibit (prevent refueling)
- **Communications:** Fail to require manual authorization

### 3. Standardization and Interoperability

Compliance with international H2 refueling standards enables operation at multiple airports:

- [ISO 19880-5](https://www.iso.org/standard/71975.html) coupling interface
- [SAE J2601](https://www.sae.org/standards/content/j2601/) fueling protocol (adapted)
- [CSA/ANSI HGV 4.3](https://www.csagroup.org/) connection devices

### 4. Modular Integration

Subsystem can interface with:
- Fixed ground H2 refueling stations
- Mobile H2 refueling tankers
- Future H2 infrastructure upgrades

## Physical Architecture

### Ground-Side Components

**H2 Dispenser Unit:**
- Final pressure regulator (350 bar to aircraft tank pressure)
- Flow control valve (electrically actuated)
- Flow meter (mass flow, ±0.5% accuracy)
- Pressure transmitters (upstream and downstream)
- Temperature sensors (for density compensation)
- Emergency shutoff valve (fast-acting, <1s closure)

**H2 Hose Assembly:**
- High-pressure flexible hose (rated >500 bar)
- Hose length: 15-20 meters (sufficient reach to aircraft receptacle)
- Breakaway coupling (activates on excessive tension or vehicle movement)
- Integrated grounding/bonding wire

**Coupling Nozzle:**
- Standardized mechanical interface (ISO 19880-5 or CSA HGV 4.3)
- Sealing mechanism (metal or elastomer seals)
- Leak detection port (for coupling verification)
- Electrical contacts for data and grounding

**Control Cabinet:**
- Refueling controller (PLC or embedded system)
- Safety relay logic (independent of main controller)
- Human-Machine Interface (HMI) for ground operator
- Data communication module (Ethernet, WiFi, or cellular)

### Aircraft-Side Components

*(Defined in [ATA 28 Fuel System](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/ATA_28-FUEL/README.md), summarized here for interface clarity)*

**H2 Fuel Receptacle:**
- Coupling interface matching ground nozzle
- Check valve preventing H2 backflow
- Fill/vent valve control
- Receptacle position: Accessible from ground (typically fuselage lower surface)

**H2 Tank System:**
- Composite overwrapped pressure vessels (COPV) at 350 or 700 bar
- H2 quantity sensors
- Pressure and temperature monitoring
- Vent system for pre-refueling pressure equalization

## Information Architecture

### Data Flows

**Refueling Authorization (Aircraft → Ground):**
- Aircraft ID and registration
- H2 tank capacity and current quantity
- Maximum fill pressure
- Authorization code (if required)

**Refueling Status (Ground → Aircraft):**
- Refueling phase (connecting, pressurizing, fueling, complete)
- Current flow rate (kg/s)
- Total quantity transferred (kg)
- Estimated time to completion

**Safety Monitoring (Bidirectional):**
- H2 leak detected (ground sensors → aircraft + ground system)
- Emergency shutdown command (aircraft or ground → refueling system)
- Coupling status (connected, sealed, leaking)

**Audit and Logging (Ground → Operations Center via 85-20-06):**
- Refueling transaction record (timestamp, aircraft ID, quantity, duration)
- Safety events and alarms
- System diagnostics and maintenance alerts

### Communication Protocols

**Primary:** Ethernet-based protocol (e.g., Modbus TCP, OPC UA, or custom)
**Backup:** Hardwired discrete signals for critical interlocks
**Wireless:** WiFi or cellular for non-critical data (optional, for convenience)

## Safety Architecture

### Hazard Mitigation Strategy

**Hazard H1: Uncontrolled H2 Release**

**Mitigation:**
- Redundant shutoff valves (two in series, independent actuation)
- Breakaway coupling (mechanical fuse)
- Pressure relief valves (prevent over-pressure rupture)
- H2 detection system (85-20-08) triggers automatic shutdown

**Hazard H2: Ignition Source Near H2**

**Mitigation:**
- Grounding/bonding (dissipate static electricity)
- Intrinsically safe electrical equipment in hazardous area
- Safety zone enforcement (no smoking, no hot work within 15m)
- Fire suppression equipment available

**Hazard H3: Coupling Failure Under Pressure**

**Mitigation:**
- Coupling strength validated for >2x operating pressure
- Periodic inspection and testing
- Leak detection at coupling before full pressurization
- Emergency depressurization capability

### Safety Instrumented System (SIS)

**SIL Rating:** SIL 3 (Safety Integrity Level 3) per [IEC 61508](https://www.iec.ch/functionalsafety/)

**SIS Functions:**
1. **Emergency Shutdown (ESD):** Close all valves, stop flow
2. **Leak Detection Shutdown:** Automatic shutdown on H2 detection
3. **Overpressure Protection:** Pressure relief and flow cutoff
4. **Grounding Verification:** Inhibit refueling if bonding not verified

**Architecture:** 2oo3 (Two-out-of-Three) voting for critical sensors (H2 detectors, pressure transmitters)

## Performance Requirements

### Refueling Rate

**Target:** 1-2 kg H2/min (typical for 350 bar systems)
**Maximum:** 3 kg H2/min (with advanced flow control)

**Rationale:** Balance refueling speed with thermal management (compression heating)

### Refueling Time

**Nominal Capacity:** 500 kg H2 (estimated for AMPEL360 BWB)
**Estimated Time:** 8-15 minutes fueling + 2-3 minutes connect/disconnect = **10-18 minutes total**

### Accuracy

**Flow Metering:** ±0.5% of reading (for billing and quantity verification)
**Quantity Totalizer:** ±1% of total quantity dispensed

### Availability

**Target:** 99.5% (refueling system available when needed)
**Maintenance:** Predictive maintenance to minimize downtime

## Integration with Other Subsystems

### 85-20-06: Data and Communications

**Interface:** Ethernet or WiFi for refueling data exchange

**Data Exchanged:**
- Refueling authorization and status
- Transaction logging
- Maintenance alerts

### 85-20-08: Safety and Monitoring

**Interface:** H2 detection sensors (analog 4-20mA or digital), discrete alarm signals

**Data Exchanged:**
- H2 concentration near aircraft
- Safety zone status (clear / hazard detected)
- Emergency shutdown command

### ATA 28: Fuel (On-Board)

**Interface:** H2 coupling (mechanical), electrical contacts (data + grounding)

**Data Exchanged:**
- Aircraft H2 quantity and pressure
- Fueling authorization
- Tank full indication

### 85-20-04: Evacuation and Rescue

**Interface:** Emergency shutdown signal (discrete)

**Operational Coordination:**
- Evacuation signal automatically shuts down H2 refueling
- ARFF notified of H2 refueling status

## Design Standards and References

- [ISO 19880-5](https://www.iso.org/standard/71975.html) — Gaseous hydrogen — Fueling stations — Part 5: Dispenser hoses and hose assemblies
- [SAE J2601](https://www.sae.org/standards/content/j2601/) — Fueling protocols for light duty gaseous hydrogen surface vehicles
- [IEC 61508](https://www.iec.ch/functionalsafety/) — Functional safety of electrical/electronic/programmable electronic safety-related systems
- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code
- [ARP4754A](https://www.sae.org/standards/content/arp4754a/) — Guidelines for development of civil aircraft and systems

## Future Enhancements

### Liquid H2 (LH2) Refueling

**Consideration:** LH2 refueling requires cryogenic handling (-253°C)

**Architectural Changes:**
- Vacuum-insulated hoses and couplings
- Cryogenic temperature monitoring
- Pre-cooling procedures
- Boil-off management

**Status:** Future capability, not in initial design

### Autonomous Refueling

**Consideration:** Robotic coupling and autonomous operation

**Architectural Changes:**
- Vision system for receptacle alignment
- Robotic arm for coupling attachment
- Enhanced diagnostics and self-test

**Status:** Technology demonstration, not production

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21

---

*Reference: [85-20-01 H2 Refueling Interface Subsystem README](./README.md)*
