# 53-10-02-001 — ANCHORS Cruise Monitoring

| Field | Value |
|-------|-------|
| **Document ID** | 53-10-02-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | OPERATIONAL |

---

## 1. Purpose

This procedure defines in-flight monitoring parameters and normal operations for ANCHORS systems during cruise.

## 2. Scope

Applicable to all flight phases, with emphasis on cruise operations.

## 3. Monitoring Parameters

| Parameter | Normal Range | Caution | Warning | Action |
|-----------|--------------|---------|---------|--------|
| Battery SoC | 30–90% | <20% or >95% | <10% or >98% | Adjust load |
| Battery Temp | 20–40°C | 40–50°C | >50°C | Reduce load |
| CO₂ Capture Rate | 5–10 kg/hr | <3 kg/hr | 0 kg/hr | Check system |
| Cabin CO₂ | 400–1000 ppm | 1000–1500 ppm | >1500 ppm | ECS priority |
| Cartridge Fill | 10–90% | >90% | >95% | Plan swap |
| ThermalBus Temp | 30–50°C | 50–60°C | >60°C | Reduce loads |

## 4. Mode Selection

| Mode | Selection | Effect | Use Case |
|------|-----------|--------|----------|
| **AUTO** | Default | Full automatic operation | Normal ops |
| **ECO** | ANCHORS → ECO | Reduced power, max efficiency | Long haul |
| **MAX** | ANCHORS → MAX | Maximum capture/recovery | Short routes |
| **STBY** | ANCHORS → STBY | Minimal operation | MEL dispatch |

## 5. Flight Phase Operations

| Phase | ANCHORS Mode | CO₂ Capture | Battery | Harvesting |
|-------|--------------|-------------|---------|------------|
| **Pre-flight** | STANDBY | OFF | Charging | OFF |
| **Taxi-out** | GROUND | WARM-UP | Discharging | OFF |
| **Takeoff** | CLIMB_DESC | REDUCED | High discharge | OFF |
| **Climb** | CLIMB_DESC | RAMPING | Moderate | LOW |
| **Cruise** | CRUISE | FULL | Balanced | FULL |
| **Descent** | CLIMB_DESC | REDUCED | Regen | LOW |
| **Approach** | CLIMB_DESC | REDUCED | Moderate | OFF |
| **Landing** | GROUND | COOL-DOWN | Regen | OFF |
| **Taxi-in** | GROUND | OFF | Charging | OFF |

## 6. Related Documents

- [53-10-21-001_ANCHORS_System_Page.md](../53-10-21_Displays/53-10-21-001_ANCHORS_System_Page.md) — System page display
- [53-10-03_Abnormal_Procedures/](../53-10-03_Abnormal_Procedures/) — Abnormal handling

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---

*END OF DOCUMENT*
