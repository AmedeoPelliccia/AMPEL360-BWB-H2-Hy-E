# INSTALLATION_DEFINITIONS — Interface and Mounting Definitions

## Purpose

This directory contains the interface and mounting definitions for all major propulsion system installations. Each definition specifies:

- Mechanical interfaces (mounts, fasteners, torque values)
- Electrical interfaces (connectors, specifications)
- Fluid interfaces (coolant, lubrication connections)
- Clearances and alignment requirements
- Reference links to Interface Control Documents (ICDs)

## Contents

| Directory | Description |
|-----------|-------------|
| Q100-61-INST-DEF-PROPULSOR-TO-PYLON | Propulsor unit to pylon mounting |
| Q100-61-INST-DEF-PYLON-TO-AIRFRAME | Pylon to BWB airframe attachment |
| Q100-61-INST-DEF-MOTOR-TO-GEARBOX | Electric motor to gearbox coupling |
| Q100-61-INST-DEF-CONTROLLER-TO-NACELLE | Motor controller nacelle mounting |
| Q100-61-INST-DEF-FAN-TO-GEARBOX | Fan assembly to gearbox attachment |

## Definition File Structure

Each installation definition directory contains:

```
Q100-61-INST-DEF-[NAME]/
├── README.md                    # Overview and context
├── installation_definition.yaml # Structured definition data
├── interface_requirements.md    # Detailed interface requirements
├── [specific_requirements].md   # Additional requirement documents
└── REFERENCES/                  # Reference documents and ICDs
    └── .gitkeep
```

## YAML Definition Schema

The `installation_definition.yaml` files follow this structure:

```yaml
installation:
  id: "Q100-61-INST-DEF-XXX"
  name: "Installation Name"
  version: "1.0.0"
  status: "Draft"
  
  mechanical:
    mount_type: "Type description"
    fasteners: [...]
    torque_values: [...]
    alignment: {...}
    
  electrical:
    connectors: [...]
    power_requirements: {...}
    
  fluid:
    connections: [...]
    flow_requirements: {...}
    
  clearances:
    operational: {...}
    maintenance: {...}
    
  references:
    icds: [...]
    drawings: [...]
    requirements: [...]
```

## Traceability

Each definition links to:
- Related requirements (REQ-61-XXX)
- Interface Control Documents
- Engineering drawings
- Safety hazard analysis

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
