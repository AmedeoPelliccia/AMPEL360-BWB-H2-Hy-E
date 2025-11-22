# 85-60-01-003 — Cryogenic Equipment

## Document Metadata

```yaml
document_id: "85-60-01-003"
title: "Cryogenic Equipment"
parent_system: "85-60-01 H2 Storage Systems"
category: "Cryogenic Systems"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-22"
```

## Purpose

This document defines the requirements, design specifications, and operational procedures for cryogenic equipment used in liquid hydrogen (LH2) storage and handling systems to support AMPEL360 BWB-H2-Hy-E aircraft refueling operations.

## Cryogenic Equipment Overview

### Scope

Cryogenic equipment for LH2 systems includes:

1. **Transfer Lines:** Vacuum-insulated piping for LH2 transport
2. **Valves:** Cryogenic-rated valves for isolation and control
3. **Pumps:** Cryogenic centrifugal pumps for LH2 transfer
4. **Level Sensors:** Differential pressure, capacitance, or float-type sensors
5. **Pressure Building Coils:** Internal heat exchangers for tank pressurization
6. **Vaporizers:** Heat exchangers to convert LH2 to GH2 (see [85-60-01-004](./85-60-01-004_Vaporization_Systems.md))

### Operating Temperature Range

- **LH2 Temperature:** -252.87°C (-423.17°F) at NBP
- **Cryogenic Equipment Rating:** Typically -270°C to +50°C

### Material Requirements

**Cryogenic Compatibility:**
- Must maintain ductility and toughness at -253°C
- Austenitic stainless steels (304, 304L, 316, 316L)
- Aluminum alloys (5083, 5086, 6061)
- Copper alloys (for seals and small components)

**Materials to Avoid:**
- Carbon steel (brittle at cryogenic temperatures)
- Most plastics (except PTFE, PCTFE for seals)

## Vacuum-Insulated Transfer Lines

### Construction

**Design:** Pipe-in-pipe with evacuated annular space

**Inner Pipe:** Stainless steel (304L or 316L) for LH2 flow

**Outer Pipe:** Stainless steel or carbon steel (structural, not in contact with LH2)

**Insulation:** Multi-layer insulation (MLI) or perlite in vacuum space

**Vacuum Quality:** <10^-4 mbar for effective insulation

**Supports:** Low thermal conductivity spacers (e.g., G-10 fiberglass or PTFE) to minimize heat transfer

### Sizing and Routing

**Line Sizing:**
- Based on required flow rate and acceptable pressure drop
- Typical velocities: 1-3 m/s for LH2

**Routing:**
- Minimize length to reduce heat ingress
- Slope lines to allow drainage and vapor venting (minimum 1:100 slope)
- Avoid low points where LH2 can pool and vaporize

**Flexibility:**
- Use bellows or expansion loops to accommodate thermal contraction (~1.5% linear contraction from ambient to -253°C)
- Allow for seismic movement and thermal cycling

### Vacuum Maintenance

**Vacuum Ports:**
- Provide vacuum pump-out ports at intervals (every 30-50 meters)
- Monitor vacuum quality periodically (annual or per manufacturer recommendation)

**Leak Testing:**
- Helium leak test during installation and after repairs
- Maximum allowable leak rate: 10^-6 mbar·L/s

### Heat Ingress and Boil-Off

**Target Heat Ingress:** <5 W/m for well-designed vacuum-insulated lines

**Boil-Off Calculation:**
- Heat ingress ÷ heat of vaporization of H2 (446 kJ/kg)
- Example: 5 W/m line, 100m length → 500 W → 1.12 kg H2/hour boil-off

**Mitigation:**
- Use boil-off vapor to pre-cool transfer lines before LH2 flow
- Recover boil-off vapor for compression or vaporization

See: [85-60-01-A-003_Thermal_Analysis.csv](./ASSETS/85-60-01-A-003_Thermal_Analysis.csv)

## Cryogenic Valves

### Valve Types

**Ball Valves:**
- Most common for isolation service
- Full-bore design minimizes pressure drop
- Stem extension to keep actuator at ambient temperature

**Globe Valves:**
- Used for throttling and flow control
- Higher pressure drop than ball valves

**Check Valves:**
- Prevent backflow
- Spring-loaded or weight-loaded poppet design

