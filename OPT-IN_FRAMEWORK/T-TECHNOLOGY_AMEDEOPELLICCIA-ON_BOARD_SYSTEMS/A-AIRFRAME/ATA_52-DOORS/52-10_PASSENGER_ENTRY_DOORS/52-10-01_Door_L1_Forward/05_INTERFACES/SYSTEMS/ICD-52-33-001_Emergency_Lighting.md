# Interface Control Document
## Door L1 Forward Emergency Lighting Interface

**ICD Number:** ICD-52-33-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 33 (Lighting)

---

## 1. INTERFACE OVERVIEW

This ICD defines the interface between Door L1 Forward and emergency lighting systems including exit signs and floor proximity lighting.

---

## 2. EXIT SIGN LIGHTING

### 2.1 Door Exit Sign
- Type: LED exit sign, internally illuminated
- Power: 28 VDC emergency bus
- Current: 0.3A continuous
- Brightness: 100 cd/m² minimum
- Location: Above door on interior side
- Battery backup: 30 minutes minimum

### 2.2 Sign Specifications
- Display: "EXIT" in English + pictogram
- Size: 300mm × 150mm
- Visibility: 30 meters in clear air
- Color: Green (emergency exit)

---

## 3. FLOOR PROXIMITY LIGHTING

### 3.1 Floor Path Lights
- Type: LED strips along cabin floor
- Spacing: 40cm intervals
- Power: Emergency lighting bus
- Activation: Automatic on emergency or low cabin lighting
- Color: White/green, photoluminescent backup

### 3.2 Door Threshold Lighting
- Location: Door sill area
- Type: LED strip, 1000mm length
- Brightness: 50 lux at floor level
- Activation: When door opens

---

## 4. ELECTRICAL INTERFACE

### 4.1 Power Connection
- Connector: MS3057-4S (4-pin)
- Location: Door frame upper left
- Voltage: 28 VDC ±4V
- Circuit protection: 5A circuit breaker

### 4.2 Control Signals
- Emergency activation: Discrete input from emergency system
- Dimming control: 0-10 VDC analog (optional)
- Fault monitoring: Open collector output

---

## 5. VERIFICATION

- [x] Photometric testing completed
- [x] Emergency power duration verified
- [ ] Integration with emergency system - testing
- [ ] Certification compliance review - pending

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
