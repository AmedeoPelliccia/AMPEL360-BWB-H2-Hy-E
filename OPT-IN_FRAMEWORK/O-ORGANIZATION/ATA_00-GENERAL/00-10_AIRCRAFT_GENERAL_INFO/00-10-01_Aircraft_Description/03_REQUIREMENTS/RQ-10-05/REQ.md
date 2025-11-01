# RQ-10-05 — Total Installed Power (15 MW Nominal)

## Statement
The hybrid-electric propulsion system shall provide a **total installed power of 15 MW (nominal continuous rating)** to support all flight phases from sea level to cruise altitude, ensuring adequate thrust margins, electrical system capacity, and energy management flexibility.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Power Generation Capacity**  
   - **Primary source (H₂ fuel cells):** ≥ **13 MW continuous** output at cruise altitude (FL350) per **RQ-10-01**.  
   - **Secondary source (CO₂ battery):** ≥ **5 MW peak discharge** for transients per **RQ-10-02**.  
   - **Tertiary source (SAF turbogenerator):** ≥ **2 MW contingency** per **RQ-10-03**.  
   - **Combined capacity:** System capable of delivering **15 MW continuous** + **5 MW transient** without exceeding thermal or electrical limits.

2. **Power Distribution and Load Allocation**  
   - **Propulsion load:** 8 × propulsors @ **1.8–2.0 MW each** = **14.4–16 MW** at takeoff/climb power setting.  
   - **Non-propulsive loads:** **≤ 500 kW** (avionics, ECS, lighting, anti-ice, cabin systems) per **E2-24**.  
   - **Peak total demand:** **≤ 16.5 MW** during takeoff; fuel cell + CO₂ battery combined provide required power.  
   - **Cruise load:** **≈ 10–11 MW** (propulsion + non-propulsive), well within fuel-cell continuous rating.

3. **Power System Architecture**  
   - **HVDC bus voltage:** **540 VDC nominal** (±10% operating range: 486–594 VDC).  
   - **Bus topology:** Dual-channel redundant with cross-tie capability per **E2-24**.  
   - **Power electronics:** DC/DC converters, inverters, and motor controllers sized for **15 MW total throughput** with ≥ **97% efficiency**.  
   - **Fault tolerance:** System remains operational with single-channel failure or single fuel-cell stack failure.

4. **Thermal Management**  
   - **Waste heat rejection:** System designed to reject **≈ 6–8 MW** waste heat (fuel cells + power electronics) at maximum continuous power.  
   - **Cooling system integration:** Coordinated with **E1-21** (ECS) and aircraft thermal management per **ATA 21-80**.  
   - **Thermal limits:** No component exceeds **80°C continuous** operating temperature.

5. **Performance Margins**  
   - **Power margin:** ≥ **10% reserve** above maximum expected demand in all flight phases.  
   - **Degradation allowance:** System meets power requirements with **≤ 5% degradation** due to fuel-cell aging or component wear over operational life.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-PWR-001**](../../V_AND_V/cases/TEST-PWR-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-PWR-GT-001**](../../V_AND_V/cases/TEST-PWR-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-PWR-FT-001**](../../V_AND_V/cases/TEST-PWR-FT-001.md)

---

## Rationale
The 15 MW nominal power target is derived from propulsion thrust requirements (8 × 2 MW propulsors) plus non-propulsive electrical loads. This sizing ensures adequate margins for takeoff, climb, and contingency scenarios while maintaining cruise efficiency. The multi-source architecture (fuel cells + battery + turbogenerator) provides redundancy and operational flexibility.

