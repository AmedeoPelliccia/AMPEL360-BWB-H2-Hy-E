# 03-00-05-02-02A - Fueling Port Specifications

## 1. Purpose
This document specifies the design and operational requirements for the hydrogen fueling port on the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope
This specification covers the aircraft-side fueling port design, location, access, protective systems, and maintenance requirements.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE AS6968 (Hydrogen Aircraft Refueling)
- ISO 19880-1 (Gaseous Hydrogen Fueling Stations - General Requirements)
- SAE AIR1157/1 (Aircraft Fuel Weight and Measure)
- NFPA 2 (Hydrogen Technologies Code)
- EN 1797 (Cryogenic Vessels - Gas/Materials Compatibility)
- ASTM E595 (Outgassing of Materials in Vacuum)

## 4. Interface Description

### 4.1 Overview
The hydrogen fueling port provides the primary interface for refueling the AMPEL360 BWB aircraft's liquid hydrogen tanks. The port is designed for safe, efficient fueling operations while maintaining cryogenic integrity and preventing hydrogen leakage.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Port Location | Fuselage Station FS 450, Starboard Side | ±100mm |
| Access Height | 2.5m from ground level | ±200mm |
| Port Type | SAE AS6968 receptacle | - |
| Port Material | 316L Stainless Steel | Cryogenic rated |
| Port Opening Diameter | 50mm | ±1mm |
| Protective Door | Aluminum alloy, hinged | Spring-assisted |
| Door Seal | Silicone rubber, inflatable | Pressure-activated |
| Thermal Insulation | Aerogel, 25mm thickness | Multi-layer |
| Vent Outlet | 15mm diameter | Upward discharge |
| Labeling | "LH2 FUEL - NO SMOKING" | High-visibility yellow |
| Access Panel | 500mm x 500mm | Tool-free opening |

### 4.3 Connection Procedure
1. **Port Access Preparation**
   - Open external access panel (tool-free release)
   - Remove protective cover from fueling port
   - Visual inspection for ice, contamination, or damage
   - Verify vent system is clear and operational
   - Check door seal integrity

2. **Pre-Fueling Port Configuration**
   - Verify aircraft fuel quantity indication system active
   - Open manual vent valve if equipped
   - Confirm port temperature sensors operational
   - Verify pressure relief valve functional test completed
   - Establish electrical bonding to aircraft

3. **Post-Fueling Port Closure**
   - Verify all valves closed and sealed
   - Install protective cover on port
   - Close access panel and verify latched
   - Document fuel quantity and port condition
   - Inspect area for frost or leakage indicators

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Access Platform | Height-adjustable, 2.0-3.0m | Mobile with outriggers |
| Inspection Mirror | LED-illuminated, 150mm diameter | For internal inspection |
| Thermal Imaging Camera | -50°C to +50°C range | For cold spot detection |
| Port Cap Tool | Non-sparking material | For protective cover removal |
| Leak Detection Spray | H2-compatible, non-freezing | Visual leak check |
| Cleaning Kit | Lint-free cloths, approved solvents | Port maintenance |

## 6. Safety Requirements
- **Port Design Safety Features**
  - Fail-safe pressure relief valve (set at 12 bar)
  - Redundant temperature sensors with alarm
  - Automatic vent system activation
  - Fire-resistant door seal material
  - Integrated static dissipation path
  - Emergency manual shutoff accessible from ground

- **Access and Operation Safety**
  - Port area marked with safety zone (5m radius)
  - Approach from upwind direction only
  - No hot work within 30m during fueling operations
  - Grounding verification before port opening
  - PPE requirements: face shield, cryogenic gloves, protective suit
  - Minimum 2 certified personnel for fueling operations

- **Maintenance Safety**
  - Port inspection required every 50 flight cycles
  - Leak test required after any port maintenance
  - Vent system verification after port work
  - Temperature sensor calibration annually
  - Pressure relief valve test every 6 months
  - Document all maintenance in aircraft log

- **Environmental Considerations**
  - Port designed for -40°C to +55°C ambient temperature
  - Rain and ice protection via drainage system
  - UV-resistant protective cover
  - Corrosion-resistant materials throughout
  - Lightning strike protection integrated

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 28 (Fuel - H2 Storage and Distribution)
  - ATA 12 (Servicing - Fueling Procedures)
  - ATA 20 (Standard Practices - Airframe)
  - ATA 31 (Indicating/Recording Systems - Fuel Quantity)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related GSE Subsystems: 03-20_Subsystems
- Related Interface: [03-00-05-02-01A_LH2_Coupling_Standards](./03-00-05-02-01A_LH2_Coupling_Standards.md)
- Related Interface: [03-00-05-02-03A_Cryogenic_Connections](./03-00-05-02-03A_Cryogenic_Connections.md)
- Related Interface: [03-00-05-06-01A_Towing_Attachment_Points](../03-00-05-06_Mechanical_Interfaces/03-00-05-06-01A_Towing_Attachment_Points.md)
- Safety Reference: [03-00-02_Safety](../../03-00-02_Safety/)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 GSE Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
