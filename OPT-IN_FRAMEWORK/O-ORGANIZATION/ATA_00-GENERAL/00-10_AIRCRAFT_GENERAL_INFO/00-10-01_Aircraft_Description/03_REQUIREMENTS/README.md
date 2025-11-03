# 00-10-01 Aircraft Description — Requirements

## Purpose
Define the top-level aircraft requirements for the AMPEL360-BWB-H₂-Hy-E configuration.  
Each requirement below es **hipervinculado** a su propia carpeta de detalle en `03_REQUIREMENTS/`.

---

## 1. General Performance Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-00-01](./RQ-00-01_Cruise-Mach-Number/REQ.md) | Cruise Mach number | 0.78 | CS-25.333 |
| [RQ-00-02](./RQ-00-02_Design-Range-Zero-Emission-Mode/REQ.md) | Design range | 3,500 km (zero-emission mode) | Mission analysis v1.0 |
| [RQ-00-03](./RQ-00-03_Passenger-Capacity-Cabin-Configuration/REQ.md) | Payload capacity | 180 pax / 20,000 kg cargo eq. | Concept baseline |
| [RQ-00-04](./RQ-00-04_Hybrid-Electric-Power-Architecture-Efficiency/REQ.md) | Takeoff field length (MTOW) | ≤ 2,000 m | CS-25.107 |
| [RQ-00-05](./RQ-00-05_Structural-Load-Efficiency-Weight-Targets/REQ.md) | Approach speed (Vapp @ MLW) | ≤ 135 kt | CS-25.125 |

---

## 2. Propulsion and Energy Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-10-01](./RQ-10-01_Primary-Energy-Source/REQ.md) | Primary energy source | LH₂ via PEM fuel-cell stacks | ATA 28 / ATA 24 |
| [RQ-10-02](./RQ-10-02_Hybrid-Storage-Closed-Loop-CO2-Battery/REQ.md) | Hybrid storage | Closed-loop CO₂ battery | ATA 28 / ATA 49 |
| [RQ-10-03](./RQ-10-03_Secondary-Fuel-Interface-SAF/REQ.md) | Secondary fuel interface | SAF (Jet-A compatible) | ATA 28 |
| [RQ-10-04](./RQ-10-04_Propulsion-Configuration-8x-Open-Fan-Electric-Propulsors/REQ.md) | Propulsion configuration | 8 × open-fan electric propulsors | ATA 61 |
| [RQ-10-05](./RQ-10-05_Total-Installed-Power-15MW-Nominal/REQ.md) | Total installed power | 15 MW (nominal) | System architecture v0.9 |
| [RQ-10-06](./RQ-10-06_Peak-Load-Buffering-20pct-Transient-CO2-Loop/REQ.md) | Peak load buffering | ±20 % transient via CO₂ loop | Energy management spec |

---

## 3. Environmental and Safety Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-20-01](./RQ-20-01_In-Flight-CO2-Emissions-0g-km-H2-Mode/REQ.md) | In-flight CO₂ emissions | 0 g/km (H₂ mode) | Sustainability framework |
| [RQ-20-02](./RQ-20-02_Ground-Refueling-Safety-ISO-19880-1-Compliance/REQ.md) | Ground refueling safety | ISO 19880-1 compliance | H₂ infrastructure |
| [RQ-20-03](./RQ-20-03_Cryogenic-Boil-Off-Management-0.1pct-h/REQ.md) | Cryogenic boil-off management | ≤ 0.1 %/h | ATA 28-30 |
| [RQ-20-04](./RQ-20-04_Acoustic-Signature-minus-25dB-vs-CS-36/REQ.md) | Acoustic signature | -25 dB vs. CS-36 | Noise model BWB-RevA |
| [RQ-20-05](./RQ-20-05_Electrical-Isolation-Fault-Tolerance-Dual-Channel-Detect-10ms/REQ.md) | Electrical isolation fault tolerance | Dual-channel detect < 10 ms | DO-160G |
| [RQ-20-06](./RQ-20-06_Fire-Suppression-Autonomous-Inerting-HALT-Logic/REQ.md) | Fire suppression | Autonomous inerting & HALT logic | ATA 26 |

---

## 4. Digital and Traceability Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-30-01](./RQ-30-01_Digital-Twin-Fidelity-99.5pct-Parameter-Sync/REQ.md) | Digital twin fidelity | ≥ 99.5 % parameter sync | OPT-IN Digital Thread |
| [RQ-30-02](./RQ-30-02_Configuration-Control-DPP-Blockchain-Automation/REQ.md) | Configuration control | DPP + blockchain automation | ATA 93 |
| [RQ-30-03](./RQ-30-03_Maintenance-Scheduling-Condition-Based-Predictive/REQ.md) | Maintenance scheduling | Condition-based predictive | ATA 01 |
| [RQ-30-04](./RQ-30-04_Data-Interoperability-S1000D-Issue-6-ASD-STE100/REQ.md) | Data interoperability | S1000D Issue 6 / ASD-STE100 | Docs baseline |
| [RQ-30-05](./RQ-30-05_Safety-Traceability-Req-Hazard-Test-Linkage/REQ.md) | Safety traceability | Req → Hazard → Test linkage | ARP4754A trace tree |

---

## 5. Certification and Compliance Targets
| ID | Requirement | Objective | Reference |
|----|-------------|----------|----------|
| [RQ-40-01](./RQ-40-01_Certification-Basis-EASA-CS-25-FAA-Part-25/REQ.md) | Certification basis | EASA CS-25 / FAA Part 25 | Regulatory |
| [RQ-40-02](./RQ-40-02_Hydrogen-Systems-SC-H2-SAE-ARP8677/REQ.md) | Hydrogen systems | SC-H2, SAE ARP8677 | Energy domain |
| [RQ-40-03](./RQ-40-03_Software-DO-178C-Level-A/REQ.md) | Software | DO-178C Level A | Avionics |
| [RQ-40-04](./RQ-40-04_Hardware-DO-254-Level-A/REQ.md) | Hardware | DO-254 Level A | Electronic modules |
| [RQ-40-05](./RQ-40-05_System-Safety-ARP4761-ARP4754A/REQ.md) | System safety | ARP4761 / ARP4754A | Safety case |
| [RQ-40-06](./RQ-40-06_Environmental-ISO-14001-50001/REQ.md) | Environmental | ISO 14001 / 50001 | Sustainability mgmt |

---

## 6. Traceability Model
All requirements map to verification artefacts through the OPT-IN matrix:

