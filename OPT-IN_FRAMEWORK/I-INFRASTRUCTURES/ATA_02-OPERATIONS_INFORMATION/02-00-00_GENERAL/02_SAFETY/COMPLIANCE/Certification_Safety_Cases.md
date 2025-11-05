# Certification Safety Cases

**Document ID:** AMPEL360-02-10-00-SAF-CSC  
**Version:** 1.0.0  
**Date:** 2025-11-05  
**Status:** Released  
**Classification:** Safety Critical - Certification

## Purpose

This document presents the safety cases for certification of the AMPEL360 BWB H₂ Hy-E Q100 INTEGRA aircraft. Safety cases provide structured arguments, supported by evidence, that the aircraft meets all applicable safety requirements and is safe for its intended operation.

## Certification Basis

### Primary Regulations

**EASA CS-25 (Large Aeroplanes):**
- Amendment 27 (current)
- Special Conditions: H₂ fuel system, BWB configuration, AI/CAOS
- Equivalent Safety Findings: As required

**FAA 14 CFR Part 25 (Airworthiness Standards):**
- Amendment 25-149 (current)
- Special Conditions: Harmonized with EASA
- Equivalent Level of Safety (ELOS): As required

### Special Conditions

**SC-H2-001: Hydrogen Fuel System**
- Rationale: No existing CS-25 requirements for H₂ fuel
- Basis: ISO 19881, NFPA 2, SAE standards, industry best practices
- Acceptance: Equivalent safety to conventional fuel systems

**SC-BWB-001: Blended Wing Body Configuration**
- Rationale: Non-conventional configuration not covered by CS-25
- Basis: CS-25 intent applied to BWB, engineering analysis, testing
- Acceptance: Equivalent safety to conventional tube-and-wing

**SC-FC-001: Fuel Cell Propulsion**
- Rationale: Novel propulsion system not covered by CS-25
- Basis: IEC fuel cell standards, automotive fuel cell experience, aviation-specific testing
- Acceptance: Equivalent safety to conventional propulsion

**SC-AI-001: AI/CAOS System**
- Rationale: AI-enhanced systems not covered by CS-25
- Basis: EASA AI Roadmap, DO-178C Level A software, human oversight
- Acceptance: AI as advisory system, human authority retained

## Safety Case 1: Hydrogen Fuel System

### Claim

**The hydrogen fuel system is safe for commercial aviation operations and provides equivalent safety to conventional jet fuel systems.**

### Argument Structure

#### Level 1: Hazard Identification and Mitigation

**Claim 1.1: All H₂ fuel system hazards have been identified**

**Evidence:**
- Preliminary Hazard Analysis (PHA) - Document ID: AMPEL-PHA-H2-001
- Functional Hazard Assessment (FHA) - Document ID: AMPEL-FHA-H2-001
- HAZOP study (hydrogen-specific) - Document ID: AMPEL-HAZOP-H2-001
- Operational experience review (automotive, industrial H₂)
- Expert review (H₂ safety specialists)

**Sub-Claims:**
- 1.1.1: Leak hazards identified (ground and flight)
- 1.1.2: Fire/explosion hazards identified
- 1.1.3: Cryogenic hazards identified
- 1.1.4: Asphyxiation hazards identified
- 1.1.5: Material compatibility hazards identified

**Claim 1.2: All identified hazards are mitigated to acceptable levels**

**Evidence:**
- Risk Register - Risk_Register.csv
- FMEA - FMEA_General_Data.csv
- Fault Tree Analysis - Fault_Tree_Analysis.md
- Mitigation effectiveness analysis
- Residual risk acceptance by Chief Safety Officer

**Sub-Claims:**
- 1.2.1: H₂ leak detection effective (<100ms, demonstrated 85ms)
- 1.2.2: Emergency isolation effective (<500ms, demonstrated)
- 1.2.3: Ventilation adequate (50 ACH emergency mode, tested)
- 1.2.4: Fire suppression effective (2-shot HFC-227ea, tested)
- 1.2.5: Safety zones enforced (50m refueling, procedural)

#### Level 2: System Design and Verification

**Claim 2.1: H₂ system design meets safety requirements**

**Evidence:**
- System design description - Document ID: AMPEL-SYS-H2-001
- Safety requirements specification - Document ID: AMPEL-REQ-H2-SAF
- Design review reports (Preliminary, Critical, Final)
- Compliance matrix (ISO 19881, NFPA 2, SAE standards)
- EASA Special Condition SC-H2-001 compliance demonstration

