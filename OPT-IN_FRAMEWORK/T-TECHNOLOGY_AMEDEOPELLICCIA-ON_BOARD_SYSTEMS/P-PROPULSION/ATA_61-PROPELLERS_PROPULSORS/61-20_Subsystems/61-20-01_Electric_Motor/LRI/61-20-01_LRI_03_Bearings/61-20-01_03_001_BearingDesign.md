# 61-20-01_03_001 — Bearing System Design

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_03_001                        |
| **LRI ID**         | LRI-61-20-01-03                        |
| **Part Number**    | PN-EM-BRG-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Purpose

This document defines the design, selection, and integration of the **Bearing System** for the 4 MW PMSM Electric Motor used in the AMPEL360 Q100 EDF propulsors.

---

## 2. Bearing Configuration

### 2.1 Bearing Arrangement

| Position            | Type                        | Designation    | Locating/Non-Locating |
|---------------------|-----------------------------|----------------|-----------------------|
| **Drive End (DE)**  | Angular Contact Ball Bearing| 7220-BECBP     | Locating              |
| **Non-Drive End (NDE)** | Cylindrical Roller Bearing | NU 220 ECM    | Non-Locating (floating)|

### 2.2 Drive End Bearing Specifications

| Parameter                  | Value                     | Unit    |
|----------------------------|---------------------------|---------|
| **Type**                   | Angular Contact Ball      | —       |
| **Bearing Designation**    | 7220-BECBP                | —       |
| **Bore Diameter (d)**      | 100                       | mm      |
| **Outer Diameter (D)**     | 180                       | mm      |
| **Width (B)**              | 34                        | mm      |
| **Contact Angle**          | 40°                       | —       |
| **Basic Dynamic Load (C)** | 138                       | kN      |
| **Basic Static Load (C0)** | 118                       | kN      |
| **Limiting Speed (grease)**| 4,800                     | RPM     |
| **Reference Speed**        | 3,800                     | RPM     |

### 2.3 Non-Drive End Bearing Specifications

| Parameter                  | Value                     | Unit    |
|----------------------------|---------------------------|---------|
| **Type**                   | Cylindrical Roller        | —       |
| **Bearing Designation**    | NU 220 ECM                | —       |
| **Bore Diameter (d)**      | 100                       | mm      |
| **Outer Diameter (D)**     | 180                       | mm      |
| **Width (B)**              | 34                        | mm      |
| **Basic Dynamic Load (C)** | 255                       | kN      |
| **Basic Static Load (C0)** | 265                       | kN      |
| **Limiting Speed (grease)**| 4,500                     | RPM     |
| **Axial Float**            | ±1.5                      | mm      |

---

## 3. Loading Analysis

### 3.1 Load Sources

| Load Type                  | DE Bearing        | NDE Bearing       | Unit    |
|----------------------------|-------------------|-------------------|---------|
| **Rotor Weight**           | 450               | 450               | N       |
| **Magnetic Pull (radial)** | 2,500             | 2,500             | N       |
| **Thrust (fan torque)**    | 8,000             | 0                 | N       |
| **Dynamic Loads (max)**    | 5,000             | 5,000             | N       |
| **Equivalent Load (P)**    | 12,800            | 6,200             | N       |

### 3.2 Life Calculation

| Parameter                  | DE Bearing        | NDE Bearing       | Unit    |
|----------------------------|-------------------|-------------------|---------|
| **Equivalent Load (P)**    | 12.8              | 6.2               | kN      |
| **Basic Rating Life (L10)**| 42,000            | 220,000           | hours   |
| **Adjusted Life (L10a)**   | 65,000            | 340,000           | hours   |
| **Design Target Life**     | 30,000            | 30,000            | hours   |
| **Safety Factor**          | 2.2               | 11.3              | —       |

---

## 4. Lubrication System

### 4.1 Lubrication Method

| Parameter                  | Value                                  |
|----------------------------|----------------------------------------|
| **Lubrication Type**       | Oil mist / Oil-air                     |
| **Oil Specification**      | MIL-PRF-23699 (Turbine Oil)            |
| **Operating Viscosity**    | 5 cSt (at 100°C)                       |
| **Flow Rate (per bearing)**| 0.3 L/min                              |
| **Oil Temperature (inlet)**| 60°C (max)                             |
| **Drain Temperature**      | 90°C (max)                             |

### 4.2 Sealing

| Position                   | Seal Type                  | Material         |
|----------------------------|----------------------------|------------------|
| **DE Inner**               | Labyrinth seal             | Stainless steel  |
| **DE Outer**               | Lip seal + air purge       | Viton            |
| **NDE Inner**              | Labyrinth seal             | Stainless steel  |
| **NDE Outer**              | Lip seal + air purge       | Viton            |

---

## 5. Thermal Design

### 5.1 Heat Sources

| Source                     | Heat Generation (W)        | Cooling Method            |
|----------------------------|----------------------------|---------------------------|
| **Bearing Friction (DE)**  | 850                        | Oil lubrication           |
| **Bearing Friction (NDE)** | 650                        | Oil lubrication           |

### 5.2 Temperature Limits

| Location                   | Max Operating | Alarm         | Trip          |
|----------------------------|---------------|---------------|---------------|
| **DE Bearing Outer Race**  | 90°C          | 100°C         | 110°C         |
| **NDE Bearing Outer Race** | 85°C          | 95°C          | 105°C         |
| **Oil Drain**              | 90°C          | 100°C         | 110°C         |

---

## 6. Condition Monitoring

### 6.1 Sensors

| Sensor ID      | Type                  | Location        | Range             |
|----------------|-----------------------|-----------------|-------------------|
| VIB-DE-01      | Accelerometer         | DE housing      | 0-20 g            |
| VIB-DE-02      | Accelerometer         | DE housing      | 0-20 g            |
| VIB-NDE-01     | Accelerometer         | NDE housing     | 0-20 g            |
| TEMP-DE-01     | RTD (PT100)           | DE outer race   | -40 to +150°C     |
| TEMP-NDE-01    | RTD (PT100)           | NDE outer race  | -40 to +150°C     |

### 6.2 Monitoring Parameters

| Parameter                  | Normal Range      | Warning         | Critical        |
|----------------------------|-------------------|-----------------|-----------------|
| **Vibration (overall)**    | < 2.0 mm/s RMS    | > 4.0 mm/s      | > 7.0 mm/s      |
| **Bearing Temperature**    | < 80°C            | > 95°C          | > 105°C         |
| **Oil Flow Rate**          | 0.25-0.35 L/min   | < 0.20 L/min    | < 0.15 L/min    |

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01
