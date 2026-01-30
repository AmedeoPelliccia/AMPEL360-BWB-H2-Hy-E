# 85-00-01-003 Passenger Evacuation and Rescue Interfaces

## Document Information

- **Document ID**: 85-00-01-003
- **Title**: Passenger Evacuation and Rescue Interfaces
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Safety & Emergency Interfaces
- **ATA Chapter**: 85 - Infrastructure Interface Standards

## Purpose

This document specifies the interfaces between the AMPEL360 BWB aircraft and airport emergency infrastructure for passenger evacuation and rescue operations. The unique BWB geometry creates novel challenges and opportunities for emergency egress that require careful integration with airport facilities and equipment.

## Scope

This specification covers:

- Door locations and evacuation slide deployment considerations
- Ground clearance and slide reach requirements
- Airport rescue vehicle access and compatibility
- Emergency communication systems integration
- Coordination with airport emergency response plans
- Cross-ATA integration with fire protection and door systems

## BWB Geometry Impact on Evacuation

### Unique Characteristics

The Blended Wing Body configuration presents distinct evacuation considerations:

1. **Wide, Flat Profile**
   - Passenger cabin width: 45-50m at widest point
   - Multiple parallel seating rows across the width
   - Distributed door locations vs. concentrated doors on conventional aircraft

2. **Lower Cabin Floor Height**
   - BWB floor height: 3.5-4.5m above ground (vs. 4.5-6.0m for conventional wide-body)
   - Reduced slide length requirement
   - Improved slide deployment reliability (shorter, less wind-sensitive)

3. **Distributed Emergency Exits**
   - 12 Type A doors (forward and aft of wing) - passenger evacuation
   - 4 Type III overwing exits - passenger evacuation
   - 2 ventral emergency hatches (flight deck crew escape only)
   - Total passenger evacuation capacity: 16 exits (12 Type A + 4 Type III) > 220 passengers in 90 seconds (CS-25.803 / FAR 25.803 requirement)

## Door Locations and Access

### Door Configuration

**Forward Section (Stations 5-12m):**
- Port: Doors 1L, 2L, 3L (Type A)
- Starboard: Doors 1R, 2R, 3R (Type A)
- Spacing: 3.5m between doors
- Ground clearance: 3.8m to door sill

**Aft Section (Stations 24-30m):**
- Port: Doors 4L, 5L, 6L (Type A)
- Starboard: Doors 4R, 5R, 6R (Type A)
- Spacing: 3.0m between doors
- Ground clearance: 4.2m to door sill

**Overwing Exits (Stations 16-19m):**
- Port: Exits 7L, 8L (Type III)
- Starboard: Exits 7R, 8R (Type III)
- Wing upper surface access: 2.8m above ground
- Slide/ramp deployment onto wing, then to ground

**Flight Deck:**
- Escape hatches: 2 ventral hatches (pilot and co-pilot positions)
- Drop height: 2.5m to ground
- Rope/strap descent system integrated

### Jetway/Stairs Compatibility

**Passenger Boarding Bridges (PBB):**
- Compatible door positions: 1L/R, 2L/R (primary boarding)
- PBB height range: 2.5-5.0m (standard airport equipment compatible)
- PBB cab dimensions: Standard 2.5m width, 3.0m length
- Approach angle: 0-15° incline (BWB doors accessible with minimal adjustment)

**Mobile Stairs:**
- Door access: All Type A doors accessible via standard GSE stairs
- Stair height requirement: 4.5m maximum (standard airport equipment)
- Platform area: 2.0m x 1.5m minimum at door threshold

## Evacuation Slide Interface

### Slide Specifications

**Type A Door Slides:**
- Length when deployed: 7.0-7.5m (reaching from 4.0m sill height to ground at 35° angle)
- Width: 1.1m (dual-lane capable)
- Inflation time: < 6 seconds (CS-25.809 / FAR 25.809 requirement)
- Capacity: 70 passengers/minute/slide
- Wind resistance: Operational up to 25 knots with guy-lines

**Overwing Slide/Ramps:**
- Type: Combination slide/escape ramp
- Stage 1: Ramp deployment onto wing upper surface (1.0m height difference)
- Stage 2: Slide from wing trailing edge to ground (3.5m drop)
- Total egress time: < 90 seconds for all passengers via all exits

