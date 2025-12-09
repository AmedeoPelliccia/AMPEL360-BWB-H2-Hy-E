---
Title: "H2 Safety Systems Design — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-06-02-03A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Safety system design requirements for hydrogen Ground Support Equipment including leak detection, fire suppression, and emergency response."
Keywords: ["ATA 03","GSE","Hydrogen","Safety","Leak Detection","Fire Suppression"]
Compliance:
  - "NASA-STD-8719.17"
  - "NFPA 2"
  - "ISO 19880-8"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Parent: "../00_INDEX.md"
  Related: "./03-00-06-02-01A_LH2_Fueling_GSE_Design.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-00-06-02-03A — H2 Safety Systems Design

## 1. Purpose

This document defines **safety system design requirements** for hydrogen GSE to mitigate risks associated with hydrogen's flammability, wide explosive range, and cryogenic properties. Effective safety systems are critical to protecting personnel, aircraft, and infrastructure.

## 2. Scope

Safety systems covered:
- **Hydrogen leak detection** and alarm systems
- **Emergency shutoff valves (ESV)** and interlocks
- **Fire detection** and suppression
- **Ventilation** and hydrogen dispersion
- **Bonding and grounding** for static discharge prevention
- **Personnel protection** systems
- **Emergency response** equipment and procedures

## 3. Applicable Documents

