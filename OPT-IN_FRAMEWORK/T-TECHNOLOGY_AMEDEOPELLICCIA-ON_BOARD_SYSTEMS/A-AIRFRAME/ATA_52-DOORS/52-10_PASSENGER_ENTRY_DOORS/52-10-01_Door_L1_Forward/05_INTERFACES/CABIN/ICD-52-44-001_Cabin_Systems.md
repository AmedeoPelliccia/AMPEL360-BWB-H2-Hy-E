# Interface Control Document
## Door L1 Forward Cabin Systems Interface

**ICD Number:** ICD-52-44-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 44 (Cabin Systems)

---

## 1. INTERFACE OVERVIEW

This ICD defines the interface between Door L1 Forward and cabin systems including cabin management, passenger address, and attendant call.

---

## 2. CABIN MANAGEMENT SYSTEM

### 2.1 Door Status Display
- Location: Flight attendant panel near door
- Display: LCD, 3-line text
- Information: Door status, lock status, slide armed
- Update rate: 2 Hz

### 2.2 Control Panel
- Type: Touch screen, 5" diagonal
- Functions: Door control, status monitoring
- Power: 28 VDC, 0.5A
- Communication: Ethernet to cabin management system

---

## 3. PASSENGER ADDRESS SYSTEM

### 3.1 Speaker Location
- Location: Above door opening, interior side
- Type: 8-ohm, 10W speaker
- Coverage: Door vestibule area
- Mounting: Bracket to door frame

### 3.2 Audio Interface
- Input: Cabin PA system, line level
- Connector: 3-pin XLR
- Impedance: 600 ohms
- Volume: Controlled by cabin system

---

## 4. ATTENDANT CALL SYSTEM

### 4.1 Call Button
- Location: Door interior panel
- Type: Illuminated push button
- Function: Call flight attendant
- Indication: Amber LED when pressed

### 4.2 Chime Integration
- Activation: Button press
- Output: Tone to cabin speakers
- Duration: 2 seconds

---

## 5. LIGHTING INTEGRATION

### 5.1 Area Lighting
- Type: LED downlights, 3× fixtures
- Location: Door ceiling area
- Control: Cabin lighting system
- Dimming: 0-100% via cabin controller

---

## 6. RESPONSIBILITIES

| Item | ATA 52 (Door) | ATA 44 (Cabin Systems) |
|------|---------------|------------------------|
| Door status signals | Provide | - |
| Control panel | Install | Provide |
| Wiring (cabin side) | - | Provide & install |
| Integration test | Support | Responsible |

---

## 7. VERIFICATION

- [ ] Cabin management display test
- [ ] PA system audio quality check
- [ ] Attendant call functional test
- [ ] Lighting control validation

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | TBD | Initial draft |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
