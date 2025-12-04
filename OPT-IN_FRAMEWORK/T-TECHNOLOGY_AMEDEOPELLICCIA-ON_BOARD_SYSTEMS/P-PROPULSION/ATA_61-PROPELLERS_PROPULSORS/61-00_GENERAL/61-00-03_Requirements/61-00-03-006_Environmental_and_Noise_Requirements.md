# 61-00-03-006 Environmental and Noise Requirements

**Document ID:** 61-00-03-006  
**Title:** Propulsor System Environmental and Noise Requirements Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** 0.1  
**Status:** DRAFT

---

## 1. Purpose

This document defines the **environmental qualification and noise requirements** for the Q100 Propulsor System, establishing the environmental design envelope and acoustic performance targets.

---

## 2. Scope

### 2.1 Environmental Scope

This document covers:
* Temperature and altitude requirements
* Humidity and moisture requirements
* Vibration and shock requirements
* EMI/EMC requirements
* Noise and acoustic requirements

### 2.2 Applicable Standards

| Standard | Title |
|----------|-------|
| RTCA DO-160G | Environmental Conditions and Test Procedures |
| MIL-STD-810H | Environmental Engineering Considerations |
| ICAO Annex 16 Vol. 1 | Aircraft Noise |
| [CS-36](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-36-aircraft-noise) | Aircraft Noise Standards |

---

## 3. Reference Documents

| ID | Title |
|----|-------|
| 61-00-03-001 | System Requirements Specification |
| DO-160G | Environmental Conditions and Test Procedures |
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/group/cs-25-large-aeroplanes) | EASA Certification Specifications |
| ICAO Annex 16 | Environmental Protection |

---

## 4. Environmental Requirements

### 4.1 Temperature Requirements

| Req ID | Parameter | Value | Standard | Verification |
|--------|-----------|-------|----------|--------------|
| ENV-61-001 | Operating temperature range | -55°C to +70°C | DO-160G Cat A1 | Test |
| ENV-61-002 | Storage temperature range | -65°C to +85°C | DO-160G | Test |
| ENV-61-003 | Temperature shock | 40°C change in 5 min | DO-160G Sec 5 | Test |
| ENV-61-004 | Thermal cycling | 20 cycles, full range | DO-160G | Test |

### 4.2 Altitude Requirements

| Req ID | Parameter | Value | Standard | Verification |
|--------|-----------|-------|----------|--------------|
| ENV-61-005 | Operating altitude | Sea level to FL410 | DO-160G Cat D2 | Test |
| ENV-61-006 | Maximum cabin altitude (unpressurized) | 15,000 ft | DO-160G | Analysis |
| ENV-61-007 | Rapid decompression | 8,000 ft to 40,000 ft in 15 sec | DO-160G Sec 4 | Test |

### 4.3 Humidity Requirements

| Req ID | Parameter | Value | Standard | Verification |
|--------|-----------|-------|----------|--------------|
| ENV-61-008 | Operating humidity | 0% to 100% RH | DO-160G Cat A | Test |
| ENV-61-009 | Condensation resistance | No degradation | DO-160G Sec 6 | Test |
| ENV-61-010 | Salt fog resistance | Per DO-160G Sec 14 | DO-160G | Test |

### 4.4 Vibration Requirements

| Req ID | Parameter | Value | Standard | Verification |
|--------|-----------|-------|----------|--------------|
| ENV-61-011 | Random vibration | Per DO-160G Category S | DO-160G Sec 8 | Test |
| ENV-61-012 | Sine vibration (resonance survey) | 5-2000 Hz sweep | DO-160G | Test |
| ENV-61-013 | Self-induced vibration | ≤2g at mount interface | — | Test |

### 4.5 Shock Requirements

| Req ID | Parameter | Value | Standard | Verification |
|--------|-----------|-------|----------|--------------|
| ENV-61-014 | Operational shock | 6g, 11 ms half-sine | DO-160G Sec 7 | Test |
| ENV-61-015 | Crash safety | Per CS-25.561 | CS-25 | Test |

### 4.6 EMI/EMC Requirements

