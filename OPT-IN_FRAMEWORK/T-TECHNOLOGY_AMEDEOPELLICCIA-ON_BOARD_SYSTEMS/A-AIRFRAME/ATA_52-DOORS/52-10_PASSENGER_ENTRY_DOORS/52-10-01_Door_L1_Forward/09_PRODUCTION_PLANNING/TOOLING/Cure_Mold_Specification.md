# Cure Mold Specification - Door L1 Forward

**Tool ID:** MOLD-001  
**Document:** AMPEL360-52-10-01-MOLD-SPEC  
**Date:** 2025-11-03  
**Status:** PRELIMINARY

---

## 1. MOLD OVERVIEW

### Purpose
Composite cure mold for autoclave processing of Door L1 Forward sandwich panels (outer and inner face sheets with honeycomb core).

### Configuration
- **Type:** Female mold (tool surface = outer mold line)
- **Material:** Invar steel (low CTE for dimensional stability)
- **Surface:** Polished to Ra 0.8 µm
- **Parting:** Single-piece construction (no parting line on part)

---

## 2. DIMENSIONS

### Mold Cavity
- **Length:** 2,400 mm
- **Width:** 1,800 mm
- **Depth:** 150 mm (accommodates core thickness + facesheets)
- **Contour:** Match outer mold line (OML) of door per drawing 52-10-01-001

### Overall Mold
- **Base plate:** 2,600 mm × 2,000 mm × 50 mm
- **Height (total):** 300 mm including supports
- **Weight (estimated):** 1,200 kg

### Tolerances
- **Contour surface:** ±0.5 mm
- **Critical features:** ±0.2 mm
- **Overall dimensions:** ±2.0 mm

---

## 3. MATERIAL SPECIFICATION

### Base Structure
- **Material:** Invar 36 (Fe-36Ni alloy)
- **Properties:**
  - CTE: 1.2 × 10⁻⁶ /°C (20-100°C)
  - Density: 8.05 g/cm³
  - Thermal conductivity: 10.7 W/m·K
- **Reason:** Low thermal expansion matches CFRP during cure cycle

### Surface Treatment
- **Machined finish:** CNC milled to contour
- **Polish:** Hand-polished to Ra 0.8 µm
- **Coating:** Hard chrome plating, 50 µm thickness
- **Final polish:** Ra 0.6 µm after chrome

---

## 4. FEATURES

### Datum System
- **Primary datum (A):** Base plane (mounting surface)
- **Secondary datum (B):** Longitudinal centerline
- **Tertiary datum (C):** Forward reference point

### Alignment Pins
- Quantity: 4 corner pins
- Material: Tool steel, hardened
- Diameter: 12 mm H7 fit
- Height: 50 mm above mold surface
- Purpose: Part alignment during layup

### Vacuum Ports
- Quantity: 8 ports
- Thread: 1/4" NPT
- Location: Perimeter of mold, evenly spaced
- Purpose: Vacuum bag connection points

### Thermocouple Ports
- Quantity: 6 ports
- Thread: 1/8" NPT with plug
- Location: Distributed across surface
- Purpose: Monitor part temperature during cure

### Lifting Points
- Quantity: 4 forged eyebolts
- Capacity: 500 kg each (2,000 kg total)
- Thread: M16
- Location: Corners of base plate

---

## 5. DESIGN REQUIREMENTS

### Thermal Performance
- **Heat-up rate:** Must support 2°C/min without distortion
- **Temperature uniformity:** ±3°C across surface at 180°C
- **Cooldown rate:** Support 3°C/min controlled cooling

### Structural Requirements
- **Autoclave pressure:** Withstand 10 bar differential
- **Deflection:** <0.5 mm under full cure pressure
- **Fatigue life:** 500 cure cycles minimum

### Surface Quality
- **Roughness:** Ra 0.6 µm (after all processing)
- **Cleanliness:** No embedded contaminants
- **Porosity:** None on molding surface
- **Release:** Compatible with Frekote 770-NC release agent

---

## 6. MANUFACTURING PROCESS

### Step 1: Base Plate Fabrication
1. Cut Invar plate to size
2. Drill mounting holes and feature holes
3. Install threaded inserts for ports and eyebolts

### Step 2: Contour Machining
1. CNC mill cavity to rough contour (+2 mm stock)
2. Semi-finish contour (+0.5 mm stock)
3. Finish contour to final dimensions

### Step 3: Surface Finishing
1. Hand polish to Ra 0.8 µm
2. Clean and degrease
3. Apply hard chrome plating (50 µm)
4. Final polish to Ra 0.6 µm

### Step 4: Final Assembly
1. Install alignment pins
2. Install vacuum port fittings
3. Install thermocouple port plugs
4. Install lifting eyebolts
5. Final cleaning

---

## 7. QUALITY CONTROL

### Dimensional Inspection
- **Method:** CMM (Coordinate Measuring Machine)
- **Frequency:** 100% after finish machining
- **Points:** 500+ measurement points
- **Report:** Full contour map vs. CAD model
- **Acceptance:** ±0.5 mm across entire surface

### Surface Quality
- **Roughness:** Profilometer measurement, Ra ≤0.6 µm
- **Visual:** 100% visual inspection under 500 lux
- **Acceptance:** No scratches, pits, or embedded particles

### Functional Tests
- **Leak test:** Vacuum ports must hold -750 mbar
- **Load test:** Lifting points to 2× rated capacity
- **Trial cure:** Validate with representative layup

---

## 8. DOCUMENTATION REQUIRED

### From Supplier
- [ ] Material certifications (Invar, chrome)
- [ ] CMM inspection report with contour map
- [ ] Surface roughness measurements
- [ ] Chrome plating thickness verification
- [ ] Load test reports for lifting points
- [ ] Operating and maintenance manual

### Company-Generated
- [ ] First article layup report
- [ ] Release agent compatibility test
- [ ] Cure cycle validation (3 parts minimum)
- [ ] Tool acceptance sign-off

---

## 9. MAINTENANCE REQUIREMENTS

### After Each Use
- Remove residual release agent and resin
- Inspect for damage (scratches, dings)
- Clean with IPA and lint-free cloth
- Apply rust inhibitor if storing >1 week

### Every 50 Cycles
- Full dimensional inspection (CMM)
- Surface roughness check
- Touch-up polish if Ra >1.0 µm
- Inspect vacuum ports for leaks

### Annual
- Re-chrome if surface degraded (Ra >1.5 µm)
- Full structural inspection
- Load test lifting points
- Update maintenance log

---

## 10. COST AND SCHEDULE

### Cost Breakdown
| Item | Cost ($) |
|------|----------|
| Invar material | 80,000 |
| CNC machining | 60,000 |
| Hand polishing | 30,000 |
| Chrome plating | 20,000 |
| Fixtures/hardware | 10,000 |
| Inspection | 15,000 |
| Documentation | 10,000 |
| Shipping | 5,000 |
| Contingency (10%) | 20,000 |
| **Total** | **250,000** |

### Schedule
| Milestone | Duration | Lead Time |
|-----------|----------|-----------|
| Design approval | - | Week 0 |
| Material procurement | 4 weeks | Week 4 |
| Rough machining | 3 weeks | Week 7 |
| Finish machining | 2 weeks | Week 9 |
| Polishing | 2 weeks | Week 11 |
| Chrome plating | 2 weeks | Week 13 |
| Final polish/assembly | 1 week | Week 14 |
| Inspection | 1 week | Week 15 |
| Trial cure | 1 week | Week 16 |
| **Delivery** | - | **Week 16** |

---

## 11. ACCEPTANCE CRITERIA

### Dimensional
- ✓ Contour within ±0.5 mm of CAD model
- ✓ All features within tolerance per drawing
- ✓ No high spots or low spots >0.3 mm

### Surface Quality
- ✓ Surface roughness Ra ≤0.6 µm
- ✓ No visual defects (scratches, pits, contamination)
- ✓ Chrome thickness 50±10 µm

### Functional
- ✓ Vacuum ports hold -750 mbar (leak rate <5 mbar/min)
- ✓ Alignment pins fit part features properly
- ✓ Trial cure produces dimensionally acceptable part
- ✓ Release agent compatibility confirmed

### Documentation
- ✓ All certifications and reports provided
- ✓ Maintenance manual included
- ✓ Tool identification plate installed

---

## 12. SUPPLIER QUALIFICATION

### Required Capabilities
- CNC machining of large steel tooling
- Invar material experience
- Chrome plating services (or subcontract)
- CMM inspection capability
- Quality system: ISO 9001 minimum

### Candidate Suppliers
1. Electroimpact (USA) - composite tooling specialist
2. Janicki Industries (USA) - large tool experience
3. MTEC Engineering (Germany) - aerospace tooling
4. TBD - European suppliers to be identified

---

**Document Control:**
- **Revision:** Draft 1.0
- **Approval:** Pending
- **Next Review:** Upon supplier quotes received
