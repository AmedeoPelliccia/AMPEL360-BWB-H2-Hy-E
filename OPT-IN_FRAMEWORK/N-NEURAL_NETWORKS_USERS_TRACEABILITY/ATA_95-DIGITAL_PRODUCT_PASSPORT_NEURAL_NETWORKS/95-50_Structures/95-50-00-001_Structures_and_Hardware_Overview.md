# 95-50-00-001 Structures and Hardware Overview

**Document ID:** 95-50-00-001  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. Introduction

This document provides a comprehensive overview of all hardware structures and physical carriers required to integrate Neural Network (NN) systems, sensors, and computing hardware throughout the AMPEL360 BWB-H2-Hy-E aircraft.

### 1.1 Purpose

Define the physical infrastructure that supports:
- **NN Computing Hardware** – IMA racks, server chassis, GPU accelerators
- **Sensors & Instrumentation** – Temperature, pressure, flow, vision systems
- **Data Acquisition** – Recorders, storage units, network switches
- **Power Distribution** – Electrical cabinets, battery modules, fuel cell interfaces
- **Fuel Systems** – H₂ tank supports, manifold racks, valve assemblies

### 1.2 Scope

This chapter covers **mounting structures, racks, brackets, and installation hardware** for NN systems across all ATA chapters. It does NOT cover:
- Functional design of systems (see ATA 95-20 Subsystems)
- Software architecture (see ATA 95-40 Software)
- Operational procedures (see ATA 95-10 Operations)

---

## 2. Hardware Structure Categories

### 2.1 Equipment Racks and Bays

**Purpose:** House LRUs, compute modules, and electronic systems

**Types:**
- **IMA Racks (95-50-42)** – Integrated Modular Avionics chassis with backplanes
- **Server Racks (95-50-46)** – 19" standard racks for information systems
- **Electrical Cabinets (95-50-24)** – Power distribution, circuit breakers, busses
- **ECS Racks (95-50-21)** – Environmental control sensors and actuators
- **Recorder Racks (95-50-31)** – FDR, CVR, and data storage modules

