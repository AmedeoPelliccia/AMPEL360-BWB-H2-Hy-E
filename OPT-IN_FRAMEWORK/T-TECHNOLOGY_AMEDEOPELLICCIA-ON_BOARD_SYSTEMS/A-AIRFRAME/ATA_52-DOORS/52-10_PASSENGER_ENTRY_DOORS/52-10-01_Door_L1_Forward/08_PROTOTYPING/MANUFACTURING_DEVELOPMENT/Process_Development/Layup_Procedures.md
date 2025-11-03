# Composite Layup Procedure Development
## Door Panel Manufacturing

**Document:** MFG-DEV-LAYUP-001  
**Status:** Development  
**Date:** 2025-11-03

### 1. LAYUP SEQUENCE

#### Face Sheet (8 plies)
1. **Tool preparation**
   - Release agent application (Frekote 700-NC, 3 coats)
   - Temperature verification (23±2°C)
   - Humidity check (40-60% RH)
   
2. **Ply 1: 0° orientation**
   - Align to tool reference marks
   - Debulk 5 minutes vacuum (>26 inHg)
   - Photo documentation
   
3. **Ply 2: +45° orientation**
   - Template alignment
   - Overlap control: 3-6mm
   - Avoid wrinkles at edges
   
4. **ECF layer** (outer face only, between ply 1-2)
   - Expanded copper foil (lightning protection)
   - Electrical continuity check
   - Overlap: 25mm minimum
   
5. **Continue plies 3-8**
   - Follow stacking sequence: [0/+45/90/-45]s
   - Photo document each ply
   - Debulk every 2 plies (5 min vacuum)

### 2. CORE PLACEMENT

#### Preparation
- Core inspection (no crushing or damage)
- Adhesive film cutting (±5mm oversize)
- Alignment verification with templates

#### Installation  
- Place film adhesive on cured face sheet
- Position core (±2mm tolerance)
- Apply light pressure (no core crushing)
- Install edge bands (25mm width)

### 3. VACUUM BAGGING

**Layup (inside to outside):**
1. Peel ply (release fabric)
2. Breather cloth (2 layers)
3. Release film (perforated)
4. Vacuum bag (nylon 6)
5. Seal with tacky tape

**Leak check:**
- Full vacuum for 5 minutes
- Leak rate <10 mbar/min
- Fix any leaks before cure

### 4. CURE CYCLE

```
Stage 1: Adhesive gel
- Ramp: 2°C/min to 120°C
- Hold: 60 min at 120°C
- Vacuum only (no pressure)

Stage 2: Prepreg cure
- Ramp: 2°C/min to 180°C  
- Apply pressure: 7 bar at 150°C
- Hold: 120 min at 180°C

Stage 3: Cooldown
- Rate: 2°C/min maximum
- Release pressure: At 80°C
- Remove from autoclave: <60°C
```

**Total cycle time:** ~8 hours

### 5. QUALITY CHECKS

**During layup:**
- [ ] Ply orientation: ±1° (check with witness marks)
- [ ] No wrinkles or bridging
- [ ] Overlaps: 3-6mm
- [ ] Photo documentation: Each ply

**After cure:**
- [ ] Visual inspection (no surface defects)
- [ ] Dimensional check (±2mm)
- [ ] Ultrasonic C-scan (<5% voids)
- [ ] Weight verification (compare to prediction)

### 6. COMMON DEFECTS & PREVENTION

| Defect | Cause | Prevention |
|--------|-------|------------|
| Wrinkles | Excessive material, poor draping | Template use, careful placement |
| Bridging | Core not seated | Proper debulking, pressure |
| Voids | Entrapped air, volatiles | Vacuum integrity, slow ramp |
| Resin-rich areas | Excessive bleeding | Control bleed thickness |
| Delamination | Contamination | Clean room procedures |

### 7. PROCESS IMPROVEMENTS

**Phase 1 (Manual):**
- Hand layup with templates
- Skilled technicians required
- Variable quality
- 2-3 days per door

**Phase 2 (Semi-automated):**
- Laser projection for ply placement
- Automated debulking
- Better consistency
- 1-2 days per door

**Phase 3 (AFP):**
- Automated fiber placement
- CNC control
- Highest quality
- <1 day per door
- **Requires equipment investment**

---

**Document Control:** MFG-DEV-LAYUP-001  
**Revision:** A
