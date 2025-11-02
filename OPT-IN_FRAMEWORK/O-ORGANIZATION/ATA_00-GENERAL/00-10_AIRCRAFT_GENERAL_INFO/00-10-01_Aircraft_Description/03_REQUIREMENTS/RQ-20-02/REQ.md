# RQ-20-02 — Ground Refueling Safety (ISO 19880-1 Compliance)

## Statement
The aircraft's **liquid hydrogen (LH₂) refueling system** shall comply with **ISO 19880-1** (Gaseous hydrogen fueling stations) and applicable cryogenic safety standards to ensure safe, reliable, and efficient ground refueling operations while minimizing risks of fire, explosion, or cryogenic injury.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Refueling System Design and Standards Compliance**  
   - LH₂ refueling interface compliant with **ISO 19880-1** (fueling protocols, connector standards, safety interlocks).  
   - Cryogenic handling per **ISO 21013** (cryogenic vessels) and **EN 1473** (LNG/LH₂ installations).  
   - Refueling connector: **standardized LH₂ coupling** (SAE or ISO emerging standard) with automatic shutoff and leak detection.  
   - Grounding and bonding per **NFPA 2** (Hydrogen Technologies Code) to prevent static discharge ignition.

2. **Safety Interlocks and Automated Protection**  
   - **Pre-refueling checks:** Automated verification of aircraft electrical systems OFF, no ignition sources, tank pressure within limits.  
   - **Flow control:** Refueling rate limited to **≤ 500 kg/h** to manage boil-off and thermal stress.  
   - **Emergency shutoff:** Automatic refueling termination within **≤ 2 seconds** upon leak detection, overpressure, or manual emergency stop.  
   - **Leak detection:** Hydrogen sensors (≤ 25% LEL) at refueling interface and tank vents with audible/visual alarms per **NFPA 2**.  
   - **Pressure relief:** Tank pressure relief valves set to **< 110%** of maximum working pressure (MAWP).

3. **Cryogenic Safety**  
   - **Personnel protection:** Refueling procedures require cryogenic-rated PPE (gloves, face shields, insulated clothing).  
   - **Cold burn prevention:** Transfer lines and couplings insulated to prevent accidental contact with -253°C surfaces.  
   - **Venting control:** Boil-off during refueling safely vented to atmosphere via elevated discharge per **ISO 19880-1** (≥ 5 m above ground, ≥ 3 m from structures).  
   - **Spill containment:** Refueling area designed for rapid LH₂ evaporation; no pooling in low-lying areas (hydrogen buoyancy ensures rapid dispersion).

4. **Fire and Explosion Prevention**  
   - **Exclusion zones:** No ignition sources within **≥ 10 m** of refueling interface during operations per **NFPA 2**.  
   - **Ventilation:** Refueling conducted in **open-air or well-ventilated** areas to prevent hydrogen accumulation (LEL = 4% in air).  
   - **Fire suppression:** Portable water spray systems available for cooling (H₂ fires: non-luminous, extinguish by fuel isolation, not by direct suppression).  
   - **Lightning protection:** Aircraft and refueling equipment bonded and grounded per **SAE ARP5416** (lightning protection).

5. **Operational Procedures and Training**  
   - **Ground crew certification:** Refueling personnel trained and certified in LH₂ handling per **ISO 19880-1** and company safety protocols.  
   - **Refueling checklists:** Standardized procedures per **ATA 12** (Servicing) with safety verification steps.  
   - **Emergency response:** Refueling locations equipped with H₂ fire/leak emergency plans, including evacuation procedures and firefighting resources.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-REFU-001**](../../V_AND_V/cases/TEST-REFU-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-REFU-GT-001**](../../V_AND_V/cases/TEST-REFU-GT-001.md)  
- Operational validation: ../../V_AND_V/cases/[**TEST-REFU-OPS-001**](../../V_AND_V/cases/TEST-REFU-OPS-001.md)

---

## Rationale
Safe LH₂ refueling is critical to operational acceptance and public confidence in hydrogen aviation. ISO 19880-1 compliance ensures interoperability with emerging hydrogen infrastructure and adherence to international safety best practices. Automated safety interlocks minimize human error risks.

