# ICD-02-10-28-002: Tank Geometry Interface

**From:** ATA 02-10 Aircraft General Data  
**To:** ATA 28 Fuel (SAF and Cryogenic)

**ICD ID:** ICD-02-10-28-002  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## Purpose

This Interface Control Document defines the geometric specifications of the hydrogen fuel tanks, including dimensions, locations, and integration within the BWB airframe structure.

## Data Exchange

### Tank Geometry Specifications

**Provided by ATA 02-10:**

#### Forward Center Tank (FCT)
- Type: Cylindrical with spherical ends
- Length: 12.5 m
- Diameter: 2.8 m
- Volume: 33,800 L
- Capacity: 2,400 kg LH₂
- Location: Station 15.0 to 27.5 m, centerline
- CG (full): Station 21.25 m

#### Aft Center Tank (ACT)
- Type: Cylindrical with spherical ends
- Length: 12.5 m
- Diameter: 2.8 m
- Volume: 33,800 L
- Capacity: 2,400 kg LH₂
- Location: Station 30.0 to 42.5 m, centerline
- CG (full): Station 36.25 m

#### Left Wing Tank (LWT)
- Type: Conformal to wing section
- Length: 8.0 m
- Width: 4.5 m
- Height: 1.8 m
- Volume: 22,550 L
- Capacity: 1,600 kg LH₂
- Location: Station 20.0 to 28.0 m, -8.0 m buttock line
- CG (full): Station 24.0 m, -8.0 m BL

#### Right Wing Tank (RWT)
- Type: Conformal to wing section
- Length: 8.0 m
- Width: 4.5 m
- Height: 1.8 m
- Volume: 22,550 L
- Capacity: 1,600 kg LH₂
- Location: Station 20.0 to 28.0 m, +8.0 m buttock line
- CG (full): Station 24.0 m, +8.0 m BL

**Data Format:** 3D CAD models (STEP), dimensional drawings  
**Update Frequency:** Static (design frozen)  
**Criticality:** High

## Tank Construction

**Materials:**
- Inner vessel: Carbon fiber composite with aluminum liner
- Vacuum jacket: Carbon fiber composite
- Insulation: Multi-layer insulation (MLI), 50 layers
- Outer shell: Composite protection layer

**Wall Thickness:**
- Inner vessel: 8 mm
- Vacuum gap: 25 mm
- Outer shell: 5 mm

**Weight Breakdown (per tank):**
- Forward/Aft Center: 480 kg empty
- Left/Right Wing: 320 kg empty
- Total tank structure: 1,600 kg

## Structural Integration

**Mounting System:**
- Forward support: Rigid attachment at forward bulkhead
- Aft support: Sliding joint for thermal expansion
- Vibration isolation: 4 Hz natural frequency minimum
- Thermal expansion allowance: ±15 mm

**Load Path:**
- Tank loads distributed to main frames
- Emergency load: 9 g forward, 6 g lateral, 4.5 g vertical
- Inertia relief during flight reduces effective loads

**Clearances:**
- Minimum to primary structure: 100 mm
- Minimum between tanks: 500 mm
- Service access clearance: 600 mm
- Emergency egress paths maintained

## BWB-Specific Integration

**Center Body Advantages:**
- Ample volume for cylindrical tanks
- Natural load paths through structure
- Optimal CG location
- Minimal aerodynamic penalty

**Wing Tank Integration:**
- Tanks positioned in thickest wing section
- Conformal shape maximizes volume
- Minimal impact on wing structural efficiency
- Heat exchange with wing surface

## Fuel Management Impact

**CG Control:**
- Center tanks provide 14.0 m CG range
- Wing tanks provide lateral balance
- Selective tank usage for CG management
- Maximum CG travel: 27% MAC

**Weight Distribution:**
- Empty tank CG vs full tank CG shift
- Impact on wing loading distribution
- Dynamic CG shift during fuel consumption

## Interface Specifications

**Data Exchange Method:**
- CAD models for installation design
- Interface control drawings
- Clearance verification documentation

**Coordinate System:**
- Aircraft datum at nose (Station 0)
- Buttock line 0 at centerline
- Water line 0 at bottom of fuselage reference

## Safety Zones

**Hazard Areas:**
- 3 m radius around fill/vent connections
- No ignition sources within 10 m
- Ventilation requirements in tank bays
- Fire detection and suppression coverage

**Maintenance Access:**
- Tank inspection doors: 4 per tank
- Service platform locations defined
- Lifting points: 8 per center tank, 4 per wing tank

## Dependencies

- Airframe structural design (ATA 53, 57)
- Weight and balance (ATA 08)
- Fuel system plumbing (ATA 28)
- Fire protection (ATA 26)
- Environmental control (ATA 21)

## Responsibilities

**ATA 02-10 (Provider):**
- Maintain master tank geometry definition
- Coordinate tank location changes
- Define clearance envelopes

**ATA 28 (Consumer):**
- Design tanks to geometry requirements
- Install and integrate fuel system
- Validate clearances and access
- Maintain tank integrity

## Change Control

Tank geometry changes require:
1. Structural re-analysis and certification
2. Weight and balance recalculation
3. CG envelope revalidation
4. Manufacturing tooling updates
5. Maintenance procedure revisions

## References

- ISO 11119: Gas Cylinders - Composite Construction
- SAE AS8015: Minimum Performance Standards for Cryogenic Fuel Tanks
- EASA CS-25.965: Fuel Tank Installation

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Review Cycle: Per design change only
