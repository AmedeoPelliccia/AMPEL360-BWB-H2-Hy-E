# 53-00-03-04-002 — Occupant Protection

## Requirement ID
**[53-00-03-04-002](./53-00-03-04-002_Occupant_Protection.md)**

## Title
Occupant Protection

## Category
[04_Crashworthiness](.  /)

## Description
The fuselage structure and cabin interior shall provide adequate protection for occupants during emergency landing scenarios, minimizing injury through proper load paths, energy absorption, and prevention of hazardous deformations or projections.  

## Rationale
Occupant protection is the primary goal of crashworthiness design. The fuselage must work as an integrated system with seats, restraints, and interior to maximize occupant survival and minimize injuries. 

For the AMPEL360 BWB hydrogen-hybrid aircraft, occupant protection is particularly critical due to:
- **Blended Wing Body configuration**: Non-conventional cabin layout with multiple seating zones and orientations
- **Wide cabin cross-section**: Increased occupant count and diversity of seat positions
- **Multi-aisle design**: Complex evacuation paths requiring protected egress corridors
- **Hydrogen fuel system**: Additional hazards requiring separation and containment strategies
- **Novel interior arrangements**: Potential for non-traditional seat orientations and configurations

## Acceptance Criteria

### Summary Table
| # | Parameter | Requirement | Verification |
|---|-----------|-------------|--------------|
| 1 | Head Injury Criterion (HIC) | <1,000 | Dynamic test |
| 2 | Occupant loads | Below CS-25.562(c) thresholds | Dynamic test |
| 3 | Sharp edges/projections | None in contact areas | Inspection |
| 4 | Overhead bin retention | Secured under crash loads | Test |
| 5 | Emergency exit operability | Operable post-crash | Test |
| 6 | Survival space | ≥12-inch radius around torso | Test + Analysis |
| 7 | Floor deflection | <2 inches relative to seat tracks | Test |

### Detailed Acceptance Criteria

#### 1. Head Injury Criterion (HIC)
| Position | HIC Limit | Measurement | Reference |
|----------|-----------|-------------|-----------|
| All occupant positions | HIC ≤ 1,000 | ATD head accelerometer | CS-25.562(c)(5) |
| Crew positions | HIC ≤ 1,000 | ATD head accelerometer | CS-25.  562(c)(5) |
| Attendant positions | HIC ≤ 1,000 | ATD head accelerometer | CS-25. 562(c)(5) |

**HIC Calculation:**
$$HIC = \left[ \frac{1}{t_2 - t_1} \int_{t_1}^{t_2} a(t) dt \right]^{2. 5} (t_2 - t_1)$$

Where:
- $a(t)$ = resultant head acceleration (g)
- $t_1, t_2$ = any two points in time during impact (seconds)
- Maximum HIC over any 36 ms interval

#### 2. Occupant Injury Criteria
| Criterion | Limit | ATD Measurement | Reference |
|-----------|-------|-----------------|-----------|
| Lumbar load | ≤1,500 lbf (6,672 N) | Lumbar load cell | CS-25.562(c)(6) |
| Femur load | ≤2,250 lbf (10,008 N) | Femur load cell | CS-25.562(c)(7) |
| Chest acceleration | ≤60g (3 ms clip) | Chest accelerometer | Industry standard |
| Pelvis acceleration | ≤130g (3 ms clip) | Pelvis accelerometer | Industry standard |
| Neck tension | ≤937 lbf (4,170 N) | Neck load cell | FMVSS 208 |
| Neck compression | ≤899 lbf (4,000 N) | Neck load cell | FMVSS 208 |

#### 3. Interior Hazard Prevention
| Hazard Type | Requirement | Verification | Reference |
|-------------|-------------|--------------|-----------|
| Sharp edges | Radius ≥0.25" (6.  4 mm) on exposed edges | Inspection | CS-25.789 |
| Projections | ≤0.5" (12. 7 mm) in strike envelope | Measurement | CS-25.789 |
| Head strike surfaces | Padded or energy-absorbing | Test | CS-25.562(c)(5) |
| Armrest release | Break-away or stow under load | Test | CS-25.785 |
| Tray table | Controlled failure mode | Test | Interior spec |

