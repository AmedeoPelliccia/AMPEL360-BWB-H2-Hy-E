# CAD Directory — CONTROLLER_ASSEMBLY

**Parent Assembly**: 61-00-04-A452 (CONTROLLER_ASSEMBLY)

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
CONTROLLER_[COMPONENT]_ASSY.[extension]
```

### Expected Files

| File Name | Description |
|-----------|-------------|
| CONTROLLER_ASSY.* | Complete controller assembly |
| CONTROLLER_INVERTER_ASSY.* | Power stage subassembly |
| CONTROLLER_COOLING_ASSY.* | Cold plate assembly |
| CONTROLLER_HOUSING_ASSY.* | Enclosure assembly |

## Part References

Parts are linked from:

```
../../../../../../PARTS/
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
