# Design Data: 06-10-01 - Overall Dimensions

## 1.0 Design Requirements Traceability

### 1.1 Certification Requirements
| Requirement | Source | Dimension Impact |
|-------------|--------|------------------|
| Emergency egress (90 seconds) | CS-25.803 | Door spacing: max 18m between Type-A exits |
| Runway overrun distance | CS-25.109 | Length affects rejected takeoff calculations |
| Airport compatibility | ICAO Annex 14 | Wingspan determines aerodrome code (4E) |
| Hangar fire protection | NFPA 409 | Height determines sprinkler system design |

### 1.2 Operational Requirements
| Requirement | Source | Dimension Impact |
|-------------|--------|------------------|
| 300 passengers (3-class) | Marketing Requirement | Cabin width 22.5m, length 35m |
| 18 LD-3 containers | Cargo Requirement | Cargo hold dimensions 18m × 3.2m × 1.6m |
| 7,500 nm range | Mission Requirement | LH₂ tank volume 13,000 L |
| Existing gate compatibility | Operational Requirement | Length <53m (typical gate limit) |

### 1.3 Performance Requirements
| Requirement | Source | Dimension Impact |
|-------------|--------|------------------|
| Cruise L/D ≥23 | Aerodynamic Requirement | Wingspan 65m (aspect ratio optimization) |
| Takeoff field length <2,500m | Performance Requirement | Wing area 650 m² (wing loading) |
| Noise Stage 5 -12 EPNdB | Environmental Requirement | Propulsor ground clearance 3.8m (blade tip) |

## 2.0 Configuration Trade Studies

### 2.1 Wingspan Optimization
**Trade Study ID:** AMPEL-TRADE-AERO-001  
**Date:** 2021-03-15

**Candidates:**
- **Option A:** 60m span → L/D = 21.5, Weight = 82,000 kg
- **Option B:** 65m span → L/D = 23.0, Weight = 85,000 kg ✓ (Selected)
- **Option C:** 70m span → L/D = 23.8, Weight = 89,000 kg

**Selection Rationale:**
- Option B provides optimal L/D vs. weight trade
- 65m span compatible with Code E airports (52-65m range)
- Option C provides only 3.5% L/D improvement but 13% weight penalty
- Structural weight increase offsets aerodynamic benefit beyond 65m

**Decision:** 65m wingspan selected (Option B)

### 2.2 Overall Length Trade
**Trade Study ID:** AMPEL-TRADE-GEOM-002  
**Date:** 2021-04-22

**Candidates:**
- **Option A:** 48m length → Tail strike angle 10°, CG range limited
- **Option B:** 52.5m length → Tail strike angle 11.5°, CG range adequate ✓ (Selected)
- **Option C:** 57m length → Tail strike angle 13°, excessive ramp space

**Selection Rationale:**
- Option B provides adequate tail strike margin (3° above rotation angle)
- 52.5m length compatible with most international gates (<55m limit)
- Option C requires larger gates, limiting airport accessibility
- Aft body length drives static pitch attitude and CG envelope

**Decision:** 52.5m length selected (Option B)

### 2.3 Overall Height Trade
**Trade Study ID:** AMPEL-TRADE-GEOM-003  
**Date:** 2021-05-10

**Candidates:**
- **Option A:** 9.8m height (propulsor embedded) → Complex inlet design
- **Option B:** 11.2m height (propulsor elevated) → Simpler inlet, standard hangar ✓ (Selected)
- **Option C:** 13.5m height (propulsor high-mounted) → Maintenance access issues

**Selection Rationale:**
- Option B provides optimal inlet flow quality (minimal distortion)
- 11.2m height compatible with standard wide-body hangars (<13m door height)
- Propulsor elevation improves maintenance access from ground
- Ground clearance adequate for blade tip safety (3.8m static)

**Decision:** 11.2m height selected (Option B)

