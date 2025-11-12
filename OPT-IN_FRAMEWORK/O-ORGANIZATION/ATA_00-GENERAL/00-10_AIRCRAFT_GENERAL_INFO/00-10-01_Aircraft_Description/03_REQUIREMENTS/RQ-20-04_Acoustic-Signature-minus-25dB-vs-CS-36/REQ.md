# RQ-20-04 — Acoustic Signature (-25 dB vs. CS-36)

## Statement
The aircraft shall achieve an **acoustic signature 25 dB below ICAO Annex 16 Volume I Chapter 4 (CS-36) noise limits** at all three certification points (takeoff, sideline, approach) through the combination of distributed open-fan electric propulsion, blended-wing-body airframe shielding, and advanced noise reduction technologies.

- 🔗 Related docs: [VERIF.md](./VERIF.md) · [TRACE.csv](./TRACE.csv) · [CHANGES.md](./CHANGES.md) · [EVIDENCE/](./EVIDENCE/)

---

## Acceptance Criteria
1. **Noise Certification Targets**  
   - **Takeoff (lateral measurement, 6.5 km from brake release):** ≤ **65 EPNdB** (CS-36 Ch 4 limit ≈ 90 EPNdB for this class; target = -25 dB).  
   - **Sideline (lateral measurement, 450 m from runway centerline):** ≤ **70 EPNdB** (CS-36 Ch 4 limit ≈ 95 EPNdB; target = -25 dB).  
   - **Approach (landing configuration, 2,000 m from threshold):** ≤ **73 EPNdB** (CS-36 Ch 4 limit ≈ 98 EPNdB; target = -25 dB).  
   - **Cumulative margin:** **≥ 25 EPNdB cumulative** below Chapter 4 limits (sum of margins at all three points).

2. **Noise Source Reduction Technologies**  
   - **Open-fan propulsors:** Low tip speed design (**tip Mach ≤ 0.7** at takeoff power) to minimize blade passage frequency (BPF) noise.  
   - **Blade count and pitch:** Optimized for distributed thrust and noise reduction (e.g., **8–12 blades per propulsor**, variable pitch for phase-of-flight optimization).  
   - **Electric motor drive:** Eliminates gearbox noise and combustor noise (vs. turbofan); enables precise RPM control for acoustic optimization.  
   - **Distributed propulsion:** 8× smaller propulsors produce lower individual noise signatures than 2× large turbofans; constructive/destructive interference managed via phasing.

3. **Airframe Shielding and Installation Effects**  
   - **BWB configuration:** Propulsors mounted on aft fuselage upper surface, shielded from ground observers by airframe.  
   - **Shielding effectiveness:** **≥ 10 dB** ground noise reduction due to BWB body shielding at approach and sideline conditions.  
   - **Installation noise:** Propulsor-airframe interaction noise (e.g., pylon-wake interaction) minimized via aeroacoustic design and CFD optimization.

4. **Operational Noise Management**  
   - **Continuous descent approach (CDA):** Flight procedures optimized for low-noise approaches (idle/low power settings, high glide slopes where possible).  
   - **Power management:** EMS reduces propulsor power during noise-sensitive flight phases (e.g., approach configuration) while maintaining flight path stability.  
   - **Noise abatement procedures:** Aircraft capable of steep approach (≥ **3.5° glide slope**) and displaced thrust reduction to minimize community noise exposure.

5. **Acoustic Modeling and Validation**  
   - **Prediction models:** Acoustic models validated via wind tunnel testing (scaled models) and full-scale ground tests.  
   - **Model uncertainty:** Noise predictions correlate with measurements within **±2 EPNdB** at all certification points.  
   - **Certification testing:** FAA/EASA flyover noise measurements per **ICAO Annex 16 Vol I** procedures.

🔗 Test artefacts:  
- Analysis: ../../V_AND_V/cases/[**TEST-ACOU-001**](../../V_AND_V/cases/TEST-ACOU-001.md)  
- Wind tunnel: ../../V_AND_V/cases/[**TEST-ACOU-WT-001**](../../V_AND_V/cases/TEST-ACOU-WT-001.md)  
- Ground test: ../../V_AND_V/cases/[**TEST-ACOU-GT-001**](../../V_AND_V/cases/TEST-ACOU-GT-001.md)  
- Flight test: ../../V_AND_V/cases/[**TEST-ACOU-FT-001**](../../V_AND_V/cases/TEST-ACOU-FT-001.md)

