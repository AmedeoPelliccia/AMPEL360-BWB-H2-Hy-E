# 85-00-07-203: Refuelling Flow and Capacity Validation

## 1. Purpose
Validate that the LH2 refueling system delivers required flow rates and total fuel capacity within operational constraints (time, temperature, safety).

## 2. Performance Requirements
### 2.1 Flow Rate
- **Target**: ≥ 500 kg/min (design requirement, may vary by aircraft)
- **Margin**: +10% capacity for degraded conditions (low ground supply pressure)

### 2.2 Refueling Time
- **Full Refuel (0-100%)**: ≤ 30 minutes (for 10,000 kg LH2 capacity)
- **Top-Up (70-100%)**: ≤ 10 minutes (turnaround operations)

### 2.3 Fuel Quality
- **Purity**: ≥ 99.97% H2 (per ISO 14687)
- **Contaminants**: Total non-H2 gases < 300 ppm

## 3. Test Objectives
### 3.1 Flow Characterization
- Measure actual flow rate vs. pressure differential
- Verify control system maintains target flow rate
- Identify flow limitations (choked flow, cavitation, boil-off)

### 3.2 Thermal Management
- Monitor LH2 temperature rise during transfer
- Validate insulation and pre-cooling effectiveness
- Quantify boil-off losses during refueling

### 3.3 Capacity Verification
- Confirm aircraft tank ullage measurement accuracy
- Validate automatic shutoff at 98% capacity (safety margin)
- Demonstrate fuel quantity indication to flight deck

## 4. Test Methods
### 4.1 Bench Test (Component)
- **Test Rig**: Flow loop with simulated aircraft tank
- **Instrumentation**: Coriolis flow meters, cryogenic thermocouples
- **Scenarios**: Nominal flow, reduced pressure, cold soak, hot day

### 4.2 Ground Test (System)
- **Test Article**: Production-representative aircraft tank
- **Ground Cart**: Operational LH2 refueling equipment
- **Cycles**: Minimum 10 full refueling cycles to demonstrate repeatability

### 4.3 Operational Validation (Acceptance)
- **Airport Trials**: Refueling at actual airport with operational constraints
- **Turnaround Simulation**: Multiple refueling cycles with ground crew timing

## 5. Acceptance Criteria
- **Flow Rate**: ≥ 500 kg/min sustained over full refuel
- **Refuel Time**: ≤ 30 minutes (0-100%)
- **Temperature**: LH2 remains < -250°C throughout transfer
- **Boil-Off**: < 2% of transferred volume
- **Repeatability**: ≤ 5% variation over 10 cycles

## 6. Safety Verification
- **Overfill Protection**: Automatic shutoff at 98% capacity
- **Emergency Shutdown**: Refueling halted within 2 seconds of fault
- **Leak Detection**: No leaks detected during or after refueling

## 7. Documentation
- Test procedures: [85-00-07-A-201](./ASSETS/85-00-07-A-201_H2_Interface_Test_Procedures.pdf)
- Flow data: Captured in [85-00-07-A-202](./ASSETS/85-00-07-A-202_H2_Interface_Test_Reports.xlsx)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
