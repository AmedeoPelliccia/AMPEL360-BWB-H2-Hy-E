# ATA 20: Standard Practices - Airframe

**TECHNOLOGY CHAPTER STATUS:** ATA 20 establishes the foundational standard practices, techniques, materials, and procedures for all airframe maintenance, repair, and modification activities on the AMPEL360 aircraft. This chapter serves as the "how-to" reference for all structural work.

## Scope and Structure
This chapter documents all standard practices for airframe maintenance, including:
- **Composite Repair:** Carbon fiber laminate repair techniques
- **Materials and Processes:** Approved materials, adhesives, resins
- **Fastening Methods:** Riveting, bolting, bonding techniques
- **Sealing and Bonding:** Fuel tank sealing, structural bonding
- **Surface Treatment:** Cleaning, painting, protective coatings
- **Inspection Techniques:** Visual, NDT, damage assessment
- **Torque Requirements:** Standard torque values for fasteners
- **Special Processes:** Cryogenic temperature considerations, hydrogen compatibility
- **Lightning Strike Protection:** LSP system repair and verification
- **Environmental Protection:** Corrosion prevention, moisture control

## The 14-Folder Skeleton
Every 6-digit component within this chapter represents a standard practice, procedure, or specification. Each component is managed through the full lifecycle skeleton to ensure requirements traceability, procedure validation, training curriculum development, and regulatory compliance.

## Regulatory Framework

### Certification Requirements
- **CS-25.603:** Materials (general requirements)
- **CS-25.605:** Fabrication Methods
- **CS-25.607:** Fasteners
- **CS-25.609:** Protection of Structure
- **CS-25.613:** Material Strength Properties and Design Values
- **CS-25 Appendix F:** Part I - Structural Integrity
- **FAA AC 43.13-1B:** Acceptable Methods, Techniques, and Practices - Aircraft Inspection and Repair
- **FAA AC 20-107B:** Composite Aircraft Structure

### Industry Standards
- **ATA iSpec 2200 Chapter 20:** Standard airframe practices
- **SAE AMS Specifications:** Aerospace Material Specifications
- **ASTM Standards:** Material testing and characterization
- **NCAMP (National Center for Advanced Materials Performance):** Composite repair guidelines
- **CMH-17 (Composite Materials Handbook):** Design and test standards
- **CACRC (Commercial Aircraft Composite Repair Committee):** Repair guidelines
- **MIL-HDBK-17:** Composite materials (historical reference)

### Composite-Specific Standards
- **SAE AIR4844:** Damage Tolerance and Fatigue Evaluation of Structure (Composite)
- **SAE ARP5089:** Repair of Composite Aircraft Structure
- **ASTM D5961:** Bearing Response of Polymer Matrix Composite Laminates
- **ASTM D7136:** Impact Resistance of Polymer Matrix Composites
- **ASTM D7137:** Compressive Residual Strength Properties (CAI)

## AMPEL360 Unique Characteristics

### 1. **Carbon Fiber Composite BWB Structure**
The AMPEL360 employs advanced carbon fiber reinforced polymer (CFRP) construction:

**Primary Structure Material:**
- **Material System:** Hexcel HexPly M21E/IMA (toughened epoxy prepreg)
- **Fiber Type:** Intermediate modulus carbon fiber (tensile modulus 290 GPa)
- **Matrix:** Toughened epoxy resin (service temp -55°C to +120°C)
- **Cure Cycle:** 180°C autoclave cure, 7 bar pressure, 2 hours dwell
- **Laminate Density:** 1,550 kg/m³ (vs. aluminum 2,780 kg/m³)
- **Typical Laminate Thickness:** 4-20mm (BWB primary structure)

**BWB-Specific Structural Elements:**
- **Center Body Skins:** 10-15mm thick composite sandwich (carbon face sheets + Nomex honeycomb core)
- **Wing Skins:** 6-12mm thick solid laminate (outer wing) to sandwich (center wing)
- **Spar Caps:** Unidirectional carbon fiber (IM fiber, 60% fiber volume fraction)
- **Rib/Frame Structures:** Fabric prepreg or resin transfer molding (RTM)
- **Composite-Metal Transitions:** Hybrid joints at landing gear attachments, door frames