### Ground Clearance Requirements

**Slide Deployment Zones (No obstacles permitted):**
- Forward section slides: 10m x 5m zone per door (10m along fuselage, 5m perpendicular)
- Aft section slides: 10m x 5m zone per door
- Overwing exits: 8m x 4m zone per exit (from wing trailing edge)

**Stand Design Considerations:**
- Pavement must support slide deployment without damage
- Drainage grates covered or slots perpendicular to slide direction
- Lighting: Emergency lighting at 50 lux minimum in slide zones
- Markings: High-visibility markings for evacuation zones (per ICAO Annex 14)

### Slide Reach and Ground Contact

**Geometric Analysis:**
| Door Position | Sill Height | Slide Length | Ground Contact Distance | Required Clear Zone |
|---------------|-------------|--------------|-------------------------|---------------------|
| 1L/R - 3L/R   | 3.8m        | 7.0m         | 6.0m from fuselage      | 10m x 5m            |
| 4L/R - 6L/R   | 4.2m        | 7.5m         | 6.5m from fuselage      | 10m x 5m            |
| 7L/R - 8L/R   | 2.8m (wing) | 3.5m (stage 2)| 5.0m from wing TE      | 8m x 4m             |

## Airport Rescue Vehicle Access

### Aircraft Rescue and Firefighting (ARFF)

**Access Paths:**
- Primary ARFF lane: Perimeter road, 10m wide, surrounding stand
- Secondary access: Through slide deployment zones (only after evacuation complete)
- Fire truck positioning: 20m from aircraft at 45° angle (standard ICAO approach)

**ARFF Vehicle Compatibility:**
- BWB profile: Lower than conventional aircraft, better access to upper surfaces
- Roof access: ARFF platform height 8-12m sufficient for BWB (vs. 12-18m for A380/B747)
- Reach: Standard articulated boom platforms adequate

**Water/Foam Application:**
- Primary risk zones: H₂ refuelling ports (stations 12-13m), fuel cell bays (stations 10-20m)
- Slide protection: Foam application must not obstruct slides if still in use
- Underside access: Improved vs. conventional aircraft (lower clearance, wider access)

### Rapid Intervention Vehicle (RIV)

**RIV Positioning:**
- Station location: Within 2 minutes response time to any part of airport
- Stand access: Direct access to all slide deployment zones
- Capacity: Minimum 500L water/foam, 2-person crew
- Equipment: Thermal imaging, H₂ leak detection, CO₂ monitors

### Ambulance and Medical Access

**Casualty Evacuation Routes:**
- Primary route: Via jetway or stairs (if still accessible)
- Secondary route: Mobile medical unit positioning at slide termination points
- Stretcher compatibility: 10m x 5m clear zones allow ambulance direct access

**Medical Staging Area:**
- Location: 50m from aircraft, upwind if possible
- Size: 20m x 30m for triage and treatment
- Access: Direct road access for ambulances

## Emergency Communication Systems

### Ground-Aircraft Communication

**Emergency Frequencies:**
- Tower: 121.5 MHz (emergency frequency)
- Ground: 121.6 MHz (airport emergency services coordination)
- ARFF: Dedicated channel (airport-specific, e.g., 453.000 MHz)

**Data Links:**
- ACARS emergency message broadcast
- Aircraft emergency status transmitted to Airport Operations Center (AOC)
- Automated notifications: Door openings, slide deployments, fire detection

### Evacuation Coordination

**Airport Emergency Response:**
- Automatic alerts to ARFF, medical, security
- Passenger count and manifest data transfer
- Evacuation status updates (real-time door/slide status)

**Public Address Integration:**
- Stand-mounted speakers linked to aircraft PA system (for crew instructions audible outside)
- Airport PA system for assembly point directions

## Passenger Flow and Assembly

### Evacuation Routes

**From Forward Doors (1L/R - 3L/R):**
- Direction: Forward and outboard from aircraft nose
- Assembly point: 100m forward of aircraft nose, 30m lateral offset
- Capacity: 110 passengers (assuming even distribution)

**From Aft Doors (4L/R - 6L/R):**
- Direction: Aft and outboard from aircraft tail
- Assembly point: 100m aft of aircraft tail, 30m lateral offset
- Capacity: 110 passengers

