# RQ-100: No Single Failure Prevents Opening

**Category:** RQ-SAFETY  
**ATA Chapter:** 52 - Doors  
**System:** 52-20 - Emergency Exits  
**Component:** 52-20-01 - Door L3 Aft Emergency Exit  
**Safety Classification:** Catastrophic

---

## Requirement Statement

**RQ-52-20-01-100:** No Single Failure Prevents Opening

### Description

The Door L3 Aft Emergency Exit shall meet the following safety requirement: **No Single Failure Prevents Opening**.

This safety requirement is critical for ensuring safe operation and emergency evacuation capability. Failure to meet this requirement could result in catastrophic consequences.

**Status:** Defined

---

## Safety Specification

**Safety Classification:** Catastrophic

**Failure Probability Target:** <10E-9

**Verification Method:** Analysis

**Safety Rationale:**
This requirement ensures that the emergency exit system operates safely and reliably under all conditions, including failure scenarios. The design shall prevent hazardous situations and ensure evacuation capability is maintained.

---

## Traceability

### Upstream Requirements
- Parent Requirement: SYS-SAF-001 (System Safety Requirements)
- Safety Assessment: [../../02_SAFETY/FHA.md](../../02_SAFETY/)
- Regulatory Basis: CS 25.1309 - Equipment, systems, and installations
- Regulatory Basis: CS 25.810 - Emergency evacuation

### Downstream Implementation
- Design Document: [../../../04_DESIGN/](../../../04_DESIGN/)
- FMEA Analysis: [../../../02_SAFETY/FMEA.md](../../../02_SAFETY/)
- FTA Analysis: [../../../02_SAFETY/FTA.md](../../../02_SAFETY/)
- Verification Plan: [../../../07_V_AND_V/](../../../07_V_AND_V/)

---

## Verification

**Method:** Analysis

**Acceptance Criteria:**
- Safety analysis shall demonstrate compliance with probability targets
- No single failure shall result in loss of function (for Catastrophic/Hazardous)
- Failure detection and annunciation shall be provided
- All failure modes shall be identified and mitigated

**Verification Status:** Pending

**Analysis References:**
- FMEA: [To be completed in 02_SAFETY]
- FTA: [To be completed in 02_SAFETY]
- Test Plan: [To be developed in 07_V_AND_V]

---

## Related Requirements

**Safety Requirements:**
- RQ-52-20-01-100: No Single Failure Prevents Opening
- RQ-52-20-01-101: Pressure Interlock
- RQ-52-20-01-105: Manual Override Always Available

**Functional Requirements:**
- RQ-52-20-01-020: Emergency Door Opening Capability
- RQ-52-20-01-027: Emergency Override Function

**Performance Requirements:**
- RQ-52-20-01-050: Door Opening Time (Powered)
- RQ-52-20-01-067: Availability

---

## Compliance & Standards

**Regulatory Requirements:**
- CS 25.1309: Equipment, systems, and installations
- CS 25.810: Emergency evacuation
- CS 25.807(c): Emergency exits
- AC 25.1309-1A: System Design and Analysis

**Industry Standards:**
- SAE ARP4761: Guidelines and Methods for Conducting the Safety Assessment
- SAE ARP4754A: Development of Civil Aircraft and Systems

---

## Safety Analysis

**Failure Effect Classification:** Catastrophic

**Hazard Mitigation:**
- Design redundancy
- Independent backup systems
- Fail-safe mechanical design
- Regular inspection and testing
- Crew training and procedures

**Failure Detection:**
- Built-in test capabilities
- Status monitoring systems
- Warning and caution alerts
- Ground test procedures

---

## Design Considerations

**Key Safety Factors:**
- Single failure tolerance (Catastrophic/Hazardous)
- Common cause failure prevention
- Environmental stress protection
- Human error prevention
- Maintenance error prevention

**Risk Mitigation:**
- Design diversity
- Functional redundancy
- Monitoring and alerting
- Regular testing and inspection

---

## Notes

**Safety Critical:**
This requirement is safety-critical and classified as Catastrophic. Special attention must be paid during design, manufacturing, and maintenance to ensure compliance.

**CAOS Integration:**
Safety status and health monitoring shall be integrated with the CAOS (Computer Aided Operations & Services) system for predictive safety management.

---

*This requirement is part of the AMPEL360 OPT-IN Framework for ATA 52-20-01 Door L3 Aft Emergency Exit.*

**Last Updated:** 2025-11-04  
**Document Version:** 1.0  
**Approval Status:** Defined
