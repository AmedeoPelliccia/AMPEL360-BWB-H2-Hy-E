# RQ-10-04 — Propulsion Configuration (8 × Open-Fan Electric Propulsors)

## Statement
The aircraft shall utilize **eight (8) distributed open-fan electric propulsors** to provide thrust, leveraging the blended-wing-body (BWB) planform for optimal aerodynamic integration, acoustic performance, and propulsive efficiency.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Propulsor Configuration and Layout**  
   - **8 propulsors** total: distributed across aft fuselage/wing trailing edge per **ATA 61**.  
   - Each propulsor: **open-fan (un-ducted)** configuration with **variable-pitch blades**.  
   - Propulsor diameter: **≈ 2.0–2.5 m** per unit (optimized for cruise efficiency and acoustic signature).  
   - Installation: **embedded** or **surface-mounted** to minimize drag and maximize boundary layer ingestion (BLI) benefit.

2. **Thrust and Power Performance**  
   - Total installed thrust (all 8 propulsors): **≥ 150 kN** at sea level static, ISA conditions.  
   - Cruise thrust per propulsor: **≈ 15–20 kN** at M0.78, FL350.  
   - Propulsive efficiency: **≥ 83%** at design cruise point.  
   - Propulsor speed range: **1,000–3,000 RPM** (variable for efficiency optimization).

3. **Electric Motor Integration**  
   - Each propulsor driven by **≈ 1.8–2.0 MW electric motor** (total 15 MW installed across 8 units).  
   - Motor type: **permanent magnet synchronous motor (PMSM)** or **induction motor** with high power density (≥ **10 kW/kg**).  
   - Motor powered from **HVDC bus (540 VDC)** via motor controllers per **E2-24** and **ATA 61**.  
   - Motor thermal management integrated with aircraft cooling system per **E1-21**.

4. **Acoustic Performance**  
   - Noise signature: **-25 dB below CS-36 Chapter 4 limits** at certification points (takeoff, sideline, approach).  
   - Open-fan blade design optimized for low interaction noise with BWB airframe.  
   - Compliance validated via acoustic testing per **RQ-20-04** and **ATA 18**.

5. **Control and Redundancy**  
   - Independent motor controllers for each propulsor (fail-safe redundancy).  
   - Thrust asymmetry management: aircraft remains controllable with **≤ 2 propulsors inoperative**.  
   - Thrust vectoring capability (optional): **±5° pitch/yaw** for enhanced control authority.  
   - Propulsor control integrated with **flight control system (ATA 27)** and **EMS (L1-22)**.

6. **Aerodynamic Integration**  
   - Boundary layer ingestion (BLI) effect quantified: **≥ 5% propulsive efficiency gain** relative to podded nacelles.  
   - Installation drag minimized: **≤ 2% cruise drag penalty** relative to idealized thrust line.  
   - Flow distortion at propulsor inlet: **DC60 ≤ 0.15** (acceptable for motor-driven fans).

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-PROP-001**](../../V_AND_V/cases/TEST-PROP-001.md)  
- Wind tunnel: ../../V_AND_V/cases/[**TEST-PROP-WT-001**](../../V_AND_V/cases/TEST-PROP-WT-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-PROP-GT-001**](../../V_AND_V/cases/TEST-PROP-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-PROP-FT-001**](../../V_AND_V/cases/TEST-PROP-FT-001.md)

---

## Rationale
Distributed open-fan electric propulsion exploits the BWB's large aft surface for propulsor integration, enabling boundary layer ingestion and reducing installation drag. Electric drive eliminates gearbox losses and enables precise thrust modulation. The 8-propulsor configuration provides redundancy, acoustic benefits (lower tip speed per unit), and scalability.

