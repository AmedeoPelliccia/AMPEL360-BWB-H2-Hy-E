# 02-50-00-002: Physical Infrastructure Map

## Document Information

- **Document ID**: 02-50-00-002
- **Title**: Physical Infrastructure Map for ATA 02 Structures
- **Version**: 1.0.0
- **Status**: DRAFT
- **Date**: 2025-11-21
- **Author**: AMPEL360 Infrastructure Planning Team
- **Applicable To**: AMPEL360 BWB H2-Hy-E Operations Infrastructure

## 1. Purpose

This document describes and diagrams the physical infrastructure map for all structures within ATA 02-50. It defines the spatial relationships, locations, zones, and interfaces between structural systems supporting operations information for the AMPEL360 BWB hydrogen-electric aircraft program.

## 2. Scope

The physical infrastructure map encompasses:

- **Aircraft-Mounted Structures**: Locations within cockpit and cabin
- **Ground Infrastructure**: Data centers, operations centers, ground support areas
- **Communication Networks**: Physical routing of cables, antennas, and ground stations
- **H₂ Operations Zones**: Safety zones around hydrogen refueling infrastructure
- **Maintenance Access**: Access routes, platforms, and service zones

## 3. Infrastructure Zones

### 3.1 Zone Classification

Infrastructure is organized into functional zones:

| Zone ID | Zone Name | Description | Primary Structures |
|---------|-----------|-------------|-------------------|
| **A-ZONE** | **Aircraft Interior** | Cockpit and cabin | EFB mounts, display mounts, access panels |
| **G-ZONE** | **Ground Operations** | Apron, taxiway, gate areas | H₂ refueling, GSE, loading equipment |
| **D-ZONE** | **Data Center** | Server and network infrastructure | Server racks, cooling, power distribution |
| **O-ZONE** | **Operations Center** | Control rooms, dispatch | Video walls, workstation mounts, displays |
| **C-ZONE** | **Communication Nodes** | Distributed communication points | Antenna mounts, cable junctions, WiFi APs |
| **S-ZONE** | **Sensor Network** | Monitoring and measurement locations | Sensor mounts, environmental enclosures |

### 3.2 Zone Relationships Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    AIRPORT ENVIRONMENT                       │
│                                                              │
│  ┌──────────────┐      ┌──────────────┐                    │
│  │   O-ZONE     │◄────►│   D-ZONE     │                    │
│  │  Operations  │ Fiber │ Data Center  │                    │
│  │   Center     │ Link  │   (Racks)    │                    │
│  └──────────────┘      └──────┬───────┘                    │
│         ▲                      │                             │
│         │                      │ Network                     │
│         │ RF Link              │ Backbone                    │
│         │                      ▼                             │
│  ┌──────┴───────────────────────────────┐                  │
│  │          C-ZONE (Communications)      │                  │
│  │  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐ │                  │
│  │  │WiFi │  │Cell │  │Sat  │  │VHF  │ │                  │
│  │  │ AP  │  │Tower│  │Dish │  │Radio│ │                  │
│  │  └─────┘  └─────┘  └─────┘  └─────┘ │                  │
│  └───────────────────┬──────────────────┘                  │
│                      │                                       │
│  ┌───────────────────▼──────────────────┐                  │
│  │         G-ZONE (Ground Ops)          │                  │
│  │  ┌──────────┐    ┌──────────┐       │                  │
│  │  │ H₂ Fuel  │    │   GSE    │       │                  │
│  │  │ Station  │    │ Parking  │       │    ┌─────────┐  │
│  │  └─────┬────┘    └──────────┘       │    │ S-ZONE  │  │
│  │        │                             │    │ Sensors │  │
│  │        │  Refuel                     │    └─────────┘  │
│  │        ▼                             │                  │
│  │  ┌──────────────────────────┐       │                  │
│  │  │       A-ZONE              │       │                  │
│  │  │  ┌────────────────────┐  │       │                  │
│  │  │  │ Cockpit (EFB Mount)│  │       │                  │
│  │  │  └────────────────────┘  │       │                  │
│  │  │      AIRCRAFT             │       │                  │
│  │  └──────────────────────────┘       │                  │
│  └──────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

## 4. Aircraft-Mounted Structures (A-ZONE)

### 4.1 Cockpit Structures

**Location**: Forward fuselage, flight deck

| Structure | Station | Frame | Description |
|-----------|---------|-------|-------------|
| Pilot EFB Mount | STA 120 | FR 10 | Left-side panel-mounted EFB bracket |
| Copilot EFB Mount | STA 120 | FR 10 | Right-side panel-mounted EFB bracket |
| Central Display Stack | STA 125 | FR 12 | Center console display mounting |
| Overhead Panel Access | STA 115 | FR 8 | Quick-access panels for avionics |

**Cross-Reference**: [02-50-01_EFB_Mounting_Systems/02-50-01-002_Cockpit_Integration.md](./02-50-01_EFB_Mounting_Systems/02-50-01-002_Cockpit_Integration.md)

### 4.2 Cabin Structures

**Location**: Main cabin, passenger areas

| Structure | Zone | Description |
|-----------|------|-------------|
| Cabin Display Mounts | Rows 1-20 | Seatback and overhead display mounts |
| WiFi Access Points | Distributed | Ceiling-mounted AP brackets (every 5 rows) |
| Sensor Enclosures | Forward/Aft | Environmental monitoring sensors |

### 4.3 Coordinate System

Aircraft structures use the standard aircraft coordinate system:
- **Station (STA)**: Longitudinal position (inches aft of datum)
- **Buttline (BL)**: Lateral position (inches from centerline)
- **Waterline (WL)**: Vertical position (inches above datum)

## 5. Ground Infrastructure (G-ZONE)

### 5.1 H₂ Refueling Infrastructure

**Location**: Apron area, designated H₂ zones

#### Safety Zones
Per [ISO 19880-1](https://www.iso.org/standard/71940.html) and [NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code):

- **Zone 1** (0-3m radius): No ignition sources, intrinsically safe equipment only
- **Zone 2** (3-7.5m radius): Protected electrical equipment, ventilation required
- **Zone 3** (7.5-15m radius): Standard industrial equipment, monitoring sensors

```
         ┌─────────────────────────────────┐
         │      Zone 3 (15m radius)         │
         │   ┌─────────────────────────┐   │
         │   │  Zone 2 (7.5m radius)   │   │
         │   │   ┌─────────────────┐   │   │
         │   │   │ Zone 1 (3m)     │   │   │
         │   │   │    ┌────┐       │   │   │
         │   │   │    │ H₂ │       │   │   │
         │   │   │    │Fueler      │   │   │
         │   │   │    └────┘       │   │   │
         │   │   └─────────────────┘   │   │
         │   └─────────────────────────┘   │
         │           Aircraft               │
         │            [BWB]                 │
         └─────────────────────────────────┘
```

**Key Structures**:
- H₂ dispenser mounting pad (reinforced concrete, grounding)
- Safety barrier posts and visual markings
- Emergency shutoff valve enclosures
- Ventilation and gas detection sensor mounts

**Cross-Reference**: [02-50-05_Ground_Equipment_Structures/02-50-05-002_H2_Refueling_Structure.md](./02-50-05_Ground_Equipment_Structures/02-50-05-002_H2_Refueling_Structure.md)

### 5.2 Ground Support Equipment (GSE)

**Location**: Gate and maintenance areas

| Equipment | Structure | Location |
|-----------|-----------|----------|
| Ground Power Unit (GPU) | Wheeled cart mount | Gate apron |
| Nitrogen/Air Service | Ground-mounted panel | Service pit |
| Loading Equipment | Bridge/belt interfaces | Gate |
| Tow Tractor Hitch | Aircraft nose gear area | Tarmac |

## 6. Data Center Infrastructure (D-ZONE)

### 6.1 Data Center Layout

**Location**: Airport operations building, Level 2

#### Floor Plan Overview

```
┌─────────────────────────────────────────────────────┐
│         DATA CENTER (D-ZONE)                         │
│                                                      │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐   │
│  │ Rack 1 │  │ Rack 2 │  │ Rack 3 │  │ Rack 4 │   │
│  │ (42U)  │  │ (42U)  │  │ (42U)  │  │ (42U)  │   │
│  │        │  │        │  │        │  │        │   │  Hot
│  │ Net    │  │ App    │  │ DB     │  │ Backup │   │  Aisle
│  └────────┘  └────────┘  └────────┘  └────────┘   │  ▼
│      ▲           ▲           ▲           ▲         │
│  ────┴───────────┴───────────┴───────────┴──────   │  Cold
│          Raised Floor (Cable Routing)              │  Aisle
│  ────┬───────────┬───────────┬───────────┬──────   │  ▲
│      │           │           │           │         │
│  ┌───▼────┐  ┌───▼────┐  ┌───▼────┐  ┌───▼────┐   │
│  │ PDU 1  │  │ PDU 2  │  │ UPS 1  │  │ UPS 2  │   │
│  │(Power) │  │(Power) │  │(Backup)│  │(Backup)│   │
│  └────────┘  └────────┘  └────────┘  └────────┘   │
│                                                      │
│  [CRAC 1]  ◄──Cooling──►  [CRAC 2]                 │
│                                                      │
│  Access Door ●                   Emergency Exit ●   │
└─────────────────────────────────────────────────────┘
```

#### Key Dimensions
- **Floor Space**: 400 m² (20m × 20m)
- **Ceiling Height**: 3.5m (raised floor: 0.6m, clear: 2.9m)
- **Rack Rows**: 4 rows, 10 racks each
- **Aisle Width**: Cold aisle 1.2m, hot aisle 0.9m

**Cross-Reference**: [02-50-02_Server_Infrastructure/02-50-02-001_Data_Center_Layout.md](./02-50-02_Server_Infrastructure/02-50-02-001_Data_Center_Layout.md)

### 6.2 Rack Locations

Racks are identified by row and position:
- **Format**: D-ZONE-RxPy (Row x, Position y)
- **Example**: D-ZONE-R1P5 = Row 1, Position 5

Each rack interfaces with:
- Raised floor cable entry
- Overhead cable tray
- PDU power feed
- Grounding busbar
- Hot aisle exhaust plenum

## 7. Operations Center Infrastructure (O-ZONE)

### 7.1 Operations Center Layout

**Location**: Airport operations building, Level 3

```
┌───────────────────────────────────────────────────────┐
│          OPERATIONS CENTER (O-ZONE)                    │
│                                                        │
│  ┌──────────────────────────────────────────────┐    │
│  │       VIDEO WALL (6×3 displays)              │    │
│  │  ┌────┬────┬────┬────┬────┬────┐            │    │
│  │  │    │    │    │    │    │    │            │    │
│  │  ├────┼────┼────┼────┼────┼────┤            │    │
│  │  │    │    │    │    │    │    │            │    │
│  │  ├────┼────┼────┼────┼────┼────┤            │    │
│  │  │    │    │    │    │    │    │            │    │
│  │  └────┴────┴────┴────┴────┴────┘            │    │
│  └──────────────────────────────────────────────┘    │
│                                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │ Worksta- │  │ Worksta- │  │ Worksta- │           │
│  │ tion 1   │  │ tion 2   │  │ tion 3   │           │
│  │ [2×LCD]  │  │ [2×LCD]  │  │ [2×LCD]  │           │
│  └──────────┘  └──────────┘  └──────────┘           │
│                                                        │
│  Control Room Access ●                                │
└───────────────────────────────────────────────────────┘
```

**Key Structures**:
- Video wall frame (steel, wall-mounted, load capacity 500 kg)
- Workstation monitor arms (dual articulating, VESA-compliant)
- Raised access floor for cable management
- Ergonomic console desks with integrated cable routing

**Cross-Reference**: [02-50-07_Display_Mounting_Systems/02-50-07-001_Operations_Center_Displays.md](./02-50-07_Display_Mounting_Systems/02-50-07-001_Operations_Center_Displays.md)

## 8. Communication Infrastructure (C-ZONE)

### 8.1 Network Backbone Routing

**Physical Layer**: Fiber optic and Cat6a Ethernet

#### Primary Routes
1. **Data Center to Operations Center**: 150m fiber run, redundant paths
2. **Operations Center to Apron**: 500m fiber run via underground conduit
3. **Apron Distribution**: Distributed WiFi APs and ground station links

#### Cable Tray System
- **Main Backbone**: 600mm wide ladder tray, overhead routing
- **Branch Routes**: 300mm tray, ceiling and wall-mounted
- **Fire Zones**: Fire-stop penetrations at zone boundaries

**Cross-Reference**: [02-50-06_Cable_Management_Systems/02-50-06-001_Cable_Tray_Systems.md](./02-50-06_Cable_Management_Systems/02-50-06-001_Cable_Tray_Systems.md)

### 8.2 Antenna Locations

| Antenna Type | Location | Mounting | Coverage |
|--------------|----------|----------|----------|
| WiFi 6 AP | Terminal roof, every 50m | Pole mount | 100m radius |
| LTE Base Station | Tower, 30m height | Mast mount | 2km radius |
| Satcom Dish | Roof, central building | Fixed pedestal | Global coverage |
| VHF Radio | Tower, 25m height | Mast mount | 50km radius |

**Cross-Reference**: [02-50-03_Communication_Infrastructure/02-50-03-003_Antenna_Systems.md](./02-50-03_Communication_Infrastructure/02-50-03-003_Antenna_Systems.md)

## 9. Sensor Network (S-ZONE)

### 9.1 Environmental Monitoring Sensors

Distributed sensors for operations monitoring:

| Sensor Type | Locations | Quantity | Purpose |
|-------------|-----------|----------|---------|
| Temperature | Aircraft, data center, apron | 50+ | Thermal monitoring |
| Humidity | Data center, storage areas | 20+ | Environmental control |
| H₂ Detection | Refueling zones | 12+ | Safety monitoring |
| Wind Speed/Direction | Apron, roof | 4 | Operations safety |
| LIDAR | Approach paths | 2 | Obstacle detection |

**Cross-Reference**: [02-50-04_Sensor_Mounting_Systems/02-50-04-001_Sensor_Locations.md](./02-50-04_Sensor_Mounting_Systems/02-50-04-001_Sensor_Locations.md)

## 10. Interface Control

### 10.1 Physical Interface Requirements

All structures must provide documented interfaces for:

1. **Mechanical Attachment**: Fastener types, torques, load ratings
2. **Electrical Grounding**: Grounding points, resistance requirements
3. **Cable Entry/Exit**: Grommet types, strain relief, IP ratings
4. **Maintenance Access**: Clearances, tool access, safety provisions

### 10.2 Interface Control Documents (ICDs)

ICDs are maintained for critical interfaces:
- Aircraft-to-ground interfaces (refueling, power, data)
- System-to-structure interfaces (equipment mounting)
- Structure-to-structure interfaces (cable routing, penetrations)

**Cross-Reference**: [02-00-05_Interfaces](../02-00_GENERAL/02-00-05_Interfaces/)

## 11. Geospatial Coordinates

### 11.1 Airport Reference System

*(Example coordinates for reference airport)*

- **Datum**: WGS84
- **Airport Reference Point (ARP)**: 45.5017° N, -122.6731° W (example)

### 11.2 Key Structure Coordinates

| Structure | Latitude | Longitude | Elevation (m MSL) |
|-----------|----------|-----------|-------------------|
| Data Center | 45.5020° N | -122.6735° W | 12 |
| Operations Center | 45.5020° N | -122.6735° W | 18 |
| H₂ Refueling Zone 1 | 45.5015° N | -122.6728° W | 10 |
| Ground Station | 45.5025° N | -122.6740° W | 15 |

*(Coordinates are illustrative and must be updated for specific deployment locations)*

## 12. Maintenance Access Routes

### 12.1 Access Corridors

Clear access routes are maintained for:
- **Emergency egress**: Minimum 1.2m width, illuminated, unobstructed
- **Equipment transport**: Minimum 2.0m width, door clearances, floor loading
- **Routine maintenance**: Ladder access, fall protection anchors

### 12.2 Restricted Zones

Some zones have access restrictions:
- **H₂ Safety Zones**: Trained personnel only, hot work permit required
- **Data Center**: Badge access, two-person rule for critical systems
- **Roof Access**: Fall protection equipment required

## 13. Future Expansion

### 13.1 Growth Provisions

The infrastructure map includes provisions for future expansion:
- **Data center**: Space for 20 additional racks
- **Apron area**: Reserved space for second H₂ refueling station
- **Cable routing**: 30% spare capacity in trays and conduits

### 13.2 Scalability

Design principles for scalable infrastructure:
- Modular rack systems
- Redundant power and cooling paths
- Flexible cable management with pull points
- Standardized mounting interfaces

## 14. Summary

This physical infrastructure map provides a comprehensive spatial framework for all structures within ATA 02-50. It establishes clear zones, locations, relationships, and interfaces that enable safe, efficient, and maintainable operations of the AMPEL360 BWB H2-Hy-E aircraft and its supporting infrastructure.

For detailed specifications of each structure type, refer to the respective subsystem documentation within [02-50_Structures](./README.md).

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.

---