**Relief Valves:**
- Protect piping and equipment from overpressure
- Must be cryogenic-rated (non-cryogenic valves can freeze shut)

### Design Features

**Extended Stem:**
- Keeps packing and actuator at ambient temperature
- Stem length: Typically 150-300mm
- Insulated and/or heat-traced stem extension

**Packing:**
- PTFE or graphite packing for cryogenic service
- Minimize stem heat conduction

**Body Material:**
- Stainless steel (CF8M cast or 316 bar stock)
- Aluminum (for weight-critical applications)

**Seat Material:**
- Metal-to-metal seats (most reliable at cryogenic temperatures)
- PTFE or PCTFE seats (soft seats, good for tight shutoff)

### Actuation

**Manual:**
- Handwheel or lever
- Suitable for infrequent operation

**Pneumatic:**
- Actuated by compressed air or N2
- Fast operation for ESD applications
- Fail-safe design (e.g., spring-return to closed on air loss)

**Electric:**
- Motor-operated valves (MOV)
- Slower than pneumatic but good for remote control
- Fail-in-place or fail-to-position (with battery backup)

## Cryogenic Pumps

### Pump Types

**Centrifugal Pumps:**
- Most common for LH2 transfer
- Submerged or external mounting
- Typical head: 50-200 meters (liquid column)

**Positive Displacement Pumps:**
- Piston or diaphragm pumps
- Used for high-pressure applications (e.g., feeding high-pressure vaporizers)
- More complex sealing requirements

### Design Features

**Submerged Pumps:**
- Motor and pump submerged in LH2 tank (simplifies sealing)
- Motor cooled by LH2 (requires cryogenic-rated motor)
- Eliminates net positive suction head (NPSH) issues

**External Pumps:**
- Pump external to tank, fed by gravity or pressure
- Requires NPSH margin (LH2 has low density → low NPSH available)
- Easier maintenance than submerged pumps

**Materials:**
- Impeller and casing: Stainless steel or aluminum
- Bearings: Self-lubricating (PTFE, carbon-graphite) or LH2-lubricated
- Seals: Mechanical seals with LH2-compatible materials (e.g., carbon-graphite faces)

### Performance Considerations

**NPSH (Net Positive Suction Head):**
- Critical for external pumps
- LH2 density: ~71 kg/m³ (vs. water: 1000 kg/m³)
- Requires higher suction pressure or taller liquid column

**Cavitation:**
- Avoid cavitation (vapor bubbles in pump) which causes damage
- Ensure NPSH available > NPSH required + safety margin (typically 1-2m)

**Efficiency:**
- Typical centrifugal pump efficiency: 50-70%
- Power consumption: 0.1-0.5 kW per kg/s LH2 flow

## Level Measurement

### Differential Pressure (DP) Transmitters

**Principle:** Measures pressure difference between top and bottom of tank

**Advantages:**
- Simple and reliable
- No moving parts
- Works with any tank geometry

**Disadvantages:**
- Requires density compensation (density varies with temperature and ortho-para ratio)
- Impulse lines can plug with ice or contaminants

**Installation:**
- Impulse lines purged with dry N2 or He (prevent ice formation)
- Temperature compensation required for accurate level measurement

### Capacitance Probes

**Principle:** Measures capacitance change as LH2 level varies

**Advantages:**
- Continuous level measurement
- No density compensation required
- Good for precise level control

**Disadvantages:**
- More expensive than DP transmitters
- Requires calibration for specific tank geometry and LH2 dielectric constant

**Installation:**
- Probe mounted vertically in tank
- Coaxial or rod-and-tube configuration

### Float Gauges

**Principle:** Mechanical float follows LH2 level, actuates position indicator

**Advantages:**
- Simple and robust
- No external power required
- Visual indication possible

**Disadvantages:**
- Moving parts can freeze or jam
- Limited accuracy
- Requires penetration into tank (potential leak point)

**Installation:**
- Float material: Low-density foam or hollow metal (stainless steel, aluminum)
- Shaft and indicator external to tank

## Pressure Building Coils

### Purpose

Vaporize small amount of LH2 inside tank to increase tank pressure for transfer operations.

### Design

**Configuration:** Coiled tube (stainless steel) inside tank vapor space

**Heat Source:** Ambient air heat exchanger or electric heater on coil exterior

