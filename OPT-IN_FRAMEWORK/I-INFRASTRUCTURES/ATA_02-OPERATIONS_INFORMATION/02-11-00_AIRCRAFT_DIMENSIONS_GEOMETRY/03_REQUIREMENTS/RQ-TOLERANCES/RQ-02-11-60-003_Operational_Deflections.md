# RQ-02-11-60-003: Operational Deflections

**Priority:** High  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

Operational deflections of aircraft structure under load shall be analyzed, predicted, and monitored to ensure adequate clearances are maintained during all flight and ground operations, with maximum deflections limited to preserve safety margins.

## Deflection Limits

**Wing Deflection:**
- Wingtip vertical deflection at MTOW: ±200mm maximum
- Wingtip vertical deflection at 2.5g: +400mm maximum
- Affects wingtip ground clearance (static 1.2m)
- Minimum clearance maintained: 0.8m (with monitoring)

**Center Body Deflection:**
- Floor deflection under distributed load: ±20mm
- Pressurization effects: +30mm (outward bulging)
- Bending under flight loads: ±50mm
- Local panel deflections: ±10mm

**Control Surface Deflection:**
- Control surface droop (unpowered): ±30mm
- Under aerodynamic load: Per design limits
- Gust load response: Transient deflections allowed
- Flutter margin preserved

## Rationale

**Ground Clearance:**
- Wingtip clearance critical at heavy weights
- Wing flex reduces clearance during taxi
- Tail clearance during rotation
- Belly clearance considerations

**Structural Integrity:**
- Deflections indicate loads
- Excessive deflections → potential damage
- Monitoring enables predictive maintenance
- Validation of structural analysis

**Aerodynamic Performance:**
- Wing twist affects lift distribution
- Excessive deflection → performance degradation
- Control surface effectiveness
- Flutter prevention

## Load Cases

**Ground Operations:**
- Static ground (MTOW): Gravity loads only
- Taxi (MTOW): Dynamic bump loads
- Turning: Lateral loads on landing gear
- Braking: Longitudinal loads

**Flight Operations:**
- Level flight at cruise: 1.0g nominal
- Maneuver loads: +2.5g / -1.0g limit
- Gust loads: Per CS-25.341
- Buffet conditions: High angle of attack

## Verification Method

**Analysis:**
- Finite Element Analysis (FEA) of structure
- Load cases per CS-25 requirements
- Deflection predictions documented
- Sensitivity studies performed

**Ground Testing:**
- Static load test to 150% limit load
- Deflection measurements at key points
- Correlation with FEA predictions
- Permanent deformation check

**Flight Testing:**
- Instrumented flight tests
- Deflection measurement (photogrammetry or sensors)
- Load factor correlation
- Envelope expansion validation

**Acceptance Criteria:**
- Predictions within 10% of test results
- No exceedance of deflection limits
- Adequate clearances maintained
- Flutter margins confirmed

## Monitoring System

**CAOS Integration:**
- Real-time load monitoring
- Deflection estimation algorithms
- Ground clearance calculation
- Crew alerting system

**Sensors:**
- Strain gauges on primary structure
- Accelerometers for load factor
- Inertial measurement unit (IMU)
- Ground proximity sensors (if applicable)

**Alerts:**
- Wingtip clearance advisory: <1.5m
- Wingtip clearance warning: <1.0m
- Overload detection
- Exceedance recording

## Operational Procedures

**Ground Operations:**
- CAOS ground mode mandatory
- Crew awareness of clearances
- Wing walkers for tight clearances
- Load monitoring active

**Flight Operations:**
- Load factor monitoring
- Turbulence reporting
- Overload inspection criteria
- Maintenance action triggered

## Thermal Effects

**Temperature Variations:**
- Thermal expansion: ±15mm for ±50°C
- Differential expansion: Composite vs. metal
- Fuel temperature effects
- H₂ cryogenic tank effects

**Corrections:**
- Thermal expansion coefficients applied
- Reference temperature: 15°C (59°F)
- Compensation in monitoring system
- Documentation of thermal state

## Fatigue Implications

**Deflection Monitoring:**
- Cycle counting for fatigue
- Exceedance tracking
- Fatigue life consumption calculation
- Inspection triggers

**Maintenance:**
- Periodic deflection measurement
- Comparison to baseline
- Structural health monitoring
- Predictive maintenance

## Compliance

**Regulatory:**
- [CS-25.305](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Strength and deformation)
- [CS-25.341](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Gust loads)
- [CS-25.345](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (High lift devices)
- [CS-25.629](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Aeroelastic stability - flutter)

**Related Requirements:**
- [RQ-02-11-30-001](../RQ-CLEARANCES/RQ-02-11-30-001_Wingtip_Clearance_1.2m_Min.md) (Wingtip Clearance)
- [RQ-02-11-30-002](../RQ-CLEARANCES/RQ-02-11-30-002_Belly_Clearance_1.8m_Min.md) (Belly Clearance)
- [RQ-02-11-60-004](RQ-02-11-60-004_Thermal_Expansion_Limits.md) (Thermal Expansion)
- Structural design requirements
