# Certification Basis Document

**Aircraft:** AMPEL360 BWB H₂ Hy-E Q100  
**Applicant:** AMPEL360 GmbH  
**Document ID:** CBD-BWB-H2-001  
**Status:** Draft  
**Date:** 2025-11-05

---

## 1. Executive Summary

This document establishes the certification basis for the AMPEL360 BWB H₂ Q100 aircraft Type Certificate application to EASA, with FAA validation.

**Primary Authority:** EASA (European Union Aviation Safety Agency)  
**Validation Authority:** FAA (Federal Aviation Administration - US)  
**Certification Standard:** CS-25 Large Aeroplanes + Special Conditions  
**Target TC Issuance:** Q4 2028

---

## 2. Applicable Regulations

### 2.1 Primary Certification Basis

**EASA CS-25 Large Aeroplanes**
- **Standard:** CS-25 Amendment [TBD - applicable at TC application date]
- **Application Date:** Q3 2026 (target)
- **Basis Date:** Amendment in effect at application date
- **Changes:** Later amendments optional unless required

**FAA Part 25 Airworthiness Standards**
- **Standard:** 14 CFR Part 25 (harmonized with CS-25)
- **Validation:** FAA validation of EASA Type Certificate
- **Bilateral Agreement:** EU-US Bilateral Aviation Safety Agreement

### 2.2 Environmental Standards

**ICAO Annex 16 Environmental Protection**
- Volume I: Aircraft Noise (Chapter 14 - latest)
- Volume II: Aircraft Engine Emissions (exempt - zero emission propulsion)
- Volume III: CO₂ Emissions (exempt - zero emission + carbon negative)

**EASA Environmental Standards:**
- CS-36 Aircraft Noise
- CS-34 Aircraft Engine Emissions (not applicable - fuel cells)

---

## 3. Special Conditions

### 3.1 Required Special Conditions

**SC-BWB-001: Blended Wing Body Geometry**
- **Reason:** Unconventional BWB configuration not explicitly addressed in CS-25
- **Scope:** Structural integrity, emergency egress, aerodynamics, systems integration
- **Status:** Proposed to EASA Q1 2026
- **Reference:** [SC-BWB-001 Document](../BWB_SPECIAL_CONDITIONS/SC-BWB-001_Geometry_Approval.md)

**SC-BWB-002: Wide Center of Gravity Range**
- **Reason:** CG range 15-42% MAC (27% span) exceeds conventional aircraft
- **Scope:** Longitudinal stability, control authority, active CG management
- **Status:** Proposed to EASA Q1 2026
- **Reference:** [SC-BWB-002 Document](../BWB_SPECIAL_CONDITIONS/SC-BWB-002_CG_Range_Approval.md)

**SC-H2-001: Hydrogen Fuel Cell Propulsion**
- **Reason:** Hydrogen cryogenic fuel system and fuel cell propulsion novel for transport category
- **Scope:** Fuel storage, distribution, safety, propulsion system certification
- **Status:** Proposed to EASA Q1 2026 (coordination with ISO 19881 adaptation)
- **Reference:** TBD (ATA 28 Fuel System / ATA 71 Powerplant documentation)

### 3.2 Optional Special Conditions

**SC-CO2-001: CO₂ Capture System**
- **Reason:** Carbon capture system not addressed in CS-25
- **Scope:** System safety, integration, performance validation
- **Status:** Optional equipment - proposed Q2 2026 if implemented
- **Reference:** TBD (ATA 21-80 CO₂ Capture System documentation)

---

## 4. Exemptions

### 4.1 Requested Exemptions
**Status:** No exemptions requested at this time

**Note:** AMPEL360 intends to fully comply with CS-25 as augmented by Special Conditions, demonstrating equivalent or superior level of safety rather than seeking exemptions.

---

## 5. Equivalent Level of Safety (ELOS)

### 5.1 ELOS Findings Required

