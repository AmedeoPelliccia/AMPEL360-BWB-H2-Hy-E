# 23-15 SATCOM

## Briefing

Satellite communications terminals and services supporting voice and/or datalink, including antenna/steering constraints and service availability management.

## Table of Contents (Suggested)

1. **SATCOM Service Scope**
   - Voice over SATCOM
   - ACARS over satellite
   - IP data services
   - Operational link services

2. **Antenna Subsystem**
   - Radome and installation
   - Antenna steering mechanisms
   - Blockage zones analysis (BWB-specific)
   - Tracking performance requirements

3. **RF Chain**
   - SDU (Satellite Data Unit)
   - HPA (High Power Amplifier)
   - LNA (Low Noise Amplifier)
   - Diplexers and filters
   - Cabling and lightning bonding

4. **Network Interfaces**
   - Datalink routers integration
   - IMA hosting considerations (if applicable)
   - Network topology
   - Quality of Service (QoS) management

5. **Security Policy Reference**
   - Credentialing and authentication
   - Key management
   - Domain separation requirements
   - Cross-reference to B30/ATA 46 governance

6. **Fault Handling**
   - Signal reacquisition logic
   - Fallback communication paths
   - Inhibit logic and procedures
   - System health monitoring

7. **Dispatch and MEL Considerations**
   - Minimum equipment requirements
   - Dispatch conditions
   - Operational limitations
   - Deferral procedures

8. **Verification and Validation**
   - Coverage analysis
   - Handover testing
   - Blockage analysis (BWB geometry)
   - Thermal and power testing

## BWB + H₂ Considerations

- **Antenna Blockage**: BWB configuration requires careful analysis of antenna blockage zones
- **Structural Integration**: SATCOM radome integration with BWB upper surface
- **Power Budget**: Consider impact of electric propulsion on available electrical power

## Subject Structure

This section contains:
- `23-15-00-satcom-general/` — General SATCOM documentation

## Document Control

- **ATA Chapter**: 23
- **Section**: 23-15
- **Title**: SATCOM
- **Status**: Active
- **Standard**: ATA iSpec 2200 SNS Extract (Revision 2024-1)
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
