# 02-20-12-001 — Weight & Balance System Overview

**Document ID:** 02-20-12-001_WB_System_Overview  
**Subsystem ID:** 02-20-12 — Weight & Balance Computer (WBC)  
**Group:** [02-20_Subsystems](../README.md)  
**Parent ATA:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Status:** DRAFT / PLACEHOLDER  
**Owner:** Digital Operations & Aircraft Performance Domain  

---

## 1. Purpose

This document provides the **system-level overview** for the **Weight & Balance Computer (WBC)** of the AMPEL360 program.

The WBC is the **authoritative source of aircraft mass, CG and loading state** used by:

- [02-20-11_Electronic_Flight_Bag](../02-20-11_Electronic_Flight_Bag/) for **operational W&B**  
- [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/) for **performance calculations**  
- CAOS / analytics (02-20-01 Digital Ops Platform) for **fleet-level analysis and optimization**  

The document:

- Defines the **role and boundaries** of the WBC  
- Summarizes its **key functions**, data flows and integration points  
- Provides input to **requirements, design and V&V** documents in the 02-20-12 subsystem  

---

## 2. Scope

### 2.1 Included

The Weight & Balance Computer covers:

- **Mass & CG computation** for all AMPEL360 variants (Q80/Q100/Q120), including:
  - Basic empty mass (BEM) and operating mass  
  - Payload loading (pax, cargo, special loads)  
  - Fuel / H₂ / auxiliary energy masses (tanks, CO₂ battery where relevant)  

- **Envelope management**:
  - Operational **CG envelopes** (taxi, takeoff, landing, in-flight)  
  - **Mass limits** (MTOW, MLW, MZFW, MRW, etc.) per aircraft configuration  
  - **Per-compartment / per-zone** loading constraints  

- **Loading workflow support**:
  - Input of **planned loads** (pax, baggage, cargo, fuels, H₂)  
  - Computation of **final loadsheet** values  
  - “What-if” and **redistribution** checks  

- **Interfaces to other 02-20 subsystems**:
  - [02-20-11_Electronic_Flight_Bag](../02-20-11_Electronic_Flight_Bag/)  
  - [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/)  
  - 02-20-01 Digital Ops Platform / CAOS  

- **Traceable computation**:
  - Deterministic, repeatable logic in accordance with AFM / WBM  
  - Optional NN-assisted estimation for **missing / noisy inputs**, with deterministic fallback  

### 2.2 Excluded

- In-flight **flight control laws** or automatic trim management (ATA 27/ATA 95)  
- Detailed **fuel / H₂ system hardware** design (ATA 28)  
- Cabin layout / seat map design (handled in cabin / interiors documentation)  
- Ground handling procedures and loading instructions editorial content  
  (covered by Ops / S1000D material under 02-xx-11_OPERATIONS_MAINTENANCE)  

---

## 3. System Context

At a high level, the WBC sits between **loading inputs**, **aircraft configuration data**, and **downstream consumers** that need **mass & CG**.

- **Upstream inputs**:
  - Flight plan & route (from 02-20-01 Digital Ops Platform)  
  - Passenger and baggage manifests  
  - Cargo manifests and special loads  
  - Fuel / H₂ loading plans and tank configurations  
  - Aircraft configuration & mod status (AFM / WBM baseline data)  

- **Core WBC functions**:
  - Transform loading data into a **mass item list**  
  - Compute **total mass, CG and inertia** at key phases:
    - Ramp / taxi  
    - Takeoff  
    - Top-of-climb, en-route, approach  
    - Landing and block-in  
  - Validate against **envelopes and structural limits**  
  - Produce structured **outputs** for EFB, performance, CAOS and recording  

- **Downstream consumers**:
  - **EFB**: W&B module, final loadsheet, crew-facing messages  
  - **Performance Computer**: takeoff / landing / cruise performance inputs  
  - **CAOS & analytics**: fleet-level mass distributions, loading statistics  
  - **Recording / ATA 31**: W&B parameters for post-flight analysis  

---

## 4. Key Functional Capabilities

### 4.1 Mass & CG Computation

- Maintain a **canonical representation of mass items**:
  - BEM and standard items  
  - Variable payload (pax + cabin baggage, checked baggage, cargo)  
  - Fuel / H₂ / CO₂ battery / other energy storage masses  
- Compute:
  - **Ramp mass**, **taxi mass**, **takeoff mass (TOW)**  
  - **Zero fuel mass (ZFW)**, **landing mass (LW)**  
  - Corresponding **CG (%MAC)** and, where required, inertia estimates  

- Support:
  - Multiple **loading scenarios** per flight (e.g. alt loads for disruption handling)  
  - Optional **auto-balancing** proposals (e.g. suggest cargo relocation to get CG closer to optimum)  

### 4.2 Envelope Checks

- Enforce aircraft **mass limits** as defined in AFM / certification data:
  - MRW, MTOW, MLW, MZFW, max/min taxi mass, etc.  
- Check **CG envelopes** for:
  - Ground configurations (taxi, takeoff, landing)  
  - Flight phases (cruise CG ranges, maneuver CG limits)  
- Handle:
  - **Hydrogen-specific CG behavior** (tank depletion, transfer strategies)  
  - BWB-specific **wide CG sensitivity** (distribution across multiple center / wing tanks and payload zones)  

### 4.3 Tank & Energy Integration (H₂ / CO₂ Battery)

In coordination with **ATA 28** and hybrid energy documentation:

- Model **H₂ tank groups**:
  - Center body tanks  
  - Outboard / wing tanks  
  - Reserve / buffer tanks (if applicable)  
