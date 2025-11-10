# RQ-02-11-20-003: Aspect Ratio 3.2

**Priority:** High  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

The aircraft wing aspect ratio shall be 3.2 ±0.1, calculated as the square of wingspan divided by reference wing area (b²/S).

## Rationale

**Aerodynamic Efficiency:**
- Optimized for BWB configuration
- Balances induced and parasitic drag
- Achieves L/D ratio of 21
- Superior to conventional aircraft (L/D ~17)

**BWB Characteristics:**
- Lower aspect ratio than conventional wings
- Entire center body generates lift
- Reduced wing bending moments
- Improved structural efficiency

**Performance Benefits:**
- 30% better fuel efficiency
- Extended range capability
- Reduced wing structural weight
- Enhanced cruise performance

## Calculation

**Formula:**
```
Aspect Ratio (AR) = b² / S
Where:
  b = wingspan = 52.0m
  S = reference area = 845m²
  
AR = (52.0)² / 845 = 2704 / 845 = 3.2
```

## Verification Method

**Calculation:**
- From approved wingspan (RQ-02-11-10-001)
- From approved wing area (RQ-02-11-10-004)
- CAD model verification
- Aerodynamic analysis validation

**Acceptance Criteria:**
- 3.1 ≤ AR ≤ 3.3
- Derived from certified dimensions
- Aerodynamic model validated

## Aerodynamic Impact

**Induced Drag:**
- Lower AR reduces wing efficiency factor
- Compensated by BWB center body lift
- Net improvement in overall efficiency

**Structural Benefits:**
- Lower wing root bending moments
- Reduced structural weight
- Easier integration with center body

## Compliance

**Standards:**
- [CS-25.103](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Stall characteristics)
- [CS-25.143](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Controllability and maneuverability)
- Aerodynamic design standards

**Related Requirements:**
- [RQ-02-11-10-001](../RQ-DIMENSIONS/RQ-02-11-10-001_Wingspan_52m.md) (Wingspan)
- [RQ-02-11-10-004](../RQ-DIMENSIONS/RQ-02-11-10-004_Wing_Area_845m2.md) (Wing Area)
- [RQ-02-11-20-005](RQ-02-11-20-005_Planform_Continuity.md) (Planform Continuity)
