# 10-VV-VPL-004 - H₂ Safety Verification Plan for Parking, Mooring, and Storage

## 1. Document Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-VV-VPL-004 |
| V&V Type | Verification Plan |
| Verification Method | Test + Analysis + Inspection |
| Status | Active |
| Revision | A |
| Date | 2025-12-10 |

## 2. Purpose

This H₂ Safety Verification Plan establishes the comprehensive verification strategy for hydrogen safety systems and procedures related to parking, mooring, and storage of the AMPEL360 BWB H₂ aircraft. It ensures that all H₂-related safety requirements are verified through appropriate testing, analysis, and inspection.

## 3. Scope

### 3.1 H₂ Systems Covered
- H₂ leak detection systems during parking/storage
- H₂ venting systems for grounded aircraft
- Cryogenic LH₂ preservation systems
- H₂ safety zones and exclusion areas
- Ground H₂ system monitoring
- Emergency response systems
- H₂ bonding and grounding systems
- Personnel safety equipment and procedures

### 3.2 Storage Conditions
- Short-term parking (< 24 hours)
- Medium-term storage (1-7 days)
- Long-term storage (> 7 days)
- Extended preservation (> 30 days)

### 3.3 Environmental Conditions
- Temperature: -40°C to +50°C ambient
- Cryogenic: -253°C (LH₂ temperature)
- Wind speeds: 0-50 knots
- Various humidity conditions

## 4. Applicable Documents

