# ICD-53-54: Fuselage to Nacelles/Pylons Interface Control Document

## 1. Purpose

This Interface Control Document (ICD) defines the structural interfaces between **ATA 53 – Fuselage** and **ATA 54 – Nacelles/Pylons** for the AMPEL360 BWB aircraft.

---

## 2. Scope

### 2.1 In Scope

- Engine mount attachment structure on fuselage/wing box
- Pylon-to-fuselage structural connections
- Thrust reaction structure
- Engine cowling support provisions

### 2.2 Out of Scope

- Nacelle/pylon internal design (covered by ATA 54)
- Engine mounting system (covered by ATA 71)
- Fuel system interfaces (covered by ATA 28)

---

## 3. Interface Definitions

### 3.1 Engine Mount Attachments

| Interface ID | Location | Zone | Load Type | Responsible CI |
|--------------|----------|------|-----------|----------------|
| IF-53-54-001 | Left engine forward mount | 400 | Thrust + Inertia | CI-53-400 |
| IF-53-54-002 | Left engine aft mount | 400 | Thrust + Inertia | CI-53-400 |
| IF-53-54-003 | Right engine forward mount | 400 | Thrust + Inertia | CI-53-400 |
| IF-53-54-004 | Right engine aft mount | 400 | Thrust + Inertia | CI-53-400 |

### 3.2 Pylon Attachments

| Interface ID | Location | Zone | Load Type | Responsible CI |
|--------------|----------|------|-----------|----------------|
| IF-53-54-010 | Left pylon primary attach | 400 | Multi-axis | CI-53-400-SPAR-REAR |
| IF-53-54-011 | Right pylon primary attach | 400 | Multi-axis | CI-53-400-SPAR-REAR |

---

## 4. Load Requirements

### 4.1 Design Load Cases

```yaml
load_cases:
  maximum_thrust:
    description: "Take-off and go-around thrust loads"
    reference: "[CS-25.361](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)"
  
  engine_out:
    description: "Engine failure yaw and roll loads"
    reference: "[CS-25.367](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)"
  
  blade_release:
    description: "Fan blade release loads"
    reference: "[CS-25.903](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)"
  
  mounting_fatigue:
    description: "Engine vibration and cyclic loads"
    reference: "[CS-25.571](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)"
```

---

## 5. Geometric Interfaces

### 5.1 Mount Geometry

- Engine thrust line: Per propulsion system definition
- Mount spacing: Per ATA 54 pylon design
- Fail-safe provisions: Redundant load paths per [CS-25.571](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)

---

## 6. Verification Method

| Requirement | Verification Method | Responsible |
|-------------|---------------------|-------------|
| Static loads | Analysis + Component Test | ATA 53 + ATA 54 |
| Fatigue | Analysis | ATA 53 |
| Fail-safe | Analysis + Full-scale Test | ATA 53 |
| Blade release | Analysis | ATA 53 |

---

## 7. Document Control

- **Document ID**: ICD-53-54
- **Version**: 1.0
- **Date**: 2025-11-24
- **Owner**: ATA 53/54 Interface Manager
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-24_.

---
