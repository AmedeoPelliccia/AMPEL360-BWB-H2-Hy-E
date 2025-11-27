# 23-95-10 — Aircraft Node (FAirCCC-A)

## Purpose

The Aircraft Node is the on-aircraft component of the FAirCCC (Federated Aircraft Communication & Computation Core) infrastructure. It handles local gradient preparation, signing, and transport initiation.

## Responsibilities

| Function | Description |
|----------|-------------|
| **Feature Gate** | Limits, units validation, PII removal |
| **Envelope Preparation** | Package gradients with metadata |
| **TPM Signing** | Hardware-anchored signature |
| **Transport Initiation** | Queue and send to ground node |

## Interfaces

- **Upstream:** Local training subsystem (97-40-20-40)
- **Downstream:** Ground Node (23-95-20)

## Security

- TPM-anchored key storage
- Secure boot attestation
- SBOM hash inclusion

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27
