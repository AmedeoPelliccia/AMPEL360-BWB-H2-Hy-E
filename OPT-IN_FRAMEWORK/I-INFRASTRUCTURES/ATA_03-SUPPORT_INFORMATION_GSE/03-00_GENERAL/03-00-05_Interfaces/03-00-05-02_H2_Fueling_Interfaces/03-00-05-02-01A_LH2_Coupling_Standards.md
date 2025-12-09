# 03-00-05-02-01A - LH2 Coupling Standards

## 1. Purpose
This document specifies the liquid hydrogen (LH2) coupling standards and requirements for ground-to-aircraft fueling operations of the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope
This specification covers LH2 coupling design, materials, connection procedures, and safety requirements for all hydrogen fueling operations.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE AS6968 (Hydrogen Aircraft Refueling)
- ISO 19880-1 (Gaseous Hydrogen Fueling Stations - General Requirements)
- ISO 21013 (Cryogenic Vessels - Pressure Relief Accessories)
- SAE J2601 (Fueling Protocols for Light Duty Gaseous Hydrogen Surface Vehicles)
- NFPA 2 (Hydrogen Technologies Code)
- CGA G-5.4 (Standard for Hydrogen Vent Systems)
- EN 1797 (Cryogenic Vessels - Gas/Materials Compatibility)

## 4. Interface Description

### 4.1 Overview
The LH2 coupling system provides a safe, leak-free connection between ground-based hydrogen fueling equipment and the aircraft's liquid hydrogen fuel tanks. The system must operate at cryogenic temperatures (-253°C) while maintaining structural integrity and preventing hydrogen leakage.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Coupling Type | SAE AS6968 Type II | - |
| Nominal Diameter | 25mm (1.0 inch) | ±0.5mm |
| Operating Pressure | 10 bar maximum | Working pressure |
| Design Pressure | 30 bar | Safety factor 3:1 |
| Operating Temperature | -253°C to +85°C | Cryogenic to ambient |
| Coupling Material | 316L Stainless Steel | ASTM A182 |
| Seal Material | PCTFE (Polychlorotrifluoroethylene) | Compatible with LH2 |
| Connection Method | Quick-disconnect with safety interlock | Fail-safe design |
| Breakaway Force | 1000 N minimum | Emergency separation |
| Leak Rate | < 1 x 10⁻⁶ mbar·L/s | Helium leak test |
| Coupling Weight | < 5 kg | Per half-coupling |

### 4.3 Connection Procedure
1. **Pre-Connection Safety Checks**
   - Verify area is clear of ignition sources
   - Confirm proper ventilation and H2 detection systems active
   - Establish electrical bonding < 0.1 Ω between aircraft and GSE
   - Verify aircraft fuel system is depressurized
   - Check weather conditions (wind < 15 knots, no lightning within 10 km)
   - Confirm all personnel wearing appropriate PPE

2. **Coupling Pre-Cool Procedure**
   - Open vent valve on aircraft side
   - Initiate slow LH2 flow through GSE coupling (1 L/min)
   - Monitor coupling temperature reduction
   - Achieve coupling temperature < -240°C before main connection
   - Typical pre-cool time: 5-10 minutes
   - Verify no visible ice accumulation at connection interface

3. **Connection Sequence**
   - Align coupling halves (aircraft and GSE)
   - Insert GSE coupling into aircraft receptacle
   - Rotate locking collar clockwise until audible click
   - Verify visual lock indicator shows GREEN
   - Perform leak check with helium sniffer
   - Confirm bonding resistance still < 0.1 Ω
   - Enable interlock signal to permit fueling

4. **Disconnection Procedure**
   - Complete fuel flow and close valves
   - Depressurize coupling chamber (< 1 bar)
   - Allow temperature stabilization (2-5 minutes)
   - Rotate locking collar counter-clockwise
   - Separate coupling halves slowly
   - Immediately install protective caps on both sides
   - Verify vent system operational

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| LH2 Fuel Truck | 10,000 L capacity minimum | Cryogenic insulated tank |
| Transfer Hose | Triple-layer vacuum insulated | 15m maximum length |
| Coupling Assembly | SAE AS6968 compliant | Aircraft-side and GSE-side |
| Leak Detector | Helium sniffer, 1 x 10⁻⁶ sensitivity | Handheld or fixed |
| Temperature Sensors | RTD type, -270°C to +100°C | K-type thermocouples |
| Pressure Gauges | 0-40 bar, digital display | ±0.5% accuracy |
| Emergency Breakaway | 1000 N activation force | Automatic shutoff valves |

## 6. Safety Requirements
- **Critical Safety Features**
  - Fail-safe mechanical interlock prevents connection under pressure
  - Automatic shutoff valves activate on coupling separation
  - Dual-redundant pressure relief valves
  - Integrated temperature monitoring
  - Emergency breakaway capability with zero-leak shutoff
  - Dead-man switch on fueling control panel

- **Pre-Operation Safety**
  - H2 detection system verification (4 sensors minimum)
  - Wind direction and speed monitoring
  - Lightning detection system active (10 km radius)
  - Fire suppression equipment positioned and ready
  - Exclusion zone established (30m radius minimum)
  - All personnel trained and certified for LH2 operations

- **During Operation Monitoring**
  - Continuous H2 concentration monitoring (alarm at 25% LEL)
  - Bonding resistance verification every 30 seconds
  - Temperature monitoring at coupling interface
  - Pressure monitoring in transfer system
  - Video surveillance of coupling area
  - Two-person minimum crew requirement

- **Emergency Response**
  - LH2 spill: immediate evacuation, activate deluge system
  - Leak detection: stop flow, maintain bonding, ventilate area
  - Coupling failure: activate emergency breakaway
  - Fire: cease fueling, activate suppression, evacuate to safe distance
  - Lightning proximity: immediate shutdown, maintain bonding

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 28 (Fuel - H2 Storage System)
  - ATA 12 (Servicing - Fueling Procedures)
  - ATA 79 (Engine Oil - Lubrication for H2 Pumps)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related GSE Subsystems: 03-20_Subsystems
- Related Interface: [03-00-05-02-02A_Fueling_Port_Specifications](./03-00-05-02-02A_Fueling_Port_Specifications.md)
- Related Interface: [03-00-05-02-03A_Cryogenic_Connections](./03-00-05-02-03A_Cryogenic_Connections.md)
- Related Interface: [03-00-05-02-04A_Fueling_Control_Interface](./03-00-05-02-04A_Fueling_Control_Interface.md)
- Related Interface: [03-00-05-01-04A_Electrical_Grounding](../03-00-05-01_Electrical_Interfaces/03-00-05-01-04A_Electrical_Grounding.md)
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
