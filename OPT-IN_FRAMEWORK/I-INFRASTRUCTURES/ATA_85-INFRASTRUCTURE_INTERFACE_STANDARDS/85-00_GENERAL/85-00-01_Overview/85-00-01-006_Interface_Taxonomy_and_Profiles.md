# 85-00-01-006 Interface Taxonomy and Profiles

## Document Information

- **Document ID**: 85-00-01-006
- **Title**: Interface Taxonomy and Profiles
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Interface Specifications
- **ATA Chapter**: 85 - Infrastructure Interface Standards

## Purpose

This document defines a systematic taxonomy of interface profiles for the AMPEL360 BWB aircraft. These profiles provide standardized, versioned specifications for physical, operational, and data interfaces with ground infrastructure, enabling clear communication between aircraft designers, airport planners, and equipment manufacturers.

## Scope

This specification covers:

- Physical interface profiles (connectors, dimensions, clearances)
- Operational interface profiles (procedures, timelines, coordination)
- Data and signalling interface profiles (protocols, data rates, message formats)
- Profile versioning and change management
- Reference by subsystem documentation

## Interface Profile Structure

Each interface profile is defined with the following attributes:

### Profile Header

- **Profile ID**: Unique identifier (format: `BWB_<CATEGORY>_<NAME>_V<major>.<minor>`)
- **Version**: Major.Minor format (e.g., V1.0, V1.1, V2.0)
- **Status**: Draft, Active, Deprecated, Obsolete
- **Effective Date**: Date from which profile is valid
- **Supersedes**: Previous profile version (if applicable)
- **Owner**: Responsible ATA chapter

### Profile Content

- **Description**: Purpose and scope of the profile
- **Physical Specifications**: Dimensions, connector types, mechanical interface details
- **Performance Specifications**: Pressures, flow rates, electrical characteristics, data rates
- **Safety Requirements**: Interlocks, monitoring, emergency procedures
- **Operational Procedures**: Standard operating procedures, timelines
- **Verification**: Test methods, acceptance criteria

## Physical Interface Profiles

### H2_REFUELLING_STAND_PROFILE_A (V1.0)

**Profile ID**: BWB_PHYS_H2_REFUELLING_STAND_A_V1.0  
**Status**: Active  
**Effective Date**: 2025-11-21  
**Owner**: ATA 85

**Description:**  
Standard hydrogen refuelling interface for fixed or mobile ground infrastructure serving AMPEL360 BWB aircraft.

**Physical Specifications:**
- **Connector Type**: SAE AS50881 compliant, high-pressure quick-disconnect
- **Coupling Size**: DN15 (15mm nominal diameter)
- **Operating Pressure Range**: 350-700 bar (5,000-10,000 psi)
- **Leak Rate**: < 0.01% of nominal flow rate
- **Connection Force**: < 150 N (manual operation)
- **Breakaway Force**: 200-300 N (emergency disconnect)

**Performance Specifications:**
- **Flow Rate**: 4-8 kg H₂/min (nominal 6 kg/min)
- **Transfer Duration**: 15-25 minutes (for 90 kg H₂)
- **H₂ Quality**: ISO 14687 Type I Grade D (99.97% purity minimum)
- **Temperature Range**: -40°C to +50°C (operational)

**Safety Requirements:**
- Grounding: < 1 Ω resistance to aircraft ground point
- Leak Detection: 0.1% LEL sensitivity, < 1 second response time
- Emergency Stop: Hardwired signal, fail-safe (refuelling stops on signal loss)
- Exclusion Zone: 10m radius during active transfer

**Operational Procedures:**
- Pre-refuelling checklist (10 items, 5 minutes)
- Refuelling sequence (initiation, monitoring, completion)
- Post-refuelling verification (pressure, temperature, leak check)

**Verification:**
- Flow rate test: ±5% accuracy over full range
- Leak test: Pressure hold at 700 bar for 10 minutes, < 0.1 bar drop
- Emergency stop test: < 2 seconds from activation to zero flow

---

### CO2_BATTERY_DOCK_TYPE_1 (V1.0)

