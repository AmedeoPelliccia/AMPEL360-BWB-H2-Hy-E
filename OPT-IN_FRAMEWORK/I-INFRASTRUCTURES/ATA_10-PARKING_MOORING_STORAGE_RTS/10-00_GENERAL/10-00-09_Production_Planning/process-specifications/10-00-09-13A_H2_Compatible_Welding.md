# 10-00-09-13A H2 Compatible Welding Process Specification

## Document Information

- **Document ID**: 10-00-09-13A
- **Title**: Hydrogen Compatible Welding Process Specification
- **Version**: 1.0 (Revision A)
- **Date**: 2025-12-10
- **Status**: Draft
- **Category**: Process Specification - Welding
- **ATA Chapter**: 10 - Parking, Mooring, Storage & RTS
- **NADCAP Code**: AC7114/1 (Fusion Welding)

## Purpose

This specification defines welding procedures, qualification requirements, and quality controls for welds on components intended for hydrogen (H2) service in ATA 10 systems. Welds must prevent hydrogen embrittlement, ensure leak-tightness, and maintain structural integrity throughout the operating life.

## Scope

This specification applies to:
- All pressure boundary welds in H2 service
- Structural welds on H2 system components
- Repair welds on qualified H2 components

## Applicable Standards

- **AWS D17.1**: Specification for Fusion Welding for Aerospace Applications
- **ASME B31.12**: Hydrogen Piping and Pipelines
- **ASME Section IX**: Welding and Brazing Qualifications
- **SAE AS6968**: Hydrogen Aircraft Systems Requirements
- **ISO/TR 15916**: Basic Considerations for the Safety of Hydrogen Systems

## Approved Welding Processes

### 1. Gas Tungsten Arc Welding (GTAW/TIG)

**Primary process for H2 components**

#### Orbital GTAW (Automated)
- **Application**: Tube-to-fitting welds, repetitive joints
- **Advantages**: Consistent quality, full penetration, minimal heat input
- **Equipment**: Automated orbital welding head with programmable controls

#### Manual GTAW
- **Application**: Repair, complex geometry, one-off joints
- **Equipment**: DC power supply with high-frequency start
- **Welder Qualification**: Per AWS D17.1 and ASME Section IX

### 2. Electron Beam Welding (EBW)

- **Application**: Thick sections, dissimilar materials, vacuum-tight joints
- **Advantages**: Deep penetration, narrow HAZ, no filler contamination
- **Equipment**: Vacuum chamber EBW system (typically outsourced)

### 3. Laser Welding

- **Application**: Precision welds, thin-wall components
- **Advantages**: Minimal heat input, controlled penetration
- **Equipment**: Nd:YAG or fiber laser welding system

## Base Materials

### Approved Materials for H2 Service

| Material | Specification | Notes |
|----------|---------------|-------|
| 316L Stainless Steel | AMS 5507, AMS 5524 | Most common for H2 service |
| 304L Stainless Steel | AMS 5511 | Alternative to 316L |
| Inconel 625 | AMS 5666 | High-temperature applications |
| Inconel 718 | AMS 5662 | High-strength applications |
| Elgiloy | AMS 5876 | Springs, bellows |

### Prohibited Materials

- High-carbon steels (>0.30% C)
- Cast iron
- Zinc-plated components
- Cadmium-plated components

## Filler Materials

### GTAW Filler Metals

| Base Material | Filler Metal | Specification |
|---------------|--------------|---------------|
| 316L SS | ER316L | AWS A5.9 |
| 304L SS | ER308L | AWS A5.9 |
| Inconel 625 | ERNiCrMo-3 | AWS A5.14 |
| Inconel 718 | ERNiFeCr-2 | AWS A5.14 |

**Filler Metal Requirements**:
- Certified chemical composition (mill certs required)
- Clean, oxide-free surface
- Store in dry, clean environment
- Re-clean if exposed to contamination

## Shielding Gas

**Primary Gas**: Argon (99.999% purity minimum)
- Grade: Welding grade or ultra-high purity (UHP)
- Moisture: <3 ppm
- Oxygen: <2 ppm

**Alternative**: Helium or Argon-Helium mix (for specific applications)

**Back Purge Gas** (for full-penetration welds):
- Argon (99.999% purity)
- Purge to <50 ppm oxygen before welding
- Maintain purge during welding and cool-down

## Pre-Weld Requirements

### Material Preparation

1. **Cleaning**:
   - Solvent cleaning (isopropyl alcohol or acetone)
   - Mechanical cleaning (stainless steel brush, abrasive, or machining)
   - Remove all oils, oxides, scale, and contaminants within 1" of weld area

2. **Fit-Up**:
   - Gap tolerance: Typically 0.000" to 0.010" for tube butt welds
   - Alignment: Concentricity within 10% of wall thickness
   - No high-low condition (offset <10% of wall thickness)

3. **Joint Design**:
   - Full penetration required for pressure boundaries
   - Backing rings prohibited (creates crevice for hydrogen)
   - Consumable inserts allowed if qualified

### Welder/Operator Qualification

- Qualified per AWS D17.1 and/or ASME Section IX
- Qualification test coupons destructively tested:
  - Visual inspection
  - Radiographic or ultrasonic testing
  - Tensile test (meets base material minimum)
  - Guided bend test (no cracks)
  - Charpy impact test of weld and HAZ at -196°C (for cryogenic applications)

- Requalification:
  - Every 6 months if not welding
  - When changing essential variables (material, process, position, etc.)

## Welding Procedure Specifications (WPS)