**Sub-Claims:**
- 2.1.1: Double-wall fuel lines with leak detection
- 2.1.2: Fail-safe shutoff valves
- 2.1.3: Intrinsically safe equipment in H₂ zones
- 2.1.4: Redundant sensors (8 per zone)
- 2.1.5: Fire-rated compartments

**Claim 2.2: H₂ system performance verified through testing**

**Evidence:**
- Ground test reports (leak detection, isolation, ventilation)
- Flight test reports (system performance, failure modes)
- Certification test reports (EASA/FAA witnessed)
- Environmental testing (DO-160)
- Reliability demonstration (MTBF targets met)

**Sub-Claims:**
- 2.2.1: Leak detection response time <100ms (tested: 85ms)
- 2.2.2: Isolation response time <500ms (tested: achieved)
- 2.2.3: Ventilation capacity 50 ACH (tested: achieved)
- 2.2.4: Fire suppression effectiveness (tested: effective)
- 2.2.5: No single point failures leading to catastrophic event (verified)

#### Level 3: Operational Safety

**Claim 3.1: H₂ operational procedures are safe and effective**

**Evidence:**
- Operations Manual - H₂ procedures chapter
- Training program description
- Training completion records
- Procedural validation (simulator, operational trials)
- Human factors analysis

**Sub-Claims:**
- 3.1.1: Refueling procedures safe (50m zone, bonding, monitoring)
- 3.1.2: Emergency procedures effective (leak, fire response)
- 3.1.3: Personnel training adequate (8 hours ground ops, 16 hours maintenance)
- 3.1.4: Coordination with emergency services (CFR training completed)

**Claim 3.2: H₂ safety culture established**

**Evidence:**
- Safety Management System (SMS) - Document ID: AMPEL-SMS-001
- Safety training records
- Safety reporting system (mandatory and voluntary)
- Just culture policy
- Continuous improvement process

### Conclusion

The hydrogen fuel system safety case demonstrates that:
1. All hazards have been systematically identified
2. All hazards are mitigated to acceptable levels
3. System design meets safety requirements
4. System performance has been verified through testing
5. Operational procedures are safe and effective
6. Safety culture supports safe H₂ operations

**The H₂ fuel system provides equivalent safety to conventional jet fuel systems and is acceptable for certification.**

---

## Safety Case 2: BWB Configuration

### Claim

**The Blended Wing Body configuration is safe for commercial aviation operations and provides equivalent safety to conventional tube-and-wing aircraft.**

### Argument Structure

#### Level 1: Flight Safety

**Claim 1.1: BWB handling characteristics are safe**

**Evidence:**
- Flight dynamics analysis - Document ID: AMPEL-AERO-BWB-001
- Control law design report - Document ID: AMPEL-FCS-001
- Flight test reports (handling qualities evaluation)
- Pilot evaluations (test pilots, training pilots, line pilots)
- Simulator validation

**Sub-Claims:**
- 1.1.1: Flight envelope protection adequate (angle of attack, speed, bank limits)
- 1.1.2: Stall characteristics benign (early warning, docile stall)
- 1.1.3: Crosswind capability adequate (30 kt demonstrated)
- 1.1.4: Control power adequate (all flight phases)
- 1.1.5: Pilot workload acceptable (handling qualities Level 1)

**Claim 1.2: CG management is safe**

**Evidence:**
- CG range analysis - Document ID: AMPEL-LOAD-BWB-001
- CAOS CG monitoring validation
- Flight test (CG excursions, handling at limits)
- Failure analysis (fuel transfer failure, sensor failure)
- Pilot procedures and training

**Sub-Claims:**
- 1.2.1: CG range adequate (15-35% MAC demonstrated safe)
- 1.2.2: CAOS monitoring effective (real-time, ±0.1% MAC accuracy)
- 1.2.3: Alerts timely (±2% MAC caution, ±1% MAC warning)
- 1.2.4: Fuel transfer adequate (automatic and manual)
- 1.2.5: No unsafe CG excursion scenarios (FTA confirms)

#### Level 2: Structural Safety

**Claim 2.1: BWB structure meets strength requirements**

