# ICD-53-25: Fuselage to Equipment Interface Control Document

## 1. Purpose

This Interface Control Document (ICD) defines the structural interfaces between **ATA 53 – Fuselage** and **ATA 25 – Equipment/Furnishings** for the AMPEL360 BWB aircraft.

---

## 2. Scope

### 2.1 In Scope

- Seat track attachments to floor structure
- Monument (galley, lavatory) attachment interfaces
- Overhead bin support structure
- Sidewall panel attachments
- Cargo restraint system interfaces

### 2.2 Out of Scope

- Equipment internal design (covered by ATA 25)
- Systems integration (covered by ATA 21, 24)
- Electrical interfaces (covered by ATA 24)

---

## 3. Interface Definitions

### 3.1 Seat Track Interfaces

| Interface ID | Location | Zone | Load Type | Responsible CI |
|--------------|----------|------|-----------|----------------|
| IF-53-25-001 | Floor beam attachments | 200/300 | Vertical + Inertia | CI-53-200-FLR-BEAM-P-L |
| IF-53-25-002 | Seat track rail | 200/300 | Shear | CI-53-200-FLR-BEAM-S-L |
| IF-53-25-003 | Emergency row seats | 300 | Inertia + Emergency | CI-53-300-FLR-BEAM-P |

### 3.2 Monument Interfaces

| Interface ID | Location | Zone | Load Type | Responsible CI |
|--------------|----------|------|-----------|----------------|
| IF-53-25-010 | Forward galley | 200 | Static + Dynamic | CI-53-200 |
| IF-53-25-011 | Aft galley | 500 | Static + Dynamic | CI-53-500-GALLEY |
| IF-53-25-012 | Lavatory attachments | 200/500 | Static | CI-53-200, CI-53-500-LAV |

---

## 4. Load Requirements

### 4.1 Design Load Cases

```yaml
load_cases:
  vertical_static:
    description: "Cabin floor static loads"
    value: "TBD psf"
    reference: "RQ-53-00-02-001"
  
  emergency_landing:
    description: "16g forward, 9g down emergency landing"
    forward_g: 16
    downward_g: 9
    reference: "[CS-25.561](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)"
```

---

## 5. Geometric Interfaces

### 5.1 Floor Grid Pattern

- Primary beam spacing: 508 mm (20 inches) typical
- Seat track pitch: Per ATA 25 specification
- Datum reference: Aircraft STA and WL coordinates

---

## 6. Verification Method

| Requirement | Verification Method | Responsible |
|-------------|---------------------|-------------|
| Static loads | Analysis + Test | ATA 53 + ATA 25 |
| Emergency loads | Analysis + Component Test | ATA 53 |
| Fatigue | Analysis | ATA 53 |

---

## 7. Document Control

- **Document ID**: ICD-53-25
- **Version**: 1.0
- **Date**: 2025-11-24
- **Owner**: ATA 53/25 Interface Manager
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-24_.

---
