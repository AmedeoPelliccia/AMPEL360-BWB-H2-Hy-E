# 85-00-01-004 Ground Handling and Turnaround Interfaces

## Document Information

- **Document ID**: 85-00-01-004
- **Title**: Ground Handling and Turnaround Interfaces
- **Version**: 1.0
- **Date**: 2025-11-21
- **Status**: Draft
- **Category**: Ground Operations
- **ATA Chapter**: 85 - Infrastructure Interface Standards

## Purpose

This document specifies the interfaces between the AMPEL360 BWB aircraft and ground handling infrastructure for routine turnaround operations. The unique BWB planform, combined with hydrogen propulsion and CO₂ battery systems, requires adapted ground support equipment (GSE) and procedures.

## Scope

This specification covers:

- Ground power and air conditioning connections
- H₂ refuelling bowser access paths
- CO₂ battery docking and servicing
- Baggage, cargo, catering, and cleaning access
- Pushback and towing interfaces
- Turnaround timeline and critical path analysis
- Cross-ATA integration with operations and servicing chapters

## BWB Planform Impact on Ground Handling

### Geometric Constraints

**Overall Dimensions:**
- Wingspan: 65m (tip to tip)
- Length: 42m (nose to tail)
- Height: 8.5m (ground to highest point)
- Ground footprint: Approximately 2,730 m² (vs. 1,800 m² for A320, 3,200 m² for B777)

**Stand Requirements:**
- Minimum stand size: 80m x 80m (includes clearances)
- Wingtip clearance to adjacent aircraft/obstacles: 7.5m minimum
- Nose/tail clearance to stand boundaries: 10m minimum

**Access Points Distribution:**
- Distributed around perimeter (wide body profile)
- Multiple simultaneous GSE operations possible (parallel servicing)
- Reduced congestion compared to conventional aircraft (wider spacing)

## Ground Power Interface

### GPU Connection Points

**Primary GPU Connection:**
- Location: Forward fuselage, port side, station 6.0m
- Type: 115V AC 400Hz, 90 kVA (standard civil aviation GPU)
- Connector: MIL-STD-2186 (NATO standard) or equivalent
- Cable length requirement: 25m (GPU positioned 20m from aircraft)

**Secondary GPU Connection (Optional):**
- Location: Aft fuselage, starboard side, station 28.0m
- Purpose: Redundancy or additional power for maintenance
- Specifications: Same as primary

**GPU Positioning:**
- Clear zone: 3m x 3m around connection point
- Cable routing: Overhead cable management (elevated at 2.5m) or ground-level with cable protectors
- GPU vehicle clearance: 2.0m from fuselage (standard GSE safety distance)

### Ground Power Requirements

**Pre-Flight Power:**
- Duration: 30-60 minutes (typical turnaround)
- Load: 40-60 kVA (avionics, lighting, air conditioning, battery pre-conditioning)
- Power quality: ±5% voltage regulation, < 3% THD (Total Harmonic Distortion)

**Maintenance Power:**
- Duration: Variable (hours to days)
- Load: 20-90 kVA (depending on systems being tested)
- Backup: Dual GPU or GPU + aircraft batteries

## Air Conditioning Interface

### Pre-Conditioned Air (PCA) Connection

**Connection Points:**
- Forward PCA: Port side, station 8.0m
- Aft PCA: Starboard side, station 26.0m
- Both connections used simultaneously for efficient cabin conditioning

**PCA Specifications:**
- Flow rate: 2.5 kg/s (5,500 lbm/hr) per connection (5.0 kg/s total)
- Supply temperature: 10-15°C (heating) or 5-10°C (cooling)
- Supply pressure: 35 kPa (5 psi)
- Connector type: ACMS (Aircraft Cooling and Monitoring System) standard

**PCA Cart Positioning:**
- Distance from aircraft: 5-10m (ducting length consideration)
- Clear zone: 4m x 4m around cart (noise and exhaust considerations)
- Duct routing: Flexible ducts, supported to prevent damage

## H₂ Refuelling Bowser Access

### Bowser Approach Paths

**Primary Refuelling Path (Port Side):**
- Approach direction: Forward to aft, along port side
- Minimum clearance: 3m from fuselage (wingtip clearance: 10m)
- Turnaround space: 15m x 10m zone for bowser positioning and operator access
- Surface requirement: Level, paved, load-bearing (15,000 kg gross vehicle weight)

