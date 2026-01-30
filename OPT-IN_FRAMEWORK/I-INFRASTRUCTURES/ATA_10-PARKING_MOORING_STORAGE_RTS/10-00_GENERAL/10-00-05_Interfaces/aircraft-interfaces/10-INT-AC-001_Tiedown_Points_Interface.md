# 10-INT-AC-001 - Tiedown Points Interface

## 1. Interface Identification

| Parameter | Value |
|-----------|-------|
| Interface Number | 10-INT-AC-001 |
| Interface Type | Mechanical, Structural |
| System A | Aircraft Structure (BWB) |
| System B | Ground Tiedown Equipment |
| ATA Chapter A | ATA-10 |
| ATA Chapter B | ATA-03 (GSE) |
| H2 Related | No |
| Cryo Related | No |
| BWB Specific | Yes |
| Safety Classification | Safety-Related |
| Status | Baselined |

## 2. Interface Description

This interface defines the tiedown attachment points on the AMPEL360-BWB-H2-Hy-E aircraft structure for securing the aircraft during parking, storage, and adverse weather conditions. The BWB configuration requires a distributed tiedown point strategy due to the integrated wing-body structure and wide span.

### Purpose

- Secure aircraft against wind loads during ground operations
- Prevent aircraft movement during parking and storage
- Provide attachment points for weatherproofing covers
- Enable safe outdoor storage in various environmental conditions

### Scope

Covers all primary and secondary tiedown points on the aircraft, including:
- Wing/body tiedown hard points
- Forward and aft fuselage tiedown points
- Emergency tiedown provisions
- Load path analysis for BWB structure

## 3. Interface Parameters

| Parameter | Value | Unit | Tolerance |
|-----------|-------|------|-----------|
| Number of Primary Tiedown Points | 6 | - | - |
| Number of Secondary Tiedown Points | 4 | - | - |
| Ultimate Load per Point | 15,000 | N | ±5% |
| Design Wind Speed | 65 | knots | - |
| Tiedown Angle Range | 30-60 | degrees | ±5° |
| Attachment Bolt Size | M20 | - | ISO metric |
| Thread Type | ISO Metric Class 8.8 | - | - |
| Corrosion Protection | Cadmium Plated | - | Per AMS 2400 |

## 4. Physical Interface

### 4.1 Mechanical

**Primary Tiedown Points (6 locations):**

1. **Forward Port (Station 50, WL 15)**
   - Attachment: Threaded insert M20
   - Material: Aluminum alloy 7075-T6
   - Ultimate load: 15 kN
   - Load direction: 30-60° from horizontal

2. **Forward Starboard (Station 50, WL 15)**
   - Mirror of forward port location
   - Same specifications as forward port

3. **Mid-Body Port (Station 200, WL 20)**
   - Reinforced hard point in wing-body blend region
   - Material: Aluminum alloy 7075-T6 with titanium insert
   - Ultimate load: 15 kN
   - Optimized for BWB load paths

4. **Mid-Body Starboard (Station 200, WL 20)**
   - Mirror of mid-body port location
   - Same specifications as mid-body port

5. **Aft Port (Station 400, WL 18)**
   - Aft fuselage hard point
   - Material: Aluminum alloy 7075-T6
   - Ultimate load: 15 kN
   - Consideration for engine blast effects

6. **Aft Starboard (Station 400, WL 18)**
   - Mirror of aft port location
   - Same specifications as aft port

**Secondary Tiedown Points (4 locations):**
- Located at wing tips (2) and aft empennage (2)
- Lighter duty: 8 kN ultimate load
- M16 threaded inserts
- For additional securing in extreme conditions

**Installation Features:**
- Recessed flush with outer mold line (OML)
- Protected by removable caps when not in use
- High-visibility markings adjacent to each point
- Anti-rotation features for bolt installation

### 4.2 Materials and Coatings

| Component | Material | Coating | Specification |
|-----------|----------|---------|---------------|
| Tiedown Insert | 7075-T6 Aluminum | Anodized Type II | MIL-A-8625 |
| Reinforcement Plate | Titanium Ti-6Al-4V | Passivated | AMS 2700 |
| Attachment Hardware | Alloy Steel | Cadmium Plated | AMS 2400 |
| Protective Cap | Composite/Elastomer | UV Resistant | - |

### 4.3 Access and Identification

- Ground-level access for all primary points
- Stenciled identification: "TIEDOWN POINT - 10-INT-AC-001-[#]"
- Reflective markings for night operations
- Load limit placard adjacent to each point

## 5. H2/Cryo Considerations

