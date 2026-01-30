# 85-00-07-503: Passenger Flow Simulation Validation

## 1. Purpose
Validate computational passenger flow models used to predict boarding times, evacuation performance, and cabin congestion.

## 2. Simulation Tools
### 2.1 Evacuation Simulation
- **Pathfinder** (Thunderhead Engineering): Agent-based egress modeling
- **STEPS** (Mott MacDonald): Pedestrian simulation for evacuation
- **FDS+Evac** (VTT/NIST): Fire + evacuation integrated modeling

### 2.2 Boarding Simulation
- **AnyLogic**: Multi-method simulation (agent-based, discrete event)
- **SimPy** (Python): Discrete event simulation
- **Custom Models**: Tailored to AMPEL360 cabin layout and boarding policy

## 3. Model Validation Approach
### 3.1 Input Parameters
- **Cabin Geometry**: Seat pitch, aisle width, door locations (from CAD)
- **Passenger Characteristics**: Walking speed, body dimensions, baggage size
- **Behavioral Assumptions**: Exit selection, queue formation, response time

### 3.2 Calibration Data
- **Benchmark Aircraft**: Evacuation and boarding data from similar aircraft
- **Literature**: Human factors studies (NIST, FAA, EASA research)
- **Preliminary Tests**: Small-scale trials to refine parameters

### 3.3 Validation Tests
- **Boarding Trials**: Measure actual boarding time, compare to simulation
- **Evacuation Pre-Tests**: Timed egress trials with volunteers
- **Sensitivity Analysis**: Vary parameters to assess model robustness

## 4. Validation Metrics
### 4.1 Evacuation
- **Total Evacuation Time**: Simulated vs. actual (target: ±10%)
- **Exit Utilization**: Per-exit throughput (target: ±15%)
- **Congestion Points**: Identify locations where passengers accumulate

### 4.2 Boarding
- **Boarding Time**: Simulated vs. actual turnaround boarding phase
- **Seat-to-Seat Interference**: Passengers blocking aisles with baggage
- **Boarding Policy Impact**: Front-to-back vs. back-to-front vs. random

## 5. Acceptance Criteria
### 5.1 Model Accuracy
- **Evacuation Time**: Within ±10% of physical test results
- **Boarding Time**: Within ±15% of operational trials
- **Flow Rates**: Per-exit flow rates within ±15%

### 5.2 Model Confidence
- **Multiple Scenarios**: Model validated across ≥ 5 different test cases
- **Statistical Analysis**: Mean and 95th percentile predictions align with data
- **Expert Review**: Model assumptions reviewed by human factors specialists

## 6. Application
### 6.1 Design Optimization
- Evaluate cabin layout alternatives (aisle width, cross-aisle location)
- Optimize emergency exit placement
- Inform boarding policy recommendations

### 6.2 Certification Evidence
- Supplement physical evacuation demonstration with simulation analysis
- Demonstrate robustness to variations (passenger load, exit blockage)

### 6.3 Operational Planning
- Predict boarding times for different load factors
- Evaluate impact of passengers with reduced mobility (PRM)

## 7. Documentation
- Model description document (algorithms, assumptions, parameters)
- Validation report: Comparison of simulated vs. actual results
- Sensitivity analysis results
- Reference: [85-00-07-A-502](./ASSETS/85-00-07-A-502_Evacuation_Test_Reports.xlsx)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
