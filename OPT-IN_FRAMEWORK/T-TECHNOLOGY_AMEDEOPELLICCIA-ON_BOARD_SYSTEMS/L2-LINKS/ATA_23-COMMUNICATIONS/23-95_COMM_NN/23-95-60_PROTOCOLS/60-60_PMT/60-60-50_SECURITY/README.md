# 60-60-50_SECURITY — PMT Security Protocols

## Purpose

This section defines the security protocols for authentication, encryption, and access control in the PMT system.

## Security Components

| Section | Function | Technology |
|---------|----------|------------|
| 50-10_Authentication | Identity verification | mTLS, JWT tokens |
| 50-20_Encryption | Data protection | AES-256-GCM, TLS 1.3 |
| 50-90_Schemas | Security schemas | Certificate profiles, policy definitions |

## Security Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PMT Data Flow                             │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│  Aircraft   │   Ground    │  Regional   │    Fleet          │
└──────┬──────┴──────┬──────┴──────┬──────┴──────┬────────────┘
       │             │             │             │
       │     ┌───────▼───────┐     │             │
       │     │ Authentication│     │             │
       │     │    (mTLS)     │     │             │
       │     └───────┬───────┘     │             │
       │             │             │             │
       └─────────────┼─────────────┼─────────────┘
                     │             │
              ┌──────▼──────┐ ┌────▼────┐
              │  Encryption │ │  Access │
              │  (AES-256)  │ │ Control │
              └──────┬──────┘ └────┬────┘
                     │             │
                     └──────┬──────┘
                            │
                    ┌───────▼───────┐
                    │   Audit Log   │
                    └───────────────┘
```

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
