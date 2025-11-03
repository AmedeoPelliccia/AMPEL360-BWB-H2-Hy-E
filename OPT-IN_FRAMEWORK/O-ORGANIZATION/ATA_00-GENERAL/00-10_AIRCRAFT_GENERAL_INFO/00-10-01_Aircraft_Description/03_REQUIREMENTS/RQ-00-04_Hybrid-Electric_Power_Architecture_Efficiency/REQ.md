# RQ-00-04 — Hybrid-Electric Power Architecture Efficiency

## Statement
The integrated **hybrid-electric propulsion system** — composed of **H₂ PEM fuel cells**, **open-fan propulsors**, and **closed-loop CO₂ buffer batteries** — shall achieve a **minimum total powertrain efficiency ≥ 55% (net DC-to-thrust)** under cruise conditions, and ≥ **48%** at mission average power, accounting for all electrical conversion, cooling, and propulsion losses.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **System-Level Efficiency**
   - η_total = (Thrust Power) / (Fuel Cell DC Power + CO₂ Buffer DC Power Input)  
   - ≥ 0.55 in cruise (M0.78 @ FL350).  
   - ≥ 0.48 for mission-weighted average over design range (3,500 km).  
   - Verified with representative **EMS dispatch schedule** and **thermal steady-state**.

2. **Subsystem Performance**
   - Fuel cell stack efficiency ≥ 60% (HHV basis) at 70% load.  
   - DC/DC conversion efficiency ≥ 97%.  
   - Open-fan propulsor propulsive efficiency ≥ 83%.  
   - CO₂ buffer round-trip efficiency ≥ 90%.  

3. **Thermal & Electrical Stability**
   - No continuous bus oscillation > ±1.5% Vnom.  
   - Stack coolant outlet temperature ≤ 80°C at max cruise power.  
   - Thermal rejection design margin ≥ 10% under ISA+10°C.

🔗 Artefacts:
- Efficiency model: ../../ENGINEERING/analyses/electrical/[**hybrid_efficiency_model.md**](../../ENGINEERING/analyses/electrical/hybrid_efficiency_model.md)  
- Powertrain block diagram: ../../DESIGN/system_design/[**hybrid_architecture_overview.md**](../../DESIGN/system_design/hybrid_architecture_overview.md)  
- Thermal map: ../../ENGINEERING/analyses/thermal/[**thermal_balance_map.md**](../../ENGINEERING/analyses/thermal/thermal_balance_map.md)

---

## Rationale
Target efficiency ensures compliance with zero-emission mission energy constraints while keeping hydrogen consumption and waste heat manageable.  
The closed-loop CO₂ battery minimizes transient hydrogen draw and enhances regenerative braking recovery.  
🔗 Reference concept: ../../DESIGN/system_design/[**hybrid_energy_management.md**](../../DESIGN/system_design/hybrid_energy_management.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **E2-24** Electrical Power  
  - **C2-28** Fuel (H₂/CO₂ hybrid loop)  
  - **P-61** Open-Fan Propulsors  
  - **L1-22** Energy Management Logic  
  - **E3-39** Electrical Panels and Conversion  
- **Secondary interfaces:**  
  - **A2 Aerodynamics** (installation drag and flow interference)  
  - **O-Operating Systems** (control coordination layer)

🔗 Decompositions:  
- Fuel-cell performance → ../SR/[**SR-ENER-001.md**](../SR/SR-ENER-001.md)  
- Power conversion & bus stability → ../SR/[**SR-ELEC-002.md**](../SR/SR-ELEC-002.md)  
- EMS optimization logic → ../SR/[**SR-CTRL-007.md**](../SR/SR-CTRL-007.md)

---

## Constraints & Interfaces
- Cryogenic hydrogen temperature and CO₂ cycle pressure limits per **ATA 28**, **ATA 21-80-00 (prov.)**.  
- HVDC bus nominal 540 V ±5%.  
- EMS dispatch must coordinate with IMA applications through **L2-LINKS (ATA 42)**.  

🔗 Interface refs:  
- ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)  
- ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)

---

## Assumptions
- Operating altitude FL350–370; ambient -50°C.  
- Stack degradation < 5% over 10,000 cycles.  
- Battery thermal loop uses same cryogenic sink as FC cooling, managed by regenerative HX.  
- Propulsor efficiency maps validated by rig testing.  

🔗 Supporting analysis: ../../ENGINEERING/analyses/thermal/[**cooling_loop_design.md**](../../ENGINEERING/analyses/thermal/cooling_loop_design.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Steady-state and transient energy flow models validated vs. component data.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)
- **Simulation:** SIL/HIL EMS optimization under mission profile dispersion.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)
- **Ground Test:** Hardware-in-loop bench with integrated FC, CO₂ buffer, and propulsor emulator.  
  - Results: ../../V_AND_V/verification/results/[**hybrid_bench_revA/**](../../V_AND_V/verification/results/hybrid_bench_revA/)

Acceptance when all metrics ≥ thresholds and model-to-test delta ≤ 2.5%.

🔗 Coverage & Trace:  
- Coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Trace: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification Basis:** ../ALR/[**ALR-004.md**](../ALR/ALR-004.md)  
- **Safety Allocations:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)  
- **Applicable Standards:**  
  - **DO-311A** (Battery Safety)  
  - **DO-160G** (Environmental Conditions)  
  - **ARP4754A / ARP4761** (System Development & Safety)  
  - **CS-25 Subpart E** (Powerplant)

🔗 Mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-004.md**](../ALR/ALR-004.md)  
- **Linked SRs:** ../SR/[**SR-ENER-001.md**](../SR/SR-ENER-001.md) · ../SR/[**SR-CTRL-007.md**](../SR/SR-CTRL-007.md)  
- **V&V Cross-Refs:** ../../V_AND_V/cases/[**TEST-ENER-EFF-001**](../../V_AND_V/cases/TEST-ENER-EFF-001.md) · ../../V_AND_V/cases/[**TEST-SIM-HYB-002**](../../V_AND_V/cases/TEST-SIM-HYB-002.md)  
- **RTM:** ../RTM/[**RTM-ENER-001.csv**](../RTM/RTM-ENER-001.csv)

---

## Notes
Performance margins shall be reviewed after initial flight test data to update powertrain efficiency maps.  
Revised targets will feed EMS optimization tuning via the **OPT-IN digital thread**.
