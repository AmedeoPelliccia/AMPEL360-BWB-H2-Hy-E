# 61-00-05-01-02A - Mounting Flanges Interface

**Document ID:** 61-00-05-01-02A  
**Title:** Mounting Flanges Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the mounting flange interface between the propulsor assembly and the nacelle/pylon structure of the AMPEL360 Q100 aircraft. The interface ensures secure structural attachment while enabling propulsor removal for maintenance.

---

## 2. Scope

This specification covers:
- Flange design and geometry
- Structural load transfer requirements
- Fastener specifications
- Installation alignment tolerances
- Access requirements for maintenance

### 2.1 Applicable Units
- All four Q100 propulsor units
- Standardized interface across all positions

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements document |
| ICD-54-61 | Structural Interface Control Document | Structure team interface |
| [CS-25.1193](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) | Cowling and Nacelle Skin | EASA regulation |
| [SAE AIR1845](https://www.sae.org/standards/content/air1845/) | Design and Installation of Propulsion Systems | Industry guidance |
| MIL-STD-1472H | Human Engineering | Access requirements |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Flange Type | Bolted circular flange | — | — | Standardized interface |
| Flange Outer Diameter | 800 | ±2.0 | mm | — |
| Flange Thickness | 25 | ±1.0 | mm | At bolt circle |
| Bolt Circle Diameter | 750 | ±0.5 | mm | — |
| Number of Bolt Holes | 24 | — | — | Equally spaced |
| Bolt Hole Diameter | 20 | +0.5/0 | mm | H9 tolerance |
| Material (Propulsor Flange) | Aluminum alloy 7075-T651 | — | — | High strength |
| Material (Nacelle Flange) | Titanium alloy Ti-6Al-4V | — | — | Galvanic compatibility |
| Flange Face Flatness | — | <0.1 mm | mm | Per ISO 1101 |
| Surface Treatment | Anodized (MIL-A-8625 Type II) | — | — | Corrosion protection |

### 4.2 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| MNT-61-001 | Maximum thrust load (axial) | 50 kN forward, 20 kN reverse | Analysis, Test |
| MNT-61-002 | Maximum side load (lateral) | 25 kN | Analysis, Test |
| MNT-61-003 | Maximum bending moment | 30 kNm | Analysis, Test |
| MNT-61-004 | Maximum torque reaction | 15 kNm | Analysis |
| MNT-61-005 | Flange stiffness (axial) | >5×10⁸ N/m | FEA |
| MNT-61-006 | Fatigue life | >60,000 flight cycles | Analysis, Test |
| MNT-61-007 | Shear load transfer (per bolt) | >50 kN ultimate | Analysis |
| MNT-61-008 | Removal time (skilled technician) | <4 hours | Demonstration |
| MNT-61-009 | Installation alignment repeatability | ±0.5 mm position, ±0.2° angle | Measurement |

### 4.3 Environmental Constraints

| Parameter | Operating Range | Survival Range | Unit | Notes |
|-----------|----------------|----------------|------|-------|
| Temperature | -40 to +120 | -55 to +150 | °C | Per DO-160G |
| Vibration | 10g RMS | 20g peak | g | Per DO-160G Category T |
| Shock | 25g | 50g | g | 11 ms half-sine |
| Humidity | 0 to 95% | — | % RH | Non-condensing |
| Salt Fog Resistance | 1000 hours | — | hours | Per ASTM B117 |

---

## 5. Interface Control

### 5.1 Dimensional Control

| Interface Point | Dimension | Tolerance | Inspection Method |
|-----------------|-----------|-----------|-------------------|
| Bolt circle diameter | Ø750 | ±0.5 mm | CMM |
| Bolt hole positions (24×) | — | ±0.3 mm | CMM |
| Flange face flatness | — | <0.1 mm | Surface plate, dial indicator |
| Flange face perpendicularity | — | <0.15 mm/100mm | CMM |
| Pilot diameter (centering) | Ø600 H7 | +0.030/0 mm | CMM, bore gauge |
| Pilot length | 15 | ±0.5 mm | Caliper |

### 5.2 Fastener Specification

| Parameter | Specification |
|-----------|---------------|
| Bolt Type | M16×2.0 Titanium alloy bolts per AMS 4967 |
| Bolt Class | Grade 23 titanium (Ti-6Al-4V) |
| Number of Bolts | 24 |
| Torque | 280 ± 15 Nm |
| Thread Locking | Loctite 243 or equivalent aerospace-grade |
| Washers | Titanium washers per MS21044 |
| Safety Wire | Not required (locking features) |
| Anti-Seize Compound | Nickel-based per MIL-PRF-907 |

### 5.3 Gasket/Seal Requirements

| Parameter | Specification |
|-----------|---------------|
| Gasket Material | PTFE-based composite |
| Gasket Thickness | 1.5 ± 0.2 mm |
| Compression Set | <20% after 1000 hours at 120°C |
| Environmental Seal | Required for dust/moisture ingress protection |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| MNT-T-001 | Ultimate load test (axial) | 75 kN (1.5× limit load) without failure | Static test |
| MNT-T-002 | Ultimate load test (lateral) | 37.5 kN without failure | Static test |
| MNT-T-003 | Fatigue test (combined loads) | 2× design life without crack initiation | Accelerated test |
| MNT-T-004 | Vibration endurance | Per DO-160G Category T, no loosening | Shaker test |
| MNT-T-005 | Installation/removal demonstration | <4 hours with standard tools | Procedure validation |
| MNT-T-006 | Alignment repeatability | ±0.5 mm, ±0.2° over 10 cycles | Measurement study |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Dimensional inspection | 100% (First Article), 10% (Production) | CMM |
| Bolt hole position verification | 100% (FA), 5% (Production) | CMM or functional gauge |
| Flatness and perpendicularity | 100% (FA), 10% (Production) | Surface plate, CMM |
| Material verification | 100% (cert review) | Material certificates |
| Surface treatment inspection | 100% (visual), 10% (coating thickness) | Visual, eddy current |
| Thread inspection (bolts) | 100% | Thread gauges, optical |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 54](../../../../S-STRUCTURES/ATA_54-NACELLES_PYLONS/README.md) — Nacelles and Pylons (structure side of interface)
- [ATA 05](../../../../ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS/README.md) — Maintenance procedures
- [ATA 20](../../../../ATA_20-STANDARD_PRACTICES/README.md) — Standard practices for fasteners

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-01-03A — Vibration Dampers
- 61-00-05-06-04A — ICD Propulsion to Structure

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-01-01A_Shaft_Coupling](61-00-05-01-01A_Shaft_Coupling.md) · [Next: 61-00-05-01-03A_Vibration_Dampers](61-00-05-01-03A_Vibration_Dampers.md) →

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
