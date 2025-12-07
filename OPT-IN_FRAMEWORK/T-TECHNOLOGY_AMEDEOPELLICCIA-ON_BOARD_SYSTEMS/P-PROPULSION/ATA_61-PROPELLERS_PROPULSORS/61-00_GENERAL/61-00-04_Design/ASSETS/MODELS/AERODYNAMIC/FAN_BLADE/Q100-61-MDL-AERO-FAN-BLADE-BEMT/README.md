# Q100-61-MDL-AERO-FAN-BLADE-BEMT

## Fan Blade BEMT Analysis Model

### Purpose

This model provides rapid aerodynamic performance predictions using Blade Element Momentum Theory (BEMT) for design iteration and performance mapping.

### Contents

```
Q100-61-MDL-AERO-FAN-BLADE-BEMT/
├── README.md                 # This file
├── model_definition.yaml     # Model specification
├── airfoil_data/             # Airfoil polar tables
│   └── .gitkeep
└── performance_maps/         # Generated performance maps
    └── .gitkeep
```

### Usage

1. **Prepare Airfoil Data**: Load polar tables for blade sections
2. **Define Geometry**: Import blade chord, twist, and airfoil distributions
3. **Run Analysis**: Execute BEMT solver for operating point matrix
4. **Generate Maps**: Create thrust, torque, and efficiency maps

### Key Outputs

- Performance maps (Ct, Cp, η vs. J)
- Spanwise loading distributions
- Off-design performance predictions

### Comparison with CFD

| Aspect | BEMT | CFD |
|--------|------|-----|
| Runtime | Seconds | Hours |
| Accuracy | ±5% thrust | ±3% thrust |
| 3D Effects | Limited | Full |
| Use Case | Trade studies | Final design |

---

**Document Control**

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Last AI update: 2025-12-05
