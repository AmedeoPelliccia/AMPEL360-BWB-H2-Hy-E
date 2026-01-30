# Q100-61-MDL-STR-FAN-BLADE-STATIC

## Fan Blade Static Structural Model

### Purpose

Static FEA for blade stress, strain, and deflection under operating loads.

### Contents

```
Q100-61-MDL-STR-FAN-BLADE-STATIC/
├── README.md
├── model_definition.yaml
├── mesh/
├── materials/
├── loads/
├── constraints/
└── results/
```

### Load Cases

| ID | Description | RPM | Condition |
|----|-------------|-----|-----------|
| LC01 | Max continuous | 2200 | Cruise |
| LC02 | Max transient | 2500 | Takeoff |
| LC03 | Overspeed | 2625 | Cold day |

---

**Document Control**

- Generated with AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT**
- Last AI update: 2025-12-05
