# Test Plan - Operations
## ATA 02-00-00 GENERAL

**Document Number:** TP-02-00-00-001  
**Revision:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

---

## 1. Test Plan Overview

### 1.1 Purpose
This test plan defines the operational testing approach for the AMPEL360 BWB H₂ Hy-E Q100 aircraft, ensuring all operational procedures, systems, and interfaces are validated prior to entry into service.

### 1.2 Scope
- Normal operations testing
- Abnormal and emergency operations testing
- H₂ system operations testing
- CAOS integration testing
- Crew procedures validation
- Ground operations validation

### 1.3 Test Objectives
- Validate operational procedures are effective and safe
- Confirm H₂ refueling procedures meet safety and efficiency targets
- Verify CAOS advisory system integration
- Assess crew workload and situational awareness
- Demonstrate regulatory compliance

---

## 2. Test Organization

### 2.1 Test Team Structure
- **Test Director:** Overall test program management
- **Flight Test Lead:** Flight test execution and safety
- **Simulator Lead:** Simulator campaign coordination
- **Ground Test Lead:** Ground operations testing
- **Human Factors Lead:** Crew performance assessment
- **Safety Officer:** Test safety oversight

### 2.2 Responsibilities
- Test planning and execution
- Data collection and analysis
- Safety monitoring
- Issue identification and resolution
- Report generation

---

## 3. Test Phases

### 3.1 Phase 1: Simulator Testing (Complete Q4 2025)

#### 3.1.1 Normal Procedures Testing
**Test ID:** VAL-02-00-101  
**Objective:** Validate normal operational procedures  
**Success Criteria:**
- 100% procedure completion within target times
- Zero procedural errors by qualified crews
- Crew workload rating <70 (NASA TLX)

**Test Matrix:**
| Test Case | Procedure | Target Time | Crews Tested |
|-----------|-----------|-------------|--------------|
| TC-101-01 | Preflight | 15 min | 20 |
| TC-101-02 | Engine Start | 5 min | 20 |
| TC-101-03 | Taxi | Variable | 20 |
| TC-101-04 | Takeoff | 3 min | 20 |
| TC-101-05 | Climb | Variable | 20 |
| TC-101-06 | Cruise | Variable | 20 |
| TC-101-07 | Descent | Variable | 20 |
| TC-101-08 | Approach | 10 min | 20 |
| TC-101-09 | Landing | 5 min | 20 |
| TC-101-10 | Shutdown | 10 min | 20 |

#### 3.1.2 Abnormal Procedures Testing
**Test ID:** VAL-02-00-102  
**Objective:** Validate abnormal procedures and crew response  
**Success Criteria:**
- Correct procedure selection 100%
- Memory items completed <30 seconds
- Appropriate crew coordination demonstrated

**Test Scenarios:**
| Scenario | System Affected | Severity | Crews Tested |
|----------|----------------|----------|--------------|
| H₂ Leak Detection | Fuel System | High | 20 |
| CAOS Degradation | AI System | Medium | 15 |
| Single Engine Failure | Propulsion | High | 20 |
| Cabin Pressure Loss | ECS | High | 20 |
| Electrical Failure | Power | Medium | 15 |
| Hydraulic System Failure | Flight Controls | High | 20 |

#### 3.1.3 Emergency Procedures Testing
**Test ID:** VAL-02-00-103  
**Objective:** Validate emergency procedures and crew performance  
**Success Criteria:**
- Immediate action items <10 seconds
- Emergency landing success rate 100%
- Crew stress management demonstrated

**Emergency Scenarios:**
| Scenario | Type | Success Criteria | Crews |
|----------|------|------------------|-------|
| H₂ Fire | Fire | Suppression <60s | 20 |
| Dual Engine Failure | Propulsion | Safe landing | 20 |
| Emergency Descent | Pressurization | 10,000 ft <4 min | 15 |
| Emergency Evacuation | Safety | <90 seconds | 20 |

#### 3.1.4 H₂ Refueling Simulation
**Test ID:** VAL-02-00-104  
**Objective:** Validate H₂ refueling procedures  
**Success Criteria:**
- Refueling completion in <45 minutes
- Zero safety violations
- Proper crew coordination

