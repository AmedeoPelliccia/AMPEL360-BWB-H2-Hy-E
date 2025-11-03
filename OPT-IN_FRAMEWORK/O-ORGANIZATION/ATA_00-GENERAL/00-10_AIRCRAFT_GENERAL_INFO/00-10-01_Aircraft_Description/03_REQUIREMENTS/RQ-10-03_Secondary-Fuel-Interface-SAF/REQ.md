# RQ-10-03 — Secondary Fuel Interface (SAF)

## Statement
The aircraft shall incorporate a **secondary fuel interface** capable of utilizing **Sustainable Aviation Fuel (SAF)** that is **Jet-A compatible** for hybrid range extension, contingency operations, and operational flexibility when hydrogen refueling infrastructure is unavailable.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **SAF Fuel System Configuration**  
   - Fuel type: **100% SAF** (ASTM D7566 approved blends) or **Jet-A/Jet-A1** fallback.  
   - Fuel tank capacity: **≥ 4,000 liters** (≈3,200 kg of SAF).  
   - Fuel system compliant with **CS-25.951** through **CS-25.979** (fuel system design).  
   - Fuel pumps, valves, and distribution per **ATA 28-40**.

2. **Turbogenerator Integration**  
   - SAF-burning auxiliary power unit (APU) or turbogenerator rated for **≥ 2 MW electrical output**.  
   - Generator electrically coupled to **HVDC bus (540 VDC)** via rectifier/converter per **E2-24**.  
   - Turbogenerator operates in **standby mode** during hydrogen-primary operations; automatically activates for contingency or range extension.  
   - Emissions during SAF operation: **ICAO Annex 16 Vol II compliance** (CO₂, NOₓ, PM).

3. **Operational Modes**  
   - **Mode 1 (H₂-primary):** Turbogenerator **OFF** or idle; SAF consumption ≈ 0.  
   - **Mode 2 (Hybrid):** Turbogenerator supplements fuel-cell output during high-demand phases (takeoff, climb, contingency).  
   - **Mode 3 (SAF-contingency):** If hydrogen depleted or fuel-cell failure, turbogenerator provides **≥ 50% of cruise power** to enable safe diversion to nearest suitable airport.

4. **Fuel Management and Control**  
   - Fuel quantity indication per **CS-25.1337**.  
   - Automatic fuel switching logic integrated with **EMS (L1-22)** and flight management system.  
   - Cross-feed capability between SAF and turbogenerator.  
   - Fuel system monitoring and alerts per **ATA 28-60**.

5. **Compatibility and Storage**  
   - SAF storage tanks constructed from **aluminum alloy or composite** compatible with SAF chemistry.  
   - Fuel system seals and hoses certified for **SAF + Jet-A** per **ASTM D7566**.  
   - Long-term storage stability: **≥ 6 months** without fuel degradation.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-SAF-001**](../../V_AND_V/cases/TEST-SAF-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-SAF-GT-001**](../../V_AND_V/cases/TEST-SAF-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-SAF-FT-001**](../../V_AND_V/cases/TEST-SAF-FT-001.md)

---

## Rationale
The SAF interface provides operational flexibility, regulatory compliance for contingency power, and backward compatibility with existing airport fuel infrastructure. This hybrid approach de-risks hydrogen adoption during the transition period while maintaining zero-emission capability as the primary operational mode.

