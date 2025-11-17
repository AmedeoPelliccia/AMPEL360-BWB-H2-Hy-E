# 95-30-00-004 Circularity Taxonomy

**Document ID:** 95-30-00-004  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

## 1. Introduction

This document defines the standardized taxonomy for circularity concepts, classifications, and terminology used throughout the AMPEL360 BWB H₂ Hy-E program.

## 2. Circularity Classifications

### 2.1 Loop Types

#### 2.1.1 Energy Loops
Flows of energy between systems for recovery and reuse.

**Categories:**
- **E-THERMAL**: Heat transfer and thermal energy recovery
- **E-ELECTRICAL**: Electrical power distribution and regeneration
- **E-MECHANICAL**: Kinetic energy recovery and storage
- **E-CHEMICAL**: Chemical energy conversion and storage (H₂, batteries)

#### 2.1.2 Material Loops
Flows of physical materials through systems.

**Categories:**
- **M-FLUID-H**: Hydraulic fluid circulation
- **M-FLUID-P**: Pneumatic gas circulation
- **M-FLUID-W**: Water and waste flows
- **M-FUEL**: Hydrogen fuel management
- **M-SOLID**: Solid materials and components

#### 2.1.3 Data Loops
Information flows for monitoring, control, and optimization.

**Categories:**
- **D-MONITOR**: Real-time system monitoring
- **D-CONTROL**: Control signals and commands
- **D-ANALYTICS**: Performance analysis and optimization
- **D-LIFECYCLE**: Digital Product Passport data

### 2.2 Flow Directions

| Code | Direction | Description |
|------|-----------|-------------|
| **UNI** | Unidirectional | One-way flow from source to target |
| **BI** | Bidirectional | Two-way flow with reversible direction |
| **CIRC** | Circular | Continuous loop within single system |
| **NET** | Network | Multi-node distribution network |

### 2.3 Circularity Strategies

#### 2.3.1 Reduce
Minimize resource consumption and waste generation.

**Strategies:**
- **R1-EFFICIENCY**: Improve conversion efficiency
- **R2-OPTIMIZATION**: Optimize operational profiles
- **R3-MINIATURIZATION**: Reduce component size and mass
- **R4-DEMATERIALIZATION**: Replace physical with digital

#### 2.3.2 Reuse
Extend component and material service life.

**Strategies:**
- **U1-DIRECT**: Direct reuse without modification
- **U2-REPAIR**: Repair and return to service
- **U3-REFURBISH**: Restore to like-new condition
- **U4-REMANUFACTURE**: Complete rebuild to original specification

#### 2.3.3 Recycle
Recover materials for new applications.

**Strategies:**
- **C1-MECHANICAL**: Physical separation and processing
- **C2-CHEMICAL**: Chemical breakdown and reconstitution
- **C3-THERMAL**: Thermal processing for material recovery
- **C4-BIOLOGICAL**: Biological degradation and recovery

#### 2.3.4 Recover
Extract residual value from waste streams.

**Strategies:**
- **V1-ENERGY**: Energy recovery from waste
- **V2-MATERIAL**: Material extraction from waste
- **V3-THERMAL**: Heat recovery from processes
- **V4-EMISSION**: CO₂ and emission capture

### 2.4 Lifecycle Phases

| Phase Code | Phase Name | Description |
|------------|------------|-------------|
| **L1-DESIGN** | Design | Circular design principles and specification |
| **L2-SOURCE** | Sourcing | Material and component procurement |
| **L3-MANUFACTURE** | Manufacturing | Production and assembly |
| **L4-OPERATE** | Operations | In-service operations and use |
| **L5-MAINTAIN** | Maintenance | Service, repair, and overhaul |
| **L6-UPGRADE** | Upgrade | Modification and improvement |
| **L7-EOL** | End of Life | Retirement and disposition |
| **L8-RECOVER** | Recovery | Material and component recovery |

## 3. Component Classifications

### 3.1 Circularity Readiness Levels (CRL)

| Level | Name | Description | Criteria |
|-------|------|-------------|----------|
| **CRL-0** | Not Assessed | No circularity assessment performed | - |
| **CRL-1** | Identified | Circularity potential identified | Documented opportunities |
| **CRL-2** | Specified | Circular requirements specified | Design requirements defined |
| **CRL-3** | Designed | Circular design completed | Design verified |
| **CRL-4** | Prototyped | Circular features prototyped | Lab testing completed |
| **CRL-5** | Validated | Circular performance validated | Flight testing completed |
| **CRL-6** | Operational | Circularity operational in service | In-service data available |
| **CRL-7** | Optimized | Continuous improvement active | Multiple improvement cycles |

### 3.2 Component Circularity Categories

#### High Circularity Potential (HCP)
Components with significant circularity opportunities:
- High energy consumption or generation
- Significant material flows
- High maintenance frequency
- High replacement cost
- Environmental impact

#### Medium Circularity Potential (MCP)
Components with moderate circularity opportunities:
- Moderate energy or material flows
- Periodic maintenance
- Moderate cost
- Some environmental impact

