# RQ-95-00-03-302 — DPP SHALL Expose EU DPP Mandatory Fields

## 1. Requirement Statement

The DPP **SHALL** expose all mandatory fields required by the **EU Digital Product Passport (DPP) Regulation** (Regulation EU 2024/1781), enabling compliance with product traceability and circular economy requirements.

## 2. Rationale

- **Legal compliance**: EU DPP regulation mandates product identification and lifecycle data
- **Circular economy**: DPP supports product repair, reuse, and recycling
- **Supply chain transparency**: Enables tracking of product origin and journey
- **Consumer protection**: Provides access to product information
- **Environmental reporting**: Supports CO₂e and sustainability metrics

The EU DPP regulation applies to aviation components and systems, requiring digital traceability throughout the product lifecycle.

## 3. Category

- **Requirement Type**: Regulatory Compliance
- **Domain**: EU Digital Product Passport Regulation
- **ATA**: 95-00-03_Requirements

## 4. Source(s)

- **EU Digital Product Passport Regulation** (Regulation EU 2024/1781):
  - Article 8 — Product passport content
  - Article 9 — Data carrier requirements
  - Annex II — Mandatory data elements
- **Ecodesign for Sustainable Products Regulation** (ESPR)

## 5. Acceptance Criteria

- [ ] DPP schema includes all EU DPP mandatory fields
- [ ] Product identification (GTIN, UUID) is present
- [ ] Lifecycle data (manufacturing, EOL) is tracked
- [ ] Environmental impact data (CO₂e) is recorded
- [ ] Data carrier (QR code, NFC) is supported
- [ ] Public/private data separation is implemented

## 6. Verification Method

- **Method**: Inspection + Analysis
- **Evidence**:
  - Gap analysis: DPP schema vs. EU DPP Regulation Annex II
  - Sample DPP exports with all mandatory fields
  - Legal review confirming compliance

## 7. Traceability

- **Design**: 95-00-04-302_EU_DPP_Regulation_Compliance_Design.md
- **Implementation**: 
  - `schema/dpp_v1.0.json` (EU DPP mandatory fields)
  - Data carrier implementation (QR code generation)
- **Test**: TC-95-00-03-302_EU_DPP_Compliance_Check
- **Certification**: MoC-95-00-03-302

## 8. Status

- **Lifecycle State**: `FOR_REVIEW`
- **Owner**: Certification WG / Sustainability Team
- **Review Status**: Pending legal and sustainability review
- **Last Updated**: 2025-11-17
- **Comments**: EU DPP regulation compliance under review.

---

## Document Control

- **Document ID**: RQ-95-00-03-302
- **Version**: 1.0
- **Status**: FOR_REVIEW
