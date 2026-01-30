# 03-50-04-03A - Passenger Boarding Bridges

## 1. Purpose
Specification for structural design of passenger boarding bridges (jetways/airbridges) connecting terminal buildings to aircraft doors for passenger boarding and deplaning operations.

## 2. Scope
- Fixed-to-building bridge structures
- Telescoping tunnel sections
- Rotunda (pivoting sections)
- Cab (aircraft interface)
- Drive and positioning systems

## 3. Applicable Documents
- ISO 16100-1 (Passenger Boarding Bridge Classification)
- NFPA 415 (Airport Terminal Buildings, Underground Fixed Guideway Transit, and Passenger Rail Systems)
- ASCE 7 (Minimum Design Loads)
- EN 12312 (Aircraft Ground Support Equipment - Passenger Stairs)
- AWS D1.1 (Structural Welding Code)

## 4. Structural Description

### 4.1 Bridge Components
| Component | Function | Material | Design Load |
|-----------|----------|----------|-------------|
| Fixed Tunnel | Building connection | Steel frame + panels | 3.5 kPa live load |
| Telescoping Tunnel | Length adjustment | Steel or aluminum | 3.5 kPa live load |
| Rotunda | Pivot section | Steel frame | 4.0 kPa + rotation moments |
| Cab | Aircraft interface | Aluminum or steel | 4.0 kPa + wind |
| Support Columns | Vertical load transfer | Steel | Dead + live + wind |
| Drive System | Positioning mechanism | Steel housing | Operational torques |

### 4.2 Load Cases
| Load Type | Magnitude | Notes |
|-----------|-----------|-------|
| Passenger Load | 3.5 kPa minimum (73 psf) | Dense crowd condition |
| Wind Load (stowed) | 160 km/h | Per ASCE 7 |
| Wind Load (deployed) | 50 km/h | Operational limit |
| Seismic | Per site seismic zone | ASCE 7 |
| Aircraft Contact | 50 kN lateral | Cab bumpers absorb |
| Thermal | -30°C to +50°C | Expansion joints required |

### 4.3 Structural Systems
- **Main Structure**: Steel or aluminum space frame
- **Floor System**: Aluminum honeycomb panels or grating
- **Walls/Ceiling**: Aluminum or composite panels
- **Glazing**: Tempered or laminated safety glass
- **Bellows**: Fabric or rubber expansion joints between sections

## 5. Structural Requirements

### 5.1 Design Criteria
| Parameter | Requirement | Standard |
|-----------|-------------|----------|
| Live Load | 3.5 kPa minimum | ISO 16100 |
| Deflection | L/250 under live load | Design practice |
| Safety Factor | 2.0 on yield | AISC 360 |
| Seismic Design | Importance Factor 1.5 | ASCE 7 |
| Fatigue Life | 100,000 cycles (extend/retract) | Per operational profile |
| Service Life | 30 years minimum | Design specification |

### 5.2 Operational Requirements
- **Reach**: Variable, typically 20-80 m from terminal
- **Height Range**: 2-8 m above apron (adjustable)
- **Rotation**: 360° continuous or ±180°
- **Slope**: ≤5° normal, ≤8° maximum
- **Transit Speed**: ≤0.5 m/s (safety limit)
- **Positioning Accuracy**: ±50 mm at aircraft door

### 5.3 Safety Systems
- Emergency stop systems
- Overload sensors and alarms
- Collision avoidance sensors
- Fall protection at all open edges
- Emergency egress capability
- Fire detection and suppression

## 6. Cross-References
- Parent Document: 03-50_Structures
- Related: 03-50-04-01A (Maintenance Platforms), 03-50-04-02A (Access Stairs/Ladders)

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID:** 03-50-04-03A
- **Version:** A
- **Status:** Active
- **Last Updated:** 2025-12-08
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Owner:** AMPEL360 GSE Structures Team

---

*Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.*
