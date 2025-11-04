# Interface Control Document
## Door L1 Forward ARINC 429 Bus Interface

**ICD Number:** ICD-52-23-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 23 (Communications)

---

## 1. INTERFACE OVERVIEW

This ICD defines the ARINC 429 data bus interface for Door L1 Forward status and control communication.

---

## 2. BUS CONFIGURATION

### 2.1 Physical Interface
- Bus type: ARINC 429 High Speed
- Bit rate: 100 kbps
- Wire: Twisted pair, shielded
- Connector: ARINC 600 compatible

### 2.2 Bus Assignment
- TX Bus 1: Door status to Flight Deck (EICAS)
- TX Bus 2: Maintenance data to CMC
- RX Bus 1: Commands from Flight Deck

---

## 3. MESSAGE DEFINITIONS

### 3.1 Door Status Message (Label 250 octal)

| Bit | Field | Values | Description |
|-----|-------|--------|-------------|
| 29-30 | SSM | 00=NCD, 01=FT, 10=NO, 11=FW | Sign/Status Matrix |
| 11-12 | Door Position | 00=Closed, 01=Transit, 10=Open, 11=Fault | Position state |
| 13 | Locked | 0=Unlocked, 1=Locked | Lock status |
| 14 | Slide Armed | 0=Disarmed, 1=Armed | Evacuation slide |
| 15-18 | Position Value | 0-15 | Analog position (0=closed, 15=full open) |
| 19-22 | Fault Code | 0-15 | Fault identifier |
| 23-28 | Reserved | - | Future use |

**Update Rate:** 2 Hz continuous, 10 Hz during operation

### 3.2 Command Message (Label 251 octal)

| Bit | Field | Values | Description |
|-----|-------|--------|-------------|
| 11 | Open Command | 0=No, 1=Open | Command door open |
| 12 | Close Command | 0=No, 1=Close | Command door close |
| 13 | Lock Command | 0=No, 1=Lock | Command locks engage |
| 14 | Unlock Command | 0=No, 1=Unlock | Command locks release |
| 15 | Seal Inflate | 0=No, 1=Inflate | Inflate seal |
| 16 | Seal Deflate | 0=No, 1=Deflate | Deflate seal |
| 17-28 | Reserved | - | Future use |

**Update Rate:** Event-triggered (on command change)

### 3.3 Maintenance Data (Label 252 octal)

| Bit | Field | Values | Description |
|-----|-------|--------|-------------|
| 11-20 | Cycle Count | 0-1023 | Operations count (×10) |
| 21-24 | Max Temp | 0-15 | Highest temp recorded (×10°C) |
| 25-28 | Fault Count | 0-15 | Number of faults |

**Update Rate:** 1 Hz continuous

---

## 4. DATA ENCODING

### 4.1 Binary Encoding
- MSB: Bit 29 (sign bit for BNR)
- LSB: Bit 11
- BCD: Used for cycle count
- Discrete: Single bit flags

### 4.2 Parity
- Bit 32: Odd parity
- Calculated over bits 1-31

### 4.3 SSM (Sign/Status Matrix)
- 00: No Computed Data (NCD)
- 01: Functional Test (FT)
- 10: Normal Operation (NO)
- 11: Failure Warning (FW)

---

## 5. FAULT CODES

| Code | Description | Action |
|------|-------------|--------|
| 0 | No fault | Normal |
| 1 | Motor overcurrent | Check motor |
| 2 | Position sensor fault | Check sensor |
| 3 | Lock malfunction | Check locks |
| 4 | Seal pressure low | Check pneumatic |
| 5 | Controller fault | Reset controller |
| 6 | Communication loss | Check wiring |
| 7 | Overtemperature | Allow cooling |
| 8-15 | Reserved | - |

---

## 6. TIMING

### 6.1 Response Times
- Command to acknowledgment: <100ms
- Door operation feedback: <50ms update
- Fault detection to indication: <200ms

### 6.2 Message Priority
- High: Fault warnings (immediate)
- Medium: Status updates (scheduled)
- Low: Maintenance data (background)

---

## 7. VERIFICATION

- [x] Message format validation
- [x] Timing analysis completed
- [x] Bit error rate testing passed
- [ ] System integration test - in progress

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
