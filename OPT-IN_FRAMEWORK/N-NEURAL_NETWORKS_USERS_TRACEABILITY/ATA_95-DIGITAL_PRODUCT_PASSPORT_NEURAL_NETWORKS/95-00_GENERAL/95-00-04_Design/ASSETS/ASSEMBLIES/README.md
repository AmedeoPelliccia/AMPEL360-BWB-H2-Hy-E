# ASSEMBLIES - Design Layer

**Purpose**: This directory contains hierarchical assembly documentation for the DPP+NN system, organized by abstraction level.

## Structure

### 01_SYSTEM_LEVEL
Top-level system assemblies integrating all subsystems. These documents provide the highest-level view of the DPP+NN system architecture.

### 02_SUBSYSTEM_LEVEL
Major subsystem assemblies, organized by functional domain:
- **MODEL_LIFECYCLE**: Training, registry, deployment controller
- **DATA_PIPELINE**: Ingestion, preprocessing, feature store
- **RUNTIME_INFERENCE**: Onboard inference engines and validation
- **MONITORING_AND_LOGS**: Performance monitoring, drift detection, logging
- **BLOCKCHAIN_DPP**: Provenance chain, cryptographic anchors, smart contracts

### 03_INTERFACE_VIEWS
Cross-system interface specifications and API definitions:
- DPP APIs and interfaces
- ATA chapter integration points (02, 28, 42, 45)
- External interfaces (ground ops, OEM portal, regulatory)

### 04_VARIANTS
Aircraft variant-specific assembly configurations:
- **Q100**: Baseline configuration (full DPP+NN suite)
- **Q80**: Cost-optimized configuration
- **Q120**: Enhanced configuration with additional capabilities

### 99_ARCHIVE
Deprecated assemblies and historical versions for reference.

## Naming Convention

All assembly documents follow this pattern:
```
95-00-04-A<nnn>_<Assembly_Name>.md
```

Where:
- `95-00-04`: ATA 95, chapter 00, section 04 (Design)
- `A<nnn>`: Assembly number (e.g., A001, A010, A020)
- `<Assembly_Name>`: Descriptive name using underscores

Supporting files:
- `.drawio` files for diagrams (same base name)
- `.json` files for machine-readable specifications (same base name)

## Assembly Hierarchy

```
A001 (System Level)
├── A010 (Model Lifecycle)
│   ├── A011 (Training Pipeline)
│   ├── A012 (Model Registry)
│   └── A013 (Deployment Controller)
├── A020 (Data Pipeline)
│   ├── A021 (Ingestion Layer)
│   ├── A022 (Preprocessing Engine)
│   └── A023 (Feature Store)
├── A030 (Runtime Inference)
│   ├── A031 (Inference Engine Primary)
│   ├── A032 (Inference Engine Monitor)
│   └── A033 (Result Validator)
├── A040 (Monitoring and Telemetry)
│   ├── A041 (Performance Monitor)
│   ├── A042 (Drift Detector)
│   └── A043 (DPP Event Logger)
└── A050 (Blockchain DPP)
    ├── A051 (Provenance Chain)
    ├── A052 (Cryptographic Anchors)
    └── A053 (Smart Contracts)
```

## Usage Guidelines

1. **Start with System Level**: Review A001 for overall architecture context
2. **Drill Down**: Follow references to subsystem assemblies for details
3. **Check Interfaces**: Review interface views for cross-system integration
4. **Variant Selection**: Consult variant documents for specific aircraft configurations
5. **Traceability**: Each assembly links to requirements and verification methods

## Traceability

All assemblies must trace to:
- **Requirements**: In `../../../95-00-03_Requirements/`
- **Verification**: In `../../../95-00-07_V_AND_V/`
- **Interfaces**: In `../../../95-00-05_Interfaces/`

## Document Control

- **Standard**: AMPEL360 Assets Standard
- **Owner**: AMPEL360 Design WG
- **Review Frequency**: Per design iteration or significant change
- **Status**: Active development

## Related Documents

- [Design Principles](../../DESIGN_PRINCIPLES.md)
- [Architecture Overview](../../ARCHITECTURE_OVERVIEW.md)
- [CAOS Integration Strategy](../../CAOS_INTEGRATION_STRATEGY.md)
- [Certification Approach](../../CERTIFICATION_APPROACH.md)
