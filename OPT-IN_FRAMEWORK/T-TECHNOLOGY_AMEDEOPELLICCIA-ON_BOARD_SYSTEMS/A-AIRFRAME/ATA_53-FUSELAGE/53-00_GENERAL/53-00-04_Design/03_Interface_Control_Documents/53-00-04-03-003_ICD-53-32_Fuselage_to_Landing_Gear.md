# ICD-53-32: Fuselage to Landing Gear Interface

## 1. Scope

This Interface Control Document (ICD) defines the interface between:
- **System A**: ATA 53 (Fuselage) – Landing gear bays and attachment structure
- **System B**: ATA 32 (Landing Gear) – Main and nose landing gear

**Aircraft**: AMPEL360 BWB  
**Zones**: Zone 100 (nose gear), Zone 400 (main gear)

## 2. Interface Overview

### 2.1 Main Landing Gear (MLG)

**Location**: Zone 400, Center Wing Box  
**Configuration**: Two main gear assemblies (left and right)  
**Retraction**: Aft retraction into centerbody bays

**Key Interface Points**:
- Forward trunnion (pivot point)
- Aft drag strut attachment
- Side brace attachment
- Hydraulic and electrical connections

### 2.2 Nose Landing Gear (NLG)

**Location**: Zone 100, Nose Section  
**Configuration**: Single nose gear assembly  
**Retraction**: Forward retraction into nose bay

**Key Interface Points**:
- Main trunnion (pivot point)
- Drag strut attachment
- Steering actuator attachment
- Hydraulic and electrical connections

## 3. Geometric Interface

### 3.1 Coordinate System

**Aircraft Reference**: X (forward), Y (right), Z (up), origin at nose

### 3.2 Main Landing Gear – Left (MLG-L)

**Forward Trunnion Location**:
- X = 540.5 m (FS 540500)
- Y = -4.2 m (BL -4200, left side)
- Z = -1.8 m (WL -1800)

**Aft Drag Strut Attachment**:
- X = 541.8 m
- Y = -4.0 m
- Z = -1.6 m

**Bay Dimensions**:
- Length (X): 2.5 m
- Width (Y): 1.8 m
- Height (Z): 2.2 m

**Clearances**:
- Minimum clearance to structure: 50 mm (retracted position)
- Minimum clearance during retraction: 25 mm

### 3.3 Main Landing Gear – Right (MLG-R)

**Mirrored** from MLG-L about aircraft centerline (Y = 0)

### 3.4 Nose Landing Gear (NLG)

**Main Trunnion Location**:
- X = 8.5 m (FS 8500)
- Y = 0.0 m (on centerline)
- Z = -1.2 m (WL -1200)

**Bay Dimensions**:
- Length (X): 1.8 m
- Width (Y): 1.2 m
- Height (Z): 1.6 m

### 3.5 Tolerances

- Trunnion location: ±1.0 mm
- Bay dimensions: ±5.0 mm
- Clearances: +5.0 / -0.0 mm (maintain minimum)

## 4. Load Interface

### 4.1 Design Load Cases

| Load Case | MLG Vertical (kN) | MLG Side (kN) | MLG Drag/Braking (kN) | NLG Vertical (kN) |
|-----------|------------------:|-------------:|----------------------:|-----------------:|
| Landing (2-point) | 1,850 | 250 | 400 | 650 |
| Landing (1-wheel) | 2,200 | 400 | 480 | 550 |
| Braking (max) | 1,200 | 150 | 800 | 400 |
| Taxi (rough) | 950 | 180 | 200 | 350 |
| Towing | 600 | 200 | 300 | 200 |

**Notes**:
- Loads are per gear assembly (MLG-L or MLG-R)
- Ultimate loads = 1.5 × Limit loads shown
- Fatigue spectrum provided separately

### 4.2 Load Distribution

**Main Gear Forward Trunnion**:
- Carries 65% of vertical load
- Carries 80% of side load
- Primary pivot point

**Main Gear Aft Drag Strut**:
- Carries 35% of vertical load
- Carries 100% of drag/braking load
- Stabilizes gear in extended position

**Main Gear Side Brace**:
- Carries 100% of side load in extended position
- Over-center locking mechanism

### 4.3 Fatigue Loads

Fatigue spectrum based on:
- 60,000 flight cycles (Design Service Goal)
- Typical landing load distribution
- Taxi and ground operations

**Reference**: ATA 32 Fatigue Spectrum Document

## 5. Structural Interface

### 5.1 Fuselage Structure (ATA 53)

**Configuration Items**:
- **CI-53-100-BAY-NLG**: Nose gear bay structure
- **CI-53-400-BAY-MLG-L**: Left main gear bay structure
- **CI-53-400-BAY-MLG-R**: Right main gear bay structure

**Materials**:
- Bay structure: CFRP with titanium fittings
- Trunnions: Titanium Ti-6Al-4V
- Bushings: Bronze or steel

**Key Structural Elements**:
- Trunnion beams (primary load path)
- Bay door frame reinforcements
- Bulkheads and floors

### 5.2 Landing Gear (ATA 32)

**Materials**:
- Main structure: High-strength steel (300M)
- Trunnion pins: Titanium or steel
- Hydraulic components: Aluminum, steel

**Key Components**:
- Shock strut
- Side brace and drag strut
- Wheels and brakes
- Retraction actuators

## 6. Bay Door Interface

### 6.1 Main Gear Bay Doors

