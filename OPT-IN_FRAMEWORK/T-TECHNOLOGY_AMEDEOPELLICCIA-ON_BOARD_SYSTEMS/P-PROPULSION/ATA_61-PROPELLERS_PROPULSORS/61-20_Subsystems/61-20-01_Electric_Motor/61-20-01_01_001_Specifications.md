# 61-20-01_01_001 — Electric Motor Specifications

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_01_001_Specifications         |
| **Subsystem**      | 61-20-01_Electric_Motor                |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. General Description

The Electric Motor is a high-power permanent magnet synchronous machine (PMSM) designed for the EDF propulsor of the AMPEL360 Q100 aircraft. Each motor converts DC electrical power from the aircraft power system into mechanical shaft power to drive the ducted fan.

---

## 2. Key Performance Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Continuous Power Rating | 4.0 | MW | At nominal operating point |
| Peak Power (30s) | 4.8 | MW | Emergency/transient |
| Nominal Speed | 3,600 | rpm | Cruise condition |
| Maximum Speed | 4,200 | rpm | Redline |
| Minimum Speed | 1,200 | rpm | Idle |
| Nominal Torque | 10,610 | Nm | At nominal power/speed |
| Peak Torque | 12,732 | Nm | 30s rating |
| Efficiency (nominal) | ≥ 96.5 | % | At design point |
| Power Factor | ≥ 0.95 | - | At nominal load |

---

## 3. Electrical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| DC Link Voltage (nominal) | 800 | V | From HV bus |
| DC Link Voltage Range | 650–900 | V | Operating range |
| Phase Current (RMS, nominal) | 1,700 | A | Per phase |
| Phase Current (RMS, peak) | 2,040 | A | 30s rating |
| Number of Phases | 3 | - | Star connection |
| Pole Pairs | 8 | - | 16-pole design |
| Winding Configuration | Distributed | - | Fractional slot |

---

## 4. Mechanical Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Outer Diameter | 650 | mm | Stator OD |
| Active Length | 400 | mm | Magnetic core |
| Total Length | 520 | mm | Including end windings |
| Shaft Diameter | 120 | mm | At coupling |
| Mass (dry) | 280 | kg | Target |
| Power Density | 14.3 | kW/kg | At nominal power |
| Moment of Inertia | 12.5 | kg·m² | Rotor |
| Critical Speed (1st) | > 5,000 | rpm | Above max operating |

---

## 5. Thermal Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Winding Insulation Class | H | - | 180°C limit |
| Max Winding Temperature | 160 | °C | Operating limit (derated) |
| Max Bearing Temperature | 120 | °C | Operating limit |
| Coolant Inlet Temperature | 40 | °C | Max design point |
| Heat Rejection (nominal) | 140 | kW | At nominal power |
| Heat Rejection (peak) | 192 | kW | At peak power |
| Cooling Flow Rate | 60 | L/min | Minimum |

---

## 6. Environmental Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Operating Altitude | 0–45,000 | ft |
| Ambient Temperature | -55 to +55 | °C |
| Humidity | 0–100% | Condensing |
| Vibration | [DO-160G](https://www.rtca.org/content/standards-guidance-materials) Cat S | - |
| EMC | [DO-160G](https://www.rtca.org/content/standards-guidance-materials) Sect. 21/22 | - |
| IP Rating | IP65 | Minimum |

---

## 7. Reliability & Maintainability

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Design Life | 60,000 | FH | Flight hours |
| MTBF | 50,000 | FH | Predicted |
| Bearing Life | 30,000 | FH | Scheduled replacement |
| TBO | 15,000 | FH | Time between overhaul |

---

## 8. Interfaces

### 8.1 Mechanical Interfaces

- **Shaft Coupling**: Splined coupling to fan hub (61-20-02)
- **Mounting**: Flange mount to nacelle frame (61-50)
- **Cooling Jacket**: Integrated liquid cooling ports (61-20-05)

### 8.2 Electrical Interfaces

- **Power Input**: 3-phase AC from PCU (61-20-04)
- **Resolver/Encoder**: Position feedback to PCU
- **Temperature Sensors**: 6× PT1000 RTDs (61-20-06)

---

## 9. Applicable Standards

- [CS-E](https://www.easa.europa.eu/document-library/certification-specifications/cs-e-amendment-6) — Engine certification
- [DO-160G](https://www.rtca.org/content/standards-guidance-materials) — Environmental qualification
- IEC 60034 — Rotating electrical machines
- IEEE 112 — Efficiency test methods

---

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending engineering review
