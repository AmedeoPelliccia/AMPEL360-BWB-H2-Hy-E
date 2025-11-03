# Interface Control Document
## Door L1 Forward Latch Fittings

**ICD Number:** ICD-52-53-004  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 53 (Fuselage)

---

## 1. INTERFACE OVERVIEW

### 1.1 Purpose
This ICD defines the latch fitting interface between Door L1 Forward latches and fuselage strike plates.

### 1.2 Scope
- Eight latch locations around door perimeter
- Latch roller and strike plate interface
- Mounting provisions for both sides
- Emergency release mechanism integration

---

## 2. PHYSICAL INTERFACE

### 2.1 Latch Locations

| Latch ID | Location | Station | Waterline | Load (kN) |
|----------|----------|---------|-----------|-----------|
| L1-TOP-1 | Top-Left | FS 101 | WL 365 | 30 |
| L1-TOP-2 | Top-Center | FS 105 | WL 370 | 30 |
| L1-TOP-3 | Top-Right | FS 109 | WL 365 | 30 |
| L1-FWD | Forward-Center | FS 100 | WL 250 | 30 |
| L1-AFT | Aft-Center | FS 110 | WL 250 | 30 |
| L1-BTM-1 | Bottom-Left | FS 101 | WL 135 | 30 |
| L1-BTM-2 | Bottom-Center | FS 105 | WL 130 | 30 |
| L1-BTM-3 | Bottom-Right | FS 109 | WL 135 | 30 |

### 2.2 Strike Plate Dimensions
- Length: 120mm
- Width: 60mm
- Thickness: 12mm
- Roller engagement: 25mm depth
- Surface finish: Ra 1.6μm

### 2.3 Latch Roller
- Diameter: 20mm (±0.05mm)
- Width: 25mm
- Material: 17-4PH stainless steel
- Coating: Hard chrome, 0.05mm thickness

---

## 3. LOAD TRANSFER

### 3.1 Operating Loads per Latch
- Radial load: 10 kN (pressure differential)
- Tangential load: 2 kN (door operation)
- Combined safety factor: 1.5

### 3.2 Ultimate Loads per Latch
- Radial load: 20 kN
- Tangential load: 4 kN
- Safety factor: 2.0

### 3.3 Load Distribution
- Total perimeter load: 240 kN
- Load per latch: 30 kN average
- Load variation: ±15% based on location

---

## 4. MATERIALS

### 4.1 Component Materials

| Component | Material | Specification | Treatment |
|-----------|----------|---------------|-----------|
| Latch body | 17-4PH SS | AMS 5643 | H1150 |
| Strike plate | 17-4PH SS | AMS 5643 | H1150 |
| Roller | 17-4PH SS | AMS 5643 | Hard chrome |
| Mounting bolts | A286 SS | NAS6206 | Aged |
| Locking pins | 4340 Steel | AMS 6414 | Heat treat |

### 4.2 Protective Coatings
- Strike plates: Passivate per AMS-QQ-P-35
- Latch bodies: Cadmium plate per QQ-P-416 (Type II)
- Roller: Hard chrome per AMS-QQ-C-320

---

## 5. TOLERANCES

### 5.1 Critical Dimensions
- Strike plate position: ±0.5mm
- Roller diameter: 20.00mm (+0.00/-0.05)
- Engagement depth: 25.0mm (±0.5)
- Strike plate flatness: 0.2mm max

### 5.2 Alignment
- Centerline alignment: ±1.0mm
- Angular alignment: ±0.3°
- Parallelism: 0.5mm over length

---

## 6. OPERATION

### 6.1 Normal Operation
1. Handle rotation: 90° from neutral to full open
2. Latch cam movement: 30mm radial displacement
3. Roller engagement: 15mm minimum contact
4. Locking: Automatic when handle in neutral

### 6.2 Emergency Operation
- Manual override: Accessible from both sides
- Emergency release force: <150N
- Pneumatic assist: Optional (ICD-52-36-001)

---

## 7. RESPONSIBILITIES

| Item | ATA 52 (Door) | ATA 53 (Fuselage) |
|------|---------------|-------------------|
| Latch mechanism | Provide & install | - |
| Strike plates | - | Provide & install |
| Mounting holes (door) | Provide | - |
| Mounting holes (fuselage) | - | Provide |
| Rigging & adjustment | Responsible | Support |
| Functional test | Responsible | Witness |

---

## 8. VERIFICATION

### 8.1 Verification Methods
- [x] Dimensional inspection
- [x] Functional test (1,000 cycles)
- [x] Ultimate load test (40 kN per latch)
- [x] Fatigue test (60,000 cycles)
- [ ] Environmental test (pending)

### 8.2 Acceptance Criteria
- Smooth operation: <100N operating force
- Engagement: 15mm minimum roller contact
- Ultimate test: 2× operating load, no failure
- Fatigue: 60,000 cycles with no crack initiation
- Wear: <0.1mm after functional cycling

---

## 9. MAINTENANCE

### 9.1 Inspection Schedule
- Pre-flight: Visual check
- 100 FH: Lubrication
- 1,000 FH: Detailed inspection
- 4,000 FH: Wear measurement
- 12,000 FH: Replace wear items

### 9.2 Adjustment Procedures
- Engagement check: Minimum 15mm contact
- Force check: 50-100N handle force
- Lock check: Positive lock engagement
- Tolerance: ±2mm adjustment range available

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
