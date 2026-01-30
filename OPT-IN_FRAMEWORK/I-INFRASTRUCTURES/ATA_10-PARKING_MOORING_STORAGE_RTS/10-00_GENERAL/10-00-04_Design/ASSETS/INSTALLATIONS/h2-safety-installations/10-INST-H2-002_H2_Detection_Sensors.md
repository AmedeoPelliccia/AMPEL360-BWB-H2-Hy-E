# 10-INST-H2-002 - H2 Detection Sensors

## 1. Purpose

Installation and calibration procedures for hydrogen detection sensors used during parking and ground operations of AMPEL360-BWB-H2 aircraft.

## 2. Scope

- H2 sensor types and specifications
- Sensor placement and coverage requirements
- Installation procedures and calibration
- Alarm configuration and response

**Effectivity**: All parking facilities supporting AMPEL360-BWB-H2 operations

## 3. Applicable Documents

- **NFPA 2** - Hydrogen Technologies Code
- **IEC 60079** - Explosive atmospheres
- **ISA-12.13.01** - Performance Requirements for Combustible Gas Detectors
- **SAE AS6968** - Hydrogen Aircraft GSE

## 4. Safety Precautions

⚠️ **WARNINGS**

- H2 detection system is critical safety equipment - failures must be addressed immediately
- Never disable or bypass H2 detection during aircraft operations
- Personnel must evacuate immediately upon 50% LEL alarm
- Only intrinsically safe or explosion-proof equipment in H2 zones

⚠️ **CAUTIONS**

- Sensors require regular calibration (monthly minimum)
- Sensor lifespan typically 2-5 years - track and replace
- False alarms must be investigated, not ignored
- Test sensors with span gas, not H2 (safety hazard)

## 5. H2 Detection Sensor Types

### 5.1 Catalytic Bead Sensors

**Principle**: Combustion of H2 on catalytic surface generates heat
**Range**: 0-100% LEL (0-4% H2)
**Response Time**: 10-30 seconds
**Accuracy**: ±5% of reading
**Advantages**: Reliable, well-proven technology
**Disadvantages**: Poisoning by silicones, lead; oxygen required

**Application**: Primary detection method for parking areas

### 5.2 Electrochemical Sensors

**Principle**: H2 oxidation generates electrical current
**Range**: 0-4% H2 (or higher)
**Response Time**: <10 seconds
**Accuracy**: ±5% of reading
**Advantages**: Fast response, low power
**Disadvantages**: Limited lifespan (2-3 years), humidity sensitive

**Application**: Portable detection equipment, backup sensors

### 5.3 Thermal Conductivity Sensors

**Principle**: H2 has high thermal conductivity vs air
**Range**: 0-100% H2
**Response Time**: 10-60 seconds
**Accuracy**: ±2% of full scale
**Advantages**: No oxygen required, long life, not poisoned
**Disadvantages**: Cross-sensitivity to other gases

**Application**: High-concentration monitoring, enclosed spaces

## 6. Sensor Placement Requirements

### 6.1 Detection Coverage Zones

**Zone 1 - Critical Area** (0-25 ft from H2 interface):
- Sensor density: 1 sensor per 500 ft² floor area
- Sensor height: Ceiling level (H2 rises) + Mid-level + Low level
- Response time: <10 seconds
- Alarm setpoint: 25% LEL (warning), 50% LEL (danger)

**Zone 2 - Controlled Area** (25-50 ft from H2 interface):
- Sensor density: 1 sensor per 1000 ft² floor area
- Sensor height: Ceiling level + Mid-level
- Response time: <30 seconds
- Alarm setpoint: 25% LEL (warning), 50% LEL (danger)

**Zone 3 - General Area** (50+ ft from H2 interface):
- Sensor density: 1 sensor per 2000 ft² floor area
- Sensor height: Ceiling level
- Response time: <60 seconds
- Alarm setpoint: 25% LEL (warning), 50% LEL (danger)

### 6.2 Specific Sensor Locations

**Required Sensor Positions**:

1. **Vent Outlet Area** (4 sensors minimum)
   - Positioned in circle around vent outlet
   - Radius: 5 ft from vent centerline
   - Height: Same as vent outlet discharge height
   - Purpose: Detect vent leaks or backflow

2. **Fuel Connection Points** (2 sensors per connection)
   - One at ceiling level above connection
   - One at connection height
   - Distance: Within 5 ft of connection
   - Purpose: Detect fueling/defueling leaks

3. **Aircraft Perimeter** (4-6 sensors)
   - Positioned around aircraft at 90° intervals
   - Distance: 10-15 ft from aircraft
   - Height: Ceiling level
   - Purpose: Detect H2 migration from aircraft

4. **Ground Level** (2-4 sensors for enclosed parking)
   - Floor level or 1 ft above floor
   - Near low points and corners
   - Purpose: Detect cold H2 vapor (may settle initially)

5. **Air Intake/HVAC** (1 sensor per intake)
   - At or near ventilation air intakes
   - Purpose: Prevent H2 being drawn into building systems

## 7. Installation Procedure

### 7.1 Pre-Installation Planning

1. **Survey parking area**
   - Measure area dimensions
   - Identify H2 sources (fuel connection, vents)
   - Locate existing electrical services
   - Identify mounting locations (walls, ceilings, poles)

2. **Calculate sensor requirements**
   - Apply density requirements per zone
   - Add sensors at required specific locations
   - Verify coverage with no dead zones
   - Plan sensor network wiring

3. **Select sensor models**
   - Verify sensors meet specifications
   - Check certifications (FM, CSA, ATEX, IECEx)
   - Confirm compatibility with alarm system
   - Verify power requirements

