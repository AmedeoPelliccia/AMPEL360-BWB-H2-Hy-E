# 85-60-01-004 — Vaporization Systems

## Document Metadata

```yaml
document_id: "85-60-01-004"
title: "Vaporization_Systems"
parent_system: "85-60-01 H2 Storage Systems"
category: "Phase Conversion Equipment"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-22"
```

## Purpose

This document defines the requirements, design specifications, and operational procedures for vaporization systems that convert liquid hydrogen (LH2) to gaseous hydrogen (GH2) for aircraft refueling operations supporting the AMPEL360 BWB-H2-Hy-E aircraft.

## Vaporization Overview

### Rationale

Aircraft are typically fueled with compressed GH2 (350 or 700 bar), while bulk storage is often in liquid form (LH2) due to higher volumetric density. Vaporization systems bridge this gap.

### Process

**LH2 to GH2 Conversion:**
- **Input:** LH2 at -253°C, 1-10 bar
- **Output:** GH2 at ambient temperature (-40°C to +50°C), 1-50 bar (before compression)
- **Heat Required:** 446 kJ/kg (latent heat of vaporization) + sensible heat to warm GH2 to ambient

**Example:** Vaporize 100 kg/hour LH2 and warm to 20°C:
- Latent heat: 100 kg/h × 446 kJ/kg = 44,600 kJ/h = 12.4 kW
- Sensible heat: 100 kg/h × 14.3 kJ/kg·K × 273 K ≈ 390,000 kJ/h = 108 kW
- **Total heat required:** ~120 kW

### Vaporizer Types

1. **Ambient Air Vaporizers (AAV):** Use ambient air as heat source (most common, no energy cost)
2. **Electric Vaporizers:** Use electric heating elements (backup or supplemental)
3. **Steam/Hot Water Vaporizers:** Use process steam or hot water (industrial sites)

## Ambient Air Vaporizers (AAV)

### Design Principle

Heat transfer from ambient air to LH2 through finned tube heat exchanger.

**Advantages:**
- No operating energy cost (uses ambient air)
- Simple and reliable (no moving parts)
- Low maintenance

**Disadvantages:**
- Performance depends on ambient temperature (reduced capacity in cold weather)
- Ice formation can block airflow (requires defrost cycles)
- Large physical size (low heat transfer coefficient for air)

### Construction

**Heat Exchanger Type:** Finned tube bundle

**Tube Material:** Aluminum (good thermal conductivity, lightweight) or stainless steel (durability)

**Fins:** Aluminum extrusions or bonded to tubes

**Tube Configuration:**
- Multiple parallel paths for LH2 flow
- Vertical orientation (natural convection of air upward)

**Frame:** Structural steel or aluminum frame with safety grating

### Sizing and Capacity

**Heat Transfer Rate:** Typically 5-20 kW per m² of frontal area (depends on ambient temperature and airflow)

**Example Sizing:**
- Required capacity: 200 kg/h LH2 vaporization + warming to 15°C ≈ 240 kW
- At 10 kW/m² (typical): Frontal area ≈ 24 m²
- AAV dimensions: ~4m wide × 6m tall × 2m deep

See: [85-60-01-A-003_Thermal_Analysis.csv](./ASSETS/85-60-01-A-003_Thermal_Analysis.csv)

### Ice Formation and Defrost

**Ice Accumulation:**
- Moisture in ambient air freezes on cold fin surfaces
- Blocks airflow and reduces heat transfer
- Significant in humid climates

**Defrost Methods:**
1. **Natural Defrost:** Stop LH2 flow, allow ambient heat to melt ice (30-60 minutes)
2. **Hot Gas Defrost:** Circulate warm GH2 through AAV (faster, 10-20 minutes)
3. **Electric Defrost:** Electric heating elements in fin pack (fastest, 5-10 minutes)

**Defrost Scheduling:**
- Monitor performance (outlet temperature or vaporization rate)
- Automatic switchover to backup AAV or electric vaporizer during defrost
- Typical defrost frequency: Every 4-12 hours in humid conditions

### Safety Features

**Pressure Relief:**
- PRV on outlet (protects AAV from over-pressure if downstream blockage)
- Set pressure: 1.5x maximum operating pressure

**Temperature Monitoring:**
- Outlet temperature sensor (verify complete vaporization — outlet should be >-100°C)
- If outlet temperature too low, LH2 may not be fully vaporized (hazard to compressor)

**H2 Detection:**
- Fixed H2 sensors near AAV (detect leaks)
- Alarm setpoint: 0.4% H2 by volume

