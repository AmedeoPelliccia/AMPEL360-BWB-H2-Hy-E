# 85-80-03-001 Utility Interconnection

## Document Information

- **Document ID**: 85-80-03-001
- **Title**: Utility Grid Interconnection Standards
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

Standards for interconnecting airport energy systems with the utility grid.

## Technical Requirements

### Interconnection Agreement

- Utility service agreement and technical specifications
- Point of common coupling (PCC) definition
- Protection and metering requirements
- Operating protocols and communication

### Protection Systems

- Anti-islanding protection per [IEEE 1547](https://standards.ieee.org/)
- Undervoltage/overvoltage trip settings
- Frequency protection (under/over frequency)
- Transfer trip schemes for grid faults

### Power Quality

- Voltage regulation: ±5% at PCC
- Harmonics per [IEEE 519](https://standards.ieee.org/): THD <5%
- Flicker per [IEC 61000-4-15](https://www.iec.ch/): Pst <1.0
- Power factor: 0.95 lagging to 0.95 leading

## Metering and Communication

- Revenue-grade metering at PCC
- Real-time data exchange with utility SCADA
- DNP3 or IEC 61850 communication protocol

## Standards

- [IEEE 1547](https://standards.ieee.org/) - DER interconnection
- [IEEE 519](https://standards.ieee.org/) - Harmonic control
- [IEC 61000](https://www.iec.ch/) - EMC standards

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
