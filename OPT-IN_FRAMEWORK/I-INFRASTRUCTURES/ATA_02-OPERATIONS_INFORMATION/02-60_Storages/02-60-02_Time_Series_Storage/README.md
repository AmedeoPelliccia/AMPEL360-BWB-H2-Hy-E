# 02-60-02 – Time-Series Storage

## Purpose

This directory defines the time-series storage infrastructure for AMPEL360 operational telemetry and metrics. It covers storage for aircraft sensor data, operations metrics, H₂ system monitoring, and predictive analytics inputs using TimescaleDB and InfluxDB.

---

## Scope

Time-series storage encompasses:

- **Aircraft Telemetry**: Sensor data from flight operations (ACARS, aircraft systems)
- **Operations Metrics**: Turnaround times, fuel consumption, performance KPIs
- **H₂ System Monitoring**: Hydrogen system telemetry and safety parameters
- **Predictive Analytics**: ML feature inputs and time-series forecasting data
- **Infrastructure Metrics**: System performance and health monitoring

---

## Key Documents

- **[02-60-02-001_TimescaleDB_Architecture.md](./02-60-02-001_TimescaleDB_Architecture.md)** – Architecture, sharding, hypertables, retention policies
- **[02-60-02-002_Data_Retention_Policy.md](./02-60-02-002_Data_Retention_Policy.md)** – Hot/warm/cold retention tiers
- **[02-60-02-003_Compression_Strategy.md](./02-60-02-003_Compression_Strategy.md)** – Compression configuration and trade-offs
- **[02-60-02-004_Query_Optimization.md](./02-60-02-004_Query_Optimization.md)** – Query patterns and indexing strategies

---

## ASSETS

### Schema
- **02-60-02-A-001_Time_Series_Schema.sql** – Schema for flight/operations metrics
- **02-60-02-A-002_Hypertables_Design.sql** – Hypertable partitioning examples
- **02-60-02-A-003_Continuous_Aggregates.sql** – Continuous aggregate definitions

### Performance
- **02-60-02-A-101_Compression_Ratio_Analysis.xlsx** – Compression analysis per table
- **02-60-02-A-102_Query_Performance.pdf** – Query performance test results

---

## Technology Stack

- **TimescaleDB** 2.x (PostgreSQL extension for time-series)
- **InfluxDB** 2.x (alternative for specific high-volume streams)
- **Grafana** (visualization and dashboards)

---

## Retention Policy

| Tier | Duration | Compression | Use Case |
|------|----------|-------------|----------|
| Hot | 7 days | None | Real-time operations, alerts |
| Warm | 90 days | 5:1 | Recent analytics, troubleshooting |
| Cold | 2 years | 10:1 | Historical analysis, compliance |

---

## Performance Targets

- **Ingestion Rate**: 100,000+ metrics/second sustained
- **Query Latency**: < 500ms for 24-hour aggregates
- **Compression Ratio**: 10:1 average
- **Availability**: 99.9%

---

## References

- [02-60-00-001 Storage Architecture Overview](../02-60-00-001_Storage_Architecture_Overview.md)
- [02-60-01 Primary Data Storage](../02-60-01_Primary_Data_Storage/)
- [TimescaleDB Documentation](https://docs.timescale.com/)
- [InfluxDB Documentation](https://docs.influxdata.com/)

---

## Document Control

- **Directory**: 02-60-02_Time_Series_Storage
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
