---
Title: "Carbon Accounting Methodology — ATA 02 Digital Operations"
Identifier: "AMPEL360-02-30-00-002"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "Sustainability Team"
CreatedAt: "2025-11-21"
ModifiedAt: "2025-11-21"
Scope: "Carbon accounting methodology for ATA 02 digital operations and infrastructure"
Abstract: "Describes the carbon accounting methodology for ATA 02, including system boundaries, scope definitions, emission factors, calculation methods, and data sources for digital operations carbon footprint."
Keywords: ["ATA 02", "Carbon Accounting", "Emissions", "Greenhouse Gas", "Digital Operations", "Scope 1", "Scope 2", "Scope 3"]
Compliance:
  - "GHG Protocol"
  - "ISO 14064-1:2018"
  - "AMPEL360 Doc Standard v1.5"
  - "EU Taxonomy Regulation"
Links:
  Parent: "./"
  Framework: "./02-30-00-001_Circularity_Framework_Overview.md"
  Dashboard: "./02-30-00-003_Circularity_Metrics_Dashboard.yaml"
  CarbonDigitalOps: "./02-30-01_Sustainability_Overview/02-30-01-002_Carbon_Accounting_Digital_Ops.md"
  DataLifecycle: "./02-30-03_Data_Lifecycle/"
  SoftwareSustainability: "./02-30-04_Software_Sustainability/"
ChangeLog:
  - {version: "1.0.0", date: "2025-11-21", author: "Sustainability Team", change: "Initial methodology definition"}
---

# Carbon Accounting Methodology — ATA 02 Digital Operations

## 1. Purpose

This document defines the **carbon accounting methodology** for **ATA 02 — Operations Information** digital operations and infrastructure within the AMPEL360 program. It establishes:

- **System boundaries** defining what is included in carbon calculations
- **Scope definitions** (Scope 1, 2, 3) for different emission categories
- **Emission factors** and data sources for calculations
- **Calculation methods** for various digital operations components
- **Data collection processes** and quality requirements
- **Reporting standards** and verification approaches

