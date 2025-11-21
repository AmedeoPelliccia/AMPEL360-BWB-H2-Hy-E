# 85-00-07-202: Safety Zones and Distances Verification

## 1. Purpose
Verify that safety exclusion zones and separation distances for LH2 refueling operations comply with regulatory and industry standards.

## 2. Safety Zone Requirements
Per [ISO/TR 15916](https://www.iso.org/standard/29316.html) and [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2):

### 2.1 Exclusion Zones
- **Primary Zone**: 7.5 m radius around refueling connection (no ignition sources, restricted access)
- **Secondary Zone**: 15 m radius (controlled access, fire suppression equipment)
- **Monitoring Zone**: 30 m radius (gas detection, emergency response staging)

### 2.2 Separation Distances
- **Buildings**: ≥ 15 m from occupied structures
- **Other Aircraft**: ≥ 30 m from adjacent parked aircraft
- **Airport Operations**: ≥ 7.5 m from taxiway centerline

## 3. Verification Methods
### 3.1 Analysis
- **Dispersion Modeling**: CFD simulation of worst-case LH2 leak (ANSYS Fluent, FLACS)
- **Fire/Explosion Modeling**: Consequence analysis for ignition scenarios
- **Exclusion Zone Validation**: Confirm no exceedance of flammability limits outside zones

### 3.2 Testing
- **Gas Detector Placement**: Verify sensor coverage and alarm thresholds
- **Controlled Release**: Small-scale LH2 venting to validate dispersion models (at certified test facility)
- **Emergency Response Drill**: Simulate leak scenario, measure response times

## 4. Acceptance Criteria
- **No Ignitable Concentrations**: < 25% LEL (Lower Explosive Limit) outside primary exclusion zone
- **Detector Coverage**: ≥ 2 sensors per zone with redundant alarming
- **Emergency Response**: < 60 seconds to initiate shutdown and evacuation

## 5. Environmental Factors
Account for:
- **Wind Speed/Direction**: Prevailing winds, worst-case calm conditions
- **Temperature Inversions**: Nighttime cold air pooling
- **Airport Layout**: Building wake effects, terrain obstacles

## 6. Documentation
- **Safety Case**: Quantitative risk assessment (QRA) per [ARP4761](https://www.sae.org/standards/content/arp4761/)
- **Emergency Response Plan**: Procedures for leak, fire, and personnel injury
- **Airport Authority Approval**: Formal acceptance of safety zones and operational restrictions

## 7. Related Documents
- [85-00-07-201 H2 V&V Plan](./85-00-07-201_H2_Infrastructure_V_and_V_Plan.md)
- [85-00-06-202 H2 Safety Analysis](../../85-00-06_Engineering/H2_INFRASTRUCTURE_ENGINEERING/85-00-06-202_H2_Safety_Distances_and_Zones_Analysis.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