- Provide:
  - Mass and CG contributions per tank / group  
  - Time- or segment-based evolution (for interface with 02-20-13 / ATA 10-xx hybrid storage)  
- Optionally:
  - Track **CO₂ battery mass**, if non-negligible for CG / inertia  
  - Provide simple estimates of **CG drift** due to energy transfer and H₂ consumption  

### 4.4 Integration with Performance Computer

The WBC provides **authoritative W&B inputs** to [02-20-13_Performance_Computer](../02-20-13_Performance_Computer/):

- **Per phase / computation request**:
  - TOW, LW, ZFW  
  - CG (%MAC) at requested phase  
  - Mass breakdown (payload vs energy vs structure)  
  - Optional inertia proxies for advanced models  

The Performance Computer uses this to:

- Compute **V-speeds**, distances, and margins (takeoff & landing)  
- Incorporate **CG-dependent aero & stability effects** (via 02-20-13-006 BWB models)  
- Evaluate **hybrid envelope** (power / thermal margins vs weight & CG)  

### 4.5 EFB Workflow Support

For [02-20-11_Electronic_Flight_Bag](../02-20-11_Electronic_Flight_Bag/):

- Provide **interactive loading workflow** support:
  - Entry of flight plan, fuel / H₂, payload  
  - Real-time feedback on mass & CG, warnings, and loadsheet completeness  
- Generate:
  - **Preliminary** and **final** W&B computations  
  - Structured **loadsheet outputs** for flight crew and ground handling  
- Interface with:
  - Airline / ground systems via 02-20-01 where integrated  

### 4.6 AI / NN-Assisted Estimation (Optional)

Where enabled and governed by ATA 95:

- Use **NN models** to assist with:
  - Estimating **actual payload distributions** from historical patterns  
  - Inferring **missing or noisy inputs** (e.g., baggage distribution by hold)  
- Always:
  - Maintain a **deterministic baseline** that is sufficient on its own  
  - Treat NN outputs as **bounded corrections / suggestions**, never the sole source of truth  
  - Log all NN usage and guardrail actions for traceability (ATA 95 & ATA 31)  

---

## 5. Data & Interfaces

### 5.1 Upstream Data

Examples (non-exhaustive):

- **Flight / Ops**:
  - Flight plan ID, route, alternate(s)  
  - Scheduled/actual block times (for CAOS correlation)  

- **Payload**:
  - Pax count per cabin section and seat group  
  - Baggage / cargo weight per compartment  
  - Special items (live animals, outsized cargo, dangerous goods tags)  

- **Energy**:
  - Fuel / H₂ loading per tank or tank group  
  - CO₂ battery SoC / mass, if modeled  

### 5.2 Downstream Interfaces

- **To EFB (02-20-11)**:
  - W&B summary for crew display  
  - Loadsheets and advisory messages  

- **To Performance Computer (02-20-13)**:
  - Structured JSON / message format with:
    - TOW, LW, ZFW, CG, breakdowns  
    - Configuration tags (variant, mod state, optional equipment)  

- **To CAOS / Analytics (02-20-01)**:
  - Post-flight **W&B snapshots** for fleet analysis  

- **To ATA 31 Recording**:
  - Selected W&B parameters at key times (e.g., brake release, lift-off, touchdown)  

---

## 6. Safety & Certification Considerations

The WBC is **safety-significant**, as incorrect W&B can cause:

- Exceedance of **structural limits** (overweight)  
- Operation **outside CG envelope** (stability & control issues)  
- Misleading performance computations and takeoff / landing decisions  

Expected characteristics (to be confirmed with authorities):

- Software assurance aligned with **DO-178C DAL B or C**  
- Clear **traceability** to AFM / certified WBM data  
- Strong **configuration control**:
  - Aircraft variant, configuration version, mod status  
  - Data packages defining BEM, moment arms, load stations, etc.  

Integration with ATA 95 (if NN assistance is used) must:

- Enforce **bounded corrections** and **envelope checks**  
- Provide **deterministic fallback** that is verifiably safe  
- Include **runtime monitoring** and **model lifecycle management**  

---

## 7. Dependencies & Cross-References

### 7.1 Internal (02-20)

- [../02-20-00-001_Subsystems_Overview.md](../02-20-00-001_Subsystems_Overview.md)  
- [../02-20-00-002_Subsystems_Integration_Map.md](../02-20-00-002_Subsystems_Integration_Map.md)  
- [../02-20-11_Electronic_Flight_Bag/](../02-20-11_Electronic_Flight_Bag/)  
- [../02-20-13_Performance_Computer/](../02-20-13_Performance_Computer/)  

*(Future)*:

- `02-20-12-002_WB_Requirements.md`  
- `02-20-12-003_WB_Interfaces.md`  
- `02-20-12-004_WB_Design.md`  
- `02-20-12-007_WB_V_and_V.md`  

### 7.2 Other ATA Chapters

- **ATA 28 — H₂ Fuel System**  
  - Tank layout, capacities, transfer logic, constraints  

- **ATA 10 / 21 / 25** (as relevant)  
  - Cabin layout, seat maps, galley / equipment masses, etc.  

- **ATA 31 — Recording**  
  - Parameters to be recorded for W&B traceability  

- **ATA 95 — Neural Networks**  
  - Any NN models integrated into W&B workflows (if applicable)  

---

## 8. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Subsystem:** 02-20-12 Weight & Balance Computer  
> **Maintainer:** Digital Ops & Performance Group  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  

| Version | Date       | Author / Team                         | Notes                          |
| ------- | ---------- | ------------------------------------- | ------------------------------ |
| 0.1.0   | 2025-11-20 | AMPEL360 Digital Ops & Performance WG | Initial WBC system overview    |
