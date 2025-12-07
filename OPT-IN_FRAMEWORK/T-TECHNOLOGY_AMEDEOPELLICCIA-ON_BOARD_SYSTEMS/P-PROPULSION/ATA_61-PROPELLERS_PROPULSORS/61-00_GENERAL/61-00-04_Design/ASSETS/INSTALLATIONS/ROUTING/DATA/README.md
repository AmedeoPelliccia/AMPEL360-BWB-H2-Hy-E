# DATA ROUTING

## Purpose

This directory contains routing specifications for all data communications in the propulsion system, including FADEC, health monitoring, and avionics interfaces.

## Contents

| Document | Description |
|----------|-------------|
| Q100-61-RTE-DATA-FADEC-BUS.md | FADEC control bus routing |
| Q100-61-RTE-DATA-HEALTH-MON.md | Health monitoring data |
| Q100-61-RTE-DATA-ARINC-429.md | ARINC-429 avionics interface |

## Data Bus Standards

### FADEC Bus (CAN)

- Protocol: CAN 2.0B
- Baud rate: 1 Mbit/s
- Redundancy: Dual bus
- Termination: 120Ω at each end

### Health Monitoring

- Protocol: Ethernet (100BASE-T)
- Data rate: 100 Mbit/s
- Interface: Onboard data recorder

### ARINC-429

- Standard: ARINC-429
- Speed: High speed (100 kbit/s)
- Interface: Aircraft avionics

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
