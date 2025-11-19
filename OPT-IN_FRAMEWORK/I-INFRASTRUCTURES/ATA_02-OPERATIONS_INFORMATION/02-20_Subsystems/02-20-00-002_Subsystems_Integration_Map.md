# 02-20-00-002 — Subsystems Integration Map

**Subsystems Group:** 02-20_Subsystems  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../README.md)  
**Axis:** I — Infrastructures  
**Status:** FRAMEWORK_DEFINED  

---

## 1. Purpose

This document captures the **integration map** between:

- The **02-20_Subsystems** (digital operations & information systems), and  
- Other **ATA chapters** (03, 28, 31, 42, 71, 95, …) and **CAOS / AirCCC**.

It provides a **single view** of:

- Which subsystems depend on which external ATA chapters  
- How data flows between digital ops, aircraft systems, and ground systems  
- Where **CAOS** and **ATA 95 neural networks** plug into 02-20

---

## 2. Scope

Included:

- Logical integration relationships (not low-level signal lists)
- High-level data flow directions (who feeds whom)
- Grouping by target ATA chapter (to_ata_28, to_ata_42, …)
- CAOS integration points at subsystem level

Out of scope:

- Detailed ICDs (Interface Control Documents)  
  → referenced from each `02-20-XX_…/` subsystem  
- Safety cases and FHA/FMEA/SSA  
  → covered in `../02-00-00_GENERAL/02-00-02_SAFETY/`  
- Neural network design details  
  → ATA 95 docs and model cards

---

## 3. High-Level Integration Overview

At a high level:

- **02-20-01_Digital_Ops_Platform** is the **hub**, exposing services and APIs.  
- **02-20-11/12/13** are **cockpit-facing calculators & tools** (EFB, W&B, performance).  
- **02-20-14/15/16** connect to **ground, planning and dispatch**.  
- **02-20-17/18/23** feed and consume **CAOS & ATA 95** predictive capabilities.  
- **H₂-centric flows** cross **02-20-12, 14, 21** with **ATA 28 & 71**.  

The YAML below is the **canonical machine-readable map** for this.

---

## 4. Integration Map (YAML)

