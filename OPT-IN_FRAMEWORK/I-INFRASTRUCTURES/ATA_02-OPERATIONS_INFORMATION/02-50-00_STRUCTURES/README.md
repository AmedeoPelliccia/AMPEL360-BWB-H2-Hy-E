# 02-50-00 STRUCTURES - Infrastructure and GSE Requirements

**AMPEL360 BWB H2 Hy-E Q100 INTEGRA Platform**

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | AMPEL360-02-50-00-OVW-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-12 |
| **Status** | Active |
| **Classification** | Operations Critical |

## Overview

This origin block contains physical infrastructure requirements, ground support equipment (GSE) interfaces, and structural/geometric data necessary for airport operations. Following the AMPEL360_DOCUMENTATION_STANDARD, this directory organizes data related to aircraft physical characteristics and ground infrastructure compatibility.

## Structure

### Reference Systems and Datums (02-50-10 to 02-50-20)
- **02-50-10**: Station Coordinate System
- **02-50-20**: Reference Datums

### Physical Dimensions and Clearances (02-50-30 to 02-50-40)
- **02-50-30**: Maximum Dimensions Envelope
- **02-50-40**: Ground Clearance Data

### Access and Layout (02-50-50 to 02-50-70)
- **02-50-50**: Door Opening Dimensions
- **02-50-60**: Seating Cabin Layout
- **02-50-70**: Aircraft Identification Data

## BWB-Specific Considerations

The Blended Wing Body configuration presents unique infrastructure challenges:

### Dimensional Characteristics
- **Wingspan**: 68.5 m (ICAO Code E)
- **Length**: 55.2 m
- **Height**: 12.8 m
- **Wide center body**: Non-traditional fuselage shape
- **Distributed weight**: Affects ground support requirements

### Ground Operations Impact
- Wider turning radius for taxiway operations
- Special gate requirements (dual jetway capability)
- Non-standard towing/pushback procedures
- Unique cargo loading positions
- Distributed passenger boarding points

### Airport Compatibility

Critical infrastructure requirements:

1. **Taxiway Width**: Minimum 25 m (vs 23 m conventional)
2. **Gate Compatibility**: Code E gates with BWB-specific jetway configuration
3. **Parking Stand**: 80m × 80m minimum
4. **Pavement Strength**: PCN 85/F/B/W/T
5. **Turning Radius**: 40 m minimum centerline radius

## Ground Support Equipment (GSE)

### BWB-Specific GSE Requirements

**Hydrogen Refueling**:
- Cryogenic LH2 refueling cart (mobile or fixed)
- Dual-point refueling capability
- Safety zone: 25m radius during refueling
- Specialized grounding equipment

**Passenger Boarding**:
- Multiple boarding bridges (2-3 points)
- Main deck access: Doors L1, R1
- Upper deck access (if applicable): L2, R2
- Compatible with standard jetways (with adapters)

**Cargo Handling**:
- Standard ULD containers (LD3-45, LD3-45W)
- Distributed cargo doors (forward, aft, belly)
- High-loader compatibility
- Special wide-body cargo loaders for center body

**Maintenance Access**:
- Elevated work platforms for wing inspection
- Engine access stands (fuel cell maintenance)
- H2 tank inspection equipment
- Specialized BWB skin access platforms

## Station Coordinate System

The AMPEL360 uses a body-fixed coordinate system:

- **X-axis (Station)**: Forward positive, datum at nose
- **Y-axis (Buttline)**: Right positive, datum at aircraft centerline
- **Z-axis (Waterline)**: Up positive, datum at lowest point

### Key Reference Points
- **Nose Datum**: Station 0
- **CG Reference**: Station 27.6 m (50% MAC)
- **Main Gear**: Station 32.4 m
- **Aft Datum**: Station 55.2 m

## Ground Clearance Requirements

Critical clearance data for ground operations:

| Point | Clearance | Condition |
|-------|-----------|-----------|
| Wingtip | 2.1 m | Static |
| Belly (lowest) | 1.8 m | MTOW, full fuel |
| Engine intake | 2.5 m | Static |
| Tail | 12.8 m | Static |
| Rotation angle | 12.5° | Takeoff |

## Door Opening Dimensions

### Passenger Doors
- **Type A**: 1.83m × 1.07m (L1/R1 forward)
- **Type III**: 1.52m × 0.91m (Emergency exits)
- **Opening arc**: 180° outward
- **Sill height**: 3.2m above ground

### Cargo Doors
- **Forward cargo**: 2.59m × 1.75m
- **Aft cargo**: 2.59m × 1.75m
- **Bulk cargo**: 1.52m × 1.42m
- **Opening method**: Upward hinging

## Airport Interface Standards

### ICAO Compliance
- **ICAO Annex 14**: Aerodromes
- **ICAO Aerodrome Code**: E (wingspan 52m to <65m) - Note: Requires waiver for 68.5m span
- **Reference Field Length**: 2,800m
- **Pavement Classification Number**: PCN 85/F/B/W/T

### Regional Variations
- **FAA**: Part 139 (Airport Certification)
- **EASA**: CS-ADR-DSN (Aerodrome Design)
- **IATA**: Airport Handling Manual compatibility

## H2 Infrastructure Requirements

### Safety Zones
- **Active refueling**: 25m exclusion radius
- **Parked with H2**: 15m safety zone
- **Maintenance**: 10m minimum clearance
- **Fire equipment**: <3 minutes response time

### Ground Equipment
- LH2 ground cart or hydrant system
- Leak detection equipment
- Emergency defueling capability
- Specialized fire suppression (gaseous H2)

## Design-Driven Structure

Each system under this origin block contains:

- Dimensional drawings and 3D models
- Ground clearance envelopes
- GSE interface specifications
- Airport compatibility analyses
- Loading/servicing procedures
- Safety zone diagrams

## Cross-References

This origin block integrates with:

- **02-00-00_GENERAL**: Overall operations framework
- **02-20-00_SYSTEMS**: Weight and balance, dimensions data
- **02-70-00_PROPULSION**: H2 refueling procedures
- **ATA 06**: Dimensions and Areas
- **ATA 07**: Lifting and Shoring
- **ATA 10**: Parking, Mooring, Storage

## Compliance

All systems within this origin block comply with:
- ICAO Annex 14 (Aerodromes)
- FAA Part 139 (Airport Certification)
- EASA CS-ADR-DSN (Aerodrome Design)
- ISO 19881 (Hydrogen Fueling)
- AMPEL360_DOCUMENTATION_STANDARD v1.4

---

**Status**: ✅ Active  
**Last Updated**: 2025-11-12  
**ICAO Code**: E (with wingspan waiver)
