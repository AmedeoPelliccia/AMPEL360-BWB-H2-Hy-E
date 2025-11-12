# RQ-10-02 — Hybrid Storage (Closed-Loop CO₂ Battery)

## Statement
The aircraft shall incorporate a **closed-loop CO₂ battery system** as hybrid energy storage to buffer transient power demands, enhance regenerative energy recovery, and reduce peak hydrogen consumption during high-power flight phases such as takeoff, climb, and go-around.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Energy Storage Capacity and Performance**  
   - Total usable energy capacity: **≥ 500 kWh** (dischargeable range).  
   - Peak discharge power: **≥ 5 MW** for ≥ **3 minutes** (takeoff/go-around).  
   - Peak charge power: **≥ 3 MW** (regenerative descent, idle taxi).  
   - Round-trip efficiency: **≥ 90%** (charge-discharge cycle).

2. **Closed-Loop CO₂ System Integration**  
   - CO₂ capture and regeneration system integrated per **ATA 21-80** (provisional).  
   - Operates as reversible electrochemical or thermochemical battery.  
   - No net CO₂ vented to atmosphere during normal operations.  
   - CO₂ working fluid is circulated in a closed loop within aircraft systems.

3. **Power Electronics and Electrical Integration**  
   - Bidirectional DC/DC converters interfaced with **HVDC bus (540 VDC nominal)** per **E2-24**.  
   - Transient response time: < **100 ms** for full power step.  
   - Voltage regulation: ±**1.5% Vnom** during charge/discharge.  
   - Thermal management coordinated with aircraft thermal system per **E1-21**.

4. **State of Charge (SOC) Management**  
   - SOC maintained between **20–80%** for nominal operations (preserves cycle life).  
   - SOC excursion ≤ **±5%** around cruise set-point during steady flight.  
   - Predictive EMS algorithms optimize SOC profile across mission per **L1-22** and **RQ-10-06**.

5. **Safety and Fault Tolerance**  
   - Thermal runaway prevention: cell-level temperature monitoring < **60°C** with active cooling.  
   - Electrical isolation monitoring per **DO-160G**.  
   - Graceful degradation: system remains functional with **10% cell failure**.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-CO2BAT-001**](../../V_AND_V/cases/TEST-CO2BAT-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-CO2BAT-GT-001**](../../V_AND_V/cases/TEST-CO2BAT-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-CO2BAT-FT-001**](../../V_AND_V/cases/TEST-CO2BAT-FT-001.md)

---

## Rationale
The closed-loop CO₂ battery decouples transient power demands from the fuel-cell system, which has slower response dynamics. This reduces fuel-cell oversizing, extends stack lifetime, and enables regenerative energy capture during descent and braking. The CO₂ working fluid provides high energy density while avoiding lithium-ion fire risks and supply chain constraints.

🔗 Concept background: ../../04_DESIGN/system_design/[**CO2_battery_architecture.md**](../../04_DESIGN/system_design/CO2_battery_architecture.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **C2-28** Fuel/Energy Systems (CO₂ loop, storage tanks)  
  - **E2-49** Airborne Auxiliary Power (battery power electronics)  
  - **E2-24** Electrical Power (HVDC integration)  
  - **L1-22** Autoflight/EMS (SOC management, power dispatch)  
  - **E1-21** Environmental Control (thermal management)

- **Key interfaces:**  
  - CO₂ battery ↔ HVDC bus (bidirectional power)  
  - CO₂ battery ↔ EMS controller (SOC, power commands)  
  - CO₂ battery ↔ thermal management (cooling)  
  - CO₂ battery ↔ fuel-cell system (coordinated power dispatch per **RQ-10-01**)

🔗 Decompositions:  
- Battery system design → ../SR/[**SR-CO2BAT-001.md**](../SR/SR-CO2BAT-001.md)  
- Power electronics → ../SR/[**SR-POWER-ELEC-001.md**](../SR/SR-POWER-ELEC-001.md)  
- EMS dispatch logic → ../SR/[**SR-EMS-002.md**](../SR/SR-EMS-002.md)

---

## Constraints & Interfaces
- **Weight and volume:** Battery system mass ≤ **2,500 kg**; volume ≤ **4 m³** to fit within fuselage underfloor compartment.  
- **Thermal constraints:** Operating temperature range **10–45°C**; thermal rejection capacity coordinated with aircraft-level heat exchangers.  
- **Electrical coordination:** Power dispatch must be synchronized with fuel-cell output to avoid bus voltage excursions beyond **±3% Vnom**.  
- **Safety isolation:** CO₂ loop must not interfere with cabin pressurization or life support systems per **ATA 21**.

🔗 Interface references:  
- Mechanical/installation: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Electrical/HVDC: ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- Data/control: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- CO₂ battery technology maturity: **TRL 6+** at program start (prototype validation required).  
- CO₂ working fluid purity maintained by onboard regeneration system (no external refill needed).  
- Cycle life: **≥ 5,000 full equivalent cycles** over aircraft operational lifetime (20 years).  
- No thermal runaway risk under normal operations (verified by component testing).

🔗 Technology readiness: ../../ENGINEERING/analyses/energy/[**CO2_battery_TRL_assessment.md**](../../ENGINEERING/analyses/energy/CO2_battery_TRL_assessment.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Electrochemical modeling, thermal simulation, and energy balance validation across mission profile.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Component Testing:** Battery module testing (capacity, power, efficiency, thermal, cycle life).  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **System Integration Testing:** CO₂ battery + fuel-cell + HVDC bus on ground testbed (iron bird).  
  - Results: ../../V_AND_V/verification/results/[**hybrid_integration_tests/**](../../V_AND_V/verification/results/hybrid_integration_tests/)

- **Flight Testing:** Mission profile validation with real transient power demands (takeoff, climb, descent, go-around).  
  - Results: ../../V_AND_V/verification/results/[**flight_test_power_buffering/**](../../V_AND_V/verification/results/flight_test_power_buffering/)

**Acceptance evidence:** Battery meets capacity, power, efficiency, and transient response targets; SOC management validated across full mission envelope; no thermal or electrical faults during testing.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-011.md**](../ALR/ALR-011.md) – Hybrid energy storage  
- **Safety standards:** **ARP4761**, **ARP4754A** (system safety assessment)  
- **Electrical standards:** **DO-160G** (environmental qualification), **DO-178C** (EMS software)  
- **Battery safety:** Applicable sections of **RTCA DO-311** (lithium battery guidance, adapted for CO₂ electrochemistry)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-011.md**](../ALR/ALR-011.md)  
- **Linked SRs:**  
  - ../SR/[**SR-CO2BAT-001.md**](../SR/SR-CO2BAT-001.md) – Battery system architecture  
  - ../SR/[**SR-POWER-ELEC-001.md**](../SR/SR-POWER-ELEC-001.md) – Bidirectional converters  
  - ../SR/[**SR-EMS-002.md**](../SR/SR-EMS-002.md) – EMS dispatch and SOC management  
- **Related Requirements:**  
  - **RQ-10-01** (Primary fuel-cell energy source)  
  - **RQ-10-06** (Peak load buffering ±20%)  
  - **RQ-20-05** (Electrical isolation fault tolerance)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-CO2BAT-001**](../../V_AND_V/cases/TEST-CO2BAT-001.md) · ../../V_AND_V/cases/[**TEST-CO2BAT-GT-001**](../../V_AND_V/cases/TEST-CO2BAT-GT-001.md) · ../../V_AND_V/cases/[**TEST-CO2BAT-FT-001**](../../V_AND_V/cases/TEST-CO2BAT-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-CO2BAT-001.csv**](../RTM/RTM-CO2BAT-001.csv)

---

## Notes
- **Technology innovation:** The closed-loop CO₂ battery represents a novel energy storage approach. Prototype validation and certification pathways are being developed in coordination with EASA and FAA.  
- **Reversible carbon use:** The CO₂ working fluid is captured and regenerated onboard, ensuring zero net emissions and avoiding reliance on external CO₂ supply.  
- **Scalability:** Battery capacity may be adjusted in future variants to optimize for different mission profiles (short-haul vs. regional).
