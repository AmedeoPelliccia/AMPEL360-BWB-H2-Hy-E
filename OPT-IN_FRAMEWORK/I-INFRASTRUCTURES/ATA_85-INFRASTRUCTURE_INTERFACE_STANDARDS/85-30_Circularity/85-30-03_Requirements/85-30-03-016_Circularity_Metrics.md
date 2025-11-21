# RQ-85-30-05-016 — Circularity Metrics

**Requirement ID**: RQ-85-30-05-016  
**Title**: Circularity Metrics  
**Subsystem**: 85-30 Circularity  
**Parent ATA**: ATA 85 – Infrastructure Interface Standards  
**Status**: DRAFT  

---

## Description

The system shall provide data necessary to compute CO₂ mineralization, upcycling factor, and battery footprint reduction KPIs under ATA 99.

---

## Rationale

Circularity metrics enable:
- **Environmental impact tracking**: Quantify CO₂ conversion and carbon footprint reduction
- **Economic viability assessment**: Calculate upcycling factor (value created vs. processing cost)
- **Regulatory reporting**: Support EU taxonomy alignment and sustainability disclosures
- **Continuous improvement**: Identify optimization opportunities in the carbon loop

---

## Verification Method

- **Analysis**: Review data collection mechanisms and metric calculation algorithms
- **Review of Design**: Verify integration with ATA 99 circularity accounting systems and dashboards

---

## Required Metrics

The system shall capture data to compute:

1. **CO₂ Mineralized**
   - Total mass of CO₂ irreversibly converted to solid carbon (kg or tonnes)
   - Percentage of input CO₂ successfully mineralized

2. **Upcycling Factor**
   - Economic value of recovered carbon feedstock (€/kg)
   - Total processing cost per kg of battery-grade carbon produced
   - Ratio: value created / cost incurred

3. **Scope 3 Impact Reduction**
   - Reduction in embedded carbon footprint of batteries through exhaust-derived carbon feedstock
   - Comparison to conventional carbon sourcing (mining, petroleum-based)

---

## Data Integration

Metrics shall be:
- **Automatically calculated** from process data and QC results
- **Exported** to ATA 99 circularity accounting systems via standard APIs
- **Visualized** in AMPEL360 dashboards and sustainability reports

---

## Traceability

**Parent Document**: [85-30-05-002 CO₂ Capture Pilot Container](../85-30-05/85-30-05-002_CO2_Capture_Pilot_Container.md)

**Related Requirements**:
- RQ-85-30-05-010 – Containerized Operation
- RQ-85-30-05-012 – Integrated Quality Control
- RQ-85-30-05-015 – DPP-Linked Traceability

**Related Standards**:
- [ATA 99 Carbon Accounting](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_99-CARBON_ACCOUNTING/README.md)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: *[to be completed]*.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21

---
