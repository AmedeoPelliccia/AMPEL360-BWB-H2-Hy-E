# 02-20-11-008 — Integration with ATA 42 (IMA / Avionics Data Interface)

**Subsystem ID:** 02-20-11  
**Group:** [02-20_Subsystems](../README.md)  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Function:** Avionics Data Interface (Read-Only)  
**Status:** OPERATIONAL  
**Version:** 1.0  

---

## 1. Purpose

This document defines the **interface between the Electronic Flight Bag (EFB)** and  
**ATA 42 — Integrated Modular Avionics (IMA)**, including:

- Data types and update rates  
- Communication media (WiFi, Ethernet/USB-C)  
- Allowed vs restricted data flows  
- Read-only boundaries to ensure certification  
- Integrity, security, and fallback modes  
- Integration with performance, W&B, weather, and charts modules  

It complements:

- `02-20-11-001_EFB_Overview.md`  
- `02-20-11-004_Performance_Calculations.md`  
- `02-20-11-005_Weight_Balance_Module.md`  
- `02-20-11-007_Charts_Navigation_Data.md`  

---

## 2. Scope

### Included
- Read-only avionics data delivered to the EFB  
- Protocols used (ARINC 763 over secure WiFi, optional wired link)  
- Data validation, coherency checks, and filtering  
- Integration with various EFB submodules  

### Excluded
- Safety-critical avionics functions  
- Flight-control-level data paths  
- Write access to any avionics bus  
- Internal ATA 42 architecture  

EFB is **strictly advisory** with **no authority** over aircraft systems.

---

## 3. Architecture Overview

```

```
                   ┌────────────────────────────┐
                   │        ATA 42 IMA          │
                   │  (Aircraft Avionics Core)   │
                   └───────────▲────────────────┘
                               │
                ARINC 763 / Secure WiFi Interface
                               │
 ┌─────────────────────────────┴──────────────────────────────┐
 │                  EFB AVIONICS INTERFACE                     │
 │                                                             │
 │    ┌─────────────┬──────────────┬──────────────┬──────────┐│
 │    │ Performance │  W&B Module  │ Weather Sys   │ Charts   ││
 │    │ 02-20-11-004│ 02-20-11-005 │ 02-20-11-006  │ 02-20-11-007 │
 │    └─────────────┴──────────────┴──────────────┴──────────┘│
 │                                                             │
 └─────────────────────────────────────────────────────────────┘
```

```

Data flows **one-way** from ATA 42 → EFB.

---

## 4. Data Provided to the EFB via ATA 42

### 4.1 Aircraft State Parameters

| Parameter | Rate | Purpose |
|-----------|------|---------|
| GPS position | 1–5 Hz | Georeferencing charts, routing |
| Ground speed | 1–10 Hz | Performance calculations |
| True airspeed | 1–10 Hz | Performance, weather |
| Pressure altitude | 1–10 Hz | Density altitude |
| Indicated altitude | 1–10 Hz | Backup reference |
| Vertical speed | 1–10 Hz | Climb/descent prediction |
| Attitude (pitch/roll) | 10 Hz | Rendering orientation |
| Heading (mag/true) | 1–10 Hz | Navigation overlays |

---

### 4.2 Aircraft Configuration Status

| Parameter | Use |
|-----------|-----|
| Flaps/slats position | TO/LND performance |
| Spoiler state | Rejected takeoff logic |
| Gear extended/retracted | Phase-of-flight detection |
| Anti-ice ON/OFF | Performance corrections |
| Weight-on-wheels | TO/LND validity |

---

### 4.3 Engine / Propulsor Parameters (Advisory Only)

- Power lever angle  
- N1 / Np / torque metrics  
- Electrical load (for performance corrections if required)  

---

### 4.4 Fuel System Data (Forwarded from ATA 28)

Handled via ATA 42 interface:

| Parameter | Purpose |
|-----------|---------|
| H₂ tank quantity | CG + TOW accuracy |
| Tank temperature | Cryogenic density |
| Tank pressure | Health monitoring |
| Active tank | Sequencing effects |
| H₂ boil-off rate (processed) | W&B / performance |

These values feed:

- `02-20-11-005_Weight_Balance_Module.md`  
- `02-20-11-004_Performance_Calculations.md`

