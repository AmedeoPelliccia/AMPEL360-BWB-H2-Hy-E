# Q100-61-PRT-STD-NAMING — Part Naming Convention

## Purpose

This document defines the naming convention for parts used in the Q100 program propulsion system (ATA 61 - Propellers/Propulsors).

## Naming Pattern

```
Q100-61-PRT-[SYSTEM]-[COMPONENT]
```

### Components

| Element | Description | Example |
|---------|-------------|---------|
| Q100 | Program identifier | Q100 |
| 61 | ATA Chapter | 61 |
| PRT | Part designator | PRT |
| SYSTEM | System code | FAN, MOTOR |
| COMPONENT | Component name | BLADE, SHAFT |

## System Codes

| Code | Description | Examples |
|------|-------------|----------|
| FAN | Fan components | BLADE, HUB, SPINNER |
| NACELLE | Nacelle components | OUTER-BARREL, INLET-LIP |
| GEARBOX | Gearbox components | SUN-GEAR, CARRIER |
| MOTOR | Motor components | STATOR-CORE, SHAFT |
| CTRL | Controller components | ENCLOSURE, HEATSINK |
| PROP | Propeller components | BLADE-FWD, PITCH-LINK |
| MNT | Mounting components | FWD-MOUNT, THRUST-LINK |
| STD | Standard parts | FASTENER, BEARING |

## Component Naming Rules

1. **Use UPPERCASE** for all identifiers
2. **Use hyphens** (-) to separate words within component names
3. **Keep names concise** but descriptive (max 25 characters)
4. **Avoid abbreviations** unless universally understood
5. **Use directional modifiers** when applicable (FWD, AFT, DE, NDE)

### Directional Modifiers

| Modifier | Meaning |
|----------|---------|
| FWD | Forward |
| AFT | Aft |
| DE | Drive End |
| NDE | Non-Drive End |
| INNER | Inner/internal |
| OUTER | Outer/external |

## Examples

| Part ID | Description |
|---------|-------------|
| Q100-61-PRT-FAN-BLADE | Fan blade |
| Q100-61-PRT-MOTOR-END-BELL-DE | Motor end bell (drive end) |
| Q100-61-PRT-NACELLE-OUTER-BARREL | Nacelle outer barrel |
| Q100-61-PRT-PROP-BLADE-FWD | Forward propeller blade |
| Q100-61-PRT-MNT-VIBRATION-DAMPER | Vibration isolation damper |

## CAD File Naming

CAD files use the part ID as the filename:

```
[PART_ID].[extension]
```

### Examples

- `Q100-61-PRT-FAN-BLADE.CATPart`
- `Q100-61-PRT-MOTOR-SHAFT.sldprt`
- `Q100-61-PRT-FAN-HUB.step`

## Standard Parts

Standard parts use a different pattern:

```
Q100-61-STD-[CATEGORY]-INDEX
```

Categories: FASTENER, BEARING, SEAL, CONNECTOR

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