#### 4.  Overhead Bin and Stowage Retention
| Component | Retention Load | Failure Mode | Reference |
|-----------|----------------|--------------|-----------|
| Overhead bins (closed) | 9g forward, 6g down | No release, no door opening | CS-25.787 |
| Overhead bins (contents) | Contents retained | No ejection of carry-on items | CS-25.  787 |
| Closets | 9g forward, 6g down | Doors secured | CS-25.787 |
| Galley equipment | 9g forward, 6g down | Secured in place | CS-25.787 |
| Lavatory equipment | 9g forward, 6g down | Secured in place | CS-25.787 |

#### 5. Emergency Exit Operability
| Requirement | Acceptance | Verification | Reference |
|-------------|------------|--------------|-----------|
| Door operation | Operable within 10 seconds | Post-crash functional test | CS-25.783 |
| Door jamming | No structural jamming | Deformation analysis | CS-25.783 |
| Slide deployment | Functional after crash | System test | CS-25.810 |
| Evacuation path | Unobstructed | Inspection | CS-25.813 |

#### 6.  Occupant Survival Space
| Zone | Minimum Clearance | Measurement | Reference |
|------|-------------------|-------------|-----------|
| Torso (radial) | ≥12 inches (305 mm) | From seat reference point | CS-25.785 |
| Head (vertical) | ≥6 inches (152 mm) | Above head position | CS-25.785 |
| Knee/leg (forward) | ≥4 inches (102 mm) | To forward obstruction | Occupant protection |
| Shoulder (lateral) | ≥2 inches (51 mm) | To adjacent structure | Occupant protection |

#### 7. Floor Deflection Control
| Parameter | Limit | Condition | Reference |
|-----------|-------|-----------|-----------|
| Relative floor deflection | <2 inches (51 mm) | Under crash loads | Seat attachment |
| Floor warping angle | <15° | Under emergency loads | CS-25.561(c) |
| Seat track distortion | Attachment maintained | Under seat loads | CS-25.785 |

## BWB-Specific Occupant Protection Considerations

### Non-Conventional Cabin Layout
| Challenge | Impact | Design Response |
|-----------|--------|-----------------|
| Wide cabin cross-section | Multiple seat orientations possible | Zone-specific protection |
| Multi-aisle configuration | Complex head strike geometry | Aisle-specific padding |
| Non-circular fuselage | Variable ceiling height | Overhead bin placement optimization |
| Distributed emergency exits | Variable evacuation distances | Protected egress corridors |
| Potential for lounges/premium spaces | Non-standard seat arrangements | Dedicated protection analysis |

### Occupant Protection Architecture
```
BWB Occupant Protection Architecture
├── Primary Protection Systems
│   ├── Seat and Restraint Systems
│   │   ├── Energy-absorbing seat structure
│   │   ├── Lap belt / 3-point harness
│   │   ├── Seat stroke mechanism
│   │   └── Headrest protection
│   │
│   ├── Floor Structure
│   │   ├── Crashworthy floor beams
│   │   ├── Seat track integrity
│   │   ├── Controlled deformation
│   │   └── Subfloor energy absorption
│   │
│   └── Fuselage Shell
│       ├── Maintained survival space
│       ├── Load path continuity
│       ├── Controlled collapse zones
│       └── No intrusion into cabin
│
├── Secondary Protection Systems
│   ├── Interior Padding
│   │   ├── Overhead bin edges
│   │   ├── Partition surfaces
│   │   ├── Monument edges
│   │   └── Window surrounds
│   │
│   ├── Stowage Retention
│   │   ├── Overhead bin latches
│   │   ├── Closet doors
│   │   ├── Galley equipment
│   │   └── Lavatory fixtures
│   │
│   └── Hazard Elimination
│       ├── Sharp edge radii
│       ├── Projection limits
│       ├── Breakaway features
│       └── Energy-absorbing surfaces
│
├── Zone-Specific Protection
│   ├── Forward Cabin (Zone A)
│   │   ├── Cockpit crew (4/5-point harness)
│   │   ├── Forward passengers
│   │   └── Galley forward position
│   │
│   ├── Center Cabin (Zone B)
│   │   ├── Main passenger area
│   │   ├── Multi-aisle configuration
│   │   ├── Lavatory locations
│   │   └── Mid-cabin galleys
│   │
│   ├── Aft Cabin (Zone C)
│   │   ├── Rear passengers
│   │   ├── Attendant stations
│   │   └── Aft galley/lavatory
│   │
│   └── Premium Zones (if applicable)
│       ├── Lie-flat seats
│       ├── Suites/pods
│       └── Lounge areas
│
└── Hydrogen-Specific Protection
    ├── Cabin/H2 separation
    │   ├── Structural barrier
    │   ├── Fire-resistant separation
    │   └── Pressure equalization
    │
    ├── Post-crash H2 management
    │   ├── Automatic isolation
    │   ├── Controlled venting
    │   └── Fire suppression
    │
    └── Evacuation from H2 hazard
        ├── Hazard zone marking
        ├── Evacuation direction guidance
        └── Protected egress routes
```

