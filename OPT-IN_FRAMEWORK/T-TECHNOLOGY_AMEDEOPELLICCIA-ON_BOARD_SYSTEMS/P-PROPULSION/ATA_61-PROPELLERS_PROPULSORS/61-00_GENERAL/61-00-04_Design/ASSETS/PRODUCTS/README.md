# PRODUCTS — ATA 61 Propellers/Propulsors Released Product Definitions

**Purpose**: This directory contains the **controlled, approved product configurations** representing deliverable product states for the AMPEL360 BWB H2 Hy-E hybrid-electric propulsion system (Q100 program).

## Project Context

The AMPEL360-BWB-H2-Hy-E is a hybrid Blended Wing Body aircraft featuring:

- **H₂ PEM Fuel Cells** — Primary power source (2× 250 kW nominal)
- **Open-Fan Propulsors** — High bypass ratio for efficiency
- **Closed-Loop CO₂ Battery** — Peak-power buffering system
- **SAF Compatibility** — Sustainable Aviation Fuel ready
- **800 VDC Architecture** — High-voltage DC electrical distribution

## Product Hierarchy

```
Q100-61-PROD-PROPULSOR-SYSTEM (Top Level)
├── Q100-61-PROD-OPEN-FAN-UNIT
├── Q100-61-PROD-ELECTRIC-DRIVE-UNIT
├── Q100-61-PROD-GEARBOX-UNIT
├── Q100-61-PROD-NACELLE-UNIT
└── Q100-61-PROD-CONTROLLER-UNIT
```

## Naming Convention

All product artifacts follow the Q100-61 prefix pattern:

```
Q100-61-[TYPE]-[PRODUCT/SYSTEM]-[VARIANT]
```

### Product Type Codes

| Code | Meaning | Description |
|------|---------|-------------|
| PROD | Product Definition | Core product definition |
| VAR  | Product Variant | Position/application variants |
| CFG  | Configuration | Configuration baselines and options |
| OPT  | Option | Customer-selectable options |
| BOM  | Bill of Materials | Material and component lists |
| SPEC | Specification | Performance/environmental specs |
| CERT | Certification | Certification evidence |
| LC   | Lifecycle | Lifecycle management data |
| STD  | Standard | Product standards and procedures |

## Directory Structure

```
PRODUCTS/
├── README.md                    # This file
│
├── PRODUCT_DEFINITIONS/         # Core product definitions
│   ├── Q100-61-PROD-PROPULSOR-SYSTEM/     # Top-level propulsion system
│   ├── Q100-61-PROD-OPEN-FAN-UNIT/        # Open-fan propulsor unit
│   ├── Q100-61-PROD-ELECTRIC-DRIVE-UNIT/  # Electric motor drive
│   ├── Q100-61-PROD-GEARBOX-UNIT/         # Reduction gearbox
│   ├── Q100-61-PROD-NACELLE-UNIT/         # Nacelle structure
│   └── Q100-61-PROD-CONTROLLER-UNIT/      # Propulsor controller
│
├── PRODUCT_VARIANTS/            # Position and application variants
│   ├── Q100-61-VAR-PROPULSOR-LH/          # Left-hand position
│   ├── Q100-61-VAR-PROPULSOR-RH/          # Right-hand position
│   ├── Q100-61-VAR-PROPULSOR-CENTER/      # Center/tail position
│   └── Q100-61-VAR-PROPULSOR-EXTENDED-RANGE/ # Extended range variant
│
├── PRODUCT_CONFIGURATIONS/      # Configuration management
│   ├── BASELINE/                # Baseline configurations
│   ├── OPTIONS/                 # Optional features
│   └── CUSTOMER_CONFIGS/        # Customer-specific configurations
│
├── BILL_OF_MATERIALS/           # BOM data for all products
│   ├── Q100-61-BOM-PROPULSOR-SYSTEM/
│   ├── Q100-61-BOM-OPEN-FAN-UNIT/
│   ├── Q100-61-BOM-ELECTRIC-DRIVE-UNIT/
│   ├── Q100-61-BOM-GEARBOX-UNIT/
│   ├── Q100-61-BOM-NACELLE-UNIT/
│   └── Q100-61-BOM-CONTROLLER-UNIT/
│
├── PRODUCT_SPECIFICATIONS/      # Technical specifications
│   ├── PERFORMANCE/             # Thrust, power, efficiency, noise
│   ├── ENVIRONMENTAL/           # Temperature, altitude, EMC
│   ├── INTERFACE/               # Mechanical, electrical, fluid, data
│   ├── RELIABILITY/             # MTBF, MTTR, dispatch
│   └── SAFETY/                  # FMEA, FTA, hazard analysis
│
├── CERTIFICATION/               # Certification evidence
│   ├── TYPE_CERTIFICATE/        # Type certification plan
│   ├── AIRWORTHINESS/           # CS-E, FAR-33 compliance
│   ├── ENVIRONMENTAL/           # Noise, emissions compliance
│   └── TEST_EVIDENCE/           # Test reports and results
│
├── PRODUCT_LIFECYCLE/           # Lifecycle management
│   ├── DEVELOPMENT/             # Development milestones
│   ├── PRODUCTION/              # Production planning
│   ├── IN_SERVICE/              # In-service support
│   └── OBSOLESCENCE/            # Obsolescence management
│
└── PRODUCT_STANDARDS/           # Product standards and procedures
```

