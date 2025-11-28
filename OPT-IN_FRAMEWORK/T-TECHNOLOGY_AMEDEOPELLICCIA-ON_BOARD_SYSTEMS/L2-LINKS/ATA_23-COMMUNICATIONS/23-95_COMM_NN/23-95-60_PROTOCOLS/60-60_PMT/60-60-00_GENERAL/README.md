# 60-60-00_GENERAL — PMT Overview

## Purpose

This directory contains the general overview, architecture documentation, and diagrams for the Predictive Maintenance Telemetry (PMT) protocol.

## Contents

| Folder | Purpose |
|--------|---------|
| diagrams/ | Architecture and data flow diagrams (SVG format) |

## PMT Architecture Overview

The PMT protocol enables real-time and batch transmission of aircraft health data across the four-tier CFLF architecture:

1. **Aircraft Tier**: Collects structural strain, thermal, cycle counter, and H2 system data
2. **Ground Tier**: Validates and ingests telemetry data streams
3. **Regional Tier**: Aggregates fleet data and performs trend analysis
4. **Fleet Tier**: Runs predictive models for RUL estimation and maintenance planning

## Key Performance Requirements

| Metric | Target | Notes |
|--------|--------|-------|
| Telemetry latency (A→G) | < 5 min | Best-effort during cruise |
| Data validation accuracy | > 99.9% | Ground ingestion validation |
| Anomaly detection latency | < 1 hour | Regional aggregator processing |
| RUL update frequency | Daily | Fleet analytics cycle |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
