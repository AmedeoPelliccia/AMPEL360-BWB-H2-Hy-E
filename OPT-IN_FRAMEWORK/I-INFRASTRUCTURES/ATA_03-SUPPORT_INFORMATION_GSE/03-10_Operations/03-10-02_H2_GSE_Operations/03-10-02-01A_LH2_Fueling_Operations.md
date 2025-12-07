---
Title: "LH₂ Fueling Operations"
Identifier: "AMPEL360-03-10-02-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES GSE Operations"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
ReviewDue: "2026-06-07"
Effectivity: "Q100 INTEGRA H₂ GSE Operations"
Abstract: "Operational procedures for liquid hydrogen (LH₂) aircraft refueling using ground support equipment, including safety protocols and cryogenic handling requirements."
Keywords: ["LH₂","Liquid Hydrogen","Fueling","Refueling","Cryogenic","GSE","ATA 03"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE AS6968 - Hydrogen Aircraft Refueling GSE"
  - "ISO 19880-8 - Gaseous Hydrogen Fuelling Stations"
  - "NFPA 2 - Hydrogen Technologies Code"
  - "IEC 60079 - ATEX Requirements"
Links:
  ParentBucket: "../"
  CrossRefs:
    Safety: "../../03-00_GENERAL/03-00-02_Safety/"
    Requirements: "../../03-00_GENERAL/03-00-03_Requirements/"
    SafetyOps: "../03-10-05_GSE_Safety_Operations/"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-10-02-01A — LH₂ Fueling Operations

## 1. Purpose

This document establishes operational procedures for liquid hydrogen (LH₂) aircraft refueling operations for AMPEL360 BWB aircraft, covering all aspects of safe cryogenic fuel transfer from ground storage systems to aircraft fuel tanks at -253°C.

## 2. Scope

This document covers:
- LH₂ refueling operational procedures
- Pre-fueling preparation and safety checks
- Fuel transfer operations and monitoring
- Post-fueling disconnect and system purging
- Emergency shutdown procedures
- Cryogenic safety protocols
- Personnel qualification requirements

This applies to all LH₂ refueling operations at certified airports with approved H₂ infrastructure.

## 3. Applicable Documents

### 3.1 External Standards
- **SAE AS6968** — Hydrogen Aircraft Refueling Ground Support Equipment
- **ISO 19880-8** — Gaseous Hydrogen — Fuelling Stations (Part 8: Airport Applications)
- **NFPA 2** — Hydrogen Technologies Code
- **IEC 60079** — Explosive Atmospheres (ATEX) Equipment Requirements
- **CGA H-3** — Cryogenic Hydrogen Storage
- **IATA DGR** — Dangerous Goods Regulations (H₂ as cargo consideration)

### 3.2 Internal References
- `03-00-02_Safety` — GSE Safety Requirements
- `03-10-05-02A_H2_Safety_Operations.md` — H₂ Safety Operations
- `03-10-05-03A_Emergency_Response_Ops.md` — Emergency Response
- ATA 28 (Aircraft Fuel System)

## 4. Operations Description

### 4.1 Overview

LH₂ refueling operations involve the transfer of cryogenic liquid hydrogen at -253°C (-423°F) from ground storage systems to aircraft fuel tanks. These operations require specialized GSE, trained personnel, and strict safety protocols due to hydrogen's unique properties:

- **Cryogenic temperature**: -253°C requiring specialized materials and handling
- **High flammability**: Wide flammability range (4-75% in air)
- **Low ignition energy**: 0.02 mJ (vs. 0.24 mJ for gasoline)
- **High diffusivity**: Rapid dispersion and potential for accumulation
- **Embrittlement risk**: Hydrogen embrittlement of metals at cryogenic temperatures

### 4.2 Operating Procedures

#### 4.2.1 Pre-Fueling Operations

| Step | Action | Responsible | Notes |
|------|--------|-------------|-------|
| 1 | Verify aircraft positioning and brakes set | Ramp Agent | Aircraft must be stable |
| 2 | Establish safety zone (7.5m radius minimum) | H₂ Safety Officer | Post barriers and signage |
| 3 | Verify weather conditions within limits | H₂ Operations Supervisor | Wind <15 kt, no precipitation |
| 4 | Inspect H₂ bowser/hydrant equipment | H₂ Refueler Operator | Check for leaks, damage, certification current |
| 5 | Test H₂ leak detection systems | H₂ Safety Officer | Verify all sensors operational |
| 6 | Position fire suppression equipment | Airport Fire/Rescue | Within 30m, ready state |
| 7 | Verify personnel PPE and qualifications | H₂ Operations Supervisor | Cryogenic gloves, face shield, H₂ certification |
| 8 | Conduct pre-fueling safety briefing | H₂ Operations Supervisor | All personnel acknowledge hazards |
| 9 | Ground bonding aircraft and GSE | H₂ Refueler Operator | Verify continuity <10 Ω |
| 10 | Connect H₂ leak detection to aircraft | H₂ Refueler Operator | Monitor aircraft tank venting |
| 11 | Verify aircraft fuel system ready | Flight Crew / H₂ Refueler | Fuel panel indications normal |
| 12 | Obtain clearance to connect | H₂ Operations Supervisor | Final authorization |

#### 4.2.2 Fueling Operations

| Step | Action | Responsible | Notes |
|------|--------|-------------|-------|
| 1 | Position fueling adapter at aircraft connection | H₂ Refueler Operator | Align carefully to avoid damage |
| 2 | Cool down transfer line (if required) | H₂ Refueler Operator | Vent initial boil-off safely |
| 3 | Connect fueling adapter to aircraft receptacle | H₂ Refueler Operator | Verify proper engagement |
| 4 | Verify connection integrity | H₂ Safety Officer | Check for leaks with detector |
| 5 | Open aircraft fuel valve (slow) | H₂ Refueler Operator | Control initial flow rate |
| 6 | Begin LH₂ transfer at low flow rate | H₂ Refueler Operator | 50-100 kg/min initial rate |
| 7 | Monitor tank temperature and pressure | H₂ Refueler Operator | Stay within aircraft limits |
| 8 | Increase to normal flow rate | H₂ Refueler Operator | Up to 500 kg/min nominal |
| 9 | Monitor for leaks continuously | H₂ Safety Officer | Visual and detector checks |
| 10 | Monitor fuel quantity and transfer rate | H₂ Refueler Operator | Compare aircraft and bowser meters |
| 11 | Slow transfer rate near target quantity | H₂ Refueler Operator | Final 5% at reduced rate |
| 12 | Stop transfer at target fuel load | H₂ Refueler Operator | Verify aircraft fuel quantity |

#### 4.2.3 Post-Fueling Operations

| Step | Action | Responsible | Notes |
|------|--------|-------------|-------|
| 1 | Close aircraft fuel valve | H₂ Refueler Operator | Stop flow before disconnect |
| 2 | Purge transfer line with GH₂ or inert gas | H₂ Refueler Operator | Remove liquid from line |
| 3 | Wait for line warmup (if required) | H₂ Refueler Operator | Prevent ice formation on disconnect |
| 4 | Disconnect fueling adapter from aircraft | H₂ Refueler Operator | Install protective caps |
| 5 | Stow transfer equipment safely | H₂ Refueler Operator | Secure hoses and adapters |
| 6 | Remove ground bonding | H₂ Refueler Operator | After all connections removed |
| 7 | Monitor for residual leaks | H₂ Safety Officer | 5-minute post-fueling check |
| 8 | Complete fueling documentation | H₂ Refueler Operator | Record quantity, time, conditions |
| 9 | Brief flight crew on fueling completion | H₂ Operations Supervisor | Confirm fuel load and any issues |
| 10 | Remove safety barriers | H₂ Safety Officer | After all clear confirmed |

### 4.3 Safety Considerations

#### 4.3.1 Critical Safety Requirements

- **No Ignition Sources**: No smoking, open flames, spark-producing tools within safety zone
- **Ventilation**: Operations in open air only; adequate natural ventilation
- **Leak Detection**: Continuous monitoring with calibrated H₂ sensors (alarm at 1% LEL)
- **Fire Suppression**: Water spray or foam equipment ready; water fog for vapor dispersion
- **Personnel Limit**: Only essential, qualified personnel in safety zone
- **Communication**: Continuous radio contact; emergency stop procedures known
- **Weather Monitoring**: Abort if wind >15 kt, precipitation, or lightning within 5 nm

#### 4.3.2 Cryogenic Hazards

- **Skin Contact**: Can cause severe frostbite in seconds
- **Eye Exposure**: Can cause permanent damage
- **Material Embrittlement**: Many metals become brittle at LH₂ temperatures
- **Oxygen Enrichment**: Air liquefaction can create O₂-enriched zones (fire hazard)
- **Pressure Build-up**: Trapped liquid expands 848× on warming to gas

#### 4.3.3 Emergency Procedures

**If H₂ Leak Detected:**
1. Stop fuel transfer immediately
2. Close all valves
3. Activate emergency ventilation fans (if available)
4. Evacuate non-essential personnel from safety zone
5. Monitor H₂ concentration until safe (<25% LEL)
6. Notify airport fire/rescue
7. Do not resume until leak source identified and corrected

**If Fire Occurs:**
1. Activate emergency stop (E-stop button)
2. Close all fuel valves
3. Evacuate all personnel from immediate area
4. Alert airport fire/rescue
5. Do not attempt to extinguish H₂ flame unless absolutely necessary
6. Use water spray to cool surrounding equipment/structures
7. Allow H₂ to burn out if controlled and not threatening other areas

## 5. Equipment Requirements

| Equipment | Specification | Quantity |
|-----------|---------------|----------|
| LH₂ Fueling Bowser | Cryogenic tanker, 5,000-10,000 kg capacity | 1 per operation |
| Transfer Hose & Adapter | Vacuum-insulated, rated -253°C, ATEX certified | 1 set |
| H₂ Leak Detectors | Response time <2 sec, alarm at 1% LEL | 4 minimum (portable + fixed) |
| Cryogenic PPE | Face shield, insulated gloves, protective clothing | Per operator |
| Grounding Equipment | Bonding cables, continuity tester | 1 set |
| Fire Suppression | Water spray/foam equipment, 200 L/min capacity | 1 unit within 30m |
| Communication Radios | Intrinsically safe, dedicated H₂ ops channel | Per crew member |
| Environmental Sensors | Wind speed, temperature, humidity monitors | 1 set |

## 6. Cross-References

- Related ATA Chapters: ATA 28 (Fuel System), ATA 02 (Operations)
- Parent Document: 03-10_Operations
- Related Safety: 03-10-05-02A_H2_Safety_Operations
- Emergency Response: 03-10-05-03A_Emergency_Response_Ops
- Operator Procedures: 03-10-06_GSE_Operator_Procedures

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.
