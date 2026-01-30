# 97-40-20-30 — Compression

## Purpose

Gradient compression techniques to reduce communication overhead while preserving model quality.

## Techniques

| Technique | Description |
|-----------|-------------|
| **Top-k Sparsification** | Keep only top k% of gradient values |
| **Random-k Sparsification** | Randomly sample k% of gradient values |
| **Quantization** | Reduce precision (8-bit, 16-bit) |
| **Error Feedback** | Accumulate compression errors |

## Default Configuration

- **Sparsification:** Top-k (k=1%)
- **Quantization:** 8-bit
- **Error Feedback:** Enabled

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
