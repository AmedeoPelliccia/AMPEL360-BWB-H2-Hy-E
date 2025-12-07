# 03-00-06-04-04A - Thrust Performance Analysis

## 1. Purpose
Define the methodology for analyzing the thrust and propulsive performance of the AMPEL360 BWB-H2-Hy-E aircraft propulsion system, ensuring adequate thrust for all flight phases, optimizing efficiency, and validating compliance with performance requirements.

## 2. Scope
This document covers:
- Thrust requirements for all flight phases
- Propulsor performance analysis (fan, propeller, or ducted fan)
- Electric motor and drive system efficiency
- Boundary layer ingestion (BLI) effects
- Distributed propulsion integration benefits
- Propulsive efficiency optimization
- Performance across the flight envelope

## 3. Applicable Documents
- [EASA CS-25 Subpart B](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Flight (Performance)
- [SAE AIR1678](https://www.sae.org/standards/content/air1678/) - Aircraft Propulsion System Performance Station Designation
- [NASA Technical Memorandum on BLI](https://ntrs.nasa.gov/) - Boundary Layer Ingestion Research
- Related to [ATA 61](https://en.wikipedia.org/wiki/ATA_100) - Propellers/Propulsors, [ATA 72](https://en.wikipedia.org/wiki/ATA_100) - Engine

## 4. Description

### 4.1 Overview
Thrust performance analysis ensures the propulsion system provides adequate thrust for takeoff, climb, cruise, and landing while maximizing propulsive efficiency. For the BWB-H2-Hy-E, the distributed electric propulsion system with boundary layer ingestion (BLI) offers unique efficiency benefits that must be accurately characterized and validated.

### 4.2 Requirements
**Thrust Requirements per Flight Phase:**

1. **Takeoff (CS-25.105-109)**
   - Sufficient thrust for takeoff distance within field length limits
   - One engine inoperative (OEI) capability
   - Thrust available: TBD kN total (all engines)
   - V1, VR, V2 speeds achievable

2. **Climb (CS-25.111-123)**
   - Minimum climb gradient with OEI
   - Enroute climb performance (drift down)
   - Climb to cruise altitude in acceptable time
   - Thrust-to-weight ratio: TBD at MTOW

3. **Cruise (CS-25.125)**
   - Thrust equals drag at cruise speed and altitude
   - Efficient cruise for maximum range
   - Typical cruise: Mach 0.78-0.82 at 35,000-41,000 ft
   - Specific air range (SAR): TBD nm/kg H2

4. **Descent and Approach**
   - Thrust modulation for speed control
   - Go-around thrust availability
   - OEI approach capability

5. **Emergency (CS-25.143)**
   - Sufficient thrust for emergency maneuvers
   - OEI thrust for safe landing

**Propulsive Efficiency Targets:**
- **Overall Propulsive Efficiency:** >85% (with BLI benefit)
- **Propulsor Efficiency:** >90% (fan or propeller)
- **Electric Motor Efficiency:** >95%
- **Power Electronics Efficiency:** >98%
- **Fuel Cell Efficiency:** >50% (H2 LHV to DC power)

### 4.3 Methodology
**Analysis Process:**

1. **Define Operating Points**
   - Identify key flight conditions (takeoff, climb, cruise, descent)
   - Define ambient conditions (altitude, temperature, Mach number)
   - Specify aircraft weight and configuration

2. **Propulsor Performance Modeling**
   - Fan/propeller performance maps (thrust vs. RPM, pressure ratio)
   - CFD analysis for aerodynamic performance
   - Account for installation effects (nacelle, pylons)
   - Model BLI effects on propulsor inflow

3. **Boundary Layer Ingestion (BLI) Analysis**
   - CFD simulation of BWB airframe boundary layer
   - Propulsor ingestion of low-momentum flow
   - Power savings coefficient (PSC) calculation
   - Distortion effects on fan stability and efficiency

   **BLI Benefit:**
   ```
   Power Saving = (P_noBLI - P_BLI) / P_noBLI × 100%
   Typical: 5-10% power reduction with BLI
   ```

4. **Electric Motor and Drive System**
   - Motor efficiency map (torque vs. speed)
   - Drive electronics losses (DC-DC converter, inverter)
   - Cable and connection losses

5. **Thrust Calculation**
   - Thrust = ṁ × (V_exit - V_flight) + (P_exit - P_amb) × A_exit
   - Where:
     - ṁ = mass flow rate through propulsor
     - V_exit = propulsor exit velocity
     - V_flight = aircraft flight velocity
     - P_exit = propulsor exit pressure
     - A_exit = propulsor exit area

6. **Performance Integration**
   - Sum thrust from all propulsors
   - Account for thrust lapse with altitude and speed
   - Calculate available thrust across flight envelope
   - Compare to required thrust from aircraft drag polar

7. **Efficiency Optimization**
   - Optimize propulsor RPM for each flight condition
   - Balance thrust distribution among propulsors
   - Maximize BLI benefit through airframe-propulsion integration
   - Minimize electrical losses

**Distributed Propulsion Benefits:**
- **Redundancy:** Multiple propulsors enable OEI operation
- **Efficiency:** Smaller, distributed fans operate at higher efficiency
- **BLI:** Integration with airframe enables boundary layer ingestion
- **Noise Reduction:** Distributed smaller sources reduce peak noise
- **Flexibility:** Independent control of each propulsor for yaw control

**Analysis Tools:**
- CFD: ANSYS Fluent, OpenFOAM (BLI, propulsor aerodynamics)
- Propulsor design: Fan design codes, blade element momentum theory
- System modeling: MATLAB/Simulink, Modelica (electric drive system)
- Aircraft performance: In-house or commercial tools (FlightStream, AVL)

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Thrust Performance Analysis Plan | Markdown/PDF | Propulsion Lead | Project start |
| Propulsor Performance Maps | CSV/Excel/PDF | Aerodynamics Engineer | PDR |
| BLI Analysis Report | PDF/Markdown | Aerodynamics Engineer | PDR |
| Electric Drive System Efficiency | Excel/Markdown | Propulsion Engineer | PDR |
| Thrust vs. Flight Envelope | CSV/Excel/Plots | Propulsion Engineer | CDR |
| Performance Validation Report | PDF/Markdown | Flight Test Engineer | Post-flight test |

## 6. Verification & Validation
**Acceptance Criteria:**
- Thrust available exceeds required thrust for all flight phases
- Propulsive efficiency meets or exceeds targets
- BLI benefit validated through CFD and testing
- Performance predictions agree with flight test data within ±5%
- OEI performance meets CS-25 requirements
- Range and endurance meet mission requirements

**Verification Methods:**
- CFD analysis for propulsor and BLI performance
- Wind tunnel testing of propulsor models
- Ground testing of electric motor and drive system
- Engine test cell (or equivalent) for propulsion system
- Flight testing for full system validation

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 05](https://en.wikipedia.org/wiki/ATA_100) - Time Limits/Maintenance Checks (thrust deterioration)
  - [ATA 61](https://en.wikipedia.org/wiki/ATA_100) - Propellers/Propulsors
  - [ATA 72](https://en.wikipedia.org/wiki/ATA_100) - Engine (electric propulsion)
  - [ATA 73](https://en.wikipedia.org/wiki/ATA_100) - Engine Fuel and Control (thrust control)
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-04-01A H2 Propulsion Integration](./03-00-06-04-01A_H2_Propulsion_Integration.md)
  - [03-00-06-04-02A Electric Motor Specifications](./03-00-06-04-02A_Electric_Motor_Specifications.md)
  - [03-00-06-07-02A Test Procedures](../03-00-06-07_Test_Engineering/03-00-06-07-02A_Test_Procedures.md)

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
