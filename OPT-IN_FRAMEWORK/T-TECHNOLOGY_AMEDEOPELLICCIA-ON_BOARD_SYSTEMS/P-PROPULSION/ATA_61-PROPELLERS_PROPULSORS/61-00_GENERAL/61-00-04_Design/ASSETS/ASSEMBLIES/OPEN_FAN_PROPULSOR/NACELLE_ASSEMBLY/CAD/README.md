# CAD Directory — NACELLE_ASSEMBLY

**Parent Assembly**: 61-00-04-A420 (NACELLE_ASSEMBLY)

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
NACELLE_[COMPONENT]_ASSY.[extension]
```

### Expected Files

| File Name | Description |
|-----------|-------------|
| NACELLE_ASSY.* | Complete nacelle assembly |
| NACELLE_INLET_ASSY.* | Inlet section subassembly |
| NACELLE_COWL_ASSY.* | Fan cowl subassembly |
| NACELLE_LINER_ASSY.* | Acoustic liner assembly |

## Part References

Parts are linked from:

```
../../../../PARTS/
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
