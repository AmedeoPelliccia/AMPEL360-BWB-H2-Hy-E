# RQ-00-05 — Structural Load Efficiency and Weight Targets

## Statement
The aircraft shall achieve a **structural efficiency ≥ 42%** (ratio of structural mass to MTOW) and a **maximum takeoff weight (MTOW) ≤ 120,000 kg**, maintaining compliance with **CS-25 Subpart C** (Structure) and **Subpart D** (Design Loads).  
The blended-wing-body (BWB) primary structure shall be designed to meet all **limit and ultimate load factors** with appropriate **fail-safe and damage tolerance** margins.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Mass Targets**  
   - **MTOW ≤ 120,000 kg** (certifiable configuration).  
   - **Operating Empty Weight (OEW) ≤ 64,000 kg.**  
   - **Payload ≥ 22,000 kg.**  
   - **Hydrogen fuel mass ≤ 16,000 kg.**  
   - Compliance verified via digital mass properties baseline and configuration audits.

2. **Structural Efficiency Metrics**  
   - Structural efficiency ≥ 42% = (Lift @ 1g cruise) / (Structural mass × g).  
   - Specific structural weight ≤ 0.26 kg/N at design limit load.  
   - Ultimate load factor = 1.5 × limit load per CS-25.303.

3. **Load Compliance**  
   - **Bending**, **torsion**, and **shear** distributions verified by FEM.  
   - Wing-root bending moment and fuselage bending continuity validated.  
   - Pressure vessel and tank integration conform to CS-25.365 and SC-H₂.  

🔗 Artefacts:  
- Mass baseline: ../../ENGINEERING/analyses/structural/[**mass_properties_baseline.md**](../../ENGINEERING/analyses/structural/mass_properties_baseline.md)  
- FEM model: ../../ENGINEERING/simulations/[**FEA_models/structural_baseline/**](../../ENGINEERING/simulations/FEA_models/structural_baseline/)  
- Load envelopes: ../../DESIGN/system_design/[**load_envelope_overview.md**](../../DESIGN/system_design/load_envelope_overview.md)

---

## Rationale
High structural efficiency is fundamental to offset the additional weight of hybrid-electric systems and cryogenic tanks.  
BWB architecture enables distributed load paths and reduced bending moments compared to tube-and-wing, allowing thinner skins and integrated spars.  
🔗 Concept reference: ../../DESIGN/system_design/[**BWB_primary_structure_concept.md**](../../DESIGN/system_design/BWB_primary_structure_concept.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **A-AIRFRAME (ATA 51–57)**  
  - **C2-28** (Fuel tank structural integration)  
  - **E1-21** (Pressure and thermal interfaces)  
  - **E2-24** (Electrical structure bonding)  
- **Subsystems involved:**  
  - Wings (ATA 57), Fuselage (ATA 53), Stabilizers (ATA 55), Nacelles/Pylons (ATA 54).  

🔗 Decompositions:  
- Wing load distribution → ../SR/[**SR-STR-001.md**](../SR/SR-STR-001.md)  
- Pressurized module strength → ../SR/[**SR-STR-002.md**](../SR/SR-STR-002.md)

---

## Constraints & Interfaces
- Hydrogen tanks structurally integrated into center body per **SC-H₂** and **CS-25.963**.  
- Mounting loads from open-fan pylons per **ATA 54/71**.  
- Cryogenic support brackets analyzed under composite stress rules (MIL-HDBK-17).

🔗 Interface refs:  
- ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- Structural materials: carbon fiber composite (70%), Ti-6Al-4V (10%), Al-Li alloy (10%), others (10%).  
- Factor of safety = 1.5 (ultimate) per CS-25.303.  
- Fatigue life ≥ 60,000 flight cycles.  
- Environmental conditions per **DO-160G** Section 8 (temperature) and Section 13 (vibration).

🔗 Material specs: ../../DESIGN/specifications/[**material_spec.md**](../../DESIGN/specifications/material_spec.md)

---

## Verification (Method & Artefacts)
- **Analysis:** FEM validation, mass correlation, and margin-of-safety calculations.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)
- **Simulation:** Dynamic loads and crashworthiness analysis.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)
- **Testing:**  
  - Static and fatigue tests on scaled test articles and structural rigs.  
  - Results: ../../V_AND_V/verification/results/[**structural_tests_revA/**](../../V_AND_V/verification/results/structural_tests_revA/)

Acceptance when all load cases satisfy limit and ultimate load compliance and mass targets within ±2%.

🔗 Trace & Coverage:  
- ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification Basis:** ../ALR/[**ALR-005.md**](../ALR/ALR-005.md)  
- **Standards:**  
  - CS-25.303 Strength and Deformation  
  - CS-25.305 Strength and Deformation Tests  
  - CS-25.307 Proof of Structure  
  - CS-25.365 Pressurized Compartment Loads  
  - **ARP4754A**, **MIL-HDBK-5J**, **SC-H₂ Fuel Storage Systems**

🔗 Mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-005.md**](../ALR/ALR-005.md)  
- **Linked SRs:** ../SR/[**SR-STR-001.md**](../SR/SR-STR-001.md) · ../SR/[**SR-STR-002.md**](../SR/SR-STR-002.md)  
- **V&V Cross-Refs:** ../../V_AND_V/cases/[**TEST-STR-001**](../../V_AND_V/cases/TEST-STR-001.md) · ../../V_AND_V/cases/[**TEST-FEM-002**](../../V_AND_V/cases/TEST-FEM-002.md)  
- **RTM:** ../RTM/[**RTM-STR-001.csv**](../RTM/RTM-STR-001.csv)

---

## Notes
Structural efficiency targets may be refined following integrated fuel-tank load tests.  
Updates to MTOW must preserve the 42% ratio and maintain fatigue life criteria per **EASA Part 25** requirements.
