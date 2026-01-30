# Q100-61-INST-DEF-CONTROLLER-TO-NACELLE — Thermal Requirements

## 1. Overview

The motor controller generates significant heat during operation. This document specifies the thermal management requirements to ensure reliable operation across all flight conditions.

## 2. Heat Generation

### 2.1 Power Loss Budget

| Component | Loss at Max Power | Notes |
|-----------|-------------------|-------|
| IGBTs/MOSFETs | 4.0 kW | Switching + conduction |
| Gate drivers | 0.3 kW | Drive circuits |
| DC link capacitors | 0.2 kW | ESR losses |
| Control electronics | 0.5 kW | Logic, sensors |
| Bus bars/wiring | 0.5 kW | Resistive |
| Magnetics (if any) | 0.5 kW | Core + copper |
| **Total** | **6.0 kW** | Typical |
| **Peak (transient)** | **8.0 kW** | 30 second duration |

### 2.2 Heat Distribution

| Zone | Heat Load | Cooling Method |
|------|-----------|----------------|
| Power stage | 70% | Cold plate |
| Control board | 15% | Forced air |
| Connectors | 10% | Conduction |
| Enclosure | 5% | Radiation/convection |

## 3. Cooling System Requirements

### 3.1 Cold Plate Performance

| Parameter | Requirement | Target |
|-----------|-------------|--------|
| Thermal resistance | ≤0.05 °C/W | 0.03 °C/W |
| Contact area | ≥800 cm² | 1000 cm² |
| Interface material | ≥5 W/mK | 6 W/mK |
| Pressure uniformity | ≥90% | 95% |

### 3.2 Coolant Flow Requirements

| Parameter | Minimum | Nominal | Maximum |
|-----------|---------|---------|---------|
| Flow rate | 15 LPM | 20 LPM | 25 LPM |
| Inlet temperature | -20°C | 35°C | 45°C |
| Pressure drop | 0.1 bar | 0.3 bar | 0.5 bar |
| Coolant type | PG/Water 50/50 | | |

### 3.3 Temperature Limits

| Location | Warning | Limit | Shutdown |
|----------|---------|-------|----------|
| Junction (Tj) | 125°C | 140°C | 150°C |
| Case (Tc) | 85°C | 95°C | 100°C |
| Cold plate | 70°C | 80°C | 85°C |
| Ambient bay | 50°C | 55°C | 60°C |

## 4. Environmental Conditions

### 4.1 Operating Range

| Phase | Ambient Temp | Altitude | Duration |
|-------|--------------|----------|----------|
| Ground hot | +55°C | Sea level | Continuous |
| Ground cold | -40°C | Sea level | Continuous |
| Cruise | -40°C | 12,000 m | Continuous |
| Emergency descent | +35°C | 3,000 m | 30 min |

### 4.2 Transient Conditions

| Condition | Rate | Duration |
|-----------|------|----------|
| Rapid descent | +50°C/min | 10 min |
| Rapid climb | -30°C/min | 10 min |
| APU heat soak | +20°C above ambient | 30 min |

## 5. Thermal Interface

### 5.1 Interface Material Selection

| Property | Requirement |
|----------|-------------|
| Thermal conductivity | ≥5 W/mK |
| Thickness | 0.5-2.0 mm |
| Compression | 30-50% |
| Long-term stability | 10,000 cycles |
| Temperature rating | -55°C to +200°C |

### 5.2 Interface Installation

1. Clean cold plate surface (IPA wipe)
2. Apply interface material (no air gaps)
3. Install controller on rails
4. Tighten mounting to specified torque
5. Verify contact pressure (gap check)

## 6. Thermal Monitoring

### 6.1 Temperature Sensors

| Sensor | Location | Type | Function |
|--------|----------|------|----------|
| T1-T6 | IGBT modules | NTC | Junction monitoring |
| T7-T8 | Cold plate | PT1000 | Coolant effectiveness |
| T9 | Inlet coolant | PT1000 | Cooling system |
| T10 | Outlet coolant | PT1000 | Heat rejection calc |

### 6.2 Thermal Protection

| Protection | Trigger | Action |
|------------|---------|--------|
| Warning | Tj > 125°C | Crew alert, derating |
| Limit | Tj > 140°C | Power reduction 50% |
| Shutdown | Tj > 150°C | Controlled shutdown |
| Flow loss | Flow < 10 LPM | Power reduction 50% |

## 7. Verification

### 7.1 Test Requirements

| Test | Condition | Acceptance |
|------|-----------|------------|
| Thermal impedance | Full power, 1 hr | Rth ≤ 0.05 °C/W |
| Hot soak | +55°C ambient, idle | All temps within limits |
| Cold soak | -40°C ambient | Startup within 5 min |
| Altitude | 12,000 m simulated | No derating required |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
