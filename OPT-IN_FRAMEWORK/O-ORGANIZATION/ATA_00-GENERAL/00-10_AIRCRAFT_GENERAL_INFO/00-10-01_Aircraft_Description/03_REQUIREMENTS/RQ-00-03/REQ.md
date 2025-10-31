# RQ-00-03 — Passenger Capacity and Cabin Configuration

## Statement
The aircraft shall accommodate **up to 220 passengers** in a **single-class high-density configuration** or **170 passengers** in a **two-class layout**, while maintaining compliance with **CS-25 emergency evacuation (≤90 s)** and **cabin environmental standards (CS-25.831)**.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Cabin Layout and Certification Compliance**  
   - Floor area utilization ≤ 85%.  
   - Exit configuration compliant with **CS-25.807** (Type A/B/C exits as applicable).  
   - Evacuation test or validated analysis meets **≤90 s** egress for max occupancy.  
   - Pressurization and ECS flow rates per **CS-25.831**.

2. **Configuration Variants**  
   - Single-class: 220 pax @ 79 cm pitch.  
   - Two-class: 170 pax (18 premium @ 97 cm pitch, 152 economy @ 79 cm).  
   - Cabin flexibility validated per **ATA 25** (Equipment/Furnishings).  

3. **Environmental and Energy Considerations**  
   - Cabin systems powered from hybrid DC bus (E2-24).  
   - ECS load compatible with cryogenic H₂ thermal integration (E1-21).  
   - Emergency lighting per ATA 33, oxygen per ATA 35.

🔗 Linked artefacts:  
- Layout: ../../DESIGN/system_design/[**cabin_layout_overview.md**](../../DESIGN/system_design/cabin_layout_overview.md)  
- Evacuation model: ../../ENGINEERING/analyses/structural/[**evacuation_simulation.md**](../../ENGINEERING/analyses/structural/evacuation_simulation.md)  
- ECS data: ../../ENGINEERING/analyses/thermal/[**ECS_load_balance.md**](../../ENGINEERING/analyses/thermal/ECS_load_balance.md)

---

## Rationale
The BWB internal volume allows for greater usable area and lower pressurization loads; however, cabin egress and comfort must satisfy existing regulatory metrics despite the novel layout.

🔗 Reference studies: ../../DESIGN/system_design/[**BWB_cabin_integration.md**](../../DESIGN/system_design/BWB_cabin_integration.md)

---

## Scope & Allocation
- **Primary domains:**  
  - C1-25 Equipment/Furnishings  
  - E1-21 Air Conditioning/Pressurization  
  - L1-22/27 Control logic (ECS, lighting, emergency)  
  - A2 Aerodynamics (fuselage-cabin coupling)

🔗 System Requirements:  
- ../SR/[**SR-CAB-001.md**](../SR/SR-CAB-001.md) – Cabin layout geometry  
- ../SR/[**SR-ECS-002.md**](../SR/SR-ECS-002.md) – Environmental control  

---

## Constraints & Interfaces
- Cabin layout must interface with **ATA 52 Doors** and **ATA 53 Fuselage** for emergency exits.  
- ECS and power integration validated via **E2-24** electrical and **E1-21** thermal subsystems.  

🔗 Interface refs:  
- ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- Cabin materials are fire-rated per **CS-25.853**.  
- Floor beams and seat tracks per baseline **BWB structural grid**.  
- Airflow model assumes **single ECS loop with regenerative CO₂ system**.

🔗 Supporting analysis: ../../ENGINEERING/analyses/thermal/[**airflow_distribution_model.md**](../../ENGINEERING/analyses/thermal/airflow_distribution_model.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Egress simulation (CFD & crowd dynamics).  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)
- **Simulation:** Virtual evacuation with passenger motion models.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)
- **Physical Test:** Partial mock-up with exit flow validation.  
  - Results: ../../V_AND_V/verification/results/[**cabin_safety_tests/**](../../V_AND_V/verification/results/cabin_safety_tests/)

**Acceptance evidence:** total evacuation time ≤ 90 s; ECS and cabin system loads within design power budget.

🔗 Trace files:  
- Coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Trace matrix: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **CS-25.807** Emergency Exits  
- **CS-25.831** Ventilation & Pressurization  
- **CS-25.853** Flammability  
- **ATA 25**, **ATA 33**, **ATA 35** applicable sections  
- **EASA AMC 25.803** Evacuation Demonstrations  

🔗 Mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-003.md**](../ALR/ALR-003.md)  
- **Linked SRs:** ../SR/[**SR-CAB-001.md**](../SR/SR-CAB-001.md) · ../SR/[**SR-ECS-002.md**](../SR/SR-ECS-002.md)  
- **V&V:** ../../V_AND_V/cases/[**TEST-CAB-EVAC-001**](../../V_AND_V/cases/TEST-CAB-EVAC-001.md)  
- **RTM:** ../RTM/[**RTM-CAB-001.csv**](../RTM/RTM-CAB-001.csv)

---

## Notes
Alternative cabin configurations (cargo or combi variants) are covered under variant-specific requirement sets in `../RQ-00-03A/` and must preserve compliance to evacuation and environmental constraints defined herein.