| Req ID | Parameter | Value | Standard | Verification |
|--------|-----------|-------|----------|--------------|
| ENV-61-016 | Conducted emissions | Per DO-160G Sec 21 Cat B | DO-160G | Test |
| ENV-61-017 | Radiated emissions | Per DO-160G Sec 21 Cat M | DO-160G | Test |
| ENV-61-018 | Conducted susceptibility | Per DO-160G Sec 22 Cat B | DO-160G | Test |
| ENV-61-019 | Radiated susceptibility | Per DO-160G Sec 20 Cat T | DO-160G | Test |
| ENV-61-020 | Lightning indirect effects | Per DO-160G Sec 22 Level 3 | DO-160G | Test |
| ENV-61-021 | HIRF susceptibility | Per DO-160G Sec 20 Cat T | DO-160G | Test |

### 4.7 Contamination Requirements

| Req ID | Parameter | Value | Standard | Verification |
|--------|-----------|-------|----------|--------------|
| ENV-61-022 | Dust resistance | Per DO-160G Sec 12 Cat D | DO-160G | Test |
| ENV-61-023 | Sand resistance | Per DO-160G Sec 12 | DO-160G | Test |
| ENV-61-024 | Fluid susceptibility | Per DO-160G Sec 11 | DO-160G | Test |
| ENV-61-025 | Icing conditions | Per CS-25.1093 | CS-25 | Test |

---

## 5. Noise Requirements

### 5.1 Regulatory Noise Limits

| Req ID | Parameter | Value | Standard | Verification |
|--------|-----------|-------|----------|--------------|
| ENV-61-026 | Aircraft noise certification | ICAO Chapter 14 | ICAO Annex 16 | Test |
| ENV-61-027 | Approach noise margin | ≥5 EPNdB below limit | ICAO | Analysis |
| ENV-61-028 | Sideline noise margin | ≥5 EPNdB below limit | ICAO | Analysis |
| ENV-61-029 | Flyover noise margin | ≥5 EPNdB below limit | ICAO | Analysis |

### 5.2 Source Noise Requirements

| Req ID | Parameter | Value | Condition | Verification |
|--------|-----------|-------|-----------|--------------|
| ENV-61-030 | Propulsor source noise | <85 dB(A) | At 1m, max power | Test |
| ENV-61-031 | Fan blade passing frequency | Optimized for low noise | Cruise | Analysis |
| ENV-61-032 | Tonal content | No prominent tones | Per ICAO | Test |

### 5.3 Cabin Noise Requirements

| Req ID | Parameter | Value | Condition | Verification |
|--------|-----------|-------|-----------|--------------|
| ENV-61-033 | Contribution to cabin noise | <5 dB(A) increase | vs. baseline | Test |
| ENV-61-034 | Vibration contribution to structure-borne noise | Minimized | Per design | Analysis |

---

## 6. Environmental Test Matrix

| Test Category | DO-160G Section | Test Required |
|---------------|-----------------|---------------|
| Temperature | Section 4 | Yes |
| Altitude | Section 4 | Yes |
| Temperature Variation | Section 5 | Yes |
| Humidity | Section 6 | Yes |
| Shock | Section 7 | Yes |
| Vibration | Section 8 | Yes |
| Sand and Dust | Section 12 | Yes |
| Salt Fog | Section 14 | Yes |
| Magnetic Effect | Section 15 | N/A |
| Power Input | Section 16 | Yes |
| Voltage Spike | Section 17 | Yes |
| Audio Frequency | Section 18 | Yes |
| Induced Signal Susceptibility | Section 19 | Yes |
| Radio Frequency Susceptibility | Section 20 | Yes |
| Emission of RF Energy | Section 21 | Yes |
| Lightning | Section 22 | Yes |
| Lightning Direct Effects | Section 23 | Analysis |
| Icing | Section 24 | Yes |
| Electrostatic Discharge | Section 25 | Yes |
| Fire, Flammability | Section 26 | Yes |

---

## 7. Traceability

### 7.1 Upstream (Source)

| Source | Document |
|--------|----------|
| [[61-00-03-001_System_Requirements]] | System Requirements |
| DO-160G | Environmental Standards |
| ICAO Annex 16 | Noise Standards |

### 7.2 Downstream (Allocation)

| Target | Document |
|--------|----------|
| [[61-00-04_Design]] | Environmental design |
| [[61-00-07_V_AND_V]] | Environmental test plan |
| [[61-00-10_Certification]] | Noise certification |

---

## 8. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-Q1 | TBD | Initial draft |

---

← [[61-00-03-005_Safety_and_Certification_Requirements]] · [[61-00-03-007_Maintainability_and_Reliability_Requirements]] →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Environmental and Noise Requirements  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-04_.

---
