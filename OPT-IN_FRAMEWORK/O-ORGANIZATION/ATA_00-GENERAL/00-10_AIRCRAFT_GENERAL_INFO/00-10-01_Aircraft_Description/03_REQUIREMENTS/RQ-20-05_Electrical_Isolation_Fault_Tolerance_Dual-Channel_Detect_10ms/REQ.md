# RQ-20-05 — Electrical Isolation Fault Tolerance (Dual-Channel Detect < 10 ms)

## Statement
The high-voltage DC (HVDC) electrical power system shall incorporate **dual-channel electrical isolation monitoring** with **fault detection response time < 10 milliseconds** to prevent electrical shock hazards, ensure personnel safety, and maintain system integrity per **DO-160G** environmental qualification standards.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Isolation Monitoring System Architecture**  
   - **Dual-channel redundancy:** Two independent isolation monitoring units (IMUs) per HVDC bus segment.  
   - **Monitoring range:** Continuous measurement of isolation resistance between HVDC bus (±270 VDC nominal, 540 VDC differential) and aircraft ground/structure.  
   - **Threshold detection:** Alert triggered if isolation resistance drops below **500 kΩ** (warning) or **100 kΩ** (fault).  
   - **Cross-channel validation:** Dual-channel agreement required before fault declaration; disagreement triggers sensor health check.

2. **Fault Detection Performance**  
   - **Detection time:** Isolation fault detected and reported to flight crew/maintenance system within **< 10 ms** of threshold crossing.  
   - **False alarm rate:** **< 1 false alarm per 10,000 flight hours** (high specificity to avoid nuisance alerts).  
   - **Fault localization:** System identifies faulted bus segment (e.g., fuel-cell output, motor controller input, battery interface) within **< 100 ms**.  
   - **Degraded mode operation:** Aircraft remains operational with single-channel isolation monitoring failure (fault tolerance).

3. **Safety Response and Fault Handling**  
   - **Crew alerting:** EICAS/ECAM alert (caution or warning level depending on fault severity) with fault location guidance.  
   - **Automatic protection (if required):** Severe isolation faults (< 10 kΩ) trigger automatic bus segment isolation via contactors within **< 50 ms** to prevent propagation.  
   - **Maintenance action:** Isolation faults logged in digital maintenance system per **ATA 45** (On-Board Maintenance Systems) for troubleshooting and repair.  
   - **Go/No-Go criteria:** Aircraft dispatch allowed with single isolation monitor failure (MEL); dual-channel failure or confirmed isolation fault < 100 kΩ prohibits dispatch.

4. **Environmental Qualification**  
   - **DO-160G compliance:** Isolation monitoring system qualified for aircraft environmental conditions (temperature, vibration, humidity, EMI, lightning, HIRF per DO-160G Category A/B).  
   - **HVDC bus voltage range:** Isolation monitoring functional across **400–650 VDC** operating range (±20% nominal).  
   - **EMI immunity:** System immune to EMI from motor controllers, inverters, and propulsor switching transients (conducted and radiated emissions per DO-160G).

5. **Personnel Safety**  
   - **Shock hazard prevention:** Isolation monitoring ensures **no > 10 mA leakage current** to aircraft structure during normal/fault conditions (below perceptible shock threshold).  
   - **Maintenance safety:** Ground servicing procedures require isolation verification before personnel access to HVDC components.  
   - **Warning labels:** High-voltage warning placards and interlock systems per **SAE ARP5412** (electrical installation practices).

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-ISOL-001**](../../V_AND_V/cases/TEST-ISOL-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-ISOL-GT-001**](../../V_AND_V/cases/TEST-ISOL-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-ISOL-FT-001**](../../V_AND_V/cases/TEST-ISOL-FT-001.md)

---

## Rationale
High-voltage electrical systems (540 VDC) present shock and fire hazards if isolation degrades. Dual-channel monitoring with fast detection (< 10 ms) ensures crew awareness and enables protective actions before hazards escalate. DO-160G qualification ensures system reliability across aircraft environmental extremes.

