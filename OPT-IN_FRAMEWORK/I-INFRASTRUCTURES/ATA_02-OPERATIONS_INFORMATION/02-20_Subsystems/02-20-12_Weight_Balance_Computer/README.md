# 02-20-12 — Weight & Balance Computer

**Subsystem ID:** 02-20-12  
**Parent Group:** [02-20_Subsystems](../README.md)  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Function Category:** Operational Computation (Mass, CG, H₂ Integration)  
**Status:** FRAMEWORK_DEFINED  
**Version:** 1.0  

---

## 1. Purpose

The **02-20-12 Weight & Balance (W&B) Computer** is the authoritative computational engine for:

- Real-time aircraft mass estimation  
- CG (Center of Gravity) evaluation  
- Envelope validation (forward / aft / lateral)  
- H₂ fuel–specific corrections (density, boil-off, sequencing)  
- Providing verified W&B outputs to:  
  - EFB (02-20-11)  
  - Performance Computer (02-20-13)  
  - Operational Data Recording (02-20-18)  
  - ATA 28 (for sequencing coordination)  

The subsystem ensures consistent, **traceable, deterministic and AI-augmented** W&B computation.

---

## 2. Scope

### In Scope
- Full W&B computational logic  
- Integration with hydogen cryogenic fuel system  
- Envelope protection logic  
- NN-enhanced predictive modules via ATA 95  
- APIs for EFB, performance, dispatch and CAOS  
- Data quality filters and coherency enforcement  

### Out of Scope
- Tank control / actuation (ATA 28 responsibility)  
- Aircraft-level flight control protections  
- FDR-level W&B channels (ATA 31; only providing data inputs)  
- Operator-specific load planning (02-20-15 integration handles this)  

---

## 3. Subsystem Structure

```

02-20-12_Weight_Balance_Computer/
├── README.md
├── 02-20-12-001_WB_System_Overview.md
├── 02-20-12-002_Load_Calculation_Engine.md
├── 02-20-12-003_CG_Envelope_Monitoring.md
├── 02-20-12-004_H2_Fuel_Integration.md
├── 02-20-12-005_Real_Time_CG_Tracking.md
├── 02-20-12-006_Integration_with_ATA_28.md
│
├── ASSETS/
│   ├── 02-20-12-A-001_WB_Architecture.drawio
│   ├── 02-20-12-A-002_CG_Envelope_BWB.svg
│   ├── 02-20-12-A-003_H2_Fuel_Effects.svg
│   └── 02-20-12-A-101_Calculation_Algorithms.pdf
│
└── Certification/
├── 02-20-12-A-501_Requirements_Traceability.md
├── 02-20-12-A-502_DO_178C_Compliance_Summary.md
├── 02-20-12-A-503_Model_Assurance_ATA_95.md
└── 02-20-12-A-504_Test_Evidence.md

```

This structure mirrors the **14-folder OPT-IN pattern**, cross-linked with ATA 02 and ATA 95.

---

## 4. System Mission

The Weight & Balance Computer provides:

- Deterministic CG computation  
- Full envelope evaluation (forward, aft, lateral)  
- Dynamic in-flight CG tracking  
- H₂-tank–induced mass & CG shifts  
- Predictive CG drift  
- Boil-off impact evaluation  
- Quality-controlled data feed to EFB, performance and CAOS subsystems  
- Fallback behavior under degraded conditions  

---

## 5. Key Responsibilities

### 5.1 Core Mass Properties Computation
- ZFW / TOW / LW computation  
- Pax/cargo distribution ingestion  
- Hull/wing/tank structural mass allocation  
- Configuration compensation (flap-dependent effects)  

### 5.2 CG Envelope Enforcement
- Dynamic limits depending on variant:
  - Q80  
  - Q100  
  - Q120  
- Hybrid (forward + aft + lateral) envelope  
- Out-of-envelope detection  

### 5.3 Hydrogen Integration (ATA 28)
- Cryogenic density conversion  
- Temperature/pressure correction  
- Tank level → mass mapping  
- Sequencing effects on CG drift  
- Predictive boil-off modelling (NN-BOILOFF-v1.0)  

### 5.4 Predictive NN Modules (ATA 95)
- CG drift prediction  
- Lateral imbalance prediction  
- H₂ sloshing effect estimation  
- Out-of-envelope early-warning horizon (2–20 min)  

### 5.5 Data Distribution
Provides certified W&B outputs to:

- **02-20-11** EFB  
- **02-20-13** Performance Computer  
- **02-20-15** Flight Planning  
- **02-20-18** Operational Data Recording  
- **CAOS** predictive analysis layer  

---

## 6. Data Inputs & Interfaces

### 6.1 Inputs

| Source | Data |
|--------|------|
| ATA 42 | Aircraft state (WOW, config, altitude) |
| ATA 28 | Tank levels, temperatures, pressures |
| 02-20-15 | Load sheet, pax manifest |
| 02-20-18 | Historical W&B data (optional) |
| ATA 95 | NN predictions |

### 6.2 Outputs

| Target | Data |
|--------|------|
| 02-20-11 | CG values, envelope, H₂ effects |
| 02-20-13 | Mass and CG for performance calc |
| 02-20-18 | W&B timeline |
| CAOS | Predictive alerts |

All outputs use validated data and include confidence flags.

---

## 7. Safety & Certification Baseline

- Software: **DO-178C DAL C** (higher than EFB because 02-20-12 outputs feed performance calculations)
- NN integration follows ATA 95 Model Assurance Framework  
- Environmental qualification inherited from hosting platform (02-20-01)  
- Fallback deterministic CG model required for safety  

Detailed evidence located at:  
`Certification/02-20-12-A-502_DO_178C_Compliance_Summary.md`

---

## 8. Links to Related Subsystems

| Subsystem | Link |
|-----------|------|
| 02-20-11 EFB | W&B UI, real-time envelope |
| 02-20-13 Performance Computer | TOW + CG inputs |
| 02-20-15 Flight Planning | Load sheet → mass distribution |
| 02-20-17 Weather | Turbulence effects on CG prediction |
| ATA 28 Fuel | Cryogenic H₂ tank data |
| ATA 42 Avionics | WOW / config state |
| ATA 95 NN | Predictive modules |

---

## 9. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Subsystem:** 02-20-12 Weight & Balance Computer  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  

| Version | Date | Author | Changes |
|--------|------|--------|---------|
| 1.0 | 2025-11-19 | AMPEL360 Digital Ops | Initial subsystem README |

```

---


o directamente quieres que te genere **toda la familia completa (001–006)** con la misma calidad que en 02-20-11?
