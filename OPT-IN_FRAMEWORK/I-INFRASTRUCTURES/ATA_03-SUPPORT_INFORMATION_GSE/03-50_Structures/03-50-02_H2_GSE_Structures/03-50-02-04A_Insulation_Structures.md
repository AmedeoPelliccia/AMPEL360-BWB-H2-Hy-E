# 03-50-02-04A - Insulation Structures

## 1. Purpose
This document specifies the structural design and installation requirements for thermal insulation systems on H2/LH2 Ground Support Equipment (GSE). It addresses the structural support of insulation, protection systems, and integration with cryogenic vessels and piping.

## 2. Scope
This specification covers:
- Vacuum insulation support structures
- Multi-layer insulation (MLI) attachment
- Foam and blanket insulation support
- Weather barriers and cladding
- Personnel protection (cold surfaces)
- Insulation on piping, vessels, and equipment

## 3. Applicable Documents
- ASTM C1728 (Standard Practice for Cryogenic Piping Insulation)
- ASTM C585 (Cellular Glass Thermal Insulation)
- EN 13458 (Cryogenic Vessels - Insulation Systems)
- ISO 21009 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- ASTM C1650 (Standard Practice for Thermal Transmittance Testing of Vacuum Insulation)
- NFPA 2 (Hydrogen Technologies Code - Fire Protection)
- Reference: 03-50-02-01A (LH2 Tank Structures), 03-50-02-02A (Cryogenic Vessel Design)

## 4. Structural Description

### 4.1 Overview
Insulation structures provide physical support, protection, and proper positioning of thermal insulation materials. The structural system must withstand environmental loads while minimizing thermal bridging and maintaining insulation effectiveness over the design life.

### 4.2 Insulation System Types

#### 4.2.1 Vacuum Insulation (for Vessels)
| Component | Function | Material | Notes |
|-----------|----------|----------|-------|
| Vacuum Jacket | Outer containment shell | Carbon steel or 304 SS | Maintains vacuum integrity |
| Spacers/Supports | Maintain annular gap | G-10 GFRP, low-k ceramics | Minimize thermal bridging |
| MLI Layers | Radiation shield | Aluminized Mylar/Dacron | 20-80 layers |
| Getter | Absorbs residual gases | Activated charcoal | Maintains vacuum quality |

**Performance Target**: Heat leak < 1 W/m² for stationary vessels

#### 4.2.2 Foam Insulation (for Piping)
| Type | Density (kg/m³) | Thermal Conductivity (W/m·K) | Application |
|------|----------------|------------------------------|-------------|
| Polyurethane Foam | 30-60 | 0.020-0.025 | LH2 piping, economical |
| Polyisocyanurate Foam | 30-50 | 0.018-0.022 | Enhanced fire resistance |
| Polystyrene (XPS) | 25-40 | 0.027-0.032 | Below-grade applications |
| Closed-Cell Elastomeric | 60-80 | 0.035-0.040 | Flexible piping, vibration areas |

**Typical Thickness**: 50-100 mm for LH2 piping

#### 4.2.3 Blanket/Wrap Insulation
| Material | Service Temp | Thermal Conductivity | Application |
|----------|--------------|---------------------|-------------|
| Aerogel Blanket | -253°C to +650°C | 0.012-0.020 W/m·K | Complex geometries, valves |
| Fiberglass Blanket | -100°C to +450°C | 0.030-0.040 W/m·K | Economical, ambient piping |
| Calcium Silicate | -18°C to +650°C | 0.050-0.065 W/m·K | High-temperature areas |

### 4.3 Structural Support for Insulation

#### 4.3.1 Piping Insulation Support
| Component | Description | Material | Spacing |
|-----------|-------------|----------|---------|
| Saddles | Support insulated pipe weight | SS or Al | Per pipe support spacing |
| Stanchions | Elevate pipe off ground | SS or painted steel | 2-3 m typical |
| Protection Shields | Prevent mechanical damage | 0.5 mm SS or Al sheet | At walkways, work areas |
| Vapor Barrier | Prevent moisture ingress | Aluminized polymer film | Continuous, sealed joints |

#### 4.3.2 Insulation Cladding (Weather Barrier)
| Material | Thickness | Application | Notes |
|----------|-----------|-------------|-------|
| Aluminum Sheet | 0.5-1.0 mm | Outdoor piping, vessels | Corrosion-resistant, lightweight |
| Stainless Steel Sheet | 0.5 mm | High-traffic areas | Durable, impact-resistant |
| PVC Jacketing | 0.8 mm | Indoor, low-exposure | Economical, easy to install |
| Composite Panels | Varies | Large flat surfaces | Structural + weather barrier |

**Fastening**: Self-tapping screws, rivets, or adhesive (compatible with cryogenic service)

### 4.4 Thermal Bridging Analysis