🔗 Sizing background: ../../DESIGN/system_design/[**power_system_sizing.md**](../../DESIGN/system_design/power_system_sizing.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **E2-24** Electrical Power (HVDC architecture, power distribution)  
  - **C2-28** Fuel/Energy (fuel-cell stacks, CO₂ battery)  
  - **E2-49** Auxiliary Power (SAF turbogenerator)  
  - **P-61** Propulsion (electric motor power demand)  
  - **L1-22** EMS (power dispatch optimization, load management)  
  - **E1-21** Environmental (thermal management, waste heat rejection)

- **Key interfaces:**  
  - Fuel-cell stacks → HVDC bus  
  - CO₂ battery → HVDC bus (bidirectional)  
  - Turbogenerator → HVDC bus  
  - HVDC bus → Propulsor motor controllers  
  - HVDC bus → Non-propulsive loads (avionics, ECS, etc.)  

🔗 Decompositions:  
- Power system architecture → ../SR/[**SR-PWR-ARCH-001.md**](../SR/SR-PWR-ARCH-001.md)  
- HVDC bus design → ../SR/[**SR-HVDC-001.md**](../SR/SR-HVDC-001.md)  
- EMS power dispatch → ../SR/[**SR-EMS-004.md**](../SR/SR-EMS-004.md)

---

## Constraints & Interfaces
- **Weight allocation:** Total power system (fuel cells + battery + turbogenerator + power electronics + cabling) ≤ **6,500 kg**.  
- **Volume allocation:** Power system components must fit within designated equipment bays and underfloor compartments per airframe layout.  
- **Electrical stability:** HVDC bus voltage must remain within **±3% of nominal** during normal operations; transient excursions ≤ **±10%** for < **100 ms**.  
- **Thermal constraints:** Waste heat must be rejected without exceeding aircraft thermal system capacity or degrading cabin comfort.  
- **Redundancy:** System architecture ensures **no single point of failure** causes total loss of propulsion power.

🔗 Interface references:  
- Electrical architecture: ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- Thermal interfaces: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Control interfaces: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- **Fuel-cell efficiency:** ≥ **60% (HHV)** at 70% load, as per **RQ-10-01**.  
- **Power electronics efficiency:** ≥ **97%** for DC/DC conversion and motor drives.  
- **Non-propulsive load growth:** **≤ 10%** increase over baseline estimate during detailed design.  
- **Operational profile:** Power demand validated against mission energy profile per **System architecture v0.9**.  
- **Component availability:** All major power system components (fuel cells, batteries, power electronics) available at **TRL 7+** by program start.

🔗 Supporting data: ../../ENGINEERING/analyses/electrical/[**power_budget_analysis.md**](../../ENGINEERING/analyses/electrical/power_budget_analysis.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Electrical system modeling, power budget analysis, thermal simulation, and mission profile validation.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Component Testing:** Fuel-cell, battery, turbogenerator, and power electronics performance testing (power, efficiency, thermal).  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Ground Integration Testing:** Full electrical system testing on iron bird (power generation, distribution, load management, fault scenarios).  
  - Results: ../../V_AND_V/verification/results/[**electrical_integration_tests/**](../../V_AND_V/verification/results/electrical_integration_tests/)

- **Flight Testing:** Mission profile power demand validation, system performance across full envelope, transient response testing.  
  - Results: ../../V_AND_V/verification/results/[**flight_test_power_system/**](../../V_AND_V/verification/results/flight_test_power_system/)

**Acceptance evidence:** Power system delivers ≥ 15 MW continuous and ≥ 5 MW transient; HVDC bus voltage stable; thermal limits not exceeded; redundancy and fault tolerance validated; power margins confirmed.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-014.md**](../ALR/ALR-014.md) – Power system architecture  
- **Electrical standards:** **DO-160G** (environmental qualification), **DO-178C/DO-254** (EMS software/hardware)  
- **Safety:** **ARP4761**, **ARP4754A** (system safety and development assurance)  
- **Hydrogen and battery standards:** **ISO 19880-1** (H₂), **RTCA DO-311** (battery safety, adapted)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-014.md**](../ALR/ALR-014.md)  
- **Linked SRs:**  
  - ../SR/[**SR-PWR-ARCH-001.md**](../SR/SR-PWR-ARCH-001.md) – Power system architecture  
  - ../SR/[**SR-HVDC-001.md**](../SR/SR-HVDC-001.md) – HVDC bus design  
  - ../SR/[**SR-EMS-004.md**](../SR/SR-EMS-004.md) – EMS power dispatch  
- **Related Requirements:**  
  - **RQ-10-01** (Fuel-cell primary power source)  
  - **RQ-10-02** (CO₂ battery hybrid storage)  
  - **RQ-10-03** (SAF turbogenerator)  
  - **RQ-10-04** (8 × propulsors, ≈16 MW total demand)  
  - **RQ-10-06** (Peak load buffering)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-PWR-001**](../../V_AND_V/cases/TEST-PWR-001.md) · ../../V_AND_V/cases/[**TEST-PWR-GT-001**](../../V_AND_V/cases/TEST-PWR-GT-001.md) · ../../V_AND_V/cases/[**TEST-PWR-FT-001**](../../V_AND_V/cases/TEST-PWR-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-PWR-001.csv**](../RTM/RTM-PWR-001.csv)

---

## Notes
- **Scalability:** The 15 MW architecture is baseline for initial aircraft variant. Future derivatives may scale to 18–20 MW for increased payload or performance.  
- **Technology margin:** Conservative power electronics efficiency (97%) provides margin for real-world losses and aging effects.  
- **Operational flexibility:** Multi-source architecture (fuel cells + battery + turbogenerator) allows optimized dispatch for efficiency, emissions, and system longevity.