**Operation:** Tank pressure opens valve, allowing LH2 into coil → vaporizes → increases tank pressure → valve closes

**Control:** Pressure switch or regulator controls coil operation

### Sizing

**Vaporization Rate:** Sized for desired pressure rise rate (e.g., 1 bar/hour)

**Example:** To raise 150,000L tank from 1 to 6 bar in 5 hours:
- Required vaporization: ~50 kg H2 (5 bar increase × 150m³ × gas density)
- Heat input: 50 kg × 446 kJ/kg ÷ (5 hours × 3600 s/hour) ≈ 1.2 kW

### Safety

**Overpressure Protection:** PRV protects tank if pressure building coil fails open

**Redundancy:** Two coils for reliability (primary and backup)

## Cryogenic Instrumentation

### Temperature Sensors

**RTDs (Resistance Temperature Detectors):**
- Platinum (Pt100 or Pt1000)
- Accurate and stable at cryogenic temperatures
- Typical accuracy: ±0.5°C

**Thermocouples:**
- Type K or Type E
- Lower accuracy than RTDs but simpler wiring
- Typical accuracy: ±2°C at cryogenic temperatures

**Installation:**
- Thermowells for protection and replaceability
- Multiple sensors for redundancy and averaging

### Pressure Sensors

**Pressure Transmitters:**
- Diaphragm-type with remote seal (keeps transmitter at ambient temperature)
- Capillary filled with low-temperature fluid (e.g., silicone oil)
- Range: 0-10 bar (for LH2 tanks), 0-50 bar (for transfer systems)

**Pressure Gauges:**
- Bourdon tube or diaphragm type
- Glycerin-filled for vibration damping
- Cryogenic-rated (materials compatible with -253°C)

## Maintenance and Inspection

### Preventive Maintenance

**Monthly:**
- Visual inspection of insulation (check for frost or ice indicating vacuum loss)
- Check valve operation (manual valves: exercise; automated valves: stroke test)
- Inspect pump operation (monitor vibration, bearing temperature if external)

**Quarterly:**
- Leak test of transfer lines and valves (soap solution or sniffer test)
- Calibrate level sensors (compare to calculated volume from deliveries)
- Test pressure building coils (verify pressure rise rate)

**Annual:**
- Vacuum pump-down of transfer lines (if vacuum has degraded)
- PRV testing (remove and bench test, or in-place test)
- Pump overhaul (if external, or per manufacturer recommendation for submerged)

### Vacuum Loss Diagnosis

**Symptoms:**
- Frost or ice formation on outer jacket
- Increased boil-off rate
- Vacuum gauge (if installed) shows degraded vacuum (>10^-3 mbar)

**Causes:**
- Leak in outer jacket (air ingress)
- Leak in inner pipe (H2 vapor ingress)
- Getter material exhausted (absorbs residual gas in vacuum space)
- Damaged MLI (excessive thermal conductivity)

**Remediation:**
- Locate leak (helium or pressure decay test)
- Repair leak (weld or flange replacement)
- Pump down vacuum space to <10^-4 mbar
- Replace getter material if necessary

## Standards and References

### Design and Construction

- [EN 13458](https://standards.cencenelec.eu/) — Cryogenic vessels — Static vacuum insulated vessels
- [ASME B31.3](https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping) — Process Piping (for cryogenic piping design)
- [ISO 21009](https://www.iso.org/standard/68454.html) — Cryogenic vessels — Static vacuum insulated vessels — Design, fabrication, inspection and tests

### Valves and Fittings

- [ASME B16.34](https://www.asme.org/codes-standards/find-codes-standards/b16-34-valves-flanged-threaded-welding-end) — Valves — Flanged, Threaded, and Welding End
- [ISO 28921](https://www.iso.org/standard/70070.html) — Industrial valves — Isolating valves for cryogenic service

### Testing and Inspection

- [ASME BPVC Section V](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-v-nondestructive-examination) — Nondestructive Examination
- [ASTM E595](https://www.astm.org/e0595-15r21.html) — Standard Test Method for Total Mass Loss and Collected Volatile Condensable Materials from Outgassing in a Vacuum Environment (for vacuum system materials)

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-22

---

*Reference: [85-60-01 H2 Storage Systems README](./README.md)*
