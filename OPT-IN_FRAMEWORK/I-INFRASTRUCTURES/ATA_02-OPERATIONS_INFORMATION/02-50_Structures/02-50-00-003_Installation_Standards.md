# 02-50-00-003: Installation Standards

## Document Information

- **Document ID**: 02-50-00-003
- **Title**: General Installation Standards for ATA 02 Structures
- **Version**: 1.0.0
- **Status**: DRAFT
- **Date**: 2025-11-21
- **Author**: AMPEL360 Installation Standards Team
- **Applicable To**: All structures within ATA 02-50

## 1. Purpose

This document defines general installation standards, tolerances, fastener specifications, torque values, and references to applicable norms for all structures within ATA 02-50. It provides a unified framework ensuring consistent, safe, and compliant installation practices across the AMPEL360 BWB H2-Hy-E program.

## 2. Scope

This standard applies to:

- **Aircraft-mounted structures**: EFB mounts, displays, access panels
- **Ground infrastructure**: Racks, enclosures, antenna mounts
- **Cable management**: Trays, conduits, wire bundles
- **Support equipment**: Platforms, ladders, safety structures

Installation requirements specific to individual subsystems are detailed in their respective folders but must comply with this general standard.

## 3. General Installation Requirements

### 3.1 Pre-Installation Checklist

Before any structure installation:

- [ ] Review approved design drawings and specifications
- [ ] Verify part numbers and serial numbers match work order
- [ ] Inspect all parts for damage, corrosion, or defects
- [ ] Ensure required tools, torque wrenches, and equipment are available and calibrated
- [ ] Confirm work area is clean, well-lit, and safe
- [ ] Review applicable safety procedures and obtain permits (e.g., hot work, confined space)

### 3.2 Environmental Conditions

Installation must occur within these environmental limits:

| Parameter | Minimum | Maximum | Notes |
|-----------|---------|---------|-------|
| Temperature | 10°C | 35°C | For adhesive curing |
| Relative Humidity | 20% | 80% | Non-condensing |
| Wind Speed (outdoor) | — | 10 m/s | For antenna/mast work |
| Precipitation | None | None | Dry conditions required |

**Exception**: Emergency repairs may be performed outside these limits with engineering approval.

### 3.3 Cleanliness

