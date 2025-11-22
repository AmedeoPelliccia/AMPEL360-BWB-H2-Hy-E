# 85-80-01-003 Low Voltage Distribution 400V

## Document Information

- **Document ID**: 85-80-01-003
- **Title**: Low Voltage Distribution 400V System Standards
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

Defines standards for 400V/230V low-voltage electrical distribution systems serving end-user equipment and loads in airport facilities supporting AMPEL360 aircraft operations.

## Scope

- 400V three-phase and 230V single-phase distribution
- Main and sub-distribution boards
- Final circuits and protection
- Cabling and wiring standards
- Earthing and bonding
- Special applications (aircraft ground power, H2 equipment)

## System Standards

### Voltage Characteristics

- **Nominal Voltage**: 400/230V (three-phase/single-phase), 50/60 Hz
- **Tolerance**: ±10% (360-440V line-to-line, 207-253V line-to-neutral)
- **Operating Range**: Preferably ±5% for sensitive equipment
- **System Type**: TN-S (separate protective earth and neutral)

### Frequency

- **Nominal**: 50 Hz (Europe, most regions) or 60 Hz (North America)
- **Tolerance**: ±1% (49.5-50.5 Hz or 59.4-60.6 Hz)

## Distribution System Design

### Main Distribution Boards (MDB)

