# 10-PRT-PHY-004 - H2 Vent Valve Prototype

## 1. Prototype Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-PRT-PHY-004 |
| Prototype Type | Physical |
| TRL Level | 3→5 |
| Status | Design |
| Version | A |
| Date | 2025-12-10 |
| Author | AMPEL360 H2 Systems Team |

## 2. Purpose

Develop and validate a cryogenic vent valve for controlled release of hydrogen gas during parking and storage operations. The valve must operate reliably at liquid hydrogen (LH2) temperatures (-253°C) while maintaining leak-tight sealing and providing adequate flow capacity for safe venting.

### 2.1 Background
The AMPEL360 BWB aircraft uses LH2 for propulsion. During parking, mooring, and storage, boil-off H2 must be safely vented to prevent pressure buildup. This prototype validates a vent valve design capable of:
- Operating at cryogenic temperatures (-253°C)
- Providing fail-safe operation (normally closed, opens on command or overpressure)
- Integrating with H2 detection and alarm systems
- Meeting aerospace reliability standards

### 2.2 Objectives
- Demonstrate valve operation at -253°C for ≥100 cycles
- Validate leak-tightness (< 1×10⁻⁶ mbar·L/s) when closed
- Measure flow capacity (target ≥ 10 kg/min LH2 equivalent)
- Assess actuation force/power requirements at cryo temperature
- Validate material compatibility with H2 and cryogenic service
- Generate certification data for valve design

## 3. Scope

### 3.1 What the Prototype Represents
This prototype represents a flight-quality vent valve for H2/LH2 venting during ground operations. It is a full-scale, fully functional prototype intended to validate the design for production.

### 3.2 Limitations
- Testing conducted with gaseous helium (ambient) and liquid nitrogen (-196°C) before LH2 (-253°C)
- Limited to component-level testing (not integrated into full aircraft system)
- Flow testing may use scaled-down flow rates (validate via CFD correlation)

### 3.3 Use Cases
- Emergency H2 venting during ground operations
- Controlled boil-off venting during long-term storage
- Pressure relief during LH2 tank servicing
- Pre-flight purge operations

## 4. Design Basis

### 4.1 Related Design Documents
- ATA_10-00-04_Design: H2 venting system design
- 10-PRT-PLN-004: H2 System Prototype Plan
- 10-PRT-POC-002: Cryo Valve POC

### 4.2 Requirements Addressed
| Requirement ID | Description | Verification Method |
|----------------|-------------|---------------------|
| REQ-10-00-H2-002 | Safe H2 venting capability | Prototype flow testing |
| REQ-10-00-CRY-001 | Valve operation at -253°C | Cryo cycling test |
| REQ-10-00-CRY-003 | Leak rate < 1×10⁻⁶ mbar·L/s | Helium leak test |
| REQ-10-00-H2-010 | Fail-safe (normally closed) | Functional test |
| REQ-10-00-MAT-001 | H2 material compatibility | Material qualification |

### 4.3 Design Constraints
- Must fit within available envelope at LH2 tank vent outlet
- Actuation power limited to 28 VDC aircraft power
- Weight target < 2 kg per valve
- Maintenance-free for 1000 flight cycles
- Must integrate with H2 detection system for automatic actuation

## 5. Prototype Specifications

