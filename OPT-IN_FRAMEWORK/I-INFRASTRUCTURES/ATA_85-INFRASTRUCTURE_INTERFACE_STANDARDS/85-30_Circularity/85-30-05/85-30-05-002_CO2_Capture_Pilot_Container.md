# 85-30-05-002 — Automated CO₂ Capture & Carbon Synthesis Pilot Unit

**Document ID**: 85-30-05-002_CO2_Capture_Pilot_Container  
**Subsystem**: 85-30 Circularity  
**Parent ATA**: ATA 85 – Infrastructure Interface Standards  
**Axis**: I — Infrastructures  
**Status**: DRAFT / CONCEPT  
**Owner**: Circularity & Materials Domain (ATA 99 / ATA 85)

---

## 1. Purpose

This document defines the functional specifications, interface standards, and operational logic for the **Automated CO₂ Capture & Carbon Synthesis Pilot Unit**.

This unit is a **containerized ground asset** designed to:

1. **Capture** CO₂ from aircraft exhaust streams and ground operation emission points.  
2. **Synthesize** solid carbon (nanomaterials, graphite) from the captured gas.  
3. **Purify and qualify** the carbon output via automated Quality Control (QC).  
4. **Supply** "green carbon" feedstock for the manufacturing of **Green-E Batteries**, as described in  
   [85-30-05-001 Battery Container Lifecycle](./85-30-05-001_Battery_Container_Lifecycle.md).

This pilot unit acts as the **physical bridge** between aircraft emissions and the circular energy-storage ecosystem.

---

## 2. System Description

### 2.1 Physical Form Factor

The system is housed within a **standardized shipping container** (ISO 20 ft or specialized air-transportable ULD equivalent) to ensure:

- **Mobility**: Deployment near airport aprons, test stands, or maintenance hangars.  
- **Modularity**: "Plug-and-play" integration with power, exhaust, and data interfaces.  
- **Scalability**: Replicable units for multi-site deployment in the AMPEL360 ecosystem.

### 2.2 Functional Modules

The container is divided into four automated internal zones:

| Zone | Function                         | Key Components |
| :--- | :------------------------------- | :------------- |
| **Zone A: Intake & Capture** | Absorption and concentration of CO₂ from exhaust or ambient streams | Direct Air Capture (DAC) inlets, flue-gas adaptors, filtration stages, sorption beds/membranes, blowers, compressors |
| **Zone B: Synthesis Reactor** | Conversion (CO₂ → C\(_{(s)}\)) | Catalytic reactors (e.g. Bosch, Sabatier-plus-pyrolysis, electrochemical or molten-salt processes), gas handling, thermal management, safety monitoring |
| **Zone C: Purification** | Removal of impurities and conditioning of carbon | Catalyst removal modules (acid wash / filtration), centrifuges, high-temperature annealing furnaces, drying units |
| **Zone D: QC & Packaging** | Analysis, acceptance, and packaging | Raman spectroscopy, TGA (Thermogravimetric Analysis), optional XRD, automated weighing, inert-atmosphere packaging, label printing |

Each zone is instrumented for **process monitoring**, **interlocks**, and **safety shut-downs**.

---

## 3. Operational Process Flow

The unit operates in an automated cycle managed by an onboard **PLC / industrial controller**, integrated with the AMPEL360 **Digital Operations Network** (CAOS).

### 3.1 Phase 1 – Exhaust Coupling & Capture

- **Input**: The container connects to aircraft exhaust interfaces or ground test-rig exhaust via **ATA 85 standard interface couplers**.  
- **Process**:
  - Exhaust gas is pre-filtered (particulates, condensables).  
  - CO₂ is concentrated to ≥ 95% purity via amine scrubbing, membrane separation, or equivalent.  
- **Key metric**:  
  - **Capture efficiency**: target ≥ 80% of accessible CO₂ stream under nominal conditions.

### 3.2 Phase 2 – Synthesis ("Carbon Loop")

- **Reaction concept** (example Bosch-type pathway):

  \[
  CO_2 + 2H_2 \rightarrow C_{(s)} + 2H_2O
  \]

  (Exact stoichiometry, catalysts, and operating conditions are technology-dependent and to be finalized during prototyping.)

- **Output**: Raw carbon mix (amorphous carbon, graphitic carbon, and possible nanostructures such as CNTs).

### 3.3 Phase 3 – Purification & Quality Control

- **Purification**:
  - Removal of catalyst residues (e.g. Fe, Ni, Co) to achieve **battery-grade purity** (target: ≥ 99.9% C).  
  - Control of particle size distribution, morphology, and surface chemistry.

- **Automated QC**:
  - **Structure**: Graphitic order and defect density (e.g. Raman I\(_D\)/I\(_G\) ratio).  
  - **Purity**: Metallic and inorganic impurity levels.  
  - **Thermal stability**: TGA profiles vs. specification.

- **Pass/Fail logic**:
  - **PASS**: Material meets Green-E battery specifications and is routed to packaging.  
  - **FAIL**: Material is diverted to internal recycling or controlled disposal, with reasons logged for continuous improvement.

### 3.4 Phase 4 – Packaging & DPP Anchoring

- **Packaging**:
  - Approved carbon is weighed (gram-to-kilogram scale batches), filled into inert containers (e.g. foil pouches, canisters), and sealed.  
