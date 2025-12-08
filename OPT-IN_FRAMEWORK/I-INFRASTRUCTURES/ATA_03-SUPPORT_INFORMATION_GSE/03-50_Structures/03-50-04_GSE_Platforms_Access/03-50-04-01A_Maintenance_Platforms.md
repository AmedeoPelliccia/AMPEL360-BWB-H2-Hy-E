# 03-50-04-01A - Maintenance Platforms

## 1. Purpose
This document specifies structural design requirements for maintenance platforms used in Ground Support Equipment (GSE) for aircraft servicing, inspection, and maintenance operations.

## 2. Scope
This specification covers:
- Fixed and mobile maintenance platforms
- Work deck structures and guardrails
- Access stairs and ladders
- Adjustable height mechanisms
- Fall protection systems

## 3. Applicable Documents
- OSHA 1910.23 (Ladders)
- OSHA 1910.28 (Duty to Have Fall Protection)
- OSHA 1910.29 (Fall Protection Systems Criteria and Practices)
- EN 131 (Ladders - Terms, Types, Functional Sizes)
- ANSI A14.3 (Fixed Ladders)
- AISC 360 (Structural Steel Design)
- AWS D1.1 (Structural Welding Code)
- Reference: 03-50-01-01A (GSE Structural Design)

## 4. Structural Description

### 4.1 Overview
Maintenance platforms provide safe, stable work surfaces at elevated positions around aircraft. Structures must support personnel, tools, equipment loads while meeting fall protection and ergonomic requirements.

### 4.2 Platform Types
| Type | Height Range | Mobility | Capacity |
|------|--------------|----------|----------|
| Fixed Work Stand | 2-6 m | Stationary | 450 kg/m² |
| Mobile Platform | 1-15 m | Self-propelled or towed | 350 kg/m² |
| Scissor Lift Platform | 3-18 m | Self-propelled | 250-450 kg |
| Aircraft Docking Platform | Variable to match aircraft | Rail-mounted or wheeled | 500 kg/m² |
| Cantilever Platform | 2-10 m | Fixed or adjustable | 300 kg/m² |

### 4.3 Structural Components
| Component | Function | Material | Design Criteria |
|-----------|----------|----------|-----------------|
| Deck/Floor | Work surface | Aluminum grating or steel plate | 2.4 kPa live load minimum |
| Support Frame | Load-bearing structure | Steel or aluminum | Bending, buckling |
| Guardrails | Fall protection | Steel or aluminum tube | 890 N horizontal, 445 N vertical (OSHA) |
| Toe Boards | Prevent falling objects | Steel or aluminum | 100 mm height minimum |
| Access Stairs | Personnel access | Steel or aluminum | 7-9 kN capacity |
| Leveling System | Stabilization | Hydraulic or mechanical jacks | 1.5× platform capacity |

### 4.4 Load Requirements
| Load Type | Magnitude | Application |
|-----------|-----------|-------------|
| Uniform Live Load | 2.4 kPa (50 psf) minimum | Entire deck area |
| Concentrated Load | 1.3 kN on 625 mm² area | Any location on deck |
| Guardrail Load | 890 N horizontal at top rail | Per OSHA 1910.29 |
| Tool/Equipment | 100 kg per work station | Specific locations |
| Impact (safety factor) | 2.0× static loads | Design requirement |

### 4.5 Height Adjustment Systems
| System Type | Height Range | Mechanism | Load Capacity |
|-------------|--------------|-----------|---------------|
| Scissor Lift | 3-18 m | Hydraulic or electric | 250-500 kg |
| Telescoping Mast | 5-20 m | Hydraulic cylinders | 200-400 kg |
| Fixed Positions | Varies | Pin-lock positions | Full platform rating |
| Continuous Adjustment | Varies | Screw jack or hydraulic | Full platform rating |

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Live Load | 2.4 kPa minimum (50 psf) | OSHA 1910.22 |
| Deflection Limit | L/240 under live load | AISC 360 |
| Safety Factor | 2.0 on yield, 3.0 on ultimate | AISC 360 |
| Guardrail Height | 1.07 m (42") minimum | OSHA 1910.29 |
| Midrail Height | 530 mm (21") nominal | OSHA 1910.29 |
| Toe Board Height | 100 mm (4") minimum | OSHA 1910.29 |
| Stair Tread Depth | 230-280 mm | OSHA 1910.25 |
| Stair Riser Height | 150-190 mm | OSHA 1910.25 |

### 5.2 Fall Protection Requirements
- Guardrails required on all sides > 1.2 m height (OSHA 1910.28)
- Top rail height: 1.07 m ± 75 mm
- Midrail height: Midpoint between top rail and platform
- Maximum opening: 485 mm (prevents person fall-through)
- Toe board: 100 mm minimum height, ≤ 6 mm gap at platform

### 5.3 Material Specifications
| Material | Application | Specification | Advantages |
|----------|-------------|---------------|------------|
| Structural Steel | Frame, heavy-duty | ASTM A36, A572 | High strength, economical |
| Aluminum Alloy | Lightweight platforms | 6061-T6, 6063-T6 | Corrosion-resistant, mobile |
| Aluminum Grating | Deck surface | ASTM B209 | Slip-resistant, lightweight |
| Stainless Steel | Corrosive environments | 304, 316 | Marine, chemical exposure |

### 5.4 Stability Requirements
| Parameter | Requirement | Test Method |
|-----------|-------------|-------------|
| Tip Over (mobile) | 1.5× stability factor | Tilt table or calculation |
| Wind Resistance (stationary) | 90 km/h (stowed), 25 km/h (deployed) | ASCE 7 |
| Outrigger Spread | Sufficient for 1.5× tip load | Stability analysis |
| Base Rigidity | No visible movement under rated load | Static load test |

### 5.5 Inspection and Testing
| Activity | Frequency | Acceptance Criteria |
|----------|-----------|---------------------|
| Visual Inspection | Daily (before use) | No visible damage, deformation |
| Load Test | Annual or after repair | 1.25× rated capacity, no permanent deformation |
| NDT (welds) | Per maintenance schedule | No cracks, defects per AWS D1.1 |
| Guardrail Integrity | Monthly | 890 N horizontal load, no failure |
| Leveling System Function | Monthly | Operate smoothly, hold load |

## 6. Cross-References
- Related ATA Chapters: ATA 03-00-06 (GSE Engineering)
- Parent Document: 03-50_Structures
- Related: 03-50-04-02A (Access Stairs/Ladders), 03-50-04-03A (Passenger Boarding Bridges)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-04-01A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
