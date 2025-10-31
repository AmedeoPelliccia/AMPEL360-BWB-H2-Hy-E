# Certification Artifacts: 04-50-01

## 1.0 Certification Basis Documents

### 1.1 Type Certificate Data Sheet (TCDS)
**Document ID:** EASA.A.XXX  
**Section:** Limitations  
**Entry:**  
> **Item 19(c) - Fuel Tank Life Limit:**  
> LH₂ Storage Tank Inner Vessel (P/N 28-100-001): Retire at 50,000 flight cycles or 20 years, whichever occurs first. Thermal cycle limit: 75,000 cycles. Refer to ALS Section 04-50-01.

### 1.2 Airworthiness Limitations Section (ALS)
**Document ID:** AMPEL360-ALS-Rev-B  
**Section:** 04-50 Fuel and Energy Storage Limits  
**Page:** 4-12  
**Limitation Text:**  
> **MANDATORY RETIREMENT - LH₂ TANK INNER VESSEL**  
> - P/N: 28-100-001, 28-100-002, 28-100-003  
> - Retirement Criteria: 50,000 FC or 20 CY (first occurrence)  
> - No life extension permitted  
> - Record compliance in aircraft logbook per ATA 05-21-01  

## 2.0 Engineering Substantiation

### 2.1 Structural Analysis Report
**Document ID:** AMPEL-STRESS-H2-TANK-001  
**Revision:** D  
**Date:** 2024-06-30  
**Author:** Dr. Elena Rodriguez, Principal Stress Engineer  
**Summary:**  
Finite element model of full-scale LH₂ tank subjected to:
- Internal pressure: 5.5 bar (max operating) to 8.8 bar (1.6× proof)
- Thermal loads: -253°C (LH₂) to +70°C (external desert hot day)
- Inertial loads: 9g ultimate load factor (crash scenario)

**Critical Stress Locations:**
1. Dome-to-cylinder weld (304L SS fillet weld): σ_max = 285 MPa
2. Tank support lug attachment: σ_max = 310 MPa
3. Penetration for fill/drain valve: σ_max = 265 MPa

**Fatigue Analysis:**
- Method: Crack initiation life per Neuber rule
- Material S-N curve: Al-Li 2195-T8 at -253°C (proprietary Alcoa data)
- Result: N_i = 147,000 cycles (initiation), N_f = 152,000 cycles (through-wall crack)
- Safety Factor: 152,000 / 50,000 = 3.04 ✓ (meets CS-25.571 requirement of SF ≥ 3.0)

### 2.2 Full-Scale Fatigue Test Report
**Document ID:** AMPEL-TEST-H2-TANK-FSFT  
**Revision:** C  
**Date:** 2024-08-22  
**Test Facility:** NASA White Sands Test Facility, New Mexico  
**Test Article:** S/N 28-100-P001 (prototype tank, identical to production standard)

**Test Spectrum:**
- Pressure cycles: 0.5 bar (min) to 6.9 bar (1.25× design max)
- Thermal cycles: +20°C to -253°C (LN₂ substitute for LH₂)
- Cycle rate: 4 cycles/hour (thermal limitation)
- Duration: 9 months (150,000 cycles)

**Instrumentation:**
- 64× strain gauges (Vishay CEA-06-125UW-350)
- 12× thermocouples (Type K, surface-mounted)
- 2× acoustic emission sensors (leak detection)
- Vacuum pressure monitoring (10⁻⁶ torr resolution)

**Results:**
- **Cycle 0-100,000:** No anomalies, strain levels per FEA predictions
- **Cycle 100,001-147,349:** Stable behavior, minor strain gauge drift corrected
- **Cycle 147,350:** Acoustic emission event detected, pressure drop observed
- **Post-Test Inspection:** 45mm fatigue crack originated at weld toe, dome-cylinder junction
- **Fractography:** Classic high-cycle fatigue striations, no manufacturing defects observed

**Conclusion:**  
Test article exceeded 3× design service goal. Retirement limit of 50,000 cycles provides adequate safety margin per AC 23.573-1C.

### 2.3 Environmental Qualification Report
**Document ID:** AMPEL-ENV-H2-TANK-002  
**Revision:** A  
**Date:** 2024-07-10  
**Scope:** Long-term environmental degradation assessment

**Test Matrix:**
- **Hydrogen embrittlement:** 5,000-hour exposure to LH₂ atmosphere
  - Pre-test fracture toughness: K_IC = 45 MPa√m
  - Post-test fracture toughness: K_IC = 41 MPa√m (9% reduction)
  - **Conclusion:** Acceptable degradation, design margins maintained
  
- **Corrosion resistance:** Salt spray (ASTM B117) + thermal cycling
  - 3,000 hours exposure simulating 20 years coastal operations
  - Surface pitting: Max depth 0.08 mm (limit: 0.15 mm)
  - **Conclusion:** Anodic coating performs adequately
  
- **Vacuum degradation:** Multi-layer insulation (MLI) aging
  - 20-year accelerated aging (Arrhenius model, 85°C/85% RH)
  - Vacuum pressure increase: 2.1×10⁻⁴ torr (limit: 1×10⁻³ torr)
  - **Conclusion:** 10× margin to vacuum loss threshold

**Certification Statement:**  
Calendar life limit of 20 years is supported by accelerated aging test data with 2.5× safety factor on environmental degradation mechanisms.

## 3.0 Regulatory Approval