## 3.0 Design Constraints and Drivers

### 3.1 Structural Constraints
**Wing Structural Box:**
- Maximum practical wingspan limited by wing root bending moment
- Carbon fiber composite wing box enables 65m span at 85,000 kg MTOW
- Wing deflection under 2.5g load: 850mm (1.3% span) within allowable limits

**Center Body Structure:**
- BWB center body width (22.5m) limited by:
  - Cabin pressurization hoop stress (0.8 bar differential)
  - Emergency evacuation requirements (max 30m evacuation path)
  - Composite panel buckling stability (10m unsupported panel width)

### 3.2 Aerodynamic Constraints
**Aspect Ratio Optimization:**
- Wingspan² / Wing Area = 65² / 650 = 6.5 (effective aspect ratio)
- BWB configuration provides lower induced drag than conventional aircraft at same AR
- Span efficiency factor (Oswald efficiency): e = 0.85 (excellent for BWB)

**Ground Effect:**
- Low wing height (center body ~1.5m above ground) provides:
  - Reduced takeoff/landing speeds (5% reduction in ground effect)
  - Challenge: Propulsor inlet ingestion risk requires 3.8m ground clearance

### 3.3 Operational Constraints
**Airport Gate Compatibility:**
- 85% of international wide-body gates accommodate aircraft <55m length
- AMPEL360 at 52.5m length compatible with:
  - Code E gates (all major hubs)
  - Most Code D gates (with diagonal parking)
- Wingspan 65m requires Code E apron (182.5m taxiway separation)

**Hangar Compatibility:**
- Standard wide-body hangar doors: 70m wide × 13m high
- AMPEL360 dimensions: 65m × 11.2m → fits with 5m/1.8m clearance
- Special consideration: BWB width (22.5m) requires diagonal entry in narrow hangars

## 4.0 Dimensional Optimization Results

### 4.1 Mass Properties Impact
**Dimensional Changes → Mass Effects:**

| Parameter | Baseline | Optimized | Mass Change |
|-----------|----------|-----------|-------------|
| Wingspan | 60m | 65m | +1,200 kg (wing structure) |
| Length | 48m | 52.5m | +800 kg (aft body structure) |
| Height | 9.8m | 11.2m | +200 kg (propulsor pylons) |
| **Total** | - | - | +2,200 kg |

**Mass Penalty Justification:**
- +2,200 kg structural mass penalty
- -1,800 kg fuel burn reduction (7,500 nm mission, improved L/D)
- **Net benefit:** -400 kg operating empty weight equivalent

### 4.2 Performance Impact
**Mission Performance (7,500 nm range, 300 pax):**

| Metric | Baseline (60m span) | Optimized (65m span) | Improvement |
|--------|---------------------|----------------------|-------------|
| Cruise L/D | 21.5 | 23.0 | +7.0% |
| Fuel Burn | 9,200 kg H₂ | 8,800 kg H₂ | -4.3% |
| Block Time | 11.2 hr | 11.0 hr | -1.8% |
| MTOW | 87,500 kg | 85,000 kg | -2.9% |

### 4.3 Economic Impact
**Direct Operating Cost (DOC) per flight:**

| Cost Element | Baseline | Optimized | Savings |
|--------------|----------|-----------|---------|
| Fuel Cost | $18,400 | $17,600 | -4.3% |
| Maintenance | $8,500 | $8,700 | +2.4% (larger wing) |
| Airport Fees | $3,200 | $3,200 | 0% (same Code E) |
| **Total DOC** | $30,100 | $29,500 | -2.0% |

**Payback Period:** Additional $1.2M per aircraft (larger wing) recovered in ~180 flights

## 5.0 Design Verification

