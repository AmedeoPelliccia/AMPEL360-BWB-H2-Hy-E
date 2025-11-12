# Cabin Height and Door Sill Mockup

**Component:** ATA 02-11-00 - AIRCRAFT_DIMENSIONS_GEOMETRY  
**Document Type:** Mockup Specification  
**Platform:** AMPEL360 BWB H2 Hy-E Q100 INTEGRA  
**Version:** 1.0  
**Date:** 2025-11-11  
**Status:** Development

---

## Purpose

This mockup specification defines the cabin interior height and door sill validation prototype for the Blended Wing Body aircraft. The BWB configuration presents unique cabin geometry challenges due to the varying cross-section profile and integration of passenger spaces within the aerodynamic lifting body.

---

## Mockup Overview

### Objectives

1. **Cabin Height Validation**: Verify adequate headroom throughout passenger cabin
2. **Door Sill Height**: Validate door sill heights for passenger boarding and emergency egress
3. **Ergonomic Assessment**: Evaluate passenger comfort and crew workability
4. **Emergency Egress**: Test evacuation procedures and compliance
5. **Ground Service Equipment Interface**: Verify compatibility with passenger boarding bridges and stairs

### BWB-Specific Challenges

The blended wing body design introduces unique cabin considerations:
- **Variable Cross-Section**: Cabin height varies significantly across the span
- **Center Body Design**: Maximum height at centerline, reduced toward edges
- **Aerodynamic Constraints**: Cabin profile optimized for lift generation
- **Multiple Cabin Zones**: Different height standards for center, mid-span, and outboard sections
- **Wide-Body Configuration**: 28m cabin width with multiple aisles

---

## Cabin Geometry Specifications

### Cross-Section Zones

| Zone | Location (BL) | Max Cabin Height | Min Cabin Height | Width | Seat Rows |
|------|---------------|------------------|------------------|-------|-----------|
| Center | 0 ± 4m | 2.45 m | 2.20 m | 8 m | 3-4-3 |
| Mid-Span Left | -4 to -10m | 2.20 m | 1.95 m | 6 m | 2-3-2 |
| Mid-Span Right | +4 to +10m | 2.20 m | 1.95 m | 6 m | 2-3-2 |
| Outboard Left | -10 to -14m | 1.95 m | 1.75 m | 4 m | 2-2 |
| Outboard Right | +10 to +14m | 1.95 m | 1.75 m | 4 m | 2-2 |

**Total Passenger Capacity:** 220 passengers in 2-class configuration

### Regulatory Requirements

**EASA CS-25.815 & FAA FAR 25.815 - Width of Aisle:**
- Minimum aisle width: 
  - Center aisle (≤9 seats): 20 inches (508 mm)
  - Outboard aisles (≤8 seats): 15 inches (381 mm)

**CS-25.813 - Emergency Exit Access:**
- Clear height above floor: ≥1.83 m (72 inches)
- Door sill height: 0.45-1.83 m above ground
- Emergency slide deployment envelope validated

---

## Door Specifications

### Passenger Entry Doors (Type A)

| Door ID | Location (FS, BL) | Sill Height | Clear Opening | Sill to Ground | Service |
|---------|-------------------|-------------|---------------|----------------|---------|
| L1 | FS 8.0, BL -10.0 | WL 2.5 m | 1.07m × 1.83m | 2.5 m | Forward Left |
| R1 | FS 8.0, BL +10.0 | WL 2.5 m | 1.07m × 1.83m | 2.5 m | Forward Right |
| L2 | FS 25.0, BL -10.0 | WL 2.5 m | 1.07m × 1.83m | 2.5 m | Mid Left |
| R2 | FS 25.0, BL +10.0 | WL 2.5 m | 1.07m × 1.83m | 2.5 m | Mid Right |

### Emergency Exits (Type III)

| Exit ID | Location (FS, BL) | Sill Height | Clear Opening | Function |
|---------|-------------------|-------------|---------------|----------|
| L3 | FS 35.0, BL -12.0 | WL 2.8 m | 0.51m × 0.91m | Overwing |
| R3 | FS 35.0, BL +12.0 | WL 2.8 m | 0.51m × 0.91m | Overwing |
| L4 | FS 42.0, BL -8.0 | WL 2.6 m | 0.51m × 0.91m | Aft |
| R4 | FS 42.0, BL +8.0 | WL 2.6 m | 0.51m × 0.91m | Aft |

**Note:** All exits meet CS-25.807 requirements for emergency evacuation (220 passengers in 90 seconds)

---

## Physical Mockup Configuration

### Full-Scale Section Mockup

**Scope:** 
- 8-meter longitudinal section (FS 8-16)
- Full 28-meter span width
- Three cabin zones represented

