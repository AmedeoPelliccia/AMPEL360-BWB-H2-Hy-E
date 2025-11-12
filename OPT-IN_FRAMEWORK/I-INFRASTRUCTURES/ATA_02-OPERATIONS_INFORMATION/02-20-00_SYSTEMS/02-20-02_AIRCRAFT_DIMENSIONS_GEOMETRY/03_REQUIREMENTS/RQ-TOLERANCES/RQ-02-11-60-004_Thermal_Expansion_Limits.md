# RQ-02-11-60-004: Thermal Expansion Limits

**Priority:** High  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

Thermal expansion and contraction of aircraft structure shall be analyzed and accommodated in design, with dimensional changes limited to maintain structural integrity, system functionality, and clearances across the operational temperature range of -55°C to +85°C.

## Thermal Environment

**Operational Temperature Range:**
- Ground operations: -40°C to +55°C (ambient)
- Flight operations: -55°C to +85°C (surface temperatures)
- H₂ tank region: -253°C (cryogenic)
- Engine bay: Up to +200°C (localized)

**Temperature Gradients:**
- Across structure: Up to 100°C differential
- Through thickness: Up to 30°C differential
- Day/night cycles: ±30°C typical
- Fuel loading effects: Significant in H₂ system

## Material Properties

**Coefficient of Thermal Expansion (CTE):**
- Aluminum alloys: 23 × 10⁻⁶ /°C
- CFRP (composite): 0 to 2 × 10⁻⁶ /°C (fiber direction)
- CFRP (composite): 30 × 10⁻⁶ /°C (transverse)
- Titanium: 9 × 10⁻⁶ /°C
- Steel (fasteners): 12 × 10⁻⁶ /°C

**Material Combinations:**
- Composite primary structure
- Metal fittings and fasteners
- Differential expansion at interfaces
- Thermal stress management critical

## Dimensional Changes

**Typical Expansion Values:**
- Wingspan (52m, CFRP, ΔT=100°C): ±5mm (fiber direction)
- Length (38.2m, CFRP, ΔT=100°C): ±4mm
- Center body width (38m, ΔT=50°C): ±2mm
- Metal fittings: Up to ±20mm localized

**Design Allowances:**
- Expansion joints at critical interfaces
- Fastener hole clearances accommodate movement
- Sliding/flexible interfaces
- Thermal isolation where required

## Critical Areas

**H₂ Tank Interface:**
- Cryogenic tank at -253°C
- Adjacent structure at ambient
- Temperature differential: ~300°C
- Thermal protection system required
- Expansion joints critical

**Wing-Body Junction:**
- Large structural members
- Significant loads transferred
- Temperature variations
- Composite-metal interfaces

**Control Systems:**
- Control cables: Temperature compensation
- Actuators: Functional across range
- Sensors: Temperature effects calibrated
- Hydraulic lines: Flexible routing

## Verification Method

**Analysis:**
- Thermal finite element analysis
- Transient thermal analysis
- Thermal stress analysis
- Interface stress analysis

**Testing:**
- Thermal cycling tests of components
- Full-scale article testing (if feasible)
- Material CTE verification
- Interface test specimens

**Acceptance Criteria:**
- Thermal stresses within allowable
- Clearances maintained at extremes
- System functionality preserved
- No thermal fatigue issues predicted

## Design Features

**Thermal Management:**
- Insulation in cryogenic areas
- Thermal barriers at interfaces
- Active cooling (if required)
- Passive ventilation

**Structural Provisions:**
- Slotted holes for expansion
- Sliding joints
- Flexible connections
- Thermal breaks

## Operational Considerations

**Ground Operations:**
- Cold soak: Pre-flight inspection adjusted
- Hot day ops: Clearance verification
- H₂ loading: Thermal shock considerations
- Fuel temperature monitoring

**Flight Operations:**
- Climb/descent: Rapid temperature changes
- Cruise: Stabilized thermal state
- High altitude: Cold soak effects
- Solar heating: One-sided effects

## Monitoring and Inspection

**Temperature Monitoring:**
- Critical areas instrumented
- CAOS thermal monitoring
- H₂ system: Extensive monitoring
- Data recording for analysis

**Inspection:**
- Thermal fatigue areas identified
- Inspection intervals defined
- Crack detection at interfaces
- Permanent deformation check

## H₂ System Special Considerations

**Cryogenic Effects:**
- Tank contraction: ~900mm on 30m length (if metal)
- Composite tank: Minimal contraction
- Support structure thermal isolation
- Fill/drain thermal cycles

**Safety:**
- Leak prevention at thermal cycles
- Pressure relief considerations
- Thermal protection system integrity
- Emergency procedures for thermal events

## Compliance

**Standards:**
- [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Damage tolerance and fatigue)
- [CS-25.603](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Materials)
- [CS-25.613](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Material strength properties)
- [MIL-HDBK-5](https://www.militaryhandbooks.com/MIL-HDBK-5) (Material properties)

**Related Requirements:**
- [RQ-02-11-60-001](RQ-02-11-60-001_Manufacturing_Tolerances.md) (Manufacturing Tolerances)
- [RQ-02-11-60-003](RQ-02-11-60-003_Operational_Deflections.md) (Operational Deflections)
- H₂ system thermal requirements
- All structural requirements