🔗 Concept background: ../../DESIGN/system_design/[**distributed_propulsion_rationale.md**](../../DESIGN/system_design/distributed_propulsion_rationale.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **P-61** Propellers/Propulsors (ATA 61 — mechanical design, blades, hubs)  
  - **E2-24** Electrical Power (motor power distribution, HVDC)  
  - **E3-39** Power Electronics (motor controllers, inverters)  
  - **L1-27** Flight Controls (thrust asymmetry management, thrust vectoring)  
  - **A2** Aerodynamics (BLI, installation effects, flow distortion)  
  - **E1-26** Fire Protection (motor bay fire detection/suppression)

- **Key interfaces:**  
  - Electric motors ↔ HVDC bus (power supply)  
  - Motor controllers ↔ Flight control system (thrust commands)  
  - Propulsor installation ↔ Airframe structure (loads, mounts)  
  - Cooling system ↔ Motor thermal management  

🔗 Decompositions:  
- Propulsor mechanical → ../SR/[**SR-PROP-001.md**](../SR/SR-PROP-001.md)  
- Electric motor → ../SR/[**SR-MOTOR-001.md**](../SR/SR-MOTOR-001.md)  
- Motor controller → ../SR/[**SR-MOTORCTL-001.md**](../SR/SR-MOTORCTL-001.md)  
- Thrust management → ../SR/[**SR-THRUSTMGMT-001.md**](../SR/SR-THRUSTMGMT-001.md)

---

## Constraints & Interfaces
- **Weight and balance:** Propulsor distribution must maintain aircraft CG within envelope across all loading conditions.  
- **Structural loads:** Propulsor thrust and gyroscopic loads transmitted to airframe structure per **ATA 54 (Nacelles/Pylons)** and **ATA 57 (Wings)**.  
- **Electrical transients:** Motor controller switching must not induce **HVDC bus voltage transients > ±3%** or EMI exceeding **DO-160G** limits.  
- **Maintenance access:** Propulsor blade and motor inspection/replacement feasible within **≤ 8 hours** maintenance downtime.  
- **Acoustic constraints:** Community noise limits per **CS-36** must be met across all operational phases.

🔗 Interface references:  
- Mechanical/structural: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Electrical/HVDC: ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- Control/data: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- Electric motor technology: **TRL 8** (flight-proven in smaller aircraft; scaling to 2 MW per unit feasible).  
- Open-fan blade design: **composite materials** (carbon fiber) with erosion-resistant leading edges.  
- Propulsor redundancy: Loss of **2 adjacent propulsors** does not result in uncontrollable yaw or roll moment.  
- Certification: **CS-25.903** (propulsion system installation) and **CS-25.1093** (propulsion system tests) apply with electric propulsion interpretations.

🔗 Technology readiness: ../../ENGINEERING/analyses/propulsion/[**electric_propulsion_TRL.md**](../../ENGINEERING/analyses/propulsion/electric_propulsion_TRL.md)

---

## Verification (Method & Artefacts)
- **Analysis:** CFD for BLI effects, structural FEA for propulsor loads, electrical system analysis for power distribution.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Wind Tunnel Testing:** Scaled model testing for aerodynamic performance, flow distortion, and acoustic signature.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Component Testing:** Electric motor bench tests (power, efficiency, thermal, endurance); propulsor blade fatigue and bird strike tests.  
  - Results: ../../V_AND_V/verification/results/[**propulsor_component_tests/**](../../V_AND_V/verification/results/propulsor_component_tests/)

- **Ground Testing:** Full-scale propulsor rig testing; integrated electrical system testing on iron bird.  
  - Results: ../../V_AND_V/verification/results/[**propulsor_ground_tests/**](../../V_AND_V/verification/results/propulsor_ground_tests/)

- **Flight Testing:** In-flight performance validation across full envelope; acoustic flyover measurements; thrust asymmetry handling.  
  - Results: ../../V_AND_V/verification/results/[**flight_test_propulsion/**](../../V_AND_V/verification/results/flight_test_propulsion/)

**Acceptance evidence:** All 8 propulsors meet thrust, efficiency, and acoustic targets; electrical integration is stable; aircraft handling meets CS-25 requirements with propulsor-out scenarios.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-013.md**](../ALR/ALR-013.md) – Electric propulsion systems  
- **Propulsion standards:** **CS-25.903** (engines), **CS-25.1093** (propulsion system tests)  
- **Electrical standards:** **DO-160G** (environmental qualification), **DO-178C/DO-254** (motor controller software/hardware)  
- **Acoustic standards:** **CS-36 Chapter 4** (noise certification)  
- **Structural:** **CS-25.301** (loads), **CS-25.303** (factors of safety)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-013.md**](../ALR/ALR-013.md)  
- **Linked SRs:**  
  - ../SR/[**SR-PROP-001.md**](../SR/SR-PROP-001.md) – Propulsor design  
  - ../SR/[**SR-MOTOR-001.md**](../SR/SR-MOTOR-001.md) – Electric motor specs  
  - ../SR/[**SR-MOTORCTL-001.md**](../SR/SR-MOTORCTL-001.md) – Motor controller  
  - ../SR/[**SR-THRUSTMGMT-001.md**](../SR/SR-THRUSTMGMT-001.md) – Thrust management logic  
- **Related Requirements:**  
  - **RQ-10-01** (Fuel-cell primary power)  
  - **RQ-10-05** (Total installed power 15 MW)  
  - **RQ-20-04** (Acoustic signature -25 dB)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-PROP-001**](../../V_AND_V/cases/TEST-PROP-001.md) · ../../V_AND_V/cases/[**TEST-PROP-WT-001**](../../V_AND_V/cases/TEST-PROP-WT-001.md) · ../../V_AND_V/cases/[**TEST-PROP-GT-001**](../../V_AND_V/cases/TEST-PROP-GT-001.md) · ../../V_AND_V/cases/[**TEST-PROP-FT-001**](../../V_AND_V/cases/TEST-PROP-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-PROP-001.csv**](../RTM/RTM-PROP-001.csv)

---

## Notes
- **Distributed propulsion philosophy:** The 8-propulsor configuration balances efficiency, redundancy, and acoustic performance. Future studies may explore 6- or 10-propulsor variants.  
- **Boundary layer ingestion:** BLI is a key enabler for BWB efficiency gains but requires careful inlet design to manage distortion and maintain motor durability.  
- **Scalability:** The modular propulsor design allows for future power upgrades (e.g., 18–20 MW total) by adding more propulsors or increasing motor rating.