### Head Strike Envelope Analysis
| Seat Position | Forward Strike Zone | Lateral Strike Zone | Overhead Strike Zone |
|---------------|---------------------|---------------------|----------------------|
| Forward-facing window | Seat back ahead, window frame | Armrest, window surround | Overhead bin, PSU |
| Forward-facing center | Seat back ahead | Adjacent seat, armrest | Overhead bin, PSU |
| Forward-facing aisle | Seat back ahead, galley/lavatory | Adjacent seat, aisle monuments | Overhead bin, ceiling |
| Aft-facing (if any) | Partition, galley | Adjacent seat, monuments | Overhead bin |
| Side-facing (if any) | Adjacent structure | Forward/aft structure | Overhead structure |

### Padding and Energy Absorption Requirements
| Surface | Padding Requirement | Energy Absorption | Reference |
|---------|---------------------|-------------------|-----------|
| Seat back upper | 2" (50 mm) minimum | HIC reduction | SAE AS8049 |
| Partition surfaces | 3" (75 mm) if in strike envelope | HIC <1,000 | CS-25.562 |
| Overhead bin edges | 1" (25 mm) radius or padded | HIC reduction | Interior spec |
| Monument corners | 2" (50 mm) radius or padded | Injury prevention | Interior spec |
| Window surrounds | 1" (25 mm) radius or padded | Laceration prevention | Interior spec |

## Occupant Categories and Protection Requirements

### By Occupant Type
| Occupant Category | Restraint Type | Special Requirements | Reference |
|-------------------|----------------|---------------------|-----------|
| Flight crew | 4/5-point harness | Shoulder harness, inertia reel | CS-25.785 |
| Cabin crew | Shoulder harness | Energy-absorbing seat | CS-25.785 |
| Passengers (standard) | Lap belt | Energy-absorbing seat | CS-25.785 |
| Passengers (business) | Lap belt | Lie-flat protection | CS-25.785 |
| Infants | Supplemental restraint | Approved child seat | CS-25.785 |
| Mobility impaired | Standard + assistance | Accessible seating | Accessibility |

### By Seat Orientation
| Orientation | Primary Restraint | Secondary Protection | Special Considerations |
|-------------|-------------------|---------------------|------------------------|
| Forward-facing | Lap belt + seat stroke | Seat back ahead | Standard approach |
| Aft-facing | Lap belt + seat back | No forward strike | Improved protection |
| Side-facing | Lap belt + shoulder | Lateral restraint | Complex load path |
| Lie-flat | Lap belt + inflatable | Bed mode protection | Sleep position |

## Verification Method

| Method | Description | Deliverable |
|--------|-------------|-------------|
| **Test** | Crash test dummy instrumentation, sled testing | [TR-53-047](../../53-00-07_V_AND_V/Test_Reports/TR-53-047_Occupant_Protection_Test.  md) |
| **Analysis** | Occupant injury modeling, FE human body models | [AR-53-047](../../53-00-06_Engineering/Crashworthiness/AR-53-047_Occupant_Injury_Analysis.md) |
| **Inspection** | Interior compatibility assessment | [IR-53-047](../../53-00-07_V_AND_V/Inspection_Reports/IR-53-047_Interior_Compatibility. md) |

