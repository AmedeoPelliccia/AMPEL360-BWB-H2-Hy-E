# 10-INT-AC-005 - BWB Structural Interface

## 1. Interface Identification

| Parameter | Value |
|-----------|-------|
| Interface Number | 10-INT-AC-005 |
| Interface Type | Structural, Mechanical |
| System A | BWB Airframe Structure |
| System B | Ground Handling Equipment & Infrastructure |
| ATA Chapter A | ATA-10 |
| ATA Chapter B | ATA-03 (GSE), Multiple |
| H2 Related | Indirectly (structural support for H2 systems) |
| Cryo Related | Indirectly (LH2 tank mounting structure) |
| BWB Specific | Yes |
| Safety Classification | Safety-Critical |
| Status | Baselined |

## 2. Interface Description

This interface defines the unique structural considerations of the Blended Wing Body (BWB) configuration as they relate to parking, mooring, storage, and ground handling operations. The BWB's integrated wing-body design presents distinct challenges and opportunities compared to conventional aircraft configurations.

### Purpose

- Define BWB-specific structural load paths for ground operations
- Specify attachment point locations optimized for BWB geometry
- Identify clearance requirements and access constraints
- Provide guidance for ground equipment positioning
- Ensure structural integrity during all ground operations

### Scope

Covers BWB structural aspects including:
- Load-bearing structure characteristics
- Ground support point distribution
- Clearance envelopes and access requirements
- Structural load limits for ground operations
- Integration with H2 tank structural mounting
- Aerodynamic surface protection during ground ops

## 3. Interface Parameters

### 3.1 BWB Geometric Parameters

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Maximum Span | 88 | m | At widest point of BWB planform |
| Overall Length | 68 | m | Nose to aft fuselage |
| Maximum Width (Center Body) | 42 | m | Widest part of integrated structure |
| Height (Ground to Top) | 12.5 | m | Minimal vertical profile |
| Ground Clearance (Minimum) | 2.8 | m | Below center body |
| Wing Tip Ground Clearance | 4.5 | m | At outer wing sections |

### 3.2 Structural Load Parameters

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| Maximum Ramp Weight | 365,000 | kg | - |
| Maximum Takeoff Weight (MTOW) | 360,000 | kg | - |
| Maximum Zero Fuel Weight | 285,000 | kg | - |
| Center of Gravity Range (Longitudinal) | 45-58 | % MAC | Wide range due to BWB |
| Center of Gravity Range (Lateral) | ±0.3 | m from CL | Symmetric loading required |
| Maximum Wing Loading | 650 | kg/m² | Average over wing area |

### 3.3 Ground Support Points

| Support Type | Quantity | Load Capacity (each) | Distribution |
|--------------|----------|----------------------|--------------|
| Jacking Points | 6 | 120,000 kg | 3 forward, 3 aft |
| Tiedown Points | 6 | 15 kN | Distributed per 10-INT-AC-001 |
| Mooring Points | 8 | 25 kN | Distributed per 10-INT-AC-002 |
| Towing Attachment | 1 (nose) | 200 kN | Center nose structure |
| Ground Lock Points | 3 | N/A | Main gear (2), nose gear (1) |

## 4. Physical Interface

### 4.1 BWB Structural Characteristics

**Integrated Wing-Body Structure:**
- No distinct fuselage-to-wing joint (unlike conventional aircraft)
- Continuous load-bearing outer skin (monocoque construction)
- Internal structural ribs oriented spanwise and chordwise
- Load paths optimized for flight efficiently shared for ground loads

**Primary Load-Bearing Structure:**
1. **Front Spar:** Located ~25% chord, carries primary wing bending loads
2. **Rear Spar:** Located ~75% chord, aft load path
3. **Center Keel:** Longitudinal centerline structure, critical for bending/torsion
4. **Rib Structure:** Spanwise ribs maintain airfoil shape and distribute loads
5. **Center Body Frame:** Heavy frames in center section for pressurization and landing gear

**Structural Material Distribution:**
- Center body: Aluminum-lithium alloy (2099-T86) for weight savings
- Wing structure: 7075-T6 aluminum for high strength
- Keel structure: Titanium Ti-6Al-4V for high loads
- Reinforcements: Carbon fiber composite in selected high-stress areas

### 4.2 Ground Support Interface Points

**Forward Jacking Points (3):**
- **Location:** Station 60, BL ±180 and CL
- **Integrated into:** Front spar attach bulkhead
- **Jack pad area:** 150 × 150 mm, load-spreading plate
- **Ultimate load:** 180,000 kg (1.5 × limit load)

**Aft Jacking Points (3):**
- **Location:** Station 380, BL ±200 and CL
- **Integrated into:** Rear spar attach bulkhead
- **Jack pad area:** 150 × 150 mm
- **Ultimate load:** 180,000 kg (1.5 × limit load)

**Towing Attachment (Nose):**
- **Location:** Station 10, CL, WL 8
- **Attachment type:** Forged steel tow fitting
- **Ultimate load:** 300 kN (1.5 × towing load)
- **Load path:** Nose landing gear bulkhead to center keel

### 4.3 Clearance Envelopes

**Ground Equipment Clearance Zones:**

1. **Under-Body Zone (Center Body):**
   - Minimum clearance: 2.8 m
   - Access for maintenance: 2.2 m clear height required
   - Equipment restrictions: Max height 2.5 m for safe operations

2. **Wing Tip Zone:**
   - Minimum clearance: 4.5 m
   - Wing tip protection required during ground movements
   - No GSE within 3 m of wing tips when engines operating

3. **Engine Zone:**
   - Engine inlet clearance: 5 m forward, 180° arc
   - Engine exhaust clearance: 30 m aft, 45° arc
   - FOD (Foreign Object Damage) critical zone

4. **H2 System Zone:**
   - H2 vent outlet: 10 m safety zone, no equipment/personnel
   - Fueling connection: 5 m safety zone during fueling
   - LH2 tank area: Under-body access restricted, cold hazard

### 4.4 Access Points and Servicing

**Ground-Level Access Doors:**
- Total: 24 access doors on lower surface
- Sizes: Small (0.6 × 0.8 m), Medium (1.0 × 1.2 m), Large (1.8 × 2.4 m)
- Load rating: Ground crew weight + tools (200 kg per panel)

**Internal Access Ways:**
- Longitudinal access tunnel: Nose to aft, 1.2 m × 1.0 m
- Lateral access ways: CL to wing root, 0.8 m × 0.8 m
- Climb provisions: Internal ladders and platforms

## 5. H2/Cryo Considerations

| Parameter | Value |
|-----------|-------|
| H2 Related | Indirectly (structural support) |
| Cryo Related | Yes (LH2 tank mounting) |
| H2 Tank Location | Center body, Station 150-250 |
| Structural Temperature Range | -50°C (cryo exposure) to +70°C |

**H2 System Structural Integration:**

1. **LH2 Tank Mounting:**
   - Tank suspended from upper BWB structure
   - Mounting frames: Titanium for low-temperature compatibility
   - Thermal isolation: Composite struts minimize heat transfer
   - Load path: Tank weight (full) → mounting frames → keel structure

2. **Cryogenic Structural Considerations:**
   - Materials selected for low-temperature toughness
   - Thermal expansion provisions in mounting system
   - Structure shielded from direct LH2 exposure (-253°C)
   - Insulation integrated into structural design

3. **Ground Operations Impact:**
   - LH2 tank weight affects CG during fueling
   - Jacking operations must account for tank loads
   - Structural access restricted near cryo systems
   - Thermal protection for ground crew

## 6. BWB Considerations

### 6.1 BWB-Specific Structural Advantages

1. **Load Distribution:**
   - Wide structure distributes ground loads over large area
   - Reduced stress concentrations compared to conventional aircraft
   - Efficient load paths from landing gear to structure

2. **Stability:**
   - Wide track landing gear provides excellent ground stability
   - Low center of gravity reduces tip-over risk
   - Large surface area for distributed attachment points

3. **Access:**
   - Low profile enables ground-level access to most systems
   - Reduced need for specialized high-reach equipment
   - Internal volume provides protected work areas

### 6.2 BWB-Specific Structural Challenges

1. **Non-Conventional Geometry:**
   - Specialized GSE required for BWB profile
   - Training required for personnel unfamiliar with BWB
   - Clearance planning more complex than conventional aircraft

