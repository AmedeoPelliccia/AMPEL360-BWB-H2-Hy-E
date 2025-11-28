# 53-80-00-04 — Energy System Safety Requirements

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-00-04 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / SAFETY |

---

## 1. Purpose

This document defines the safety requirements for the 53-80 Energy systems, derived from the System Safety Assessment (SSA) and Functional Hazard Assessment (FHA). These requirements ensure the energy distribution and management systems meet aviation safety standards per CS-25.1309 and DO-178C/DO-254.

## 2. Safety Objectives

### 2.1 Primary Safety Goals

| Goal ID | Statement | Criticality |
|---------|-----------|-------------|
| SG-NRG-001 | Prevent electrical fire or arc flash | Hazardous |
| SG-NRG-002 | Prevent battery thermal runaway | Hazardous |
| SG-NRG-003 | Maintain essential power for flight | Major |
| SG-NRG-004 | Prevent uncontrolled energy release | Hazardous |
| SG-NRG-005 | Enable safe shutdown in emergency | Major |

### 2.2 Safety Classification Summary

| System | Function | Failure Condition | Classification |
|--------|----------|-------------------|----------------|
| HVDC distribution | Power routing | Complete loss | Major |
| HVDC protection | Fault isolation | Failure to trip | Hazardous |
| Thermal cooling | Battery TMS | Loss of cooling | Hazardous |
| Thermal protection | Over-temp cutoff | Failure to respond | Hazardous |
| Energy management | Optimization | Incorrect commands | Minor |

## 3. Electrical Safety Requirements

### 3.1 Arc Flash Prevention

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-E-001 | HVDC conductors shall be fully insulated with no exposed terminals in accessible areas | Inspection |
| SR-E-002 | All HVDC connection points shall have arc-resistant enclosures rated for prospective fault current | Test |
| SR-E-003 | Bus protection shall clear faults within 10 ms to limit arc energy | Test |
| SR-E-004 | Maintenance access points shall require deliberate de-energization sequence | Procedure |
| SR-E-005 | Arc flash boundary shall be marked on all HVDC equipment | Inspection |

### 3.2 Ground Fault Protection

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-E-010 | Ground fault detection shall operate at ≤ 30 mA threshold | Test |
| SR-E-011 | Ground fault trip time shall be < 50 ms | Test |
| SR-E-012 | Ground fault location shall be indicated to crew | Demonstration |
| SR-E-013 | TN-S grounding scheme shall be implemented throughout | Design review |
| SR-E-014 | Insulation monitoring shall provide continuous protection | Analysis |

### 3.3 Overcurrent Protection

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-E-020 | Each load channel shall have dedicated SSCB protection | Inspection |
| SR-E-021 | SSCBs shall trip within 1 ms for instantaneous overcurrent | Test |
| SR-E-022 | Protection selectivity shall ensure only faulted section trips | Analysis |
| SR-E-023 | I²t let-through shall be below conductor damage threshold | Calculation |
| SR-E-024 | SSCB status shall be annunciated to crew | Demonstration |

### 3.4 Galvanic Isolation

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-E-030 | HVDC to 28V circuits shall have 2500 VDC isolation | Test |
| SR-E-031 | Control signals crossing voltage boundaries shall be optically isolated | Design review |
| SR-E-032 | Isolation barrier shall withstand 2× peak voltage + 1000V | Test |

## 4. Thermal Safety Requirements

### 4.1 Battery Thermal Protection

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-T-001 | Battery cooling shall maintain cell temperature < 45°C in all conditions | Test |
| SR-T-002 | Dual redundant temperature sensors per battery module | Inspection |
| SR-T-003 | Loss of cooling shall trigger load reduction within 1 second | Test |
| SR-T-004 | Thermal runaway containment shall limit propagation to one module | Test |
| SR-T-005 | Battery isolation shall be automatic if ΔT > 5°C between cells | Test |

### 4.2 Coolant System Protection

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-T-010 | Coolant leak detection shall identify leaks > 0.1 L/min | Test |
| SR-T-011 | Coolant level low shall trigger warning at 85% volume | Test |
| SR-T-012 | Coolant over-temperature shall trigger warning at 95°C (HT) / 60°C (LT) | Test |
| SR-T-013 | Pressure relief shall activate at 4.0 bar | Test |
| SR-T-014 | Coolant shall be non-flammable per FAR 25.863 | Material test |

### 4.3 Pump Failure Protection

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-T-020 | Backup pump shall auto-start within 500 ms of primary failure | Test |
| SR-T-021 | Flow monitoring shall detect < 50% nominal flow | Test |
| SR-T-022 | Dual pump operation capability for high demand | Demonstration |
| SR-T-023 | Pump failure annunciation to crew within 2 seconds | Test |

## 5. Protection System Requirements

