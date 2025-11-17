# RQ-95-00-03-301 — DPP SHALL Support EU AI Act High-Risk Documentation

## 1. Requirement Statement

The DPP **SHALL** capture and maintain all documentation required by the **EU AI Act** for high-risk AI systems, including:
- Technical documentation (Annex IV)
- Risk management documentation
- Data governance documentation
- Conformity assessment records
- Post-market monitoring plans

## 2. Rationale

- **Legal compliance**: EU AI Act mandates comprehensive documentation for high-risk AI
- **Market access**: Compliance required for operation in EU airspace
- **Liability protection**: Proper documentation protects against legal claims
- **Regulatory inspection**: Authorities must be able to verify compliance
- **Certification prerequisite**: EASA requires AI Act compliance for type certificates

Non-compliance risks:
- Fines up to €35M or 7% of global turnover
- Prohibition from EU market
- Certification delays or denials
- Liability in case of incidents

## 3. Category

- **Requirement Type**: Regulatory Compliance
- **Domain**: EU AI Act Compliance
- **ATA**: 95-00-03_Requirements

## 4. Source(s)

- **[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)** (Regulation EU 2024/1689):
  - Article 11 — Technical documentation
  - Annex IV — Technical documentation for high-risk AI
  - Article 9 — Risk management system
  - Article 72 — Post-market monitoring
- **[EASA AI Roadmap 2.0](https://www.easa.europa.eu/en/light/topics/artificial-intelligence)** — Alignment with EU AI Act

## 5. Acceptance Criteria

- [ ] DPP schema includes all Annex IV mandatory fields
- [ ] Technical documentation can be exported in required format
- [ ] Risk management records are linked to DPP
- [ ] Conformity assessment status is tracked
- [ ] Post-market monitoring plan is stored
- [ ] Documentation is accessible for regulatory inspections

## 6. Verification Method

- **Method**: Inspection + Analysis
- **Evidence**:
  - Gap analysis: DPP schema vs. Annex IV requirements
  - Sample DPP exports showing all required fields
  - Legal review confirming compliance
  - Certification authority acceptance

## 7. Traceability

- **Design**: 95-00-04-301_EU_AI_Act_Compliance_Design.md
- **Implementation**: 
  - `schema/dpp_v1.0.json` (Annex IV fields)
  - Documentation export tooling
- **Test**: TC-95-00-03-301_EU_AI_Act_Compliance_Check
- **Certification**: MoC-95-00-03-301 (legal opinion + EASA acceptance)

## 8. Status

- **Lifecycle State**: `FOR_REVIEW`
- **Owner**: Certification WG / Legal Team
- **Review Status**: Pending legal review
- **Last Updated**: 2025-11-17
- **Comments**: Legal team reviewing against final EU AI Act text (Regulation 2024/1689).

---

## Document Control

- **Document ID**: RQ-95-00-03-301
- **Version**: 1.0
- **Status**: FOR_REVIEW
