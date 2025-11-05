# RQ-02-10-20-003: MZFW Specification

**Requirement ID:** RQ-02-10-20-003  
**Category:** Weights  
**Priority:** Critical  
**Status:** Approved

## Requirement

The aircraft Maximum Zero Fuel Weight (MZFW) shall not exceed 135,000 kg to ensure wing structural integrity throughout the flight envelope.

**MZFW:** 135,000 kg (297,624 lb)  
**Typical ZFW:** 117,000 kg (257,940 lb)  
**Calculation:** OEW + Payload + Crew + Baggage

## Rationale

MZFW limit ensures:
- Wing bending relief from fuel weight accounted for
- Wing root bending moment within design limits
- Structural fatigue life targets achieved
- Flight loads in all conditions acceptable
- BWB structural efficiency maintained

## Operational Impact

**Maximum Payload Scenario:**
- OEW: 95,000 kg
- Maximum Payload: 40,000 kg
- Results in MZFW = 135,000 kg

**Available Fuel at MTOW:**
- MTOW - MZFW = 50,000 kg total
- H₂ usable fuel: 8,000 kg
- This limits provides structural margin

## Verification

- **Method:** Analysis
- **Procedure:** Wing structural analysis and load calculations
- **Acceptance Criteria:**
  - Wing bending moment at MZFW within allowables
  - Fatigue analysis demonstrates required life
  - Gust and maneuver loads evaluated at MZFW
  - Flutter analysis completed

## Compliance

- CS-25.25: Weight limits
- CS-25.301: Loads
- CS-25.303: Factor of safety
- CS-25.305: Strength and deformation
- CS-25.571: Damage tolerance and fatigue evaluation

## Related Requirements

- RQ-02-10-20-001: MTOW Specification
- RQ-02-10-20-002: MLW Specification
- RQ-02-10-20-004: OEW Specification
- RQ-02-10-30-001: Passenger Capacity
- RQ-02-10-30-002: Cargo Capacity

---

**Document Control:**
- Version: 1.0
- Status: Approved
- Last Updated: 2025-11-05
- Approved By: Structures Chief Engineer
