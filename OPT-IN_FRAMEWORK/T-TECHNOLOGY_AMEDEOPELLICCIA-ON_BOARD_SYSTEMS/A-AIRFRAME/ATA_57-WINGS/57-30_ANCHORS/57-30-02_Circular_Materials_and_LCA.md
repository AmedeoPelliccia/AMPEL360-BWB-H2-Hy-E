# 57-30-02 — Circular Materials and LCA

**ATA Chapter:** 57 – Wings  
**Bucket ID:** 57-30_ANCHORS  
**Document ID:** 57-30-02  
**Lifecycle Tags:** [Design, Production, End-of-Life]  

---

## 1. Purpose

This document describes the **materials circularity** and **Life Cycle Assessment (LCA)** framework for wing structures in the AMPEL360 BWB H2 Hybrid Electric aircraft.

---

## 2. Scope

Included in this sub-bucket:

- Material families and their sustainability characteristics  
- LCA boundaries and methodology for wing components  
- Embodied carbon accounting  
- Recycling pathways and material recovery rates  

Excluded:

- Detailed structural analysis (see `57-50_Structures`)
- Manufacturing processes (see `57-00-09_Production_Planning`)

---

## 3. Material Families

### 3.1 Wing Primary Structure Materials

| Material Family | Application | Recyclability | Embodied Carbon |
|-----------------|-------------|---------------|-----------------|
| CFRP (Carbon Fiber Reinforced Polymer) | Wing skins, spars | Moderate (pyrolysis) | TBD kg CO₂e/kg |
| Al-Li Alloys | Ribs, fittings | High (remelting) | TBD kg CO₂e/kg |
| Titanium Alloys | Fasteners, critical joints | High (remelting) | TBD kg CO₂e/kg |
| Bio-based Composites | Secondary structures | High (composting) | TBD kg CO₂e/kg |

### 3.2 Secondary Structure Materials

| Material Family | Application | Recyclability | Embodied Carbon |
|-----------------|-------------|---------------|-----------------|
| Thermoplastic Composites | Fairings, access panels | High (reprocessing) | TBD kg CO₂e/kg |
| Recycled Aluminum | Non-critical brackets | Very High | TBD kg CO₂e/kg |

---

## 4. LCA Framework

### 4.1 System Boundary

The LCA boundary for wing systems includes:

- **Cradle-to-Gate**: Raw material extraction through manufacturing  
- **Use Phase**: Operational impacts including maintenance  
- **End-of-Life**: Recycling, recovery, and disposal  

### 4.2 Functional Unit

- Per kilogram of wing structure  
- Per flight hour of operation  
- Per passenger-kilometer (allocated)  

### 4.3 Impact Categories

| Category | Unit | Method |
|----------|------|--------|
| Global Warming Potential (GWP) | kg CO₂e | IPCC 2021 |
| Acidification Potential | kg SO₂e | CML 2002 |
| Resource Depletion | kg Sb-eq | CML 2002 |

---

## 5. Interfaces

- **ATA 85 Circularity**: Global circularity framework and material databases  
- **ATA 99 DPP**: Material passport integration  
- **57-30-04 ReUse ReCycle Strategies**: End-of-life pathways  

---

## 6. Traceability

- Related Requirements: REQ-57-30-010 (TBD)  
- Related DPP IDs: See [57-30-03_Wing_DPP_and_Traceability_Links.md](./57-30-03_Wing_DPP_and_Traceability_Links.md)  

---

## 7. Status

- **Applicability:** MANDATORY for ATA 57  
- **Current Status:** Framework defined, data population in progress  

---

## 8. Document Control

- **Standard:** OPT-IN Framework v1.1  
- **Owner:** AMPEL360 Documentation WG  
- **Status:** DRAFT – Subject to human review and approval  
- **Last Updated:** 2025-11-28  
- **AI Assistance:** Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- **Human Approver:** _[to be completed]_  
- **Repository:** `AMPEL360-BWB-H2-Hy-E`

---

> **See Also:**  
> - [57-30-00_GENERAL-ANCHORS.md](./57-30-00_GENERAL-ANCHORS.md) – Normative bucket definition  
> - [ASSETS/DIAGRAMS/57-30-02_LCA_boundary_diagram.mermaid](./ASSETS/DIAGRAMS/57-30-02_LCA_boundary_diagram.mermaid) – LCA boundary diagram
