# 53-00-01-002 — Structural Segmentation and Nomenclature

**Document ID**: 53-00-01-002  
**Version**: 1.0  
**Date**: 2025-11-22  
**Status**: DRAFT

---

## 1. Purpose

This document establishes the **standard nomenclature and segmentation scheme** for the AMPEL360 BWB fuselage structure. It ensures that all stakeholders—design engineers, analysts, manufacturers, certification authorities, and maintenance organizations—use consistent terminology when referring to structural elements, zones, and assemblies.

---

## 2. BWB Fuselage Structural Philosophy

Unlike conventional tube-and-wing aircraft, the BWB integrates the fuselage (center body) seamlessly with the wing. Key characteristics:

- **Center Body**: The pressurized passenger/cargo compartment is embedded within a wide, blended wing-body structure
- **No Distinct Fuselage/Wing Boundary**: Structural elements transition smoothly from center body to outer wing
- **Multi-Deck Potential**: The deep center body allows for stacked passenger decks
- **Load-Carrying Outer Surface**: The outer skin participates in both aerodynamic shaping and structural load transfer

For clarity, we define:

- **"Fuselage" (ATA 53)**: The center body and pressurized cabin region
- **"Wing" (ATA 57)**: The outer wing panels beyond the center body, including control surfaces
- **"Wing-Body Fairing" or "Blending Region"**: The transition zone jointly owned by ATA 53 and ATA 57

---

## 3. Longitudinal Segmentation (Zones)

The fuselage is divided into **longitudinal zones** from nose to tail:

| Zone | Name | Description | Key Features |
|:-----|:-----|:------------|:-------------|
| **Zone 100** | Forward Fuselage / Nose | Cockpit, radome, forward equipment bay | Flight deck structure, avionics bay, weather radar mount, windshields |
| **Zone 200** | Forward Cabin / Entry | Passenger entry doors, forward galley | Door frames, floor beams, cabin pressure shell, galley attach points |
| **Zone 300** | Mid Cabin (Forward) | Main passenger cabin area (forward) | Seat rails, overhead bin supports, window cut-outs, cabin floor structure |
| **Zone 400** | Center Wing Box / Main Gear Bay | Wing carry-through, main landing gear attachments | Heaviest structural section, wing spars, main gear well, cargo floor |
| **Zone 500** | Mid Cabin (Aft) | Main passenger cabin area (aft) | Seat rails, lavatories, galleys, cabin systems routing |
| **Zone 600** | Aft Cabin / Cargo | Aft passenger/cargo area, APU bay | Aft pressure bulkhead, cargo compartment, APU firewall |
| **Zone 700** | Tail / Empennage Interface | Tail cone, vertical stabilizer attach (if applicable) | Aft fuselage taper, control surface attachments, tail strike protection |

**Note**: Zone numbering may be adjusted during detailed design. This scheme provides a common reference.

---

## 4. Transverse Segmentation (Frames and Stations)

The fuselage structure is divided by **transverse frames** (also called "bulkheads" or "ribs" in some contexts):

- **Frame Numbering**: Frames are numbered sequentially from nose to tail, e.g., FR10, FR20, FR30, … FR700
  - **Major Frames**: Heavy structural frames at critical load transfer points (e.g., pressure bulkheads, gear attachment frames)
  - **Intermediate Frames**: Standard frames at regular intervals (e.g., every 500 mm or 20 inches)
  - **Half Frames**: Partial frames that do not span the full circumference

- **Fuselage Stations (FS)**: A coordinate system along the aircraft longitudinal axis
  - **FS 0**: Defined at the aircraft nose (datum point)
  - **FS increases** toward the tail
  - Example: FS 2500 = 2500 mm aft of the nose datum
  - Critical stations align with major frames, e.g., FR100 at FS 1200, FR400 at FS 8000, etc.

**Frame Spacing**:
- Forward and aft cabin: ~500 mm (standard frame pitch)
- Center wing box (Zone 400): Variable spacing to align with wing spars and gear loads
- Structural analysis determines optimal spacing based on load paths and buckling criteria

