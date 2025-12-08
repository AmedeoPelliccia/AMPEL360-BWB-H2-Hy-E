---
Title: "LH2 Fueling GSE Tests"
Identifier: "AMPEL360-03-00-07-02-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 GSE V&V Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Test specification for liquid hydrogen (LH₂) fueling Ground Support Equipment verification."
Keywords: ["ATA 03","GSE","LH2","Hydrogen","Fueling","Cryogenic"]
Compliance:
  - "SAE AS6968"
  - "ISO 19880-8"
  - "NASA-STD-8719.17"
Links:
  ParentGeneral: "../../"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 GSE V&V Team", change: "Initial release" }
---

# 03-00-07-02-01A — LH₂ Fueling GSE Tests

## 1. Purpose

This document defines test specifications for verification of liquid hydrogen (LH₂) fueling Ground Support Equipment used for refueling the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope

This test specification covers:

- LH₂ transfer system functional tests
- Refueling flow rate and capacity verification
- Connection/disconnection operations
- Emergency shutdown system testing
- Automated control system verification
- Cryogenic performance validation

## 3. Applicable Documents

- [SAE AS6968](https://www.sae.org/standards/content/as6968/) — Hydrogen Aircraft Refueling
- [ISO 19880-8](https://www.iso.org/standard/71940.html) — H₂ Fueling Stations
- [ASME B31.12](https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines) — Hydrogen Piping
- [NASA-STD-8719.17](https://standards.nasa.gov/standard/nasa/nasa-std-871917) — Hydrogen Safety
- [03-00-07-01-01A](../03-00-07-01_GSE_Verification_Planning/03-00-07-01-01A_GSE_Verification_Strategy.md) — Verification Strategy

## 4. Test Requirements

### 4.1 Test Objectives

- Verify LH₂ fueling system meets flow rate requirements (≥500 kg/h)
- Validate safe connection and disconnection procedures
- Confirm emergency shutdown response time (<2 seconds)
- Verify automated control system functionality
- Validate operator interface and alarms
- Confirm no contamination of hydrogen fuel

### 4.2 Test Setup

| Equipment | Specification | Calibration Status |
|-----------|---------------|-------------------|
| LH₂ Storage Dewar | ≥5000 kg capacity, -253°C | Pressure relief tested |
| Mass Flow Meter | 0-1000 kg/h, ±0.5% | NIST traceable, annual |
| Cryogenic Thermocouples | Type T, -270°C to +50°C, ±0.5°C | NIST traceable, semi-annual |
| Pressure Transducers | 0-50 bar, ±0.1% FS | NIST traceable, annual |
| H₂ Gas Detectors | 0-1000 ppm, ±1% | Annual calibration |
| Data Acquisition System | 100 Hz sampling, 16-bit | Annual calibration |
| Test Aircraft Receptacle | AMPEL360-compatible interface | N/A (test fixture) |

### 4.3 Test Procedure

| Step | Action | Expected Result | Pass/Fail Criteria |
|------|--------|-----------------|-------------------|
| 1 | Pre-operational checks | All systems green, no leaks detected | All checks complete, H₂ < 25 ppm |
| 2 | Connect fueling hose to aircraft receptacle | Proper sealing, no leaks | Connection force within spec, leak < 1×10⁻⁶ mbar·L/s |
| 3 | Initiate automated refueling sequence | System enters refueling mode | Mode confirmed, all interlocks satisfied |
| 4 | Perform slow fill (pre-cooling) | Aircraft tank temperature decreases | Tank temp reaches -240°C within 15 min |
| 5 | Perform fast fill (refueling) | LH₂ transfer at specified rate | Flow rate 500-600 kg/h |
| 6 | Monitor fuel purity | H₂ purity maintained | Purity ≥99.97% |
| 7 | Reach fill level setpoint | Automatic shutoff at 95% capacity | Shutoff occurs, no overflow |
| 8 | Perform topping procedure | Maintain tank pressure | Pressure 3-5 bar |
| 9 | Disconnect fueling hose | No spills, proper purging | H₂ gas < 25 ppm during disconnect |
| 10 | Emergency shutdown test | Immediate stop of all LH₂ flow | Shutdown < 2 seconds, valves close |

## 5. Acceptance Criteria

### 5.1 Functional Criteria

- ✅ Refueling flow rate: 500-600 kg/h (nominal 550 kg/h)
- ✅ Refueling time: Complete fill within 60 minutes for empty tank
- ✅ Connection/disconnection: No spills, leak rate < 1×10⁻⁶ mbar·L/s
- ✅ Emergency shutdown: Response time < 2 seconds
- ✅ H₂ purity: ≥99.97% throughout refueling
- ✅ Temperature control: Tank pre-cooling to -240°C within 15 minutes
- ✅ Pressure control: Maintain 3-5 bar during topping

### 5.2 Safety Criteria

- ✅ No H₂ gas detection above 25% LEL during normal operations
- ✅ Emergency shutdown functional and tested
- ✅ All interlocks operational
- ✅ Ground bonding verified (resistance < 1Ω)
- ✅ Operator alarms functional and tested
- ✅ Personal protective equipment requirements validated

## 6. Safety Considerations

### 6.1 Hazards

| Hazard | Severity | Mitigation |
|--------|----------|------------|
| H₂ Leak | Critical | Continuous gas detection, ventilation, explosion-proof equipment |
| Cryogenic Burn | Major | Cryogenic PPE, training, safety procedures |
| Rapid Phase Transition | Critical | Controlled fill rates, pressure relief systems |
| Fire/Explosion | Critical | Bonding/grounding, ATEX equipment, fire suppression |
| Asphyxiation | Major | O₂ monitoring, ventilation, emergency procedures |

### 6.2 Safety Procedures

- **Pre-Test**: Safety briefing, PPE check, emergency drill
- **During Test**: Continuous H₂ and O₂ monitoring, safety officer present
- **Emergency**: Emergency shutdown tested, fire brigade notified and on standby
- **Post-Test**: Purging procedures, area clearance before personnel entry

### 6.3 Required PPE

- Cryogenic face shield
- Cryogenic gloves (15" minimum)
- Cryogenic apron
- Safety shoes (non-sparking)
- Fire-resistant clothing
- H₂ gas detector (personal)

## 7. Cross-References

- Parent Document: [03-00-07_V_AND_V](../)
- Related Cryogenic Tests: [03-00-07-02-02A_Cryogenic_GSE_Validation.md](./03-00-07-02-02A_Cryogenic_GSE_Validation.md)
- Related Safety Tests: [03-00-07-02-03A_H2_Safety_Systems_Tests.md](./03-00-07-02-03A_H2_Safety_Systems_Tests.md)
- Related Leak Tests: [03-00-07-02-04A_H2_Leak_Detection_Tests.md](./03-00-07-02-04A_H2_Leak_Detection_Tests.md)
- Related GSE Engineering: [03-00-06_Engineering](../../03-00-06_Engineering/)
- Related Interfaces: [03-00-05_Interfaces](../../03-00-05_Interfaces/)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 GSE V&V Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-07-02-01A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Verification & Validation Team

---