---

## Rationale
The -25 dB target represents a transformative reduction in aircraft noise, enabling operations at noise-restricted airports and supporting community acceptance of aviation growth. Distributed electric propulsion + BWB shielding are key enablers. Achieving this target differentiates the aircraft for urban/regional operations.

🔗 Acoustic design basis: ../../04_DESIGN/system_design/[**noise_reduction_strategy.md**](../../04_DESIGN/system_design/noise_reduction_strategy.md)

---

## Scope & Allocation
- **Primary domains:**  
  - **P-61** Propulsion (open-fan acoustic design per **ATA 61**)  
  - **A2** Aerodynamics (BWB shielding, installation aeroacoustics)  
  - **L1-27** Flight Controls (noise abatement procedures, approach profiles)  
  - **L1-22** EMS (power management for noise reduction)  
  - **O-18** Vibration and Noise Analysis (acoustic modeling per **ATA 18**)

- **Key interfaces:**  
  - Propulsor blade design → Acoustic signature (BPF, broadband)  
  - Propulsor installation (location, pylon geometry) → Airframe shielding effectiveness  
  - EMS power dispatch → Propulsor RPM/power → Noise levels  
  - Flight procedures (approach angle, power settings) → Community noise exposure

🔗 Decompositions:  
- Propulsor acoustic design → ../SR/[**SR-ACOU-PROP-001.md**](../SR/SR-ACOU-PROP-001.md)  
- BWB shielding analysis → ../SR/[**SR-ACOU-SHIELD-001.md**](../SR/SR-ACOU-SHIELD-001.md)  
- Noise abatement procedures → ../SR/[**SR-ACOU-OPS-001.md**](../SR/SR-ACOU-OPS-001.md)

---

## Constraints & Interfaces
- **Propulsor efficiency trade-off:** Low tip speed (acoustic benefit) may reduce propulsive efficiency; design optimizes both objectives.  
- **Airframe shielding dependency:** Shielding effectiveness varies with observer angle and flight phase; full benefit realized at approach and sideline, less at takeoff overhead.  
- **Weight penalty:** Acoustic treatments (e.g., nacelle liners, blade geometry complexity) add weight; net benefit must justify cost.  
- **Certification uncertainty:** CS-36 Chapter 4 limits are based on turbofan benchmarks; certification authorities may apply scrutiny to novel configurations (BWB + distributed propulsion).

🔗 Interface references:  
- Propulsor/airframe integration: ../../INTERFACES/[**51_mechanical_interfaces.md**](../../INTERFACES/51_mechanical_interfaces.md)  
- Flight control/EMS: ../../INTERFACES/[**53_data_interfaces.md**](../../INTERFACES/53_data_interfaces.md)

---

## Assumptions
- **Baseline comparison:** CS-36 Chapter 4 limits for **150-seat, twin-turbofan aircraft** (MTOW ≈ 80–90 tonnes); limits scale with aircraft weight.  
- **Atmospheric conditions:** Noise measurements per **ICAO Annex 16 Vol I** (standard day, no wind, specified flight profiles).  
- **Technology maturity:** Open-fan acoustic design validated via scaled wind tunnel tests and computational aeroacoustics (CAA); full-scale validation required during flight test.  
- **Community noise modeling:** Airport-specific noise contour modeling (e.g., INM, AEDT) demonstrates community benefit of -25 dB reduction.

🔗 Supporting analysis: ../../ENGINEERING/analyses/acoustic/[**noise_prediction_model_BWB_RevA.md**](../../ENGINEERING/analyses/acoustic/noise_prediction_model_BWB_RevA.md)

---

## Verification (Method & Artefacts)
- **Analysis:** Computational aeroacoustics (CAA) modeling; propulsor source noise prediction; airframe shielding analysis; noise contour modeling.  
  - Plan: ../../V_AND_V/verification/plans/[**SVCP_verification_plan.md**](../../V_AND_V/verification/plans/SVCP_verification_plan.md)

- **Wind Tunnel Testing:** Scaled acoustic testing (1/10 to 1/4 scale models) with microphone arrays; validation of shielding and propulsor noise sources.  
  - Procedures: ../../V_AND_V/verification/procedures/[**74_test_procedures.md**](../../V_AND_V/verification/procedures/74_test_procedures.md)

