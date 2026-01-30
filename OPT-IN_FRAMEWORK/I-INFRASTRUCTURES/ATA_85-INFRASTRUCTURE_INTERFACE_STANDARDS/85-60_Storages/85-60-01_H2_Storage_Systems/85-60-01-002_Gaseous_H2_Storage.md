# 85-60-01-002 — Gaseous H2 Storage

## Document Metadata

```yaml
document_id: "85-60-01-002"
title: "Gaseous H2 Storage"
parent_system: "85-60-01 H2 Storage Systems"
category: "Storage Equipment"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-22"
```

## Purpose

This document defines the requirements, design specifications, and operational procedures for gaseous hydrogen (GH2) storage systems used in ground infrastructure to support AMPEL360 BWB-H2-Hy-E aircraft refueling operations.

## GH2 Storage Overview

### Applications

1. **Primary Storage:** Direct compression of H2 gas from electrolysis or delivery
2. **Buffer Storage:** Intermediate storage between LH2 vaporization and aircraft refueling
3. **Cascade Systems:** Multi-bank storage for efficient high-pressure dispensing

### Advantages vs. LH2

- No cryogenic handling required (simpler operations)
- Lower capital cost for small-scale storage (<5,000 kg)
- No boil-off losses
- Faster response time for refueling demand

### Disadvantages vs. LH2

- Lower volumetric energy density (requires more space)
- Higher compression energy (0.5-2 kWh/kg H2 for 350-700 bar)
- Pressure cycling fatigue (limits vessel lifetime)
- Higher capital cost for large-scale storage (>10,000 kg)

## GH2 Vessel Types

### Type I: All-Metal Vessels

**Construction:** Steel or aluminum
**Pressure Rating:** Up to 200 bar (typical)
**Applications:** Low-pressure buffer storage, legacy systems
**Advantages:** Low cost, proven technology
**Disadvantages:** Heavy, limited pressure rating

### Type II: Metal Liner with Hoop Wrap

**Construction:** Metal liner (steel or aluminum) with composite hoop wrap (fiberglass)
**Pressure Rating:** Up to 300 bar
**Applications:** Moderate-pressure storage
**Advantages:** Lighter than Type I, moderate cost
**Disadvantages:** Heavier than Type III/IV, limited pressure rating

### Type III: Metal Liner with Full Wrap

**Construction:** Aluminum or steel liner with full composite wrap (carbon fiber or fiberglass)
**Pressure Rating:** 350-700 bar
**Applications:** High-pressure cascade storage for aircraft refueling
**Advantages:** High pressure rating, proven in automotive H2 applications
**Disadvantages:** Higher cost, requires periodic inspection

### Type IV: Polymer Liner with Full Wrap

**Construction:** HDPE (High-Density Polyethylene) liner with carbon fiber wrap
**Pressure Rating:** 350-700 bar
**Applications:** High-pressure cascade storage, lightweight installations
**Advantages:** Lightest weight, no metal liner corrosion, excellent fatigue resistance
**Disadvantages:** Highest cost, H2 permeation through polymer liner (minimal but measurable)

**Recommended for AMPEL360:** Type III or IV vessels for 350 bar cascade storage

See: [85-60-01-A-001_Tank_Specifications.csv](./ASSETS/85-60-01-A-001_Tank_Specifications.csv)

## Cascade Storage System

### Concept

A cascade system uses multiple banks of GH2 vessels at different pressures to efficiently dispense H2 to aircraft without excessive compression cycling.

**Configuration:**
- **Low-Pressure Bank:** 150-250 bar (fills aircraft from 0 to ~150 bar)
- **Medium-Pressure Bank:** 250-400 bar (fills aircraft from ~150 to ~250 bar)
- **High-Pressure Bank:** 400-500 bar (fills aircraft from ~250 to target pressure)

**Advantages:**
- Minimizes compression energy (vessels refilled in batches, not per aircraft)
- Reduces pressure cycling and vessel fatigue
- Enables faster refueling (higher pressure differential drives flow rate)

### Sizing

**Cascade Rule of Thumb:** Total GH2 storage capacity = 3-5x aircraft tank capacity

**Example for 500 kg H2 Aircraft:**
- Aircraft tank: 500 kg at 350 bar (assuming Type III COPV, ~1,900 liters geometric)
- Cascade storage: 1,500-2,500 kg GH2
- Typical distribution: 30% low bank, 40% medium bank, 30% high bank

