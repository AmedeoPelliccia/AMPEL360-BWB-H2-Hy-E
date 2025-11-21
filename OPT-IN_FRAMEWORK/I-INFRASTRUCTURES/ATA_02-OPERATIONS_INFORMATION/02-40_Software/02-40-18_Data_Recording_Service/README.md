# 02-40-18 – Data Recording Service

## Purpose

This folder contains the operational data recording service that logs events, stores time-series data, and interfaces with the Digital Product Passport (DPP) for immutable audit trails and compliance.

---

## Scope

- **Event Logger**: Operational event logging with correlation IDs
- **Time-Series Database**: High-performance time-series data storage
- **DPP Interface**: Integration with blockchain-based Digital Product Passport
- **Query API**: Historical data retrieval for analytics and audits
- **Compliance**: Retention policies for regulatory compliance

---

## Documentation Files

- **[02-40-18-001_Recording_Architecture.md](02-40-18-001_Recording_Architecture.md)**: Data recording architecture
- **[02-40-18-002_Event_Logger.md](02-40-18-002_Event_Logger.md)**: Event logging schema and correlation
- **[02-40-18-003_Time_Series_DB.md](02-40-18-003_Time_Series_DB.md)**: Time-series database design
- **[02-40-18-004_DPP_Interface.md](02-40-18-004_DPP_Interface.md)**: Digital Product Passport integration

---

## ASSETS Structure

### Source_Code/
- **event_collector/**: Event collection agents and sidecars
- **timeseries_writer/**: Time-series database writers (InfluxDB, TimescaleDB)
- **dpp_client/**: DPP/blockchain integration client

---

## Integration

Receives data from:
- All 02-40 subsystems (events, metrics, logs)
- **[ATA 31 FDR](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/D-DATA/ATA_31-INDICATING_RECORDING_RECORDING_FUNCTION/)**: Flight data recorder events

Provides data to:
- **[02-40-19 Analytics Engine](../02-40-19_Analytics_Engine/)**: Historical analysis
- **[02-40-23 Predictive Ops](../02-40-23_Predictive_Ops_Software/)**: ML training data
- **[ATA 95 DPP](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)**: Event anchoring

---

## References

- [ATA 95 Digital Product Passport](../../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206) – Data governance requirements

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: _2025-11-21_.
