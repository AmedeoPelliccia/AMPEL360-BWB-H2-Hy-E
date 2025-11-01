# RQ-40-02 — Hydrogen Systems (SC-H2, SAE ARP8677)

## Statement
Hydrogen fuel and energy systems shall comply with **EASA Special Condition for Hydrogen (SC-H2)**, **SAE ARP8677** (Hydrogen Aircraft Installation Standards), and applicable hydrogen safety standards to ensure safe design, installation, operation, and maintenance of LH₂ systems.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **SC-H2 Compliance**  
   - **Special Condition scope:** LH₂ storage, distribution, fuel-cell integration, venting, fire protection, crash safety, ground handling.  
   - **Safety assessment:** Comprehensive safety case per **ARP4761** addressing hydrogen-specific hazards (cryogenic exposure, embrittlement, flammability, asphyxiation).  
   - **Material compatibility:** All materials in contact with LH₂ qualified for cryogenic and hydrogen service (no embrittlement, permeation limits met).

2. **SAE ARP8677 Standards**  
   - **Installation practices:** Hydrogen system installation per **SAE ARP8677** (piping, fittings, seals, sensors, grounding, bonding).  
   - **Leak detection:** Hydrogen leak detection system per ARP8677 (sensor placement, alarm thresholds, response procedures).  
   - **Maintenance procedures:** Hydrogen system maintenance per ARP8677 (purging, leak checking, component replacement, personnel training).

3. **Hydrogen Safety Standards**  
   - **ISO 19880-1:** Fueling station interface and safety interlocks (per **RQ-20-02**).  
   - **ISO 14687:** Hydrogen fuel quality (purity, contaminants).  
   - **NFPA 2:** Hydrogen Technologies Code (fire safety, venting, exclusion zones).  
   - **EN 1473:** LNG/LH₂ installation safety (cryogenic system design).

4. **System-Level Requirements**  
   - **Crash safety:** Hydrogen tanks and piping protected per crashworthiness requirements (survivable accident envelope).  
   - **Fire protection:** Hydrogen fire detection and suppression per **RQ-20-06** and **ATA 26**.  
   - **Venting safety:** Hydrogen venting to atmosphere per safe dispersion criteria (no accumulation in confined spaces).  
   - **Ground operations:** Hydrogen ground handling procedures and equipment per **ISO 19880-1** and airport safety requirements.

5. **Certification and Approval**  
   - **Authority acceptance:** EASA and FAA accept hydrogen system design via Special Condition compliance demonstration.  
   - **Test validation:** Hydrogen system safety validated via ground tests (leak, fire, crash, fueling), component tests, and analysis.

🔗 Test artefacts:  
- Hydrogen safety case: ../../CERTIFICATION/[**H2_Safety_Case.pdf**](../../CERTIFICATION/H2_Safety_Case.pdf)  
- Compliance evidence: ../../CERTIFICATION/[**SC-H2_compliance_matrix.csv**](../../CERTIFICATION/SC-H2_compliance_matrix.csv)

---

## Rationale
Hydrogen propulsion is novel for commercial aviation; SC-H2 and ARP8677 provide regulatory framework and industry best practices. Compliance ensures hydrogen hazards are mitigated to acceptable levels, enabling safe operations and regulatory approval.

🔗 Hydrogen certification strategy: ../../CERTIFICATION/[**hydrogen_certification_approach.md**](../../CERTIFICATION/hydrogen_certification_approach.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **C2-28** Fuel Systems (LH₂ storage, distribution)  
  - **E2-24** Electrical Power (fuel-cell energy systems)  
  - **E1-26** Fire Protection (hydrogen fire safety)  
  - **O-10** Certification (SC-H2 compliance demonstration)

🔗 Decompositions:  
- SC-H2 compliance plan → ../../CERTIFICATION/[**SC-H2_compliance_plan.md**](../../CERTIFICATION/SC-H2_compliance_plan.md)

---

## Compliance References
- **Certification basis:** **EASA SC-H2** (Special Condition for Hydrogen), **SAE ARP8677** (Hydrogen Aircraft Installation Standards)  
- **Hydrogen standards:** **ISO 19880-1** (fueling), **ISO 14687** (fuel quality), **NFPA 2** (fire safety), **EN 1473** (cryogenic safety)  
- **Related requirements:** **RQ-10-01** (H₂ fuel system), **RQ-20-02** (refueling safety), **RQ-20-03** (boil-off), **RQ-20-06** (fire suppression)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-041.md**](../ALR-041.md) – Hydrogen systems certification  
- **V&V Cross-refs:** Hydrogen system tests (**TEST-FC-001**, **TEST-REFU-001**, **TEST-CRYO-001**)

---

## Notes
- **Regulatory evolution:** SC-H2 framework evolving as hydrogen aviation matures; aircraft design anticipates compliance with emerging regulations.  
- **Industry collaboration:** SAE and EASA working groups (G-40 Hydrogen Aircraft) developing standards; program actively participates to influence and adopt best practices.
