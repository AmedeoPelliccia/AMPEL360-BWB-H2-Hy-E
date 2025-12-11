# 10-PRT-PLN-004 - H2 System Prototype Plan

## 1. Prototype Plan Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-PRT-PLN-004 |
| Plan Type | System - Hydrogen Safety & Handling |
| TRL Target | 4-6 |
| Status | Active |
| Version | A |
| Date | 2025-12-10 |
| Author | AMPEL360 H2 Systems Team |

## 2. Executive Summary

This plan defines the prototyping strategy for hydrogen (H2) and liquid hydrogen (LH2) systems used during parking, mooring, and storage operations of the AMPEL360 BWB aircraft. Given the critical safety implications of H2 handling on the ground, this plan emphasizes validation of detection, venting, cryogenic component operation, and material compatibility.

The H2 systems prototyping program will advance from TRL 3-4 (proof-of-concept and component validation) to TRL 5-6 (system demonstration in relevant environment), providing essential safety data for certification.

## 3. Purpose and Objectives

### 3.1 Purpose
Develop and validate prototypes for safe H2/LH2 ground operations including:
- H2 leak detection systems
- H2 venting and dispersion systems
- Cryogenic valves for LH2 servicing
- Cryogenic insulation for LH2 systems
- Material compatibility with H2 and cryogenic conditions

### 3.2 Objectives
- Demonstrate H2 detection at 4% LEL (Lower Explosive Limit) with <1 second response
- Validate safe H2 venting with controlled dispersion (no accumulation)
- Prove cryogenic valve operation at -253°C (LH2 temperature)
- Demonstrate insulation performance for LH2 tank access points
- Validate material compatibility (no embrittlement, adequate sealing)
- Generate safety data for certification authorities
- Advance TRL from 3-4 to 5-6

### 3.3 Success Criteria
| Criterion | Metric | Target Value |
|-----------|--------|--------------|
| H2 Detection Sensitivity | % LEL detection | ≤ 4% LEL |
| H2 Detection Response Time | seconds | < 1.0 s |
| H2 Sensor False Alarm Rate | per year | < 5 |
| Vent Flow Rate | kg/min (LH2) | ≥ 10 kg/min (TBD) |
| Cryo Valve Operation | successful cycles at -253°C | ≥ 100 |
| Cryo Valve Leak Rate | mbar·L/s | < 1×10⁻⁶ |
| Insulation Performance | boil-off rate | < 2% per day |
| Material H2 Compatibility | cycles without embrittlement | ≥ 1000 |

## 4. Scope

### 4.1 In Scope
- **H2 Detection Prototypes**: Sensors, alarm integration, placement optimization
- **H2 Venting Prototypes**: Vent valves, vent stacks, dispersion analysis
- **Cryogenic Valve Prototypes**: LH2-compatible valves for servicing
- **Cryogenic Insulation Prototypes**: Multi-layer insulation (MLI), vacuum jackets
- **Material Testing**: H2 embrittlement, cryo cycling, seal performance
- **Proof-of-Concept Demonstrations**: Novel H2 safety technologies
- **Digital Twin**: H2 dispersion modeling

### 4.2 Out of Scope
- Onboard aircraft LH2 storage tanks (covered under ATA 28 or propulsion system)
- LH2 production or liquefaction equipment
- Ground-based LH2 storage tanks (GSE infrastructure)
- LH2 refueling systems (separate from parking/storage)
- Flight operations H2 systems

### 4.3 Technology Readiness Level
| Component | Current TRL | Target TRL | Strategy |
|-----------|-------------|------------|----------|
| H2 Detection | 4 | 6 | POC → prototype → field testing |
| H2 Venting | 3 | 5 | POC → prototype → CFD validation |
| Cryo Valves | 3 | 5 | Material testing → functional prototype |
| Cryo Insulation | 4 | 6 | Lab testing → system-level prototype |

## 5. Requirements Traceability

