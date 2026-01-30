# ATA 22 — AUTOFLIGHT

## Overview

This is ATA Chapter 22: AUTOFLIGHT, part of the T — TECHNOLOGY AMEDEOPELLICCIA — ON BOARD SYSTEMS axis.

## Structure

This chapter follows the mandatory OPT-IN Framework structure:

### 22-00_GENERAL (Lifecycle Folders)

The GENERAL layer contains 14 mandatory lifecycle folders covering the complete development cycle:

1. **22-00-01_Overview**: System overview and global architecture
2. **22-00-02_Safety**: Safety framework and analysis
3. **22-00-03_Requirements**: Requirements and traceability
4. **22-00-04_Design**: Design specifications and patterns
5. **22-00-05_Interfaces**: Interface control documents
6. **22-00-06_Engineering**: Analysis, models, and simulation
7. **22-00-07_V_AND_V**: Verification and validation
8. **22-00-08_Prototyping**: Prototype development
9. **22-00-09_Production_Planning**: Manufacturing planning
10. **22-00-10_Certification**: Certification evidence
11. **22-00-11_EIS_Versions_Tags**: Configuration management
12. **22-00-12_Services**: Maintenance and service
13. **22-00-13_Subsystems_Components**: Component breakdown
14. **22-00-14_Ops_Std_Sustain**: Operational standards

### Cross-ATA Root Buckets

The following buckets are mandatory in every ATA chapter:

- **22-10_Operations**: Operational procedures and use cases
- **22-20_Subsystems**: Functional subsystems (design-driven internal structure)
- **22-30_ANCHORS**: Sustainability, LCA, and circular economy
- **22-40_Software**: Software, control logic, and AI/ML
- **22-50_Structures**: Physical structures and frames
- **22-60_Storages**: Tanks, reservoirs, and storage
- **22-70_Propulsion**: Propulsion interfaces (if applicable)
- **22-80_Energy**: Energy management and distribution
- **22-90_Tables_Schemas_Diagrams**: Data tables and documentation

### ATA iSpec 2200 Standard Numbering System (SNS) Structure

In addition to the OPT-IN Framework structure, this chapter includes an **ATA iSpec 2200 compliant SNS breakdown** for certification and publication purposes:

- **[ATA-22-auto-flight/](./ATA-22-auto-flight/)**: Root directory for SNS structure with S1000D CSDB

The SNS structure provides:
- Industry-standard ATA numbering for maintenance manuals
- S1000D-based technical publication management
- Integration with existing aviation documentation systems
- Aircraft Maintenance Manual (AMM) and Illustrated Parts Catalog (IPC) views

#### SNS Sections (ATA 22-xx)

- **22-00**: Auto Flight, General — Architecture, modes philosophy, redundancy, integration boundaries
- **22-10**: Autopilot — Automatic control laws, engagement/disengagement logic
- **22-20**: Speed–Attitude Correction — Speed/attitude capture and correction functions
- **22-30**: Auto Throttle — Autothrottle/autothrust computation and mode logic
- **22-40**: System Monitor — Monitoring, BIT, fault detection, mode inhibition
- **22-50**: Aerodynamic Load Alleviating — Gust/load alleviation functions

See [ATA-22-auto-flight/README.md](./ATA-22-auto-flight/README.md) for complete SNS structure documentation.

## Scope and Boundaries

**ATA 22** is scoped to **flight guidance/automatic flight functions** including:
- Autopilot and automatic flight control
- Autothrottle/autothrust systems
- System monitoring and fault management
- Load alleviation functions

**Not included in ATA 22** (belong to other chapters):
- Flight controls/actuators (ATA 27)
- Navigation sensors (ATA 34)
- Communications (ATA 23)
- Electrical power (ATA 24)
- Displays/indicating (ATA 31)
- IMA computing platform (ATA 42)

## Document Control

- **ATA Chapter**: 22
- **Status**: Active
- **Owner**: AMPEL360 Documentation WG
- **Standard**: OPT-IN Framework v1.1 + ATA iSpec 2200 SNS
- **Last Updated**: 2026-01-08