**Secondary Refuelling Path (Starboard Side):**
- Mirror configuration of port side
- Allows flexibility for stand orientation and wind direction considerations

### Bowser Interface Details

**Mobile H₂ Bowser Specifications:**
- Type: Compressed gas trailer, DOT/ASME certified
- Capacity: 500-1,000 kg H₂ (compressed at 700 bar)
- Hose length: 15m (retracting hose reel)
- Connection time: < 2 minutes (including pre-connection checks)

**Safety Considerations:**
- Exclusion zone during refuelling: 10m radius (no other GSE or personnel)
- Grounding: Both aircraft and bowser grounded, continuity verified
- Communication: Radio link between bowser operator and aircraft fueler panel
- Emergency stop: Accessible from both ground and cockpit

**Sequencing with Other GSE:**
- H₂ refuelling typically early in turnaround (while passengers disembark)
- Completes before cargo/baggage loading (to minimize personnel in vicinity)
- Coordination via ground handling management system

## CO₂ Battery Docking

### Battery Access

**Battery Bay Locations:**
- Port bays: Stations 18m and 21m (ventral access)
- Starboard bays: Stations 18m and 21m (ventral access)
- Total: 4 battery modules

**Access Requirements:**
- Clearance height: 2.5m (under fuselage)
- Access width: 1.5m (per bay)
- Battery cart approach: Perpendicular to fuselage centerline

### Battery Servicing Cart

**Cart Specifications:**
- Type: Electric-powered lift cart (zero-emission GSE)
- Lift capacity: 500 kg (per battery module)
- Positioning accuracy: ±10mm (for docking alignment)
- Lifting speed: 0.1 m/s (controlled, low-vibration)

**Docking Procedure:**
1. Cart positioned under bay (2 minutes)
2. Alignment with guide rails (1 minute)
3. Lifting to docking height (2 minutes)
4. Electrical and thermal connections (1 minute)
5. Verification of connections (1 minute)
- **Total time: 7 minutes per module** (can be done in parallel for multiple modules)

**Operations Modes:**
- **Top-up charging** (during turnaround): Partial charge (20-30% SOC increase in 45-60 minutes)
- **Full charging** (overnight): 80-90% SOC in 4-6 hours
- **Module swap** (future capability): Complete module exchange in 15 minutes

## Baggage and Cargo Handling

### Cargo Door Locations

**Forward Cargo Compartment:**
- Door: Forward fuselage, port side, station 9.0m
- Size: 1.8m x 1.3m (Type A cargo door)
- Sill height: 2.5m above ground
- Capacity: 8 LD3-45 containers (10,000 kg)

**Aft Cargo Compartment:**
- Door: Aft fuselage, starboard side, station 25.0m
- Size: 1.8m x 1.3m (Type A cargo door)
- Sill height: 2.5m above ground
- Capacity: 8 LD3-45 containers (10,000 kg)

**Bulk Cargo Hold:**
- Access: Via forward cargo door, aft section of hold
- Capacity: 2,500 kg (loose baggage and odd-sized cargo)

### Cargo Loading Equipment

**High Loaders / Container Loaders:**
- Type: Self-propelled or towable container loaders
- Platform height: 2.5-3.0m (adjustable)
- Load capacity: 7,000 kg (for handling multiple LD3-45s)
- Positioning: 5m clear zone forward of cargo door for loader approach

**Belt Loaders:**
- Application: Bulk cargo hold (loose baggage)
- Type: Extendable belt conveyor
- Height range: 1.5-3.0m
- Angle: 15-20° (shallow for baggage handling)

**Ground Handling Sequence:**
1. Disembarkation of passengers (T+0 to T+15)
2. Unloading of forward cargo (T+5 to T+20, parallel with pax deplane)
3. Unloading of aft cargo (T+5 to T+20, parallel)
4. Loading of forward cargo (T+25 to T+40)
5. Loading of aft cargo (T+25 to T+40)
6. Baggage reconciliation and door closure (T+50)

## Catering and Cleaning Access

### Catering Door Locations

**Forward Galley:**
- Door: Forward fuselage, starboard side, station 5.0m
- Size: 1.5m x 1.5m (standard catering door)
- Sill height: 3.5m above ground
- Catering highloader required (standard airport GSE)

