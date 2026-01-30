# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Amedeo Pelliccia <amedeo.pelliccia@icloud.com>

# SSOT — Single Source of Truth

## Overview

This directory contains the Single Source of Truth for Rigging Adjustment And Calibration (27-40-40-rigging-adjustment-and-calibration).

The SSOT is organized according to the complete product lifecycle (LC01–LC14):

## Lifecycle Phases

### LC01 — Problem Statement
Requirements genesis, problem definition, and stakeholder needs.

### LC02 — System Requirements
- **REQUIREMENTS/**: Requirements specifications and traceability matrices
- **INTERFACES/**: Interface Control Documents (ICDs) for ATA 22, ATA 24, ATA 29, ATA 31

### LC03 — Design Models
- **ARCH/**: System architecture and design patterns
- **SCHEMATICS/**: Electrical and system schematics
- **ACTUATOR_SELECTION/**: EHA/EMA/PCU selection and sizing
- **EWIS/**: Electrical Wiring Interconnection System

### LC04 — Engineering Analysis
- **LOADS_SIZING/**: Aerodynamic and structural loads analysis
- **POWER_BUDGET_EHA_EMA/**: Power consumption analysis for actuators
- **THERMAL/**: Thermal analysis and heat dissipation
- **RELIABILITY_MTBF/**: Reliability and MTBF analysis
- **EMI_HIRF_LIGHTNING/**: EMI, HIRF, and lightning protection analysis

### LC05 — Integration, Testing & Prototyping
Test procedures, protocols, reports, and rig specifications.

### LC06 — Quality
Inspection plans, NCR, and supplier quality documentation.

### LC07 — Safety & Security
- **FHA/**: Functional Hazard Assessment
- **PSSA/**: Preliminary System Safety Assessment
- **SSA/**: System Safety Assessment
- **HAZARD_LOGS/**: Hazard tracking and logs

### LC08 — Certification & First Flight
Compliance matrix, MoC, and flight test support data.

### LC09 — Green Baselines
Material selection and emissions data.

### LC10 — Industrialization & CM
MBOM/PBOM, CM baselines, and work instructions.

### LC11 — Operations
Operational limitations and procedures.

### LC12 — Support Services
Service bulletin placeholders.

### LC13 — MRO & Sustainment
MSG-3 maintenance task placeholders.

### LC14 — Retirement & Circularity
End-of-life disposal and recycling plans.

## Usage

Each lifecycle folder contains specific artifacts for that phase. Refer to individual README files within each folder for detailed information.

## Document Control

- **Subject**: 27-40-40-rigging-adjustment-and-calibration
- **Type**: SSOT (Single Source of Truth)
- **Standard**: OPT-IN Framework / ATA iSpec 2200
- **Last Updated**: 2026-01-09
