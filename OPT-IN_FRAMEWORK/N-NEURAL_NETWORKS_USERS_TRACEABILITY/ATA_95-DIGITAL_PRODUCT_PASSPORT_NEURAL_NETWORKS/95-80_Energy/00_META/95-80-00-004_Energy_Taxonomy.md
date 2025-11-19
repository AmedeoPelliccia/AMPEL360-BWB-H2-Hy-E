# 95-80-00-004 Energy Taxonomy

**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**ATA Chapter:** 95-80 (Energy)

---

## 1. Purpose

This document establishes a standardized taxonomy for energy-related terminology used throughout the AMPEL360 Energy module (95-80). It ensures consistent understanding and communication across all energy domains.

---

## 2. Energy Domains

### 2.1 Electrical Energy

**Definition**: Energy in the form of electric charge flow through conductors.

**Key Terms**:
- **Voltage (V)**: Electric potential difference, measured in Volts
- **Current (I)**: Rate of electric charge flow, measured in Amperes
- **Power (P)**: Rate of energy transfer, P = V × I, measured in Watts
- **Energy (E)**: Capacity to do work, E = P × t, measured in Watt-hours (Wh) or Joules (J)
- **Frequency (f)**: For AC systems, measured in Hertz (Hz)
- **Power Factor (PF)**: Ratio of real power to apparent power (dimensionless, 0-1)

**Sub-categories**:
- **DC (Direct Current)**: Unidirectional flow
  - 270 VDC: Primary high-voltage DC bus
  - 28 VDC: Secondary low-voltage DC bus
- **AC (Alternating Current)**: Bidirectional oscillating flow
  - 115 VAC: Single-phase AC
  - 200/115 VAC: Three-phase AC
  - 400 Hz: Standard aviation frequency

### 2.2 Chemical Energy

**Definition**: Energy stored in molecular bonds, released through chemical reactions.

**Key Terms**:
- **LHV (Lower Heating Value)**: Energy released excluding water vapor condensation heat
- **HHV (Higher Heating Value)**: Energy released including water vapor condensation heat
- **Mass Flow Rate**: kg/s or kg/h
- **Energy Content**: kWh/kg or MJ/kg
- **Stoichiometry**: Reactant-to-product molar ratios

**Application to AMPEL360**:
- **LH₂ (Liquid Hydrogen)**:
  - LHV: 33.3 kWh/kg (120 MJ/kg)
  - HHV: 39.4 kWh/kg (142 MJ/kg)
  - Storage: Cryogenic at -253°C (20 K)
  - Fuel cell reaction: 2H₂ + O₂ → 2H₂O + electrical energy + heat

### 2.3 Hydraulic Energy

**Definition**: Energy transmitted through pressurized fluid flow.

**Key Terms**:
- **Pressure (P)**: Force per unit area, measured in psi or bar
- **Flow Rate (Q)**: Volume per time, measured in L/min or GPM
- **Hydraulic Power**: P_hyd = P × Q (pressure × flow)
- **Accumulator**: Energy storage device using gas compression
- **Efficiency**: Ratio of output mechanical work to input hydraulic power

**Application to AMPEL360**:
- **System Pressure**: 5000 psi (345 bar)
- **Fluid**: Aviation hydraulic fluid (MIL-PRF-83282 or equivalent)
- **Accumulators**: Gas-charged for emergency/peak loads
- **Pumps**: Electric motor-driven (replacing engine-driven pumps)

### 2.4 Pneumatic Energy

**Definition**: Energy stored in compressed gas.

**Key Terms**:
- **Pressure (P)**: Gauge or absolute, measured in psi or bar
- **Volume (V)**: Storage capacity, measured in liters or cubic feet
- **Temperature (T)**: Affects gas density and energy content
- **Mass Flow Rate**: kg/s or SCFM (standard cubic feet per minute)
- **Ideal Gas Law**: PV = nRT

**Application to AMPEL360**:
- **Bleed Air Replacement**: Electric compressors instead of engine bleed
- **Pressure Ranges**:
  - High pressure: 200 psi (ECS, anti-ice)
  - Medium pressure: 50-100 psi (general pneumatics)
- **Storage**: Pressure vessels for demand smoothing

### 2.5 Thermal Energy

**Definition**: Energy associated with temperature and heat transfer.

**Key Terms**:
- **Temperature (T)**: Measured in °C or K
- **Heat (Q)**: Thermal energy transfer, measured in Joules or BTU
- **Heat Transfer Rate**: Power, measured in Watts or BTU/hr
- **Specific Heat Capacity (cp)**: Energy per mass per temperature, J/(kg·K)
- **Thermal Conductivity (k)**: W/(m·K)
- **Convection Coefficient (h)**: W/(m²·K)

