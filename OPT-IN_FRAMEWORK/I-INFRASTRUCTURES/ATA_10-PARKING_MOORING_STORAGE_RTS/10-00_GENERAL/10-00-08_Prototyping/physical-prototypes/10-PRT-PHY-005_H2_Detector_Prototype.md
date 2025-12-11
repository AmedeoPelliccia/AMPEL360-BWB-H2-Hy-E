# 10-PRT-PHY-005 - H2 Detector Prototype

## 1. Prototype Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-PRT-PHY-005 |
| Prototype Type | Physical |
| TRL Level | 4→6 |
| Status | Design |
| Version | A |
| Date | 2025-12-10 |
| Author | AMPEL360 H2 Safety Team |

## 2. Purpose

Develop and validate a hydrogen (H2) detection system for ground operations safety during parking, mooring, and storage of the AMPEL360 BWB aircraft. The detector must provide reliable, fast-response H2 leak detection to enable immediate response and prevent hazardous accumulations.

### 2.1 Background
Hydrogen is colorless, odorless, highly flammable (4-75% by volume in air), and has low ignition energy (0.02 mJ). Safe ground operations require continuous monitoring for H2 leaks. This prototype validates a detection system meeting aerospace safety standards with detection at 4% LEL (Lower Explosive Limit, equivalent to 1.6% H2 by volume) and response time < 1 second.

### 2.2 Objectives
- Demonstrate H2 detection sensitivity ≤ 4% LEL (0.16% H2 by volume)
- Validate response time < 1 second
- Assess false alarm rate (target < 5 per year)
- Evaluate environmental robustness (temperature, humidity, vibration)
- Integrate with alarm system and automatic shutoff
- Generate certification data for H2 safety system

## 3. Scope

### 3.1 What the Prototype Represents
Full-scale, production-representative H2 detection system including:
- H2 sensor element (catalytic bead, electrochemical, or other technology)
- Signal processing electronics
- Alarm output interface
- Power supply interface
- Mounting hardware

### 3.2 Limitations
- Testing conducted in controlled environment (lab and outdoor test pad)
- Limited long-term exposure testing (months vs. years)
- Certification testing (e.g., FAA/EASA) to follow prototype validation

### 3.3 Use Cases
- Continuous H2 monitoring during LH2 servicing
- Leak detection during aircraft parking/storage
- Area monitoring in enclosed hangars
- Integration with automatic H2 vent valve actuation

## 4. Design Basis

### 4.1 Related Design Documents
- ATA_10-00-02_Safety: H2 hazard analysis
- ATA_10-00-04_Design: H2 safety system design
- 10-PRT-PLN-004: H2 System Prototype Plan
- 10-PRT-POC-001: H2 Detection POC (sensor technology trade study)

### 4.2 Requirements Addressed
| Requirement ID | Description | Verification Method |
|----------------|-------------|---------------------|
| REQ-10-00-H2-001 | H2 detection at 4% LEL | Calibration testing (10-PRT-TST-005) |
| REQ-10-00-H2-003 | Response time < 1 second | Time-stamped data logging |
| REQ-10-00-H2-004 | Auto shutdown on detection | Integration testing |
| REQ-10-00-H2-005 | Redundant sensors (min 2/zone) | System architecture review |
| REQ-10-00-ENV-001 | Operation -40°C to +50°C | Environmental chamber testing |
| REQ-10-00-ENV-002 | Humidity 0-100% RH | Environmental chamber testing |

### 4.3 Design Constraints
- Must use intrinsically safe design (no ignition source in hazardous area)
- Power consumption < 5W per sensor (continuous operation)
- Output must interface with aircraft 28 VDC power and alarm system
- Sensor element life ≥ 5 years or 10,000 hours
- Maintenance: sensor replacement only (no calibration in field)

## 5. Prototype Specifications

### 5.1 Physical Characteristics
| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| Sensor Head Dimensions | 80 x 60 x 40 | mm | ±5 |
| Sensor Weight | 0.3 | kg | ±0.05 |
| Cable Length | 10 | m | ±1 |
| Electronics Box Dimensions | 150 x 100 x 50 | mm | ±5 |
| Electronics Box Weight | 0.8 | kg | ±0.1 |
| Scale | Full-scale | - | - |

