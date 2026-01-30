# 10-INST-H2-004 - Emergency Purge Installation

## 1. Purpose

Installation procedures for emergency hydrogen purge systems used to rapidly vent LH2 from aircraft fuel tanks during emergency situations.

## 2. Scope

- Emergency purge system components and design
- Installation of purge connections and equipment
- Activation procedures and safety protocols
- Integration with emergency response systems

**Effectivity**: All parking facilities supporting AMPEL360-BWB-H2 aircraft with LH2 fuel

## 3. Applicable Documents

- **ATA 28** - Fuel System
- **NFPA 2** - Hydrogen Technologies Code
- **SAE AS6968** - Hydrogen Aircraft GSE
- **ISO 13984** - Liquid Hydrogen safety

## 4. Safety Precautions

⚠️ **WARNINGS**

- Emergency purge releases large volumes of H2 - creates flammable atmosphere
- Evacuate all personnel minimum 100 ft before activating purge
- Purge may create cold vapor cloud that settles temporarily
- Never attempt to light off H2 cloud - allow natural dispersion
- Emergency responders must be briefed on purge system before operations

## 5. Emergency Purge System Overview

### 5.1 Function and Purpose

**Purpose**: Rapidly empty LH2 fuel tanks in emergency situations
- Fire on or near aircraft
- Major fuel system leak
- Preparation for emergency towing
- Other situations requiring immediate H2 removal

**Design Criteria**:
- Purge rate: 500-1000 lb/min (dependent on tank size)
- Complete purge time: 15-30 minutes (full tanks)
- Remote activation from safe distance (100+ ft)
- Fail-safe design (power failure does not prevent activation)
- Manual backup if automatic system fails

### 5.2 System Components

| Component | Function | Specification |
|-----------|----------|---------------|
| Emergency Purge Valve | Opens to dump H2 | 6-8" diameter, normally closed |
| Vent Stack | Directs H2 upward | 20 ft height minimum, 6-8" diameter |
| Remote Activation Panel | Activates purge from safe distance | 100 ft from aircraft minimum |
| Backup Manual Valve | Manual purge if remote fails | Accessible without aircraft approach |
| Pressure Relief | Overpressure protection | Set 10% above tank design pressure |
| Flow Indicator | Confirms purge flow | Visual or electronic |
| Temperature Sensors | Monitor vent temperature | Detect blockage or abnormal conditions |

## 6. Installation Requirements

### 6.1 Vent Stack Installation

**Location**: 
- Minimum 50 ft from buildings and structures
- Downwind of prevailing wind (if possible)
- Clear overhead space (no obstructions within 50 ft above)
- Accessible for maintenance

**Height**: 
- Minimum 20 ft above ground (higher than normal vent)
- Minimum 10 ft above any adjacent structure within 50 ft
- High enough to clear H2 detection zones

**Design**:
- Diameter: 6-8" (match purge valve size)
- Material: Stainless steel 316L
- Insulation: Foam or vacuum jacket (prevent atmospheric moisture condensation)
- Guy wires: Required if height >20 ft
- Lightning protection: Bonding to ground grid
- Discharge: Upward only, no rain cap

**Installation Procedure**:

1. Survey and mark vent stack location
2. Install foundation pad (concrete, 4 ft x 4 ft x 6" thick)
3. Install base plate with anchor bolts
4. Erect vent stack sections
5. Install guy wires if required (3 minimum, 120° spacing)
6. Bond stack to grounding grid (verify <0.003 ohms resistance)
7. Install lightning protection (air terminal at top)
8. Install signage: "EMERGENCY H2 PURGE VENT - STAY CLEAR 100 FT"

### 6.2 Emergency Purge Valve Installation

**Location**: On aircraft fuel system (installed by aircraft manufacturer)
**Ground Interface**: Quick-connect coupling at aircraft service panel

**Ground Equipment Installation**:

1. **Purge line from aircraft to vent stack**
   - Material: Stainless steel, insulated
   - Diameter: 6" minimum (match valve size)
   - Length: As short as practical (minimize pressure drop)
   - Supports: Every 10 ft, allow thermal contraction
   - Quick-disconnect at aircraft end (cryogenic-rated)

2. **Activation mechanism**
   - Pneumatic or electric actuator on purge valve
   - Air supply: 80-100 psig, oil-free compressed air
   - Electrical: 115V AC or 28V DC, explosion-proof
   - Backup: Manual handwheel if actuator fails

3. **Flow indication**
   - Paddle-type flow switch in vent line
   - Visual indicator (flag or light) visible from activation panel
   - Remote indication at activation panel

### 6.3 Remote Activation Panel Installation

**Location**:
- Minimum 100 ft from aircraft
- Clear line of sight to aircraft and vent stack
- Protected from weather (enclosure or shelter)
- Near emergency assembly point

**Panel Components**:
- Emergency purge activation button (red, protected cover)
- Purge status indicator (lights: READY, PURGING, COMPLETE)
- Abort/close button (yellow)
- Tank pressure gauge (displays aircraft tank pressure remotely)
- Flow indicator (confirms H2 flowing)
- Communication link (to aircraft and/or control tower)

**Installation Procedure**:

1. Install panel enclosure or shelter
2. Run electrical/pneumatic lines from aircraft purge valve to panel
   - Underground preferred (burial depth 24" minimum)
   - Overhead if underground not practical (minimum 12 ft height)
   - Explosion-proof conduit in H2 zones
3. Wire panel components per electrical drawings
4. Install communication equipment (radio or hardwire)
5. Test all functions (use nitrogen or air, not H2)
6. Install instructional placard with activation procedures
7. Illuminate panel for night operations

## 7. Operational Procedures

### 7.1 Pre-Activation (Emergency Decision)

**Activate Emergency Purge If**:
- Fire on or adjacent to aircraft
- Major H2 fuel system leak (>1 gpm)
- Directed by incident commander
- Other imminent threat requiring H2 removal

**Do NOT Activate If**:
- Minor leak that can be controlled
- No imminent threat
- Personnel not evacuated

### 7.2 Emergency Purge Activation

1. **Sound evacuation alarm** - evacuate all personnel 100+ ft
2. **Verify personnel clear** - visual check and radio confirmation
3. **Establish exclusion zone** - 100 ft radius around aircraft and vent
4. **Don PPE** - operator at activation panel wears PPE
5. **Open protective cover** on activation button
6. **Press ACTIVATE button** - hold for 3 seconds
7. **Confirm activation** - check status indicator shows "PURGING"
8. **Confirm flow** - check flow indicator, visual observation of vent
9. **Monitor purge** - observe tank pressure decreasing
10. **Purge complete when**:
    - Tank pressure <5 psig
    - Flow indicator shows no flow
    - Estimated time elapsed (based on tank volume)
11. **Secure system** - close purge valve (automatic or manual)
12. **Document event** - time, duration, quantity purged, reason

### 7.3 Post-Purge Actions

1. **Do not approach aircraft** for minimum 15 minutes (allow H2 dispersion)
2. **Monitor H2 sensors** - verify H2 concentration <25% LEL before re-entry
3. **Inspect purge system** - check for ice, damage, proper closure
4. **Inspect aircraft** - look for damage from purge or original emergency
5. **Inert fuel tanks** - purge with nitrogen or dry air before maintenance
6. **Notify authorities** - emergency purge is reportable event
7. **Document incident** - complete report with timeline and actions

## 8. Testing and Maintenance

### 8.1 System Testing

**Functional Test** (quarterly):
- Test remote activation signal (actuate valve using test button, not H2)
- Verify indication and communication systems
- Check power supply and backup battery (if equipped)
- Test abort/close function
- Document test results

**Full System Test** (annually):
- Perform functional test as above
- Leak test all connections (use nitrogen)
- Inspect vent stack for corrosion, blockage, damage
- Load test guy wires (if equipped)
- Verify grounding resistance
- Exercise purge valve (full stroke test with inert gas)

### 8.2 Maintenance

**Monthly**:
- Visual inspection of all components
- Check activation panel for damage or weather intrusion
- Verify signage legible

**Quarterly**:
- Lubricate purge valve and actuator (per manufacturer)
- Test manual backup activation
- Inspect insulation on purge line and vent stack

**Annually**:
- Complete inspection per test procedure above
- Replace any worn or damaged components
- Update emergency procedures if system changes

## 9. BWB Considerations

- BWB may have multiple fuel tanks requiring multiple purge points
- Purge activation may need to be sequential or simultaneous
- Verify purge capacity adequate for BWB tank volume
- Consider BWB ground clearance for purge line routing

## 10. Emergency Responder Coordination

### 10.1 Pre-Incident Planning

- Provide emergency responders (fire, police, EMS) with:
  - Facility tour including purge system location
  - Training on H2 hazards and purge procedures
  - Copy of emergency procedures
  - Emergency contact information
  - Site map with H2 zones marked

### 10.2 Incident Response

- Incident commander has authority to order purge activation
- Aircraft operator/owner must be notified if possible
- Purge activation does not require owner permission if imminent threat
- Emergency responders must maintain exclusion zone during purge

## 11. Quality Assurance

- Quarterly functional testing mandatory
- Maintain test and maintenance logs
- Train all personnel on purge system operation
- Review and update procedures annually
- Investigate any false activations

## 12. Cross-References

- **10-INST-H2-001** - H2 Venting System Installation
- **10-INST-H2-002** - H2 Detection Sensors
- **ATA 28** - Fuel System
- **Emergency Response Plan** - Site-specific

## 13. Revision History

| Rev | Date       | Author              | Description          |
|-----|------------|---------------------|----------------------|
| A   | 2025-12-09 | Amedeo Pelliccia    | Initial release      |

---

## Document Control

- **Document ID**: 10-INST-H2-004
- **Revision**: A
- **Status**: DRAFT - Subject to human review and approval
- **Safety Critical**: YES
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-12-09
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
