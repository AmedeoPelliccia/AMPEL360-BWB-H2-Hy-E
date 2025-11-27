# [53-00-03-01-005](./53-00-03-01-005_Compatibility_with_SHM_Assumptions.md): Compatibility with SHM Assumptions

## Requirement ID
**53-00-03-01-005**

## Title
Compatibility with SHM Assumptions

## Category
01_Structural_Integrity

## Description
The fuselage structural design shall be compatible with Structural Health Monitoring (SHM) system assumptions, including sensor placement, damage detection capabilities, and structural response characteristics. The structure shall provide adequate signal propagation and sensor accessibility for effective health monitoring.

This requirement ensures that the structural design enables compliance with:
- [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (Damage Tolerance and Fatigue Evaluation) through enhanced inspection capability
- [CS-25.1529](https://www. easa.europa. eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) (Instructions for Continued Airworthiness) through condition-based maintenance
- FAR 25.571 and FAR 25. 1529

## Rationale
SHM systems rely on specific structural characteristics for effective operation. The structural design must support SHM functionality to enable:
- **Condition-based maintenance**: Reduce scheduled inspections through continuous monitoring
- **Enhanced safety**: Real-time damage detection capabilities
- **Operational efficiency**: Reduced aircraft downtime and maintenance costs
- **Extended inspection intervals**: Credit SHM for extended threshold and repeat intervals

For the AMPEL360 BWB hydrogen-hybrid aircraft, SHM compatibility is particularly important due to:
- **Blended Wing Body configuration**: Large, integrated structure with limited visual access
- **Hydrogen system integration**: Critical monitoring of tank-structure interfaces and cryogenic zones
- **Advanced composites**: Complex damage modes (delamination, disbond) requiring specialized detection
- **Novel certification approach**: SHM may be required to demonstrate damage tolerance compliance

## Acceptance Criteria

### Summary Table
| # | Parameter | Requirement | Verification |
|---|-----------|-------------|--------------|
| 1 | Critical area sensor coverage | ≥ 95% | Analysis + Test |
| 2 | Ultrasonic attenuation | ≤ 20 dB over monitoring distance | Test |
| 3 | Signal interference at joints | Characterized and mitigated | Test |
| 4 | Sensor mounting provisions | Defined in design | Design Review |
| 5 | FEA integration | Signal paths validated | Analysis |
| 6 | Documentation | SHM requirements included | Design Review |

### Detailed Acceptance Criteria

#### 1. Sensor Coverage of Critical Areas
| Zone Classification | Coverage Requirement | Damage Types |
|--------------------|---------------------|--------------|
| Principal Structural Elements (PSE) | ≥ 98% | Fatigue cracks, corrosion |
| Damage-Tolerant Areas | ≥ 95% | Cracks, delamination |
| Fatigue-Critical Details | 100% | Fatigue cracks |
| Composite Primary Structure | ≥ 95% | Delamination, disbond, impact |
| H2 Tank Support Structure | 100% | Cracks, hydrogen effects |

#### 2. Signal Propagation Requirements
| Material Type | Maximum Attenuation | Monitoring Distance | Frequency Range |
|--------------|---------------------|---------------------|-----------------|
| Aluminum alloy | ≤ 15 dB | Up to 1. 0 m | 100-500 kHz |
| CFRP laminate | ≤ 20 dB | Up to 0.75 m | 50-300 kHz |
| Titanium alloy | ≤ 12 dB | Up to 1.2 m | 100-400 kHz |
| Sandwich structure | ≤ 25 dB | Up to 0.5 m | 25-150 kHz |
| Hybrid joints | ≤ 30 dB | Up to 0.3 m | Site-specific |

#### 3. Structural Joint Design for SHM
| Joint Type | Signal Interference Limit | Design Provision |
|------------|---------------------------|------------------|
| Bolted metallic | ≤ 6 dB transmission loss | Bypass sensors across joint |
| Bolted composite | ≤ 10 dB transmission loss | Sensor pairs on each side |
| Bonded joints | ≤ 3 dB transmission loss | Continuous monitoring path |
| Hybrid interfaces | Characterized per location | Dedicated sensor network |

#### 4. Sensor Mounting Provisions
| Requirement | Specification |
|-------------|---------------|
| Surface preparation | Per sensor OEM specification |
| Mounting location flatness | ≤ 0. 5 mm over sensor footprint |
| Edge distance | ≥ 25 mm from edges, fasteners, doublers |
| Access for installation | Minimum 100 mm clearance radius |
| Access for replacement | Removable panels or designed access |
| Wire routing provisions | Conduits, brackets, penetrations designed in |

#### 5. FEA Model Integration
- Sensor locations included in structural FE model
- Signal propagation paths validated through wave propagation analysis
- Sensor mass and stiffness effects included in dynamic model
- Thermal effects on sensor performance analyzed
- Damage scenarios correlated with sensor response predictions

#### 6.  Documentation Requirements
| Document | SHM Content Required |
|----------|---------------------|
| Structural Design Report | Sensor locations, signal paths, access provisions |
| Stress Report | Sensor installation effects on allowables |
| Fatigue & DT Report | SHM credit for inspection intervals |
| Manufacturing Plan | Sensor installation procedures |
| ICA / AMM | Sensor calibration, maintenance, replacement |

## SHM Technology Requirements

### Sensor Technologies
| Technology | Application | Damage Detection Capability |
|------------|-------------|----------------------------|
| Piezoelectric (PZT) | Guided wave generation/reception | Cracks, delamination, disbond, corrosion |
| Fiber Bragg Grating (FBG) | Strain monitoring | Load monitoring, impact detection, crack growth |
| Acoustic Emission (AE) | Passive damage detection | Active damage growth, fiber breakage |
| Comparative Vacuum Monitoring (CVM) | Surface crack detection | Fatigue cracks at known hot spots |
| Eddy Current Array (ECA) | Metallic crack detection | Surface and near-surface cracks |

### Sensor Network Architecture
```
SHM Sensor Network Architecture
├── Zone 1: Forward Fuselage
│   ├── Pressure bulkhead monitoring
│   ├── Nose gear attachment
│   └── Cockpit window frames
├── Zone 2: Center Fuselage
│   ├── Wing-body junction (high priority)
│   ├── Cabin floor structure
│   ├── Door frame surrounds
│   └── Passenger window frames
├── Zone 3: Aft Fuselage
│   ├── Empennage attachment
│   ├── APU mount structure
│   └── Aft pressure bulkhead
├── Zone 4: H2 System Integration
│   ├── Tank support structure (critical)
│   ├── Cryogenic zone interfaces
│   └── Vent line attachments
└── Data Acquisition System
    ├── Zone controllers
    ├── Central processor
    └── Data storage and transmission
```

### Detection Requirements by Damage Type
| Damage Type | Minimum Detectable Size | Probability of Detection (POD) |
|-------------|------------------------|-------------------------------|
| Fatigue crack (metallic) | 2.5 mm (0.1 in) | ≥ 90% at 95% confidence |
| Delamination (composite) | 25 mm (1. 0 in) diameter | ≥ 90% at 95% confidence |
| Disbond (bonded joint) | 25 mm (1. 0 in) diameter | ≥ 90% at 95% confidence |
| Impact damage (BVID) | 25 J threshold | ≥ 90% at 95% confidence |
| Corrosion (metallic) | 10% thickness loss | ≥ 90% at 95% confidence |

## Structural Design Provisions for SHM

### Material Selection Considerations
| Material Property | SHM Implication | Design Action |
|-------------------|-----------------|---------------|
| Acoustic impedance | Affects wave transmission | Match sensor-structure impedance |
| Damping characteristics | Affects signal range | Adjust sensor spacing accordingly |
| Anisotropy (composites) | Directional wave propagation | Model wave velocity variation |
| Temperature sensitivity | Affects signal velocity | Include temperature compensation |
| Moisture absorption | Affects wave velocity | Account for conditioned properties |

### Structural Configuration Guidelines
| Feature | SHM-Compatible Design | Avoid |
|---------|----------------------|-------|
| Stiffener layout | Regular spacing for predictable wave paths | Irregular patterns causing mode conversion |
| Fastener patterns | Consistent pitch/edge distance | Clustered fasteners blocking propagation |
| Thickness transitions | Gradual tapers | Abrupt changes causing reflections |
| Cutout reinforcements | Symmetric doublers | Complex overlapping reinforcements |
| Access panels | Designed sensor access locations | Sensors behind permanent structure |

### Installation Zone Classification
| Zone Type | Definition | Installation Window |
|-----------|------------|---------------------|
| Primary installation | Sensors installed during manufacturing | Before final assembly |
| Secondary installation | Sensors installed at final assembly | Before first flight |
| Retrofit-ready | Provisions for future sensors | Any maintenance interval |

## Signal Propagation Analysis

### Wave Propagation Modeling Requirements
| Analysis Type | Purpose | Software/Method |
|--------------|---------|-----------------|
| Lamb wave dispersion | Characterize wave modes | Semi-analytical FEM (SAFE) |
| Sensor response simulation | Predict damage detection | Time-domain FEA |
| Coverage optimization | Optimize sensor placement | Raytracing algorithms |
| Temperature compensation | Baseline adjustment | Empirical correlation |

### Validation Testing
| Test Level | Objective | Articles |
|------------|-----------|----------|
| Coupon | Wave velocity characterization | Flat panels |
| Element | Joint transmission loss | Stiffened panels, joints |
| Component | Sensor network functionality | Section barrels |
| Full-scale | System validation | Fatigue test article |

## Verification Method

| Method | Description | Deliverable |
|--------|-------------|-------------|
| **Analysis** | Wave propagation modeling, sensor coverage analysis | Analysis Report AR-53-005 |
| **Test** | Sensor functionality testing on structural test articles | Test Report TR-53-005 |
| **Inspection** | Design review of sensor integration provisions | Design Review Report DRR-53-005 |

### Verification Activities Detail
| Activity | Objective | Pass Criteria |
|----------|-----------|---------------|
| Coverage analysis | Verify ≥95% critical area coverage | Documented sensor placement plan |
| Wave propagation test | Measure actual attenuation | ≤ specified limits per material |
| Joint transmission test | Characterize signal loss at joints | ≤ specified limits per joint type |
| Detectability demonstration | Validate POD at detectable damage size | ≥ 90/95 POD/confidence |
| Environmental effects test | Validate performance over temperature range | Stable detection across envelope |
| EMI/EMC test | Verify no interference with aircraft systems | Compliance with DO-160G |

## Traceability

### Parent Requirements
| Requirement | Title | Source |
|-------------|-------|--------|
| [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Damage Tolerance and Fatigue Evaluation | EASA CS-25 |
| [CS-25.1529](https://www. easa.europa. eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Instructions for Continued Airworthiness | EASA CS-25 |
| FAR 25.571 | Damage Tolerance and Fatigue Evaluation | FAA FAR Part 25 |
| AMPEL360-SHM-STR-001 | SHM Strategy Document | Internal |

### Related Requirements
| Requirement ID | Title | Relationship |
|----------------|-------|--------------|
| [53-00-03-01-001](./53-00-03-01-001_Ultimate_Load_Capability.md) | Ultimate Load Capability | Structure performance basis |
| [53-00-03-01-004](./53-00-03-01-004_Environmental_Durability. md) | Environmental Durability | Sensor durability requirements |
| [53-00-03-03-001](../03_Damage_Tolerance_and_Inspection/53-00-03-03-001_Damage_Growth_Prediction.md) | Damage Growth Prediction | SHM interval basis |
| [53-00-03-03-004](../03_Damage_Tolerance_and_Inspection/53-00-03-03-004_SHM_for_Damage_Detection.md) | SHM for Damage Detection | System-level requirements |
| [53-00-03-07-001](../07_SHM_and_Monitoring/53-00-03-07-001_Sensor_Network_Coverage.md) | Sensor Network Coverage | Detailed sensor requirements |
| [53-00-03-07-002](../07_SHM_and_Monitoring/53-00-03-07-002_Data_Acquisition_Requirements.md) | Data Acquisition Requirements | Data system interface |

### Child Requirements
| Requirement ID | Title | Component | Status |
|----------------|-------|-----------|--------|
| [57-00-03-07-001](../../../../ATA_57-WINGS/57-00_GENERAL/57-00-03_Requirements/07_SHM_and_Monitoring/57-00-03-07-001_Wing_SHM_Compatibility.md) | Wing SHM Compatibility | Wing/BWB Junction | Draft |
| [24-00-03-SHM-001](../../../../../E2-ENERGY/ATA_24-ELECTRICAL_POWER/24-00_GENERAL/24-00-03_Requirements/SHM_Interface/24-00-03-SHM-001_SHM_Power_Requirements.md) | SHM Power Requirements | Electrical Power | Draft |
| [45-00-03-SHM-001](../../../../../I-INFORMATION_INTELLIGENCE_INTERFACES/ATA_45-ONBOARD_MAINTENANCE_SYSTEMS/45-00_GENERAL/45-00-03_Requirements/SHM_Integration/45-00-03-SHM-001_SHM_CMS_Integration.md) | SHM CMS Integration | Central Maintenance | Draft |
| [28-00-03-SHM-001](../../../../../C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/28-00_GENERAL/28-00-03_Requirements/SHM_H2_Interface/28-00-03-SHM-001_H2_Tank_Structure_Monitoring.md) | H2 Tank Structure Monitoring | Cryogenic Fuel System | Draft |
| [54-00-03-07-001](../../../../ATA_54-NACELLES_PYLONS/54-00_GENERAL/54-00-03_Requirements/07_SHM_and_Monitoring/54-00-03-07-001_Nacelle_Structure_SHM.md) | Nacelle Structure SHM | Nacelles/Pylons | Draft |
| [55-00-03-07-001](../../../../ATA_55-STABILIZERS/55-00_GENERAL/55-00-03_Requirements/07_SHM_and_Monitoring/55-00-03-07-001_Empennage_SHM_Compatibility.md) | Empennage SHM Compatibility | Stabilizers | Draft |
| [52-00-03-07-001](../../../../ATA_52-DOORS/52-00_GENERAL/52-00-03_Requirements/07_SHM_and_Monitoring/52-00-03-07-001_Door_Surround_SHM.md) | Door Surround SHM | Door Structures | Draft |

### Interface Requirements
| Interface | Document | Content |
|-----------|----------|---------|
| Master ICD Register | [ICD-SHM-000](../../../../../L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ICD-SHM-000_Master_Interface_Register.md) | All SHM interfaces index |
| Electrical System | [ICD-53-24-SHM-001](../../../../../L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ICD-53-24-SHM-001_Electrical_Power_Interface.md) | Power requirements, wire routing |
| Wing-Body Junction | [ICD-53-57-SHM-001](../../../../../L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ICD-53-57-SHM-001_Wing_Body_Junction_Interface.md) | Sensor network at BWB junction |
| Maintenance System | [ICD-53-45-SHM-001](../../../../../L2-LINKS/INTERFACE_CONTROL/SHM_INTERFACES/ICD-53-45-SHM-001_CMS_Maintenance_Interface.md) | CMS data interface |

### Cross-ATA Traceability
For the complete traceability matrix of SHM requirements across all ATA chapters, see:
- [SHM Cross-ATA Traceability Matrix](../ASSETS/matrices/SHM_Cross_ATA_Traceability_Matrix.csv)

### Verification Activities
| Activity ID | Title | Type | Status |
|-------------|-------|------|--------|
| V&V-53-011 | SHM Integration Verification | Analysis + Test | Planned |
| [V&V-53-011](../../../../../../P-PROGRAM/VERIFICATION_VALIDATION/SHM/V&V-53-011_SHM_Integration_Verification.md) | SHM Integration Verification | Analysis + Test | Planned |
| V&V-53-012 | Sensor Placement Validation | Analysis | Planned |
| V&V-53-013 | Signal Propagation Testing | Test | Planned |
| [V&V-53-014](../../../../../../P-PROGRAM/VERIFICATION_VALIDATION/SHM/V&V-53-014_POD_Demonstration.md) | POD Demonstration | Test | Planned |
| V&V-53-015 | Environmental Performance Test | Test | Planned |

For the complete V&V program documentation, see the [SHM V&V Program](../../../../../../P-PROGRAM/VERIFICATION_VALIDATION/SHM/README.md).

## Assumptions and Constraints

### Assumptions
- SHM technology based on piezoelectric sensors and guided wave propagation as primary method
- Fiber Bragg Grating sensors for strain-based monitoring as secondary method
- Sensor system electronics meet DO-160G environmental qualification
- Sensor installation does not require structure modification that reduces allowables
- Baseline data acquisition performed prior to aircraft entry into service
- Sensor system designed for 30-year service life with replaceable sensor heads

### Constraints

#### Structural Impact Limits
| Parameter | Limit | Justification |
|-----------|-------|---------------|
| Local stress concentration (sensor mount) | ≤ 5% increase | Fatigue impact acceptable |
| Stiffness knockdown (sensor area) | ≤ 2% local reduction | Negligible global effect |
| Added mass (sensor system) | ≤ 50 kg total | Weight budget allocation |
| Power consumption | ≤ 500 W continuous | Electrical system capacity |

#### Operational Constraints
| Constraint | Requirement | Rationale |
|------------|-------------|-----------|
| Temperature range | -55°C to +85°C operational | Standard flight envelope |
| Cryogenic zone sensors | -253°C to +40°C | H2 tank adjacent areas |
| Vibration tolerance | Per DO-160G Cat S | Engine, aerodynamic excitation |
| EMI/EMC compliance | DO-160G Section 21 | No interference with avionics |

#### Retrofit Considerations
| Requirement | Specification |
|-------------|---------------|
| Sensor replacement access | Without major disassembly |
| Wiring upgrade provisions | Spare conduit capacity |
| Processor upgrade | Modular, replaceable LRU |
| Technology insertion | Architecture supports new sensor types |

## SHM Certification Considerations

### Regulatory Framework
| Document | Applicability | Status |
|----------|---------------|--------|
| EASA CM-S-012 | SHM for structural damage assessment | Issue 1 (2018) |
| FAA AC 25.571-1D | Damage tolerance and fatigue evaluation | Current |
| SAE ARP6461 | SHM guidance | In development |
| MIL-HDBK-1823A | POD demonstration methods | Reference |

### Certification Credit Approach
| Application | Potential Credit | Substantiation Required |
|-------------|------------------|------------------------|
| Threshold extension | Extended initial inspection | POD demonstration, reliability data |
| Interval extension | Longer repeat inspection intervals | Continuous monitoring reliability |
| Method substitution | SHM replaces NDI | Equivalent POD demonstration |
| Damage tolerance | Alternative means of compliance | SHM as scheduled inspection |

## Safety Impact
**Design Assurance Level (DAL)**: C (Major)

The SHM compatibility requirement itself is not safety-critical, but supports safety-critical damage tolerance compliance:
- **Primary impact**: Enables enhanced damage detection capability
- **Secondary impact**: Supports condition-based maintenance optimization
- **Failure mode**: SHM system failure reverts to conventional inspection program

Note: The SHM system itself may have higher DAL requirements per [53-00-03-07-001](../07_SHM_and_Monitoring/53-00-03-07-001_Sensor_Network_Coverage.md). 

## Compliance Matrix

| Requirement Aspect | Verification Method | Status |
|-------------------|---------------------|--------|
| Sensor coverage (≥95%) | Analysis + Test | Planned |
| Signal attenuation (≤20 dB) | Test | Planned |
| Joint interference mitigation | Test | Planned |
| Sensor mounting provisions | Design Review | Planned |
| FEA integration | Analysis | Planned |
| Documentation completeness | Design Review | Planned |

## Priority
**MEDIUM**

## Status
**UNDER REVIEW**

## Owner
SHM Systems Team / Structures Engineering

## Reviewers
| Role | Name | Status | Date |
|------|------|--------|------|
| Lead Reviewer | SHM Systems Lead | Pending | — |
| Structures Reviewer | Structures Engineering Lead | Pending | — |
| Certification Reviewer | Certification Engineer | Pending | — |
| Avionics Reviewer | Avionics Integration Lead | Pending | — |
| Maintenance Reviewer | MRB Representative | Pending | — |

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-11-22 | AI (GitHub Copilot) / Amedeo Pelliccia | Initial draft |
| 1.1 | 2025-11-27 | AI (GitHub Copilot) / Amedeo Pelliccia | Enhanced with sensor technology matrix, detection requirements, signal propagation analysis, certification considerations, structural design provisions |

## Last Updated
2025-11-27

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **UNDER REVIEW** |
| Human Approver | **[Pending Assignment - SHM Systems Lead]** |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| File Path | `OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_53-FUSELAGE/53-00_GENERAL/53-00-03_Requirements/01_Structural_Integrity/` |
| Last AI Update | 2025-11-27 |

---

## Notes for Reviewers

1. **Sensor Technology Matrix**: Added comprehensive table of SHM technologies with applications and capabilities
2. **Detection Requirements**: Added quantified POD requirements per damage type aligned with MIL-HDBK-1823A
3. **Signal Propagation**: Added detailed attenuation limits per material type and frequency ranges
4. **Sensor Network Architecture**: Visual hierarchy showing zone-based sensor deployment
5. **Structural Design Provisions**: New section on material selection and configuration guidelines for SHM compatibility
6. **Certification Considerations**: Added regulatory framework and credit approach for SHM
7. **H2-Specific**: Included cryogenic zone sensor requirements for hydrogen tank interfaces
8. **Action Required**:
   - Assign human approver from SHM Systems leadership
   - Coordinate with Structures Engineering on sensor mounting load effects
   - Validate POD requirements with certification authority
   - Confirm sensor technology selection with SHM supplier

---

## References

1. EASA CS-25 Amendment 27 - Certification Specifications for Large Aeroplanes
2. FAA FAR Part 25 - Airworthiness Standards: Transport Category Airplanes
3.  EASA CM-S-012 - Structural Health Monitoring for Structural Damage Assessment
4. FAA AC 25. 571-1D - Damage Tolerance and Fatigue Evaluation of Structure
5. MIL-HDBK-1823A - Nondestructive Evaluation System Reliability Assessment
6. SAE ARP6461 - Guidelines for Implementation of Structural Health Monitoring on Fixed Wing Aircraft
7.  RTCA DO-160G - Environmental Conditions and Test Procedures for Airborne Equipment
8. CMH-17 Volume 3 - Polymer Matrix Composites: Materials Usage, Design, and Analysis
9. NASA/CR-2011-217085 - Structural Health Monitoring: Current Status and Perspectives
10.  Giurgiutiu, V. (2014) - Structural Health Monitoring with Piezoelectric Wafer Active Sensors

---