**Configuration**: Two-piece clamshell doors per bay  
**Actuation**: Mechanically linked to gear extension/retraction  
**Material**: CFRP sandwich panels

**Interface to Fuselage**:
- Hinge points: 4 per door
- Latch points: 2 per door
- Seal interface: Elastomeric seal, continuous

**Clearances During Operation**:
- Door-to-gear: 30 mm minimum
- Door-to-door: 10 mm gap (closed position)

### 6.2 Nose Gear Bay Door

**Configuration**: Single door, forward hinging  
**Actuation**: Mechanically linked to gear extension  
**Material**: CFRP sandwich

## 7. Systems Interface

### 7.1 Hydraulic

- Hydraulic lines routed through bay structure
- Fuselage provides: Routing supports, clamps, penetrations
- Gear provides: Flexible hoses, connections

### 7.2 Electrical

- Electrical harnesses for gear position sensors, lights
- Fuselage provides: Wire routing, connectors, penetrations
- Gear provides: Sensors, harness

### 7.3 Fire Protection

- Main gear bays: Fire detection and suppression
- Fuselage provides: Fire barriers, ventilation, drain
- Gear provides: No special requirements

## 8. Installation and Assembly

### 8.1 Assembly Sequence

1. Install trunnion fittings in fuselage structure
2. Install bay door hinges and latches
3. Install landing gear (jacking required)
4. Connect hydraulic and electrical systems
5. Install bay doors
6. Functional test (extension, retraction, door operation)

### 8.2 Fasteners and Hardware

- Trunnion bolts: Titanium, minimum diameter 30 mm
- Torque: Per ATA 32 Installation Manual
- Safety: Lock-wire or safety bolts

### 8.3 Access and Tooling

- Bay access: Through bay doors (gear retracted)
- Installation access: External (gear) and internal (fittings)
- Special tooling: Trunnion installation jig, alignment tools

## 9. Inspection and Maintenance

### 9.1 Inspection Access

- Visual inspection: Through bay doors
- Detailed inspection: Gear removed, access panels
- NDI: Ultrasonic for bushings, radiography for fittings

### 9.2 Inspection Intervals

- Pre-flight: Visual check, no leaks, door operation
- A-check (500 FH): Detailed visual, functional test
- C-check (3000 FH): Detailed inspection, NDI on fittings

### 9.3 Maintenance Tasks

- Lubrication: Trunnion bushings, door hinges
- Adjustment: Door fit, latch engagement
- Replacement: Bushings, seals, worn components

## 10. Environmental Requirements

- **Temperature**: -54°C to +71°C (operational)
- **Humidity**: Up to 100% RH
- **Contamination**: Mud, water, de-icing fluid exposure
- **Corrosion Protection**: All steel components cadmium plated or equivalent

## 11. Verification and Testing

### 11.1 Interface Verification

- Fit check: First article installation
- Load verification: Rig test of trunnion interface
- Fatigue test: Full-scale fatigue test (gear and structure)

### 11.2 Acceptance Criteria

- Geometric: ±1.0 mm on trunnion location
- Load: Ultimate load capability demonstrated
- Fatigue: No failure or significant crack growth in test

## 12. Design Responsibility Matrix

| Item | Design Responsibility | Analysis Responsibility | Test Responsibility |
|------|----------------------|-------------------------|---------------------|
| Trunnion fittings | ATA 53 | ATA 53 | Joint |
| Bay structure | ATA 53 | ATA 53 | ATA 53 |
| Bay doors | ATA 53 | ATA 53 | ATA 53 |
| Landing gear | ATA 32 | ATA 32 | ATA 32 |
| Interface loads | Joint | Joint | Joint |
| System integration | Joint | Joint | Joint |

## 13. Change Control

**ICD Version**: 1.0  
**ICD Owner**: ATA 53 Chief Design Engineer (primary), ATA 32 Chief Engineer (secondary)

**Change Process**:
1. Change request submitted to both ATA 53 and ATA 32
2. Impact assessment by both teams
3. Joint review meeting
4. Approval by both Chief Engineers and CCB
5. Update ICD, increment version
6. Notify all stakeholders

**Major Changes** (requiring re-approval):
- Trunnion location change
- Load case change
- Material change

**Minor Changes** (notification only):
- Clarifications, corrections
- Tolerance relaxation (if justified)
- Document updates

## 14. References

- **ATA 53 Requirements**: [../../53-00-03_Requirements/](../../53-00-03_Requirements/)
- **ATA 53 Configuration Items**: [../02_Configuration_Items/](../02_Configuration_Items/)
  - CI-53-100-BAY-NLG
  - CI-53-400-BAY-MLG-L
  - CI-53-400-BAY-MLG-R
- **ATA 32 Landing Gear Design Specification**: (ATA 32 document)
- **CS-25.721**: [Landing Gear: general](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)
- **CS-25.723**: [Shock Absorption Tests](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)

---

## Document Control

- **Document ID**: ICD-53-32
- **Title**: Fuselage to Landing Gear Interface
- **Version**: 1.0
- **Date**: 2025-11-22
- **Owner**: ATA 53 Chief Design Engineer
- **Approval**: _[to be completed]_
- **Status**: DRAFT
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

**Signatures**:
- ATA 53 Chief Design Engineer: _[to be completed]_
- ATA 32 Chief Engineer: _[to be completed]_
- Configuration Manager: _[to be completed]_

**AI Assistance**:
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Human approver: _[to be completed]_.
- Last AI update: _2025-11-22_.
