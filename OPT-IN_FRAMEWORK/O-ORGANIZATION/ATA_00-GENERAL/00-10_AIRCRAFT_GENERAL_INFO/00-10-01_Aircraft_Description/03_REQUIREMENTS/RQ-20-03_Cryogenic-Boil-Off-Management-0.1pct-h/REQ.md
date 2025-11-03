# RQ-20-03 — Cryogenic Boil-Off Management (≤ 0.1%/h)

## Statement
The liquid hydrogen (LH₂) storage system shall maintain a **boil-off rate ≤ 0.1% per hour** under nominal ground and flight conditions to minimize hydrogen losses, ensure mission fuel availability, and maintain cryogenic system safety per **ATA 28-30** (fuel system—cryogenic management).

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Boil-Off Rate Targets**  
   - **Ground operations (ambient +15°C to +40°C):** ≤ **0.1%/h** hydrogen mass loss rate during typical turnaround (30–60 min).  
   - **Flight operations (cruise at FL350, -54°C ambient):** ≤ **0.05%/h** due to reduced external heat loads.  
   - **Extended ground hold (hot day, +40°C):** ≤ **0.15%/h** with active cooling support (if required).  
   - **Acceptance:** Measured boil-off rate verified via tank mass measurement and vent flow monitoring over ≥ **4-hour test periods**.

2. **Thermal Insulation Performance**  
   - **Tank insulation:** Multi-layer vacuum insulation (MLVI) with effective thermal conductivity ≤ **0.002 W/(m·K)**.  
   - **Heat leak:** Total heat ingress to LH₂ tank ≤ **50 W per 1,000 kg H₂ capacity** at design conditions.  
   - **Insulation integrity:** Vacuum pressure maintained at ≤ **10⁻⁴ mbar** over operational life; periodic leak checks per maintenance schedule.  
   - **Penetration sealing:** All tank penetrations (fill/vent ports, instrumentation feedthroughs) thermally optimized to minimize heat bridges.

3. **Pressure Management and Venting**  
   - **Tank operating pressure:** **2–5 bar absolute** (nominal); pressure relief valve set to **≤ 8 bar** (MAWP).  
   - **Vent system:** Controlled venting to atmosphere via elevated discharge (≥ **5 m** above fuselage) to ensure safe hydrogen dispersion.  
   - **Vent flow monitoring:** Real-time measurement of vent mass flow rate for boil-off rate calculation and system health monitoring.  
   - **Ground venting:** Ground support equipment available for controlled depressurization and H₂ recovery (if applicable).

4. **Active Cooling (Optional/Contingency)**  
   - **Cryocooler integration (if installed):** Active cryogenic cooling system capable of reducing boil-off to **≤ 0.05%/h** during extended ground holds.  
   - **Power requirement:** Cryocooler power draw ≤ **5 kW** from APU or ground power.  
   - **Activation criteria:** Automatic activation if ground hold exceeds **2 hours** and ambient temperature > **+35°C**.

5. **Mission Fuel Margin**  
   - **Fuel planning:** Boil-off losses accounted for in mission fuel calculations; **≥ 3%** mission fuel margin includes expected boil-off during ground and flight operations.  
   - **Operational impact:** Boil-off rate ≤ 0.1%/h ensures **≤ 1% fuel loss** during typical **3-hour turnaround + 5-hour flight** = **0.8% total boil-off**.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-CRYO-001**](../../V_AND_V/cases/TEST-CRYO-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-CRYO-GT-001**](../../V_AND_V/cases/TEST-CRYO-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-CRYO-FT-001**](../../V_AND_V/cases/TEST-CRYO-FT-001.md)

---

## Rationale
Minimizing boil-off is critical for fuel efficiency, operational economics, and mission reliability. Target ≤ 0.1%/h is achievable with state-of-the-art vacuum insulation and represents a practical balance between insulation complexity/weight and fuel losses. Lower boil-off reduces hydrogen venting (safety) and improves range predictability.

