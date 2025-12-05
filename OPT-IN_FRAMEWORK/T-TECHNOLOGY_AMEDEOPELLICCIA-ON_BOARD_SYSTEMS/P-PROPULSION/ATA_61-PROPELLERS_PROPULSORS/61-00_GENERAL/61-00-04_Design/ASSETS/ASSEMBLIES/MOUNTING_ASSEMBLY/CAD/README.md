# CAD Directory — MOUNTING_ASSEMBLY

**Parent Assembly**: 61-00-04-A470 (MOUNTING_ASSEMBLY)

## Directory Structure

```
CAD/
├── PRODUCTS/          # Native CAD assembly files
│   ├── CATIA/        # .CATProduct files
│   ├── SOLIDWORKS/   # .sldasm files
│   └── NX/           # .prt assembly files
├── NEUTRAL/          # Exchange formats
├── VISUALIZATION/    # Lightweight viewing formats
└── RENDERS/          # Visual documentation
```

## Naming Convention

```
MOUNT_[COMPONENT]_ASSY.[extension]
```

### Expected Files

| File Name | Description |
|-----------|-------------|
| MOUNT_ASSY.* | Complete mounting assembly |
| MOUNT_FWD_ASSY.* | Forward mount subassembly |
| MOUNT_AFT_ASSY.* | Aft mount subassembly |
| MOUNT_ISOLATOR_ASSY.* | Vibration isolator assembly |
| MOUNT_THRUST_LINK_ASSY.* | Thrust link assembly |

## Part References

Parts are linked from:

```
../../../../../PARTS/
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
