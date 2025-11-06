# RQ-02-11-60-002: Assembly Tolerances

**Priority:** Critical  
**Status:** Approved  
**Version:** 1.0.0

## Requirement Statement

Assembly tolerances shall be defined and controlled to ensure proper fit-up of major structural components, maintain aerodynamic contours, and enable efficient assembly processes while meeting all performance requirements.

## Assembly Tolerance Stack-Up

**Major Assembly Interfaces:**
- Wing-to-center body: ±0.15m positional
- Wing sections: ±0.10m joint alignment
- Control surfaces: ±0.05m hinge line
- Landing gear: ±0.02m attachment points
- Doors: ±0.05m frame alignment

**Tolerance Accumulation:**
- Stack-up analysis performed for all load paths
- Worst-case analysis for critical features
- Statistical (RSS) analysis for non-critical
- Shim allowance included in design

## Rationale

**Structural Requirements:**
- Load path continuity
- Uniform stress distribution
- Fatigue life preservation
- Damage tolerance maintenance

**Aerodynamic Requirements:**
- Surface continuity across joints
- Step/gap control at joints
- Contour maintenance
- Flush fastener requirements

**Assembly Efficiency:**
- Minimize shimming operations
- Reduce rework requirements
- Accelerate assembly cycle
- Enable lean manufacturing

## Joint Specifications

**Step and Gap Limits:**
- Critical aerodynamic surfaces: ±1mm
- Primary structure joints: ±2mm
- Secondary structure: ±5mm
- Non-aerodynamic: ±10mm

**Fastener Hole Alignment:**
- Critical joints: ±0.5mm misalignment max
- Primary joints: ±1.0mm misalignment max
- Secondary joints: ±2.0mm misalignment max
- Drilling through assembled parts acceptable

## Verification Method

**Assembly Inspection:**
- Photogrammetry of major assemblies
- Laser scanning for surface verification
- Physical measurement of critical joints
- Gap and step measurement at all joints

**Shimming Documentation:**
- Shim thickness recorded
- Shim location documented
- Torque values recorded
- As-built configuration captured

**Acceptance Criteria:**
- All joints within tolerance
- Shim thickness within allowable range
- Fastener holes align (or drilled on assembly)
- Surface contour maintained

## Assembly Fixtures and Tooling

**Fixture Requirements:**
- Fixture accuracy: ±0.05m or better
- Precision locating features
- Adjustability for tolerance compensation
- Thermal stability (temperature controlled environment)

**Tooling Inspection:**
- Pre-assembly fixture verification
- Periodic recalibration
- Wear monitoring
- Fixture certification

## Shimming Procedures

**Shim Application:**
- Shim material: Aluminum or composite
- Maximum shim thickness: 3mm single location
- Stepped shims: For gaps >1.5mm
- Tapered shims: For angular misalignment

**Shim Location:**
- Document all shim locations
- Capture in digital twin
- Include in maintenance records
- Mark on structure per procedure

## Special Assembly Considerations

**BWB Specific:**
- Large surface area assemblies
- Contour matching critical
- Multiple assembly sequences evaluated
- Fixture design critical for success

**Composite Assemblies:**
- Co-bonding vs. secondary bonding
- Cure cycle compatibility
- Thermal expansion during assembly
- Bond line thickness control

## Non-Conformance

**Out-of-Tolerance Conditions:**
- Engineering review required
- Structural analysis for loads
- Aerodynamic assessment for performance
- Repair/rework procedure approved

**Corrective Actions:**
- Root cause analysis
- Process improvement
- Tooling adjustment
- Supplier corrective action (if applicable)

## Digital Twin Integration

**As-Built Documentation:**
- Actual assembly dimensions recorded
- Shim locations and thickness
- Joint gap measurements
- Digital model updated with actuals

**Configuration Management:**
- As-designed vs. as-built comparison
- Deviation tracking
- Change implementation
- Historical record maintenance

## Compliance

**Standards:**
- SAE AIR7211 (Assembly tolerance)
- ASME Y14.5 (GD&T)
- AS9100 (Quality management)
- ATA iSpec 2200 (Assembly documentation)

**Related Requirements:**
- RQ-02-11-60-001 (Manufacturing Tolerances)
- RQ-02-11-60-005 (Measurement Accuracy)
- RQ-02-11-20-005 (Planform Continuity)
- All structural interface requirements
