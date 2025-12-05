# Q100-61-INST-DEF-MOTOR-TO-GEARBOX — Alignment Requirements

## 1. Overview

Precise alignment between the electric motor and reduction gearbox is critical for efficient power transmission, bearing life, and vibration control. This document specifies alignment requirements and procedures.

## 2. Alignment Specifications

### 2.1 Angular Alignment

| Parameter | Limit | Target | Verification |
|-----------|-------|--------|--------------|
| Angular misalignment (all planes) | ≤0.5 mrad | 0.2 mrad | Laser alignment |
| Angular tolerance per tooth | ≤0.1 mrad | 0.05 mrad | Calculated |

### 2.2 Parallel Offset

| Parameter | Limit | Target | Verification |
|-----------|-------|--------|--------------|
| Radial offset (horizontal) | ≤0.05 mm | 0.02 mm | Laser alignment |
| Radial offset (vertical) | ≤0.05 mm | 0.02 mm | Laser alignment |
| Total indicator runout | ≤0.07 mm | 0.03 mm | Calculated |

### 2.3 Axial Position

| Parameter | Limit | Notes |
|-----------|-------|-------|
| Axial float range | 2.0 mm | Coupling design allowance |
| Nominal axial gap | 1.0 mm | Centered in float range |
| Thermal growth allowance | 0.5 mm | Motor expansion |

## 3. Alignment Method

### 3.1 Equipment Required

| Item | Specification |
|------|---------------|
| Laser alignment system | ±0.001 mm resolution |
| Dial indicators | 0.01 mm graduation |
| Feeler gauges | 0.02-1.00 mm set |
| Torque wrench | Calibrated, 10-100 Nm |

### 3.2 Procedure Overview

1. **Rough alignment** — Visual and straight edge
2. **Soft foot check** — All mounting points
3. **Laser setup** — Mount sensors on coupling halves
4. **Measurement** — Angular and offset readings
5. **Shimming** — Calculate and install shims
6. **Verification** — Re-measure and document
7. **Final torque** — Torque all fasteners to spec

### 3.3 Soft Foot Correction

| Mount Point | Maximum Soft Foot | Correction |
|-------------|-------------------|------------|
| Motor front left | 0.05 mm | Shim as required |
| Motor front right | 0.05 mm | Shim as required |
| Motor rear left | 0.05 mm | Shim as required |
| Motor rear right | 0.05 mm | Shim as required |

## 4. Thermal Considerations

### 4.1 Cold to Hot Growth

| Component | Temperature Rise °C | Axial Growth mm | Vertical Growth mm |
|-----------|---------------------|-----------------|-------------------|
| Motor | 60 | 0.3 | 0.15 |
| Gearbox | 40 | 0.2 | 0.10 |

### 4.2 Compensation

- Set motor 0.1 mm LOW at cold alignment
- Set motor 0.05 mm TOWARD gearbox at cold alignment

## 5. Verification Requirements

### 5.1 Initial Alignment

| Check | Acceptance Criteria |
|-------|---------------------|
| Angular misalignment | ≤0.3 mrad |
| Parallel offset | ≤0.03 mm TIR |
| Soft foot | ≤0.03 mm |
| Bolt torque | Per spec ±5% |

### 5.2 Hot Check (After 2-Hour Run)

| Check | Acceptance Criteria |
|-------|---------------------|
| Angular change | ≤0.2 mrad from prediction |
| Offset change | ≤0.02 mm from prediction |
| Vibration | ≤2.5 mm/s RMS |

## 6. Documentation

Record the following in the installation log:
- Date and technician
- Laser system calibration date
- All measurement readings (cold)
- Shim thickness at each mount
- Final alignment values
- Hot check results (if performed)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
