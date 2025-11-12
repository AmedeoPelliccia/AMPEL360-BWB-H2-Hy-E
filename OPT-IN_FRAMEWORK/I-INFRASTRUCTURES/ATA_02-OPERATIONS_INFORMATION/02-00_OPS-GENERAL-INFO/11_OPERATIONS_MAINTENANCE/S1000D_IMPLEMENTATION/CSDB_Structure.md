# Common Source Database (CSDB) Structure

**Version:** 1.0  
**Date:** 2025-11-05

---

## 1. CSDB Overview

The CSDB is the centralized repository for all S1000D data modules, publication modules, and related content.

## 2. Directory Structure

```
CSDB/
├── DMC/                    # Data Modules
│   ├── ATA_02/
│   │   ├── 02-00-00/
│   │   ├── 02-32-00/
│   │   └── ...
│   ├── ATA_28/
│   └── ...
├── PMC/                    # Publication Modules
├── ICN/                    # Illustrations
│   ├── CGM/
│   ├── SVG/
│   └── X3D/
├── COM/                    # Common Information
│   ├── Tools/
│   ├── Materials/
│   └── Safety/
├── IMF/                    # Information Management Files
├── SCH/                    # Schemas
│   ├── S1000D_6-0/
│   └── Business_Rules/
└── DDN/                    # Data Dispatch Notes
```

## 3. Access Control

| Role | Permissions |
|------|-------------|
| Author | Read, Write (assigned DMs) |
| Reviewer | Read, Comment |
| Approver | Read, Approve |
| Publisher | Read, Publish |
| Admin | Full access |

## 4. Version Control

- Git-based version control
- Branch per data module
- Pull request workflow
- Automated validation on commit

## 5. Backup Strategy

- Daily incremental backups
- Weekly full backups
- Offsite replication (AWS S3)
- 7-year retention

---

**Document Owner:** IT Operations
