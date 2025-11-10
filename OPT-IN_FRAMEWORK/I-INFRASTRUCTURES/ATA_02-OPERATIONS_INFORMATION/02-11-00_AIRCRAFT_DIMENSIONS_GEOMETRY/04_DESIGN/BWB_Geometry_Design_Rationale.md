# BWB Geometry Design Rationale

**Document ID:** AMPEL360-02-11-00-DES-002  
**Version:** 1.0.0

## Why Blended Wing Body?

### Aerodynamic Efficiency

**Conventional Aircraft (tube & wing):**
- Fuselage: 0% lift, 40% drag
- Wing: 100% lift, 60% drag
- L/D typical: 17

**BWB (AMPEL360):**
- Center body: 35% lift, 25% drag
- Wing: 65% lift, 75% drag  
- L/D achieved: 21 (+24% improvement)

**Key Mechanisms:**
- Wetted area reduction: 25% less per unit volume
- Lift distribution optimization
- Reduced interference drag
- Natural laminar flow over center body

### Structural Efficiency

**Weight Savings: 15% vs conventional**

**Mechanisms:**
- Distributed loads across wide center body
- Bending moment reduction (wide support)
- Efficient pressure vessel (flat sides)
- No separate wing-fuselage joint

**Load Paths:**
- Cabin pressure: Distributed over 38m width
- Wing bending: Multiple load paths
- Landing loads: Wide gear track (30m)

### H₂ Integration Advantages

**Tank Placement:**
- Upper deck: Natural separation from cabin
- Volume available: 350 m³ (vs 250 m³ conventional)
- Thermal management: Efficient due to geometry
- Safety: Physical separation + ventilation

**BWB Enables:**
- 4 independent tanks (redundancy)
- Optimal CG range (center + wing tanks)
- Simplified refueling access (top surface)

## Geometry Breakdown

### Planform Design

**Overall Shape:**
- Continuous lifting surface (no breaks)
- Smooth blending center to tip
- Leading edge: Compound curve (37° average sweep)
- Trailing edge: Variable sweep (-12° outer, 0° center)

**Why This Shape?**
- M0.82 cruise optimization (37° sweep)
- High lift at low speed (thickness distribution)
- Control surface integration (trailing edge)
- Structural continuity (smooth load paths)

### Cross-Section Evolution

**Station 0 (Nose):**
- Sharp nose (laminar flow)
- Width: 2m
- Height: 2m

**Station 15 (Max Width):**
- Width: 38m (passenger cabin)
- Height: 8.5m (internal)
- T/C: 15% (structural depth)
- Double-bubble pressure vessel

**Station 26 (Wingtip):**
- Width: 0.5m (tip chord 3.5m)
- Height: 0.3m
- T/C: 8% (aerodynamic surface)

### Volume Utilization

**Total Volume: 2,650 m³**

**Distribution:**
- Pressurized (passenger): 1,200 m³ (45%)
- Pressurized (other): 650 m³ (25%)
- H₂ tanks: 350 m³ (13%)
- Systems bays: 300 m³ (11%)
- Wheel wells: 150 m³ (6%)

**Efficiency vs Conventional:**
- Volume utilization: 78% vs 65%
- Passenger volume per m² planform: 1.42 vs 0.95

## Critical Geometric Decisions

### Decision 1: Center Body Width 38m

**Options Considered:**
- 32m: Insufficient passenger capacity (180 pax)
- 35m: Marginal for 220 pax, tight layout
- **38m: Selected** - optimal for 220 pax + systems
- 42m: Excessive gate requirements, heavier structure

**Selection Criteria:**
- Passenger comfort (8-abreast center section)
- H₂ tank volume accommodation
- Structural efficiency (pressure loads)
- Gate compatibility (42m gates available)

### Decision 2: Aspect Ratio 3.2

**Options Considered:**
- AR 2.5: Lower efficiency, lighter structure
- **AR 3.2: Selected** - optimal BWB range
- AR 4.0: Higher efficiency, incompatible with Code E
- AR 5.0: Requires 65m+ span (Code F airports)

**Trade-off Analysis:**
- AR 3.2 provides 95% of AR 4.0 efficiency
- Airport compatibility critical (business case)
- Structural weight acceptable
- Ground handling manageable

### Decision 3: Sweep 37°

**Options Considered:**
- 30°: M0.75 max cruise (too slow)
- 35°: M0.80 max (marginal for route network)
- **37°: Selected** - M0.82 capable, efficient
- 40°: M0.85 capable, excessive wing weight

**Analysis:**
- M0.82 sufficient for 95% of routes
- 37° enables natural laminar flow
- Structural efficiency acceptable
- Manufacturing complexity manageable

## Geometric Validation

**CFD Analysis (10,000+ hours):**
- L/D = 21 confirmed at M0.82
- Stall characteristics acceptable
- Control power adequate
- High-lift system validated

**Structural Analysis (FEM):**
- Weight target achieved (95,000 kg OEW)
- Fatigue life: 60,000 flight cycles
- Damage tolerance verified
- Load path efficiency confirmed

**Wind Tunnel Testing:**
- 1:10 scale model (200 hours)
- Performance confirmed ±2%
- Stability derivatives validated
- Control effectiveness verified