**Structure:**
- **Frame:** Aluminum profiles simulating fuselage frames at 600mm spacing
- **Skin:** Plywood panels with interior finish
- **Floor:** Raised floor system with under-floor cargo simulation
- **Ceiling:** Contoured ceiling panels with lighting and PSU mockups
- **Windows:** Acrylic windows at representative spacing

**Features:**
- 4 × Type A doors (2 operational, 2 static)
- 32 passenger seats (mix of economy and business class)
- 2 galleys (forward and mid-cabin)
- 2 lavatories
- Overhead bins (full width)
- Lighting system (LED strips)
- Air distribution outlets

---

## Test Program

### Test Series 1: Cabin Height Compliance

**Objective:** Verify minimum headroom requirements throughout cabin

**Test Method:**
- Anthropometric mannequins (5th, 50th, 95th percentile)
- Walking clearance assessment
- Standing reach envelope testing
- Emergency equipment accessibility

**Measurement Points (per zone):**
- Centerline height (every 2m longitudinally)
- Aisle centerline height
- Seat location height (above armrest)
- Overhead bin clearance
- Galley working height
- Lavatory interior height

**Acceptance Criteria:**
- 95th percentile passenger: Standing clearance ≥ 150mm
- 50th percentile: Comfortable standing (≥ 200mm clearance)
- Aisle walking: No head contact with ceiling or bins
- Emergency equipment: Reachable by 5th percentile crew

---

### Test Series 2: Door Sill Height Validation

**Objective:** Validate door sill heights for safe boarding and egress

**Test Scenarios:**

#### Ground Boarding (Passenger Boarding Bridge)
- **Bridge Height Range:** 2.0 - 3.5 m adjustable
- **Bridge Angle:** 0° to 8° slope
- **Test Cases:**
  - Optimal docking (level bridge)
  - Maximum upward slope
  - Maximum downward slope
  - Misaligned bridge (±200mm lateral)

**Measurements:**
- Passenger step height (sill to bridge floor)
- Crew mobility assessment
- Wheelchair boarding path
- Carry-on baggage clearance

**Pass Criteria:**
- Step height: 150-300mm (optimal)
- Maximum step: <400mm
- Wheelchair ramp: ≤12° slope
- Bridge contact: No interference with door operation

---

#### Mobile Stairs Boarding
- **Stair Type:** Towable passenger stairs, Code E compatible
- **Platform Height:** Adjustable 2.0-3.0m
- **Test Cases:**
  - Standard stairs (optimal height)
  - Minimum height stairs
  - Maximum height stairs
  - Adverse weather (wind loading)

**Measurements:**
- Stair platform to sill gap
- Handrail continuity
- Passenger flow rate (persons/minute)
- Emergency descent time

**Pass Criteria:**
- Platform gap: <100mm
- Handrails: Continuous from stairs to cabin
- Flow rate: ≥30 passengers/minute
- Emergency descent: 220 passengers <90 seconds

---

#### Emergency Evacuation
- **Slide Deployment:** Inflatable escape slide
- **Slide Angle:** 42° ±5° from horizontal
- **Test Cases:**
  - Normal evacuation (slide only)
  - Door over wing (auxiliary egress)
  - Mixed egress (stairs + slides)
  - Adverse conditions (wind, darkness)

**Test Protocol:**
- 220 test subjects (crew + volunteers)
- Mix of ages and mobility levels
- Cabin smoke simulation (non-toxic)
- Emergency lighting only
- Timed evacuation drill

**Acceptance:**
- Full evacuation in <90 seconds
- No injuries during egress
- Slide inflation time <6 seconds
- All exits functional

---

### Test Series 3: Ergonomic Assessment

**Objective:** Evaluate passenger comfort and crew workability

#### Passenger Comfort Evaluation
- **Participants:** 30 passengers, varied demographics
- **Duration:** 2-hour simulated flight
- **Assessments:**
  - Seat comfort rating (1-10 scale)
  - Headroom adequacy
  - Personal space perception
  - Aisle width adequacy
  - Overhead bin accessibility
  - Lavatory usability

#### Crew Workability Study
- **Participants:** 6 cabin crew (2 per shift)
- **Duration:** Full simulated flight cycle
- **Tasks:**
  - Pre-flight cabin preparation
  - Safety demonstration
  - Meal/beverage service
  - Passenger assistance
  - Emergency procedure rehearsal

**Data Collection:**
- Video recording of all activities
- Ergonomic motion analysis
- Time-and-motion studies
- Participant surveys and interviews
- Physical workload assessment (NASA-TLX)

**Acceptance Criteria:**
- Passenger comfort: Mean rating ≥ 7/10
- Crew workload: Acceptable per NASA-TLX (<60)
- No ergonomic risk factors identified
- Service times within industry standards

