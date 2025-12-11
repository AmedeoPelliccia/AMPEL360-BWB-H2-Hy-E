# 10-INST-TD-004 - Tiedown Load Requirements

## 1. Purpose

This document specifies load requirements for tiedown systems on the AMPEL360-BWB-H2 aircraft, including wind load calculations and safety factors.

## 2. Scope

- Design load requirements for tiedown systems
- Wind load calculations for BWB configuration
- Safety factors and load distribution
- Environmental conditions and limits

**Effectivity**: All AMPEL360-BWB-H2 aircraft configurations

## 3. Applicable Documents

- **CS-25.561** - Emergency landing conditions
- **CS-25.629** - Aeroelastic stability
- **MIL-STD-970** - Tiedown provisions
- **ASCE 7** - Minimum design loads for buildings and other structures

## 4. Safety Precautions

⚠️ **WARNINGS**
- Never exceed maximum demonstrated wind speed with minimum tiedowns
- Additional tiedowns required for winds >40 knots
- Account for fuel load when calculating required tiedown forces
- BWB configuration requires higher lateral loads than conventional aircraft

## 5. Design Load Requirements

### 5.1 Basic Load Cases

**Load Case 1: Normal Parking (Wind ≤40 knots)**
- Vertical load: 1.0g aircraft weight (balanced on gear and tiedowns)
- Longitudinal load: ±0.5g aircraft weight (fore/aft wind)
- Lateral load: ±0.75g aircraft weight (beam wind) **BWB-specific**
- Safety factor: 1.5 (ultimate load)

**Load Case 2: High Wind (Wind 40-60 knots)**
- Vertical load: 1.2g aircraft weight (dynamic effects)
- Longitudinal load: ±0.8g aircraft weight
- Lateral load: ±1.0g aircraft weight **BWB-specific**
- Safety factor: 1.5 (ultimate load)

**Load Case 3: Storm (Wind >60 knots)**
- Vertical load: 1.5g aircraft weight (gusts, dynamic)
- Longitudinal load: ±1.2g aircraft weight
- Lateral load: ±1.5g aircraft weight **BWB-specific**
- Safety factor: 1.5 (ultimate load)
- Additional tiedowns required (8-10 points)

### 5.2 BWB Configuration Factors

**Increased Lateral Loads**: BWB configuration experiences higher lateral loads due to:
- Large lifting surface area (wing-body integration)
- Lower center of gravity height
- Wider wingspan (approximately XXX ft)
- Lateral load factor increased by 50% vs conventional aircraft

**Wing Flexibility**: BWB wing structure may exhibit:
- Greater deflection under asymmetric loading
- Twist under beam wind conditions
- Requires distributed tiedown load on each wing panel

### 5.3 Load Distribution

**Minimum 6-Point Tiedown**:
- Forward points (2): 30% of total load
- Wing points (2): 30% of total load **BWB-specific**
- Aft points (2): 40% of total load

**Recommended 8-Point Tiedown** (winds >40 knots):
- Forward points (2): 25% of total load
- Wing outboard (2): 20% of total load
- Wing inboard (2): 15% of total load
- Aft points (2): 40% of total load

## 6. Wind Load Calculations

### 6.1 Wind Force on Aircraft

**Basic Wind Force Equation**:
```
F = 0.5 × ρ × V² × Cd × A
```

Where:
- F = Force (lb)
- ρ = Air density (0.00238 slug/ft³ at sea level)
- V = Wind velocity (ft/s)
- Cd = Drag coefficient (1.2-1.5 for BWB configuration)
- A = Projected area (ft²)

**BWB Projected Areas** (approximate):
- Frontal area (longitudinal wind): XXX ft²
- Side area (lateral wind): XXX ft² (significantly larger than conventional)
- Top area (vertical wind): XXX ft²

### 6.2 Example Calculations

**40 knot wind (67.6 ft/s), beam (lateral)**:
- F = 0.5 × 0.00238 × (67.6)² × 1.4 × XXX ft²
- F = approximately XX,XXX lb lateral force
- Distributed to 6 tiedown points = X,XXX lb per point
- With safety factor 1.5 = X,XXX lb design load per point

**60 knot wind (101.4 ft/s), beam (lateral)**:
- F = 0.5 × 0.00238 × (101.4)² × 1.4 × XXX ft²
- F = approximately XX,XXX lb lateral force
- Distributed to 8 tiedown points = X,XXX lb per point
- With safety factor 1.5 = X,XXX lb design load per point

### 6.3 Dynamic Load Factors

**Gust Factor**: 1.3 (for wind gusts)
**Dynamic Amplification**: 1.2 (for oscillatory motion)
**Combined Factor**: 1.56 (applied to static wind loads)

## 7. Environmental Limits

### 7.1 Operating Limits

| Configuration | Max Wind Speed | Min Tiedown Points | Additional Requirements |
|---------------|----------------|--------------------|-----------------------|
| Normal Parking | 40 knots | 6 | Standard procedures |
| High Wind | 60 knots | 8 | Secondary tiedowns, inspection every 4 hrs |
| Storm | 80 knots | 10 | All available tiedowns, inspection every 2 hrs |
| Extreme | >80 knots | Hangar | Not approved for outdoor tiedown |

### 7.2 Fuel Load Considerations

**LH2 Fuel Load Effects**:
- Full tanks: CG shifts aft, increases aft tiedown loads by 15%
- Empty tanks: CG shifts forward, increases forward tiedown loads by 10%
- Calculate actual CG per Weight & Balance Manual (ATA 02)

**Wind Limitations with Partial Fuel**:
- <25% fuel: Limit wind to 50 knots (reduced aft weight, tail may lift)
- 25-75% fuel: Normal limits apply
- >75% fuel: Normal limits apply

## 8. H2/BWB Considerations

### 8.1 BWB Structural Considerations

- Wing structure is primary load path for lateral loads
- Tiedown points must be at structural hard points (ribs, spars)
- Do not overload individual tiedown points (max design load per point)

### 8.2 H2 Safety Considerations

- Increased tiedown security near H2 vent areas (no aircraft movement)
- Emergency access paths must remain clear
- H2 detection sensors must be operational during tiedown operations

## 9. Quality Assurance

- Load calculations must be verified by structural engineer
- Tiedown configuration must be documented for each operation
- Inspection of tiedown integrity every 12 hours during high wind
- Real-time wind monitoring required for winds >40 knots

## 10. Cross-References

- **10-INST-TD-001** - Tiedown Points Installation
- **10-INST-TD-002** - BWB Tiedown Locations
- **10-INST-TD-003** - Tiedown Hardware Specifications
- **ATA 02** - Weight and Balance Manual

## 11. Revision History

| Rev | Date       | Author              | Description          |
|-----|------------|---------------------|----------------------|
| A   | 2025-12-09 | Amedeo Pelliccia    | Initial release      |

---

## Document Control

- **Document ID**: 10-INST-TD-004
- **Revision**: A
- **Status**: DRAFT - Subject to human review and approval
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