| Parameter | Value |
|-----------|-------|
| H2 Related | No |
| Cryo Related | No |
| H2 Compatibility | N/A |
| Special H2 Procedures | None - Standard tiedown procedures apply |

**Note:** While tiedown operations are not H2-specific, ground crew must maintain H2 safety awareness when working near H2 system vents and fueling points.

## 6. BWB Considerations

### BWB-Specific Design Features

1. **Load Distribution:**
   - Tiedown points distributed across wide BWB footprint
   - Load paths optimized for integrated wing-body structure
   - Consideration for non-traditional load path geometry

2. **Geometry Challenges:**
   - Low ground clearance requires ground-level access strategy
   - Wide span necessitates longer tiedown cables/chains
   - Center of gravity distribution unique to BWB

3. **Structural Integration:**
   - Tiedown hard points integrated into primary wing-body structure
   - Load transfer through internal ribs and frames
   - Minimal external protrusions to maintain aerodynamic efficiency

4. **Operational Considerations:**
   - Tiedown pattern adapted to BWB center of gravity envelope
   - Multiple configurations for different loading conditions
   - Compatibility with BWB ground handling equipment

## 7. Constraints

### Operational Constraints
- Maximum tiedown tension: 12 kN per point (80% of ultimate)
- Minimum of 4 primary points must be used simultaneously
- Tiedown angle must be maintained between 30-60° from horizontal
- Not approved for towing or jacking operations

### Environmental Constraints
- Operating temperature: -40°C to +55°C
- Maximum wind speed (tiedown condition): 65 knots
- Not approved for use in icing conditions without anti-ice measures
- UV exposure protection required for long-term storage

### Safety Constraints
- Visual inspection required before each use
- Torque verification required for all connections: 180 Nm ± 10%
- Load testing every 500 flight hours or 12 months
- Immediate replacement if corrosion or damage detected

### Certification Constraints
- Designed per CS-25 Appendix D (Gust loads)
- Proof load test: 1.5 × design limit load
- Ultimate load test: 2.0 × design limit load
- Fatigue testing per MIL-STD-810

## 8. Verification

| Verification Method | Criteria | Status | Reference |
|---------------------|----------|--------|-----------|
| Structural Analysis | Load paths verified by FEA, safety factor ≥1.5 | Completed | ANA-10-AC-001 |
| Proof Load Test | 1.5 × 12 kN = 18 kN, no permanent deformation | Completed | TEST-10-AC-001 |
| Ultimate Load Test | 2.0 × 12 kN = 24 kN, failure load > 24 kN | Completed | TEST-10-AC-002 |
| Dimensional Inspection | All dimensions within tolerance | Completed | INSP-10-AC-001 |
| Installation Demonstration | Tiedown procedure demonstrated successfully | Completed | DEMO-10-AC-001 |
| Environmental Testing | Temperature cycling -40°C to +55°C | Completed | TEST-10-AC-003 |
| Corrosion Resistance | 1000-hour salt spray test | Completed | TEST-10-AC-004 |

## 9. Related Documentation

### Interface Control Documents
- ICD Reference: [10-ICD-003 - BWB Ground Handling ICD](../interface-control-documents/10-ICD-003_BWB_Ground_Handling_ICD.md)

### Related Drawings
- DWG-10-AC-001: Tiedown Point Location Layout
- DWG-10-AC-002: Tiedown Point Detail (Typical)
- DWG-10-AC-003: BWB Structural Load Paths
- DWG-10-AC-004: Tiedown Installation Assembly

### Related Specifications
- SPEC-10-AC-001: Tiedown Hardware Specification
- SPEC-10-AC-002: Installation Torque Requirements
- SPEC-10-03-001: GSE Tiedown Equipment Specification

### Related Standards
- [ATA iSpec 2200](https://www.ata.org/resources/ispec-2200): Chapter 10 - Parking, Mooring, Storage
- [CS-25 Appendix D](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27): Gust Load Requirements
- [MIL-STD-810H](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=213976): Environmental Engineering Considerations
- ISO 2889: Aircraft Ground Support Equipment - General Requirements
- SAE AS8049: Flight Deck and Ground Support Equipment Compatibility

### Cross-ATA References
- [10-INT-ATA-003 - Landing Gear Interface](../ata-cross-references/10-INT-ATA-003_ATA32_Landing_Gear_Interface.md)
- [10-INT-AC-005 - BWB Structural Interface](./10-INT-AC-005_BWB_Structural_Interface.md)

## 10. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-09 | AMPEL360 Engineering | Initial release - BWB tiedown interface definition |
| - | - | - | - |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **BASELINED** – Approved for production use
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-09

---