**Advantages vs. Aluminum:**
- **Weight Savings:** 20-25% lighter than equivalent aluminum structure
- **Fatigue Resistance:** No crack propagation (damage-tolerant by delamination)
- **Corrosion Immunity:** No galvanic corrosion (but moisture absorption concern)
- **Complex Shapes:** BWB blended contours easier to manufacture with composites

**Challenges:**
- **Impact Sensitivity:** Barely Visible Impact Damage (BVID) can hide internal delamination
- **Repair Complexity:** Requires autoclave or heated bonding equipment
- **Moisture Sensitivity:** Epoxy absorbs moisture (affects hot/wet properties)
- **Lightning Strike:** Requires dedicated lightning strike protection (LSP) system
- **Cryogenic Effects:** LH₂ tank proximity creates cold-soaked structure (-100°C localized)

### 2. **Cryogenic Temperature Effects**
LH₂ fuel at -253°C affects adjacent structure:

**Cold Zone Definition:**
- **Primary Cold Zone:** Within 500mm of LH₂ tank outer vessel
- **Secondary Cold Zone:** 500-1000mm from tank (thermal gradient)
- **Steady-State Temperature:** -100°C to -20°C (varies with distance from tank)

**Material Property Changes:**
**Carbon Fiber Composite (CFRP):**
- **Strength:** Increases 10-15% at cryogenic temperatures (fiber-dominated)
- **Modulus:** Increases 5% (stiffens)
- **Toughness:** Decreases 20% (matrix embrittlement)
- **Thermal Contraction:** 1.5 mm/m from +20°C to -100°C

**Aluminum Alloys (fittings, inserts):**
- **Strength:** Increases significantly (2024-T3: +30% yield strength)
- **Ductility:** Decreases (brittle at extreme cold)
- **Thermal Contraction:** 2.3 mm/m from +20°C to -100°C

**Implications for Repair:**
- Cold-soaked structure must warm to ambient before repair (6-hour minimum)
- Special low-temperature epoxies required for cold-zone repairs (cure at 0°C capable)
- Thermal cycling testing mandatory for all cold-zone repairs (100 cycles -100°C to +80°C)

### 3. **Hydrogen Embrittlement Considerations**
Hydrogen gas can embrittle high-strength metals:

**Susceptible Materials:**
- **High-Strength Steels:** AISI 4340 (landing gear), 17-4PH (fasteners)
- **Titanium Alloys:** Ti-6Al-4V (primary structure fittings)
- **Aluminum Alloys:** 7075-T6 (limited susceptibility, but monitored)

**Mitigation:**
- **Material Selection:** Use lower-strength steels (<1,200 MPa tensile) in H₂ zones
- **Plating Restrictions:** No cadmium plating in H₂ zones (promotes embrittlement)
- **Inspection:** Enhanced ultrasonic inspection for fittings near H₂ tank (every C-Check)

**Repair Considerations:**
- Welding prohibited on high-strength steels in H₂ zones (use bolted repairs)
- Fasteners in H₂ zones must be A286 stainless steel (resistant to embrittlement)
- Hydrogen bake-out procedure for any metallic repairs in H₂ proximity (200°C, 4 hours)

### 4. **Lightning Strike Protection (LSP)**
Composite structure requires embedded LSP system:

**LSP System Components:**
- **Expanded Copper Foil (ECF):** 0.1mm thick mesh embedded in outer ply
- **Aluminum Flame-Spray (AFS):** Thin aluminum coating on composite surfaces
- **Lightning Diverter Strips:** Copper strips along leading edges, tips, antennas
- **Bonding Jumpers:** Electrical continuity between structural elements

