# Q100-61-STD-NAMING-CONVENTION — Drawing Naming Convention Standard

## Purpose

This document defines the naming convention for all ATA 61 drawings in the AMPEL360-BWB-H2-Hy-E project (Q100 program).

## Scope

Applies to all drawing files, drawing sets, templates, and symbol libraries under ATA 61.

---

## 1. Primary Naming Pattern

### 1.1 Standard Format

```
Q100-61-[TYPE]-[SYSTEM]-[COMPONENT].[ext]
```

### 1.2 Components

| Element | Description | Examples |
|---------|-------------|----------|
| `Q100` | Program identifier | Q100 (AMPEL360 program) |
| `61` | ATA chapter | 61 (Propellers/Propulsors) |
| `TYPE` | Drawing type code | DRW, SCH, ICD, INST, DIAG |
| `SYSTEM` | System/subsystem code | OFP, EMD, PV, MNT, FPS |
| `COMPONENT` | Component identifier | BLADE, HUB, MOTOR, etc. |
| `ext` | File extension | svg, yaml, md |

---

## 2. Type Codes

| Code | Full Name | Description |
|------|-----------|-------------|
| DRW | Engineering Drawing | Detailed part/assembly drawings |
| SCH | Schematic | Electrical, hydraulic, pneumatic schematics |
| ICD | Interface Control Drawing | Interface definition documents |
| INST | Installation Drawing | Installation and routing drawings |
| DIAG | Diagram | Block diagrams, flow diagrams |
| SET | Drawing Set | Collection of related drawings |
| STD | Standard | Standard/procedure documents |
| TPL | Template | Drawing templates |
| SYM | Symbol Library | Reusable symbol collections |
| TYPE | Type Definition | Drawing type definitions |

---

## 3. System Codes

| Code | System Name | OPT-IN Buckets |
|------|-------------|----------------|
| OFP | Open Fan Propulsor | 61-20_Subsystems, 61-50_Structures, 61-70_Propulsion |
| EMD | Electric Motor Drive | 61-40_Software, 61-80_Energy |
| PV | Propeller Variants | 61-20_Subsystems |
| MNT | Mounting System | 61-50_Structures |
| FPS | Full Propulsor System | 61-00_GENERAL, 61-70_Propulsion, 61-90_Tables_Schemas_Diagrams |

---

## 4. Component Codes

### 4.1 OFP (Open Fan Propulsor)

| Code | Component |
|------|-----------|
| BLADE | Fan blades |
| HUB | Hub assembly |
| NAC | Nacelle structure |
| PITCH | Pitch control mechanism |
| DEICE | De-icing system |

### 4.2 EMD (Electric Motor Drive)

| Code | Component |
|------|-----------|
| MOTOR | Electric motor |
| CTRL | Motor controller |
| PWR | Power electronics |
| COOL | Cooling system |
| SENS | Sensors |

### 4.3 MNT (Mounting System)

| Code | Component |
|------|-----------|
| MOUNT | Engine mounts |
| PYLON | Pylon structure |
| VIB | Vibration isolation |
| ATT | Structural attachments |
| FAIR | Fairings |

### 4.4 FPS (Full Propulsor System)

| Code | Component |
|------|-----------|
| ASSY | Assembly drawings |
| SYS | System schematics |
| INT | Interface control |
| INST | Installation |

---

## 5. Sequence Numbers

When multiple drawings exist for the same component:

```
Q100-61-DRW-OFP-BLADE-001.svg
Q100-61-DRW-OFP-BLADE-002.svg
Q100-61-DRW-OFP-BLADE-003.svg
```

- Use 3-digit sequence numbers (001-999)
- Start at 001 for each component
- Do not reuse numbers after deletion

---

## 6. Special Prefixes

### 6.1 Drawing Sets

```
Q100-61-SET-[SYSTEM]/
```

Examples:
- `Q100-61-SET-OFP/`
- `Q100-61-SET-EMD/`

### 6.2 Templates

```
Q100-61-TPL-[SIZE]-[ORIENTATION].svg
```

Examples:
- `Q100-61-TPL-A0-LANDSCAPE.svg`
- `Q100-61-TPL-A4-PORTRAIT.svg`

### 6.3 Symbol Libraries

```
Q100-61-SYM-[CATEGORY].svg
```

Examples:
- `Q100-61-SYM-ELECTRICAL.svg`
- `Q100-61-SYM-PROPULSION.svg`

---

## 7. File Extensions

| Extension | Use |
|-----------|-----|
| `.svg` | Vector drawings (released) |
| `.yaml` | Set definitions, indexes |
| `.md` | Documentation, lists |
| `.dxf` | CAD interchange |

---

## 8. Examples

### Complete Drawing Names

```
Q100-61-DRW-OFP-BLADE-001.svg        # Fan blade drawing #1
Q100-61-SCH-EMD-PWR-001.svg          # Power schematic
Q100-61-ICD-FPS-INT-001.svg          # System interface
Q100-61-INST-MNT-PYLON-001.svg       # Pylon installation
Q100-61-DIAG-FPS-SYS-001.svg         # System diagram
```

### Set and Support Files

```
Q100-61-SET-MASTER-INDEX.yaml        # Master index
Q100-61-STD-NAMING-CONVENTION.md     # This document
Q100-61-TPL-A3-LANDSCAPE.svg         # A3 template
Q100-61-SYM-GDT.svg                  # GD&T symbols
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
