# RQ-10-02 — Hybrid Storage (Closed-loop CO₂ Battery)

## Statement
The aircraft shall incorporate a **closed-loop CO₂ battery system** as hybrid storage for **peak load buffering** and **transient power management**, integrated with the hydrogen PEM fuel-cell primary source and HVDC electrical distribution, to support **±20% transient loads** while maintaining **zero in-flight venting** of CO₂ and complying with all safety, electrical, and thermal requirements.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
The CO₂ battery system is accepted when **all** of the following are satisfied:

1. **System Capacity & Performance**  
   - Energy storage capacity ≥ **500 kWh** with discharge capability ≥ **5 MW** per [RQ-10-02.1](#8-requirements-traceability-rq-10-02).  
   - Closed-loop operation with **no venting** of CO₂ during normal and emergency operations per [RQ-10-02.2](#8-requirements-traceability-rq-10-02).  
   - HVDC interface at **540 VDC** with response time < **100 ms** to load transients per [RQ-10-02.3](#8-requirements-traceability-rq-10-02).  
   - State-of-Charge (SOC) control maintained within **20–80%** band per [RQ-10-02.4](#8-requirements-traceability-rq-10-02).  
   - Fault tolerance to **≥10% cell failure** without system-level degradation per [RQ-10-02.5](#8-requirements-traceability-rq-10-02).

2. **Integration & Safety**  
   - Thermal loop simulation validates closed-loop CO₂ operation across mission envelope.  
   - System integration tests confirm HVDC interface compliance and response characteristics.  
   - FHA/PSSA verification demonstrates fault tolerance and safety compliance.  
   - EMS simulation confirms SOC control algorithm effectiveness.

3. **Evidence Set**  
   - **Ground test** TEST-CO2BAT-GT-001 validates capacity and discharge performance.  
   - **Analysis** and thermal loop simulation verify closed-loop operation.  
   - **System Integration Test** confirms HVDC interface and response time.  
   - **Flight test** and EMS simulation validate SOC control strategy.  
   - **FHA/PSSA** verification confirms fault tolerance design.

🔗 Test artefacts:  
- Ground Test: ../../V_AND_V/cases/[**TEST-CO2BAT-GT-001**](../../V_AND_V/cases/TEST-CO2BAT-GT-001.md)  
- Analysis: ../../V_AND_V/cases/[**TEST-CO2BAT-AN-001**](../../V_AND_V/cases/TEST-CO2BAT-AN-001.md)  
- System Integration: ../../V_AND_V/cases/[**TEST-CO2BAT-SI-001**](../../V_AND_V/cases/TEST-CO2BAT-SI-001.md)  
- Flight Test: ../../V_AND_V/cases/[**TEST-CO2BAT-FT-001**](../../V_AND_V/cases/TEST-CO2BAT-FT-001.md)  
- Safety: ../../SAFETY/FHA/[**FHA-CO2BAT-001**](../../SAFETY/FHA/FHA-CO2BAT-001.md)

---

## Rationale
The closed-loop CO₂ battery provides essential peak load buffering for the hybrid propulsion system, enabling efficient operation of the hydrogen PEM fuel cells at optimal efficiency points while accommodating transient power demands from the electric propulsors. The closed-loop design eliminates in-flight venting, supporting the zero-emission mission profile.

🔗 Background analysis: ../../DESIGN/system_design/[**co2_battery_rationale.md**](../../DESIGN/system_design/co2_battery_rationale.md)

---

## Scope & Allocation
- **Primary domains:** E2-24 (HVDC electrical), C2-28 (H₂/CO₂ thermal systems), P-49 (Battery/Energy storage), L1-22 (Energy Management System).  
- **Aircraft-level KPI:** Peak power capability, transient response, zero-emission operation.

🔗 Decompositions:  
- Battery thermal management → ../SR/[**SR-THERM-001.md**](../SR/SR-THERM-001.md)  
- EMS power split control → ../SR/[**SR-CTRL-007.md**](../SR/SR-CTRL-007.md)  
- HVDC bus stability → ../SR/[**SR-ELEC-003.md**](../SR/SR-ELEC-003.md)

---

## Constraints & Interfaces
- **Thermal constraints:** CO₂ loop must operate within validated temperature/pressure envelope without exceeding structural limits.  
- **Electrical isolation:** HVDC interface must maintain isolation per DO-160G with dual-channel fault detection.  
- **Safety margins:** Fault tolerance must not compromise adjacent systems or create cascading failures.

🔗 Interface refs:  
- Electrical/HVDC: ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- Thermal/CO₂: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Data/EMS: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- CO₂ battery operates in conjunction with hydrogen PEM fuel cells as primary energy source.  
- SAF turbogenerator is **OFF** during zero-emission operation; CO₂ battery provides transient buffering.  
- Thermal management system (TMS) maintains CO₂ within operating envelope across mission phases.

🔗 Config evidence: ../../ENGINEERING/analyses/thermal/[**co2_thermal_analysis.md**](../../ENGINEERING/analyses/thermal/co2_thermal_analysis.md)

---

## 8. Requirements Traceability (RQ-10-02)

| RQ ID | Requirement Summary | Design Reference | Verification Method |
|-------|---------------------|------------------|---------------------|
| RQ-10-02.1 | ≥500 kWh capacity, ≥5 MW discharge | §3.1 Design Parameters | Ground test TEST-CO2BAT-GT-001 |
| RQ-10-02.2 | Closed-loop CO₂ operation, no venting | §2.1 System Composition / §3.2 Subsystem Breakdown | Analysis, thermal loop simulation |
| RQ-10-02.3 | HVDC 540 VDC interface, <100 ms response | §4.1 Power Interfaces / §4.2 Wiring Diagram | System Integration Test |
| RQ-10-02.4 | SOC control 20–80% | §3.2 Control Logic / §6 Future Work | Flight test, EMS simulation |
| RQ-10-02.5 | Fault tolerance 10% cell failure | §5 Safety and Compliance | FHA/PSSA verification |

---

## Verification (Method & Artefacts)
- **Analysis:** Thermal loop modeling, power flow analysis, EMS simulation.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)
- **Ground Test:** Capacity and discharge performance testing per TEST-CO2BAT-GT-001.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)
- **System Integration Test:** HVDC interface validation, response time characterization.  
  - Results: ../../V_AND_V/verification/results/[**co2_battery_integration_revA/**](../../V_AND_V/verification/results/co2_battery_integration_revA/)
- **Flight Test (as applicable):** SOC control validation, transient response demonstration.  
- **Safety Verification:** FHA/PSSA analysis for fault tolerance and failure modes.  
  - Safety docs: ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

**Acceptance evidence:** All sub-requirements (RQ-10-02.1 through RQ-10-02.5) verified with test correlation within tolerance.

🔗 Coverage & Trace:  
- Coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Req↔Test: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-010.md**](../ALR/ALR-010.md)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md) → ../../SAFETY/SSA/[**SSA_report.md**](../../SAFETY/SSA/SSA_report.md)  
- **Standards mapping:**  
  - HVDC electrical: DO-160G  
  - Energy storage: ATA 24 / ATA 28  
  - Battery systems: ATA 49  
  - System safety: ARP4761 / ARP4754A  
- **Compliance matrix:** ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-010.md**](../ALR/ALR-010.md)  
- **Linked SRs:**  
  - ../SR/[**SR-THERM-001.md**](../SR/SR-THERM-001.md) — Battery thermal management  
  - ../SR/[**SR-CTRL-007.md**](../SR/SR-CTRL-007.md) — EMS power split control  
  - ../SR/[**SR-ELEC-003.md**](../SR/SR-ELEC-003.md) — HVDC bus stability  
- **V&V Cross-refs:**  
  - ../../V_AND_V/cases/[**TEST-CO2BAT-GT-001**](../../V_AND_V/cases/TEST-CO2BAT-GT-001.md)  
  - ../../V_AND_V/cases/[**TEST-CO2BAT-AN-001**](../../V_AND_V/cases/TEST-CO2BAT-AN-001.md)  
  - ../../V_AND_V/cases/[**TEST-CO2BAT-SI-001**](../../V_AND_V/cases/TEST-CO2BAT-SI-001.md)  
  - ../../V_AND_V/cases/[**TEST-CO2BAT-FT-001**](../../V_AND_V/cases/TEST-CO2BAT-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-CO2BAT-001.csv**](../RTM/RTM-CO2BAT-001.csv) · ../RTM/[**RTM-CO2BAT-002.csv**](../RTM/RTM-CO2BAT-002.csv)

---

## Notes
The CO₂ battery closed-loop design is a critical enabler for zero-emission operation. Any design changes that affect venting, thermal management, or fault tolerance must be reviewed through the configuration control process and re-verified per this requirement specification.

Future work includes optimization of SOC control algorithms (§6) and advanced fault prediction/mitigation strategies to improve operational efficiency and maintainability.