## Electric Vaporizers

### Design Principle

Electric heating elements directly heat LH2 to GH2.

**Advantages:**
- Compact size
- Precise temperature control
- Independent of ambient conditions
- Fast response time

**Disadvantages:**
- High electrical energy consumption (0.3-0.5 kWh per kg H2)
- Operating cost (electricity)
- Requires significant electrical power (e.g., 240 kW for 200 kg/h)

### Construction

**Heating Element Type:**
- Immersion heaters (electric resistance elements in pressure vessel)
- Shell-and-tube heat exchanger with electric heating jacket

**Materials:**
- Pressure vessel: Stainless steel
- Heating elements: Inconel or stainless steel sheath
- Insulation: Vacuum jacket or foam insulation

**Power Supply:**
- Three-phase AC (typical: 480V or 380V)
- Electrical capacity: 1-2 kW per kg/h vaporization capacity

### Control

**Temperature Control:**
- PID controller maintains outlet temperature setpoint (e.g., +15°C)
- Modulates electric power to heating elements

**Safety Interlocks:**
- Low flow interlock (prevents element overheating if no LH2 flow)
- High temperature cutoff (prevents GH2 overheating)
- Ground fault detection (electrical safety)

### Applications

**Primary Use Cases:**
- Backup for AAV (when defrosting or insufficient ambient temperature)
- Supplemental heating (trim temperature control)
- Peak demand response (rapid capacity increase)

## Steam/Hot Water Vaporizers

### Design Principle

Heat transfer from steam or hot water to LH2 through heat exchanger.

**Advantages:**
- No electrical energy consumption (if waste steam available)
- High heat transfer coefficient (compact size)
- Stable performance (independent of ambient conditions)

**Disadvantages:**
- Requires steam or hot water source (not available at most airports)
- Risk of ice blockage in tubes if steam supply interrupted
- More complex system (boiler, condensate return)

### Construction

**Heat Exchanger Type:** Shell-and-tube or plate-and-frame

**Shell Side:** Steam or hot water

**Tube Side:** LH2/GH2

**Materials:**
- Tubes: Stainless steel (cryogenic compatible)
- Shell: Carbon steel (if steam side only) or stainless steel

### Sizing

**Heat Transfer Coefficient:** High (steam condensation: 3,000-10,000 W/m²·K)

**Compact Design:** Significantly smaller than AAV for same capacity

**Example:**
- 240 kW vaporizer with 5,000 W/m²·K and 100°C steam: ~5 m² heat transfer area

### Applications

**Industrial Sites:** Where steam is available from co-generation or industrial processes

**Not Typical for Airports:** Unless waste heat source available (e.g., auxiliary power generation)

## Vaporization System Configuration

### Single Vaporizer

**Application:** Small installations (<100 kg/h capacity)

**Reliability:** Single point of failure (backup often manual switchover to electric)

### Parallel Vaporizers

**Configuration:** Two or more AAVs in parallel

**Advantages:**
- Redundancy (continue operation if one AAV fails or defrosting)
- Modular capacity (stage vaporizers based on demand)

**Control:**
- Automated switchover between AAVs
- Load sharing based on outlet temperature or flow rate

### Cascaded Vaporizers

**Configuration:** AAV followed by electric trim heater

**Advantages:**
- AAV provides bulk vaporization (low cost)
- Electric heater provides precise temperature control (small capacity)

**Example:**
- 200 kg/h AAV provides GH2 at -50°C to +10°C (depending on ambient)
- 20 kW electric heater trims temperature to +15°C ±2°C

## Integration with Compression

### Vaporizer Outlet Pressure

**Low-Pressure Vaporization:** 1-10 bar
- Requires high-pressure compression (e.g., 350 or 700 bar for aircraft)
- Higher compression energy but simpler vaporizer design

**High-Pressure Vaporization:** 50-400 bar
- Vaporize LH2 at elevated pressure using cryogenic pump + vaporizer
- Lower compression energy but more complex (high-pressure vaporizer)

**Trade-Off:**
- Low-pressure vaporization preferred for simplicity and lower capital cost
- High-pressure vaporization considered for large-scale, high-efficiency systems

### Compression

After vaporization, GH2 is compressed to refueling pressure (350 or 700 bar).

See: [85-60-01-005_Pressure_Management.md](./85-60-01-005_Pressure_Management.md)

## Instrumentation and Control

### Temperature Measurement

