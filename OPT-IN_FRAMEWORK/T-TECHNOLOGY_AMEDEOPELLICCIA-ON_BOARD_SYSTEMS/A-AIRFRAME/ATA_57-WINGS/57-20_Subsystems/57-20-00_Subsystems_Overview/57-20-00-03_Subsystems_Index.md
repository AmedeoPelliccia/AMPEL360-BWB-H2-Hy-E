# 57-20-00-03_Subsystems_Index

**Version:** 1.0  
**Date:** 2025-11-28  
**Status:** Draft

---

## Purpose

This document provides a comprehensive index of all physical subsystems within the ATA 57 Wing Subsystems layer (57-20_Subsystems).

---

## Subsystems Index

| ID | Subsystem | Description | Key Interfaces |
|----|-----------|-------------|----------------|
| 57-21 | [FLAPS](../57-21_FLAPS/57-21_GENERAL-FLAPS/57-21-01_Overview.md) | Trailing edge high-lift devices for lift augmentation during takeoff and landing | ATA 27, ATA 31, ATA 32 |
| 57-22 | [SPOILERS](../57-22_SPOILERS/57-22_GENERAL-SPOILERS/57-22-01_Overview.md) | Lift-dump devices and speed brakes for drag augmentation | ATA 27, ATA 22, ATA 31 |
| 57-23 | [AILERONS](../57-23_AILERONS/57-23_GENERAL-AILERONS/57-23-01_Overview.md) | Roll control surfaces for lateral flight control | ATA 27, ATA 22, ATA 31 |
| 57-24 | [SLATS](../57-24_SLATS/57-24_GENERAL-SLATS/57-24-01_Overview.md) | Leading edge high-lift devices for improved stall characteristics | ATA 27, ATA 31, ATA 30 |
| 57-25 | [WING_STRUCTURE](../57-25_WING_STRUCTURE/57-25_GENERAL-WING_STRUCTURE/57-25-01_Overview.md) | Primary wing structural components and load paths | ATA 53, ATA 55, ATA 51 |
| 57-26 | [FUEL_TANKS](../57-26_FUEL_TANKS/57-26_GENERAL-FUEL_TANKS/57-26-01_Overview.md) | Integral wing fuel storage tanks and related systems | ATA 28, ATA 73, H₂ systems |
| 57-27 | [H2_WING_INTEGRATION](../57-27_H2_WING_INTEGRATION/57-27_GENERAL-H2_WING_INTEGRATION/57-27-01_Overview.md) | Hydrogen system integration within wing structure | ATA 28, ATA 73, AMPEL360 H₂ |
| 57-28 | [WING_ICE_PROTECTION](../57-28_WING_ICE_PROTECTION/57-28_GENERAL-WING_ICE_PROTECTION/57-28-01_Overview.md) | Anti-ice and de-ice systems for wing surfaces | ATA 30, ATA 21, ATA 36 |
| 57-29 | [WING_SENSORS_ACTUATION](../57-29_WING_SENSORS_ACTUATION/57-29_GENERAL-WING_SENSORS_ACTUATION/57-29-01_Overview.md) | Wing-mounted sensors and actuation systems | ATA 22, ATA 27, ATA 31 |

---

## Cross-Reference to ATA Chapters

| ATA Chapter | Relationship to 57-20 Subsystems |
|-------------|----------------------------------|
| ATA 21 | ECS interfaces with ice protection |
| ATA 22 | Auto Flight interfaces with control surfaces |
| ATA 27 | Flight Controls interfaces with all control surfaces |
| ATA 28 | Fuel System interfaces with wing fuel tanks and H₂ |
| ATA 30 | Ice Protection interfaces with 57-28 |
| ATA 31 | Indicating Systems interfaces with sensors |
| ATA 32 | Landing Gear interfaces with flap systems |
| ATA 36 | Pneumatics interfaces with ice protection |
| ATA 51 | Standard Practices for structural work |
| ATA 53 | Fuselage interfaces with wing structure |
| ATA 55 | Stabilizers relate to wing control philosophy |
| ATA 73 | Engine Fuel and Control interfaces with H₂ |

---

## Lifecycle Coverage Matrix

| Subsystem | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 |
|-----------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 57-21 FLAPS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 57-22 SPOILERS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 57-23 AILERONS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 57-24 SLATS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 57-25 WING_STRUCTURE | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 57-26 FUEL_TANKS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 57-27 H2_WING_INTEGRATION | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 57-28 WING_ICE_PROTECTION | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 57-29 WING_SENSORS_ACTUATION | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---


## Applicable Standards and Regulations

| Standard | Description | Link |
|----------|-------------|------|
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) | EASA Certification Specifications for Large Aeroplanes | EASA |
| [14 CFR Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) | FAA Airworthiness Standards: Transport Category Airplanes | FAA |
| [DO-178C](https://www.rtca.org/products/do-178c-software-considerations-in-airborne-systems-and-equipment-certification/) | Software Considerations in Airborne Systems | RTCA |
| [DO-254](https://www.rtca.org/products/do-254/) | Design Assurance Guidance for Airborne Electronic Hardware | RTCA |
| [ARP4754A](https://www.sae.org/standards/content/arp4754a/) | Guidelines for Development of Civil Aircraft and Systems | SAE |
| [ARP4761](https://www.sae.org/standards/content/arp4761/) | Guidelines for Safety Assessment of Civil Airborne Systems | SAE |
| [Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012) | EASA Production Organization Approval | EASA |

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
