# 85-80-07-001 UPS Systems

## Document Information

- **Document ID**: 85-80-07-001
- **Title**: Uninterruptible Power Supply Standards
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

Standards for UPS systems ensuring continuity of critical loads.

## UPS Topologies

### Online Double-Conversion

- **Application**: Critical systems (ATC, fire safety, security)
- **Efficiency**: 94-96% at full load, 97-99% in eco-mode
- **Transfer Time**: Zero (continuous operation)
- **Standards**: [IEC 62040-3](https://www.iec.ch/)

### Line-Interactive

- **Application**: IT equipment, telecommunications
- **Efficiency**: 95-98%
- **Transfer Time**: <4 ms

### Offline (Standby)

- **Application**: Non-critical workstations
- **Transfer Time**: <10 ms

## Battery Systems

- **Technology**: VRLA or lithium-ion
- **Backup Time**: 10-30 minutes typical (bridge to generator)
- **Sizing**: 125% of connected load for future growth
- **Temperature**: 20-25°C for optimal life

## Maintenance

- Annual battery testing and capacity verification
- Periodic load bank testing
- Replacement per manufacturer recommendations (5-10 years VRLA, 10-15 years Li-ion)

## Standards

- [IEC 62040](https://www.iec.ch/) - Uninterruptible power systems
- [IEEE 446 (Orange Book)](https://standards.ieee.org/) - Emergency and standby power

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.
