# 10-MDL-ASM-001 — BWB Parking Configuration

## 1. Purpose

This assembly model defines the complete parking configuration for the AMPEL360 Blended Wing Body (BWB) aircraft with hydrogen propulsion. It addresses the unique geometric and operational requirements of the BWB configuration, including:

- Extended wingspan parking envelope
- Non-traditional aircraft footprint
- Hydrogen safety zones and exclusion areas
- Ground equipment positioning and access
- Multi-point tiedown configuration

## 2. Scope

This model applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **Configuration**: Blended Wing Body with H2 propulsion
- **Parking Scenarios**:
  - Short-term parking (operational between flights)
  - Long-term parking (storage periods)
  - Maintenance parking (with work platforms)
  - Emergency parking (rapid evacuation scenarios)

**Out of Scope**:
- Active taxiing and towing operations (see ATA 09)
- In-hangar storage configurations
- Fueling operations (see ATA 28)

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-ASM-001 |
| Model Type | Assembly |
| CAD System | CATIA V6 |
| Version | 1.0 |
| Status | ACTIVE |
| Created | 2025-12-09 |
| Last Modified | 2025-12-09 |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| CATIA V6 | 10-MDL-ASM-001_BWB_Parking.CATProduct | `cad-native/catia/` | TBD |
| STEP AP242 | 10-MDL-ASM-001_BWB_Parking.step | `exchange-formats/step/` | TBD |
| JT Open | 10-MDL-ASM-001_BWB_Parking.jt | `exchange-formats/jt/` | TBD |
| glTF 2.0 | 10-MDL-ASM-001_BWB_Parking.glb | `visualization/gltf/` | TBD |

## 5. Assembly Description

### 5.1 Overall Configuration

The BWB parking configuration assembly includes:

1. **Aircraft envelope** (reference geometry)
   - BWB outer mold line (OML)
   - Wing span: ~80m (TBD)
   - Length: ~60m (TBD)
   - Ground clearance zones

2. **Parking pad layout**
   - Parking spot boundaries
   - Safety markings and zones
   - Access pathways
   - H2 exclusion zones

3. **Tiedown points** (6-point configuration)
   - Wing tiedown locations (4 points)
   - Nose tiedown location (1 point)
   - Tail tiedown location (1 point)

4. **Ground equipment positions**
   - GPU (Ground Power Unit) location
   - H2 detection equipment
   - Fire suppression equipment
   - Access platforms

### 5.2 BWB-Specific Considerations

**Extended Wingspan:**
- Parking spot width: 85m minimum
- Wingtip clearance: 2.5m minimum each side
- Adjacent aircraft spacing: 5m minimum

**Integrated Wing-Body Structure:**
- Non-traditional load distribution
- Multiple tiedown points across span
- Distributed ground support points

**Low Ground Clearance:**
- Belly clearance: ~1.2m (TBD)
- Landing gear configuration
- Access limitations under aircraft

### 5.3 H2 Safety Zones

**Primary H2 Safety Zone:**
- Radius: 10m from fuel tank vents
- No open flames or spark sources
- Continuous H2 monitoring required

**Secondary H2 Safety Zone:**
- Radius: 25m from fuel system
- Controlled access during fueling/defueling
- Emergency equipment staging area

**Ventilation Requirements:**
- Outdoor parking preferred
- Wind direction monitoring
- Forced ventilation for enclosed areas

## 6. Geometry Description

### 6.1 Key Dimensions

| Dimension | Value (mm) | Notes |
|-----------|------------|-------|
| Overall Length | TBD | Aircraft nose to tail |
| Wingspan | TBD | Wingtip to wingtip |
| Parking Envelope Length | TBD | Including clearances |
| Parking Envelope Width | TBD | Including clearances |
| Ground Contact Points | TBD | Landing gear configuration |

### 6.2 Coordinate System

- **Origin**: Aircraft nose landing gear ground contact point
- **X-axis**: Forward (nose direction)
- **Y-axis**: Right wing direction
- **Z-axis**: Up (vertical)

All tiedown and equipment positions referenced to this coordinate system.

## 7. Component Assembly Structure

