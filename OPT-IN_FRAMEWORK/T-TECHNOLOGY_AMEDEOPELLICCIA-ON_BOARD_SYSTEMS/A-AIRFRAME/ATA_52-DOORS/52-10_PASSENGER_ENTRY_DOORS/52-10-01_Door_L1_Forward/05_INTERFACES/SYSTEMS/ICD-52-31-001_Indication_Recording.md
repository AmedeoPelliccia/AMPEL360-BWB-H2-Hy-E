# Interface Control Document
## Door L1 Forward Indication and Recording Interface

**ICD Number:** ICD-52-31-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 31 (Indicating/Recording Systems)

---

## 1. INTERFACE OVERVIEW

This ICD defines the interface between Door L1 Forward and aircraft indication/recording systems including flight deck displays and maintenance data recording.

---

## 2. FLIGHT DECK INDICATIONS

### 2.1 Door Status Display
- Location: EICAS (Engine Indicating and Crew Alerting System)
- Indications:
  - Door unlocked (amber advisory)
  - Door open (red warning)
  - Door not fully closed/latched (amber caution)
  - Slide armed (green status)
  
### 2.2 Warning Lights
- Master warning: Door open in flight
- Master caution: Door unlocked
- Advisory: Seal pressure low

---

## 3. ARINC 429 DATA OUTPUT

### 3.1 Door Status Word (Label 250 octal)
- Bit 11-12: Door position (00=closed, 01=transit, 10=open, 11=fault)
- Bit 13: Lock status (0=unlocked, 1=locked)
- Bit 14: Slide armed (0=disarmed, 1=armed)
- Bit 15-18: Position (0-15, 0=closed, 15=full open)
- Bit 19-22: Fault codes
- Word rate: 2 Hz continuous, 10 Hz during operation

### 3.2 Maintenance Data
- Cycle counter (累積開閉回数)
- Fault history (last 100 events)
- Temperature exceedances
- Power consumption trends

---

## 4. CENTRAL MAINTENANCE COMPUTER (CMC)

### 4.1 Recorded Parameters
- Door operations count
- Fault codes with timestamp
- Lock/unlock cycles
- Motor current profile
- Temperature excursions
- Abnormal operation detection

### 4.2 Data Rate
- Normal: 1 Hz to CMC
- Event-triggered: Immediate fault logging

---

## 5. VERIFICATION

- [x] EICAS display format approved
- [x] ARINC 429 message validated
- [ ] CMC interface testing - in progress
- [ ] Flight test validation - scheduled

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