- [NASA-STD-8719.17](https://standards.nasa.gov/) — Safety Standard for Hydrogen and Hydrogen Systems
- [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) — Hydrogen Technologies Code
- [ISO 19880-8](https://www.iso.org/standard/71940.html) — Gaseous Hydrogen Fueling Stations
- [IEC 60079](https://www.iec.ch/) — Explosive Atmospheres Standards
- [NFPA 70](https://www.nfpa.org/) — National Electrical Code (hazardous locations classification)

## 4. Hydrogen Hazard Characteristics

### 4.1 Key Safety Properties

| Property | Value | Safety Implication |
|----------|-------|---------------------|
| **Flammability Range** | 4-75% by volume in air | Wide range; easy to form flammable mixture |
| **Lower Explosive Limit (LEL)** | 4% by volume | Alarm at 10% LEL (0.4%) for safety margin |
| **Autoignition Temperature** | 585°C (1,085°F) | Lower than gasoline (495°C) but higher than many hydrocarbons |
| **Minimum Ignition Energy** | 0.017 mJ | Very low; static spark can ignite |
| **Flame Speed** | 3.46 m/s (vs. 0.4 m/s for gasoline) | Fast-burning; rapid pressure rise |
| **Flame Visibility** | Nearly invisible in daylight (UV/IR detectable) | Special detectors required |
| **Buoyancy** | 14× lighter than air | Rises rapidly; accumulates at ceilings |
| **Diffusivity** | 3.8× faster than natural gas | Disperses quickly in open air |

### 4.2 Hazard Scenarios

| Scenario | Likelihood | Severity | Mitigation |
|----------|------------|----------|------------|
| **Small Leak (< 1 kg/min)** | Medium | Low-Medium | Leak detection, ventilation, auto-shutoff |
| **Large Leak (> 10 kg/min)** | Low | High | Emergency shutoff, evacuation, fire brigade |
| **Fire (jet flame or flash fire)** | Low | High | Fire detection, let burn (if safe), protect exposures |
| **Explosion (confined space)** | Very Low | Catastrophic | Prevent ignition sources, ensure ventilation |
| **Cryogenic Release (LH2)** | Medium | Medium | PPE, venting, monitoring until dispersed |

## 5. Hydrogen Leak Detection Systems

### 5.1 Sensor Technologies

| Sensor Type | Operating Principle | Response Time | Application |
|-------------|---------------------|---------------|-------------|
| **Catalytic Bead** | H2 combustion on heated catalyst | 5-10 seconds (T90) | General area monitoring, outdoor |
| **Electrochemical** | H2 oxidation on electrode | 10-15 seconds | Portable monitors, confined spaces |
| **Thermal Conductivity** | H2 conducts heat faster than air | 5-10 seconds | Fixed installations, high reliability |
| **Optical (Infrared)** | Absorption of specific wavelengths | 1-2 seconds | Long-range detection, flame detection |
| **Acoustic (Ultrasonic)** | Detects high-frequency sound of gas jet | < 1 second | Large leaks, outdoor |

**AMPEL360 Standard**: Use thermal conductivity or catalytic bead sensors for fixed installations; electrochemical for portable detectors.

### 5.2 Sensor Placement

| Location | Sensor Type | Quantity | Alarm Setpoint |
|----------|-------------|----------|----------------|
| **LH2 Tank Vent** | Fixed (thermal conductivity) | 1 per vent | 10% LEL (0.4%) |
| **Pump Enclosure** | Fixed | 2 (redundant) | 10% LEL |
| **Hose Connection Points** | Fixed | 1 per connection | 10% LEL |
| **Operator Cab** | Fixed | 1 | 10% LEL |
| **Indoor Storage/Maintenance** | Fixed (ceiling-mounted) | 1 per 100 m² | 10% LEL |
| **Portable Monitor** | Portable (electrochemical) | Carried by operator | 10% LEL |

**Sensor Height**: Mount sensors within 300mm of ceiling (hydrogen rises) or near potential leak sources.

### 5.3 Alarm and Response

| Alarm Level | H2 Concentration | Response |
|-------------|------------------|----------|
| **Low Alarm** | 10% LEL (0.4%) | Visual and audible warning; investigate source; increase ventilation |
| **High Alarm** | 25% LEL (1.0%) | Activate ESV; evacuate area (30m radius); call fire brigade |
| **Fail-Safe** | Sensor failure or power loss | Default to alarm state; check system |

**Alarm Requirements**:
- Visual: Flashing red strobe light (≥ 0.5 Hz flash rate)
- Audible: ≥ 85 dBA at 3m, distinct tone (preferably pulsed)
- Remote: Alarm signal to airport fire station and control tower

## 6. Emergency Shutoff Systems

### 6.1 Emergency Shutoff Valve (ESV)

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| **Valve Type** | Pneumatically or hydraulically actuated ball valve | Fail-closed (spring return or dead-man switch) |
| **Closing Time** | ≤ 2 seconds from activation | Fast closure to stop leak |
| **Location** | At tank outlet, upstream of pump, and at hose inlet | Multiple ESVs for sectional isolation |
| **Actuation** | Manual (emergency stop button) + automatic (high H2 alarm, fire detection, loss of power) | Redundant activation |
| **Manual Reset** | Require manual reset after ESV closure | Prevent automatic restart |

### 6.2 Emergency Stop (E-Stop) Buttons

| Location | Type | Action |
|----------|------|--------|
| **Operator Control Panel** | Large mushroom button (red, palm-strike) | Close all ESVs, stop pump, activate alarm |
| **Exterior of GSE** | 2-4 buttons (all sides of vehicle) | Accessible to ground crew from any position |
| **Remote E-Stop** | Wireless transmitter (carried by safety officer) | Range ≥ 100m |

### 6.3 Interlocks

Prevent unsafe operations:

| Interlock | Condition | Action Prevented |
|-----------|-----------|------------------|
| **Parking Brake** | Brake not engaged | Pump cannot start |
| **Hose Connected** | Nozzle not connected to aircraft | Pump cannot start |
| **Bonding Verified** | Resistance > 10 ohms | Pump cannot start |
| **Tank Pressure High** | Pressure > 5.5 bar | Close tank outlet valve, vent to atmosphere |
| **Low LH2 Level** | Tank < 5% capacity | Stop pump to avoid running dry |

## 7. Fire Detection and Suppression

### 7.1 Fire Detection

**Hydrogen Flame Characteristics**:
- Nearly invisible in daylight (pale blue, faint)
- Detectable by UV/IR sensors
- Hot (2,045°C adiabatic flame temperature)
- Jet flame (high velocity from pressurized leak)

| Detector Type | Detection Method | Application |
|---------------|------------------|-------------|
| **UV/IR Flame Detector** | Detects UV (185-260 nm) and IR (4.3 μm CO2 emission) | Primary fire detection for H2; fast response (< 5 seconds) |
| **Heat Detector** | Rate-of-rise or fixed-temperature | Backup; slower response but reliable |
| **Smoke Detector** | Optical or ionization | Not effective for H2 (no smoke); do not rely on |

**Detector Placement**: 
- Cover all areas within 10m of H2 equipment
- Field of view overlap for redundancy
- Avoid direct sun exposure (false alarms)

### 7.2 Fire Suppression Strategy

**Hydrogen Fire Response Philosophy**:
1. **Jet Flame (Pressurized Leak)**: 
   - **DO NOT EXTINGUISH** unless absolutely necessary (re-ignition risk, explosion)
   - **Protect exposures** (cool nearby equipment/structures with water spray)
   - **Shut off source** (close ESV if safe to approach)
   - **Let burn** until fuel exhausted

2. **Equipment Fire (Not H2 Itself)**:
   - **Extinguish** with dry chemical (Class ABC or BC) or CO2
   - Protect LH2 tank from heat exposure

### 7.3 Fire Suppression Systems

| System Type | Agent | Application | Activation |
|-------------|-------|-------------|------------|
| **Dry Chemical** | Monoammonium phosphate (Class ABC) or sodium bicarbonate (Class BC) | Engine bay, pump area | Manual or automatic (heat/flame detection) |
| **Inert Gas (N2, Ar, CO2)** | Displaces oxygen | Enclosed electrical cabinets | Automatic (smoke/heat detection) |
| **Water Spray (Deluge)** | Water | LH2 tank exposure protection (cooling) | Manual activation by fire brigade |

**DO NOT USE**:
- Water directly on LH2 (violent boiling)
- Foam or halons (ineffective on hydrogen)

## 8. Ventilation and Hydrogen Dispersion

### 8.1 Ventilation Requirements

| Space Type | Ventilation Rate | Purpose |
|------------|------------------|---------|
| **Outdoor GSE** | Natural ventilation (open air) | Hydrogen disperses rapidly; no forced ventilation needed |
| **Enclosed Equipment Cabinets** | 6 air changes per hour (ACH) minimum | Prevent hydrogen accumulation |
| **Indoor Storage/Maintenance** | 12 ACH with exhaust at ceiling | Remove rising hydrogen |
| **Confined Spaces** | Continuous forced ventilation + O2 monitoring | Maintain O2 > 19.5% by volume |

### 8.2 Vent Stack Design

| Parameter | Requirement | Rationale |
|-----------|-------------|-----------|
| **Height** | ≥ 3m above equipment, ≥ 7m for fixed installations | Disperse hydrogen above personnel |
| **Location** | Away from air intakes, ignition sources (≥ 3m), and building openings | Prevent re-entry or ignition |
| **Ignition at Tip** | Pilot flame or spark ignitor (optional but recommended) | Burn small releases in controlled manner |
| **Rain Cap** | Weather protection with >4× vent area | Prevent water ingress without restricting flow |

### 8.3 Hydrogen Dispersion Modeling

For major installations, perform CFD (Computational Fluid Dynamics) modeling to predict:
- Hydrogen concentration contours for leak scenarios
- Effect of wind direction and speed
- Identification of accumulation zones

**Design Criterion**: For a 10 kg/min leak, hydrogen concentration < 25% LEL (1% by volume) at 10m downwind under 2 m/s wind.

## 9. Bonding and Grounding

### 9.1 Static Electricity Hazards

Hydrogen's low minimum ignition energy (0.017 mJ) makes it susceptible to static ignition. Sources:
- Fuel flow through hoses (triboelectric charging)
- Clothing friction (especially synthetic fabrics)
- Separation of dissimilar materials

### 9.2 Bonding Requirements

| Connection | Resistance | Verification |
|------------|------------|--------------|
| **GSE Truck to Aircraft** | < 10 ohms | Test with ohmmeter before connecting hose |
| **GSE Truck to Ground** | < 25 ohms | Via tires (conductive) or ground cable |
| **Hose to Nozzle** | < 1 ohm (continuous metal path) | Built-in bonding |
| **Operator Gloves** | Use conductive gloves or ensure metal-to-metal contact | Avoid insulating gloves during connection |

### 9.3 Grounding Cable

- **Size**: 6 AWG (13 mm²) copper cable minimum
- **Clamps**: Positive-contact clamps (no paint scraping; penetrate to bare metal)
- **Connection Sequence**: 
  1. Connect ground cable to aircraft
  2. Connect ground cable to GSE
  3. Verify < 10 ohms with ohmmeter
  4. Connect fuel nozzle
- **Disconnection Sequence**: Reverse order

## 10. Personnel Protection

### 10.1 Personal Protective Equipment (PPE)

| PPE Item | Specification | Purpose |
|----------|---------------|---------|
| **Cryogenic Gloves** | Rated to -253°C, loose-fitting | Protect from cold burns |
| **Face Shield** | Full-face polycarbonate | Protect from LH2 splash |
| **Flame-Resistant Clothing** | Nomex or equivalent (not synthetic) | Prevent clothing ignition |
| **Steel-Toe Boots** | Conductive soles (< 10⁶ ohms) for static dissipation | Foot protection and grounding |
| **Safety Glasses** | ANSI Z87.1 rated, under face shield | Eye protection |

### 10.2 Training and Competency

All personnel working with H2 GSE shall complete:

| Training Module | Duration | Content |
|----------------|----------|---------|
| **Hydrogen Safety Fundamentals** | 4 hours | Properties, hazards, emergency response |
| **GSE Operation** | 8 hours | Normal procedures, interlocks, troubleshooting |
| **Emergency Procedures** | 4 hours | E-stop, evacuation, fire response, first aid for cryogenic burns |
| **Practical Exercises** | 8 hours | Simulated refueling, leak response, fire drill |
| **Refresher Training** | 4 hours annually | Review procedures and lessons learned |

**Certification**: Issue competency certificate after successful completion; re-certify annually.

## 11. Emergency Response Equipment

| Equipment | Specification | Location |
|-----------|---------------|----------|
| **Portable H2 Detector** | 0-100% LEL range, < 10 sec response | Operator carries during refueling |
| **Fire Extinguisher** | 20-lb dry chemical (Class BC) | Mounted on GSE within 10m of operator |
| **First Aid Kit** | Include burn treatment (non-adhesive dressings, saline, burn gel) | GSE cab |
| **Emergency Eyewash** | Portable, 15-minute supply | For cryogenic splashes |
| **Communication Radio** | Direct link to airport fire station and tower | Operator carries |
| **Wind Sock or Anemometer** | Visual wind direction indicator | Near refueling location |

## 12. Safety Audits and Inspections

### 12.1 Pre-Operation Checks (Daily)

| Item | Check | Acceptance |
|------|-------|------------|
| **H2 Sensors** | Function test (bump test with 50% LEL calibration gas) | Alarm activates within 10 seconds |
| **ESV** | Activate E-stop, verify valve closure | Closes in < 2 seconds, fuel flow stops |
| **Fire Detectors** | Test lamp (UV/IR detectors) | Alarm activates |
| **Bonding Cable** | Visual inspection for damage; resistance test | < 10 ohms |
| **Hose and Nozzle** | Visual inspection for damage, leaks, frost | No visible damage |

### 12.2 Periodic Inspections

| Inspection | Frequency | Performed By |
|------------|-----------|--------------|
| **H2 Sensor Calibration** | 6 months | Qualified technician with certified calibration gas |
| **Pressure Relief Valve Test** | 5 years (or per code) | Authorized inspector (AI) |
| **Fire Suppression System** | 12 months | Fire protection contractor |
| **Structural Integrity (Tank, Piping)** | 5 years | NDT (non-destructive testing) specialist |

## 13. Cross-References

- **Parent Document**: [03-00-06_Engineering](../00_INDEX.md)
- **Related H2 GSE Engineering**: 
  - [03-00-06-02-01A_LH2_Fueling_GSE_Design](./03-00-06-02-01A_LH2_Fueling_GSE_Design.md)
  - [03-00-06-02-02A_Cryogenic_GSE_Requirements](./03-00-06-02-02A_Cryogenic_GSE_Requirements.md)
  - [03-00-06-02-04A_H2_GSE_Materials](./03-00-06-02-04A_H2_GSE_Materials.md)
- **GSE Safety Requirements**: [03-00-02_Safety](../../03-00-02_Safety/)
- **GSE Operations**: [03-10_Operations](../../../03-10_Operations/)

## 14. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-06-02-03A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Engineering & Certification WG

---
