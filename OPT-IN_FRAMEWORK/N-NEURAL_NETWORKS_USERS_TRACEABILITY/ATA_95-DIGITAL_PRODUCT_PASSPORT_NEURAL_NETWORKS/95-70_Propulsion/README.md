# 95-70: Propulsion Digital Product Passport

## Overview

The Propulsion Digital Product Passport (DPP) provides comprehensive documentation and traceability for all propulsion systems (ATA 70-79) within the AMPEL360 BWB H₂ Hy-E Q100 aircraft. This DPP integrates with CAOS (Computer Aided Operations & Services) for AI-powered propulsion optimization and health monitoring.

## Purpose

- **Centralize Documentation**: Aggregate all propulsion system documentation across ATA chapters
- **Enable Traceability**: Link components through entire lifecycle (design → manufacturing → operations → end-of-life)
- **Support Neural Networks**: Provide structured data for AI/ML-based optimization
- **Ensure Compliance**: Maintain regulatory compliance (EASA, FAA, EU AI Act, EU DPP Regulation)
- **Facilitate Circularity**: Track components for recycling and reuse

## Structure

```
95-70_Propulsion/
├── README.md (this file)
├── 95-70-00-001_Propulsion_DPP_Overview.md
├── 95-70-00-002_Propulsion_Scope_and_Boundaries.md
├── 95-70-00-003_Cross_ATA_Propulsion_Map.csv
│
├── 00_META/                                          # Metadata and Governance
│   ├── 95-70-00-004_Propulsion_Taxonomy.md
│   ├── 95-70-00-005_Propulsion_Traceability_Matrix.csv
│   ├── 95-70-00-006_Propulsion_Assets_Registry.json
│   ├── 95-70-00-007_Interfaces_to_Storages_and_Circularity.md
│   └── 95-70-00-008_CAOS_Propulsion_Hooks.md
│
├── 95-70-70_Propulsion_Practices_and_Standards/     # ATA 70
│   ├── README.md
│   ├── 95-70-70-001_Propulsion_Practices_Overview.md
│   ├── 95-70-70-002_Standard_Practices_for_Propulsion_Installations.md
│   ├── 95-70-70-003_Safety_Margins_and_Limits.md
│   ├── 95-70-70-004_Propulsion_Configuration_Baselines.md
│   ├── 95-70-70-005_Links_to_ATA_70_95-00-04_Design_and_95-00-07_VV.md
│   └── ASSETS/
│       ├── 95-70-70-A-001_Propulsion_Practices_BlockDiagram.drawio
│       ├── 95-70-70-A-002_Limits_and_Margins_Table.csv
│       ├── 95-70-70-A-003_Propulsion_Config_Schema.json
│       └── 95-70-70-A-004_Propulsion_Practices_Checklist.md
│
├── 95-70-71_PowerPlant_Integration/                 # ATA 71
│   ├── README.md
│   ├── 95-70-71-001_PowerPlant_Integration_Overview.md
│   ├── 95-70-71-002_Nacelle_Pylon_and_Mounting_Concepts.md
│   ├── 95-70-71-003_Interfaces_with_Structures_95-50-70_and_53.md
│   ├── 95-70-71-004_Access_Maintainability_and_Safety_Envelopes.md
│   ├── 95-70-71-005_Links_to_ATA_71_95-20-70_and_95-10_Operations.md
│   └── ASSETS/
│       ├── 95-70-71-A-001_PowerPlant_Integration_Layout.drawio
│       ├── 95-70-71-A-002_Clearance_and_Envelope_Table.csv
│       └── 95-70-71-A-003_PowerPlant_IFD_Interface_Spec.yaml (placeholder)
│
├── 95-70-72_Engines_and_Propulsors/                 # ATA 72
├── 95-70-73_Engine_Fuel_and_Supply/                 # ATA 73
├── 95-70-75_Bleed_and_Air_Management/               # ATA 75
├── 95-70-76_Propulsion_Control_Systems/             # ATA 76
├── 95-70-77_Propulsion_Indications_and_Health/      # ATA 77
├── 95-70-78_Exhaust_and_Emissions/                  # ATA 78
└── 95-70-79_Lubrication_and_Oil_Systems/            # ATA 79
    └── (Each with README, 5 core documents, and ASSETS folder)
```

