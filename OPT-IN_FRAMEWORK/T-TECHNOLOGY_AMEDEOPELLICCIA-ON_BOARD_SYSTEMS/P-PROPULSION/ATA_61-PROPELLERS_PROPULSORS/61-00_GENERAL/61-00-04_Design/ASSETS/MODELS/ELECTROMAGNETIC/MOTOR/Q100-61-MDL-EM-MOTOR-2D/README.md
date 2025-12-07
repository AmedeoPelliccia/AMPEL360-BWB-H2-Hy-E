# Q100-61-MDL-EM-MOTOR-2D

## Electric Motor 2D Electromagnetic Model

### Purpose

Primary electromagnetic model for the hybrid-electric propulsion motor. Provides torque capability, efficiency maps, and loss data for thermal analysis.

### Contents

```
Q100-61-MDL-EM-MOTOR-2D/
├── README.md
├── model_definition.yaml
├── geometry/         # 2D cross-section
├── materials/        # B-H curves, conductivity
├── windings/         # Winding layout
└── results/          # Performance outputs
```

### Key Outputs

| Output | Description | Use |
|--------|-------------|-----|
| Efficiency map | η(T, n) | System performance |
| Loss breakdown | Cu, Fe, PM losses | Thermal model inputs |
| Inductances | Ld, Lq | Control model |
| Back-EMF | Voltage waveform | Inverter sizing |

### Integration

- **Outputs to**: Q100-61-MDL-THM-MOTOR (losses → heat sources)
- **Outputs to**: Q100-61-MDL-DYN-MOTOR-CONTROL (plant model)
- **Outputs to**: Q100-61-MDL-PERF-PROPULSOR (efficiency maps)

---

**Document Control**

- Generated with AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT**
- Last AI update: 2025-12-05
