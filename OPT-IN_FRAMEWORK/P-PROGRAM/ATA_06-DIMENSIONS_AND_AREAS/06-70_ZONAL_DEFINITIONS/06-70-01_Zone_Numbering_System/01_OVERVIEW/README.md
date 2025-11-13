---
title: Overview: 06-70-01 - Zone Numbering System
identifier: 06-70-01-001A
version: 0.1
author: Amedeo Pelliccia
status: Approved
classification: Technical
scope: Dimensions And Areas architecture and integration with related subsystems
created_at: 2025-11-13
next_review: 2026-05-12
compliance:
  - ATA iSpec 2200
  - S1000D
  - AMPEL360 OPT-IN Framework
---

<!-- GENCCC_STATUS: pending -->
<!-- GENCCC_SCOPE: system_description, architecture, integration -->

# Overview: 06-70-01 - Zone Numbering System


> 🔗 **Linked Verification Matrix:** [../../07_V_AND_V/06-70-01-001A_Traceability_Matrix.csv](../../07_V_AND_V/06-70-01-001A_Traceability_Matrix.csv)

## Purpose
This component establishes the standardized zone numbering system for the AMPEL360 aircraft, enabling systematic identification of maintenance zones and access points per ATA 100 specifications.

## Zone Numbering Standard

### ATA 100 Zone Numbering System
The AMPEL360 follows ATA iSpec 2200 zone numbering conventions, adapted for the Blended Wing Body (BWB) configuration:

**Zone Format:** XXX (three-digit code)
- **First Digit (Hundreds):** Major aircraft section
- **Second Digit (Tens):** Subsection within major section
- **Third Digit (Units):** Specific zone within subsection

### AMPEL360 Zone Structure

#### Major Sections (First Digit)
| Zone Range | Section | Description |
|------------|---------|-------------|
| **100-199** | Nose Section | Forward fuselage, cockpit, avionics |
| **200-299** | Forward Center Body | Forward cabin, forward cargo |
| **300-399** | Center Body | Main cabin, LH₂ tanks, systems |
| **400-499** | Propulsor Zones | Engine installations, nacelles |
| **500-599** | Aft Center Body | Aft cabin, APU, tail cone |
| **600-699** | Lower Fuselage | Belly fairing, landing gear, utilities |
| **700-799** | Left Wing | Left wing structure, systems |
| **800-899** | Right Wing | Right wing structure, systems |
| **900-999** | Aft Section | Tail cone, aft fuselage |

## Detailed Zone Breakdown

### 100 Series: Nose Section
**Zone 100-110: Cockpit and Flight Deck**
- **Zone 110:** Windshield and forward pressure bulkhead
- **Zone 111:** Captain's side panel
- **Zone 112:** First Officer's side panel
- **Zone 113:** Overhead panel
- **Zone 114:** Center pedestal
- **Zone 115:** Flight deck floor

**Zone 120-130: Nose Avionics Bay**
- **Zone 121:** Forward equipment rack (left)
- **Zone 122:** Forward equipment rack (right)
- **Zone 123:** Weather radar compartment
- **Zone 124:** Forward electronics cooling bay

**Zone 140-150: Nose Landing Gear Bay**
- **Zone 141:** Nose gear wheel well
- **Zone 142:** Nose gear doors (left)
- **Zone 143:** Nose gear doors (right)
- **Zone 144:** Nose gear hydraulics compartment

### 200 Series: Forward Center Body
**Zone 210-220: Forward Cabin**
- **Zone 211:** Forward cabin left side (rows 1-10)
- **Zone 212:** Forward cabin right side (rows 1-10)
- **Zone 213:** Forward galley (left)
- **Zone 214:** Forward galley (right)
- **Zone 215:** Forward lavatory cluster

**Zone 230-240: Forward Cargo Hold**
- **Zone 231:** Forward cargo compartment (left)
- **Zone 232:** Forward cargo compartment (right)
- **Zone 233:** Forward cargo door (left)
- **Zone 234:** Forward cargo door (right)

### 300 Series: Center Body (Main Section)
**Zone 310-320: Main Cabin**
- **Zone 311:** Main cabin left side (rows 11-30)
- **Zone 312:** Main cabin center section (rows 11-30)
- **Zone 313:** Main cabin right side (rows 11-30)
- **Zone 314:** Mid galley (left)
- **Zone 315:** Mid galley (right)
- **Zone 316:** Mid lavatory cluster

**Zone 330-340: Main Systems Bay**
- **Zone 331:** Main electronics bay (left)
- **Zone 332:** Main electronics bay (right)
- **Zone 333:** ECS equipment bay
- **Zone 334:** Hydraulic equipment bay

**Zone 350-360: LH₂ Tank Zone**
- **Zone 351:** LH₂ tank #1 (forward left)
- **Zone 352:** LH₂ tank #2 (forward right)
- **Zone 353:** LH₂ tank #3 (center left)
- **Zone 354:** LH₂ tank #4 (center right)
- **Zone 355:** LH₂ tank #5 (aft left)
- **Zone 356:** LH₂ tank #6 (aft right)
- **Zone 357:** LH₂ fuel cell bay

**Zone 370-380: Main Landing Gear Bay**
- **Zone 371:** Main gear wheel well (left)
- **Zone 372:** Main gear wheel well (right)
- **Zone 373:** Main gear doors (left)
- **Zone 374:** Main gear doors (right)

### 400 Series: Propulsor Zones
**Zone 410-420: Left Propulsor**
- **Zone 411:** Left propulsor nacelle
- **Zone 412:** Left propulsor inlet
- **Zone 413:** Left propulsor fan section
- **Zone 414:** Left propulsor turbine section
- **Zone 415:** Left propulsor exhaust
- **Zone 416:** Left propulsor pylon