🔗 Cryogenic design basis: ../../04_DESIGN/system_design/[**cryogenic_tank_design.md**](../../04_DESIGN/system_design/cryogenic_tank_design.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **C2-28** Fuel Systems (LH₂ tanks, insulation, vent system per **ATA 28-10**, **ATA 28-30**)  
  - **E1-21** Environmental Control (potential cryocooler integration with ECS)  
  - **E1-30** Ice and Rain Protection (thermal management, anti-ice coordination)  
  - **L1-22** EMS (fuel quantity monitoring, boil-off compensation in fuel planning)  
  - **O-01** Maintenance Policy (insulation inspection, vacuum integrity checks)

- **Key interfaces:**  
  - LH₂ tank → Insulation system (MLVI)  
  - Tank pressure sensors → Vent system control logic  
  - Vent system → Overboard discharge (safe dispersion)  
  - Fuel quantity monitoring → Flight management system (fuel remaining calculations)

🔗 Decompositions:  
- Tank insulation design → ../SR/[**SR-TANK-INS-001.md**](../SR/SR-TANK-INS-001.md)  
- Vent system design → ../SR/[**SR-VENT-001.md**](../SR/SR-VENT-001.md)  
- Boil-off monitoring → ../SR/[**SR-FUEL-MON-001.md**](../SR/SR-FUEL-MON-001.md)

---

## Constraints & Interfaces
- **Weight penalty:** High-performance insulation (MLVI) adds **≈ 15–20%** to tank structural weight; trade-off between insulation thickness and fuel capacity.  
- **Volume constraint:** Insulation thickness (**≈ 50–100 mm** MLVI) reduces usable fuel volume; tank sizing accounts for insulation envelope.  
- **Maintenance access:** Vacuum insulation requires periodic integrity checks (vacuum leak detection); damaged insulation panels must be replaceable without complete tank removal.  
- **Safety:** Hydrogen venting must not accumulate in confined spaces or near ignition sources; vent discharge location critical per **RQ-20-02**.

🔗 Interface references:  
- Cryogenic/mechanical: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Fuel monitoring/data: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- **Ambient conditions:** Boil-off analysis based on **ISA ground conditions (+15°C to +40°C)** and **ISA flight conditions (-54°C at FL350)**.  
- **Insulation degradation:** Vacuum insulation performance degrades by **< 10%** over **20-year aircraft lifetime** with proper maintenance.  
- **Venting losses:** All boil-off gas vented to atmosphere (no onboard re-liquefaction or utilization assumed in baseline design).  
- **Operational profile:** Typical turnaround **≤ 1 hour**; extended ground holds (> 2 hours) are infrequent exceptions.

🔗 Supporting analysis: ../../ENGINEERING/analyses/thermal/[**boiloff_thermal_analysis.md**](../../ENGINEERING/analyses/thermal/boiloff_thermal_analysis.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Thermal modeling of LH₂ tank and insulation system; heat leak calculation; boil-off rate prediction across operational envelope.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Component Testing:** MLVI panel thermal performance testing; vacuum integrity and long-term stability validation.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Ground Testing:** Full-scale tank boil-off testing under controlled ambient conditions (hot soak, cold soak, cyclic thermal); vent flow measurement.  
  - Results: ../../V_AND_V/verification/results/[**cryogenic_boiloff_tests/**](../../V_AND_V/verification/results/cryogenic_boiloff_tests/)

- **Flight Testing:** In-flight boil-off monitoring across mission profile; correlation with predictions; fuel quantity accuracy validation.  
  - Results: ../../V_AND_V/verification/results/[**flight_test_cryogenic/**](../../V_AND_V/verification/results/flight_test_cryogenic/)

**Acceptance evidence:** Measured boil-off rate ≤ 0.1%/h (ground) and ≤ 0.05%/h (flight); thermal models correlate within ±10%; fuel quantity predictions accurate within ±2%.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-022.md**](../ALR/ALR-022.md) – Cryogenic fuel system  
- **Cryogenic standards:** **ISO 21013** (cryogenic vessels), **EN 1473** (LH₂/LNG installations)  
- **Fuel system:** **CS-25.951** through **CS-25.979** (fuel system design and venting)  
- **Hydrogen safety:** **EASA Special Condition for Hydrogen**, **SAE ARP8677**  
- **Thermal:** **ATA 28-30** (fuel system—cryogenic), **ATA 30** (ice/thermal protection)  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) → ../../SAFETY/PSSA/[**PSSA_report.md**](../../SAFETY/PSSA/PSSA_report.md)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-022.md**](../ALR/ALR-022.md)  
- **Linked SRs:**  
  - ../SR/[**SR-TANK-INS-001.md**](../SR/SR-TANK-INS-001.md) – Tank insulation design  
  - ../SR/[**SR-VENT-001.md**](../SR/SR-VENT-001.md) – Vent system design  
  - ../SR/[**SR-FUEL-MON-001.md**](../SR/SR-FUEL-MON-001.md) – Fuel quantity monitoring  
- **Related Requirements:**  
  - **RQ-10-01** (LH₂ fuel system)  
  - **RQ-20-02** (Ground refueling and H₂ handling safety)  
  - **RQ-00-02** (Design range 3,500 km — affected by boil-off fuel losses)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-CRYO-001**](../../V_AND_V/cases/TEST-CRYO-001.md) · ../../V_AND_V/cases/[**TEST-CRYO-GT-001**](../../V_AND_V/cases/TEST-CRYO-GT-001.md) · ../../V_AND_V/cases/[**TEST-CRYO-FT-001**](../../V_AND_V/cases/TEST-CRYO-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-CRYO-001.csv**](../RTM/RTM-CRYO-001.csv)

---

## Notes
- **Technology benchmark:** 0.1%/h boil-off rate is consistent with advanced LH₂ storage systems (e.g., aerospace, space launch ground support). Target is aggressive but achievable with careful thermal design.  
- **Extended ground operations:** For airports with frequent long ground holds (e.g., de-icing delays), optional active cryocooler system may be cost-effective to reduce fuel losses.  
- **Future improvements:** Advances in aerogel or foam insulation may reduce insulation weight while maintaining boil-off performance in future aircraft variants.