---

## 5. Lateral and Vertical Segmentation

### 5.1 Buttock Lines (BL) and Water Lines (WL)

- **Buttock Lines (BL)**: Lateral (spanwise) coordinate
  - BL 0: Aircraft centerline
  - BL increases outboard (e.g., BL 1000, BL 2000, … BL 8000 at outer wing edge)
  - For BWB, BL extends continuously from center body to wing tips

- **Water Lines (WL)**: Vertical coordinate
  - WL 0: Defined at aircraft bottom reference (e.g., underside of keel beam)
  - WL increases upward
  - Example: WL 1500 = 1500 mm above the keel beam

### 5.2 Decks

For multi-deck configurations:

- **Main Deck (Upper Deck)**: Primary passenger cabin, typically WL 1200 to WL 2500
- **Lower Deck**: Cargo or additional passenger seating, typically WL 300 to WL 1200
- **Floor Beams**: Structural beams spanning laterally (BL-to-BL) to support cabin floors
- **Cross Beams**: Fore-and-aft beams connecting floor beams to frames

Deck numbering:
- **Deck 1**: Lower deck
- **Deck 2**: Main deck
- **Deck 3**: Upper deck (if present)

---

## 6. Structural Components Nomenclature

### 6.1 Primary Structure

- **Skin Panels**: Outer aerodynamic surface
  - Designation: Zone + Panel Type + ID (e.g., `Z300-SKIN-L12` = Zone 300, left side, panel 12)
  - Materials: Typically carbon fiber reinforced polymer (CFRP), aluminum-lithium alloy, or hybrid