### 7.2 Sensor Installation

**Mounting Instructions**:

1. **Select mounting location**
   - Avoid dead air spaces (corners, behind obstructions)
   - Minimum 1 ft from walls/ceilings if not surface-mounted
   - Protected from mechanical damage
   - Accessible for maintenance and calibration

2. **Install mounting bracket** (if required)
   - Use stainless steel or aluminum (corrosion resistance)
   - Secure to structure per manufacturer requirements
   - Verify level and alignment

3. **Mount sensor**
   - Orient sensor per manufacturer instructions (sample intake direction)
   - Secure firmly (vibration resistant)
   - Verify sensing element not obstructed

4. **Connect wiring**
   - Use wiring appropriate for classified area (explosion-proof conduit)
   - Follow wiring diagram from sensor and alarm system
   - Typical: 4-20 mA analog output or digital communication
   - Connect power, signal, and ground/shield
   - Label all wiring clearly

5. **Configure sensor**
   - Set sensor address (if network system)
   - Configure alarm setpoints: 25% LEL (low), 50% LEL (high)
   - Set relays for alarm outputs (if local)
   - Enable trending/datalogging (if available)

### 7.3 System Integration

1. **Connect to central alarm system**
   - Wire all sensors to centralized monitoring panel
   - Configure zone identification (per sensor location)
   - Set up alarm prioritization
   - Configure notification (audible, visual, remote)

2. **Test communication**
   - Verify each sensor communicates with central system
   - Check signal integrity (no dropouts or noise)
   - Test alarm transmission (apply test gas)

3. **Install alarm devices**
   - Audible alarm: Horn/siren (min 90 dB)
   - Visual alarm: Strobe lights (red for danger)
   - Remote notification: Auto-dial, email, SMS (if equipped)
   - Status display: Annunciator panel showing sensor readings

## 8. Calibration and Testing

### 8.1 Initial Calibration

**Calibration Procedure** (perform at installation):

1. **Zero calibration**
   - Expose sensor to fresh air (0% H2)
   - Allow sensor to stabilize (5 minutes minimum)
   - Perform zero/baseline calibration per manufacturer

2. **Span calibration**
   - Apply certified span gas (typically 50% LEL, 2% H2 in air)
   - Allow sensor to stabilize and read span gas
   - Adjust sensor to read correct span value
   - Verify reading within ±5% of span gas value

3. **Alarm testing**
   - Apply gas to trigger low alarm (25% LEL)
   - Verify low alarm activates
   - Apply gas to trigger high alarm (50% LEL)
   - Verify high alarm activates
   - Verify alarm notification (audible, visual, remote)

### 8.2 Periodic Calibration

**Frequency**:
- Monthly: Functional test (apply test gas, verify alarm)
- Quarterly: Span calibration check
- Annually: Full calibration (zero and span) + functional test

**Calibration Record**:
- Date and time
- Sensor location/ID
- Calibration gas used (concentration, lot number)
- Zero and span readings
- Adjustments made
- Pass/fail result
- Technician name and signature

### 8.3 Functional Testing

**Monthly Functional Test**:

1. Apply test gas to sensor (50% LEL)
2. Verify sensor reads correct value (within ±10%)
3. Verify low alarm activates (25% LEL threshold)
4. Verify high alarm activates (50% LEL threshold)
5. Verify audible and visual alarms activate
6. Verify remote notification (if equipped)
7. Document test results

**Bump Test** (daily recommended during operations):
- Quick exposure of sensor to test gas
- Verify sensor responds and alarms
- Takes <1 minute per sensor
- Identifies failed sensors immediately

## 9. Alarm Response Procedures

### 9.1 Low Alarm (25% LEL, 1% H2)

**Warning Level**:

1. Acknowledge alarm (do not silence)
2. Notify ground supervisor
3. Investigate source (visual inspection from safe distance)
4. Increase ventilation (if enclosed parking)
5. Monitor adjacent sensors for spread
6. Do not continue H2 operations until source identified
7. If concentration increasing or not decreasing, evacuate and escalate to High Alarm procedures

### 9.2 High Alarm (50% LEL, 2% H2)

**Danger Level**:

1. **Evacuate area immediately** (all personnel)
2. **Activate emergency alarm** (site-wide notification)
3. **Shut down non-essential electrical equipment** (if safe to do so)
4. **Activate emergency ventilation** (maximum rate)
5. **Summon emergency response team**
6. **Do not re-enter until H2 <25% LEL** and authorized
7. **Investigate and repair H2 source** before resuming operations

## 10. BWB Considerations

- BWB upper surface sensor placement may require elevated mounting
- Wide wingspan requires more sensors for coverage
- Integrated wing-body creates larger enclosed volume (hangar)
- Distributed fuel tanks may have multiple H2 sources

## 11. Quality Assurance

- Maintain calibration records for all sensors
- Track sensor lifespan and schedule replacement
- Document all alarms and investigations
- Review false alarm rate (target <1 per month per sensor)
- Annual system performance review

## 12. Cross-References

- **10-INST-H2-001** - H2 Venting System Installation
- **10-INST-H2-003** - Cryo Safety Equipment
- **NFPA 2** - Hydrogen Technologies Code
- **IEC 60079** - Explosive Atmospheres

## 13. Revision History

| Rev | Date       | Author              | Description          |
|-----|------------|---------------------|----------------------|
| A   | 2025-12-09 | Amedeo Pelliccia    | Initial release      |

---

## Document Control

- **Document ID**: 10-INST-H2-002
- **Revision**: A
- **Status**: DRAFT - Subject to human review and approval
- **Safety Critical**: YES
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
