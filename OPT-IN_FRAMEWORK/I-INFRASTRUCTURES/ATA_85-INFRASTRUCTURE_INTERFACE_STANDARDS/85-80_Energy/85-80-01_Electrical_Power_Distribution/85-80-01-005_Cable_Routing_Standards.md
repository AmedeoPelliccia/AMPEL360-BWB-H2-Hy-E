# 85-80-01-005 Cable Routing Standards

## Document Information

- **Document ID**: 85-80-01-005
- **Title**: Cable Routing and Installation Standards
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

Defines standards for routing, installation, and protection of power cables in airport infrastructure supporting AMPEL360 aircraft operations.

## Scope

- Cable installation methods (buried, ducted, trays, ladders)
- Route planning and segregation
- Mechanical and environmental protection
- Identification and documentation
- Testing and commissioning

## Cable Installation Methods

### Direct Buried Cables

#### Installation Standards

- **Minimum Depth**: 
  - HV (11kV-33kV): 1.2m
  - LV (400V): 0.8m
  - Under roads/vehicular areas: Add 0.3m
- **Bedding**: 100mm sand layer below and above cable
- **Marker Tape**: Warning tape 300mm above cable
- **Backfill**: Screened soil, compacted in layers
- **Standards**: [IEC 60364-5-52](https://www.iec.ch/)

#### Route Marking

- **Surface Markers**: At changes of direction, joints, terminations
- **Marker Posts**: At 50m intervals on long runs
- **Drawings**: Accurate as-built with GPS coordinates

#### Protection

- **Mechanical Protection**: Cable tiles or covers in high-risk areas
- **Rodent Protection**: Stainless steel tape armor or PVC sheathing
- **Thermal**: Derating based on soil thermal resistivity

### Duct Banks

#### Duct Configuration

- **Material**: HDPE or PVC ducts
- **Sizing**: Cable OD + 50% clearance minimum
- **Arrangement**: Triangular or rectangular formation
- **Spare Ducts**: 30% spare capacity for future expansion

#### Installation

- **Concrete Encasement**: Minimum 100mm all sides
- **Depth**: As per direct burial above
- **Draw Pits**: Maximum 50m spacing, at direction changes >30°
- **Duct Entry**: Sealed with fire-rated compound

### Cable Trays and Ladders

#### System Design

- **Material**: Galvanized steel, stainless steel (corrosive environments), or aluminum
- **Loading**: Maximum 50% fill for power cables (heat dissipation)
- **Width**: 150mm, 225mm, 300mm, 450mm, 600mm, 900mm standard
- **Standards**: [IEC 61537](https://www.iec.ch/)

#### Support and Fixing

- **Support Spacing**:
  - Steel trays: 1.5m for <300mm, 2.0m for 300-600mm, 2.5m for >600mm
  - Aluminum trays: Reduce by 30%
- **Fixing**: To structural steel or concrete using brackets/hangers
- **Expansion Joints**: Every 30m or at building expansion joints

#### Cable Arrangement

- **Multicore Cables**: Single layer, touching arrangement
- **Single-Core Cables**: Trefoil or flat formation, secured with cleats
- **Segregation**: HV, LV, and control cables in separate trays or 300mm minimum spacing

### Conduits

#### Application

- **Use**: Mechanical protection, concealed routes, exposed areas
- **Material**: 
  - Steel (galvanized or PVC-coated) for mechanical protection
  - PVC for general use, non-flammable areas
  - Flexible metallic for equipment connections

#### Sizing

- **Fill Factor**: Maximum 40% for multi-cable installation
- **Minimum Size**: 20mm for general circuits, 25mm for submains
- **Bends**: Maximum two 90° bends between draw points
- **Pull Boxes**: At 30m maximum spacing, at bends

## Route Planning

### Segregation Requirements

| Cable Type      | Minimum Separation (Open Air) | Comments                      |
|-----------------|-------------------------------|-------------------------------|
| HV Power / LV Power | 300mm                       | Separate trays/ducts          |
| Power / Control | 300mm                       | EMI considerations            |
| Power / Data    | 500mm                       | High EMI sensitivity          |
| Fire Alarm      | Dedicated route              | Fire safety requirement       |

### Crossing and Proximity

- **HV/LV Crossings**: 90° where possible, minimum 300mm vertical separation
- **Parallel Runs**: Limit to 10m maximum for HV/LV in same trench
- **Other Services**: 500mm from gas, 300mm from water/telecom

### Route Coordination

- **Avoid**: High-temperature areas (boiler rooms, hot pipes >60°C)
- **Access**: Maintain accessibility for inspection and maintenance
- **Future Expansion**: Reserve 30% spare capacity in routes
- **3D Coordination**: BIM coordination for complex areas

## Mechanical Protection

### Protection Methods

- **Underground**: Concrete slabs, marker tiles, or warning tape
- **Surface**: Cable covers, yellow jackets in pedestrian/vehicle areas
- **Wall-Mounted**: Trunking, channeling, or conduit
- **Floor Crossings**: Heavy-duty cable covers or recessed trays

### Special Areas

#### Vehicle Crossings

- **Protection**: Steel pipes or reinforced concrete troughs
- **Depth**: Minimum 1.0m or 0.6m with concrete protection
- **Signage**: Surface marking where concealed covers present trip hazard

#### Hazardous Areas (H2 Facilities)

- **Equipment**: ATEX/IECEx certified cable glands and fittings
- **Cable Type**: LSZH sheath, mineral-insulated where specified
- **Bonding**: Enhanced bonding to prevent static accumulation
- **Sealing**: Gas-tight seals at zone boundaries

## Cable Joints and Terminations

### Joints

- **Location**: In accessible draw pits, junction boxes, or substations
- **Type**: Heat-shrink or cold-shrink for polymeric cables
- **HV Joints**: Factory-prepared kits per manufacturer specifications
- **Testing**: Partial discharge test for HV joints >11kV

### Terminations

- **Indoor Terminations**: Heat-shrink or cold-shrink stress control
- **Outdoor Terminations**: Weatherproof, UV-resistant
- **HV Terminations**: Cable sealing ends (CSE) with stress cones
- **Earthing**: Cable screens earthed at both ends (HV), single-point earthing for control cables

## Cable Identification

### Labeling

- **Frequency**: At terminations, joints, every 10m on trays, entry/exit of ducts
- **Content**: Cable designation per cable schedule, circuit number, voltage rating
- **Material**: UV-resistant, durable plastic tags or heat-shrink sleeves
- **Color Coding**: Per voltage level (e.g., red for HV, orange for LV)

### Cable Markers

- **Underground**: Marker posts at accessible points
- **Trays**: Route identification labels at 10m intervals
- **Drawings**: As-built drawings with cable routes and IDs

## Fire Protection

### Fire Barriers

- **Penetrations**: All floor/wall penetrations fire-stopped with certified materials
- **Rating**: Match building fire rating (typically 2 hours)
- **Materials**: Intumescent seals, fire-rated boards, or mortar
- **Standards**: Local fire codes, [IEC 60331](https://www.iec.ch/)

### Fire-Resistant Cables

- **Application**: Escape routes, fire alarm, emergency lighting
- **Standard**: [IEC 60331](https://www.iec.ch/) (circuit integrity), [IEC 60332](https://www.iec.ch/) (flame propagation)
- **LSZH Cables**: Low smoke zero halogen in enclosed public areas

### Cable Tray Fire Barriers

- **Vertical Trays**: Fire barriers at each floor level
- **Horizontal Trays**: At fire compartment boundaries
- **Materials**: Intumescent wraps or boards

## Testing and Commissioning

### Pre-Installation Tests

- **Drum Tests**: Insulation resistance, conductor continuity (before laying)

### Post-Installation Tests

#### Low Voltage Cables

1. **Continuity**: All conductors and earth
2. **Insulation Resistance**: Minimum 1 MΩ (new), 0.5 MΩ (existing)
3. **Earth Fault Loop Impedance**: To verify disconnection times
4. **Polarity**: Correct phase sequence

#### High Voltage Cables

1. **Insulation Resistance**: Minimum 100 MΩ for new cables
2. **Voltage Withstand Test**: AC test at 2.5-3.0 x rated voltage
3. **Partial Discharge Test**: For cables >11kV, <10 pC required
4. **Cable Sheath Integrity**: Sheath voltage test
5. **Tan Delta**: Dissipation factor measurement (diagnostic)

### Documentation

- Test certificates with date, tester, equipment, results
- As-built cable schedules and route drawings
- Commissioning reports

## Maintenance

### Periodic Inspections

- **Visual Inspection**: Annual for exposed cables, biennial for concealed
- **Thermographic Survey**: Annual for HV cables and critical LV feeders
- **Partial Discharge Monitoring**: Continuous or periodic for critical HV cables

### Condition Assessment

- **Insulation Resistance**: Every 3-5 years
- **Tan Delta Testing**: For HV cables showing degradation
- **Cable Fault Location**: TDR or other methods when faults suspected

## Environmental Considerations

### Temperature

- **Ambient Derating**: Apply factors per [IEC 60364-5-52](https://www.iec.ch/) for >30°C
- **Soil Temperature**: Consider for buried cables (assume 20°C or local data)
- **Grouping**: Derating for multiple cables in proximity

### Corrosion Protection

- **Metallic Armor**: Galvanized, PVC-covered, or suitable for environment
- **Cable Trays**: Hot-dip galvanized, stainless steel (coastal), or powder-coated
- **Earthing Conductors**: Copper or stainless steel in aggressive soils

## Standards and Compliance

### Primary Standards

- [IEC 60364-5-52](https://www.iec.ch/) - Selection and erection of electrical equipment - Wiring systems
- [IEC 61537](https://www.iec.ch/) - Cable management - Cable tray systems and cable ladder systems
- [IEC 60502](https://www.iec.ch/) - Power cables with extruded insulation
- [IEC 60331](https://www.iec.ch/) - Tests for electric cables under fire conditions - Circuit integrity
- [IEC 60332](https://www.iec.ch/) - Tests on electric cables under fire conditions - Test for vertical flame propagation

### Regional Standards

- Europe: EN standards aligned with IEC, plus national variations
- North America: [NEC (NFPA 70)](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=70), IEEE standards
- Local: Airport authority cable installation standards

## Cross-References

- **85-80-01-001** - Primary Distribution 33kV (HV cable specifications)
- **85-80-01-002** - Secondary Distribution 11kV (MV cable specifications)
- **85-80-01-003** - Low Voltage Distribution 400V (LV cable specifications)
- **85-80-01-004** - Substation Design (cable entry and termination)
- **85-80-01-A-004** - Cable Sizing Calculations (detailed methodology)

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
