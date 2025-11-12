# Interface Control Document
## Door L1 Forward Slide Bustle Interface

**ICD Number:** ICD-52-85-001  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 52 (Evacuation Slide)

---

## 1. INTERFACE OVERVIEW

This ICD defines the interface between Door L1 Forward and the Type A evacuation slide/bustle assembly.

---

## 2. PHYSICAL INTERFACE

### 2.1 Bustle Mounting
- Location: Lower door frame, interior side
- Mounting points: 6× hard points
- Fasteners: NAS1352-08 (8 bolts)
- Load capacity: 200 kg static load

### 2.2 Bustle Dimensions
- Length: 1,200mm
- Width: 500mm
- Depth: 300mm (stowed)
- Weight: 45 kg (slide pack + bustle)

---

## 3. SLIDE SPECIFICATIONS

### 3.1 Slide Pack
- Type: Type A, single-lane
- Capacity: 110 persons per 90 seconds
- Inflation time: 6 seconds maximum
- Inflation system: Dual cylinder, CO₂/N₂ mix

### 3.2 Deployment
- Trigger: Door opening with slide armed
- Manual deployment: Pull handle override
- Disconnect: Manual release at door sill

---

## 4. ARMING SYSTEM

### 4.1 Arming Mechanism
- Type: Girt bar engagement
- Status indication: Mechanical flag (red/green)
- Electrical indication: 28 VDC signal to door controller
- Armed position: Girt bar secured to floor fitting

### 4.2 Disarming
- Method: Lift girt bar, rotate to stowed position
- Indication change: Green flag visible
- Electrical signal: Armed status cleared

---

## 5. ELECTRICAL INTERFACE

### 5.1 Arming Status Signal
- Signal: SLIDE_ARMED
- Type: Discrete, 28 VDC / Open
- Connector: Included in door signal connector (J2)
- Update: On status change

### 5.2 Inflation Monitoring (Optional)
- Sensor: Pressure switch in inflation line
- Signal: SLIDE_INFLATED (discrete)
- Purpose: Post-deployment verification

---

## 6. LOAD INTERFACE

### 6.1 Static Loads
- Slide pack weight: 45 kg
- Safety factor: 2.0 (design for 90 kg)
- Mounting bolt shear: 10 kN each

### 6.2 Dynamic Loads
- Deployment shock: 50g peak acceleration
- Inflation force: 15 kN outward
- Landing impact: Design per CS-25.807

---

## 7. CLEARANCES

### 7.1 Deployment Path
- Clear zone: 45° cone, 10-meter radius
- No obstructions: Fuselage features, ground equipment
- Wind limit: 25 knots for safe deployment

### 7.2 Stowage Clearance
- Bustle to seat: 150mm minimum
- Bustle to floor: Flush mount
- Access for inspection: Top panel removable

---

## 8. MAINTENANCE

### 8.1 Inspection Schedule
- Daily: Visual check, arming status
- Monthly: Detailed inspection, girt bar check
- Annual: Slide pack removal and inspection
- 6 years: Slide pack replacement

### 8.2 Service Access
- Bustle cover: Tool-free removal (4 quarter-turn fasteners)
- Slide pack: Requires 2 persons for removal
- Weight handling: Lifting fixture recommended

---

## 9. RESPONSIBILITIES

| Item | ATA 52 (Door) | ATA 52 (Slide) |
|------|---------------|----------------|
| Mounting hard points | Provide | - |
| Bustle assembly | - | Provide & install |
| Slide pack | - | Provide & install |
| Arming mechanism | Interface | Provide |
| Electrical signal | Interface | Provide sensor |
| Inspection | Support | Responsible |

---

## 10. VERIFICATION

- [x] Static load test (90 kg @ 2.0 SF)
- [x] Deployment test (functional)
- [x] Arming system test
- [x] Electrical signal validation
- [ ] Certification witness test - scheduled

---

## 11. CERTIFICATION

### 11.1 Applicable Requirements
- CS-25.807: Emergency exits
- CS-25.809: Emergency exit arrangements
- CS-25.810: Emergency egress assist
- CS-25.812: Emergency lighting

### 11.2 Test Evidence
- Deployment time: <6 seconds (tested)
- Evacuation rate: 110 persons / 90 seconds (certified)
- Inflation reliability: >99.5% (fleet data)

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
