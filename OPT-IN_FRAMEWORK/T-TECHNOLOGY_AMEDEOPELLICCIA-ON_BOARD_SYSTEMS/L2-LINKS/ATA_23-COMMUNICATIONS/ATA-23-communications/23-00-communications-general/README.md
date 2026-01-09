# 23-00 Communications — General

## Briefing

Chapter-level scope, architecture, partitioning, standards, redundancy, dispatch philosophy, and cross-system dependencies for aircraft communications.

## Table of Contents (Suggested)

1. **Scope and Boundaries**
   - What is ATA 23 vs ATA 31/34/42/46
   - System boundaries and interfaces

2. **High-Level Communications Architecture**
   - Voice/data/cabin/service communications overview
   - System integration philosophy

3. **Network Segmentation**
   - Flight deck communications domain
   - Cabin communications domain
   - Maintenance communications domain

4. **Antenna/Radio Placement Philosophy**
   - BWB-specific considerations
   - Blockage and shadowing analysis
   - RF interference mitigation

5. **Power, Cooling, and Environmental Constraints**
   - ATA 24 (Electrical) interfaces
   - ATA 21 (ECS) interfaces
   - Environmental operating limits

6. **HMI/Annunciation Overview**
   - Interfaces to ATA 31 (Instruments)
   - Crew interface philosophy
   - Warning and caution logic

7. **Maintainability Concept + BITE Overview**
   - Built-in test equipment strategy
   - Fault isolation philosophy
   - Maintenance access requirements

8. **Cyber/Security Cross-Reference Policy**
   - Link to B30/ATA 46 governance
   - Domain separation requirements
   - Secure communications policy

9. **Compliance Basis and Certification Assumptions**
   - Applicable regulations (CS-25, FAA Part 25)
   - Certification approach
   - Special conditions and exemptions

10. **Top-Level Verification Strategy**
    - Analysis requirements
    - Test requirements
    - Inspection requirements

## BWB + H₂ Fuel-Cell/Electric Program Considerations

### EMC/EMI and Conducted Noise
- Higher-risk environment due to HV switching/inverters
- Make this a first-class requirement and verification stream
- Establish noise immunity requirements for all communications equipment

### Antenna Placement on BWB
- Different blockage/shadowing constraints
- Structural integration challenges
- Treat as design drivers for 23-10/15

### Domain Segregation
- Keep ATA 23 functional scope clean
- Place cybersecurity controls under B30 governance (or ATA 46)
- Cross-reference from ATA 23

## Subject Structure

This section contains:
- `23-00-00-communications-general/` — General communications documentation

## Document Control

- **ATA Chapter**: 23
- **Section**: 23-00
- **Title**: Communications — General
- **Status**: Active
- **Standard**: ATA iSpec 2200 SNS Extract (Revision 2024-1)
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia
