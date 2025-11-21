# 02-40-13 – Performance Calculator

## Purpose

This folder contains the performance calculation engine that computes takeoff, landing, and cruise performance for the AMPEL360 BWB-H₂-Hy-E aircraft. The calculator integrates BWB-specific aerodynamic models and hydrogen propulsion characteristics, with optional NN-assisted enhancements.

---

## Scope

- **Takeoff Algorithm**: Runway required, V-speeds, climb gradients
- **Landing Algorithm**: Landing distance, approach speeds, contaminated runway cases
- **Cruise Optimization**: Cost index optimization, speed/altitude selection
- **BWB-Specific Calculations**: Custom aerodynamic models for blended wing body
- **NN Integration**: Neural network-assisted performance predictions with safety constraints

---

## Certification

This module is safety-critical and certified to [DO-178C](https://www.rtca.org/content/standards-guidance-materials) **Level C** (Major failure condition).

---

## Documentation Files

- **[02-40-13-001_Calculator_Architecture.md](02-40-13-001_Calculator_Architecture.md)**: Architecture of performance calculation engine
- **[02-40-13-002_Takeoff_Algorithm.md](02-40-13-002_Takeoff_Algorithm.md)**: Takeoff performance algorithms and assumptions
- **[02-40-13-003_Landing_Algorithm.md](02-40-13-003_Landing_Algorithm.md)**: Landing performance algorithms and safety margins
- **[02-40-13-004_Cruise_Optimization.md](02-40-13-004_Cruise_Optimization.md)**: Cruise optimization logic with cost index
- **[02-40-13-005_BWB_Specific_Calculations.md](02-40-13-005_BWB_Specific_Calculations.md)**: BWB-specific aerodynamic models
- **[02-40-13-006_NN_Integration.md](02-40-13-006_NN_Integration.md)**: Neural network integration and safety constraints

---

## ASSETS Structure

### Source_Code/
- **core_engine/**: Core calculation engine (Python/NumPy or C++)
- **nn_wrapper/**: NN inference integration (ONNX runtime)
- **validation/**: Validation suite with reference cases
- **benchmarks/**: Performance benchmarks and profiling scripts

### Algorithms/
- **02-40-13-A-101_Takeoff_Algorithm.pdf**: Formal takeoff algorithm description
- **02-40-13-A-102_Landing_Algorithm.pdf**: Formal landing algorithm description
- **02-40-13-A-103_Optimization_Methods.pdf**: Optimization methods overview

### Validation/
- **02-40-13-A-201_Flight_Test_Correlation.xlsx**: Correlation with flight test data
- **02-40-13-A-202_CFD_Validation.xlsx**: Validation against CFD results

---

## Integration

Used by:
- **[02-40-11 EFB Software](../02-40-11_EFB_Software/)**: Embedded calculation library
- **[02-40-15 Flight Planning Software](../02-40-15_Flight_Planning_Software/)**: Route optimization constraints

---

## References

- [EASA CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)
- [DO-178C](https://www.rtca.org/content/standards-guidance-materials)
- [ATA 28 H₂ Fuel System](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: _2025-11-21_.
