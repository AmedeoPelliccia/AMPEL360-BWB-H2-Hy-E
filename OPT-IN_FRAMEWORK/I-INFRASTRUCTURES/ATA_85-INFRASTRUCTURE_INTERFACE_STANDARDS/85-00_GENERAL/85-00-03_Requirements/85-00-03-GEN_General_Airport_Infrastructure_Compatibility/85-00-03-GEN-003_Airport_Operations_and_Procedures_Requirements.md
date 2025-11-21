# 85-00-03-GEN-003 — Airport Operations and Procedures Requirements

## 1. Requirement Statement

The AMPEL360 BWB H₂ Hy-E aircraft **SHALL** be compatible with standard airport operational procedures including:

- **Ground Movement**: Standard taxiing procedures without requiring specialized towing or ground handling
- **Pushback and Towing**: Compatible with standard pushback tractors and towing equipment rated for Code C aircraft
- **Engine Start**: Capable of autonomous engine start (fuel cell system activation) without external ground power dependency
- **De-icing/Anti-icing**: Compatible with standard de-icing fluid application equipment and procedures
- **Turnaround Time**: Target turnaround time of **45 minutes** for typical short/medium-haul operations

## 2. Rationale

Operational compatibility with standard airport procedures is essential for:

- **Economic Viability**: Minimize need for specialized ground equipment and procedures
- **Airport Acceptance**: Facilitate adoption by airport operators and ground service providers
- **Operational Efficiency**: Achieve competitive turnaround times comparable to conventional aircraft
- **Crew Training**: Leverage existing training and procedures where possible

**BWB-Specific Considerations**:
- Unique fuselage shape may affect ground handling and service vehicle access
- Hydrogen propulsion introduces novel operational procedures (see RQ-85-00-03-H2-003)
- Pilot visibility and control during ground operations may differ from conventional aircraft

**Consequences if not satisfied**:
- Higher operating costs due to specialized equipment and procedures
- Resistance from airport operators and ground handlers
- Operational delays and reduced aircraft utilization
- Complexity in crew training and procedures

## 3. Category

- **Requirement Type**: Operational — Airport Procedures and Ground Operations
- **Domain**: Airport Operations and Ground Handling
- **ATA**: 85-00-03_Requirements / GEN

## 4. Source(s)

