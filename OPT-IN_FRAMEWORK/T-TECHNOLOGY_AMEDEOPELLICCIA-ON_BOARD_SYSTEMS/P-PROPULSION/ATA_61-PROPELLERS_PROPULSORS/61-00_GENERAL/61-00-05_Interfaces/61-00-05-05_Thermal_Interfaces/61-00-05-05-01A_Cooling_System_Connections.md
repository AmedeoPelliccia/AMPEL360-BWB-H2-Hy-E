# 61-00-05-05-01A - Cooling System Connections Interface

**Document ID:** 61-00-05-05-01A  
**Title:** Cooling System Connections Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the coolant connections between the aircraft thermal management system (ATA 21) and the Q100 propulsor motor/power electronics cooling loops.

---

## 2. Scope

This specification covers:
- Coolant supply and return connections
- Flow rate and pressure requirements
- Coolant specifications
- Quick-disconnect fittings for maintenance
- Thermal performance requirements

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements |
| ICD-21-61 | Thermal Management Interface Control Document | Thermal system interface |
| [SAE AS5877](https://www.sae.org/standards/content/as5877/) | Quick Disconnect Couplings | Industry standard |
| [MIL-PRF-87257](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=213961) | Coolant, Aircraft, Inhibited Glycol | Coolant specification |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Tolerance | Unit | Notes |
|-----------|-------|-----------|------|-------|
| Supply Line Diameter | 25 | ±0.5 | mm | Inner diameter |
| Return Line Diameter | 32 | ±0.5 | mm | Inner diameter (larger for lower pressure drop) |
| Connection Type | Quick-disconnect (SAE AS5877) | — | — | Self-sealing, no-spill |
| Material (Lines) | Aluminum alloy 6061-T6 | — | — | Lightweight, corrosion-resistant |
| Material (Fittings) | Stainless steel 316L | — | — | Corrosion-resistant |
| Design Pressure | 10 | — | bar | Operating pressure |
| Design Temperature | -40 to +120 | — | °C | Coolant temperature range |

### 4.2 Coolant Specifications

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Coolant Type | 50/50 ethylene glycol/water | — | Per MIL-PRF-87257 |
| Freezing Point | -37 | °C | — |
| Boiling Point | +108 | °C | At 1 bar |
| Specific Heat | 3.5 | kJ/(kg·K) | At 50°C |
| Density | 1,070 | kg/m³ | At 20°C |
| Viscosity | 3.5 | cP | At 50°C |
| pH | 7.5-9.5 | — | Corrosion inhibitors |

### 4.3 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| THC-61-001 | Coolant flow rate | 10 ± 1 L/min per propulsor | Test |
| THC-61-002 | Supply pressure | 5 ± 1 bar | Test |
| THC-61-003 | Supply temperature | 40-60 °C | Test |
| THC-61-004 | Maximum return temperature | 85 °C | Test |
| THC-61-005 | Heat rejection capacity | 200 kW per propulsor | Test |
| THC-61-006 | Pressure drop (supply to return) | <2 bar at rated flow | Test |
| THC-61-007 | Leak rate | <10 mL/hour per connection | Visual inspection |
| THC-61-008 | Quick-disconnect time | <30 seconds per connection | Demonstration |

### 4.4 Environmental Constraints

| Parameter | Operating Range | Survival Range | Unit | Notes |
|-----------|----------------|----------------|------|-------|
| Ambient Temperature | -40 to +50 | -55 to +70 | °C | External environment |
| Vibration | 10g RMS | 20g peak | g | Per DO-160G |

---

## 5. Interface Control

### 5.1 Connection Specification

| Interface Point | Type | Thread/Size | Flow Direction | Notes |
|-----------------|------|-------------|----------------|-------|
| Coolant Supply Inlet | Quick-disconnect female | 1" SAE AS5877 | Aircraft → Propulsor | Self-sealing |
| Coolant Return Outlet | Quick-disconnect male | 1.25" SAE AS5877 | Propulsor → Aircraft | Self-sealing |

### 5.2 Flow Path

```
Aircraft Thermal Management System
        ↓ (Supply: 40-60°C, 5 bar, 10 L/min)
   Propulsor Inlet
        ↓
   Motor Cooling Jacket
        ↓
   Power Electronics Cold Plate
        ↓
   Propulsor Outlet
        ↓ (Return: <85°C, 3-4 bar)
Aircraft Thermal Management System (Heat Rejection)
```

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| THC-T-001 | Flow rate verification | 10 ±1 L/min | Flow bench |
| THC-T-002 | Pressure drop measurement | <2 bar at rated flow | Pressure transducers |
| THC-T-003 | Heat rejection test | 200 kW capacity | Thermal dynamometer |
| THC-T-004 | Leak test (connections) | <10 mL/hour | Pressure hold + visual |
| THC-T-005 | Quick-disconnect functional test | <30 sec, no spill | Timed procedure |
| THC-T-006 | Thermal cycle test | 1,000 cycles, no degradation | Thermal cycling |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Leak test (each connection) | 100% | Pressure test (1.5× design) |
| Flow test | 10% (sampling) | Flow bench |
| Quick-disconnect function | 100% | Functional test |
| Visual inspection | 100% | Workmanship, damage |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 21](../../../../ATA_21-AIR_CONDITIONING/README.md) — Air Conditioning and Thermal Management
- [ATA 30](../../../../ATA_30-ICE_RAIN_PROTECTION/README.md) — Ice and Rain Protection (coolant anti-freeze)

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-05-02A — Heat Exchanger Mounts
- 61-00-05-01-04A — Thrust Bearings (bearing lubrication/cooling)

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Parent: 61-00-05_Interfaces](../README.md) · [Next: 61-00-05-05-02A_Heat_Exchanger_Mounts](61-00-05-05-02A_Heat_Exchanger_Mounts.md) →

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
