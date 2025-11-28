# 60-60-90_SCHEMAS — PMT Data Schemas

## Purpose

This directory contains the master data schemas for the Predictive Maintenance Telemetry (PMT) protocol, defining data structures used across all PMT layers.

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

## Schema Registry

All schemas are registered in the central schema registry for:

- Version management
- Compatibility checking
- Schema evolution tracking
- Consumer notification

## Cross-References

| Schema | Used By |
|--------|---------|
| telemetry.v1.json | 60-60-10 Aircraft Telemetry |
| ingestion.v1.avsc | 60-60-20 Ground Ingestion |
| aggregation.v1.parquet | 60-60-30 Regional Aggregator |
| analytics.v1.proto | 60-60-40 Fleet Analytics |
| security.v1.yaml | 60-60-50 Security |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
