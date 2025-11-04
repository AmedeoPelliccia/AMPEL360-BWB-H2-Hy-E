# Design Scaling Analysis
## SM-001 Quarter-Scale Model

**Document:** SM-001-SCALING  
**Status:** Not Started  
**Date:** 2025-11-03

### 1. OBJECTIVE

Create quarter-scale wind tunnel model for aerodynamic testing:
- External door contour effects
- Flow separation analysis
- Pressure distribution
- Drag contribution

### 2. SCALING RATIOS

**Geometric Scale:** 1:4 (linear dimensions)  
**Area Scale:** 1:16  
**Volume Scale:** 1:64

**Full Scale Door:** 1120mm × 1880mm  
**Quarter Scale:** 280mm × 470mm

### 3. REYNOLDS NUMBER CONSIDERATIONS

Full scale flight (250 m/s, sea level):
- Re ≈ 18 × 10⁶

Quarter scale wind tunnel (achievable):
- Re ≈ 2 × 10⁶ (velocity limited)
- Not true Reynolds number match
- Acceptable for pressure distribution

### 4. MODEL CONSTRUCTION

**Method:** 3D printing (SLA or SLS)  
**Material:** ABS or nylon  
**Surface finish:** 400 grit (smooth)

**Features to include:**
- Door outer mold line
- Hinge fairings
- Surrounding fuselage contour
- Surface details (panel lines)

**Features to omit:**
- Internal structure
- Mechanisms
- Interior trim

### 5. INSTRUMENTATION

- Surface pressure taps (20-30 locations)
- Pressure transducers
- Force balance (drag measurement)
- Flow visualization (tufts or oil flow)

### 6. TEST PLAN

#### Wind Tunnel Tests
- Velocity range: 20-80 m/s
- Angle of attack: -5° to +10°
- Sideslip: 0° to ±15°
- Door positions: Closed only (flush)

#### Data to Collect
- Surface pressure distribution
- Drag coefficient
- Flow separation points
- Comparison to CFD predictions

### 7. COST & SCHEDULE

**Budget:** $8,000  
- 3D printing: $2,000
- Instrumentation: $3,000
- Wind tunnel time: $2,500
- Analysis: $500

**Duration:** 8 weeks  
**Priority:** Low (optional)

---

**Document Control:** SM-001-SCALING-001  
**Revision:** A
