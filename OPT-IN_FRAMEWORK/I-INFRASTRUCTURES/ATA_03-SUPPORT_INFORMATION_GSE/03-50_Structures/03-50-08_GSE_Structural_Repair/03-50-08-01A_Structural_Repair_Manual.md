# 03-50-08-01A - Structural Repair Manual

## 1. Purpose
General specification and procedures for structural repairs to Ground Support Equipment (GSE), including damage assessment, repair design, execution, and post-repair verification.

## 2. Scope
- Repair classification and approval process
- Damage assessment and repair design
- Repair methods (welding, bolting, composite)
- Quality assurance and inspection
- Return-to-service criteria

## 3. Applicable Documents
- AWS D1.1 (Structural Welding Code - Steel)
- ASME BPVC Section IX (Welding and Brazing Qualifications)
- AC 43.13-1B (Acceptable Methods, Techniques, and Practices - Aircraft Inspection and Repair)
- API 579-1/ASME FFS-1 (Fitness-For-Service)

## 4. Structural Description

### 4.1 Repair Classifications
| Class | Description | Approval Required | Examples |
|-------|-------------|-------------------|----------|
| Minor | Cosmetic, no structural impact | Technician | Paint touch-up, non-structural panel replacement |
| Standard | Defined in repair manual | Supervisor | Crack repair per SRM, bolt replacement |
| Major | Significant structural repair | Engineer + Inspector | Weld repair of primary structure, major corrosion |
| Design Modification | Changes original design | Engineering + Approval Authority | Reinforcement, material substitution |

### 4.2 Repair Process
1. **Damage Assessment**: Inspect, document, classify
2. **Repair Design**: Determine method, materials, procedures
3. **Approval**: Obtain required approvals per classification
4. **Preparation**: Clean, remove damage, prepare surfaces
5. **Execution**: Perform repair per approved procedure
6. **Inspection**: NDT and visual inspection
7. **Documentation**: Record repair details, test results
8. **Return-to-Service**: Sign-off by authorized personnel

### 4.3 Repair Methods
| Method | Application | Advantages | Limitations |
|--------|-------------|------------|-------------|
| Welding | Cracks, corrosion, structural damage | Permanent, full-strength | Requires qualified welder, heat-affected zone |
| Bolted Doubler Plate | Cracks, weak sections | Removable, no heat | Adds weight, stress concentration at fasteners |
| Composite Patch | Cracks, corrosion (non-critical) | Lightweight, no heat | Lower strength, surface prep critical |
| Section Replacement | Severe damage/corrosion | Full restoration | Time-consuming, may require fabrication |

### 4.4 Damage Types and Repairs
| Damage | Typical Repair | Notes |
|--------|---------------|-------|
| Crack < 25 mm | Drill stop-holes, monitor or weld | Stop crack propagation |
| Crack > 25 mm | Weld repair + reinforcement | Requires engineering evaluation |
| General Corrosion | Clean, treat, re-coat | If within corrosion allowance |
| Pitting Corrosion (deep) | Grind out, weld fill, blend | Restore thickness |
| Deformation (buckling) | Heat straighten or replace | Depends on severity |
| Fastener Damage | Drill out, oversize, or helicoil | Restore thread integrity |

### 4.5 H2 System Repairs
- **Material**: Same as original or approved equivalent (304L/316L SS)
- **Welding**: Per ASME B31.12, low-hydrogen processes (GTAW preferred)
- **Testing**: Hydrostatic test + leak test after repair
- **Inspection**: 100% PT or RT of welds
- **Documentation**: Detailed records for H2 safety compliance

## 5. Structural Requirements

### 5.1 Repair Strength Requirements
- **Design Goal**: Restore to original strength (100%)
- **Minimum Acceptable**: 90% of original strength (with engineering evaluation)
- **Fatigue Life**: 100% of original design life (for cyclic loading areas)
- **Safety Factor**: Same as original design (typically 2.0)

### 5.2 Weld Repair Procedure
1. Remove damage (grind or machine) to clean metal
2. Prepare weld groove per AWS D1.1
3. Preheat if required (typically not for SS, Al)
4. Weld using qualified procedure (WPS)
5. Post-weld heat treatment if required (pressure vessels)
6. Inspect (visual + NDT per original requirements)
7. Verify dimensions, blend contours

### 5.3 Quality Assurance
- All repairs performed by qualified personnel
- Welding per qualified WPS and qualified welders (AWS/ASME)
- Inspection per original specification or more stringent
- Documentation: Repair log, photos, inspection reports
- Retention: Permanent record

### 5.4 Post-Repair Inspection
| Repair Type | Inspection | Acceptance |
|-------------|------------|------------|
| Weld Repair | VT + PT or MT | No defects per AWS D1.1 |
| Weld Repair (pressure) | VT + PT + UT or RT | ASME VIII acceptance |
| Bolted Repair | VT + torque verification | All fasteners installed, torqued |
| Composite Repair | VT + tap test | Bond integrity, no delamination |

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-08-02A (Welding Procedures), 03-50-08-03A (Composite Repair), 03-50-08-04A (Cryogenic Vessel Repair)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-08-01A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
