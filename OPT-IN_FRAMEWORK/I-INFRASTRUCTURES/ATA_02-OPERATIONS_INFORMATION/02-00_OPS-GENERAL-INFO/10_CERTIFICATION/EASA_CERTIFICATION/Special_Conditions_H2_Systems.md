# Special Conditions - H₂ Systems
## AMPEL360 BWB H₂ Hy-E Q100 INTEGRA

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Classification: Certification Critical

---

## 1. Background

The AMPEL360 aircraft incorporates liquid hydrogen fuel storage and fuel cell propulsion systems that are not addressed by existing CS-25 provisions. Special conditions are required to establish an equivalent level of safety.

---

## 2. Proposed Special Conditions

### SC-H2-001: Hydrogen Fuel System Installation
**Requirement:** The hydrogen fuel system installation must be designed to minimize hazards to the aircraft in the event of leakage or spillage.

**Means of Compliance:**
- Physical separation from ignition sources
- Ventilation systems (10 air changes/hour normal, 50 emergency)
- Leak detection system (8 sensors per zone, continuous monitoring)
- Emergency defueling capability (60 minutes maximum)

### SC-H2-002: Cryogenic Tank Requirements
**Requirement:** Liquid hydrogen tanks must withstand operational loads, temperature extremes, and maintain structural integrity.

**Means of Compliance:**
- Double-wall vacuum-insulated construction
- Storage temperature -253°C, pressure 2.8-3.2 bar
- Boil-off rate ≤0.3% per day
- Pressure relief system
- Tank integrity monitoring
- ISO 19881 adapted for aviation

### SC-H2-003: Fuel Cell Powerplant Installation
**Requirement:** Fuel cell powerplant must provide reliable power with safety equivalent to turbine engines.

**Means of Compliance:**
- Total power output 10 MW (4× 2.5 MW stacks)
- Efficiency 55-60%
- Cold start ≤3 minutes, hot start ≤30 seconds
- Power response time ≤3 seconds
- Emergency shutdown ≤30 seconds
- Redundancy and graceful degradation

### SC-H2-004: Hydrogen Fuel Quality
**Requirement:** Hydrogen fuel quality must be maintained to prevent system degradation or failure.

**Means of Compliance:**
- SAE J2719 fuel quality standard
- Contamination monitoring
- Fuel quality verification procedures
- Refueling quality control

### SC-H2-005: Leak Detection and Warning
**Requirement:** The aircraft must have a leak detection system providing timely warning of hydrogen leaks.

**Means of Compliance:**
- Minimum 8 sensors per H₂ zone
- Continuous monitoring during all operations
- LEL (Lower Explosive Limit) detection threshold
- Crew alerting system
- Automatic emergency response initiation

### SC-H2-006: Ventilation and Inerting
**Requirement:** Adequate ventilation must prevent accumulation of hydrogen in enclosed spaces.

**Means of Compliance:**
- Normal ventilation: 10 air changes/hour
- Emergency ventilation: 50 air changes/hour
- Automatic activation on leak detection
- Inerting system for fuel cell compartments
- Integration with ATA 47 inerting

### SC-H2-007: Fire Detection and Suppression
**Requirement:** Fire detection and suppression must be H₂-compatible and effective.

**Means of Compliance:**
- H₂-specific fire detection (UV/IR sensors)
- H₂-capable suppression agents
- Zone isolation capability
- Crew notification and response procedures

### SC-H2-008: Emergency Procedures
**Requirement:** Emergency procedures must address H₂-specific scenarios.

**Means of Compliance:**
- H₂ leak response procedures
- Fuel cell malfunction procedures
- Emergency ventilation activation
- Emergency defueling (ground)
- Crew training requirements

### SC-H2-009: Ground Refueling Procedures
**Requirement:** Hydrogen refueling must be conducted safely with appropriate protocols.