**ELOS-BWB-001: BWB Emergency Evacuation**
- **Paragraph:** CS-25.803, CS-25.807
- **Rationale:** Wide cabin geometry (28 m) with distributed exits
- **Demonstration:** Full-scale evacuation demonstration (90 seconds)
- **Status:** Planned for Q3 2027

**ELOS-BWB-002: BWB Cabin Pressurization**
- **Paragraph:** CS-25.365, CS-25.841
- **Rationale:** Non-cylindrical cabin structure
- **Demonstration:** Pressure vessel analysis + proof testing
- **Status:** In Development

**ELOS-H2-001: Hydrogen Fuel Jettison**
- **Paragraph:** CS-25.1001 (Fuel Jettisoning)
- **Rationale:** Hydrogen cannot be safely jettisoned
- **Demonstration:** Fuel burn procedures + emergency landing capability
- **Status:** Proposed (show fuel jettison not required for safety)

---

## 6. Referenced Standards and Documents

### 6.1 Design and Manufacturing Standards

**International Standards:**
- ISO 19881: Gaseous hydrogen - Land vehicle fuel containers (adapted for aviation)
- ISO 14687: Hydrogen fuel quality specifications
- SAE ARP4754A: Development of Civil Aircraft and Systems
- SAE ARP4761: Safety Assessment Process
- RTCA DO-178C: Software Considerations in Airborne Systems
- RTCA DO-254: Hardware Considerations in Airborne Systems
- RTCA DO-160G: Environmental Conditions and Test Procedures

**Industry Standards:**
- ATA iSpec 2200: Information Standards for Aviation Maintenance
- S1000D: International Technical Publications Specification
- AIAA G-095: Guide to Hydrogen Fuel Cell Aircraft Propulsion

**Material Standards:**
- ASTM D7137: Composite impact testing
- ASTM E1444: Magnetic particle inspection
- Various composite material specifications

### 6.2 Operational Standards

**ICAO Standards:**
- Annex 6: Operation of Aircraft
- Annex 8: Airworthiness of Aircraft
- Annex 14: Aerodromes (Code E compatibility)
- Annex 16: Environmental Protection

**Other Standards:**
- IATA AHM: Airport Handling Manual (hydrogen operations)
- NFPA 2: Hydrogen Technologies Code (ground operations)

---

## 7. Certification Program Elements

### 7.1 Analysis Methods

**Structural Analysis:**
- Finite Element Analysis (FEA) - ANSYS, NASTRAN
- Composite failure criteria - Tsai-Wu, Hashin
- Damage tolerance analysis - FAA AC 20-107B

**Aerodynamic Analysis:**
- Computational Fluid Dynamics (CFD) - FLUENT, Star-CCM+
- Wind tunnel testing - Multiple scales
- Flight dynamics simulation - MATLAB/Simulink

**Systems Analysis:**
- Functional Hazard Assessment (FHA)
- Failure Modes and Effects Analysis (FMEA)
- Fault Tree Analysis (FTA)
- Common Cause Analysis (CCA)

### 7.2 Test Program

**Ground Tests:**
- Static structural tests (wing, fuselage, landing gear)
- Fatigue testing (full-scale test article)
- Pressure vessel testing (cabin, fuel tanks)
- Landing gear drop tests
- Fire testing (materials, systems)
- Lightning strike testing
- Bird strike testing
- Systems integration testing

**Flight Tests:**
- Performance validation (range, speed, altitude)
- Handling qualities (stall, maneuvers, control)
- Systems validation (all aircraft systems)
- Environmental testing (icing, hot/cold weather)
- Noise certification
- Function and reliability testing

**Special Tests:**
- Hydrogen system testing (tanks, fuel cells, safety)
- Emergency evacuation demonstration
- Ditching demonstration (or analysis)
- CAOS AI system validation

---

## 8. Certification Schedule

### 8.1 Major Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| **Pre-Application Consultation** | Q4 2025 | Planned |
| **Special Conditions Proposal** | Q1 2026 | In Development |
| **Type Certificate Application** | Q3 2026 | Planned |
| **Ground Vibration Test** | Q4 2026 | Planned |
| **Static Structural Tests** | Q1-Q2 2027 | Planned |
| **First Flight** | Q3 2027 | Planned |
| **Flight Test Campaign** | Q3 2027 - Q2 2028 | Planned |
| **Certification Testing Complete** | Q3 2028 | Planned |
| **Type Certificate Issuance** | Q4 2028 | Target |

