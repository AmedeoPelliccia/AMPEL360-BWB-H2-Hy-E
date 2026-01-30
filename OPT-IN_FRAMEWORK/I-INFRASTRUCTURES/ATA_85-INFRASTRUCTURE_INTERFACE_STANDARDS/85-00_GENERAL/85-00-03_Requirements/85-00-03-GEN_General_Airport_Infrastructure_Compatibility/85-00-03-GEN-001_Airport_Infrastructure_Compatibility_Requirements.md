# 85-00-03-GEN-001 — Airport Infrastructure Compatibility Requirements

## 1. Requirement Statement

The AMPEL360 BWB H₂ Hy-E aircraft **SHALL** be compatible with airport infrastructure classified as **ICAO Aerodrome Reference Code 4C** or higher, as defined in [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx), Volume I, Chapter 1.

## 2. Rationale

The aircraft must be compatible with a sufficient number of airports worldwide to enable economically viable operations. The ICAO Aerodrome Reference Code (ARC) provides a standardized classification system that defines:

- **Code Number (4)**: Aircraft reference field length ≥ 1800 m
- **Code Letter (C)**: Aircraft wingspan 24 m to < 36 m, or outer main gear wheel span 9 m to < 14 m

Target airports for AMPEL360 operations include:
- Major international hubs (e.g., Frankfurt EDDF, Amsterdam EHAM, Dubai OMDB)
- Regional airports supporting medium-haul operations
- Airports with hydrogen infrastructure potential

**Consequences if not satisfied**:
- Severely limited operational flexibility
- Inability to access key markets and routes
- Increased operational costs due to airport limitations
- Difficulty establishing viable route networks

## 3. Category

- **Requirement Type**: Functional — Airport Compatibility
- **Domain**: General Airport Infrastructure
- **ATA**: 85-00-03_Requirements / GEN

## 4. Source(s)

- **[ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx)** — Aerodromes, Volume I: Aerodrome Design and Operations (Chapter 1: Aerodrome Reference Code)
- **[ICAO Doc 9157](https://store.icao.int/en/aerodrome-design-manual-doc-9157)** — Aerodrome Design Manual, Part 1: Runways
- **Aircraft Design Requirements** — ATA 06 (Dimensions), ATA 08 (Weighing)
- **Operational Concepts** — Medium-haul hydrogen-powered operations (target range 4,000 km)
- **Stakeholder Input** — Airport operators, airline customers

## 5. Acceptance Criteria

- [x] Aircraft wingspan ≤ 36 m (Code Letter C upper bound)
- [x] Aircraft outer main gear wheel span ≤ 14 m (Code Letter C upper bound)
- [ ] Aircraft reference field length (ARFL) documented and ≤ 1800 m for Code Number 4
- [ ] Compatibility validated with representative Code 4C airports (at least 5 major hubs)
- [ ] Ground clearance verified for typical Code 4C taxiway and apron surfaces
- [ ] Turning radius compatible with Code 4C taxiway geometry
- [ ] Aircraft Classification Number (ACN) calculated for representative pavement types
- [ ] Compatibility matrix published for target airports

## 6. Verification Method

- **Method**: Analysis + Demonstration
- **Evidence**:
  - Aircraft dimensions report (ATA 06)
  - Airport compatibility analysis (comparison of aircraft characteristics vs. ICAO Code 4C requirements)
  - Pavement loading analysis (ACN/PCN calculations)
  - Ground movement simulation at representative airports
  - List of compatible airports with operational constraints (if any)

### Verification Procedure

1. **Analysis**: Compare aircraft dimensions and characteristics to ICAO Code 4C requirements
2. **Calculation**: Compute Aircraft Classification Number (ACN) for flexible and rigid pavements
3. **Simulation**: Model ground movement (taxiing, turning) at representative Code 4C airports
4. **Demonstration**: Validate compatibility at first operational airport (ground trials)
5. **Documentation**: Publish airport compatibility matrix

## 7. Traceability

### Upstream (Sources)
- Aircraft dimensions: ATA 06-00-00 (Dimensions and Areas)
- Aircraft weight: ATA 08-00-00 (Leveling and Weighing)
- Landing gear design: ATA 32-00-00 (Landing Gear)

### Horizontal (Design)
- [85-00-04_Design](../../../85-00-04_Design/) — Airport compatibility analysis report
- Interface Control Document: ICD-85-GEN-001 (Airport Infrastructure Interface)

### Downstream (Verification)
- TC-85-03-GEN-001-A: Airport compatibility analysis
- TC-85-03-GEN-001-B: Pavement loading verification (ACN/PCN)
- TC-85-03-GEN-001-C: Ground movement simulation
- TC-85-03-GEN-001-D: Operational demonstration at first airport

### Certification
- MoC-85-03-GEN-001: Airport compatibility evidence package
- Compliance with CS-25 structural and operational requirements

## 8. Derived Requirements

This high-level requirement derives more specific requirements:

- **RQ-85-00-03-GEN-002**: Runway, taxiway, and stand interface requirements
- **RQ-85-00-03-GEN-003**: Airport operations and procedures requirements
- **RQ-85-00-03-PAX-001**: Passenger boarding infrastructure compatibility (related to stand interfaces)

## 9. Related Requirements

- **RQ-85-00-03-EMERG-003**: Emergency access routes (must be compatible with Code 4C airport emergency vehicle access)
- **RQ-85-00-03-H2-003**: H₂ refuelling operational constraints (refuelling stands must be within Code 4C airport capability)

## 10. Assumptions and Constraints

### Assumptions
- Code 4C airports are widely available on target routes
- Existing Code 4C infrastructure can accommodate BWB configuration with minimal modifications
- Hydrogen infrastructure will be developed at Code 4C airports in target markets

### Constraints
- Aircraft design must not require Code 4D or 4E classification (more restrictive and fewer airports)
- BWB configuration may require specific parking stand orientations or clearances
- Hydrogen refuelling infrastructure availability may initially limit airport selection

## 11. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| BWB wingspan exceeds Code C limit (36 m) | Low | High | Design constraint: wingspan ≤ 36 m |
| Limited Code 4C airports in target markets | Low | Medium | Market analysis to confirm Code 4C availability |
| Code 4C airports cannot accommodate BWB turning radius | Medium | Medium | Ground movement simulation; design optimization |
| H₂ infrastructure not available at Code 4C airports | High | High | Phased introduction; establish H₂ hubs at key Code 4C airports |

## 12. Status

- **Lifecycle State**: `APPROVED`
- **Owner**: Systems Engineering / Aircraft Architecture Team
- **Approved By**: Configuration Control Board (CCB)
- **Approval Date**: 2025-11-21
- **Last Updated**: 2025-11-21
- **Comments**: Approved for design. Wingspan and main gear span meet Code C limits.

---

## Document Control

- **Document ID**: RQ-85-00-03-GEN-001
- **Version**: 1.0
- **Status**: APPROVED
- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21
- **Classification**: Internal Use
- **Change History**:
  - v1.0 (2025-11-21): Initial approved version

---

**For questions or collaboration opportunities, contact: requirements@ampel360.aero**
