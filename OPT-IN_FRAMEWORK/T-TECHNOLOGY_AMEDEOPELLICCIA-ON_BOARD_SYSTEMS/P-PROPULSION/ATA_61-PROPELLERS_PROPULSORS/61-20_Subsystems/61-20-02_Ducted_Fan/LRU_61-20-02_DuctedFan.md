# LRU 61-20-02 — Ducted Fan Assembly

| Field                | Value                                  |
|----------------------|----------------------------------------|
| **LRU ID**           | LRU-61-20-02                           |
| **Part Number**      | PN-EDF-DFA-001                         |
| **ATA Chapter**      | 61 – Propellers / Propulsors           |
| **Subsystem**        | 61-20-02_Ducted_Fan                    |
| **Programme**        | AMPEL360 BWB H₂ Hy-E Q100              |
| **Status**           | Active                                 |
| **Version**          | 1.0                                    |
| **Last Updated**     | 2025-12-01                             |
| **Owner**            | AMPEL360 Propulsion Team               |
| **Standard**         | OPT-IN Framework v1.2                  |

---

## 1. LRU Overview

The **Ducted Fan Assembly (DFA)** is a Line Replaceable Unit (LRU) that represents the complete aerodynamic thrust-producing module of each EDF propulsor.

### 1.1 LRU Classification

| Attribute              | Value                                      |
|------------------------|--------------------------------------------|
| **LRU Type**           | Mechanical / Aerodynamic Assembly          |
| **Replacement Level**  | Line (On-Wing)                             |
| **MTBF Target**        | 25,000 flight hours                        |
| **MTTR Target**        | 4 hours                                    |
| **Interchangeability** | Yes (all 4 propulsor positions)            |

---

## 2. LRU Composition

This LRU comprises the following Line Replaceable Items (LRI):

| LRI ID                    | Description           | Part Number       | Qty |
|---------------------------|-----------------------|-------------------|-----|
| LRI-61-20-02-01           | Rotor Assembly        | PN-DF-ROT-001     | 1   |
| LRI-61-20-02-02           | Stator Assembly       | PN-DF-STA-001     | 1   |
| LRI-61-20-02-03           | Nacelle Duct Assembly | PN-DF-NAC-001     | 1   |

---

## 3. Physical Characteristics

| Parameter                | Value                     | Unit    |
|--------------------------|---------------------------|---------|
| **Overall Diameter**     | 1,200                     | mm      |
| **Axial Length**         | 850                       | mm      |
| **Total Mass**           | 185                       | kg      |
| **Blade Count (Rotor)**  | 14                        | blades  |
| **Stator Vane Count**    | 21                        | vanes   |

---

## 4. Performance Envelope

| Parameter                | Nominal Value | Maximum     | Unit    |
|--------------------------|---------------|-------------|---------|
| **Thrust (Cruise)**      | 25            | 32          | kN      |
| **Thrust (Max T/O)**     | 40            | 45          | kN      |
| **Fan Speed (Cruise)**   | 3,800         | 4,200       | RPM     |
| **Bypass Ratio**         | 8.5           | —           | —       |
| **Fan Pressure Ratio**   | 1.45          | 1.55        | —       |

---

## 5. Interfaces

### 5.1 Mechanical Interfaces

| Interface ID    | Connected To                    | Type           | Description                          |
|-----------------|---------------------------------|----------------|--------------------------------------|
| IF-DF-M01       | 61-20-01_Electric_Motor         | Shaft Coupling | Torque transfer, 4 MW nominal        |
| IF-DF-M02       | 61-50_Structures                | Flange Mount   | Nacelle frame attachment (8× bolts)  |
| IF-DF-M03       | 61-20-06_Health_Sensing         | Sensor Mounts  | Accelerometers, strain gauges        |

### 5.2 Aerodynamic Interfaces

| Interface ID    | Description                                           |
|-----------------|-------------------------------------------------------|
| IF-DF-A01       | Inlet flow interface (ambient / boundary layer)       |
| IF-DF-A02       | Exhaust nozzle interface (thrust vector)              |

---

## 6. Maintenance Concept

### 6.1 Replacement Procedure

1. **Preparation:** Secure aircraft, de-energize propulsion system
2. **Access:** Remove nacelle access panels (4× panels)
3. **Disconnect:** Shaft coupling, sensor harnesses, cooling lines
4. **Remove:** Release 8× flange bolts, extract LRU with tooling
5. **Install:** Reverse procedure, torque to specification
6. **Verification:** Run-up test, vibration check, leak test

### 6.2 Scheduled Maintenance

| Task ID          | Description                      | Interval        |
|------------------|----------------------------------|-----------------|
| MT-DF-001        | Visual inspection               | 500 FH          |
| MT-DF-002        | Blade tip clearance check       | 1,000 FH        |
| MT-DF-003        | Borescope inspection            | 2,500 FH        |
| MT-DF-004        | Full disassembly / overhaul     | 12,500 FH       |

---

## 7. Certification References

| Requirement            | Reference                              |
|------------------------|----------------------------------------|
| **Structural Integrity** | CS-25.571, CS-25.573                 |
| **Bird Strike**        | CS-25.631                              |
| **Containment**        | CS-E 810, CS-25.903(d)                 |
| **Noise**              | CS-36 / ICAO Annex 16                  |

---

## 8. Related Documentation

- [LRI/61-20-02_LRI_01_Rotor/](./LRI/61-20-02_LRI_01_Rotor/)
- [LRI/61-20-02_LRI_02_Stator/](./LRI/61-20-02_LRI_02_Stator/)
- [LRI/61-20-02_LRI_03_Nacelle/](./LRI/61-20-02_LRI_03_Nacelle/)
- [meta/61-20-02_SUBSYSTEM.yaml](./meta/61-20-02_SUBSYSTEM.yaml)
- [SysML/](./SysML/)

---

## 9. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** Produced with AI assistance (GitHub Copilot)
- **Approval:** Pending human review per `61-00-11_EIS_Versions_Tags`
- **Last AI Update:** 2025-12-01
