# 23-95-40 — Fleet Core (FAirCCC-F)

## Purpose

The Fleet Core is the central hub of the FAirCCC infrastructure. It maintains the model registry, manages release candidates, and integrates with CAOS and DPP systems.

## Responsibilities

| Function | Description |
|----------|-------------|
| **Registry** | Model version management |
| **Release** | Produce release candidates |
| **DPP Integration** | Digital Product Passport sync |
| **CAOS Integration** | Channel orchestration |

## Interfaces

- **Upstream:** Regional Nodes (23-95-30)
- **Downstream:** Model distribution (CFLF-MODEL channel)

## Integrations

- CAOS (Collaborative Autonomous Operations System)
- DPP (Digital Product Passport)
- SATCOM for model distribution

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
