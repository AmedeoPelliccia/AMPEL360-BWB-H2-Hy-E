# 02-60-05 – Backup Storage

## Purpose

This directory defines the backup and disaster recovery infrastructure ensuring business continuity and compliance with aviation regulations. Implements 3-2-1 backup strategy with defined RPO and RTO objectives.

---

## Scope

- **Database Backups**: Full, incremental, and differential backups of all databases
- **System Backups**: VM snapshots, configuration backups, IaC repositories
- **Offsite Replication**: Geographic redundancy for disaster scenarios
- **Recovery Testing**: Regular DR drills and validation procedures

---

## Key Documents

- **[02-60-05-001_Backup_Strategy.md](./02-60-05-001_Backup_Strategy.md)** – Global backup strategy and 3-2-1 rule
- **[02-60-05-002_Incremental_Backup_System.md](./02-60-05-002_Incremental_Backup_System.md)** – Incremental/differential backup design
- **[02-60-05-003_Offsite_Replication.md](./02-60-05-003_Offsite_Replication.md)** – Cross-region replication
- **[02-60-05-004_Recovery_Procedures.md](./02-60-05-004_Recovery_Procedures.md)** – Recovery workflows
- **[02-60-05-005_Backup_Testing_Schedule.md](./02-60-05-005_Backup_Testing_Schedule.md)** – DR drill schedule

---

## ASSETS

- **02-60-05-A-001_Veeam_Backup_Jobs.xml** – Backup job configurations
- **02-60-05-A-002_Retention_Policy.yaml** – Retention policies per data class
- **02-60-05-A-003_Replication_Schedule.yaml** – Replication schedules
- **02-60-05-A-101_Database_Recovery.pdf** – DB restore procedures
- **02-60-05-A-102_VM_Recovery.pdf** – VM recovery steps
- **02-60-05-A-201_Recovery_Test_2025_Q3.pdf** – DR test report template

---

## RPO/RTO Targets

| System | RPO | RTO |
|--------|-----|-----|
| Critical OLTP | 15 minutes | 4 hours |
| Data Warehouse | 1 hour | 24 hours |
| Documents | 24 hours | 24 hours |
| ML Models | 24 hours | 48 hours |

---

## Document Control

- **Directory**: 02-60-05_Backup_Storage
- **Version**: 1.0
- **Status**: DRAFT
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.