| Requirement ID | Description | Priority | Prototype |
|----------------|-------------|----------|-----------|
| REQ-10-00-H2-001 | H2 detection at 4% LEL | Critical | 10-PRT-PHY-005, 10-PRT-POC-001 |
| REQ-10-00-H2-002 | H2 venting safe dispersion | Critical | 10-PRT-PHY-004, 10-PRT-POC-003 |
| REQ-10-00-H2-003 | H2 sensor response time < 1s | Critical | 10-PRT-PHY-005 |
| REQ-10-00-H2-004 | Automatic shutdown on H2 detect | High | 10-PRT-POC-001 |
| REQ-10-00-CRY-001 | LH2 valve operation at -253°C | High | 10-PRT-PHY-004, 10-PRT-POC-002 |
| REQ-10-00-CRY-002 | Cryo insulation boil-off < 2%/day | High | 10-PRT-PHY-006 |
| REQ-10-00-CRY-003 | Cryo valve leak rate < 1×10⁻⁶ | High | 10-PRT-PHY-004 |
| REQ-10-00-MAT-001 | H2 material compatibility | High | Material testing program |
| REQ-10-00-MAT-002 | Cryo material performance | High | Material testing program |

## 6. Prototype Strategy

### 6.1 Prototyping Approach
**Three-Phase Approach**:

**Phase 1: Proof-of-Concept (Q1 2026)**
- H2 sensor technology evaluation (10-PRT-POC-001)
- Cryo valve feasibility at -253°C (10-PRT-POC-002)
- H2 venting dispersion simulation (10-PRT-POC-003)
- Material screening tests

**Phase 2: Component Prototypes (Q2-Q3 2026)**
- H2 detector prototype with alarm integration (10-PRT-PHY-005)
- H2 vent valve prototype (10-PRT-PHY-004)
- Cryo insulation prototype (10-PRT-PHY-006)
- Digital twin of H2 venting (10-PRT-DT-002)

**Phase 3: System Integration (Q4 2026)**
- Integrated H2 safety system demonstration
- Combined venting and detection testing
- Environmental testing (wind, temperature extremes)

### 6.2 Prototype Types
- [x] Physical Prototype - H2 detector, vent valve, insulation
- [x] Proof of Concept - Sensor technology, cryo valve operation
- [x] Mockup - H2 venting layout visualization
- [x] Digital Twin - H2 dispersion CFD modeling
- [ ] 3D Printed Parts - Limited use (not for H2-wetted parts)

### 6.3 Scale and Fidelity
- **H2 Detectors**: Full-scale prototypes (representative of production)
- **Vent Valve**: Full-scale prototype, representative flow rates
- **Cryo Insulation**: Component-level at full scale
- **Venting Mockup**: Reduced scale (1:10) for dispersion visualization, CFD validation

## 7. H2/BWB/Cryo Considerations

| Parameter | Applicable | Details |
|-----------|-----------|---------|
| H2 Related | Yes | Core focus of this plan |
| Cryo Related | Yes | LH2 at -253°C operations |
| BWB Specific | Partial | Integration with BWB ground operations |

### 7.1 H2 Safety Requirements
**Critical Safety Requirements**:
- **Material Selection**: 
  - 316/316L stainless steel for H2-wetted parts (proven compatibility)
  - Inconel 625/718 for high-stress H2 applications
  - PTFE, Kalrez for seals (no elastomers in H2 service)
- **Leak Testing**: 
  - Helium leak testing to 1×10⁻⁶ mbar·L/s or better
  - Pressure decay testing for all H2 systems
- **Ventilation**: 
  - Natural ventilation: > 5 air changes/hour
  - Forced ventilation if natural insufficient
  - Vent discharge at least 5m above grade, away from ignition sources
- **Detection**: 
  - Minimum 2 sensors per zone (redundancy)
  - Sensor placement: high points (H2 rises), low points (LH2 spills)
  - Sensor calibration every 6 months
- **Bonding/Grounding**: 
  - Bonding resistance < 1 ohm
  - Grounding to aircraft and GSE
- **Emergency Procedures**: 
  - Automatic valve shutoff on detection
  - Visual and audible alarms
  - Emergency shutdown accessible from multiple locations

### 7.2 Cryogenic Safety Requirements
- **PPE**: Cryogenic gloves (rated to -253°C), face shields, long-sleeve protection
- **Procedures**: 
  - Pre-cool procedures to minimize thermal shock
  - Slow valve operation to prevent pressure surges
  - Controlled warm-up after LH2 operations
- **Emergency**: 
  - Cryo spill kits at each LH2 access point
  - Oxygen monitoring (LH2 boil-off displaces O₂)
