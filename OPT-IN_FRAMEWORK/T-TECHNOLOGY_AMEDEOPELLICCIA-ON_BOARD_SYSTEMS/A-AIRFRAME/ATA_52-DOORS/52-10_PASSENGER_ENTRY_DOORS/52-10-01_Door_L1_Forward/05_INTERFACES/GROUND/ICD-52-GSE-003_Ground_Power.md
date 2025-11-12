# Interface Control Document
## Door L1 Forward Ground Power Interface

**ICD Number:** ICD-52-GSE-003  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ GSE (Ground Power Unit)

---

## 1. INTERFACE OVERVIEW

This ICD defines the ground power interface for Door L1 Forward testing and operation during ground servicing.

---

## 2. GROUND POWER CONNECTION

### 2.1 Aircraft Ground Power
- Connection point: External power receptacle (ATA 24)
- Voltage: 28 VDC or 115 VAC 400 Hz
- Door system powered: Via aircraft distribution
- No direct GSE connection: Door uses aircraft power

### 2.2 Power Requirements for Door Testing
- Voltage: 28 VDC ±4V
- Current: 35A maximum (door operation)
- Duration: 15-20 seconds per cycle
- Test cycles: Up to 10 consecutive operations

---

## 3. GROUND TEST PROCEDURES

### 3.1 Pre-Flight Door Test
1. Connect GPU to aircraft
2. Verify 28 VDC bus powered
3. Flight deck door control: Test open/close cycle
4. Verify position indication
5. Verify lock engagement
6. Disconnect GPU or start APU

### 3.2 Maintenance Testing
- Extended testing: GPU connection for troubleshooting
- Powered ground testing: Full functional test capability
- Load testing: GPU must supply full 35A load

---

## 4. SAFETY REQUIREMENTS

### 4.1 Ground Operations Safety
- Chocks installed: Before door operations
- Ground crew present: During power-on tests
- Slide disarmed: Verified before door test
- Clear zone: Personnel clear of door swing

### 4.2 Power Quality
- Voltage regulation: ±4V maximum deviation
- Transient suppression: GPU must have protection
- Ground fault protection: Per aircraft requirements

---

## 5. VERIFICATION

- [x] Ground test procedures documented
- [x] GPU power quality verified
- [ ] Maintenance manual updated
- [ ] Training completed

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | TBD | Initial draft |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