- **[ICAO Doc 9157](https://store.icao.int/en/aerodrome-design-manual-doc-9157)** — Aerodrome Design Manual, Part 4: Visual Aids
- **[IATA Ground Operations Manual (IGOM)](https://www.iata.org/en/publications/manuals/ground-operations-manual/)** — Industry standard ground handling procedures
- **[ICAO Doc 9640](https://www.icao.int/safety/airnavigation/OPS/Pages/manual-aircraft-ground-de-icing.aspx)** — Manual of Aircraft Ground De-icing/Anti-icing Operations
- **Operational Concepts** — AMPEL360 turnaround time targets and efficiency goals
- **Stakeholder Input** — Ground service providers, airline operators, airport authorities

## 5. Acceptance Criteria

- [ ] Ground movement procedures documented (taxiing, holding, parking)
- [ ] Towing and pushback interfaces compatible with standard Code C tractors
- [ ] Towing points and attachment procedures defined and validated
- [ ] Engine start (fuel cell activation) procedures documented and tested
- [ ] De-icing/anti-icing procedures compatible with standard fluid application equipment
- [ ] Turnaround time analysis completed (target: 45 minutes)
- [ ] Ground handling procedures validated with representative equipment
- [ ] Pilot visibility and control during ground operations verified (simulation + flight test)
- [ ] Operational procedures manual (OPM) section for ground operations approved

## 6. Verification Method

- **Method**: Analysis + Demonstration + Test
- **Evidence**:
  - Ground operations procedures manual
  - Towing and pushback equipment compatibility analysis
  - Turnaround time simulation and analysis
  - Ground handling demonstration with representative equipment
  - De-icing procedure validation (ground test)
  - Pilot visibility assessment during taxi operations (simulator + flight test)

### Verification Procedure

1. **Analysis**: 
   - Define ground movement procedures (normal and non-normal)
   - Analyze towing and pushback equipment compatibility
   - Model turnaround time for typical operations
2. **Demonstration**: 
   - Validate towing and pushback with representative equipment
   - Conduct turnaround simulation with ground service providers
3. **Test**: 
   - Validate fuel cell startup procedures
   - Test de-icing fluid application and runoff
   - Verify pilot visibility during taxiing (simulator and flight test)

## 7. Traceability

### Upstream (Sources)
- Aircraft dimensions: ATA 06 (towing point locations, ground clearances)
- Ground handling: ATA 09 (Towing and Taxiing)
- Propulsion: ATA 28 (H₂ fuel cell startup procedures)
- Environmental protection: ATA 30 (Ice and Rain Protection)

### Horizontal (Design)
- [85-00-04_Design](../../../85-00-04_Design/) — Ground operations interface design
- [85-10_Operations](../../../../85-10_Operations/) — Operational procedures and manuals
- ICD-85-GEN-003: Ground Operations Interface Control Document

### Downstream (Verification)
- TC-85-03-GEN-003-A: Ground movement procedures validation
- TC-85-03-GEN-003-B: Towing and pushback equipment compatibility test
- TC-85-03-GEN-003-C: Turnaround time simulation
- TC-85-03-GEN-003-D: De-icing procedure validation
- TC-85-03-GEN-003-E: Pilot visibility assessment during taxi operations

### Certification
- MoC-85-03-GEN-003: Airport operations and procedures compliance evidence
- CS-25.783 (Doors and exits — Emergency evacuation): Ground egress procedures

## 8. Detailed Requirements Breakdown

### 8.1 Ground Movement

| Aspect | Requirement | Justification |
|--------|------------|---------------|
| **Taxiing** | Aircraft shall taxi under its own power on all Code C taxiways | Standard operational capability |
| **Turning Radius** | Minimum turning radius ≤ 30 m (nose gear steering) | Compatible with Code C taxiway geometry |
| **Taxi Speed** | Maximum taxi speed: 30 kt (straight), 10 kt (turns) | Safety and controllability |
| **Visibility** | Pilot visibility meets CS-25.773 requirements | Safe ground operations |
| **Braking** | Effective braking on taxiways without specialized procedures | Standard ground control |

### 8.2 Pushback and Towing

| Aspect | Requirement | Justification |
|--------|------------|---------------|
| **Towing Points** | Nose gear towing lug compatible with standard Code C tractors | Standard equipment compatibility |
| **Towing Breakaway** | Breakaway load ≥ tractor capacity (safety feature) | Prevent damage during abnormal towing |
| **Pushback Angle** | 180° pushback capability (turn and straight) | Operational flexibility |
| **Towing Speed** | Maximum towing speed: 5 kt | Safety during towing operations |
| **Towbar** | Compatible with IATA standard towbars for Code C aircraft | No specialized equipment required |

### 8.3 Engine Start (Fuel Cell System)

| Aspect | Requirement | Justification |
|--------|------------|---------------|
| **Autonomous Start** | Fuel cell system shall start using aircraft battery power | No external GPU dependency |
| **Startup Time** | Fuel cell system ready for taxi ≤ 5 minutes | Operational efficiency |
| **Ground Power (Optional)** | Aircraft shall accept external ground power for startup (optional) | Flexibility in case of battery depletion |
| **Safety Interlocks** | H₂ fuel cell startup interlocked with safety systems | Prevent unsafe startup conditions |

### 8.4 De-icing and Anti-icing

| Aspect | Requirement | Justification |
|--------|------------|---------------|
| **Fluid Compatibility** | Aircraft surfaces compatible with Type I, II, III, IV fluids per [AMS 1428](https://www.sae.org/standards/content/ams1428/) | Standard de-icing fluids |
| **Application Method** | Standard de-icing truck spray equipment compatible | No specialized de-icing equipment |
| **Fluid Runoff** | Fluid runoff directed away from H₂ vents and electrical connections | Safety and contamination prevention |
| **Holdover Time** | De-icing holdover times per SAE ARP 4737 applicable | Standard operational procedures |

### 8.5 Turnaround Operations

Target turnaround time breakdown (45 minutes total):

| Activity | Duration | Concurrent Activities |
|----------|----------|----------------------|
| **Arrival and Passenger Disembarkation** | 10 min | — |
| **Cabin Cleaning and Preparation** | 15 min | Cargo unloading/loading, H₂ refuelling, water/waste servicing |
| **H₂ Refuelling** | 15 min | Concurrent with cleaning, cargo, catering |
| **Passenger Boarding** | 15 min | Final cabin checks |
| **Pre-Departure Checks and Pushback** | 5 min | — |

**Critical Path**: Passenger disembarkation → Cabin preparation → Passenger boarding → Departure

## 9. Related Requirements

- **RQ-85-00-03-GEN-001**: Airport infrastructure compatibility (parent requirement)
- **RQ-85-00-03-GEN-002**: Runway, taxiway, and stand interfaces (physical compatibility)
- **RQ-85-00-03-H2-003**: H₂ refuelling operational constraints (turnaround time impact)
- **RQ-85-00-03-PAX-002**: Turnaround and ground service interface requirements (detailed turnaround procedures)

## 10. Assumptions and Constraints

### Assumptions
- Ground service providers have standard Code C ground handling equipment
- H₂ refuelling infrastructure available at target airports (see RQ-85-00-03-H2-001)
- Airport operational procedures can accommodate 45-minute turnaround time
- De-icing facilities and procedures available at cold-weather airports

### Constraints
- BWB configuration may limit access to certain aircraft areas during turnaround
- H₂ refuelling safety zones may restrict concurrent ground service activities
- Pilot visibility during taxi may require additional crew training or procedures
- Novel propulsion system may require specialized ground crew training

## 11. Operational Considerations

- **BWB Taxi Visibility**: Pilots may have limited ground visibility due to BWB configuration; taxi cameras or procedures may be required
- **H₂ Safety Zones**: During H₂ refuelling, ground service equipment must maintain safe distances (see RQ-85-00-03-H2-003)
- **Turnaround Efficiency**: Concurrent activities (refuelling, catering, cleaning) are critical to achieving 45-minute target
- **Cold Weather Operations**: De-icing procedures must account for H₂ system components and BWB surfaces
- **Remote Stands**: If boarding bridges not available, mobile stairs must accommodate BWB door locations

## 12. Status

- **Lifecycle State**: `FOR_REVIEW`
- **Owner**: Flight Operations & Ground Operations Teams
- **Approved By**: Pending CCB review
- **Approval Date**: TBD
- **Last Updated**: 2025-11-21
- **Comments**: Pending ground operations procedure definition. Turnaround time analysis in progress.

---

## Document Control

- **Document ID**: RQ-85-00-03-GEN-003
- **Version**: 1.0
- **Status**: FOR_REVIEW — Pending CCB approval
- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21
- **Classification**: Internal Use
- **Change History**:
  - v1.0 (2025-11-21): Initial draft for review

---

**For questions or collaboration opportunities, contact: operations@ampel360.aero**