- **Digital anchoring**:
  - A **Digital Product Passport (DPP)** record is generated for each batch.  
  - DPP is anchored to ATA 02-90-13 DPP schemas and ATA 99 circularity accounting.

---

## 4. Output Specifications – "Green-E" Battery Feedstock

### 4.1 Material Targets

- **Material type**: Carbon nanomaterials (e.g. CNTs, graphene) and/or high-purity spherical/flake graphite.  
- **Intended applications**:
  - Anode active materials.  
  - Conductive additives for Li-ion and solid-state batteries.  
  - Potential future use in structural energy-storage concepts.

- **Quantity**:
  - Pilot phase: gram-to-kilogram scale per batch, optimized for **high value per kg** rather than bulk tonnage.

### 4.2 Quality Constraints (Indicative Targets)

To be compatible with `85-30-05-001_Battery_Container_Lifecycle`:

- **Purity (carbon)**: ≥ 99.9 wt% C.  
- **Ash content**: ≤ 0.05 wt%.  
- **Moisture**: ≤ 50 ppm.  
- **Specific surface area (BET)**: tailored to the target chemistry (e.g. 2–5 m²/g for conventional graphite anodes).  
- **Metallic impurities**: within battery OEM limits (to be defined during detailed design and qualification).

---

## 5. Digital & Circularity Interfaces

### 5.1 Traceability (DPP Integration)

Every batch produced generates a `MaterialBatch` object in the **DPP system** (ATA 02-90 / 02-90-13).

Example conceptual payload:
```json
{
  "batch_id": "C-SYNTH-PILOT-001-BATCH-88",
  "source_co2": {
    "origin": "AIRCRAFT_EXHAUST",
    "flight_id": "AMPEL-TEST-FLT-09",
    "capture_location": "LEMD-STAND-42"
  },
  "production_data": {
    "method": "CATALYTIC_CVD",
    "mass_produced_g": 450.5,
    "purity_percent": 99.92
  },
  "quality_control": {
    "raman_id_g_ratio": 0.85,
    "status": "APPROVED_FOR_BATTERY_USE"
  },
  "destination": "BATTERY_MFG_LAB_04"
}
```

All DPP records must:

- Be uniquely identifiable.
- Be cryptographically anchorable (e.g. ATA 02-90-13 blockchain anchors).
- Maintain full provenance from **CO₂ source → process conditions → QC results → destination**.

### 5.2 Circularity & Carbon Accounting (ATA 99)

This unit directly contributes to circularity KPIs, including:

- **CO₂ mineralized**: total mass of CO₂ irreversibly converted to solid carbon.
- **Upcycling factor**: economic value of recovered carbon vs. cost of capture and processing.
- **Scope 3 impact reduction**: reduction in embedded carbon footprint of batteries through exhaust-derived carbon feedstock.

These metrics feed into ATA 99 **Circularity & Carbon Accounting** dashboards and reports.

---

## 6. Requirements Mapping

This concept document supports and refines the following high-level requirements (to be formalized in `85-30-03_Requirements`):

- **RQ-85-30-05-010 – Containerized Operation**
  The system shall operate autonomously within a standardized containerized footprint (e.g. ISO 20 ft or equivalent), including all capture, synthesis, purification, and packaging functions.

- **RQ-85-30-05-012 – Integrated Quality Control**
  The system shall include inline Quality Control capable of certifying that carbon produced meets defined specifications for use in battery applications.

- **RQ-85-30-05-015 – DPP-Linked Traceability**
  The system shall capture all relevant process parameters and associate them with each produced material batch via a Digital Product Passport record.

- **RQ-85-30-05-016 – Circularity Metrics**
  The system shall provide data necessary to compute CO₂ mineralization, upcycling factor, and battery footprint reduction KPIs under ATA 99.

(Additional detailed requirements to be maintained in `85-30-03_Requirements/` as separate requirement files.)

---

## 7. Next Steps

1. **Technology down-selection**

   - Evaluate candidate reactor technologies (Bosch, electrolysis, CVD-based, etc.) against airport energy availability, safety, and throughput.

2. **Interface definition**

   - Define mechanical, electrical, and data interfaces under ATA 85 (e.g. 85-20 Airport Infrastructure Interfaces; 85-40 Ground Energy Interfaces).

3. **Pilot prototype build**

   - Build and commission a pilot reactor (Zone B) for gram-scale synthesis tests and initial QC characterization.

4. **Qualification roadmap**

   - Define the test plan to qualify CO₂-derived carbon as **battery-grade material**, including collaboration with cell manufacturers and labs.

5. **Integration with ATA 99**

   - Align metrics and reporting formats with ATA 99 Circularity and carbon-accounting schemas.

---

## References

- [85-30-05-001 Battery Container Lifecycle](./85-30-05-001_Battery_Container_Lifecycle.md)
- `02-90-13_DPP_Data_Structures/` – DPP schemas and blockchain anchor formats
- ATA 99 – Circularity & Carbon Accounting (future chapter references)
- Airport infrastructure and energy interface standards (ATA 85-20 / 85-40, to be detailed)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot / ChatGPT), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: *[to be completed]*.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21
- **Version**: 0.1.0

---