### 5.2 Material Specifications
| Component | Material | Specification | Justification |
|-----------|----------|--------------|---------------|
| Sensor Housing | 316 SS | ASTM A240 | Corrosion-resistant, H2 safe |
| Sintered Filter (dust) | 316 SS | 40 μm pore | Protect sensor, allow H2 diffusion |
| Electronics Enclosure | Aluminum | 6061-T6 | Lightweight, EMI shielding |
| Cable | Shielded twisted pair | AWG 22 | Signal integrity, noise immunity |
| Connector | Circular, IP67 | MIL-DTL-38999 | Environmental sealing |
| Sensor Element | Catalytic bead or electrochemical | Commercial | Based on POC selection |

### 5.3 Manufacturing Method
- **Primary Method**: Integration of COTS (Commercial Off-The-Shelf) H2 sensor with custom electronics
- **Secondary Processes**: 
  - CNC machining for sensor housing and mounting bracket
  - PCB assembly for signal conditioning electronics
  - Potting/conformal coating for electronics protection
- **Quality Standards**: 
  - IPC-A-610 for PCB assembly
  - ISO 9001 for overall manufacturing

### 5.4 Performance Specifications
| Parameter | Specification | Unit | Verification Method |
|-----------|--------------|------|---------------------|
| Detection Range | 0 to 100 | % LEL (0-4% H2 vol.) | Calibration test (10-PRT-TST-005) |
| Alarm Threshold | 4 | % LEL (0.16% H2) | Calibration test |
| Response Time (T90) | < 1 | second | Step response test |
| Accuracy | ±5 | % of reading | Calibration against known standards |
| Operating Temperature | -40 to +50 | °C | Environmental chamber test |
| Storage Temperature | -50 to +70 | °C | Specification (not tested) |
| Humidity | 0 to 100 | % RH, non-condensing | Humidity chamber test |
| Vibration Resistance | 5 | g (10-200 Hz) | Vibration table test |
| Sensor Life | ≥ 5 | years or 10,000 hrs | Accelerated aging test (partial) |
| False Alarm Rate | < 5 | per year | Long-term monitoring (months) |
| Power Consumption | < 5 | W | Power measurement |

## 6. H2/BWB/Cryo Considerations

### 6.1 System Classification
| Parameter | Value | Details |
|-----------|-------|---------|
| H2 Related | Yes | Core function: H2 detection |
| Cryo Related | Partial | Sensor may be near LH2 (cold environment) |
| BWB Specific | No | Generic sensor, not BWB-geometry-specific |

### 6.2 H2 Safety Requirements
- **Intrinsic Safety**: Sensor head must be intrinsically safe (Class I, Div 1 or Zone 1 rating) or installed outside hazardous area with sampling line
- **Sensor Placement**: 
  - High points (H2 rises, lighter than air)
  - Near LH2 tank vent outlets
  - Low points if LH2 spill risk (cold H2 vapor can be denser than air initially)
- **Redundancy**: Minimum 2 sensors per detection zone (voting logic: 1-out-of-2 for alarm)
- **Calibration**: Factory calibration, field verification every 6 months with known H2 concentration
- **Alarm Integration**: 
  - Visual alarm (flashing beacon)
  - Audible alarm (horn, ≥85 dB)
  - Automatic vent valve actuation
  - Automatic shutdown of LH2 transfer (if applicable)

### 6.3 Cryogenic Requirements
- **Cold Environment**: Sensor may experience -50°C or colder near LH2 tank
  - Sensor housing: 316 SS handles cryo temperatures
  - Electronics: Heater or insulation to keep electronics above -40°C operating limit
- **Condensation**: Moisture may condense on sensor in cold areas
  - Sintered filter prevents liquid ingress
  - Sensor design must handle condensation without false alarms

### 6.4 BWB-Specific Requirements
Not directly applicable (generic sensor). BWB integration considerations:
- Multiple sensors required due to wide aircraft footprint
- Sensor placement optimized for BWB LH2 tank locations