**LSP Repair Requirements:**
- Any repair >25mm diameter must restore LSP continuity
- Resistance measurement: <2.5 milliohms across repair (per SAE ARP5414)
- Copper mesh must overlap 50mm minimum with existing LSP
- Post-repair lightning strike test (simulated strike, 200 kA peak current)

### 5. **Composite-to-Metal Hybrid Joints**
BWB structure includes critical metal fittings:

**Hybrid Joint Locations:**
- **Landing Gear Attachments:** Titanium fittings bonded into composite structure
- **Door Frames:** Aluminum extrusions bonded to composite fuselage
- **Propulsor Mounts:** Steel pylon attachment fittings
- **Wing Attachment Points:** Main spar titanium splice fittings

**Joint Design:**
- **Bonding:** Structural adhesive (Cytec FM 300 film adhesive, 120°C cure)
- **Mechanical Fastening:** Titanium or A286 bolts as backup load path
- **Corrosion Barrier:** Glass fiber isolation ply (prevents galvanic corrosion)

**Repair Challenges:**
- Disbonding at composite-metal interface requires rebond (not field-repairable)
- Fastener holes in composite must be pristine (no oversizing allowed)
- Titanium fittings cannot be welded (precipitation hardening disrupted)

### 6. **Moisture Control**
Epoxy matrix absorbs moisture, affecting properties:

**Moisture Absorption:**
- **Saturation Level:** 1.5% by weight (in 100% humidity, 70°C, 1,000 hours)
- **Effect on Tg (Glass Transition):** Decreases from 180°C to 150°C (wet)
- **Effect on Compression Strength:** Decreases 10% (hot/wet conditions)

**Drying Requirements:**
- Composite parts must be dried before repair if moisture >0.5%
- Drying cycle: 80°C, dry air circulation, 24 hours minimum
- Moisture measurement: Microwave moisture meter (non-destructive)

## Standard Practices Categories

### 1. **Materials and Processes (20-10)**
Standard materials, adhesives, sealants, and process specifications:
- Approved composite prepregs and repair materials
- Structural adhesives (film adhesives, paste adhesives)
- Sealants (fuel tank, environmental)
- Paints and protective coatings
- Material storage and handling (freezer storage for prepregs)

### 2. **Fastening (20-20)**
Methods for mechanical fastening:
- Riveting (solid rivets, blind rivets)
- Bolting (torque requirements, locking methods)
- Composite fastening (hole preparation, torque limits)
- Fastener materials and specifications
- Hole repair and oversizing procedures

### 3. **Bonding and Sealing (20-30)**
Adhesive bonding and sealing practices:
- Surface preparation (abrading, solvent cleaning, primer application)
- Adhesive application (film adhesive layup, paste adhesive application)
- Cure cycles (autoclave, vacuum bag, heated blanket)
- Bond quality inspection (tap test, ultrasonic C-scan)
- Sealant application (faying surfaces, fasteners, interfaces)

### 4. **Composite Repair (20-40)**
Techniques specific to composite structure repair:
- Damage assessment (visual inspection, NDT techniques)
- Scarfing (taper sanding to prepare repair area)
- Patch design (ply orientation matching, taper ratios)
- Vacuum bag repair (portable vacuum pump systems)
- Post-repair inspection and testing

### 5. **Surface Treatment (20-50)**
Cleaning, painting, and protective coatings:
- Composite surface cleaning (avoid solvents that attack matrix)
- Paint system application (primer, topcoat)
- Paint removal (chemical stripping vs. mechanical sanding)
- Protective coatings (erosion protection, anti-static coatings)
- Markings and placards (paint vs. decals)

### 6. **Inspection Techniques (20-60)**
Non-destructive testing and damage assessment:
- Visual inspection standards (lighting, magnification)
- Tap testing (coin tap, mechanical tap hammer)
- Ultrasonic inspection (pulse-echo, through-transmission, phased array)
- Thermography (IR imaging for delamination detection)
- X-ray/CT scanning (internal damage mapping)
- Moisture measurement (microwave moisture meter)

