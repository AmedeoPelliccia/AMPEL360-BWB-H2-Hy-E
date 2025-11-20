# 02-20-15 — Flight Planning Integration

**Subsystem ID:** 02-20-15_Flight_Planning_Integration  
**Parent Group:** 02-20 Turnaround & Ground Ops Coordination  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / WORKING  

---

## 1. Purpose

02-20-15 defines how **Ground Ops Management (02-20-14)** interacts with:

- **Flight Planning systems (FPL)**  
- **ATFM / slot management** (CTOT, regulations)  
- **Dispatch & OCC tools**  
- **Predictive Ops NN (02-20-23)**

The goal is to keep **turnaround reality**, **flight plan assumptions** and **slot constraints** coherent in near-real-time, and to provide a clean interface for:

- Updating EOBT / TOBT / target off-block times based on ground truth  
- Propagating **disruptions** (e.g. GSE shortage, H₂ safety constraints) to flight planning  
- Feeding **risk scores & recommendations** into dispatch decisions  

---

## 2. Scope

### 2.1 Included

- Interfaces between **02-20-14 Ground Ops Management** and:

  - Airline flight planning / dispatch systems  
  - ATC / ATFM slot management (CTOT / regulations)  
  - Predictive Ops NN (02-20-23) for departure delay risk  

- Data models for:

  - Turnaround → FPL status mapping (EOBT, TOBT, TSAT, off-block)  
  - Delay / cause codes attributable to ground services  
  - Slot usage / infringement indicators  

- Eventing and API patterns for:

  - Pushing updated times & statuses from turnaround model  
  - Receiving FPL changes (route, cruise level, fuel, slot) and assessing impact  
  - Providing “what-if” hooks for Predictive Ops NN  

### 2.2 Excluded

- Internal algorithms of 3rd-party flight planning or ATFM tools  
- Airspace trajectory optimisation, cost index optimisers, or fuel policies  
- Aircraft performance model details (handled by performance subsystems)  

---

## 3. Key Relationships

- **02-20-14 Ground Ops Management**  
  - Provides: turnaround status, GSE constraints, H₂ safety windows, delay causes  
  - Consumes: planned off-block, slot times, dispatch decisions  

- **02-20-23 Predictive Ops NN**  
  - Consumes: historical turnaround + FPL data, realised vs planned times  
  - Provides: risk of departure delay, suggested buffers, stand/slot choices  

- **ATA 95 Neural Networks (95-xx)**  
  - Owns NN governance, traceability and assurance; 02-20-15 is the **operational interface**.  

---

## 4. Document Map

- [02-20-15-001_FPL_Integration_Overview.md](./02-20-15-001_FPL_Integration_Overview.md)  
- [02-20-15-002_Turnaround_to_FPL_Interface.md](./02-20-15-002_Turnaround_to_FPL_Interface.md)  
- [02-20-15-003_Slots_and_ATFM_Integration.md](./02-20-15-003_Slots_and_ATFM_Integration.md) 
- [02-20-15-004_FPL_Change_Propagation.md](./02-20-15-004_FPL_Change_Propagation.md)   
- [02-20-15-005_Predictive_Ops_FPL_Hooks.md](./02-20-15-005_Predictive_Ops_FPL_Hooks.md)  

Architecture & assets:

- [02-20-15-A-001_FPL_Integration_Architecture.md](./02-20-15-A-001_FPL_Integration_Architecture.md)  
- `ASSETS/02-20-15-A-001_FPL_Integration_Architecture.svg` *(future diagram)*  

Test data:

- [TEST_DATA/02-20-15-T-001_FPL_Delay_Scenarios.json](./TEST_DATA/02-20-15-T-001_FPL_Delay_Scenarios.json)  

---

## 5. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Subsystem:** 02-20-15 Flight Planning Integration  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  

| Version | Date       | Author / Team                         | Notes                                |
| ------- | ---------- | ------------------------------------- | ------------------------------------ |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Dispatch WG    | Initial subsystem README (skeleton). |
