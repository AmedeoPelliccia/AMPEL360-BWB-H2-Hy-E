# 61-00-05-06-02A - ICD Propulsion to Avionics

**Document ID:** ICD-24/27/42-61 (61-00-05-06-02A)  
**Title:** Interface Control Document — Propulsion System to Avionics Systems  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Introduction

### 1.1 Purpose
This ICD defines all interfaces between the Q100 Propulsion System (ATA 61) and aircraft avionics systems including Electrical Power (ATA 24), Flight Controls (ATA 27), and Integrated Modular Avionics (ATA 42).

### 1.2 Scope
- Electrical power distribution (800 VDC bus)
- Flight control commands and feedback (AFDX, discretes)
- Health monitoring and maintenance data (ARINC 429)
- Ground support equipment interfaces

### 1.3 Applicable Documents
- 61-00-05-02-01A — Power Distribution
- 61-00-05-02-02A — Control Signals
- 61-00-05-03-01A — ARINC 429 Buses
- 61-00-05-03-02A — AFDX Networks

---

## 2. System Overviews

### 2.1 Propulsion System (ATA 61)
- Four electric ducted fan propulsors
- Propulsor Control Units (PCUs)
- Power electronics and motor controllers
- Health monitoring sensors

**Interface Responsibilities:**
- Accept electrical power and control commands
- Provide thrust output and status feedback
- Report health and maintenance data

### 2.2 Avionics Systems

#### ATA 24 — Electrical Power
- 800 VDC power generation and distribution
- Power quality management
- Ground fault detection

**Interface Responsibilities:**
- Provide 800 VDC power (up to 4.5 MW per propulsor)
- Manage power bus quality and protection

#### ATA 27 — Flight Controls
- Flight Control Computers (FCCs)
- Pilot command inputs
- Thrust management algorithms

**Interface Responsibilities:**
- Generate thrust commands
- Receive propulsor status and feedback
- Manage differential thrust for control

#### ATA 42 — Integrated Modular Avionics
- AFDX network switches
- Data concentrators
- Central Maintenance Computer (CMC)

**Interface Responsibilities:**
- Provide AFDX network infrastructure
- Collect and process health/maintenance data

---

## 3. Interface Summary

| Interface Type | Direction | Specification Reference | Criticality |
|----------------|-----------|-------------------------|-------------|
| 800 VDC Power | Avionics → Propulsion | 61-00-05-02-01A | Safety-critical |
| Thrust Commands (AFDX) | Avionics → Propulsion | 61-00-05-03-02A | Safety-critical |
| Propulsor Status (AFDX) | Propulsion → Avionics | 61-00-05-03-02A | Critical |
| Discrete Commands | Avionics → Propulsion | 61-00-05-02-02A | Safety-critical |
| Discrete Status | Propulsion → Avionics | 61-00-05-02-02A | Critical |
| Health Data (ARINC 429) | Propulsion → Avionics | 61-00-05-03-01A | Important |
| Maintenance Data (ARINC 429) | Propulsion → Avionics | 61-00-05-03-01A | Non-critical |

---

## 4. Key Interface Requirements

### 4.1 Electrical Power Interface (ATA 24 ↔ ATA 61)

| Requirement | Propulsion Responsibility | Avionics Responsibility |
|-------------|---------------------------|-------------------------|
| Voltage | Accept 800 ±10% VDC | Provide 800 ±10% VDC |
| Power | Draw ≤4.5 MW continuous | Supply ≥4.5 MW per propulsor |
| Power Factor | Maintain >0.95 | — |
| Fault Detection | Report ground faults | Detect and isolate ground faults |

### 4.2 Flight Control Interface (ATA 27 ↔ ATA 61)

| Requirement | Propulsion Responsibility | Flight Control Responsibility |
|-------------|---------------------------|-------------------------------|
| Thrust Command | Execute within 100 ms | Send at 100 Hz via AFDX VL-6101 |
| Thrust Feedback | Report actual thrust at 100 Hz | Monitor and close loop |
| Emergency Shutdown | Respond within 10 ms | Send hardwired discrete + AFDX |
| Differential Thrust | Provide per-propulsor control | Coordinate for yaw/roll control |

### 4.3 Data Network Interface (ATA 42 ↔ ATA 61)

| Requirement | Propulsion Responsibility | IMA Responsibility |
|-------------|---------------------------|---------------------|
| AFDX End System | Comply with ARINC 664 Part 7 | Provide dual-redundant AFDX switches |
| Virtual Link Allocation | Respect BAG and bandwidth limits | Allocate VLs per network design |
| Health Data | Transmit via VL-6121 at 32 ms BAG | Route to Health Monitoring Computer |
| Maintenance Data | Transmit via A429 Label 102 | Route to CMC |

---

## 5. Physical Interface Locations

### 5.1 Connector Locations

| Interface | Location (Aircraft Reference) | Propulsion Side Connector | Avionics Side Connector |
|-----------|-------------------------------|---------------------------|-------------------------|
| Power (Propulsor 1) | Nacelle 1, Station 450 | MIL-DTL-38999/25 (female) | MIL-DTL-38999/25 (male) |
| AFDX Network A (Prop 1-4) | Avionics bay, Rack 2 | RJ-45 (propulsor end) | RJ-45 (switch port) |
| ARINC 429 TX-A (Prop 1) | Avionics bay, Rack 3 | MIL-DTL-38999/11 (female) | MIL-DTL-38999/11 (male) |
| Discrete I/O (Prop 1) | Nacelle 1, Station 470 | MIL-DTL-38999/17 (female) | MIL-DTL-38999/17 (male) |

---

## 6. Verification and Validation

### 6.1 Interface Verification Matrix

| Interface | Verification Method | Test Reference | Status |
|-----------|---------------------|----------------|--------|
| Power quality | Test | PWR-T-002 | TBD |
| Thrust command latency | Test | AFDX-T-002 | TBD |
| Discrete signal timing | Test | CTL-T-003 | TBD |
| AFDX VL compliance | Analysis + Test | AFDX-T-004 | TBD |
| Health data accuracy | Test | SEN-T-001 through SEN-T-006 | TBD |

### 6.2 Integration Test Plan

1. **Power-On Test**: Verify 800 VDC power delivery and propulsor acceptance
2. **Control Loop Test**: Verify thrust command/feedback loop performance
3. **Network Test**: Verify AFDX and ARINC 429 data transmission
4. **Redundancy Test**: Verify failover behavior for dual-redundant interfaces
5. **Emergency Procedures Test**: Verify emergency shutdown and fault handling

---

## 7. Operations and Maintenance

### 7.1 Ground Support Equipment
- Propulsor Test Set (PTS) interfaces via same connectors
- Diagnostic software access via AFDX network (ground mode)
- Power supply: 800 VDC ground power cart

### 7.2 Troubleshooting
- Use CMC Built-In Test (BIT) for fault isolation
- Monitor AFDX network traffic with protocol analyzer
- Check discrete signal status with multimeter/oscilloscope

---

## 8. Cross-References

### 8.1 Related ICDs
- ICD-28-61 — Propulsion to Fuel System
- ICD-54-61 — Propulsion to Structure

### 8.2 Detailed Interface Specifications
- 61-00-05-02_Electrical_Interfaces (all documents)
- 61-00-05-03_Data_Interfaces (all documents)

---

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Integration Team | Initial release |

---

← [Previous: 61-00-05-06-01A_ICD_Template](61-00-05-06-01A_ICD_Template.md) · [Next: 61-00-05-06-03A_ICD_Propulsion_to_Fuel_System](61-00-05-06-03A_ICD_Propulsion_to_Fuel_System.md) →

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
