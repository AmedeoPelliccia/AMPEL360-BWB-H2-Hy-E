# ATA 23 — COMMUNICATIONS

## Overview

This directory contains the complete **ATA 23 Communications** system documentation following the **AMPEL360 SBJ (Subject) Code Assignment** structure. The organization maps each Table of Contents (TOC) bullet to a specific **23-xx-yy** subject code for complete traceability and navigability.

## Structure

The ATA 23 Communications chapter is organized into the following major sections:

### 23-00 — Communications General
Foundation and cross-cutting concerns for the communications system.

**Subject Codes (yy):** 00-10, 90-92
- Scope, architecture, network segmentation
- EMC/EMI considerations for BWB and electric propulsion
- Antenna placement philosophy
- Cyber security and compliance basis

### 23-10 — Speech Communications
Voice communication systems for flight crew and ATC.

**Subject Codes (yy):** 00-07, 10, 90
- VHF and HF voice radios
- Audio endpoints and RF distribution
- Recording/monitoring policy
- EMC/EMI constraints

### 23-15 — SATCOM
Satellite communication systems for voice, data, and IP services.

**Subject Codes (yy):** 00-07, 10
- Antenna/radome/steering with BWB considerations
- RF chain and network interfaces
- Security policy and fault handling
- Dispatch/MEL requirements

### 23-20 — Data Transmission and Automatic Calling
Datalink, ATSU/CMU, and automatic calling (SELCAL) systems.

**Subject Codes (yy):** 00-08, 10
- ATSU/CMU architecture
- VDL/SATCOM bearer integration
- Message security and integrity
- Logging and traceability

### 23-30 — Passenger Address, Entertainment and Comfort
Cabin communication, PA systems, and IFE boundaries.

**Subject Codes (yy):** 00-07, 10
- PA architecture and zoning
- Audio distribution and priority
- Cabin segmentation and safety isolation
- Emergency/fallback power

### 23-40 — Interphone
Flight, cabin, service, and maintenance interphone systems.

**Subject Codes (yy):** 00-06, 10
- Interphone types and station hardware
- Routing and priority logic
- Audio integration and emergency power
- BITE/troubleshooting

### 23-50 — Audio Integrating
Audio Management Unit (AMU) and Audio Control Panel (ACP) systems.

**Subject Codes (yy):** 00-06, 10, 90
- AMU/ACP concept and I/O inventory
- Mixing and priority rules
- BITE and degradation management
- EMC/EMI and noise management (electric propulsion environment)

### 23-60 — Static Discharging
Static discharge devices and RF performance interaction.

**Subject Codes (yy):** 00-04, 10
- Device inventory and placement
- Bonding/grounding impacts on RF
- Inspection and maintenance
- Noise reduction evidence

### 23-70 — Audio and Video Monitoring
Cabin/door/service monitoring systems.

**Subject Codes (yy):** 00-05, 10
- Video chain and audio monitoring
- Privacy/security policy
- Failure/dispatch impacts
- Latency and quality verification

### 23-80 — Integrated Automatic Tuning
Radio auto-tuning systems and database integration.

**Subject Codes (yy):** 00-04, 10
- Functional scope and limits
- Interfaces to radios and databases (ATA 34)
- HMI authority rules
- Failure modes and prevention

## Directory Structure

Each subject code folder (23-xx-yy) contains:

```
23-xx-yy-descriptive-name/
├── SSOT/                              # Single Source of Truth
│   ├── LC01_Requirements/
│   ├── LC02_System_Requirements/
│   ├── LC03_Design/
│   ├── LC04_Analysis/
│   ├── LC05_VnV/
│   ├── LC06_Quality/
│   ├── LC07_Safety/
│   └── LC08_Certification/
└── PUB/                               # Publications
    ├── AMM/                           # Aircraft Maintenance Manual
    │   ├── CSDB/                      # Common Source Database
    │   │   ├── DM/                    # Data Modules
    │   │   ├── PM/                    # Publication Modules
    │   │   ├── DML/                   # Data Module Lists
    │   │   ├── ICN/                   # Illustrations
    │   │   ├── BREX/                  # Business Rules
    │   │   ├── COMMON/                # Common information
    │   │   └── APPLICABILITY/         # Applicability statements
    │   ├── EXPORT/                    # Export/publication outputs
    │   ├── bindings.csv
    │   └── csdb.profile.yaml
    └── IPC/                           # Illustrated Parts Catalog
        ├── CSDB/                      # (same structure as AMM)
        ├── EXPORT/
        ├── bindings.csv
        └── csdb.profile.yaml
```

