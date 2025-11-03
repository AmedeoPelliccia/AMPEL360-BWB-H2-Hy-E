# RQ-00-01 — Cruise Mach Number

## Statement

The aircraft shall achieve a **cruise Mach number ≥ 0.78** at **FL350 (≈10.7 km)** in **ISA conditions**, at **design operating weight (DOW + mission fuel for design range)**, with **normal system configuration** and **open-fan propulsors in nominal efficiency band**.

* 🔗 Supporting docs for this requirement: [VERIF.md](../../../07_V_AND_V/VERIF.md) · [TRACE.csv](../../../07_V_AND_V/TRACE.csv) · [CHANGES.md](../../../07_V_AND_V/CHANGES.md) · [EVIDENCE/](../../../07_V_AND_V/EVIDENCE/)

---

## Acceptance Criteria

* Demonstrated **steady cruise** at **M ≥ 0.78** with:

  * Thrust specific power margin ≥ **5%** (available vs. required)
  * Flight path angle |γ| ≤ **0.2°** for ≥ **20 min** stabilized segment
  * Fuel-cell stack operating point within certified limits (temperature, voltage spread, humidity)
  * CO₂ buffer cycling ≤ **±5% SOC** around its nominal cruise set-point
  * Compliance with **CS-25** performance and handling qualities applicable to cruise

* Sensitivity verified for **ISA ±10°C** and **±2%** pressure deviation.

🔗 Test artefacts:

* Analysis: ../../../07_V_AND_V/cases/[**TEST-ENER-001**](../../../07_V_AND_V/cases/TEST-ENER-001.md)
* SIL/HIL: ../../../07_V_AND_V/cases/[**TEST-SIM-CRZ-001**](../../../07_V_AND_V/cases/TEST-SIM-CRZ-001.md)
* Flight: ../../../07_V_AND_V/cases/[**TEST-FT-CRZ-078**](../../../07_V_AND_V/cases/TEST-FT-CRZ-078.md)

---

## Rationale

Mach 0.78 ensures competitive block times versus tube-and-wing benchmarks while preserving BWB aero efficiency and open-fan acoustic margins.
🔗 Background analysis: ../../../04_DESIGN/system_design/[**performance_rationale.md**](../../../04_DESIGN/system_design/performance_rationale.md)

---

## Scope & Allocation

* **Primary domains:** A2 (Aerodynamics), P-61 (Open-fan), E2-24 (HVDC), C2-28 (H₂/CO₂), L1-22/27 (Autoflight & Control Laws).
* **Aircraft-level KPI:** Block time and mission fuel at design range.

🔗 Decompositions (examples):

* Propulsor capability → ../../../03_REQUIREMENTS/SR/[**SR-PROP-004.md**](../../../03_REQUIREMENTS/SR/SR-PROP-004.md)
* EMS cruise management → ../../../03_REQUIREMENTS/SR/[**SR-CTRL-007.md**](../../../03_REQUIREMENTS/SR/SR-CTRL-007.md)

---

## Constraints & Interfaces

* Must not violate **noise constraints (CS-36)** in step-climb profiles near M0.78.
* EMS shall maintain FC efficiency ≥ design target and keep CO₂ buffer within cruise limits without thrust oscillations.

🔗 Interface refs: ../../../05_INTERFACES/[**53_data_interfaces.md**](../../../05_INTERFACES/53_data_interfaces.md) · ../../../05_INTERFACES/[**52_electrical_interfaces.md**](../../../05_INTERFACES/52_electrical_interfaces.md)

---

## Assumptions

* Clean configuration (no external stores), anti-ice OFF, cabin pressurization nominal.
* Turbogenerator (SAF) **OFF** in zero-emission cruise.
* Open-fan propulsors within validated aeroacoustic envelope for the specified Mach/Re.

🔗 Config evidence: ../../../06_ENGINEERING/analyses/structural/[**mass_properties_baseline.md**](../../../06_ENGINEERING/analyses/structural/mass_properties_baseline.md)

---

## Verification (Method & Artefacts)

* **Analysis:** Mission/performance analysis; propulsion-aero coupling; EMS power-split models.

  * 🔗 Plan: ../../../07_V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../../07_V_AND_V/verification/plans/SVCP_verification_plan.md)
* **Simulation (SIL/HIL):** 6-DoF with aero/prop maps; EMS closed-loop.

  * 🔗 Procedures: ../../../07_V_AND_V/verification/procedures/[**74_test_procedures.md**](../../../07_V_AND_V/verification/procedures/74_test_procedures.md)
* **Ground Test:** Propulsor rig maps → installation corrections.
* **Flight Test:** Demonstration at FL350; performance carding per test plan.

  * 🔗 Results bucket: ../../../07_V_AND_V/verification/results/[**cruise_performance_revA/**](../../../07_V_AND_V/verification/results/cruise_performance_revA/)

**Acceptance evidence:** model-to-flight correlation ≤ **3%** delta in drag and power.
🔗 Coverage: ../../../07_V_AND_V/coverage/[**code_coverage.md**](../../../07_V_AND_V/coverage/7J_code_coverage.csv) · ../../../07_V_AND_V/traceability/[**req_to_test_trace.csv**](../../../07_V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References

* **Certification basis:** ../../../10_CERTIFICATION/ALR/[**ALR-001.md**](../../../10_CERTIFICATION/ALR/ALR-001.md)
* **Safety allocation:** ../../../02_SAFETY/FHA/[**FHA_report.md**](../../../02_SAFETY/FHA/FHA_report.md) → ../../../02_SAFETY/PSSA/[**PSSA_report.md**](../../../02_SAFETY/PSSA/PSSA_report.md) → ../../../02_SAFETY/SSA/[**SSA_report.md**](../../../02_SAFETY/SSA/SSA_report.md)
* **Standards mapping:** ../../../10_CERTIFICATION/[**CS25_mapping.md**](../../../10_CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability

* **Parent ALR:** ../../../10_CERTIFICATION/ALR/[**ALR-001.md**](../../../10_CERTIFICATION/ALR/ALR-001.md)
* **Linked SRs:** ../../../03_REQUIREMENTS/SR/[**SR-PROP-004.md**](../../../03_REQUIREMENTS/SR/SR-PROP-004.md) · ../../../03_REQUIREMENTS/SR/[**SR-CTRL-007.md**](../../../03_REQUIREMENTS/SR/SR-CTRL-007.md)
* **V&V Cross-refs:** ../../../07_V_AND_V/cases/[**TEST-ENER-001**](../../../07_V_AND_V/cases/TEST-ENER-001.md) · ../../../07_V_AND_V/cases/[**TEST-SIM-CRZ-001**](../../../07_V_AND_V/cases/TEST-SIM-CRZ-001.md) · ../../../07_V_AND_V/cases/[**TEST-FT-CRZ-078**](../../../07_V_AND_V/cases/TEST-FT-CRZ-078.md)
* **RTM rows:** ../../../03_REQUIREMENTS/RTM/[**RTM-CRZ-001.csv**](../../../03_REQUIREMENTS/RTM/RTM-CRZ-001.csv) · ../../../03_REQUIREMENTS/RTM/[**RTM-CRZ-002.csv**](../../../03_REQUIREMENTS/RTM/RTM-CRZ-002.csv) · ../../../03_REQUIREMENTS/RTM/[**RTM-CRZ-003.csv**](../../../03_REQUIREMENTS/RTM/RTM-CRZ-003.csv)

---

## Notes

If the final certified cruise level differs (e.g., FL330/FL370), this requirement shall be re-verified with identical criteria and updated atmospheric and Reynolds corrections.

---