### Test Program Structure
```
Occupant Protection Test Program (V&V-53-047/048/049)
├── Dynamic Sled Tests (CS-25.562)
│   ├── Test 1 (vertical)
│   │   ├── 35 fps, 14g pulse
│   │   ├── Representative floor section
│   │   ├── ATD (50th percentile male)
│   │   └── Injury criteria measurements
│   │
│   ├── Test 2 (longitudinal)
│   │   ├── 44 fps, 26g pulse
│   │   ├── Representative cabin section
│   │   ├── ATD (50th percentile male)
│   │   └── Injury criteria measurements
│   │
│   └── Additional configurations
│       ├── Business class seats
│       ├── Attendant seats
│       ├── Side-facing seats (if applicable)
│       └── Lie-flat positions (if applicable)
│
├── Head Strike Tests
│   ├── Free motion headform (FMH)
│   ├── Seat back impact
│   ├── Partition impact
│   ├── Monument impact
│   └── Overhead bin impact
│
├── Stowage Retention Tests
│   ├── Overhead bin retention (9g, 6g)
│   ├── Bin door latch strength
│   ├── Content retention
│   └── Closet door retention
│
├── Component Tests
│   ├── Seat attachment strength
│   ├── Restraint system strength
│   ├── Armrest breakaway
│   └── Tray table failure mode
│
├── Interior Hazard Assessment
│   ├── Sharp edge survey
│   ├── Projection measurement
│   ├── Padding thickness verification
│   └── Breakaway force measurement
│
└── Post-Crash Exit Tests
    ├── Door operation after deformation
    ├── Slide deployment
    ├── Evacuation path clearance
    └── Emergency lighting function
```

### Test Instrumentation
| Measurement | Sensor Type | Location | Reference |
|-------------|-------------|----------|-----------|
| Head acceleration | Tri-axial accelerometer | ATD head CG | CS-25.562 |
| Chest acceleration | Tri-axial accelerometer | ATD chest | CS-25.562 |
| Pelvis acceleration | Tri-axial accelerometer | ATD pelvis | CS-25.562 |
| Lumbar load | Load cell | ATD lumbar spine | CS-25.562(c)(6) |
| Femur load | Load cell | ATD femur (bilateral) | CS-25.562(c)(7) |
| Neck loads | 6-axis load cell | ATD neck | FMVSS 208 |
| Belt loads | Load cell | Lap belt, shoulder belt | Restraint design |
| Floor deflection | String pots, LVDT | Floor-to-seat track | Seat attachment |
| High-speed video | Cameras | Multiple angles | Kinematics |

## Traceability

