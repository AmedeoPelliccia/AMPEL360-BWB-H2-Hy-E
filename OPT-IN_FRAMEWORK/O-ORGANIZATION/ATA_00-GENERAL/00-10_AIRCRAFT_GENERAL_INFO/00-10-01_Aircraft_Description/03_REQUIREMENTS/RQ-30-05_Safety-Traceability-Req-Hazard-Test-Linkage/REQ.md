# RQ-30-05 — Safety Traceability (Req → Hazard → Test Linkage)

## Statement
Complete bidirectional traceability shall be maintained between **requirements**, **hazards**, and **verification tests** throughout the development lifecycle per **ARP4754A** trace tree methodology, ensuring regulatory compliance and safety case completeness.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Requirements Traceability**  
   - **Forward traceability:** Every requirement (aircraft, system, component level) traces forward to verification method (analysis, test, inspection, demonstration).  
   - **Backward traceability:** Every verification artifact traces back to parent requirement(s).  
   - **Coverage:** ≥ **100% traceability** for safety-critical requirements (DAL A/B per DO-178C/DO-254).

2. **Hazard Linkage**  
   - **FHA/PSSA/SSA integration:** Hazards identified in Functional Hazard Assessment (FHA), Preliminary System Safety Assessment (PSSA), and System Safety Assessment (SSA) linked to related requirements.  
   - **Safety requirements derivation:** Safety requirements (failure conditions, probability targets, detection/mitigation) derived from hazard analysis and traceable to verification.  
   - **FMEA/FTA integration:** Failure modes (FMEA) and fault trees (FTA) linked to requirements and hazards.

3. **Test Linkage**  
   - **Test case traceability:** Every test case (unit, integration, system, flight test) traceable to requirements and hazards addressed.  
   - **Test coverage metrics:** Automated coverage analysis shows **100% requirement coverage** by verification activities.  
   - **Regression testing:** Traceability enables automated regression test selection when requirements change (test only affected areas).

4. **Tool Support and Automation**  
   - **Requirements management tool:** DOORS, Polarion, or equivalent tool captures traceability links.  
   - **Automated trace matrix generation:** Requirements Traceability Matrix (RTM) and Hazard Traceability Matrix (HTM) auto-generated from tool database.  
   - **Real-time compliance monitoring:** Dashboard displays traceability gaps, orphaned requirements, untested hazards.

5. **Regulatory Audit Readiness**  
   - **Certification evidence:** Traceability matrices and supporting evidence (test reports, analysis results) package for regulatory submission.  
   - **Continuous compliance:** Traceability maintained throughout in-service phase (service bulletins, modifications trace back to safety assessment updates).

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-TRACE-001**](../../V_AND_V/cases/TEST-TRACE-001.md)  
- Audit validation: ../../V_AND_V/cases/[**TEST-TRACE-AUDIT-001**](../../V_AND_V/cases/TEST-TRACE-AUDIT-001.md)

---

## Rationale
Regulatory safety case requires demonstrating that all hazards are identified, mitigated, and verified. Traceability provides evidence chain from requirements through safety analysis to verification, essential for **ARP4754A** and **ARP4761** compliance and certification approval.

🔗 Safety methodology: ../../04_DESIGN/system_design/[**safety_traceability_framework.md**](../../04_DESIGN/system_design/safety_traceability_framework.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **O-02** Safety (safety assessments per **ATA 02 SAFETY**)  
  - **O-03** Requirements (requirements management per **ATA 03 REQUIREMENTS**)  
  - **O-07** V&V (verification traceability per **ATA 07 V_AND_V**)  
  - **O-10** Certification (regulatory compliance evidence)

🔗 Decompositions:  
- Traceability data model → ../SR/[**SR-TRACE-MODEL-001.md**](../SR/SR-TRACE-MODEL-001.md)  
- Automated trace generation → ../SR/[**SR-TRACE-AUTO-001.md**](../SR/SR-TRACE-AUTO-001.md)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-034.md**](../ALR-034.md) – Safety traceability  
- **Safety standards:** **ARP4754A** (development of civil aircraft and systems), **ARP4761** (safety assessment process)  
- **Software/hardware:** **DO-178C** (software traceability), **DO-254** (hardware traceability)  
- **System engineering:** **ISO/IEC 15288** (systems life cycle processes — traceability requirements)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-034.md**](../ALR-034.md)  
- **Linked SRs:** ../SR/[**SR-TRACE-MODEL-001.md**](../SR/SR-TRACE-MODEL-001.md), ../SR/[**SR-TRACE-AUTO-001.md**](../SR/SR-TRACE-AUTO-001.md)  
- **Related Requirements:** **RQ-30-01** (Digital twin), **RQ-30-02** (DPP configuration traceability)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-TRACE-001**](../../V_AND_V/cases/TEST-TRACE-001.md)

---

## Notes
- **Best practice:** Traceability is foundational to systems engineering and safety management; requirement applies across all domains (not just safety-critical).  
- **Tool investment:** Modern requirements management tools (DOORS Next, Jama, Polarion) provide robust traceability features; initial setup effort pays dividends throughout lifecycle.
