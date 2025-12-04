# PROFILES

## Purpose

Partition-level configuration profiles for DO-178C software development.

## Contents

| Profile | Description | Applicable Partitions |
|---------|-------------|----------------------|
| [`level_A_partition.yaml`](./level_A_partition.yaml) | DO-178C Level A (Catastrophic) | P-FCS, P-GNC |
| [`level_B_partition.yaml`](./level_B_partition.yaml) | DO-178C Level B (Hazardous) | P-ADS |

## Profile Structure

Each profile defines:

* DO-178C objectives and compliance requirements
* ARINC 653 partition configuration
* CAST-32A multi-core requirements
* Verification and testing requirements
* Coding standards
* AI assistance rules
* Traceability requirements
* Certification evidence requirements

## Usage

Profiles are referenced by GenCCC to:

1. Validate partition configuration completeness
2. Generate appropriate verification requirements
3. Apply correct coverage targets
4. Enforce AI assistance rules

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Status**: Active
- **Owner**: AMPEL360 SW WG
- **Last Updated**: 2025-12-04

---
