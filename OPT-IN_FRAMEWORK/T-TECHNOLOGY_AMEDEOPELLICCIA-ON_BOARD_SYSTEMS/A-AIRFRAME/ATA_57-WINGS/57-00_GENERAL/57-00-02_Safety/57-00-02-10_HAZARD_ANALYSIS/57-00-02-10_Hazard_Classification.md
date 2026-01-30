# 57-00-02-10 — Hazard Classification

**ATA Chapter**: 57 — Wings  
**Folder**: 57-00-02_Safety / 57-00-02-10_HAZARD_ANALYSIS  
**Status**: DRAFT  
**Owner**: Airframe & Structures Domain (ATA 57)

---

## 1. Purpose

This document defines the **severity and likelihood classification schemes** used for hazard assessment in the ATA 57 Wing domain.

---

## 2. Severity Classification

Per [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes):

| Class | Severity | Definition | Crew Effects | Passenger Effects |
| :-- | :-- | :-- | :-- | :-- |
| 1 | **Catastrophic** | Failure conditions resulting in multiple fatalities, usually with loss of the airplane | N/A | Multiple fatalities |
| 2 | **Hazardous** | Large reduction in safety margins; physical distress or higher workload | Very high workload | Serious/fatal injury to few |
| 3 | **Major** | Significant reduction in safety margins or functional capabilities | Significant workload | Physical discomfort |
| 4 | **Minor** | Slight reduction in safety margins; slight increase in workload | Slight workload | Some inconvenience |
| 5 | **No Effect** | No effect on operational capability or safety | None | None |

---

## 3. Probability Classification

| Class | Probability | Quantitative | Qualitative Definition |
| :-- | :-- | :-- | :-- |
| A | **Probable** | > 10⁻⁵ /FH | Expected to occur one or more times during operational life |
| B | **Remote** | 10⁻⁵ – 10⁻⁷ /FH | Unlikely per airplane, may occur in fleet |
| C | **Extremely Remote** | 10⁻⁷ – 10⁻⁹ /FH | Not expected per airplane, few times in fleet |
| D | **Extremely Improbable** | < 10⁻⁹ /FH | Not expected during entire fleet operational life |

---

## 4. Risk Matrix

The risk matrix combines severity and probability to determine required actions:

|  | Probable (A) | Remote (B) | Extremely Remote (C) | Extremely Improbable (D) |
| :-- | :-- | :-- | :-- | :-- |
| **Catastrophic (1)** | Not Allowed | Not Allowed | Not Allowed | Acceptable |
| **Hazardous (2)** | Not Allowed | Not Allowed | Acceptable | Acceptable |
| **Major (3)** | Not Allowed | Acceptable | Acceptable | Acceptable |
| **Minor (4)** | Acceptable | Acceptable | Acceptable | Acceptable |
| **No Effect (5)** | Acceptable | Acceptable | Acceptable | Acceptable |

---

## 5. Classification Guidance

### 5.1 Structural Failures

| Failure Type | Typical Severity | Rationale |
| :-- | :-- | :-- |
| Primary structure failure | Catastrophic | Potential loss of aircraft |
| Secondary structure failure | Major to Hazardous | Depends on extent and consequences |
| Fatigue crack initiation | Minor to Major | If detected before failure |
| Corrosion damage | Minor to Major | Depends on extent |

### 5.2 Aeroelastic Events

| Event | Severity | Rationale |
| :-- | :-- | :-- |
| Flutter | Catastrophic | Rapid divergent oscillation |
| Control reversal | Hazardous | Loss of intended control |
| Divergence | Catastrophic | Static instability |

### 5.3 Control Surface Failures

| Failure | Severity | Rationale |
| :-- | :-- | :-- |
| Total loss of roll control | Catastrophic | Unable to control aircraft |
| Partial loss of roll control | Hazardous | Reduced controllability |
| Asymmetric flap/slat | Hazardous | Roll upset at critical phase |

---

## 6. Application Rules

1. **Conservative approach**: When uncertainty exists, classify toward higher severity/probability.  
2. **Combination effects**: Consider combined failures where applicable.  
3. **Phase sensitivity**: Account for flight phase effects on severity.  
4. **Crew capability**: Consider crew ability to recognize and respond.  

---

## 7. References

- [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)  
- [ARP4761](https://www.sae.org/standards/content/arp4761/)  
- [57-00-02-00_Safety_Taxonomy.md](../57-00-02-00_SAFETY_OVERVIEW/57-00-02-00_Safety_Taxonomy.md)  

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** — Subject to human review and approval.  
- Human approver: _[to be completed]_.  
- Repository: `AMPEL360-BWB-H2-Hy-E`  
- Last AI update: 2025-11-29