🔗 Background: ../../04_DESIGN/system_design/[**hybrid_fuel_strategy.md**](../../04_DESIGN/system_design/hybrid_fuel_strategy.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **C2-28** Fuel Systems (SAF storage, distribution, control per **ATA 28-40**)  
  - **E2-49** Airborne Auxiliary Power (turbogenerator)  
  - **E2-24** Electrical Power (turbogenerator electrical output integration)  
  - **L1-22** EMS/Autoflight (fuel mode selection logic)  
  - **E1-26** Fire Protection (fuel tank and turbogenerator fire detection/suppression)

- **Key interfaces:**  
  - SAF fuel tanks → Turbogenerator  
  - Turbogenerator electrical output → HVDC bus  
  - EMS controller → Fuel mode selection (H₂ vs. SAF)  
  - Cockpit displays → Fuel quantity, mode status  

🔗 Decompositions:  
- SAF fuel system → ../SR/[**SR-SAF-001.md**](../SR/SR-SAF-001.md)  
- Turbogenerator specs → ../SR/[**SR-TURBOGEN-001.md**](../SR/SR-TURBOGEN-001.md)  
- Fuel mode logic → ../SR/[**SR-EMS-003.md**](../SR/SR-EMS-003.md)

---

## Constraints & Interfaces
- **Weight allocation:** SAF system (tanks + turbogenerator) ≤ **1,800 kg empty** + **3,200 kg fuel** when full.  
- **Fire safety:** SAF tanks and turbogenerator must comply with **CS-25.863** (fire zones), **ATA 26** (fire detection and suppression).  
- **Emissions trade-off:** SAF operation produces CO₂ emissions; however, lifecycle CO₂ from SAF is **≤ 80% lower** than fossil Jet-A (per ASTM D7566 sustainability criteria).  
- **Operational complexity:** Flight crew training required for dual-fuel operations and fuel mode management.  
- **Infrastructure dependency:** SAF availability varies by airport; operational planning must account for SAF supply chain.

🔗 Interface references:  
- Fuel system mechanical: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Electrical integration: ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- Control and data: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- SAF supply chain maturity: **100% SAF blends** available at major airports by entry into service (EIS).  
- Turbogenerator technology: **commercial off-the-shelf (COTS)** APU or small gas turbine adapted for electrical generation.  
- Fuel system design leverages existing **Jet-A** certification basis with **SAF compatibility validation** per ASTM D7566.  
- Regulatory acceptance: **CS-25 and FAA Part 25** allow hybrid H₂/SAF architecture with appropriate safety case.

🔗 Technology and supply chain: ../../ENGINEERING/analyses/fuel/[**SAF_availability_assessment.md**](../../ENGINEERING/analyses/fuel/SAF_availability_assessment.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Fuel system design analysis, compatibility studies (SAF chemistry vs. materials), and emissions modeling.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Component Testing:** SAF compatibility tests (seals, hoses, pumps), turbogenerator performance testing (power, emissions, endurance).  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Integration Testing:** Ground testbed validation of fuel mode switching, EMS coordination, and electrical integration.  
  - Results: ../../V_AND_V/verification/results/[**SAF_integration_tests/**](../../V_AND_V/verification/results/SAF_integration_tests/)

- **Flight Testing:** SAF mode flight validation (contingency scenarios, fuel consumption, emissions measurement).  
  - Results: ../../V_AND_V/verification/results/[**flight_test_SAF_operations/**](../../V_AND_V/verification/results/flight_test_SAF_operations/)

**Acceptance evidence:** SAF fuel system operates safely and reliably; turbogenerator provides required contingency power; fuel mode switching is seamless; emissions comply with ICAO standards.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-012.md**](../ALR/ALR-012.md) – Secondary fuel system  
- **Fuel system standards:** **CS-25.951** through **CS-25.979** (fuel system design and installation)  
- **SAF standards:** **ASTM D7566** (Sustainable Aviation Fuel specifications)  
- **Emissions:** **ICAO Annex 16 Volume II** (aircraft engine emissions)  
- **Fire protection:** **CS-25.863** (fire zones), **ATA 26**  
- **Electrical:** **DO-160G** (turbogenerator electrical qualification)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-012.md**](../ALR/ALR-012.md)  
- **Linked SRs:**  
  - ../SR/[**SR-SAF-001.md**](../SR/SR-SAF-001.md) – SAF fuel system design  
  - ../SR/[**SR-TURBOGEN-001.md**](../SR/SR-TURBOGEN-001.md) – Turbogenerator specifications  
  - ../SR/[**SR-EMS-003.md**](../SR/SR-EMS-003.md) – Fuel mode management logic  
- **Related Requirements:**  
  - **RQ-10-01** (Primary H₂ fuel-cell system)  
  - **RQ-20-01** (In-flight CO₂ emissions – SAF mode produces emissions)  
  - **RQ-20-06** (Fire suppression)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-SAF-001**](../../V_AND_V/cases/TEST-SAF-001.md) · ../../V_AND_V/cases/[**TEST-SAF-GT-001**](../../V_AND_V/cases/TEST-SAF-GT-001.md) · ../../V_AND_V/cases/[**TEST-SAF-FT-001**](../../V_AND_V/cases/TEST-SAF-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-SAF-001.csv**](../RTM/RTM-SAF-001.csv)

---

## Notes
- **Operational priority:** The aircraft is designed for **hydrogen-primary** operations. SAF mode is **secondary/contingency only** to maximize zero-emission flight time.  
- **Emissions accounting:** When operating in SAF mode, CO₂ emissions are calculated and reported per CORSIA requirements, but lifecycle emissions are significantly reduced due to SAF sustainability criteria.  
- **Future evolution:** As hydrogen infrastructure matures globally, SAF system usage is expected to decline, and future variants may eliminate SAF capability to reduce weight and complexity.