**Profile ID**: BWB_PHYS_CO2_BATTERY_DOCK_1_V1.0  
**Status**: Active  
**Effective Date**: 2025-11-21  
**Owner**: ATA 85

**Description:**  
Mechanical, electrical, and thermal docking interface for CO₂ battery module exchange and charging.

**Physical Specifications:**
- **Docking Mechanism**: Three-point kinematic coupling (precision: ±10mm lateral, ±5mm vertical)
- **Module Dimensions**: 1.2m x 0.8m x 0.6m (L x W x H), 450 kg mass
- **Guide Rails**: V-groove guides, 1.5m travel length
- **Retention**: Electromechanical latches, 4 points, 2,000 kg hold force (combined)

**Electrical Interface:**
- **Connector Type**: High-current Anderson SB350, 350A rated (derated to 200A continuous)
- **Voltage Range**: 600-850V DC
- **Current Capability**: 200A continuous, 300A peak (10 seconds)
- **Signal Interface**: Ethernet (1000BASE-T), RJ45 connector + 4 discrete I/O lines (24V logic)

**Thermal Interface:**
- **Coolant Connector**: Quick-disconnect, 50mm bore (Stäubli RBE series or equivalent)
- **Coolant Type**: Propylene glycol 50/50 mix (freeze point: -37°C)
- **Flow Rate**: 30-50 L/min (regulated by ground cooling cart)
- **Temperature**: Supply 10-15°C, return 25-35°C (nominal ΔT = 15°C)

**Safety Requirements:**
- Docking Verification: Position sensors confirm full engagement before electrical connection
- Thermal Runaway Protection: Temperature sensors on battery (limit: +55°C)
- Emergency Undock: Manual release override (accessible from ground and cockpit)

**Operational Procedures:**
- Docking sequence (7 steps, 7 minutes total)
- Charging initiation (handshake protocol, 2 minutes)
- Undocking sequence (5 steps, 5 minutes)

**Verification:**
- Mechanical alignment test: 100 dock/undock cycles, no damage
- Electrical test: 1,000 connection cycles, resistance < 1 mΩ
- Thermal test: 500 L coolant flow at 50°C for 8 hours, no leaks

---

### GPU_CONNECTION_PROFILE_BWB (V1.0)

**Profile ID**: BWB_PHYS_GPU_CONNECTION_V1.0  
**Status**: Active  
**Effective Date**: 2025-11-21  
**Owner**: ATA 24 (referenced by ATA 85)

**Description:**  
Ground power unit electrical connection interface for AMPEL360 BWB aircraft.

**Physical Specifications:**
- **Connector Type**: MIL-STD-2186 (NATO standard) or equivalent
- **Connector Location**: Forward fuselage, port side, station 6.0m, 2.0m above ground
- **Cable Length**: 25m (from GPU to aircraft)
- **Connector Retention**: Bayonet lock with secondary safety latch

**Electrical Specifications:**
- **Voltage**: 115V AC, three-phase, wye configuration
- **Frequency**: 400 Hz ±1 Hz
- **Power Rating**: 90 kVA (continuous)
- **Current**: 450A per phase (maximum)
- **Power Factor**: > 0.9 (at rated load)
- **Voltage Regulation**: ±5% from no-load to full-load
- **Harmonic Distortion**: < 3% THD (Total Harmonic Distortion)

**Safety Requirements:**
- Ground Fault Protection: 30 mA trip threshold, < 30 ms response
- Overload Protection: 110% for 2 minutes, 125% trip in 10 seconds
- Connector Interlock: GPU output disabled when connector not fully engaged

**Operational Procedures:**
- GPU positioning and cable routing (3 minutes)
- Connector engagement and power-on sequence (2 minutes)
- Power quality verification (automatic, 30 seconds)
- Disconnection sequence (1 minute)

**Verification:**
- Voltage and frequency test: Verification over 0-100% load range
- Transient test: Load step 0-90 kVA in 100ms, voltage within ±10% during transient
- Endurance test: 1,000 connection/disconnection cycles

---

## Operational Interface Profiles

### EMERGENCY_EVAC_INTERFACE_LEVEL_1 (V1.0)

