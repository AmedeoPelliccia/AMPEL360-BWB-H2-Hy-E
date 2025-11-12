# Interface Control Document
## Door L1 Forward Electrical Interface

**ICD Number:** ICD-52-24-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 24 (Electrical Power)

---

## 1. INTERFACE OVERVIEW

### 1.1 Purpose
This ICD defines the electrical power interface between Door L1 Forward and the aircraft electrical power distribution system.

### 1.2 Scope
- Primary 28 VDC power supply
- Emergency power backup
- Signal interfaces
- Connector specifications
- Circuit protection
- EMI/lightning protection

---

## 2. POWER REQUIREMENTS

### 2.1 Primary Power
- Voltage: 28 VDC nominal (22-29 VDC operating range)
- Current: 30A maximum (door operation)
- Standby current: 0.2A continuous
- Circuit breaker: 35A thermal, 28 VDC bus
- Wire gauge: 8 AWG (power), 20 AWG (signals)
- Circuit ID: CB-52-01 on Load Distribution Panel 2

### 2.2 Power Consumption Profile

| Operating Mode | Power (W) | Current (A) | Duration (sec) | Energy (Wh) |
|----------------|-----------|-------------|----------------|-------------|
| Standby | 5 | 0.2 | Continuous | - |
| Opening (powered) | 840 | 30 | 15 | 3.5 |
| Closing (powered) | 840 | 30 | 18 | 4.2 |
| Emergency opening | 1200 | 43 | 8 | 2.7 |
| Warning lights | 15 | 0.5 | Continuous | - |
| Position sensors | 2 | 0.07 | Continuous | - |

### 2.3 Emergency Power
- Source: Emergency 28 VDC bus
- Backup time: 30 minutes minimum
- Load: Position indication and warning only (0.7A)
- Battery backup: Integrated in door controller

---

## 3. CONNECTOR SPECIFICATIONS

### 3.1 Power Connector (J1)
- Type: MIL-DTL-38999 Series III
- Part Number: D38999/26WG35PN
- Shell size: 25
- Pins: 4 power, 2 ground
- Location: Frame Station 105, WL 250, BL -540
- Mounting: Three-point bayonet lock
- Mating connector: D38999/26WG35SN (fuselage side)

### 3.2 Signal Connector (J2)
- Type: ARINC 600 compatible
- Part Number: ARINC600-2-RC-50
- Pins: 50 (32 used, 18 spare)
- Location: Adjacent to J1 (100mm spacing)
- Mounting: Rack and panel with jackscrews
- Mating connector: ARINC600-2-PC-50 (fuselage side)

### 3.3 Connector Environmental Protection
- Sealing: Grommet and O-ring per MIL-DTL-38999
- IP rating: IP67 when mated
- Corrosion: Salt spray per MIL-STD-810, Method 509
- Vibration: Per MIL-STD-810, Method 514, Category 4

---

## 4. SIGNAL INTERFACE

### 4.1 Power Signals (J1)

| Signal | Pin | Type | Voltage | Current | Function |
|--------|-----|------|---------|---------|----------|
| DOOR_28V_PWR_A | A | Power | 28 VDC | 15A | Main power A |
| DOOR_28V_PWR_B | B | Power | 28 VDC | 15A | Main power B |
| DOOR_GND_A | C | Ground | - | 15A | Power return A |
| DOOR_GND_B | D | Ground | - | 15A | Power return B |
| DOOR_EMERG_PWR | E | Power | 28 VDC | 5A | Emergency backup |
| DOOR_EMERG_GND | F | Ground | - | 5A | Emergency return |

### 4.2 Control Signals (J2)

| Signal | Pin | Type | Range | Update Rate | Function |
|--------|-----|------|-------|-------------|----------|
| DOOR_POS_ANALOG | B1 | Analog | 0-5 VDC | 100 Hz | Position feedback |
| DOOR_LOCKED | B2 | Discrete | 28V/Open | On change | Locked status |
| DOOR_UNLOCKED | B3 | Discrete | 28V/Open | On change | Unlocked status |
| DOOR_OPEN_LIMIT | B4 | Discrete | 28V/Open | On change | Fully open |
| DOOR_CLOSED_LIMIT | B5 | Discrete | 28V/Open | On change | Fully closed |
| DOOR_CMD_OPEN | B6 | Discrete | 28V/GND | - | Open command |
| DOOR_CMD_CLOSE | B7 | Discrete | 28V/GND | - | Close command |
| DOOR_MOTOR_TEMP | B8 | Analog | 0-5 VDC | 1 Hz | Motor temperature |
| DOOR_CTRL_TEMP | B9 | Analog | 0-5 VDC | 1 Hz | Controller temp |
| DOOR_FAULT | B10 | Discrete | 28V/Open | On change | Fault indication |
| SEAL_INFLATED | B11 | Discrete | 28V/Open | On change | Seal pressure OK |
| SEAL_INFLATE_CMD | B12 | Discrete | 28V/GND | - | Inflate seal |
| SLIDE_ARMED | B13 | Discrete | 28V/Open | On change | Slide armed status |
| DOOR_AJAR | B14 | Discrete | 28V/Open | On change | Not fully closed |