#### 3.1.5 CAOS Integration Simulation
**Test ID:** VAL-02-00-105  
**Objective:** Validate CAOS advisory system integration  
**Success Criteria:**
- Advisory accuracy >85%
- Crew acceptance rate >80%
- Response time <2 seconds

---

### 3.2 Phase 2: Ground Validation (Q1 2026)

#### 3.2.1 Weight and Balance Ground Test
**Test ID:** VAL-02-00-201  
**Objective:** Validate weight and balance procedures  
**Test Activities:**
- Empty weight determination
- CG range verification
- Loading procedure validation
- Documentation accuracy check

**Success Criteria:**
- Weight measurement accuracy ±0.5%
- CG calculation accuracy ±1%
- Procedure completion time <2 hours

#### 3.2.2 H₂ Refueling Ground Test
**Test ID:** VAL-02-00-202  
**Objective:** Validate actual H₂ refueling operations  
**Test Activities:**
- Connection procedure validation
- Flow rate verification (target: 175 kg/min)
- Safety system testing
- Emergency disconnect testing

**Success Criteria:**
- Full refuel (8000 kg) in <45 minutes
- Zero leaks detected
- All safety interlocks functional
- Emergency disconnect <5 seconds

**Test Matrix:**
| Test | Parameter | Target | Acceptance |
|------|-----------|--------|------------|
| Refuel Time | Full tank | 45 min | 43-47 min |
| Flow Rate | kg/min | 175 | 165-185 |
| Temperature | Tank wall | <-253°C | Maintained |
| Pressure | Tank | 350 bar | 345-355 bar |

#### 3.2.3 Emergency Equipment Test
**Test ID:** VAL-02-00-203  
**Objective:** Validate emergency equipment accessibility and function  
**Test Activities:**
- Fire extinguisher access and operation
- Emergency oxygen system
- Emergency lighting system
- Evacuation equipment

**Success Criteria:**
- All equipment accessible within target times
- 100% functionality
- Crew proficiency demonstrated

---

### 3.3 Phase 3: Flight Test Validation (Q2-Q4 2026)

#### 3.3.1 Initial Flight Test Plan
**Test ID:** VAL-02-00-301  
**Objective:** Validate basic flight characteristics and handling  
**Flight Hours:** 50 hours  
**Test Flights:** 15 flights

**Test Areas:**
- Basic handling qualities
- Stability and control
- Performance envelope
- Systems integration
- Emergency procedures

#### 3.3.2 Performance Flight Tests
**Test ID:** VAL-02-00-302  
**Objective:** Validate aircraft performance specifications  
**Flight Hours:** 75 hours  
**Test Flights:** 20 flights

**Performance Parameters:**
| Parameter | Target | Test Method |
|-----------|--------|-------------|
| Range | 3500 NM | Long-range flight |
| Cruise Speed | Mach 0.82 | Speed sweep |
| Ceiling | 43,000 ft | Altitude climb |
| Fuel Efficiency | 0.8 kg H₂/NM | Cruise segments |
| Takeoff Distance | <2500 m | Multiple takeoffs |
| Landing Distance | <2000 m | Multiple landings |

#### 3.3.3 H₂ System Flight Tests
**Test ID:** VAL-02-00-303  
**Objective:** Validate H₂ fuel system in flight operations  
**Flight Hours:** 40 hours  
**Test Flights:** 12 flights

**Test Focus:**
- Fuel system performance at altitude
- Temperature management
- Pressure stability
- System redundancy
- Emergency procedures

#### 3.3.4 CAOS Flight Tests
**Test ID:** VAL-02-00-304  
**Objective:** Validate CAOS in operational environment  
**Flight Hours:** 35 hours  
**Test Flights:** 10 flights

**CAOS Validation:**
- Advisory accuracy in real operations
- Crew interaction and acceptance
- System reliability
- Decision support effectiveness
- Failure mode handling

**Success Criteria:**
- Advisory accuracy >85%
- System availability >99%
- Crew acceptance rating >80%
- Response time <2 seconds

---

### 3.4 Phase 4: Operational Validation (2027)

