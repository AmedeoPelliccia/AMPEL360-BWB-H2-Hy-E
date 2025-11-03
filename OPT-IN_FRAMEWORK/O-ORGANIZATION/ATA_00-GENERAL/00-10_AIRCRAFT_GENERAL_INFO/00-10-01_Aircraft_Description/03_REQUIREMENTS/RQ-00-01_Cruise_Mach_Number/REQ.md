# RQ-00-01 — Cruise Mach Number

## Statement
The aircraft shall achieve a **cruise Mach number ≥ 0.78** at **FL350 (≈10.7 km)** in **ISA conditions**, at **design operating weight (DOW + mission fuel for design range)**, with **normal system configuration** and **open-fan propulsors in nominal efficiency band**.

- 🔗 Supporting docs for this requirement: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
- Demonstrated **steady cruise** at **M ≥ 0.78** with:
  - Thrust specific power margin ≥ **5%** (available vs. required)  
  - Flight path angle |γ| ≤ **0.2°** for ≥ **20 min** stabilized segment  
  - Fuel-cell stack operating point within certified limits (temperature, voltage spread, humidity)  
  - CO₂ buffer cycling ≤ **±5% SOC** around its nominal cruise set-point  
  - Compliance with **CS-25** performance and handling qualities applicable to cruise
- Sensitivity verified for **ISA ±10°C** and **±2%** pressure deviation.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-ENER-001**](../../V_AND_V/cases/TEST-ENER-001.md)  
- SIL/HIL: ../../V_AND_V/cases/[**TEST-SIM-CRZ-001**](../../V_AND_V/cases/TEST-SIM-CRZ-001.md)  
- Flight: ../../V_AND_V/cases/[**TEST-FT-CRZ-078**](../../V_AND_V/cases/TEST-FT-CRZ-078.md)

---

## Rationale
Mach 0.78 ensures competitive block times versus tube-and-wing benchmarks while preserving BWB aero efficiency and open-fan acoustic margins.  
🔗 Background analysis: ../../DESIGN/system_design/[**performance_rationale.md**](../../DESIGN/system_design/performance_rationale.md)

---

## Scope & Allocation
- **Primary domains:** A2 (Aerodynamics), P-61 (Open-fan), E2-24 (HVDC), C2-28 (H₂/CO₂), L1-22/27 (Autoflight & Control Laws).
- **Aircraft-level KPI:** Block time and mission fuel at design range.

🔗 Decompositions (examples):  
- Propulsor capability → ../SR/[**SR-PROP-004.md**](../SR/SR-PROP-004.md)  
- EMS cruise management → ../SR/[**SR-CTRL-007.md**](../SR/SR-CTRL-007.md)

---

## Constraints & Interfaces
- Must not violate **noise constraints (CS-36)** in step-climb profiles near M0.78.  
- EMS shall maintain FC efficiency ≥ design target and keep CO₂ buffer within cruise limits without thrust oscillations.

🔗 Interface refs: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md) · ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)

---

## Assumptions
- Clean configuration (no external stores), anti-ice OFF, cabin pressurization nominal.  
- Turbogenerator (SAF) **OFF** in zero-emission cruise.  
- Open-fan propulsors within validated aeroacoustic envelope for the specified Mach/Re.

🔗 Config evidence: ../../ENGINEERING/analyses/structural/[**mass_properties_baseline.md**](../../ENGINEERING/analyses/structural/mass_properties_baseline.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Mission/performance analysis; propulsion-aero coupling; EMS power-split models.  
  - 🔗 Plan: ../../V_AND_V/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)
- **Simulation (SIL/HIL):** 6-DoF with aero/prop maps; EMS closed-loop.  
  - 🔗 Procedures: ../../V_AND_V/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)
- **Ground Test:** Propulsor rig maps → installation corrections.  
- **Flight Test:** Demonstration at FL350; performance carding per test plan.  
  - 🔗 Results bucket: ../../V_AND_V/results/[**cruise_performance_revA/**](../../V_AND_V/verification/results/cruise_performance_revA/)

**Acceptance evidence:** model-to-flight correlation ≤ **3%** delta in drag and power.  
🔗 Coverage: ../../V_AND_V/coverage/[**code_coverage.md**](../../V_AND_V/coverage/7J_code_coverage.csv) · ../../V_AND_V/traceability/[**req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-001.md**](../ALR/ALR-001.md)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md) → ../../SAFETY/SSA/[**SSA_report.md**](../../SAFETY/SSA/SSA_report.md)  
- **Standards mapping:** ../../CERTIFICATION/[**CS25_mapping.md**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-001.md**](../ALR/ALR-001.md)  
- **Linked SRs:** ../SR/[**SR-PROP-004.md**](../SR/SR-PROP-004.md) · ../SR/[**SR-CTRL-007.md**](../SR/SR-CTRL-007.md)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-ENER-001**](../../V_AND_V/cases/TEST-ENER-001.md) · ../../V_AND_V/cases/[**TEST-SIM-CRZ-001**](../../V_AND_V/cases/TEST-SIM-CRZ-001.md) · ../../V_AND_V/cases/[**TEST-FT-CRZ-078**](../../V_AND_V/cases/TEST-FT-CRZ-078.md)  
- **RTM rows:** ../RTM/[**RTM-CRZ-001.csv**](../RTM/RTM-CRZ-001.csv) · ../RTM/[**RTM-CRZ-002.csv**](../RTM/RTM-CRZ-002.csv) · ../RTM/[**RTM-CRZ-003.csv**](../RTM/RTM-CRZ-003.csv)

---

## Notes
If the final certified cruise level differs (e.g., FL330/FL370), this requirement shall be re-verified with identical criteria and updated atmospheric and Reynolds corrections.

