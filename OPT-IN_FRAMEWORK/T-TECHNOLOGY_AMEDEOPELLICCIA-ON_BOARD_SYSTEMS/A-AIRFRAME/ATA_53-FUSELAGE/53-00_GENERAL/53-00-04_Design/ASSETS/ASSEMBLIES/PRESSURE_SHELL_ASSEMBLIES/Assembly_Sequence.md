# Pressure Shell Assembly Sequence

## Overview

This document describes the high-level assembly sequence for integrating the upper shell, lower shell, and side shell modules into the complete pressure cabin structure for the AMPEL360 BWB-H2-Hy-E aircraft.

---

## Assembly Strategy

The pressure shell is assembled using a **modular approach**:

1. **Module Fabrication** — Each shell module (upper, lower, left side, right side) is fabricated independently on dedicated tooling
2. **Module Integration** — Modules are joined using precision alignment fixtures
3. **Final Assembly** — Complete pressure shell is mated with floor assemblies and door frames
4. **System Testing** — Pressure testing and final inspection

---

## Detailed Assembly Sequence

### Phase 1: Module Fabrication (Parallel)

These activities occur simultaneously in different work cells:

- **Upper Shell Module** (ASM-53-200-001)
  - Assembly Tool: AT-53-200-001
  - Duration: 6 weeks
  - See: [ASM-53-200-001_Upper_Shell_Module.yaml](ASM-53-200-001_Upper_Shell_Module.yaml)

- **Lower Shell Module** (ASM-53-200-002)
  - Assembly Tool: AT-53-200-002
  - Duration: 6 weeks
  - See: [ASM-53-200-002_Lower_Shell_Module.yaml](ASM-53-200-002_Lower_Shell_Module.yaml)

- **Side Shell Left** (ASM-53-300-001)
  - Assembly Tool: AT-53-300-001
  - Duration: 5 weeks
  - See: [ASM-53-300-001_Side_Shell_Left.yaml](ASM-53-300-001_Side_Shell_Left.yaml)

- **Side Shell Right** (ASM-53-300-002)
  - Assembly Tool: AT-53-300-002
  - Duration: 5 weeks
  - See: [ASM-53-300-002_Side_Shell_Right.yaml](ASM-53-300-002_Side_Shell_Right.yaml)

### Phase 2: Lower-to-Side Integration (Week 7-8)

**Step 2.1**: Position lower shell module on final assembly fixture FAF-53-200

**Step 2.2**: Transport and position left side shell using overhead crane

**Step 2.3**: Align left side shell to lower shell using:
- Laser tracker system
- Precision alignment pins at frames FR-10, FR-20, FR-30
- Tolerance: ±0.5 mm at all frames

**Step 2.4**: Install temporary fasteners at 300 mm spacing

**Step 2.5**: Apply structural adhesive (AF-163-2K) to joint interface

**Step 2.6**: Install permanent fasteners per `Fastener_Schedules.csv`
- Fastener type: Ti-6Al-4V, M8x20
- Spacing: 150 mm
- Torque: 40 Nm ±5%

**Step 2.7**: Repeat Steps 2.2-2.6 for right side shell

**Step 2.8**: Cure adhesive per manufacturer specification (24 hours at 20°C)

**Step 2.9**: NDT inspection of all joint bond lines

### Phase 3: Upper Shell Integration (Week 9-10)

**Step 3.1**: Verify dimensional compliance of lower+side assembly
- Critical dimensions within ±0.8 mm
- Frame alignment within ±0.3 mm

**Step 3.2**: Transport upper shell module to final assembly fixture

**Step 3.3**: Position upper shell using overhead crane with spreader bar

**Step 3.4**: Align upper shell to lower+side assembly:
- Laser tracker verification at all frames
- Alignment pins at critical stations
- Tolerance: ±0.5 mm circumferentially

**Step 3.5**: Install temporary fasteners at 300 mm spacing

**Step 3.6**: Apply structural adhesive to all joint interfaces

**Step 3.7**: Install permanent fasteners per schedule
- Longitudinal joints: M8x20, 150 mm spacing
- Circumferential joints: M8x25, 120 mm spacing
- Torque per specification

**Step 3.8**: Cure adhesive (24 hours minimum)

**Step 3.9**: Remove all temporary fasteners

**Step 3.10**: NDT inspection of all upper shell joints

### Phase 4: Floor and Door Integration (Week 11-12)

**Step 4.1**: Install floor beam assemblies (see [FLOOR_ASSEMBLIES](../FLOOR_ASSEMBLIES/))
- Primary beam grid
- Floor panels
- Seat tracks

**Step 4.2**: Install door frame assemblies (see [DOOR_FRAME_ASSEMBLIES](../DOOR_FRAME_ASSEMBLIES/))
- 8 passenger door frames
- 4 cargo door frames

**Step 4.3**: Install all environmental seals

**Step 4.4**: Install pressurization system test ports

### Phase 5: Final Inspection and Testing (Week 13-14)

**Step 5.1**: Dimensional inspection of complete pressure shell
- Full 3D laser scan
- Comparison to master CAD model
- Tolerance: ±1.0 mm overall

**Step 5.2**: Pressure test sequence:
- Leak test at 0.5 psi differential
- Structural test at 1.5× design differential (12 psi)
- Hold for 10 minutes minimum
- Monitor strain gauges at critical locations

**Step 5.3**: Final NDT inspection
- Ultrasonic inspection of all joints
- X-ray of critical fastener clusters
- Thermography of bond lines

**Step 5.4**: Documentation completion
- Assembly traveler sign-off
- QC inspection records
- Test reports
- As-built measurements

---

## Critical Tooling Requirements

| Tool ID | Description | Accuracy | Calibration |
|---------|-------------|----------|-------------|
| FAF-53-200 | Final Assembly Fixture | ±0.2 mm | Quarterly |
| LASER-TRACK-01 | Laser Tracker System | ±0.05 mm | Monthly |
| CRANE-50T | 50-Ton Overhead Crane | - | Annual |
| SPREADER-53-200 | Upper Shell Spreader Bar | ±0.3 mm | Semi-annual |

---

## Quality Gates

Assembly cannot proceed to next phase without:

1. **Phase 1 Gate**: All modules dimensionally compliant, NDT passed
2. **Phase 2 Gate**: Lower-side joints verified, pressure seal integrity confirmed
3. **Phase 3 Gate**: Full shell dimensionally compliant, all joints NDT approved
4. **Phase 4 Gate**: Floor and doors installed, fit verification passed
5. **Phase 5 Gate**: Pressure test passed, final inspections complete

---

## Personnel Requirements

- **Assembly Lead**: 1 (present all phases)
- **Composite Technicians**: 6-8
- **NDT Inspectors**: 2 (Level II certified)
- **Quality Engineers**: 2
- **Crane Operators**: 2 (certified for 50-ton capacity)
- **Tooling Technicians**: 2

---

## References

- [CS-25.783 – Fuselage Doors](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)
- [CS-25.789 – Retention of Items of Mass](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)
- Assembly Standards: `../ASSETS/Assembly_Standards.md`
- Fastener Schedules: `../ASSETS/Fastener_Schedules.csv`
- QC Inspection Points: `../ASSETS/QC_Inspection_Points.csv`

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status**: DRAFT – Subject to human review and approval
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22
