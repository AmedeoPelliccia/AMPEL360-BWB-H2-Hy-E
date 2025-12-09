# 03-50-03-01A - Mobile GSE Chassis

## 1. Purpose
This document specifies the structural design requirements for mobile Ground Support Equipment (GSE) chassis systems. It defines the framework, suspension interface, and structural integrity requirements for self-propelled and towed GSE vehicles.

## 2. Scope
This specification covers:
- Chassis frame design for mobile GSE
- Load-bearing structure and cross-members
- Mounting points for equipment and systems
- Suspension and axle attachment
- Towing and lifting interfaces
- Crash protection and rollover safety

## 3. Applicable Documents
- SAE J1100 (Motor Vehicle Dimensions)
- SAE J2014 (Braking System)
- ISO 11228 (Ergonomics - Manual Handling)
- AISC 360 (Structural Steel Design)
- AWS D1.2 (Structural Welding Code - Aluminum)
- OSHA 1910.178 (Powered Industrial Trucks)
- Reference: 03-50-01-01A (GSE Structural Design)

## 4. Structural Description

### 4.1 Overview
Mobile GSE chassis provide the structural foundation for equipment transport and operation. The chassis must support operational loads, dynamic forces during movement, and withstand environmental conditions while maintaining equipment alignment and accessibility.

### 4.2 Chassis Configurations

| Type | Description | Typical Application | Load Capacity |
|------|-------------|---------------------|---------------|
| Ladder Frame | Two longitudinal rails with cross-members | LH2 tankers, heavy equipment | 10-40 tonnes |
| Backbone | Central beam with outriggers | Specialized equipment | 5-15 tonnes |
| Space Frame | Tubular triangulated structure | Lightweight, high-performance GSE | 2-10 tonnes |
| Monocoque | Integrated body-chassis | Compact equipment | 1-5 tonnes |

### 4.3 Chassis Frame Components

| Component | Function | Material | Design Criteria |
|-----------|----------|----------|-----------------|
| Main Rails | Primary longitudinal load path | ASTM A572 Gr 50 or 6061-T6 Al | Bending, torsion resistance |
| Cross-Members | Lateral stiffness, mounting points | ASTM A36 or 6061-T6 Al | Shear, local crushing |
| Gussets | Load distribution at joints | Same as rails | Stress concentration mitigation |
| Equipment Mounts | Secure payload/equipment | ASTM A36 with reinforcement | Equipment-specific loads |
| Suspension Mounts | Attach axles/springs | High-strength steel | Dynamic loads, fatigue |
| Tow Hitch | Towing interface | ASTM A514 (high strength) | Impact, towing loads |

### 4.4 Load Cases for Mobile GSE

#### 4.4.1 Static Loads
| Load Type | Magnitude | Application |
|-----------|-----------|-------------|
| Dead Load | Chassis + equipment weight | Uniform distribution |
| Payload | Maximum operating capacity | Per design specification |
| Personnel | 100 kg per work position | Point loads at platforms |
| Fuel/Fluids | Full tank/reservoir capacity | Distributed on support frame |

#### 4.4.2 Dynamic Loads
| Condition | Load Factor | Notes |
|-----------|-------------|-------|
| Acceleration | 0.5g longitudinal | Braking, acceleration |
| Cornering | 0.3g lateral | Turning maneuvers |
| Road Shock | 3.0g vertical | Potholes, uneven ground |
| Emergency Braking | 0.8g longitudinal | ABS-equipped vehicles |
| Collision | Per FMVSS or equivalent | Crash protection |

#### 4.4.3 Environmental Loads
- **Wind Load**: 1.5 kPa on projected area (stationary, high wind)
- **Thermal**: -40°C to +50°C ambient range
- **Corrosion**: Salt spray per ASTM B117 (500 hours minimum)

### 4.5 Suspension and Axle Integration

| System | Design Requirement | Standard |
|--------|-------------------|----------|
| Axle Mounting | Withstand 3× static load | SAE J691 |
| Spring Attachment | Fatigue life > 500,000 cycles | SAE J1528 |
| Shock Absorber Mounts | Dynamic loads up to 5× static | ISO 3450 |
| Anti-sway Bars | Lateral stability | SAE J2227 |

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Chassis Bending Stiffness | > 1000 Nm²/degree | SAE J826 |
| Torsional Stiffness | > 10,000 Nm/degree | SAE J826 |
| Safety Factor (static) | 2.0 on yield | AISC 360 |
| Safety Factor (dynamic) | 1.5 on yield | AISC 360 |
| Fatigue Life | 500,000 km or 20 years | SAE J1099 |
| Corrosion Protection | Hot-dip galv. or equivalent | ASTM A123 |

### 5.2 Material Specifications
| Material | Application | Specification | Yield Strength |
|----------|-------------|---------------|----------------|
| High-Strength Steel | Main rails, heavy-duty | ASTM A572 Gr 50 | 345 MPa |
| Carbon Steel | Cross-members, brackets | ASTM A36 | 250 MPa |
| Aluminum Alloy | Lightweight chassis | 6061-T6 | 275 MPa |
| High-Strength Steel (mounting) | Suspension, tow hitch | ASTM A514 | 690 MPa |

### 5.3 Welding Requirements
- **Welding Process**: GMAW or SMAW per AWS D1.1 (steel), D1.2 (aluminum)
- **Joint Efficiency**: 0.85 minimum (partial inspection) to 1.0 (full inspection)
- **Weld Inspection**: Visual + 10% UT/MT on critical joints
- **Welder Qualification**: Per AWS D1.1 or equivalent

### 5.4 Testing Requirements
| Test | Requirement | Frequency |
|------|-------------|-----------|
| Static Load Test | 1.5× rated capacity | Prototype + production sample |
| Torsion Test | Measure stiffness | Prototype |
| Fatigue Test | 2× design life cycles | Prototype |
| Road Test | 10,000 km validation | Prototype |
| Corrosion Test | 1000 hours salt spray | Per material qualification |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-00-06 (GSE Engineering)
  - ATA 03-30 (Anchors and Tie-downs)
- Parent Document: 03-50_Structures
- Related Documents:
  - 03-50-01-01A (GSE Structural Design)
  - 03-50-03-02A (Trailer Frame Design)
  - 03-50-03-03A (Self Propelled Frames)
  - 03-50-03-04A (Modular Frame Systems)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-03-01A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