Each weld configuration requires a qualified WPS documenting:
- Base material(s) and filler metal
- Welding process (GTAW, EBW, etc.)
- Joint design and fit-up tolerances
- Preheat and interpass temperature (if applicable)
- Welding parameters (current, voltage, travel speed, flow rates)
- Post-weld treatment requirements
- Inspection and testing requirements

### Welding Parameters (Typical for 316L SS)

**Orbital GTAW (tube-to-fitting, 0.035" wall)**:
- Current: 50-70 A (DCEN)
- Voltage: 10-12 V
- Travel Speed: 6-10 IPM
- Shielding Gas Flow: 15-20 CFH
- Back Purge Flow: 10-15 CFH

## Welding Execution

### Environmental Controls

- **Temperature**: 50°F to 100°F (no welding outside this range)
- **Humidity**: <70% RH (to minimize porosity)
- **Wind**: No drafts (indoor welding or windscreens required)
- **Cleanliness**: Clean, dry, dust-free environment

### Tack Welding

- Use same filler metal and process as final weld
- Tack welds must be full penetration (will become part of final weld)
- Blend tack ends to avoid inclusions

### Root Pass

- Full penetration required
- Back purge maintained throughout root pass
- Monitor purge O2 level (<50 ppm)

### Fill and Cap Passes

- Maintain shielding gas coverage
- Interpass temperature: <350°F (to avoid grain growth and sensitization)
- Clean between passes if necessary

## Post-Weld Treatment

### Stress Relief (Optional)

- Typically not required for austenitic stainless steels
- If performed: 1600-1800°F, furnace cool
- Inert atmosphere required (argon or vacuum)

### Solution Annealing (for austenitic SS)

- **Purpose**: Remove sensitization, restore corrosion resistance
- **Temperature**: 1900-2100°F
- **Time**: 5-10 minutes at temperature
- **Quench**: Water quench (rapid cooling required)
- **Atmosphere**: Inert or vacuum (to prevent oxidation)

### Post-Weld Cleaning

1. **Mechanical Cleaning**: Remove discoloration (heat tint) with stainless wire brush or abrasive
2. **Pickling**: Nitric-hydrofluoric acid pickle (per ASTM A380) to remove embedded iron and chromium-depleted layer
3. **Passivation**: Nitric acid or citric acid passivation (per ASTM A380 or AMS 2700)
4. **Final Rinse**: DI water rinse, compressed air dry

## Inspection and Testing

### Visual Inspection (100%)

Per AWS D17.1:
- No cracks, incomplete fusion, or undercutting
- Uniform bead profile
- No excessive spatter or contamination
- Smooth tie-in with base material

### Liquid Penetrant Testing (100%)

- Per ASTM E1417 or AMS 2644
- Applied to all accessible weld surfaces
- Acceptance: No linear indications >0.030", no rounded indications >0.060"

### Radiographic Testing (100% for pressure boundaries)

- Per ASTM E1742 or AMS 2647
- Film or digital radiography
- Acceptance Criteria:
  - No cracks, incomplete fusion, or incomplete penetration
  - Porosity: <5% of wall thickness in any 1" length
  - Slag inclusions: <5% of wall thickness

### Ultrasonic Testing (as applicable)

- For thick sections or inaccessible welds
- Per ASTM E164 or equivalent
- Technician: NAS-410 Level II or III

### Helium Leak Testing (100%)

**Method**: Helium mass spectrometer

**Acceptance Criteria**:
- **Leak Rate**: ≤1×10⁻⁹ std cc/sec (one nanoleak)
- **Test Procedure**:
  1. Evacuate component, backfill with helium to design pressure
  2. Probe all welds with mass spectrometer detector
  3. Document leak rate at each joint
  4. Repair and re-test any leaks above specification

### Destructive Testing (qualification and sample)

**Tensile Test** (per ASTM E8):
- Weld tensile strength ≥ base material minimum

**Guided Bend Test** (per ASME Section IX):
- No cracks or defects >0.125" in any direction

**Charpy Impact Test** (for cryogenic service):
- Test weld metal and HAZ at -196°C (LN2 temperature)
- Acceptance: ≥20 ft-lbs (27 J) typical

## Weld Repair

### Repair Authorization

- All repairs require engineering approval
- Repair WPS must be qualified
- Document repair location, extent, and method

### Repair Process

1. Remove defective weld by grinding or machining
2. Inspect excavation (PT or MT)
3. Re-weld using qualified WPS
4. Re-inspect per original inspection requirements
5. Limit: Typically 2 repairs maximum in same location

## Safety Requirements

### Hydrogen Safety

- Welding on H2 components must be performed in designated H2-free areas
- Components must be purged and cleaned before welding
- H2 detectors in area (if any residual H2 risk)

### Welding Safety

- Proper ventilation (fume extraction)
- Personal protective equipment (welding helmet, gloves, flame-resistant clothing)
- Fire extinguisher readily available

## Documentation and Traceability

### Required Records

- Welding Procedure Specification (WPS)
- Procedure Qualification Record (PQR)
- Welder/Operator qualification certificates
- Weld log (welder ID, date, WPS used, parameters)
- Inspection and test reports (VT, PT, RT, leak test)
- Repair records (if applicable)

### Record Retention

- Permanent (life of component + 5 years minimum)

## References

- [10-00-09-01A_Master_Manufacturing_Plan.md](../manufacturing-plans/10-00-09-01A_Master_Manufacturing_Plan.md)
- [10-00-09-04A_H2_Components_Manufacturing.md](../manufacturing-plans/10-00-09-04A_H2_Components_Manufacturing.md)
- [10-00-09-11A_Heat_Treatment_Spec.md](10-00-09-11A_Heat_Treatment_Spec.md)
- [10-00-09-22A_NDT_Requirements.md](../quality-control/10-00-09-22A_NDT_Requirements.md)

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-10

---
