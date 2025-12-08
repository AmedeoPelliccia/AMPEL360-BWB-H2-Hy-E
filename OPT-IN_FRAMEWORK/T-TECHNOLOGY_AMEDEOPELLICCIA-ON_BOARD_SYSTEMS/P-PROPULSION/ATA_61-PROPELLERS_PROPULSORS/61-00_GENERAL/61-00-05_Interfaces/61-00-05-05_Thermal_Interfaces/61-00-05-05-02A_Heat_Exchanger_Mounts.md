# 61-00-05-05-02A - Heat Exchanger Mounts Interface

**Document ID:** 61-00-05-05-02A  
**Title:** Heat Exchanger Mounts Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the structural mounting interface for propulsor heat exchangers (if installed locally) or coolant routing attachments to the nacelle structure.

---

## 2. Scope

This specification covers:
- Heat exchanger mounting brackets
- Vibration isolation provisions
- Thermal expansion accommodation
- Access for maintenance
- Load transfer to structure

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements |
| 61-00-05-01-02A | Mounting Flanges | Related structural interface |
| [ASME BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-2-bpvc-section-viii-rules-construction-pressure-vessels-division-2-alternative-rules) | Pressure Vessel Code | Heat exchanger design |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Mounting Bracket Material | Aluminum alloy 7075-T651 | — | — | High strength |
| Number of Mounting Points | 4 | — | — | Per heat exchanger |
| Bolt Size | M10×1.5 | — | — | Grade 12.9 |
| Bolt Torque | 60 | ±5 | Nm | — |
| Vibration Isolator Type | Elastomeric bushing | — | — | — |
| Isolator Stiffness | 5×10⁵ | ±20% | N/m | — |

### 4.2 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| HXM-61-001 | Maximum static load | 500 N per mount | Test |
| HXM-61-002 | Thermal expansion accommodation | ±3 mm | Design feature |
| HXM-61-003 | Vibration isolation | >10 dB at >100 Hz | Test |
| HXM-61-004 | Mount fatigue life | >60,000 flight cycles | Analysis, Test |

---

## 5. Interface Control

### 5.1 Mounting Configuration

- 4-point mount, symmetrical
- Vibration isolators at each mount point
- Slotted holes for thermal expansion
- Tool-free access for removal

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| HXM-T-001 | Static load test | 750 N (1.5× limit) per mount, no failure | Load test |
| HXM-T-002 | Vibration isolation | >10 dB isolation | Shaker test |
| HXM-T-003 | Thermal expansion | ±3 mm without binding | Thermal cycle test |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 54](../../../../S-STRUCTURES/ATA_54-NACELLES_PYLONS/README.md) — Nacelles and Pylons

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-05-01A_Cooling_System_Connections](61-00-05-05-01A_Cooling_System_Connections.md) · [Next: 61-00-05-05-03A_Thermal_Insulation_Boundaries](61-00-05-05-03A_Thermal_Insulation_Boundaries.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Thermal Interfaces  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