## Key Features

### 1. Neural Network Integration

- **CAOS Integration**: Real-time propulsion optimization via AI
- **Predictive Maintenance**: Health monitoring and remaining useful life (RUL) prediction
- **Thrust Optimization**: Fuel efficiency improvements through ML models
- **Digital Twin**: Physics-based simulation with fleet learning

### 2. H₂ Hybrid Propulsion

- **Open-Fan Propulsors**: Counter-rotating, electrically driven
- **Cryogenic Fuel System**: LH₂ at -253°C integration
- **Hybrid Control**: Coordination of fuel cells, batteries, and motors
- **CO₂ Circularity**: Waste heat recovery for carbon capture

### 3. Comprehensive Traceability

- **Component Registry**: JSON-based asset tracking (95-70-00-006)
- **Traceability Matrix**: Requirements → Design → Testing → Certification (95-70-00-005)
- **Cross-ATA Mapping**: Interfaces with 30+ other ATA chapters (95-70-00-003)

### 4. Lifecycle Support

All propulsion systems documented through:
- Requirements and specifications
- Design and interfaces
- Manufacturing and testing
- Operations and maintenance
- End-of-life and recycling

## Quick Start

1. **Overview**: Start with [95-70-00-001_Propulsion_DPP_Overview.md](95-70-00-001_Propulsion_DPP_Overview.md)
2. **Scope**: Review [95-70-00-002_Propulsion_Scope_and_Boundaries.md](95-70-00-002_Propulsion_Scope_and_Boundaries.md)
3. **Taxonomy**: Understand component classification in [00_META/95-70-00-004_Propulsion_Taxonomy.md](00_META/95-70-00-004_Propulsion_Taxonomy.md)
4. **Specific System**: Navigate to relevant ATA chapter folder (70-79)

## Interfaces

### Internal AMPEL360 Systems

- **ATA 28**: H₂ Fuel Storage and Distribution
- **ATA 24**: Electrical Power (fuel cells, generators)
- **ATA 21-80**: CO₂ Capture and Circularity
- **ATA 50-57**: Structures (nacelles, pylons, wings)
- **ATA 42**: Integrated Avionics (data bus interfaces)

### Neural Network Systems

- **95-20-70**: NN Propulsion Optimization
- **95-30-70**: NN Health Monitoring
- **95-60-70**: NN Asset Management

See [95-70-00-003_Cross_ATA_Propulsion_Map.csv](95-70-00-003_Cross_ATA_Propulsion_Map.csv) for complete interface mapping.

## Regulatory Compliance

- **EASA CS-E**: Engine certification
- **EASA CS-25**: Aircraft integration
- **FAA FAR Part 33/25**: US certification
- **EU AI Act**: High-risk AI systems (propulsion control)
- **EU DPP Regulation**: Product passport requirements
- **ISO 19881**: Gaseous hydrogen fuel containers

## Document Control

- **Owner**: AMPEL360 Propulsion Systems Engineering
- **Status**: Active
- **Standard**: OPT-IN Framework v1.1
- **Last Updated**: 2025-11-17
- **Review Cycle**: Quarterly

## Related Documentation

- [ATA 95 General Requirements](../95-00_GENERAL/95-00-03_Requirements/)
- [CAOS AI Integration](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/I2-R_AND_D/ATA_40-AI_INTEGRATION/)
- [Physical Propulsion Systems](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/)
- [AMPEL360 Documentation Standard](../../../../AMPEL360_DOCUMENTATION_STANDARD.md)

## Version History

| Version | Date       | Author               | Changes                          |
|---------|------------|----------------------|----------------------------------|
| 1.0     | 2025-11-13 | AMPEL360 Doc WG      | Initial bucket creation          |
| 2.0     | 2025-11-17 | AMPEL360 Doc Team    | Complete DPP structure implemented |

---

**Bucket**: 95-70_Propulsion  
**ATA Chapters**: 70-79  
**Classification**: Internal Use  
**Next Review**: 2026-02-17
