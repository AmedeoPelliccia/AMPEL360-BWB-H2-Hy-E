# Schemas Index

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-97-40-40-90-SPEC-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Overview

This directory contains JSON schemas for all data structures used by the Envelope Analytics subsystem (97-40-40).

---

## 2. Schema Catalog

| Schema | Purpose | Used By |
|--------|---------|---------|
| envelope_state.schema.json | Complete envelope state message | OFEC output |
| margin_data.schema.json | Individual margin data | Margin calculator |
| advisory_event.schema.json | Advisory events | Advisory engine |
| performance_report.schema.json | Performance reports | Post-flight analysis |
| prediction.schema.json | Predictive dynamics output | Predictor |

---

## 3. Schema Versions

All schemas follow semantic versioning:
- Current version: 1.0.0
- Compatible with OFEC Protocol schemas in L2-LINKS

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
