# RQ-10-01 — Primary Energy Source

## Statement
The aircraft shall use **liquid hydrogen (LH₂)** as the primary energy source via **PEM (Proton Exchange Membrane) fuel-cell stacks** for all mission phases, providing clean electrical power to the hybrid-electric propulsion system with **zero direct CO₂ emissions** during flight operations in hydrogen-only mode.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Fuel Cell System Configuration**  
   - PEM fuel-cell stacks sized for **15 MW nominal continuous power** output.  
   - Stack efficiency ≥ **60% (HHV basis)** at 70% rated load.  
   - Hydrogen consumption rate validated against mission energy profile.  
   - Stack operating temperature maintained between **60–80°C** with integrated thermal management.

2. **Hydrogen Storage and Supply**  
   - Cryogenic LH₂ stored at **≤ 20 K** in vacuum-insulated tanks per **ATA 28-10**.  
   - Boil-off rate ≤ **0.1%/h** per **RQ-20-03**.  
   - Supply pressure regulation: **5–10 bar** at fuel-cell inlet.  
   - Emergency venting system compliant with **ISO 19880-1**.

3. **Electrical Output and Integration**  
   - DC power output integrated with **ATA 24 HVDC bus** (540 VDC nominal).  
   - Power quality: voltage ripple ≤ **±2%**, transient response < **50 ms** for 20% load step.  
   - Fault isolation coordination with **E2-24 electrical architecture**.

4. **Emissions and Environmental**  
   - Zero carbon emissions during hydrogen-only operation.  
   - Water vapor byproduct managed per **ATA 38** (condensate collection or overboard venting).  
   - Compliance with **CS-25 environmental standards**.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-FC-001**](../../V_AND_V/cases/TEST-FC-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-FC-GT-001**](../../V_AND_V/cases/TEST-FC-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-FC-FT-001**](../../V_AND_V/cases/TEST-FC-FT-001.md)

---

## Rationale
Liquid hydrogen combined with PEM fuel cells provides the highest gravimetric energy density among practical zero-emission energy sources, enabling long-range operations while meeting sustainability targets. PEM technology offers fast response, high efficiency, and proven scalability for aerospace applications.

🔗 Background analysis: ../../04_DESIGN/system_design/[**hydrogen_energy_rationale.md**](../../04_DESIGN/system_design/hydrogen_energy_rationale.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **C2-28** Fuel/Cryogenic Systems (LH₂ storage, handling)  
  - **E2-24** Electrical Power (fuel-cell integration, HVDC)  
  - **E1-21** Environmental Control (thermal management, humidity)  
  - **L1-22** Energy Management System (power dispatch logic)

- **Key interfaces:**  
  - Hydrogen supply → Fuel-cell stacks  
  - Fuel-cell DC output → HVDC distribution bus  
  - Thermal rejection → Aircraft thermal management system  
  - Control signals → EMS master controller

🔗 Decompositions:  
- Fuel-cell stack design → ../SR/[**SR-FC-001.md**](../SR/SR-FC-001.md)  
- LH₂ tank specifications → ../SR/[**SR-TANK-001.md**](../SR/SR-TANK-001.md)  
- EMS control algorithms → ../SR/[**SR-EMS-001.md**](../SR/SR-EMS-001.md)

---

## Constraints & Interfaces
- **Cryogenic safety:** LH₂ handling must comply with **ISO 19880-1** and **EASA Special Condition for Hydrogen**.  
- **Thermal management:** Fuel-cell waste heat (≈6 MW @ full power) must be rejected without exceeding thermal system capacity.  
- **Electrical stability:** Fuel-cell transient response coordinated with **CO₂ buffer** (**RQ-10-02**) to prevent bus voltage excursions.  
- **Weight and volume:** Fuel-cell system mass and installation volume must fit within aircraft mass/balance envelope.

🔗 Interface references:  
- Cryogenic interfaces: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Electrical interfaces: ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- Data/control interfaces: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- LH₂ supply infrastructure available at operational airports per **I-85 Infrastructure Interface Standards**.  
- Fuel-cell stack technology maturity: **TRL 7+** at program start.  
- Membrane degradation rate: < **2% per 1000 hours** under nominal operating conditions.  
- Water management: condensate either stored or safely vented during flight.

🔗 Supporting evidence: ../../ENGINEERING/analyses/energy/[**fuel_cell_technology_readiness.md**](../../ENGINEERING/analyses/energy/fuel_cell_technology_readiness.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Thermodynamic modeling, energy balance, and mass-flow validation.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Component Testing:** Fuel-cell stack bench tests (power, efficiency, transient response, endurance).  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Integration Testing:** Fuel-cell + HVDC bus + thermal system validation on iron bird or ground testbed.  
  - Results: ../../V_AND_V/verification/results/[**fuel_cell_integration_tests/**](../../V_AND_V/verification/results/fuel_cell_integration_tests/)

- **Flight Testing:** In-flight power demand validation across mission profile.  
  - Results: ../../V_AND_V/verification/results/[**flight_test_energy_validation/**](../../V_AND_V/verification/results/flight_test_energy_validation/)

**Acceptance evidence:** Fuel-cell performance meets power, efficiency, and reliability targets across full operating envelope; hydrogen consumption matches mission analysis within **±5%**.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-010.md**](../ALR/ALR-010.md) – Hydrogen propulsion systems  
- **Hydrogen standards:** **ISO 19880-1**, **SAE ARP8677**, **EASA Special Condition SC-H2**  
- **Electrical standards:** **DO-160G** (environmental qualification)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-010.md**](../ALR/ALR-010.md)  
- **Linked SRs:**  
  - ../SR/[**SR-FC-001.md**](../SR/SR-FC-001.md) – Fuel-cell stack specifications  
  - ../SR/[**SR-TANK-001.md**](../SR/SR-TANK-001.md) – LH₂ tank design  
  - ../SR/[**SR-EMS-001.md**](../SR/SR-EMS-001.md) – Energy management  
- **Related Requirements:**  
  - **RQ-10-02** (Hybrid CO₂ buffer)  
  - **RQ-20-02** (Ground refueling safety)  
  - **RQ-20-03** (Boil-off management)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-FC-001**](../../V_AND_V/cases/TEST-FC-001.md) · ../../V_AND_V/cases/[**TEST-FC-GT-001**](../../V_AND_V/cases/TEST-FC-GT-001.md) · ../../V_AND_V/cases/[**TEST-FC-FT-001**](../../V_AND_V/cases/TEST-FC-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-FC-001.csv**](../RTM/RTM-FC-001.csv)

---

## Notes
- **Hybrid operation:** SAF turbogenerator (**RQ-10-03**) serves as backup/auxiliary power but does not alter the primary hydrogen-based architecture.  
- **Technology evolution:** As PEM fuel-cell technology matures, efficiency and power density targets may be updated in future program phases via formal **CHANGES.md** process.  
- **Scalability:** Architecture designed to support future power increases (e.g., 18–20 MW) with modular fuel-cell stack addition.
