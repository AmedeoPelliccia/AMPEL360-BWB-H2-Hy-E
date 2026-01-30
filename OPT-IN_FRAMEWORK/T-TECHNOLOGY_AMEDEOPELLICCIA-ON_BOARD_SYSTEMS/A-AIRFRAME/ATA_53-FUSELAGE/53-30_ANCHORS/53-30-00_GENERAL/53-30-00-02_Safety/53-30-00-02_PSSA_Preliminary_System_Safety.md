# 53-30-00-02 — Preliminary System Safety Assessment (PSSA)

**Document ID:** 53-30-00-02-003  
**ATA Chapter:** 53 – Fuselage  
**Subsystem Band:** 53-30_ANCHORS — Aircraft Networks, Circular, Harvesting, Operating & Renewable Systems  
**Version:** 1.1  
**Date:** 2025-11-25  
**Status:** DRAFT  

---

## 1. Purpose

This Preliminary System Safety Assessment (PSSA) establishes the **safety architecture**, **derived safety requirements**, **probability budgets**, and **common cause considerations** for the **53-30 ANCHOR'S** systems integrated into the fuselage.

It follows the safety methodology defined in:

- **ARP4761** — *Guidelines and Methods for Conducting the Safety Assessment Process*  
  https://www.sae.org/standards/content/arp4761/  
- **ARP4754A** — *Guidelines for Development of Civil Aircraft and Systems*  
  https://www.sae.org/standards/content/arp4754a/  
- **EASA CS-25** — *Certification Specifications for Large Aeroplanes*  
  https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25  
- **14 CFR Part 25**  
  https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25  

---

## 2. Cross-Referenced Internal Documentation (Hyperlinked)

All referenced internal documentation is pure-text (`.md` or `.csv`) and located under the 53-30 directory:

- [53-30-00-02_FHA_Functional_Hazard_Assessment.md](./53-30-00-02_FHA_Functional_Hazard_Assessment.md)
- [53-30-00-02_Safety_Assessment_Plan.md](./53-30-00-02_Safety_Assessment_Plan.md)
- [53-30-00-02_Zonal_Safety_Analysis.md](./53-30-00-02_Zonal_Safety_Analysis.md)
- [53-30-00-02_Common_Cause_Analysis.md](./53-30-00-02_Common_Cause_Analysis.md)
- [53-30-00-01_System_Architecture.md](../53-30-00-01_Overview/53-30-00-01_System_Architecture.md)
- [53-30-00-03_System_Requirements_Spec.md](../53-30-00-03_Requirements/53-30-00-03_System_Requirements_Spec.md)
- [53-30-00-07_Verification_Matrix.csv](../53-30-00-07_V_AND_V/53-30-00-07_Verification_Matrix.csv)
- [53-30-00-02_Hazard_Log.csv](./53-30-00-02_Hazard_Log.csv)

**No binary files or proprietary formats are referenced.  
All tables are stored in CSV only.**

---

## 3. Scope and System Description

ANCHOR'S covers naturally circular and regenerative systems integrated into the fuselage, including:

- harvesting systems (airflow, condensate, waste heat)  
- CO₂ capture and separation modules  
- water/waste recycling loops  
- battery regeneration loops  
- thin-film solar and vibration energy harvesters  
- regenerative structural panels  
- circular networks (ThermalBus, ResourceBus, CO₂ and water networks)

Full system description:  
[53-30-00-01_System_Architecture.md](../53-30-00-01_Overview/53-30-00-01_System_Architecture.md)

---

## 4. PSSA Methodology

Aligned with:

- **ARP4761** (FHA → PSSA → SSA flow)  
- **CS-25.1309** safety objectives  
- **AMC 20-152A** for AI/ML assurance (ATA 95 links)  
  https://www.easa.europa.eu/en/document-library/advisory-material/amc-20-152a

This PSSA:

- derives safety requirements  
- allocates requirements to fuselage ANCHOR'S architecture  
- establishes probability budgets  
- identifies common-cause hazards  
- prepares inputs for SSA, FMEA, FTA, ZSA

---

## 5. Safety Architecture

### 5.1 Safety-Related Functions

A filtered subset from the FHA (full FHA here):  
[53-30-00-02_FHA_Functional_Hazard_Assessment.md](./53-30-00-02_FHA_Functional_Hazard_Assessment.md)

