# Q100-61-INST-DEF-PYLON-TO-AIRFRAME — Load Paths

## 1. Overview

This document describes the load paths for the pylon-to-airframe attachment, detailing how propulsive, inertial, and aerodynamic loads are transferred from the propulsion system to the BWB airframe structure.

## 2. Load Path Diagram

```
                    ┌─────────────────────────┐
                    │   PROPULSOR UNIT        │
                    │   (Thrust, Inertia)     │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │   PROPULSOR-PYLON       │
                    │   MOUNTS                │
                    │   (Forward, Aft, Links) │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │   PYLON STRUCTURE       │
                    │   (Box beam)            │
                    └───────────┬─────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
    ┌────▼────┐           ┌─────▼─────┐          ┌────▼────┐
    │ UPPER   │           │  SHEAR    │          │ LOWER   │
    │ ATTACH  │           │  PINS     │          │ ATTACH  │
    │ (2x)    │           │  (4x)     │          │ (2x)    │
    └────┬────┘           └─────┬─────┘          └────┬────┘
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │   BWB AIRFRAME          │
                    │   (Wing structure)      │
                    └─────────────────────────┘
```

## 3. Primary Load Paths

### 3.1 Thrust Load Path

| Load | Primary Path | Backup Path |
|------|--------------|-------------|
| Forward Thrust | Lower attachments → Airframe rib | Upper attachments (10% backup) |
| Reverse Thrust | Lower attachments → Airframe rib | Upper attachments (10% backup) |

**Description**: Thrust loads are reacted primarily through the lower attachment clevis fittings, which transfer load directly into the airframe rear spar and ribs. The upper attachments provide a backup path in case of lower attachment degradation.

### 3.2 Vertical Load Path

| Load | Upper Attachment | Lower Attachment |
|------|------------------|------------------|
| Positive g-load | 40% | 60% |
| Negative g-load | 55% | 45% |
| Ground loads | 35% | 65% |

**Description**: Vertical loads (weight, inertia, lift) are distributed between upper and lower attachments based on moment arm geometry. The lower attachments carry more load due to proximity to the propulsor CG.

### 3.3 Lateral Load Path

| Load | Shear Pins | Upper Fitting | Lower Fitting |
|------|------------|---------------|---------------|
| Side gust | 70% | 20% | 10% |
| Crosswind | 60% | 25% | 15% |
| Gyroscopic | 50% | 30% | 20% |

**Description**: Lateral loads are primarily reacted by the close-tolerance shear pins, which transfer side loads directly into the airframe without relying on friction at bolt interfaces.

### 3.4 Torque Load Path

| Load | Upper-Lower Couple | Shear Pins |
|------|-------------------|------------|
| Propeller torque | 80% | 20% |
| Gyroscopic moment | 70% | 30% |

**Description**: Torque and moment loads are reacted through a force couple between upper and lower attachments, with shear pins providing additional constraint.

## 4. Fail-Safe Analysis

### 4.1 Single Load Path Failure

| Failed Element | Remaining Capacity | Safe Flight Time |
|----------------|-------------------|------------------|
| One upper attachment | 120% limit load | Unlimited (degraded) |
| One lower attachment | 115% limit load | Unlimited (degraded) |
| One shear pin | 100% limit load | Unlimited |
| Two shear pins | 85% limit load | Return to base |

### 4.2 Crack Propagation

| Location | Detectable Size | Critical Size | Growth Rate |
|----------|-----------------|---------------|-------------|
| Upper fitting | 2.5 mm | 12 mm | 0.001 mm/FH |
| Lower fitting | 2.5 mm | 15 mm | 0.0008 mm/FH |
| Shear pin hole | 1.5 mm | 6 mm | 0.002 mm/FH |

**Inspection Interval**: Based on crack growth analysis, inspection interval is 3,000 FH after damage detection.

## 5. Load Cases Summary

| ID | Case | Thrust kN | Vertical g | Lateral g | Torque kNm |
|----|------|-----------|------------|-----------|------------|
| LC1 | Cruise | 80 | 1.0 | 0 | 45 |
| LC2 | Max Climb | 150 | 1.2 | 0 | 85 |
| LC3 | Maneuver | 120 | 2.5 | 0.3 | 70 |
| LC4 | Gust | 90 | 1.0 | 0.5 | 50 |
| LC5 | Landing | 0 | 2.0 | 0.2 | 0 |
| LC6 | Ground | 0 | 1.0 | 0 | 0 |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
