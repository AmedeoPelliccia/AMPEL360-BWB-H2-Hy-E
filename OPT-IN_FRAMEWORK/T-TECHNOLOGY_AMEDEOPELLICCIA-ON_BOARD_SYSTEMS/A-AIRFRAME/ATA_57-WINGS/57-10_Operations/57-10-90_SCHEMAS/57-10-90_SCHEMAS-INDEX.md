# 57-10-90 — Schemas Index

## Purpose

Index of JSON schemas used for wing operations data exchange.

## Schema Catalog

| Schema ID | File | Description |
|-----------|------|-------------|
| wing_ops_state | [57-10-90_wing_ops_state.schema.json](./57-10-90_wing_ops_state.schema.json) | Wing operational state |
| wing_margin_event | [57-10-90_wing_margin_event.schema.json](./57-10-90_wing_margin_event.schema.json) | Margin exceedance events |
| shm_alert | [57-10-90_shm_alert.schema.json](./57-10-90_shm_alert.schema.json) | SHM alert messages |
| lifecycle_counter | [57-10-90_lifecycle_counter.schema.json](./57-10-90_lifecycle_counter.schema.json) | Lifecycle usage counters |

## Schema Versioning

| Schema | Current Version | Last Updated |
|--------|-----------------|--------------|
| wing_ops_state | 1.0.0 | 2025-11-28 |
| wing_margin_event | 1.0.0 | 2025-11-28 |
| shm_alert | 1.0.0 | 2025-11-28 |
| lifecycle_counter | 1.0.0 | 2025-11-28 |

## Usage

These schemas are used for:
- Data validation in OFEC pipelines
- CAOS event formatting
- MMIP capsule content validation
- Fleet analytics data exchange

## References

- [57-10-60_STRUCTURAL_HEALTH_MONITORING](../57-10-60_STRUCTURAL_HEALTH_MONITORING/)
- [57-10-70_LIFECYCLE_ANALYTICS](../57-10-70_LIFECYCLE_ANALYTICS/)
- [57-10-80_CAOS_INTEGRATION](../57-10-80_CAOS_INTEGRATION/)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

---
