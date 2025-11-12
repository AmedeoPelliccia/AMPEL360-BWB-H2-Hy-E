# RQ-034: Girt Bar Attachment System

**Category:** RQ-FUNCTIONAL  
**ATA Chapter:** 52 - Doors  
**System:** 52-20 - Emergency Exits  
**Component:** 52-20-01 - Door L3 Aft Emergency Exit  
**Criticality:** Critical

---

## Requirement Statement

**RQ-52-20-01-034:** Girt Bar Attachment System

### Description

The Door L3 Aft Emergency Exit shall provide the following functional capability: **Girt Bar Attachment System**.

Slide attachment

This functional requirement is essential for emergency evacuation operations and must be validated through rigorous testing and demonstration.

**Status:** Defined

---

## Functional Specification

**Function:** Girt Bar Attachment System

**Criticality Level:** Critical

**Verification Method:** Test

**Operational Context:**
This function must be available and operational under all normal and emergency operating conditions, including:
- Ground operations
- Emergency evacuation scenarios
- Loss of power conditions
- Extreme environmental conditions

---

## Traceability

### Upstream Requirements
- Parent Requirement: SYS-FNC-001 (System Functional Requirements)
- Regulatory Basis: CS 25.807 - Emergency Exits
- Regulatory Basis: CS 25.809 - Emergency Exit Arrangement
- Regulatory Basis: CS 25.810 - Emergency Evacuation

### Downstream Implementation
- Design Document: [../../../04_DESIGN/](../../../04_DESIGN/)
- Interface Specification: [../../../05_INTERFACES/](../../../05_INTERFACES/)
- Engineering Analysis: [../../../06_ENGINEERING/](../../../06_ENGINEERING/)
- Verification Plan: [../../../07_V_AND_V/](../../../07_V_AND_V/)

---

## Verification

**Method:** Test

**Acceptance Criteria:**
- Function shall operate as specified under all conditions
- Response time shall meet performance requirements
- Function shall be fail-safe
- Manual override capability shall be demonstrated (where applicable)

**Verification Status:** Pending

**Test References:**
- Test Plan: [To be developed in 07_V_AND_V]
- Test Procedures: [To be developed]
- Test Reports: [To be completed]

---

## Related Requirements

**Functional Requirements:**
- RQ-52-20-01-020: Emergency Door Opening Capability
- RQ-52-20-01-021: Dual Activation Modes
- RQ-52-20-01-023: Automatic Slide Deployment

**Performance Requirements:**
- RQ-52-20-01-050: Door Opening Time (Powered)
- RQ-52-20-01-051: Door Opening Time (Manual)

**Safety Requirements:**
- RQ-52-20-01-100: Emergency Exit Safety
- RQ-52-20-01-101: Fail-Safe Operation

---

## Compliance & Standards

**Regulatory Requirements:**
- CS 25.807: Emergency exits
- CS 25.809: Emergency exit arrangement
- CS 25.810: Emergency evacuation
- TSO-C69c: Emergency Evacuation Slides

**Industry Standards:**
- SAE AS8015: Minimum Performance Standard for Escape Slide Systems
- SAE AIR1370: Aircraft Emergency Exits

---

## Design Considerations

**Key Factors:**
- Reliability under stress
- Ease of operation (panic scenarios)
- Redundancy and fail-safe design
- Maintenance accessibility
- Human factors engineering

**Risk Mitigation:**
- Dual redundant systems where critical
- Manual override capability
- Regular testing and inspection
- Crew training requirements

---

## Failure Modes & Effects

**Potential Failure Modes:**
- Loss of primary activation
- Mechanical jamming
- Power supply failure
- Environmental degradation

**Mitigation:**
- Manual backup systems
- Fail-safe mechanical design
- Regular preventive maintenance
- Environmental protection

---

## Notes

**Emergency Exit Specific:**
This functional requirement is critical for emergency evacuation and must meet all certification requirements under CS 25.807-810.

**CAOS Integration:**
Functional status shall be monitored by the CAOS (Computer Aided Operations & Services) system for health monitoring and predictive maintenance.

---

*This requirement is part of the AMPEL360 OPT-IN Framework for ATA 52-20-01 Door L3 Aft Emergency Exit.*

**Last Updated:** 2025-11-04  
**Document Version:** 1.0  
**Approval Status:** Defined