#### 4.4.1 Heat Leak Through Supports
| Support Configuration | Heat Leak (W per support) | Improvement Factor |
|-----------------------|--------------------------|-------------------|
| Metallic support (no insulation) | 10-50 W | Baseline |
| Insulated metallic support | 2-10 W | 5× improvement |
| Low-conductivity pads (G-10) | 0.5-2 W | 20× improvement |
| Aerogel-wrapped support | 0.2-1 W | 50× improvement |

**Design Goal**: Support heat leak < 10% of total system heat leak

#### 4.4.2 Cladding Thermal Bridging
- **Joint Design**: Overlapping joints minimize air infiltration
- **Fastener Spacing**: 150-300 mm to prevent wind uplift
- **Thermal Breaks**: Neoprene or rubber washers on fasteners

### 4.5 Structural Loads on Insulation Systems

#### 4.5.1 Load Types
| Load | Magnitude | Design Consideration |
|------|-----------|---------------------|
| Self-Weight | Insulation + cladding density | Support capacity |
| Wind Load | Per ASCE 7 (up to 2.5 kPa) | Cladding attachment strength |
| Ice/Snow | Per local climate | Additional dead load |
| Thermal Cycling | Contraction/expansion | Flexible joints, allow movement |
| Personnel Load | 1.0 kN point load | Protection shields, walkways |

#### 4.5.2 Cladding Design Wind Pressure
| Exposure | Design Wind Speed | Cladding Pressure |
|----------|------------------|-------------------|
| Open terrain (C) | 160 km/h | 1.8 kPa |
| Urban/suburban (B) | 140 km/h | 1.4 kPa |
| Hurricane zones | 200 km/h | 2.8 kPa |

**Fastener Design**: Resist pullout and shear from wind pressure

### 4.6 Fire Protection and H2 Safety

#### 4.6.1 Fire-Rated Insulation
| Requirement | Specification | Application |
|-------------|---------------|-------------|
| Fire Resistance | 1-2 hour rating | Near ignition sources |
| Flame Spread | Class A (≤25) per ASTM E84 | All exposed surfaces |
| Smoke Development | ≤50 per ASTM E84 | Enclosed spaces |
| Non-combustible | ASTM E136 | Within 10 m of H2 vent |

#### 4.6.2 H2 Leak Detection Integration
- **Sensor Ports**: Penetrations through insulation for H2 sensors
- **Sealing**: Maintain thermal and vapor barrier integrity
- **Accessibility**: Allow sensor maintenance without insulation removal

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Insulation Thickness (LH2 piping) | 50-100 mm | ASTM C1728 |
| Cladding Attachment Strength | 2× design wind load | ASCE 7 |
| Thermal Conductivity (effective) | < 0.025 W/m·K at mean temp | ASTM C177 |
| Vapor Barrier Permeance | < 0.05 perm | ASTM E96 |
| Compressive Strength (foam) | > 200 kPa | Support weight without crushing |
| Service Life | 20 years minimum | UV and weather-resistant materials |

### 5.2 Installation Requirements
| Task | Requirement | Inspection |
|------|-------------|------------|
| Surface Preparation | Clean, dry, rust-free | Visual inspection |
| Vapor Barrier Application | Continuous, sealed joints | Pressure test (piping) |
| Insulation Fit | Tight joints, no gaps | Visual, thermal imaging |
| Cladding Fastening | Per design spacing | Pull test (sample) |
| Weather Seal | All penetrations sealed | Water spray test |

### 5.3 Quality Assurance Testing
| Test | Frequency | Acceptance Criteria |
|------|-----------|---------------------|
| Thermal Performance Test | Per vessel/system | Heat leak within ±10% of design |
| Vacuum Leak Test | Per vessel | < 10⁻⁹ mbar·L/s |
| Moisture Content | Before foam application | < 15% relative humidity on surface |
| Cladding Pull Test | 1 per 20 m² | No failure at 2× design load |
| IR Thermography | Initial + periodic | No hot spots >10°C above ambient |

### 5.4 Maintenance and Inspection
| Activity | Frequency | Acceptance Criteria |
|----------|-----------|---------------------|
| Visual Inspection (cladding) | Quarterly | No damage, corrosion, loose fasteners |
| Thermal Imaging | Annually | Insulation effective, no degradation |
| Vacuum Pressure Check (vessels) | Continuous (gauge) | Maintain < 10⁻⁴ mbar |
| Moisture Intrusion Check | Annually (piping) | No moisture in insulation |
| Repair Damaged Insulation | As needed | Restore original performance |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-00-06 (GSE Engineering)
- Parent Document: 03-50_Structures
- Related Documents:
  - 03-50-02-01A (LH2 Tank Structures)
  - 03-50-02-02A (Cryogenic Vessel Design)
  - 03-50-02-03A (H2 Piping Supports)
  - 03-50-05-02A (Weather Protection)
  - 03-50-06-04A (Cryogenic Stress Analysis)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-02-04A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