**Aft Galley:**
- Door: Aft fuselage, port side, station 30.0m
- Size: 1.5m x 1.5m
- Sill height: 3.5m above ground

**Mid-Cabin Service Point (if equipped):**
- Location: Mid-fuselage, starboard side, station 17.0m
- Purpose: Crew rest supplies, medical equipment resupply

### Catering Operations

**Catering Highloader:**
- Type: Scissor lift truck with enclosed platform
- Platform height: 3.5-4.0m (adjustable)
- Platform size: 2.5m x 2.0m
- Capacity: 1,500 kg (full galley service load)

**Catering Sequence:**
- Deplaning complete before catering access (safety/security)
- Forward and aft catering in parallel (2 vehicles, T+20 to T+45)
- Waste and potable water servicing concurrent (T+20 to T+50)

### Cleaning Access

**Cabin Cleaning:**
- Access: Via passenger doors (1L/R, 2L/R using jetway or stairs)
- Cleaning team: 4-6 personnel
- Duration: 20-30 minutes (quick clean) or 60-90 minutes (deep clean)

**Lavatory Servicing:**
- Waste access: Ventral panels, stations 10m, 20m, 28m
- Lavatory service vehicle: Standard airport lavatory cart
- Water and waste simultaneous servicing (T+20 to T+35)

## Pushback and Towing

### Towing Points

**Nose Towing Point:**
- Location: Nose gear, centerline
- Type: Standard tow bar attachment (NATO or equivalent)
- Load capacity: 150,000 kg (aircraft maximum taxi weight)
- Towbar angle: ±60° (for maneuvering)

**Wing Towing Points (Emergency/Maintenance):**
- Location: Main wing spars, stations 16m (port) and 16m (starboard)
- Purpose: For towing without nose gear (maintenance scenarios)
- Special towing rig required

### Pushback Tractor

**Tractor Specifications:**
- Type: Towbarless tractor (preferred) or conventional tow tractor
- Push capacity: 40,000 kg (aircraft on level ground, brakes released)
- Lifting capacity: 25,000 kg (nose gear load)

**Towbarless Operation:**
- Aircraft nose gear captured by tractor cradle
- Clearance verification: Automated sensors or ground crew visual check
- Push speed: 3-5 km/h (walking pace)
- Push distance: 30-50m (typical stand to taxiway clearance)

**Pushback Sequence:**
1. Pre-pushback checklist complete (T+75)
2. Ground crew communication established (intercom or hand signals)
3. Tractor positioned and connected (T+78)
4. Pushback clearance from ATC (T+80)
5. Pushback execution (T+80 to T+85, 5 minutes for 40m push)
6. Tractor disconnect, aircraft taxi clearance (T+85)

### Towing for Maintenance

**Towing to Hangar:**
- Speed: 5-10 km/h (faster than pushback, but controlled)
- Escort: Safety vehicles (front and rear)
- Clearance checks: Wingtip observers for tight spaces

**Special Considerations for BWB:**
- Wide wingspan requires careful clearance monitoring
- Lower profile improves visibility for tow crew
- Center of gravity further aft than conventional aircraft (affects towing dynamics)

## Turnaround Timeline and Critical Path

### Standard 60-Minute Turnaround

| Time (T+min) | Activity | Critical Path? | GSE Required |
|--------------|----------|----------------|--------------|
| 0 | Aircraft arrival, engines shutdown | ✓ | - |
| 2 | Wheel chocks, ground power connected | ✓ | GPU |
| 5 | Passenger disembarkation begins (door 1L/R) | ✓ | Jetway or stairs |
| 5 | Cargo unloading begins (parallel) | - | Container loaders |
| 10 | H₂ refuelling initiated | ✓ | H₂ bowser |
| 15 | Passenger disembarkation complete | ✓ | - |
| 20 | Catering and cleaning begin | - | Catering highloaders, cleaning crew |
| 25 | H₂ refuelling complete (15 min duration) | ✓ | - |
| 25 | Cargo loading begins | ✓ | Container loaders |
| 30 | CO₂ battery top-up begins (if required) | - | Battery cart |
| 40 | Cargo loading complete | ✓ | - |
| 45 | Catering and cleaning complete | - | - |
| 45 | Passenger boarding begins | ✓ | Jetway or stairs |
| 55 | Boarding complete, doors closed | ✓ | - |
| 58 | Pre-flight checks complete, GPU disconnected | ✓ | - |
| 60 | Pushback ready | ✓ | Pushback tractor |