### 5.1 Physical Characteristics
| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| Overall Length | 180 | mm | ±5 |
| Valve Body Diameter | 50 | mm | ±2 |
| Port Diameter | 25.4 | mm (1") | ±0.5 |
| Weight | 1.8 | kg | ±0.2 |
| Scale | Full-scale | - | - |

### 5.2 Material Specifications
| Component | Material | Specification | Justification |
|-----------|----------|--------------|---------------|
| Valve Body | 316L SS | ASTM A182 | H2 compatible, weldable |
| Valve Seat | Inconel 625 | AMS 5666 | High hardness, cryo + H2 |
| Poppet | 316 SS | ASTM A276 | Low friction, H2 compatible |
| Stem | Monel K-500 | ASTM B865 | High strength at cryo |
| Seals (Primary) | PTFE | ASTM D4894 | Cryo + H2 compatible |
| Seals (Backup) | Kalrez 4079 | DuPont spec | Extreme cryo capability |
| Actuator Housing | 6061-T6 Al | ASTM B211 | Lightweight, non-H2-wetted |
| Fasteners | 316 SS | ASTM F593 | H2 compatible |

### 5.3 Manufacturing Method
- **Primary Method**: CNC machining for valve body and internal components
- **Secondary Processes**: 
  - TIG welding (per AWS D10.4) for pressure boundary
  - Electropolishing for H2-wetted surfaces
  - Heat treatment (solution annealing) for stress relief
- **Quality Standards**: 
  - ASME B31.12 for H2 piping components
  - Helium leak testing per MIL-STD-750

### 5.4 Performance Specifications
| Parameter | Specification | Unit | Verification Method |
|-----------|--------------|------|---------------------|
| Operating Temperature | -253 to +50 | °C | Cryo chamber testing |
| Operating Pressure | 0 to 10 | bar(g) | Pressure testing |
| Leak Rate (closed) | < 1×10⁻⁶ | mbar·L/s | He leak test (10-PRT-TST-003) |
| Flow Capacity (open) | ≥ 10 | kg/min (LH2) | Flow testing |
| Actuation Time | < 2 | seconds | Functional test |
| Actuation Force | < 50 | N | Load cell measurement |
| Cryo Cycles | ≥ 100 | cycles | Durability test |
| H2 Exposure Cycles | ≥ 1000 | cycles | Fatigue test |

## 6. H2/BWB/Cryo Considerations

### 6.1 System Classification
| Parameter | Value | Details |
|-----------|-------|---------|
| H2 Related | Yes | H2 venting, H2-wetted materials |
| Cryo Related | Yes | Operating at -253°C (LH2 temperature) |
| BWB Specific | No | Generic valve, not BWB-specific geometry |

### 6.2 H2 Safety Requirements
- **Material Compatibility**: All H2-wetted parts must resist embrittlement (316 SS, Inconel proven)
- **Leak Testing**: Helium leak test to 1×10⁻⁶ mbar·L/s acceptance when closed
- **Cleanliness**: "LH2 clean" per NASA KSC-C-123 (no hydrocarbons, moisture)
- **Bonding**: Electrical bonding path < 1 ohm to prevent static buildup
- **Vent Discharge**: Valve outlet must connect to vent stack discharging ≥5m above grade, away from ignition sources

### 6.3 Cryogenic Requirements
- **Operating Temperature**: Continuous operation at -253°C (20K)
- **Pre-Cooling**: Gradual pre-cool procedure to avoid thermal shock (cool-down rate < 50 K/min)
- **Thermal Cycling**: Must withstand ≥100 cycles from ambient to -253°C without degradation
- **Material Behavior**: 
  - 316 SS retains toughness at -253°C (no brittle fracture)
  - PTFE remains flexible (with some hardening, acceptable)
  - Kalrez backup seals for extreme low-temp sealing
- **Insulation**: Valve body to be insulated (MLI or foam) to minimize heat leak into LH2 system

### 6.4 BWB-Specific Requirements
Not applicable (valve is generic component).

### 6.5 Special Safety Requirements
| Hazard | Severity | Mitigation |
|--------|----------|------------|
| H2 leak from valve | Hazardous | Leak testing; redundant seals; H2 detection |
| Valve fails to open (overpressure) | Hazardous | Fail-safe design; pressure relief; redundant actuation |
| Valve fails to close (H2 release) | Major | Robust actuation; manual backup; alarm integration |
| Cryo burn from cold surface | Minor | Insulation; warning labels; PPE |
| Material failure at cryo temp | Major | Material qualification; stress analysis; safety factor |

## 7. Manufacturing Plan

### 7.1 Process Flow
1. **Material Procurement**: 316L SS bar stock, Inconel for seat, PTFE/Kalrez seals (4 weeks lead time)
2. **CNC Machining**: Valve body, poppet, stem, seat (2 weeks)
3. **Welding/Brazing**: Assemble valve body components (1 week)
4. **Heat Treatment**: Solution anneal 316 SS for stress relief and H2 compatibility (3 days)
5. **Electropolishing**: H2-wetted surfaces for leak-tightness (1 week)
6. **Assembly**: Install seals, actuator, instrumentation (1 week)
7. **Leak Testing**: Helium leak test at ambient (2 days)
8. **Functional Testing**: Actuation, flow testing at ambient (1 week)
9. **Cryogenic Testing**: LN₂ testing, then LH₂ testing if available (2 weeks)
10. **Final Inspection & Documentation** (3 days)

### 7.2 Manufacturing Procedures
- **Welding**: Per AWS D10.4, qualified welder, 100% visual inspection, radiography for critical welds
- **Machining Tolerances**: ±0.05 mm for sealing surfaces, ±0.1 mm general
- **Cleanliness**: Parts cleaned with isopropanol, dried with filtered N₂, assembled in clean room or laminar flow hood
- **Seals**: Handle with gloves, inspect for damage, lubricate with approved cryo lubricant (Krytox)

### 7.3 Quality Control Points
| Stage | Inspection | Acceptance Criteria |
|-------|------------|---------------------|
| Material Receipt | Mill certs, material ID | Certs match specs, material properly identified |
| Machining | Dimensional inspection | Within tolerances, surface finish Ra < 0.8 μm (sealing surfaces) |
| Welding | Visual, RT or UT | No cracks, porosity, incomplete fusion |
| Heat Treatment | Hardness test | Rockwell B < 90 (ductile) |
| Electropolishing | Surface finish | Ra < 0.4 μm |
| Assembly | Torque verification | Fasteners to spec torque |
| Leak Test (ambient) | He leak test | < 1×10⁻⁶ mbar·L/s |
| Functional Test | Actuation, flow | Opens/closes reliably, flow ≥ target |

### 7.4 Schedule
| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Design Freeze | 2026-04-15 | Planned |
| Material Procurement | 2026-05-15 | Planned |
| Fabrication Start | 2026-05-20 | Planned |
| Fabrication Complete | 2026-06-20 | Planned |
| Ambient Testing Complete | 2026-06-30 | Planned |
| Cryo Testing Complete | 2026-07-31 | Planned |
| Delivery to Integration | 2026-08-05 | Planned |

### 7.5 Cost Estimate
| Item | Cost (USD) |
|------|-----------|
| Materials (316 SS, Inconel, seals) | $4,000 |
| CNC Machining (external vendor) | $8,000 |
| Welding/Assembly (internal labor) | $3,000 |
| Heat Treatment (external service) | $500 |
| Electropolishing (external service) | $1,000 |
| Actuator (COTS electric actuator) | $2,500 |
| Instrumentation (pressure, temp sensors) | $1,500 |
| Testing (ambient, cryo facilities) | $10,000 |
| Documentation/Engineering | $2,000 |
| Contingency (20%) | $6,500 |
| **Total** | **$39,000** |

## 8. Test Plan Overview

### 8.1 Test Objectives
- Validate valve operation at -253°C
- Measure leak rate when closed
- Measure flow capacity when open
- Assess actuation reliability over multiple cycles
- Validate material compatibility with H2 and cryo

### 8.2 Test Types
- [x] Dimensional Verification (post-fabrication)
- [x] Functional Testing (ambient temperature)
- [x] Leak Testing (ambient and cryo)
- [x] Cryogenic Testing (LN₂ at -196°C, then LH₂ at -253°C if available)
- [x] Flow Testing (ambient gas, then cryo)
- [x] Durability Testing (≥100 cryo cycles)

### 8.3 Test Plan Reference
Detailed test procedures in **10-PRT-TST-003: H2 Valve Prototype Test Plan**.

## 9. Results Summary

[To be completed after testing - Q3 2026]

### 9.1 Test Results
| Test | Result | Pass/Fail | Comments |
|------|--------|-----------|----------|
| Dimensional Check | TBD | TBD | To be completed |
| Ambient Leak Test | TBD | TBD | To be completed |
| Cryo Leak Test (-196°C LN₂) | TBD | TBD | To be completed |
| Cryo Leak Test (-253°C LH₂) | TBD | TBD | To be completed |
| Flow Test (ambient) | TBD | TBD | To be completed |
| Cryo Cycling (100 cycles) | TBD | TBD | To be completed |
| Actuation Reliability | TBD | TBD | To be completed |

### 9.2 Performance Against Specifications
[Analysis to be completed after testing]

## 10. Lessons Learned

[To be completed after testing and evaluation]

### 10.1 Design Lessons
- TBD

### 10.2 Manufacturing Lessons
- TBD

### 10.3 Testing Lessons
- TBD

## 11. Recommendations

### 11.1 Next Steps
- [Pending test results]

### 11.2 Production Considerations
- [To be determined based on prototype performance]

### 11.3 Design Improvements
- [To be identified during testing]

## 12. Attachments and References

### 12.1 CAD Files
- 10-PRT-PHY-004-CAD-001: Valve assembly model
- 10-PRT-PHY-004-CAD-002: Valve body detail
- 10-PRT-PHY-004-CAD-003: Actuator interface

### 12.2 Drawings
- 10-PRT-PHY-004-DWG-001: Valve assembly drawing
- 10-PRT-PHY-004-DWG-002: Machining drawing (valve body)
- 10-PRT-PHY-004-DWG-003: Machining drawing (poppet/stem)

### 12.3 Photos
- [To be added during fabrication and testing]

### 12.4 Related Documents
- 10-PRT-PLN-004: H2 System Prototype Plan
- 10-PRT-POC-002: Cryo Valve POC
- 10-PRT-TST-003: H2 Valve Prototype Test Plan
- 10-PRT-RPT-002: H2 System Prototype Report

## 13. Standards and Regulations

### 13.1 Applicable Standards
- **ASME B31.12**: Hydrogen Piping and Pipelines (valve design criteria)
- **SAE AS6968**: Hydrogen Aircraft Ground Support Equipment
- **NFPA 2**: Hydrogen Technologies Code (safety requirements)
- **ISO 13984**: Liquid Hydrogen - Land Vehicle Fuel Tanks (cryo valve guidance)
- **AWS D10.4**: Welding Stainless Steel for Cryogenic Service
- **MIL-STD-750**: Leak Testing (helium mass spectrometer method)
- **NASA KSC-C-123**: Cleanliness for H2/LH2 systems

### 13.2 Compliance Notes
- Valve design follows ASME B31.12 §6.3 (component design)
- Material selection per ASME B31.12 §5 (materials for H2 service)
- Leak testing per MIL-STD-750 Method 1071 (fine leak test)

## 14. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Design Engineer | TBD | | YYYY-MM-DD |
| H2 Systems Lead | TBD | | YYYY-MM-DD |
| Safety Officer | TBD | | YYYY-MM-DD |
| Manufacturing Engineer | TBD | | YYYY-MM-DD |
| Test Engineer | TBD | | YYYY-MM-DD |

## 15. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-10 | AMPEL360 H2 Systems Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last Update**: 2025-12-10
