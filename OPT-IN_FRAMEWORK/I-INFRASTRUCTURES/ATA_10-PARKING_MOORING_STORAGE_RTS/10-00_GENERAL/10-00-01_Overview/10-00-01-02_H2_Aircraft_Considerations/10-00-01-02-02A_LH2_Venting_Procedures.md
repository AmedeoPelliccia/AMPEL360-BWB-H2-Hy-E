# 10-00-01-02-02A - LH2 Venting Procedures

## 1. Purpose

This document establishes procedures for liquid hydrogen (LH2) venting operations during parking and storage of the AMPEL360-BWB-H2 aircraft, ensuring safe management of hydrogen boil-off.

## 2. Scope

This document covers:

- Normal boil-off venting during parking operations
- Emergency venting procedures
- Vent system monitoring and control
- Environmental and safety considerations for H2 venting

## 3. Applicable Documents

- [ATA iSpec 2200](https://www.atastandards.org/) - Information Standards for Aviation Maintenance
- [ATA 100 Chapter 10](https://www.atastandards.org/) - Parking, Mooring, Storage and Return to Service
- [NFPA 2 - Hydrogen Technologies Code](https://www.nfpa.org/)
- [SAE AS6968](https://www.sae.org/) - Hydrogen Aircraft Ground Support Equipment
- [ATA 28 - Fuel System Documentation](../../../../ATA_28-FUEL/)

## 4. Description

### 4.1 Overview

Liquid hydrogen boils continuously due to heat ingress into the cryogenic storage system. During parking and storage operations, this boil-off gas must be safely managed through:

- Controlled venting to atmosphere
- Boil-off gas capture and utilization (where available)
- Pressure management within safe limits
- Monitoring of vent system operation

### 4.2 H2/LH2 considerations

#### 4.2.1 Boil-Off Management

**Normal Operating Conditions:**
- LH2 temperature: -253°C (-423°F)
- Normal boil-off rate: 0.1-0.3% of tank volume per day
- Tank pressure range: 2-5 bar (29-73 psi)
- Vent activation pressure: 4.5 bar (65 psi)
- Vent closure pressure: 3.0 bar (44 psi)

**Factors Affecting Boil-Off:**
- Ambient temperature
- Solar radiation exposure
- Wind conditions
- Tank insulation integrity
- Fuel quantity remaining

#### 4.2.2 Venting System Operation

**Automatic Venting (Normal Mode):**
1. Tank pressure monitored continuously
2. Vent valve opens automatically at set pressure
3. H2 gas vented to atmosphere through dedicated vent mast
4. Vent discharge height: Minimum 5 meters above aircraft
5. Vent valve closes when pressure normalizes

**Manual Venting (Maintenance Mode):**
- Requires qualified personnel authorization
- Ground-based vent control panel operation
- Pressure monitoring during manual vent
- Documentation of manual vent events

### 4.3 BWB Configuration Considerations

#### 4.3.1 Vent Mast Locations

BWB-specific vent system features:
- Multiple vent points integrated into BWB upper surface
- Vent discharge directed away from aircraft structure
- H2 gas dispersion patterns mapped for BWB geometry
- Clearance requirements from BWB control surfaces and sensors

#### 4.3.2 Access for Vent System Maintenance

- Vent system components accessible via BWB-specific access panels
- Ground equipment positioning for vent system servicing
- Safety considerations for working near vent discharge points

## 5. Requirements

| Requirement | Specification | Notes |
|-------------|---------------|-------|
| RQ-10-02-02-001 | Vent system operational check before each parking period | Verify automatic operation |
| RQ-10-02-02-002 | Vent discharge minimum 5 meters above highest aircraft point | H2 dispersion safety |
| RQ-10-02-02-003 | H2 detection at vent discharge point | Verify proper dispersion |
| RQ-10-02-02-004 | Vent valve position indication | Ground monitoring capability |
| RQ-10-02-02-005 | Pressure relief redundancy | Dual vent valve system |
| RQ-10-02-02-006 | Vent discharge velocity minimum 20 m/s | Ensure adequate dispersion |
| RQ-10-02-02-007 | Maximum tank pressure 5.5 bar | Safety relief setting |
| RQ-10-02-02-008 | Vent event logging | Record all vent operations |

## 6. Safety Considerations

### 6.1 Normal Venting Operations

**Pre-Parking Checks:**
1. Verify vent system status indication
2. Check for vent system anomalies or warnings
3. Ensure parking position allows safe vent dispersion
4. Brief ground personnel on active venting status

**During Parking:**
1. Monitor tank pressure trending
2. Check for abnormal boil-off rates
3. Verify vent plume dispersion (if visible)
4. Maintain clear zone under vent discharge

**Post-Parking:**
1. Review vent event log
2. Document any anomalies
3. Calculate actual boil-off rate
4. Report unusual events to maintenance

### 6.2 Emergency Venting

**Emergency Vent Conditions:**
- Rapid pressure increase (> 1 bar per hour)
- Tank overpressure warning
- LH2 system anomaly requiring rapid depressurization
- Fire or explosion risk mitigation

**Emergency Vent Procedure:**
1. Activate emergency vent (manual override if necessary)
2. Evacuate personnel from Zone 1 (3-meter radius)
3. Notify airport fire services
4. Monitor pressure reduction
5. Do not attempt to stop emergency vent until pressure normalized
6. Investigate cause before return to service

### 6.3 Personnel Safety

**Hazards During Venting:**
- Hydrogen gas (flammable, asphyxiant)
- Cold gas (cryogenic temperature)
- High-velocity discharge
- Ice formation on vent components

**Safety Precautions:**
- Maintain minimum 10-meter distance from vent discharge
- No ignition sources within 15-meter radius of vent
- PPE required for close approach (cryogenic gloves, face shield)
- Continuous H2 monitoring in work area

## 7. Cross-References

- Related ATA Chapters:
  - [ATA 28 - Fuel](../../../../ATA_28-FUEL/) - LH2 tank system design
  - [ATA 73 - Engine Fuel and Control](../../../../ATA_73-ENGINE_FUEL_AND_CONTROL/)
  - [ATA 30 - Ice and Rain Protection](../../../../ATA_30-ICE_RAIN_PROTECTION/) - Vent ice prevention
- Parent Document: [10-00-01_Overview](../../)
- Related H2 Documents:
  - [10-00-01-02-01A_H2_Parking_Requirements.md](./10-00-01-02-01A_H2_Parking_Requirements.md)
  - [10-00-01-02-03A_Cryo_System_Standby.md](./10-00-01-02-03A_Cryo_System_Standby.md)
  - [10-00-01-02-04A_H2_Safety_Zones.md](./10-00-01-02-04A_H2_Safety_Zones.md)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-12-08*.

---
