# LRU 61-20-01 — Electric Motor Assembly

| Field                | Value                                  |
|----------------------|----------------------------------------|
| **LRU ID**           | LRU-61-20-01                           |
| **Part Number**      | PN-EDF-EMA-001                         |
| **ATA Chapter**      | 61 – Propellers / Propulsors           |
| **Subsystem**        | 61-20-01_Electric_Motor                |
| **Programme**        | AMPEL360 BWB H₂ Hy-E Q100              |
| **Status**           | Active                                 |
| **Version**          | 1.0                                    |
| **Last Updated**     | 2025-12-01                             |
| **Owner**            | AMPEL360 Propulsion Team               |
| **Standard**         | OPT-IN Framework v1.2                  |

---

## 1. LRU Overview

The **Electric Motor Assembly (EMA)** is a Line Replaceable Unit (LRU) that represents the complete 4 MW high-power electric machine used in each EDF propulsor of the AMPEL360 Q100.

### 1.1 LRU Classification

| Attribute              | Value                                      |
|------------------------|--------------------------------------------|
| **LRU Type**           | Electromechanical / Power Conversion       |
| **Motor Type**         | Permanent Magnet Synchronous Motor (PMSM)  |
| **Replacement Level**  | Line (On-Wing)                             |
| **MTBF Target**        | 30,000 flight hours                        |
| **MTTR Target**        | 6 hours                                    |
| **Interchangeability** | Yes (all 4 propulsor positions)            |

---

## 2. LRU Composition

This LRU comprises the following Line Replaceable Items (LRI):

| LRI ID                    | Description              | Part Number       | Qty |
|---------------------------|--------------------------|-------------------|-----|
| LRI-61-20-01-01           | Stator Assembly          | PN-EM-STA-001     | 1   |
| LRI-61-20-01-02           | Rotor Assembly           | PN-EM-ROT-001     | 1   |
| LRI-61-20-01-03           | Bearing System           | PN-EM-BRG-001     | 1   |
| LRI-61-20-01-04           | Housing/Frame Assembly   | PN-EM-HSG-001     | 1   |

---

## 3. Physical Characteristics

| Parameter                | Value                     | Unit    |
|--------------------------|---------------------------|---------|
| **Overall Diameter**     | 650                       | mm      |
| **Axial Length**         | 520                       | mm      |
| **Total Mass**           | 380                       | kg      |
| **Power Density**        | 10.5                      | kW/kg   |
| **Pole Count**           | 12                        | poles   |
| **Slot Count**           | 72                        | slots   |

---

## 4. Performance Envelope

| Parameter                  | Nominal Value | Maximum     | Unit    |
|----------------------------|---------------|-------------|---------|
| **Continuous Power**       | 4,000         | 4,400       | kW      |
| **Peak Power (30s)**       | 4,800         | 5,200       | kW      |
| **Nominal Speed**          | 3,800         | 4,200       | RPM     |
| **Maximum Torque**         | 10,050        | 11,100      | N·m     |
| **Peak Efficiency**        | 98.5          | —           | %       |
| **Nominal DC Voltage**     | 800           | 850         | V       |
| **Phase Current (RMS)**    | 1,800         | 2,200       | A       |

---

## 5. Interfaces

### 5.1 Mechanical Interfaces

| Interface ID    | Connected To                    | Type           | Description                          |
|-----------------|---------------------------------|----------------|--------------------------------------|
| IF-EM-M01       | 61-20-02_Ducted_Fan             | Shaft Coupling | Direct-drive torque transfer         |
| IF-EM-M02       | 61-50_Structures                | Flange Mount   | Nacelle frame attachment (12× bolts) |
| IF-EM-M03       | 61-20-06_Health_Sensing         | Sensor Mounts  | Temperature, vibration probes        |

### 5.2 Electrical Interfaces

| Interface ID    | Connected To                    | Type           | Description                          |
|-----------------|---------------------------------|----------------|--------------------------------------|
| IF-EM-E01       | 61-20-04_Propulsor_Control_Unit | 3-Phase Power  | 800 VDC / 3-phase AC power input     |
| IF-EM-E02       | 61-20-04_Propulsor_Control_Unit | Signal         | Resolver / encoder feedback          |
| IF-EM-E03       | 61-20-06_Health_Sensing         | Signal         | Temperature sensors (12× RTDs)       |

### 5.3 Thermal Interfaces

| Interface ID    | Connected To                    | Type           | Description                          |
|-----------------|---------------------------------|----------------|--------------------------------------|
| IF-EM-T01       | 61-20-05_Cooling_Loop           | Liquid Cooling | Stator jacket coolant (glycol-water) |
| IF-EM-T02       | 61-20-05_Cooling_Loop           | Oil Cooling    | Bearing lubrication / cooling        |

---

## 6. Maintenance Concept

### 6.1 Replacement Procedure

1. **Preparation:** Secure aircraft, de-energize HV system, isolate cooling
2. **Access:** Remove nacelle access panels (6× panels)
3. **Disconnect:** Power cables, signal harnesses, cooling lines
4. **Separate:** Shaft coupling from ducted fan
5. **Remove:** Release 12× flange bolts, extract LRU with lifting fixture
6. **Install:** Reverse procedure, torque to specification
7. **Verification:** Insulation test, alignment check, run-up test

### 6.2 Scheduled Maintenance

| Task ID          | Description                           | Interval        |
|------------------|---------------------------------------|-----------------|
| MT-EM-001        | Visual inspection (external)          | 500 FH          |
| MT-EM-002        | Insulation resistance test            | 1,000 FH        |
| MT-EM-003        | Bearing vibration analysis            | 1,000 FH        |
| MT-EM-004        | Winding temperature trending          | Continuous      |
| MT-EM-005        | Cooling system leak check             | 2,500 FH        |
| MT-EM-006        | Full disassembly / overhaul           | 15,000 FH       |

---

## 7. Certification References

| Requirement              | Reference                              |
|--------------------------|----------------------------------------|
| **Electrical Safety**    | CS-25.1353, CS-25.1355                 |
| **Fire Protection**      | CS-25.863, CS-25.1181                  |
| **EMC/HIRF**             | CS-25.1316, CS-25.1317                 |
| **Continued Airworthiness** | CS-25.1529                          |
| **Motor Qualification**  | SAE ARP 5754, DO-160G                  |

---

## 8. Related Documentation

- [LRI/61-20-01_LRI_01_Stator/](./LRI/61-20-01_LRI_01_Stator/)
- [LRI/61-20-01_LRI_02_Rotor/](./LRI/61-20-01_LRI_02_Rotor/)
- [LRI/61-20-01_LRI_03_Bearings/](./LRI/61-20-01_LRI_03_Bearings/)
- [LRI/61-20-01_LRI_04_Housing/](./LRI/61-20-01_LRI_04_Housing/)
- [meta/61-20-01_SUBSYSTEM.yaml](./meta/61-20-01_SUBSYSTEM.yaml)
- [SysML/](./SysML/)

---

## 9. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** Produced with AI assistance (GitHub Copilot)
- **Approval:** Pending human review per `61-00-11_EIS_Versions_Tags`
- **Last AI Update:** 2025-12-01