### 8.2 Critical Path Items

1. **Special Conditions Approval** (Q3 2026) - Required before extensive testing
2. **Ground Vibration Test** (Q4 2026) - Validates structural dynamics
3. **Static Structural Tests** (Q1-Q2 2027) - Demonstrates structural integrity
4. **First Flight** (Q3 2027) - Enables flight test program
5. **Hydrogen System Certification** (Q1-Q3 2028) - Novel propulsion approval
6. **Evacuation Demonstration** (Q3 2028) - Required for TC

---

## 9. Certification Team

### 9.1 AMPEL360 Organization

**Certification Management:**
- Certification Manager: TBD
- Deputy Certification Manager: TBD
- Compliance Engineers: TBD (3-5 positions)

**Technical Disciplines:**
- Structures: Chief Structures Engineer
- Flight Test: Flight Test Director
- Systems: Chief Systems Engineer
- Propulsion: Fuel Cell Systems Engineer
- Safety: Safety Assessment Lead

### 9.2 EASA Organization

**Primary Contacts:**
- Certification Project Manager: TBD
- Novel Aircraft Types Section: BWB evaluation
- Structures Section: Composite BWB approval
- Propulsion Section: Hydrogen/fuel cell systems
- Flight Test Section: Flight testing oversight

### 9.3 External Support

**Designated Representatives:**
- DER (Structures): TBD
- DER (Systems): TBD
- DER (Propulsion): TBD
- Flight Test Pilot (EASA authorized): TBD

**Test Facilities:**
- Wind Tunnel: TBD (European facility)
- Static Test: TBD (Large component capability)
- Flight Test Base: TBD (Code E airport with H₂ infrastructure)

---

## 10. Compliance Statement

**Statement:** The AMPEL360 BWB H₂ Q100 aircraft certification basis consists of:

- **EASA CS-25** (Amendment applicable at TC application date) ✅
- **Special Condition SC-BWB-001** (BWB geometry) ⏳
- **Special Condition SC-BWB-002** (Wide CG range) ⏳
- **Special Condition SC-H2-001** (Hydrogen propulsion) ⏳
- **ELOS Findings** (As required) ⏳
- **FAA Part 25 Validation** (US market access) ⏳

**Status:** Certification basis defined - regulatory approval of Special Conditions required

**Next Steps:**
1. Finalize Special Condition proposals (Q1 2026)
2. Submit to EASA for review (Q1 2026)
3. Incorporate EASA feedback (Q2 2026)
4. Submit Type Certificate Application (Q3 2026)

---

## 11. Document Control

### 11.1 Approvals

- [ ] Certification Manager: ___________________ Date: ______
- [ ] Chief Engineer: ___________________ Date: ______
- [ ] Program Manager: ___________________ Date: ______
- [ ] Legal Review: ___________________ Date: ______

### 11.2 Revisions

| Rev | Date | Description | Author |
|-----|------|-------------|--------|
| 1.0 | 2025-11-05 | Initial certification basis document | AMPEL360 Cert Team |

### 11.3 Related Documents

- [Certification Plan](../Certification_Plan.md)
- [Type Certificate Data Sheet Draft](../Type_Certificate_Data_Sheet_Draft.md)
- [CS-25 Compliance Matrix](CS25_Compliance_Matrix.csv)
- [FAA Part 25 Compliance Matrix](FAA_Part25_Compliance_Matrix.csv)
- [Special Conditions](../BWB_SPECIAL_CONDITIONS/)

---

**Document Control:**
- Version: 1.0
- Status: Draft
- Classification: Company Confidential + Regulatory Submission
- Next Review: Special Conditions Submission (Q1 2026)

---

**END OF CERTIFICATION BASIS DOCUMENT**