**Means of Compliance:**
- Refueling time ≤45 minutes
- Flow rate 120 kg/min
- Safety zone 50m radius
- Grounding resistance ≤3 milliohm
- Fire equipment on standby
- Personnel H₂ certification (8 hours minimum)
- EN 17127 refueling standards

### SC-H2-010: Maintenance and Inspection
**Requirement:** Maintenance and inspection procedures must ensure continued H₂ system safety.

**Means of Compliance:**
- Pressure test 5 bar for 30 seconds
- Leak detection system verification
- Tank integrity monitoring
- Fuel cell performance monitoring
- Predictive maintenance via CAOS

---

## 3. Standards Adoption

### 3.1 ISO 19881:2018
**Status:** Adapted for aviation application
**Document:** `H2_SPECIFIC_CERTIFICATION/ISO_19881_Compliance.md`

### 3.2 SAE J2719
**Status:** Adopted with aviation-specific requirements
**Document:** `H2_SPECIFIC_CERTIFICATION/SAE_J2719_Fuel_Quality.md`

### 3.3 NFPA 2:2020
**Status:** Safety baseline for H₂ operations
**Document:** `H2_SPECIFIC_CERTIFICATION/NFPA_2_Hydrogen_Code.md`

### 3.4 EN 17127
**Status:** Refueling protocol basis
**Document:** `H2_SPECIFIC_CERTIFICATION/Refueling_Standards_Compliance.md`

---

## 4. Safety Case

A comprehensive H₂ safety case has been developed:
- `H2_SPECIFIC_CERTIFICATION/H2_Safety_Case.md`

The safety case demonstrates equivalent or superior safety to conventional jet fuel systems through:
- Defense-in-depth architecture
- Multiple independent safety systems
- Quantitative risk analysis
- Operational safety procedures

---

## 5. Authority Coordination

### 5.1 EASA
- Special conditions proposed: 2026-01-15
- Technical working group: 2026-02-15
- Comments received: 2026-03-01
- Status: Active review

### 5.2 FAA
- Parallel issue papers development
- Harmonization with EASA approach
- Joint technical discussions

---

## 6. Compliance Status

| Special Condition | Status | Evidence | Target Date |
|-------------------|--------|----------|-------------|
| SC-H2-001 Installation | Active | Design Review | 2026-Q2 |
| SC-H2-002 Cryogenic Tanks | Active | Test Program | 2026-Q3 |
| SC-H2-003 Fuel Cells | Active | Ground Tests | 2026-Q3 |
| SC-H2-004 Fuel Quality | Complete | SAE J2719 | Complete |
| SC-H2-005 Leak Detection | Active | System Tests | 2026-Q2 |
| SC-H2-006 Ventilation | Active | System Tests | 2026-Q2 |
| SC-H2-007 Fire Systems | Planning | Test Plan | 2026-Q3 |
| SC-H2-008 Emergency Proc | Active | Proc Validation | 2026-Q4 |
| SC-H2-009 Refueling | Active | Demo Program | 2026-Q2 |
| SC-H2-010 Maintenance | Planning | Procedures | 2027-Q1 |

---

## 7. Test Evidence

Ground test evidence will be documented in:
- `TEST_EVIDENCE/Ground_Test_Results/CERT-GT-001_H2_Refueling_Test.md`
- `TEST_EVIDENCE/Ground_Test_Results/Ground_Test_Results.csv`

Flight test evidence will be documented in:
- `TEST_EVIDENCE/Flight_Test_Evidence/CERT-FT-002_H2_System_Flight_Tests.md`
- `TEST_EVIDENCE/Flight_Test_Evidence/Flight_Test_Results.csv`

---

## 8. Related Documents

- `Certification_Master_Plan.md`
- `Regulatory_Strategy.md`
- `H2_SPECIFIC_CERTIFICATION/` (all documents)
- `FAA_CERTIFICATION/Issue_Papers_H2_Propulsion.md`

---

**Approval:**
- Prepared by: Safety Team
- Reviewed by: Cert Team
- Authority Review: EASA (Active)
- Date: 2025-11-05