### 6.5 Special Safety Requirements
| Hazard | Severity | Mitigation |
|--------|----------|------------|
| Sensor fails to detect H2 (false negative) | Catastrophic | Redundant sensors, periodic calibration verification, self-test function |
| False alarm (false positive) | Minor | Proper sensor selection, calibration, environmental testing, 1-out-of-2 voting |
| Sensor ignition source | Catastrophic | Intrinsically safe design, explosion-proof enclosure if not intrinsically safe |
| Sensor failure/degradation | Hazardous | Sensor health monitoring, replacement schedule (5 years), self-test |

## 7. Manufacturing Plan

### 7.1 Process Flow
1. **Sensor Selection**: Based on POC results (catalytic bead, electrochemical, or other) (complete by Q1 2026)
2. **COTS Sensor Procurement**: Order commercial H2 sensor module (4 weeks lead time)
3. **Custom Housing Design & Fabrication**: CNC machine 316 SS housing, sintered filter (3 weeks)
4. **Electronics Design**: Signal conditioning PCB design (2 weeks)
5. **PCB Fabrication & Assembly**: External PCB vendor (4 weeks)
6. **Integration**: Sensor into housing, electronics assembly (1 week)
7. **Potting/Conformal Coating**: Electronics protection (1 week)
8. **Cable & Connector Assembly**: Shielded cable, connector (3 days)
9. **Calibration**: Factory calibration with known H2 standards (1 week)
10. **Testing**: Functional, environmental, durability (3 weeks)

### 7.2 Manufacturing Procedures
- **Sensor Handling**: ESD precautions for sensor element
- **Housing Assembly**: Clean parts, verify O-ring seals, torque fasteners to spec
- **Electronics Assembly**: Per IPC-A-610 Class 2 (aerospace)
- **Calibration**: NIST-traceable H2 standards, document calibration curve

### 7.3 Quality Control Points
| Stage | Inspection | Acceptance Criteria |
|-------|------------|---------------------|
| COTS Sensor Receipt | Datasheet verification, visual inspection | Meets datasheet specs, no damage |
| Housing Machining | Dimensional inspection | Dimensions within tolerance |
| PCB Assembly | Visual inspection, AOI | No shorts, opens, solder defects per IPC-A-610 |
| Sensor Integration | Leak test (housing O-rings) | No leaks with pressurized air |
| Calibration | Multi-point calibration (0, 1%, 2%, 4% LEL) | Accuracy ±5% of reading |
| Functional Test | Response to H2 challenge gas | Response time < 1 s, alarm activates |
| Environmental Test | Temperature cycling, humidity | No failures, performance within spec |

### 7.4 Schedule
| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Sensor Technology Selection (POC) | 2026-03-31 | Planned |
| Design Freeze | 2026-04-30 | Planned |
| COTS Sensor Procurement | 2026-05-31 | Planned |
| Custom Parts Fabrication | 2026-05-31 | Planned |
| Integration Complete | 2026-06-15 | Planned |
| Calibration & Testing | 2026-06-30 | Planned |
| Delivery to System Integration | 2026-07-15 | Planned |

### 7.5 Cost Estimate
| Item | Cost (USD) |
|------|-----------|
| COTS H2 Sensor (qty 3 for testing) | $6,000 ($2,000 each) |
| Custom Housing (316 SS, machining) | $2,500 |
| Sintered Filter | $300 |
| Custom Electronics PCB (design, fab, assy) | $4,000 |
| Cable & Connectors | $500 |
| Enclosures (electronics box) | $800 |
| Calibration Gas (H2 standards) | $1,000 |
| Testing (environmental chamber rental) | $3,000 |
| Labor (integration, testing) | $5,000 |
| Documentation | $1,000 |
| Contingency (20%) | $4,820 |
| **Total** | **$28,920** |

## 8. Test Plan Overview

