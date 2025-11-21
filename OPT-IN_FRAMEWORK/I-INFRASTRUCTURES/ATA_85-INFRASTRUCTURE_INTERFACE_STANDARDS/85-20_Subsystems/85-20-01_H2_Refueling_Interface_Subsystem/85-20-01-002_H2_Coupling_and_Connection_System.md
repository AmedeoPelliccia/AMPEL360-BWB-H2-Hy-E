# 85-20-01-002 — H2 Coupling and Connection System

## Document Metadata

```yaml
document_id: "85-20-01-002"
title: "H2 Coupling and Connection System"
parent_system: "85-20-01 H2 Refueling Interface Subsystem"
category: "Component Specification"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

This document specifies the mechanical coupling and connection system that provides the physical interface between the ground H2 refueling equipment and the aircraft H2 fuel receptacle. The coupling must ensure leak-tight operation under high pressure while allowing safe and rapid connection/disconnection.

## Coupling Interface Standard

**Primary Standard:** [ISO 19880-5](https://www.iso.org/standard/71975.html) or [CSA/ANSI HGV 4.3](https://www.csagroup.org/)

**Pressure Rating:** 500 bar (nominal operating: 350 bar for Type III tanks, 700 bar for Type IV)

**Connection Type:** Single-hand operation, self-sealing nozzle and receptacle

## Mechanical Design

### Nozzle (Ground-Side)

- **Material:** Stainless steel 316L (corrosion resistant, H2 compatible)
- **Sealing:** Dual seals (primary: metal face seal, secondary: elastomer O-ring)
- **Locking Mechanism:** Quarter-turn bayonet or push-to-connect with locking collar
- **Dust Cap:** Protective cap when not connected
- **Grounding Contact:** Integrated electrical bonding pin

### Receptacle (Aircraft-Side)

*(Part of [ATA 28](../../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/ATA_28-FUEL/README.md), interface spec provided here)*

- **Material:** Stainless steel or titanium (weight optimized)
- **Check Valve:** Prevents H2 backflow when disconnected
- **Fill Valve:** Remotely actuated from aircraft or ground
- **Position:** Fuselage lower surface, accessible from ground (typically near landing gear)

### Hose Assembly

- **Length:** 15-20 meters (sufficient reach without tension)
- **Inner Diameter:** 12-19 mm (sized for target flow rate)
- **Pressure Rating:** >500 bar (safety factor >1.4)
- **Material:** Thermoplastic or composite liner, stainless steel braiding, protective outer jacket
- **Temperature Range:** -40°C to +85°C (ambient conditions)
- **Bend Radius:** Minimum 10x hose diameter (prevent kinking)

### Breakaway Coupling

**Purpose:** Protect aircraft and equipment if vehicle drives away with hose connected

**Location:** Mid-hose or near nozzle

**Activation Force:** 200-400 N axial tension (sufficient to break away, not activate accidentally)

**Breakaway Action:**
1. Mechanical separation at predetermined point
2. Automatic closure of valves on both sides
3. Venting of trapped H2 to safe location
4. Visual/audible alarm

**Standards:** [UL 567](https://www.ul.com/resources/ul-567-standard-emergency-breakaway-fittings-petroleum-products) (adapted for H2)

## Connection Procedure

### Pre-Connection Checks

1. Inspect coupling and receptacle for damage, contamination
2. Verify aircraft grounding/bonding established
3. Confirm safety zone clear (85-20-08)
4. Obtain refueling authorization (85-20-05)

### Connection Sequence

1. **Approach:** Align nozzle with aircraft receptacle
2. **Insert:** Push nozzle into receptacle until mechanical engagement
3. **Lock:** Rotate locking collar or engage locking mechanism (audible/tactile click)
4. **Verify:** Visual inspection of locking indicator, check grounding continuity
5. **Pressurize:** Gradually pressurize coupling (0-5 bar in 5 seconds) while monitoring for leaks
6. **Leak Check:** Hold pressure, verify no H2 detected (85-20-08 sensors)
7. **Ready:** If no leaks, proceed to refueling

### Disconnection Sequence

1. **Complete:** Ensure refueling complete, valves closed
2. **Depressurize:** Vent H2 from coupling to <1 bar
3. **Unlock:** Disengage locking mechanism
4. **Withdraw:** Pull nozzle straight out from receptacle
5. **Cap:** Install dust caps on nozzle and receptacle
6. **Stow:** Secure hose and nozzle on dispenser

## Leak Prevention

### Primary Sealing

**Metal Face Seal:** Precision-machined sealing surfaces, compressed upon connection

**Material:** Soft metal (e.g., silver-plated) or hard metal (e.g., stainless steel) depending on design

**Seal Load:** Provided by locking mechanism (spring-loaded or mechanical advantage)

### Secondary Sealing

**Elastomer O-Ring:** Backup seal for additional leak prevention

**Material:** H2-compatible elastomer (e.g., HNBR, FFKM)

**Temperature Range:** -40°C to +150°C

### Leak Detection

**Coupling Leak Detection Port:** Small port between primary and secondary seals, connected to H2 sensor

**Detection Method:** If primary seal leaks, H2 detected in leak detection port before reaching atmosphere

**Action:** Automatic shutoff, alarm, depressurize coupling

## Grounding and Bonding

**Purpose:** Dissipate static electricity to prevent ignition source

### Electrical Bonding Path

1. **Aircraft Grounding:** Aircraft structure connected to ground via dedicated grounding cable or landing gear
2. **Hose Bonding:** Conductive wire integrated into hose assembly
3. **Coupling Bonding:** Electrical contact between nozzle and receptacle (spring-loaded pin/socket)
4. **Verification:** Bonding continuity verified before refueling authorized

### Resistance Requirement

**Maximum Resistance:** 1 ohm (aircraft structure to ground infrastructure)

**Verification:** Automatic continuity test before each refueling operation

**Standards:** [NFPA 77](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=77) (Static electricity bonding)

## Safety Features

### Over-Pressure Protection

**Pressure Relief Valve:** Coupling includes relief valve set at 1.1x maximum operating pressure

**Capacity:** Sufficient to prevent rupture if valve fails closed

### Temperature Monitoring

**Purpose:** Detect excessive heating due to compression or flow friction

**Sensors:** Thermocouples on nozzle and receptacle

**Limit:** +85°C maximum (triggers alarm and flow reduction)

### Misconnection Prevention

**Mechanical Keying:** Coupling nozzle designed to fit only correct aircraft receptacle

**Labeling:** Clear marking "H2 ONLY - HIGH PRESSURE" on nozzle and receptacle

## Inspection and Maintenance

### Pre-Refueling Inspection (Every Use)

- Visual inspection for damage, cracks, excessive wear
- Check seals for cuts, contamination
- Verify locking mechanism function
- Test grounding continuity

### Periodic Inspection (Monthly)

- Detailed visual inspection under magnification
- Leak test at operating pressure
- Measure seal compression and wear
- Check hose flexibility and outer jacket condition

### Major Inspection (Annual or 500 Refueling Cycles)

- Disassemble coupling, inspect internal components
- Replace seals (elastomer O-rings)
- Hydrostatic pressure test (1.5x operating pressure)
- Replace hose if any damage found

### Replacement Criteria

- **Immediate:** Visible damage, leak during operation, failed pressure test
- **Scheduled:** Seals every 2 years, hose every 5 years or 2500 cycles (whichever first)

## Material Compatibility

### H2 Embrittlement Considerations

**Susceptible Materials (Avoid):**
- High-strength steels (>1000 MPa tensile strength)
- Certain aluminum alloys

**H2-Compatible Materials (Use):**
- Austenitic stainless steels (304, 316L)
- Aluminum alloys (6061-T6, 7075-T73 with precautions)
- Inconel, Monel (nickel alloys)
- PTFE, HNBR, FFKM (polymers for seals)

**Standards:** [ISO/TR 15916](https://www.iso.org/standard/29316.html) (Basic considerations for the safety of hydrogen systems)

## Performance Specifications

| Parameter | Value | Verification Method |
|-----------|-------|---------------------|
| Pressure Rating | 500 bar | Hydrostatic test |
| Leak Rate | <10⁻⁶ mbar·L/s | Helium leak test |
| Connection Time | <30 seconds | Operational test |
| Disconnection Time | <20 seconds | Operational test |
| Grounding Resistance | <1 ohm | Continuity test |
| Operating Temperature | -40 to +85°C | Thermal chamber test |
| Hose Bend Cycles | >10,000 | Fatigue test |
| Breakaway Force | 200-400 N | Load test |

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21

---

*Reference: [85-20-01 H2 Refueling Interface Subsystem README](./README.md)*
