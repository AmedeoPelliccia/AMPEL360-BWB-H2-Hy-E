# ATA 25 — Equipment/Furnishings — Subject Code Index (00_INDEX.md)

**Version:** 1.0  
**Date:** 2026-01-09  
**Purpose:** Complete subject (yy) code mapping for ATA 25 Equipment/Furnishings

---

## Quick Reference

| Section | Code Range | Actual Subjects | Description |
|---------|------------|-----------------|-------------|
| 25-00 | 00-08, 10 | 10 | Equipment/Furnishings General |
| 25-10 | 00-07, 10 | 9 | Flight Compartment |
| 25-20 | 00-07, 10, 90 | 10 | Passenger Compartment |
| 25-30 | 00-06, 10, 90 | 9 | Galley |
| 25-40 | 00-05, 10 | 7 | Lavatories |
| 25-50 | 00-04, 10 | 6 | Additional Compartments |
| 25-60 | 00-06, 10 | 8 | Emergency |
| 25-70 | 00-03, 10 | 5 | Available |
| 25-80 | 00-06, 10 | 8 | Insulation |
| **Total** | | **72** | **All sections** |

**Note:** Subject code ranges are non-contiguous. The codes listed above represent the actual implemented subjects, not all numbers in the range. For example, "00-08, 10" means subjects 00, 01, 02, 03, 04, 05, 06, 07, 08, and 10 (skipping 09).

---

## 25-00 — Equipment/Furnishings General

Chapter boundary, governance, zoning, interfaces to owner systems, maintainability philosophy, and publication strategy.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-00-00 | Chapter overview | Equipment/Furnishings chapter general landing topic | `25-00-00-chapter-overview/` |
| 25-00-01 | Scope & boundaries | What is ATA 25 vs other ATA chapters | `25-00-01-scope-boundaries/` |
| 25-00-02 | Architecture & zoning | Flight deck / cabin / cargo / crew rest | `25-00-02-architecture-and-zoning/` |
| 25-00-03 | Interfaces matrix | ATA 21/23/24/33/35/38/44/50/52/26 as applicable | `25-00-03-interfaces-matrix/` |
| 25-00-04 | Attachment standards | Mounting rails, hardpoints, retainers | `25-00-04-attachment-standards/` |
| 25-00-05 | Materials, flammability & toxicity constraints | Project policy pointer | `25-00-05-materials-flammability-toxicity/` |
| 25-00-06 | Maintainability & access philosophy | LRU vs furniture modules, access paths | `25-00-06-maintainability-and-access-philosophy/` |
| 25-00-07 | Inspection & servicing concept | Cleaning, wear, cabin checks | `25-00-07-inspection-and-servicing-concept/` |
| 25-00-08 | Safety & human factors | Evac, accessibility, injury prevention | `25-00-08-safety-and-human-factors/` |
| 25-00-09 | Configuration & change control | Baselines, options, SB/retrofit impacts for furnishings | `25-00-09-configuration-and-change-control/` |
| 25-00-10 | Verification strategy | Fit checks, loads, abuse, durability, evacuation support | `25-00-10-verification-strategy/` |

**Note:** Subject code 25-00-09 is not used in this implementation. The range is non-contiguous.

---

## 25-10 — Flight Compartment

Flight deck furnishings and removable equipment (seats, stowage, tables, partitions, etc.).

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-10-00 | Flight compartment overview | Section-level overview | `25-10-00-flight-compartment-overview/` |
| 25-10-01 | Flight crew seats | Installation, adjustment, restraints | `25-10-01-flight-crew-seats/` |
| 25-10-02 | Observer/jump seats | If applicable | `25-10-02-observer-jump-seats/` |
| 25-10-03 | Stowage/wardrobes/manual storage | Flight deck storage provisions | `25-10-03-stowage-wardrobes-manual-storage/` |
| 25-10-04 | Tables/partitions/sunshades | Where treated as furnishings | `25-10-04-tables-partitions-sunshades/` |
| 25-10-05 | Equipment racks & enclosures | As furnishings, not the equipment itself | `25-10-05-equipment-racks-and-enclosures/` |
| 25-10-06 | Floor coverings and anti-skid provisions | Flight deck flooring | `25-10-06-floor-coverings-and-anti-skid/` |
| 25-10-07 | Flight deck escape provisions | Interfaces to doors/exits procedures | `25-10-07-flight-deck-escape-provisions/` |
| 25-10-10 | Verification | Static loads, endurance, ergonomics, maintainability checks | `25-10-10-verification/` |