### 5.1 CAD Model Validation
**Master Geometry Checks:**
1. **Overall Dimensions:** Extracted from CATIA DMU, compared to specification
   - Wingspan: 65,000 mm (nominal), 64,987 mm (CAD) → -13mm deviation ✓
   - Length: 52,500 mm (nominal), 52,512 mm (CAD) → +12mm deviation ✓
   - Height: 11,200 mm (nominal), 11,195 mm (CAD) → -5mm deviation ✓

2. **Mass Properties:** Calculated from CAD (assigned material densities)
   - Operating Empty Weight: 52,300 kg (within 2% of analytical estimate)
   - CG Position: 58.2% MAC (within design envelope 45-65% MAC)

3. **Clearance Verification:**
   - Propulsor ground clearance: 3,812 mm (min required 3,800 mm) ✓
   - Tail strike angle: 11.6° (min required 11.0°) ✓
   - Cargo door clearance (open): No interference with structure ✓

### 5.2 Manufacturing Feasibility
**Tooling Compatibility:**
- Wing assembly jig: 70m × 40m (accommodates 65m wingspan + tooling)
- Center body jig: 30m × 25m (accommodates 22.5m width)
- Final assembly station: 80m × 60m (adequate for 52.5m length)

**Transportation:**
- Wing panels: Max 25m length (transportable by road, rail, barge)
- Center body sections: Max 12m width (requires oversized load permit, feasible)
- Propulsor nacelles: 5.2m diameter (standard heavy-haul trucking)

### 5.3 Certification Compliance
**CS-25 Requirements:**

| Requirement | Specification | AMPEL360 Compliance |
|-------------|---------------|---------------------|
| CS-25.783(c) | Type-A exit: 42" × 72" min | 48" × 78" (8 exits) ✓ |
| CS-25.803(b) | 90-sec evacuation | Analysis shows 82 sec ✓ |
| CS-25.109 | Accelerate-stop distance | 2,450m (field length 2,500m) ✓ |
| ICAO Annex 14 | Code E wingspan 52-65m | 65.0m (at limit) ✓ |

## 6.0 Design Changes and Configuration Control

### 6.1 Major Design Changes (Rev History)
**Rev A → Rev B (2021-08-15):**
- **Change:** Wingspan increased from 62m to 65m
- **Reason:** Performance optimization (L/D improvement)
- **Impact:** Wing structural mass +800 kg, fuel burn -3.2%
- **Approval:** Chief Engineer, Program Manager

**Rev B → Rev C (2022-02-20):**
- **Change:** Overall length increased from 51.2m to 52.5m
- **Reason:** Tail strike margin (rotation angle clearance)
- **Impact:** Aft body structural mass +400 kg, tail strike angle +0.8°
- **Approval:** Chief Engineer, Flight Test Manager

### 6.2 Configuration Freeze
**Dimensional Freeze Date:** 2022-06-01 (Critical Design Review)

**Post-Freeze Changes Require:**
1. Engineering Change Request (ECR) submission
2. Impact analysis (performance, weight, cost, schedule)
3. Certification Authority notification (if affects type design)
4. Program Management approval (Level 1 change)

**Frozen Dimensions:**
- Wingspan: 65.0 m ±50 mm (no changes without regulatory review)
- Length: 52.5 m ±50 mm (no changes without gate compatibility re-analysis)
- Height: 11.2 m ±50 mm (no changes without hangar compatibility re-check)

## 7.0 Design Tools and Methods

### 7.1 CAD/CAE Tools
**Primary Design Environment:**
- **CATIA V6:** 3D master geometry, digital mockup (DMU)
- **Siemens NX:** Detailed part design, manufacturing engineering
- **Dassault 3DEXPERIENCE:** Collaborative design, PLM integration

**Analysis Tools:**
- **ANSYS Mechanical:** Structural FEA (wing deflection, pressurization stress)
- **MSC Nastran:** Detailed stress analysis (critical interfaces)
- **STAR-CCM+:** CFD (propulsor inlet flow, aerodynamic performance)

