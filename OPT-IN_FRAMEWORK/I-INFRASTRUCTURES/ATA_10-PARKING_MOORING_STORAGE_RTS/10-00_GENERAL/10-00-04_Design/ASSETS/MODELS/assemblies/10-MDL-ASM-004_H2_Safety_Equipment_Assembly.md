# 10-MDL-ASM-004 — H2 Safety Equipment Assembly

## 1. Purpose

This assembly model defines the hydrogen safety equipment required for safe parking and storage of the AMPEL360-BWB-H2 aircraft. It includes detection, ventilation, fire suppression, and protective equipment specific to hydrogen fuel systems.

## 2. Scope

This model applies to:

- **Aircraft Type**: AMPEL360-BWB-H2-Hy-E
- **Safety Scenarios**:
  - Normal parking operations with H2 onboard
  - Fuel system maintenance with H2 present
  - Emergency H2 leak response
  - Fire suppression and emergency procedures

**Includes**:
- H2 detection and monitoring equipment
- Ventilation and dispersion systems
- Fire suppression equipment
- Personal protective equipment (PPE) stations
- Safety signage and barriers

## 3. Model Information

| Parameter | Value |
|-----------|-------|
| Model Number | 10-MDL-ASM-004 |
| Model Type | Assembly |
| CAD System | SolidWorks |
| Version | 1.0 |
| Status | ACTIVE |
| Created | 2025-12-09 |
| Last Modified | 2025-12-09 |

## 4. Available Formats

| Format | Filename | Location | Checksum |
|--------|----------|----------|----------|
| SolidWorks | 10-MDL-ASM-004_H2_Safety_Equipment.sldasm | `cad-native/solidworks/` | TBD |
| STEP AP242 | 10-MDL-ASM-004_H2_Safety_Equipment.step | `exchange-formats/step/` | TBD |
| glTF 2.0 | 10-MDL-ASM-004_H2_Safety_Equipment.glb | `visualization/gltf/` | TBD |

## 5. Assembly Description

### 5.1 H2 Detection System

**H2 Leak Detectors (8x)**
- Fixed detection stations around aircraft
- Detection range: 0-4% H2 by volume
- Response time: < 1 second
- Alarm levels: 1% (warning), 2% (alarm), 4% (evacuation)
- Component: [10-MDL-H2-002 — H2 Detector Housing](../components/h2-systems/10-MDL-H2-002_H2_Detector_Housing.md)

**Detection Station Locations:**
1. Near fuel tank vents (4x)
2. Below aircraft belly (2x)
3. Ground equipment areas (2x)

**Portable H2 Detectors (4x)**
- Handheld units for mobile inspection
- Battery powered, intrinsically safe
- Data logging capability

### 5.2 Ventilation System

**Forced Air Ventilation (for enclosed parking)**
- Air change rate: 12 ACH minimum
- Direction: Low-level exhaust (H2 rises)
- High-level fresh air intake
- Emergency ventilation: 30 ACH

**Wind Socks and Indicators (4x)**
- Positioned around parking area
- Monitor wind direction for H2 dispersion
- Illuminated for night operations

### 5.3 Fire Suppression Equipment

**Mobile Fire Suppression Carts (2x)**
- Dry powder extinguisher (Class D)
- Water spray system (cooling)
- CO2 system (inerting)
- Positioning: Within 20m of aircraft

**Fixed Fire Suppression (for enclosed areas)**
- Water deluge system
- Foam application capability
- Automatic activation on detection

**Emergency Equipment Stations (4x)**
- Fire extinguishers (5kg dry powder)
- Fire blankets
- Emergency shut-off tools
- First aid kits

### 5.4 Protective Equipment

**PPE Stations (2x)**
- Anti-static clothing
- Face shields
- Insulated gloves (cryogenic)
- Safety boots (conductive)
- Hard hats
- Emergency breathing apparatus

### 5.5 Safety Barriers and Signage

