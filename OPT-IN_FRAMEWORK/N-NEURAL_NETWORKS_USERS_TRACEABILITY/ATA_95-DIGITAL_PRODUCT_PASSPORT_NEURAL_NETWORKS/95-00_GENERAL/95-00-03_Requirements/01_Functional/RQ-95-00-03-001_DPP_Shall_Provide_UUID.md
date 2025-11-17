# RQ-95-00-03-001 — DPP SHALL Provide Unique UUID Per Model

## 1. Requirement Statement

The DPP **SHALL** assign a **globally unique identifier (UUID)** to each neural network model instance covered under ATA 95, in accordance with the identifier scheme defined in 95-00-01-007_DPP_Data_Model_and_Identifiers.md.

## 2. Rationale

- **Avoids identifier collisions** across fleets, programs, and organizations
- **Supports configuration control** and long-term archival requirements
- **Enables unambiguous traceability** in certification and incident analysis
- **Facilitates integration** with external systems (model registries, CI/CD pipelines)
- **Aligns with industry standards** for digital product identification

Without unique identifiers, it would be impossible to:
- Track model versions across the lifecycle
- Correlate models with specific aircraft configurations
- Support regulatory inspections and audits
- Maintain certification evidence packages

## 3. Category

- **Requirement Type**: Functional
- **Domain**: Identification & Traceability
- **ATA**: 95-00-03_Requirements

## 4. Source(s)

- **[95-00-01-004_DPP_Objectives_for_Neural_Networks.md](../../95-00-01_Overview/)** — Section 2.3 (Unique Identification)
- **[95-00-01-007_DPP_Data_Model_and_Identifiers.md](../../95-00-01_Overview/)** — UUID specification
- **[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)** (Regulation EU 2024/1689) — Article 11 (High-risk AI documentation)
- **[EU DPP Framework](https://ec.europa.eu/commission/presscorner/detail/en/ip_2024_1689)** (Regulation EU 2024/1781) — Article 8 (Unique product identifiers)
- **[RFC 4122](https://www.rfc-editor.org/rfc/rfc4122)** — A Universally Unique Identifier (UUID) URN Namespace
- **[ISO/IEC 19941](https://www.iso.org/standard/66639.html)** — Information technology — Cloud computing — Interoperability and portability

## 5. Acceptance Criteria

- [x] Every DPP record includes a valid UUID conforming to RFC 4122
- [x] No two models in the DPP database share the same UUID
- [ ] UUID is stored in DPP JSON (`uuid` field)
- [ ] UUID is stored in aircraft configuration records
- [ ] UUID is stored in model registry metadata
- [ ] UUID generation occurs at model creation time
- [ ] UUID is immutable once assigned (cannot be changed)
- [ ] UUID format validation is enforced by JSON schema
- [ ] UUID uniqueness is enforced by database constraints

## 6. Verification Method

- **Method**: Analysis + Test
- **Evidence**:
  - JSON Schema validation reports demonstrating `uuid` field enforcement
  - Database uniqueness constraint checks (unit tests)
  - Sample DPP exports showing UUID usage in production
  - Integration test results with model registry
  - Code review showing UUID generation at model creation

### Verification Procedure

1. **Static Analysis**: Review JSON schema to confirm UUID field is mandatory
2. **Unit Test**: Generate 10,000 UUIDs and verify no collisions
3. **Integration Test**: Create multiple models and verify unique UUIDs in database
4. **System Test**: Export DPP records and verify UUID presence and format
5. **Inspection**: Review model registry integration for UUID propagation

## 7. Traceability

- **Design**: 95-00-04-001_DPP_JSON_Schema.json (uuid field specification)
- **Implementation**: 
  - `src/dpp/core/uuid_generator.py` (UUID generation logic)
  - `schema/dpp_v1.0.json` (JSON schema with UUID field)
  - `db/migrations/001_create_dpp_table.sql` (UUID column with UNIQUE constraint)
- **Test**: 
  - TC-95-00-03-001_UUID_Uniqueness_Check
  - TC-95-00-03-001A_UUID_Format_Validation
  - TC-95-00-03-001B_UUID_Immutability_Test
- **Certification**: MoC-95-00-03-001 (traceability evidence package)

## 8. Status

- **Lifecycle State**: `APPROVED`
- **Owner**: Requirements WG / Data Architecture Team
- **Approved By**: Configuration Control Board
- **Approval Date**: 2025-11-17
- **Last Updated**: 2025-11-17
- **Comments**: Approved for implementation. UUID format shall be RFC 4122 version 4 (random).

---

## Document Control

- **Document ID**: RQ-95-00-03-001
- **Version**: 1.0
- **Status**: APPROVED
- **Classification**: Internal Use
- **Change History**:
  - v1.0 (2025-11-17): Initial approved version
