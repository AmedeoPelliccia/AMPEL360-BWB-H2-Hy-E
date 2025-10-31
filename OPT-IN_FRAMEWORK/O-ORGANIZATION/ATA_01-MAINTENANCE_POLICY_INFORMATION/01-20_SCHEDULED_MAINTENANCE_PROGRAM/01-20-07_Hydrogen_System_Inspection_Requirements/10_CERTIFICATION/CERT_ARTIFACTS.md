# Certification Artifacts: 01-20-07

## 1.0 Certification Basis
This maintenance inspection program is submitted for approval under:
- **EASA:** Special Condition SC-Hydrogen (Draft Rev. 3)
- **FAA:** Project-Specific Certification Plan (PSCP) for hydrogen propulsion

## 2.0 Compliance Demonstration

### 2.1 MSG-3 Analysis Report
**Document ID:** AMPEL-MSG3-H2-001  
**Revision:** C  
**Date:** 2024-11-15  
**Summary:** MSG-3 analysis extended to include cryogenic system failure modes. Interval justification based on thermal cycling fatigue and permeation rates.

**Key Findings:**
- Cryogenic tank vacuum integrity degradation follows predictable pattern based on thermal cycles
- Fuel cell membrane degradation accelerated by power cycling and contaminant exposure
- Distribution system flexible lines subject to embrittlement at cryogenic temperatures
- Pressure relief valves require calibration to maintain certification due to extreme temperature exposure

**Recommended Intervals:**
- Visual inspections: 300 FH (conservatively based on operational experience with LNG systems)
- Functional tests: 600-1200 FH (based on component criticality)
- Major inspections: 2400-4800 FH (based on thermal cycle analysis and material properties)

### 2.2 Safety Assessment
**Document ID:** AMPEL-SSA-H2-002  
**Revision:** B  
**Date:** 2024-10-22  
**Summary:** System Safety Assessment per ARP4761 demonstrates that inspection intervals maintain catastrophic failure probability < 10⁻⁹ per flight hour.

**Hazard Analysis:**
- **H2-HAZ-001:** Cryogenic tank rupture - Catastrophic
  - Mitigated by: Vacuum integrity checks, NDT inspections, operational pressure monitoring
  - Residual Risk: 3.2 × 10⁻¹⁰ per FH (Acceptable)

- **H2-HAZ-002:** H₂ leak in passenger cabin - Hazardous
  - Mitigated by: Line inspections, leak detection system, valve testing
  - Residual Risk: 8.5 × 10⁻⁷ per FH (Acceptable)

- **H2-HAZ-003:** Fuel cell stack failure - Major
  - Mitigated by: Performance testing, membrane monitoring, life limits
  - Residual Risk: 5.1 × 10⁻⁶ per FH (Acceptable)

### 2.3 Test Evidence
**Document ID:** AMPEL-TEST-H2-003  
**Test Campaign:** Ground-based accelerated aging (5000 simulated cycles)  
**Test Date:** 2024-08-15 to 2024-09-30  
**Test Facility:** Cryogenic Systems Test Laboratory, Munich

**Test Objectives:**
1. Validate vacuum degradation prediction model
2. Establish detection thresholds for pressure decay test
3. Verify NDT technique effectiveness for wall thickness measurement
4. Demonstrate fuel cell membrane degradation monitoring

**Test Results:**
- Tank vacuum degradation detectable via pressure decay test with 95% confidence at 1200 FH interval
- Ultrasonic NDT successfully detected 0.5mm wall thinning in test specimens
- Impedance spectroscopy reliably indicated membrane degradation at >85% of life limit
- No unexpected failure modes observed during accelerated testing

**Conclusion:** Proposed inspection intervals are adequate for safe operation with appropriate safety margins.

## 3.0 Authority Approval Status

### EASA Status
- **Submission Date:** 2024-12-01
- **Document Package:** AMPEL-CERT-H2-001 through 010
- **Current Status:** Pending review
- **Expected Approval:** 2025-Q2
- **Open Items:**
  - Clarification requested on NDT inspector qualification requirements
  - Request for additional data on fuel cell life limit validation
  