**Primary Safety Zone (10m radius)**
- Physical barriers (retractable posts and chains)
- Warning signage (multi-language)
- Ground markings (yellow and black stripes)
- Access control points

**Secondary Safety Zone (25m radius)**
- Warning signs at perimeter
- Controlled access during operations
- Equipment staging area

## 6. Component List

| Component ID | Description | Quantity | Critical |
|--------------|-------------|----------|----------|
| 10-MDL-H2-001 | H2 Vent Valve | 4 | Yes |
| 10-MDL-H2-002 | H2 Detector Housing | 8 | Yes |
| 10-MDL-H2-003 | Cryo Insulation Cover | 2 | Yes |
| SUPP-001 | Fire Suppression Cart | 2 | Yes |
| SUPP-002 | PPE Station | 2 | Yes |
| SUPP-003 | Safety Barrier Set | 12 | No |
| SUPP-004 | Warning Sign Set | 16 | No |

## 7. Materials

| Component | Material | Specification | Notes |
|-----------|----------|---------------|-------|
| Detector Housing | Aluminum Alloy | 6061-T6 | Corrosion resistant |
| Vent Valve Body | Stainless Steel 316L | AMS 5507 | Cryogenic compatible |
| Insulation Cover | Aerogel Composite | Custom specification | Ultra-low thermal conductivity |
| Barriers | Aluminum/Plastic | Lightweight | Retractable posts |
| Signage | Aluminum/Reflective | ANSI Z535 | Weather resistant |

## 8. H2 Safety Zones

### 8.1 Primary Safety Zone (10m radius)

**Restrictions:**
- No open flames or spark sources
- No smoking
- No hot work (welding, grinding)
- Intrinsically safe equipment only
- Continuous H2 monitoring required
- Limited personnel access

**Required Equipment:**
- Fixed H2 detectors (4x minimum)
- Fire suppression equipment
- Emergency ventilation
- Safety barriers

### 8.2 Secondary Safety Zone (25m radius)

**Restrictions:**
- Controlled access during H2 operations
- No unauthorized vehicles
- Fire suppression equipment present
- Emergency response team on standby

**Required Equipment:**
- Portable H2 detectors
- Fire extinguishers
- Communication equipment
- PPE stations

### 8.3 Hydrogen Dispersion Analysis

See related CFD analysis:
- [10-SIM-CFD-001 — H2 Dispersion Analysis](../simulations/cfd/10-SIM-CFD-001_H2_Dispersion_Analysis.md)

Key findings:
- H2 rises rapidly due to low density (fastest at 10-15 m/s)
- Outdoor parking preferred for natural dispersion
- Wind speed > 2 m/s effectively disperses H2
- Enclosed spaces require forced ventilation

## 9. H2/BWB Considerations

### 9.1 BWB-Specific Layout

**Fuel Tank Locations:**
- Integrated wing-body fuel tanks
- Multiple tank compartments
- Vent locations on upper wing surface
- Large surface area for potential leaks

**Equipment Positioning:**
- Detectors positioned based on vent locations
- Access routes avoid wing upper surface
- Equipment staging on wing trailing edge side
- Emergency equipment accessible from multiple directions

### 9.2 Hydrogen Properties

| Property | Value | Implication |
|----------|-------|-------------|
| Density | 0.0899 kg/m³ (at STP) | Lighter than air, rises rapidly |
| Boiling Point | -252.87°C | Cryogenic temperatures |
| Flammability Range | 4-75% in air | Wide flammability range |
| Auto-ignition Temp | 585°C | Relatively high |
| Flame Visibility | Nearly invisible | Special flame detection required |
| Diffusion Rate | Very high | Disperses quickly outdoors |

## 10. Safety Procedures

### 10.1 Pre-Parking Checklist

- [ ] H2 detection system operational and calibrated
- [ ] Fire suppression equipment inspected and ready
- [ ] Safety zones marked and barriers in place
- [ ] PPE available and inspected
- [ ] Emergency response team briefed
- [ ] Weather conditions acceptable (wind > 2 m/s for outdoor)
- [ ] Communication systems tested

