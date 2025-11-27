# 23-95-50 — Security

## Purpose

This folder contains security specifications, authentication protocols, and encryption standards for the COMM_NN subsystem.

## Security Features

| Feature | Implementation |
|---------|----------------|
| **Encryption** | mTLS (TLS 1.3) |
| **Encoding** | CBOR for gradient envelopes |
| **Authentication** | TPM-anchored signatures |
| **Attestation** | SBOM hash + model hash + build provenance |
| **Secure Aggregation** | Pairwise masks or threshold secret sharing |

## Threat Mitigations

- Poisoned gradient detection
- Server-side DP enforcement
- Contribution thresholds
- Anomaly filters
- Per-model kill-switches

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
