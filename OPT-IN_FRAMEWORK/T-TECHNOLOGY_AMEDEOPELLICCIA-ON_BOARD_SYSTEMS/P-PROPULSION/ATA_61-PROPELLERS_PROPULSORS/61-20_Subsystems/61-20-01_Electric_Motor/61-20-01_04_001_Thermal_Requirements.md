# 61-20-01_04_001 — Thermal Requirements

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_04_001_Thermal_Requirements   |
| **Subsystem**      | 61-20-01_Electric_Motor                |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. Overview

This document specifies the thermal requirements for the Electric Motor (61-20-01) and its interface with the Cooling Loop (61-20-05) subsystem.

---

## 2. Heat Generation

### 2.1 Loss Sources

| Loss Type | Nominal (kW) | Peak (kW) | % of Total |
|-----------|--------------|-----------|------------|
| Copper Losses (I²R) | 85 | 130 | 60% |
| Iron Losses (Core) | 35 | 38 | 25% |
| Mechanical Losses | 12 | 14 | 9% |
| Stray Losses | 8 | 10 | 6% |
| **Total Heat Rejection** | **140** | **192** | 100% |

### 2.2 Heat Distribution

| Component | Heat Load (kW) | Cooling Method |
|-----------|----------------|----------------|
| Stator Windings | 95 | Jacket cooling |
| Stator Core | 30 | Jacket cooling |
| Rotor | 8 | Air gap / conduction |
| Drive-End Bearing | 3.5 | Oil lubrication |
| Non-Drive-End Bearing | 3.0 | Oil lubrication |
| Resolver/Sensors | 0.5 | Conduction |

---

## 3. Temperature Limits

### 3.1 Component Temperature Limits

| Component | Max Operating (°C) | Max Transient (°C) | Duration |
|-----------|-------------------|-------------------|----------|
| Winding Hotspot | 160 | 175 | 60 s |
| Winding Average | 145 | 160 | 60 s |
| Stator Core | 140 | 155 | 60 s |
| Rotor Magnets | 150 | 165 | 30 s |
| Magnet Demagnetization | 180 | - | Never |
| DE Bearing | 120 | 135 | 30 s |
| NDE Bearing | 120 | 135 | 30 s |
| Housing Surface | 80 | 95 | - |

### 3.2 Ambient Conditions

| Condition | Value |
|-----------|-------|
| Ground Hot Day | +55°C |
| Cruise Altitude | -57°C |
| Max Altitude | FL450 |
| Nacelle Internal (max) | +85°C |

---

## 4. Cooling Requirements

### 4.1 Liquid Cooling Circuit

| Parameter | Requirement |
|-----------|-------------|
| Coolant Type | 50/50 ethylene glycol-water |
| Inlet Temperature (max) | 40°C |
| Inlet Temperature (min) | -20°C |
| Outlet Temperature (max) | 75°C |
| Flow Rate (nominal) | 60 L/min |
| Flow Rate (min) | 45 L/min |
| Pressure Drop (max) | 1.5 bar |
| System Pressure (nominal) | 3.0 bar |
| System Pressure (max) | 5.0 bar |

### 4.2 Heat Exchanger Requirements

| Parameter | Value |
|-----------|-------|
| Heat Rejection Capacity | ≥ 200 kW |
| Approach Temperature | ≤ 15°C |
| Effectiveness | ≥ 0.85 |

---

## 5. Thermal Protection

### 5.1 Temperature Monitoring

| Sensor | Location | Trip Level | Action |
|--------|----------|------------|--------|
| T1 | Winding U | 155°C | Derate to 50% |
| T2 | Winding V | 155°C | Derate to 50% |
| T3 | Winding W | 155°C | Derate to 50% |
| T4 | DE Bearing | 115°C | Warning |
| T5 | NDE Bearing | 115°C | Warning |
| T6 | Coolant Out | 70°C | Derate to 75% |

### 5.2 Shutdown Thresholds

| Condition | Threshold | Response Time |
|-----------|-----------|---------------|
| Winding Over-temperature | 170°C | < 1 s |
| Bearing Over-temperature | 130°C | < 1 s |
| Coolant Loss | Flow < 30 L/min | < 5 s |
| Coolant Over-temperature | 80°C | < 1 s |

---

## 6. Thermal Transients

### 6.1 Startup (Cold Soak)

| Phase | Duration | Notes |
|-------|----------|-------|
| Pre-heat | 5 min | Coolant circulation only |
| Idle | 2 min | 10% power, warm bearings |
| Ready | - | All temps > 0°C |

### 6.2 Hot Shutdown

| Requirement | Value |
|-------------|-------|
| Coolant Rundown | 3 min minimum |
| Max ΔT/dt (cooldown) | 10°C/min |
| Soak-back Protection | Active for 10 min |

---

## 7. Thermal Analysis Requirements

### 7.1 Analysis Cases

| Case | Ambient | Altitude | Power | Duration |
|------|---------|----------|-------|----------|
| Ground Hot | +55°C | SL | 100% | Continuous |
| Ground Cold | -40°C | SL | 100% | 30 min |
| Cruise | -57°C | FL410 | 85% | 8 hr |
| Emergency Climb | +20°C | FL250 | 120% | 30 s |
| Windmill | -57°C | FL410 | 0% | 30 min |

### 7.2 Margin Requirements

| Margin Type | Value |
|-------------|-------|
| Temperature Margin | ≥ 15°C to limit |
| Cooling Capacity Margin | ≥ 20% |
| Flow Rate Margin | ≥ 25% |

---

## 8. Interface to Cooling Loop

See `61-20-01_04_002_Cooling_Interface.yaml` for detailed interface definition.

---

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending engineering review
