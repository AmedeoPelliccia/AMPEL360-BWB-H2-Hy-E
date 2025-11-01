# RQ-20-06 — Fire Suppression (Autonomous Inerting & HALT Logic)

## Statement
The aircraft shall incorporate an **autonomous fire detection and suppression system** utilizing **automated inerting** and **HALT (Halon Automatic Logic Trigger)** control logic for critical fire zones including fuel-cell compartments, battery bays, propulsor nacelles, and cargo/cabin areas, ensuring rapid fire suppression per **ATA 26** (Fire Protection) and **CS-25.851** through **CS-25.869**.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Fire Detection System**  
   - **Dual-loop detection:** Redundant fire/smoke detectors in all designated fire zones per **CS-25.1203**.  
   - **Detection time:** Fire/smoke detected within **≤ 5 seconds** of ignition (validated via fire test).  
   - **False alarm rate:** **< 1 false alarm per 5,000 flight hours** per zone.  
   - **Detector types:** Optical smoke detectors (cargo/cabin), thermal detectors (engine/propulsor zones), ionization detectors (electrical bays).  
   - **Coverage:** All Class A, B, C, and D fire zones per **CS-25.1191** through **CS-25.1203**.

2. **Autonomous Inerting System**  
   - **Inerting agent:** Nitrogen (N₂) or CO₂ for electrical/battery fires; Halon alternatives (HFC-227ea, Novec 1230) for propulsor/fuel-cell zones.  
   - **Automatic discharge:** Fire detection in critical zones triggers automatic suppression agent discharge within **≤ 10 seconds** (no crew action required for first discharge).  
   - **Concentration targets:**  
     - Electrical/battery bays: O₂ concentration reduced to **< 12%** (below combustion threshold) within **30 seconds**.  
     - Propulsor/fuel-cell zones: Halon alternative concentration ≥ **5–6%** (per agent spec) within **10 seconds**.  
   - **Agent capacity:** Sufficient for **≥ 2 discharge cycles** per fire zone (initial knockdown + reserve for reflash).

3. **HALT (Halon Automatic Logic Trigger) Control Logic**  
   - **Automatic activation criteria:**  
     - Dual-loop fire detection confirmed (both channels agree).  
     - Fire zone temperature exceeds **300°C** (electrical/battery) or **500°C** (propulsor/fuel-cell).  
     - Smoke density exceeds **5% obscuration per meter** (cargo/cabin).  
   - **Manual override:** Flight crew can manually command suppression discharge via cockpit controls (override automatic logic if needed).  
   - **Discharge sequencing:** Staged discharge (initial knockdown + hold/reflash protection) per fire zone requirements.  
   - **Post-discharge monitoring:** Continuous temperature/smoke monitoring to detect reflash; automatic second discharge if reflash detected within **2 minutes**.

4. **Critical Fire Zones and Protection**  
   - **Fuel-cell compartments (ATA 28/24):** Autonomous N₂ inerting + Halon alternative; O₂ enrichment risk mitigated.  
   - **CO₂ battery bays (ATA 28/49):** Autonomous N₂ inerting; thermal runaway detection and suppression.  
   - **Propulsor nacelles (ATA 61/26):** Dual-loop detection + Halon alternative; engine fire bottle system.  
   - **SAF turbogenerator (ATA 49/26):** Dual-loop detection + Halon alternative per APU fire protection standards.  
   - **Cargo compartments (ATA 50/26):** Class C cargo fire suppression per **CS-25.857** (smoke detection + suppression).  
   - **Cabin (ATA 44/26):** Portable fire extinguishers + smoke detection; automatic suppression in lavatories per **CS-25.854**.  
   - **Electrical/avionics bays (ATA 24/39/26):** N₂ inerting or Halon alternative; HVDC arc fault protection coordination.

