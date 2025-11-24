# Boundary Conditions – Global FEA Model

## 1. Purpose

This document defines the boundary conditions used in the ATA 53 Global FEA Model for different analysis scenarios.

---

## 2. Coordinate System

```yaml
coordinate_system:
  origin: "Aircraft nose (STA 0)"
  x_axis: "Positive forward (fuselage longitudinal)"
  y_axis: "Positive right (spanwise)"
  z_axis: "Positive up (vertical)"
```

---

## 3. Standard Boundary Condition Sets

### 3.1 BC Set 1: Wing Attachment Analysis

Used for fuselage loads with wing as reactive structure.

| BC ID | Location | Grid Set | DOF Constrained | Description |
|-------|----------|----------|-----------------|-------------|
| BC-001 | Wing-fuselage attach fwd | GSET-WNG-FWD | 1,2,3,4,5,6 | Fixed at forward spar |
| BC-002 | Wing-fuselage attach aft | GSET-WNG-AFT | 1,2,3 | Pinned at rear spar |

### 3.2 BC Set 2: Landing Gear Analysis

Used for landing impact load cases.

| BC ID | Location | Grid Set | DOF Constrained | Description |
|-------|----------|----------|-----------------|-------------|
| BC-010 | Main gear trunnion L | GSET-MLG-L | 1,2,3 | Ground reaction point |
| BC-011 | Main gear trunnion R | GSET-MLG-R | 1,2,3 | Ground reaction point |
| BC-012 | Nose gear attachment | GSET-NLG | 1,2,3 | Ground reaction point |

### 3.3 BC Set 3: Pressure Analysis

Used for cabin pressurization load cases.

| BC ID | Location | Grid Set | DOF Constrained | Description |
|-------|----------|----------|-----------------|-------------|
| BC-020 | Wing attachment | GSET-WNG | 1,2,3,4,5,6 | Fixed support |
| BC-021 | Empennage attach | GSET-EMP | 1,2,3 | Symmetric support |

---

## 4. Load Application

### 4.1 Inertia Loads

Applied as GRAV load with appropriate acceleration factors per load case.

### 4.2 Pressure Loads

Applied as PLOAD2 on internal pressure shell elements.

### 4.3 Point Loads

Applied at interface grids using FORCE cards.

---

## 5. Document Control

- **Document ID**: 53-00-04-04-004
- **Version**: 1.0
- **Date**: 2025-11-24
- **Owner**: ATA 53 Stress Team Lead
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-24_.

---