**Profile ID**: BWB_OPER_EMERGENCY_EVAC_L1_V1.0  
**Status**: Active  
**Effective Date**: 2025-11-21  
**Owner**: ATA 85 (coordination), ATA 52, ATA 26 (content)

**Description:**  
Coordinated emergency evacuation procedures and infrastructure interface requirements for normal circumstances at certified airports.

**Prerequisites:**
- Airport certified for BWB operations (ICAO Annex 14 compliant)
- ARFF Category (minimum): Category 9 (aircraft length 52-66m)
- H₂ fire response capability verified
- Stand evacuation zones marked and clear

**Aircraft Capabilities:**
- 12 Type A doors + 4 Type III overwing exits
- Evacuation capacity: 220 passengers in 90 seconds (demonstrated)
- Emergency lighting: Operational (battery-backed, 30 minutes minimum)

**Airport Infrastructure:**
- Clear evacuation zones: 10m x 5m per door/exit
- Assembly points: 100m from aircraft, illuminated (20 lux minimum)
- ARFF response time: < 3 minutes to any point on aircraft
- Medical staging area: 50m from aircraft, 20m x 30m minimum

**Coordination Procedures:**
1. Emergency declared: Aircraft transmits emergency signal (automatic + crew confirmation)
2. Airport operations center notified: < 30 seconds
3. ARFF dispatch: < 1 minute
4. Door/slide deployment: Crew-initiated, automatic slide inflation (< 6 seconds)
5. Passenger evacuation: 90 seconds target (all passengers off aircraft)
6. ARFF arrival: < 3 minutes from declaration
7. Assembly and accountability: 5-10 minutes post-evacuation

**Data Interfaces:**
- Emergency signal: ACARS message + discrete signal to airport tower
- Door status: Real-time transmission to airport operations center
- Passenger count: Manifest data transmitted pre-evacuation

**Success Criteria:**
- Evacuation time: < 90 seconds
- Injuries: Zero (goal), minimize (acceptable)
- All passengers accounted: < 15 minutes post-evacuation

---

### TURNAROUND_STANDARD_60MIN (V1.0)

**Profile ID**: BWB_OPER_TURNAROUND_60MIN_V1.0  
**Status**: Active  
**Effective Date**: 2025-11-21  
**Owner**: ATA 02 (content), ATA 85 (infrastructure interface)

**Description:**  
Standard 60-minute turnaround operational profile for routine flights at equipped airports.

**Prerequisites:**
- H₂ refuelling capability (mobile bowser or fixed system)
- GPU and PCA available
- Standard GSE (cargo loaders, catering, stairs/jetway)
- Ground crew trained for BWB operations

**Timeline (Critical Path):**
- T+0: Arrival, engines shutdown
- T+2: Wheel chocks, GPU connected, ground power established
- T+5: Passenger disembarkation begins (door 1L/R)
- T+10: H₂ refuelling initiated (primary port, port side)
- T+15: Disembarkation complete
- T+25: H₂ refuelling complete (15 min @ 6 kg/min)
- T+25: Cargo loading begins (forward and aft, parallel)
- T+40: Cargo loading complete
- T+45: Passenger boarding begins
- T+55: Boarding complete, doors closed
- T+58: GPU disconnected, pre-flight complete
- T+60: Pushback ready

**Parallel Activities (Non-Critical Path):**
- Catering and cleaning: T+20 to T+45
- CO₂ battery top-up (if required): T+30 to T+50 (20 min fast charge)
- Lavatory/water servicing: T+20 to T+35

**GSE Requirements:**
- GPU: 90 kVA, 115V AC 400Hz
- PCA: 2 carts, 2.5 kg/s each
- H₂ bowser: 500 kg capacity minimum
- Cargo loaders: 2 units (forward and aft)
- Catering highloaders: 2 units
- Pushback tractor: Towbarless or tow bar capable

**Performance Metrics:**
- On-time performance: > 95% turnarounds completed within 60 minutes (±5 min buffer)
- Safety: Zero ground incidents per 1,000 turnarounds
- H₂ refuelling efficiency: 85-95 kg transferred (depending on flight plan)

---