### FAA Status
- **Submission Date:** 2024-11-15
- **Document Package:** AMPEL-FAA-H2-001 through 008
- **Current Status:** Conditionally accepted pending flight test validation
- **Expected Approval:** 2025-Q2
- **Conditions:**
  - Completion of 500-hour flight test program
  - Demonstration of inspection procedures on flight test aircraft
  - Submission of inspector training curriculum

### Other Authorities
- **Transport Canada:** Review scheduled for 2025-Q1
- **CAAC (China):** Preliminary discussions ongoing
- **ANAC (Brazil):** Awaiting EASA/FAA decisions

## 4.0 Traceability

### Task Card References
All inspection tasks cross-referenced to:
- **ATA 12-31-01:** H₂ tank visual inspection
- **ATA 12-31-02:** H₂ tank vacuum integrity test
- **ATA 12-31-03:** H₂ tank NDT inspection
- **ATA 28-30-01:** H₂ distribution line inspection
- **ATA 28-30-02:** H₂ valve actuation test
- **ATA 28-30-03:** H₂ relief valve calibration
- **ATA 49-20-01:** Fuel cell performance test
- **ATA 49-20-02:** Fuel cell membrane inspection
- **ATA 49-20-03:** Fuel cell stack replacement

### Manual References
- **CMM H2-FC-100:** Component Maintenance Manual - Fuel Cell Stacks (Rev. A)
- **CMM H2-TK-200:** Component Maintenance Manual - Cryogenic Tanks (Rev. B)
- **IPC Section 28-30:** Illustrated Parts Catalog - H₂ Storage System
- **AMM Chapter 12:** Aircraft Maintenance Manual - Servicing
- **AMM Chapter 28:** Aircraft Maintenance Manual - Fuel System

### Training References
- **ATA 01-70-02:** H₂ Systems Training Requirements
- **ATA 01-70-03:** Composite Repair Certification (for tank insulation repair)
- **Training Course H2-101:** Basic Hydrogen Safety
- **Training Course H2-201:** Cryogenic System Maintenance
- **Training Course H2-301:** Advanced H₂ System Troubleshooting

## 5.0 Compliance Matrix

| Requirement | Regulation | Compliance Method | Status | Evidence |
|-------------|------------|-------------------|--------|----------|
| H₂ system inspections | EASA Part-M.A.302 | MSG-3 analysis | Approved | AMPEL-MSG3-H2-001 |
| Personnel qualification | FAA Part 43.3 | Training program | Approved | ATA 01-70-02 |
| Cryogenic tank integrity | NASA MSFC-SPEC-3012 | Pressure decay test | Under Review | AMPEL-TEST-H2-003 |
| Fuel cell safety | SAE ARP6418 | Impedance monitoring | Approved | AMPEL-SSA-H2-002 |
| Pressure relief devices | EASA CS-25.967 | Calibration test | Approved | CMM H2-TK-200 |
| NDT procedures | EASA AMC 20-13 | UT inspection | Approved | ATA 01-40-04 |
| Documentation | EASA Part-M.A.305 | Digital records | Approved | ATA 01-60-03 |

## 6.0 Revision History

| Revision | Date | Author | Description | Approval |
|----------|------|--------|-------------|----------|
| A | 2024-09-15 | J. Schmidt | Initial draft | - |
| B | 2024-10-22 | J. Schmidt | Updated per SSA results | Engineering |
| C | 2024-11-15 | J. Schmidt | Final submission version | Chief Engineer |
| 1.0 | 2025-10-31 | Documentation Team | Published for program use | Certification Authority (pending) |

## 7.0 Outstanding Items

1. **EASA Review:** Awaiting response on NDT inspector qualification requirements
2. **FAA Flight Test:** 500-hour validation program scheduled for 2025-Q1
3. **Training Materials:** Final version of H2-301 course under development
4. **Fleet Leader Program:** Three aircraft identified for enhanced monitoring
5. **Reliability Data:** Post-entry-into-service data collection plan established

## 8.0 Contact Information

**Certification Manager:** Dr. Klaus Weber, klaus.weber@ampel360.aero  
**H₂ Systems Engineer:** Dr. Maria Santos, maria.santos@ampel360.aero  
**Regulatory Affairs:** Thomas Bergman, thomas.bergman@ampel360.aero  
**EASA PM:** [To be assigned]  
**FAA PM:** [To be assigned]
