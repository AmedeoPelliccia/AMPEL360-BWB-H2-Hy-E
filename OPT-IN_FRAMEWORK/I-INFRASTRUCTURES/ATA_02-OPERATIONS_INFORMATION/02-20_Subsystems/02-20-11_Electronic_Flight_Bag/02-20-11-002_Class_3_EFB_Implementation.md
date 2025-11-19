# 02-20-11-002 — Class 3 EFB Implementation

**Subsystem ID:** 02-20-11
**Group:** [02-20_Subsystems](../README.md)
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)
**Axis:** I — Infrastructures
**Status:** OPERATIONAL
**Version:** 1.0

---

# 1. Purpose

This document defines the **Class 3 / Portable Electronic Flight Bag (EFB) implementation** used in AMPEL360 aircraft operations.

It details:

* Hardware platform
* Mounting & installation
* Electrical integration
* Connectivity architecture
* Operational constraints
* Environmental & EMC considerations
* Class 3 compliance with AC 120-76D / AMC 20-25
* Maintenance, update, and safety boundaries

It complements:
→ `02-20-11-001_EFB_Overview.md`

---

# 2. Scope

## Included

* Device architecture (iPad Pro 12.9” baseline)
* Certified cockpit mounting solution
* Power supply & charging logic
* Data connectivity (WiFi, LTE, wired)
* Environmental specification and testing
* Equipment qualification summary
* Operational constraints for Class 3 use
* Integration with 02-20-01 Digital Ops Platform, ATA 42, and AOC

## Excluded

* Airline-specific MDM configuration
* Ground connectivity infrastructure
* Software application architecture (see `02-20-11-001`)
* Internal ATA 42 avionics details beyond interface boundaries

---

# 3. Class 3 EFB Definition (Regulatory Basis)

### FAA

* **AC 120-76D** — EFB, Class 3 Portable, Type B
* **OpSpec A061** — Required for airline authorization

### EASA

* **AMC 20-25** — EFB, Portable / Class 2–3
* **Part-OPS SPA.EFB.xxx** — Operational requirements

### Characteristics of Class 3 EFBs

* Mounted in cockpit on **certified bracket**
* Powered **from aircraft electrical power**
* Connected to aircraft **data networks** (non-safety-critical)
* Must pass DO-160 environmental tests (vibration, temperature, EMI)
* No authority over safety-critical avionics
  → *Advisory only*

---

# 4. Hardware Architecture

## 4.1 Device Specification (Baseline)

| Component        | Specification                |
| ---------------- | ---------------------------- |
| Model            | iPad Pro 12.9” (M2 or later) |
| CPU/GPU          | Apple Silicon (≥ M2)         |
| Display          | 2732 × 2048, anti-glare      |
| Storage          | 256–512 GB NVMe              |
| Connectivity     | WiFi 802.11ac, LTE optional  |
| Battery          | 40.8 Wh integrated           |
| Operating System | iPadOS (Hardened profile)    |
| Physical Buttons | Minimal — mounted for safety |

### Remarks:

* Device is considered **Portable + Permanently Mounted** for Class 3.
* All operational apps must run in **airline-approved EFB mode**.

---

## 4.2 Protective Exterior

* High-impact polymer shell
* Anti-slip backplate
* Fire-retardant per **FAR 25.853(a)**
* Anti-reflective display film
* Operational tolerance for gloves (flight crew)

---

# 5. Mounting & Installation

## 5.1 Cockpit Mount Requirements

Standard references:

* **DO-160G**, Sections 4–8, 16, 20–21
* **AC 120-76D** mounting criteria
* **AMC 20-25** human factors

### Mount Characteristics

| Requirement   | Value                           |
| ------------- | ------------------------------- |
| Design        | Quick-release, single-hand      |
| Vibration     | DO-160G Cat S compliant         |
| Impact        | Survive 9g forward acceleration |
| Viewing angle | Adjustable 20–60°               |
| Glare control | Verified during HF testing      |
| Locking       | Mechanical & friction-based     |

### Placement Guidelines

* Must not obstruct primary flight displays (PFD/ND)
* Must not interfere with flight controls
* Must allow full side-stick movement
* Must be reachable with restraints fastened

---

## 5.2 Cabling & Connectors

* Power cable: **USB-C to certified 28V DC adaptor**
* Data connection (optional):

  * USB-C to Ethernet
  * USB-C to maintenance bus
* Cable routing:

  * Must not interfere with flight controls
  * Strain-relief required on both ends
  * Fire-resistant conduits recommended

---

# 6. Electrical Integration

## 6.1 Power Supply

EFBs receive aircraft power from:

```
28V DC BUS → DC-DC Converter (5V/3A USB-C PD) → EFB Device
```

Design constraints:

* Converter must be DO-160 compliant
* Over-current protection: ≤ 3.5 A
* Over-temperature shutdown
* EMI shielding required near avionics harnesses

