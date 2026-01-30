# ICD-53-52: Fuselage to Doors Interface Control Document

## 1. Purpose

This Interface Control Document (ICD) defines the structural interfaces between **ATA 53 – Fuselage** and **ATA 52 – Doors** for the AMPEL360 BWB aircraft.

---

## 2. Scope

### 2.1 In Scope

- Passenger door cutout reinforcement
- Door hinge attachment structure
- Door latch receptacle provisions
- Emergency exit structure
- Cargo door interfaces

### 2.2 Out of Scope

- Door mechanism design (covered by ATA 52)
- Door seals and pressurization (covered by ATA 21/52)
- Door operation procedures

---

## 3. Interface Definitions

### 3.1 Passenger Door Interfaces

| Interface ID | Location | Zone | Load Type | Responsible CI |
|--------------|----------|------|-----------|----------------|
| IF-53-52-001 | Door 1L frame | 200 | Pressure + Inertia | CI-53-200-DOOR-1L-FR |
| IF-53-52-002 | Door 1R frame | 200 | Pressure + Inertia | CI-53-200-DOOR-1R-FR |
| IF-53-52-003 | Door 2L frame | 300 | Pressure + Inertia | CI-53-300-DOOR-2L-FR |
| IF-53-52-004 | Door 2R frame | 300 | Pressure + Inertia | CI-53-300 |

### 3.2 Emergency Exit Interfaces

| Interface ID | Location | Zone | Load Type | Responsible CI |
|--------------|----------|------|-----------|----------------|
| IF-53-52-010 | Overwing exit L | 300 | Pressure + Inertia | CI-53-300-EXIT-OW-L |
| IF-53-52-011 | Overwing exit R | 300 | Pressure + Inertia | CI-53-300 |

### 3.3 Cargo Door Interfaces

| Interface ID | Location | Zone | Load Type | Responsible CI |
|--------------|----------|------|-----------|----------------|
| IF-53-52-020 | Forward cargo door | 400 | Pressure + Ground handling | CI-53-400 |
| IF-53-52-021 | Aft cargo door | 500 | Pressure + Ground handling | CI-53-500 |

---

## 4. Load Requirements

### 4.1 Design Load Cases

```yaml
load_cases:
  cabin_pressure:
    description: "Maximum cabin differential pressure"
    value: "8.6 psi"
    reference: "[CS-25.365](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)"
  
  door_slam:
    description: "Door operation loads"
    reference: "[CS-25.783](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)"
  
  emergency_opening:
    description: "Emergency door opening loads"
    reference: "[CS-25.809](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)"
```

---

## 5. Geometric Interfaces

### 5.1 Door Cutout Geometry

- Door opening dimensions: Per ATA 52 specification
- Hinge line locations: Per door mechanism design
- Threshold requirements: Per [CS-25.810](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)

---

## 6. Verification Method

| Requirement | Verification Method | Responsible |
|-------------|---------------------|-------------|
| Pressure loads | Analysis + Test | ATA 53 |
| Fatigue | Analysis | ATA 53 |
| Door operation | Integration test | ATA 52 |
| Emergency exit | Certification test | ATA 52 |

---

## 7. Document Control

- **Document ID**: ICD-53-52
- **Version**: 1.0
- **Date**: 2025-11-24
- **Owner**: ATA 53/52 Interface Manager
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-24_.

---