## Data and Signalling Interface Profiles

### ENERGY_TELEMETRY_PROFILE_BWB_V1 (V1.0)

**Profile ID**: BWB_DATA_ENERGY_TELEMETRY_V1.0  
**Status**: Active  
**Effective Date**: 2025-11-21  
**Owner**: ATA 85 (ground side), ATA 28, ATA 80 (aircraft side)

**Description:**  
Data interface profile for real-time monitoring of H₂ refuelling and CO₂ battery operations.

**Physical Layer:**
- **Medium**: CAN bus (Controller Area Network) for H₂, Ethernet (1000BASE-T) for CO₂ batteries
- **Connector**: CAN - 9-pin D-sub, Ethernet - RJ45
- **Cable**: CAN - twisted pair, shielded; Ethernet - Cat6, shielded

**Data Link Layer:**
- **CAN**: ISO 11898 (CAN 2.0B), 500 kbps bit rate, extended frame format
- **Ethernet**: IEEE 802.3, TCP/IP stack

**Application Layer:**

**H₂ Refuelling Telemetry (CAN Messages):**

| Message ID | Name | Data | Update Rate | Priority |
|------------|------|------|-------------|----------|
| 0x100 | H2_FLOW_RATE | Flow rate (kg/min), 16-bit unsigned | 10 Hz | High |
| 0x101 | H2_PRESSURE | Tank pressure (bar), 16-bit unsigned | 1 Hz | Medium |
| 0x102 | H2_TEMPERATURE | Tank temperature (°C), 16-bit signed | 1 Hz | Medium |
| 0x103 | H2_LEAK_STATUS | Leak detected (boolean), leak level (% LEL) | 10 Hz | Critical |
| 0x104 | H2_REFUEL_STATUS | State (idle, refuelling, complete, fault), 8-bit enum | 1 Hz | Medium |
| 0x1FF | H2_EMERGENCY_STOP | Emergency stop command (ground or aircraft) | Event-driven | Critical |

**CO₂ Battery Telemetry (Ethernet Messages, JSON format):**

```json
{
  "timestamp": "ISO 8601 datetime",
  "battery_id": "module identifier (1-4)",
  "state_of_charge": 0.0-100.0,
  "voltage": 600-850,
  "current": -200 to +200,
  "temperature": {
    "cells": [array of 12 temperatures],
    "max": temperature,
    "min": temperature,
    "average": temperature
  },
  "coolant": {
    "flow_rate": 30-50,
    "temp_supply": 10-15,
    "temp_return": 25-35
  },
  "status": "charging | discharging | idle | fault",
  "faults": [array of fault codes]
}
```

**Update Rate**: 1 Hz (normal operation), 10 Hz (during fault conditions)

**Security:**
- Authentication: Pre-shared key (PSK) for Ethernet connection
- Encryption: AES-256 for sensitive data (not required for telemetry, but recommended for command messages)
- Access Control: Ground equipment must authenticate before sending commands

**Verification:**
- Data integrity test: CRC verification for CAN messages, TCP checksum for Ethernet
- Latency test: End-to-end latency < 100 ms (CAN), < 50 ms (Ethernet)
- Reliability test: < 1 message error per 10⁶ messages transmitted

---

### GROUND_AIRCRAFT_INTERLOCK_PROFILE (V1.0)

**Profile ID**: BWB_DATA_GROUND_AIRCRAFT_INTERLOCK_V1.0  
**Status**: Active  
**Effective Date**: 2025-11-21  
**Owner**: ATA 85 (coordination), multiple ATA owners (content)

**Description:**  
Safety interlock signals exchanged between aircraft and ground equipment to ensure safe operations.

**Signal Interface:**
- **Type**: Discrete I/O, 24V DC logic (high = 18-30V, low = 0-5V)
- **Connector**: 37-pin D-sub (shared with other ground service signals)
- **Wiring**: Individual shielded twisted pairs for each signal

**Interlock Signals (Aircraft to Ground):**