### Parent Requirements
| Requirement | Title | Source |
|-------------|-------|--------|
| [CS-25.562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Emergency Landing Dynamic Conditions | EASA CS-25 |
| [CS-25. 785](https://www.easa. europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Seats, Berths, Safety Belts, and Harnesses | EASA CS-25 |
| [CS-25.787](https://www.easa.  europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Stowage Compartments | EASA CS-25 |
| [CS-25.789](https://www.easa. europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Retention of Items of Mass | EASA CS-25 |
| [FAR 25.562](https://www.  ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) | Emergency Landing Dynamic Conditions | FAA FAR Part 25 |

### Related Requirements
| Requirement ID | Title | Relationship |
|----------------|-------|--------------|
| [53-00-03-04-001](./53-00-03-04-001_Emergency_Landing_Loads.md) | Emergency Landing Loads | Structural basis |
| [53-00-03-04-003](./53-00-03-04-003_Energy_Absorption_Structures.md) | Energy Absorption Structures | Energy management |
| [53-00-03-04-004](./53-00-03-04-004_Post_Crash_Egress. md) | Post-Crash Egress | Evacuation capability |
| [53-00-03-05-001](../05_Fire_Smoke_Toxicity/53-00-03-05-001_Fire_Resistance. md) | Fire Resistance | Post-crash fire |
| [25-00-03-04-001](../../../../ATA_25-EQUIPMENT_FURNISHINGS/25-00-03_Requirements/04_Crashworthiness/25-00-03-04-001_Seat_Crashworthiness.  md) | Seat Crashworthiness | Seat requirements |

### Child Requirements
| Requirement ID | Title | Component |
|----------------|-------|-----------|
| [53-00-03-04-002-A](./53-00-03-04-002-A_Head_Strike_Protection.md) | Head Strike Protection | Interior surfaces |
| [53-00-03-04-002-B](./53-00-03-04-002-B_Stowage_Retention.  md) | Stowage Retention | Overhead bins, closets |
| [53-00-03-04-002-C](./53-00-03-04-002-C_Floor_Deflection_Control.md) | Floor Deflection Control | Floor structure |
| [53-00-03-04-002-D](./53-00-03-04-002-D_Interior_Hazard_Prevention.md) | Interior Hazard Prevention | All interior |

### Interface Requirements
| Interface | Document | Content |
|-----------|----------|---------|
| Seats | [ICD-53-25-002](../../53-00-05_Interfaces/Furnishings/ICD-53-25-002_Seat_Attachment_Interface.md) | Seat attachment loads |
| Interior | [ICD-53-25-004](../../53-00-05_Interfaces/Furnishings/ICD-53-25-004_Interior_Interface.md) | Monument interface |
| Floor | [53-20-03](../../../53-20_Subsystems/53-20-03_Cabin_Floor_and_Supports/README.md) | Floor structure |
| Doors | [53-20-02](../../../53-20_Subsystems/53-20-02_Door_Surround_Structure/README.md) | Exit operability |

### Verification Activities
| Activity ID | Title | Type | Status | Document Link |
|-------------|-------|------|--------|---------------|
| [V&V-53-047](../../53-00-07_V_AND_V/V&V-53-047_Occupant_Injury_Analysis.md) | Occupant Injury Analysis | Analysis + Test | Planned | `../../53-00-07_V_AND_V/` |
| [V&V-53-048](../../53-00-07_V_AND_V/V&V-53-048_Interior_Compatibility_Testing.md) | Interior Compatibility Testing | Test + Inspection | Planned | `../../53-00-07_V_AND_V/` |
| [V&V-53-049](../../53-00-07_V_AND_V/V&V-53-049_Emergency_Exit_Functionality.md) | Emergency Exit Functionality After Crash | Test | Planned | `../../53-00-07_V_AND_V/` |

## Assumptions and Constraints

### Assumptions
| Parameter | Value | Basis |
|-----------|-------|-------|
| Restraint system (crew) | 4/5-point harness | CS-25.785 |
| Restraint system (passengers) | Lap belt minimum | CS-25.785 |
| ATD specification | 50th percentile male (Hybrid III) | FAA standard |
| Seat pitch (economy) | 28-34 inches | Typical configuration |
| Seat pitch (business) | 40-60 inches | Premium configuration |

### Constraints

#### Structural Constraints
| Constraint | Limit | Rationale |
|------------|-------|-----------|
| Floor warping | ≤15° | Seat attachment integrity |
| Cabin intrusion | ≤6 inches | Survival space |
| Aisle obstruction | None | Evacuation |
| Exit path blockage | None | Evacuation |

#### Interior Constraints
| Constraint | Requirement | Rationale |
|------------|-------------|-----------|
| Flammability | Per CS-25.853 | Fire safety |
| Heat release | Per CS-25.853 | Fire safety |
| Smoke density | Per CS-25.853 | Evacuation visibility |
| Toxicity | Per CS-25.853 | Occupant safety |

#### Material Constraints
| Material Application | Requirement | Reference |
|---------------------|-------------|-----------|
| Seat cushions | Fire-blocking layer | CS-25.853 |
| Interior panels | Self-extinguishing | CS-25.853 |
| Padding materials | Low heat release | CS-25.853 |
| Structural composites | Fire-resistant | CS-25.853 |

## Safety Impact
**Design Assurance Level (DAL)**: A (Catastrophic)

Failure to provide adequate occupant protection could result in:
- **Occupant injury/fatality**: Excessive acceleration loads, structural intrusion
- **Increased injury severity**: Inadequate restraint, head strike hazards
- **Evacuation impairment**: Injured occupants blocking egress
- **Secondary injuries**: Loose objects, sharp edges, projections

This requirement is **safety-critical** and requires the highest level of design assurance and verification rigor.

### Safety Assessment References
| Document | Title | Path |
|----------|-------|------|
| [53-00-02-001](../../53-00-02_Safety/53-00-02-001_Fuselage_Safety_Concept.md) | Fuselage Safety Concept | `../../53-00-02_Safety/` |
| [53-00-02-004](../../53-00-02_Safety/53-00-02-004_Crashworthiness_Philosophy.md) | Crashworthiness Philosophy | `../../53-00-02_Safety/` |

## Compliance Matrix

| CS-25 Paragraph | Requirement | Verification | Status | Evidence Document |
|-----------------|-------------|--------------|--------|-------------------|
| CS-25.562(a) | Dynamic conditions | Test | Planned | [CR-53-047](../../53-00-10_Certification/CR-53-047_Occupant_Protection_Compliance.md) |
| CS-25.562(c) | Injury criteria | Test | Planned | CR-53-047 |
| CS-25.785 | Seats and restraints | Test | Planned | [CR-53-048](../../53-00-10_Certification/CR-53-048_Seat_Compliance.md) |
| CS-25.787 | Stowage compartments | Test | Planned | [CR-53-049](../../53-00-10_Certification/CR-53-049_Stowage_Compliance.md) |
| CS-25.789 | Retention of mass items | Test | Planned | CR-53-049 |
| CS-25.853 | Interior flammability | Test | Planned | [CR-53-050](../../53-00-10_Certification/CR-53-050_Flammability_Compliance.md) |

## Priority
**CRITICAL**

## Status
**DRAFT**

## Owner
Crashworthiness Team / Cabin Design

## Reviewers
| Role | Name | Status | Date |
|------|------|--------|------|
| Lead Reviewer | Crashworthiness Lead | Pending | — |
| Interiors Reviewer | Cabin Design Lead | Pending | — |
| Safety Reviewer | Safety Engineering | Pending | — |
| Certification Reviewer | Certification Engineer | Pending | — |
| Human Factors Reviewer | Human Factors Engineer | Pending | — |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1. 0 | 2025-11-22 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial draft |
| 1.  1 | 2025-11-28 | AI (GitHub Copilot) / Amedeo Pelliccia | Added hyperlinks, BWB architecture, injury criteria, test program |

## Last Updated
2025-11-28

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Human Approver | **Amedeo Pelliccia** (Pending Signature) |
| Approval Date | _2025-12-05_ (Target) |
| Repository | [`AMPEL360-BWB-H2-Hy-E`](https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E) |
| File Path | `OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/04_Crashworthiness/` |
| Last AI Update | 2025-11-28 |

---

## Related Documentation Index

### 53-00_GENERAL Structure

| Folder | Document | Title | Path |
|--------|----------|-------|------|
| [53-00-02_Safety](../../53-00-02_Safety/) | [53-00-02-001](../../53-00-02_Safety/53-00-02-001_Fuselage_Safety_Concept.md) | Safety Concept | `../../53-00-02_Safety/` |
| [53-00-02_Safety](../../53-00-02_Safety/) | [53-00-02-004](../../53-00-02_Safety/53-00-02-004_Crashworthiness_Philosophy.md) | Crashworthiness Philosophy | `../../53-00-02_Safety/` |
| [53-00-05_Interfaces](../../53-00-05_Interfaces/) | [ICD-53-25-002](../../53-00-05_Interfaces/Furnishings/ICD-53-25-002_Seat_Attachment_Interface. md) | Seat Attachment | `../../53-00-05_Interfaces/` |
| [53-00-05_Interfaces](../../53-00-05_Interfaces/) | [ICD-53-25-004](../../53-00-05_Interfaces/Furnishings/ICD-53-25-004_Interior_Interface.md) | Interior Interface | `../../53-00-05_Interfaces/` |
| [53-00-06_Engineering](../../53-00-06_Engineering/) | [AR-53-047](../../53-00-06_Engineering/Crashworthiness/AR-53-047_Occupant_Injury_Analysis.md) | Occupant Injury Analysis | `../../53-00-06_Engineering/Crashworthiness/` |
| [53-00-07_V_AND_V](../../53-00-07_V_AND_V/) | [V&V-53-047](../../53-00-07_V_AND_V/V&V-53-047_Occupant_Injury_Analysis.md) | Injury Analysis | `../../53-00-07_V_AND_V/` |
| [53-00-10_Certification](../../53-00-10_Certification/) | [CR-53-047](../../53-00-10_Certification/CR-53-047_Occupant_Protection_Compliance. md) | Compliance Report | `../../53-00-10_Certification/` |

### 53-00-03_Requirements (Sibling Documents)

| Category | Document | Title | Path |
|----------|----------|-------|------|
| [04_Crashworthiness](.  /) | [53-00-03-04-001](./53-00-03-04-001_Emergency_Landing_Loads.md) | Emergency Landing Loads | `./` |
| [04_Crashworthiness](./) | **[53-00-03-04-002](./53-00-03-04-002_Occupant_Protection.  md)** | **Occupant Protection** | `./` ← THIS FILE |
| [04_Crashworthiness](. /) | [53-00-03-04-003](./53-00-03-04-003_Energy_Absorption_Structures.md) | Energy Absorption Structures | `./` |
| [04_Crashworthiness](./) | [53-00-03-04-004](./53-00-03-04-004_Post_Crash_Egress.md) | Post-Crash Egress | `./` |
| [05_Fire_Smoke_Toxicity](../05_Fire_Smoke_Toxicity/) | [53-00-03-05-001](../05_Fire_Smoke_Toxicity/53-00-03-05-001_Fire_Resistance.  md) | Fire Resistance | `../05_Fire_Smoke_Toxicity/` |

### 53-20_Subsystems References

| Folder | Document | Title | Path |
|--------|----------|-------|------|
| [53-20-02_Door_Surround_Structure](../../../53-20_Subsystems/53-20-02_Door_Surround_Structure/) | [README](../../../53-20_Subsystems/53-20-02_Door_Surround_Structure/README.md) | Door Surround | `../../../53-20_Subsystems/53-20-02_Door_Surround_Structure/` |
| [53-20-03_Cabin_Floor_and_Supports](../../../53-20_Subsystems/53-20-03_Cabin_Floor_and_Supports/) | [README](../../../53-20_Subsystems/53-20-03_Cabin_Floor_and_Supports/README.md) | Cabin Floor | `../../../53-20_Subsystems/53-20-03_Cabin_Floor_and_Supports/` |

---

## Notes for Reviewers

1. **BWB-Specific Considerations**: Added non-conventional cabin layout protection architecture
2. **Injury Criteria**: Comprehensive table with all CS-25.  562(c) criteria plus industry standards
3. **Head Strike Envelope**: Position-specific analysis for BWB multi-aisle configuration
4. **Occupant Categories**: Protection requirements by occupant type and seat orientation
5. **Interior Hazard Prevention**: Detailed padding and radii requirements
6. **Test Program**: Full hierarchy including dynamic sled, head strike, and component tests
7. **Action Required**:
   - Confirm cabin layout with Interiors team
   - Validate injury criteria limits with Human Factors
   - Coordinate stowage retention tests with Interiors team
   - Review H2-specific protection with Safety Engineering

---

## References

1. [EASA CS-25 Amendment 27](https://www.  easa.europa.  eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Certification Specifications for Large Aeroplanes
2.  [FAA FAR Part 25](https://www. ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) - Airworthiness Standards: Transport Category Airplanes
3.   SAE AS8049 - Performance Standard for Seats in Civil Rotorcraft, Transport Aircraft, and General Aviation Aircraft
4. FAA AC 25.562-1B - Dynamic Evaluation of Seat Restraint Systems & Occupant Protection
5. SAE ARP5765 - Crashworthiness Handbook for Cabin Interiors
6. NHTSA FMVSS 208 - Occupant Crash Protection
7. SAE J211 - Instrumentation for Impact Test
8.  Hybrid III ATD Manual - Anthropomorphic Test Device Specification