🔗 Safety rationale: ../../DESIGN/system_design/[**H2_infrastructure_safety.md**](../../DESIGN/system_design/H2_infrastructure_safety.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **C2-28** Fuel Systems (LH₂ tanks, refueling interface per **ATA 28-10**)  
  - **I-03** Ground Support Equipment (LH₂ refueling trucks, dispensers, safety equipment)  
  - **O-02** Operations Information (refueling procedures, safety protocols per **ATA 12**)  
  - **E1-26** Fire Protection (fire detection, suppression systems)  
  - **I-85** Infrastructure Interface Standards (H₂ refueling station compatibility)

- **Key interfaces:**  
  - Aircraft LH₂ tank → Refueling interface connector  
  - Refueling system → Ground H₂ storage and dispensing equipment  
  - Safety interlocks → Aircraft electrical system (power-off verification)  
  - Leak detection sensors → Ground crew alert systems

🔗 Decompositions:  
- Refueling interface design → ../SR/[**SR-REFU-001.md**](../SR/SR-REFU-001.md)  
- Safety interlock logic → ../SR/[**SR-SAFE-INT-001.md**](../SR/SR-SAFE-INT-001.md)  
- Ground procedures → ../../OPERATIONS_AND_MAINTENANCE/procedures/[**H2_refueling_SOP.md**](../../OPERATIONS_AND_MAINTENANCE/procedures/H2_refueling_SOP.md)

---

## Constraints & Interfaces
- **Refueling time:** Target refueling time **≤ 30 minutes** for full LH₂ load (≈4,000 kg) to match operational turnaround requirements.  
- **Infrastructure dependency:** LH₂ refueling infrastructure availability varies by airport; operational planning must account for H₂ network coverage.  
- **Regulatory approval:** Airport authorities and fire marshals must approve H₂ refueling operations per local regulations and **ICAO Annex 14** (Aerodromes).  
- **Environmental conditions:** Refueling operations restricted during **thunderstorms** or when **wind speed > 15 m/s** (dispersion concerns).

🔗 Interface references:  
- Ground equipment: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Safety systems: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)  
- Infrastructure: ../../INTERFACES/[**85_infrastructure_interfaces.md**](../../INTERFACES/85_infrastructure_interfaces.md)

---

## Assumptions
- **ISO 19880-1 applicability:** Standard developed for gaseous H₂ fueling stations; adapted principles apply to LH₂ cryogenic refueling with supplemental cryogenic safety standards.  
- **Ground equipment maturity:** LH₂ refueling trucks and dispensers available at **TRL 7+** (demonstrated in pilot programs, e.g., airport hydrogen hubs).  
- **Regulatory harmonization:** ICAO and national aviation authorities developing harmonized H₂ aircraft refueling standards by aircraft entry into service (EIS).  
- **Emergency response readiness:** Airport fire/rescue services trained in H₂ incident response (specialized training beyond conventional jet fuel).

🔗 Infrastructure readiness: ../../ENGINEERING/analyses/infrastructure/[**H2_infrastructure_assessment.md**](../../ENGINEERING/analyses/infrastructure/H2_infrastructure_assessment.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Hazard analysis (FMEA, FTA) for refueling operations; leak and fire scenario modeling.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Ground Testing:** Refueling system functional tests (connector mating, flow control, emergency shutoff, leak detection); safety interlock validation.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Operational Validation:** Full-scale refueling demonstrations with LH₂ ground equipment; emergency scenario drills (leak detection, emergency shutoff, evacuation).  
  - Results: ../../V_AND_V/verification/results/[**refueling_operational_tests/**](../../V_AND_V/verification/results/refueling_operational_tests/)

- **Certification:** Compliance audit against **ISO 19880-1**, **NFPA 2**, and **EASA Special Condition for Hydrogen Aircraft**.  
  - Compliance: ../../CERTIFICATION/[**H2_refueling_safety_cert.pdf**](../../CERTIFICATION/H2_refueling_safety_cert.pdf)

**Acceptance evidence:** Refueling system meets ISO 19880-1 requirements; safety interlocks functional; emergency shutoff < 2 s; ground crew trained and certified; hazard analysis complete.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-021.md**](../ALR/ALR-021.md) – H₂ ground operations safety  
- **Hydrogen standards:** **ISO 19880-1** (fueling stations), **NFPA 2** (Hydrogen Technologies Code), **SAE ARP8677** (H₂ aircraft systems)  
- **Cryogenic standards:** **ISO 21013** (cryogenic vessels), **EN 1473** (LH₂/LNG installations)  
- **Lightning protection:** **SAE ARP5416** (aircraft lightning protection)  
- **Airport operations:** **ICAO Annex 14** (Aerodromes), **ATA 12** (Servicing)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-021.md**](../ALR/ALR-021.md)  
- **Linked SRs:**  
  - ../SR/[**SR-REFU-001.md**](../SR/SR-REFU-001.md) – Refueling interface design  
  - ../SR/[**SR-SAFE-INT-001.md**](../SR/SR-SAFE-INT-001.md) – Safety interlock logic  
- **Related Requirements:**  
  - **RQ-10-01** (LH₂ primary energy source)  
  - **RQ-20-03** (Boil-off management during refueling)  
  - **RQ-20-06** (Fire suppression systems)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-REFU-001**](../../V_AND_V/cases/TEST-REFU-001.md) · ../../V_AND_V/cases/[**TEST-REFU-GT-001**](../../V_AND_V/cases/TEST-REFU-GT-001.md) · ../../V_AND_V/cases/[**TEST-REFU-OPS-001**](../../V_AND_V/cases/TEST-REFU-OPS-001.md)  
- **RTM rows:** ../RTM/[**RTM-REFU-001.csv**](../RTM/RTM-REFU-001.csv)

---

## Notes
- **Infrastructure transition:** Early operations may require dedicated H₂ refueling at select airports; broader network deployment expected by 2030–2035.  
- **Standardization:** Industry working groups (SAE, ISO, ICAO) developing standardized LH₂ refueling connectors and protocols to ensure global interoperability.  
- **Public perception:** Safe, reliable refueling operations essential for public acceptance and regulatory approval of hydrogen aviation.