**Evidence:**
- Structural design report - Document ID: AMPEL-STR-BWB-001
- Structural analysis (FEA, hand calculations)
- Static testing (wing, fuselage, joints)
- Fatigue testing (120,000 cycles, 2× lifetime)
- Damage tolerance analysis

**Sub-Claims:**
- 2.1.1: Limit load (2.5g) with safety factor 1.5 (ultimate 3.75g)
- 2.1.2: Distributed load paths (no single point failures)
- 2.1.3: Damage tolerant design (detectability before critical)
- 2.1.4: Fatigue life 120,000 cycles (exceeds 90,000 design life)
- 2.1.5: Special attention to BWB-specific load paths (tested)

**Claim 2.2: BWB structure monitored in operation**

**Evidence:**
- Structural Health Monitoring (SHM) system design
- Fiber optic sensors (primary load paths)
- CAOS integration (anomaly detection)
- Maintenance program (inspection intervals)
- Fleet monitoring (data from all aircraft)

#### Level 3: Evacuation Safety

**Claim 3.1: BWB evacuation is safe and timely**

**Evidence:**
- Evacuation demonstration - 75 seconds (target 90 seconds)
- Exit layout analysis (12 exits optimized for BWB)
- Emergency lighting design (enhanced for wide cabin)
- Passenger flow simulation
- Crew training program

**Sub-Claims:**
- 3.1.1: Evacuation time <90 seconds (demonstrated 75 seconds)
- 3.1.2: Exit capacity adequate (880 persons/minute, need 147/minute)
- 3.1.3: Emergency lighting adequate (photometric testing)
- 3.1.4: Crew procedures effective (demonstrated in full-scale drill)
- 3.1.5: Passenger briefing adequate (BWB-specific safety card)

### Conclusion

The BWB configuration safety case demonstrates that:
1. BWB handling characteristics are safe and well-understood
2. CG management is effective and monitored
3. BWB structure meets all strength requirements
4. Structure is monitored for anomalies in operation
5. Evacuation is safe, timely, and well-practiced

**The BWB configuration provides equivalent safety to conventional tube-and-wing aircraft and is acceptable for certification.**

---

## Safety Case 3: Fuel Cell Propulsion

### Claim

**The fuel cell propulsion system is safe for commercial aviation operations and provides equivalent safety to conventional turbine engines.**

### Argument Structure

#### Level 1: System Reliability

**Claim 1.1: Fuel cell system reliability is adequate**

**Evidence:**
- Reliability analysis - Document ID: AMPEL-REL-FC-001
- FMEA (fuel cell components)
- FTA (total power loss)
- Operational data (automotive fuel cells, stationary fuel cells)
- Test data (AMPEL360 fuel cell stacks)

**Sub-Claims:**
- 1.1.1: Individual stack MTBF >10,000 FH (demonstrated 12,000 FH)
- 1.1.2: 4 stacks provide redundancy (operate on 2)
- 1.1.3: Common cause failures mitigated (design diversity)
- 1.1.4: Total power loss probability <10⁻⁶ /FH (FTA confirms)
- 1.1.5: Graceful degradation (automatic load shedding)

**Claim 1.2: Fuel cell safety hazards mitigated**

**Evidence:**
- Fuel cell hazard analysis - Document ID: AMPEL-HAZ-FC-001
- Thermal management design
- High voltage safety design (800V DC)
- Fire protection design
- Crew procedures and training

**Sub-Claims:**
- 1.2.1: Thermal runaway prevented (cooling redundancy, monitoring)
- 1.2.2: High voltage isolated (insulation, interlocks)
- 1.2.3: Fire detection and suppression (dedicated system)
- 1.2.4: Emergency shutdown safe (graceful, no hazards)
- 1.2.5: Maintenance procedures safe (lockout/tagout)

#### Level 2: Emergency Power

**Claim 2.1: Emergency electrical power available**

**Evidence:**
- Emergency power analysis - Document ID: AMPEL-PWR-EMER-001
- APU specification (emergency start, power output)
- Battery specification (capacity, duration)
- Load shedding logic
- Flight test (fuel cell failure scenarios)

**Sub-Claims:**
- 2.1.1: APU provides backup power (if fuel cells fail)
- 2.1.2: Battery provides final backup (30 minutes essential systems)
- 2.1.3: Load shedding automatic (priority to critical systems)
- 2.1.4: Emergency power sufficient (flight instruments, controls, comms)
- 2.1.5: Multiple failures required for total power loss (extremely improbable)