🔗 Electrical safety design: ../../DESIGN/system_design/[**HVDC_safety_architecture.md**](../../DESIGN/system_design/HVDC_safety_architecture.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **E2-24** Electrical Power (HVDC bus, isolation monitoring per **ATA 24**)  
  - **E3-39** Electrical/Electronic Panels (isolation monitoring hardware)  
  - **L1-22** EMS (fault handling logic, automatic protection)  
  - **I-31** Indicating/Recording (crew alerts, fault annunciation)  
  - **O-02** Operations (maintenance procedures, MEL)

- **Key interfaces:**  
  - HVDC bus → Isolation monitoring units (IMUs)  
  - IMUs → EMS controller (fault status, protective actions)  
  - IMUs → Flight deck displays (crew alerting)  
  - IMUs → Maintenance system (fault logging per **ATA 45**)

🔗 Decompositions:  
- Isolation monitor design → ../SR/[**SR-ISOL-MON-001.md**](../SR/SR-ISOL-MON-001.md)  
- Fault handling logic → ../SR/[**SR-EMS-FAULT-001.md**](../SR/SR-EMS-FAULT-001.md)  
- Crew procedures → ../SR/[**SR-CREW-ELEC-001.md**](../SR/SR-CREW-ELEC-001.md)

---

## Constraints & Interfaces
- **Measurement accuracy:** Isolation monitoring must distinguish between acceptable transient impedance changes (e.g., switching transients) and true isolation faults.  
- **EMI environment:** HVDC switching (motor controllers, converters) generates high-frequency EMI; isolation monitors must filter noise while maintaining fast detection.  
- **Redundancy cost:** Dual-channel monitoring adds weight and cost; trade-off justified by criticality of isolation fault detection.  
- **Maintenance complexity:** False alarms or sensor failures increase maintenance burden; system design prioritizes high reliability and low false alarm rate.

🔗 Interface references:  
- HVDC electrical: ../../INTERFACES/[**52_electrical_interfaces.md**](../../INTERFACES/52_electrical_interfaces.md)  
- Control/data: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- **Isolation degradation modes:** Gradual isolation degradation (e.g., insulation aging, moisture ingress) provides early warning before catastrophic failure.  
- **Crew response time:** Crew reacts to isolation alerts within **< 30 seconds** per standard operating procedures; automatic protection (if required) provides immediate response.  
- **Maintenance actions:** Isolation faults typically resolved by component replacement (e.g., damaged cable, faulty contactor); root cause analysis conducted per **ARP4761**.  
- **Regulatory acceptance:** FAA/EASA accept dual-channel isolation monitoring as sufficient for high-voltage aircraft electrical system safety.

🔗 Safety analysis: ../../ENGINEERING/analyses/safety/[**electrical_hazard_analysis.md**](../../ENGINEERING/analyses/safety/electrical_hazard_analysis.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Fault tree analysis (FTA) for isolation fault scenarios; safety assessment per **ARP4761**; EMI analysis for monitoring system immunity.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Component Testing:** Isolation monitor unit bench testing (accuracy, response time, EMI immunity per DO-160G).  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Ground Integration Testing:** Full HVDC system testing on iron bird with injected isolation faults; validation of detection time, crew alerting, automatic protection.  
  - Results: ../../V_AND_V/verification/results/[**electrical_integration_tests/**](../../V_AND_V/verification/results/electrical_integration_tests/)

- **Flight Testing:** In-flight isolation monitoring validation; environmental stress testing (temperature, vibration, EMI); crew procedure validation.  
  - Results: ../../V_AND_V/verification/results/[**flight_test_electrical_safety/**](../../V_AND_V/verification/results/flight_test_electrical_safety/)

**Acceptance evidence:** Dual-channel isolation monitoring functional; fault detection < 10 ms verified; false alarm rate < 1 per 10,000 hrs; DO-160G qualification complete; crew procedures validated.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-024.md**](../ALR-024.md) – Electrical system safety  
- **Electrical standards:** **DO-160G** (environmental qualification), **SAE ARP5412** (aircraft electrical installation practices)  
- **Safety:** **ARP4761** (safety assessment), **CS-25.1351** (electrical system safety)  
- **Software:** **DO-178C Level A** (isolation monitor software, EMS fault handling)  
- **Hardware:** **DO-254 Level A** (isolation monitor hardware)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-024.md**](../ALR-024.md)  
- **Linked SRs:**  
  - ../SR/[**SR-ISOL-MON-001.md**](../SR/SR-ISOL-MON-001.md) – Isolation monitor design  
  - ../SR/[**SR-EMS-FAULT-001.md**](../SR/SR-EMS-FAULT-001.md) – EMS fault handling  
  - ../SR/[**SR-CREW-ELEC-001.md**](../SR/SR-CREW-ELEC-001.md) – Crew procedures  
- **Related Requirements:**  
  - **RQ-10-05** (HVDC 540 VDC electrical architecture)  
  - **RQ-20-06** (Fire suppression — electrical faults can initiate fires)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-ISOL-001**](../../V_AND_V/cases/TEST-ISOL-001.md) · ../../V_AND_V/cases/[**TEST-ISOL-GT-001**](../../V_AND_V/cases/TEST-ISOL-GT-001.md) · ../../V_AND_V/cases/[**TEST-ISOL-FT-001**](../../V_AND_V/cases/TEST-ISOL-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-ISOL-001.csv**](../RTM/RTM-ISOL-001.csv)

---

## Notes
- **High-voltage safety culture:** Aircraft maintenance and flight operations require specialized training and procedures for 540 VDC systems (comparable to electric vehicle industry practices).  
- **Fast detection rationale:** < 10 ms detection time ensures fault awareness before potential arc flash or thermal runaway scenarios develop.  
- **Industry benchmarking:** Dual-channel isolation monitoring with < 10 ms detection is state-of-the-art for high-voltage electric propulsion aircraft and electric vehicles.
