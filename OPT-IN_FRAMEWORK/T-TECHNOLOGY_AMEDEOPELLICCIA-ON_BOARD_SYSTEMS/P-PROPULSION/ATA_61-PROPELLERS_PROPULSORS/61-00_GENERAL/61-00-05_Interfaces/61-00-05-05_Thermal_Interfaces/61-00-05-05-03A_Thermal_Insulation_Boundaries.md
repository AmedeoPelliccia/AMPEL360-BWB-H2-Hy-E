# 61-00-05-05-03A - Thermal Insulation Boundaries Interface

**Document ID:** 61-00-05-05-03A  
**Title:** Thermal Insulation Boundaries Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the thermal insulation boundary interfaces between propulsor hot/cold zones and the surrounding aircraft structure to prevent thermal damage and ensure personnel safety.

---

## 2. Scope

This specification covers:
- Insulation materials and thicknesses
- High-temperature zones (motor, power electronics)
- Cryogenic zones (H₂ lines, if applicable)
- Touch-temperature limits for maintenance
- Fire barrier integration

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements |
| [FAR 25.1193](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-E/section-25.1193) | Cowling and Nacelle Skin | Thermal protection requirements |
| [ISO 13732-1](https://www.iso.org/standard/37891.html) | Hot Surfaces — Contact Temperature Limits | Safety limits |

---

## 4. Interface Description

### 4.1 Thermal Zones

| Zone | Component | Max Surface Temp | Insulation Type | Thickness |
|------|-----------|------------------|-----------------|-----------|
| Zone A | Motor housing exterior | 150°C | Ceramic fiber blanket | 25 mm |
| Zone B | Power electronics enclosure | 100°C | Aerogel composite | 10 mm |
| Zone C | Coolant lines (hot) | 90°C | Elastomeric foam | 15 mm |
| Zone D | H₂ lines (cryogenic) | -253°C | Vacuum-insulated pipe | N/A |
| Zone E | Nacelle interior (touchable) | 43°C | Per ISO 13732-1 | Variable |

### 4.2 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| THI-61-001 | Maximum touch temperature (maintenance) | 43°C | Thermal imaging |
| THI-61-002 | Thermal conductivity (insulation) | <0.05 W/(m·K) | Material test |
| THI-61-003 | Fire resistance | Per FAR 25 Appendix F Part I | Burn test |
| THI-61-004 | Cryogenic insulation effectiveness | <5 W/m heat leak | Calorimetry |
| THI-61-005 | Insulation service life | >30,000 flight hours | Qualification |

---

## 5. Interface Control

### 5.1 Insulation Material Specifications

| Material | Application | Max Temp | Thermal Conductivity | Notes |
|----------|-------------|----------|----------------------|-------|
| Ceramic fiber blanket | Motor housing | 1,200°C | 0.04 W/(m·K) at 500°C | Non-combustible |
| Aerogel composite | Electronics enclosure | 250°C | 0.015 W/(m·K) at 100°C | Hydrophobic |
| Elastomeric foam | Coolant lines | 150°C | 0.035 W/(m·K) at 50°C | Flexible, closed-cell |
| Vacuum-insulated pipe | H₂ cryogenic | -270°C to +100°C | <0.001 W/(m·K) effective | Multi-layer insulation |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| THI-T-001 | Touch temperature test | <43°C after 2 hours operation | Thermal imaging |
| THI-T-002 | Thermal conductivity | Per material spec | ASTM C177 |
| THI-T-003 | Fire resistance | Self-extinguishing, <25 mm burn length | FAR 25 Appendix F |
| THI-T-004 | Cryogenic heat leak | <5 W/m | Calorimetry |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 26](../../../../ATA_26-FIRE_PROTECTION/README.md) — Fire Protection
- [ATA 54](../../../../S-STRUCTURES/ATA_54-NACELLES_PYLONS/README.md) — Nacelles and Pylons

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-05-02A_Heat_Exchanger_Mounts](61-00-05-05-02A_Heat_Exchanger_Mounts.md) · [Parent: 61-00-05_Interfaces](../README.md) →

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