### Conclusion

The fuel cell propulsion safety case demonstrates that:
1. Fuel cell system reliability is adequate with redundancy
2. Fuel cell safety hazards are mitigated
3. Emergency electrical power is available
4. Total power loss is extremely improbable

**The fuel cell propulsion system provides equivalent safety to conventional turbine engines and is acceptable for certification.**

---

## Safety Case 4: CAOS AI System

### Claim

**The CAOS AI system enhances safety without introducing unacceptable risks.**

### Argument Structure

#### Level 1: Human Authority

**Claim 1.1: Human pilot retains authority**

**Evidence:**
- CAOS design philosophy document
- Human-machine interface design
- Override capability (one button, immediate)
- Training program (human authority emphasized)
- Operational procedures

**Sub-Claims:**
- 1.1.1: CAOS is advisory only, not prescriptive
- 1.1.2: Override is simple and immediate (one button)
- 1.1.3: Pilot can accept, modify, or reject any CAOS recommendation
- 1.1.4: No automation surprise (transparent AI decisions)
- 1.1.5: Legal authority remains with pilot (unchanged)

**Claim 1.2: CAOS failure does not compromise safety**

**Evidence:**
- CAOS failure modes analysis
- Independent Safety Monitor design
- Conventional systems independence
- Flight test (CAOS failures simulated)
- Pilot training (CAOS-inoperative operations)

**Sub-Claims:**
- 1.2.1: All conventional systems independent of CAOS
- 1.2.2: CAOS failure detected (self-monitoring + ISM)
- 1.2.3: Revert to conventional displays automatic
- 1.2.4: Aircraft fully operable without CAOS
- 1.2.5: Pilots trained for CAOS-inoperative operations

#### Level 2: CAOS Reliability

**Claim 2.1: CAOS advisory is reliable**

**Evidence:**
- CAOS validation report - Document ID: AMPEL-CAOS-VAL-001
- False positive rate: 3.2% (target <5%)
- False negative rate: 0.8% (target <1%)
- Independent Safety Monitor effectiveness
- Operational feedback (pilot surveys)

**Sub-Claims:**
- 2.1.1: False positive rate acceptable (3.2% < 5% target)
- 2.1.2: False negative rate acceptable (0.8% < 1% target)
- 2.1.3: ISM catches most false positives (99% detection)
- 2.1.4: Crew verification process effective (training)
- 2.1.5: Continuous improvement (operational data feedback)

### Conclusion

The CAOS AI system safety case demonstrates that:
1. Human pilot retains authority at all times
2. CAOS failure does not compromise safety
3. CAOS advisory is reliable with acceptable error rates
4. Independent Safety Monitor provides additional protection
5. CAOS enhances safety as an additional layer

**The CAOS AI system enhances safety without introducing unacceptable risks and is acceptable for certification.**

---

## Overall Safety Argument

### Integration of Safety Cases

The four individual safety cases (H₂ fuel system, BWB configuration, fuel cell propulsion, CAOS AI) are integrated to form the overall safety argument for the AMPEL360 aircraft:

1. **Novel technologies individually safe:** Each novel system meets safety requirements
2. **Integration considered:** System interactions analyzed (e.g., H₂ leak + electrical failure)
3. **Defense in depth:** Multiple independent safety barriers
4. **No single point failures:** Redundancy prevents single failures causing catastrophic events
5. **Human factors:** Pilot training, procedures, and authority appropriate
6. **Continuous improvement:** Safety performance monitored, lessons learned incorporated

### Top-Level Claim

**The AMPEL360 BWB H₂ Hy-E Q100 INTEGRA aircraft is safe for commercial aviation operations and meets all applicable certification requirements.**

### Supporting Evidence

- All individual safety cases (above)
- Integrated system safety assessment - Document ID: AMPEL-SSA-001
- Flight test program completion
- Certification test completion
- Compliance matrix (CS-25 + Special Conditions)
- EASA/FAA approval (pending)

---

**Document Owner:** Chief Engineer - Certification / Head of Safety  
**Next Review Date:** 2026-11-05 (or upon certification)  
**Configuration Control:** Git SHA-256: [hash]  
**Classification:** Safety Critical - Certification  
**Distribution:** Certification authorities, senior management, safety committee