---

## 5. Protocols & Connectivity

### 5.1 Wireless (Primary)

**ARINC 763 over WPA3-Enterprise + VPN**

Advantages:

- Certified Class 3 EFB path  
- Low latency (<500 ms)  
- No access to safety-critical networks  

### 5.2 Wired (Optional / Maintenance)

- USB-C → Ethernet tether  
- Read-only restricted firewall rules  
- Used mainly for operator-specific workflows  

---

## 6. Data Validation & Filtering

### 6.1 Validation Pipeline

```

ATA 42 IMA
│
▼
Raw Data Packet
│ Validation:
│ - checksum
│ - signature
│ - coherence
│ - timestamp window
▼
Accepted & Filtered Data
│
▼
EFB Submodules

```

### 6.2 Coherency Checks

- Reject impossible transitions (e.g., sudden CG change)  
- Block stale or non-timestamped data  
- Compare GPS vs IRS drift  

---

## 7. Integration with EFB Submodules

### 7.1 Performance Module (02-20-11-004)

Uses:

- Flap/slat setting  
- Engine performance state  
- Anti-ice  
- Pressure altitude  
- SAT/TAT  
- Aircraft speed and heading  

Determines:

- V1/VR/V2  
- Runway length required  
- Climb gradient  

---

### 7.2 Weight & Balance Module (02-20-11-005)

Uses:

- WOW state  
- H₂ tank levels (routed through ATA 42)  
- Fuel temperature/pressure  
- Aircraft configuration  

Determines:

- CG status  
- Predicted CG drift  
- Cross-check with load sheet  

---

### 7.3 Weather Integration (02-20-11-006)

Uses:

- Aircraft position  
- Altitude (multiple sources)  
- SAT/TAT  
- Heading & speed  

Feeds:

- Weather overlays  
- Predictive turbulence (NN)

---

### 7.4 Charts & Navigation (02-20-11-007)

Uses:

- GPS or blended position  
- Heading  
- Ground speed  

Supports:

- Georeferenced charts  
- Runway/taxi guidance  
- Enroute navigation  

---

## 8. Safety, Access Restrictions & Cybersecurity

### 8.1 Safety Boundaries

EFB is:

- **Strictly read-only**  
- **Non-flight-critical (DAL D)**  
- **No authority** over avionics or flight controls  
- **No command paths** into ATA 42 or ATA 28  
- **Advisory only**  

### 8.2 Cybersecurity Controls

- WPA3 + VPN  
- Certificate-based authentication  
- Packet signing  
- Time-window validation  
- Message replay prevention  
- DO-326A / ED-202A compliant  
- Tamper detection and logging  

---

## 9. Failure Modes & Fallback

### 9.1 Loss of Avionics Data

Fallback:

- Cached values (short-term only)  
- Manual input prompts (for performance module)  
- Restricted-function mode  

### 9.2 Invalid / Corrupted Data

- Discard packet  
- Warn crew  
- Trigger fallback (deterministic mode)  
- Log to `02-20-18_Operational_Data_Recording`  

### 9.3 Loss of WiFi Link

- Switch to LTE (operator optional)  
- Reduced update rate  
- Loss of georeferencing if position unavailable  

---

## 10. Traceability

### Requirements

- RQ-02-11-ATA42-001 — EFB shall receive avionics data via secure read-only channel  
- RQ-02-11-ATA42-002 — EFB shall not send commands to avionics systems  
- RQ-02-11-ATA42-003 — All avionics data shall be verified and filtered  
- RQ-02-11-ATA42-004 — EFB shall degrade gracefully on data loss  

### Design

- 02-20-11-A-001 EFB Architecture  
- ATA 42 Avionics Interface Overview  

### Interfaces

- ATA 42 IMA  
- ATA 28 Fuel System (via ATA 42)  
- 02-20-11 Performance / W&B / Charts / Weather modules  

---

## 11. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Subsystem:** 02-20-11 Electronic Flight Bag  
> **Function:** ATA 42 Integration  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  

| Version | Date | Author | Changes |
|--------|------|--------|---------|
| 1.0 | 2025-11-19 | AMPEL360 Digital Ops | Initial interface specification |

```