**Key Requirements:**
- Shock and vibration isolation per [RTCA DO-160G](https://www.rtca.org/content/standards-guidance-materials)
- Thermal management (air cooling, liquid cooling, heat sinks)
- [EMI](https://en.wikipedia.org/wiki/Electromagnetic_interference)/[RFI](https://en.wikipedia.org/wiki/Radio-frequency_interference) shielding
- Quick-release mechanisms for [LRU](https://en.wikipedia.org/wiki/Line-replaceable_unit) replacement
- Cable management and strain relief

### 2.2 Sensor and Antenna Mounts

**Purpose:** Position sensors and antennas for optimal coverage and performance

**Types:**
- **Wing-mounted sensors (95-50-57)** – Ice detection, temperature probes
- **Pylon-mounted sensors (95-50-70)** – Engine health monitoring, vibration
- **Fuselage-mounted antennas (95-50-53)** – Communications, navigation, weather radar

**Key Requirements:**
- Aerodynamic fairings to minimize drag
- Lightning protection and bonding
- Access panels for maintenance
- Thermal protection in hot zones

### 2.3 Cable Routing Structures

**Purpose:** Organize and protect wiring harnesses and fiber optic cables

**Types:**
- **Cable trays (95-50-24)** – Ladder-type or solid bottom
- **Conduits** – Metal or composite for harsh environments
- **Clamps and tie-downs** – Vibration resistance, chafe protection
- **Grommets and pass-throughs** – Sealed penetrations through bulkheads

**Key Requirements:**
- Separation from hydraulic lines and hot structures
- Bonding to aircraft ground
- Accessibility for inspection and repair
- Fire-resistant materials

### 2.4 Tank and Fuel System Supports

**Purpose:** Secure cryogenic H₂ tanks and fuel distribution hardware

**Types:**
- **Tank cradles (95-50-28)** – Support H₂ tanks with thermal expansion accommodation
- **Manifold brackets** – Mount valves, sensors, and distribution piping
- **Insulation shields** – Thermal barriers between cold tanks and warm structure
- **Firewall structures** – Separation between fuel zones and occupied areas

**Key Requirements:**
- Load paths for crash loads ([EASA CS-25.561](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27))
- Thermal expansion joints
- Leak detection integration
- Fire-resistant materials ([FAR 25.853](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-D/subject-group-ECFR61b1513e00c1bd8/section-25.853))

### 2.5 Access Panels and Doors

**Purpose:** Provide maintenance access to installed equipment

**Types:**
- **Quick-access panels** – Tool-less or quarter-turn fasteners
- **Service doors** – Larger openings for LRU removal
- **Inspection ports** – Visual checks without equipment removal

**Key Requirements:**
- Pressure sealing where required
- Flush or low-profile external finish
- Clear labeling and placarding
- Captive fasteners to prevent FOD

---

## 3. Integration with Aircraft Structure

### 3.1 Fuselage Bays (ATA 53)

**Equipment Bays:**
- **Forward avionics bay** – IMA racks, electrical cabinets
- **Mid-fuselage electronics bay** – Information systems, recorders
- **Aft equipment bay** – APU support structures

**Design Considerations:**
- Floor reinforcement for heavy racks
- Cable runs through frames and stringers
- Cooling air ducting from ECS
- Access from cabin or exterior service doors

### 3.2 Wing Structures (ATA 57)

**Wing Box Integration:**
- **Leading edge** – Ice detection sensors, pitot-static probes
- **Trailing edge** – Antenna mounts in winglets or tips
- **Wing-to-body fairing** – Wiring transitions, sensor clusters

**Design Considerations:**
- Vibration from wing bending
- Temperature extremes (cold soak at altitude)
- Lightning strike protection
- Aerodynamic cleanness

### 3.3 Pylon and Nacelle Structures (ATA 70-79)

**Engine Integration:**
- **Pylon equipment bay** – Engine control units, fuel control
- **Nacelle-mounted sensors** – Vibration, temperature, pressure
- **Thrust reverser structures** – Mounting for sensors and actuators

**Design Considerations:**
- High vibration environment
- High temperature zones
- Fire-resistant materials
- Rapid access for line maintenance

---

## 4. Structural Load Paths

### 4.1 Static Loads

**Sources:**
- Equipment weight (gravity)
- Pressurization loads (fuselage)
- Thermal expansion (H₂ tanks, hot structures)

**Analysis:**
- [FEA](https://en.wikipedia.org/wiki/Finite_element_analysis) verification of attach fittings
- Margin of safety calculations per [EASA CS-25.303](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)
- Fatigue life assessment

### 4.2 Dynamic Loads

**Sources:**
- Flight maneuvers (limit and ultimate loads)
- Landing and ground loads
- Engine vibration transmission
- Aerodynamic buffet

**Analysis:**
- [Modal analysis](https://en.wikipedia.org/wiki/Modal_analysis) to avoid resonance
- Shock and vibration testing per [RTCA DO-160G](https://www.rtca.org/content/standards-guidance-materials)
- Random vibration profiles for each zone

### 4.3 Crash Loads

**Requirements:**
- Emergency landing ([EASA CS-25.561](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27))
- Crashworthiness of fuel systems ([EASA CS-25.963](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27))
- Retention of heavy equipment

**Analysis:**
- Dynamic drop tests for seat structures
- Sled tests for equipment mounts
- Finite element simulation of crash scenarios

---

## 5. Material Selection

### 5.1 Metallic Structures

**Aluminum Alloys:**
- [7075-T6](https://en.wikipedia.org/wiki/7075_aluminium_alloy) for high-strength brackets
- [6061-T6](https://en.wikipedia.org/wiki/6061_aluminium_alloy) for general-purpose racks
- [2024-T3](https://en.wikipedia.org/wiki/2024_aluminium_alloy) for sheet metal panels

**Titanium Alloys:**
- [Ti-6Al-4V](https://en.wikipedia.org/wiki/Ti-6Al-4V) for high-temperature mounts (near engines)
- Corrosion-resistant in H₂ environment

**Stainless Steel:**
- CRES 321 for firewall structures
- CRES 15-5PH for high-strength fasteners

### 5.2 Composite Structures

**Carbon Fiber (CFRP):**
- Equipment bay panels for weight reduction
- EMI shielding with conductive layers

**Glass Fiber (GFRP):**
- Antenna radomes
- Non-load-bearing fairings

**Aramid Fiber (Kevlar):**
- Fire-resistant barriers
- Ballistic protection for critical systems

### 5.3 Surface Treatments

**Corrosion Protection:**
- Anodize (aluminum)
- Alodine (chromate conversion coating)
- Primer and paint systems

**Bonding and Grounding:**
- Cadmium plate on fasteners
- Aluminum spray on composite surfaces for conductivity

---

## 6. Installation Standards

### 6.1 Fastener Selection

**Thread Types:**
- **[UNJ threads](https://en.wikipedia.org/wiki/Unified_Thread_Standard)** – Aerospace standard for bolts
- **UNJF** – Fine threads for thin sections
- **Self-locking nuts** – Prevailing torque or nylon inserts

**Torque Specifications:**
- Per [MIL-STD-1312](https://assist.dla.mil/online/start/) or manufacturer specifications
- Torque seals for inspection
- Controlled tightening sequence for multiple-fastener joints

### 6.2 Bonding and Grounding

**Electrical Bonding:**
- Bonding jumpers across joints per [SAE AS50881](https://www.sae.org/standards/content/as50881/)
- Maximum resistance: 2.5 milliohms
- Bonding to aircraft structure for [lightning protection](https://en.wikipedia.org/wiki/Lightning_protection)

**Grounding Points:**
- Designated grounding studs on equipment racks
- Separation of digital and analog grounds
- Star grounding topology for sensitive electronics

### 6.3 Safety Wiring

**Applications:**
- Fasteners on critical structures (flight controls, engine mounts)
- Fluid fittings (hydraulic, fuel, oxygen)
- Electrical connectors in high-vibration zones

**Standards:**
- [SAE AS50881](https://www.sae.org/standards/content/as50881/) (wiring practices)
- [AC 43.13-1B](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/99861) (acceptable methods)

---

## 7. Thermal Management

### 7.1 Cooling Requirements

**Air-Cooled Equipment:**
- Forced convection from ECS ducts
- Natural convection with heat sinks
- Inlet and exhaust vents with filters

**Liquid-Cooled Equipment:**
- Fuel cell stacks and power inverters
- Liquid-to-air heat exchangers
- Coolant routing and leak containment

### 7.2 Thermal Barriers

**Hot Zones:**
- APU compartment (up to 500°C)
- Engine pylons (up to 400°C)
- Exhaust ducts

**Cold Zones:**
- H₂ tanks (-253°C)
- Cryogenic valves and piping

**Insulation Materials:**
- Multi-layer insulation (MLI) for cryogenics
- Ceramic blankets for high-temperature zones
- Closed-cell foam for moderate insulation

---

## 8. Maintenance and Access

### 8.1 Access Philosophy

**Categories:**
- **Daily checks** – Visual inspection through ports
- **Line maintenance** – LRU replacement via quick-access panels
- **Base maintenance** – Major component removal via service doors

**Design Guidelines:**
- Equipment removal paths clear of interference
- Lifting eyes or handles on heavy units
- Clear placarding of access panel functions

### 8.2 CAOS Integration

**Digital Twin Hooks:**
- 3D position data for all structures
- Sensor locations for predictive maintenance
- Access panel schedules linked to maintenance tasks

**Real-Time Monitoring:**
- Structural health monitoring sensors
- Thermal load tracking
- Vibration analysis for early fault detection

---

## 9. Cross-References

### 9.1 Within ATA 95
- **[95-00-13 Subsystems & Components](../../95-00_GENERAL/95-00-13_Subsystems_Components/)** – Hardware parts list
- **[95-20 Subsystems](../../95-20_Subsystems/)** – Functional system descriptions
- **[95-30 Circularity](../../95-30_Circularity/)** – End-of-life disassembly

### 9.2 To Other ATA Chapters
- **[ATA 21 - ECS](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E1-ENVIRONMENT/ATA_21-AIR_CONDITIONING_AND_PRESSURIZATION/)** – Cooling ducts and manifolds
- **[ATA 24 - Electrical](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_24-ELECTRICAL_POWER/)** – Power distribution racks
- **[ATA 28 - Fuel](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENIC_SYSTEMS/ATA_28-FUEL_SAF_AND_CRYOGENIC/)** – H₂ tank supports
- **[ATA 53 - Fuselage](../../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_53-FUSELAGE/)** – Equipment bay structure

---

## 10. Document Control

| Version | Date       | Author                     | Changes                |
|---------|------------|----------------------------|------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Documentation Team | Initial creation       |

---

**Maintained by:** AMPEL360 Structures Team  
**Contact:** structures@ampel360.aero
