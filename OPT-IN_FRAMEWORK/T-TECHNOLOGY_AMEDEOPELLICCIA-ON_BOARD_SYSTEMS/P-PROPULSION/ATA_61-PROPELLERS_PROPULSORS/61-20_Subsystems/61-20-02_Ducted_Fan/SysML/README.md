# SysML Models — 61-20-02_Ducted_Fan

This folder contains references to SysML specifications for the Ducted Fan subsystem.

## Shared Model

The primary SysML specification for the EDF propulsor (including the Ducted Fan) is maintained in:

- **[../61-20-01_Electric_Motor/SysML/ATA61_EDF_Propulsor.sysml](../61-20-01_Electric_Motor/SysML/ATA61_EDF_Propulsor.sysml)**

This shared model contains the complete EDF propulsor architecture including:
- Block Definition Diagram (BDD) — EDF Propulsor structure
- Internal Block Diagram (IBD) — Subsystem interfaces  
- Requirements Diagram (REQ) — High-level requirements
- Activity Diagram (ACT) — Startup sequence
- Parametric Diagram (PAR) — Performance constraints

## Ducted Fan Specific Elements

The shared SysML model includes the following Ducted_Fan block:

```sysml
block Ducted_Fan {
    part rotor : Rotor;
    part stator : Stator;
    part spinner : Spinner;
    part duct : Fan_Duct;
    value fanDiameter : m;
    value bladeCount : int;
    value efficiencyMap : Curve;
}
```

## Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Version:** 1.0
- **Last Updated:** 2025-12-01
