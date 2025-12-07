# Q100-61-INST-DEF-FAN-TO-GEARBOX — Balance Requirements

## 1. Overview

Precise balance of the open-fan assembly is critical for vibration control, bearing life, and passenger comfort. This document specifies the balance requirements and procedures.

## 2. Balance Limits

### 2.1 Component Balance (Before Assembly)

| Component | Static Imbalance | Dynamic Imbalance | Notes |
|-----------|------------------|-------------------|-------|
| Hub | ≤5 g·mm | ≤25 g·mm² | Factory balanced |
| Each blade | ≤2 g·mm | ≤10 g·mm² | Matched set |
| Spinner | ≤3 g·mm | ≤15 g·mm² | Factory balanced |

### 2.2 Assembled Fan Balance

| Parameter | Limit | Target | Verification |
|-----------|-------|--------|--------------|
| Static imbalance | ≤10 g·mm | ≤5 g·mm | Balance machine |
| Dynamic imbalance | ≤50 g·mm² | ≤25 g·mm² | Balance machine |
| Residual vibration | ≤2.5 mm/s RMS | ≤1.5 mm/s | Ground run |

### 2.3 In-Service Limits

| Condition | Vibration Limit | Action |
|-----------|-----------------|--------|
| Normal | ≤5 mm/s RMS | None |
| Elevated | 5-10 mm/s RMS | Monitor, schedule rebalance |
| High | 10-15 mm/s RMS | Reduce power, land ASAP |
| Critical | >15 mm/s RMS | Immediate power reduction |

## 3. Balance Procedure

### 3.1 Equipment Required

| Item | Specification |
|------|---------------|
| Balance machine | ≤1 g·mm sensitivity |
| Trial weights | 5-100 g set |
| Protractor | 1° resolution |
| Torque wrenches | Calibrated |
| Vibration analyzer | 0.1 mm/s resolution |

### 3.2 Procedure Steps

1. **Preparation**
   - Mount fan assembly on balance fixture
   - Verify all blades installed to correct pitch
   - Record blade serial numbers and positions

2. **Initial Spin**
   - Spin to 1500 RPM
   - Record imbalance magnitude and angle
   - Compare to limits

3. **Correction Calculation**
   - Calculate correction weight and position
   - Use two-plane method for dynamic balance
   - Account for influence coefficients

4. **Weight Installation**
   - Install correction weights at calculated positions
   - Use approved weight types only
   - Secure weights properly

5. **Verification Spin**
   - Re-spin at 1500 RPM
   - Verify within limits
   - Document final balance

### 3.3 Balance Weight Locations

| Location | Weight Type | Maximum |
|----------|-------------|---------|
| Hub inner ring | Clamp-on | 50 g per position |
| Hub outer ring | Bolt-on | 100 g per position |
| Blade cuff (if needed) | Adhesive | 20 g per blade |

## 4. Blade Matching

### 4.1 Moment Weight Matching

| Parameter | Tolerance |
|-----------|-----------|
| Individual blade moment | ±0.5% of nominal |
| Set matching | ≤0.3% blade-to-blade |
| Replacement blade | Match to set average |

### 4.2 Blade Position Effects

- Blades with higher moment should be installed opposite each other
- Track and balance chart determines optimal positions
- Document blade positions in installation record

## 5. Track and Balance

### 5.1 Blade Tracking

| Parameter | Limit | Method |
|-----------|-------|--------|
| Tip track variation | ≤5 mm | Strobe/flag |
| Track adjustment | Pitch link | Per AMM |

### 5.2 Post-Installation Ground Run

| Check | Duration | Acceptance |
|-------|----------|------------|
| Idle check | 5 min | ≤3 mm/s vibration |
| Mid-power check | 3 min | ≤4 mm/s vibration |
| Full-power check | 1 min | ≤5 mm/s vibration |

## 6. Documentation

Record in installation log:
- Balance machine readings (initial and final)
- Correction weights (mass, position, type)
- Blade serial numbers and positions
- Ground run vibration readings
- Technician signature and date

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---