### 7.2 Parametric Design Approach
**Design Variables:**
1. Wingspan (optimization variable: 60-70m range)
2. Overall length (constraint: <55m for gate compatibility)
3. Center body width (constraint: 20-25m for cabin capacity)
4. Propulsor ground clearance (constraint: >3.5m for safety)

**Objective Function:**
- Minimize DOC = f(fuel_burn, maintenance, acquisition_cost)
- Subject to: Gate compatibility, hangar compatibility, CS-25 compliance

**Optimizer:** Multi-objective genetic algorithm (MOGA)
- Population: 500 candidate configurations
- Generations: 100 iterations
- Convergence: Pareto front identified at generation 73

### 7.3 Design Validation Methods
**Virtual Testing:**
- Digital mockup interference checks (1,200+ critical clearances verified)
- FEA structural validation (ultimate load = 1.5 × limit load)
- CFD aerodynamic validation (cruise L/D within 2% of wind tunnel)

**Physical Testing:**
- 1/10 scale wind tunnel model (dimensional accuracy ±0.5mm)
- Full-scale structural test article (wing static test to ultimate load)
- Ground vibration test (modal analysis, validate FEA model)

## 8.0 Lessons Learned

### 8.1 BWB Dimensional Challenges
**Challenge 1: Reference Datum Definition**
- **Issue:** No conventional firewall reference point (typical datum)
- **Solution:** Define datum at nose apex (FS 0), establish BRS coordinate system
- **Lesson:** Early definition of reference system critical for multi-disciplinary teams

**Challenge 2: Width Measurement**
- **Issue:** BWB width varies continuously (no constant "fuselage width")
- **Solution:** Define max cabin width (22.5m) and document width variation curve
- **Lesson:** Specify measurement stations for all critical width dimensions

### 8.2 Design Process Improvements
**Improvement 1: Integrated Trade Studies**
- Wingspan, length, height optimized simultaneously (not sequentially)
- Result: Better global optimum (2% lower DOC than sequential optimization)

**Improvement 2: Airport Database Integration**
- Gate/hangar dimensions from 200 airports integrated in CAD environment
- Result: Real-time compatibility checking during design phase

**Improvement 3: Digital Twin from Day 1**
- As-designed CAD model maintained in parallel with physical mockup
- Result: 30% reduction in design rework (dimensional interference issues)

## 9.0 Future Work

### 9.1 Dimensional Monitoring (In-Service)
**Planned Enhancements:**
- Embedded strain gauges (wing deflection monitoring in real-time)
- Photogrammetry (rapid dimensional inspection during C-Check)
- Digital twin update (as-flown dimensions fed back to design model)

### 9.2 Next-Generation Sizing
**Derivative Aircraft Studies:**
- **AMPEL360-200:** Stretched variant (+8m length, 350 pax)
- **AMPEL360-300:** Reduced range variant (-5m span, 6,000 nm)
- **AMPEL360F:** Freighter variant (optimize cargo hold dimensions)

## 10.0 References

### 10.1 Internal Documents
- AMPEL-TRADE-AERO-001: Wingspan Optimization Trade Study
- AMPEL-TRADE-GEOM-002: Overall Length Trade Study
- AMPEL-TRADE-GEOM-003: Overall Height Trade Study
- AMPEL-CDR-GEOM-001: Critical Design Review (Geometry Package)

### 10.2 External Standards
- SAE AS8015: Aircraft Coordinate System
- ASME Y14.5: Geometric Dimensioning and Tolerancing
- ICAO Annex 14: Aerodromes (Design Standards)
- CS-25: Certification Specifications for Large Aeroplanes

### 10.3 Related ATA Chapters
- ATA 51-57: Structural Component Dimensions (detailed breakout)
- ATA 07: Lifting and Shoring (jack point locations derived from dimensions)
- ATA 08: Leveling and Weighing (datum references)
- ATA 09: Towing and Taxiing (tow bar attachment coordinates)
