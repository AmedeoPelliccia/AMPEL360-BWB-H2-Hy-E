# 03-50-03-03A - Self-Propelled Frames

## 1. Purpose
This document specifies structural design requirements for self-propelled Ground Support Equipment (GSE) frames, including motorized platforms, tugs, loaders, and specialized service vehicles.

## 2. Scope
This specification covers:
- Integrated chassis-powertrain structures
- Engine and transmission mounting
- Drive system integration
- Operator cab/platform structural support
- Stability and rollover protection

## 3. Applicable Documents
- ISO 3691 (Industrial Trucks - Safety Requirements)
- OSHA 1910.178 (Powered Industrial Trucks)
- ROPS/FOPS standards (ISO 3471, ISO 3449)
- SAE J1040 (Performance Criteria for Rollover Protective Structures)
- AWS D1.1 (Structural Welding Code)
- Reference: 03-50-03-01A (Mobile GSE Chassis)

## 4. Structural Description

### 4.1 Overview
Self-propelled GSE frames integrate structural support for propulsion systems, operator stations, and work equipment while maintaining mobility and operational flexibility.

### 4.2 Vehicle Classes
| Class | Power Range | Application | Typical Speed |
|-------|-------------|-------------|---------------|
| Compact Utility | 10-30 kW | Indoor GSE, light duties | 0-15 km/h |
| Standard GSE Tug | 30-100 kW | Aircraft towing, equipment transport | 0-25 km/h |
| Heavy-Duty Tug | 100-300 kW | Large aircraft towing | 0-30 km/h |
| Service Truck | 50-200 kW | Mobile maintenance, refueling | 0-50 km/h |

### 4.3 Structural Integration
| System | Mounting Requirement | Load Type |
|--------|---------------------|-----------|
| Engine/Motor | Vibration-isolated mounts | Dynamic, 3-5g vibration |
| Transmission | Rigid mount to frame | Torque reaction, 2× rated |
| Drive Axle | Flexible mounting | Dynamic road loads |
| Operator Station | ROPS/FOPS certified | Rollover/falling object protection |
| Hydraulic System | Secure mounting with access | Pressure pulsation, weight |
| Battery Pack (electric) | Crashworthy enclosure | Impact protection, thermal management |

### 4.4 Stability Analysis
| Parameter | Requirement | Test Method |
|-----------|-------------|-------------|
| Static Stability (lateral) | Tip angle > 35° | Tilt table test |
| Dynamic Stability | No tip at 20 km/h, 10 m radius turn | Road test |
| Longitudinal Stability | CG within wheelbase | Load distribution analysis |
| Braking Stability | No rear lift at 0.6g braking | Brake test |

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Frame Stiffness | Minimize powertrain vibration transmission | < 0.5 mm deflection at engine mounts |
| ROPS (if applicable) | Withstand rollover energy | ISO 3471 |
| FOPS (if applicable) | 116 kN distributed load | ISO 3449 |
| Safety Factor | 2.0 on yield | AISC 360 |
| Service Life | 30,000 hours or 20 years | Per operational profile |

### 5.2 Powertrain Mounting
- **Engine Mounts**: Rubber isolators, 3-5 Hz natural frequency
- **Transmission Mount**: Rigid, withstand 2× peak torque
- **Alignment**: Maintain driveline angularity < 3°

### 5.3 Operator Protection
- **ROPS Certification**: Required for open-cab vehicles
- **Seat Belt Anchorage**: 13.5 kN ultimate load per ISO 3776
- **Cab Structure**: Enclose operator, 360° visibility

## 6. Cross-References
- Related ATA Chapters: ATA 03-00-06 (GSE Engineering)
- Parent Document: 03-50_Structures
- Related: 03-50-03-01A (Mobile GSE Chassis), 03-50-04 (GSE Platforms/Access)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-03-03A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