### 5.1 Solid State Circuit Breaker (SSCB)

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-P-001 | SSCB shall be certified to DO-160G environmental requirements | Qualification |
| SR-P-002 | SSCB failure mode shall be to trip (fail-safe) | Analysis |
| SR-P-003 | SSCB trip response time < 1 ms for short circuit | Test |
| SR-P-004 | SSCB shall have remote reset capability only | Design review |
| SR-P-005 | SSCB status monitoring shall include trip cause | Demonstration |

### 5.2 Thermal Cutoff Devices

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-P-010 | Thermal cutoffs shall be independent of control system | Inspection |
| SR-P-011 | Cutoff setpoints: HT bus 105°C, LT bus 70°C | Test |
| SR-P-012 | Thermal cutoff response time < 100 ms | Test |
| SR-P-013 | Manual reset only after investigation | Procedure |

### 5.3 Fault Detection and Isolation

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-P-020 | Fault detection coverage > 95% of failure modes | Analysis |
| SR-P-021 | Fault isolation time < 100 ms for electrical faults | Test |
| SR-P-022 | Fault annunciation to crew within 2 seconds | Demonstration |
| SR-P-023 | Fault log shall capture pre-fault conditions | Test |
| SR-P-024 | Independent fault monitors for dual-redundant systems | Inspection |

## 6. Energy Management Safety Requirements

### 6.1 Load Shedding

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-M-001 | Essential loads shall never be shed automatically | Analysis |
| SR-M-002 | Load shedding sequence shall be deterministic | Test |
| SR-M-003 | Load shedding shall be reversible (automatic restore) | Test |
| SR-M-004 | Crew override of load shedding shall be available | Demonstration |

### 6.2 Power Source Management

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-M-010 | Battery discharge limit 20% SOC minimum | Test |
| SR-M-011 | Source transfer time < 50 ms | Test |
| SR-M-012 | Automatic source isolation on reverse power | Test |
| SR-M-013 | Manual source selection capability | Demonstration |

### 6.3 Regeneration Safety

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-M-020 | Regeneration shall cease if battery cannot accept charge | Test |
| SR-M-021 | Regeneration power limit 800 kW | Test |
| SR-M-022 | Regeneration shall not interfere with flight controls | Analysis |
| SR-M-023 | Regeneration failure shall be fail-safe (no regen) | Analysis |

## 7. Monitoring and Annunciation Requirements

### 7.1 Crew Alerting

| Req ID | Alert Type | Condition | Annunciation |
|--------|------------|-----------|--------------|
| SR-A-001 | Warning | Battery over-temperature | EICAS amber |
| SR-A-002 | Warning | Coolant system degraded | EICAS amber |
| SR-A-003 | Caution | HVDC bus abnormal voltage | EICAS amber |
| SR-A-004 | Caution | SSCB tripped | EICAS amber |
| SR-A-005 | Master Warning | Thermal runaway risk | EICAS red + aural |
| SR-A-006 | Master Warning | HVDC bus failure | EICAS red + aural |

### 7.2 Built-In Test

| Req ID | Requirement | Verification |
|--------|-------------|--------------|
| SR-A-010 | Power-on BIT coverage > 80% of faults | Analysis |
| SR-A-011 | Continuous BIT for safety-critical functions | Demonstration |
| SR-A-012 | BIT failure indication within 5 seconds | Test |
| SR-A-013 | Maintenance BIT > 95% fault coverage | Analysis |

## 8. Design Assurance Requirements

### 8.1 Software (DO-178C)

| Function | DAL | Rationale |
|----------|-----|-----------|
| SSCB control logic | B | Prevents hazardous conditions |
| Thermal protection logic | B | Battery safety critical |
| EMS core algorithms | C | Mission critical |
| Monitoring/display | D | Information only |

### 8.2 Hardware (DO-254)

| Component | DAL | Rationale |
|-----------|-----|-----------|
| SSCB power electronics | B | Safety critical |
| Temperature sensors | B | Thermal protection |
| DC-DC converters | C | Power distribution |
| Current sensors | C | Protection inputs |

## 9. Traceability

### 9.1 To System Safety Assessment

| Requirement | SSA Hazard ID | Classification |
|-------------|---------------|----------------|
| SR-E-001 to SR-E-005 | HAZ-NRG-001 | Hazardous |
| SR-T-001 to SR-T-005 | HAZ-NRG-002 | Hazardous |
| SR-P-001 to SR-P-024 | HAZ-NRG-003 | Major/Hazardous |
| SR-M-001 to SR-M-023 | HAZ-NRG-004 | Major |

### 9.2 Reference Documents

- [53-00-02 Safety Assessment](../../53-00_GENERAL/53-00-02_Safety/)
- [CS-25.1309](https://www.easa.europa.eu/en/certification-specifications/cs-25-large-aeroplanes)
- [ARP 4754A](https://www.sae.org/standards/content/arp4754a/)
- [ARP 4761](https://www.sae.org/standards/content/arp4761/)

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-00-04 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Author** | AMPEL360 Safety Team |
| **Reviewer** | _[To be assigned]_ |
| **Approver** | _[To be assigned]_ |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*