- **Ground Testing:** Full-scale propulsor acoustic testing on outdoor test stand; far-field microphone measurements.  
  - Results: ../../V_AND_V/verification/results/[**acoustic_ground_tests/**](../../V_AND_V/verification/results/acoustic_ground_tests/)

- **Flight Testing:** Noise certification flyovers per **ICAO Annex 16 Vol I** procedures; microphone arrays at certification points; correlation with predictions.  
  - Results: ../../V_AND_V/verification/results/[**flight_test_noise_certification/**](../../V_AND_V/verification/results/flight_test_noise_certification/)

**Acceptance evidence:** Measured noise levels at takeoff, sideline, and approach ≤ target EPNdB levels; cumulative margin ≥ 25 EPNdB below CS-36 Chapter 4; FAA/EASA noise certification achieved.

🔗 Coverage:  
- Test coverage: ../../V_AND_V/coverage/[**7J_code_coverage.csv**](../../V_AND_V/coverage/7J_code_coverage.csv)  
- Traceability: ../../V_AND_V/traceability/[**7N_req_to_test_trace.csv**](../../V_AND_V/traceability/7N_req_to_test_trace.csv)

---

## Compliance References
- **Certification basis:** ../ALR/[**ALR-023.md**](../ALR/ALR-023.md) – Noise certification  
- **Noise standards:** **ICAO Annex 16 Volume I** (Aircraft Noise), **CS-36** (EASA noise certification), **FAA Part 36** (US noise standards)  
- **Acoustic modeling:** **ATA 18** (Vibration and Noise Analysis), **SAE ARP876** (gas turbine noise prediction — adapted for electric propulsion)  
- **Flight procedures:** **ICAO Doc 8168** (PANS-OPS) for noise abatement procedures  
- **Safety allocation:** ../../SAFETY/FHA/[**FHA_report.md**](../../SAFETY/FHA/FHA_report.md) (noise does not directly affect safety, but community acceptance affects operational viability)

🔗 Compliance mapping: ../../CERTIFICATION/[**AT_FAR_CS25_compliance.csv**](../../CERTIFICATION/AT_FAR_CS25_compliance.csv)

---

## Traceability
- **Parent ALR:** ../ALR/[**ALR-023.md**](../ALR/ALR-023.md)  
- **Linked SRs:**  
  - ../SR/[**SR-ACOU-PROP-001.md**](../SR/SR-ACOU-PROP-001.md) – Propulsor acoustic design  
  - ../SR/[**SR-ACOU-SHIELD-001.md**](../SR/SR-ACOU-SHIELD-001.md) – BWB shielding effectiveness  
  - ../SR/[**SR-ACOU-OPS-001.md**](../SR/SR-ACOU-OPS-001.md) – Noise abatement operations  
- **Related Requirements:**  
  - **RQ-10-04** (8× open-fan propulsors — acoustic design)  
  - **RQ-00-01** (Cruise Mach 0.78 — acoustic constraints)  
- **V&V Cross-refs:** ../../V_AND_V/cases/[**TEST-ACOU-001**](../../V_AND_V/cases/TEST-ACOU-001.md) · ../../V_AND_V/cases/[**TEST-ACOU-WT-001**](../../V_AND_V/cases/TEST-ACOU-WT-001.md) · ../../V_AND_V/cases/[**TEST-ACOU-GT-001**](../../V_AND_V/cases/TEST-ACOU-GT-001.md) · ../../V_AND_V/cases/[**TEST-ACOU-FT-001**](../../V_AND_V/cases/TEST-ACOU-FT-001.md)  
- **RTM rows:** ../RTM/[**RTM-ACOU-001.csv**](../RTM/RTM-ACOU-001.csv)

---

## Notes
- **Market differentiator:** -25 dB noise reduction opens access to noise-restricted airports (e.g., London City, Orange County, Amsterdam late-night operations) and enhances community acceptance.  
- **Technology synergy:** Electric propulsion + BWB shielding + distributed propulsion are mutually reinforcing for noise reduction; achievement of -25 dB requires all three elements.  
- **Reference:** Noise model BWB-RevA (cited in requirements table) provides detailed acoustic predictions and validation data.