## Governance Note

This is an **AMPEL360 internal SBJ allocation for scaffolding**. If your licensed **SNS (System Numbering Standard) extract** already assigns official 5th–6th digit subjects for ATA 23, reconcile or rename to match it.

**Reserved codes:** yy=90–99 are reserved for **program-specific deltas** (e.g., BWB antenna blockage, EMC/EMI considerations for electric propulsion).

## Key Features

### BWB-Specific Considerations
- **23-00-91**: BWB antenna blockage and shadowing analysis
- **23-15-02**: SATCOM antenna pointing with BWB geometry constraints
- Antenna placement philosophy across the blended wing body configuration

### Electric Propulsion Environment
- **23-00-90**: EMC/EMI program delta for HV switching and inverter noise
- **23-10-90**: Speech communications EMC/EMI constraints
- **23-50-90**: Audio integrating EMC/EMI and noise management

### Safety and Security
- **23-00-08**: Cyber/security cross-reference to B30/ATA-46 governance
- **23-00-92**: Domain segregation (safety vs cabin vs maintenance isolation)
- **23-20-05**: Message security and integrity controls
- **23-30-03**: Cabin segmentation and safety-critical isolation

## Standards and Compliance

Communications systems must comply with:
- **CS-25.1309**: Equipment, systems, and installations
- **DO-160**: Environmental conditions and test procedures
- **DO-178C**: Software considerations in airborne systems
- **DO-254**: Design assurance for airborne electronic hardware
- **RTCA DO-290C**: Air-ground datalink communications
- **EUROCAE ED-120**: SATCOM safety and performance standards
- **ATA iSpec 2200**: Maintenance information standards
- **S1000D**: Technical publication specification

Refer to **23-00-09** (Compliance basis) for complete regulatory mapping.

## Cross-References

### Related ATA Chapters
- **ATA 21**: Air Conditioning (power/cooling interfaces)
- **ATA 24**: Electrical Power (power distribution, emergency power)
- **ATA 31**: Indicating/Recording Systems (HMI, annunciations)
- **ATA 34**: Navigation (FMS integration, databases)
- **ATA 42**: Integrated Modular Avionics (IMA hosting)
- **ATA 46**: Information Systems (cyber security, data management)

### Internal Cross-References
- **23-40-04** → **23-50**: Interphone audio integration
- **23-10-06** → Recorder interfaces (if ATA 31 or dedicated recorder)
- **23-80-02** → **ATA 34**: Navigation database interfaces

## Document Control

- **ATA Chapter**: 23 — Communications
- **Structure Standard**: AMPEL360 SBJ Code Assignment
- **Status**: Active
- **Owner**: AMPEL360 Communications System WG
- **Version**: 1.0
- **Date**: 2026-01-09
- **Repository**: AMPEL360-AIR-T

## Usage

1. **For Requirements**: Navigate to `23-xx-yy-*/SSOT/LC01_Requirements/`
2. **For Design**: Navigate to `23-xx-yy-*/SSOT/LC03_Design/`
3. **For Maintenance**: Navigate to `23-xx-yy-*/PUB/AMM/`
4. **For Parts**: Navigate to `23-xx-yy-*/PUB/IPC/`
5. **For Verification**: Navigate to `23-xx-yy-*/SSOT/LC05_VnV/`

## Contributing

When adding documentation:
1. Use the correct **23-xx-yy** subject code
2. Place content in the appropriate lifecycle folder (LC01-LC08) or publication folder (AMM/IPC)
3. Maintain traceability with clear cross-references
4. Update this index when adding new subjects

---

**For detailed subject code mapping, see:** [00_INDEX.md](./00_INDEX.md)