**Refueling Cycles:** Size cascade to support 3-5 aircraft refuelings before requiring compressor recharge

See: [85-60-01-A-004_Capacity_Planning.md](./ASSETS/85-60-01-A-004_Capacity_Planning.md)

## Design Requirements

### Pressure Rating

**Design Pressure:** 1.5x maximum operating pressure (per [ISO 11119](https://www.iso.org/standard/68620.html))

**Maximum Operating Pressure:**
- **350 bar systems:** Design pressure 525 bar
- **700 bar systems:** Design pressure 1,050 bar

**Pressure Relief:**
- Thermally-activated pressure relief device (TPRD) per [ISO 19881](https://www.iso.org/standard/66394.html)
- Set pressure: Design pressure or lower

### Material Selection

**Composite Materials (Type III/IV):**
- **Fiber:** Carbon fiber (T700, T800) or fiberglass (E-glass)
- **Resin:** Epoxy (typical) or polyester
- **Liner:** Aluminum 6061-T6 (Type III) or HDPE (Type IV)

**Environmental Considerations:**
- UV resistance (outdoor installations)
- Temperature range: -40°C to +85°C
- Humidity and salt spray resistance (coastal locations)

### Pressure Cycling and Fatigue

**Design Life:** Minimum 15,000 pressure cycles (per [ISO 11119-3](https://www.iso.org/standard/70754.html))

**Pressure Cycle Definition:** 0-100% maximum operating pressure

**Testing:**
- Hydraulic cycle test to 2x design life (30,000 cycles)
- Burst test on representative samples (>2.25x design pressure)

**In-Service Monitoring:**
- Cycle counting (track pressure cycles per vessel)
- Retire vessels at end of design life or per manufacturer recommendation

## Installation and Layout

### Vessel Mounting

**Orientation:** Horizontal or vertical (horizontal preferred for ease of piping)

**Support:** Saddle supports (horizontal) or skirt support (vertical)

**Restraint:** Seismic restraints per local building codes (e.g., [ASCE 7](https://www.asce.org/publications-and-news/asce-7))

### Manifolding

**High-Pressure Manifolds:**
- Stainless steel tubing or pipe (e.g., 316 SS)
- Wall thickness per [ASME B31.3](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping) for H2 service
- Minimize dead volume (reduces trapped H2 and improves efficiency)

**Isolation Valves:**
- Ball valves or automated valves per bank
- Manual isolation for maintenance
- Pressure indication per bank

### Safety Distances

Per [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2):

- **To occupied buildings:** 25 meters (350 bar), 50 meters (700 bar)
- **Between vessel banks:** 3 meters or vessel diameter, whichever is greater
- **To lot lines:** Per risk assessment (typically 15-25 meters)
- **To ignition sources:** 10 meters minimum

## Instrumentation and Controls

### Pressure Monitoring

**Pressure Transmitters:**
- One per bank (minimum)
- Redundant transmitters for critical applications (safety-rated)
- Range: 0-600 bar (for 350 bar system), 0-1,000 bar (for 700 bar system)

**Pressure Switches:**
- High-pressure alarm (e.g., 95% of design pressure)
- Low-pressure warning (e.g., refill required)

### Temperature Monitoring

**RTDs or Thermocouples:**
- Monitor vessel temperature (affects H2 density and pressure)
- Detect abnormal heating (fire, rapid filling, external heat source)

### Flow Metering

**Mass Flow Meters:**
- Coriolis or thermal mass flow meters
- Measure H2 dispensed to aircraft
- Accuracy: ±1% or better (for billing and inventory)

## Safety Systems

### H2 Detection

**Fixed H2 Sensors:**
- Near vessels, manifolds, and valves
- Minimum 4 sensors per vessel bank
- Alarm setpoint: 0.4% H2 by volume (10% LEL)

See: [85-20-08 Safety and Monitoring Subsystem](../../85-20_Subsystems/85-20-08_Safety_and_Monitoring_Subsystem/README.md)

### Fire Protection

**Passive Protection:**
- Vessel coatings (fire-resistant or insulating coatings for prolonged fire exposure)
- Spacing and separation (minimize fire spread)

**Active Protection:**
- Water deluge or spray system (cool vessels during fire)
- Automatic activation on flame detection
- Manual activation capability

### Pressure Relief

**Thermally-Activated PRD (TPRD):**
- Activates at ~110°C (prevents vessel rupture in fire)
- Vents H2 to safe location (upward or to flare stack)
- Disposable device (must be replaced after activation)

**Pressure Relief Valve (PRV):**
- Backup for TPRD or for non-fire overpressure events
- Set at design pressure
- Vent to safe location

### Emergency Shutdown (ESD)

**ESD Triggers:**
- H2 detection >0.4% by volume
- Fire detection
- High vessel pressure (>95% design pressure)
- Manual ESD button

**ESD Actions:**
1. Close all fill and dispense valves
2. Isolate vessel banks (if automated valves installed)
3. Activate water deluge (if fire detected)
4. Sound alarm and notify ARFF

## Operational Procedures

### Normal Operations

**Daily Inspections:**
- Visual check of vessels and piping for damage or leaks
- Verify pressure readings for each bank
- Check H2 detection system operational
- Review cycle count logs

**GH2 Fill Procedure (from Compressor or Vaporizer):**
1. Verify high-pressure bank has capacity
2. Open isolation valves to bank being filled
3. Start compressor or vaporizer
4. Monitor fill pressure and rate
5. Stop fill when target pressure reached (e.g., 450 bar for high bank)
6. Close isolation valves
7. Log fill quantity and bank pressures

**Aircraft Refueling (Cascade Dispensing):**
1. Connect refueling hose to aircraft (per [85-20-01 H2 Refueling Interface](../../85-20_Subsystems/85-20-01_H2_Refueling_Interface_Subsystem/README.md))
2. Dispense from low-pressure bank until pressure equalized
3. Switch to medium-pressure bank
4. Switch to high-pressure bank for final fill
5. Monitor total quantity dispensed
6. Disconnect and log transaction

### Maintenance

**Monthly:**
- Visual inspection of vessels and supports
- Check TPRD mounting and condition
- Test H2 detectors (bump test)

**Quarterly:**
- Inspect high-pressure piping and fittings
- Test ESD system (simulated)
- Review cycle count and compare to design life

**Annual:**
- Vessel external visual inspection (per [ISO 11119](https://www.iso.org/standard/68620.html))
- PRV testing (remove and bench test, or in-place test)
- Leak test of piping and connections (soap solution or sniffer)

**End of Design Life:**
- Retire vessels per manufacturer recommendation
- Disposal or recertification (if allowed by manufacturer)

### Emergency Procedures

**GH2 Leak:**
1. Activate ESD (close isolation valves)
2. Evacuate personnel upwind
3. Notify ARFF (establish safety perimeter, minimum 100m)
4. Monitor H2 concentration (safe approach after H2 dispersed)
5. Identify and isolate leaking vessel or component

**Fire Near GH2 Storage:**
1. Activate water deluge (cool vessels, prevent TPRD activation or vessel failure)
2. Evacuate area (minimum 300m)
3. Notify ARFF (defensive operations, protect exposures)
4. If TPRD activates, allow H2 to vent and burn (do not extinguish unless leak can be stopped)
5. After fire, inspect vessels for damage before returning to service

## Standards and References

### Design and Construction

- [ISO 11119-3](https://www.iso.org/standard/70754.html) — Gas cylinders — Refillable composite gas cylinders — Part 3: Fully wrapped fibre reinforced composite gas cylinders with non-load-sharing metallic or non-metallic liners
- [ASME B31.3](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping) — Process Piping (for H2 piping design)
- [ISO 19881](https://www.iso.org/standard/66394.html) — Gaseous hydrogen — Land vehicle fuel containers

### Safety and Operations

- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code
- [SAE J2579](https://www.sae.org/standards/content/j2579/) — Technical Information Report for Fuel Systems in Fuel Cell and Other Hydrogen Vehicles
- [ISO 19880-5](https://www.iso.org/standard/71975.html) — Gaseous hydrogen — Fueling stations — Part 5: Dispenser hoses and hose assemblies

### Testing and Inspection

- [ISO 11623](https://www.iso.org/standard/70909.html) — Transportable gas storage devices — Periodic inspection and testing of composite gas cylinders
- [CSA B51](https://www.csagroup.org/store/product/CSA%20B51:19/) — Boiler, Pressure Vessel, and Pressure Piping Code (Canada)

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

*Reference: [85-60-01 H2 Storage Systems README](./README.md)*
