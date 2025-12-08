# 61-00-05-06-04A - ICD Propulsion to Structure

**Document ID:** ICD-54-61 (61-00-05-06-04A)  
**Title:** Interface Control Document — Propulsion System to Aircraft Structure  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Introduction

### 1.1 Purpose
This ICD defines all interfaces between the Q100 Propulsion System (ATA 61) and the Aircraft Structure (ATA 54), including nacelles, pylons, and airframe attachment points.

### 1.2 Scope
- Mechanical mounting interfaces (flanges, fasteners)
- Structural load transfer (thrust, side loads, moments)
- Vibration isolation
- Thermal interfaces and expansion accommodation
- Access and removal provisions for maintenance

### 1.3 Applicable Documents
- 61-00-05-01-02A — Mounting Flanges
- 61-00-05-01-03A — Vibration Dampers
- 61-00-05-05-03A — Thermal Insulation Boundaries

---

## 2. System Overviews

### 2.1 Propulsion System (ATA 61)
- Four propulsor units: electric motor + ducted fan assembly
- Mass per propulsor: ~1,200 kg
- Maximum thrust per propulsor: 50 kN forward, 20 kN reverse
- Operating temperature range: -40°C to +120°C (motor housing exterior)

**Interface Responsibilities:**
- Transfer thrust loads to nacelle/pylon structure
- Provide vibration-isolated mounting
- Accommodate thermal expansion (±5 mm)
- Enable removal/installation within 8 hours

### 2.2 Aircraft Structure (ATA 54)
- Nacelles: Composite and aluminum construction
- Pylons: Aluminum alloy, integrated with wing/fuselage structure
- Mounting interfaces: Titanium flanges

**Interface Responsibilities:**
- Accept propulsor loads (thrust, side, torque, bending)
- Provide mounting flanges with alignment features
- Provide access for propulsor installation/removal
- Maintain structural integrity under all load cases

---

## 3. Interface Summary

| Interface Type | Specification Reference | Load Condition | Criticality |
|----------------|-------------------------|----------------|-------------|
| Mounting Flange | 61-00-05-01-02A | Static + dynamic structural loads | Safety-critical |
| Vibration Isolation | 61-00-05-01-03A | Vibration transmission control | Critical |
| Thermal Expansion | 61-00-05-01-02A | ±5 mm axial, ±2 mm radial | Important |
| Thermal Insulation | 61-00-05-05-03A | Touch temperature <43°C | Safety (maintenance) |

---

## 4. Key Interface Requirements

### 4.1 Structural Load Interface

| Load Case | Propulsion System Loads | Structure Requirements |
|-----------|-------------------------|------------------------|
| Maximum Forward Thrust | 50 kN axial per propulsor | Accept 50 kN × 1.5 = 75 kN ultimate |
| Maximum Reverse Thrust | 20 kN axial per propulsor | Accept 20 kN × 1.5 = 30 kN ultimate |
| Maximum Side Load | 25 kN lateral per propulsor | Accept 25 kN × 1.5 = 37.5 kN ultimate |
| Maximum Bending Moment | 30 kNm | Accept 30 kNm × 1.5 = 45 kNm ultimate |
| Maximum Torque Reaction | 15 kNm | Accept 15 kNm × 1.5 = 22.5 kNm ultimate |
| Propulsor Weight (static) | ~1,200 kg × 9.81 m/s² = 11.8 kN | Accept 11.8 kN × 2.0 = 23.6 kN ultimate (downward) |

### 4.2 Mounting Flange Interface

| Parameter | Propulsion Responsibility | Structure Responsibility |
|-----------|---------------------------|--------------------------|
| Flange Type | Circular bolted flange, Ø800 mm | Matching circular flange, Ø800 mm |
| Flange Material | Aluminum alloy 7075-T651 | Titanium alloy Ti-6Al-4V |
| Bolt Circle | Ø750 mm, 24× M16 bolts | Matching Ø750 mm bolt pattern |
| Alignment | Pilot diameter Ø600 mm H7 | Pilot bore Ø600 mm h7 |
| Installation Tolerance | ±0.5 mm position, ±0.2° angle | Provide alignment features |

### 4.3 Vibration Isolation Interface

| Requirement | Propulsion Responsibility | Structure Responsibility |
|-------------|---------------------------|--------------------------|
| Isolator Type | 12× elastomeric isolators per propulsor | Provide mounting bosses for isolators |
| Transmissibility | <0.3 at 300-3000 Hz | Accept transmitted vibration levels |
| Static Deflection | ~3 mm under weight | — |
| Dynamic Deflection | ≤5 mm | Accept deflection in mounting clearances |