5. **Safety and Certification**  
   - **Fire test validation:** Flame extinction within **30 seconds** of suppression discharge per **CS-25.865**.  
   - **Agent toxicity:** Halon alternatives meet **CS-25.851(a)** toxicity limits (safe for crew/passengers during discharge).  
   - **System reliability:** Fire detection/suppression system reliability ≥ **10⁻⁵ failures per flight hour** (catastrophic hazard per **ARP4761**).  
   - **Maintenance monitoring:** Fire suppression agent quantity and system health monitored per **ATA 45** (On-Board Maintenance Systems).

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-FIRE-001**](../../V_AND_V/cases/TEST-FIRE-001.md)  
- Fire test: ../../V_AND_V/cases/[**TEST-FIRE-FT-001**](../../V_AND_V/cases/TEST-FIRE-FT-001.md)  
- Integration test: ../../V_AND_V/cases/[**TEST-FIRE-INT-001**](../../V_AND_V/cases/TEST-FIRE-INT-001.md)

---

## Rationale
Hydrogen fuel-cells, high-voltage batteries, and electric propulsion systems introduce novel fire hazards requiring advanced autonomous suppression. HALT logic ensures rapid, reliable fire knockdown without reliance on crew response time. Inerting is particularly effective for enclosed electrical/battery fires where traditional Halon may be less effective.

