# 03-00-06-04-02A - Electric Motor Specifications

## 1. Purpose
Define the specifications and requirements for electric motors used in the AMPEL360 BWB-H2-Hy-E distributed propulsion system, ensuring adequate thrust, efficiency, reliability, and integration compatibility with the aircraft electrical and propulsion systems.

## 2. Scope
This document covers:
- Electric motor type selection and technology
- Performance specifications (power, torque, speed)
- Electrical characteristics and interfaces
- Thermal management requirements
- Mechanical integration and mounting
- Control system requirements
- Reliability and maintenance considerations

## 3. Applicable Documents
- [EASA CS-E](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-e-engines) - Engines (adapted for electric propulsion)
- [DO-160G](https://www.rtca.org/content/standards-guidance-materials) - Environmental Conditions and Test Procedures for Airborne Equipment
- [MIL-STD-704F](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35789) - Aircraft Electric Power Characteristics
- [SAE ARP5692](https://www.sae.org/standards/content/arp5692/) - Electric Motor Specification

## 4. Description

### 4.1 Overview
Electric motors convert electrical power from the fuel cell/battery system into mechanical shaft power to drive propulsors. For the BWB-H2-Hy-E, a distributed propulsion architecture is envisioned with multiple electric motors driving fans or propellers, enabling redundancy, boundary layer ingestion (BLI), and improved propulsive efficiency.

### 4.2 Requirements
**Performance Requirements:**
- **Power Rating:** TBD kW per motor (based on thrust requirements)
- **Rated Speed:** TBD RPM (typical 3,000-10,000 RPM for direct-drive, higher for geared)
- **Torque:** Continuous and peak torque specifications
- **Efficiency:** >95% at cruise conditions, >90% across operating range
- **Power Density:** >5 kW/kg target (motor only, excluding drive electronics)
- **Operating Envelope:** Sea level to 45,000 ft altitude, -55°C to +85°C ambient

**Motor Type Selection:**
Candidate technologies:
1. **Permanent Magnet Synchronous Motor (PMSM)**
   - High efficiency and power density
   - Compact and lightweight
   - Requires power electronics for control
   - Demagnetization risk at high temperatures

2. **Switched Reluctance Motor (SRM)**
   - Robust and fault-tolerant
   - No permanent magnets (lower cost, supply chain resilience)
   - Lower efficiency than PMSM
   - Higher acoustic noise

3. **Wound Rotor Synchronous Motor (WRSM)**
   - No permanent magnets
   - Controllable power factor
   - Requires slip rings or brushless exciter

**Recommended:** PMSM for highest efficiency and power density.

**Electrical Interface:**
- **Supply Voltage:** TBD VDC (typical 540V, 800V, or higher for aircraft)
- **Current:** Based on power and voltage (P = V × I × √3 × PF)
- **Control:** Three-phase AC, variable frequency drive (VFD)
- **Protection:** Over-current, over-voltage, over-temperature protection
- **Isolation:** High-voltage isolation per DO-160G

**Thermal Management:**
- **Cooling Method:** Liquid cooling (glycol/water) or air cooling
- **Maximum Winding Temperature:** 180°C (Class H insulation)
- **Thermal Sensors:** Thermocouples or RTDs in windings and bearings
- **Heat Rejection:** TBD kW at maximum power

**Mechanical Integration:**
- **Mounting:** Flange-mounted to propulsor gearbox or direct-drive to fan
- **Alignment:** Precision alignment required (<0.1 mm runout)
- **Vibration:** Withstand aircraft vibration per DO-160G Category S
- **Bearings:** Precision ball or roller bearings, grease-lubricated or oil-lubricated
- **Shaft Seals:** Environmental seals to prevent moisture/contamination ingress

**Control System:**
- **Motor Controller:** Integrated VFD with torque/speed control
- **Communication:** CAN bus or ARINC 429 for aircraft integration
- **Sensors:** Rotor position (resolver or encoder), temperature, vibration
- **Control Modes:** Speed control, torque control, power limit
- **Redundancy:** Dual-redundant control channels for safety-critical propulsion

### 4.3 Methodology
**Specification Development Process:**

1. **Mission Analysis**
   - Define thrust requirements from aircraft performance analysis
   - Determine power requirements accounting for propulsor efficiency
   - Define operating envelope (altitude, speed, temperature)

2. **Technology Trade Study**
   - Evaluate motor technologies (PMSM vs. SRM vs. WRSM)
   - Compare power density, efficiency, cost, reliability
   - Select optimal motor type

3. **Preliminary Design**
   - Size motor based on power and speed requirements
   - Estimate weight and dimensions
   - Define cooling approach

4. **Detailed Specification**
   - Document performance requirements
   - Specify electrical, thermal, mechanical interfaces
   - Define test requirements and acceptance criteria

5. **Supplier Selection**
   - Issue RFQ (Request for Quotation) to motor suppliers
   - Evaluate proposals against specifications
   - Select supplier and award contract

6. **Development and Testing**
   - Supplier develops motor per specifications
   - Conduct factory acceptance testing (FAT)
   - Integration testing with motor controller and propulsor
   - Qualification testing per DO-160G

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Electric Motor Specification | Markdown/PDF | Propulsion Engineer | PDR |
| Motor Trade Study Report | Markdown/PDF | Propulsion Engineer | Conceptual design |
| Motor Sizing Calculations | Excel/Markdown | Propulsion Engineer | PDR |
| Supplier RFQ Package | PDF | Procurement | PDR |
| Motor Test Plan | Markdown | Test Engineer | CDR |
| Motor Qualification Report | PDF | Supplier/Test Engineer | Pre-flight |

## 6. Verification & Validation
**Acceptance Criteria:**
- Motor meets all performance specifications
- Efficiency validated across operating range
- Thermal management adequate for continuous operation
- Electrical interfaces compatible with aircraft power system
- Motor passes environmental qualification per DO-160G
- Reliability targets met (MTBF, failure rates)

**Test Methods:**
- Dynamometer testing for performance validation
- Thermal testing (steady-state and transient)
- Endurance testing (100+ hours at rated power)
- Environmental testing (temperature, altitude, vibration per DO-160G)
- Electrical testing (insulation resistance, hi-pot)
- Integration testing with motor controller and propulsor

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 24](https://en.wikipedia.org/wiki/ATA_100) - Electrical Power
  - [ATA 61](https://en.wikipedia.org/wiki/ATA_100) - Propellers/Propulsors (motor-propulsor integration)
  - [ATA 72](https://en.wikipedia.org/wiki/ATA_100) - Engine (electric motor as prime mover)
  - [ATA 80](https://en.wikipedia.org/wiki/ATA_100) - Starting (motor startup)
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-04-01A H2 Propulsion Integration](./03-00-06-04-01A_H2_Propulsion_Integration.md)
  - [03-00-06-04-04A Thrust Performance Analysis](./03-00-06-04-04A_Thrust_Performance_Analysis.md)
  - [03-00-06-05-03A Hardware Integration](../03-00-06-05_Avionics_Engineering/03-00-06-05-03A_Hardware_Integration.md)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AI (GitHub Copilot) | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
