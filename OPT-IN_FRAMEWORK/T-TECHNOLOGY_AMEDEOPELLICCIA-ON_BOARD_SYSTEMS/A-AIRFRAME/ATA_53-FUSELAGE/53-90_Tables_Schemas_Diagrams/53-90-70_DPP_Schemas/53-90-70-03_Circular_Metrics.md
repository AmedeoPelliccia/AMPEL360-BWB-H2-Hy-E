# 53-90-70-03 Circular Metrics

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-70-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / SUSTAINABILITY |
| **ATA Chapter** | 53-90-70 |

---

## 1. Purpose

This document defines the circular economy metrics tracked in the Digital Product Passport for ANCHORS components, supporting sustainability goals and regulatory compliance.

## 2. Circularity Framework

### 2.1 Circular Economy Principles

```
         ┌──────────────────────────────────────────┐
         │           CIRCULAR ECONOMY                │
         │                                          │
         │    ┌────────┐  ┌────────┐  ┌────────┐   │
         │    │ DESIGN │──│  USE   │──│  END   │   │
         │    │  FOR   │  │ PHASE  │  │   OF   │   │
         │    │CIRCULAR│  │        │  │  LIFE  │   │
         │    └────┬───┘  └────┬───┘  └────┬───┘   │
         │         │           │           │        │
         │    ┌────▼───────────▼───────────▼────┐  │
         │    │     MATERIAL RECOVERY            │  │
         │    │  ┌───────┬───────┬───────┐      │  │
         │    │  │REUSE  │REPAIR │RECYCLE│      │  │
         │    │  └───────┴───────┴───────┘      │  │
         │    └─────────────────────────────────┘  │
         └──────────────────────────────────────────┘
```

### 2.2 ANCHORS Circularity Strategy

| Strategy | Application | Target |
|----------|-------------|--------|
| **Design for Longevity** | Battery packs, TMS | 10+ year life |
| **QuickSwap** | Batteries, CO2 cartridges | 10-min exchange |
| **Material Recovery** | All components | 85% recyclable |
| **Carbon Sequestration** | CO2 capture | Negative carbon |

## 3. Metric Definitions

### 3.1 Carbon Metrics

| Metric | Unit | Definition | Calculation |
|--------|------|------------|-------------|
| **embodied_carbon** | kg CO2e | Manufacturing emissions | LCA cradle-to-gate |
| **operational_carbon** | kg CO2e/FH | In-use emissions per flight hour | Energy × emission factor |
| **avoided_carbon** | kg CO2e | Carbon avoided vs. baseline | Baseline - actual |
| **sequestered_carbon** | kg CO2 | CO2 permanently stored | Cartridge capacity × utilization |

### 3.2 Material Metrics

| Metric | Unit | Definition | Target |
|--------|------|------------|--------|
| **recyclability** | % | Material mass recyclable | ≥ 85% |
| **recycled_content** | % | Recycled material used | ≥ 30% |
| **critical_materials** | list | Critical raw materials used | Minimize |
| **hazardous_content** | % | Hazardous material content | ≤ 1% |

### 3.3 Lifecycle Metrics

| Metric | Unit | Definition | Tracking |
|--------|------|------------|----------|
| **repair_count** | count | Number of repairs | Per component |
| **refurbish_count** | count | Number of refurbishments | Per component |
| **reuse_cycles** | count | Reuse instances | Per component |
| **service_life** | years | Total service life | Start to EOL |
| **remaining_life** | % | Estimated remaining useful life | Predictive |

### 3.4 Circularity Index

The **Circularity Index** (CI) is a composite metric measuring overall circular economy performance:

```
CI = w1 × (Recyclability/100) + 
     w2 × (RecycledContent/100) + 
     w3 × (RemainingLife/100) + 
     w4 × (RepairScore) + 
     w5 × (CarbonScore)

Where:
  w1 = 0.25 (Recyclability weight)
  w2 = 0.20 (Recycled content weight)
  w3 = 0.20 (Remaining life weight)
  w4 = 0.15 (Repair potential weight)
  w5 = 0.20 (Carbon performance weight)
  
  CI range: 0.0 (linear) to 1.0 (fully circular)
```

## 4. Component-Specific Metrics

### 4.1 Battery Pack (ANCH-BAT)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Embodied Carbon | 2,450 kg CO2e | < 3,000 | ✅ |
| Recyclability | 92% | ≥ 90% | ✅ |
| Recycled Content | 35% | ≥ 30% | ✅ |
| Service Life | 10 years | ≥ 10 years | ⏳ |
| Circularity Index | 0.78 | ≥ 0.75 | ✅ |

### 4.2 CO2 Cartridge (ANCH-CO2)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Embodied Carbon | 180 kg CO2e | < 250 | ✅ |
| Sequestered Carbon | 50 kg/cartridge | ≥ 45 kg | ✅ |
| Recyclability | 98% | ≥ 95% | ✅ |
| Reuse Cycles | 500 | ≥ 400 | ✅ |
| Circularity Index | 0.92 | ≥ 0.85 | ✅ |

### 4.3 Thermal Components (ANCH-TH)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Embodied Carbon | 850 kg CO2e | < 1,000 | ✅ |
| Recyclability | 88% | ≥ 85% | ✅ |
| Recycled Content | 25% | ≥ 20% | ✅ |
| Service Life | 15 years | ≥ 12 years | ✅ |
| Circularity Index | 0.72 | ≥ 0.70 | ✅ |

## 5. Reporting Requirements

### 5.1 Regulatory Alignment

| Regulation | Requirement | ANCHORS Compliance |
|------------|-------------|---------------------|
| EU Battery Regulation | Carbon footprint, recycled content | ✅ Tracked |
| EU CSRD | Sustainability reporting | ✅ Tracked |
| EU Ecodesign | Circularity requirements | ✅ Tracked |
| ICAO CORSIA | Aviation carbon accounting | ✅ Tracked |

### 5.2 Reporting Frequency

| Report | Frequency | Recipients |
|--------|-----------|------------|
| Component Carbon Footprint | Per installation | OEM, Operator |
| Fleet Sustainability | Quarterly | Management, Regulators |
| Circularity Dashboard | Real-time | Operations |
| End-of-Life Report | Per disposal | Sustainability, Recycler |

## 6. Data Collection

### 6.1 Automatic Collection

| Data Source | Metrics | Frequency |
|-------------|---------|-----------|
| BMS | Battery SOH, cycles | Continuous |
| CO2 Controller | Sequestered CO2 | Per flight |
| Thermal Sensors | Component health | Continuous |
| DPP Events | Maintenance actions | Per event |

### 6.2 Manual Input

| Data Type | Source | Frequency |
|-----------|--------|-----------|
| LCA Data | Supplier | Per design change |
| Material Composition | Supplier | Per part number |
| Recycling Records | Recycler | Per disposal |
| Audit Results | Third party | Annual |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
