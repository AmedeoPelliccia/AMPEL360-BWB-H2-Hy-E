# 61-00-05-04-01A - H₂ Fuel Supply Connections Interface

**Document ID:** 61-00-05-04-01A  
**Title:** Hydrogen Fuel Supply Connections Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the hydrogen fuel supply connections between the aircraft cryogenic H₂ system (ATA 28) and the Q100 propulsor fuel cell or H₂-powered generator interfaces.

---

## 2. Scope

This specification covers:
- Cryogenic H₂ supply line connections
- Flow control interfaces
- Temperature and pressure monitoring
- Emergency shutoff provisions
- Material compatibility and safety requirements

### 2.1 Applicable Units
- All four Q100 propulsor units (if H₂-powered generators used)
- Centralized fuel cell system interfaces

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements |
| ICD-28-61 | Fuel System Interface Control Document | Fuel system interface |
| [SAE AIR7928](https://www.sae.org/standards/content/air7928/) | Hydrogen Aircraft — Safety Considerations | H₂ safety |
| [ISO 14687](https://www.iso.org/standard/69539.html) | Hydrogen Fuel Quality | Fuel specifications |
| [EN 1797-2](https://standards.iteh.ai/catalog/standards/cen/d8e4f8c5-9d8a-4c9a-8a0e-c5e2c5e2c5e2/en-1797-2-2001) | Cryogenic Vessels | Cryogenic standards |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Supply Line Diameter | 25 | ±0.5 | mm | Inner diameter |
| Connection Type | VCR (vacuum coupling) | — | — | Metal gasket seal |
| Material (Line) | Stainless steel 316L | — | — | H₂ compatible |
| Material (Fittings) | Stainless steel 316L | — | — | Electropolished |
| Design Pressure | 350 | — | bar | At ambient temp |
| Design Temperature | -253 | — | °C | Liquid H₂ (20 K) |
| Gaseous H₂ Supply Temperature | -40 to +80 | — | °C | After vaporization |
| Maximum Flow Rate | 2.0 | — | kg/min | Per propulsor |

### 4.2 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| H2F-61-001 | Supply pressure (gaseous) | 5-10 bar | Test |
| H2F-61-002 | Supply pressure regulation | ±0.5 bar | Test |
| H2F-61-003 | Flow rate capability | 0-2.0 kg/min | Test |
| H2F-61-004 | Leak rate | <1×10⁻⁶ mbar·L/s | Helium leak test |
| H2F-61-005 | Emergency shutoff time | <2 seconds | Test |
| H2F-61-006 | Purity (H₂) | >99.97% per ISO 14687 | Analysis |
| H2F-61-007 | Connection torque | Per VCR spec | Installation procedure |

### 4.3 Environmental Constraints

| Parameter | Operating Range | Survival Range | Unit | Notes |
|-----------|----------------|----------------|------|-------|
| Ambient Temperature | -40 to +50 | -55 to +70 | °C | External environment |
| Vibration | 10g RMS | 20g peak | g | Per DO-160G |
| Thermal Cycling | 1,000 cycles | — | cycles | -253°C to +50°C |

---

## 5. Interface Control

### 5.1 Connection Specification

| Interface Point | Specification | Torque | Inspection Method |
|-----------------|---------------|--------|-------------------|
| H₂ supply inlet (propulsor side) | VCR 1/2" male | 40 Nm | Helium leak test |
| H₂ return (if applicable) | VCR 1/2" female | 40 Nm | Helium leak test |
| Purge gas connection | VCR 1/4" | 20 Nm | Functional test |

### 5.2 Safety Features

| Feature | Specification |
|---------|---------------|
| Emergency Shutoff Valve | Fail-safe closed, <2 sec actuation |
| Pressure Relief Valve | Set at 1.5× design pressure |
| Flame Arrestor | Integrated in supply line |
| Grounding/Bonding | <10 mΩ to aircraft structure |
| H₂ Detection | Sensor <1% LEL detection |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| H2F-T-001 | Leak test (connections) | <1×10⁻⁶ mbar·L/s | Helium mass spectrometer |
| H2F-T-002 | Pressure cycle test | 10,000 cycles, 0-350 bar, no leak | Pressure cycling fixture |
| H2F-T-003 | Flow rate verification | 0-2.0 kg/min per spec | Flow bench |
| H2F-T-004 | Emergency shutoff test | <2 sec from command to closure | High-speed measurement |
| H2F-T-005 | Thermal shock test | 100 cycles, no degradation | Thermal cycling chamber |
| H2F-T-006 | Burst pressure test | >2× design pressure | Hydrostatic test |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Leak test (each connection) | 100% | Helium leak detector |
| Material certification | 100% | Certificate review |
| Surface finish (electropolish) | 10% (sampling) | Visual, profilometer |
| Dimensional inspection | 100% (First Article), 10% (Production) | CMM |
| Pressure test | 100% | Hydrostatic (1.5× design) |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 28](../../../../F-FUEL/ATA_28-FUEL/README.md) — Fuel System (H₂ source)
- [ATA 73](../../../../P-PROPULSION/ATA_73-ENGINE_FUEL_CONTROL/README.md) — Engine Fuel and Control
- [ATA 26](../../../../ATA_26-FIRE_PROTECTION/README.md) — Fire Protection (H₂ safety)

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-04-02A — Safety Interlocks
- 61-00-05-04-03A — Pressure Regulation
- 61-00-05-04-04A — Leak Detection Integration

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Parent: 61-00-05_Interfaces](../README.md) · [Next: 61-00-05-04-02A_Safety_Interlocks](61-00-05-04-02A_Safety_Interlocks.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Hydrogen System Interfaces  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
