# 02-20-11-009 — Safety and Certification

**Subsystem ID:** 02-20-11  
**Group:** [02-20_Subsystems](../README.md)  
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)  
**Axis:** I — Infrastructures  
**Function:** Safety, Certification & Cybersecurity Baseline  
**Status:** OPERATIONAL  
**Version:** 1.0  

---

## 1. Purpose

This document consolidates the **safety, certification and cybersecurity baseline**
for the AMPEL360 **Electronic Flight Bag (EFB)** subsystem, including:

- Regulatory references (FAA/EASA)  
- Safety objectives and failure conditions  
- Software assurance (DO-178C)  
- Equipment qualification (DO-160)  
- Cybersecurity (DO-326A / ED-202A)  
- AI/NN-specific assurance hooks (ATA 95)  
- Links to certification evidence artefacts  

It is the **primary reference** for audits and certification dossiers related to
02-20-11.

---

## 2. Scope

### Included

- EFB **as a system** (HW + SW + integration)  
- Operational use in the **flight deck**  
- Safety classification and failure condition analysis (at high level)  
- Software DAL and process references  
- Cyber and HF aspects relevant to safety and approval  

### Excluded

- Operator-specific approvals (OpSpecs, AOC-specific limitations)  
- Detailed safety analysis artefacts (FHA/FMEA/SSA documents)  
- Full DO-178C and DO-330 evidence (referenced but not reproduced)  
- Detailed ATA 95 model assurance (covered in ATA 95 docs)  

---

## 3. Regulatory References

### 3.1 EFB Regulatory Framework

- **FAA**  
  - AC 120-76D — Electronic Flight Bags  
  - Operational approval via OpSpec A061  

- **EASA**  
  - AMC 20-25 — Airworthiness and operational considerations for EFB  
  - CAT.OP.MPA.295 & SPA.EFB.xxx — EFB operation and approval  

### 3.2 Software & Hardware

- **Software**  
  - RTCA DO-178C / EUROCAE ED-12C — Software Considerations in Airborne Systems  
  - DO-330 / ED-215 — Software Tool Qualification (if applicable)  

- **Hardware / Environment**  
  - RTCA DO-160G / ED-14G — Environmental Conditions and Test Procedures  

### 3.3 Cybersecurity

- DO-326A / ED-202A — Airworthiness Security Process Specification  
- DO-355 / ED-204 — Information Security Guidance for Continuing Airworthiness  

### 3.4 AI / Neural Networks (ATA 95)

- EASA AI Roadmap / AI Concept Papers (reference only)  
- ATA 95 internal guidance for NN assurance and traceability  

---

## 4. Safety Role & Classification

### 4.1 EFB Role

The EFB is a **non-safety-critical advisory system** which:

- Provides **operational information** (docs, performance, W&B, weather, charts)  
- Displays **advisories and predictions** from CAOS / NNs  
- Does **not** send commands to safety-critical systems  
- Does **not** host flight-control laws  

### 4.2 Failure Conditions

EFB failures are assumed to cause:

- **Major** at most (loss/erroneous information requiring crew workload)  
- No direct **catastrophic** or **hazardous** failure condition on their own  

Therefore:

- EFB software: **DO-178C DAL D** (typical)  
- Underlying data sources (ATA 42/28/31/95) may be higher DAL but are out of scope
  of 02-20-11 certification.

---

## 5. Safety Objectives

High-level safety objectives:

1. **SO-01 — Information Integrity**  
   - The EFB must not display **corrupted or unverified** safety-relevant data
     without an explicit warning.

2. **SO-02 — Fail-Safe Behaviour**  
   - On loss of data or internal malfunction, the EFB must **fail passive**, i.e.:
     - Stop updating  
     - Flag data as invalid  
     - Avoid misleading crew  

3. **SO-03 — Clear Authority Boundaries**  
   - EFB outputs must be clearly labelled as **advisory**.  
   - Crew must always be able to **override** EFB recommendations.

4. **SO-04 — Human Factors**  
   - User interface must minimize risk of **misinterpretation**.  
   - Colour coding and symbology must follow HF best practices.

5. **SO-05 — Cyber Protection**  
   - EFB must be **segregated** from safety-critical networks.  
   - Compromise of the EFB must not compromise aircraft safety-critical systems.

---

## 6. Software Assurance (DO-178C)

### 6.1 DAL Allocation

- EFB application software (performance, W&B, weather, charts): **DAL D**  
- Supporting tools may be subject to **DO-330** if they can introduce errors that
  bypass verification.

### 6.2 Life Cycle Artefacts (Pointer Only)

These artefacts live under:

- `ASSETS/Certification/02-20-11-A-501_DO_178C_Evidence.pdf`  
- `ASSETS/Certification/02-20-11-A-502_AC_120-76D_Compliance.pdf`  

Typical contents:

- PSAC — Plan for Software Aspects of Certification  
- SDP — Software Development Plan  
- SVP — Software Verification Plan  
- SCMP — Software Configuration Management Plan  
- SQAP — Software Quality Assurance Plan  
- Requirements, design, code, test evidence  
- Traceability matrices (Req ↔ Design ↔ Code ↔ Test)  

---

## 7. Equipment Qualification (DO-160)

### 7.1 Environmental Categories (Typical Baseline)