- **Aircraft structures**: Clean per [AMS 1526](https://www.sae.org/standards/content/ams1526/) (aqueous cleaning) or equivalent
- **Ground structures**: Wipe clean with solvent (IPA or equivalent), no visible contamination
- **Electrical contacts**: Clean with contact cleaner, verify continuity

## 4. Fastener Standards

### 4.1 Fastener Types and Applications

| Application | Fastener Type | Material | Standard | Coating |
|-------------|---------------|----------|----------|---------|
| Aircraft structural | AN/MS bolts | Titanium or SS | [MS20004](https://www.assist.dla.mil/) | Dry film lube |
| Aircraft non-structural | NAS screws | A286 steel | [NAS1351](https://www.assist.dla.mil/) | Cadmium or zinc-nickel |
| Ground equipment | Hex cap screws | Stainless 316 | [ISO 4017](https://www.iso.org/standard/63228.html) | Passivated |
| Cable tray | Thread-forming screws | Stainless 304 | [ISO 1479](https://www.iso.org/standard/6050.html) | None |
| Electrical grounding | Hex bolts with washers | Bronze or copper | [DIN 931](https://www.din.de/) | Tin-plated |

### 4.2 Torque Requirements

#### Aircraft Structures

Torque values per [AC 43.13-1B](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/99861), [Chapter 7](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/99861):

| Bolt Size | Dry Torque (ft-lb) | Lubed Torque (ft-lb) | Notes |
|-----------|-------------------|---------------------|-------|
| AN3 (#10) | 20-25 | 12-15 | Use castellated nut + cotter pin |
| AN4 (1/4") | 50-70 | 30-40 | Inspect threads, no damage |
| AN5 (5/16") | 80-90 | 48-55 | Verify grip length |
| AN6 (3/8") | 160-185 | 95-110 | Washer under nut |
| AN7 (7/16") | 235-255 | 140-155 | Check for proper fit |

**Lubrication**: Use dry film lubricant (e.g., molybdenum disulfide) unless otherwise specified.

#### Ground Structures

Torque values for ISO metric fasteners:

| Bolt Size | Grade 8.8 (Nm) | Grade 10.9 (Nm) | Notes |
|-----------|----------------|-----------------|-------|
| M6 | 10-12 | 14-17 | Common for brackets |
| M8 | 24-29 | 34-41 | Rack mounting bolts |
| M10 | 48-58 | 68-83 | Heavy equipment |
| M12 | 83-100 | 117-142 | Structural connections |
| M16 | 200-240 | 280-340 | Large platform supports |

**Lubrication**: Apply anti-seize compound on stainless-to-stainless threads.

### 4.3 Torque Verification

- Use calibrated torque wrenches (calibrated within last 12 months)
- Apply torque in increments (50%, 75%, 100% of final value)
- Mark torqued fasteners with witness marks (paint or marker)
- Document torque application in installation record

### 4.4 Lock wire and Safety

For critical fasteners (e.g., on aircraft, near H₂ systems):

- **Lock wire**: Use 0.032" stainless steel per [MS20995](https://www.assist.dla.mil/)
- **Direction**: Tighten lock wire in direction that tightens fastener
- **Twist**: 6-8 twists per inch, uniform tension
- **Inspection**: No kinks, breaks, or loose ends

**Alternative**: Self-locking nuts (NAS679 or equivalent) may be used where lock wire is impractical.

## 5. Dimensional Tolerances

### 5.1 General Tolerances

Unless otherwise specified on drawings:

| Feature | Tolerance | Applies To |
|---------|-----------|------------|
| Linear dimensions | ±0.5 mm | Brackets, plates, small parts |
| Hole spacing | ±0.25 mm | Mounting hole patterns |
| Angles | ±1° | Bend angles, mounting angles |
| Flatness | 0.5 mm / 100 mm | Mounting surfaces |
| Hole diameter | +0.1 / -0.0 mm | Clearance holes |

### 5.2 Critical Interfaces

Higher precision required for:

- **Aircraft hard points**: ±0.1 mm on hole locations
- **RF antenna mounts**: ±0.5° alignment, ±1 mm height
- **EFB mounts**: ±2 mm position (for ergonomics and visibility)

### 5.3 As-Built Verification

After installation:
- Measure and record actual dimensions
- Compare to drawing tolerances
- Document deviations exceeding tolerance (requires engineering disposition)

## 6. Material and Finish Standards

### 6.1 Materials

Approved materials for structures:

| Application | Material | Specification | Remarks |
|-------------|----------|---------------|---------|
| Aircraft primary structure | Aluminum 7075-T6 | [AMS 4045](https://www.sae.org/standards/content/ams4045/) | High strength |
| Aircraft secondary structure | Aluminum 6061-T6 | [AMS 4027](https://www.sae.org/standards/content/ams4027/) | Good formability |
| Ground equipment frames | Steel ASTM A36 | [ASTM A36](https://www.astm.org/a0036_a0036m-19.html) | Structural steel |
| Enclosures | Stainless 304/316 | [ASTM A240](https://www.astm.org/a0240_a0240m-20a.html) | Corrosion resistance |
| Composite parts | Carbon fiber/epoxy | [AMS 3913](https://www.sae.org/standards/content/ams3913/) | Lightweight, high strength |

### 6.2 Surface Finishes and Coatings

#### Aircraft Structures
- **Aluminum parts**: Anodize per [MIL-A-8625 Type II](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35789) (clear or dyed)
- **Steel parts**: Cadmium plate per [AMS 2400](https://www.sae.org/standards/content/ams2400/) or zinc-nickel per [AMS 2417](https://www.sae.org/standards/content/ams2417/)
- **Primer/paint**: Epoxy primer per [MIL-PRF-23377](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36271), topcoat per [MIL-PRF-85285](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=203241)

#### Ground Structures
- **Outdoor exposure**: Hot-dip galvanize per [ASTM A123](https://www.astm.org/a0123_a0123m-17.html) or powder coat over zinc primer
- **Indoor equipment**: Powder coat or electrostatic paint, minimum 50 μm thickness
- **Stainless steel**: Passivate per [ASTM A967](https://www.astm.org/a0967_a0967m-17.html) (no further coating required)

### 6.3 Corrosion Protection

For dissimilar metal interfaces:
- Use isolation bushings or washers (nylon, PTFE)
- Apply corrosion-inhibiting compound (e.g., zinc chromate paste)
- Avoid galvanic couples (e.g., aluminum to steel) without isolation

## 7. Grounding and Bonding

### 7.1 Electrical Bonding Requirements

All metallic structures must be bonded to aircraft or facility ground:

| Structure Type | Max Resistance to Ground | Bonding Method |
|----------------|-------------------------|----------------|
| Aircraft-mounted | < 0.001 Ω | Direct metal-to-metal contact or bonding strap |
| Enclosures (EMI) | < 0.01 Ω | Star washers and bonding jumpers |
| Racks and cabinets | < 0.1 Ω | Grounding busbar connection |
| Cable trays | < 1 Ω | Bonded at supports, continuous path |

### 7.2 Bonding Procedure

1. Clean mating surfaces (remove paint, anodize, or oxide)
2. Apply conductive grease or corrosion inhibitor
3. Install bonding strap or hardware
4. Torque fasteners per specification
5. Measure resistance with low-resistance ohmmeter
6. Document resistance value in installation record

**Reference**: [MIL-STD-464](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=284195) for electromagnetic environmental effects.

## 8. Cable Management Standards

### 8.1 Cable Routing

General principles:
- **Separation**: Power and signal cables separated by minimum 150 mm
- **Bend radius**: Minimum 10× cable diameter (fiber optic: 20×)
- **Support spacing**: Maximum 1.5 m for horizontal runs, 1.0 m for vertical
- **Strain relief**: At all terminations and equipment interfaces

### 8.2 Cable Ties and Clamps

| Cable Bundle Diameter | Tie/Clamp Type | Spacing |
|----------------------|----------------|---------|
| < 25 mm | Nylon cable tie (UV-rated) | Every 300 mm |
| 25-50 mm | Cushioned clamp | Every 500 mm |
| > 50 mm | Heavy-duty clamp | Every 750 mm |

**Installation**: Hand-tighten only, avoid over-compression (maximum 80% bundle compression).

### 8.3 Labeling

All cables, trays, and conduits must be labeled per [02-50-06-004_Labeling_Standards.md](./02-50-06_Cable_Management_Systems/02-50-06-004_Labeling_Standards.md):

- **Format**: System-Type-Number (e.g., OPS-ETH-0042)
- **Label material**: Laminated vinyl or heat-shrink, UV-resistant
- **Placement**: Both ends of cable, every access point, every 10 m on long runs

## 9. Inspection and Testing

### 9.1 Visual Inspection

After installation, perform visual inspection for:
- Correct part number and orientation
- All fasteners installed and torqued (witness marks visible)
- No damage, burrs, or sharp edges
- Proper clearances from adjacent structure or equipment
- Grounding straps and bonds in place
- Labels and markings legible and correct

### 9.2 Functional Testing

Where applicable:
- **Mechanical**: Load test to 150% rated load (for platforms, hoists)
- **Electrical**: Continuity and ground resistance check
- **Environmental**: Verify IP rating with water spray test (for enclosures)
- **Operational**: Verify mounted equipment functions correctly

### 9.3 Non-Destructive Testing (NDT)

Critical aircraft structures require NDT:
- **Visual**: 100% of welds and fastener holes
- **Penetrant (PT)**: Suspect cracks or defects in non-ferrous metals
- **Magnetic Particle (MT)**: Steel welds and high-stress areas
- **Ultrasonic (UT)**: Composite laminates for delamination

**Reference**: [ASNT Level II](https://www.asnt.org/) certified technicians perform NDT.

## 10. Documentation and Records

### 10.1 Installation Record Contents

Each structure installation must be documented with:
- Work order or job card number
- Structure ID and serial number
- Installation date and personnel (name, certification)
- Torque values applied (including calibration sticker ID of torque wrench)
- Ground resistance measurements
- Deviation or discrepancy notes (with engineering disposition)
- Inspector signature and stamp

### 10.2 As-Built Records

After installation, update as-built records:
- CAD drawings with actual dimensions
- Photographs of completed installation
- Component traceability (serial numbers, batch codes)
- Configuration status (effectivity, mods incorporated)

### 10.3 Retention

Installation records retained per regulatory requirements:
- **Aircraft**: Life of aircraft + 1 year (per [Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012))
- **Ground infrastructure**: Minimum 10 years or life of structure

## 11. Safety Requirements

### 11.1 Personal Protective Equipment (PPE)

Required PPE for structure installation:
- Safety glasses (ANSI Z87.1)
- Hard hat (ANSI Z89.1) for overhead work
- Steel-toe boots (ASTM F2413)
- Gloves (cut-resistant for handling sheet metal)
- Hearing protection if noise > 85 dBA
- Fall protection harness and lanyard for work > 1.8 m height

### 11.2 Fall Protection

For elevated work:
- Use scaffolding, aerial lifts, or fall arrest systems
- Anchor points rated for 5000 lb (22 kN) per person
- 100% tie-off when climbing or working at height
- Inspect harness and lanyard before each use

### 11.3 Hazardous Environments

Special precautions for:
- **H₂ areas**: Intrinsically safe tools, hot work permit, gas monitoring
- **Confined spaces**: Entry permit, atmospheric testing, rescue plan
- **High voltage**: Lockout/tagout (LOTO), voltage verification

**Reference**: OSHA 1910 regulations (USA) or equivalent local standards.

## 12. Quality Control and Acceptance

### 12.1 Inspection Points

Quality hold points during installation:
1. **Before installation**: Part verification and cleanliness check
2. **After fastening**: Torque witness mark and alignment check
3. **After grounding**: Resistance measurement
4. **Final inspection**: Visual, functional, documentation review

### 12.2 Acceptance Criteria

Structure is acceptable when:
- All dimensions within tolerance
- All fasteners torqued and safety-wired per specification
- Ground resistance within limits
- No workmanship defects (scratches, dents, corrosion)
- Documentation complete and signed

### 12.3 Non-Conformance

If structure does not meet acceptance criteria:
- Document discrepancy with photos and measurements
- Submit to engineering for disposition (accept, rework, or reject)
- Implement corrective action
- Re-inspect after rework

## 13. Applicable Standards and References

### 13.1 Aerospace Standards

- **[CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)** — Large Aeroplanes (structural requirements)
- **[Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)** — Certification Procedures
- **[AC 43.13-1B](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/99861)** — Acceptable Methods, Techniques, and Practices – Aircraft Inspection and Repair
- **[DO-160G](https://www.rtca.org/)** — Environmental Conditions and Test Procedures for Airborne Equipment
- **[MIL-STD-464](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=284195)** — Electromagnetic Environmental Effects

### 13.2 Industrial Standards

- **[ISO 9001:2015](https://www.iso.org/standard/62085.html)** — Quality Management Systems
- **[ISO 4017](https://www.iso.org/standard/63228.html)** — Hexagon Head Screws
- **[ASTM A36](https://www.astm.org/a0036_a0036m-19.html)** — Structural Steel
- **[ASTM A123](https://www.astm.org/a0123_a0123m-17.html)** — Zinc Coating (Hot-Dip)
- **[IEC 60529](https://webstore.iec.ch/publication/2452)** — Degrees of Protection (IP Code)

### 13.3 Safety Standards

- **[NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code)** — Hydrogen Technologies Code
- **[ISO 19880-1](https://www.iso.org/standard/71940.html)** — Gaseous Hydrogen Fueling Stations
- **OSHA 1910** — Occupational Safety and Health Standards (USA)

## 14. Revision and Updates

### 14.1 Document Maintenance

This standard is reviewed and updated:
- Annually, or
- When new regulations, materials, or techniques are introduced, or
- After significant installation discrepancies or safety events

### 14.2 Change Control

Changes to this standard require:
- Engineering review and approval
- Quality assurance concurrence
- Update of affected subsystem documents
- Training and communication to installation personnel

## 15. Summary

This installation standards document provides a comprehensive, traceable framework for the safe and compliant installation of all structures within ATA 02-50. Adherence to these standards ensures consistent quality, regulatory compliance, and operational safety across the AMPEL360 BWB H2-Hy-E program.

For subsystem-specific installation procedures, refer to the respective subsystem folders and documents within [02-50_Structures](./README.md).

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.

---