### 7. **Corrosion Control (20-70)**
Although composites don't corrode, metal components do:
- Galvanic corrosion prevention (isolation, protective coatings)
- Corrosion inspection procedures (metal fittings, fasteners)
- Corrosion removal and treatment
- Corrosion-resistant materials selection
- Environmental protection for metal-composite interfaces

### 8. **Torque Requirements (20-80)**
Standard torque values for all fastener types:
- Torque tables for titanium bolts (dry vs. lubricated)
- Torque limits for composite fasteners (prevent bearing failure)
- Torque wrench calibration requirements
- Marking conventions for torqued fasteners
- Re-torque procedures (if fastener loosens)

### 9. **Special Processes (20-90)**
Unique processes for AMPEL360:
- Cryogenic zone repair procedures
- Hydrogen compatibility verification
- Lightning strike protection restoration
- Large-area vacuum bagging techniques
- Heated blanket cure procedures (portable equipment)

## Composite Repair Philosophy

### Design Principles
**Strength Recovery:**
- **Objective:** Restore 100% of original structural strength
- **Method:** Match original ply count and orientation
- **Verification:** Coupon testing (tension, compression, bearing, shear)

**Stiffness Matching:**
- **Critical for BWB:** Stiffness mismatch causes load redistribution
- **Method:** Match laminate thickness and fiber volume fraction
- **Tolerance:** Repair stiffness within ±10% of original

**Aerodynamic Smoothness:**
- **External Repairs:** Must maintain original contour (±0.5mm surface profile)
- **Method:** Fill with low-density filler, sand smooth, apply surfacing film
- **Verification:** Template check or laser scan

### Repair Categories
**Category 1: Cosmetic Repair**
- **Damage:** Paint scratches, surface abrasion (depth <0.2mm)
- **Repair:** Clean, sand, repaint (no structural repair)
- **Approval:** Line maintenance (mechanic sign-off)

**Category 2: Minor Structural Repair**
- **Damage:** Impact damage <25mm diameter, <2mm deep
- **Repair:** Fill with paste adhesive, sand, restore LSP, paint
- **Approval:** Structural repair manual (SRM) procedure, inspector sign-off
- **Time:** 4-8 hours (single shift)

**Category 3: Major Structural Repair**
- **Damage:** Impact damage 25-100mm diameter, through-thickness penetration
- **Repair:** Scarf sand, apply composite patch (vacuum bag cure)
- **Approval:** SRM procedure, structural engineering review
- **Time:** 2-3 days (multi-shift with cure cycle)

**Category 4: Non-Standard Repair**
- **Damage:** Large damage >100mm, critical structure, new damage mode
- **Repair:** Custom engineering analysis, possibly test validation
- **Approval:** OEM engineering disposition, certification authority approval
- **Time:** Weeks to months (engineering + fabrication + testing)

## Typical Composite Repair Procedure

### Step-by-Step Process (Category 3 Repair Example)

**Step 1: Damage Assessment (1 hour)**
1. Visual inspection (document with photos, measurements)
2. Tap test (define delamination extent with mechanical tap hammer)
3. Ultrasonic C-scan (if available, map internal damage)
4. Mark repair boundary (50mm beyond visible damage minimum)

**Step 2: Surface Preparation (2 hours)**
1. Mask area around repair (protect surrounding paint)
2. Sand to remove paint (80-grit sandpaper, hand sanding)
3. Clean with solvent (isopropyl alcohol, lint-free wipes)
4. Scarf sand damaged area (30:1 taper ratio = 1mm depth per 30mm lateral)
5. Final cleaning (solvent wipe, dry with compressed air)

**Step 3: Patch Fabrication (4 hours)**
1. Determine ply count and orientation (match original laminate)
2. Cut prepreg plies to size (stagger ply edges for taper)
3. Apply release film to tool plate
4. Layup plies on tool (consolidate with hand roller)
5. Cover with peel ply and breather
6. Vacuum bag assembly (seal edges with tacky tape)

