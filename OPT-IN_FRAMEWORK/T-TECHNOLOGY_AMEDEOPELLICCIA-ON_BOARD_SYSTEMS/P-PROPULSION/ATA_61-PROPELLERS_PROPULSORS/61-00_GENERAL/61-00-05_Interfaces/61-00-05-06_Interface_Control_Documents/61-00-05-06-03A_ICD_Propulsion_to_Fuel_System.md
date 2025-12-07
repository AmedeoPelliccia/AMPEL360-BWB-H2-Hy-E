# 61-00-05-06-03A - ICD Propulsion to Fuel System

**Document ID:** ICD-28-61 (61-00-05-06-03A)  
**Title:** Interface Control Document — Propulsion System to Hydrogen Fuel System  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Introduction

### 1.1 Purpose
This ICD defines all interfaces between the Q100 Propulsion System (ATA 61) and the Hydrogen Fuel System (ATA 28), including H₂ supply, pressure regulation, safety interlocks, and leak detection.

### 1.2 Scope
- Gaseous H₂ supply connections (post-vaporization)
- Pressure regulation and control
- Safety interlock signals
- Leak detection integration
- Emergency shutoff provisions

### 1.3 Applicable Documents
- 61-00-05-04-01A — H₂ Fuel Supply Connections
- 61-00-05-04-02A — Safety Interlocks
- 61-00-05-04-03A — Pressure Regulation
- 61-00-05-04-04A — Leak Detection Integration

---

## 2. System Overviews

### 2.1 Propulsion System (ATA 61)
- Four propulsor units with integrated power generation (fuel cells or H₂ generators)
- H₂ consumption: ~2 kg/min per propulsor at max power
- Pressure requirement: 5-10 bar regulated

**Interface Responsibilities:**
- Accept H₂ fuel at specified pressure and purity
- Monitor H₂ leaks and pressure anomalies
- Execute emergency shutoff commands
- Report H₂ consumption and system status

### 2.2 Fuel System (ATA 28)
- Cryogenic liquid H₂ (LH₂) storage tanks
- LH₂ vaporization and warming
- High-pressure gaseous H₂ distribution
- Pressure regulation to propulsion requirements

**Interface Responsibilities:**
- Supply gaseous H₂ at 5-10 bar, >99.97% purity
- Regulate pressure to ±0.5 bar
- Provide emergency shutoff capability
- Monitor H₂ leaks in distribution system

---

## 3. Interface Summary

| Interface Type | Direction | Specification Reference | Criticality |
|----------------|-----------|-------------------------|-------------|
| H₂ Supply (gaseous) | Fuel System → Propulsion | 61-00-05-04-01A | Safety-critical |
| Pressure Regulation | Fuel System → Propulsion | 61-00-05-04-03A | Critical |
| H₂ Leak Detection | Both (shared sensors) | 61-00-05-04-04A | Safety-critical |
| Safety Interlocks | Both (hardwired) | 61-00-05-04-02A | Safety-critical |
| Emergency Shutoff | Propulsion/Pilot → Fuel System | 61-00-05-04-02A | Safety-critical |

---

## 4. Key Interface Requirements

### 4.1 H₂ Supply Interface

| Requirement | Propulsion Responsibility | Fuel System Responsibility |
|-------------|---------------------------|----------------------------|
| Supply Pressure | Accept 5-10 bar | Regulate to 8 ±0.5 bar |
| Flow Rate | Consume ≤2 kg/min per propulsor | Supply ≥2 kg/min per propulsor |
| Purity | Accept ≥99.97% H₂ | Provide ≥99.97% H₂ per ISO 14687 |
| Temperature | Accept -40 to +80°C | Provide gaseous H₂ in this range |
| Leak Rate | Monitor and report | Monitor distribution system |

### 4.2 Safety Interlock Interface

