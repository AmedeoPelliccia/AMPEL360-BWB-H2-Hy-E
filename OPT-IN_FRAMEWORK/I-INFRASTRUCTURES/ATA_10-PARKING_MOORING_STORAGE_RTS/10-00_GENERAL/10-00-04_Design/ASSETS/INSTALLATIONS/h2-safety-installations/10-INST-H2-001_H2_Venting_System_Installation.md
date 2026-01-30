# 10-INST-H2-001 - H2 Venting System Installation

## 1. Purpose

Installation procedures for hydrogen venting systems during parking operations of AMPEL360-BWB-H2 aircraft to safely release boil-off gas from LH2 fuel tanks.

## 2. Scope

- H2 vent system components and installation
- Vent outlet positioning and clearances
- Ventilation requirements for enclosed parking
- Integration with H2 detection systems

**Effectivity**: All AMPEL360-BWB-H2 aircraft parking facilities with LH2 fuel

## 3. Applicable Documents

- **ATA 28** - Fuel System
- **NFPA 2** - Hydrogen Technologies Code
- **SAE AS6968** - Hydrogen Aircraft GSE
- **ISO 13984** - Liquid Hydrogen - Land Vehicle Fueling System Interface
- **NFPA 55** - Compressed Gases and Cryogenic Fluids Code

## 4. Safety Precautions

⚠️ **WARNINGS**

- **FLAMMABLE GAS**: Hydrogen is extremely flammable (4-75% concentration in air)
- **CRYOGENIC HAZARD**: LH2 temperature -253°C (-423°F) causes severe cold burns
- **ASPHYXIATION**: Hydrogen displaces oxygen in confined spaces
- **EXPLOSION RISK**: Hydrogen-air mixtures can explode with minimal ignition energy
- **PERSONNEL TRAINING**: Only H2-trained personnel may work on venting systems

⚠️ **CAUTIONS**

- Vent outlets must direct H2 upward and away from aircraft and buildings
- Minimum 15 ft clearance from vent outlet to any ignition source
- Never cap or obstruct H2 vent outlets
- Continuous H2 monitoring required during parking operations

## 5. H2 Venting System Overview

### 5.1 Function

**Purpose**: Safely release hydrogen boil-off gas from LH2 tanks during parking
- LH2 continuously boils due to heat ingress
- Boil-off rate approximately 0.1-1.0% of tank volume per day
- Venting prevents tank over-pressurization
- Controlled release minimizes H2 accumulation

### 5.2 System Components

| Component | Function | Specification |
|-----------|----------|---------------|
| Tank Pressure Relief Valve | Overpressure protection | Set pressure XX psig |
| Vent Lines | Gas transport from tank to outlet | Stainless steel, vacuum-insulated |
| Vent Mast/Stack | Directs H2 upward | Height 10 ft minimum above aircraft |
| Flame Arrestor | Prevents flame propagation | Per NFPA 2 |
| Check Valves | Prevent backflow | Redundant design |
| Temperature Sensors | Monitor vent temperature | -253°C to +100°C range |
| Pressure Sensors | Monitor tank pressure | 0-100 psig range |

## 6. Installation Requirements

### 6.1 Vent Outlet Positioning

**Height Requirements**:
- Minimum 10 ft above highest point of aircraft
- Minimum 15 ft above ground level
- For enclosed parking: Through roof with upward discharge

**Clearances from Vent Outlet**:
- To any building: 25 ft minimum
- To ignition sources: 50 ft minimum
- To air intakes (HVAC): 50 ft minimum
- To personnel areas: 25 ft minimum
- To other aircraft: 50 ft minimum

**Orientation**:
- Discharge vertically upward
- No bend >15° from vertical in last 5 ft
- Wind deflector cap optional (must not restrict flow)
- Protected from precipitation (rain, snow)

### 6.2 Vent Line Installation

