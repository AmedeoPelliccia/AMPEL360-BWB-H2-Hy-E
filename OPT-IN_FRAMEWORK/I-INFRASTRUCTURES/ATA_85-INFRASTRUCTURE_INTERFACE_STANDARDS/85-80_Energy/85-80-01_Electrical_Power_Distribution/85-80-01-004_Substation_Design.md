# 85-80-01-004 Substation Design

## Document Information

- **Document ID**: 85-80-01-004
- **Title**: Electrical Substation Design Standards
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-22

## Purpose

Establishes design standards for electrical substations serving airport infrastructure for AMPEL360 aircraft operations, covering layout, civil works, equipment arrangement, and safety requirements.

## Scope

- 33kV/11kV and 11kV/400V substations
- Indoor and outdoor configurations
- Civil and structural requirements
- HVAC and fire protection
- Access and security
- Safety features and compliance

## Substation Types

### Primary Substations (33/11kV)

- **Capacity**: 5-20 MVA transformers
- **Configuration**: Indoor or outdoor
- **Application**: Main supply points for airport zones

### Distribution Substations (11kV/400V)

- **Capacity**: 500-2500 kVA transformers
- **Configuration**: Primarily indoor (packaged or custom)
- **Application**: Building and area distribution

## Site Selection Criteria

### Location Requirements

- **Accessibility**: Vehicle access for maintenance and equipment replacement
- **Proximity**: Close to load centers to minimize cable runs
- **Clearances**: Adequate space for equipment, maintenance, and future expansion
- **Flood Risk**: Elevated or flood-protected areas
- **Noise**: Isolated from noise-sensitive areas where possible

### Space Requirements

| Substation Type        | Typical Floor Area | Height    | Transformer Access |
|------------------------|--------------------|-----------|--------------------|
| 33/11kV (Indoor)       | 100-200 m²        | 4-5 m     | Overhead crane     |
| 11kV/400V Packaged     | 20-40 m²          | 3 m       | Personnel door     |
| 11kV/400V Custom       | 40-80 m²          | 3-4 m     | Double door        |

## Civil and Structural Design

### Building Structure