**From Overwing Exits (7L/R - 8L/R):**
- Direction: Outboard from wing tips
- Assembly point: 50m lateral from wing tips
- Capacity: 40 passengers (overflow from other exits)

### Stand Design for Evacuation

**Safe Zones (per ICAO Annex 14 and NFPA 403):**
- Minimum 50m from aircraft for assembly points
- Upwind positioning (prevailing wind consideration)
- Illumination: 20 lux minimum at assembly points
- Markings: High-visibility signs and pavement markings

**Barriers and Guidance:**
- Retractable barriers guide passengers away from aircraft
- Illuminated guidance strips (photo-luminescent or LED)
- Audio beacons at assembly points (for visibility-impaired conditions)

## Integration with Airport Emergency Plans

### ICAO Annex 14 Compliance

**Aerodrome Emergency Planning:**
- BWB-specific scenarios added to airport emergency exercises
- ARFF training on BWB access and H₂ safety
- Slide deployment zone marking and protection

**Airport Emergency Plan (AEP) Amendments:**
- BWB evacuation procedures documented
- H₂ fire response protocols (reference [ATA 26 Fire Protection](../../../T-TECHNOLOGY/E1-ENVIRONMENT/ATA_26-FIRE_PROTECTION/))
- Medical response scaled for 220-passenger capacity

### Mutual Aid Agreements

**Off-Airport Resources:**
- Local fire departments (secondary response)
- Regional hospitals (mass casualty coordination)
- Specialized H₂ incident response teams

## Cross-ATA Integration

### ATA 26 - Fire Protection

**Interface Points:**
- Fire detection system status → 85 evacuation triggers
- Halon/water suppression activation → 85 slide deployment inhibits (if fire in slide deployment zone)
- Emergency lighting → 85 ground lighting coordination

**Shared Procedures:**
- Fire scenario response protocols
- H₂ fire-specific procedures (water deluge, not foam)
- Post-fire inspection requirements

### ATA 52 - Doors

**Interface Points:**
- Door status (open/closed/armed) → 85 evacuation readiness
- Slide deployment sensors → 85 ground status displays
- Door opening commands ↔ 85 evacuation initiation

**Shared Data:**
- Door operation history (for reliability tracking)
- Slide inflation pressure and deployment time logs
- Door/slide maintenance status

### ATA 02 - Operations Information

**Interface Points:**
- Passenger manifest and count → 85 evacuation accountability
- Special assistance passengers (PRMs) → 85 evacuation priority
- Crew emergency procedures → 85 ground coordination protocols

**Training Integration:**
- Cabin crew training on BWB-specific evacuation procedures
- Ground crew training on slide deployment zone management
- Joint exercises with airport emergency services

## Certification and Testing

### CS-25 / FAR 25 Requirements

**CS-25.803 / FAR 25.803 - Emergency Evacuation:**
- Full-scale evacuation demonstration: 220 passengers in 90 seconds
- Half of exits blocked (worst-case scenario)
- Emergency lighting only (nighttime conditions)
- Representative passenger mix (age, mobility)

**CS-25.809 / FAR 25.809 - Emergency Exit Arrangement:**
- Exit type and size verification
- Slide deployment and inflation testing
- Dual-lane capability demonstration (Type A doors)

### Airport Compatibility Testing

**Ground Testing at Airports:**
- Slide deployment tests at representative stands
- ARFF vehicle access trials
- Communication system integration verification
- Night/low-visibility evacuation exercises

**Airport Certification:**
- ICAO Annex 14 compliance (stand geometry, lighting, markings)
- Airport emergency plan approval by civil aviation authority
- ARFF training and qualification for BWB operations

## Future Enhancements

### Advanced Evacuation Systems

- **Inflatable evacuation chutes with integrated lighting** (LED strips for guidance)
- **Autonomous ground vehicles** (AGVs) for passenger transport from assembly points to terminals
- **Augmented reality (AR) guidance** for crew (via helmet-mounted displays showing evacuation status)

### Smart Airport Integration

- **Real-time tracking of evacuees** (via passenger mobile devices, anonymized)
- **Predictive modeling** of evacuation flow (AI-optimized assembly point selection)
- **Integrated command center** with aircraft, ARFF, and medical data fusion

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
