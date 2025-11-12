# Weight Distribution Test Rig
# Aircraft Weighing and CG Measurement System

**System ID:** WDR-02-10-002  
**Date:** 2026-Q3 (Planned)  
**Status:** Design Phase  
**Purpose:** Production weight and balance validation

---

## 1. Overview

### 1.1 Purpose

Precision aircraft weighing system for:
- Empty weight determination
- Center of gravity location measurement
- Weight distribution validation
- Production weight tracking
- Compliance with CS-25.25 (Weight Limits) and CS-25.29 (Empty Weight and CG)

---

## 2. System Design

### 2.1 Load Cell Configuration

**Main Gear Load Cells (2×):**
- Capacity: 50,000 kg each
- Accuracy: ±0.05% FS (±25 kg)
- Type: Compression, strain gauge
- Model: HBM C16A (or equivalent)

**Nose Gear Load Cell (1×):**
- Capacity: 15,000 kg
- Accuracy: ±0.05% FS (±7.5 kg)
- Type: Compression, strain gauge

**Jacking Pads:**
- Height-adjustable platforms (±50 mm)
- Level indicators (spirit level, ±0.1°)
- Quick-attach to aircraft jack points

### 2.2 Data Acquisition

**System:** National Instruments cDAQ-9189
- Channels: 4× strain gauge inputs (bridge completion)
- Sampling rate: 100 Hz
- Resolution: 24-bit
- Software: LabVIEW custom application

**Display:**
- Real-time weight readout (each gear + total)
- CG calculation (longitudinal + lateral)
- Tare function (subtract equipment weight)
- Data logging (CSV export)

---

## 3. Weighing Procedure

### 3.1 Preparation

1. **Aircraft Configuration:**
   - Remove all fluids (fuel, water, oil) - drain to minimum residual
   - Close all doors and panels
   - Remove loose equipment (if not part of OEW)
   - Install all required equipment (per weight & balance manual)
   - Set control surfaces to neutral (flaps up, gear down)

2. **Environmental:**
   - Indoor facility (wind < 5 kt)
   - Temperature: 15-25°C (record actual)
   - Level floor (verified within ±0.1° across footprint)

3. **Rig Setup:**
   - Position load cells under each gear
   - Level aircraft (pitch ±0.5°, roll ±0.3°)
   - Verify no external loads (remove tow bar, chocks, etc.)
   - Tare system (zero with aircraft on cells)

### 3.2 Measurement

1. Allow system to stabilize (5 minutes, weight readings stable within ±10 kg)
2. Record weight on each load cell (3 readings, 1 minute apart)
3. Calculate average weights
4. Repeat measurement after repositioning aircraft (verification)

**Acceptance:** Two measurements agree within ±0.2% or 50 kg, whichever is greater

### 3.3 Calculation

**Total Weight:**
W_total = W_nose + W_main_left + W_main_right

**Longitudinal CG:**
CG_x = (W_nose × L_nose + W_main × L_main) / W_total
- L_nose: Distance from datum to nose gear
- L_main: Distance from datum to main gear centerline

**Lateral CG:**
CG_y = (W_main_right - W_main_left) × Track_width / (2 × W_total)
- Track_width: Lateral separation of main gear

---

## 4. System Calibration

### 4.1 Procedure

**Load Cell Calibration:**
- Frequency: Annually + before each aircraft weighing
- Method: Deadweight calibration using certified masses
- Traceability: NIST-traceable calibration lab
- Points: 0%, 25%, 50%, 75%, 100% of rated capacity

**System Verification:**
- Known weight test (calibrated masses on each load cell)
- Acceptance: Reading within ±0.1% of applied load

### 4.2 Uncertainty Budget

| Source | Uncertainty (kg) |
|--------|-----------------|
| Load cell accuracy | ±25 |
| Load cell repeatability | ±10 |
| Temperature effect | ±5 |
| Eccentric loading | ±8 |
| Data acquisition | ±2 |
| **Combined (RSS)** | **±28 kg** |

**Total Weight Uncertainty:** ±28 kg (0.03% of MTOW)

---

## 5. Weight Tracking

### 5.1 Database

**Records for Each Aircraft:**
- Serial number, registration
- Weighing date and conditions
- Empty weight (actual vs. target)
- CG location (x, y, z)
- Equipment list (installed items)
- Deviations from specification

**Trending:**
- Weight growth monitoring (production series)
- Statistical analysis (mean, std dev)
- Corrective actions for out-of-tolerance aircraft

---

## 6. Budget and Schedule

### 6.1 Cost

| Item | Cost (€) |
|------|---------|
| Load cells (3×) | 35,000 |
| Jacking pads & structure | 25,000 |
| Data acquisition system | 15,000 |
| Software development | 10,000 |
| Calibration equipment | 8,000 |
| Installation & commissioning | 12,000 |
| **Total** | **105,000** |

### 6.2 Timeline

- Design: Q1 2026
- Procurement: Q2 2026
- Installation: Q3 2026
- Calibration & validation: Q3 2026
- Production ready: Q4 2026

---

## 7. Deliverables

1. **Weighing Procedure** - Step-by-step work instruction
2. **Calibration Plan** - Annual calibration schedule
3. **Weighing Form** - Data collection template
4. **Database** - Weight & CG tracking system
5. **Training Materials** - Operator certification program

---

**Document Owner:** Weight & Balance Engineer  
**Approval:** [ ] Manufacturing | [ ] QA | [ ] Flight Test  
**Status:** Design Phase
