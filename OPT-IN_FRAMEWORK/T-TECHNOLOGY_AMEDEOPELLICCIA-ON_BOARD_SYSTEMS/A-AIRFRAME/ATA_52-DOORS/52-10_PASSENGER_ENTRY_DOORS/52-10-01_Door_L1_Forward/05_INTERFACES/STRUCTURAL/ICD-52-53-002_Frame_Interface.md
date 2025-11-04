# Interface Control Document
## Door L1 Forward Frame Interface

**ICD Number:** ICD-52-53-002  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 53 (Fuselage Frame)

---

## 1. INTERFACE OVERVIEW

### 1.1 Purpose
This ICD defines the interface between Door L1 Forward and the fuselage frame structure at Frames 100, 105, and 110.

### 1.2 Scope
- Frame reinforcement requirements
- Shear tie connections
- Load distribution from door to frame
- Access cutouts in frames

---

## 2. PHYSICAL INTERFACE

### 2.1 Frame Locations
- Frame 100: Forward edge of door opening
- Frame 105: Mid-door support
- Frame 110: Aft edge of door opening

### 2.2 Frame Reinforcement
- Frame cap increase: 50% section modulus at door opening
- Web doubler: 3mm thickness, 200mm height
- Material: 7075-T6 aluminum alloy

### 2.3 Shear Tie Locations

| Frame | Shear Ties | Fasteners | Load Capacity |
|-------|------------|-----------|---------------|
| Frame 100 | 4 | NAS1352 | 8 kN each |
| Frame 105 | 6 | NAS1352 | 8 kN each |
| Frame 110 | 4 | NAS1352 | 8 kN each |

---

## 3. LOAD TRANSFER

### 3.1 Frame Loads
- Vertical shear: 35 kN per frame
- Circumferential tension: 20 kN per frame
- Moment: 10 kN⋅m per frame

### 3.2 Load Path
Door loads → Frame doublers → Frames → Longitudinal stringers

---

## 4. MATERIALS

| Component | Material | Specification |
|-----------|----------|--------------|
| Frame caps | Al 7075-T6 | AMS-QQ-A-250/12 |
| Web doublers | Al 7075-T6 | AMS-QQ-A-250/12 |
| Shear ties | Al 2024-T4 | AMS-QQ-A-250/4 |

---

## 5. VERIFICATION

- [x] FEM analysis of frame with door loads
- [x] Static test of frame assembly
- [ ] Fatigue test (scheduled Q2 2026)

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
