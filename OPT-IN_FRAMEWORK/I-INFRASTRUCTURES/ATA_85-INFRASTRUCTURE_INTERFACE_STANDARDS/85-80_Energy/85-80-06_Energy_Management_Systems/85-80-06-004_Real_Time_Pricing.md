# 85-80-06-004 Real-Time Pricing

## Document Information

- **Document ID**: 85-80-06-004
- **Title**: Real-Time Pricing Integration Standards
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

Standards for integrating real-time pricing signals into energy management decisions.

## Pricing Mechanisms

### Time-of-Use (TOU) Tariffs

- On-peak, mid-peak, off-peak periods
- Seasonal variations
- Fixed schedule published in advance

### Real-Time Pricing (RTP)

- Hourly or sub-hourly electricity prices
- Based on wholesale market conditions
- Day-ahead and hour-ahead pricing

### Critical Peak Pricing (CPP)

- Higher rates during system stress events
- Limited number of events per year
- Advance notification required

## Integration

- Automatic load adjustment based on price signals
- Battery storage charge/discharge optimization
- Load shifting to low-price periods
- Integration with [85-80-06-003 Optimization Algorithms](./85-80-06-003_Optimization_Algorithms.md)

## Communication

- Price signal delivery via API, email, or SMS
- OpenADR protocol for automated DR
- Integration with utility billing systems

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
