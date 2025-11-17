# RQ-95-00-03-402 — DPP SHALL Record CO₂e Metrics

## 1. Requirement Statement

The DPP **SHALL** record **carbon dioxide equivalent (CO₂e) metrics** for neural network model training and deployment, including:
- Training energy consumption (kWh)
- Training CO₂e emissions (kg CO₂e)
- Inference energy per prediction (Wh)
- Infrastructure carbon footprint
- Data center location and grid carbon intensity

## 2. Rationale

- **Environmental accountability**: AMPEL360's carbon-negative mission requires tracking all emissions
- **Regulatory compliance**: EU regulations require product environmental impact disclosure
- **Sustainability reporting**: Corporate ESG reporting requires AI carbon footprint data
- **Optimization opportunity**: Identifying high-carbon models enables green AI initiatives
- **Transparency**: Stakeholders increasingly demand environmental impact data

AI model training can have significant carbon footprint:
- Large language models: 100-500 tons CO₂e
- Computer vision models: 10-100 tons CO₂e
- Edge models: 1-10 kg CO₂e

AMPEL360 must track and minimize this impact to maintain carbon-negative operations.

## 3. Category

- **Requirement Type**: Data & Metadata
- **Domain**: Environmental Impact & Sustainability
- **ATA**: 95-00-03_Requirements

## 4. Source(s)

- **AMPEL360 Mission** — Carbon-negative aviation commitment
- **[EU Digital Product Passport Regulation](https://ec.europa.eu/commission/presscorner/detail/en/ip_2024_1689)** — Environmental impact disclosure
- **[ISO 14064](https://www.iso.org/standard/66453.html)** — Greenhouse gas quantification and reporting
- **[Green Software Foundation](https://greensoftware.foundation/)** — Software carbon intensity standard

## 5. Acceptance Criteria

- [x] DPP schema includes CO₂e metric fields
- [ ] Training energy consumption is measured
- [ ] Grid carbon intensity is recorded
- [ ] CO₂e is calculated using standard methodology
- [ ] Inference energy per prediction is estimated
- [ ] Data center location is captured

## 6. Verification Method

- **Method**: Analysis + Measurement
- **Evidence**:
  - Sample DPP with complete CO₂e metrics
  - Energy measurement methodology documentation
  - Comparison with industry benchmarks
  - Sustainability report including DPP CO₂e data

## 7. Traceability

- **Design**: 95-00-04-402_CO2e_Metrics_Schema_Design.md
- **Implementation**: 
  - `schema/dpp_v1.0.json` (CO₂e fields)
  - `src/dpp/sustainability/carbon_tracker.py`
- **Test**: TC-95-00-03-402_CO2e_Metrics_Capture
- **Certification**: MoC-95-00-03-402

## 8. Status

- **Lifecycle State**: `APPROVED`
- **Owner**: Sustainability WG / ML Engineering
- **Approval Date**: 2025-11-17
- **Last Updated**: 2025-11-17
- **Comments**: Approved. Use Green Software Foundation methodology.

---

## Document Control

- **Document ID**: RQ-95-00-03-402
- **Version**: 1.0
- **Status**: APPROVED
