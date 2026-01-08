# ATA 21 Quick Reference

## Directory Location

```
programs/AMPEL360-AIR-T/ATA-21-air-conditioning/
```

## 8 ATA Sections

| Code | Directory | Description |
|------|-----------|-------------|
| 21-00 | `21-00-air-conditioning-general` | General |
| 21-10 | `21-10-compression` | Compression |
| 21-20 | `21-20-distribution` | Distribution |
| 21-30 | `21-30-pressurization-control` | Pressurization |
| 21-40 | `21-40-heating` | Heating |
| 21-50 | `21-50-cooling` | Cooling |
| 21-60 | `21-60-temperature-control` | Temperature |
| 21-70 | `21-70-moisture-air-contaminant-control` | Moisture/Air |

## Subject Pattern

```
21-xx-yy-21-xx-<subject-name>/
├─ SSOT/                    # Master content
└─ PUB/
   ├─ AMM/CSDB/            # Maintenance Manual
   └─ IPC/CSDB/            # Parts Catalog
```

## CSDB Subdirectories

- **DM/** - Data Modules
- **PM/** - Publication Modules
- **DML/** - Data Module Lists
- **ICN/** - Illustrations
- **BREX/** - Business Rules
- **COMMON/** - Common content
- **APPLICABILITY/** - Applicability tables

## Key Files

- `bindings.csv` - DMC to PMC mappings
- `csdb.profile.yaml` - S1000D configuration
- `README.md` - Documentation

## Quick Commands

### View structure
```bash
tree programs/AMPEL360-AIR-T/ATA-21-air-conditioning/ -L 3
```

### Find all bindings files
```bash
find programs/AMPEL360-AIR-T/ATA-21-air-conditioning/ -name "bindings.csv"
```

### Find all CSDB/DM directories
```bash
find programs/AMPEL360-AIR-T/ATA-21-air-conditioning/ -path "*/CSDB/DM"
```

## Documentation

- **README.md** - Complete structure guide
- **STRUCTURE_VERIFICATION.md** - Compliance checklist
- **IMPLEMENTATION_SUMMARY.md** - Full implementation details
- **QUICK_REFERENCE.md** - This file

## Standards

- **ATA iSpec 2200** - Section numbering
- **S1000D Issue 5.0+** - CSDB structure
- **AMPEL360** - Documentation standards

## Stats

- 8 sections
- 8 subjects (21-xx-00)
- 16 publication views (AMM + IPC)
- 193 directories
- 186 files

---

**Status**: COMPLETE ✅  
**Date**: 2026-01-08  
**Branch**: copilot/rework-ata-21-directory
