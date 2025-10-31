# 00-10-01 Aircraft Description — Requirements

## Purpose
Define the top-level aircraft requirements for the AMPEL360-BWB-H₂-Hy-E configuration.  
Each requirement below es **hipervinculado** a su propia carpeta de detalle en `03_REQUIREMENTS/`.

---

## 1. General Performance Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-00-01](./RQ-00-01/REQ.md) | Cruise Mach number | 0.78 | CS-25.333 |
| [RQ-00-02](./RQ-00-02/REQ.md) | Design range | 3,500 km (zero-emission mode) | Mission analysis v1.0 |
| [RQ-00-03](./RQ-00-03/REQ.md) | Payload capacity | 180 pax / 20,000 kg cargo eq. | Concept baseline |
| [RQ-00-04](./RQ-00-04/REQ.md) | Takeoff field length (MTOW) | ≤ 2,000 m | CS-25.107 |
| [RQ-00-05](./RQ-00-05/REQ.md) | Approach speed (Vapp @ MLW) | ≤ 135 kt | CS-25.125 |

---

## 2. Propulsion and Energy Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-10-01](./RQ-10-01/REQ.md) | Primary energy source | LH₂ via PEM fuel-cell stacks | ATA 28 / ATA 24 |
| [RQ-10-02](./RQ-10-02/REQ.md) | Hybrid storage | Closed-loop CO₂ battery | ATA 28 / ATA 49 |
| [RQ-10-03](./RQ-10-03/REQ.md) | Secondary fuel interface | SAF (Jet-A compatible) | ATA 28 |
| [RQ-10-04](./RQ-10-04/REQ.md) | Propulsion configuration | 8 × open-fan electric propulsors | ATA 61 |
| [RQ-10-05](./RQ-10-05/REQ.md) | Total installed power | 15 MW (nominal) | System architecture v0.9 |
| [RQ-10-06](./RQ-10-06/REQ.md) | Peak load buffering | ±20 % transient via CO₂ loop | Energy management spec |

---

## 3. Environmental and Safety Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-20-01](./RQ-20-01/REQ.md) | In-flight CO₂ emissions | 0 g/km (H₂ mode) | Sustainability framework |
| [RQ-20-02](./RQ-20-02/REQ.md) | Ground refueling safety | ISO 19880-1 compliance | H₂ infrastructure |
| [RQ-20-03](./RQ-20-03/REQ.md) | Cryogenic boil-off management | ≤ 0.1 %/h | ATA 28-30 |
| [RQ-20-04](./RQ-20-04/REQ.md) | Acoustic signature | -25 dB vs. CS-36 | Noise model BWB-RevA |
| [RQ-20-05](./RQ-20-05/REQ.md) | Electrical isolation fault tolerance | Dual-channel detect < 10 ms | DO-160G |
| [RQ-20-06](./RQ-20-06/REQ.md) | Fire suppression | Autonomous inerting & HALT logic | ATA 26 |

---

## 4. Digital and Traceability Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-30-01](./RQ-30-01/REQ.md) | Digital twin fidelity | ≥ 99.5 % parameter sync | OPT-IN Digital Thread |
| [RQ-30-02](./RQ-30-02/REQ.md) | Configuration control | DPP + blockchain automation | ATA 93 |
| [RQ-30-03](./RQ-30-03/REQ.md) | Maintenance scheduling | Condition-based predictive | ATA 01 |
| [RQ-30-04](./RQ-30-04/REQ.md) | Data interoperability | S1000D Issue 6 / ASD-STE100 | Docs baseline |
| [RQ-30-05](./RQ-30-05/REQ.md) | Safety traceability | Req → Hazard → Test linkage | ARP4754A trace tree |

---

## 5. Certification and Compliance Targets
| ID | Requirement | Objective | Reference |
|----|-------------|----------|----------|
| [RQ-40-01](./RQ-40-01/REQ.md) | Certification basis | EASA CS-25 / FAA Part 25 | Regulatory |
| [RQ-40-02](./RQ-40-02/REQ.md) | Hydrogen systems | SC-H2, SAE ARP8677 | Energy domain |
| [RQ-40-03](./RQ-40-03/REQ.md) | Software | DO-178C Level A | Avionics |
| [RQ-40-04](./RQ-40-04/REQ.md) | Hardware | DO-254 Level A | Electronic modules |
| [RQ-40-05](./RQ-40-05/REQ.md) | System safety | ARP4761 / ARP4754A | Safety case |
| [RQ-40-06](./RQ-40-06/REQ.md) | Environmental | ISO 14001 / 50001 | Sustainability mgmt |

---

## 6. Traceability Model
All requirements map to verification artefacts through the OPT-IN matrix:

