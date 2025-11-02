# RQ-20-01 — In-Flight CO₂ Emissions (0 g/km in H₂ Mode)

## Statement
The aircraft shall achieve **zero direct CO₂ emissions (0 g/km)** during flight operations when operating in **hydrogen-only mode** (primary PEM fuel-cell system active, SAF turbogenerator OFF), contributing to the aircraft's zero-emission sustainability framework.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Zero Carbon Emissions Verification**  
   - **In-flight emissions:** 0 g CO₂/km validated via fuel composition analysis and stoichiometric calculation.  
   - **Primary energy source:** LH₂ combustion produces only H₂O (water vapor); no carbon-containing byproducts.  
   - **CO₂ battery loop:** Closed-loop CO₂ system does not vent CO₂ to atmosphere during normal operations per **RQ-10-02**.  
   - **SAF turbogenerator status:** **OFF** during zero-emission flight segments (H₂-only mode).

2. **Operational Mode Definition**  
   - **Mode 1 (Zero-emission/H₂-primary):** Fuel-cell stacks provide **100%** of propulsive and non-propulsive power; SAF turbogenerator OFF or standby; **0 g CO₂/km**.  
   - **Mode 2 (Hybrid):** SAF turbogenerator supplements power during high-demand or contingency; CO₂ emissions calculated per ICAO CORSIA methodology; **not zero-emission mode**.  
   - **Mission profile:** Aircraft designed for **≥ 90%** of flight time in **Mode 1 (zero-emission)** for design range missions.

3. **Emissions Monitoring and Reporting**  
   - Onboard data logging captures fuel source selection (H₂ vs. SAF) and power output per **ATA 31** (Indicating/Recording Systems).  
   - Post-flight emissions reporting per **ICAO Annex 16 Vol III** (CO₂ certification) and **CORSIA** (Carbon Offsetting and Reduction Scheme).  
   - Digital Product Passport (**N-95**) tracks cumulative zero-emission flight hours and CO₂ avoidance.

4. **Water Vapor Management**  
   - H₂ fuel-cell byproduct: **pure water vapor** (H₂O), no carbon content.  
   - Water management per **ATA 38** (Water/Waste): condensate collection or controlled overboard venting.  
   - No environmental impact from water vapor emissions (naturally occurring atmospheric component).

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-EMI-001**](../../V_AND_V/cases/TEST-EMI-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-EMI-GT-001**](../../V_AND_V/cases/TEST-EMI-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-EMI-FT-001**](../../V_AND_V/cases/TEST-EMI-FT-001.md)

---

## Rationale
Achieving zero in-flight CO₂ emissions addresses aviation's climate impact, aligning with ICAO's Carbon Neutral Growth (CNG) goals and supporting regional/national net-zero aviation commitments. Hydrogen fuel cells produce only water vapor, eliminating carbon emissions at the source without reliance on offsetting mechanisms.

🔗 Sustainability framework: ../../DESIGN/system_design/[**sustainability_framework.md**](../../DESIGN/system_design/sustainability_framework.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **C2-28** Fuel Systems (H₂ as zero-carbon fuel per **RQ-10-01**)  
  - **E2-24** Electrical Power (fuel-cell power generation)  
  - **N-95** Digital Product Passport (emissions tracking, lifecycle accounting)  
  - **L1-22** EMS (operational mode management, fuel source selection)

- **Key interfaces:**  
  - Fuel-cell system → Zero CO₂ emissions certification  
  - EMS → Operational mode logging (H₂-only vs. hybrid)  
  - Digital twin → Emissions reporting and traceability  
  - Flight data recorder → Post-flight emissions audit trail

🔗 Decompositions:  
- Emissions accounting → ../SR/[**SR-EMIS-001.md**](../SR/SR-EMIS-001.md)  
- DPP integration → ../SR/[**SR-DPP-001.md**](../SR/SR-DPP-001.md)

---

## Constraints & Interfaces
- **Operational constraint:** Zero-emission mode limited to hydrogen-primary operations; SAF mode produces **≈ 80 g CO₂/km** (SAF lifecycle emissions lower than fossil jet fuel but non-zero).  
- **Regulatory landscape:** ICAO/EASA/FAA emissions certification frameworks evolving to include hydrogen propulsion; aircraft must comply with emerging **H₂ aircraft emissions standards**.  
- **Lifecycle emissions:** While in-flight CO₂ = 0 g/km, upstream H₂ production emissions depend on source ("green" electrolysis vs. "grey" steam methane reforming); operational sustainability requires **green H₂ supply chain**.  
- **Verification complexity:** Emissions = 0 g/km is self-evident from H₂ stoichiometry, but operational mode compliance (H₂-only vs. hybrid) requires robust data logging and auditing.

🔗 Interface references:  
- Emissions monitoring: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)  
- DPP traceability: ../../INTERFACES/[**54_digital_interfaces.md**](../../INTERFACES/54_digital_interfaces.md)

