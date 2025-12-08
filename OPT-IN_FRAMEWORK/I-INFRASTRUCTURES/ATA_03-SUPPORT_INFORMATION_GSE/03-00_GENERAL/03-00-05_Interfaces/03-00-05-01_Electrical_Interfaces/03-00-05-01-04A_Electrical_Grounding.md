# 03-00-05-01-04A - Electrical Grounding

## 1. Purpose
This document specifies the electrical grounding and bonding requirements for ground support equipment operations with the AMPEL360 BWB H₂ Hy-E aircraft, with special emphasis on hydrogen safety.

## 2. Scope
This specification covers all aspects of electrical grounding for GSE-to-aircraft connections, including bonding procedures, resistance requirements, and safety protocols specific to hydrogen-fueled aircraft operations.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ARP4754A (Guidelines for Development of Civil Aircraft and Systems)
- NFPA 77 (Recommended Practice on Static Electricity)
- SAE AS6968 (Hydrogen Aircraft Refueling)
- IEEE 1809 (Standard for Grounding of DC Equipment Enclosures)
- MIL-B-5087 (Bonding, Electrical, and Lightning Protection)
- ISO 19880-1 (Gaseous Hydrogen Fueling Stations - General Requirements)

## 4. Interface Description

### 4.1 Overview
Proper electrical grounding is critical for safe GSE operations, particularly for hydrogen-fueled aircraft. This document specifies grounding requirements to prevent static discharge, ensure electrical safety, and maintain electromagnetic compatibility during all ground operations.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Bonding Resistance | < 1.0 Ω | Aircraft to ground |
| H2 Fueling Bonding | < 0.1 Ω | Aircraft to H2 GSE (10× stricter for static discharge prevention with H₂) |
| Ground Cable Size | AWG 2 minimum | Green/yellow insulation |
| Ground Connection Points | 6 locations minimum | Around aircraft perimeter |
| Connector Type | Copper clamp, 50mm² contact | Cadmium plated |
| Bonding Cable Length | 7.5m maximum | Per connection point |
| Ground Test Interval | Before each operation | During H2 fueling |

### 4.3 Connection Procedure
1. **Pre-Operation Grounding Procedure**
   - Visually inspect all grounding cables and clamps
   - Clean connection surfaces to bare metal
   - Verify ground test equipment is calibrated
   - Establish main ground connection first

2. **Bonding Sequence**
   - Connect main ground cable to designated aircraft attachment point
   - Verify bonding resistance < 1.0 Ω with calibrated tester
   - Connect secondary ground cables if required
   - For H2 operations: establish bonding to H2 GSE < 0.1 Ω
   - Document all resistance measurements

3. **Post-Operation Procedure**
   - Verify all equipment de-energized before disconnection
   - Disconnect secondary grounds first
   - Remove main ground connection last
   - Store cables properly to prevent damage
   - Document any bonding anomalies

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Ground Bonding Cable | AWG 2, 7.5m length | Green/yellow striped jacket |
| Bonding Clamps | 50mm² copper contact area | Spring-loaded, cadmium plated |
| Resistance Tester | 0.01-100 Ω range, ±2% accuracy | Calibrated annually |
| Ground Test Points | Labeled "GROUND" locations | Minimum 6 per aircraft |
| Portable Ground Reel | 30m cable capacity | Mobile unit with brake |
| ESD Control Kit | Wrist straps, mats | For electronics servicing |

## 6. Safety Requirements
- **General Grounding Safety**
  - Never operate GSE equipment without proper grounding
  - Establish ground before connecting any electrical interface
  - Maintain grounding throughout entire operation
  - Verify continuity if any connection is disturbed
  - Use only approved grounding equipment

- **H2 Aircraft Specific Requirements** (CRITICAL)
  - **Mandatory < 0.1 Ω bonding during ALL H2 operations**
  - Establish bonding BEFORE opening H2 fuel port
  - Continuous resistance monitoring during H2 fueling
  - Bonding must remain until H2 port is sealed
  - Immediate fueling cessation if bonding resistance exceeds 0.1 Ω
  - Static dissipation time: minimum 30 seconds before H2 connection
  - All personnel must be grounded when within 3m of H2 operations
  - Use conductive footwear and ESD garments during H2 servicing

- **Environmental Considerations**
  - Verify ground integrity in wet conditions
  - Enhanced bonding requirements in low humidity (< 30% RH)
  - Additional ground points required in high wind conditions
  - Monitor for ground connection degradation during operations

- **Emergency Procedures**
  - Loss of grounding during H2 fueling: IMMEDIATE SHUTDOWN
  - Suspected lightning proximity: cease all GSE operations
  - Static discharge event: isolate area, inspect all connections
  - Ground fault detection: disconnect all GSE immediately

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 24 (Electrical Power)
  - ATA 28 (Fuel - H2 System)
  - ATA 12 (Servicing)
  - ATA 20 (Standard Practices)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related GSE Subsystems: 03-20_Subsystems
- Related Interface: [03-00-05-01-01A_GPU_Aircraft_Connection](./03-00-05-01-01A_GPU_Aircraft_Connection.md)
- Related Interface: [03-00-05-02-04A_Fueling_Control_Interface](../03-00-05-02_H2_Fueling_Interfaces/03-00-05-02-04A_Fueling_Control_Interface.md)
- H2 Safety Reference: [03-00-02_Safety](../../03-00-02_Safety/)

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