- **Location**: Central electrical room per building/area
- **Incoming Supply**: From 11kV/400V transformer
- **Busbar Rating**: 1600A to 4000A
- **Form of Separation**: Form 3b or Form 4 per [IEC 61439](https://www.iec.ch/)
- **Metering**: Main energy meter with CT/VT measurement
- **Protection**: MCCB or ACB with electronic trip units

### Sub-Distribution Boards (SDB)

- **Location**: Floor/zone distribution within buildings
- **Supply**: From MDB via sub-main cables
- **Busbar Rating**: 400A to 1600A typical
- **Outgoing Circuits**: MCCBs and MCBs for final circuits
- **Form**: Form 2b minimum per [IEC 61439](https://www.iec.ch/)

### Final Distribution Boards (FDB)

- **Application**: Local distribution for specific areas or equipment groups
- **Supply**: From SDB
- **Protection**: MCBs or RCBOs
- **Rating**: Up to 400A

## Protection Devices

### Circuit Breakers

#### Molded Case Circuit Breakers (MCCB)

- **Application**: Main feeders, sub-mains (100A-1600A)
- **Type**: Thermal-magnetic or electronic trip
- **Breaking Capacity**: Minimum 35 kA at 400V
- **Standards**: [IEC 60947-2](https://www.iec.ch/)

#### Miniature Circuit Breakers (MCB)

- **Application**: Final circuits (6A-125A)
- **Curve Type**: 
  - Type B (3-5 In): Lighting, general loads
  - Type C (5-10 In): Motors, transformers (inductive loads)
  - Type D (10-20 In): High inrush (large motors, welding equipment)
- **Breaking Capacity**: Minimum 10 kA at 400V
- **Standards**: [IEC 60898](https://www.iec.ch/)

### Residual Current Devices (RCD)

- **Type AC**: General use (sinusoidal AC currents)
- **Type A**: DC-sensitive (variable speed drives, electronic equipment)
- **Type B**: High-frequency sensitive (EV chargers, H2 electrolyzers)
- **Ratings**: 30mA (personal protection), 100-300mA (fire protection)
- **Standards**: [IEC 61008](https://www.iec.ch/), [IEC 61009](https://www.iec.ch/)

### Surge Protection Devices (SPD)

- **Type 1**: At main distribution board (lightning protection)
- **Type 2**: At sub-distribution boards (switching overvoltages)
- **Type 3**: At sensitive equipment (local protection)
- **Coordination**: T1+T2+T3 cascaded protection
- **Standards**: [IEC 61643-11](https://www.iec.ch/)

## Cable Systems

### Power Cables

#### Multi-Core Cables (Fixed Installation)

- **Type**: XLPE or PVC insulated, PVC or LSZH sheathed
- **Conductor**: Stranded copper
- **Standards**: [IEC 60502](https://www.iec.ch/)

#### Single-Core Cables

- **Application**: High-current feeders (>200A)
- **Installation**: Grouped in trefoil or flat formation
- **Standards**: [IEC 60502](https://www.iec.ch/)

### Cable Sizing

Based on:
1. **Current-Carrying Capacity**: Per IEC 60364-5-52, considering:
   - Ambient temperature
   - Installation method
   - Grouping factor
   - Thermal insulation
2. **Voltage Drop**: Maximum 4% for lighting, 5% for power
3. **Short-Circuit Withstand**: Per [IEC 60364-4-43](https://www.iec.ch/)
4. **Earth Fault Loop Impedance**: To ensure disconnection times per [IEC 60364-4-41](https://www.iec.ch/)

See [85-80-01-A-004_Cable_Sizing_Calculations.md](./ASSETS/85-80-01-A-004_Cable_Sizing_Calculations.md) for detailed methodology.

## Earthing and Bonding

### Earthing System (TN-S)

- **Protective Earth (PE)**: Separate conductor throughout
- **Neutral (N)**: Connected to earth at supply transformer only
- **Main Earthing Terminal (MET)**: At main distribution board
- **Earth Conductor**: Copper, sized per [IEC 60364-5-54](https://www.iec.ch/)

### Equipotential Bonding

#### Main Bonding

Connect to MET:
- Incoming metallic services (water, gas)
- Structural steel
- Cable trays and conduits
- Lightning protection system

#### Supplementary Bonding

In special locations (wet areas, outdoor, conductive environments):
- Between exposed conductive parts
- Between exposed and extraneous conductive parts
- Additional earth connections

### Earth Resistance

- **Main Earth Electrode**: Maximum 1 ohm
- **Supplementary Electrodes**: As required to achieve target resistance
- **Testing**: Annual verification, record results

## Special Applications

### Aircraft Ground Power (400Hz GPU)

- **Dedicated Feeders**: From MDB to GPU units
- **Protection**: Coordinated with 85-80-05 standards
- **Cable Sizing**: Based on high-frequency considerations
- **See**: [85-80-05-001_400Hz_GPU_Systems.md](../85-80-05_Aircraft_Ground_Power/85-80-05-001_400Hz_GPU_Systems.md)

### H2 Production Equipment

- **Hazardous Area Classification**: ATEX/IECEx Zone 2 or Division 2
- **Equipment**: Certified for use in classified areas
- **Bonding**: Enhanced bonding to prevent static discharge
- **Protection**: Type B RCD mandatory
- **Cable Glands**: Explosion-proof where required
- **See**: [85-80-02-003_Green_H2_Production.md](../85-80-02_Renewable_Energy_Generation/85-80-02-003_Green_H2_Production.md)

### Electric Vehicle Charging Stations

- **Dedicated Circuits**: From SDB
- **Protection**: Type B RCD, overcurrent protection
- **Cable**: Sized for continuous duty (125% of rated current)
- **Communication**: Integration with energy management system
- **Standards**: [IEC 61851](https://www.iec.ch/)

## Power Quality

### Harmonic Mitigation

- **Assessment**: Harmonic analysis for non-linear loads (VFDs, LED lighting, EV chargers)
- **Limits**: Per [IEEE 519](https://standards.ieee.org/)
- **Mitigation**: Passive or active filters where THD >5%

### Voltage Unbalance

- **Target**: <2% voltage unbalance
- **Cause**: Unbalanced single-phase loads
- **Solution**: Redistribute loads across phases

### Transient Protection

- **SPDs**: As specified above
- **Filters**: For sensitive equipment
- **Isolation Transformers**: Where galvanic isolation required

## Installation Standards

### Wiring Methods

- **Cable Trays**: For multi-cable runs in accessible areas
- **Conduits**: For mechanical protection (steel or PVC)
- **Cable Ducts**: Underfloor or concealed routing
- **Cleats and Clips**: For direct fixing to structures
- **Standards**: [IEC 60364-5-52](https://www.iec.ch/)

### Segregation

- **Power and Control**: Separate trays/conduits or minimum 300mm spacing
- **Fire Barriers**: At floor/wall penetrations
- **Magnetic Separation**: Single-core cables in steel conduit to be avoided

### Identification

- **Cable Labels**: At terminations and regular intervals
- **Color Coding**: 
  - Phase: Brown (L1), Black (L2), Grey (L3)
  - Neutral: Blue
  - Earth: Green/Yellow
- **Circuit Identification**: At distribution boards

## Safety and Compliance

### Electrical Safety

- **Access**: Distribution boards in locked electrical rooms or secured enclosures
- **Warning Signs**: At all electrical equipment
- **Isolation**: Lockable isolators for maintenance
- **Testing**: Periodic inspection and testing per [IEC 60364-6](https://www.iec.ch/)

### Arc Flash

- **Hazard Assessment**: Required for all distribution boards >400A
- **PPE**: Based on incident energy calculation
- **Labels**: Arc flash warning labels at equipment
- **Standards**: [IEEE 1584](https://standards.ieee.org/)

### Fire Safety

- **Fire-Rated Cables**: In escape routes and high-risk areas
- **Fire Barriers**: Properly sealed cable penetrations
- **Fire Stopping**: Per building fire safety code

## Monitoring and Metering

### Energy Metering

- **Main Meters**: At MDB (billing-grade accuracy)
- **Sub-Meters**: At SDB for departmental/area monitoring
- **Metering Points**: Critical loads, renewable generation, storage systems
- **Communication**: Modbus, M-Bus, or IEC 61850 to energy management system

### Power Monitoring

- **Parameters**: Voltage, current, power factor, harmonics
- **Frequency**: Real-time or 15-minute intervals
- **Integration**: See [85-80-06 Energy Management Systems](../85-80-06_Energy_Management_Systems/README.md)

## Testing and Commissioning

### Pre-Commissioning Tests

1. **Insulation Resistance**: Minimum 1 MΩ at 500V DC (new installations)
2. **Continuity**: Earth and bonding conductors
3. **Polarity**: Correct phase, neutral, and earth connections
4. **Earth Fault Loop Impedance**: To verify disconnection times
5. **RCD Trip Times**: At rated residual current

### Commissioning Tests

1. **Load Testing**: Verify ratings and operation under load
2. **Protection Coordination**: Trip testing of circuit breakers
3. **Voltage Drop**: Measure at full load
4. **Thermographic Survey**: Identify hot spots at connections

### Documentation

- Test certificates per [IEC 60364-6](https://www.iec.ch/)
- As-built drawings (single-line, layout, cable schedules)
- Equipment data sheets and certificates

## Maintenance

### Periodic Inspection and Testing

- **Initial**: At commissioning
- **Routine**: Every 3-5 years for commercial installations, annually for industrial
- **After Fault**: Following any electrical fault or incident

### Visual Inspections

- **Frequency**: Annual
- **Checks**: Damage, overheating, loose connections, corrosion
- **Thermography**: Annual for critical distribution boards

## Standards and References

### Primary Standards

- [IEC 60364](https://www.iec.ch/) - Low-voltage electrical installations
- [IEC 61439](https://www.iec.ch/) - Low-voltage switchgear and controlgear assemblies
- [IEC 60947](https://www.iec.ch/) - Low-voltage switchgear and controlgear
- [IEC 60898](https://www.iec.ch/) - Circuit-breakers for overcurrent protection for household and similar installations
- [IEEE 519](https://standards.ieee.org/) - Harmonic Control in Electrical Power Systems

### Regional Standards

- Europe: [BS 7671](https://electrical.theiet.org/) (UK), HD 60364 (EU harmonization)
- North America: [NFPA 70 (NEC)](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=70)
- Local: Airport and municipal electrical codes

## Cross-References

- **85-80-01-002** - Secondary Distribution 11kV (upstream supply)
- **85-80-01-004** - Substation Design (transformer and distribution rooms)
- **85-80-01-005** - Cable Routing Standards (installation details)
- **85-80-05** - Aircraft Ground Power (400Hz GPU interface)
- **85-80-06** - Energy Management Systems (metering and monitoring)

## Revision History

| Version | Date       | Author               | Changes                  |
|---------|------------|----------------------|--------------------------|
| 1.0     | 2025-11-22 | AMPEL360 Doc Team    | Initial release          |

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---