- **Materials**: Reinforced concrete or steel frame, brick/block walls
- **Fire Resistance**: Minimum 2-hour fire rating for walls and roof
- **Weatherproofing**: IP54 minimum for outdoor equipment enclosures
- **Foundations**: Designed for transformer weight plus 50% safety margin
- **Standards**: Local building codes, [IEC 61936-1](https://www.iec.ch/)

### Access and Egress

- **Personnel Doors**: Minimum 1.0m wide, opening outward
- **Equipment Access**: Roller shutter or double doors for transformer removal
- **Emergency Exit**: Secondary exit for substations >50 m²
- **Ramps**: Maximum 1:12 gradient for equipment movement

### Ventilation

#### Natural Ventilation (Preferred for Transformers)

- **Inlet Grilles**: Low level, sized for 0.5 m/s air velocity
- **Outlet Grilles**: High level, 1.5x inlet area
- **Louvers**: Weather-resistant, IP44 minimum, with insect screens

#### Forced Ventilation

- **Application**: High-density substations, insufficient natural ventilation
- **Capacity**: Based on transformer losses and 40°C max internal temperature
- **Fans**: Thermostatically controlled, N+1 redundancy
- **Standards**: [IEC 60076-2](https://www.iec.ch/)

## Electrical Equipment Layout

### 33kV Switchgear Arrangement

- **Clearances**: 
  - Front: 1.5m minimum for operation
  - Rear: 0.8m for cabling (if accessible)
  - Top: 0.5m to ceiling
- **Busbar Orientation**: Horizontal busbar preferred
- **Segregation**: Form 3b or Form 4 per [IEC 62271-200](https://www.iec.ch/)

### Transformer Placement

- **Oil-Filled Transformers**:
  - Bund for 110% oil volume
  - Oil catchment pit with gravel/stone chip filter
  - Minimum 1.5m clearance on all sides
  - Fire walls if <10m from buildings

- **Dry-Type Transformers**:
  - Direct floor mounting or low plinths
  - 1.0m clearance for maintenance
  - Vibration isolation if noise-sensitive

### 11kV and LV Switchgear

- **Clearances**: Per manufacturer plus local codes (typically 1.0m front, 0.6m rear)
- **Cable Entry**: From below (underfloor trenches) or above (cable trays)
- **Ventilation**: Adequate space around ventilation openings

## Cable Management

### Cable Trenches

- **Depth**: 600mm minimum below floor level
- **Width**: Based on cable quantity, minimum 300mm
- **Covers**: Removable checker plate, load-rated
- **Drainage**: Sumps at low points, connected to drainage system
- **Fire Barriers**: At substation boundaries

### Cable Entry Points

- **Sealing**: Fire-rated seals for all wall/floor penetrations
- **Support**: Cable trays or racks immediately outside substation
- **Segregation**: HV, LV, control cables in separate routes
- **Labeling**: Cable identification at entry points

## Earthing and Lightning Protection

### Substation Earthing

- **Earth Grid**: Copper strip or rod grid under substation floor
- **Resistance**: <1 ohm for 33kV, <5 ohm for 11kV substations
- **Connections**: All metallic structures bonded to earth grid
- **Testing**: Annual verification with records
- **Standards**: [IEEE 80](https://standards.ieee.org/)

### Lightning Protection

- **Air Termination**: Lightning rods on roof (outdoor substations)
- **Down Conductors**: Minimum two, opposite corners, bonded to earth grid
- **SPD**: Type 1+2 coordinated surge protection devices
- **Standards**: [IEC 62305](https://www.iec.ch/)

## Safety Systems

### Fire Protection

#### Fire Detection

- **Smoke Detectors**: In all substations
- **Heat Detectors**: Above transformers
- **Alarm**: Local and remote to control room
- **Standards**: [NFPA 72](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=72)

#### Fire Suppression

- **Oil-Filled Transformers**: Automatic water spray or foam system
- **Dry-Type Substations**: CO₂ or clean agent (if unmanned)
- **Manual**: Fire extinguishers (CO₂ for electrical fires)
- **Standards**: [NFPA 850](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=850)

### Access Control

- **Doors**: Locked, restricted to authorized personnel only
- **Interlocks**: On HV compartments
- **Signage**: Warning signs for electrical hazards, arc flash labels
- **CCTV**: Surveillance of entries (recommended)

### Lighting and Emergency Lighting

- **Normal Lighting**: 200 lux minimum at floor level
- **Emergency Lighting**: Battery-backed, 50 lux minimum, 3-hour duration
- **Exit Signs**: Illuminated, visible from all locations
- **Control**: Outside main entrance with key switch override

## HVAC and Environmental Control

### Temperature Control

- **Design Temperature**: 40°C maximum for equipment rating
- **Ambient Consideration**: Based on local climate data
- **Heating**: Frost protection in cold climates (minimum 5°C)
- **Dehumidification**: If relative humidity >80% regularly

### Humidity Control

- **Maximum**: 95% relative humidity (non-condensing)
- **Control**: Ventilation, dehumidifiers in coastal or humid climates
- **Corrosion Protection**: Anti-corrosion coatings on steelwork

## Monitoring and Control

### Local Control Panel

- **Location**: Inside substation or external control room
- **Functions**: Control switches, indication lamps, alarms
- **Annunciation**: Audible and visual alarms
- **Interlocking**: Operational interlocks per operating procedures

### Remote Monitoring

- **SCADA**: Voltage, current, power, alarms, equipment status
- **Communication**: Fiber optic or dedicated pilot cables
- **Protocol**: IEC 61850, Modbus, or DNP3
- **Integration**: See [85-80-06-001 SCADA Architecture](../85-80-06_Energy_Management_Systems/85-80-06-001_SCADA_Architecture.md)

## Documentation

### Design Documents

- Site plan and substation layout drawings
- Single-line diagrams (see [85-80-01-A-001](./ASSETS/85-80-01-A-001_Single_Line_Diagrams.svg))
- Civil and structural drawings
- HVAC and fire protection schematics
- Earthing layout and calculations

### Operational Documents

- Operating procedures (normal and emergency)
- Maintenance schedules and procedures
- Safety rules and access procedures
- Equipment manuals and certifications

## Standards and Compliance

### Primary Standards

- [IEC 61936-1](https://www.iec.ch/) - Power installations exceeding 1 kV AC
- [IEC 62271](https://www.iec.ch/) - High-voltage switchgear and controlgear
- [IEC 60076](https://www.iec.ch/) - Power transformers
- [IEEE 80](https://standards.ieee.org/) - Guide for Safety in AC Substation Grounding
- [NFPA 850](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=850) - Recommended Practice for Fire Protection for Electric Generating Plants

### Regional Standards

- Europe: EN standards aligned with IEC
- North America: IEEE, NFPA, NEC
- Local: Building codes, fire codes, electrical safety regulations

## Cross-References

- **85-80-01-001** - Primary Distribution 33kV
- **85-80-01-002** - Secondary Distribution 11kV
- **85-80-01-003** - Low Voltage Distribution 400V
- **85-80-01-005** - Cable Routing Standards
- **85-80-06** - Energy Management Systems
- **85-80-07** - Emergency Power

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