#### 3.4.1 Line Operations Safety Audit
**Test ID:** VAL-02-00-401  
**Objective:** Validate operational safety in service environment  
**Duration:** 6 months  
**Target:** 500+ operational flights

**LOSA Activities:**
- Threat and error management observation
- Procedural compliance assessment
- Crew performance evaluation
- Safety culture assessment

**Success Criteria:**
- Zero Category A/B events
- Threat management effectiveness >95%
- Error management effectiveness >90%
- Procedural compliance >98%

#### 3.4.2 Crew Procedures Validation
**Test ID:** VAL-02-00-402  
**Objective:** Validate crew procedures in line operations  
**Scope:** All operational procedures  
**Crews:** Minimum 50 line crews

**Validation Areas:**
- Procedure effectiveness
- Crew coordination
- Workload management
- Decision making
- Communication

#### 3.4.3 Maintenance Procedures Validation
**Test ID:** VAL-02-00-403  
**Objective:** Validate maintenance procedures and documentation  
**Duration:** 12 months  
**Target:** 1000+ maintenance tasks

**Validation Areas:**
- Procedure accuracy
- Task completion times
- Parts availability
- Documentation quality
- Training effectiveness

---

## 4. Test Data Requirements

### 4.1 Data Collection
- Flight parameters (1 Hz minimum)
- System states and status
- Crew actions and inputs
- Environmental conditions
- Video recording (critical phases)
- Audio recording (crew communication)

### 4.2 Data Analysis
- Statistical analysis of performance
- Trend analysis for anomalies
- Comparative analysis vs. requirements
- Human factors analysis
- Safety analysis

### 4.3 Data Management
- Secure data storage
- Version control
- Access control
- Retention policy (20 years minimum)

---

## 5. Safety Management

### 5.1 Safety Criteria
- No test shall exceed design limits
- Crew safety is paramount
- Environmental safety maintained
- Emergency procedures available and briefed
- Abort criteria clearly defined

### 5.2 Risk Assessment
- Pre-test risk assessment required
- Hazard identification and mitigation
- Safety review board approval
- Continuous risk monitoring

### 5.3 Emergency Procedures
- Test abort procedures
- Emergency landing sites
- Emergency response team
- Communications protocols

---

## 6. Test Schedule

### 6.1 Overall Timeline
| Phase | Start | End | Duration |
|-------|-------|-----|----------|
| Phase 1: Simulator | 2025-10-01 | 2025-12-31 | 3 months |
| Phase 2: Ground | 2026-01-01 | 2026-03-31 | 3 months |
| Phase 3: Flight Test | 2026-06-01 | 2026-12-31 | 7 months |
| Phase 4: Operational | 2027-01-01 | 2027-06-30 | 6 months |

### 6.2 Dependencies
- Simulator availability (Phase 1)
- Prototype completion (Phase 2)
- Regulatory approval (Phase 3)
- Type certification (Phase 4)
- Launch customer agreement (Phase 4)

---

## 7. Success Criteria Summary

### 7.1 Overall Program Success
- All test objectives met
- All requirements validated
- Regulatory compliance demonstrated
- Safety targets achieved
- Zero Category A/B safety events

### 7.2 Key Performance Indicators
| KPI | Target | Measurement |
|-----|--------|-------------|
| Test Completion Rate | 100% | Tests completed vs. planned |
| Safety Event Rate | 0 Cat A/B | Events per 1000 hours |
| Procedure Effectiveness | >95% | Success rate |
| Crew Acceptance | >85% | Survey rating |
| CAOS Accuracy | >85% | Correct advisories |
| H₂ Refuel Time | <45 min | Actual time |

---

## 8. Reporting

### 8.1 Test Reports
- Daily test logs
- Weekly progress reports
- Phase completion reports
- Final test campaign report
- Compliance report

### 8.2 Issue Reporting
- Real-time issue logging
- Daily issue review
- Weekly issue summary
- Monthly management report

---

## 9. Document Control

**Revision History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-05 | Test Team | Initial release |

**Approvals:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Director | TBD | | |
| Chief Engineer | TBD | | |
| Safety Officer | TBD | | |

---

**Document Status:** Active  
**Next Review Date:** 2025-12-05  
**Owner:** Test Director