---

## Instrumentation

### Measurement Equipment

| Instrument | Specification | Quantity | Purpose |
|------------|---------------|----------|---------|
| Laser Distance Meter | ±2mm, 50m range | 4 | Height measurements |
| Anthropometric Mannequin | 5th, 50th, 95th %ile | 3 sets | Clearance validation |
| Digital Inclinometer | ±0.1° accuracy | 2 | Door/ramp angles |
| Load Cell | 0-2000N, ±0.5% | 8 | Door operation forces |
| Video Camera (HD) | 1080p, 60fps | 12 | Documentation |
| Motion Capture System | 10-camera array | 1 | Ergonomic analysis |
| Environmental Sensors | Temp, humidity, CO2 | 8 | Comfort monitoring |
| Timer/Stopwatch | 0.01s resolution | 4 | Evacuation timing |

---

## Documentation and Deliverables

### Test Reports

1. **Cabin Height Compliance Report**
   - As-built measurements vs. design
   - Zone-by-zone compliance matrix
   - Non-conformances and resolutions
   - Anthropometric validation results

2. **Door Sill Validation Report**
   - Sill height verification
   - Ground service equipment compatibility
   - Boarding/deboarding flow analysis
   - Emergency egress validation

3. **Ergonomic Assessment Report**
   - Passenger comfort analysis
   - Crew workload evaluation
   - Recommendations for optimization
   - Comparative analysis (vs. conventional aircraft)

4. **Photographic and Video Documentation**
   - Comprehensive photo library
   - Annotated key features
   - Evacuation drill footage
   - Ergonomic motion analysis videos

### Design Outputs

- Updated cabin arrangement drawings
- Door installation specifications
- Ground service equipment interface requirements
- Crew training materials

---

## Schedule and Resources

### Timeline

| Phase | Duration | Milestone |
|-------|----------|-----------|
| Mockup Design | 4 weeks | Design review approval |
| Procurement | 6 weeks | All materials on site |
| Construction | 8 weeks | Mockup complete |
| Instrumentation | 2 weeks | All systems operational |
| Test Series 1 | 2 weeks | Cabin height validation |
| Test Series 2 | 3 weeks | Door sill validation |
| Test Series 3 | 3 weeks | Ergonomic assessment |
| Analysis & Reporting | 3 weeks | Final reports |
| **Total** | **31 weeks** | Complete package |

### Resources

**Personnel:**
- Lead Engineer (full-time)
- 2× Test Engineers (full-time)
- Ergonomics Specialist (part-time)
- Safety Officer (part-time)
- 4× Technicians (full-time)
- Admin Support (part-time)

**Facilities:**
- 400 m² covered workspace
- Climate control (15-30°C)
- Power supply (200A, 3-phase)
- Lighting (≥500 lux)
- Emergency services access

---

## Regulatory Compliance

### Applicable Regulations

- **EASA CS-25.785:** Seats, berths, safety belts, and harnesses
- **EASA CS-25.807:** Emergency exits
- **EASA CS-25.810:** Emergency egress assist means
- **EASA CS-25.813:** Emergency exit access
- **EASA CS-25.815:** Width of aisle
- **EASA CS-25.817:** Maximum number of seats abreast
- **FAA FAR Part 25 (equivalent sections)**

### Certification Coordination

- Early engagement with EASA and FAA
- Invite authority observers to key tests
- Provide test plans 30 days in advance
- Immediate reporting of non-compliances
- Documentation per AC 25.807-1A guidance

---

## Risk Management

### Critical Risks

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Insufficient cabin height | High | Low | FEA validation pre-build |
| Door sill too high | High | Medium | Multiple stair configurations |
| Failed evacuation test | Critical | Low | Rehearsals, expert review |
| Ergonomic issues | Medium | Medium | Early user involvement |
| Mockup construction delays | Medium | High | Buffer in schedule |

### Safety Considerations

- Emergency stop system for powered doors
- Fire suppression equipment on site
- First aid kit and trained personnel
- Evacuation routes clearly marked
- Test participant screening (health)

---

## Related Documents

- ATA 52-10-00: Passenger Doors
- ATA 25-00-00: Equipment and Furnishings
- Station_BL_WL_Visualizer_v1.py
- BWB Cabin Cross-Section Drawings
- Emergency Evacuation Analysis

---

## Document Control

**Revision History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-11 | AMPEL360 Engineering | Initial release |

**Approval:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Cabin Systems Engineer | TBD | ___________ | ______ |
| Human Factors Specialist | TBD | ___________ | ______ |
| Certification Engineer | TBD | ___________ | ______ |
| Safety Manager | TBD | ___________ | ______ |

---

**Copyright © 2025 AMPEL360 Project. All Rights Reserved.**