### 4.3 ARINC 429 Interface (J2)
- Transmit high: Pin C1
- Transmit low: Pin C2
- Receive high: Pin C3
- Receive low: Pin C4
- Bit rate: 100 kbps
- Word rate: 50 Hz
- Label: 250 (octal) for door status
- See ICD-52-23-001 for detailed protocol

---

## 5. CIRCUIT PROTECTION

### 5.1 Overcurrent Protection
- Main power: 35A thermal circuit breaker (CB-52-01)
- Emergency power: 10A circuit breaker (CB-52-01E)
- Signal circuits: Electronic limiting in door controller
- Motor protection: Thermal cutout at 85°C

### 5.2 Overvoltage Protection
- Transient suppression: TVS diodes to 45V
- Sustained overvoltage: Controller shutdown at >32 VDC
- Recovery: Automatic when voltage returns to normal

### 5.3 Short Circuit Protection
- Power short: Circuit breaker trip <100ms
- Signal short: Current limited to 0.5A per circuit
- Ground fault: Detected by controller, fault indication

---

## 6. EMI/LIGHTNING PROTECTION

### 6.1 Lightning Protection
- Level: Level 1 (direct strike capability)
- Current rating: 200 kA peak per DO-160G
- Cable shielding: 360° bond at both ends
- Transient protection: MOV and TVS at connector

### 6.2 EMI Shielding
- Cable shielding: Braid shield, 95% coverage minimum
- Connector backshell: Conductive, 360° termination
- Shield bonding resistance: <2.5 mΩ
- EMI attenuation: 60 dB @ 1-10 GHz per DO-160G

### 6.3 Grounding
- Primary ground: Through connector ground pins
- Secondary ground: Bonding strap, 0.5 AWG
- Bonding resistance: <2.5 mΩ to fuselage structure
- Ground loop prevention: Single-point ground architecture

---

## 7. CABLE ROUTING

### 7.1 Power Cable
- Route: Load Distribution Panel 2 → FS 105 via floor
- Length: 8.5 meters ±0.5m
- Type: MIL-W-22759/34, 8 AWG, PTFE insulation
- Shield: Not required for power
- Bend radius: 10× wire diameter minimum
- Support: Every 300mm, cushioned clamps

### 7.2 Signal Cable
- Route: Door Controller Unit → Door via door hinge
- Length: 2.0 meters (includes service loop)
- Type: MIL-W-22759/16, 20 AWG, shielded twisted pair
- Shield: Braid, 95% coverage
- Bend radius: 6× cable diameter minimum
- Flex life: 60,000 cycles (door operations)

---

## 8. MONITORING

### 8.1 CAOS Integration Signals
- Current monitoring: 0.1A resolution, 10 Hz sample rate
- Voltage monitoring: 0.1V resolution, 10 Hz sample rate
- Temperature: Motor and controller, 0.5°C resolution
- Cycle counting: Non-volatile memory, door operations
- Fault logging: Last 100 faults with timestamp

### 8.2 Health Monitoring
- Power quality: Voltage and current trending
- Temperature trending: Predict failures
- Cycle counting: Maintenance scheduling
- Fault history: Troubleshooting support

---

## 9. RESPONSIBILITIES

### 9.1 Interface Ownership

| Item | ATA 52 (Door) | ATA 24 (Electrical) |
|------|---------------|---------------------|
| Door controller | Provide & install | - |
| Power connector (J1) | Install | Provide |
| Signal connector (J2) | Install | Provide |
| Power cable | - | Provide & install |
| Signal cable | Provide & install | - |
| Circuit breakers | - | Provide & install |
| Load distribution | - | Design & implement |
| Functional test | Responsible | Support |

### 9.2 Maintenance Access
- Connectors: Accessible with panel removal
- Circuit breakers: Flight deck panel
- Door controller: Accessible from cabin side

---

## 10. VERIFICATION

### 10.1 Verification Methods
- [x] Dimensional inspection (connector locations)
- [x] Continuity test (all circuits)
- [x] Insulation resistance (>100 MΩ @ 500 VDC)
- [x] Functional test (all operating modes)
- [x] EMI test per DO-160G Category M
- [x] Lightning test per DO-160G Section 23
- [ ] Environmental test (-55°C to +85°C) - scheduled
- [ ] Vibration test per DO-160G - scheduled

### 10.2 Acceptance Criteria
- All signals functional per specification
- Insulation resistance: >100 MΩ at 500 VDC
- Contact resistance: <10 mΩ per pin
- EMI: No emissions exceeding DO-160G Category M limits
- Lightning: No damage, all circuits functional after strike
- Operating time: Open 15±2 sec, Close 18±2 sec

---

## 11. MAINTENANCE

### 11.1 Inspection Schedule
- Pre-flight: Visual check of connectors
- 500 FH: Detailed visual inspection
- 2,000 FH: Connector contact check
- 8,000 FH: Insulation resistance test
- 16,000 FH: Cable replacement (flex section)

### 11.2 Troubleshooting
- Built-in test (BIT) codes displayed on controller
- Fault isolation to LRU level
- Spare pins available for future expansion
- Test connector on controller for ground test

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
