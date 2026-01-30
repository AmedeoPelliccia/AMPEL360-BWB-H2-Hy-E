# 23-95-69-SCHEMAS

## Purpose

This directory contains the master data schemas for the COMM_NN protocols,
defining data structures used across all PMT layers.

## Schema Categories

| Schema Type | Format | Description |
|-------------|--------|-------------|
| Telemetry | JSON Schema | Aircraft sensor data formats |
| Ingestion | Avro | Ground station data formats |
| Aggregation | Parquet | Regional aggregation formats |
| Analytics | Protobuf | Fleet analytics data formats |
| Security | X.509/JWT | Authentication token formats |

## Schema Versioning

Schemas follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes requiring consumer updates
- **MINOR**: Backward-compatible additions
- **PATCH**: Backward-compatible fixes

## Cross-References

| Schema | Used By |
|--------|---------|
| telemetry.v1.json | 23-95-61 Aircraft Telemetry |
| ingestion.v1.avsc | 23-95-62 Ground Ingestion |
| aggregation.v1.parquet | 23-95-63 Regional Aggregator |
| analytics.v1.proto | 23-95-64 Fleet Analytics |
| security.v1.yaml | 23-95-65 Security |

## Related Sections

- [97-40-49-SCHEMAS](../../../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_97-NEURAL_NETWORK_MODELS/97-40_Software/97-40-40_PREDICTIVE_MAINTENANCE/97-40-49-SCHEMAS/) — Model schemas

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
