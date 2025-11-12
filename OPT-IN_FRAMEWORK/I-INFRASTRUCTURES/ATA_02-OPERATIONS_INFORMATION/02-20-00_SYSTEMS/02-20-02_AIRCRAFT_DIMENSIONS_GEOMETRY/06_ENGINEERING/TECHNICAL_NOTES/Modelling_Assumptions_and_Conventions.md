# Modelling Assumptions and Conventions

**Document ID:** 02-11-00-TN-001  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Status:** Draft  
**Date:** 2025-11-10

---

## 1. Purpose

Document modelling assumptions and conventions used across all engineering analyses to ensure consistency and traceability.

---

## 2. General Assumptions

### 2.1 Analysis Scope
- **Design point:** Cruise at Mach 0.82, FL410, ISA conditions
- **Design life:** 60,000 flight hours (design service goal), 90,000 flight hours (design service objective)
- **Aircraft configuration:** As defined in `04_DESIGN` frozen baseline

### 2.2 Regulatory Basis
- **Certification basis:** CS-25 (latest amendment applicable at certification)
- **Special conditions:** BWB configuration, H₂ fuel system (to be defined)
- **Safety factors:** Per CS-25.303 (ultimate load = 1.5 × limit load)

---

## 3. Structural Analysis Assumptions

### 3.1 Load Application
- **Inertia relief:** Applied at aircraft CG for symmetric maneuver loads
- **Load distribution:** Per global FEM, validated against hand calculations
- **Aerodynamic loads:** From CFD or handbook methods, applied as distributed pressures

### 3.2 Material Properties
- **Allowables:** A-basis for single load path (99% reliability, 95% confidence), B-basis for multiple load path (90% reliability, 95% confidence)
- **Temperature:** Room temperature (RT) unless otherwise specified
- **Moisture:** Ambient moisture for composites (conditioned to equilibrium)
- **Knockdown factors:** Applied per MIL-HDBK-5J and CMH-17

### 3.3 Connections and Joints
- **Fasteners:** Modeled with RBE2/RBE3 elements or detailed finite elements
- **Fitting factors:** 1.15 applied per CS-25.625
- **Bearing stress:** Calculated per net section and bearing allowables

---

## 4. Aerodynamic Analysis Assumptions

### 4.1 Flow Conditions
- **Steady-state:** All aerodynamic analyses assume steady flow unless dynamic analysis required
- **Turbulence:** Fully turbulent flow (no laminar-turbulent transition modeled unless specified)
- **Compressibility:** Mach number effects included for M > 0.3

### 4.2 Geometry Idealization
- **Surface quality:** Smooth surface (no excrescences in baseline CFD)
- **Control surfaces:** Neutral (0° deflection) unless otherwise specified
- **Landing gear:** Retracted for cruise analysis, extended for take-off/landing

### 4.3 Atmospheric Conditions
- **Standard atmosphere:** ISA (International Standard Atmosphere) per ISO 2533
- **Hot day:** ISA +10°C or ISA +15°C as specified
- **Cold day:** ISA -10°C (if required)

---

## 5. Performance Analysis Assumptions

### 5.1 Engine Performance
- **Thrust:** Per engine manufacturer data (sea level static to cruise altitude)
- **SFC:** Specific fuel consumption per engine deck (kg/kN/hr)
- **Installation losses:** 2% thrust loss for installation effects

### 5.2 Mission Profile
- **Take-off:** Brake release, acceleration, rotation, climb to 35 ft
- **Climb:** Climb to cruise altitude per standard climb schedule
- **Cruise:** Constant altitude or step-climb as specified
- **Descent:** Idle descent from cruise to approach altitude
- **Landing:** Approach, flare, touchdown, braking to full stop

### 5.3 Reserves
- **Regulatory reserves:** 5% contingency + 30 min hold + alternate (200 km)
- **Operational reserves:** Additional reserves as specified by operator

---

## 6. Weight and Balance Assumptions

### 6.1 Mass Properties
- **OEW:** Operating Empty Weight per detailed mass breakdown
- **Payload:** 400 passengers at 100 kg each + 20 kg baggage per passenger
- **Fuel:** Liquid H₂ at -253°C, density 70.8 kg/m³

### 6.2 CG Calculation
- **Reference datum:** Aircraft nose (station 0.0)
- **MAC:** Mean Aerodynamic Chord calculated from wing planform
- **CG envelope:** Forward and aft limits per stability and control analysis

---

## 7. Ground Clearance Assumptions

### 7.1 Aircraft Attitudes
- **Level static:** Aircraft on level ground, gear at static compression
- **Tail-down:** Maximum pitch angle with main gear on ground, nose gear off ground
- **Rotation:** Dynamic pitch angle during take-off rotation

### 7.2 Gear Stroke
- **Static stroke:** Gear compression under static weight
- **Dynamic stroke:** Additional compression during landing impact or taxi bump
- **Maximum stroke:** Limit of shock absorber travel

---

## 8. Simulation Assumptions

### 8.1 FEM Analysis
- **Element types:** Shell elements for skin, beam elements for stringers/frames
- **Mesh density:** Convergence study performed to ensure mesh independence
- **Contact:** Bonded contact for skin-stringer interface, frictionless for sliding surfaces

### 8.2 CFD Analysis
- **Turbulence model:** k-ω SST for attached flow, DES/LES for separated flow
- **Wall treatment:** Wall-resolved (y+ < 1) for accurate boundary layer prediction
- **Convergence:** Residuals < 10⁻⁶, force coefficients stable within 0.1%

### 8.3 Multibody Dynamics
- **Rigid bodies:** Aircraft structure modeled as rigid body with flexibility effects if required
- **Joints:** Revolute, prismatic, and spherical joints per actual mechanism
- **Contact:** Penalty method or compliant contact for ground interaction

---

## 9. Sign Conventions

### 9.1 Coordinate Systems
- **X-axis:** Positive forward (nose direction)
- **Y-axis:** Positive right (starboard wing)
- **Z-axis:** Positive up (vertical)

### 9.2 Load Factors
- **Positive:** Upward acceleration (e.g., +2.5g pull-up)
- **Negative:** Downward acceleration (e.g., -1.0g push-over)

### 9.3 Moments and Rotations
- **Positive pitch:** Nose up
- **Positive roll:** Right wing down
- **Positive yaw:** Nose right

---

## 10. Units

### 10.1 Standard Units (SI)
- **Length:** meters (m)
- **Mass:** kilograms (kg)
- **Force:** Newtons (N), kilonewtons (kN)
- **Stress:** Pascals (Pa), Megapascals (MPa)
- **Temperature:** Kelvin (K) or Celsius (°C)

### 10.2 Aviation Units (where applicable)
- **Speed:** Knots Indicated Airspeed (KIAS), Knots True Airspeed (KTAS)
- **Altitude:** feet (ft)
- **Distance:** nautical miles (nm) or kilometers (km)

---

## 11. Documentation and Traceability

### 11.1 Version Control
- All analysis models and results version-controlled per MIL-STD-483
- Major revisions tied to `04_DESIGN` baseline changes

### 11.2 Assumptions Log
- Any deviation from standard assumptions documented in analysis report
- Sensitivity studies performed for critical assumptions

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Author:** Chief Engineer – Engineering Analysis
- **Reviewed by:** Program Chief Engineer
- **Date:** 2025-11-10