## 6.2 Charging Logic

* EFBs are **fully charged** on ground before flight
* During flight:

  * Powered continuously for longevity
  * Battery used only as short-term fallback
* Charging prohibited during:

  * Critical phases (takeoff/landing) if mandated by airline
  * Specific MEL/CDL conditions

---

# 7. Connectivity Architecture

```
            ┌──────────────────────────┐
            │       Electronic         │
            │     Flight Bag (EFB)     │
            └───────┬──────────┬───────┘
                    │          │
        ┌───────────▼───┐  ┌───▼───────────┐
        │  WiFi 802.11ac │  │  USB-C (opt)  │
        └───────────┬────┘  └──────┬────────┘
                    │              │
       ┌────────────▼──────────────▼──────────┐
       │      Aircraft / AOC Interfaces        │
       │   (ATA 42 IMA, Maintenance Bus,       │
       │    Ground WiFi, Dispatch Systems)     │
       └───────────────────────────────────────┘
```

## 7.1 Wireless Connectivity

* Ground WiFi (updates, sync, document downloads)
* Cockpit WiFi (via IMA or approved AP)
* WPA3-Enterprise + VPN
* Latency target: < 500 ms

## 7.2 Wired Connectivity (Optional)

* Maintenance bus (read-only)
* Ethernet via USB-C dongle
* Restriction: no avionics command paths

---

# 8. Environmental & EMC Considerations

### DO-160 Qualification Summary

| Section           | Category          |
| ----------------- | ----------------- |
| Temperature       | B2                |
| Vibration         | S                 |
| EMI/EMC           | R                 |
| Fluids            | F                 |
| Fire/Flammability | A                 |
| Pressure          | D                 |
| Humidity          | B                 |
| Crash Safety      | Conforms to mount |

### Operational Envelope

* Operating temperature: 0–40°C
* Storage temperature: –20 to +45°C
* Altitude: Up to flight deck altitude (pressurized)
* Lighting: Compatible with NVIS cockpit environments

---

# 9. Operational Constraints (Class 3 EFB)

* EFB must **not** exert control over any safety-critical system
* Must remain **available** during all flight phases
* Must be **secured** at all times (no loose equipment risk)
* Must allow crew to:

  * Quickly remove/replace
  * Operate under turbulence
  * Read under sunlight conditions
* Must integrate into operator MEL policies
* Must support **pilot workflows** covered in:
  → `../../02-10_Operations/`

---

# 10. Integration with Other Subsystems

## 10.1 Digital Ops Platform (02-20-01)

* API client (REST/events)
* Document updates
* CAOS advisory ingestion
* KPI/event reporting

## 10.2 Performance Computer (02-20-13)

* Receives performance outputs
* Provides BWB/H₂-aware UI
* Hosts fallback calculations

## 10.3 Weight & Balance (02-20-12)

* Displays CG limits & H₂ dynamics
* Manages cargo/pax interactions

## 10.4 Weather Information System (02-20-17)

* Consumes graphical weather data
* Displays turbulence predictions

## 10.5 Predictive Ops NN (02-20-23)

* Displays delay/turnaround risk levels
* Shows CAOS-generated advisories

---

# 11. Security Considerations

* Mandatory MDM (Mobile Device Management)
* Mandatory encryption (AES-256)
* Secure boot & signed updates
* No sideloading or jailbroken devices
* Continuous monitoring (MDM + CAOS)
* DO-326A alignment
* Crew authentication:

  * Biometric + PIN

---

# 12. Maintenance & Update Workflow

### Software Updates

* Delivered via ground WiFi
* Versioning controlled by Digital Ops Platform
* Rollback supported via local snapshot

### Hardware Maintenance

* Annual mount inspection
* Power converter check every 800 flight hours
* Battery replacement every 24–36 months

### MEL/CDL Items

* 1 EFB inoperative = allowed with restrictions
* Dual inoperative = dispatch prohibited (unless alternate procedures exist)

---

# 13. Traceability

## Requirements

* RQ-02-20-11-A — Class 3 mounting
* RQ-02-20-11-B — Power integration
* RQ-02-20-11-C — Connectivity requirements
* RQ-02-20-11-D — Environmental tests

## Design

* 02-20-11-A-003 Class 3 Integration Diagram
* 02-20-11-A-001 System Architecture

## Interfaces

* ATA 42 (avionics)
* 02-20-01 Digital Ops Platform
* AOC / Dispatch

## Certification

* DO-160G tests
* AC 120-76D / AMC 20-25 compliance
* DO-326A cybersecurity

---

# 14. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-11 Electronic Flight Bag
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Guidelines

| Version | Date       | Author               | Changes                            |
| ------- | ---------- | -------------------- | ---------------------------------- |
| 1.0     | 2025-11-19 | AMPEL360 Digital Ops | Initial Class 3 EFB Implementation |

---