- **Stringers (Longerons)**: Longitudinal stiffeners running nose-to-tail
  - Designation: Stringer + Position (e.g., `STR-T01` = top center stringer, `STR-B05` = bottom stringer #5)
  - Spacing: Typically 150-200 mm, optimized for buckling and fatigue

- **Frames (Ribs)**: Transverse structural members
  - Designation: Frame Number (e.g., `FR250`, `FR400-M` for major frame at station 400)
  - Types: Ring frames, hat-stiffened frames, C-channel frames

- **Spars (in wing-body region)**: Primary longitudinal members in wing carry-through
  - Designation: Spar + ID (e.g., `SPAR-FWD`, `SPAR-AFT`, `SPAR-C` for center spar)

### 6.2 Secondary Structure

- **Floor Beams**: Lateral beams supporting cabin floor
  - Designation: Floor Beam + Station (e.g., `FLR-BEAM-300` at FR300)
  
- **Bulkheads**: 
  - **Forward Pressure Bulkhead** (`FWD-PBH`): Seals forward cabin pressure envelope
  - **Aft Pressure Bulkhead** (`AFT-PBH`): Seals aft cabin pressure envelope
  - **Cargo Bulkheads**: Separate cargo compartments from cabin

- **Keel Beam**: Central longitudinal beam at bottom of fuselage, provides bending stiffness and ground support
  - Designation: `KEEL-BEAM`

- **Fairings**: Aerodynamic non-structural or lightly loaded skins
  - Examples: nose fairing, tail cone fairing, landing gear door fairings

### 6.3 Joints and Fasteners

- **Splice Joints**: Connect fuselage sections during assembly
  - Designation: Splice + Location (e.g., `SPLICE-FR400` = major splice at Frame 400)
  - Types: Bolted joints, bonded joints, hybrid mechanical-bonded

- **Stringers-to-Skin Joints**: Adhesive bonding, riveting, or co-curing (for composites)

- **Frame-to-Skin Attachment**: Clips, angles, or integral co-bonded construction

---

## 7. Assemblies and Modules

For manufacturing and assembly, the fuselage is divided into **modules** or **sections**:

| Module ID | Name | Zone Coverage | Key Interfaces |
|:----------|:-----|:--------------|:---------------|
| **MOD-100** | Nose Section | Zone 100 | Radome, flight deck structure, forward equipment bay |
| **MOD-200** | Forward Cabin Section | Zone 200-300 | Forward pressure bulkhead, main entry doors, galleys |
| **MOD-400** | Center Wing Box Section | Zone 400 | Wing carry-through, main landing gear, cargo floor, fuel tanks |
| **MOD-500** | Aft Cabin Section | Zone 500-600 | Aft cabin, lavatories, aft cargo, aft pressure bulkhead |
| **MOD-700** | Tail Section | Zone 700 | Tail cone, APU installation, empennage attach fittings |

**Major Joints**: Modules are joined at **major frame stations** (e.g., FR200, FR400, FR600) using bolted or bonded splices.

**Transport Considerations**: Module size is constrained by manufacturing facility door widths, road/rail transport envelopes, and final assembly line capabilities.

---

## 8. Cut-Outs and Apertures

- **Doors (ATA 52)**:
  - Passenger doors: e.g., `DOOR-L1` (left side, position 1), `DOOR-R2` (right side, position 2)
  - Cargo doors: e.g., `CARGO-DOOR-FWD`, `CARGO-DOOR-AFT`
  - Emergency exits: Designated per certification requirements ([CS-25.807](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes))

- **Windows (ATA 56)**:
  - Window + Side + ID (e.g., `WIN-L12` = left side, window #12)
  - Overwing windows: Special reinforcement in wing-body fairing region

- **Access Panels**: For maintenance access to systems and equipment
  - Designation: Access Panel + Location (e.g., `ACP-Z300-10`)

---

## 9. Coordinate System Summary

| Coordinate | Abbreviation | Zero Datum | Positive Direction | Typical Units |
|:-----------|:-------------|:-----------|:-------------------|:--------------|
| Fuselage Station | FS | Nose | Aft | mm |
| Buttock Line | BL | Centerline | Outboard (left/right) | mm |
| Water Line | WL | Keel beam bottom | Upward | mm |

**Sign Convention**:
- Left side: Negative BL (or designated BL-L)
- Right side: Positive BL (or designated BL-R)
- Above centerline: Positive WL
- Forward of datum: FS values < datum FS

---

## 10. Configuration Control and Change Management

- All structural elements are tracked as **Configuration Items (CIs)** in the AMPEL360 PLM system
- Changes to nomenclature, zone boundaries, or frame numbering require **Engineering Change Order (ECO)** approval
- This document is the **master reference** for ATA 53 nomenclature; any deviation must be justified and documented
- Cross-references to other ATA chapters (e.g., ATA 52 door locations, ATA 32 gear attachment frames) must remain synchronized

See `53-00-01-006_Digital_Twin_and_Config_Management.md` for details on traceability.

---

## 11. Visual Reference

> **Note**: Diagrams illustrating the zone layout, frame numbering, and module breakdown are stored in `ASSETS/diagrams/`:
> - `53-00-01-A001_Fuselage_Segmentation.svg` (to be created)
> - `53-00-01-A002_Frame_Numbering.svg` (to be created)
> - `53-00-01-A003_Coordinate_System.svg` (to be created)

---

## 12. Usage Guidelines

- **Design Engineers**: Use this nomenclature consistently in all CAD models, drawings, and specifications
- **Stress Analysts**: Reference frame numbers and stations when defining FEA boundary conditions and load paths
- **Manufacturing**: Use module IDs and frame numbering for work orders, assembly sequences, and quality inspections
- **Maintenance**: Reference zone, frame, and stringer IDs in inspection checklists and repair manuals
- **Certification**: Use standardized nomenclature in compliance reports and substantiation documents

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

## References

- AMPEL360 Documentation Standard: `/AMPEL360_DOCUMENTATION_STANDARD.md`
- ATA iSpec 2200: Section numbering and nomenclature
- [CS-25.807 Emergency Exits](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)
- ISO 1151: Flight dynamics — Concepts, quantities and symbols
- SAE AS8015: Fuselage station, buttock line, and waterline identification
