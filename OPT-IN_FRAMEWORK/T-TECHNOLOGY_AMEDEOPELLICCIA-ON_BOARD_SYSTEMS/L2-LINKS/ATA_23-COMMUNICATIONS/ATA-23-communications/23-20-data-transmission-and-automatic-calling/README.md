# 23-20 Data Transmission and Automatic Calling

## Briefing

Aircraft **datalink and "automatic calling"** functions (classically ACARS/ATSU-related flows and SELCAL), message routing, and operational communications automation.

## Table of Contents (Suggested)

1. **Functional Scope**
   - Datalink services overview
   - Addressing schemes
   - Store-and-forward mechanisms
   - Message prioritization

2. **ATSU/CMU Architecture**
   - Air Traffic Services Unit (ATSU) architecture
   - Communications Management Unit (CMU)
   - Hosting model (if separate from IMA)
   - Redundancy and failover

3. **ACARS / Datalink Network Interfaces**
   - VDL (VHF Data Link) Mode 2
   - SATCOM bearer cross-links
   - HF datalink (if applicable)
   - Network selection logic

4. **Automatic Calling**
   - SELCAL (Selective Calling) concepts
   - SELCAL code management
   - HF SELCAL interactions (cross-ref 23-10)
   - Alert and annunciation

5. **Message Security and Integrity**
   - Message authentication
   - Integrity checking
   - Policy cross-reference (B30/ATA 46)
   - Secure datalink considerations

6. **Integration with FMS/Navigation**
   - ATA 34 (Navigation) interfaces
   - Cockpit HMI (ATA 31) integration
   - Automatic position reporting
   - Flight plan uplink/downlink

7. **Logging/Traceability Requirements**
   - Operational logging
   - Compliance logging
   - Audit trail requirements
   - Data retention policies

8. **Failure Modes**
   - Message loss handling
   - Duplication detection
   - Stale data handling
   - Message rerouting

9. **Verification and Validation**
   - Latency testing
   - Throughput testing
   - Reliability testing
   - Loss recovery testing
   - Cybersecurity testing

## BWB + H₂ Considerations

- **EMC/EMI**: Ensure datalink equipment is immune to electric propulsion system noise
- **Network Architecture**: Consider hydrogen fuel system monitoring data transmission requirements

## Subject Structure

This section contains:
- `23-20-00-data-transmission-general/` — General data transmission and automatic calling documentation

## Document Control

- **ATA Chapter**: 23
- **Section**: 23-20
- **Title**: Data Transmission and Automatic Calling
- **Status**: Active
- **Standard**: ATA iSpec 2200 SNS Extract (Revision 2024-1)
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
