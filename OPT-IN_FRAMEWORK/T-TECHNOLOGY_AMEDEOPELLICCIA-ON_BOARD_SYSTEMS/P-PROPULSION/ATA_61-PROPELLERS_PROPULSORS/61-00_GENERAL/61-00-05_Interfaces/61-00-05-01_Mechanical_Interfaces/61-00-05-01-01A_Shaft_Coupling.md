# 61-00-05-01-01A - Shaft Coupling Interface

**Document ID:** 61-00-05-01-01A  
**Title:** Shaft Coupling Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the shaft coupling interface between the electric motor and ducted fan assembly in the AMPEL360 Q100 propulsion system. The coupling interface ensures reliable torque transmission while accommodating alignment tolerances and thermal expansion.

---

## 2. Scope

This specification covers:
- Mechanical coupling design and materials
- Torque transmission requirements
- Alignment tolerances
- Installation and removal procedures
- Inspection and maintenance requirements

### 2.1 Applicable Units
- All four Q100 propulsor units (Positions 1-4)
- Both primary and redundant motor configurations

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements document |
| 61-00-04-001 | Propulsor Design Specification | Design baseline |
| [SAE AS5282](https://www.sae.org/standards/content/as5282/) | Aerospace Flexible Couplings | Industry standard |
| [ISO 14691](https://www.iso.org/standard/54831.html) | Petroleum and Natural Gas Industries — Flexible Couplings | Reference standard |
| MIL-STD-167-1A | Mechanical Vibrations of Shipboard Equipment | Vibration requirements |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Coupling Type | Flexible disk pack | — | — | High-torque, low-backlash |
| Shaft Diameter (Motor Side) | 150 | ±0.05 | mm | Ground finish |
| Shaft Diameter (Fan Side) | 150 | ±0.05 | mm | Ground finish |
| Coupling Outer Diameter | 280 | ±1.0 | mm | — |
| Axial Length | 120 | ±2.0 | mm | — |
| Material (Disk Pack) | Titanium alloy (Ti-6Al-4V) | — | — | High strength-to-weight |
| Material (Hubs) | Aerospace aluminum (7075-T6) | — | — | Corrosion resistant |
| Mass | 8.5 | ±0.5 | kg | Per coupling assembly |

### 4.2 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| SHC-61-001 | Maximum continuous torque | 12,000 Nm | Test |
| SHC-61-002 | Peak transient torque (5 sec) | 18,000 Nm | Test |
| SHC-61-003 | Torsional stiffness | 8×10⁶ Nm/rad | Analysis, Test |
| SHC-61-004 | Angular misalignment capability | ±0.5° | Test |
| SHC-61-005 | Parallel offset capability | ±2.0 mm | Test |
| SHC-61-006 | Axial displacement capability | ±5.0 mm | Test |
| SHC-61-007 | Maximum operating speed | 3,600 rpm | Test |
| SHC-61-008 | Torsional damping | >2% critical | Analysis |
| SHC-61-009 | Backlash | <0.1° | Inspection |
| SHC-61-010 | Service life | >20,000 flight hours | Qualification |

### 4.3 Environmental Constraints

| Parameter | Operating Range | Survival Range | Unit | Notes |
|-----------|----------------|----------------|------|-------|
| Temperature | -40 to +120 | -55 to +150 | °C | Per DO-160G |
| Vibration | 5g RMS | 15g peak | g | Per MIL-STD-167 |
| Shock | 20g | 40g | g | 11 ms half-sine |
| Humidity | 0 to 95% | — | % RH | Non-condensing |
| Salt Fog Resistance | 500 hours | — | hours | Per ASTM B117 |

---

## 5. Interface Control

### 5.1 Dimensional Control

| Interface Point | Dimension | Tolerance | Inspection Method |
|-----------------|-----------|-----------|-------------------|
| Motor shaft bore (hub) | Ø150 H7 | +0.040/0 mm | CMM, bore gauge |
| Fan shaft bore (hub) | Ø150 H7 | +0.040/0 mm | CMM, bore gauge |
| Hub face runout | — | <0.02 mm TIR | Dial indicator |
| Bolt circle diameter | Ø240 | ±0.1 mm | CMM |
| Bolt hole positions (12×) | — | ±0.1 mm | CMM |

### 5.2 Fastener Specification

| Parameter | Specification |
|-----------|---------------|
| Bolt Type | M12×1.5 Class 12.9 |
| Number of Bolts | 12 per hub (24 total) |
| Torque | 95 ± 5 Nm |
| Thread Locking | Loctite 243 or equivalent |
| Safety Wire | Required per NASA-STD-5020 |

### 5.3 Surface Finish

| Surface | Finish | Standard |
|---------|--------|----------|
| Shaft bore | Ra 0.8 μm max | ISO 1302 |
| Hub face | Ra 1.6 μm max | ISO 1302 |
| Bolt holes | Ra 3.2 μm max | ISO 1302 |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| SHC-T-001 | Static torque capacity | ≥18,000 Nm without permanent deformation | Bench test |
| SHC-T-002 | Fatigue life (torque cycling) | >10⁷ cycles at 12,000 Nm | Accelerated test |
| SHC-T-003 | Torsional stiffness measurement | 8×10⁶ ±10% Nm/rad | Bench test |
| SHC-T-004 | Misalignment capability | No degradation at ±0.5° angular, ±2 mm parallel | Bench test |
| SHC-T-005 | Vibration endurance | Per DO-160G, Category T | Shaker test |
| SHC-T-006 | Temperature cycling | -55°C to +150°C, 100 cycles | Environmental chamber |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Dimensional inspection | 100% (First Article), 10% (Production) | CMM |
| Material verification | 100% (Cert review) | Material certs |
| Surface finish | 10% (sampling) | Profilometer |
| Magnetic particle inspection (hubs) | 100% | MPI per AMS 2303 |
| Balance check (complete assembly) | 100% | Dynamic balancing |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 61-20](../../61-20_Subsystems/README.md) — Propulsor Subsystems
- [ATA 54](../../../../S-STRUCTURES/ATA_54-NACELLES_PYLONS/README.md) — Nacelles and Pylons (mounting)
- [ATA 05](../../../../ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS/README.md) — Time Limits and Maintenance Checks

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-01-03A — Vibration Dampers (downstream coupling interface)
- 61-00-05-05-01A — Cooling System Connections (thermal effects)

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Parent: 61-00-05_Interfaces](../README.md) · [Next: 61-00-05-01-02A_Mounting_Flanges](61-00-05-01-02A_Mounting_Flanges.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Mechanical Interfaces  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
