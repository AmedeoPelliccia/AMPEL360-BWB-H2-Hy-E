# RQ-95-00-03-003 — DPP SHALL Link To Models And Artifacts

## 1. Requirement Statement

The DPP **SHALL** maintain bidirectional links between the DPP record and all associated artifacts, including:
- Neural network model files (weights, architecture)
- Training datasets and validation datasets
- Training logs and metrics
- Certification evidence packages
- Safety assessment documents (FHA, FMEA, FTA)
- Operational Design Domain (ODD) definitions

## 2. Rationale

- **Enables complete traceability**: From DPP record to all lifecycle artifacts
- **Supports regulatory inspections**: Auditors can quickly access all evidence
- **Facilitates incident investigation**: All relevant artifacts immediately available
- **Enables reproducibility**: Complete artifact set allows model reconstruction
- **Supports knowledge preservation**: Links prevent artifact loss over time

Without proper artifact linking:
- Critical evidence may be lost or inaccessible
- Regulatory compliance becomes difficult to demonstrate
- Incident investigations are slowed or incomplete
- Model reproducibility is compromised

## 3. Category

- **Requirement Type**: Functional
- **Domain**: Traceability & Artifact Management
- **ATA**: 95-00-03_Requirements

## 4. Source(s)

- **[95-00-01-004_DPP_Objectives_for_Neural_Networks.md](../../95-00-01_Overview/)** — Section 2.5 (Artifact Management)
- **[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)** — Article 11 (Technical documentation)
- **[EU DPP Framework](https://ec.europa.eu/commission/presscorner/detail/en/ip_2024_1689)** — Article 10 (Data carrier requirements)
- **[DO-178C](https://www.rtca.org/content/standards-guidance-materials)** — Section 11 (Configuration management)
- **[ISO 15489](https://www.iso.org/standard/62542.html)** — Records management standard

## 5. Acceptance Criteria

- [x] DPP JSON schema includes artifact reference fields
- [ ] All artifact types listed above are linkable
- [ ] Links support multiple storage backends (filesystem, S3, artifact registry)
- [ ] Link integrity validation is performed
- [ ] Broken link detection and reporting
- [ ] Artifact versioning is tracked alongside links
- [ ] Links include cryptographic hashes for integrity verification

## 6. Verification Method

- **Method**: Test + Inspection
- **Evidence**:
  - Integration tests creating DPP with multiple artifact links
  - Link integrity validation tests
  - Sample DPP exports showing artifact references
  - Code review of link management logic

## 7. Traceability

- **Design**: 95-00-04-003_DPP_Artifact_Linking_Specification.md
- **Implementation**: 
  - `src/dpp/artifacts/artifact_manager.py`
  - `schema/dpp_v1.0.json` (artifact reference fields)
- **Test**: 
  - TC-95-00-03-003_Artifact_Linking
  - TC-95-00-03-003A_Link_Integrity_Check
- **Certification**: MoC-95-00-03-003

## 8. Status

- **Lifecycle State**: `APPROVED`
- **Owner**: Requirements WG / Data Architecture Team
- **Approval Date**: 2025-11-17
- **Last Updated**: 2025-11-17
- **Comments**: Approved. Use URI format for artifact references.

---

## Document Control

- **Document ID**: RQ-95-00-03-003
- **Version**: 1.0
- **Status**: APPROVED
