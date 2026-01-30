# 03-90-02-03A - Cryogenic Flow Diagrams

## 1. Purpose

This document defines standards for cryogenic flow diagrams specific to Liquid Hydrogen (LH2) Ground Support Equipment operating at -253°C, including thermodynamic considerations, phase change management, and boil-off handling.

## 2. Scope

This specification covers cryogenic flow diagrams for:
- LH2 storage and conditioning systems
- Cryogenic transfer and distribution
- Cooldown and warmup procedures
- Boil-off gas (BOG) management
- Cryogenic liquid level control
- Heat leak analysis and mitigation

## 3. Applicable Documents

- [ISO 21013](https://www.iso.org/standard/71940.html) - Cryogenic Vessels - Pressure Relief Accessories
- [ISO 21029](https://www.iso.org/standard/54704.html) - Cryogenic Vessels - Cleanliness for Cryogenic Service
- [ASME B31.3](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping) - Process Piping (Chapter IX - High Pressure)
- [CGA P-12](https://www.cganet.com/) - Safe Handling of Cryogenic Liquids
- [NIST Technical Note 1343](https://www.nist.gov/) - Thermophysical Properties of Hydrogen
- [EN 13458](https://www.en-standard.eu/) - Cryogenic Vessels - Static Vacuum Insulated Vessels

## 4. Documentation Description

### 4.1 Overview

Cryogenic flow diagrams are specialized process flow diagrams that emphasize:
- Thermodynamic state changes (liquid to gas phase transitions)
- Heat transfer and thermal management
- Pressure and temperature relationships
- Cooldown/warmup transients
- Safety systems for cryogenic operations

These diagrams are essential for safe and efficient cryogenic LH2 handling.

### 4.2 Format and Structure

| Element | Format | Standard |
|---------|--------|----------|
| Process Blocks | Rectangular with rounded corners | ISO 5807 |
| Flow Direction | Bold arrows | ISO 5807 |
| State Indicators | P, T, ṁ, h annotations | Engineering notation |
| Phase Indication | Color or pattern fill | Liquid=blue, gas=light blue, two-phase=hatched |
| Energy Flows | Dashed arrows | Heat in (red), heat out (blue) |

### 4.3 Content Requirements

#### 4.3.1 Thermodynamic State Points

Each major state point in the flow diagram must indicate:

| Parameter | Symbol | Units | Notes |
|-----------|--------|-------|-------|
| Pressure | P | bar (psia) | Absolute pressure |
| Temperature | T | K (°C) | Actual temperature |
| Mass Flow | ṁ | kg/s (lb/hr) | Flow rate |
| Enthalpy | h | kJ/kg (Btu/lb) | Specific enthalpy |
| Quality | x | - | For two-phase (0=liquid, 1=gas) |
| Density | ρ | kg/m³ (lb/ft³) | Fluid density |

**Example State Point Annotation:**
```
SP-1: LH2 Storage Outlet
P = 4.5 bar
T = 21.2 K (-252°C)
ṁ = 1.5 kg/s
h = -240 kJ/kg
State: Saturated liquid
```

#### 4.3.2 LH2 Storage System Flow Diagram

**Key Components:**

1. **Inner Vessel (LH2 Storage)**
   - Liquid volume and ullage space
   - Saturation conditions
   - Liquid withdrawal location (bottom)
   - Vapor space connection (top)

2. **Outer Jacket (Vacuum Space)**
   - Vacuum level (< 10⁻³ mbar)
   - Multi-layer insulation (MLI)
   - Vacuum maintenance system
   - Leak rate monitoring

3. **Pressure Build System**
   - LH2 extraction from bottom
   - Ambient vaporizer or electric heater
   - GH2 return to tank vapor space
   - Pressure control valve
   - Target pressure setpoint

4. **Boil-Off Gas (BOG) Management**
   - Natural boil-off rate (% per day)
   - BOG collection header
   - BOG compressor (if used)
   - BOG vent or flare
   - BOG reliquefaction (if applicable)

**Heat Leak Sources:**
- Piping penetrations
- Support structures
- Instrumentation
- Radiation (warm surfaces)
- Total heat leak (W)

**Diagram Requirements:**
- Show all heat inputs (ambient, solar, conduction)
- Indicate boil-off generation rate
- Show pressure control strategy
- Include safety relief paths

#### 4.3.3 Cryogenic Transfer Flow Diagram

**Transfer Modes:**

**Mode 1: Pressure Differential Transfer**
- Source tank pressurized (pressure build)
- Receiver tank at lower pressure
- Flow driven by ΔP
- Flow rate dependent on pressure difference
- Suitable for short transfers

**Mode 2: Pump Transfer**
- Cryogenic pump in circuit
- Controlled flow rate
- Higher transfer rates
- Pump NPSH considerations
- Pump cooldown requirements

**Transfer Sequence:**

1. **Pre-Cool Phase:**
   - Initial pipe temperature (ambient)
   - Cooldown flow rate (reduced)
   - Vapor generation and venting
   - Time to reach steady state
   - Thermal stress management

2. **Steady Transfer Phase:**
   - Full flow rate
   - Minimal vapor generation
   - Pressure stabilization
   - Flow metering
   - Level monitoring (source and receiver)

3. **Post-Transfer Phase:**
   - Line drainage or blow-down
   - Warmup (if required)
   - Line purge (N2 or GH2)
   - Isolation

**Energy Balance:**
- Cooling energy required for pipe cooldown
- Latent heat of vaporization
- Sensible heat gain during transfer
- Transfer efficiency calculation

#### 4.3.4 Cooldown Procedure Flow Diagram

**Controlled Cooldown Steps:**

| Step | Target T (K) | Time (min) | Flow Rate | Notes |
|------|--------------|------------|-----------|-------|
| 1 | 300 → 250 | 5-10 | Low | Slow initial cool |
| 2 | 250 → 150 | 10-15 | Low | Monitor thermal stress |
| 3 | 150 → 77 | 15-20 | Medium | LN2 temp region |
| 4 | 77 → 21 | 20-30 | Medium | LH2 temp region |
| 5 | 21 (steady) | 10 | Full | Stabilization |

**Thermal Contraction:**
- Total contraction: ~0.3% (300K to 20K)
- Support system accommodation
- Expansion joint movement
- Flange alignment maintenance

**Vent Gas Handling:**
- Vent capacity required (scfm)
- Vent line sizing
- Vent stack height and dispersion
- Ignition source control near vent

#### 4.3.5 Phase Change Management

**Liquid-to-Gas Vaporization:**

| Parameter | Liquid (20K) | Gas (300K) | Ratio |
|-----------|--------------|------------|-------|
| Density (kg/m³) | 70.8 | 0.082 | 863:1 |
| Volume for 1 kg | 0.0141 m³ | 12.2 m³ | 863:1 |
| Enthalpy (kJ/kg) | -240 | 3950 | Δh=4190 |

**Implications:**
- 1 liter of LH2 → 863 liters of GH2 (at STP)
- Rapid vaporization can cause pressure surges
- Adequate vent capacity essential
- Two-phase flow complications

**Two-Phase Flow Regions:**
- Identify where two-phase flow possible
- Quality (x) range along path
- Pressure drop considerations
- Flow regime (bubbly, slug, annular)
- Instrumentation challenges

#### 4.3.6 Heat Exchanger Flow Diagrams

**Ambient Vaporizers:**

**Air-Heated Vaporizer:**
- LH2 inlet state
- GH2 outlet state
- Air flow (natural or forced)
- Heat transfer area
- Capacity (kg/hr LH2 → Nm³/hr GH2)
- Anti-icing provisions

**Water Bath Vaporizer:**
- LH2 inlet state
- GH2 outlet state
- Water recirculation
- Heater capacity
- Freeze protection
- Capacity (kg/hr LH2 → Nm³/hr GH2)

**Performance Curves:**
- Flow rate vs outlet temperature
- Flow rate vs pressure drop
- Ambient temperature effects

#### 4.3.7 Level Control Systems

**Differential Pressure Level Measurement:**
- ΔP across tank height
- Compensate for fluid density variation
- Accuracy considerations
- Alarm setpoints (high, low, high-high, low-low)

**Capacitance Level Measurement:**
- Dielectric constant difference (liquid vs vapor)
- Continuous measurement
- Less affected by density changes
- Suitable for slosh conditions

**Level Control Strategy:**
- Fill control (prevent overfill)
- Withdrawal control (prevent pump cavitation)
- BOG generation correlation

#### 4.3.8 Boil-Off Gas (BOG) Flow Diagram

**BOG Generation:**
- Heat leak rate → BOG rate
- Tank design: 0.1% - 0.5% per day typical
- Transfer operations: higher BOG rate
- Environmental factors (solar, wind, ambient T)

**BOG Handling Options:**

**Option 1: Vent to Atmosphere**
- Vent stack design (height, diameter)
- Dilution with ambient air
- Dispersion modeling
- No ignition sources in zone

**Option 2: BOG Compression**
- Compressor type (reciprocating, screw)
- Compression ratio
- Discharge pressure
- Cooling requirements
- Storage of GH2

**Option 3: BOG Reliquefaction**
- Refrigeration system
- Energy consumption
- Liquefaction efficiency
- Return to LH2 storage

**BOG Utilization:**
- Fuel for heating/vaporization
- Pressure build makeup gas
- Purge gas source
- Economic considerations

### 4.4 Energy Analysis

**Heat Leak Calculation:**

| Source | Heat Input (W) | % of Total |
|--------|----------------|------------|
| Piping | TBD | TBD |
| Supports | TBD | TBD |
| Instrumentation | TBD | TBD |
| Neck/penetrations | TBD | TBD |
| Radiation | TBD | TBD |
| **Total** | **TBD** | **100%** |

**BOG Generation:**
- Heat leak (W) ÷ Latent heat of H2 (kJ/kg) = BOG rate (kg/s)
- Example: 50 W ÷ 446 kJ/kg ≈ 0.0001 kg/s ≈ 8.6 kg/day

### 4.5 Safety Considerations

**Overpressure Protection:**
- Primary relief valve (PRV) sizing
- Secondary/backup relief
- Set pressures and capacity
- Relief discharge routing

**Vacuum Loss:**
- Detection of vacuum degradation
- Impact on boil-off rate
- Vacuum pump restart
- Potential for rollover or stratification

**Thermal Shock:**
- Rapid cooldown hazards (material embrittlement)
- Rapid warmup hazards (pressure surges)
- Controlled ramp rates

**Personnel Protection:**
- Cryogenic burn hazards
- Asphyxiation in confined spaces
- Vapor cloud formation
- PPE requirements

## 5. Cross-References

- Related ATA Chapters: ATA 12 (Servicing), ATA 28 (Fuel)
- Parent Document: [03-90_Tables_Schemas_Diagrams](../README.md)
- Related Documents:
  - [03-90-02-01A LH2 System Schematics](./03-90-02-01A_LH2_System_Schematics.md)
  - [03-90-02-02A H2 Piping Diagrams](./03-90-02-02A_H2_Piping_Diagrams.md)
  - [03-90-05-01A LH2 Fueling PFD](../03-90-05_Process_Flow_Diagrams/03-90-05-01A_LH2_Fueling_PFD.md)
  - [03-90-06-02A H2 Equipment Specs](../03-90-06_Specification_Tables/03-90-06-02A_H2_Equipment_Specs.md)

## 6. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 H2 Systems Engineering | Initial release |

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-08.

---