| Signal Name | Pin | Description | Active State |
|-------------|-----|-------------|--------------|
| AIRCRAFT_READY | 1 | Aircraft systems powered, ready for ground services | High |
| ENGINES_STOPPED | 2 | All engines stopped and cooled (> 10 min) | High |
| FIRE_SYSTEM_ARMED | 3 | Fire detection and suppression systems operational | High |
| DOORS_CLOSED | 4 | All passenger and cargo doors closed and locked | High |
| WHEEL_CHOCKS_REQ | 5 | Aircraft requires wheel chocks (weight on wheels) | High |
| EMERGENCY_STOP_ACFT | 6 | Aircraft-initiated emergency stop (all ground ops) | Low (fail-safe) |

**Interlock Signals (Ground to Aircraft):**

| Signal Name | Pin | Description | Active State |
|-------------|-----|-------------|--------------|
| GROUND_POWER_AVAIL | 11 | GPU connected and power available | High |
| H2_REFUEL_ACTIVE | 12 | H₂ refuelling in progress | High |
| WHEEL_CHOCKS_IN | 13 | Wheel chocks in place (verified by sensor or crew) | High |
| GROUNDING_CONNECTED | 14 | Aircraft grounded (< 1 Ω resistance) | High |
| GSE_CLEAR | 15 | All ground equipment clear of aircraft (ready for pushback) | High |
| EMERGENCY_STOP_GND | 16 | Ground-initiated emergency stop (all aircraft ops) | Low (fail-safe) |

**Logic Requirements:**
- H₂ refuelling permissive: AIRCRAFT_READY AND ENGINES_STOPPED AND FIRE_SYSTEM_ARMED AND DOORS_CLOSED AND WHEEL_CHOCKS_IN AND GROUNDING_CONNECTED
- Pushback permissive: ENGINES_STOPPED AND DOORS_CLOSED AND GSE_CLEAR AND (NOT H2_REFUEL_ACTIVE)

**Fail-Safe Design:**
- Emergency stop signals (pins 6, 16) are active-low: Loss of signal triggers emergency stop
- Critical interlocks are hardwired (not software-dependent)

**Verification:**
- Signal level test: Verify voltage levels for high and low states
- Interlock logic test: Verify permissive conditions (e.g., attempt H₂ refuelling with door open = should be blocked)
- Fail-safe test: Disconnect emergency stop signal, verify immediate cessation of operations

---

## Profile Versioning and Change Management

### Version Numbering

**Major Version (X.0):**
- Incompatible changes (e.g., connector type change, new safety requirements)
- Requires re-certification or re-approval
- Previous version may be deprecated or obsoleted

**Minor Version (X.Y):**
- Compatible enhancements (e.g., additional optional data fields, improved procedures)
- Backward compatible with previous minor versions
- No re-certification required (but validation recommended)

### Change Process

1. **Proposal**: Change request submitted by any stakeholder (design team, operator, airport, supplier)
2. **Review**: Technical review by interface working group (representatives from relevant ATA chapters)
3. **Impact Assessment**: Determine affected systems, documentation, certification basis
4. **Approval**: Decision by chief engineer or designated authority
5. **Implementation**: Update profile document, notify all stakeholders
6. **Verification**: Test new profile version (if applicable)
7. **Release**: Publish updated profile, update cross-references in subsystem documents

### Profile Status Lifecycle

```
Draft → Active → Deprecated → Obsolete
         ↑          ↓
         └──────────┘ (minor version updates remain Active)
```

- **Draft**: Under development, not for operational use
- **Active**: Approved for use, current version
- **Deprecated**: Superseded by newer version, still acceptable but not recommended
- **Obsolete**: No longer valid, must not be used for new designs or installations

---

## Reference in Subsystem Documentation

Subsystem documents (in other ATA chapters) shall reference interface profiles using the following format:

**Example (in ATA 28 Fuel System document):**

> "The H₂ refuelling interface shall comply with profile **BWB_PHYS_H2_REFUELLING_STAND_A_V1.0** as defined in [85-00-01-006 Interface Taxonomy and Profiles](85-00-01-006_Interface_Taxonomy_and_Profiles.md)."

**Benefits:**
- Single source of truth for interface specifications
- Clear traceability from requirements to detailed design
- Version control enables impact analysis for changes

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