🔗 Fire safety design: ../../DESIGN/system_design/[**fire_protection_architecture.md**](../../DESIGN/system_design/fire_protection_architecture.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **E1-26** Fire Protection (fire detection/suppression systems per **ATA 26**)  
  - **C2-28** Fuel Systems (fuel-cell and H₂ tank fire protection)  
  - **E2-24/49** Electrical/Auxiliary Power (battery and turbogenerator fire protection)  
  - **P-61** Propulsion (propulsor nacelle fire protection)  
  - **L1-22** EMS (HALT logic, automatic fire response)  
  - **O-02** Operations (fire response procedures, crew training)

- **Key interfaces:**  
  - Fire detectors → HALT logic controller (dual-loop confirmation)  
  - HALT controller → Suppression agent discharge valves (automatic activation)  
  - HALT controller → Flight deck (crew alerting, manual override controls)  
  - HALT controller → Maintenance system (agent quantity monitoring, fault logging)

🔗 Decompositions:  
- Fire detection system → ../SR/[**SR-FIRE-DET-001.md**](../SR/SR-FIRE-DET-001.md)  
- HALT logic design → ../SR/[**SR-HALT-001.md**](../SR/SR-HALT-001.md)  
- Suppression agent system → ../SR/[**SR-FIRE-SUP-001.md**](../SR/SR-FIRE-SUP-001.md)

---

## Constraints & Interfaces
- **Agent weight:** Fire suppression agents (Halon alternatives, N₂) add **≈ 200–300 kg** system weight; trade-off between safety and weight.  
- **Agent environmental impact:** Halon alternatives (HFCs) have global warming potential; industry transitioning to lower-GWP agents (e.g., Novec 1230, CO₂, N₂).  
- **Crew procedures:** Automatic suppression reduces crew workload but requires crew training for manual override and post-fire assessment.  
- **Maintenance logistics:** Suppression agent refilling requires ground support equipment and trained personnel; agent availability at all operational airports.

🔗 Interface references:  
- Fire protection system: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Control/data: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- **Fire hazard probability:** Fire risk assessment (FHA/PSSA) identifies fuel-cell, battery, and propulsor zones as highest fire risk areas requiring autonomous suppression.  
- **Agent effectiveness:** N₂ inerting effective for Class C electrical fires (smothering); Halon alternatives effective for Class B flammable liquid fires (chemical suppression).  
- **Reflash risk:** H₂ fuel-cell fires may reflash after initial suppression; staged discharge and continuous monitoring required.  
- **Regulatory acceptance:** FAA/EASA accept autonomous fire suppression (HALT logic) for novel propulsion systems with appropriate safety case per **ARP4761**.

🔗 Fire hazard analysis: ../../ENGINEERING/analyses/safety/[**fire_hazard_assessment.md**](../../ENGINEERING/analyses/safety/fire_hazard_assessment.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Fire hazard analysis (FHA, FMEA, FTA); fire zone identification per **CS-25.1191**; suppression effectiveness modeling.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Component Testing:** Fire detector response time testing; suppression agent discharge performance (flow rate, concentration, dispersion).  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Fire Testing:** Full-scale fire tests per **CS-25.865** (flame extinction within 30 s); reflash detection and suppression; toxicity validation.  
  - Results: ../../V_AND_V/verification/results/[**fire_suppression_tests/**](../../V_AND_V/verification/results/fire_suppression_tests/)

- **Integration Testing:** HALT logic validation (automatic discharge triggers, manual override, fault tolerance); iron bird testing with simulated fire scenarios.  
  - Results: ../../V_AND_V/verification/results/[**fire_system_integration_tests/**](../../V_AND_V/verification/results/fire_system_integration_tests/)

- **Flight Testing:** Smoke detector functional checks; fire bottle discharge simulation (non-destructive); crew procedure validation.  
  - Results: ../../V_AND_V/verification/results/[**flight_test_fire_system/**](../../V_AND_V/verification/results/flight_test_fire_system/)

**Acceptance evidence:** Fire detection < 5 s; automatic suppression discharge < 10 s; flame extinction < 30 s; false alarm rate < target; HALT logic functional; crew procedures validated; CS-25 fire protection compliance achieved.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-025.md**](../ALR-025.md) – Fire protection  
- **Fire protection standards:** **CS-25.851** through **CS-25.869** (fire protection), **ATA 26** (Fire Protection systems)  
- **Detection:** **CS-25.1203** (fire detection), **CS-25.1207** (fire detectors—cargo compartments)  
- **Suppression:** **CS-25.1195** (fire extinguishing systems), **CS-25.865** (fire test procedures)  
- **Cargo:** **CS-25.857** (Class C cargo compartments)  
- **Halon alternatives:** **ICAO Annex 16 Vol III** (environmental protection, ozone depletion)  
- **Safety:** **ARP4761** (safety assessment), **ARP4754A** (development assurance)  
- **Software:** **DO-178C Level A** (HALT logic software)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-025.md**](../ALR-025.md)  
- **Linked SRs:**  
  - ../SR/[**SR-FIRE-DET-001.md**](../SR/SR-FIRE-DET-001.md) – Fire detection system  
  - ../SR/[**SR-HALT-001.md**](../SR/SR-HALT-001.md) – HALT logic design  
  - ../SR/[**SR-FIRE-SUP-001.md**](../SR/SR-FIRE-SUP-001.md) – Suppression agent system  
- **Related Requirements:**  
  - **RQ-10-01** (Fuel-cell fire protection)  
  - **RQ-10-02** (CO₂ battery thermal runaway/fire risk)  
  - **RQ-10-03** (SAF turbogenerator fire protection)  
  - **RQ-20-05** (Electrical isolation faults can initiate fires)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-FIRE-001**](../../V_AND_V/cases/TEST-FIRE-001.md) · ../../V_AND_V/cases/[**TEST-FIRE-FT-001**](../../V_AND_V/cases/TEST-FIRE-FT-001.md) · ../../V_AND_V/cases/[**TEST-FIRE-INT-001**](../../V_AND_V/cases/TEST-FIRE-INT-001.md)  
- **RTM rows:** ../RTM/[**RTM-FIRE-001.csv**](../RTM/RTM-FIRE-001.csv)

---

## Notes
- **Novel fire hazards:** H₂ fuel-cells and high-voltage batteries introduce fire characteristics different from conventional jet fuel fires; specialized suppression strategies required.  
- **H₂ fire characteristics:** Hydrogen burns with nearly invisible flame; thermal imaging or UV flame detectors required for reliable detection.  
- **HALT logic precedent:** Autonomous fire suppression with HALT-type logic used in military aircraft and some commercial cargo aircraft; adaptation for H₂/electric propulsion is novel.  
- **Agent transition:** Aviation industry transitioning away from Halon (ozone depletion) to alternatives (HFC-227ea, Novec 1230, N₂, CO₂); aircraft design anticipates future low-GWP agent availability.
