# Interface Control Document
## Door L1 Forward IMA Integration

**ICD Number:** ICD-52-42-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 42 (Integrated Modular Avionics)

---

## 1. INTERFACE OVERVIEW

This ICD defines the integration of Door L1 Forward with the aircraft Integrated Modular Avionics (IMA) system for control, monitoring, and data processing.

---

## 2. IMA ARCHITECTURE

### 2.1 Cabinet Assignment
- IMA Cabinet: CAB-2 (Common Computing Resource)
- Partition: DOOR-MGMT
- Priority: Level 3 (non-flight-critical)
- CPU allocation: 5% partition
- Memory: 64 MB

### 2.2 I/O Module
- Type: ARINC 653 I/O module
- Location: IMA Cabinet 2, Slot 7
- Interfaces: 4× ARINC 429, 16× discrete, 8× analog

---

## 3. DATA INTERFACE

### 3.1 ARINC 429 Connections
- RX from Flight Deck: Commands, configuration
- TX to Flight Deck: Status, position, warnings
- TX to CMC: Maintenance data
- RX from Power System: Power status

### 3.2 Discrete I/O
- 8× Door position sensors (inputs)
- 4× Lock status switches (inputs)
- 2× Motor control (outputs)
- 2× Valve control (outputs)

### 3.3 Analog I/O
- 2× Temperature sensors
- 1× Position potentiometer
- 1× Current sensor

---

## 4. SOFTWARE INTERFACE

### 4.1 Application Software
- Name: Door Management Application (DMA)
- Version: 1.0.0
- DO-178C Level: Level C
- Update rate: 10 Hz

### 4.2 Data Exchange
- Internal bus: AFDX (Avionics Full-Duplex Switched Ethernet)
- Bandwidth: 10 Mbps allocated
- Latency: <50ms end-to-end
- Protocol: ARINC 664 Part 7

---

## 5. HEALTH MONITORING

### 5.1 Built-In Test (BIT)
- Continuous BIT: Sensor validation, communication checks
- Initiated BIT: Full functional test on command
- Fault reporting: Via ARINC 429 to CMC

### 5.2 Redundancy
- Dual power inputs (primary/backup)
- Software watchdog timer
- Fail-safe mode: Position reporting only

---

## 6. VERIFICATION

- [x] IMA partition configuration validated
- [x] ARINC 429 message sets tested
- [ ] DO-178C software qualification - in progress
- [ ] Integration testing - scheduled

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