**Note:** Subject codes 25-10-08 and 25-10-09 are not used in this implementation. The range is non-contiguous.

---

## 25-20 — Passenger Compartment

Cabin interior architecture: seats, bins, lining, partitions, attendant stations.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-20-00 | Passenger compartment overview | Section-level overview | `25-20-00-passenger-compartment-overview/` |
| 25-20-01 | Passenger seats | Tracks, retention, IFE provisions boundary | `25-20-01-passenger-seats/` |
| 25-20-02 | Cabin attendant seats and stations | As furnishings | `25-20-02-cabin-attendant-seats-and-stations/` |
| 25-20-03 | Overhead stowage bins and latches | Bin systems and retention | `25-20-03-overhead-stowage-bins-and-latches/` |
| 25-20-04 | Lining, sidewalls, ceiling panels, monuments | Furnishings scope | `25-20-04-lining-sidewalls-ceiling-panels-monuments/` |
| 25-20-05 | Curtains/partitions/class dividers | Cabin separation systems | `25-20-05-curtains-partitions-class-dividers/` |
| 25-20-06 | Floor coverings/carpets/liners | Cabin flooring systems | `25-20-06-floor-coverings-carpets-liners/` |
| 25-20-07 | Accessibility provisions | PRM considerations, handholds, signage boundary | `25-20-07-accessibility-provisions/` |
| 25-20-10 | Verification | Loads, abuse, latch integrity, evacuation clearances | `25-20-10-verification/` |
| 25-20-90 | BWB cabin layout modularity program delta | Monument zoning constraints for BWB configuration | `25-20-90-bwb-cabin-layout-modularity-program-delta/` |

**Note:** Subject codes 25-20-08 and 25-20-09 are not used in this implementation. The range is non-contiguous.

---

## 25-30 — Galley

Galley monuments and removable equipment integration.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-30-00 | Galley overview | Section-level overview | `25-30-00-galley-overview/` |
| 25-30-01 | Galley structures/monuments and attach points | Monument installation and attachment | `25-30-01-galley-structures-and-attach-points/` |
| 25-30-02 | Inserts integration | Ovens/chillers/coffee makers—mounting and restraint | `25-30-02-inserts-integration/` |
| 25-30-03 | Trolleys/carts and retention systems | Cart stowage and restraint | `25-30-03-trolleys-carts-and-retention/` |
| 25-30-04 | Interfaces | 24 power, 38 water/waste, 21 ventilation, 26 fire protection | `25-30-04-interfaces/` |
| 25-30-05 | Safety & operational constraints | Hot surfaces, pinch points, secure stow | `25-30-05-safety-and-operational-constraints/` |
| 25-30-06 | Cleaning/maintenance access | Galley maintenance provisions | `25-30-06-cleaning-and-maintenance-access/` |
| 25-30-10 | Verification | Restraint loads, abuse, thermal adjacency checks | `25-30-10-verification/` |
| 25-30-90 | Galley load-shedding compatibility program delta | Compatibility with electric energy management | `25-30-90-galley-load-shedding-compatibility-program-delta/` |

**Note:** Subject codes 25-30-07, 25-30-08, and 25-30-09 are not used in this implementation. The range is non-contiguous.

---

## 25-40 — Lavatories

Lavatory monuments and removable fittings.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-40-00 | Lavatories overview | Section-level overview | `25-40-00-lavatories-overview/` |
| 25-40-01 | Lavatory monument/module installation | Module installation and attach points | `25-40-01-lavatory-module-installation/` |
| 25-40-02 | Furnishings | Mirrors, cabinets, dispensers, seats where applicable | `25-40-02-lavatory-furnishings/` |
| 25-40-03 | Interfaces | 38 water/waste, 24 power, 21 ventilation | `25-40-03-interfaces/` |
| 25-40-04 | Accessibility and safety constraints | PRM and safety considerations | `25-40-04-accessibility-and-safety/` |
| 25-40-05 | Cleaning/maintenance access | Lavatory maintenance provisions | `25-40-05-cleaning-and-maintenance-access/` |
| 25-40-10 | Verification | Fit, door clearances, latch integrity, abuse checks | `25-40-10-verification/` |

**Note:** Subject codes 25-40-06 through 25-40-09 are not used in this implementation. The range is non-contiguous.

---

## 25-50 — Additional Compartments