#### Low Circularity Potential (LCP)
Components with limited circularity opportunities:
- Minimal energy or material flows
- Infrequent maintenance
- Low cost
- Minimal environmental impact

## 4. KPI Taxonomy

### 4.1 KPI Categories

| Category | Code | Description |
|----------|------|-------------|
| Efficiency | **EFF** | Conversion and recovery efficiency metrics |
| Utilization | **UTL** | Resource utilization and capacity metrics |
| Waste | **WST** | Waste generation and diversion metrics |
| Lifecycle | **LFC** | Component and material lifecycle metrics |
| Performance | **PRF** | System performance and reliability metrics |
| Environmental | **ENV** | Environmental impact metrics |
| Economic | **ECN** | Cost and economic value metrics |

### 4.2 KPI Naming Convention

Format: `{Category}-{System}-{Metric}-{Unit}`

**Examples:**
- `EFF-PWR-RECOVERY-PCT`: Electrical power recovery efficiency percentage
- `UTL-H2-BOILOFF-KG`: H₂ boil-off utilization in kilograms
- `WST-HYD-LEAK-ML`: Hydraulic fluid leak waste in milliliters
- `LFC-BATTERY-CYCLES-NUM`: Battery lifecycle in number of cycles

## 5. Interface Taxonomy

### 5.1 Physical Interfaces

| Type | Code | Description |
|------|------|-------------|
| Thermal | **TH-IF** | Heat exchange interface |
| Electrical | **EL-IF** | Electrical connection |
| Mechanical | **ME-IF** | Mechanical coupling |
| Fluid | **FL-IF** | Fluid transfer connection |
| Pneumatic | **PN-IF** | Pneumatic connection |

### 5.2 Digital Interfaces

| Type | Code | Description |
|------|------|-------------|
| Sensor Data | **SD-IF** | Sensor data output |
| Control Signal | **CS-IF** | Control command input |
| Status Report | **SR-IF** | System status reporting |
| DPP Data | **DPP-IF** | Digital Product Passport data |

## 6. ATA-Specific Taxonomy Extensions

### 6.1 ATA 21 - Environmental Control
- **THERMAL-LOOP**: Thermal management circuits
- **AIR-QUALITY**: Air quality monitoring and control
- **FILTER-MGMT**: Filter lifecycle management

### 6.2 ATA 24 - Electrical Power
- **LOAD-SHARE**: Load sharing and optimization
- **REGEN-BRAKE**: Regenerative braking systems
- **REDUNDANCY**: Redundant power path management

### 6.3 ATA 28 - Fuel (H₂)
- **BOILOFF-MGT**: Boil-off gas management
- **CRYO-COOL**: Cryogenic cooling applications
- **H2-PURITY**: Hydrogen purity management

### 6.4 ATA 29 - Hydraulic
- **ACCUM-MGMT**: Accumulator management
- **FLUID-COND**: Fluid condition monitoring
- **LEAK-PREV**: Leak prevention and detection

### 6.5 ATA 36 - Pneumatic
- **BLEED-OPT**: Bleed air optimization
- **PRESS-REG**: Pressure regulation
- **HEAT-REC**: Heat recovery from pneumatics

### 6.6 ATA 38 - Water/Waste
- **POTABLE**: Potable water management
- **GREY-WATER**: Grey water treatment
- **BLACK-WATER**: Black water processing
- **RECLAIM**: Water reclamation systems

### 6.7 ATA 49 - APU
- **APU-LOAD**: APU loading optimization
- **APU-HEAT**: APU heat recovery
- **APU-SHARE**: Resource sharing with main systems

### 6.8 ATA 70 - Propulsion
- **FUEL-CELL**: Fuel cell operations
- **THERMAL-MGT**: Propulsion thermal management
- **EXHAUST-MGT**: Exhaust and byproduct management

### 6.9 ATA 80 - Energy Storage
- **SOC-MGT**: State of charge management
- **SOH-MON**: State of health monitoring
- **CYCLE-OPT**: Charge/discharge cycle optimization
- **CO2-BATT**: CO₂ battery systems

## 7. Cross-References

### 7.1 Related Documents
- 95-30-00-001: Circularity Overview
- 95-30-00-005: Circularity Traceability Matrix
- 95-30-00-006: Circularity KPI Definitions
- 95-30-00-007: Circularity Assets Registry

### 7.2 External Standards
- ISO 14040: Life Cycle Assessment - Principles and Framework
- ISO 14044: Life Cycle Assessment - Requirements and Guidelines
- EN 45552: General method for the assessment of the durability of energy-related products
- EU Battery Regulation 2023/1542

## 8. Document Control

| Item | Details |
|------|---------|
| **Owner** | AMPEL360 Sustainability WG - Taxonomy Lead |
| **Approved By** | Chief Engineer - Systems Integration |
| **Next Review** | 2026-05-17 |
| **Classification** | Internal |

---

*This document is part of the AMPEL360 OPT-IN Framework and follows the structure defined in OPT-IN_FRAMEWORK_STANDARD.md*
