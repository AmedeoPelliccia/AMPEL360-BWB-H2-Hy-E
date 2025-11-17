# RQ-95-00-03-401 — DPP SHALL Store Training Data Lineage

## 1. Requirement Statement

The DPP **SHALL** capture and maintain complete **training data lineage** for each neural network model, including:
- Source datasets (origin, version, collection date)
- Data preprocessing steps and transformations
- Data augmentation techniques applied
- Train/validation/test split methodology
- Data quality metrics and validation results

## 2. Rationale

- **Reproducibility**: Complete data lineage enables model reproduction and validation
- **Regulatory compliance**: EU AI Act requires data governance documentation
- **Quality assurance**: Traceability from data to model performance
- **Bias detection**: Understanding data sources helps identify potential biases
- **Certification evidence**: Authorities require data provenance for AI approval
- **Incident investigation**: Data issues may contribute to model failures

Without data lineage:
- Model behavior cannot be fully explained
- Certification authorities cannot verify data quality
- Bias and fairness cannot be properly assessed
- Reproduction of results is impossible

## 3. Category

- **Requirement Type**: Data & Metadata
- **Domain**: Data Lineage & Provenance
- **ATA**: 95-00-03_Requirements

## 4. Source(s)

- **[95-00-01_Overview/](../../95-00-01_Overview/)** — DPP data model objectives
- **[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)** — Article 10 (Data and data governance)
- **[ISO/IEC 5259](https://www.iso.org/standard/81088.html)** — Data quality for AI systems
- **[W3C PROV](https://www.w3.org/TR/prov-overview/)** — Provenance data model standard

## 5. Acceptance Criteria

- [x] DPP schema includes data lineage fields
- [ ] All training datasets are referenced with version/hash
- [ ] Preprocessing pipeline is documented
- [ ] Data quality metrics are captured
- [ ] Data source provenance is tracked
- [ ] Lineage is visualizable (graph or table)

## 6. Verification Method

- **Method**: Inspection + Analysis
- **Evidence**:
  - Sample DPP with complete data lineage
  - Data lineage visualization
  - Certification review confirming adequacy
  - Reproducibility test using lineage info

## 7. Traceability

- **Design**: 95-00-04-401_Data_Lineage_Schema_Design.md
- **Implementation**: 
  - `schema/dpp_v1.0.json` (data lineage fields)
  - `src/dpp/data/lineage_tracker.py`
- **Test**: 
  - TC-95-00-03-401_Data_Lineage_Capture
  - TC-95-00-03-401A_Reproducibility_Test
- **Certification**: MoC-95-00-03-401

## 8. Status

- **Lifecycle State**: `APPROVED`
- **Owner**: Data WG / ML Engineering Team
- **Approval Date**: 2025-11-17
- **Last Updated**: 2025-11-17
- **Comments**: Approved. Use W3C PROV-compatible format where possible.

---

## Document Control

- **Document ID**: RQ-95-00-03-401
- **Version**: 1.0
- **Status**: APPROVED