**Inlet Temperature:**
- Verify LH2 inlet temperature (should be near -253°C)
- RTD or thermocouple

**Outlet Temperature:**
- Critical for safety (ensure complete vaporization)
- Alarm if outlet <-100°C (liquid may be present)
- Typical setpoint: +15°C ±5°C

**Ambient Temperature:**
- Monitor for AAV performance prediction and defrost scheduling

### Pressure Measurement

**Inlet Pressure:**
- Typically 1-10 bar (from LH2 tank)

**Outlet Pressure:**
- 1-50 bar (before compression)
- Alarm on high pressure (indication of downstream blockage)

### Flow Measurement

**Mass Flow Meter:**
- Coriolis or thermal mass flow meter
- Verify vaporization capacity (kg/h)
- Accuracy: ±1% or better

### Control System

**Automated Control:**
- PLC or DCS (Distributed Control System)
- Sequences vaporizers based on demand
- Manages defrost cycles
- Interlocks for safety (e.g., stop LH2 flow if outlet temperature too low)

**HMI (Human-Machine Interface):**
- Display temperatures, pressures, flow rates
- Alarm annunciation
- Manual control override

## Operational Procedures

### Startup

1. Verify H2 detection system operational
2. Check vaporizer for frost or ice (defrost if necessary)
3. Open LH2 supply valve slowly (pre-cool vaporizer to avoid thermal shock)
4. Monitor outlet temperature (should rise to ambient after initial cool-down)
5. When outlet temperature stabilized, begin GH2 delivery to compressor

### Normal Operation

**Continuous Monitoring:**
- Outlet temperature (ensure >-100°C, target ~+15°C)
- Flow rate (match aircraft refueling demand)
- Ice accumulation on AAV (visual inspection or performance degradation)

**Defrost Scheduling:**
- Automatic switchover to backup vaporizer
- Defrost cycle per section above (natural, hot gas, or electric)
- Return vaporizer to service after defrost complete

### Shutdown

1. Close LH2 supply valve
2. Allow GH2 in vaporizer to flow out (purge to compressor or vent)
3. When vaporizer warmed to ambient, isolate and secure

**Extended Shutdown:**
- Purge vaporizer with dry N2 or GH2 (prevent moisture ingress)
- Isolate and lock out

### Emergency Procedures

**LH2 Leak at Vaporizer:**
1. Close LH2 supply valve (upstream isolation)
2. Activate ESD (emergency shutdown system)
3. Evacuate personnel upwind
4. Notify ARFF (establish safety perimeter)
5. Allow LH2 to vaporize (do not attempt to contain)

**Incomplete Vaporization (Liquid Carryover):**
1. Reduce LH2 flow rate (allow more residence time in vaporizer)
2. If outlet temperature remains <-100°C, shut down vaporizer
3. Switch to backup vaporizer or electric vaporizer
4. Investigate cause (ice blockage, insufficient heat transfer, excessive demand)

## Maintenance

### Preventive Maintenance

**Weekly:**
- Visual inspection for frost, ice, or leaks
- Check outlet temperature and flow rate (verify performance)

**Monthly:**
- Inspect heat exchanger fins (AAV) for damage or corrosion
- Test defrost system (manual activation and timing)
- Calibrate temperature sensors

**Annual:**
- Pressure test vaporizer (per ASME or manufacturer recommendation)
- Inspect internal tubes for corrosion or deposits (if accessible)
- Test PRV (remove and bench test)

### Performance Monitoring

**Heat Transfer Degradation:**
- Monitor outlet temperature vs. ambient temperature trend
- Reduced performance indicates: Ice buildup, fin damage, or reduced airflow

**Corrective Actions:**
- More frequent defrost cycles
- Clean or repair fins
- Verify no obstructions to airflow

## Standards and References

### Design and Construction

- [ASME B31.3](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping) — Process Piping (for vaporizer piping)
- [ASME BPVC Section VIII](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii-division-1-rules-construction-pressure-vessels) — Pressure Vessel Code (for pressure vessel vaporizers)
- [EN 13458](https://standards.cencenelec.eu/) — Cryogenic vessels (applicable to vaporizer design)

### Safety and Operations

- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code
- [ISO 22734](https://www.iso.org/standard/73573.html) — Hydrogen generators using water electrolysis

### Heat Transfer

- [TEMA Standards](https://www.tema.org/) — Tubular Exchanger Manufacturers Association (heat exchanger design)

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

*Reference: [85-60-01 H2 Storage Systems README](./README.md)*
