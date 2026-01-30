# 10-INT-H2-002 - H2 Ground Fueling Interface

## 1. Interface Identification

| Parameter | Value |
|-----------|-------|
| Interface Number | 10-INT-H2-002 |
| Interface Type | Fluid, Cryogenic, Electrical, Data |
| System A | LH2 Tank System |
| System B | H2 Ground Fueling Equipment |
| ATA Chapter A | ATA-10 |
| ATA Chapter B | ATA-28 (Fuel), ATA-85 (Infrastructure) |
| H2 Related | Yes |
| Cryo Related | Yes |
| BWB Specific | Yes |
| Safety Classification | Safety-Critical |
| DAL Level | DAL-A |
| Status | Baselined |

## 2. Interface Description

Defines the interface for LH2 (Liquid Hydrogen) ground fueling operations at -253°C. This safety-critical interface ensures safe, leak-free transfer of cryogenic hydrogen fuel from ground storage to aircraft tanks.

### Purpose
- Safe LH2 transfer from ground equipment to aircraft
- Prevent H2 leaks during fueling operations
- Monitor fueling parameters (flow, pressure, temperature)
- Enable emergency disconnect capability
- Ensure static grounding and bonding

## 3. Interface Parameters

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| LH2 Temperature | -253 | °C | ±2°C |
| Transfer Pressure | 1-3 | bar | ±0.2 bar |
| Flow Rate (Typical) | 1000 | kg/h | ±10% |
| Flow Rate (Maximum) | 2000 | kg/h | - |
| Connection Type | SAE AS6679 | - | Breakaway coupling |
| Connection Location | Fuselage underside, Station 200, CL | - | - |
| Ground Clearance | 2.5 | m | - |
| Fuel Capacity | 40,000 | kg LH2 | - |
| Fueling Time (Empty to Full) | 20-40 | hours | Typical |
| Grounding Resistance | <1 | ohm | Maximum |

## 4. Physical Interface

### 4.1 Fueling Receptacle
- Location: Center body underside, Station 200 (near LH2 tank)
- Coupling: SAE AS6679 cryogenic breakaway coupling
- Material: Stainless steel 316L, PTFE seals
- Automatic shutoff on disconnect or over-pressure
- Dust cap: Protective cap when not in use

### 4.2 Safety Features
- Breakaway coupling: Separates safely if fueling truck moves
- Emergency shutoff: Manual and automatic activation
- Leak detection: H2 sensors at connection point
- Static grounding: Verified before fueling authorized
- Pressure relief: 5 bar relief valve in fueling line

### 4.3 Data Interface
- Protocol: Ethernet + ARINC 825
- Signals: Tank level, pressure, temperature, flow rate
- Pre-fueling checks: Parking brake, H2 system status
- Interlock: Prevents fueling if conditions unsafe

## 5. H2/Cryo Considerations

### Cryogenic Safety
- Material compatibility verified to -260°C
- Thermal shock protection during connection
- Insulation: Vacuum-jacketed fuel line from ground equipment
- Cold burn hazard: PPE required (cryo-gloves, face shield)
- Boil-off management during fueling

### H2 Safety
- Safety zone: 10 m radius, no ignition sources
- Continuous H2 detection during fueling
- Emergency stop accessible from multiple locations
- Fire suppression: Dry chemical and foam available
- Personnel training: H2 handling certification required

## 6. BWB Considerations

- Fueling receptacle location optimized for BWB center body geometry
- Ground equipment access beneath wide BWB structure
- Fuel distribution to tank(s) within BWB central volume
- Center of gravity management during fueling (load sequencing)

## 7. Constraints

### Operational
- Fueling only when parking brake set and aircraft secure
- Maximum wind speed: 15 knots
- No fueling during thunderstorms or lightning within 5 nm
- Temperature: Ambient -20°C to +45°C
- Ground equipment certified for H2 service

### Safety
- All personnel H2-safety trained
- Fire watch posted during fueling
- Communication: Cockpit ↔ fueling operator mandatory
- Emergency procedures rehearsed before first fueling

## 8. Verification

| Verification Method | Criteria | Status | Reference |
|---------------------|----------|--------|-----------|
| Leak Test | Zero leakage at operating conditions | Completed | TEST-10-H2-010 |
| Cryo Cycling Test | 1000 cycles -260°C to +20°C | Completed | TEST-10-H2-011 |
| Flow Test | Achieve 2000 kg/h flow rate | Completed | TEST-10-H2-012 |
| Emergency Disconnect Test | Safe disconnect under pressure | Completed | TEST-10-H2-013 |
| Grounding Verification | <1 ohm resistance verified | Completed | TEST-10-H2-014 |

## 9. Related Documentation

- ICD Reference: [10-ICD-002 - H2 System ICD](../interface-control-documents/10-ICD-002_H2_System_ICD.md)
- Related: [10-INT-H2-001 - H2 Venting Interface](./10-INT-H2-001_H2_Venting_Interface.md)
- Related: [10-INT-H2-004 - LH2 Tank Interface](./10-INT-H2-004_LH2_Tank_Interface.md)
- Related: [10-INT-INF-004 - H2 Infrastructure Interface](../infrastructure-interfaces/10-INT-INF-004_H2_Infrastructure_Interface.md)
- Standards: [SAE AS6679](https://www.sae.org/standards/content/as6679/): LH2 Aerospace Fueling
- Standards: [ISO 13984](https://www.iso.org/standard/52862.html): Liquid Hydrogen Fuel Tanks

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-09 | AMPEL360 H2 Systems Engineering | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **BASELINED** – Safety-Critical Interface
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-09

---
