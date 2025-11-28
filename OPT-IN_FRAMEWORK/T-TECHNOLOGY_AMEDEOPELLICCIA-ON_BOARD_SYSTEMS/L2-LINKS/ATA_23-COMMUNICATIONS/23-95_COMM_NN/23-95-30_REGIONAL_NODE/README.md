# 23-95-30 — Regional Node (FAirCCC-R)

## Purpose

The Regional Node coordinates secure aggregation across multiple ground stations and provides checkpointing and uplink to the Fleet Core.

## Responsibilities

| Function | Description |
|----------|-------------|
| **Coordination** | Wait for N≥T clients |
| **SecAgg Server** | Secure aggregation orchestration |
| **Checkpointing** | Save intermediate states |
| **Uplink** | Forward aggregated gradients |

## Interfaces

- **Upstream:** Ground Nodes (23-95-20)
- **Downstream:** Fleet Core (23-95-40)

## Aggregation Protocol

- Wait for minimum client threshold
- Unmask sum only (secure aggregation)
- Apply FedAvg or FedAdam

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
