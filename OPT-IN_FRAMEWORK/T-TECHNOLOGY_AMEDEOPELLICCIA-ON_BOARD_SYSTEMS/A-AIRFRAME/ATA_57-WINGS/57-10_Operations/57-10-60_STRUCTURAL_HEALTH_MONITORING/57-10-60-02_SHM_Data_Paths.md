# 57-10-60-02 — SHM Data Paths

## Purpose

Define the data paths for Structural Health Monitoring (SHM) data from
sensors to analysis systems, including OFEC integration.

## On-Aircraft Data Flow

### Sensor to Concentrator

| Sensor Group | Concentrator | Interface |
|--------------|--------------|-----------|
| Root zone | SHM-CU-01 | Fiber/analog |
| Inboard zone | SHM-CU-01 | Fiber/analog |
| Mid-span zone | SHM-CU-02 | Fiber/analog |
| Outboard zone | SHM-CU-02 | Fiber/analog |
| Tip zone | SHM-CU-02 | Fiber/analog |

### Concentrator to Processor

| Path | Rate | Protocol |
|------|------|----------|
| SHM-CU-01 → SHM-P | 10 Hz | AFDX |
| SHM-CU-02 → SHM-P | 10 Hz | AFDX |

### Processor Outputs

| Destination | Content | Rate |
|-------------|---------|------|
| EICAS | Alert discretes | Event |
| FDR | Key parameters | 1 Hz |
| QAR | Full dataset | 10 Hz |
| OFEC publisher | Selected data | 1 Hz |

## OFEC Integration

SHM data flows to ground systems via OFEC:

### 23-95-60-60_OFEC Interface

| Component | Function | Data Content |
|-----------|----------|--------------|
| 60-60-10_AIRCRAFT_PUBLISHER | Transmit SHM summary | Key strains, alerts |
| 60-60-20_GROUND_RECEIVER | Receive and store | Full SHM dataset |

### Data Package

| Field | Type | Units | Rate |
|-------|------|-------|------|
| timestamp | ISO 8601 | UTC | Per sample |
| flight_phase | enum | - | Per sample |
| sensor_id | string | - | Per sample |
| value | float | sensor-specific | Per sample |
| status | enum | - | Per sample |

## Ground Processing

### Real-Time Processing

| Function | System | Latency |
|----------|--------|---------|
| Alert detection | Ground SHM server | < 1 s |
| Usage index update | Analytics | < 10 s |
| Fleet comparison | Fleet monitor | < 60 s |

### Post-Flight Processing

| Function | System | Timing |
|----------|--------|--------|
| Full data download | QAR ingest | Post-flight |
| Detailed analysis | Engineering workstation | As required |
| Trend analysis | Analytics platform | Daily |

## Data Retention

| Data Type | On-Aircraft | Ground | Archive |
|-----------|-------------|--------|---------|
| Alerts | Last 100 | 1 year | Permanent |
| Summary | Last 50 flights | 5 years | Permanent |
| Raw data | Current flight | 90 days | As required |

## References

- 23-95-60-60_OFEC (telemetry transport)
- [57-10-60-01_SHM_Sensor_Layout](./57-10-60-01_SHM_Sensor_Layout.md)
- [57-10-60-03_SHM_Alarm_Policies](./57-10-60-03_SHM_Alarm_Policies.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

---
