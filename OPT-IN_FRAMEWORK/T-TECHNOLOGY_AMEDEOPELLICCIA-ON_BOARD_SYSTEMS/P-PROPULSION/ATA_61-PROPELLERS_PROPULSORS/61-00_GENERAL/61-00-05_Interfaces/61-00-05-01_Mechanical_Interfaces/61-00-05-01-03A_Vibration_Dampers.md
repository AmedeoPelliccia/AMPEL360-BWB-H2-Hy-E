# 61-00-05-01-03A - Vibration Dampers Interface

**Document ID:** 61-00-05-01-03A  
**Title:** Vibration Dampers Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the vibration damper interface within the AMPEL360 Q100 propulsor assembly. Vibration dampers isolate high-frequency motor and fan vibrations from the aircraft structure while maintaining structural integrity for load transfer.

---

## 2. Scope

This specification covers:
- Vibration isolator design and materials
- Vibration isolation performance requirements
- Dynamic stiffness and damping characteristics
- Installation and maintenance requirements
- Interface to mounting flanges and structure

### 2.1 Applicable Units
- All four Q100 propulsor units
- Both primary and redundant vibration isolation paths

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements document |
| 61-00-02-PSSA-001 | Preliminary Safety Assessment | Safety requirements |
| [MIL-STD-167-1A](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35861) | Mechanical Vibrations of Shipboard Equipment | Vibration standards |
| [DO-160G Section 8](https://www.rtca.org/content/standards-guidance-materials) | Environmental Conditions — Vibration | Aviation standard |
| [ISO 10846](https://www.iso.org/standard/50453.html) | Acoustics and Vibration — Laboratory Measurement | Test methods |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Isolator Type | Elastomeric with wire mesh damping | — | — | Hybrid design |
| Number of Isolators per Propulsor | 12 | — | — | Distributed mounting |
| Isolator Height (installed) | 45 | ±2.0 | mm | Under nominal load |
| Isolator Diameter | 80 | ±1.0 | mm | — |
| Material (Elastomer) | Fluorosilicone rubber (Mil-R-83248) | — | — | Fuel-resistant |
| Material (Wire Mesh) | Stainless steel 316L | — | — | Corrosion-resistant |
| Hardness (Elastomer) | 60 ± 5 Shore A | — | — | At 23°C |
| Static Load Rating (per isolator) | 2,500 | ±200 | N | Nominal propulsor weight |
| Dynamic Load Rating (per isolator) | 5,000 | — | N | Peak loads |

### 4.2 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| VIB-61-001 | Vibration isolation frequency | >300 Hz | Test |
| VIB-61-002 | Transmissibility at 300-3000 Hz | <0.3 (>10 dB isolation) | Test |
| VIB-61-003 | Static stiffness (axial) | 1.2×10⁶ N/m per isolator | Test |
| VIB-61-004 | Static stiffness (lateral) | 0.8×10⁶ N/m per isolator | Test |
| VIB-61-005 | Damping ratio | 0.10 to 0.20 | Test |
| VIB-61-006 | Maximum static deflection | 3 mm | Analysis |
| VIB-61-007 | Maximum dynamic deflection | 5 mm | Test |
| VIB-61-008 | Service life | >30,000 flight hours | Qualification |
| VIB-61-009 | Temperature stability | Stiffness variation <20% over temp range | Test |
| VIB-61-010 | Creep resistance | <10% deflection change after 1000 hrs at max load | Test |

### 4.3 Environmental Constraints

| Parameter | Operating Range | Survival Range | Unit | Notes |
|-----------|----------------|----------------|------|-------|
| Temperature | -40 to +120 | -55 to +150 | °C | Per DO-160G |
| Vibration Input | 10g RMS | 20g peak | g | Per DO-160G Category T |
| Shock | 25g | 50g | g | 11 ms half-sine |
| Humidity | 0 to 95% | — | % RH | Non-condensing |
| Fuel Exposure | Resistant | — | — | Jet fuel and H₂ exposure |
| Ozone Resistance | >500 hours | — | hours | Per ASTM D1149 |

---

## 5. Interface Control

### 5.1 Dimensional Control

| Interface Point | Dimension | Tolerance | Inspection Method |
|-----------------|-----------|-----------|-------------------|
| Mounting bolt pattern | Per isolator design | ±0.2 mm | CMM |
| Installed height (at nominal load) | 45 mm | ±2 mm | Height gauge under load |
| Isolator centerline alignment | — | ±1 mm | CMM |
| Load plane parallelism | — | <0.5° | Angle measurement |

### 5.2 Fastener Specification

| Parameter | Specification |
|-----------|---------------|
| Mounting Bolt Type | M10×1.5 Class 12.9 steel |
| Number of Bolts per Isolator | 2 (top), 2 (bottom) |
| Torque | 60 ± 5 Nm |
| Thread Locking | Loctite 243 or equivalent |
| Washers | Hardened steel per DIN 125 |
| Safety Wire | Required for critical isolators |

### 5.3 Preload Requirements

| Parameter | Specification |
|-----------|---------------|
| Installation Preload | 2,500 ± 200 N per isolator |
| Preload Verification Method | Torque wrench + angle rotation |
| Settling Time | Allow 24 hours after installation |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| VIB-T-001 | Static stiffness measurement | 1.2×10⁶ ±15% N/m (axial) | Load-deflection test |
| VIB-T-002 | Dynamic stiffness measurement | Per spec across frequency range | Impedance head test |
| VIB-T-003 | Transmissibility measurement | <0.3 at 300-3000 Hz | Shaker test, accelerometers |
| VIB-T-004 | Damping ratio measurement | 0.10 to 0.20 | Half-power bandwidth method |
| VIB-T-005 | Temperature cycling | Performance variation <20% | Environmental chamber |
| VIB-T-006 | Fatigue life test | >2× design life (60,000 FH equivalent) | Accelerated cycling |
| VIB-T-007 | Ultimate load test | 3× static rating without rupture | Tensile/compressive test |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Dimensional inspection | 100% (First Article), 10% (Production) | CMM, calipers |
| Hardness verification (elastomer) | 100% (FA), 5% (Production) | Shore A durometer |
| Material certification | 100% | Material certs review |
| Visual inspection | 100% | Visual for defects, voids |
| Static load-deflection check | 10% (sampling) | Load frame, LVDT |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 54](../../../../S-STRUCTURES/ATA_54-NACELLES_PYLONS/README.md) — Nacelles and Pylons (mounting structure)
- [ATA 05](../../../../ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS/README.md) — Vibration isolator inspection intervals
- [ATA 20](../../../../ATA_20-STANDARD_PRACTICES/README.md) — Standard practices for vibration isolation

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-01-02A — Mounting Flanges (downstream interface)
- 61-00-05-01-04A — Thrust Bearings (vibration transmission)

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-01-02A_Mounting_Flanges](61-00-05-01-02A_Mounting_Flanges.md) · [Next: 61-00-05-01-04A_Thrust_Bearings](61-00-05-01-04A_Thrust_Bearings.md) →

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