| Interlock Signal | Source | Destination | Response Time | Action |
|------------------|--------|-------------|---------------|--------|
| H2_LEAK_DETECTED | Leak detectors | Both systems | <500 ms | Close supply valves, alert crew |
| H2_OVERPRESSURE | Pressure sensors | Both systems | <200 ms | Close supply valves, relieve pressure |
| EMERG_H2_SHUTOFF | Pilot command | Both systems | <2 seconds | Close all H₂ valves, purge lines |
| GROUND_SAFETY_PIN | Ground equipment | Propulsion | Immediate | Disable H₂ valve opening |

### 4.3 Leak Detection Interface

| Zone | Sensor Location | Alarm Level 1 (Caution) | Alarm Level 2 (Warning) | Response |
|------|-----------------|--------------------------|-------------------------|----------|
| Propulsor Inlet | Each nacelle H₂ inlet | 0.4% H₂ (10% LEL) | 1.0% H₂ (25% LEL) | Increase ventilation / Close valves |
| Nacelle Interior | Ventilated zones | 0.4% H₂ | 1.0% H₂ | Increase ventilation / Close valves |
| Fuel Cell Enclosure | Enclosure interior | 0.4% H₂ | 1.0% H₂ | Activate purge / Close valves |

---

## 5. Physical Interface Locations

### 5.1 H₂ Supply Connections

| Propulsor | H₂ Supply Line Station | Connection Type | Line Size |
|-----------|------------------------|-----------------|-----------|
| Propulsor 1 | Nacelle 1, Station 480 | VCR 1/2" male (propulsor side) | 25 mm ID |
| Propulsor 2 | Nacelle 2, Station 480 | VCR 1/2" male | 25 mm ID |
| Propulsor 3 | Nacelle 3, Station 480 | VCR 1/2" male | 25 mm ID |
| Propulsor 4 | Nacelle 4, Station 480 | VCR 1/2" male | 25 mm ID |

### 5.2 Safety Interlock Connections

- Hardwired discrete signals via MIL-DTL-38999 connectors
- Signals duplicated on AFDX VL-6101 for redundancy
- Fail-safe design: Loss of signal = shutoff state

---

## 6. Verification and Validation

### 6.1 Interface Verification Matrix

| Interface | Verification Method | Test Reference | Status |
|-----------|---------------------|----------------|--------|
| H₂ supply pressure | Test | H2F-T-001 | TBD |
| Flow rate capability | Test | H2F-T-003 | TBD |
| Leak detection response | Test | H2L-T-001, H2L-T-002 | TBD |
| Safety interlock timing | Test | H2S-T-001 | TBD |
| Emergency shutoff | Test | H2F-T-004 | TBD |

### 6.2 Integration Test Plan

1. **H₂ Flow Test**: Verify supply pressure, flow rate, and purity
2. **Leak Detection Test**: Inject calibration gas, verify alarm and response
3. **Safety Interlock Test**: Simulate fault conditions, verify shutoff
4. **Emergency Shutoff Test**: Verify <2 second closure from command
5. **Pressure Regulation Test**: Verify ±0.5 bar regulation under varying load

---

## 7. Operations and Maintenance

### 7.1 Ground Servicing
- H₂ ground supply cart interface (compatible with aircraft fittings)
- Purge procedure before and after H₂ operations
- Leak check after every connection/disconnection

### 7.2 Safety Procedures
- Ground safety pin must be installed when H₂ system is being serviced
- Personnel training required for H₂ handling
- Fire extinguishing equipment (Class D for H₂ fires) must be available

---

## 8. Cross-References

### 8.1 Related ICDs
- ICD-24/27/42-61 — Propulsion to Avionics
- ICD-54-61 — Propulsion to Structure

### 8.2 Detailed Interface Specifications
- 61-00-05-04_Hydrogen_System_Interfaces (all documents)

---

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Integration Team | Initial release |

---

← [Previous: 61-00-05-06-02A_ICD_Propulsion_to_Avionics](61-00-05-06-02A_ICD_Propulsion_to_Avionics.md) · [Next: 61-00-05-06-04A_ICD_Propulsion_to_Structure](61-00-05-06-04A_ICD_Propulsion_to_Structure.md) →

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
