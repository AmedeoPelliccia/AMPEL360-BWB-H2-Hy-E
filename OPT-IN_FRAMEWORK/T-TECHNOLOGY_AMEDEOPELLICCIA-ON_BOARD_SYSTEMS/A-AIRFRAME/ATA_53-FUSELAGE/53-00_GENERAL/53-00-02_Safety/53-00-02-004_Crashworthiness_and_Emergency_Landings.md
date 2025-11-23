# 53-00-02-004 — Crashworthiness and Emergency Landings

**ATA Chapter**: 53 — Fuselage  
**Folder**: 53-00-02_Safety  
**Status**: DRAFT  
**Owner**: Airframe & Structures Domain (ATA 53)

---

## 1. Purpose

Define the **crashworthiness and emergency landing design philosophy** for the AMPEL360 BWB fuselage structure, establishing:

- Structural requirements for survivable crash scenarios.  
- Load paths and energy absorption mechanisms.  
- Occupant protection and evacuation considerations.  
- Integration with landing gear ([ATA 32](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/M-MECHANICS/ATA_32-LANDING_GEAR/)) and emergency systems ([ATA 25](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C1-COCKPIT_CABIN_CARGO/ATA_25-EQUIPMENT_FURNISHINGS/)/[ATA 26](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E1-ENVIRONMENT/ATA_26-FIRE_PROTECTION/)).

This document focuses on **structural crashworthiness**; occupant restraint systems and evacuation are covered in [ATA 25](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C1-COCKPIT_CABIN_CARGO/ATA_25-EQUIPMENT_FURNISHINGS/).

---

## 2. Regulatory Basis

Crashworthiness requirements for fuselage structure are derived from:

- **[CS-25.561](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)**: General emergency landing conditions.  
- **[CS-25.562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)**: Emergency landing dynamic conditions.  
- **[CS-25.563](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)**: Structural ditching provisions.  
- **[CS-25.721](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)**: General (landing gear design loads interface with fuselage).  
- **[FAR 25.561-563](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-C)**: Federal equivalents to CS-25.  
- **[AC 20-146B](https://www.faa.gov/regulations_policies/advisory_circulars)**: Methodology for Dynamic Seat Certification by Analysis.  
- **[AC 25-17A](https://www.faa.gov/regulations_policies/advisory_circulars)**: Transport Airplane Cabin Interiors Crashworthiness Handbook.

---

## 3. Crashworthiness Design Philosophy

### 3.1 Design Objectives

The fuselage structure shall:

1. **Maintain survivable volume**: Prevent intrusion into occupant space during defined crash scenarios.  
2. **Control deceleration**: Provide energy absorption to limit occupant loads to survivable levels (≤ 16g vertical, ≤ 20g horizontal per [CS-25.562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)).  
3. **Enable evacuation**: Preserve structural integrity of emergency exits and evacuation routes post-crash.  
4. **Prevent fuel spillage**: Maintain integrity of fuel system attachments and minimize breach of fuel tanks.  
5. **Resist post-crash fire**: See [53-00-02-003_Fire_Smoke_Toxicity_Considerations.md](./53-00-02-003_Fire_Smoke_Toxicity_Considerations.md) for FST aspects.

### 3.2 Design Principles

- **Progressive collapse**: Structural elements fail in controlled sequence, absorbing energy without sudden overload.  
- **Stiff upper structure**: Floor beams and seat attachment structure remain relatively rigid to support occupant loads.  
- **Deformable lower structure**: Subfloor and landing gear attachment areas designed to crush and absorb impact energy.  
- **Redundant load paths**: Multiple paths for load transfer reduce risk of catastrophic failure.

---

## 4. Emergency Landing Load Cases

### 4.1 Regulatory Load Cases

Per [CS-25.561](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) and [CS-25.562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes), the structure shall withstand:

| Load Case | Vertical (g) | Longitudinal (g) | Lateral (g) | Notes |
|:--|:--:|:--:|:--:|:--|
| Upward | +3.0 | — | — | Inertia relief case |
| Downward | -6.0 | +9.0 | — | Forward crash landing |
| Downward | -6.0 | -1.5 | ±3.0 | Lateral crash landing |
| Ditching | Variable | Variable | Variable | Water impact, buoyancy |

Loads are applied to **all masses** (structure, systems, occupants, cargo) simultaneously.

### 4.2 Dynamic Conditions

Per [CS-25.562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes), dynamic testing or analysis shall demonstrate:

- Floor deceleration not exceeding **16g vertical, 20g horizontal** at seat attachment points.  
- Seat and restraint system retention under these decelerations.  
- No hazardous deformation of structure that could injure occupants.

Dynamic analysis methods are detailed in [53-00-06_Engineering](../53-00-06_Engineering/).

---

## 5. Energy Absorption Mechanisms

### 5.1 Subfloor Crush Structure

The lower fuselage / subfloor area is designed to absorb crash energy through:

- **Crushable structural elements**: Designed to plastically deform at controlled load levels.  
- **Energy-absorbing materials**: Honeycomb or foam fillers in critical zones.  
- **Progressive failure modes**: Avoid sudden collapse; maintain controlled deceleration profile.

### 5.2 Landing Gear Load Path

Integration with [ATA 32 (Landing Gear)](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/M-MECHANICS/ATA_32-LANDING_GEAR/) ensures:

- Landing gear attachment structure can **tolerate gear separation** in severe crash without compromising cabin integrity.  
- Load distribution from gear to fuselage structure avoids stress concentrations.  
- Gear stroke (compression) absorbs initial impact energy before fuselage crush begins.

### 5.3 Floor Beam System

The floor structure provides:

- **Rigid support** for seats and cargo, transferring loads to fuselage primary structure.  
- **Minimized deformation** at seat attachment points to protect occupants.  
- **Fail-safe design** with redundant load paths to prevent floor collapse.

---

## 6. Occupant Protection

### 6.1 Survival Space

The fuselage structure shall maintain:

- **Minimum headroom** in occupied areas (no roof collapse onto occupants).  
- **Lateral integrity** (no side wall intrusion into seating areas).  
- **Foot well clearance** (no excessive floor deformation that traps occupant lower limbs).

### 6.2 Load Transfer to Occupants

Structural design limits loads transmitted to occupants via:

- **Seat attachment points**: Floor structure designed for seat loads per [CS-25.562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes).  
- **Secondary impacts**: Minimize hazardous projections, sharp edges, and loose objects.  
- **Restraint system interfaces**: Coordination with [ATA 25](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C1-COCKPIT_CABIN_CARGO/ATA_25-EQUIPMENT_FURNISHINGS/) for seat belt and shoulder harness attachment.

---

## 7. Emergency Exits and Evacuation

### 7.1 Exit Integrity

Emergency exits ([ATA 52 (Doors)](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_52-DOORS/)) shall:

- Remain **operable post-crash** (no jamming due to fuselage deformation).  
- Provide **clear opening** without obstruction from displaced structure.  
- Meet **certification test requirements** for opening forces and operation time.

### 7.2 Evacuation Slides

Structural provisions for evacuation slides include:

- **Mounting points** that remain intact post-crash.  
- **Clearance** for slide deployment without structural interference.  
- **Load paths** to support slide attachment loads during deployment and use.

### 7.3 Structural Integrity During Evacuation

The fuselage shall maintain:

- **Stable cabin environment** for at least 90 seconds post-crash (evacuation time requirement).  
- **Access paths** from all occupied areas to exits (no floor collapse or debris blockage).  
- **Resistance to post-crash fire** long enough for evacuation (see [53-00-02-003](./53-00-02-003_Fire_Smoke_Toxicity_Considerations.md)).

---

## 8. Ditching and Water Landings

### 8.1 Regulatory Requirements

Per [CS-25.563](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes), the structure shall:

- Provide **probable escape** for occupants in ditching scenarios.  
- Maintain **buoyancy** for a reasonable time to enable evacuation.  
- Prevent **rapid flooding** that could trap occupants or sink aircraft quickly.

### 8.2 Structural Considerations

- **Watertight compartmentalization**: Bulkheads and seals to limit water ingress.  
- **Impact loads**: Water impact can exceed land crash loads; structure must tolerate hydrodynamic pressures.  
- **Emergency exits**: Must be operable and positioned to enable evacuation from floating aircraft.

### 8.3 BWB-Specific Challenges

The BWB configuration may have unique ditching characteristics:

- **Large wetted area**: Potential for high hydrodynamic loads on lower surface.  
- **Buoyancy distribution**: Wide fuselage may affect stability in water (pitch/roll).  
- **Exit accessibility**: Wide cabin may require more exits or longer evacuation distances to water-accessible exits.

---

## 9. Cargo and Fuel System Protection

### 9.1 Cargo Restraint

Cargo compartments shall:

- Prevent **cargo shifting** into occupied areas during crash.  
- Provide **barriers or nets** rated for crash loads.  
- Avoid **penetration** of floor by cargo masses during upward inertia load cases.

### 9.2 Fuel System Integrity

Fuel tanks and lines shall:

- Be **separated** from occupied areas by crash-resistant barriers.  
- Incorporate **frangible fittings** that break away to prevent fuel spillage into cabin.  
- Meet **[CS-25.721](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)** and [CS-25 Subpart E](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) fuel system crash resistance requirements.

Fuel system design is detailed in [ATA 28 (Fuel)](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/); structural interfaces are defined in [53-00-05_Interfaces](../53-00-05_Interfaces/).

---

## 10. Special Considerations for BWB Configuration

### 10.1 Wide-Body Center-Body

- **Lateral stiffness**: Wider fuselage may require additional lateral reinforcement to prevent side wall collapse.  
- **Multiple load paths**: More stringers/longerons available for redundancy.  
- **Longer floor spans**: May require additional floor beams or energy-absorbing subfloor structure.

### 10.2 Composite Structure

If using composite primary structure:

- **Crush behavior**: Composites may fracture rather than crush; design must ensure energy absorption without brittle failure.  
- **Post-crash integrity**: Delamination or fiber breakage must not compromise evacuation routes.  
- **Fire resistance**: See [53-00-02-003](./53-00-02-003_Fire_Smoke_Toxicity_Considerations.md) for material fire performance.

### 10.3 Integration with Landing Gear

Landing gear attachment points in BWB may be unconventional:

- **Wing-integrated gear**: Load paths into wing-fuselage blend area must be carefully designed.  
- **Center-body gear**: Potential for multiple gear posts; coordinated energy absorption and load distribution.

---

## 11. Testing and Certification

### 11.1 Static Testing

Per [CS-25.561](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes), static tests shall verify:

- Ultimate load capability under emergency landing load cases.  
- Floor and seat attachment structure strength.  
- Cargo barrier effectiveness.

### 11.2 Dynamic Testing

Per [CS-25.562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes), dynamic tests (or validated analysis) shall demonstrate:

- Floor deceleration pulse characteristics.  
- Seat and restraint system performance under crash loads.  
- Structural deformation modes and energy absorption.

### 11.3 Full-Scale Testing

For novel BWB configuration:

- **Vertical drop test**: Full-scale or representative section, per [AC 20-146B](https://www.faa.gov/regulations_policies/advisory_circulars).  
- **Ditching model testing**: Scaled hydrodynamic tests or CFD validation.  
- **Evacuation demonstration**: Full aircraft with structural integrity maintained post-crash (coordination with [ATA 25](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C1-COCKPIT_CABIN_CARGO/ATA_25-EQUIPMENT_FURNISHINGS/)).

Testing plans are detailed in [53-00-07_V_and_V](../53-00-07_V_AND_V/).

---

## 12. Maintenance and Inspection

### 12.1 In-Service Inspections

Crashworthiness-related inspections include:

- **Floor structure**: Check for cracks, corrosion, or damage at seat attachment points.  
- **Energy absorbers**: Ensure crush elements are not pre-damaged or degraded.  
- **Emergency exit surrounds**: Verify structural integrity and alignment for proper operation.

### 12.2 Post-Incident Inspections

After hard landings or minor crashes:

- **Damage assessment**: Evaluate permanent deformation of subfloor, floor beams, seat tracks.  
- **Repair or replace**: Per approved repair manuals; energy absorbers may be single-use.  
- **Functionality checks**: Verify emergency exits still operate correctly.

Inspection procedures are coordinated with [ATA 05 (Time Limits / Maintenance Checks)](../../../../../../O-ORGANIZATION/ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS/).

---

## 13. Documentation and Traceability

### 13.1 Required Documentation

- **Crash analysis reports**: FEA or physical test results demonstrating compliance with [CS-25.561/562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes).  
- **Test plans and results**: Static, dynamic, and ditching tests per certification basis.  
- **Design substantiation**: Load paths, energy absorption mechanisms, material properties.  
- **Repair procedures**: For post-crash or hard landing damage.

### 13.2 Traceability Links

- To **[53-00-03_Requirements](../53-00-03_Requirements/)**: Crashworthiness structural requirements.  
- To **[53-00-04_Design](../53-00-04_Design/)**: Detailed design of crash-resistant features.  
- To **[53-00-06_Engineering](../53-00-06_Engineering/)**: Crash analysis methods and models.  
- To **[53-00-07_V_and_V](../53-00-07_V_AND_V/)**: Crash testing and validation activities.  
- To **[ATA 25](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C1-COCKPIT_CABIN_CARGO/ATA_25-EQUIPMENT_FURNISHINGS/)**: Seat and restraint system integration.  
- To **[ATA 32](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/M-MECHANICS/ATA_32-LANDING_GEAR/)**: Landing gear load path coordination.

---

## 14. Assumptions and Dependencies

- **Crash scenarios**: Based on [CS-25.561/562](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) load cases; additional scenarios for novel BWB config may be defined with authorities.  
- **Material properties**: Crash analysis uses validated material models; aging or environmental effects may require re-analysis.  
- **Mass distribution**: Occupant and cargo loading assumptions must reflect operational reality.  
- **Coordination with other systems**: Crashworthiness is a system-level property; changes in seats, cargo restraints, or landing gear affect overall performance.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** — Subject to human review and approval.  
- Human approver: _[to be completed]_.  
- Repository: `AMPEL360-BWB-H2-Hy-E`  
- Last AI update: 2025-11-22
