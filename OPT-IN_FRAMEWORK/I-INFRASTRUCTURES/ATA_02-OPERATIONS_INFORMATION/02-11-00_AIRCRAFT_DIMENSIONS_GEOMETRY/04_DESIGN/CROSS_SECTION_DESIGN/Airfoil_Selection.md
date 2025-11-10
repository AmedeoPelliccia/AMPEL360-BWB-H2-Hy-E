# Airfoil Selection

**Document ID:** AMPEL360-02-11-00-DES-CS-002  
**Version:** 1.0.0

## BWB Airfoil Requirements

**Unlike conventional aircraft, BWB requires:**
- Dual-purpose sections (lift + volume)
- Variable thickness (8% to 15%)
- Smooth camber distribution
- Low drag across speed range

## Selected Airfoil Family

**Base Family:** Modified NASA SC(2) series

**Customization:**
- Increased thickness (up to 15%)
- Optimized camber distribution
- Pressure recovery tailored
- Boundary layer management

## Spanwise Distribution

| Station | Airfoil Type | T/C | Purpose |
|---------|-------------|-----|---------|
| Centerline | SC(2)-0015-mod | 15% | Max volume, lift |
| 10m span | SC(2)-0014-mod | 14% | Cabin, tanks |
| 20m span | SC(2)-0010-mod | 10% | Wing transition |
| Wingtip | SC(2)-0008-mod | 8% | Aerodynamic |

## Performance Characteristics

**Cruise (M0.82, α=2°):**
- CL: 0.45 (center body)
- CD: 0.018 (total)
- L/D contribution: Positive
- Laminar flow: 40% chord

**Low Speed (approach):**
- CL,max: 2.5 (with high-lift devices)
- Stall: Progressive, root-first
- Control: Adequate authority

## Validation

**Wind Tunnel:**
- 2D section tests completed
- 3D integration validated
- Performance confirmed

**CFD:**
- Detailed analysis of all sections
- Transition prediction
- Separation characteristics

**Status:** Frozen baseline  
**Approved:** 2024-03-01