The methodology aligns with:
- **[GHG Protocol Corporate Standard](https://ghgprotocol.org/corporate-standard)** — Global standard for corporate carbon accounting
- **[ISO 14064-1:2018](https://www.iso.org/standard/66453.html)** — Specification for GHG quantification and reporting
- **[EU Taxonomy Regulation](https://finance.ec.europa.eu/sustainable-finance/tools-and-standards/eu-taxonomy-sustainable-activities_en)** — Technical screening criteria for climate objectives

---

## 2. System Boundaries

### 2.1 Organizational Boundary

**ATA 02 Digital Operations** encompasses:

**In Scope**:
- Digital infrastructure supporting operations information (data centers, edge devices, network equipment)
- Software systems and applications for operations data processing
- ML/AI models for operational optimization (training and inference)
- Data storage and archival systems
- Electronic Flight Bag (EFB) devices and associated infrastructure
- Operations data collection sensors and IoT devices
- Development, test, and production environments

**Out of Scope** (covered in other ATAs):
- Aircraft onboard systems (covered in ATA 20-80)
- Physical manufacturing facilities (covered in relevant production ATAs)
- Corporate office facilities (covered in enterprise carbon accounting)

### 2.2 Temporal Boundary

- **Baseline Year**: 2024 (calendar year)
- **Reporting Frequency**: Quarterly for management reporting, annual for external disclosure
- **Forecast Period**: 2024-2030 (aligned with AMPEL360 roadmap)

### 2.3 Operational Boundary

Carbon accounting covers three scopes following the GHG Protocol:

#### Scope 1: Direct Emissions
- Backup generators at data center facilities (if owned/operated by AMPEL360)
- Fleet vehicles for IT equipment transport (if applicable)

**Note**: Most ATA 02 digital operations have minimal Scope 1 emissions as systems are primarily electric.

#### Scope 2: Indirect Emissions from Purchased Energy
- Electricity for data centers (owned or colocation facilities)
- Electricity for edge computing devices
- Electricity for development and test environments
- Electricity for network infrastructure
- Cooling systems for data centers

**Approach**: Location-based and market-based methods (dual reporting)

#### Scope 3: Other Indirect Emissions
**Category 1 — Purchased Goods & Services**:
- Hardware procurement (servers, storage, networking equipment, EFB devices, sensors)
- Software licenses and cloud services
- Professional services for IT operations

**Category 2 — Capital Goods**:
- Data center infrastructure (if capitalized)
- Major hardware investments

**Category 4 — Upstream Transportation**:
- Shipping of hardware components
- Logistics for equipment delivery

**Category 5 — Waste Generated**:
- E-waste disposal and recycling

**Category 11 — Use of Sold Products**:
- Energy consumption of EFB devices during aircraft operations (if AMPEL360 provides devices)

**Category 15 — Investments**:
- Emissions from data center investments (if applicable)

---

## 3. Emission Factors and Data Sources

### 3.1 Electricity Emission Factors

#### Location-Based Method
Use grid-average emission factors by region:

| Region | Grid Emission Factor | Source | Update Frequency |
|--------|---------------------|---------|------------------|
| EU Average | 0.275 kg CO₂e/kWh | [EEA](https://www.eea.europa.eu/) | Annual |
| Germany | 0.420 kg CO₂e/kWh | [German Environment Agency](https://www.umweltbundesamt.de/) | Annual |
| France | 0.057 kg CO₂e/kWh | [RTE](https://www.rte-france.com/) | Annual |
| US Average | 0.386 kg CO₂e/kWh | [EPA eGRID](https://www.epa.gov/egrid) | Annual |
| Nordic Mix | 0.045 kg CO₂e/kWh | [Nordic Energy Regulators](https://nordicenergyregulators.org/) | Annual |

#### Market-Based Method
Use specific emission factors from:
- Renewable Energy Certificates (RECs)
- Power Purchase Agreements (PPAs)
- Supplier-specific emission factors
- Residual mix factors (for unbundled RECs)

**Priority Order**:
1. Direct contracts with renewable energy generators (0 kg CO₂e/kWh)
2. Bundled RECs from specific renewable projects
3. Unbundled RECs with residual mix adjustment
4. Utility-specific emission factors
5. Grid average (if no market instrument available)

### 3.2 Hardware Embodied Carbon

Typical embodied carbon values for common components:

| Component Type | Embodied Carbon | Lifetime | Source |
|----------------|-----------------|----------|--------|
| Server (2U) | 1,200 kg CO₂e | 5 years | [Dell Product Carbon Footprint](https://www.dell.com/en-us/dt/corporate/social-impact/advancing-sustainability/climate-action/product-carbon-footprints.htm) |
| Storage Array (10TB) | 2,500 kg CO₂e | 7 years | [HP Environmental Data](https://www8.hp.com/us/en/hp-information/environment/product-data.html) |
| Network Switch (48-port) | 150 kg CO₂e | 7 years | Industry average |
| EFB Tablet | 80 kg CO₂e | 4 years | [Apple Environmental Reports](https://www.apple.com/environment/) |
| IoT Sensor | 5 kg CO₂e | 8 years | Supplier data |

**Method**: Allocate embodied carbon over useful lifetime using straight-line depreciation.

**Annual Amortized Carbon** = Embodied Carbon / Useful Lifetime (years)

### 3.3 Cloud Services Emission Factors

For cloud infrastructure (IaaS, PaaS, SaaS):

| Provider | Emission Factor | Renewable % | Source |
|----------|----------------|-------------|--------|
| AWS | Provider-specific tool | 100% (goal 2025) | [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) |
| Azure | Provider-specific tool | 100% (achieved 2021) | [Microsoft Emissions Impact Dashboard](https://www.microsoft.com/en-us/sustainability/emissions-impact-dashboard) |
| Google Cloud | Provider-specific tool | 100% (achieved 2017) | [Google Cloud Carbon Footprint](https://cloud.google.com/carbon-footprint) |

**Best Practice**: Use provider-specific carbon accounting tools when available; otherwise apply regional grid factors to estimated energy consumption.

### 3.4 Software Carbon Intensity

For software operations:

**Energy per Transaction** = (CPU utilization × CPU TDP × Time) + (Memory × Power) + (Storage I/O × Power) + (Network × Power)

**Carbon per Transaction** = Energy per Transaction × Grid Emission Factor

**Typical Values** (for reference):
- API call: 0.1-10 Wh (0.00003-0.003 kg CO₂e at EU average)
- Database query: 0.01-1 Wh (0.000003-0.0003 kg CO₂e at EU average)
- ML inference: 1-100 Wh (0.0003-0.03 kg CO₂e at EU average)
- ML training (small model): 10-1,000 kWh (3-300 kg CO₂e at EU average)
- ML training (large model): 1,000-100,000 kWh (300-30,000 kg CO₂e at EU average)

**Data Sources**:
- Application Performance Monitoring (APM) tools
- Infrastructure monitoring (CPU, memory, I/O metrics)
- Power Usage Effectiveness (PUE) measurements
- [Green Software Foundation tools](https://greensoftware.foundation/)

---

## 4. Calculation Methods

### 4.1 Data Center Energy Consumption

**Total Data Center Energy** = IT Equipment Energy + Cooling Energy + Other Facility Energy

**IT Equipment Energy** = Σ (Server Power × Utilization × Hours) + Σ (Storage Power × Hours) + Σ (Network Power × Hours)

**Cooling Energy** = IT Equipment Energy × (PUE - 1)

Where:
- **PUE** (Power Usage Effectiveness) = Total Facility Energy / IT Equipment Energy
- Target PUE: < 1.3 for modern data centers, < 1.5 for older facilities

**Data Center Carbon Emissions** = Total Data Center Energy × Emission Factor (location- or market-based)

### 4.2 Edge Computing Energy Consumption

**Edge Device Energy** = Device Count × Average Power per Device × Hours × Utilization Factor

**Example — EFB Tablets**:
- Average Power: 10W (active), 1W (idle)
- Daily Usage: 4 hours active, 20 hours idle
- Daily Energy per Device: (10W × 4h) + (1W × 20h) = 60 Wh = 0.06 kWh
- Annual Energy per Device: 0.06 kWh/day × 365 days = 21.9 kWh
- Annual Carbon per Device: 21.9 kWh × 0.275 kg CO₂e/kWh (EU avg) = 6.0 kg CO₂e

**Total Edge Carbon** = Σ (Edge Device Energy × Emission Factor)

### 4.3 Network Infrastructure

**Network Energy** = Σ (Switch Power × Count × Hours) + Σ (Router Power × Count × Hours) + Transmission Energy

**Transmission Energy Estimate** (if direct measurement unavailable):
- Use data transfer volume and network energy intensity factor: ~0.05 kWh/GB (industry average, highly variable)

### 4.4 ML Model Training Carbon

**Training Carbon** = Training Energy × Emission Factor

**Training Energy** = GPU Power × GPU Count × Training Hours × PUE

**Example**:
- Model: Flight delay predictor neural network
- GPUs: 8× NVIDIA A100 (400W TDP each)
- Training Time: 48 hours
- PUE: 1.2
- Training Energy: 400W × 8 × 48h × 1.2 = 184.3 kWh
- Training Carbon: 184.3 kWh × 0.275 kg CO₂e/kWh (EU avg) = 50.7 kg CO₂e

**Amortization**: Divide by number of inference runs or useful model lifetime to get per-inference carbon allocation.

### 4.5 Hardware Embodied Carbon Allocation

**Annual Hardware Carbon** = Σ (Device Embodied Carbon / Useful Lifetime)

**Example**:
- 100 servers, 1,200 kg CO₂e each, 5-year lifetime
- Annual Embodied Carbon: (100 × 1,200) / 5 = 24,000 kg CO₂e/year

---

## 5. Data Collection Process

### 5.1 Data Sources

| Data Type | Source | Collection Frequency | Responsible Team |
|-----------|--------|---------------------|------------------|
| Electricity consumption | Utility bills, submeter data | Monthly | Facilities |
| Server/storage utilization | Infrastructure monitoring tools (Prometheus, Grafana) | Continuous | IT Operations |
| Cloud usage | Cloud provider dashboards/APIs | Daily | DevOps |
| Hardware inventory | Asset management system | Real-time | IT Asset Management |
| Software transactions | APM tools (New Relic, Datadog) | Continuous | Software Engineering |
| ML training metrics | MLOps platform (MLflow, Weights & Biases) | Per training run | AI/ML Team |

### 5.2 Data Quality Requirements

**Tier 1 (Highest Priority)**:
- Directly measured data (utility bills, submeters, cloud provider reports)
- Quality Target: ±5% accuracy
- Coverage: ≥95% of emissions

**Tier 2 (Moderate Priority)**:
- Estimated data using specific proxies (nameplate power × utilization)
- Quality Target: ±15% accuracy
- Coverage: 4-5% of emissions

**Tier 3 (Lower Priority)**:
- Industry averages or general proxies
- Quality Target: ±30% accuracy
- Coverage: <1% of emissions

### 5.3 Data Management

- **Storage**: Centralized carbon accounting database (ATA 02-60 Storage Systems)
- **Retention**: 10 years minimum (regulatory requirement)
- **Access Control**: Read access for reporting teams, write access restricted to data owners
- **Audit Trail**: All data entries logged with timestamp and user ID
- **Backup**: Daily backups, quarterly archives

---

## 6. Reporting and Verification

### 6.1 Internal Reporting

**Monthly Dashboard**: Real-time metrics for operational monitoring
- Total carbon emissions (Scope 1, 2, 3)
- Carbon intensity per transaction
- Key driver analysis (top emission sources)
- Trend vs. baseline and targets

**Quarterly Management Report**: Executive-level summary
- Quarter-over-quarter and year-over-year trends
- Progress against reduction targets
- Initiative impact assessment
- Recommendations for improvement

### 6.2 External Reporting

**Annual Sustainability Report**: Public disclosure
- Total GHG emissions by scope (GHG Protocol format)
- Emission intensity metrics
- Reduction initiatives and outcomes
- Forward-looking targets and commitments
- Third-party verification statement

**Regulatory Filings**: As required
- EU Taxonomy alignment assessment
- [EU AI Act](https://artificialintelligenceact.eu/) environmental impact disclosures
- National reporting requirements (if applicable)

### 6.3 Verification Approach

**Internal Verification** (quarterly):
- Data quality checks (completeness, consistency, outlier detection)
- Calculation methodology review
- Cross-checks with operational data (energy bills, hardware inventory)

**External Verification** (annual):
- Third-party limited assurance per [ISAE 3410](https://www.iaasb.org/publications/international-standard-assurance-engagements-isae-3410-assurance-engagements-greenhouse-gas) or [ISO 14064-3](https://www.iso.org/standard/66455.html)
- Scope: Scope 1, 2, and material Scope 3 categories
- Materiality threshold: ±5% of total reported emissions

---

## 7. Boundaries and Limitations

### 7.1 Known Limitations

1. **Scope 3 Category 11 (Use of Sold Products)**: EFB device usage during flight operations is estimated based on average usage patterns; actual usage may vary significantly.

2. **Cloud Provider Emissions**: Reliance on provider-reported data; methodology differences between providers may affect comparability.

3. **Software Energy Profiling**: Granular per-transaction energy measurement requires instrumentation that may not be available for all legacy systems.

4. **Embodied Carbon Data**: Hardware embodied carbon relies on manufacturer-provided data or industry averages; supply chain-specific values may differ.

### 7.2 Uncertainty Assessment

**Overall Uncertainty Estimate**: ±12% for total ATA 02 carbon footprint

**By Scope**:
- Scope 1: ±5% (minimal emissions, high measurement accuracy)
- Scope 2: ±8% (primarily electricity, good measurement infrastructure)
- Scope 3: ±20% (reliance on estimates and external data)

### 7.3 Improvement Roadmap

**2025**: Implement sub-metering for major data center equipment to improve allocation accuracy
**2026**: Deploy APM tools with built-in carbon profiling for all production applications
**2027**: Require supplier-specific embodied carbon data for all hardware procurement >€10K
**2028**: Achieve <±8% overall uncertainty through enhanced measurement infrastructure

---

## 8. Related Documentation

### Core Framework
- [Circularity Framework Overview](./02-30-00-001_Circularity_Framework_Overview.md) — Overall circularity principles and domain structure
- [Circularity Metrics Dashboard](./02-30-00-003_Circularity_Metrics_Dashboard.yaml) — KPI definitions and dashboard configuration

### Detailed Carbon Accounting
- [Carbon Accounting for Digital Ops](./02-30-01_Sustainability_Overview/02-30-01-002_Carbon_Accounting_Digital_Ops.md) — Operational details and examples
- [Data Storage Energy Efficiency](./02-30-03_Data_Lifecycle/02-30-03-002_Storage_Energy_Efficiency.md) — Storage-specific energy and carbon
- [ML Model Carbon Footprint](./02-30-04_Software_Sustainability/02-30-04-003_ML_Model_Carbon_Footprint.md) — ML-specific methodology

### External References
- **[GHG Protocol](https://ghgprotocol.org/)** — Global standard for carbon accounting
- **[ISO 14064-1:2018](https://www.iso.org/standard/66453.html)** — GHG quantification specification
- **[Green Software Foundation](https://greensoftware.foundation/)** — Software carbon intensity standards

---

## 9. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-11-21 | Sustainability Team | Initial methodology definition |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---

**End of Document**
