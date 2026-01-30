# Q100-61-MDL-THM-MOTOR

## Electric Motor Thermal Management Model

### Purpose

Critical thermal model for the high power-density PMSM motor. Predicts hot spot temperatures and cooling requirements for the hybrid-electric propulsion system.

### Contents

```
Q100-61-MDL-THM-MOTOR/
├── README.md
├── model_definition.yaml
├── heat_sources/         # Loss maps from EM analysis
├── cooling/              # Cooling jacket design parameters
└── results/              # Temperature predictions
```

### Key Analysis Cases

| ID | Description | Duration | Condition |
|----|-------------|----------|-----------|
| THM01 | Cruise continuous | Steady-state | Design power |
| THM02 | Takeoff transient | 5 min | Max power |
| THM03 | Hot day derating | Steady-state | ISA+30°C |
| THM04 | Cooling failure | Transient | Degraded |

### Temperature Limits

| Component | Limit (°C) | Basis |
|-----------|------------|-------|
| Winding hot spot | 180 | Class H insulation |
| Magnets (N48SH) | 150 | Demagnetization |
| Bearings | 120 | Lubricant limits |

### Integration

- **Inputs from**: Q100-61-MDL-EM-MOTOR-2D (loss maps)
- **Outputs to**: Q100-61-MDL-PERF-PROPULSOR (derating curves)

---

**Document Control**

- Generated with AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT**
- Last AI update: 2025-12-05
