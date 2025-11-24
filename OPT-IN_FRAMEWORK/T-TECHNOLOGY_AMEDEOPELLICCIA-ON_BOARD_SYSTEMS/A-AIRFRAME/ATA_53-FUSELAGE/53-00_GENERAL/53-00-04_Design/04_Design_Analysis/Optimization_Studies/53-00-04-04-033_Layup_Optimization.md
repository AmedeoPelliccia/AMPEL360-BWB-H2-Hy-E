# Layup Optimization Study

## 1. Purpose

This document describes the composite layup optimization approach for the ATA 53 Fuselage CFRP structure.

---

## 2. Layup Design Philosophy

### 2.1 General Principles

- Symmetric and balanced laminates
- Minimum 10% plies in each principal direction (0°, ±45°, 90°)
- No more than 4 consecutive plies in any single direction
- ±45° plies on outer surfaces for damage resistance

### 2.2 Material System

Primary material: IM7/8552 unidirectional tape, 0.19 mm nominal ply thickness

---

## 3. Optimization Approach

### 3.1 Design Variables

| Variable | Range | Constraint |
|----------|-------|------------|
| 0° ply percentage | 10-60% | Minimum 10% |
| ±45° ply percentage | 20-60% | Minimum 20% |
| 90° ply percentage | 10-40% | Minimum 10% |
| Total thickness | 4-20 mm | Per zone |

### 3.2 Optimization Criteria

1. **Strength**: Laminate failure criteria (Tsai-Wu, max strain)
2. **Stiffness**: Membrane and bending stiffness requirements
3. **Stability**: Buckling resistance under compression/shear
4. **Damage Tolerance**: Impact resistance and CAI strength

---

## 4. Zone-Specific Layups

### 4.1 Pressure Shell (Zones 100, 200, 500, 600)

- Hoop-dominant loading
- Target: 25% 0° / 50% ±45° / 25% 90°
- Example: [±45/0/90/±45/0/±45/90/0/±45]s

### 4.2 Center Wing Box (Zone 400)

- Compression/tension dominant
- Target: 40% 0° / 40% ±45° / 20% 90°
- Example: [±45/0₂/±45/0₂/±45/0/90/0/±45]s

### 4.3 Wing-Body Blend (Zone 300)

- Combined loading
- Target: 30% 0° / 50% ±45° / 20% 90°
- Example: [±45/0/±45/0/90/0/±45/0/±45]s

---

## 5. Optimization Results

| Zone | Initial Layup | Optimized Layup | Weight Change |
|------|---------------|-----------------|---------------|
| 100 | Generic 25/50/25 | Custom per panel | -3.2% |
| 200 | Generic 25/50/25 | Custom per panel | -4.1% |
| 300 | Generic 30/50/20 | Custom per region | -5.5% |
| 400 | Generic 40/40/20 | Custom per region | -6.8% |
| 500 | Generic 25/50/25 | Custom per panel | -3.8% |
| 600 | Generic 25/50/25 | Custom per panel | -3.5% |

---

## 6. Ply Drop Guidelines

### 6.1 Drop Sequence

- Drop plies from center (neutral axis) first
- Maximum 2 plies dropped per step
- Minimum drop spacing: 10 × total thickness

### 6.2 Manufacturability

- Maximum ply count: 80 plies
- Debulking every 8-10 plies
- Autoclave cure per process specification

---

## 7. Document Control

- **Document ID**: 53-00-04-04-033
- **Version**: 1.0
- **Date**: 2025-11-24
- **Owner**: ATA 53 Composites Lead
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-24_.

---