## Relationship to Other ASSETS Directories

The PRODUCTS directory represents the **released, configured states** that reference:

| Directory | Relationship |
|-----------|--------------|
| [PARTS](../PARTS/) | Individual component definitions |
| [ASSEMBLIES](../ASSEMBLIES/) | CAD assembly models |
| [DRAWINGS](../DRAWINGS/) | Engineering drawings |
| [MODELS](../MODELS/) | Analysis and simulation models |
| [INSTALLATIONS](../INSTALLATIONS/) | Integration data |

## Product Baseline Summary

### Q100-61-PROD-PROPULSOR-SYSTEM

The top-level integrated propulsion system comprising all sub-products. This product represents the complete deliverable unit for aircraft integration.

**Key Specifications (Baseline)**:

| Parameter | Value | Notes |
|-----------|-------|-------|
| Propulsion Type | Hybrid-Electric | H₂ Fuel Cell + CO₂ Battery |
| Max Thrust | 85 kN per unit | At sea level, ISA |
| Fan Diameter | 2.8 m | Open-fan architecture |
| Electric Power | 2× 500 kW motors | 800 VDC input |
| System Weight (Dry) | 1,850 kg | Including nacelle |
| Bypass Ratio | 25:1 (effective) | Open-fan configuration |

### Product Variants

| Variant | Position | Delta from Baseline |
|---------|----------|---------------------|
| Q100-61-VAR-PROPULSOR-LH | Left inboard/outboard | Mirrored mounting |
| Q100-61-VAR-PROPULSOR-RH | Right inboard/outboard | Baseline mounting |
| Q100-61-VAR-PROPULSOR-CENTER | Tail-mounted | Centerline, thrust vectoring |
| Q100-61-VAR-PROPULSOR-EXTENDED-RANGE | Any position | Enhanced efficiency mode |

### Product Options

| Option | Description |
|--------|-------------|
| Q100-61-OPT-HIGH-POWER | Increased motor power for MTOW variants |
| Q100-61-OPT-EXTENDED-RANGE | Optimized for long-range cruise efficiency |
| Q100-61-OPT-REDUCED-NOISE | Enhanced acoustic treatment |
| Q100-61-OPT-SAF-OPTIMIZED | Optimized for SAF fuel operation |

## Certification Targets

- **CS-E** ([EASA Certification Specifications for Engines](https://www.easa.europa.eu/document-library/certification-specifications))
- **FAR Part 33** ([FAA Airworthiness Standards: Aircraft Engines](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-33))
- **ICAO Annex 16** — Environmental (Noise, Emissions)
- **CS-25.1309** — Systems Safety Assessment

## Usage Guidelines

1. **Product Definitions** — Start with `PRODUCT_DEFINITIONS/` for core product information
2. **Configuration** — Use `PRODUCT_CONFIGURATIONS/` for baseline and option selection
3. **BOM** — Reference `BILL_OF_MATERIALS/` for material planning
4. **Specifications** — Use `PRODUCT_SPECIFICATIONS/` for technical requirements
5. **Certification** — Track compliance in `CERTIFICATION/`

## Traceability

All products must maintain traceability to:

- **Requirements**: In `../../../61-00-03_Requirements/`
- **Safety Analysis**: In `../../../61-00-02_Safety/`
- **Verification**: In `../../../61-00-07_V_AND_V/`
- **Interfaces**: In `../../../61-00-05_Interfaces/`

## Related Documents

- [AMPEL360 Assets Standard](../../../../../../../AMPEL360_ASSETS_STANDARD.md)
- [OPT-IN Framework Standard](../../../../../../../OPT-IN_FRAMEWORK_STANDARD.md)
- [Design README](../../README.md)
- [ASSEMBLIES Directory](../ASSEMBLIES/README.md)
- [PARTS Directory](../PARTS/README.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
