# Weight Data Collection

**Component Code:** 02-10-00  
**Component Name:** AIRCRAFT_GENERAL_DATA  
**Subfolder:** 09_PRODUCTION_PLANNING/DATA_GENERATION  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100 INTEGRA

## Overview

This document establishes procedures for collecting accurate weight and center of gravity (CG) data for the AMPEL360 aircraft throughout the production lifecycle. Weight data is critical for flight safety, performance calculations, and regulatory compliance.

## Weight Categories

### 1. Basic Empty Weight (BEW)
- **Definition:** Weight of aircraft structure, powerplant, fixed equipment, unusable fuel, and full operating fluids
- **Includes:**
  - Airframe structure (BWB composite structure)
  - Fuel cell propulsion system
  - H₂ storage system (empty tanks)
  - Avionics and electrical systems
  - Hydraulic system (full fluid)
  - Fixed cabin equipment and furnishings
  - CAOS system hardware
  - Unusable H₂ fuel residual

### 2. Operating Empty Weight (OEW)
- **Definition:** BEW plus crew, crew baggage, catering, removable equipment
- **Variable Items:**
  - Flight crew and baggage
  - Cabin crew and baggage
  - Potable water and lavatory chemicals
  - Catering supplies
  - Removable emergency equipment
  - Operator-specific equipment

### 3. Maximum Structural Weights
- **Maximum Ramp Weight (MRW):** Maximum weight for ground operations
- **Maximum Takeoff Weight (MTOW):** Maximum weight for takeoff
- **Maximum Landing Weight (MLW):** Maximum weight for landing
- **Maximum Zero Fuel Weight (MZFW):** Maximum weight with no usable fuel

## Weighing Procedures

### Pre-Weighing Preparation

#### Aircraft Configuration
1. **Leveling**
   - Position aircraft on level weighing platform
   - Use electronic level or spirit level to verify aircraft is level per datum
   - Adjust landing gear if necessary to achieve level attitude
   - Document any deviations from standard level position

2. **Systems Preparation**
   - Drain H₂ fuel system to residual (unusable) quantity
   - Fill hydraulic system to specified level
   - Set pneumatic system to atmospheric pressure
   - Fill water system to specified level (or empty per procedure)
   - Remove all loose equipment not part of BEW

3. **Equipment Verification**
   - Verify all permanently installed equipment is present
   - Document any missing items with weight adjustments
   - Ensure all access panels and doors are closed and secured
   - Check for foreign objects or debris

#### Weighing Equipment Setup
1. **Load Cell Placement**
   - Position calibrated load cells under each landing gear
   - Ensure load cells are on stable, level surface
   - Verify load cell capacity exceeds expected loads
   - Check calibration certificates are current (within 6 months)

2. **Environmental Conditions**
   - Record ambient temperature (acceptable range: 10-30°C)
   - Record atmospheric pressure
   - Ensure no wind or air movement in hangar
   - Document any conditions outside normal parameters

### Weighing Execution

#### Measurement Process
1. **Initial Readings**
   - Zero all load cells before aircraft loading
   - Record tare weights if using platforms
   - Allow load cells to stabilize (minimum 5 minutes)
   - Verify no external loads on aircraft (chocks, jacks, etc.)

2. **Weight Measurement**
   - Record weight on each landing gear simultaneously
   - Take multiple readings (minimum 3) for verification
   - Calculate average of readings if variation is within tolerance
   - Document any anomalies or unusual readings

3. **Tare Corrections**
   - Subtract weight of platforms, adapters, or fixtures
   - Apply temperature corrections if required
   - Account for landing gear shock strut position
   - Document all correction factors applied

#### CG Calculation
1. **Longitudinal CG**
   - Measure arm (horizontal distance) from each gear to datum
   - Calculate moment for each gear (weight × arm)
   - Sum moments and divide by total weight
   - Express as percentage of Mean Aerodynamic Chord (MAC)

2. **Lateral CG**
   - Measure lateral offset of each gear from centerline
   - Calculate lateral moment for each gear
   - Verify lateral CG is within limits (typically near centerline)
   - Document any asymmetry

3. **Vertical CG**
   - Calculate using standard formulas for landing gear geometry
   - Account for BWB-specific geometry
   - Verify against design predictions

### Data Recording

#### Weighing Data Sheet
Record the following information:
- Aircraft serial number (MSN)
- Date and time of weighing
- Weighing personnel (names and certifications)
- Ambient conditions
- Weight readings for each gear (main left, main right, nose)
- Total aircraft weight
- Calculated CG location (longitudinal, lateral, vertical)
- Equipment calibration data
- Deviations from standard configuration

