# 61-20-01_03_001 — Electrical Interface Specification

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_03_001_Electrical_Interface   |
| **Subsystem**      | 61-20-01_Electric_Motor                |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. Overview

This document defines the electrical interfaces between the Electric Motor (61-20-01) and its connected systems, primarily the Propulsor Control Unit (61-20-04) and Health Sensing system (61-20-06).

---

## 2. Power Interface

### 2.1 Motor Power Cables (3-Phase AC)

| Parameter | Specification |
|-----------|---------------|
| Connector Type | MIL-DTL-38999 Series III, Size 25 |
| Number of Contacts | 3 power + 1 ground |
| Current Rating | 2,500 A per phase (continuous) |
| Voltage Rating | 1,000 V AC |
| Cable Type | Aircraft-grade ETFE insulated |
| Cable Gauge | 2 × 4/0 AWG per phase (parallel) |
| Cable Length | 2.5 m (max) |
| Shielding | Overall braid, 95% coverage |

### 2.2 Power Interface Pin Assignment

| Pin | Signal | Direction | Notes |
|-----|--------|-----------|-------|
| A | Phase U | PCU → Motor | Power |
| B | Phase V | PCU → Motor | Power |
| C | Phase W | PCU → Motor | Power |
| D | Ground | - | Chassis ground |

---

## 3. Position Feedback Interface

### 3.1 Resolver Interface

| Parameter | Specification |
|-----------|---------------|
| Type | Brushless resolver |
| Pole Pairs | 8 (matching motor) |
| Excitation Frequency | 10 kHz |
| Excitation Voltage | 7 V RMS |
| Output Voltage | 2.5 V RMS (nominal) |
| Accuracy | ±2 arcmin (electrical) |
| Operating Temperature | -55°C to +175°C |

### 3.2 Resolver Connector

| Parameter | Specification |
|-----------|---------------|
| Connector Type | MIL-DTL-38999 Series III, Size 11 |
| Number of Contacts | 6 |
| Cable Type | Shielded twisted pairs |
| Cable Length | 3.0 m (max) |

### 3.3 Resolver Pin Assignment

| Pin | Signal | Direction | Notes |
|-----|--------|-----------|-------|
| 1 | REF+ | PCU → Resolver | Excitation + |
| 2 | REF- | PCU → Resolver | Excitation - |
| 3 | SIN+ | Resolver → PCU | Sine output + |
| 4 | SIN- | Resolver → PCU | Sine output - |
| 5 | COS+ | Resolver → PCU | Cosine output + |
| 6 | COS- | Resolver → PCU | Cosine output - |

---

## 4. Temperature Sensor Interface

### 4.1 RTD Sensors

| Parameter | Specification |
|-----------|---------------|
| Sensor Type | PT1000 Class A |
| Number of Sensors | 6 |
| Measurement Range | -50°C to +200°C |
| Accuracy | ±0.15°C at 0°C |
| Connection | 4-wire |
| Locations | 3× stator windings, 2× bearings, 1× coolant |

### 4.2 Temperature Sensor Connector

| Parameter | Specification |
|-----------|---------------|
| Connector Type | MIL-DTL-38999 Series III, Size 15 |
| Number of Contacts | 24 (4 per sensor) |
| Cable Type | Shielded, PTFE insulated |
| Cable Length | 3.0 m (max) |

### 4.3 Temperature Sensor Pin Assignment

| Pin Range | Sensor | Signals |
|-----------|--------|---------|
| 1-4 | Winding U | I+, I-, V+, V- |
| 5-8 | Winding V | I+, I-, V+, V- |
| 9-12 | Winding W | I+, I-, V+, V- |
| 13-16 | DE Bearing | I+, I-, V+, V- |
| 17-20 | NDE Bearing | I+, I-, V+, V- |
| 21-24 | Coolant | I+, I-, V+, V- |

---

## 5. Vibration Sensor Interface

### 5.1 Accelerometer Specifications

| Parameter | Specification |
|-----------|---------------|
| Sensor Type | IEPE accelerometer |
| Number of Sensors | 3 (X, Y, Z axes) |
| Sensitivity | 100 mV/g |
| Frequency Range | 2 Hz – 20 kHz |
| Measurement Range | ±50 g |
| Bias Voltage | 8–12 V DC |
| Bias Current | 2–10 mA |

### 5.2 Vibration Sensor Connector

| Parameter | Specification |
|-----------|---------------|
| Connector Type | MIL-DTL-38999 Series III, Size 9 |
| Number of Contacts | 6 |
| Cable Type | Low-noise coaxial |

---

## 6. Grounding Requirements

| Requirement | Specification |
|-------------|---------------|
| Chassis Ground | ≤ 2.5 mΩ to airframe ground |
| EMI Ground | 360° backshell bonding |
| Shield Termination | Both ends, via backshell |
| Bonding Jumper | 10 AWG minimum |

---

## 7. EMC Requirements

| Parameter | Specification |
|-----------|---------------|
| Conducted Emissions | [DO-160G](https://www.rtca.org/content/standards-guidance-materials) Section 21, Cat B |
| Radiated Emissions | [DO-160G](https://www.rtca.org/content/standards-guidance-materials) Section 21, Cat M |
| Conducted Susceptibility | [DO-160G](https://www.rtca.org/content/standards-guidance-materials) Section 22 |
| Radiated Susceptibility | [DO-160G](https://www.rtca.org/content/standards-guidance-materials) Section 20, Cat T |
| Lightning | [DO-160G](https://www.rtca.org/content/standards-guidance-materials) Section 22, Level 3 |
| HIRF | [DO-160G](https://www.rtca.org/content/standards-guidance-materials) Section 20, Cat YY |

---

## 8. Interface Diagram Reference

See `61-20-01_03_002_HarnessDiagram.svg` for the complete harness routing and connector locations.

---

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending engineering review