Crew rest modules, underfloor equipment spaces, and extra compartments treated as furnishings.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-50-00 | Additional compartments overview | Section-level overview | `25-50-00-additional-compartments-overview/` |
| 25-50-01 | Crew rest compartments | Modules, bunks, privacy partitions | `25-50-01-crew-rest-compartments/` |
| 25-50-02 | Wardrobes/stowage monuments outside cabin core | External storage monuments | `25-50-02-wardrobes-and-external-stowage-monuments/` |
| 25-50-03 | Cargo accessory equipment treated as furnishings | Restraints/latches/rollers boundary-managed | `25-50-03-cargo-accessory-equipment-boundary-managed/` |
| 25-50-04 | Lifts/stairs | If applicable in multi-deck concepts | `25-50-04-lifts-stairs-multideck-provisions/` |
| 25-50-05 | Reserved | Reserved for future additional-compartment subjects | `25-50-05-reserved/` |
| 25-50-06 | Reserved | Reserved for future additional-compartment subjects | `25-50-06-reserved/` |
| 25-50-07 | Reserved | Reserved for future additional-compartment subjects | `25-50-07-reserved/` |
| 25-50-08 | Reserved | Reserved for future additional-compartment subjects | `25-50-08-reserved/` |
| 25-50-09 | Reserved | Reserved for future additional-compartment subjects | `25-50-09-reserved/` |
| 25-50-10 | Verification | Loads, restraint integrity, access/egress | `25-50-10-verification/` |

**Note:** Subject codes 25-50-05 through 25-50-09 are not used in this implementation. The range is non-contiguous.

---

## 25-60 — Emergency

Emergency equipment stowage, accessibility, and inspection.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-60-00 | Emergency overview | Section-level overview | `25-60-00-emergency-overview/` |
| 25-60-01 | Evacuation equipment | Slides/rafts integration and stowage governance | `25-60-01-evacuation-equipment/` |
| 25-60-02 | Life vests / flotation devices | Stowage, access, inspections | `25-60-02-life-vests-flotation-devices/` |
| 25-60-03 | ELT/locator devices stowage provisions | System boundary-managed | `25-60-03-locator-devices-stowage/` |
| 25-60-04 | First-aid and medical kits | Stowage/accessibility | `25-60-04-first-aid-and-medical-kits/` |
| 25-60-05 | Emergency tools | Crash axe, flashlights, megaphones, etc. | `25-60-05-emergency-tools/` |
| 25-60-06 | Inspection intervals and servicing checks | Maintenance intervals and procedures | `25-60-06-inspection-intervals-and-servicing-checks/` |
| 25-60-07 | Reserved emergency subject | Placeholder for future emergency equipment subject | `25-60-07-reserved-emergency-subject/` |
| 25-60-08 | Reserved emergency subject | Placeholder for future emergency equipment subject | `25-60-08-reserved-emergency-subject/` |
| 25-60-09 | Reserved emergency subject | Placeholder for future emergency equipment subject | `25-60-09-reserved-emergency-subject/` |
| 25-60-10 | Verification | Access time, retention loads, inspection repeatability | `25-60-10-verification/` |

**Note:** Subject codes 25-60-07, 25-60-08, and 25-60-09 are not used in this implementation. The range is non-contiguous.

---

## 25-70 — Available

Controlled placeholder for airline/customer options.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-70-00 | Available overview | Section-level overview | `25-70-00-available-overview/` |
| 25-70-01 | Allocation policy | What qualifies to live in 25-70 | `25-70-01-allocation-policy/` |
| 25-70-02 | Airline option packages | Placeholders + governance | `25-70-02-airline-option-packages/` |
| 25-70-03 | Customer configuration deltas | CSDB applicability linkage | `25-70-03-customer-configuration-deltas/` |
| 25-70-04 | Reserved subject 04 | Reserved/available slot for airline/customer options | `25-70-04-reserved-subject-04/` |
| 25-70-05 | Reserved subject 05 | Reserved/available slot for airline/customer options | `25-70-05-reserved-subject-05/` |
| 25-70-06 | Reserved subject 06 | Reserved/available slot for airline/customer options | `25-70-06-reserved-subject-06/` |
| 25-70-07 | Reserved subject 07 | Reserved/available slot for airline/customer options | `25-70-07-reserved-subject-07/` |
| 25-70-08 | Reserved subject 08 | Reserved/available slot for airline/customer options | `25-70-08-reserved-subject-08/` |
| 25-70-09 | Reserved subject 09 | Reserved/available slot for airline/customer options | `25-70-09-reserved-subject-09/` |
| 25-70-10 | Verification | Configuration control checks | `25-70-10-verification/` |

