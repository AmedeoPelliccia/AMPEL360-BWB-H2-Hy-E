# 57-00-02-00 — Safety Taxonomy

**ATA Chapter**: 57 — Wings  
**Folder**: 57-00-02_Safety / 57-00-02-00_SAFETY_OVERVIEW  
**Status**: DRAFT  
**Owner**: Airframe & Structures Domain (ATA 57)

---

## 1. Purpose

This document defines the **safety terminology, definitions, and classifications** used throughout the ATA 57 safety documentation.

Consistent use of these terms ensures clarity and traceability across:

- Hazard analyses.  
- Safety requirements.  
- Design documentation.  
- Certification evidence.  

---

## 2. Hazard Severity Classifications

Per [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) and [ARP4761](https://www.sae.org/standards/content/arp4761/):

| Classification | Definition | Flight Crew Workload | Passenger Effects |
| :-- | :-- | :-- | :-- |
| **Catastrophic** | Failure conditions that would result in multiple fatalities, usually with the loss of the airplane | N/A | Multiple fatalities |
| **Hazardous** | Large reduction in safety margins; physical distress or excessive workload such that crew cannot perform tasks accurately or completely | Very high workload or physical distress | Serious or fatal injury to small number |
| **Major** | Significant reduction in safety margins; significant increase in crew workload or physical discomfort | Significant workload increase | Physical discomfort |
| **Minor** | Slight reduction in safety margins; slight increase in crew workload | Slight workload increase | Some inconvenience |
| **No Safety Effect** | No effect on operational capability or safety | None | None |

---

## 3. Failure Probability Classifications

| Probability Level | Definition | Quantitative Range |
| :-- | :-- | :-- |
| **Probable** | Anticipated to occur one or more times during the operational life | > 10⁻⁵ per flight hour |
| **Remote** | Unlikely to occur to each airplane but may occur several times when considering the total operational life of all airplanes | 10⁻⁵ to 10⁻⁷ per flight hour |
| **Extremely Remote** | Not anticipated to occur to each airplane but may occur a few times when considering the total operational life of all airplanes | 10⁻⁷ to 10⁻⁹ per flight hour |
| **Extremely Improbable** | So unlikely that it is not anticipated to occur during the entire operational life of all airplanes of one type | < 10⁻⁹ per flight hour |

---

## 4. Structural Safety Terms

| Term | Definition |
| :-- | :-- |
| **Limit Load** | The maximum load expected in service |
| **Ultimate Load** | Limit load multiplied by the factor of safety (typically 1.5) |
| **Residual Strength** | The load-carrying capability remaining after damage |
| **Damage Tolerance** | Attribute ensuring that damage can be detected before it causes structural failure |
| **Fail-Safe** | Design approach where failure of one element does not cause failure of the structure |
| **Safe-Life** | Design approach based on replacement before fatigue life is exhausted |

---

## 5. Hazard Types (Wing Domain)

| Hazard Category | Description | Examples |
| :-- | :-- | :-- |
| **Structural Failure** | Loss of structural integrity | Spar fracture, skin rupture |
| **Aeroelastic Instability** | Flutter, divergence, control reversal | Wing flutter |
| **Control Surface Failure** | Loss or malfunction of movable surfaces | Aileron jam, flap asymmetry |
| **Fuel System Hazard** | Leakage, fire, explosion | Wing tank leak |
| **Ice Protection Failure** | Loss of ice protection | Leading edge ice accumulation |

---

## 6. Analysis Method Definitions

| Method | Definition | Reference |
| :-- | :-- | :-- |
| **FHA** | Functional Hazard Assessment — identifies hazards and classifies severity | [ARP4761](https://www.sae.org/standards/content/arp4761/) |
| **FTA** | Fault Tree Analysis — deductive analysis of failure combinations | [ARP4761](https://www.sae.org/standards/content/arp4761/) |
| **FMEA/FMECA** | Failure Modes and Effects (Criticality) Analysis — inductive analysis of failure effects | [ARP4761](https://www.sae.org/standards/content/arp4761/) |
| **ZSA** | Zonal Safety Analysis — identifies hazards from installation and zone effects | [ARP4761](https://www.sae.org/standards/content/arp4761/) |
| **CCA** | Common Cause Analysis — identifies common failures across systems | [ARP4761](https://www.sae.org/standards/content/arp4761/) |

---

## 7. Abbreviations

| Abbreviation | Meaning |
| :-- | :-- |
| CCA | Common Cause Analysis |
| DT | Damage Tolerance |
| FHA | Functional Hazard Assessment |
| FMEA | Failure Modes and Effects Analysis |
| FTA | Fault Tree Analysis |
| PSSA | Preliminary System Safety Assessment |
| SHM | Structural Health Monitoring |
| SSA | System Safety Assessment |
| ZSA | Zonal Safety Analysis |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** — Subject to human review and approval.  
- Human approver: _[to be completed]_.  
- Repository: `AMPEL360-BWB-H2-Hy-E`  
- Last AI update: 2025-11-29
