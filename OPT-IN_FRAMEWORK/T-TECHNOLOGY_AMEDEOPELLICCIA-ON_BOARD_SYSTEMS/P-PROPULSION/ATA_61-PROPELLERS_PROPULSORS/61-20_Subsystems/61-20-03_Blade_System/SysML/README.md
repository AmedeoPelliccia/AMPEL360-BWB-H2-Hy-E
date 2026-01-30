# SysML Models — 61-20-03_Blade_System

This folder contains SysML 1.6 textual specifications for the Blade System subsystem.

## Contents

- **ATA61_Blade_System.sysml** — Complete SysML package containing:
  - Block Definition Diagram (BDD) — Blade System structure (Blade, Hub_Attachment, Material, Airfoil)
  - Internal Block Diagram (IBD) — Blade interfaces and load paths
  - Requirements Diagram (REQ) — Blade-specific requirements (efficiency, FOD, fatigue, weight, containment, recyclability)
  - Activity Diagram (ACT) — Blade manufacturing process
  - Parametric Diagram (PAR) — Aerodynamic performance constraints
  - State Machine (STM) — Blade lifecycle states

## Key Blocks

```sysml
block Blade_System {
    part bladeSet : Blade[12];
    part hubInterface : Hub_Attachment;
    value bladeCount : int = 12;
    value totalBladeWeight : kg;
}

block Blade {
    value chordDistribution : Curve;
    value twistDistribution : Curve;
    value materialSpec : Material;
    value aeroProfileID : String;
}
```

## Requirements Coverage

| Requirement ID | Description |
|----------------|-------------|
| REQ-61-20-03-001 | Isentropic efficiency ≥ 92% |
| REQ-61-20-03-002 | Bird strike per CS-E 800 |
| REQ-61-20-03-003 | 10^9 cycle fatigue life |
| REQ-61-20-03-004 | Blade weight ≤ 8 kg |
| REQ-61-20-03-005 | Containment per CS-E 810 |
| REQ-61-20-03-006 | ≥ 80% recyclability |

## Usage

These specifications can be imported into SysML-compatible tools such as:
- Cameo Systems Modeler
- OpenMBEE
- Papyrus
- Eclipse-based SysML tools

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Version:** 1.0
- **Last Updated:** 2025-12-01
