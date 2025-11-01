# RQ-40-01 — Certification Basis (EASA CS-25 / FAA Part 25)

## Statement
The aircraft shall be certified under **EASA CS-25** (Large Aeroplanes) and **FAA Part 25** (Airworthiness Standards: Transport Category Airplanes) as the primary certification basis, with Special Conditions and Equivalent Level of Safety (ELOS) findings as required for novel technologies.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Type Certification Basis**  
   - **Regulatory framework:** EASA CS-25 Amendment 27 (or later) and FAA Part 25 Amendment 140 (or later) as applicable at program start.  
   - **Concurrent certification:** Pursue EASA and FAA Type Certificates simultaneously (harmonized certification approach where possible).  
   - **Certification schedule:** Type Certificate achieved within **[X] years** of program launch; Entry Into Service (EIS) within **[Y] years**.

2. **Special Conditions (Novel Technologies)**  
   - **Hydrogen propulsion:** Special Condition for hydrogen fuel system safety (cryogenic storage, fuel-cell operation, hydrogen venting) per **EASA SC-H2** framework.  
   - **Electric propulsion:** Special Condition for high-voltage electrical systems (HVDC distribution, isolation monitoring, motor-driven propulsors) per emerging standards.  
   - **Blended-wing-body:** Special Conditions for BWB airframe (structural certification, ditching, emergency evacuation) as required.  
   - **Autonomous systems:** If applicable, Special Conditions for advanced automation/autonomy features (EMS, flight controls).

3. **Equivalent Level of Safety (ELOS) Findings**  
   - **Novel design features:** Where compliance with existing regulations impractical (e.g., BWB cabin layout vs. tube-and-wing evacuation standards), demonstrate Equivalent Level of Safety via analysis, testing, or operational procedures.  
   - **ELOS documentation:** Comprehensive safety case for each ELOS finding, including hazard analysis, risk mitigation, and compensating measures.

4. **Compliance Verification**  
   - **Compliance matrix:** Detailed compliance matrix mapping each CS-25/Part 25 paragraph to verification method (analysis, test, inspection, demonstration, similarity).  
   - **Certification plan:** Type Certification Plan (TCP) defining certification strategy, milestones, deliverables, and authority engagement.  
   - **Authority coordination:** Regular engagement with EASA and FAA (Issue Papers, certification meetings, test witnessing) throughout development.

5. **Regulatory Acceptance**  
   - **Type Certificate issuance:** EASA and FAA Type Certificates issued confirming compliance with certification basis.  
   - **Production certification:** Production Organization Approval (POA) / Production Certificate (PC) for manufacturing.  
   - **Operational approval:** Aircraft eligible for commercial air transport operations under applicable operating regulations (EASA Part-CAT, FAA Part 121/135).

🔗 Test artefacts:  
- Certification plan: ../../CERTIFICATION/[**Type_Certification_Plan.pdf**](../../CERTIFICATION/Type_Certification_Plan.pdf)  
- Compliance matrix: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Rationale
CS-25 and Part 25 are established certification standards for transport category aircraft, ensuring airworthiness and safety. Novel technologies (H₂, electric propulsion, BWB) require Special Conditions and ELOS findings to adapt regulations to innovative design, while maintaining equivalent safety levels.

🔗 Certification strategy: ../../CERTIFICATION/[**certification_strategy_overview.md**](../../CERTIFICATION/certification_strategy_overview.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **O-10** Certification (all **ATA 10 CERTIFICATION** activities)  
  - **O-02** Safety (safety assessments supporting certification)  
  - **O-07** V&V (verification evidence for compliance demonstration)  
  - **O-00** General (program management, authority coordination)

🔗 Decompositions:  
- Certification plan → ../../CERTIFICATION/[**Type_Certification_Plan.pdf**](../../CERTIFICATION/Type_Certification_Plan.pdf)  
- Special Conditions → ../../CERTIFICATION/[**Special_Conditions/**](../../CERTIFICATION/Special_Conditions/)

---

## Compliance References
- **Certification basis:** CS-25, FAA Part 25 (primary), Special Conditions (H₂, electric, BWB)  
- **Guidance:** **AC 20-174** (Development of Civil Aircraft and Systems), **AMC-25** (Acceptable Means of Compliance)  
- **Processes:** **Part 21** (Certification Procedures for Aircraft and Related Products), **FAA Order 8110.4** (Type Certification)

🔗 Regulatory framework: ../../CERTIFICATION/[**regulatory_framework.md**](../../CERTIFICATION/regulatory_framework.md)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-040.md**](../ALR-040.md) – Master certification requirement  
- **Related Requirements:** **RQ-40-02** through **RQ-40-06** (domain-specific certification compliance)  
- **Certification deliverables:** ../../CERTIFICATION/ (all certification documentation)

---

## Notes
- **Regulatory coordination:** Early and continuous engagement with EASA and FAA essential for novel technologies to align certification approach and avoid late-stage surprises.  
- **International recognition:** EASA and FAA Type Certificates facilitate global market access via bilateral agreements and third-country validations.
