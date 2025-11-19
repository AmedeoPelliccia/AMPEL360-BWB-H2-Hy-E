# 95-70-00-001: Propulsion DPP Overview

## 1. Introduction

This document provides a comprehensive overview of the Propulsion Digital Product Passport (DPP) within the AMPEL360 BWB H₂ Hy-E Q100 aircraft framework. The Propulsion DPP serves as the central repository for all propulsion-related documentation, traceability, and lifecycle information within ATA 95 (Neural Networks & Digital Product Passport).

## 2. Purpose

The Propulsion DPP aims to:

- **Centralize Documentation**: Aggregate all propulsion system documentation across ATA 70-79
- **Enable Traceability**: Link propulsion components to design, manufacturing, operations, and maintenance
- **Support Neural Networks**: Provide structured data for AI/ML-based propulsion optimization and health monitoring
- **Ensure Compliance**: Maintain regulatory compliance (EASA, FAA, EU AI Act, EU DPP Regulation)
- **Facilitate Circularity**: Track propulsion components for end-of-life recycling and reuse

## 3. Scope

The Propulsion DPP covers:

### 3.1 ATA Chapters Included

- **ATA 70**: Standard Practices - Propulsion
- **ATA 71**: Power Plant Integration
- **ATA 72**: Engines and Propulsors (Open-Fan, Hybrid, Electric)
- **ATA 73**: Engine Fuel and Supply (H₂ interfaces)
- **ATA 75**: Bleed and Air Management
- **ATA 76**: Propulsion Control Systems (FADEC, Hybrid Control)
- **ATA 77**: Propulsion Indications and Health Monitoring
- **ATA 78**: Exhaust and Emissions
- **ATA 79**: Lubrication and Oil Systems

### 3.2 Cross-ATA Interfaces

The Propulsion DPP interfaces with:

- **ATA 28**: Fuel System (H₂ storage and distribution)
- **ATA 30**: Ice and Rain Protection (engine inlet protection)
- **ATA 36**: Pneumatic Systems (bleed air integration)
- **ATA 49**: Airborne Auxiliary Power
- **ATA 50-57**: Structures (nacelles, pylons, mounting)
- **ATA 80**: Starting Systems

### 3.3 AMPEL360-Specific Systems

- **Hybrid Propulsion**: H₂ fuel cells + electric motors + open-fan architecture
- **CO₂ Loop Integration**: Links to ATA 21-80 CO₂ capture system
- **CAOS Integration**: Neural network-based propulsion optimization
- **Cryogenic Interfaces**: H₂ fuel system at -253°C

## 4. Document Hierarchy

```
95-70_Propulsion/
├── 95-70-00-001_Propulsion_DPP_Overview.md (this document)
├── 95-70-00-002_Propulsion_Scope_and_Boundaries.md
├── 95-70-00-003_Cross_ATA_Propulsion_Map.csv
│
├── 00_META/
│   ├── 95-70-00-004_Propulsion_Taxonomy.md
│   ├── 95-70-00-005_Propulsion_Traceability_Matrix.csv
│   ├── 95-70-00-006_Propulsion_Assets_Registry.json
│   ├── 95-70-00-007_Interfaces_to_Storages_and_Circularity.md
│   └── 95-70-00-008_CAOS_Propulsion_Hooks.md
│
├── 95-70-70_Propulsion_Practices_and_Standards/
├── 95-70-71_PowerPlant_Integration/
├── 95-70-72_Engines_and_Propulsors/
├── 95-70-73_Engine_Fuel_and_Supply/
├── 95-70-75_Bleed_and_Air_Management/
├── 95-70-76_Propulsion_Control_Systems/
├── 95-70-77_Propulsion_Indications_and_Health/
├── 95-70-78_Exhaust_and_Emissions/
└── 95-70-79_Lubrication_and_Oil_Systems/
```

## 5. Key Features

### 5.1 Neural Network Integration

The Propulsion DPP is designed for seamless integration with CAOS (Computer Aided Operations & Services):

