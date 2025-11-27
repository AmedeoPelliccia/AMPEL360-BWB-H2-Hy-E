# 97-40-20-10 — DP-SGD

## Purpose

Differentially Private Stochastic Gradient Descent (DP-SGD) implementation for privacy-preserving model training.

## Key Documents

- [`DP-SGD-SPEC.md`](./DP-SGD-SPEC.md) — Complete specification

## Algorithm Overview

1. Compute per-sample gradients
2. Clip gradients to L2 bound C
3. Aggregate clipped gradients
4. Add calibrated Gaussian noise
5. Update model parameters

## Parameters

| Parameter | Symbol | Default |
|-----------|--------|---------|
| Clipping Bound | C | 1.0 |
| Noise Multiplier | σ | 1.1 |
| Learning Rate | η | 0.01 |

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