- **Materials**: 
  - All materials qualified to -253°C (tensile, impact, fatigue testing)
  - Minimum 100 thermal cycles in prototype testing

### 7.3 Special Facilities/Equipment
- **H2 Test Facility**: 
  - Outdoor test area with 15m (50 ft) clearance
  - Explosion-proof electrical equipment
  - H2 gas supply (compressed H2 for detection testing)
  - LH2 supply (small dewar, <50L for valve testing)
  - Adequate ventilation and wind monitoring
- **Cryo Test Chamber**: 
  - Cryostat capable of -253°C (26K)
  - LN₂ cooling (77K) for preliminary testing
  - Instrumentation feed-throughs
  - Pressure/temperature monitoring
- **Safety Equipment**: 
  - H2 detectors (permanent installation at test site)
  - Fire suppression (dry chemical, CO₂ - no water on LH2)
  - Emergency shutdown system
  - Personal H2 monitors for test personnel

## 8. Prototype Components

| Component | Doc Number | Type | Purpose | TRL |
|-----------|------------|------|---------|-----|
| H2 Vent Valve | 10-PRT-PHY-004 | Physical | Cryo valve operation | 3→5 |
| H2 Detector | 10-PRT-PHY-005 | Physical | Detection sensitivity | 4→6 |
| Cryo Insulation | 10-PRT-PHY-006 | Physical | Thermal performance | 4→6 |
| H2 Detection POC | 10-PRT-POC-001 | POC | Sensor technology | 3→4 |
| Cryo Valve POC | 10-PRT-POC-002 | POC | Feasibility at -253°C | 3→4 |
| H2 Venting POC | 10-PRT-POC-003 | POC | Safe dispersion | 3→4 |
| H2 Venting Mockup | 10-PRT-MCK-003 | Mockup | Layout visualization | 2→3 |
| H2 Venting Digital Twin | 10-PRT-DT-002 | Digital | Dispersion modeling | 3→5 |

## 9. Materials and Manufacturing

### 9.1 H2-Compatible Materials
| Material | Application | H2 Compatible | Cryo Compatible | Standard |
|----------|-------------|---------------|-----------------|----------|
| 316/316L SS | Valves, piping, fittings | Yes | Yes | ASTM A312 |
| Inconel 625 | High-stress valve internals | Yes | Yes | ASTM B443 |
| Monel 400 | Sealing surfaces | Yes | Yes | ASTM B127 |
| PTFE | Seals, gaskets | Yes | Yes | ASTM D4894 |
| Kalrez | High-performance seals | Yes | Yes | DuPont spec |
| Aluminum 6061-T6 | Non-wetted structures | No (H2 wetted) | Yes | ASTM B211 |

**Materials to Avoid**:
- Carbon steel (H2 embrittlement)
- Most elastomers (H2 permeation, cryo brittleness)
- Zinc-plated fasteners (liquid metal embrittlement with H2)

### 9.2 Manufacturing Methods
- **Welding**: TIG welding per AWS D10.4 (cryo service), orbital welding for repeatability
- **Machining**: CNC machining for precision valve components
- **Brazing**: Silver brazing for certain joints (avoid contamination)
- **Heat Treatment**: Solution annealing for austenitic stainless (reduce embrittlement susceptibility)
- **Surface Finish**: Electropolish for H2-wetted surfaces (reduce leak paths)

### 9.3 Quality Control
- **Weld Inspection**: Radiography (RT) or ultrasonic testing (UT) for all pressure-containing welds
- **Leak Testing**: 100% helium leak testing, acceptance < 1×10⁻⁶ mbar·L/s
- **Material Certification**: Mill certs for all H2-wetted materials
- **Cleanliness**: "LH2 clean" per NASA KSC-C-123 or equivalent (no hydrocarbons, moisture)

## 10. Testing and Validation Plan

### 10.1 Test Objectives
- Validate H2 detection sensitivity and response time
- Demonstrate safe H2 venting without accumulation
- Prove cryo valve operation and sealing at -253°C
- Validate insulation thermal performance
- Assess material compatibility over multiple cycles
- Generate safety data for certification

### 10.2 Test Types and Sequence

#### 10.2.1 Material Testing (Ongoing, start Q1 2026)
- H2 embrittlement testing per ASTM G142
- Cryogenic tensile testing per ASTM E1450
- Thermal cycling (ambient to -253°C, 100+ cycles)
- Seal leak testing at cryo temperatures

