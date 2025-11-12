# Structural Weight Optimization

**Document ID:** AMPEL360-02-11-00-DES-OPT-002  
**Version:** 1.0.0

## Optimization Objectives

**Primary Goal:** Minimize structural weight while maintaining safety and certification compliance.

**Targets:**
- OEW (Operating Empty Weight): ≤95,000 kg
- Structural efficiency: ≥85%
- Fatigue life: 60,000 flight cycles
- Safety factors: CS-25 compliant

## Optimization Scope

### Primary Structure

**Wing Box:**
- Spars: 2 main, 1 auxiliary
- Ribs: Spacing optimized
- Skins: Composite layup
- **Target: 18,500 kg**

**Center Body:**
- Frames: 600mm spacing
- Stringers: 200mm pitch
- Pressure vessel: Double-bubble
- **Target: 18,500 kg**

**Secondary Structure:**
- Fairings, panels, doors
- Non-load bearing
- **Target: 6,500 kg**

## Optimization Methods

### Topology Optimization

**Software:** Altair OptiStruct, ANSYS Topological

**Process:**
1. Define design space
2. Apply loads and constraints
3. Run optimization (minimize volume)
4. Interpret results (manufacturable)
5. Iterate design

**Results:**
- Weight reduction: 8-12% per component
- Load paths: Clearly defined
- Structural efficiency: Improved

### Size Optimization

**Variables:**
- Skin thickness: 3-8mm range
- Stiffener spacing: 150-250mm
- Frame depth: 100-200mm

**Constraints:**
- Ultimate strength: 1.5x limit load
- Buckling: Safety factor ≥1.5
- Fatigue: 3x service life

**Results:**
- Wing box: 18,500 kg (target met)
- Center body: 18,500 kg (target met)
- Total structure: 43,500 kg

### Material Optimization

**Composite Layup:**
- Fiber orientation: Optimized per load
- Ply thickness: Minimized
- Ply drops: Gradual (manufacturability)

**Material Selection:**
- Primary structure: IM7/8552 (carbon/epoxy)
- Secondary: Aluminum 2024-T3
- Fasteners: Titanium (critical), steel (standard)

**Weight Savings:**
- vs. Aluminum: 20% lighter
- vs. Standard composite: 5% lighter
- **Total benefit: 23% vs. metal baseline**

## Key Optimizations Achieved

### Wing Box Design

**Spar Caps:**
- Original: Constant section
- Optimized: Tapered (root to tip)
- **Weight saving: 850 kg (9%)**

**Rib Design:**
- Original: Uniform ribs
- Optimized: Variable depth
- **Weight saving: 320 kg (12%)**

**Skin Thickness:**
- Original: Constant gauge
- Optimized: Variable (2-ply gradient)
- **Weight saving: 580 kg (8%)**

### Center Body Structure

**Frame Spacing:**
- Original: 500mm uniform
- Optimized: 600mm standard, 300mm at attachments
- **Weight saving: 420 kg (5%)**

**Pressure Vessel:**
- Original: Single bubble
- Optimized: Double bubble (structural efficiency)
- **Weight saving: 1,200 kg (15%)**

**Floor Structure:**
- Original: Uniform
- Optimized: Honeycomb sandwich (optimized)
- **Weight saving: 380 kg (18%)**

## Validation

### FEM Analysis

**Model:**
- Elements: 5M+ (full aircraft)
- Load cases: 250+ (flight envelope)
- Material models: Progressive damage

**Results:**
- All load cases: Passed
- Ultimate load: 1.5x (demonstrated)
- Fatigue: 180,000 cycles (3x life tested)

### Testing

**Static Tests:**
- Wing box: Full-scale test
- Ultimate load: 1.5x demonstrated
- Failure mode: As predicted
- Margin: 8% above requirement

**Fatigue Tests:**
- Coupons: 500+ specimens
- Components: 10 critical areas
- Full-scale: Section tested
- Life: >3x required (validated)

**Manufacturing Trials:**
- Prototype parts: 50+ produced
- Weight: Within ±2% of prediction
- Quality: Meets standards
- Producibility: Confirmed

## Weight Breakdown

### As-Optimized (OEW: 95,000 kg)

**Structure: 43,500 kg (45.8%)**
- Wing box: 18,500 kg
- Center body: 18,500 kg
- Secondary: 6,500 kg

**Systems: 22,500 kg (23.7%)**
- Propulsion: 8,500 kg
- Avionics: 2,800 kg
- Electrical: 3,200 kg
- Environmental: 2,000 kg
- Hydraulics: 1,800 kg
- Other: 4,200 kg

**Furnishings: 12,000 kg (12.6%)**
- Seats: 4,800 kg (220 seats)
- Galleys: 2,400 kg
- Lavatories: 800 kg
- Overhead bins: 1,600 kg
- Other: 2,400 kg

**H₂ System: 5,000 kg (5.3%)**
- Tanks: 3,200 kg (4 tanks)
- Plumbing: 800 kg
- Insulation: 600 kg
- Safety systems: 400 kg

**Operational Items: 12,000 kg (12.6%)**
- Crew: 1,200 kg (6 crew)
- Catering: 1,800 kg
- Potable water: 800 kg
- Emergency equipment: 600 kg
- Other: 7,600 kg

## Comparison with Targets

**OEW Target: 95,000 kg**
- Achieved: 95,000 kg ✓
- Margin: 0 kg (tight but met)

**Structural Weight Target: 43,500 kg**
- Achieved: 43,500 kg ✓
- vs. Conventional: 15% lighter

**Weight Growth Allowance:**
- Design: 0 kg (tight design)
- Development: 2% (1,900 kg reserved)
- Production: 1% (950 kg expected)

## Future Optimization Potential

**Advanced Materials:**
- Graphene-enhanced composites: -3% weight
- Nano-materials: -2% weight
- **Potential: -5% (2,175 kg)**

**Manufacturing:**
- Additive manufacturing (metal parts): -8% part weight
- Advanced joining (no fasteners): -2% weight
- **Potential: -3% (1,300 kg)**

**Topology:**
- Further iteration: -1% weight
- Multi-objective: -0.5% weight
- **Potential: -1.5% (650 kg)**

**Total Future Potential: -9.5% (4,125 kg)**

## Certification

**CS-25.305 (Strength):**
- Static tests: Passed ✓
- Ultimate load: 1.5x demonstrated ✓

**CS-25.571 (Damage Tolerance):**
- Fatigue: 3x life demonstrated ✓
- Crack growth: Slow growth validated ✓

**CS-25.573 (Damage Tolerance):**
- Fail-safe: Multiple load paths ✓
- Inspection: Accessible ✓

**Status:** Optimization complete  
**Weight Target:** Met (95,000 kg OEW)  
**Frozen:** 2024-04-01  
**Approved:** 2024-03-30
