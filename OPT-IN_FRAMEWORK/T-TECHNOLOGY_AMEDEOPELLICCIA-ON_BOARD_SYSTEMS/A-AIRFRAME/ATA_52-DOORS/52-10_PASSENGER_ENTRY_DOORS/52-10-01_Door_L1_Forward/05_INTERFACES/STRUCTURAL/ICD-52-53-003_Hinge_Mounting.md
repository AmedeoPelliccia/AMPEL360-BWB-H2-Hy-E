# Interface Control Document
## Door L1 Forward Hinge Mounting

**ICD Number:** ICD-52-53-003  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 53 (Fuselage)

---

## 1. INTERFACE OVERVIEW

### 1.1 Purpose
This ICD defines the hinge mounting interface between Door L1 Forward and the fuselage structure.

### 1.2 Scope
- Three hinge locations along forward edge
- Hinge pin and bearing interface
- Mounting bolt patterns
- Load transfer through hinges

---

## 2. PHYSICAL INTERFACE

### 2.1 Hinge Locations (Fuselage Coordinates)

| Hinge | Station (X) | Waterline (Z) | Buttline (Y) |
|-------|-------------|---------------|--------------|
| Upper | FS 102 | WL 360 | BL -560 |
| Middle | FS 105 | WL 250 | BL -560 |
| Lower | FS 108 | WL 140 | BL -560 |

### 2.2 Hinge Dimensions
- Pin diameter: 25mm (±0.02mm)
- Pin length: 150mm
- Bearing length: 120mm
- Mounting bolt pattern: 4 × M12 per hinge half

### 2.3 Mounting Bolt Specifications
- Bolt: NAS6604-12A (M12, A286 steel)
- Torque: 95 N⋅m (±10%)
- Washer: NAS1149F12
- Lock: NAS679C-12 (castellated nut with cotter pin)

---

## 3. LOAD TRANSFER

### 3.1 Operating Loads per Hinge
- Vertical load: 15 kN
- Fore-aft load: 2 kN
- Lateral load: 5 kN
- Moment: 2.5 kN⋅m

### 3.2 Ultimate Loads per Hinge
- Vertical load: 30 kN
- Fore-aft load: 4 kN
- Lateral load: 10 kN
- Safety factor: 2.0

### 3.3 Load Distribution
- Upper hinge: 35% of total vertical load
- Middle hinge: 35% of total vertical load
- Lower hinge: 30% of total vertical load

---

## 4. MATERIALS

### 4.1 Hinge Components

| Component | Material | Specification | Coating |
|-----------|----------|---------------|---------|
| Hinge pin | Ti-6Al-4V | AMS 4928 | Cadmium plate |
| Hinge bracket (door) | Ti-6Al-4V | AMS 4928 | Anodize |
| Hinge bracket (fuselage) | 17-4PH SS | AMS 5643 | Passivate |
| Bearing bushing | Bronze | SAE 660 | As cast |

### 4.2 Lubrication
- Dry film lubricant: MoS₂ per MIL-L-23398
- Application: Pin and bearing surfaces
- Re-lubrication: Every 2,000 flight hours

---

## 5. TOLERANCES

### 5.1 Critical Tolerances
- Pin diameter: 25.00mm (+0.00/-0.02)
- Bearing bore: 25.05mm (+0.03/+0.01) [H7 fit]
- Pin-to-bracket alignment: ±0.5mm
- Mounting hole position: ±0.3mm

### 5.2 Surface Finish
- Pin surface: Ra 0.8μm
- Bearing surface: Ra 1.6μm
- Mounting face: Ra 3.2μm

---

## 6. RESPONSIBILITIES

| Item | ATA 52 (Door) | ATA 53 (Fuselage) |
|------|---------------|-------------------|
| Hinge pin | Provide & install | - |
| Door hinge bracket | Provide & install | - |
| Fuselage hinge bracket | - | Provide & install |
| Bearing bushings | Install | Provide |
| Mounting bolts | Install | Provide |
| Alignment check | Responsible | Support |

---

## 7. VERIFICATION

### 7.1 Verification Methods
- [x] Dimensional inspection (CMM)
- [x] Fit check (hinge swing test)
- [x] Static load test to ultimate
- [x] Fatigue test (120,000 cycles)
- [ ] Corrosion testing (in progress)

### 7.2 Acceptance Criteria
- Smooth operation through full swing (0° to 180°)
- No binding or interference
- Ultimate load: 2× operating load, no permanent deformation
- Fatigue life: >120,000 cycles (4× design life)
- Pin wear: <0.1mm after fatigue test

---

## 8. MAINTENANCE

### 8.1 Inspection Schedule
- Pre-flight: Visual check for damage
- Daily: Lubrication check
- 500 FH: Detailed visual inspection
- 2,000 FH: Pin wear measurement
- 8,000 FH: Bearing replacement

### 8.2 Wear Limits
- Pin diameter: 24.80mm (replace if below)
- Bearing bore: 25.20mm (replace if above)
- Bushing wear: 0.15mm max radial clearance

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
