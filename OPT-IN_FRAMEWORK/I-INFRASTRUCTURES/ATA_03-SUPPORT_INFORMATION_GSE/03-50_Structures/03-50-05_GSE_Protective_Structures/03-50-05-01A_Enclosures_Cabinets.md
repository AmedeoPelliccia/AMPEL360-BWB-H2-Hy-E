# 03-50-05-01A - Enclosures and Cabinets

## 1. Purpose
Specification for structural design of equipment enclosures and cabinets for Ground Support Equipment (GSE), providing protection for electrical, electronic, and mechanical systems from environmental conditions and unauthorized access.

## 2. Scope
- Outdoor equipment enclosures
- Control cabinets and panels
- Instrument housings
- Battery boxes and compartments
- Environmental protection (NEMA/IP ratings)

## 3. Applicable Documents
- NEMA 250 (Enclosures for Electrical Equipment)
- IEC 60529 (Degrees of Protection - IP Code)
- UL 508A (Industrial Control Panels)
- IEEE C37.20.2 (Metal-Clad Switchgear)
- AWS D1.1 (Structural Welding Code)

## 4. Structural Description

### 4.1 Enclosure Classifications
| NEMA Type | IP Rating | Environment | Application |
|-----------|-----------|-------------|-------------|
| NEMA 3R | IP24 | Outdoor, rain | General outdoor GSE |
| NEMA 4 | IP66 | Outdoor, washdown | Wet environments, marine |
| NEMA 4X | IP66 | Corrosive | Marine, chemical exposure |
| NEMA 12 | IP54 | Indoor, dust | Indoor equipment rooms |
| Hazardous Location | IP66/67 | Explosive atmosphere | H2 areas (Class I Div 2) |

### 4.2 Structural Components
| Component | Material | Thickness | Purpose |
|-----------|----------|-----------|---------|
| Outer Shell | Carbon steel or SS | 1.5-3.0 mm | Structural enclosure |
| Door/Access Panel | Same as shell | Same as shell | Equipment access |
| Mounting Plate | Steel or aluminum | 3-6 mm | Component mounting |
| Gasketing | EPDM or silicone | 3-6 mm | Environmental seal |
| Hardware | Stainless steel | Varies | Latches, hinges, fasteners |
| Ventilation Louvers | Aluminum or steel | 1.5 mm | Airflow (with filters) |

### 4.3 Load Requirements
| Load Type | Requirement | Notes |
|-----------|-------------|-------|
| Component Weight | 1.5× installed equipment | Internal load |
| Wind Load | Per ASCE 7 for projected area | External pressure |
| Impact Resistance | IK08 (5 joules) minimum | Accidental impact |
| Seismic | Per site classification | Mounting integrity |
| Thermal Expansion | Accommodate -40°C to +70°C | Material selection |

### 4.4 H2 Area Enclosures (Class I Div 2)
- **Flame paths**: Machined or gasketed
- **Ventilation**: Purged or intrinsically safe
- **Electrical**: Explosion-proof components or purging
- **Grounding**: Continuous bond to facility ground
- **Material**: No aluminum in direct H2 contact (embrittlement risk)

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Ingress Protection | Per application (IP54-IP67) | IEC 60529 |
| Corrosion Protection | Zinc-plated or SS | ASTM B633 |
| Sealing Effectiveness | Rain-tight per NEMA 250 | UL testing |
| Thermal Management | Internal temp < 40°C above ambient | Heat dissipation calc |
| Door Strength | Withstand 100 N force | Access durability |
| Safety Factor | 2.0 on mounting system | Structural integrity |

### 5.2 Environmental Testing
- **Salt Spray**: 1000 hours per ASTM B117 (marine)
- **Thermal Cycling**: -40°C to +70°C, 20 cycles
- **Water Ingress**: Per IEC 60529 for claimed IP rating
- **Vibration**: Per IEC 60068-2-6 (mobile GSE)

### 5.3 Materials
- **Mild Steel**: Powder-coated or painted, economical
- **Galvanized Steel**: Good corrosion resistance, economical
- **Stainless Steel 304/316**: Excellent corrosion resistance, higher cost
- **Aluminum**: Lightweight, good corrosion resistance (not for H2 wetted)
- **Fiberglass/Composite**: Non-metallic, insulating, corrosion-proof

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-05-02A (Weather Protection), 03-50-05-03A (Blast Protection H2)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-05-01A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
