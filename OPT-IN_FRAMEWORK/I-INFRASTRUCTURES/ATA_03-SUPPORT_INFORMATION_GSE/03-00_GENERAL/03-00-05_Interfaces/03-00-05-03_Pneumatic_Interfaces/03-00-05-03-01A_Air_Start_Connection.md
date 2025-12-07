# 03-00-05-03-01A - Air Start Connection

## 1. Purpose
This document specifies the interface requirements for pneumatic engine starting operations using ground-based air start units for the AMPEL360 BWB H₂ Hy-E aircraft.

## 2. Scope
This specification covers the air start connection interface, pressure requirements, procedures, and safety considerations for engine ground starting operations.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ARP4754A (Guidelines for Development of Civil Aircraft and Systems)
- SAE AS1241 (Air Start Units and Accessories)
- MIL-PRF-23699 (Lubricating Oil, Aircraft Turbine Engines)
- ISO 2533 (Standard Atmosphere)

## 4. Interface Description

### 4.1 Overview
The air start interface provides high-pressure pneumatic power from ground support equipment to rotate the aircraft engines for ground starting operations. This system is essential for engine maintenance testing and pre-flight procedures.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Connector Type | MS24484-4C (2.5 inch) | - |
| Connection Location | Engine pylon, each engine | Access panel required |
| Supply Pressure | 30-50 psi (2.0-3.4 bar) | Operating range |
| Maximum Pressure | 65 psi (4.5 bar) | Absolute maximum |
| Air Flow Rate | 60 lbs/min (27 kg/min) | Minimum per engine |
| Air Temperature | 0°C to +50°C | At supply |
| Coupling Material | Aluminum alloy 6061-T6 | Anodized |
| Hose Diameter | 2.5 inch (63.5mm) | Internal diameter |
| Maximum Hose Length | 15m | From air start unit |

### 4.3 Connection Procedure
1. **Pre-Connection Checks**
   - Position air start unit within 15m of aircraft
   - Verify air supply pressure 30-50 psi
   - Check hose for damage or contamination
   - Inspect aircraft receptacle for FOD
   - Verify engine area clear of personnel
   - Ensure fire extinguisher positioned

2. **Connection Steps**
   - Remove protective cap from aircraft receptacle
   - Align coupling and insert into receptacle
   - Rotate locking collar clockwise until secure
   - Verify visual lock indicator
   - Gradually increase air pressure
   - Monitor for leaks at connection

3. **Engine Start Procedure**
   - Coordinate with flight deck
   - Initiate engine start sequence per aircraft procedures
   - Monitor air pressure and flow rate
   - Typical start duration: 30-60 seconds
   - Confirm engine self-sustaining before disconnecting

4. **Disconnection**
   - Reduce air supply pressure to zero
   - Rotate locking collar counter-clockwise
   - Remove coupling from receptacle
   - Install protective cap
   - Store equipment properly

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Air Start Unit | 150 CFM capacity | Diesel or electric powered |
| Air Hose | 2.5 inch diameter, 15m | Reinforced rubber |
| Pressure Regulator | 0-100 psi range | Adjustable |
| Pressure Gauge | 0-100 psi, digital | ±1 psi accuracy |
| Oil-Water Separator | 5 micron filtration | Inline filter |
| Quick-Disconnect Coupling | MS24484-4C compatible | Both ends |

## 6. Safety Requirements
- **Pneumatic Safety**
  - Never exceed 65 psi supply pressure
  - Verify pressure relief valve operational
  - Inspect hoses before each use
  - Maintain clear area around rotating engine
  - Use hearing protection during engine start
  - Secure hoses to prevent whipping if disconnected

- **H2 Aircraft Considerations**
  - Ensure air supply is oil-free and dry
  - No ignition sources near H2 fuel system
  - Verify ventilation adequate before engine start
  - Monitor for H2 leaks before pneumatic operations
  - Position air start unit upwind of aircraft

- **Operational Safety**
  - Minimum 2-person crew for engine start operations
  - Maintain communication with flight deck
  - Fire watch required during and after engine start
  - Verify engine intake and exhaust areas clear
  - Follow noise abatement procedures

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 71 (Power Plant)
  - ATA 72 (Engine - Turbine/Turboprop)
  - ATA 80 (Starting)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related Interface: [03-00-05-03-02A_Bleed_Air_Interface](./03-00-05-03-02A_Bleed_Air_Interface.md)
- Related Interface: [03-00-05-03-03A_Pneumatic_Pressure_Standards](./03-00-05-03-03A_Pneumatic_Pressure_Standards.md)

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