#### 10.2.2 H2 Detection Testing (Q2 2026)
- Sensor calibration and sensitivity (10-PRT-TST-005)
- Response time measurement
- False alarm rate assessment (long-duration test)
- Environmental effects (humidity, temperature, contaminants)
- Integration with alarm system

#### 10.2.3 H2 Venting Testing (Q2-Q3 2026)
- Cryo valve operation at -253°C (10-PRT-TST-003)
- Vent flow rate measurement
- H2 dispersion testing (outdoor, with wind monitoring)
- CFD validation with test data
- Emergency shutdown sequence

#### 10.2.4 Cryo Insulation Testing (Q3 2026)
- Thermal performance (boil-off rate) (10-PRT-TST-004)
- Vacuum integrity (for vacuum-jacketed insulation)
- Thermal cycling durability
- Installation/removal procedures

#### 10.2.5 System Integration Testing (Q4 2026)
- Combined detection and venting system
- Simulated LH2 servicing scenario
- Emergency response procedures
- Personnel training validation

### 10.3 Test Facilities
- **H2 Test Site**: Outdoor facility with H2 gas supply, wind monitoring, safety systems (Partner facility TBD, or build dedicated test pad)
- **Cryo Test Lab**: LH2 testing capability, either partner facility (NASA, national lab) or contracted service
- **Materials Lab**: Tensile testing, microscopy for embrittlement assessment (AMPEL360 or contracted)
- **CFD/Simulation**: In-house digital twin lab

## 11. Schedule and Milestones

| Milestone | Target Date | Dependencies | Status |
|-----------|-------------|--------------|--------|
| H2 Plan Approval | 2025-12-31 | This document | In Progress |
| Test Facility Access Secured | 2026-01-31 | Negotiations with partners | Planned |
| Material Testing Complete | 2026-03-31 | Material procurement | Planned |
| POC Phase Complete | 2026-03-31 | Initial testing | Planned |
| H2 Detector Prototype Delivery | 2026-05-31 | POC results | Planned |
| Vent Valve Prototype Delivery | 2026-06-30 | POC, materials test | Planned |
| Cryo Insulation Prototype Delivery | 2026-07-31 | Design, materials | Planned |
| Component Testing Complete | 2026-09-30 | All prototypes delivered | Planned |
| System Integration Testing | 2026-10-01 to 2026-12-31 | Component tests | Planned |
| H2 Systems Final Report | 2027-01-31 | All testing complete | Planned |

### 11.1 Critical Path
1. **Test Facility Access** - Long lead item, affects all testing
2. **Cryo Test Capability** - Limited availability, schedule early
3. **Material Qualification** - Must precede prototype fabrication
4. **Safety Approvals** - Required before H2 testing begins

## 12. Resources and Budget

### 12.1 Team
| Role | Name/Organization | Responsibility |
|------|-------------------|----------------|
| H2 Systems Lead | TBD | Overall H2 system prototyping |
| Cryo Specialist | TBD | Cryogenic component design |
| Safety Engineer | TBD | H2 safety analysis and test approvals |
| Test Engineer | TBD | Test execution |
| Materials Engineer | TBD | Material selection and qualification |
| CFD Analyst | TBD | H2 dispersion modeling |

### 12.2 Budget Estimate
| Category | Estimated Cost (USD) |
|----------|---------------------|
| Materials (H2-compatible, cryo-rated) | $80,000 |
| H2 Detectors (prototypes + commercial units) | $40,000 |
| Cryogenic Valves (custom prototypes) | $60,000 |
| Insulation Materials (MLI, vacuum jackets) | $30,000 |
| Test Facility Rental/Setup | $150,000 |
| LH2 Supply for Testing | $40,000 |
| Safety Equipment (sensors, alarms, PPE) | $30,000 |
| Material Testing (external lab) | $50,000 |
| CFD/Simulation Software/Compute | $20,000 |
| Labor (internal, 2 FTE for 1 year) | $250,000 |
| External Consultants (H2 safety) | $50,000 |
| Travel (to test sites) | $20,000 |
| Documentation | $10,000 |
| Contingency (25%, high risk) | $205,000 |
| **Total** | **$1,035,000** |

