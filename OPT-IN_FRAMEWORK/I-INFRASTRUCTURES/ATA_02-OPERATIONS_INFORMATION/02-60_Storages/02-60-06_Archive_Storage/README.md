# 02-60-06 – Archive Storage

## Purpose

Long-term cold storage for compliance and regulatory retention using glacier-class storage and LTO tape libraries.

---

## Scope

- **Compliance Archives**: Regulatory-mandated data retention (5-25 years)
- **Operational Archives**: Historical operational data for analysis
- **Immutable Records**: Write-once-read-many (WORM) for compliance
- **Retrieval Services**: SLA-based retrieval from cold storage

---

## Key Documents

- **[02-60-06-001_Archive_Strategy.md](./02-60-06-001_Archive_Strategy.md)** – Archive tiers and SLAs
- **[02-60-06-002_Glacier_Integration.md](./02-60-06-002_Glacier_Integration.md)** – Glacier-style storage integration
- **[02-60-06-003_Tape_Library_Management.md](./02-60-06-003_Tape_Library_Management.md)** – LTO tape lifecycle
- **[02-60-06-004_Compliance_Retention.md](./02-60-06-004_Compliance_Retention.md)** – Retention requirements
- **[02-60-06-005_Data_Retrieval_SLA.md](./02-60-06-005_Data_Retrieval_SLA.md)** – Retrieval SLAs

---

## Compliance Requirements

Per [EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012) and [FAA Part 121](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-121):

- **Flight Records**: 25 years
- **Maintenance Records**: Aircraft lifetime + 5 years
- **Certification Evidence**: Indefinite

---

## Document Control

- **Directory**: 02-60-06_Archive_Storage
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
