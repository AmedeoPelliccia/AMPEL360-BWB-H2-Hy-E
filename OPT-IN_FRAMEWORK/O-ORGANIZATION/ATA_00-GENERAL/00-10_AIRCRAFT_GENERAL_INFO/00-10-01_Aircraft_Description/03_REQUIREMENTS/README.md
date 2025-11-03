# 00-10-01 Aircraft Description — Requirements

## Purpose
Define the top-level aircraft requirements for the AMPEL360-BWB-H₂-Hy-E configuration.  
Each requirement below es **hipervinculado** a su propia carpeta de detalle en `03_REQUIREMENTS/`.

---

## 1. General Performance Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-00-01](./RQ-00-01_Cruise_Mach_Number/REQ.md) | Cruise Mach Number | 0.78 | CS-25.333 |
| [RQ-00-02](./RQ-00-02_Design_Range_Zero-Emission_Mode/REQ.md) | Design Range (Zero-Emission Mode) | 3,500 km (zero-emission mode) | Mission analysis v1.0 |
| [RQ-00-03](./RQ-00-03_Passenger_Capacity_and_Cabin_Configuration/REQ.md) | Passenger Capacity and Cabin Configuration | 180 pax / 20,000 kg cargo eq. | Concept baseline |
| [RQ-00-04](./RQ-00-04_Hybrid-Electric_Power_Architecture_Efficiency/REQ.md) | Hybrid-Electric Power Architecture Efficiency | ≤ 2,000 m | CS-25.107 |
| [RQ-00-05](./RQ-00-05_Structural_Load_Efficiency_and_Weight_Targets/REQ.md) | Structural Load Efficiency and Weight Targets | ≤ 135 kt | CS-25.125 |

---

## 2. Propulsion and Energy Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-10-01](./RQ-10-01_Primary_Energy_Source/REQ.md) | Primary Energy Source | LH₂ via PEM fuel-cell stacks | ATA 28 / ATA 24 |
| [RQ-10-02](./RQ-10-02_Hybrid_Storage_Closed-Loop_CO2_Battery/REQ.md) | Hybrid Storage (Closed-Loop CO₂ Battery) | Closed-loop CO₂ battery | ATA 28 / ATA 49 |
| [RQ-10-03](./RQ-10-03_Secondary_Fuel_Interface_SAF/REQ.md) | Secondary Fuel Interface (SAF) | SAF (Jet-A compatible) | ATA 28 |
| [RQ-10-04](./RQ-10-04_Propulsion_Configuration_8x_Open-Fan_Electric_Propulsors/REQ.md) | Propulsion Configuration (8 × Open-Fan Electric Propulsors) | 8 × open-fan electric propulsors | ATA 61 |
| [RQ-10-05](./RQ-10-05_Total_Installed_Power_15_MW_Nominal/REQ.md) | Total Installed Power (15 MW Nominal) | 15 MW (nominal) | System architecture v0.9 |
| [RQ-10-06](./RQ-10-06_Peak_Load_Buffering_20pct_Transient_via_CO2_Loop/REQ.md) | Peak Load Buffering (±20% Transient via CO₂ Loop) | ±20 % transient via CO₂ loop | Energy management spec |

---

## 3. Environmental and Safety Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-20-01](./RQ-20-01_In-Flight_CO2_Emissions_0_gkm_in_H2_Mode/REQ.md) | In-Flight CO₂ Emissions (0 g/km in H₂ Mode) | 0 g/km (H₂ mode) | Sustainability framework |
| [RQ-20-02](./RQ-20-02_Ground_Refueling_Safety_ISO_19880-1_Compliance/REQ.md) | Ground Refueling Safety (ISO 19880-1 Compliance) | ISO 19880-1 compliance | H₂ infrastructure |
| [RQ-20-03](./RQ-20-03_Cryogenic_Boil-Off_Management_0.1pct_h/REQ.md) | Cryogenic Boil-Off Management (≤ 0.1%/h) | ≤ 0.1 %/h | ATA 28-30 |
| [RQ-20-04](./RQ-20-04_Acoustic_Signature_-25_dB_vs_CS-36/REQ.md) | Acoustic Signature (-25 dB vs. CS-36) | -25 dB vs. CS-36 | Noise model BWB-RevA |
| [RQ-20-05](./RQ-20-05_Electrical_Isolation_Fault_Tolerance_Dual-Channel_Detect_10ms/REQ.md) | Electrical Isolation Fault Tolerance (Dual-Channel Detect < 10 ms) | Dual-channel detect < 10 ms | DO-160G |
| [RQ-20-06](./RQ-20-06_Fire_Suppression_Autonomous_Inerting_HALT_Logic/REQ.md) | Fire Suppression (Autonomous Inerting & HALT Logic) | Autonomous inerting & HALT logic | ATA 26 |

---

## 4. Digital and Traceability Requirements
| ID | Requirement | Target / Value | Reference |
|----|-------------|----------------|----------|
| [RQ-30-01](./RQ-30-01_Digital_Twin_Fidelity_99.5pct_Parameter_Sync/REQ.md) | Digital Twin Fidelity (≥ 99.5% Parameter Sync) | ≥ 99.5 % parameter sync | OPT-IN Digital Thread |
| [RQ-30-02](./RQ-30-02_Configuration_Control_DPP_Blockchain_Automation/REQ.md) | Configuration Control (DPP + Blockchain Automation) | DPP + blockchain automation | ATA 93 |
| [RQ-30-03](./RQ-30-03_Maintenance_Scheduling_Condition-Based_Predictive/REQ.md) | Maintenance Scheduling (Condition-Based Predictive) | Condition-based predictive | ATA 01 |
| [RQ-30-04](./RQ-30-04_Data_Interoperability_S1000D_Issue_6_ASD-STE100/REQ.md) | Data Interoperability (S1000D Issue 6 / ASD-STE100) | S1000D Issue 6 / ASD-STE100 | Docs baseline |
| [RQ-30-05](./RQ-30-05_Safety_Traceability_Req_Hazard_Test_Linkage/REQ.md) | Safety Traceability (Req → Hazard → Test Linkage) | Req → Hazard → Test linkage | ARP4754A trace tree |

---

## 5. Certification and Compliance Targets
| ID | Requirement | Objective | Reference |
|----|-------------|----------|----------|
| [RQ-40-01](./RQ-40-01_Certification_Basis_EASA_CS-25_FAA_Part_25/REQ.md) | Certification Basis (EASA CS-25 / FAA Part 25) | EASA CS-25 / FAA Part 25 | Regulatory |
| [RQ-40-02](./RQ-40-02_Hydrogen_Systems_SC-H2_SAE_ARP8677/REQ.md) | Hydrogen Systems (SC-H2, SAE ARP8677) | SC-H2, SAE ARP8677 | Energy domain |
| [RQ-40-03](./RQ-40-03_Software_DO-178C_Level_A/REQ.md) | Software (DO-178C Level A) | DO-178C Level A | Avionics |
| [RQ-40-04](./RQ-40-04_Hardware_DO-254_Level_A/REQ.md) | Hardware (DO-254 Level A) | DO-254 Level A | Electronic modules |
| [RQ-40-05](./RQ-40-05_System_Safety_ARP4761_ARP4754A/REQ.md) | System Safety (ARP4761 / ARP4754A) | ARP4761 / ARP4754A | Safety case |
| [RQ-40-06](./RQ-40-06_Environmental_ISO_14001_50001/REQ.md) | Environmental (ISO 14001 / 50001) | ISO 14001 / 50001 | Sustainability mgmt |

---

## 6. Traceability Model
All requirements map to verification artefacts through the OPT-IN matrix:

