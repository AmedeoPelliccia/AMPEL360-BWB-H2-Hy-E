# Station System Design

**Document ID:** AMPEL360-02-11-00-DES-RS-003  
**Version:** 1.0.0

## Station System Overview

**Purpose:** Define longitudinal reference system for component location and documentation.

## Station Numbering Convention

### Fuselage Stations (FS)

**Definition:** Longitudinal measurements along aircraft X-axis

**Units:** Millimeters from nose apex (FS 0)

**Range:**
- Nose: FS 0
- Datum: FS 15000
- Tail: FS 28500

### Major Stations

| Station | Location | Description |
|---------|----------|-------------|
| FS 0 | Nose apex | Nose tip, forward-most point |
| FS 2500 | Forward bulkhead | Pressure vessel forward boundary |
| FS 5000 | Flight deck | Cockpit center |
| FS 7500 | Forward cabin | Passenger cabin begins |
| FS 10000 | Forward gear | Main gear forward location |
| FS 12500 | Forward cargo | Cargo door station |
| **FS 15000** | **Datum** | **Reference datum point** |
| FS 17500 | Aft cabin | Galley location |
| FS 20000 | Aft cargo | Aft cargo door |
| FS 22500 | Systems bay | APU, hydraulics |
| FS 25000 | Aft section | Tail cone begins |
| FS 27000 | Aft bulkhead | Pressure vessel aft boundary |
| FS 28500 | Tail | Aft-most point |

## Wing Stations (WS)

**Definition:** Spanwise measurements along aircraft Y-axis

**Origin:** Aircraft centerline (BL 0)

**Range:**
- Centerline: WS 0 (BL 0)
- Maximum width: WS 19000 (BL ±19000, 38m total width)
- Wingtip: WS 26000 (BL ±26000, 52m span)

### Major Wing Stations

| Wing Station | Location | Description |
|--------------|----------|-------------|
| WS 0 | Centerline | Aircraft centerline (BL 0) |
| WS 5000 | Inner wing | Cabin blend region |
| WS 10000 | Mid wing | Primary structure, systems |
| WS 15000 | Outer wing | Wing transition |
| WS 19000 | Max width | Center body maximum width |
| WS 20000 | Outer wing | Control surfaces begin |
| WS 26000 | Wingtip | Wingtip, maximum span |

## Station Spacing

### Primary Structure

**Frame Stations:**
- Spacing: 600mm (standard)
- Designation: FS + frame number
- Example: Frame 25 at FS 15000

**Heavy Frames:**
- Spacing: 3000mm (every 5th frame)
- Designation: HF + number
- Example: HF5 at FS 15000

### Wing Ribs

**Rib Stations:**
- Spacing: 800mm (standard)
- Designation: WS + rib number
- Example: Rib 12.5 at WS 10000

**Heavy Ribs:**
- Spacing: 2400mm (every 3rd rib)
- Designation: HR + number
- Landing gear attachments

## Station Identification

### Drawing Call-outs

**Format:** FS 15000
- Prefix: FS (Fuselage Station)
- Value: 15000 (millimeters from FS 0)
- No decimal point (integer millimeters)

**Wing Format:** WS 10000 or BL ±10000
- WS: Wing Station (spanwise)
- BL: Butt Line (lateral from centerline)
- Sign: ± indicates left/right

### Part Number Integration

**Location Code in P/N:**
- Format: AMPEL-02-11-FS15000-001
- Component: 02-11 (dimensions/geometry)
- Station: FS15000
- Sequence: 001

## Station Tolerances

### Critical Stations

**Pressure Bulkheads:**
- Tolerance: ±0.5mm
- Reason: Pressure vessel integrity
- Inspection: 100% verification

**Landing Gear Attach:**
- Tolerance: ±1.0mm
- Reason: Load path alignment
- Inspection: Measurement required

### Standard Stations

**Frame Locations:**
- Tolerance: ±2.0mm
- Reason: Assembly fit
- Inspection: Sample verification

**General Structure:**
- Tolerance: ±5.0mm
- Reason: Manufacturing variation
- Inspection: Visual

## Manufacturing Use

### Assembly Fixtures

**Fixture Stations:**
- Reference: Datum (FS 15000)
- Measurement: Forward and aft from datum
- Tooling balls: At key stations
- Verification: Laser tracker

### Quality Control

**Inspection Stations:**
- Key features: Major stations
- Documentation: Station-referenced
- Traceability: Part serial number + station
- Archive: Digital records

## Maintenance Documentation

### Access Panels

**Panel Identification:**
- Station location: Primary identifier
- Example: "Access panel at FS 12500"
- Reference: Station + description
- Maintenance manual: Station-indexed

### Component Location

**Line Replaceable Units (LRU):**
- Location: Station + zone
- Example: "APU at FS 22500, Zone D"
- Removal/installation: Station-referenced
- Wiring diagrams: Station-based

## Digital Twin Application

### CAD Model

**Model Structure:**
- Sections: Station-bounded
- Assembly: Station-based insertion
- BOM: Station in description

### Simulation Models

**FEM Mesh:**
- Node locations: Station-referenced
- Element groups: Station ranges
- Load application: At stations
- Results: Station-based output

## Certification Documentation

**Type Certificate:**
- Key stations: Defined
- Tolerances: Specified
- Inspection: Required points
- Traceability: Station-based

**Compliance:**
- ATA 100: Full compliance
- ISO standards: Compatible
- CS-25: Referenced

**Status:** Baseline frozen  
**Approved:** 2024-02-05
