# 85-00-03-GEN-002 — Runway, Taxiway, and Stand Interface Requirements

## 1. Requirement Statement

The AMPEL360 BWB H₂ Hy-E aircraft **SHALL** be compatible with runway, taxiway, and aircraft stand infrastructure that meets the following minimum specifications:

- **Runway Length**: ≥ 2,100 m (at sea level, ISA conditions, maximum takeoff weight)
- **Runway Width**: ≥ 45 m (per [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx) Code 4C requirements)
- **Taxiway Width**: ≥ 23 m (per ICAO Annex 14 Code C requirements)
- **Taxiway Separation**: Aircraft wingtip clearance ≥ 4.5 m from taxiway edge
- **Aircraft Stand Dimensions**: Minimum 60 m × 60 m apron area
- **Pavement Strength**: Pavement Classification Number (PCN) ≥ 50 on flexible pavements, ≥ 60 on rigid pavements

## 2. Rationale

These specifications ensure the aircraft can operate safely at airports with Code 4C infrastructure while accounting for:

- **Runway Length**: Sufficient for takeoff and landing with appropriate safety margins under normal and adverse conditions
- **Runway and Taxiway Width**: Adequate clearance for BWB wingspan and main gear track
- **Taxiway Separation**: Safe wingtip clearance during taxiing, accounting for pilot visibility and control
- **Stand Dimensions**: Space for aircraft parking, ground service equipment, and safety zones
- **Pavement Strength**: Adequate to support aircraft weight without pavement damage

**Consequences if not satisfied**:
- Inability to operate at target airports
- Risk of runway or taxiway overruns
- Wingtip or ground contact during taxiing
- Pavement damage and operational restrictions
- Safety hazards during ground operations

## 3. Category

- **Requirement Type**: Physical — Infrastructure Dimensions and Specifications
- **Domain**: Runway, Taxiway, and Stand Interfaces
- **ATA**: 85-00-03_Requirements / GEN

## 4. Source(s)