---

## Assumptions
- **Hydrogen purity:** LH₂ supply meets **ISO 14687** (≥ 99.97% purity); trace carbon impurities negligible.  
- **CO₂ battery loop:** Closed-loop CO₂ system remains sealed during normal operations (no unintended CO₂ venting).  
- **Operational discipline:** Flight crews adhere to zero-emission mode protocol (H₂-only) for mission segments where infrastructure and reserves permit.  
- **Regulatory acceptance:** ICAO and regional authorities recognize H₂ fuel-cell propulsion as **zero-emission technology** for certification and reporting purposes.

🔗 Supporting evidence: ../../ENGINEERING/analyses/environmental/[**hydrogen_emissions_analysis.md**](../../ENGINEERING/analyses/environmental/hydrogen_emissions_analysis.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Stoichiometric calculation confirming H₂ + O₂ → H₂O (no carbon); lifecycle emissions assessment (green H₂ supply chain).  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Ground Testing:** Fuel-cell exhaust composition analysis (water vapor only, no CO₂ detection).  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Flight Testing:** In-flight emissions monitoring (onboard sensors confirm zero CO₂ in H₂-only mode); operational mode logging validation.  
  - Results: ../../V_AND_V/verification/results/[**flight_test_emissions/**](../../V_AND_V/verification/results/flight_test_emissions/)

- **Certification:** ICAO Annex 16 Vol III compliance demonstration (zero CO₂ emissions in H₂ mode); CORSIA reporting validation.  
  - Compliance: ../../CERTIFICATION/[**emissions_certification_report.pdf**](../../CERTIFICATION/emissions_certification_report.pdf)

**Acceptance evidence:** Analytical and empirical confirmation of 0 g CO₂/km in H₂-only mode; operational mode tracking functional; regulatory compliance achieved.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-020.md**](../ALR/ALR-020.md) – Environmental sustainability  
- **Emissions standards:** **ICAO Annex 16 Volume III** (CO₂ emissions certification), **CORSIA** (Carbon Offsetting and Reduction Scheme)  
- **Hydrogen standards:** **ISO 14687** (hydrogen fuel quality)  
- **Data recording:** **CS-25.1457** (flight data recorder), **ATA 31**  
- **Sustainability framework:** Internal sustainability policy and lifecycle emissions accounting per **RQ-40-06**

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-020.md**](../ALR/ALR-020.md)  
- **Linked SRs:**  
  - ../SR/[**SR-EMIS-001.md**](../SR/SR-EMIS-001.md) – Emissions accounting methodology  
  - ../SR/[**SR-DPP-001.md**](../SR/SR-DPP-001.md) – Digital Product Passport emissions tracking  
- **Related Requirements:**  
  - **RQ-10-01** (LH₂ fuel-cell primary energy source)  
  - **RQ-10-02** (Closed-loop CO₂ battery — no venting)  
  - **RQ-10-03** (SAF mode produces emissions — not zero-emission)  
  - **RQ-40-06** (ISO 14001/50001 environmental management)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-EMI-001**](../../V_AND_V/cases/TEST-EMI-001.md) · ../../V_AND_V/cases/[**TEST-EMI-GT-001**](../../V_AND_V/cases/TEST-EMI-GT-001.md) · ../../V_AND_V/cases/[**TEST-EMI-FT-001**](../../V_AND_V/cases/TEST-EMI-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-EMIS-001.csv**](../RTM/RTM-EMIS-001.csv)

---

## Notes
- **Lifecycle perspective:** While in-flight CO₂ = 0 g/km, true net-zero aviation requires green hydrogen production (renewable energy electrolysis). Operational sustainability depends on H₂ supply chain decarbonization.  
- **Contrail impact:** H₂ combustion increases water vapor emissions, potentially affecting contrail formation and radiative forcing. Ongoing research assesses net climate impact (CO₂ elimination vs. H₂O contrail effects).  
- **Regulatory evolution:** ICAO is developing H₂ aircraft emissions standards; aircraft design anticipates compliance with emerging regulations.
