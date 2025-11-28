# 23-95-65-SECURITY

## Purpose

This subchapter defines the security protocols for authentication, encryption,
and access control in the PMT system.

## Structure

| Section | Purpose |
|---------|---------|
| 23-95-65-10_Authentication | Identity verification (mTLS, JWT) |
| 23-95-65-20_Encryption | Data protection (AES-256-GCM, TLS 1.3) |
| 23-95-65-90_Schemas | Security schema definitions |

## Security Requirements

| Requirement | Level | Standard |
|-------------|-------|----------|
| Authentication | Mutual TLS | X.509 certificates |
| Encryption in transit | AES-256-GCM | TLS 1.3 |
| Encryption at rest | AES-256 | FIPS 140-2 |
| Access control | Role-based | OAuth 2.0 scopes |
| Audit logging | Complete | DO-326A compliant |

## Certificate Hierarchy

| Certificate | Issuer | Validity | Usage |
|-------------|--------|----------|-------|
| Fleet Root CA | Self-signed | 10 years | Trust anchor |
| Regional CA | Fleet Root | 5 years | Regional signing |
| Ground Station | Regional CA | 1 year | Ground auth |
| Aircraft | Fleet Root | 3 years | Aircraft auth |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
