# Interface Control Document
## Door L1 Forward Fire Detection Interface

**ICD Number:** ICD-52-26-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 26 (Fire Protection)

---

## 1. INTERFACE OVERVIEW

This ICD defines the fire detection and protection interface for Door L1 Forward and surrounding areas.

---

## 2. FIRE ZONE CLASSIFICATION

### 2.1 Door Area Fire Zones
- Zone designation: Class D (designated fire zone)
- Fire detection: Required per CS-25.858
- Detection type: Smoke detection in cabin
- Response time: <60 seconds detection to alert

### 2.2 Fire Barriers
- Door structure: Fire-resistant materials
- Interior panels: FAR 25.853 compliant
- Seal materials: Self-extinguishing
- Wiring insulation: Fire-resistant per AS50881

---

## 3. FIRE DETECTION SYSTEM

### 3.1 Smoke Detectors
- Location: Ceiling near door, cabin side
- Type: Photoelectric or ionization
- Quantity: 1 detector within 3 meters
- Power: 28 VDC from emergency bus
- Signal: Discrete to fire detection system

### 3.2 Detection Coverage
- Coverage area: Door vestibule and adjacent cabin
- Detector spacing: Per NFPA 72 guidelines
- Redundancy: Part of cabin smoke detection system
- Testing: Monthly functional test per MEL

---

## 4. FIRE SUPPRESSION

### 4.1 Portable Extinguishers
- Location: Adjacent to door (bulkhead mounted)
- Type: Halon 1211 or approved alternative
- Capacity: 1.4 kg minimum
- Accessibility: <10 seconds from any cabin seat

### 4.2 Automatic Suppression
- Fixed system: Not required for door area
- Portable only: Manual fire fighting by crew
- Evacuation: Primary response to cabin fire

---

## 5. MATERIALS FLAMMABILITY

### 5.1 Door Materials Compliance
- Interior panels: Pass vertical burn test
- Seat cushions (if applicable): Pass oil burner test  
- Carpeting: Class I flame spread
- Insulation: Non-combustible or self-extinguishing

### 5.2 Test Standards
- FAR 25.853: Compartment interiors
- FAR 25.855: Cargo/baggage compartments
- FAR 25.856: Thermal/acoustic insulation
- OSU 65/65: Heat release test

---

## 6. ELECTRICAL FIRE PREVENTION

### 6.1 Wiring Protection
- Wire insulation: AS50881 (fire-resistant)
- Circuit protection: Breakers and fuses
- Arc fault detection: In door control circuits
- Overtemperature: Motor thermal cutout

### 6.2 Fault Protection
- Short circuit: Immediate breaker trip
- Overload: Thermal protection
- Ground fault: Detection and isolation
- Smoke: Detector in door controller area

---

## 7. EMERGENCY EGRESS

### 7.1 Fire Emergency Egress
- Door operation: Manual override if fire
- Emergency lighting: Activated automatically
- Slide deployment: Available if door area clear
- Alternate exits: Per emergency evacuation plan

### 7.2 Crew Procedures
- Fire detected: Evacuation decision by captain
- Door assessment: Check door area before use
- Passenger briefing: Emergency exit procedures
- Coordination: Cabin crew communication

---

## 8. INTERFACE SIGNALS

### 8.1 Fire Detection System Inputs
- Smoke detector: Discrete signal to FDS
- Temperature sensors: Analog signal (if installed)
- Fire extinguisher discharge: Discrete signal
- Door status: Position signal to FDS

### 8.2 Fire Detection System Outputs
- Fire warning: Flight deck bell and light
- Cabin alert: Public address announcement
- Emergency lighting: Automatic activation
- Door unlocking: Automatic (some systems)

---

## 9. VERIFICATION

- [ ] Fire detection system functional test
- [ ] Material flammability certification
- [ ] Emergency egress demonstration
- [ ] Crew training procedures review

---

## 10. RESPONSIBILITIES

| Item | ATA 52 (Door) | ATA 26 (Fire Protection) |
|------|---------------|--------------------------|
| Fire-resistant materials | Provide | Certify compliance |
| Smoke detectors | Mounting provision | Provide & install |
| Fire extinguishers | Mounting bracket | Provide equipment |
| Emergency lighting | Integrate | Provide signals |
| Testing | Support | Responsible |

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | TBD | Initial draft |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
