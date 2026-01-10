# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>

# SSOT — Single Source of Truth

## Overview

This directory contains the Single Source of Truth for Safety Philosophy, Zoning and Fluid Compatibility (29-00-20-safety-philosophy-zoning-and-fluid-compatibility).

The SSOT is organized according to the complete product lifecycle (LC01-LC14):

## Lifecycle Phases

### LC01 — Problem Statement
Requirements genesis, problem definition, and stakeholder needs.

### LC02 — System Requirements
- **REQUIREMENTS/**: Requirements specifications and traceability matrices
  - `29-00-20_requirements.csv`
  - `29-00-20_traceability.csv`
- **INTERFACES/**: Interface Control Documents (ICDs)
  - `ICD_ATA24_electrical_power_for_pumps_and_controls.md`
  - `ICD_ATA27_flight_controls_power_users.md`
  - `ICD_ATA32_landing_gear_brakes_steering_power_users.md`
  - `ICD_ATA26_fire_protection_zones_and_detection.md`
  - `ICD_ATA31_indications_warnings_and_bite.md`

### LC03 — Design Models
- **ARCH/**: System architecture and design patterns
- **SCHEMATICS/**: System schematics
- **PIPING_ROUTING/**: Piping and routing layouts
- **VALVES_ACTUATION/**: Valve and actuation designs
- **SENSOR_PLACEMENT/**: Sensor placement documentation
- **EWIS/**: Electrical Wiring Interconnection System

### LC04 — Engineering Analysis
- **PRESSURE_DROP_AND_FLOW_SIZING/**: Pressure drop and flow sizing analysis
- **TRANSIENTS_WATER_HAMMER/**: Transients and water hammer analysis
- **THERMAL_COOLING/**: Thermal and cooling analysis
- **CONTAMINATION_AND_FILTER_SIZING/**: Contamination and filter sizing
- **RELIABILITY_AVAILABILITY/**: Reliability and availability analysis
- **EMI_HIRF_LIGHTNING/**: EMI, HIRF, and lightning protection analysis

### LC05 — Integration, Testing & Prototyping
- **TEST_PROCEDURES/**: Test procedures and protocols
- **TEST_REPORTS/**: Test execution reports
- **RIGS/**: Test rig specifications and configurations

### LC06 — Quality
- **INSPECTION_PLANS/**: Quality inspection plans
- **NCR/**: Non-Conformance Reports
- **SUPPLIER_QUALITY/**: Supplier quality documentation

### LC07 — Safety & Security
- **FHA/**: Functional Hazard Assessment
- **PSSA/**: Preliminary System Safety Assessment
- **SSA/**: System Safety Assessment
- **HAZARD_LOGS/**: Hazard tracking and logs

### LC08 — Certification & First Flight
- **COMPLIANCE_MATRIX/**: Regulatory compliance matrices
- **MoC/**: Means of Compliance documentation
- **FLIGHT_TEST_SUPPORT/**: Flight test support data

### LC09 — Green Baselines
- **MATERIALS_EMISSIONS/**: Material selection and emissions data

### LC10 — Industrialization & CM
- **MBOM_PBOM/**: Manufacturing and Product Bill of Materials
- **CM_BASELINES/**: Configuration Management baselines
- **WORK_INSTRUCTIONS/**: Manufacturing work instructions

### LC11 — Operations
- **OPS_LIMITATIONS/**: Operational limitations and procedures

### LC12 — Support Services
- **SERVICE_BULLETINS_PLACEHOLDERS/**: Service bulletin placeholders

### LC13 — MRO & Sustainment
- **MSG3_TASKS_PLACEHOLDERS/**: MSG-3 maintenance task placeholders

### LC14 — Retirement & Circularity
- **DISPOSAL_RECYCLING_PLACEHOLDERS/**: End-of-life disposal and recycling plans

## Usage

Each lifecycle folder contains specific artifacts for that phase. Refer to individual README files within each folder for detailed information.

## Document Control

- **Subject**: 29-00-20
- **Type**: SSOT (Single Source of Truth)
- **Standard**: OPT-IN Framework / ATA iSpec 2200
- **Last Updated**: 2026-01-09
