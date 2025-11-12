# 00-10-01 Aircraft Description — Safety Overview

## Purpose  
Define the global safety principles that govern the AMPEL360-BWB-H₂-Hy-E aircraft architecture.  
This document establishes how safety objectives cascade from system design to certification under the OPT-IN framework.

## Safety Philosophy  
Safety is embedded as a **design driver**, not a constraint. The AMPEL360 program applies a **system-of-systems safety architecture** integrating airworthiness, energy management, and digital assurance layers.

Key principles:
1. **Top–down functional hazard analysis (FHA):**  
   All operational and system-level functions are categorized by failure effect severity in accordance with ARP4761.
2. **Probabilistic safety targets:**  
   The aircraft-level catastrophic failure probability ≤ 10⁻⁹ per flight hour, distributed across systems using quantitative safety allocation.
3. **Energy-domain hazard segregation:**  
   Independent containment and isolation of hydrogen, CO₂ loop, and electrical HVDC systems.  
   Double containment, continuous leak detection, and real-time inerting logic reduce energy interaction risk.
4. **Fire and explosion prevention:**  
   Hydrogen zones follow ISO 19880 and SAE ARP8677 standards with ventilation, non-sparking materials, and hydrogen sensors networked to the OMS.
5. **Cryogenic system safety:**  
   Pressure relief, boil-off control, and automatic vent routing designed per CS-H₂ and EASA Special Condition SC-H2.
6. **Electrical and electromagnetic protection:**  
   HVDC bus fault detection, isolation, and EMI shielding compliant with DO-160G and MIL-STD-461F.
7. **Software and autonomy assurance:**  
   All IMA applications developed to DO-178C Level A integrity with real-time health monitoring and cross-channel comparison.
8. **Integrated Safety Monitoring (ISM):**  
   Continuous model-based monitoring of temperatures, voltages, pressures, and vibration signatures enables early fault detection.

## Safety Lifecycle Integration  
- Safety assessments (FHA, PSSA, SSA) linked directly to design baselines in the OPT-IN digital thread.  
- Verification and validation activities traced through model-based evidence in **V&V skeletons** of each ATA.  
- Safety data feeds into the **maintenance program (ATA 01)** and **operational manuals (ATA 02)**.  
- Every hazard has a digital lineage from requirement → design → verification → certification artifact.

## Interfaces  
- **Certification:** EASA/FAA authorities, Design Organisation Approval (DOA), and Continuing Airworthiness Management Organisation (CAMO).  
- **Engineering:** Systems safety, reliability, and design assurance teams.  
- **Operations:** Flight operations, maintenance, and ground safety engineering.

## Status  
Baseline system safety concept defined — integration with detailed PSSA underway for hybrid-energy systems and cryogenic loops.
