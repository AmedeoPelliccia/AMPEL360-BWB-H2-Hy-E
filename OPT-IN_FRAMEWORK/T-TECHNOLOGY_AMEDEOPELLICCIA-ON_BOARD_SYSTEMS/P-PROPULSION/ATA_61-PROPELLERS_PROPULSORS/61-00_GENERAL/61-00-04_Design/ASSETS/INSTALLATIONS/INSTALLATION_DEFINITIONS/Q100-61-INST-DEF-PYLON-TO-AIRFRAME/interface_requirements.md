# Q100-61-INST-DEF-PYLON-TO-AIRFRAME — Interface Requirements

## 1. Structural Interface Requirements

### 1.1 Upper Attachment

| Requirement ID | Description | Value | Verification |
|----------------|-------------|-------|--------------|
| REQ-61-STR-001 | Ultimate load capacity | ≥500 kN per fitting | Analysis + Test |
| REQ-61-STR-002 | Fatigue life | ≥60,000 flight cycles | Analysis + Test |
| REQ-61-STR-003 | Fitting alignment tolerance | ±0.25 mm | Inspection |
| REQ-61-STR-004 | Bolt torque | 180 Nm ±5% | Inspection |

### 1.2 Lower Attachment

| Requirement ID | Description | Value | Verification |
|----------------|-------------|-------|--------------|
| REQ-61-STR-005 | Ultimate load capacity | ≥600 kN per fitting | Analysis + Test |
| REQ-61-STR-006 | Fatigue life | ≥60,000 flight cycles | Analysis + Test |
| REQ-61-STR-007 | Fitting alignment tolerance | ±0.20 mm | Inspection |
| REQ-61-STR-008 | Bolt torque | 220 Nm ±5% | Inspection |

### 1.3 Shear Pins

| Requirement ID | Description | Value | Verification |
|----------------|-------------|-------|--------------|
| REQ-61-STR-009 | Shear capacity per pin | ≥150 kN | Analysis + Test |
| REQ-61-STR-010 | Installation interference | 0.01-0.03 mm | Inspection |
| REQ-61-STR-011 | Corrosion protection | Passivated per QQ-P-35 | Inspection |

### 1.4 Fail-Safe Design

| Requirement ID | Description | Value | Verification |
|----------------|-------------|-------|--------------|
| REQ-61-STR-012 | Single load path failure | Structure shall sustain limit load | Analysis |
| REQ-61-STR-013 | Inspection interval | 3,000 FH after damage | Analysis |
| REQ-61-STR-014 | Detectable crack size | ≥2.5 mm | Test |

## 2. Load Path Requirements

### 2.1 Vertical Loads

| Load Case | Upper Fitting | Lower Fitting | Verification |
|-----------|---------------|---------------|--------------|
| 1g steady | 40% | 60% | Analysis |
| 2.5g maneuver | 40% | 60% | Analysis |
| -1.0g maneuver | 55% | 45% | Analysis |

### 2.2 Thrust Loads

| Load Case | Primary Path | Backup Path | Verification |
|-----------|--------------|-------------|--------------|
| Max thrust | Lower attachment (100%) | N/A | Analysis |
| Reverse thrust | Lower attachment (100%) | N/A | Analysis |
| Asymmetric thrust | Lower + Shear pins | Upper backup | Analysis |

### 2.3 Lateral Loads

| Load Case | Shear Pins | Upper Fitting | Verification |
|-----------|------------|---------------|--------------|
| Max sideslip | 70% | 30% | Analysis |
| Crosswind landing | 60% | 40% | Analysis |

## 3. Routing Requirements

### 3.1 Electrical Conduits

| Requirement ID | Description | Value | Verification |
|----------------|-------------|-------|--------------|
| REQ-61-RTE-001 | Main power conduit ID | ≥50 mm | Inspection |
| REQ-61-RTE-002 | EMI shielding effectiveness | ≥60 dB | Test |
| REQ-61-RTE-003 | Firewall penetration rating | FAR 25.867 | Analysis + Test |

### 3.2 Fluid Penetrations

| Requirement ID | Description | Value | Verification |
|----------------|-------------|-------|--------------|
| REQ-61-RTE-004 | Coolant bulkhead fitting rating | 10 bar | Test |
| REQ-61-RTE-005 | Lube oil bulkhead fitting rating | 15 bar | Test |
| REQ-61-RTE-006 | Leak rate | Zero visible | Test |

## 4. Environmental Requirements

| Requirement ID | Description | Value | Verification |
|----------------|-------------|-------|--------------|
| REQ-61-ENV-010 | Temperature range | -55°C to +85°C | Analysis |
| REQ-61-ENV-011 | Corrosion protection | MIL-PRF-8625 Type III | Inspection |
| REQ-61-ENV-012 | Lightning protection | Zone 2A | Analysis + Test |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