**Step 4: Cure Cycle (8 hours)**
1. Apply vacuum (25-28 inches Hg, verify no leaks)
2. Heat to cure temperature (120°C for FM 300 adhesive)
3. Hold at temperature (2 hours dwell)
4. Cool to <60°C before removing vacuum
5. Remove bagging materials, inspect cured patch

**Step 5: Secondary Bonding (if required) (1 hour)**
1. Abrade patch and parent structure bonding surfaces (240-grit)
2. Solvent wipe (isopropyl alcohol)
3. Apply primer (BR-127 corrosion inhibiting primer)
4. Apply film adhesive (FM 300, 0.15mm thickness)
5. Position patch in repair cavity

**Step 6: Cure and Consolidation (8 hours)**
1. Apply peel ply and breather over patch
2. Vacuum bag (same as Step 4)
3. Heat cure (120°C, 2 hours)
4. Cool and remove bagging

**Step 7: Contouring and Finishing (3 hours)**
1. Remove peel ply (reveals textured surface)
2. Fill low spots with paste filler (Hysol EA 9394)
3. Sand smooth (match original contour, 120-grit → 220-grit progression)
4. Apply surfacing film (if required for aerodynamic smoothness)

**Step 8: LSP Restoration (2 hours)**
1. Apply copper mesh over repair area (50mm overlap with existing LSP)
2. Bond mesh with conductive adhesive
3. Measure resistance (must be <2.5 milliohms)
4. Apply protective coating over mesh

**Step 9: Painting (4 hours + dry time)**
1. Mask repair area (protect surrounding finish)
2. Apply primer (epoxy primer, 2 coats)
3. Apply base coat (color match to aircraft livery)
4. Apply clear coat (UV protection)
5. Remove masking, inspect finish

**Step 10: Final Inspection and Documentation (1 hour)**
1. Visual inspection (smooth contour, good paint match)
2. Tap test (verify no delamination introduced during repair)
3. Ultrasonic inspection (if required by SRM)
4. Complete repair record (photos, dimensions, materials used)
5. Logbook entry and inspector sign-off

**Total Time:** ~34 hours (4-5 days with cure cycles)

## Material Storage Requirements

### Composite Prepreg Storage
**Hexcel HexPly M21E/IMA Prepreg:**
- **Storage Temperature:** -18°C (0°F) freezer
- **Shelf Life:** 12 months at -18°C, 10 days at room temperature (out-time)
- **Thaw Time:** 12 hours at room temperature before use
- **Out-Time Tracking:** Log every removal from freezer (date, duration)
- **Packaging:** Keep in sealed foil bag (moisture barrier) until use

### Adhesives
**FM 300 Film Adhesive:**
- **Storage:** -18°C freezer (same as prepreg)
- **Shelf Life:** 18 months at -18°C, 30 days at room temperature
- **Thaw Time:** 8 hours at room temperature

**Hysol EA 9394 Paste Adhesive:**
- **Storage:** Room temperature (15-25°C)
- **Shelf Life:** 12 months from manufacture
- **Working Time:** 45 minutes at 25°C (decreases at higher temperature)

### Sealants
**PR-1440 Fuel Tank Sealant:**
- **Storage:** Cool, dry location (10-25°C)
- **Shelf Life:** 6 months from manufacture
- **Working Time:** 4 hours at 25°C
- **Cure Time:** 24 hours at 25°C (accelerated at higher temperature)

## Quality Control

### Repair Quality Verification
**Visual Inspection:**
- Surface smooth (no voids, wrinkles, foreign objects)
- Edges feathered (smooth transition to parent structure)
- No contamination (oil, grease, moisture)

**Tap Test:**
- Performed over entire repair area + 50mm beyond
- Solid, crisp sound indicates good consolidation
- Dull, dead sound indicates delamination (reject repair)

**Ultrasonic Inspection:**
- Pulse-echo or through-transmission technique
- Acceptance: No indications >6mm diameter (per SRM)
- Document with C-scan image (archived with repair record)

