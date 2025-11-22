# 85-60-01-001 — Liquid H2 Tanks

## Document Metadata

```yaml
document_id: "85-60-01-001"
title: "Liquid H2 Tanks"
parent_system: "85-60-01 H2 Storage Systems"
category: "Storage Equipment"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-22"
```

## Purpose

This document defines the requirements, design specifications, and operational procedures for liquid hydrogen (LH2) storage tanks used in ground infrastructure to support AMPEL360 BWB-H2-Hy-E aircraft refueling operations.

## LH2 Properties and Handling Requirements

### Physical Properties

- **Boiling Point:** -252.87°C (-423.17°F) at 1 atm
- **Density (liquid):** ~71 kg/m³ at NBP (Normal Boiling Point)
- **Density (gas):** 0.08988 kg/m³ at STP
- **Expansion Ratio:** 1:848 (liquid to gas at 15°C)
- **Heat of Vaporization:** 446 kJ/kg

### Storage Challenges

1. **Cryogenic Temperature:** Requires vacuum insulation to minimize heat ingress
2. **Low Density:** Requires large tank volumes for practical fuel quantities
3. **Boil-Off:** Continuous evaporation due to heat ingress (0.2-0.5% per day typical)
4. **Ortho-Para Conversion:** Releases heat, requiring catalytic conversion or time for equilibration
5. **Embrittlement:** Most structural materials become brittle at LH2 temperatures

## Tank Design Requirements

### Tank Construction

