# 85-00-02-003 Safety Zones and Separation Criteria

## Document Information
- **Document ID**: 85-00-02-003
- **Title**: Safety Zones and Separation Criteria for Infrastructure Interfaces
- **Version**: 1.0
- **Status**: Draft
- **Last Updated**: 2025-11-21

## Purpose

This document describes **safety zones** and separation requirements for BWB infrastructure interfaces. It specifies minimum distances, physical barriers, and procedural controls to ensure that hazards in one domain (H₂ refueling, CO₂ battery systems, passenger flows, GSE operations) do not propagate to adjacent areas or systems.

## Scope

Safety zones and separation criteria cover:
- **H₂ safety zones** (Ex zones, exclusion zones, restricted access zones)
- **CO₂ battery container safety distances** (thermal, electrical, access control)
- **Passenger flow separation** from energy systems and GSE
- **Rescue vehicle access lanes** and clearances around BWB doors and slides
- **GSE routing** to avoid conflicts with energy interfaces and evacuation routes

## H₂ Safety Zones

### Ex Zone Classification

H₂ refueling creates potentially explosive atmospheres that must be controlled through **Ex zone (explosion hazard zone) classification** per [IEC 60079-10-1](https://webstore.iec.ch/publication/632) and [NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code).

#### Zone 0 (Continuous or Long-Period Hazard)

**Definition**: Area where explosive H₂-air mixture is present continuously or for long periods

**Location at BWB Interface**:
- Interior of H₂ dispenser hose (upstream of connector)
- Interior of aircraft H₂ tank vent system
- Normally **not present** at external interface during normal operations

**Separation Distance**: Not applicable (internal to sealed systems)

**Requirements**:
- Ex-rated equipment only (Category 1 per ATEX)
- Intrinsically safe electrical systems
- No hot work or ignition sources permitted

#### Zone 1 (Likely to Occur Occasionally)

**Definition**: Area where explosive H₂-air mixture is likely during normal operations

**Location at BWB Interface**:
- **3-meter radius** around H₂ dispenser nozzle/connector during refueling operations
- **2-meter radius** around H₂ vent outlets on aircraft
- Area beneath H₂ connector when connected (H₂ lighter than air, but small leaks may accumulate)

**Separation Distance**: Minimum 3 meters from any ignition source, non-essential personnel, or non-Ex-rated equipment

**Requirements**:
- Ex-rated equipment (Category 2 per ATEX)
- Physical barriers (cones, tape, fencing) during refueling
- Continuous H₂ monitoring with automatic alarm at 25% LEL (Lower Explosive Limit)
- Only trained personnel with non-sparking tools allowed
- No smoking, no hot work, no mobile phones (unless Ex-rated)

#### Zone 2 (Unlikely to Occur, Brief Duration)

**Definition**: Area where explosive H₂-air mixture is unlikely or present only briefly

**Location at BWB Interface**:
- **10-meter radius** around H₂ dispenser during refueling operations
- **5-meter radius** around H₂ vent outlets
- General stand area downwind of H₂ operations (H₂ disperses rapidly)

**Separation Distance**: Minimum 10 meters from passenger boarding areas, non-essential personnel

**Requirements**:
- General-purpose electrical equipment acceptable (with appropriate precautions)
- H₂ monitoring recommended (alarm at 50% LEL)
- Access control signage and procedural controls
- No intentional ignition sources (welding, cutting, smoking)

### H₂ Safety Zone Summary Table

| **Zone** | **Description** | **Radius from H₂ Source** | **Ignition Source Control** | **Personnel Access** | **Monitoring** |
|----------|-----------------|---------------------------|----------------------------|---------------------|----------------|
| Zone 0 | Continuous hazard | N/A (internal systems) | Category 1 Ex equipment | No access | Continuous |
| Zone 1 | Likely occasional hazard | 3 m (connector), 2 m (vent) | Category 2 Ex equipment | Trained personnel only, non-sparking tools | Continuous, alarm @ 25% LEL |
| Zone 2 | Unlikely/brief hazard | 10 m (general area) | General precautions | Access controlled | Recommended, alarm @ 50% LEL |
| Normal | No H₂ hazard | >10 m | Standard practices | Normal operations | Background monitoring |

### H₂ Safety Zone Diagram

See [ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg](ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg) for visual representation of H₂ safety zones on typical BWB stand.

## CO₂ Battery Container Safety Distances

### Thermal Safety Distance

**Objective**: Prevent thermal cascade between CO₂ battery containers or to adjacent systems

**Minimum Separation**:
- **5 meters** between CO₂ battery containers (lateral)
- **3 meters** between CO₂ battery container and aircraft fuselage (when not docked)
- **10 meters** between CO₂ battery container and H₂ refueling area
- **2 meters** between CO₂ battery container and passenger flow paths

**Rationale**:
- Thermal runaway can produce **radiant heat** sufficient to ignite adjacent containers or materials
- 5-meter separation provides time for fire suppression activation and limits radiant heat flux to <5 kW/m²
- 3-meter separation from aircraft allows safe emergency disconnect without exposing fuselage to excessive heat

**Verification**: Thermal analysis modeling and fire testing per [UL 9540A](https://standardscatalog.ul.com/ProductDetail.aspx?productId=UL9540A)

### Electrical Safety Distance

**Objective**: Prevent electrical arc propagation and enable safe isolation

**Minimum Separation**:
- **2 meters** between high-voltage (>1000 VDC) CO₂ battery terminals and conductive structures
- **1 meter** between CO₂ battery container and non-Ex-rated electrical equipment
- **Clear approach zone** of 1.5 meters for emergency disconnect access

**Rationale**:
- Electrical arcing distance in air ~1 mm per kV; 2-meter separation provides large safety margin for CO₂ battery voltages (typically 800-1500 VDC)
- Access zone allows personnel to safely operate emergency disconnect without entering high-voltage proximity zone

**Verification**: High-voltage safety analysis per [IEC 60364-4-41](https://webstore.iec.ch/publication/1851)

### Access Control Zone

**Objective**: Prevent personnel entry during charging/discharging operations

**Zone Definition**:
- **3-meter radius** around CO₂ battery container during active charging/discharging
- Physical barriers (fencing, cones) or procedural controls (lockout/tagout)
- Visual indicators (lights, signs) showing container status

**Personnel Allowed**:
- Trained battery technicians with PPE (arc flash suit, insulated gloves)
- Emergency responders with appropriate PPE and training

**Exit Criteria**:
- Charging/discharging complete
- Container isolated electrically
- Surface temperature <50°C
- Visual and instrumented confirmation of safe state

## Passenger Flow Separation from Energy Systems

### Objective

Ensure passengers, crew, and non-essential personnel cannot inadvertently enter hazardous areas or interfere with energy system operations.

### BWB-Specific Challenges

The BWB configuration presents unique passenger flow challenges:
- **Wide fuselage** (~70 meters span) requires multiple boarding points
- **Central passenger compartment** is surrounded by propulsion and energy systems on outer edges
- **Large number of passengers** (400-500) creates high-density flows on stand

### Separation Requirements

| **Interface** | **Passenger Separation Distance** | **Physical Barrier Required?** | **Procedural Controls** |
|---------------|----------------------------------|-------------------------------|------------------------|
| H₂ refueling area | >10 meters (Zone 2 boundary) | Yes (during refueling) | No boarding during refueling |
| CO₂ battery container | >5 meters | Yes (when charging) | Container status indicators |
| High-voltage ground power | >3 meters | Yes (physical guards on connectors) | Visual warnings at connector |
| Aircraft vent outlets (H₂, fuel cell) | >2 meters | No (vent directed away from stand) | Vent outlet placards |
| GSE routing lanes | >1 meter | No | GSE speed limits, spotter required |

### Passenger Boarding Bridges and Stairs

**Design Criteria**:
- Boarding bridges must **not cross H₂ refueling zones** or CO₂ battery areas
- Stair positions selected to maintain **>5 meters** from energy system interfaces
- Emergency egress paths routed **away from** H₂ and CO₂ battery zones

**BWB Implementation**:
- **Forward boarding doors** (typical 2-3 doors on nose section) are >15 meters from H₂ refueling area (aft of wing)
- **Mid-fuselage doors** (typical 2-4 doors per side) positioned between wing roots, separated from underwing H₂ and CO₂ interfaces
- **Aft boarding doors** (1-2 doors) positioned >10 meters forward of APU and CO₂ battery area

See [ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg](ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg) for boarding door/bridge positioning on BWB stand.

## Rescue Vehicle Access Lanes and Clearances

### Objective

Ensure Airport Rescue and Fire Fighting (ARFF) vehicles can reach all BWB exits within **3 minutes** of emergency declaration, per [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx) and local airport regulations.

### Minimum Access Lane Widths

| **Vehicle Type** | **Lane Width (minimum)** | **Turning Radius** | **Vertical Clearance** |
|------------------|--------------------------|--------------------|----------------------|
| ARFF primary vehicle | 6 meters | 15 meters | 5 meters |
| ARFF support vehicle | 4 meters | 12 meters | 4 meters |
| Ambulance | 3.5 meters | 10 meters | 3.5 meters |
| Mobile stairs (emergency egress) | 5 meters | 8 meters | 4 meters |

### BWB-Specific Rescue Access Requirements

**Wide-Body Challenges**:
- BWB span (~70 meters) requires **multiple rescue access points** from different directions
- **Low ground clearance** (~2 meters at wing leading edge) may limit ARFF vehicle approach angles
- **Distributed exits** across wide fuselage require coordinated rescue from multiple sides

**Rescue Access Lanes on Stand**:
1. **Forward access lane**: Along nose, connects to taxiway, width ≥6 meters
2. **Port side access lane**: Parallel to fuselage port side, width ≥5 meters (may be narrower due to terminal proximity)
3. **Starboard side access lane**: Parallel to fuselage starboard side, width ≥6 meters (primary ARFF access)
4. **Aft access lane**: Behind tail, width ≥5 meters, connects to apron

**Exclusions from Access Lanes**:
- No H₂ refueling equipment parked in access lanes (must be positioned on stub taxiway or designated zone)
- No CO₂ battery containers in access lanes during passenger operations
- No GSE stored or parked in access lanes
- Boarding bridges must retract clear of access lanes in emergency

### Clearances Around Doors and Slides

**Slide Deployment Zones**:
- **10 meters** forward of door (for slide inflation and passenger flow)
- **3 meters** lateral of door (for slide width and rebound)
- **No obstacles >0.5 meters height** within slide deployment zone

**ARFF Equipment Positioning**:
- Mobile stairs can approach within **2 meters** of door sill
- ARFF vehicle boom/ladder can approach within **3 meters** of fuselage (standoff for stability)
- Foam/water application from **5-10 meters** (effective range of monitors)

**BWB-Specific Considerations**:
- **Overwing exits** may require specialized rescue platforms due to low wing height (~2-3 meters above ground)
- **Under-fuselage access** (if required for belly landing scenario) needs minimum 4-meter clearance and stable ground surface

See [ASSETS/85-00-02-A-004_Evacuation_and_Rescue_Scenarios.svg](ASSETS/85-00-02-A-004_Evacuation_and_Rescue_Scenarios.svg) for rescue access lane layout and slide deployment zones.

## GSE Routing and Separation

### Objective

Route ground support equipment (GSE) to service the aircraft without creating conflicts with energy interfaces, passenger flows, or rescue access lanes.

### GSE Categories and Routing

| **GSE Type** | **Approach Zone** | **Separation from H₂** | **Separation from CO₂** | **Separation from Passengers** | **Speed Limit** |
|--------------|-------------------|------------------------|------------------------|------------------------------|----------------|
| Catering truck | Forward/mid doors | >5 meters | >5 meters | 2 meters (when stationary) | 10 km/h |
| Baggage loader | Cargo doors (fwd/aft) | >10 meters | >5 meters | >5 meters | 10 km/h |
| Fuel/H₂ truck | Underwing H₂ connector | N/A (servicing point) | >10 meters | >10 meters (during ops) | 5 km/h |
| CO₂ battery transporter | Aft dock | >10 meters | N/A (servicing point) | >5 meters | 5 km/h |
| Ground power unit | Electrical connector | >5 meters | >3 meters | >3 meters | 10 km/h |
| Potable water truck | Service panel (fwd) | >5 meters | >5 meters | 2 meters (when stationary) | 10 km/h |
| Lavatory service | Service panel (aft) | >5 meters | >5 meters (or >3 if CO₂ isolated) | 2 meters (when stationary) | 10 km/h |

### GSE Routing Principles

1. **One-way flow** where possible to avoid GSE conflicts
2. **Designated GSE lanes** marked on stand (paint or lighting)
3. **Energy system priority**: H₂ and CO₂ operations have priority; other GSE must wait or reroute
4. **Spotter required** for GSE movements within 5 meters of aircraft or in congested areas
5. **Emergency stop**: All GSE stop immediately on "stand unsafe" declaration

## Stand Layout Design Principles

Integrating all safety zones and separation criteria into stand design:

1. **H₂ refueling position**: Aft/outboard of wing, >10 meters from passenger doors, >15 meters from terminal building
2. **CO₂ battery dock**: Aft fuselage, >10 meters from H₂, >5 meters from passenger areas, direct access to apron
3. **Passenger boarding**: Forward and mid-fuselage doors, >10 meters from all energy interfaces
4. **Rescue access lanes**: Perimeter clearance ≥5 meters, maintained clear at all times
5. **GSE staging area**: Outboard of aircraft, >5 meters from nose/tail, clear of rescue access lanes

See [ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg](ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg) for integrated stand layout.

## Verification and Compliance

### Design Verification

- **3D CAD modeling** of stand layout with BWB aircraft model, GSE, and energy equipment
- **Clearance analysis** for all separation distances (automated checks in CAD)
- **Rescue access simulation** (ARFF vehicle routing and timing)
- **Evacuation modeling** (passenger flow simulation with slide deployment)

### Operational Compliance

- **Stand certification**: Airport authority certifies stand layout meets all safety zone requirements
- **Periodic inspections**: Quarterly verification of marking, signage, and physical barriers
- **Operational audits**: Safety observations during turnaround operations to verify procedural compliance
- **Non-compliance reporting**: Any separation distance violation triggers immediate "stand unsafe" declaration and investigation

## Related Documents

- [85-00-02-001_Safety_Concepts_and_Objectives.md](85-00-02-001_Safety_Concepts_and_Objectives.md) - Safety objectives
- [85-00-02-002_Hazard_Analysis_at_Interface_Level.md](85-00-02-002_Hazard_Analysis_at_Interface_Level.md) - Interface hazards
- [85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md](85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md) - Energy interface safety
- [85-00-02-005_Passenger_Evacuation_and_Rescue_Safety_Interfaces.md](85-00-02-005_Passenger_Evacuation_and_Rescue_Safety_Interfaces.md) - Evacuation interfaces
- [85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md](85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md) - Operational procedures
- [ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg](ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg) - Stand layout diagram

## References

- **[IEC 60079-10-1](https://webstore.iec.ch/publication/632)**: Explosive atmospheres — Part 10-1: Classification of areas — Explosive gas atmospheres
- **[NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code)**: Hydrogen Technologies Code (Chapter 7: Fueling)
- **[ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx)**: Aerodromes — Volume I: Aerodrome Design and Operations
- **[UL 9540A](https://standardscatalog.ul.com/ProductDetail.aspx?productId=UL9540A)**: Test Method for Evaluating Thermal Runaway Fire Propagation in Battery Energy Storage Systems
- **[IEC 60364-4-41](https://webstore.iec.ch/publication/1851)**: Low-voltage electrical installations — Part 4-41: Protection for safety — Protection against electric shock
- **IATA Airport Handling Manual (AHM)**: Section on Aircraft Stand Design

## Document Control

- **Owner**: AMPEL360 Safety & Certification Team
- **Approver**: Chief Safety Officer
- **Review Frequency**: Quarterly
- **Next Review**: 2026-02-21
- **Repository**: AMPEL360-BWB-H2-Hy-E
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **DRAFT** – Subject to human review and approval
- Human approver: _[to be completed]_
- Last AI update: 2025-11-21

---
*This document is part of the AMPEL360 OPT-IN Framework certification package.*
