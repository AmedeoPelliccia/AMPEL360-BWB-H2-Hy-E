# RQ-00-02 — Design Range (Zero-Emission Mode)

## Statement
The aircraft shall achieve a **design range ≥ 3,500 km** in **zero-emission flight mode** (hydrogen PEM fuel-cells as the primary source, SAF turbogenerator **OFF** except for contingencies) with the **standard payload** and **mission reserves** as defined in the mission profile, under **ISA conditions** and **nominal configuration**.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
Range demonstration is accepted when the following are **all** satisfied for the **reference mission**:

1. **Mission Profile Definition (baseline)**  
   - Taxi-out, takeoff, climb, **cruise**, descent, approach/landing.  
   - **Reserves & contingencies** per certification/ops basis (alternate + holding + final reserve), documented in [mission_profile.md](../../DESIGN/system_design/mission_profile.md).  
   - **Zero in-flight CO₂** (H₂ mode) throughout planned segments; SAF TG may be **armed but not used** unless contingency criteria are met.

2. **Performance & Energy**  
   - Net mission distance ≥ **3,500 km** (GNSS-equivalent great-circle + procedures) per [range_methodology.md](../../DESIGN/system_design/range_methodology.md).  
   - Energy balance closes with ≥ **5% hydrogen mass margin** at landing (post-reserve).  
   - CO₂ buffer cyclic depth within limits (±SOC bands) per EMS spec [SR-CTRL-007](../SR/SR-CTRL-007.md).  
   - Propulsor efficiency within validated map envelopes per [SR-PROP-004](../SR/SR-PROP-004.md).

3. **Environmental & Handling**  
   - Winds and temperatures per mission envelope in [performance_rationale.md](../../DESIGN/system_design/performance_rationale.md).  
   - Handling qualities and protections nominal (no abnormal law triggers) per autoflight requirements.

4. **Evidence Set**  
   - **Analysis** pack shows mission closure with mass/energy margins.  
   - **Simulation** runs reproduce range ≥ 3,500 km with model-to-analysis delta ≤ **3%**.  
   - **Flight** demo (when applicable) achieves extrapolated or direct evidence matching analysis within tolerance.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-MSN-DR-001**](../../V_AND_V/cases/TEST-MSN-DR-001.md)  
- SIL/HIL: ../../V_AND_V/cases/[**TEST-SIM-DR-002**](../../V_AND_V/cases/TEST-SIM-DR-002.md)  
- Flight: ../../V_AND_V/cases/[**TEST-FT-DR-003**](../../V_AND_V/cases/TEST-FT-DR-003.md)

---

## Rationale
A ≥3,500 km zero-emission design range secures competitive network coverage while maintaining BWB efficiency, hydrogen safety margins, and open-fan acoustic constraints.  
🔗 Background: ../../DESIGN/system_design/[**range_methodology.md**](../../DESIGN/system_design/range_methodology.md)

---

## Scope & Allocation
- **Primary domains:** A2 Aerodynamics, **C2-28** Fuel/H₂/SAF (cryogenic), **E2-24** Electrical/HVDC, **P-61** Open-fan propulsors, **L1-22/27** Autoflight & control.  
- **KPI:** Block energy per seat-km; zero-emission mission completion rate.

🔗 Decompositions:  
- EMS mission energy management → ../SR/[**SR-CTRL-007.md**](../SR/SR-CTRL-007.md)  
- Propulsor efficiency envelope → ../SR/[**SR-PROP-004.md**](../SR/SR-PROP-004.md)

---

## Constraints & Interfaces
- **Noise & community constraints** must remain compliant (CS-36 margins) for departure/arrival procedures implicit in the mission.  
- **Hydrogen handling** (boil-off, venting, pressure) must comply with cryogenic limits in interfaces.  
- **Electrical** isolation and HVDC transients shall not violate bus stability during mission step changes.

🔗 Interface refs:  
- Data bus & EMS: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)  
- Electrical/HVDC: ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- Fuel/cryogenic: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)

---

## Assumptions
- Standard payload per **00-10 aircraft definition** and mass properties in ../../ENGINEERING/analyses/structural/[**mass_properties_baseline.md**](../../ENGINEERING/analyses/structural/mass_properties_baseline.md).  
- ISA atmosphere; anti-ice **OFF** in cruise (unless stated otherwise in mission variant).  
- SAF TG **OFF**; usage triggers contingency branch and is excluded from zero-emission range metric.

---

## Verification (Method & Artefacts)
- **Analysis:** Mission synthesis + energy closure (hydrogen mass flow, EMS split, aero/prop maps).  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)
- **Simulation (SIL/HIL):** 6-DoF with EMS controller-in-the-loop; wind/temp dispersions.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)
- **Flight Test (as applicable):** Range carding and extrapolation with validated correction factors.  
  - Results: ../../V_AND_V/verification/results/[**range_demo_revA/**](../../V_AND_V/verification/results/range_demo_revA/)

**Acceptance evidence:** mission distance ≥3,500 km with all margins met and correlation within tolerance.

🔗 Coverage & Trace:  
- Coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Req↔Test: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-002.md**](../ALR/ALR-002.md)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md) → ../../SAFETY/SSA/[**SSA_report.md**](../../SAFETY/SSA/SSA_report.md)  
- **Standards mapping:** ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-002.md**](../ALR/ALR-002.md)  
- **Linked SRs:** ../SR/[**SR-CTRL-007.md**](../SR/SR-CTRL-007.md) · ../SR/[**SR-PROP-004.md**](../SR/SR-PROP-004.md)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-MSN-DR-001**](../../V_AND_V/cases/TEST-MSN-DR-001.md) · ../../V_AND_V/cases/[**TEST-SIM-DR-002**](../../V_AND_V/cases/TEST-SIM-DR-002.md) · ../../V_AND_V/cases/[**TEST-FT-DR-003**](../../V_AND_V/cases/TEST-FT-DR-003.md)  
- **RTM rows:** ../RTM/[**RTM-DR-001.csv**](../RTM/RTM-DR-001.csv) · ../RTM/[**RTM-DR-002.csv**](../RTM/RTM-DR-002.csv)

---

## Notes
Mission variants (e.g., **hot-and-high**, anti-ice ON, headwind bias) shall be tracked as separate verification scenarios and do not degrade the baseline zero-emission range requirement unless formally re-baselined in [CHANGES.md](./CHANGES.md).