**Zone 430-440: Right Propulsor**
- **Zone 431:** Right propulsor nacelle
- **Zone 432:** Right propulsor inlet
- **Zone 433:** Right propulsor fan section
- **Zone 434:** Right propulsor turbine section
- **Zone 435:** Right propulsor exhaust
- **Zone 436:** Right propulsor pylon

### 500 Series: Aft Center Body
**Zone 510-520: Aft Cabin**
- **Zone 511:** Aft cabin left side (rows 31-40)
- **Zone 512:** Aft cabin right side (rows 31-40)
- **Zone 513:** Aft galley
- **Zone 514:** Aft lavatory cluster

**Zone 530-540: APU and Aft Systems**
- **Zone 531:** APU compartment
- **Zone 532:** APU fire suppression system
- **Zone 533:** Aft equipment bay

**Zone 550-560: Aft Cargo Hold**
- **Zone 551:** Aft cargo compartment
- **Zone 552:** Bulk cargo compartment
- **Zone 553:** Aft cargo door

### 600 Series: Lower Fuselage
**Zone 610-620: Belly Fairing**
- **Zone 611:** Forward belly fairing
- **Zone 612:** Center belly fairing
- **Zone 613:** Aft belly fairing

**Zone 630-640: Utilities Bay**
- **Zone 631:** Water/waste system compartment
- **Zone 632:** Battery compartment
- **Zone 633:** Auxiliary systems bay

### 700 Series: Left Wing
**Zone 710-720: Left Wing Root**
- **Zone 711:** Left wing root leading edge
- **Zone 712:** Left wing root main box
- **Zone 713:** Left wing root trailing edge

**Zone 730-740: Left Wing Mid-Span**
- **Zone 731:** Left wing mid-span leading edge
- **Zone 732:** Left wing mid-span main box
- **Zone 733:** Left wing mid-span trailing edge

**Zone 750-760: Left Wing Tip**
- **Zone 751:** Left wing tip leading edge
- **Zone 752:** Left wing tip main box
- **Zone 753:** Left wing tip trailing edge
- **Zone 754:** Left winglet

### 800 Series: Right Wing
**Zone 810-820: Right Wing Root**
- **Zone 811:** Right wing root leading edge
- **Zone 812:** Right wing root main box
- **Zone 813:** Right wing root trailing edge

**Zone 830-840: Right Wing Mid-Span**
- **Zone 831:** Right wing mid-span leading edge
- **Zone 832:** Right wing mid-span main box
- **Zone 833:** Right wing mid-span trailing edge

**Zone 850-860: Right Wing Tip**
- **Zone 851:** Right wing tip leading edge
- **Zone 852:** Right wing tip main box
- **Zone 853:** Right wing tip trailing edge
- **Zone 854:** Right winglet

### 900 Series: Aft Section
**Zone 910-920: Tail Cone**
- **Zone 911:** Upper tail cone
- **Zone 912:** Lower tail cone
- **Zone 913:** Aft pressure bulkhead

**Zone 930-940: Aft Fairing**
- **Zone 931:** Aft fairing upper surface
- **Zone 932:** Aft fairing lower surface

## Zone Access and Environment

### Access Classification
| Access Type | Definition | Example Zones |
|-------------|------------|---------------|
| **Type 1:** Daily access | Interior zones accessible without tools | 211-213 (cabin) |
| **Type 2:** Periodic access | Requires panel removal (hand tools) | 331-334 (equipment bays) |
| **Type 3:** Infrequent access | Requires major disassembly | 371-372 (gear bays) |
| **Type 4:** Special access | Requires scaffolding/lifts | 411-416 (propulsors) |
| **Type 5:** Restricted access | Safety certification required | 351-357 (LH₂ zones) |

### Environmental Conditions
| Zone Range | Environment | Considerations |
|------------|-------------|----------------|
| 100-199 | Pressurized, climate controlled | Avionics cooling |
| 200-299 | Pressurized, climate controlled | Passenger comfort |
| 300-399 | Mixed (pressurized cabin + unpressurized tanks) | LH₂ cryogenic |
| 400-499 | Unpressurized, high temperature | Engine hot zones |
| 500-599 | Pressurized, climate controlled | APU heat management |
| 600-699 | Unpressurized, ambient | Weather protection |
| 700-899 | Unpressurized, ambient | Fuel tanks, systems |
| 900-999 | Unpressurized, ambient | Minimal systems |

## Zone Identification Marking

### Physical Markings
- **Zone Placards:** Permanent placards at zone boundaries (yellow text on black)
- **Zone Stencils:** Stenciled zone numbers on structure (50mm high characters)
- **Access Panels:** Zone number marked on each access panel
- **Maintenance Platforms:** Zone identification at platform entry points

### Digital Zone Identification
- **AR Overlay:** Augmented reality zone identification via tablet/smart glasses
- **Digital Manuals:** Interactive 3D models with zone highlighting
- **Maintenance Planning:** Work packages organized by zone

## Interface with Other ATA Chapters

### ATA 05: Periodic Maintenance Checks
- Zone-based inspection schedules
- Zonal inspection procedures

### ATA 12: Servicing
- Zone-based servicing points
- Service panel locations by zone

### ATA 24-49: Systems
- System routing through zones
- Zone environmental conditions for equipment

## Document Status
**Status:** Approved  
**Last Review:** 2025-11-01  
**Next Review:** 2026-05-01