**Type:** Double-wall, vacuum-insulated cryogenic vessel per [EN 13458](https://standards.cencenelec.eu/)

**Materials:**
- **Inner vessel:** Austenitic stainless steel (e.g., 304L, 316L) or aluminum alloy (e.g., 5083)
- **Outer vessel:** Carbon steel or stainless steel
- **Insulation:** Multi-layer insulation (MLI) or perlite powder in vacuum space

**Orientation:** Vertical or horizontal (horizontal preferred for large capacities)

### Capacity and Sizing

**Typical Sizes:**
- **Small:** 50,000 liters (3,550 kg H2)
- **Medium:** 150,000 liters (10,650 kg H2)
- **Large:** 500,000 liters (35,500 kg H2)

**Sizing Criteria:**
- Aircraft fleet size and refueling frequency
- Daily H2 consumption rate
- Delivery truck capacity and frequency
- Minimum 3-5 days operational reserve

See: [85-60-01-A-004_Capacity_Planning.md](./ASSETS/85-60-01-A-004_Capacity_Planning.md)

### Pressure Rating

**Design Pressure:** Typically 10-16 bar (150-232 psi)

**Operating Pressure:** 1-10 bar (14.5-145 psi)

**Rationale:** Low pressure minimizes tank wall thickness and cost, while providing sufficient head pressure for transfer operations.

**Pressure Relief:** Multiple pressure relief valves (PRVs) set at design pressure

### Insulation Performance

**Target Heat Ingress:** <0.5 W/m² of tank surface area

**Vacuum Quality:** <10^-4 mbar (high vacuum)

**Boil-Off Rate:** <0.3% per day for well-designed systems

**Insulation Types:**
- **MLI (Multi-Layer Insulation):** 20-60 layers of reflective film (e.g., aluminized Mylar)
- **Perlite:** Granular insulation in evacuated space (alternative to MLI)
- **Vacuum:** Eliminates conductive and convective heat transfer

## Tank Components and Systems

### Fill and Drain

**LH2 Fill Connection:**
- Vacuum-insulated bayonet-type coupling
- Compatible with tanker truck delivery hoses
- Located for easy tanker access

**Vapor Return Line:**
- Returns boil-off vapor to tanker during fill (pressure equalization)
- Prevents over-pressurization of delivery tank

**LH2 Withdrawal:**
- Bottom withdrawal (highest pressure, liquid phase)
- Top withdrawal (for vapor return or vaporizer feed)

### Pressure Management

**Pressure Building Coil:**
- Internal heat exchanger to vaporize small amount of LH2
- Increases tank pressure for transfer operations (e.g., 6-10 bar)

**Pressure Relief Valves (PRVs):**
- Primary PRV set at design pressure (e.g., 16 bar)
- Secondary PRV as backup
- Vent to safe location (minimum 3m above grade, away from ignition sources)

**Burst Disc:**
- Fail-safe overpressure protection
- Set above PRV setpoint (e.g., 20 bar)

### Level and Instrumentation

**Level Measurement:**
- Differential pressure transmitter (most common)
- Capacitance probe (alternative)
- Float gauge (simple mechanical backup)

**Temperature Sensors:**
- Multiple RTDs (Resistance Temperature Detectors) in liquid space
- Monitor for stratification and para-ortho conversion heat

**Pressure Transmitters:**
- Tank pressure monitoring
- Vacuum space pressure monitoring (for insulation integrity)

**Alarms:**
- High/low level
- High pressure
- Low vacuum (insulation failure)
- High H2 concentration near tank

## Safety Systems

### H2 Detection

**Fixed H2 Sensors:**
- Locations: Near tank vents, fill connection, transfer lines, and low points
- Quantity: Minimum 4 sensors per tank (redundancy for safety-critical)
- Alarm setpoints: 0.4% H2 by volume (10% LEL)

See: [85-20-08 Safety and Monitoring Subsystem](../../85-20_Subsystems/85-20-08_Safety_and_Monitoring_Subsystem/README.md)

### Fire Protection

**Water Deluge System:**
- Purpose: Cool tank in case of fire (prevent BLEVE — Boiling Liquid Expanding Vapor Explosion)
- Activation: Manual or automatic (flame detection)
- Coverage: Entire tank surface, minimum 10 L/min/m²

**Fire Detection:**
- Flame detectors (UV/IR) around tank perimeter
- Thermal imaging cameras

### Emergency Shutdown (ESD)

**ESD Triggers:**
- H2 detection >0.4% by volume
- Fire detection
- Tank over-pressure
- Loss of vacuum insulation (high vacuum pressure)
- Manual ESD button

**ESD Actions:**
1. Close all fill and transfer valves
2. Activate water deluge (if fire detected)
3. Sound audible alarm
4. Notify ARFF and operations center

### Grounding and Bonding

**Requirements:**
- Tank bonded to ground grid (resistance <10 ohms)
- All transfer hoses include bonding wires
- Periodic resistance testing (annual)

## Siting and Layout

### Separation Distances

Per [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2):

- **To occupied buildings:** 50 meters minimum
- **To lot lines:** 25 meters minimum (or per risk assessment)
- **Between LH2 tanks:** 3 meters or tank diameter, whichever is greater
- **To ignition sources:** 25 meters minimum
- **To emergency exits:** Sufficient for safe evacuation

### Access and Egress

- Minimum two means of egress from tank area
- Clear access for emergency vehicles (ARFF)
- Paved surface for tanker delivery

### Containment

**Spill Containment:**
- Impoundment area sized for 110% of tank capacity
- Sloped to drain away from critical equipment
- Remote ignition sources from potential LH2 pool

**Note:** LH2 spills vaporize rapidly; containment primarily for LH2 tanker failures during transfer.

## Operational Procedures

### Normal Operations

**Daily Inspections:**
- Visual check for frost or ice formation (indicates insulation failure or leak)
- Check pressure and level readings
- Verify H2 detection system operational
- Check vacuum integrity (if vacuum gauge installed)

**LH2 Fill Procedure:**
1. Confirm tank has capacity for delivery
2. Position tanker truck in designated fill area
3. Establish bonding between tanker and tank
4. Connect fill hose and vapor return line
5. Purge air from hoses with H2 vapor
6. Open valves and begin transfer (monitor flow rate and pressures)
7. Close valves when target level reached
8. Bleed pressure from hoses before disconnect
9. Disconnect hoses and stow
10. Log delivery quantity and tank level

**Boil-Off Management:**
- Capture boil-off vapor for use in vaporizers or compressors (preferred)
- Vent safely if capture not possible (minimize waste)
- Monitor and trend boil-off rate (indicator of insulation performance)

### Emergency Procedures

**LH2 Leak:**
1. Activate ESD (close all valves)
2. Evacuate personnel upwind of leak
3. Notify ARFF (do not approach leak with ignition sources)
4. Establish safety perimeter (minimum 100 meters)
5. Allow LH2 to vaporize naturally (do not attempt to contain)
6. Monitor with H2 detectors (safe approach only after H2 dispersed)

**Fire Near LH2 Tank:**
1. Activate water deluge system (cool tank, prevent BLEVE)
2. Evacuate area (minimum 300 meters)
3. Notify ARFF (defensive operations only — protect exposures, allow H2 to burn off)
4. Do not extinguish H2 fire unless leak can be stopped (re-ignition hazard)

**Tank Over-Pressure:**
1. PRV should automatically relieve pressure
2. Investigate cause (external fire, loss of vacuum insulation, pressure building coil malfunction)
3. If PRV fails to relieve, activate ESD and evacuate
4. ARFF to cool tank with water spray (if safe to approach)

## Maintenance

### Preventive Maintenance

**Monthly:**
- Inspect tank exterior for damage or corrosion
- Check PRV vent stack for obstructions
- Test H2 detectors (bump test)
- Check bonding connections

**Quarterly:**
- Inspect fill and transfer couplings for damage
- Verify vacuum integrity (if equipped with vacuum gauge)
- Test ESD system (simulated activation)

**Annual:**
- PRV inspection and recertification (per ASME or EN standards)
- Vacuum pump-down (if vacuum has degraded)
- Leak test of inner vessel (if accessible)
- Full safety system inspection (H2 detectors, fire detection, deluge system)

### Tank Inspection

**External Visual Inspection:** Annual (per [ASME BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-division-1-rules-construction-pressure-vessels))

**Internal Inspection:** Every 10 years (requires tank warm-up, purge, and entry — significant operation)

**Non-Destructive Testing (NDT):**
- Ultrasonic testing (UT) of welds and critical areas
- Radiographic testing (RT) if structural concerns
- Performed during internal inspection or as needed

## Standards and References

### Design and Construction

- [EN 13458](https://standards.cencenelec.eu/) — Cryogenic vessels — Static vacuum insulated vessels
- [ASME BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-division-1-rules-construction-pressure-vessels) — Pressure Vessel Code
- [ISO 21009](https://www.iso.org/standard/68454.html) — Cryogenic vessels — Static vacuum insulated vessels — Part 1: Design, fabrication, inspection and tests

### Safety and Operations

- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code
- [ISO 22734](https://www.iso.org/standard/73573.html) — Hydrogen generators using water electrolysis
- [CGA P-6](https://www.cganet.com/) — Standard Density Data, Atmospheric Gases and Hydrogen

### Inspection and Testing

- [ASME BPVC Section V](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-v-nondestructive-examination) — Nondestructive Examination
- [API 620](https://www.api.org/products-and-services/oil-and-natural-gas/refining/api-620) — Design and Construction of Large, Welded, Low-Pressure Storage Tanks

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

*Reference: [85-60-01 H2 Storage Systems README](./README.md)*
