# Interface Control Document
## Door L1 Forward Seal Interface

**ICD Number:** ICD-52-53-005  
**Issue:** 1.0  
**Date:** 2025-11-03  
**Systems:** ATA 52 (Doors) ↔ ATA 53 (Fuselage)

---

## 1. INTERFACE OVERVIEW

### 1.1 Purpose
This ICD defines the sealing interface between Door L1 Forward and fuselage structure to maintain cabin pressure and environmental protection.

### 1.2 Scope
- Primary inflatable seal system
- Secondary blade seal backup
- Seal groove geometry and surface finish
- EMI/EMC bonding seal
- Drainage system integration

---

## 2. PHYSICAL INTERFACE

### 2.1 Primary Seal System
- Type: Inflatable silicone pressure seal
- Cross-section (relaxed): 50mm × 25mm
- Cross-section (compressed): 45mm × 15mm
- Perimeter length: 5,840mm
- Inflation pressure: 15 psi nominal (10-20 psi range)
- Material: Silicone elastomer per AMS3325

### 2.2 Seal Groove (Fuselage Side)
- Width: 52mm (+1.0/-0.5mm)
- Depth: 28mm (±0.5mm)
- Surface finish: Ra 3.2μm maximum
- Corner radii: 2mm minimum (no sharp edges)
- Groove location: 20mm inboard from door opening edge

### 2.3 Seal Compression Surface (Door Side)
- Contact width: 40mm minimum
- Flatness: 1.0mm over 300mm span
- Surface finish: Ra 6.3μm maximum
- Material: Anodized aluminum

---

## 3. SEALING PERFORMANCE

### 3.1 Leak Rate Requirements
- Maximum leak rate: 0.05 CFM @ 8.5 psi differential
- Test pressure: 8.5 psi (operating pressure)
- Test method: Pressure decay per AS25.783

### 3.2 Pressure Range
- Operating differential: 8.5 psi typical
- Maximum differential: 9.1 psi
- Proof test: 10.2 psi (1.2× max operating)

### 3.3 Seal Life
- Design life: 30,000 flight cycles
- Inspection interval: 8,000 flight hours
- Replacement interval: 16,000 flight hours or condition

---

## 4. SECONDARY SEAL SYSTEM

### 4.1 Blade Seal Specifications
- Type: Flexible rubber blade seal
- Material: EPDM rubber per AMS-R-6855
- Thickness: 3mm
- Width: 25mm
- Function: Backup for primary seal, environmental protection

### 4.2 Installation
- Location: Outboard of primary seal
- Attachment: Adhesive bonded to door frame
- Adhesive: PR-1422 Class B sealant
- Interference: 5mm minimum when door closed

---

## 5. MATERIALS

### 5.1 Seal Materials

| Component | Material | Specification | Properties |
|-----------|----------|---------------|------------|
| Primary seal | Silicone | AMS3325 | Temp: -65°F to +400°F |
| Blade seal | EPDM | AMS-R-6855 | Weather resistant |
| EMI seal | Conductive silicone | MIL-G-83528 | <2.5 mΩ bonding |
| Adhesive | Polysulfide | PR-1422 Class B | Fuel resistant |

### 5.2 Compatibility
- Fluids: Compatible with Skydrol, fuel, deicing fluid
- UV resistance: 5,000 hours no degradation
- Ozone resistance: Per ASTM D1149

---

## 6. EMI/LIGHTNING PROTECTION

### 6.1 Conductive Seal
- Type: Silicone with conductive filler
- Location: Perimeter bonding strip
- Width: 10mm
- Bonding resistance: <2.5 mΩ per MIL-B-5087

### 6.2 Lightning Protection
- Level: Level 1 (direct strike)
- Current path: Through conductive seal to fuselage
- Test: Per DO-160G Section 23
- Bonding straps: 4 locations, 0.5 AWG

---

## 7. DRAINAGE SYSTEM

### 7.1 Drain Paths
- Number of drains: 4 (one per corner)
- Drain tube size: 12mm ID
- Drain location: Bottom of seal groove
- Discharge: Overboard through fuselage

### 7.2 Drain Performance
- Flow rate: >50 ml/min at 0° pitch
- No pooling in seal groove
- Freeze protection: Drain tube heated (optional)

---

## 8. TOLERANCES

### 8.1 Groove Tolerances
- Width: 52mm (+1.0/-0.5)
- Depth: 28mm (±0.5)
- Straightness: 2mm over 1000mm
- Surface waviness: 0.5mm max

### 8.2 Seal Compression
- Nominal compression: 40% (10mm)
- Minimum compression: 30% (7.5mm)
- Maximum compression: 50% (12.5mm)

---

## 9. RESPONSIBILITIES

| Item | ATA 52 (Door) | ATA 53 (Fuselage) |
|------|---------------|-------------------|
| Primary seal | Provide & install | - |
| Seal groove | - | Provide machined groove |
| Blade seal | Provide & install | - |
| EMI seal | Provide & install | - |
| Inflation system | Provide & install | - |
| Drain system | Install drain tubes | Provide drain paths |

---

## 10. VERIFICATION

### 10.1 Verification Methods
- [x] Dimensional inspection
- [x] Surface finish measurement
- [x] Leak test @ 8.5 psi
- [x] Compression uniformity check
- [ ] Durability test (30,000 cycles) - in progress
- [ ] Environmental aging test - scheduled

### 10.2 Acceptance Criteria
- Leak rate: <0.05 CFM @ 8.5 psi
- Compression: 30-50% across entire perimeter
- No local gaps >1mm
- Seal inflation: Even distribution, no bulges
- Bonding resistance: <2.5 mΩ

---

## 11. MAINTENANCE

### 11.1 Inspection Schedule
- Pre-flight: Visual check for damage
- Daily: Check for leaks (soap test if needed)
- 500 FH: Detailed visual inspection
- 2,000 FH: Seal compression check
- 8,000 FH: Major inspection, measure wear
- 16,000 FH: Seal replacement

### 11.2 Repair Procedures
- Minor cuts (<10mm): Field repair with patch kit
- Major damage: Replace seal segment (spliced)
- Leak repairs: Temporary only, permanent fix at base
- Re-rigging: After any seal replacement

---

## REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-03 | A. Pelliccia | Initial release |

---

*This ICD is part of the AMPEL360 OPT-IN Framework interface documentation.*
