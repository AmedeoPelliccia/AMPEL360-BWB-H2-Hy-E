# 61-00-05-02-04A - Grounding and Bonding Interface

**Document ID:** 61-00-05-02-04A  
**Title:** Grounding and Bonding Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the electrical grounding and bonding requirements for the Q100 propulsor system to ensure electrical safety, EMI/EMC compliance, lightning protection, and fault current management.

---

## 2. Scope

This specification covers:
- Protective earth (PE) grounding
- Signal reference grounding
- EMI shielding and chassis bonding
- Lightning protection bonding
- Fault current return paths
- Static discharge provisions

### 2.1 Applicable Units
- All four Q100 propulsor units
- Associated electrical enclosures and structures

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements document |
| [SAE ARP5414](https://www.sae.org/standards/content/arp5414a/) | Aircraft Lightning Zoning | Lightning protection |
| [SAE ARP5416](https://www.sae.org/standards/content/arp5416/) | Aircraft Lightning Test Methods | Lightning testing |
| [MIL-B-5087B](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35977) | Bonding, Electrical, and Lightning Protection | Bonding standard |
| [DO-160G Section 17](https://www.rtca.org/content/standards-guidance-materials) | Voltage Spike | Transient protection |

---

## 4. Interface Description

### 4.1 Grounding System Architecture

```
Aircraft Structure Ground (Primary Reference)
           │
           ├─── Propulsor Mounting Structure Ground
           │    │
           │    ├─── Motor Housing Ground
           │    │    ├─── Motor Frame (Protective Earth)
           │    │    └─── Motor Stator Laminations
           │    │
           │    ├─── Power Electronics Enclosure Ground
           │    │    ├─── Chassis Ground
           │    │    ├─── Heat Sink Ground
           │    │    └─── Shield Termination Ground
           │    │
           │    └─── Nacelle Structure Ground
           │         ├─── Lightning Strike Attachment Points
           │         └─── Fan Duct Bonding
           │
           └─── Electrical System Ground (800V Return)
                ├─── High-Voltage Return Path
                └─── Fault Current Path
```

### 4.2 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Primary Ground Stud Size | M10 | — | — | Stainless steel |
| Ground Stud Torque | 25 | ±3 | Nm | With lock washer |
| Ground Cable Gauge (Primary PE) | 6 AWG | — | — | Minimum |
| Ground Cable Gauge (Secondary PE) | 10 AWG | — | — | Minimum |
| Bonding Jumper Gauge | 12 AWG | — | — | Flexible braid |
| Contact Surface Finish | Tin-plated or bare aluminum | — | — | Anti-corrosion |
| Bonding Strap Material | Copper braid or aluminum strap | — | — | High conductivity |
| Bonding Strap Cross-Section | ≥25 | — | mm² | Current capacity |

### 4.3 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| GND-61-001 | Ground loop resistance (propulsor to aircraft structure) | <2.5 mΩ | Test |
| GND-61-002 | Bonding jumper resistance | <1 mΩ | Test |
| GND-61-003 | Ground fault current capacity | >10,000 A for 100 ms | Analysis, Test |
| GND-61-004 | Lightning current capacity | Zone 2A: 200 kA (Component A) | Analysis per SAE ARP5414 |
| GND-61-005 | Shield continuity (end-to-end) | <10 mΩ | Test |
| GND-61-006 | Isolation (high voltage to PE) | >10 MΩ at 500 VDC | Test |
| GND-61-007 | Galvanic corrosion protection | Dissimilar metal isolation or protective plating | Inspection |
| GND-61-008 | Common-mode noise rejection | >60 dB at power line frequencies | Test |

### 4.4 Environmental Constraints

| Parameter | Operating Range | Survival Range | Unit | Notes |
|-----------|----------------|----------------|------|-------|
| Temperature | -40 to +125 | -55 to +150 | °C | Joint temperature |
| Vibration | 10g RMS | 20g peak | g | Per DO-160G Category T |
| Corrosion Resistance | 1,000 hours | — | hours | Salt fog per ASTM B117 |
| Humidity | 0 to 95% | — | % RH | Non-condensing |

---

## 5. Interface Control

### 5.1 Grounding Points

| Grounding Point | Location | Stud/Connection Type | Cable/Strap Gauge | Function |
|-----------------|----------|---------------------|-------------------|----------|
| GP-61-001 | Motor housing base flange | M10 stud | 6 AWG | Primary PE |
| GP-61-002 | Power electronics chassis | M10 stud | 6 AWG | Primary PE |
| GP-61-003 | Propulsor mounting flange | Bonding teeth | 12 AWG jumper | Structure bond |
| GP-61-004 | Fan duct (forward) | M8 stud | 10 AWG | Lightning protection |
| GP-61-005 | Fan duct (aft) | M8 stud | 10 AWG | Lightning protection |
| GP-61-006 | Nacelle inlet lip | Bonding strap | 25 mm² strap | Lightning protection |
| GP-61-007 | Cable shield terminations | Shield clamp | Shield braid | EMI grounding |

### 5.2 Bonding Requirements

| Interface | Bonding Method | Resistance Target | Test Frequency |
|-----------|----------------|-------------------|----------------|
| Motor to mounting structure | Direct metal-to-metal + bonding jumper | <2.5 mΩ | Assembly, annual |
| Power electronics to motor | Dedicated ground bus | <1 mΩ | Assembly |
| Cable shields to chassis | 360° clamp or backshell | <10 mΩ | Assembly |
| Nacelle to propulsor | Bonding jumpers at mounting points | <5 mΩ | Assembly, annual |
| Dissimilar metals | Isolation washer + protective plating | No galvanic couple | Inspection |

### 5.3 Lightning Protection Zones

| Zone | Description | Propulsor Components | Bonding Requirements |
|------|-------------|----------------------|----------------------|
| 2A | Direct strike zone | Fan duct inlet, spinner | Low-impedance bond, <10 mΩ |
| 2B | Swept stroke zone | Fan duct exterior, nacelle | Multiple bonding jumpers |
| 3 | Indirect effects zone | Motor housing, electronics | Standard bonding, surge protection |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| GND-T-001 | Ground loop resistance | <2.5 mΩ propulsor to structure | 4-wire Kelvin measurement |
| GND-T-002 | Bonding jumper resistance | <1 mΩ per jumper | 4-wire measurement |
| GND-T-003 | Lightning indirect effects | Per DO-160G Section 22, no damage | Surge test per MIL-STD-461 |
| GND-T-004 | Ground fault current test | 10,000 A for 100 ms, no damage | High-current pulse test |
| GND-T-005 | Isolation resistance | >10 MΩ at 500 VDC | Megohmmeter |
| GND-T-006 | EMI shielding effectiveness | >40 dB at 10 kHz - 1 GHz | Shielded room, transfer impedance |
| GND-T-007 | Corrosion resistance | 1,000 hours salt fog, no degradation | ASTM B117 |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Ground resistance (all points) | 100% | 4-wire Kelvin measurement |
| Bonding jumper installation | 100% | Visual, torque verification |
| Isolation resistance (HV to PE) | 100% | Megohmmeter (500 VDC) |
| Surface preparation (mating surfaces) | 100% | Visual, cleanliness check |
| Torque verification (ground studs) | 100% | Torque wrench |
| Galvanic compatibility | 100% (design), 10% (production) | Material review, visual |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 24](../../../../E-ELECTRICAL/ATA_24-ELECTRICAL_POWER/README.md) — Electrical Power (grounding architecture)
- [ATA 92](../../../../ATA_92-ELECTRICAL_INSTALLATION/README.md) — Electrical Installation (bonding practices)
- [ATA 20](../../../../ATA_20-STANDARD_PRACTICES/README.md) — Standard Practices (bonding procedures)

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-02-01A — Power Distribution (fault current paths)
- 61-00-02-SFHA-001 — System Functional Hazard Assessment (electrical safety)

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-02-03A_Sensor_Connections](61-00-05-02-03A_Sensor_Connections.md) · [Parent: 61-00-05_Interfaces](../README.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Electrical Interfaces  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
