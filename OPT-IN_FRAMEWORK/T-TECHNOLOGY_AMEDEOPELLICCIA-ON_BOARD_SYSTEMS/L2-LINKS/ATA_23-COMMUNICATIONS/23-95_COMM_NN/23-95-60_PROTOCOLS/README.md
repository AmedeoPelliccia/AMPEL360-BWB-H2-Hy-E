# 23-95-60 — Protocols

## Purpose

This folder contains protocol specifications for the four CFLF channels.

## Protocol Channels

| Channel | Direction | Data Type | Safety |
|---------|-----------|-----------|--------|
| **CFLF-GRAD** | A→G→R→F | DP-masked gradients | Non-safety |
| **CFLF-MODEL** | F→R→G→A | Trained models | Non-safety |
| **CFLF-TELEM** | A→G→R→F | Anonymized telemetry | Non-safety |
| **CFLF-SAFETY** | F→R→G→A | Safety models | DO-178C/ML |

## Transport Characteristics

- **GRAD:** Low-rate, best-effort, preemptible
- **MODEL:** Medium-rate, guaranteed delivery
- **TELEM:** Low-rate, sampled
- **SAFETY:** High-priority, verified delivery

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
