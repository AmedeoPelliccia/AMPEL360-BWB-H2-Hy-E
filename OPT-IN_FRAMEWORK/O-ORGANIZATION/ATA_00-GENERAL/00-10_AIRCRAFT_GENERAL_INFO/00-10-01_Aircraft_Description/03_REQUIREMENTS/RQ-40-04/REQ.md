# RQ-40-04 — Hardware (DO-254 Level A)

## Statement
All safety-critical electronic hardware shall be developed and verified in compliance with **DO-254 Level A** (Design Assurance Guidance for Airborne Electronic Hardware) for functions whose failure would result in catastrophic consequences.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Design Assurance Level (DAL) Assignment**  
   - **Level A:** HVDC power electronics, isolation monitoring hardware, fuel-cell controllers, battery management electronics, motor controllers.  
   - **DAL determination:** Per ARP4754A safety assessment and ARP4761 hazard analysis.

2. **DO-254 Process Compliance**  
   - **Planning:** Hardware Design Plan (HDP), Hardware Verification Plan (HVP), Hardware Configuration Management Plan (HCMP), Hardware Quality Assurance Plan (HQAP).  
   - **Requirements:** Hardware requirements captured and traceable.  
   - **Design:** Conceptual, detailed design with analysis (thermal, EMI, reliability).  
   - **Implementation:** Component selection, PCB layout, FPGA/ASIC development.  
   - **Verification:** Inspection, analysis, testing per HVP; requirements-based and structural coverage.  
   - **Configuration management:** Version control, change control per HCMP.

3. **Level A Verification**  
   - **Requirements-based testing:** All hardware requirements verified.  
   - **Environmental testing:** DO-160G qualification (temperature, vibration, EMI, lightning, HIRF).  
   - **FPGA/ASIC verification:** If applicable, gate-level simulation, formal verification, structural coverage.

4. **Certification Data Package**  
   - **Hardware Accomplishment Summary (HAS):** Summary of DO-254 compliance.  
   - **Hardware Configuration Index (HCI):** Inventory of hardware deliverables.

🔗 Test artefacts:  
- DO-254 compliance: ../../V_AND_V/certification/[**DO254_compliance/**](../../V_AND_V/certification/DO254_compliance/)

---

## Rationale
DO-254 ensures rigorous electronic hardware development for safety-critical functions, minimizing hardware-related safety risks.

---

## Scope & Allocation
- **Level A hardware:**  
  - **E2-24** HVDC electronics, isolation monitoring  
  - **E3-39** Power electronics (motor controllers, converters)  
  - **C2-28** Fuel-cell and battery controllers

🔗 Decompositions:  
- Hardware architecture → ../../ENGINEERING/hardware/[**hardware_architecture.md**](../../ENGINEERING/hardware/hardware_architecture.md)

---

## Compliance References
- **Certification basis:** **DO-254 Level A**, **ARP4754A** (DAL determination)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-043.md**](../ALR-043.md) – Hardware certification

---

## Notes
- **Complex electronic hardware:** FPGA/ASIC development requires additional rigor (structural coverage, formal methods).