### 3.1 EASA Type Certificate Amendment
**Document ID:** EASA TC Amendment 001 to Type Certificate EASA.A.XXX  
**Issue Date:** 2024-09-15  
**Approval Statement:**  
> The airworthiness limitation for the LH₂ tank inner vessel (P/N 28-100-001/-002/-003) has been reviewed and is **APPROVED** as specified in ALS Section 04-50-01. This limitation is **MANDATORY** and must be incorporated into the aircraft maintenance program per Part-M.A.302.

**Certification Manager:** Dipl.-Ing. Klaus Hoffmann, EASA  
**Signature:** [Digital Signature on File]

### 3.2 FAA Type Certificate Data Sheet
**Document ID:** FAA TCDS XXX (pending final approval)  
**Expected Issue:** 2025-Q2  
**Status:** Under review; preliminary acceptance letter issued 2024-11-05

## 4.0 Traceability Matrix

| ATA 04 Limitation | Substantiation Document | Test Evidence | Regulatory Approval |
|-------------------|------------------------|---------------|---------------------|
| 50,000 FC limit | AMPEL-STRESS-H2-TANK-001 | AMPEL-TEST-H2-TANK-FSFT | EASA TC Amend 001 |
| 20 CY limit | AMPEL-ENV-H2-TANK-002 | Accelerated aging tests | EASA TC Amend 001 |
| Vacuum threshold | AMPEL-STRESS-H2-TANK-001 | Thermal analysis | EASA TC Amend 001 |
| Leak detection requirement | AMPEL-SSA-H2-002 | Leak detection system qual | EASA TC Amend 001 |

## 5.0 Compliance Instructions

**For Operators:**
1. Establish tracking system for flight cycles and thermal cycles per ATA 05-21-01
2. Record tank serial number and installation date in aircraft logbook (AMM 28-00-00)
3. At each major maintenance check (C-Check or higher), verify cycle count accuracy
4. When limit approached (>47,500 FC or 19 CY), initiate replacement tank procurement
5. Upon reaching limit, ground aircraft until tank replacement completed

**For Maintenance Organizations:**
1. Tank removal procedure: AMM Task 28-11-00-400-801
2. Replacement installation: AMM Task 28-11-00-400-802
3. System leak test after installation: AMM Task 28-21-00-710-001
4. Logbook entry: "LH₂ tank inner vessel (S/N XXX) installed, zero-time entry, compliance with ALS 04-50-01"

**Penalties for Non-Compliance:**
Operation beyond specified life limit constitutes operation of an unairworthy aircraft. Regulatory actions may include:
- Certificate of Airworthiness revocation
- Operator certificate suspension
- Civil penalties (EASA: up to €4,000 per day; FAA: up to $50,000 per violation)

## 6.0 Certification Test Summary

### 6.1 Qualification Tests Completed
| Test | Standard | Result | Date |
|------|----------|--------|------|
| Proof pressure | CS-25.963(a) | PASS | 2024-05-12 |
| Ultimate pressure | CS-25.963(b) | PASS | 2024-05-14 |
| Vibration | CS-25.963(c) | PASS | 2024-06-03 |
| Full-scale fatigue | AC 23.573-1C | PASS | 2024-08-22 |
| Thermal shock | NASA-STD-5001B | PASS | 2024-07-19 |
| Leak detection | CS-25.981 | PASS | 2024-06-28 |
| Material qual | ASTM E1820 | PASS | 2024-04-10 |
| Environmental aging | ASTM B117 | PASS | 2024-07-10 |

### 6.2 Inspection and Test Plans (ITP)
**ITP-H2-TANK-001:** Manufacturing Quality Control
- 100% radiographic inspection of all welds
- Dye penetrant inspection of external surfaces
- Helium leak test (sensitivity: 1×10⁻⁹ atm·cc/s)
- Proof pressure test at 1.5× design pressure
- Vacuum integrity test (achieve < 1×10⁻⁵ torr)

**Result:** All production tanks (S/N 001 through 010) passed ITP requirements

## 7.0 Service Experience Monitoring

### 7.1 Fleet Leader Program
**Aircraft Designation:** AMPEL360-FLP-001 through -010

**Enhanced Monitoring:**
- Strain gauge instrumentation on 3 tanks (S/N 001, 005, 009)
- Accelerated inspection at 25,000 FC (one tank removed for teardown)
- Monthly vacuum pressure trending
- Thermal cycle correlation study

**Findings to Date:** (as of 2024-10-31)
- Maximum flight cycles accumulated: 8,450 FC (S/N 001)
- No anomalies detected in service
- Strain gauge data correlates with FEA predictions within 8%
- Vacuum pressure remains stable (< 1×10⁻⁵ torr all aircraft)

### 7.2 Service Bulletin Program
**Active SBs:**
- **SB-AMPEL-28-001:** Thermal cycle counter software update (mandatory, compliance by 2025-03-31)
- **SB-AMPEL-28-002:** Enhanced vacuum pressure monitoring (optional)

**Pending SBs:**
- None at this time

### 7.3 Continued Airworthiness Actions
**Next Review Date:** 2025-09-15 (annual review)

**Potential Actions:**
- Life limit extension if service data supports (requires regulatory approval)
- Inspection program addition if unexpected degradation observed
- Emergency Airworthiness Directive if safety issue identified

## 8.0 Document Control

**Classification:** CONTROLLED - REGULATORY DOCUMENT  
**Distribution:** Operators, MROs, Regulatory Authorities  
**Retention:** Aircraft lifetime + 20 years  
**Archive Location:** Engineering Records Management System  
**Document Owner:** Chief Engineer - Airworthiness & Certification  
**Contact:** cert@ampel360.aero