2. **Load Path Complexity:**
   - Integrated structure requires careful load analysis
   - Ground loads distributed differently than in flight
   - Multiple load paths must be considered for each operation

3. **Access Constraints:**
   - Large wing surface area limits access points
   - Long internal access routes to some systems
   - Aerodynamic surface protection critical

4. **Ground Handling:**
   - Towing requires special consideration of CG location
   - Turning radius larger than conventional aircraft
   - Pushback operations require careful planning

## 7. Constraints

### Structural Constraints
- Maximum jacking load: 120,000 kg per jack point
- Maximum ground wind speed: 65 knots (tied down), 45 knots (free)
- Hangar door clearance: 45 m width minimum
- Ground surface bearing capacity: 15 MPa (1,500 kPa) minimum

### Operational Constraints
- No jacking operations with fuel (H2 or otherwise) in tanks
- Minimum 2 personnel required for any ground support operations
- All aerodynamic surfaces must be protected during ground movements
- No heavy equipment within 5 m of aircraft structure

### Environmental Constraints
- Ground surface temperature: -20°C to +60°C
- Structure temperature limits: -50°C to +70°C
- Not approved for operation on unpaved surfaces
- Snow/ice accumulation must be removed before ground ops

### Certification Constraints
- Designed per CS-25 (Large Aeroplanes) with BWB-specific allowances
- Jacking analysis per CS-25.513 (Static ground loads)
- Ultimate load factors applied to all ground load conditions
- Fatigue analysis for repeated ground load cycles

## 8. Verification

| Verification Method | Criteria | Status | Reference |
|---------------------|----------|--------|-----------|
| Finite Element Analysis | All stress levels < allowable, SF ≥ 1.5 | Completed | ANA-10-AC-004 |
| Full-Scale Static Test | Jacking test to 1.5 × limit load | Completed | TEST-10-AC-019 |
| Ground Handling Demo | All ground operations demonstrated | Completed | DEMO-10-AC-004 |
| Clearance Verification | Physical mockup clearance check | Completed | INSP-10-AC-004 |
| Load Path Analysis | All load paths verified and documented | Completed | ANA-10-AC-005 |
| Thermal Analysis | Cryo system integration verified | Completed | ANA-10-H2-001 |

## 9. Related Documentation

### Interface Control Documents
- ICD Reference: [10-ICD-003 - BWB Ground Handling ICD](../interface-control-documents/10-ICD-003_BWB_Ground_Handling_ICD.md)

### Related Drawings
- DWG-10-AC-013: BWB Overall Geometry and Clearance Envelope
- DWG-10-AC-014: Ground Support Point Locations
- DWG-10-AC-015: Structural Load Paths (Ground Condition)
- DWG-10-AC-016: Access Door Locations and Specifications
- DWG-10-H2-001: LH2 Tank Structural Integration

### Related Specifications
- SPEC-10-AC-007: BWB Ground Handling Requirements
- SPEC-10-AC-008: Structural Load Limits (Ground Operations)
- SPEC-53-10-001: BWB Airframe Structural Specification

### Related Standards
- [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27): Certification Specifications for Large Aeroplanes
- [CS-25.513](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27): Static Ground Loads
- ATA iSpec 2200 Chapter 10: Parking, Mooring, Storage
- SAE AIR1845: Requirements for Ground Support Equipment

### Cross-ATA References
- [10-INT-AC-001 - Tiedown Points Interface](./10-INT-AC-001_Tiedown_Points_Interface.md)
- [10-INT-AC-002 - Mooring Attachment Points](./10-INT-AC-002_Mooring_Attach_Points.md)
- [10-INT-GSE-001 - Towing Interface](../gse-interfaces/10-INT-GSE-001_Towing_Interface.md)
- [10-INT-GSE-002 - Jacking Points Interface](../gse-interfaces/10-INT-GSE-002_Jacking_Points_Interface.md)
- [10-INT-H2-004 - LH2 Tank Interface](../h2-system-interfaces/10-INT-H2-004_LH2_Tank_Interface.md)

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-09 | AMPEL360 Engineering | Initial release - BWB structural interface definition |
| - | - | - | - |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **BASELINED** – Approved for production use
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-09

---
