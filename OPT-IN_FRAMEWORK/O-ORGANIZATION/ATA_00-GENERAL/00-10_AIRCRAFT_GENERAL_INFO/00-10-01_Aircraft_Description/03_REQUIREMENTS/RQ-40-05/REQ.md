# RQ-40-05 — System Safety (ARP4761 / ARP4754A)

## Statement
Aircraft and system development shall follow **ARP4754A** (Guidelines for Development of Civil Aircraft and Systems) and **ARP4761** (Guidelines and Methods for Conducting the Safety Assessment Process on Civil Airborne Systems and Equipment) to ensure systematic safety assessment and compliance with CS-25.1309 (Equipment, systems, and installations).

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **ARP4754A Development Process**  
   - **Aircraft/System development lifecycle:** Requirements → Design → Implementation → Verification → Certification per ARP4754A.  
   - **Safety assessment integration:** Safety activities integrated throughout development (concurrent engineering).  
   - **Configuration management:** Requirements, design, and verification under configuration control.

2. **ARP4761 Safety Assessment**  
   - **Functional Hazard Assessment (FHA):** Identify functions and associated hazards (catastrophic, hazardous, major, minor, no safety effect).  
   - **Preliminary System Safety Assessment (PSSA):** Allocate failure probability targets, derive safety requirements, propose architecture.  
   - **System Safety Assessment (SSA):** Demonstrate compliance with safety objectives via analysis (FMEA, FTA, CCA) and verification.  
   - **Common Cause Analysis (CCA):** Assess common mode failures, zonal hazards, particular risks.

3. **CS-25.1309 Compliance**  
   - **Failure condition classification:** Catastrophic (≤ 10⁻⁹ per flight hour), Hazardous (≤ 10⁻⁷), Major (≤ 10⁻⁵).  
   - **Single failure tolerance:** Catastrophic failures extremely improbable; hazardous failures remote.  
   - **Warning and protection:** Crew alerted to failures; systems include protection against foreseeable misuse.

4. **Safety Case Documentation**  
   - **System Safety Assessment Report (SSAR):** Comprehensive safety case for aircraft-level and system-level functions.  
   - **FHA/PSSA/SSA reports:** Documented per ARP4761 guidelines.  
   - **Compliance matrix:** CS-25.1309 paragraph-by-paragraph compliance demonstration.

5. **Regulatory Acceptance**  
   - **Authority review:** Safety assessments reviewed and accepted by EASA/FAA during certification.

🔗 Test artefacts:  
- Safety case: ../../SAFETY/[**SSAR_System_Safety_Assessment_Report.pdf**](../../SAFETY/SSAR_System_Safety_Assessment_Report.pdf)

---

## Rationale
ARP4754A and ARP4761 provide industry-standard methodology for systematic safety assessment. Compliance demonstrates safety objectives are met, enabling CS-25.1309 compliance and certification approval.

---

## Scope & Allocation
- **Primary domains:**  
  - **O-02** Safety (FHA, PSSA, SSA per **ATA 02 SAFETY**)  
  - **O-10** Certification (safety case submission)  
  - All systems (safety assessment required for all aircraft functions)

🔗 Decompositions:  
- Safety assessment plan → ../../SAFETY/[**Safety_Assessment_Plan.pdf**](../../SAFETY/Safety_Assessment_Plan.pdf)

---

## Compliance References
- **Certification basis:** **ARP4754A**, **ARP4761**, **CS-25.1309**, **AC 25.1309-1A**

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-044.md**](../ALR-044.md) – System safety  
- **Related:** All requirements (safety assessment traces to all system requirements)

---

## Notes
- **Safety-driven design:** Safety assessment identifies safety requirements that drive system architecture (redundancy, monitoring, protection).