```yaml
# 02-20-00-002_Subsystems_Integration_Map
# Logical integration map between 02-20 subsystems, other ATA chapters and CAOS.

subsystems_integration:

  # ─────────────────────────────────────────────
  # 1) 02-20 → ATA 95 (Neural Networks & DPP)
  # ─────────────────────────────────────────────
  to_ata_95:
    - subsystem: "02-20-13_Performance_Computer"
      links_to: "95-20-27_NN_Flight_Controls"
      data_flow:
        from_02_20_13:
          - "Performance demand, mission profile, aircraft state"
        to_02_20_13:
          - "Refined performance predictions from aero/perf NNs"
        notes: "NN-based performance predictor (02-20-13-005) uses ATA 95 models with traceability."

    - subsystem: "02-20-17_Weather_Information_System"
      links_to: "95-20_Subsystems (Weather NN)"
      data_flow:
        from_02_20_17:
          - "Historical and live weather data, turbulence reports"
        to_02_20_17:
          - "Short-term predictive turbulence and hazard fields"
        notes: "NN-WEATHER-PRED models documented under ATA 95 with model cards."

    - subsystem: "02-20-23_Predictive_Operations_NN"
      links_to: "95-20_Subsystems (Ops NNs, RL agents)"
      data_flow:
        from_02_20_23:
          - "Operational scenarios, model telemetry, training stats"
        to_02_20_23:
          - "Deployed NN/RL agents and policies"
        notes: "Delay prediction, turnaround optimization and resource allocation RL."

  # ─────────────────────────────────────────────
  # 2) 02-20 → ATA 28 (Hydrogen Fuel System)
  # ─────────────────────────────────────────────
  to_ata_28:
    - subsystem: "02-20-12_Weight_Balance_Computer"
      links_to: "ATA_28 H2 Fuel Quantity & Management"
      data_flow:
        from_ata_28:
          - "Tank levels, temperatures, pressures"
        to_ata_28:
          - "Derived CG and load distribution constraints (advisory)"
        notes: "Real-time H2 mass impacts CG envelope and loadability."

    - subsystem: "02-20-21_H2_Operations_Management"
      links_to: "ATA_28 Refueling & Conditioning"
      data_flow:
        from_ata_28:
          - "Refuelling state, valve status, interlocks"
        to_ata_28:
          - "Requested refuelling profiles and ops constraints (non-command)"
        notes: "Coordinates H2 ground operations logic with 02-10 and ATA 03 GSE."

    - subsystem: "02-20-14_Ground_Ops_Management"
      links_to: "ATA_28 + ATA_03 H2 GSE"
      data_flow:
        from_ata_28_03:
          - "Availability and health of H2 GSE, connection status"
        to_ata_28_03:
          - "Turnaround plan and H2 operation windows"
        notes: "Ensures turnarounds respect H2 system and GSE capabilities."

  # ─────────────────────────────────────────────
  # 3) 02-20 → ATA 42 (IMA, Avionics, Data Buses)
  # ─────────────────────────────────────────────
  to_ata_42:
    - subsystem: "02-20-11_Electronic_Flight_Bag"
      links_to: "ATA_42 IMA / Data Concentrators"
      data_flow:
        from_ata_42:
          - "Position, altitude, airspeed, configuration, fuel/H2 data"
        to_ata_42:
          - "Advisory performance limits, suggested speeds, route proposals"
        notes: "Connectivity typically via ARINC 763 / secure WiFi for Class 3 EFB."

    - subsystem: "02-20-13_Performance_Computer"
      links_to: "ATA_42 FMS / Guidance"
      data_flow:
        from_ata_42:
          - "Flight plan, weight, environmental data"
        to_ata_42:
          - "Recommended climb/descent profiles, speeds, altitude changes"
        notes: "Provides inputs to FMS optimization (advisory)."

    - subsystem: "02-20-17_Weather_Information_System"
      links_to: "ATA_42 Displays & Networks"
      data_flow:
        from_ata_42:
          - "Aircraft position, heading, route path"
        to_ata_42:
          - "Graphical weather overlays and hazard polygons"
        notes: "Feeds cockpit displays and/or EFB."

  # ─────────────────────────────────────────────
  # 4) 02-20 → ATA 31 (Indicating & Recording)
  # ─────────────────────────────────────────────
  to_ata_31:
    - subsystem: "02-20-18_Operational_Data_Recording"
      links_to: "ATA_31 Flight Data / Central Maintenance Recording"
      data_flow:
        from_02_20_18:
          - "Operations events, KPIs, subsystem health summaries"
        to_02_20_18:
          - "Recorded flight-data segments for replay/analytics"
        notes: "Provides operations-focused recording on top of raw FDR."

    - subsystem: "02-20-23_Predictive_Operations_NN"
      links_to: "ATA_31 Data Repositories"
      data_flow:
        from_ata_31:
          - "Historical operations datasets for training"
        to_ata_31:
          - "Derived labels and features for future analytics"
        notes: "Feedback loop for continuous improvement of models."

  # ─────────────────────────────────────────────
  # 5) 02-20 → ATA 03 (Support Information & GSE)
  # ─────────────────────────────────────────────
  to_ata_03:
    - subsystem: "02-20-14_Ground_Ops_Management"
      links_to: "ATA_03 Ground Support Equipment"
      data_flow:
        from_ata_03:
          - "GSE availability, connection status, constraints"
        to_ata_03:
          - "Planned GSE usage, sequencing, required service windows"
        notes: "Aligns turnaround plan with actual GSE capabilities."

    - subsystem: "02-20-21_H2_Operations_Management"
      links_to: "ATA_03 H2 Refuelling Units"
      data_flow:
        from_ata_03:
          - "H2 truck/plant readiness, line pressure"
        to_ata_03:
          - "Requested refuel start/end, flow limits, safety conditions"
        notes: "Ensures airport-side H2 operations match aircraft constraints."

  # ─────────────────────────────────────────────
  # 6) 02-20 → CAOS / AirCCC
  # ─────────────────────────────────────────────
  to_caos:
    - subsystem: "02-20-01_Digital_Ops_Platform"
      role: "Primary data backbone for CAOS"
      data_flow:
        from_platform:
          - "Consolidated ops events, KPIs and state from all 02-20 subsystems"
        to_platform:
          - "CAOS-generated insights, alerts, recommendations"
        notes: "Acts as bidirectional bridge between ops systems and CAOS core."

    - subsystem: "02-20-18_Operational_Data_Recording"
      role: "Historical data provider"
      data_flow:
        from_02_20_18:
          - "Curated ops datasets and KPI histories"
        to_02_20_18:
          - "CAOS annotations and analysis results"
        notes: "Supports fleet-wide analytics and post-event reviews."

    - subsystem: "02-20-23_Predictive_Operations_NN"
      role: "CAOS-aligned predictive service layer"
      data_flow:
        from_caos:
          - "Scenario definitions, KPI objectives, policy constraints"
        to_caos:
          - "Predictions, recommended actions, confidence metrics"
        notes: "Implements CAOS use cases for predictive operations."

  # ─────────────────────────────────────────────
  # 7) Misc / Other ATA Links (High Level)
  # ─────────────────────────────────────────────
  other_links:
    - subsystem: "02-20-19_Crew_Resource_Management"
      links_to:
        - "ATA_31 (for logging crew ops events)"
        - "ATA_44/25 (for cabin & comms integration, when defined)"
      notes: "CRM tools may log events and interact with cabin/comm systems."

    - subsystem: "02-20-22_Passenger_Experience_Management"
      links_to:
        - "ATA_44 (IFEC / cabin network, when defined)"
        - "ATA_21 (ECS comfort data)"
      notes: "Uses cabin and ECS data to evaluate passenger experience."

````

---

## 5. How to Use This Map

* As a **navigation index**:

  * Start from a subsystem (e.g. `02-20-13_Performance_Computer`) and see which ATA chapters it touches.
* As a **change impact tool**:

  * If an interface in ATA 28 or 42 changes, this document shows which subsystems must be re-assessed.
* As **input for certification & safety**:

  * Supports FHA/FMEA/SSA by making digital-ops interfaces explicit.
* As **ground truth for CAOS integration**:

  * CAOS architecture docs should be consistent with the `to_caos` section above.

---

## 6. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Toolchain:** GitHub + MCP Doc Control + AMPEL360 OPT-IN Guidelines
> **Scope:** Logical integration map for all 02-20_Subsystems

| Version | Date       | Author / Team                         | Changes                            |
| ------- | ---------- | ------------------------------------- | ---------------------------------- |
| 0.1     | YYYY-MM-DD | AMPEL360 Digital Operations & CAOS WG | Initial integration map definition |

```

