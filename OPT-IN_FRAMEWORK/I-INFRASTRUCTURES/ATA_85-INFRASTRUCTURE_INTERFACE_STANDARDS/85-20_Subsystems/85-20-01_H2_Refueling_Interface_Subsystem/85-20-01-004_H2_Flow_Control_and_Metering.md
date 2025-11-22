# 85-20-01-004 — H2 Flow Control and Metering

## Document Metadata

```yaml
document_id: "85-20-01-004"
title: "H2 Flow Control and Metering"
parent_system: "85-20-01 H2 Refueling Interface Subsystem"
category: "Component Specification"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

This document specifies the flow control and metering systems that regulate H2 flow rate, measure quantity transferred, and manage refueling completion for safe and efficient operations.

## Flow Control System

### Flow Control Valve

**Type:** Electrically actuated proportional valve with position feedback

**Control:** PID (Proportional-Integral-Derivative) control for smooth flow regulation

**Flow Range:** 0-3 kg H2/min (nominal 1-2 kg/min)

**Response Time:** <500ms to achieve setpoint flow rate

**Positioning Accuracy:** ±2% of commanded position

### Flow Rate Control Strategy

**Phase 1: Initial Fill (0-20% tank capacity)**
- Slow flow rate: 0.5 kg/min
- Purpose: Verify system integrity, minimize temperature rise

**Phase 2: Bulk Fill (20-90% tank capacity)**
- Normal flow rate: 1.5-2.0 kg/min
- Purpose: Efficient refueling while managing thermal effects

**Phase 3: Topping (90-100% tank capacity)**
- Reduced flow rate: 0.5-1.0 kg/min
- Purpose: Precise final quantity, minimize overshoot

**Adaptive Control:** Flow rate adjusted based on:
- Tank pressure (reduce flow as pressure increases)
- Temperature (reduce flow if excessive heating)
- Safety conditions (reduce or stop on warnings)

## Pressure Management

### Pressure Regulation

**Supply Pressure:** Variable (typically 400-900 bar from ground storage)

**Delivery Pressure:** Matched to aircraft tank pressure (350 or 700 bar nominal)

**Pressure Regulator:** Two-stage regulation for stability

**Stage 1:** High-pressure regulator (supply → 400 bar intermediate)
**Stage 2:** Fine regulator (400 bar → tank pressure + margin)

### Pressure Monitoring

**Upstream Pressure Transducer:**
- Range: 0-1000 bar
- Accuracy: ±0.5% full scale
- Purpose: Monitor supply pressure, detect supply issues

**Downstream Pressure Transducer (at Coupling):**
- Range: 0-1000 bar
- Accuracy: ±0.25% full scale
- Purpose: Monitor aircraft tank pressure, control refueling completion

**Differential Pressure:**
- Calculate: ΔP = P_supply - P_tank
- Purpose: Ensure adequate pressure differential for flow (minimum 50 bar)

### Over-Pressure Protection

**Pressure Relief Valve:** Set at 1.1x maximum operating pressure (typically 770 bar for 700 bar system)

**Over-Pressure Shutdown:** Automatic valve closure if pressure exceeds limit

**Pressure Limiting Control:** Software limit prevents commanding pressure above maximum

## Flow Metering

### Mass Flow Meter

**Technology:** Coriolis mass flow meter (direct mass measurement, independent of pressure/temperature)

**Range:** 0-5 kg/min (oversized for margin)

**Accuracy:** ±0.5% of reading

**Output:** 4-20 mA analog + digital (Modbus, HART, or similar)

**Temperature Compensation:** Integrated temperature sensor for density correction (if needed)

### Totalizer

**Function:** Accumulate total mass of H2 transferred during refueling operation

**Accuracy:** ±1% of total quantity (accumulated error over full refueling)

**Display:** Real-time totalizer on HMI (kg transferred)

**Reset:** Automatic reset at start of new refueling operation

**Backup:** Independent hardware totalizer for billing verification

### Volumetric Correction

**Standard Conditions:** H2 quantity reported at standard conditions (15°C, 1 bar) for consistency

**Correction Factors:**
- Temperature (via temperature sensor at flow meter)
- Pressure (via pressure transducer)
- Compressibility (per real gas equation of state for H2)

**Calculation:** Mass_std = Mass_measured × (P_measured / P_std) × (T_std / T_measured) × Z_factor

## Refueling Completion Logic

### Target Quantity Determination

**Source:** Aircraft data (via 85-20-06 communication)

**Inputs:**
- Aircraft H2 tank capacity (e.g., 500 kg)
- Current H2 quantity on board (from aircraft gauging)
- Requested quantity to upload

**Calculation:** Target_qty = Requested_qty OR (Capacity - Current_qty) whichever less

### Completion Detection

**Method 1: Quantity-Based (Primary)**
- Monitor totalizer
- When total >= Target_qty, initiate shutdown sequence

**Method 2: Pressure-Based (Secondary)**
- Monitor tank pressure
- When tank pressure >= Target_pressure (e.g., 700 bar for Type IV tank), initiate shutdown

**Method 3: Flow-Based (Backup)**
- Monitor flow rate
- If flow drops below minimum (tank full, cannot accept more), initiate shutdown

### Shutdown Sequence

**Phase 1: Flow Ramp-Down (0-5 seconds)**
1. Gradually close flow control valve (prevents pressure surge)
2. Reduce flow from bulk rate to zero over 5 seconds

**Phase 2: Valve Closure (5-6 seconds)**
1. Close main shutoff valve
2. Verify zero flow on flow meter

**Phase 3: System Stabilization (6-10 seconds)**
1. Monitor tank pressure (allow pressure equalization)
2. Verify no leaks (H2 detection, coupling leak detector)

**Phase 4: Completion Indication (10+ seconds)**
1. Display "Refueling Complete" on HMI
2. Transmit completion status to aircraft and operations center (via 85-20-06)
3. Log transaction (aircraft ID, quantity transferred, duration, timestamp)

## Thermal Management

### Compression Heating

**Issue:** H2 compression during refueling generates heat, raising gas temperature

**Calculation:** ΔT ≈ 40-60°C for 350 bar refueling, 80-100°C for 700 bar refueling (adiabatic compression)

**Mitigation:**
- Flow rate control (slower flow = more time for heat dissipation)
- Pre-cooling (optional, for future LH2 or high-rate systems)

### Temperature Monitoring

**Sensors:**
- H2 gas temperature (at flow meter and coupling)
- Coupling and hose surface temperature

**Limits:**
- H2 gas: <85°C (warning), <100°C (critical)
- Coupling surface: <100°C (advisory)

**Control Action:** Reduce flow rate if temperature limits approached

## Metering Accuracy and Verification

### Calibration

**Frequency:** Annual or every 1000 refueling operations (whichever first)

**Method:**
- Gravimetric calibration (weigh reference cylinder before/after H2 transfer)
- OR Comparison to reference master meter (if available)

**Acceptance:** ±0.5% agreement with reference

**Records:** Calibration certificate for flow meter, stored electronically

### Billing Accuracy

**Requirement:** ±1% total quantity for commercial billing (if applicable)

**Verification:** Independent totalizer, periodic audit

**Traceability:** Flow meter traceable to national standards (NIST, PTB, etc.)

## Control System Architecture

### Hardware

**PLC or Embedded Controller:** Industrial-grade, rated for outdoor use (-20 to +60°C)

**I/O Modules:**
- Analog inputs: Pressure, temperature, flow rate (4-20 mA, 0-10V)
- Digital inputs: Interlocks, emergency stop, status signals
- Analog outputs: Valve control (4-20 mA)
- Digital outputs: Alarms, status indicators

**Safety Relay Module:** Independent of main PLC, hardwired safety logic

### Software

**Control Algorithm:** PID control for flow rate, state machine for refueling sequence

**Data Logging:** Log all sensor data (1 Hz) and events (timestamp, value, alarm status)

**Diagnostics:** Self-test at startup, continuous health monitoring

**Updates:** Version-controlled software, change management process

### Communication Interfaces

**Local HMI:** Touchscreen display for operator

**Data Link (to 85-20-06):** Ethernet, Modbus TCP, or OPC UA for:
- Refueling authorization
- Status reporting
- Audit data

**Maintenance Port:** USB or Ethernet for diagnostics and software updates

## Performance Specifications

| Parameter | Value | Verification Method |
|-----------|-------|---------------------|
| Flow Rate Range | 0.5-3.0 kg H2/min | Flow test with reference |
| Flow Control Accuracy | ±5% of setpoint | Closed-loop test |
| Pressure Range | 0-1000 bar | Sensor datasheet |
| Pressure Accuracy | ±0.5% FS (upstream), ±0.25% FS (downstream) | Calibration test |
| Flow Meter Accuracy | ±0.5% of reading | Gravimetric calibration |
| Totalizer Accuracy | ±1% of total quantity | End-to-end refueling test |
| Valve Response Time | <500 ms | Step response test |

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21

---

*Reference: [85-20-01 H2 Refueling Interface Subsystem README](./README.md)*