- **Predictive Maintenance**: Health monitoring data feeds NN models
- **Performance Optimization**: Real-time thrust, efficiency, and thermal management
- **Anomaly Detection**: Early warning of degradation or failures
- **Digital Twin**: Physics-based simulation validated by fleet data

### 5.2 Traceability Matrix

Each propulsion component is traced through:

- **Design Phase**: Requirements → Design → Verification
- **Manufacturing**: Suppliers → Parts → Assembly → Testing
- **Operations**: Installation → Monitoring → Maintenance → Replacement
- **End-of-Life**: Decommission → Recycling → Material Recovery

### 5.3 Regulatory Compliance

- **EASA CS-25**: Large aircraft certification
- **FAA FAR Part 25**: US certification equivalence
- **EU AI Act**: High-risk AI system requirements (propulsion control)
- **EU DPP Regulation**: Product passport requirements
- **ISO 19881**: Gaseous hydrogen - Land vehicle fuel containers

## 6. Data Schema

The Propulsion DPP uses standardized JSON schemas (see 95-70-00-006):

```json
{
  "asset_id": "PROP-72-001",
  "component_type": "Open-Fan Propulsor",
  "ata_chapter": "72",
  "location": "Left Wing Position 1",
  "criticality": "Critical",
  "status": "Active",
  "health_score": 0.95,
  "next_maintenance": "2026-03-15",
  "interfaces": ["ATA-28", "ATA-73", "ATA-76"],
  "nn_models": ["propulsion_health_monitor", "thrust_optimizer"]
}
```

## 7. Lifecycle Integration

The Propulsion DPP supports all 14 lifecycle folders:

1. **OVERVIEW**: System concept and purpose
2. **SAFETY**: FMEA, FHA, hazard analysis
3. **REQUIREMENTS**: Functional and performance specifications
4. **DESIGN**: CAD models, architecture, specifications
5. **INTERFACES**: Integration points with other systems
6. **ENGINEERING**: FEA, CFD, thermal analysis
7. **V&V**: Verification and validation plans
8. **PROTOTYPING**: Development hardware
9. **PRODUCTION**: Manufacturing processes
10. **CERTIFICATION**: Regulatory compliance evidence
11. **OPERATIONS**: Procedures, maintenance schedules
12. **ASSETS**: Digital product passport data
13. **SUBSYSTEMS**: Component breakdown structure
14. **META**: Documentation control and governance

## 8. Usage Guidelines

### 8.1 For Engineers

- Reference this DPP when designing propulsion interfaces
- Update traceability matrix when modifying components
- Link all design changes to requirements

### 8.2 For Operations

- Use health monitoring data for predictive maintenance
- Consult operating limits and procedures
- Report anomalies to NN systems for fleet learning

### 8.3 For Certification

- Provide evidence of compliance via traceability matrix
- Demonstrate safety case for NN-based control systems
- Track all changes through configuration management

## 9. Maintenance and Updates

- **Owner**: AMPEL360 Propulsion Systems Engineering
- **Review Cycle**: Quarterly
- **Change Control**: Configuration Control Board (CCB)
- **Version Control**: Git-based with semantic versioning

## 10. Related Documents

- [95-70-00-002: Propulsion Scope and Boundaries](95-70-00-002_Propulsion_Scope_and_Boundaries.md)
- [95-70-00-003: Cross-ATA Propulsion Map](95-70-00-003_Cross_ATA_Propulsion_Map.csv)
- [95-00-03: General Requirements](../../95-00_GENERAL/95-00-03_Requirements/README.md)
- [ATA 28: Fuel System](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENIC_SYSTEMS/ATA_28-FUEL_SAF_AND_CRYOGENIC/)

## 11. Version History

| Version | Date       | Author               | Changes                    |
|---------|------------|----------------------|----------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Doc Team    | Initial creation           |

---

**Document ID**: 95-70-00-001  
**Status**: Active  
**Classification**: Internal Use  
**Next Review**: 2026-02-17