#### Weight and Balance Report
Generate comprehensive report including:
- Summary of weights and CG
- Comparison to design predictions
- Equipment list with individual weights
- Moment calculations
- Loading limitations
- Certification statement

## BWB-Specific Considerations

### Center Body Weight Distribution
- Large center body area requires careful load distribution analysis
- Multiple load paths for weight transmission to landing gear
- Wing-body blending affects CG calculations
- Wider CG range than conventional aircraft

### H₂ System Weight Effects
- Empty H₂ tanks weight and CG contribution
- Tank mounting structure weight
- Cryogenic insulation weight
- H₂ fuel system plumbing and valves

### Composite Structure Considerations
- Lighter weight than metal structure
- Weight variation between composite layups
- Moisture absorption effects on weight
- Long-term weight growth monitoring

## Production vs. Prototype Weighing

### Prototype Aircraft
- **Frequency:** Multiple weighings during development
- **Detail Level:** Extensive subsystem weight breakdown
- **Purpose:** Validate weight predictions, identify weight growth
- **Documentation:** Comprehensive as-weighed report with analysis

### Production Aircraft
- **Frequency:** Each aircraft after final assembly
- **Detail Level:** Standard weight and balance report
- **Purpose:** Certification, flight safety, operations
- **Documentation:** Standard format suitable for AFM

## Weight Growth Management

### Weight Tracking
- Track weight growth from design to production
- Identify sources of weight increase
- Implement weight reduction initiatives
- Monitor trends across serial numbers

### Design Changes
- Assess weight impact of all design changes
- Update weight predictions in design database
- Communicate weight changes to certification authority
- Adjust loading limitations if required

## Quality Assurance

### Measurement Accuracy
- **Load Cell Accuracy:** ±0.1% of reading minimum
- **Total Weight Accuracy:** ±0.25% of total weight
- **CG Location Accuracy:** ±0.5% MAC
- **Repeatability:** Multiple measurements within ±0.5%

### Verification and Validation
1. **Independent Verification**
   - Second person verifies all calculations
   - Quality inspector reviews weighing procedure compliance
   - Engineering reviews unusual or out-of-tolerance results

2. **Validation Methods**
   - Compare to design predictions (should be within 2%)
   - Compare to previous serial numbers (trend analysis)
   - Verify against similar aircraft configurations
   - Flight test validation of CG location

### Non-Conformances
- Document any weights outside tolerance
- Engineering review and disposition
- Corrective action if required
- Update certification documentation

## Integration with CAOS System

### Digital Weight Management
- Automatic data entry into CAOS database
- Real-time weight tracking during production
- Predictive weight analysis for future aircraft
- Fleet-wide weight trend monitoring

### AI-Assisted Analysis
- Anomaly detection in weighing data
- Automated comparison to predictions
- Weight optimization recommendations
- Configuration management integration

## Deliverables

### Prototype Phase
- **Document:** Prototype Weighing Report
- **Content:** Detailed weight breakdown, CG analysis, comparison to predictions
- **Timeline:** Within 1 week of weighing
- **Approval:** Chief Engineer and Certification Authority

### Production Phase
- **Document:** Aircraft Weight and Balance Report
- **Content:** Standard W&B data, equipment list, loading limitations
- **Timeline:** Within 3 days of weighing
- **Approval:** Quality Assurance and Flight Operations

### Type Certificate Data Sheet
- **Document:** TCDS Weight Limitations
- **Content:** Certified weights, CG limits, weight limitations
- **Timeline:** Certification + 30 days
- **Approval:** Certification Authority (EASA/FAA)

## Training Requirements

### Weighing Personnel
- Certified weighing technician course completion
- BWB-specific procedures training
- Load cell operation and calibration verification
- CG calculation methods for BWB configuration

### Quality Inspectors
- Weight and balance principles
- Acceptance criteria and tolerance limits
- Non-conformance disposition procedures
- Regulatory requirements knowledge

## Related Documents
- ATA 02-20-00: Weight and Balance
- ATA 02-21-00: Empty Weight Data
- ATA 02-26-00: Weighing Procedures
- ATA 08-00-00: Leveling and Weighing

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-05 | AMPEL360 Engineering | Initial release |

---

**Document Control:**
- Version: 1.0
- Status: Active
- Classification: Flight Safety Critical
- Next Review: Post-prototype weighing