**Material**: Stainless steel 316L or equivalent
**Insulation**: Vacuum-jacketed or foam-insulated for cryogenic service
**Size**: Per aircraft fuel system design (typically 1-2" diameter)
**Support**: Every 5 ft maximum, allow for thermal contraction
**Flexibility**: Include expansion loops or flexible sections

**Installation Steps**:

1. **Route vent line from aircraft fuel system**
   - Follow aircraft fuel system interface points (ref ATA 28)
   - Maintain minimum 6" clearance from electrical systems
   - Avoid low points (condensation trap)
   - Slope upward toward vent outlet (minimum 1:100)

2. **Install supports and hangers**
   - Use stainless steel supports (no galvanic corrosion)
   - Allow for thermal contraction (line cools to -253°C)
   - Insulate supports from structure (thermal breaks)
   - Verify support load capacity

3. **Install pressure relief and safety devices**
   - Install flame arrestor near vent outlet
   - Install check valves to prevent backflow
   - Install pressure relief valve per design
   - Install temperature and pressure sensors

4. **Connect to aircraft**
   - Use quick-disconnect couplings (H2-rated, cryogenic)
   - Install at fuel system vent outlet (typically upper fuselage)
   - Verify coupling compatibility and sealing
   - Apply cryogenic sealant (if specified)

5. **Install vent mast/stack**
   - Secure mast to ground or structure
   - Verify vertical alignment (±2° tolerance)
   - Install guy wires if height >15 ft
   - Ground mast electrically (bonding)

### 6.3 Enclosed Parking (Hangar) Requirements

**Additional Requirements for Hangars**:

1. **Ventilation System**
   - Mechanical ventilation required (natural ventilation insufficient)
   - Minimum 6 air changes per hour
   - Ventilation intakes at low level (H2 rises, but dense cold vapor may settle)
   - Exhaust outlets at high level (H2 accumulates at ceiling)

2. **Vent Routing Through Roof**
   - Vent line penetrates roof
   - Discharge minimum 10 ft above roof level
   - Seal roof penetration (weatherproof)
   - Install roof flashing

3. **H2 Detection**
   - Multiple H2 sensors throughout hangar
   - Sensors at ceiling level (primary)
   - Sensors at mid-height (secondary)
   - Alarm at 25% LEL (1% H2)
   - Emergency shutdown at 50% LEL (2% H2)

4. **Electrical Classification**
   - Hangar classified as Class I, Division 2 (NEC)
   - All electrical equipment explosion-proof or intrinsically safe
   - No ignition sources within 25 ft of vent outlet

## 7. H2 Detection System Integration

### 7.1 Detection Sensor Placement

**Sensor Locations** (minimum):
- 4 sensors in circle around vent outlet (5 ft radius, at vent height)
- 2 sensors at aircraft fuel system vent connection points
- 2 sensors at ground level (below aircraft)
- Additional sensors based on hangar size and configuration

**Sensor Specifications**:
- Type: Catalytic or electrochemical
- Range: 0-4% H2 (0-100% LEL)
- Accuracy: ±5% of reading
- Response time: <10 seconds (T90)
- Alarm setpoints: 25% LEL (warning), 50% LEL (alarm)

### 7.2 Alarm and Response

**Warning Alarm** (25% LEL, 1% H2):
- Audible and visual alarm
- Notify ground personnel
- Increase ventilation (if equipped)
- Monitor continuously

**Danger Alarm** (50% LEL, 2% H2):
- Evacuate area immediately
- Activate emergency ventilation
- Shut down non-essential electrical equipment
- Summon emergency response team
- Do not enter until H2 <25% LEL

## 8. BWB Considerations

### 8.1 BWB Fuel Tank Location

- LH2 tanks typically located in center fuselage/wing root area
- Vent outlets on upper surface of BWB (highest point)
- Multiple vent outlets possible due to distributed tank design
- Access to vent connections may require elevated platforms

### 8.2 BWB Upper Surface Access

- Vent connections on upper BWB surface require access platforms
- Platforms must be bonded to aircraft (electrical continuity)
- Non-sparking materials and tools required
- Fall protection for personnel working at height

## 9. Operational Procedures

### 9.1 Pre-Parking Checklist

- [ ] Verify vent system integrity (visual inspection)
- [ ] Test H2 detection sensors (calibration current)
- [ ] Check ventilation system operation (if enclosed)
- [ ] Verify emergency equipment availability
- [ ] Brief personnel on H2 hazards and emergency procedures
- [ ] Establish exclusion zone (25 ft minimum)
- [ ] Post H2 safety signage

### 9.2 Vent Connection Procedure

1. **Don cryogenic PPE** (face shield, insulated gloves, apron)
2. **Verify aircraft fuel system depressurized** (<5 psig)
3. **Connect grounding cable** to aircraft (verify continuity)
4. **Approach vent connection point** (use elevated platform if required)
5. **Inspect coupling** for damage, contamination, ice
6. **Align coupling** with aircraft vent outlet
7. **Connect coupling** (push or screw-type per design)
8. **Verify coupling engagement** (visual and tactile check)
9. **Open isolation valves** (aircraft and ground side, if present)
10. **Monitor H2 sensors** for leaks (check for H2 increase)
11. **Label connection** ("H2 VENT CONNECTED - DO NOT DISCONNECT")

### 9.3 Vent Disconnection Procedure

1. **Verify tank pressure <5 psig** (check gauges)
2. **Close isolation valves** (if present)
3. **Don cryogenic PPE**
4. **Disconnect coupling** (reverse connection procedure)
5. **Cap aircraft vent outlet** (protective cap to prevent contamination)
6. **Disconnect grounding cable**
7. **Inspect coupling** and vent line for ice, damage
8. **Remove labels** and signage
9. **Store vent equipment** properly

## 10. Quality Assurance

### 10.1 Installation Inspection

- Leak test all connections (H2 leak detector or bubble test with N2)
- Verify vent line support adequacy
- Check electrical bonding (< 0.003 ohms)
- Test H2 detection system (span gas calibration)
- Document installation with photos
- Sign-off by H2 qualified inspector

### 10.2 Periodic Inspection

- **Daily** (when aircraft present): Visual inspection of vent connections
- **Weekly**: H2 sensor calibration check
- **Monthly**: Leak test vent system
- **Annually**: Complete system inspection and testing

### 10.3 Maintenance Records

- Maintain log of vent connections and disconnections
- Record H2 sensor readings during operations
- Document any H2 alarms or incidents
- Track maintenance and repairs

## 11. Emergency Procedures

### 11.1 H2 Leak at Vent Connection

1. Evacuate personnel to safe distance (100 ft minimum)
2. Activate emergency alarm
3. Do not attempt to close valves or tighten connections
4. Allow H2 to vent safely (it will disperse upward)
5. Monitor H2 concentration remotely
6. Summon emergency response team
7. Re-enter only when H2 <25% LEL and authorized

### 11.2 Fire at Vent Outlet

1. Evacuate area immediately
2. DO NOT attempt to extinguish H2 flame
3. Allow controlled burn (safer than extinguishing and creating explosive cloud)
4. Summon fire department
5. Protect exposures (cool adjacent structures with water)
6. If fire must be extinguished, use dry chemical or CO2 (then eliminate ignition source)

## 12. Cross-References

- **ATA 28** - Fuel System
- **10-INST-H2-002** - H2 Detection Sensors
- **10-INST-H2-004** - Emergency Purge Installation
- **NFPA 2** - Hydrogen Technologies Code
- **SAE AS6968** - Hydrogen Aircraft GSE

## 13. Revision History

| Rev | Date       | Author              | Description          |
|-----|------------|---------------------|----------------------|
| A   | 2025-12-09 | Amedeo Pelliccia    | Initial release      |

---

## Document Control

- **Document ID**: 10-INST-H2-001
- **Revision**: A
- **Status**: DRAFT - Subject to human review and approval
- **Safety Critical**: YES
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