**Application to AMPEL360**:
- **Waste Heat Sources**:
  - Fuel cell stacks: 1.0-1.5 MW thermal
  - Electric motors: 100-200 kW thermal
  - Power electronics: 50-100 kW thermal
- **Heat Sinks**:
  - LH₂ boil-off cooling
  - Ambient air (heat exchangers)
  - Liquid cooling loops
- **Heat Recovery**: Cabin heating, anti-ice, water heating

### 2.6 Mechanical Energy

**Definition**: Energy associated with motion or position.

**Key Terms**:
- **Kinetic Energy**: E_k = ½ m v², energy of motion
- **Potential Energy**: E_p = m g h, energy of position
- **Torque (τ)**: Rotational force, measured in N·m
- **Rotational Speed (ω)**: RPM or rad/s
- **Mechanical Power**: P_mech = τ × ω

**Application to AMPEL360**:
- **Propulsion**: Electric motors converting electrical to mechanical
- **Motor Power**: 1.5-2.8 MW per motor
- **Propeller/Fan Speed**: Variable, controlled by motor drives
- **Efficiency**: Electrical to mechanical ~95%

---

## 3. Energy Flow Directions

### 3.1 Generation
- Energy conversion from source (H₂) to usable form (electrical)
- Primary: Fuel cells
- Secondary: APU, battery discharge, regenerative braking

### 3.2 Distribution
- Transfer of energy from generation to consumption points
- Electrical: Buses, contactors, cables
- Hydraulic: Lines, valves, manifolds
- Pneumatic: Ducts, valves, regulators

### 3.3 Consumption
- Conversion of energy into useful work or output
- Propulsion, actuation, heating, cooling, computing, lighting

### 3.4 Storage
- Temporary holding of energy for later use
- Batteries (electrical), accumulators (hydraulic), pressure vessels (pneumatic)

### 3.5 Dissipation/Loss
- Unwanted energy conversion, typically to heat
- Resistive losses, friction, inefficiencies

### 3.6 Recovery
- Capture and reuse of energy that would otherwise be lost
- Regenerative braking, waste heat utilization

---

## 4. Energy Quality Metrics

### 4.1 Efficiency (η)
- **Definition**: Ratio of useful output energy to total input energy
- **Formula**: η = E_out / E_in × 100%
- **Units**: Percentage (%)
- **Typical Values**:
  - Fuel cell: 55-60%
  - Electric motor: 94-96%
  - DC/DC converter: 96-98%
  - Hydraulic pump: 85-92%

### 4.2 Power Quality

**For Electrical Systems**:
- **Voltage Regulation**: Deviation from nominal voltage (typically ±5%)
- **Frequency Stability**: For AC systems (typically ±0.5 Hz)
- **Total Harmonic Distortion (THD)**: Measure of waveform purity (<5% target)
- **Power Factor (PF)**: Ratio of real to apparent power (>0.95 target)

**For Hydraulic Systems**:
- **Pressure Ripple**: Variation in pressure (typically <5%)
- **Contamination**: Fluid cleanliness level (ISO 4406)

**For Pneumatic Systems**:
- **Pressure Stability**: Variation in delivered pressure
- **Moisture Content**: Dew point specification

### 4.3 Reliability

- **Mean Time Between Failures (MTBF)**: Hours
- **Availability**: Percentage of time system is operational
- **Redundancy Level**: N, N+1, N+2, etc.

---

## 5. Energy Conversion Processes

### 5.1 Electrochemical (Fuel Cells)
- **Process**: H₂ + O₂ → H₂O + electricity + heat
- **Input**: Hydrogen and oxygen (from air)
- **Output**: DC electrical power, water, waste heat
- **Efficiency**: 55-60% (electrical), 85-90% (total with heat recovery)

### 5.2 Electromechanical (Motors/Generators)
- **Process**: Interaction of magnetic fields and currents
- **Motor Mode**: Electrical → Mechanical
- **Generator Mode**: Mechanical → Electrical (regenerative braking)
- **Efficiency**: 94-96% bidirectional

### 5.3 Electrohydraulic (Pumps)
- **Process**: Electric motor drives hydraulic pump
- **Input**: Electrical power
- **Output**: Pressurized fluid flow
- **Efficiency**: 85-92% overall

### 5.4 Electropneumatic (Compressors)
- **Process**: Electric motor drives air compressor
- **Input**: Electrical power
- **Output**: Compressed air
- **Efficiency**: 70-85% depending on compression ratio