| DO-160 Section | Category | Notes |
|----------------|----------|-------|
| Temperature | B2 | Cockpit environment |
| Vibration | S | Mounted to cockpit structure |
| EMI/EMC | R | Proximity to avionics |
| Fluids | F | Minimal exposure |
| Fire/Flammability | A | Materials-certified mount |
| Pressure | D | Pressurized cabin |
| Humidity | B | Cockpit environment |

Device-level evidence and mount qualification are captured in:

- `ASSETS/Certification/02-20-11-A-503_DO_160_Qualification.pdf` (placeholder path)

---

## 8. Cybersecurity (DO-326A / ED-202A)

### 8.1 Security Objectives

- Prevent **unauthorized access** to EFB data and functions  
- Ensure **confidentiality** of operational and airline data  
- Ensure **integrity** of software and nav/document database updates  
- Ensure that compromise of EFB cannot **propagate** to safety-critical domains  

### 8.2 Controls

- Strong authentication (crew ID + PIN + biometric where enabled)  
- Encrypted storage (AES-256 or equivalent)  
- Secure boot & signed binaries  
- TLS + VPN for all remote communications  
- Role-based access control (RBAC) for admin functions  
- Regular vulnerability management (patching policy coordinated with operator)  

Security risk assessment and mitigations reside in:

- `ASSETS/Certification/02-20-11-A-504_Security_Risk_Assessment.pdf` (placeholder)

---

## 9. AI / Neural Networks Safety Hooks (ATA 95)

The EFB consumes predictions from ATA 95 NN models via:

- `02-20-13_Performance_Computer`  
- `02-20-17_Weather_Information_System`  
- `02-20-23_Predictive_Operations_NN`  

### 9.1 Assurance Principles

- NNs are **not** directly certified under DO-178C in 02-20-11.  
- Assurance is provided through ATA 95 and respective subsystems.

EFB-specific safety measures:

1. **AI Transparency**  
   - AI-enhanced outputs are clearly distinguished (e.g., icon/label).  

2. **Fallback Availability**  
   - Deterministic fallback algorithms always available (e.g., legacy performance tables).  

3. **Input Validation**  
   - EFB only passes **validated, range-checked** inputs to NN-backed services.  

4. **Output Reasonableness Checks**  
   - Performance, W&B or hazard predictions checked against physical and
     operational limits; suspicious outputs rejected.  

5. **Logging & Traceability**  
   - All AI-enhanced calls and outputs can be correlated with ATA 95 model
     versions (via DPP and model IDs).

For NN lifecycle and model governance, refer to ATA 95 documents.

---

## 10. Failure Modes & Effects (High-Level)

### 10.1 Representative Failure Modes

- Total EFB failure (black screen)  
- Partial module failure (e.g., charts only, performance only)  
- Data outage (loss of ATA 42/28/31/02-20-01 feeds)  
- Corrupted updates (docs, nav data)  
- Incorrect AI prediction (within ATA 95 scope)  

### 10.2 Mitigations

- Redundancy: typically **two EFBs** (left/right seat)  
- Backup procedures (paper or alternative digital systems)  
- Clear crew procedures in OM-A/OM-B  
- Fail-passive behaviour:
  - EFB modules **disable** themselves if data cannot be trusted  
  - Warnings are raised but system does not send unsafe commands  

---

## 11. Human Factors & Usability

HF goals:

- Avoid **mode confusion** between deterministic and AI-augmented modes  
- Maintain consistent **colour semantics** (e.g., amber/caution, red/warning)  
- Ergonomic interaction in turbulence (minimal complex gestures)  
- Legibility in day/night/low brightness conditions  
- Quick access to emergency content (QRH, checklists) even during partial failures  

HF evaluation:

- Simulator campaigns  
- Line evaluation with representative crews  
- Feedback loop via CAOS analytics (e.g., doc usage, UI paths)

---

## 12. Certification Evidence Index (Pointers)

Certification-related artefacts for 02-20-11 are stored under:

- `ASSETS/Certification/`

Recommended filenames (placeholders):

- `02-20-11-A-501_DO_178C_Evidence.pdf`  
- `02-20-11-A-502_AC_120-76D_Compliance.pdf`  
- `02-20-11-A-503_DO_160_Qualification.pdf`  
- `02-20-11-A-504_Security_Risk_Assessment.pdf`  
- `02-20-11-A-505_AI_Use_Assessment_Summary.pdf`  

---

## 13. Traceability

### Requirements

- RQ-02-11-SAF-001 — EFB shall be advisory-only with no command authority  
- RQ-02-11-SAF-002 — EFB software shall comply with DO-178C DAL D  
- RQ-02-11-SAF-003 — EFB shall implement fail-passive behaviour on faults  
- RQ-02-11-SAF-004 — AI-enhanced outputs shall be traceable and fallback-capable  
- RQ-02-11-SAF-005 — EFB shall comply with applicable EFB regulatory guidance  

### Design / Evidence References

- `02-20-11-001_EFB_Overview.md`  
- `02-20-11-002_Class_3_EFB_Implementation.md`  
- `02-20-11-004_Performance_Calculations.md`  
- `02-20-11-005_Weight_Balance_Module.md`  
- `02-20-11-007_Charts_Navigation_Data.md`  

---

## 14. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia  
> **Subsystem:** 02-20-11 Electronic Flight Bag  
> **Function:** Safety & Certification Baseline  
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Framework  

| Version | Date       | Author / Team                          | Changes                                |
|---------|------------|-----------------------------------------|----------------------------------------|
| 1.0     | 2025-11-19 | AMPEL360 Digital Operations & CAOS WG  | Initial safety & certification summary |

```