| FHA ID | Function / Hazard | Severity | Objective |
|--------|-------------------|----------|-----------|
| FC-003 | CO₂ accumulation in bays | Major/Hazardous | Prevent unsafe local concentration |
| FC-005 | Battery thermal runaway | Hazardous | Prevent/contain, probability < 1E-7 |
| FC-007 | Unsafe water contamination | Major | Prevent unsafe water delivery |
| FC-010 | Structural impairment | Major/Hazardous | Maintain structural integrity |

---

### 5.2 Independence Requirements

| System | Required Independence | Basis |
|--------|------------------------|-------|
| Battery cooling | Dual independent loops | FC-005 |
| Battery monitoring power | Independent feed / local reserve | FC-005 |
| CO₂ capture | Single with manual backup | FC-003 |
| Water recycling | Bypass path to safe dump | FC-007 |
| Energy harvesting | No independence needed | Performance-only |

---

### 5.3 Monitoring Requirements

| Hazard | Monitoring Requirement |
|--------|--------------------------|
| Thermal runaway | Cell-level temperature + bay sensors |
| CO₂ leak | Gas concentration sensors |
| Water contamination | Water quality sensors |
| Over-pressure | Pressure sensors + relief logic |
| Excess structural heating | Skin temperature sensors |

---

## 6. Derived Safety Requirements (DSRs)

Full traceability matrix in:  
[53-30-00-07_Verification_Matrix.csv](../53-30-00-07_V_AND_V/53-30-00-07_Verification_Matrix.csv)

| DSR ID | Requirement | FHA Ref | Verification Method |
|--------|-------------|----------|----------------------|
| DSR-001 | Thermal isolation to prevent propagation | FC-005 | Test + Analysis |
| DSR-002 | Cooling loop failure detected < 5 s | FC-005 | Test |
| DSR-003 | CO₂ bay ventilation provisions | FC-003 | Analysis + Inspection |
| DSR-004 | Automatic battery bay suppression | FC-005 | Test |
| DSR-005 | No cell-to-cell propagation | FC-005 | Test & Analysis |
| DSR-006 | Water output must meet quality limits | FC-007 | Test |
| DSR-007 | Sensor failure triggers bypass/dump | FC-007 | Test |
| DSR-008 | CO₂ unit failure must not block ECS safety | FC-003 | FMEA + Test |
| DSR-009 | Structure must maintain ultimate load with ANCHOR'S integration | FC-010 | Structural Analysis |
| DSR-010 | Loss of harvesting shall not mislead flight crew | FC-003/005 | Test + HMI inspection |

---

## 7. Probability Budget Allocation

### 7.1 Battery Thermal Runaway (FC-005)

Safety objective: **P < 1×10⁻⁷ per FH**

| Contributor | Probability Budget |
|-------------|---------------------|
| Cell defects | < 1E-8 |
| Cooling loop failure | < 1E-8 |
| External damage | < 1E-8 |
| Control malfunction | < 1E-8 |

Details tracked in:  
[53-30-00-02_Hazard_Log.csv](./53-30-00-02_Hazard_Log.csv)

---

## 8. Common Cause Failure (CCF) Summary

Full detail:  
[53-30-00-02_Common_Cause_Analysis.md](./53-30-00-02_Common_Cause_Analysis.md)

| CCA ID | Common Cause | Mitigation |
|--------|--------------|------------|
| CCA-001 | Electrical bus failure | Independent/local reserves |
| CCA-002 | Software/NN error | DAL allocation + assurance per AMC 20-152A |
| CCA-003 | Coolant leak | Leak detection + isolation |
| CCA-004 | Bay fire | Zonal segregation + fire barriers |
| CCA-005 | Maintenance error | Clear AMM + config control |

---

## 9. Zonal Safety (ZSA)

Performed according to:

- **CS 25.1309**, **CS 25.863**, **CS 25.869**, **CS 25.1713**  
  https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25

ZSA document (text only):  
[53-30-00-02_Zonal_Safety_Analysis.md](./53-30-00-02_Zonal_Safety_Analysis.md)

---

## 10. Open Actions

- Complete fault trees → [53-30-00-02_FTA_Fault_Trees.md](./53-30-00-02_FTA_Fault_Trees.md)  
- Finalise probability budgets → update in `Hazard_Log.csv`  
- Supplier coordination for reliability data  
- NN/ML assurance allocation (crosslink ATA 95)  
- Update ZSA after installation refinement  

---

## Document Control

Generated with the assistance of AI (ChatGPT / GitHub Copilot), prompted by **Amedeo Pelliccia**.  
Status: **DRAFT — Subject to human review**.  
Human approver: **[Pending]**  
Repository: `AMPEL360-BWB-H2-Hy-E`  
Last AI update: **2025-11-25**