### 5.5 Power Electronic Conversion
- **DC/DC Conversion**: Voltage level change
  - Buck converter: Step-down
  - Boost converter: Step-up
  - Efficiency: 96-98%
- **DC/AC Inversion**: DC to AC power
  - Efficiency: 95-97%
- **AC/DC Rectification**: AC to DC power
  - Efficiency: 95-97%

---

## 6. Energy State Definitions

### 6.1 Available Energy
- Energy ready for immediate use
- Includes: Fuel in tanks, battery charge, accumulator pressure

### 6.2 Reserved Energy
- Energy allocated for specific purposes (e.g., emergency reserves)
- Not available for normal operations

### 6.3 Stored Energy
- Energy held in storage systems
- Batteries, accumulators, compressed gas

### 6.4 In-Transit Energy
- Energy currently flowing through distribution systems
- Transient, momentary state

### 6.5 Consumed Energy
- Energy that has been converted into useful work or heat

### 6.6 Lost Energy
- Energy dissipated without useful output
- Losses, inefficiencies, waste

---

## 7. Energy Management Terms

### 7.1 Load Prioritization
- **Critical Loads**: Essential for flight safety (flight controls, avionics)
- **Essential Loads**: Required for safe operations (communications, navigation)
- **Non-Essential Loads**: Comfort and convenience (IFE, galleys)
- **Shedding**: Controlled disconnection of lower-priority loads

### 7.2 Power Management Modes

**Normal Mode**:
- All systems operational
- Full power available from fuel cells

**Degraded Mode**:
- Partial system failure
- Reduced power availability
- Automatic load shedding

**Emergency Mode**:
- Critical systems only
- Battery backup power
- Minimum safe flight duration (30 minutes target)

### 7.3 Energy Optimization

**Peak Shaving**:
- Using storage (batteries) to reduce peak demand on fuel cells

**Demand Response**:
- Adjusting non-critical loads based on available supply

**Efficiency Optimization**:
- Operating systems at maximum efficiency points

**Predictive Management**:
- Using mission profiles to optimize energy use

---

## 8. Measurement and Units

### 8.1 SI Units (Primary)

| Quantity | Unit | Symbol |
|----------|------|--------|
| Energy | Joule | J |
| Power | Watt | W |
| Voltage | Volt | V |
| Current | Ampere | A |
| Resistance | Ohm | Ω |
| Frequency | Hertz | Hz |
| Temperature | Kelvin | K |
| Pressure | Pascal | Pa |
| Mass Flow | kg/second | kg/s |

### 8.2 Common Aviation Units

| Quantity | Unit | Symbol | Conversion |
|----------|------|--------|------------|
| Energy | Watt-hour | Wh | 1 Wh = 3600 J |
| Power | Kilowatt | kW | 1 kW = 1000 W |
| Temperature | Celsius | °C | °C = K - 273.15 |
| Pressure | psi | psi | 1 psi = 6894.76 Pa |
| Pressure | bar | bar | 1 bar = 100,000 Pa |
| Flow | Liters/min | L/min | Various |
| Flow | Gallons/min | GPM | 1 GPM = 3.785 L/min |

---

## 9. Abbreviations and Acronyms

| Abbreviation | Full Term |
|--------------|-----------|
| AC | Alternating Current |
| APU | Auxiliary Power Unit |
| DC | Direct Current |
| ECS | Environmental Control System |
| EMS | Energy Management System |
| FADEC | Full Authority Digital Engine Control |
| GPM | Gallons Per Minute |
| HHV | Higher Heating Value |
| IFE | In-Flight Entertainment |
| LH₂ | Liquid Hydrogen |
| LHV | Lower Heating Value |
| PEM | Proton Exchange Membrane (fuel cell) |
| PF | Power Factor |
| SoC | State of Charge |
| SSPC | Solid-State Power Controller |
| THD | Total Harmonic Distortion |
| VDC | Volts Direct Current |
| VAC | Volts Alternating Current |

---

## 10. Related Documents

| Document | Description |
|----------|-------------|
| [95-80-00-001](../95-80-00-001_Energy_Overview.md) | Energy module overview |
| [95-80-00-002](../95-80-00-002_Energy_System_Boundaries_and_Scope.md) | System boundaries |
| [95-80-00-006](95-80-00-006_Energy_Balances_and_KPI_Definitions.md) | KPI definitions |

---

## 11. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Energy WG | Initial version |

---

**Document Control**
- **Standard**: OPT-IN Framework v1.5
- **Owner**: AMPEL360 Documentation WG
- **Classification**: Technical Reference