### 4.4 Thermal Interface

| Requirement | Propulsion Responsibility | Structure Responsibility |
|-------------|---------------------------|--------------------------|
| Motor Housing Temperature | ≤150°C exterior surface | Accept radiant heat flux |
| Touch Temperature (Maintenance) | ≤43°C on accessible surfaces | — |
| Thermal Expansion | Accommodate ±5 mm axial, ±2 mm radial | Provide slotted holes for axial growth |
| Insulation | Provide insulation per 61-00-05-05-03A | Accommodate insulation thickness |

---

## 5. Physical Interface Locations

### 5.1 Propulsor Mounting Stations

| Propulsor | Nacelle Station | Fuselage/Wing Reference | Access |
|-----------|-----------------|-------------------------|--------|
| Propulsor 1 (Port Outboard) | Nacelle 1, Station 450 | Wing BL -8,000 mm | Forward access panel |
| Propulsor 2 (Port Inboard) | Nacelle 2, Station 450 | Wing BL -3,000 mm | Forward access panel |
| Propulsor 3 (Starboard Inboard) | Nacelle 3, Station 450 | Wing BL +3,000 mm | Forward access panel |
| Propulsor 4 (Starboard Outboard) | Nacelle 4, Station 450 | Wing BL +8,000 mm | Forward access panel |

### 5.2 Flange Orientation

- Propulsor flange face perpendicular to thrust axis
- Bolt hole #1 at 12 o'clock position (top dead center)
- Pilot feature provides ±0.5 mm radial alignment

---

## 6. Verification and Validation

### 6.1 Interface Verification Matrix

| Interface | Verification Method | Test Reference | Status |
|-----------|---------------------|----------------|--------|
| Static load capacity | Test | MNT-T-001, MNT-T-002 | TBD |
| Fatigue life | Test | MNT-T-003 | TBD |
| Vibration isolation | Test | VIB-T-003 | TBD |
| Thermal expansion | Test + Analysis | MNT-T-006 | TBD |
| Installation time | Demonstration | MNT-T-005 | TBD |

### 6.2 Integration Test Plan

1. **Static Load Test**: Apply limit loads in all directions, verify no permanent deformation
2. **Ultimate Load Test**: Apply ultimate loads, verify no failure
3. **Fatigue Test**: Apply 2× design life cycles, verify no crack initiation
4. **Vibration Test**: Measure transmissibility, verify <0.3 at >300 Hz
5. **Thermal Cycle Test**: Perform 100 thermal cycles, verify no degradation
6. **Installation/Removal Demonstration**: Verify <8 hours with standard tools

---

## 7. Operations and Maintenance

### 7.1 Installation Procedure

1. **Preparation**:
   - Inspect mounting flanges (cleanliness, damage)
   - Install vibration isolators on propulsor
   - Apply anti-seize compound to bolt threads

2. **Alignment**:
   - Position propulsor using handling fixture
   - Engage pilot feature for radial alignment
   - Insert alignment pins at 12 o'clock and 6 o'clock

3. **Fastening**:
   - Install 24× M16 bolts with titanium washers
   - Torque in star pattern to 280 ±15 Nm
   - Install thread locking compound

4. **Verification**:
   - Check alignment (±0.5 mm, ±0.2°)
   - Perform electrical continuity test (grounding)
   - Connect all interfaces (electrical, thermal, H₂)
   - Perform ground functional test

**Estimated Time**: 6-8 hours with 2 technicians

### 7.2 Removal Procedure

1. Disconnect all interfaces (electrical, thermal, H₂)
2. Remove 24× mounting bolts
3. Use handling fixture to support propulsor weight
4. Slide propulsor aft to disengage pilot feature
5. Lower propulsor using overhead crane

**Estimated Time**: 4-6 hours

---

## 8. Cross-References

### 8.1 Related ICDs
- ICD-24/27/42-61 — Propulsion to Avionics
- ICD-28-61 — Propulsion to Fuel System

### 8.2 Detailed Interface Specifications
- 61-00-05-01_Mechanical_Interfaces (all documents)
- 61-00-05-05-03A — Thermal Insulation Boundaries

---

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Integration Team | Initial release |

---

← [Previous: 61-00-05-06-03A_ICD_Propulsion_to_Fuel_System](61-00-05-06-03A_ICD_Propulsion_to_Fuel_System.md) · [Parent: 61-00-05_Interfaces](../README.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Interface Control Documents  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