## 13. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| H2 test facility unavailable/delayed | Medium | High | Identify backup facilities; plan phased testing |
| Cryo test capability limited | High | High | Partner with NASA/national lab; portable LH2 dewar |
| Material embrittlement issues | Medium | High | Conservative material selection (316 SS, Inconel); early testing |
| H2 safety approval delays | Medium | High | Engage authorities early; detailed safety analysis |
| Prototype fabrication quality issues | Medium | Medium | Qualified welders/fabricators; rigorous QC |
| Budget overrun (cryo testing expensive) | Medium | High | Cost tracking; prioritize critical tests |
| LH2 supply interruptions | Medium | Medium | Coordinate with supplier; flexible schedule |
| Test results require redesign | High | High | Build schedule margin; iterative prototyping |
| Personnel safety incident | Low | Critical | Rigorous safety procedures; training; PPE; emergency drills |

## 14. Success Metrics and Evaluation

### 14.1 Key Performance Indicators
| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| H2 Detection Sensitivity | ≤ 4% LEL | Sensor calibration testing |
| H2 Detection Response | < 1 s | Time-stamped data logging |
| Cryo Valve Cycles | ≥ 100 at -253°C | Cyclic testing in cryostat |
| Cryo Valve Leak Rate | < 1×10⁻⁶ mbar·L/s | Helium leak testing |
| Insulation Performance | < 2% boil-off/day | Calorimetry testing |
| Material Cycles | ≥ 1000 H2 exposures | Fatigue testing |
| Safety Tests Passed | 100% | Test reports |

### 14.2 TRL Assessment Criteria
- **TRL 4**: Component and/or breadboard validation in laboratory environment
  - *Evidence*: POC tests, material tests, component tests in lab
- **TRL 5**: Component and/or breadboard validation in relevant environment
  - *Evidence*: Prototype tests in simulated ground operations, environmental testing
- **TRL 6**: System/subsystem model or prototype demonstration in a relevant environment
  - *Evidence*: Integrated H2 safety system test in representative outdoor environment

## 15. Documentation and Deliverables

- [x] H2 System Prototype Plan (this document)
- [ ] Proof-of-Concept Reports (10-PRT-POC-001, 002, 003)
- [ ] Prototype Specifications (10-PRT-PHY-004, 005, 006)
- [ ] CAD Models (vent valve, detector mounting, insulation design)
- [ ] Material Test Reports
- [ ] Test Plans (10-PRT-TST-003, 004, 005)
- [ ] Test Reports (10-PRT-TST-003, 004, 005)
- [ ] H2 System Prototype Report (10-PRT-RPT-002)
- [ ] Digital Twin Documentation (10-PRT-DT-002)
- [ ] H2 Safety Analysis Report (for certification)
- [ ] Lessons Learned (captured in 10-PRT-RPT-004)

## 16. References

### 16.1 Standards and Regulations
- **SAE AS6968**: Hydrogen Aircraft Ground Support Equipment
- **NFPA 2**: Hydrogen Technologies Code (2020 or later)
- **ISO 13984**: Liquid Hydrogen - Land Vehicle Fuel Tanks
- **ASME B31.12**: Hydrogen Piping and Pipelines
- **AWS D10.4**: Welding Austenitic Stainless Steel Tubing and Piping Systems in Sanitary Applications
- **ASTM G142**: Standard Test Method for Determination of Susceptibility of Metals to Embrittlement in Hydrogen Containing Environments at High Pressure, High Temperature, or Both
- **ASTM E1450**: Standard Test Method for Tensile Testing of Structural Alloys in Liquid Helium
- **NASA KSC-C-123**: Cleanliness of Components for Use in Oxygen, Fuel, and Pneumatic Systems

### 16.2 Related Documents
- 10-PRT-PLN-001: Master Prototyping Plan
- ATA_10-00-02_Safety: Safety analysis and hazards
- ATA_10-00-03_Requirements: H2 system requirements
- ATA_10-00-04_Design: H2 system design documentation

## 17. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| H2 Systems Lead | TBD | | YYYY-MM-DD |
| Safety Engineer | TBD | | YYYY-MM-DD |
| Test Manager | TBD | | YYYY-MM-DD |
| Prototyping Program Manager | TBD | | YYYY-MM-DD |
| Chief Engineer | TBD | | YYYY-MM-DD |

## 18. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-10 | AMPEL360 H2 Systems Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last Update**: 2025-12-10