### 8.1 Test Objectives
- Validate H2 detection sensitivity (≤ 4% LEL)
- Measure response time (< 1 s)
- Assess false alarm rate (long-term monitoring)
- Environmental qualification (-40°C to +50°C, 0-100% RH)
- Vibration/shock resistance
- Sensor life (accelerated aging if feasible)

### 8.2 Test Types
- [x] Calibration Testing (multiple H2 concentrations)
- [x] Response Time Testing (step input, time-stamped logging)
- [x] Environmental Testing (temperature, humidity chambers)
- [x] Vibration Testing (vibration table, 5g, 10-200 Hz)
- [x] False Alarm Assessment (long-term monitoring in clean air and with interferents)
- [x] Integration Testing (with alarm system, vent valve actuation)
- [ ] Accelerated Aging (if time permits, simulate years of operation)

### 8.3 Test Plan Reference
Detailed test procedures in **10-PRT-TST-005: H2 Detector Prototype Test Plan**.

## 9. Results Summary

[To be completed after testing - Q2-Q3 2026]

### 9.1 Test Results
| Test | Result | Pass/Fail | Comments |
|------|--------|-----------|----------|
| Calibration (0-4% LEL) | TBD | TBD | To be completed |
| Response Time | TBD | TBD | To be completed |
| Accuracy | TBD | TBD | To be completed |
| Low Temperature (-40°C) | TBD | TBD | To be completed |
| High Temperature (+50°C) | TBD | TBD | To be completed |
| Humidity (100% RH) | TBD | TBD | To be completed |
| Vibration (5g) | TBD | TBD | To be completed |
| False Alarm Rate | TBD | TBD | To be completed |
| Alarm Integration | TBD | TBD | To be completed |

### 9.2 Performance Against Specifications
[Analysis to be completed after testing]

## 10. Lessons Learned

[To be completed after testing and evaluation]

### 10.1 Design Lessons
- TBD

### 10.2 Manufacturing Lessons
- TBD

### 10.3 Testing Lessons
- TBD

## 11. Recommendations

### 11.1 Next Steps
- [Pending test results]

### 11.2 Production Considerations
- [To be determined based on prototype performance]

### 11.3 Design Improvements
- [To be identified during testing]

## 12. Attachments and References

### 12.1 CAD Files
- 10-PRT-PHY-005-CAD-001: Sensor housing assembly
- 10-PRT-PHY-005-CAD-002: Mounting bracket

### 12.2 Schematics
- 10-PRT-PHY-005-SCH-001: Signal conditioning circuit

### 12.3 Photos
- [To be added during fabrication and testing]

### 12.4 Related Documents
- 10-PRT-PLN-004: H2 System Prototype Plan
- 10-PRT-POC-001: H2 Detection POC (sensor technology selection)
- 10-PRT-TST-005: H2 Detector Prototype Test Plan
- 10-PRT-RPT-002: H2 System Prototype Report

## 13. Standards and Regulations

### 13.1 Applicable Standards
- **SAE AS6968**: Hydrogen Aircraft Ground Support Equipment
- **NFPA 2**: Hydrogen Technologies Code (H2 detection requirements)
- **IEC 60079-29-1**: Explosive Atmospheres - Gas Detectors - Performance Requirements
- **ISA 12.13.01**: Performance Requirements for Combustible Gas Detectors
- **IPC-A-610**: Acceptability of Electronic Assemblies
- **ISO 26142**: Hydrogen Detection Apparatus - Stationary Applications

### 13.2 Compliance Notes
- Sensor design to meet IEC 60079-29-1 Type 2 (continuous monitoring)
- Detection at ≤25% LEL (4% LEL exceeds requirement)
- Response time T90 < 30 s (1 s exceeds requirement)
- Intrinsically safe or explosion-proof design per IEC 60079 series

## 14. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Design Engineer | TBD | | YYYY-MM-DD |
| H2 Safety Lead | TBD | | YYYY-MM-DD |
| Safety Officer | TBD | | YYYY-MM-DD |
| Test Engineer | TBD | | YYYY-MM-DD |
| Electronics Engineer | TBD | | YYYY-MM-DD |

## 15. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-10 | AMPEL360 H2 Safety Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last Update**: 2025-12-10
