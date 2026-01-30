# 97-40-20-50 — Aggregation

## Purpose

Server-side aggregation algorithms for combining client gradients.

## Algorithms

| Algorithm | Description |
|-----------|-------------|
| **FedAvg** | Weighted averaging of client updates |
| **FedAdam** | Adaptive learning rate aggregation |
| **FedProx** | Proximal term for heterogeneous data |

## Aggregation Pipeline

1. Collect gradients from N≥T clients
2. Apply secure aggregation unmask
3. Run selected aggregation algorithm
4. Update global model
5. Checkpoint and version

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
