# RQ-40-03 — Software (DO-178C Level A)

## Statement
All safety-critical aircraft software shall be developed and verified in compliance with **DO-178C Level A** (Software Considerations in Airborne Systems and Equipment Certification) for functions whose failure would result in catastrophic consequences.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Development Assurance Level (DAL) Assignment**  
   - **Level A (catastrophic):** Flight control laws, EMS critical functions, fuel-cell control, HALT logic, isolation monitoring.  
   - **Level B (hazardous):** Navigation, autoflight, engine indication, battery management.  
   - **Level C/D (major/minor):** Cabin systems, passenger information, non-critical monitoring.  
   - **DAL determination:** Per **ARP4754A** safety assessment (FHA/PSSA/SSA) and **ARP4761** hazard analysis.

2. **DO-178C Process Compliance**  
   - **Planning:** Software Planning Process, Software Development Plan (SDP), Software Verification Plan (SVP), Software Configuration Management Plan (SCMP), Software Quality Assurance Plan (SQAP).  
   - **Development:** Requirements → Design → Code implementation with full traceability per **RQ-30-05**.  
   - **Verification:** Reviews, analysis, testing per SVP; structural coverage analysis (MC/DC for Level A).  
   - **Configuration management:** Version control, change control, problem reporting per SCMP.  
   - **Quality assurance:** Independent QA audits per SQAP; SOI (Software Overview of Compliance) produced.

3. **Level A Verification Objectives**  
   - **Requirements-based testing:** All high-level and low-level requirements verified by test cases.  
   - **Structural coverage (MC/DC):** Modified Condition/Decision Coverage achieved for all Level A code.  
   - **Code reviews:** Source code reviewed against coding standards and low-level requirements.  
   - **Traceability:** Bidirectional traceability from requirements → design → code → tests.

4. **Tool Qualification**  
   - **Development tools:** Compilers, linkers, code generators qualified per **DO-178C Tool Qualification** (or tool output verified).  
   - **Verification tools:** Test harnesses, coverage analyzers, static analysis tools qualified as applicable.

5. **Certification Data Package**  
   - **Software Accomplishment Summary (SAS):** Summary of DO-178C compliance for certification authorities.  
   - **Software Configuration Index (SCI):** Inventory of all software deliverables (executables, source, documentation).  
   - **Certification liaison:** SOI and compliance evidence reviewed and accepted by EASA/FAA.

🔗 Test artefacts:  
- DO-178C compliance evidence: ../../V_AND_V/certification/[**DO178C_compliance/**](../../V_AND_V/certification/DO178C_compliance/)

---

## Rationale
DO-178C is the industry standard for aircraft software development assurance. Level A compliance for catastrophic functions ensures rigorous development and verification, minimizing software-related safety risks and enabling certification approval.

🔗 Software development process: ../../ENGINEERING/[**software_development_plan.md**](../../ENGINEERING/software_development_plan.md)

---

## Scope & Allocation
- **Level A software:**  
  - **L1-22/27** Flight Control Laws, EMS (fuel-cell, battery, propulsor power management)  
  - **E1-26** HALT logic (autonomous fire suppression)  
  - **E2-24** Isolation monitoring, HVDC protection logic

🔗 Decompositions:  
- Software architecture → ../../ENGINEERING/software/[**software_architecture.md**](../../ENGINEERING/software/software_architecture.md)

---

## Compliance References
- **Certification basis:** **DO-178C** (Level A for catastrophic functions), **ARP4754A** (DAL determination)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-042.md**](../ALR-042.md) – Software certification

---

## Notes
- **DO-178C vs. DO-178B:** DO-178C incorporates model-based development, object-oriented programming, and formal methods (supplements DO-331, DO-332, DO-333).