### 4.1 H₂-Specific Standards
- [SAE AS6968](https://www.sae.org/standards/content/as6968/) - Hydrogen Aviation Fuel Cells and Tanks
- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) - Hydrogen Technologies Code (2020 Edition)
- [ISO 13984](https://www.iso.org/standard/23585.html) - Liquid Hydrogen - Land Vehicle Fuelling System Interface
- [ISO 14687](https://www.iso.org/standard/69539.html) - Hydrogen Fuel Quality - Product Specification
- EASA Special Conditions for H₂ Aircraft
- FAA Policy Memo on H₂ Propulsion

### 4.2 Safety Standards
- [SAE ARP4761](https://www.sae.org/standards/content/arp4761/) - Safety Assessment Process
- [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) - Equipment, Systems, and Installations
- SAE ARP4754A - Development Assurance
- MIL-STD-882E - System Safety

### 4.3 Related AMPEL360 Documents
- 10-00-02_Safety/H2_Safety_Assessment
- 10-00-03_Requirements/H2_Safety_Requirements
- 10-00-04_Design/H2_System_Design

## 5. H₂ Safety Requirements Overview

### 5.1 Requirements Categories

| Category | Count | DAL | Primary Verification |
|----------|-------|-----|---------------------|
| Leak Detection | 15 | A | Test |
| Venting System | 12 | A | Test + Analysis |
| Dispersion Safety | 10 | A | Analysis + Test |
| Cryogenic Safety | 18 | A | Test |
| Safety Zones | 8 | B | Analysis + Demonstration |
| Bonding/Grounding | 6 | B | Test + Inspection |
| Monitoring Systems | 14 | A | Test |
| Emergency Response | 10 | B | Demonstration + Test |
| Personnel Protection | 8 | C | Inspection + Demonstration |
| **Total** | **101** | | |

### 5.2 Design Assurance Levels (DAL)
- **DAL A (Catastrophic)**: Failure could result in H₂ explosion or major fire
- **DAL B (Hazardous)**: Failure could result in localized H₂ fire or injury
- **DAL C (Major)**: Failure could result in H₂ leak without immediate danger

## 6. Verification Strategy

### 6.1 H₂ Leak Detection System Verification

#### 6.1.1 Test Requirements
- **Test**: 10-VV-TST-005_H2_Leak_Detection_Test.md
- **Sensor Types**: Electrochemical, catalytic bead, thermal conductivity
- **Detection Threshold**: ≤ 10% LEL (Lower Explosive Limit)
- **Response Time**: < 1 second
- **Coverage**: 100% of critical zones

#### 6.1.2 Test Conditions
- Calibration verification at installation
- Detection threshold testing with known H₂ concentrations
- Response time measurement
- Alarm activation verification
- Integration with aircraft systems
- Environmental testing (-40°C to +50°C)

#### 6.1.3 Pass/Fail Criteria
| Parameter | Requirement | Tolerance |
|-----------|-------------|-----------|
| Detection Threshold | ≤ 10% LEL | ±5% |
| Response Time | < 1.0 sec | ±0.1 sec |
| Alarm Activation | Visual + Audible | 100% reliability |
| Sensor Lifetime | > 2 years | Demonstrated |

### 6.2 H₂ Venting System Verification

#### 6.2.1 Test Requirements
- **Test**: 10-VV-TST-006_H2_Venting_Test.md
- **Vent Valve Operation**: Open/close functionality at -253°C
- **Flow Rate**: Sufficient to prevent over-pressure
- **Safe Dispersion**: H₂ concentration < 4% vol at 10m distance

#### 6.2.2 Analysis Requirements
- **Analysis**: 10-VV-ANL-002_H2_Safety_Analysis_Verification.md
- **CFD Modeling**: H₂ dispersion patterns
- **Worst-Case Scenarios**: Maximum vent rate, minimum ventilation
- **Safety Distances**: Exclusion zones based on dispersion

#### 6.2.3 Test Conditions
- Vent valve operation at cryogenic temperatures
- Flow rate measurement under various conditions
- Dispersion measurement in outdoor test facility
- Wind tunnel testing for various wind conditions

### 6.3 Cryogenic System Verification

#### 6.3.1 Test Requirements
- **Test**: 10-VV-TST-007_Cryo_System_Test.md
- **Material Testing**: Compatibility at -253°C
- **Valve Operation**: Functionality at cryogenic temperatures
- **Insulation Performance**: Boiloff rate limits
- **Thermal Cycling**: 100 cycles minimum

#### 6.3.2 Test Specimens
- Valve samples (10 specimens)
- Insulation samples (15 specimens)
- Seal samples (20 specimens)
- Structural joints (10 specimens)

#### 6.3.3 Pass/Fail Criteria
| Component | Test | Requirement | Tolerance |
|-----------|------|-------------|-----------|
| Valves | Operation at -253°C | 100% functionality | No failures |
| Insulation | Thermal conductivity | < 0.02 W/m·K | ±10% |
| Seals | Leak rate | < 1×10⁻⁶ mbar·L/s | ±20% |
| Joints | Structural integrity | No cracks/failures | Zero defects |

### 6.4 LH₂ Preservation Verification

#### 6.4.1 Test Requirements
- **Test**: 10-VV-TST-008_LH2_Preservation_Test.md
- **Duration**: 30-day minimum storage test
- **Boiloff Rate**: < 2% per day (target: 0.5%)
- **Pressure Management**: Maintain safe pressure range
- **Temperature Monitoring**: Continuous monitoring

#### 6.4.2 Test Setup
- Full-scale LH₂ tank or representative test article
- Environmental chamber for temperature control
- Continuous data acquisition
- Remote monitoring and alarms

#### 6.4.3 Measurements
- Daily boiloff rate
- Tank pressure (continuous)
- Tank temperature distribution
- Ambient conditions
- Insulation performance

## 7. Safety Zone Verification

### 7.1 H₂ Safety Zones

#### 7.1.1 Zone Definitions
- **Zone 1 (Exclusion)**: 0-5m from vent outlets - No personnel
- **Zone 2 (Controlled)**: 5-15m from vents - Trained personnel only
- **Zone 3 (Monitored)**: 15-30m from vents - General access with monitoring

#### 7.1.2 Verification Method
- **Analysis**: CFD dispersion modeling
- **Test**: Actual H₂ dispersion measurements
- **Demonstration**: Safety zone marking and procedures

#### 7.1.3 Dispersion Analysis
- **Tool**: FLUENT or PHAST
- **Scenarios**: Maximum vent rate, various wind conditions
- **Criteria**: H₂ concentration < 4% vol outside Zone 1

### 7.2 Bonding and Grounding Verification

#### 7.2.1 Test Requirements
- Ground resistance: < 10 ohms
- Bonding continuity: < 0.1 ohms
- Static discharge path verification

#### 7.2.2 Test Procedure
- Pre-flight bonding check procedure
- Ground cart bonding verification
- Personnel grounding verification

## 8. Emergency Response Verification

### 8.1 Emergency Procedures
- H₂ leak response procedure
- Fire suppression procedure
- Evacuation procedure
- Emergency venting procedure

### 8.2 Verification Method
- **Demonstration**: Emergency drills (quarterly)
- **Test**: Emergency equipment functionality
- **Training**: Personnel certification

### 8.3 Emergency Equipment
- H₂ fire extinguishers (Class D)
- Emergency ventilation systems
- Personal protective equipment
- Emergency shutdown systems

## 9. Inspection Program

### 9.1 Pre-Parking Inspection
- **Procedure**: 10-VV-INS-003_H2_System_Inspection.md
- **Frequency**: Before each parking period
- **Items**: Leak detection sensors, vent valves, grounding, safety equipment

### 9.2 During-Storage Inspection
- **Frequency**: Daily for long-term storage
- **Items**: Pressure levels, temperature, sensor functionality, safety zones

### 9.3 Post-Storage Inspection
- **Frequency**: Before return to service
- **Items**: Full H₂ system inspection, leak test, functional test

## 10. Validation Activities

### 10.1 Operational Validation
- **Document**: validation-activities/10-VV-VAL-002_H2_Safety_Validation.md
- **Activities**: Actual parking/storage operations
- **Duration**: 6-month validation period
- **Scenarios**: Various storage durations and conditions

### 10.2 Long-Term Performance
- Extended storage (> 30 days)
- Multiple thermal cycles
- Various environmental conditions
- Maintenance procedure validation

## 11. Compliance Evidence

### 11.1 SAE AS6968 Compliance
- **Matrix**: compliance-evidence/10-VV-CMP-002_H2_Regulations_Compliance.md
- **Key Requirements**: Storage safety, leak detection, venting, emergency response
- **Status Tracking**: Continuous compliance monitoring

### 11.2 NFPA 2 Compliance
- **Matrix**: compliance-evidence/10-VV-CMP-003_NFPA2_Compliance.md
- **Key Requirements**: Safety distances, ventilation, electrical classification
- **Verification**: Inspection and analysis

### 11.3 Special Conditions
- EASA Special Conditions for H₂ Aircraft
- FAA equivalency findings
- Custom compliance methods as needed

## 12. Test Facilities and Equipment

### 12.1 H₂ Safety Test Facility Requirements
- Outdoor test area with adequate ventilation
- H₂ gas supply system (controlled release)
- Safety monitoring systems
- Remote control capability
- Emergency response equipment

### 12.2 Cryogenic Test Facility Requirements
- Cryogenic chamber (-253°C capability)
- LH₂ handling equipment
- Thermal cycling equipment
- Safety systems for cryogenic testing

### 12.3 Instrumentation
- H₂ concentration sensors (various types)
- Temperature sensors (cryogenic rated)
- Pressure sensors
- Flow meters
- Data acquisition systems

## 13. Safety Precautions for Testing

### 13.1 Personnel Safety
- H₂ safety training mandatory
- Cryogenic safety training
- PPE requirements: Face shields, cryogenic gloves, safety shoes
- Medical surveillance program

### 13.2 Test Safety
- Safety plan for each test
- Minimum safe distances
- Emergency procedures posted
- Fire suppression equipment available
- Medical support on standby

### 13.3 Environmental Protection
- H₂ venting to safe areas
- No ignition sources
- Weather restrictions (wind, rain)
- Environmental monitoring

## 14. Schedule

### 14.1 Verification Milestones

| Milestone | Target Date | Dependencies |
|-----------|-------------|--------------|
| H₂ Leak Detection System Test Complete | M+8 | Sensors delivered |
| Venting System Test Complete | M+10 | Test facility ready |
| Cryogenic System Test Complete | M+12 | LH₂ supply available |
| LH₂ Preservation Test Complete | M+16 | 30-day test duration |
| Safety Zone Validation Complete | M+14 | CFD analysis complete |
| Emergency Response Validation Complete | M+18 | Personnel trained |
| H₂ Safety Verification Complete | M+20 | All tests complete |

### 14.2 Critical Path
1. Facility preparation (M+0 to M+3)
2. Equipment procurement (M+0 to M+6)
3. Component testing (M+6 to M+12)
4. System integration testing (M+10 to M+16)
5. Operational validation (M+14 to M+20)

## 15. Reporting

### 15.1 Test Reports
- Individual test reports: Within 2 weeks of completion
- H₂ safety summary report: Quarterly
- Final H₂ safety verification report: M+20

### 15.2 Compliance Reports
- SAE AS6968 compliance status: Quarterly
- NFPA 2 compliance status: Quarterly
- Special conditions compliance: As required by authority

## 16. Risk Management

### 16.1 H₂ Safety Risks

| Risk | Severity | Likelihood | Mitigation |
|------|----------|-----------|------------|
| H₂ leak during testing | Catastrophic | Medium | Remote operation, safety zones, detection |
| Cryogenic injury | Hazardous | Low | PPE, training, procedures |
| Test equipment failure | Major | Medium | Backup equipment, maintenance |
| Inadequate ventilation | Hazardous | Low | CFD verification, monitoring |

### 16.2 Risk Controls
- Safety review before each test
- Continuous H₂ monitoring during tests
- Emergency response team on standby
- Weather monitoring and restrictions

## 17. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| H₂ Safety Manager | | | |
| V&V Manager | | | |
| Chief Engineer | | | |
| QA Manager | | | |
| Certification Manager | | | |

## 18. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-10 | AMPEL360 H₂ Safety Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-10