**Resistance Measurement (LSP):**
- Four-wire Kelvin measurement (eliminates lead resistance)
- Acceptance: <2.5 milliohms across repair
- Measure at 3 locations, record all values

### Repair Approval Authority
**Line Maintenance (Category 1):**
- Mechanic with Type Rating
- Inspector sign-off (dual inspection)

**Structural Repair Manual (Category 2-3):**
- Mechanic with composite repair certification
- Structural Inspector sign-off (Level 2 minimum)
- Engineering review if damage exceeds SRM limits

**Engineering Disposition (Category 4):**
- Structural Engineering analysis and design
- Prototype repair and testing (coupon or component level)
- Certification Authority approval (EASA/FAA)
- Incorporation via Service Bulletin (mandatory or optional)

## Integration with Other Chapters

### Data Flows
```
ATA 20 (Standard Practices)
    ↓ Repair Procedures → ATA 51-57 (Structures - specific repairs)
    ↓ Material Specs → ATA 06 (Dimensions - material properties)
    ↓ Inspection Methods → ATA 05 (Maintenance Checks - inspection tasks)
    ↓ Torque Values → All chapters with fasteners
    ↓ NDT Techniques → ATA 51-57 (damage tolerance inspections)
```

### Cross-References
- **ATA 05-30:** Structural Inspection Program (uses ATA 20 NDT methods)
- **ATA 06-20:** Surface Areas (material properties affect weight calculations)
- **ATA 12-50:** Fluid Servicing (composite protection during servicing)
- **ATA 28-30:** LH₂ Tank (cryogenic effects on adjacent structure)
- **ATA 51-57:** Structures (all structural repairs reference ATA 20)

## Training and Certification

### Composite Repair Technician Certification
**Prerequisites:**
- Aircraft Maintenance Technician License (national authority)
- Minimum 2 years experience in aircraft maintenance
- EASA Part-66 Cat B1/B2 (or national equivalent)

**Training Curriculum (80 hours):**
1. Composite Materials Fundamentals (8 hours)
2. Damage Assessment and NDT (16 hours)
3. Surface Preparation and Scarfing (8 hours)
4. Patch Fabrication and Layup (16 hours)
5. Vacuum Bagging and Cure Cycles (16 hours)
6. Lightning Strike Protection Repair (8 hours)
7. Quality Control and Inspection (8 hours)

**Practical Examination:**
- Perform Category 2 repair on sample panel (8 hours)
- Repair inspected and tested (destructive test)
- Pass/Fail based on repair quality

**Recertification:** Every 24 months (16-hour recurrent training)

### AMPEL360 Type-Specific Training
**Additional Topics (24 hours):**
- BWB structure unique features
- Cryogenic zone repair procedures
- Hydrogen compatibility requirements
- Large-area vacuum bag techniques

## Document Hierarchy
```
ATA 20 (This Chapter)
├── Standard Practices Manual (SPM)
├── Composite Repair Manual (CRM)
├── Material and Process Specifications (MPS)
├── Approved Materials List (AML)
├── Torque Tables (all fastener types)
├── NDT Procedures Manual
├── Repair Training Curriculum
└── Quality Control Checklists
```

## Revision Control
Changes to ATA 20 procedures require:
1. **Engineering Validation:** Test new repair procedure on coupons
2. **Safety Assessment:** Verify repair maintains structural integrity
3. **Regulatory Approval:** EASA/FAA review for major changes
4. **Training Update:** Revise training materials, notify certified technicians
5. **Service Bulletin:** Issue SB if affects existing fleet repairs

## Future Enhancements
- **Automated Fiber Placement (AFP):** In-situ repair using robotic fiber placement
- **3D-Printed Composite Patches:** Additive manufacturing for complex geometries
- **Self-Healing Composites:** Matrix resin with healing agents (research phase)
- **Augmented Reality Repair Guidance:** AR headset overlays repair instructions on actual structure
- **Non-Destructive Cure Monitoring:** Real-time cure state monitoring (dielectric sensors)