```
10-MDL-ASM-001_BWB_Parking_Configuration
├── Aircraft_Reference_Geometry
│   ├── BWB_Outer_Mold_Line
│   ├── Landing_Gear_Positions
│   └── Fuel_System_Locations
├── Parking_Pad_Layout
│   ├── Parking_Spot_Markings
│   ├── Safety_Zones
│   └── Access_Pathways
├── Tiedown_System (10-MDL-ASM-002)
│   ├── Wing_Tiedown_Points (4x)
│   ├── Nose_Tiedown_Point (1x)
│   └── Tail_Tiedown_Point (1x)
├── Ground_Equipment_Layout
│   ├── GPU_Position
│   ├── H2_Detector_Stations (4x)
│   └── Fire_Suppression_Equipment (2x)
└── Documentation_Elements
    ├── Dimension_Annotations
    └── Safety_Zone_Graphics
```

## 8. Materials

Not applicable - this is a layout/configuration assembly with reference geometry and documentation elements.

## 9. H2/BWB Considerations

### 9.1 BWB Configuration Impact

**Positive Aspects:**
- Large wing area provides multiple stable tiedown points
- Wide stance improves stability in crosswinds
- Integrated structure simplifies load paths

**Challenges:**
- Requires oversized parking spots
- Limited under-aircraft access
- Special ground equipment required
- Wingtip clearance critical

### 9.2 Hydrogen System Impact

**Safety Requirements:**
- H2 leak detection at multiple points
- Emergency ventilation capability
- Exclusion zones enforced with barriers
- Fire suppression pre-positioned

**Operational Considerations:**
- Wind direction monitoring mandatory
- Personnel training on H2 hazards
- Emergency procedures posted
- Communication systems for alerts

## 10. Related Documentation

### Related Models
- [10-MDL-ASM-002 — Tiedown System Assembly](./10-MDL-ASM-002_Tiedown_System_Assembly.md)
- [10-MDL-ASM-004 — H2 Safety Equipment Assembly](./10-MDL-ASM-004_H2_Safety_Equipment_Assembly.md)

### Related Drawings
- TBD: 10-00-04-AXXX_Parking_Layout_Plan
- TBD: 10-00-04-AXXX_H2_Safety_Zone_Plan
- TBD: 10-00-04-AXXX_Tiedown_Point_Locations

### Related Specifications
- TBD: REQ-10-001 — Parking Configuration Requirements
- TBD: REQ-10-050 — H2 Safety Zone Requirements
- TBD: REQ-10-100 — BWB Ground Handling Requirements

### Related Standards
- **ATA 10** — Parking, Mooring, Storage & RTS
- **SAE AS6968** — Hydrogen Aircraft Systems
- **CS-25** — Certification Specifications for Large Aeroplanes
- **NFPA 2** — Hydrogen Technologies Code

## 11. Usage and Applications

This parking configuration assembly is used for:

1. **Airport Facilities Planning**
   - Design of parking spots and aprons
   - Safety zone layout and marking
   - Ground equipment placement

2. **Ground Operations Training**
   - Visual reference for ground crews
   - Safety zone awareness training
   - Equipment positioning procedures

3. **Simulation and Analysis**
   - Ground operations simulation
   - Wind load analysis on parked aircraft
   - Emergency evacuation planning

4. **Certification Evidence**
   - Demonstration of compliance with CS-25
   - H2 safety zone verification
   - Ground handling procedures validation

## 12. Validation and Verification

### Design Validation
- [ ] Parking envelope verified against airport standard sizes
- [ ] Tiedown point loads analyzed (see 10-SIM-FEA-001)
- [ ] H2 safety zones comply with SAE AS6968
- [ ] Ground clearances verified for all aircraft attitudes

### Operational Validation
- [ ] Mock-up parking trials conducted
- [ ] Ground crew accessibility verified
- [ ] Emergency procedures tested
- [ ] Equipment positioning validated

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Design Team | Initial release |

## 14. Approvals

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Design Engineer | TBD | TBD | TBD |
| Lead Engineer | TBD | TBD | TBD |
| Safety Engineer | TBD | TBD | TBD |
| Configuration Manager | TBD | TBD | TBD |

---

## Document Control

- **Document ID**: 10-MDL-ASM-001
- **Version**: 1.0
- **Status**: ACTIVE
- **Classification**: Technical
- **Last Updated**: 2025-12-09
- **Owner**: AMPEL360 ATA 10 Design Team
- **Repository**: AMPEL360-BWB-H2-Hy-E
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.

---

**See Also:**
- [MODELS README.md](../README.md)
- [MODELS Index](../00_INDEX.md)