- **[ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx)** — Aerodromes, Volume I, Chapters 3 (Runways) and 4 (Taxiways)
- **[ICAO Doc 9157](https://store.icao.int/en/aerodrome-design-manual-doc-9157)** — Aerodrome Design Manual, Parts 1-3
- **[FAA AC 150/5300-13](https://www.faa.gov/airports/resources/advisory_circulars/)** — Airport Design
- **Aircraft Performance Analysis** — Takeoff and landing performance calculations (ATA 05)
- **Structural Design** — Landing gear loads and Aircraft Classification Number (ACN) calculations (ATA 32)
- **Operational Concepts** — Target airports and operational scenarios

## 5. Acceptance Criteria

- [x] Runway length requirement documented (2,100 m minimum)
- [ ] Takeoff and landing performance verified for 2,100 m runway (ISA, sea level, MTOW)
- [ ] Taxiway width and separation verified against aircraft wingspan and main gear track
- [ ] Aircraft turning radius calculated and compared to Code C taxiway geometry
- [ ] Aircraft Classification Number (ACN) calculated for flexible and rigid pavements
- [ ] Stand dimensions validated for ground service equipment access and safety zones
- [ ] Compatibility verified at representative airports (at least 3 different airports)
- [ ] Pavement loading analysis completed and approved by structural engineering

## 6. Verification Method

- **Method**: Analysis + Test + Demonstration
- **Evidence**:
  - Takeoff and landing performance analysis (ATA 05)
  - Aircraft Classification Number (ACN) calculation report (ATA 32)
  - Pavement loading analysis (comparison of ACN vs. typical airport PCN values)
  - Taxiway geometry simulation (turning radius, wingtip clearances)
  - Ground movement demonstration at test airport
  - Stand layout analysis with ground service equipment mockup

### Verification Procedure

1. **Analysis**: 
   - Calculate takeoff and landing distances for various conditions
   - Compute ACN for flexible and rigid pavements using ICAO methodology
   - Analyze taxiway geometry and wingtip clearances
2. **Simulation**: Model aircraft taxiing and turning on Code C taxiways
3. **Test**: Validate pavement loading with representative ground loads
4. **Demonstration**: Conduct ground movement trials at first operational airport

## 7. Traceability

### Upstream (Sources)
- Aircraft dimensions: ATA 06 (wingspan, length, height, main gear track)
- Aircraft weight: ATA 08 (maximum takeoff weight, landing weight)
- Performance: ATA 05 (takeoff and landing performance)
- Landing gear: ATA 32 (gear configuration, loads, ACN)

### Horizontal (Design)
- [85-00-04_Design](../../../85-00-04_Design/) — Runway and taxiway interface analysis
- ICD-85-GEN-002: Runway and Taxiway Interface Control Document

### Downstream (Verification)
- TC-85-03-GEN-002-A: Takeoff and landing performance analysis
- TC-85-03-GEN-002-B: ACN/PCN pavement compatibility analysis
- TC-85-03-GEN-002-C: Taxiway geometry and clearance simulation
- TC-85-03-GEN-002-D: Ground movement demonstration

### Certification
- MoC-85-03-GEN-002: Runway and taxiway compatibility evidence
- CS-25.105 (Takeoff), CS-25.125 (Landing): Performance compliance

## 8. Detailed Requirements Breakdown

### 8.1 Runway Requirements

| Parameter | Requirement | Justification |
|-----------|------------|---------------|
| **Length** | ≥ 2,100 m | Takeoff distance at MTOW + safety margin |
| **Width** | ≥ 45 m | ICAO Code 4C requirement |
| **Shoulder Width** | ≥ 7.5 m each side | ICAO Code C requirement |
| **Surface** | Paved, dry friction coefficient ≥ 0.5 | Safe braking and directional control |
| **Slope** | Longitudinal ≤ 1.5%, transverse ≤ 1.5% | Acceptable for takeoff and landing performance |

### 8.2 Taxiway Requirements

| Parameter | Requirement | Justification |
|-----------|------------|---------------|
| **Width** | ≥ 23 m | ICAO Code C requirement |
| **Shoulder Width** | ≥ 10 m each side | ICAO Code C requirement |
| **Minimum Turning Radius** | ≥ 30 m (centerline radius) | BWB turning geometry |
| **Separation from Objects** | Wingtip clearance ≥ 4.5 m | Safety margin during taxiing |
| **Centerline Markings** | Standard ICAO markings | Pilot visual guidance |

### 8.3 Aircraft Stand Requirements

| Parameter | Requirement | Justification |
|-----------|------------|---------------|
| **Apron Area** | ≥ 60 m × 60 m | Aircraft footprint + ground service equipment |
| **Clearance from Fixed Objects** | ≥ 7.5 m | Safety zone per ICAO Annex 14 |
| **Service Vehicle Access** | 360° access or designated service zones | Ground handling efficiency |
| **Pavement Markings** | Aircraft parking position, nose wheel stop | Precise positioning for boarding bridges |

## 9. Related Requirements

- **RQ-85-00-03-GEN-001**: Airport infrastructure compatibility (parent requirement)
- **RQ-85-00-03-PAX-001**: Passenger boarding infrastructure (boarding bridge compatibility with stand layout)
- **RQ-85-00-03-EMERG-003**: Emergency access routes (emergency vehicle access to stands)

## 10. Assumptions and Constraints

### Assumptions
- Runway and taxiway surfaces are well-maintained and meet ICAO standards
- Typical Code 4C airport PCN values are sufficient for AMPEL360 operations
- Stand layouts can accommodate BWB-specific ground service equipment positioning

### Constraints
- BWB configuration may require larger turning radii than conventional aircraft
- Hydrogen refuelling operations may require additional stand clearances (see RQ-85-00-03-H2-003)
- Some older Code C airports may have marginally narrow taxiways requiring operational procedures

## 11. Operational Considerations

- **Wet Runway Operations**: Performance analysis must account for contaminated runways (wet, slush, snow)
- **High-Altitude Airports**: Runway length requirement increases with altitude and temperature
- **Narrow Taxiways**: Operational procedures (e.g., reduced taxi speed, wing walkers) may be required at minimum-width taxiways
- **Stand Orientation**: BWB may require specific stand orientations for optimal boarding bridge alignment

## 12. Status

- **Lifecycle State**: `FOR_REVIEW`
- **Owner**: Aircraft Performance & Systems Engineering Teams
- **Approved By**: Pending CCB review
- **Approval Date**: TBD
- **Last Updated**: 2025-11-21
- **Comments**: Pending performance analysis completion. ACN calculations in progress.

---

## Document Control

- **Document ID**: RQ-85-00-03-GEN-002
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

**For questions or collaboration opportunities, contact: requirements@ampel360.aero**