**Note:** Subject codes 25-70-04 through 25-70-09 are not used in this implementation. The range is non-contiguous.

---

## 25-80 — Insulation

Thermal/acoustic insulation as a furnishings-managed topic.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 25-80-00 | Insulation overview | Section-level overview | `25-80-00-insulation-overview/` |
| 25-80-01 | Thermal insulation | Coverage, thickness classes, installation rules | `25-80-01-thermal-insulation/` |
| 25-80-02 | Acoustic insulation | Noise reduction targets and placement logic | `25-80-02-acoustic-insulation/` |
| 25-80-03 | Condensation control and moisture barriers | Moisture management systems | `25-80-03-condensation-control-and-moisture-barriers/` |
| 25-80-04 | Materials & flammability constraints | Policy pointer | `25-80-04-materials-and-flammability-constraints/` |
| 25-80-05 | Installation workmanship and sealing rules | Installation standards | `25-80-05-installation-workmanship-and-sealing/` |
| 25-80-06 | Inspection/repair/replace rules | Maintenance procedures | `25-80-06-inspection-repair-replace/` |
| 25-80-07 | Interfaces to ECS/structures/systems | Definition of insulation interfaces and responsibilities | `25-80-07-interfaces-ecs-structures-systems/` |
| 25-80-08 | Special zones and limitations | Insulation rules in fire zones, wet areas, equipment bays | `25-80-08-special-zones-and-limitations/` |
| 25-80-09 | Insulation configuration and documentation | Drawings, part lists, and change control for insulation | `25-80-09-configuration-and-documentation/` |
| 25-80-10 | Verification | Thermal performance adjacency checks, moisture tests, durability | `25-80-10-verification/` |

**Note:** Subject codes 25-80-07, 25-80-08, and 25-80-09 are not used in this implementation. The range is non-contiguous.

---

## Naming Convention

Folder names follow the pattern:

```
25-{xx}-{yy}-{descriptive-slug}
```

Where:
- `xx` = section code (00, 10, 20, 30, 40, 50, 60, 70, 80)
- `yy` = subject code (00-10 for standard subjects, 90-99 for program-specific deltas)
- `descriptive-slug` = human-readable kebab-case description

**Example:** `25-20-01-passenger-seats/`

The two-digit `yy` code remains stable even if the descriptive slug is refined later, ensuring deterministic folder names and traceability.

---

## Program-Specific Delta Codes (yy=90-99)

Reserved for **AMPEL360-specific deltas** to avoid collisions with official SNS extracts:

| Code | Usage | Sections Using |
|------|-------|----------------|
| 90 | BWB cabin layout modularity and galley load-shedding | 25-20, 25-30 |
| 91-99 | Reserved for future program-specific needs | — |

---

## Cross-References by Topic

### BWB-Specific
- **25-00-02**: Architecture & zoning (BWB cabin layout considerations)
- **25-20-90**: BWB cabin layout modularity program delta

### Electric Propulsion Environment
- **25-30-90**: Galley load-shedding compatibility with electric energy management
- **25-00-03**: Interfaces matrix (electrical power management)

### Safety-Critical
- **25-00-08**: Safety & human factors
- **25-20-07**: Accessibility provisions
- **25-40-04**: Accessibility and safety constraints
- **25-60**: Emergency (all subjects)
- All **LC07_Safety** folders in SSOT

### Verification & Validation
- All subjects with **yy=10**: V&V folders
- **25-00-10**: Verification strategy (top-level)

---

## Document Control

| Field | Value |
|-------|-------|
| **Document** | ATA 25 Subject Code Index |
| **Version** | 1.0 |
| **Date** | 2026-01-09 |
| **Status** | Active |
| **Owner** | AMPEL360 Equipment/Furnishings System WG |
| **Repository** | AMPEL360-AIR-T |
| **Related** | README.md, ATA_03_NUMBERING_GUIDE.md |

---

## Usage Notes

1. **Adding a new subject:** Use the next available `yy` code in the appropriate section, or use 91-99 for program-specific needs.
2. **Reconciliation with SNS:** If official SNS codes are provided, update this index and rename folders accordingly.
3. **Traceability:** Always reference the full ATA code (e.g., 25-20-01) in requirements, design documents, and test cases.
4. **Navigation:** Use this index to locate the correct subject folder before creating or updating documentation.

---

**For narrative overview, see:** [README.md](./README.md)
