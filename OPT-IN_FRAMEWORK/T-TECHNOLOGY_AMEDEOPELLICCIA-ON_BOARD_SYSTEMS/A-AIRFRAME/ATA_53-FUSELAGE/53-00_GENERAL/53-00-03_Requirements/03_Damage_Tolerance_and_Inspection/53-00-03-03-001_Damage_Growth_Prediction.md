# [53-00-03-02-001](./53-00-03-02-001_Maximum_Differential_Pressure.md): Maximum Differential Pressure

## Requirement ID
**53-00-03-02-001**

## Title
Maximum Differential Pressure

## Category
02_Pressurization_and_Decompression

## Description
The fuselage pressure vessel shall safely contain a maximum differential pressure of **9.3 psi (64.1 kPa)** between cabin interior and exterior ambient pressure, with appropriate structural margins. This requirement covers normal operations at maximum certified altitude.

This requirement ensures compliance with:
- [CS-25.365](https://www. easa.europa. eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (Pressurized Compartment Loads)
- [CS-25. 841](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (Pressurized Cabins)
- [CS-25.843](https://www. easa.europa. eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (Tests for Pressurized Cabins)
- FAR 25.365, FAR 25.841, FAR 25.843

## Rationale
Maximum differential pressure represents the most demanding operational condition for the pressure vessel. The structure must safely contain this pressure to maintain cabin environment and occupant safety at cruise altitude.

For the AMPEL360 BWB hydrogen-hybrid aircraft, pressure containment is particularly critical due to:
- **Blended Wing Body configuration**: Non-cylindrical pressure vessel with complex stress distributions
- **Integrated cabin volume**: Large, wide cabin cross-section requiring reinforced pressure boundaries
- **Hydrogen system proximity**: Pressure vessel interfaces with LH2 tank support structures
- **Extended service life**: 60,000 flight cycles requiring robust fatigue performance under pressure cycling

## Acceptance Criteria

### Summary Table
| # | Parameter | Requirement | Verification |
|---|-----------|-------------|--------------|
| 1 | Maximum operating ΔP | 9.3 psi (64.1 kPa) | Analysis + Test |
| 2 | Proof pressure factor | 1.33 × ΔP = 12.4 psi | Test |
| 3 | Burst pressure factor | ≥ 2.0 × ΔP = 18.6 psi | Test |
| 4 | Permanent deformation at max ΔP | None detectable | Inspection |
| 5 | Pressure uniformity | ±0.1 psi across cabin | Test |
| 6 | Structural margin of safety | MS ≥ 0 at all locations | Analysis |

### Detailed Acceptance Criteria

#### 1. Maximum Operating Differential Pressure
| Condition | Altitude | Cabin Altitude | ΔP |
|-----------|----------|----------------|-----|
| Normal cruise | 43,000 ft | 8,000 ft | 8.6 psi |
| Maximum certified | 43,000 ft | 6,000 ft | 9.3 psi |
| Emergency descent | 25,000 ft | Sea level | 5.5 psi |
| Ground (max relief) | Sea level | -500 ft | 0.5 psi |

#### 2.  Proof Pressure Test Requirements
| Parameter | Requirement | Basis |
|-----------|-------------|-------|
| Proof pressure | 1.33 × 9.3 = 12.4 psi | CS-25.843(b) |
| Hold duration | ≥ 5 minutes | Industry practice |
| Acceptance criteria | No structural failure | CS-25.843(b) |
| Post-test inspection | No permanent deformation > 0.1% | Internal standard |
| Number of cycles | 1 full cycle | Certification requirement |

#### 3. Burst Pressure Requirements
| Parameter | Requirement | Basis |
|-----------|-------------|-------|
| Minimum burst pressure | 2.0 × 9.3 = 18.6 psi | CS-25.365(d) |
| Demonstrated margin | ≥ 2.0 × ΔP | Positive margin at failure |
| Test article | Representative structure | Full-scale or component |
| Failure mode | Controlled, predictable | Safety assessment |

#### 4. Deformation Limits
| Load Level | Deformation Limit | Measurement |
|------------|-------------------|-------------|
| Normal operating (9.3 psi) | Elastic only | Strain gauges |
| Proof (12.4 psi) | ≤ 0.1% permanent | Dimensional survey |
| Post-proof | Return to original | Dimensional survey |

#### 5.  Pressure Distribution
| Zone | Uniformity Requirement | Measurement Points |
|------|------------------------|-------------------|
| Forward cabin | ±0.1 psi of nominal | 4 locations |
| Center cabin | ±0.1 psi of nominal | 8 locations |
| Aft cabin | ±0.1 psi of nominal | 4 locations |
| Cargo compartments | ±0. 1 psi of nominal | 4 locations |

#### 6. Structural Margin Requirements
| Location | MS Requirement | Critical Load Case |
|----------|----------------|-------------------|
| Pressure bulkheads | MS ≥ 0.10 | ΔP + thermal |
| Fuselage skin panels | MS ≥ 0 | ΔP + flight loads |
| Door cutouts | MS ≥ 0. 05 | ΔP + flight loads |
| Window cutouts | MS ≥ 0. 05 | ΔP + flight loads |
| Frame splices | MS ≥ 0 | ΔP + fatigue |
| Longitudinal joints | MS ≥ 0 | ΔP + fatigue |

## BWB-Specific Pressure Vessel Considerations

### Non-Cylindrical Geometry Challenges
| Challenge | Impact | Design Response |
|-----------|--------|-----------------|
| Non-circular cross-section | Bending stresses in skin | Optimized frame spacing |
| Variable curvature | Stress concentrations | Gradual transitions |
| Wide cabin span | High hoop loads | Internal pressure walls |
| Blended transition | Complex stress field | Detailed FEA optimization |

### Pressure Vessel Architecture
```
BWB Pressure Vessel Configuration
├── Forward Pressure Bulkhead
│   ├── Flat bulkhead (reinforced)
│   └── Nose gear bay interface
│
├── Cabin Pressure Shell
│   ├── Upper skin panels (low curvature)
│   ├── Side skin panels (variable curvature)
│   ├── Lower skin panels (cargo floor interface)
│   ├── Internal pressure walls (cabin width constraint)
│   └── Frame/stringer grid (orthogrid or isogrid)
│
├── Pressure Boundaries
│   ├── Wing-body junction seals
│   ├── Door frame seals (passenger, cargo, service)
│   ├── Window seals
│   ├── System penetration seals
│   └── H2 tank compartment interface
│
└── Aft Pressure Bulkhead
    ├── Dome or flat configuration
    ├── Empennage attachment interface
    └── APU compartment separation
```

### Stress Distribution Analysis Requirements
| Analysis Type | Purpose | Software/Method |
|---------------|---------|-----------------|
| Global FEA | Overall pressure response | NASTRAN/ABAQUS |
| Detail FEA | Cutout stress concentrations | Local submodeling |
| Fatigue analysis | Pressure cycle damage | Miner's rule + S-N data |
| Damage tolerance | Crack growth under pressure | AFGROW/NASGRO |

## Combined Loading Requirements

### Pressure + Flight Loads
| Load Case | Components | Criticality |
|-----------|------------|-------------|
| ΔP + 2. 5g maneuver | Pressure + bending + shear | Upper fuselage |
| ΔP + -1.0g maneuver | Pressure + reverse bending | Lower fuselage |
| ΔP + gust | Pressure + dynamic loads | Frame attachments |
| ΔP + ground | Pressure + landing loads | Keel beam, MLG interface |

### Pressure + Thermal Loads
| Condition | Temperature Range | Combined Effect |
|-----------|-------------------|-----------------|
| High altitude cruise | -55°C OAT, +20°C cabin | Thermal stress + ΔP |
| Ground hot day | +50°C ambient | Reduced ΔP margin |
| Rapid decompression | Transient thermal | Thermal shock + ΔP relief |

### Pressure + H2 System Thermal
| Interface Zone | Thermal Condition | Pressure Interaction |
|----------------|-------------------|---------------------|
| Tank support frames | -253°C to +40°C gradient | Thermal stress + ΔP |
| Fuselage-tank interface | Cryogenic exposure | Material property changes |
| Vent line routing | Cold gas exposure | Local thermal stress |

## Verification Method

| Method | Description | Deliverable |
|--------|-------------|-------------|
| **Test** | Full-scale pressure vessel proof test and burst test | Test Report TR-53-006 |
| **Analysis** | FEA of pressure loads on fuselage structure | Analysis Report AR-53-006 |
| **Inspection** | Post-test inspection for permanent deformation | Inspection Report IR-53-006 |

### Test Program Structure
```
Pressure Vessel Test Program (V&V-53-014/015/016)
├── Development Tests
│   ├── Material characterization (pressure fatigue)
│   ├── Coupon pressure cycling
│   └── Element joint tests
│
├── Component Tests
│   ├── Pressure bulkhead proof/burst
│   ├── Door frame section test
│   ├── Window frame section test
│   └── Splice joint fatigue under pressure
│
├── Full-Scale Tests
│   ├── Static pressure proof test (12.4 psi)
│   ├── Pressure cycling (2 DSG: 60,000 cycles)
│   ├── Combined pressure + flight loads
│   ├── Ultimate pressure test
│   └── Burst test (destructive)
│
└── Special Tests
    ├── Rapid decompression test
    ├── Thermal + pressure combined
    └── H2 interface thermal cycling + pressure
```

### Test Instrumentation
| Measurement | Sensor Type | Locations |
|-------------|-------------|-----------|
| Strain | Strain gauge rosettes | 500+ locations |
| Pressure | Pressure transducers | 20 cabin locations |
| Displacement | LVDTs, photogrammetry | Bulkheads, frames |
| Temperature | Thermocouples | Skin, frames, H2 interface |
| Acoustic emission | AE sensors | Damage-prone areas |

## Traceability

### Parent Requirements
| Requirement | Title | Source |
|-------------|-------|--------|
| [CS-25.365](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Pressurized Compartment Loads | EASA CS-25 |
| [CS-25.841](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Pressurized Cabins | EASA CS-25 |
| [CS-25. 843](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Tests for Pressurized Cabins | EASA CS-25 |
| FAR 25.365, 25.841, 25.843 | Equivalent FAA requirements | FAA FAR Part 25 |

### Related Requirements
| Requirement ID | Title | Relationship |
|----------------|-------|--------------|
| [53-00-03-02-002](./53-00-03-02-002_Pressure_Cycle_Endurance.md) | Pressure Cycle Endurance | Fatigue life under ΔP |
| [53-00-03-02-003](./53-00-03-02-003_Rapid_Decompression. md) | Rapid Decompression | Emergency condition |
| [53-00-03-01-001](../01_Structural_Integrity/53-00-03-01-001_Ultimate_Load_Capability. md) | Ultimate Load Capability | Combined ΔP + flight loads |
| [53-00-03-01-002](../01_Structural_Integrity/53-00-03-01-002_Limit_Load_Elastic_Behavior.md) | Limit Load Elastic Behavior | Elastic response at max ΔP |
| 21-00-03-01-001 | Cabin Pressure Control | System providing ΔP |
| 52-00-03-02-001 | Door Pressure Sealing | Boundary integrity |
| 56-00-03-02-001 | Window Pressure Integrity | Boundary integrity |

### Child Requirements
| Requirement ID | Title | Component |
|----------------|-------|-----------|
| 53-10-03-02-001 | Forward Bulkhead Pressure Capability | Forward Fuselage |
| 53-20-03-02-001 | Center Fuselage Pressure Capability | Center Fuselage |
| 53-30-03-02-001 | Aft Bulkhead Pressure Capability | Aft Fuselage |
| 53-20-03-02-010 | Internal Pressure Wall Requirements | BWB Cabin Structure |
| 53-00-03-02-020 | Pressure Boundary Sealing | All Seals |

### Interface Requirements
| Interface | Document | Content |
|-----------|----------|---------|
| Pressurization System | ICD-53-21-001 | Pressure control interface |
| Doors | ICD-53-52-001 | Door frame loads, sealing |
| Windows | ICD-53-56-001 | Window frame loads, sealing |
| H2 Tank Compartment | ICD-53-73-002 | Pressure boundary at tank interface |

### Verification Activities
| Activity ID | Title | Type | Status |
|-------------|-------|------|--------|
| V&V-53-014 | Pressure Vessel Proof Test | Test | Planned |
| V&V-53-015 | Burst Pressure Test | Test | Planned |
| V&V-53-016 | Pressure Distribution Test | Test | Planned |
| V&V-53-017 | Pressure + Flight Loads Test | Test | Planned |
| V&V-53-018 | Pressure Fatigue Test | Test | Planned |
| V&V-53-019 | Pressure FEA Correlation | Analysis | Planned |

## Assumptions and Constraints

### Assumptions
- Maximum operating altitude: 43,000 ft (13,106 m)
- Cabin altitude maintained at ≤ 8,000 ft (2,438 m) per CS-25.841
- Standard atmosphere model for pressure calculations
- Pressurization system maintains target ΔP ±0.1 psi
- Relief valve opens at 9.5 psi (safety margin)
- Negative pressure relief at -0.5 psi

### Constraints

#### Operational Altitude Envelope
| Parameter | Value | Basis |
|-----------|-------|-------|
| Maximum certified altitude | 43,000 ft | Performance requirement |
| Maximum cabin altitude | 8,000 ft | CS-25.841 |
| Resulting maximum ΔP | 9.3 psi | Pressure schedule |
| Emergency descent altitude | 10,000 ft | O2 system requirement |

#### Material Constraints
| Material | Pressure Capability | Limitation |
|----------|--------------------| ----------|
| CFRP skin | Excellent fatigue | Impact damage sensitivity |
| Al-Li frames | Good fatigue, light | Corrosion protection needed |
| Ti fittings | High strength | Cost, machining |
| Sealants | Pressure sealing | Service life, temperature |

#### Design Constraints
| Constraint | Limit | Rationale |
|------------|-------|-----------|
| Skin thickness (min) | Per damage tolerance | BVID resistance |
| Frame spacing (max) | 533 mm (21 in) typical | Pressure pillowing |
| Stringer spacing | 150-200 mm | Skin stability |
| Door cutout reinforcement | Local doubler | Stress concentration |
| Window spacing | Per passenger requirements | Cabin layout |

#### Combined Load Factors
| Load Case | ΔP Factor | Flight Load Factor |
|-----------|-----------|-------------------|
| Normal operations | 1.0 | 1. 0 |
| Limit | 1.0 | 1. 0 (limit maneuver/gust) |
| Ultimate | 1.0 | 1. 5 (ultimate) |
| Proof | 1. 33 | N/A |
| Burst | 2.0 | N/A |

## Safety Impact
**Design Assurance Level (DAL)**: A (Catastrophic)

Failure to contain maximum differential pressure could result in:
- **Rapid decompression**: Loss of cabin pressure at altitude
- **Structural failure**: Pressure vessel rupture
- **Occupant injury/fatality**: Hypoxia, debris, structural collapse
- **Loss of aircraft**: Catastrophic structural failure

This requirement is **safety-critical** and requires the highest level of design assurance, verification rigor, and continued airworthiness attention.

## Compliance Matrix

| CS-25 Paragraph | Requirement | Verification | Status |
|-----------------|-------------|--------------|--------|
| CS-25.365(a) | External pressure loads | Analysis + Test | Planned |
| CS-25.365(d) | Pressure vessel burst | Test | Planned |
| CS-25.365(e) | Combined loads | Analysis + Test | Planned |
| CS-25.841(a) | Cabin pressure altitude | Analysis | Planned |
| CS-25.843(a) | Strength test | Test (proof) | Planned |
| CS-25.843(b) | Proof factor 1.33 | Test | Planned |

## Priority
**CRITICAL**

## Status
**UNDER REVIEW**

## Owner
Structures Engineering Team / Pressurization Systems

## Reviewers
| Role | Name | Status | Date |
|------|------|--------|------|
| Lead Reviewer | Structures Engineering Lead | Pending | — |
| Pressurization Reviewer | ECS Systems Lead | Pending | — |
| Certification Reviewer | Certification Engineer | Pending | — |
| Safety Reviewer | Safety Engineering | Pending | — |
| Test Reviewer | Structural Test Lead | Pending | — |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-22 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial draft |
| 1.1 | 2025-11-27 | AI (GitHub Copilot) / Amedeo Pelliccia | Enhanced with BWB considerations, combined loads, test program, H2 interface considerations |

## Last Updated
2025-11-27

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **UNDER REVIEW** |
| Human Approver | **[Pending Assignment - Structures Engineering Lead]** |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| File Path | `OPT-IN_FRAMEWORK/T-TECHNOLOGY/A-AIRFRAME/ATA_53_FUSELAGE/53-00-00_GENERAL/53-00-03_Requirements/02_Pressurization_and_Decompression/` |
| Last AI Update | 2025-11-27 |

---

## Notes for Reviewers

1. **BWB-Specific Considerations**: Added section on non-cylindrical pressure vessel challenges unique to blended wing body configuration
2. **Pressure Vessel Architecture**: Visual hierarchy showing pressure boundary components
3. **Combined Loading**: Expanded to include pressure + flight + thermal + H2 interface loads
4. **Test Program Structure**: Comprehensive test hierarchy from development to full-scale
5.  **Internal Pressure Walls**: BWB may require internal pressure walls to constrain cabin width—requirement 53-20-03-02-010 added
6. **H2 Interface**: Added thermal considerations for pressure vessel adjacent to cryogenic tanks
7. **Safety Impact**: DAL A classification with specific failure consequences
8. **Action Required**:
   - Assign human approver from Structures Engineering leadership
   - Confirm maximum operating altitude with Performance Engineering
   - Coordinate with ECS on pressure schedule and relief valve settings
   - Validate test program scope with Structural Test organization
   - Review H2 tank interface thermal requirements with Propulsion

---

## References

1. EASA CS-25 Amendment 27 - Certification Specifications for Large Aeroplanes
2. FAA FAR Part 25 - Airworthiness Standards: Transport Category Airplanes
3. FAA AC 25.365-1 - Pressurized Cabin Loads (advisory)
4. CMH-17 Volume 3 - Composite Materials Handbook (pressure vessel design)
5.  MMPDS - Metallic Materials Properties Development and Standardization
6. NASA/TM-2004-213484 - Blended Wing Body Structural Design Considerations
7. AIAA 2018-1050 - BWB Pressurized Cabin Design Challenges
8.  Niu, M. C. Y. - Airframe Structural Design (pressure cabin chapter)

---