**Critical Path:** Disembarkation → H₂ refuelling → Cargo loading → Boarding → Pushback

### Extended Turnaround (90 Minutes, with Full CO₂ Charge)

- Same as 60-minute, but with full CO₂ battery charge (T+10 to T+70)
- Critical path unchanged (CO₂ charging in parallel with other activities)

### Rapid Turnaround (45 Minutes, Future Capability)

- Requires: Battery swap (instead of charge), pre-positioned H₂ bowser, optimized cargo handling
- Passenger flow optimization (multiple doors boarding simultaneously)
- Relies on airport infrastructure readiness and advanced GSE coordination

## Cross-ATA Integration

### ATA 02 - Operations Information

**Interface Points:**
- Turnaround planning and scheduling → 85 GSE coordination
- Ground handling procedures documentation → 85 infrastructure requirements
- Passenger and cargo manifests → 85 loading/unloading sequences

**Reference Documents:**
- [02-20-14 Ground Operations Management](../../../I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-20_Subsystems/02-20-14_Ground_Ops_Management/)
- [02-20-21 H₂ Operations Procedures](../../../I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/02-20_Subsystems/02-20-21_H2_Ops/)

### ATA 12 - Servicing

**Interface Points:**
- Potable water and waste servicing → 85 access point locations
- Hydraulic and pneumatic servicing → 85 GSE positioning
- Oil and fluid replenishment → 85 ground crew access requirements

### ATA 09 - Towing and Taxiing

**Interface Points:**
- Towing procedures → 85 pushback and towing infrastructure
- Nose gear loads and attachment → 85 ground vehicle specifications
- Taxiway and stand clearances → 85 aircraft dimensions and maneuvering

### ATA 10 - Parking, Mooring, Storage

**Interface Points:**
- Wheel chock specifications → 85 stand equipment
- Tie-down points (for outdoor storage) → 85 ground anchoring
- Covers and weather protection → 85 BWB-specific covers (due to unique shape)

## Ground Handling Safety

### GSE Safety Zones

**Active GSE Zones:**
- H₂ bowser: 10m exclusion radius during refuelling
- Cargo loaders: 5m clear zone at cargo doors
- Pushback tractor: 3m clear zone around tractor and towbar

**Personnel Safety:**
- High-visibility vests required for all ground crew
- Communication: Headsets for noisy environment, hand signals for line-of-sight
- Training: BWB-specific training for ground crew (geometry, H₂ safety, battery systems)

### Foreign Object Debris (FOD) Prevention

**Stand Cleanliness:**
- Pre-arrival FOD walk (within 30 minutes of arrival)
- Post-departure FOD walk
- BWB lower profile increases risk of ingestion (wider intake area closer to ground)

### Weather Considerations

**Wind:**
- Maximum crosswind for pushback: 20 knots (BWB higher surface area, more wind-sensitive)
- H₂ refuelling wind limit: 25 knots (higher winds may require indoor refuelling facility)

**Ice and Snow:**
- De-icing access: From above (standard de-icing trucks compatible)
- BWB upper surface area: 2,500 m² (vs. 1,200 m² for A320) – longer de-icing time
- Anti-icing fluid application: Specialized nozzles for distributed application

## Future Infrastructure Evolution

### Autonomous GSE

- **Autonomous pushback tractors** (GPS-guided, collision avoidance)
- **Automated cargo loaders** (robotic container handling)
- **Self-driving H₂ bowsers** (pre-programmed routes, automated refuelling)

### Smart Stand Integration

- **Real-time GSE tracking** (RFID or GPS for all equipment)
- **Turnaround optimization AI** (dynamic scheduling based on actual progress)
- **Integrated communication** (all GSE and crew on unified data network)

### Energy-Efficient GSE

- **Electric GSE** (zero-emission ground operations)
- **H₂ fuel cell GSE** (using same H₂ infrastructure as aircraft)
- **Solar-powered ground equipment** (for low-power applications)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21

---