### 10.2 During Parking Operations

- [ ] Continuous H2 monitoring active
- [ ] Safety zones enforced
- [ ] Personnel trained and equipped with PPE
- [ ] Fire suppression equipment positioned
- [ ] Communication maintained with operations center
- [ ] Log all H2 detection readings

### 10.3 Emergency Response Procedures

**H2 Leak Detected (1-2% concentration):**
1. Activate warning alarms
2. Evacuate non-essential personnel from primary zone
3. Activate emergency ventilation
4. Shut down all electrical equipment
5. Prepare fire suppression equipment
6. Locate and isolate leak source

**H2 Leak Critical (>2% concentration):**
1. Activate evacuation alarms
2. Evacuate all personnel from secondary zone
3. Activate emergency response team
4. Shut down all electrical power to area
5. Deploy fire suppression equipment
6. Notify emergency services

**H2 Fire:**
1. Activate fire suppression systems
2. Evacuate all personnel immediately
3. Call emergency services
4. Do not attempt to extinguish unless trained
5. If safe, shut off H2 supply
6. Establish safety perimeter (100m minimum)

## 11. Related Documentation

### Related Models
- [10-MDL-ASM-001 — BWB Parking Configuration](./10-MDL-ASM-001_BWB_Parking_Configuration.md)
- [10-MDL-H2-001 — H2 Vent Valve](../components/h2-systems/10-MDL-H2-001_H2_Vent_Valve.md)
- [10-MDL-H2-002 — H2 Detector Housing](../components/h2-systems/10-MDL-H2-002_H2_Detector_Housing.md)
- [10-MDL-H2-003 — Cryo Insulation Cover](../components/h2-systems/10-MDL-H2-003_Cryo_Insulation_Cover.md)

### Related Simulations
- [10-SIM-CFD-001 — H2 Dispersion Analysis](../simulations/cfd/10-SIM-CFD-001_H2_Dispersion_Analysis.md)
- [10-SIM-CFD-002 — Ventilation Flow Analysis](../simulations/cfd/10-SIM-CFD-002_Ventilation_Flow_Analysis.md)

### Related Specifications
- TBD: REQ-10-400 — H2 Safety Equipment Requirements
- TBD: REQ-10-410 — Detection System Requirements
- TBD: REQ-10-420 — Fire Suppression Requirements

### Related Standards
- **SAE AS6968** — Hydrogen Aircraft Systems
- **ISO 14687** — Hydrogen fuel — Product specification
- **NFPA 2** — Hydrogen Technologies Code
- **ISO 19880-1** — Gaseous hydrogen — Fueling stations
- **SAE AIR7901** — Hydrogen Propulsion for Aircraft
- **ANSI Z535** — Safety Signs and Tags

## 12. Training Requirements

All personnel working near H2-fueled aircraft must complete:

1. **H2 Safety Awareness** (4 hours)
   - H2 properties and hazards
   - Detection and monitoring
   - Emergency procedures

2. **Equipment Operation** (2 hours)
   - H2 detectors
   - Fire suppression equipment
   - PPE donning and use

3. **Emergency Response** (4 hours)
   - Leak response procedures
   - Fire response procedures
   - Evacuation procedures
   - First aid for cryogenic exposure

4. **Practical Exercises** (4 hours)
   - Simulated leak scenarios
   - Equipment deployment
   - Emergency evacuation

**Recertification**: Annual

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 1.0 | 2025-12-09 | AMPEL360 Safety Team | Initial release |

---

## Document Control

- **Document ID**: 10-MDL-ASM-004
- **Version**: 1.0
- **Status**: ACTIVE
- **Classification**: Safety Critical
- **Last Updated**: 2025-12-09
- **Owner**: AMPEL360 ATA 10 Safety Team
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
