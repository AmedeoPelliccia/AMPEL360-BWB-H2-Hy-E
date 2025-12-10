# 03-90-05-01A - LH2 Fueling Process Flow Diagram

## 1. Purpose

Define the process flow diagram for aircraft Liquid Hydrogen (LH2) fueling operations, documenting the complete sequence from GSE storage to aircraft tanks.

## 2. Scope

This PFD covers: LH2 fueling connection, flow control, safety interlocks, monitoring systems, and normal/emergency procedures for aircraft refueling.

## 3. Applicable Documents

- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) - Hydrogen Technologies Code
- [SAE AIR7652](https://www.sae.org/) - Liquid Hydrogen Fueling System for Aircraft
- [ISO 21029](https://www.iso.org/standard/54704.html) - Cryogenic Vessels - Cleanliness for Cryogenic Service
- [CGA P-12](https://www.cganet.com/) - Safe Handling of Cryogenic Liquids

## 4. Documentation Description

### 4.1 Overview

The LH2 fueling PFD shows the complete process from GSE LH2 storage through transfer equipment to aircraft fuel tanks, including all control and safety systems.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Process Blocks | Flow diagram format | ISO 5807 |
| Equipment | Standard P&ID symbols | ISA-5.1 |
| Control Logic | Interlock descriptions | Functional text |
| Safety Systems | Highlighted/red borders | Emphasis on critical systems |

### 4.3 Content Requirements

#### 4.3.1 Fueling System Overview

**Major Components:**

| Equipment | Function | Specification |
|-----------|----------|---------------|
| LH2 Storage Tank | Source of LH2 | Capacity: TBD liters, Pressure: 4-6 bar |
| Transfer Pump | Pressurize LH2 flow | Flow rate: TBD kg/min, Head: TBD bar |
| Flowmeter | Measure fuel quantity | Coriolis mass flow, Accuracy: ±0.5% |
| Fueling Hose | Connect GSE to aircraft | Vacuum-insulated, Quick disconnect |
| Safety Systems | Protect aircraft & GSE | ESD, leak detection, grounding |

#### 4.3.2 Pre-Fueling Checks

**Mandatory Permissives:**
- [ ] Aircraft properly positioned and chocked
- [ ] Aircraft fuel system ready (valves open, vents clear)
- [ ] GSE LH2 tank level sufficient for fueling
- [ ] All H2 detectors operational and reading < 10% LEL
- [ ] Fire detection system operational
- [ ] Emergency shutdown system tested
- [ ] Bonding cable connected (aircraft to GSE)
- [ ] Weather conditions acceptable (no lightning within 5 km)
- [ ] Fueling operator certified and present
- [ ] Communication established (GSE ↔ Aircraft)
- [ ] Emergency response equipment positioned

#### 4.3.3 Fueling Sequence

**Step-by-Step Process:**

1. **Connect Fueling Hose:**
   - Position hose nozzle to aircraft receptacle
   - Verify sealing and locking
   - Check bonding continuity

2. **Cooldown Phase:**
   - Open cooldown valve (low flow ~10% of fueling rate)
   - Monitor hose temperature decrease
   - Vent aircraft tank (boil-off during cooldown)
   - Time required: ~5-10 minutes
   - Target hose temperature: < -240°C

3. **Ramp-Up Phase:**
   - Gradually increase flow rate
   - Monitor pressures (GSE and aircraft)
   - Check for leaks (visual and gas detection)
   - Flow rate increase: 10% per minute up to target

4. **Normal Fueling Phase:**
   - Maintain target flow rate (e.g., 200 kg/min)
   - Monitor aircraft tank level (capacitance or DP)
   - Monitor aircraft tank pressure (maintain 2-4 bar)
   - Vent aircraft tank as needed (manage ullage pressure)
   - Totalizer tracking fuel quantity delivered

5. **Topping-Off Phase:**
   - Reduce flow rate as target quantity approached
   - Final level adjustment
   - Ensure aircraft tank not overfilled

6. **Fueling Complete:**
   - Close fueling valve
   - Stop transfer pump
   - Depressurize hose (vent to safe location)
   - Allow hose to warm slightly (reduce cold shock on disconnect)
   - Disconnect hose from aircraft
   - Cap aircraft receptacle
   - Remove bonding cable
   - Document fuel quantity and time

#### 4.3.4 Safety Interlocks During Fueling

**Automatic Shutdown (ESD) Triggers:**

| Condition | Action | Response Time |
|-----------|--------|---------------|
| H2 detected > 25% LEL | Stop fueling, close ESVs, vent system | < 3 sec |
| Fire detected | Stop fueling, close ESVs, activate fire suppression | < 3 sec |
| Aircraft tank overfill (high-high level) | Stop fueling immediately | < 2 sec |
| Fueling hose disconnected (break-away) | Close ESVs, stop pump | < 1 sec |
| Loss of bonding continuity | Stop fueling | < 3 sec |
| Aircraft emergency signal | Stop fueling, close ESVs | < 2 sec |
| Manual E-stop pressed | Stop fueling, close ESVs | < 1 sec |
| Communication loss | Stop fueling (after timeout) | 10 sec |

**Warnings (Continue Fueling with Caution):**

| Condition | Action | Operator Response |
|-----------|--------|-------------------|
| H2 detected 10-25% LEL | Alarm, log event | Investigate source, increase ventilation |
| Flow rate deviation | Alarm | Adjust pump speed or valve position |
| Pressure deviation | Alarm | Check for blockage or leak |
| Aircraft tank level approaching target | Warning | Prepare for topping-off phase |

#### 4.3.5 Emergency Procedures

**Emergency Disconnect:**
- Break-away coupling activates automatically on excessive pull
- Both sides seal immediately (double-shutoff design)
- GSE side vents pressure safely
- Aircraft side remains sealed

**Spill Response:**
- Small spill (< 10 liters): Allow evaporation, ventilate area, control ignition sources
- Large spill (> 10 liters): Activate emergency response, evacuate area, monitor H2 levels

**Fire Response:**
- LH2 pool fire: Do not extinguish (risk of vapor cloud), cool surrounding equipment with water spray
- Equipment fire: Use appropriate extinguisher (CO2, dry chemical), activate fixed fire suppression

#### 4.3.6 Monitoring and Control

**Operator Interface (HMI):**
- Real-time display of: flow rate, totalizer, pressures, temperatures, H2 levels
- Alarms: Prioritized, color-coded, with acknowledge button
- Trend charts: Key parameters over time
- Fueling summary: Start time, end time, quantity delivered

**Data Logging:**
- All fueling operations logged
- Stored for: safety analysis, billing, maintenance planning
- Minimum retention: 5 years

#### 4.3.7 Defueling Process (if required)

**Aircraft LH2 Defueling:**
- Similar process in reverse
- Defuel pump on GSE (if needed) or use aircraft tank pressure
- Transfer LH2 from aircraft to GSE recovery tank
- Purge aircraft system with GH2 or nitrogen (if extended downtime)

## 5. Cross-References

- Related ATA Chapters: ATA 12 (Servicing), ATA 28 (Fuel)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-02-01A LH2 System Schematics](../03-90-02_H2_GSE_Schematics/03-90-02-01A_LH2_System_Schematics.md)
  - [03-90-02-04A H2 Safety Schematics](../03-90-02_H2_GSE_Schematics/03-90-02-04A_H2_Safety_Schematics.md)
  - [03-90-05-02A H2 Transfer PFD](./03-90-05-02A_H2_Transfer_PFD.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 H2 Operations Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
