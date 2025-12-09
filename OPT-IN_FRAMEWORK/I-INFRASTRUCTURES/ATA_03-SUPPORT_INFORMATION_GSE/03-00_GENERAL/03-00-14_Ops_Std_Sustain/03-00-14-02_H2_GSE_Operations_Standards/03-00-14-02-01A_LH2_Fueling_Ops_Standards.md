---
Title: "LH2 Fueling Operations Standards"
Identifier: "AMPEL360-03-00-14-02-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Hydrogen Operations Team"
ResponsibleOrg: "I-INFRASTRUCTURES H2 GSE Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Operational standards for liquid hydrogen (LH2) fueling operations for AMPEL360 aircraft."
Keywords: ["ATA 03","GSE","LH2","Hydrogen","Fueling","Cryogenic","Operations","Standards"]
Compliance:
  - "SAE AS6968"
  - "ISO 19880-8"
  - "NFPA 2"
  - "ATA iSpec 2200"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../../"
  Siblings:
    - "./03-00-14-02-02A_Cryogenic_Ops_Standards.md"
    - "./03-00-14-02-03A_H2_Safety_Ops_Standards.md"
    - "./03-00-14-02-04A_H2_Emergency_Ops_Standards.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 H2 Operations Team", change: "Initial release" }
---

# 03-00-14-02-01A — LH2 Fueling Operations Standards

## 1. Purpose

This document establishes **operational standards for liquid hydrogen (LH₂) fueling operations** for the AMPEL360 BWB H₂ Hy-E aircraft. It defines procedures, safety requirements, equipment specifications, and operational parameters to ensure safe, efficient, and compliant LH₂ fueling at -253°C.

## 2. Scope

### 2.1 Coverage

This document covers LH₂ fueling operations including:

1. **Pre-Fueling Operations**
   - Safety zone establishment
   - Equipment inspection and setup
   - Communication protocol initiation
   - Environmental condition verification

2. **Fueling Operations**
   - Connection procedures
   - Cooldown and purge cycles
   - Fuel transfer operations
   - Real-time monitoring
   - Quantity verification

3. **Post-Fueling Operations**
   - Disconnection procedures
   - Equipment securing
   - Documentation and reporting
   - Post-operation inspection

4. **Special Procedures**
   - First fill procedures
   - Defueling operations
   - Cold weather operations
   - Emergency disconnection

### 2.2 Exclusions

- Aircraft fuel system design (covered under [ATA 28 — Fuel](../../../../../ATA_28-FUEL/))
- Hydrogen production and storage infrastructure (covered under [ATA 85](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/))
- Maintenance of fueling equipment (covered under [ATA 03-30_ANCHORS](../../../03-30_ANCHORS/))

## 3. Applicable Documents

### 3.1 Hydrogen and Cryogenic Standards

| Standard | Title | Application |
|----------|-------|-------------|
| **[SAE AS6968](https://www.sae.org/standards/content/as6968/)** | Hydrogen Aircraft Refueling | Primary fueling standard |
| **[ISO 19880-8](https://www.iso.org/standard/71940.html)** | Gaseous Hydrogen — Fueling Stations: Part 8 | Fueling protocols |
| **[NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2)** | Hydrogen Technologies Code | Safety requirements |
| **[CGA G-5.4](https://www.cganet.com/)** | Standard for Hydrogen Piping Systems | Piping and connections |
| **[ISO 13985](https://www.iso.org/standard/63534.html)** | Liquid Hydrogen — Land Vehicle Fuel Tanks | Cryogenic fuel handling |

### 3.2 Internal References

- [03-00-14-02-02A_Cryogenic_Ops_Standards.md](./03-00-14-02-02A_Cryogenic_Ops_Standards.md) — Cryogenic operations
- [03-00-14-02-03A_H2_Safety_Ops_Standards.md](./03-00-14-02-03A_H2_Safety_Ops_Standards.md) — H2 safety standards
- [03-00-14-02-04A_H2_Emergency_Ops_Standards.md](./03-00-14-02-04A_H2_Emergency_Ops_Standards.md) — Emergency procedures
- [03-00-02_Safety](../../03-00-02_Safety/) — GSE safety assessments

## 4. Operations/Sustainment Requirements

### 4.1 LH₂ Fueling System Overview

The AMPEL360 LH₂ fueling system comprises:

- **Mobile LH₂ Fueling Unit**: Cryogenic tanker with integrated pumping system
- **Fueling Control System**: Automated monitoring and control
- **Safety Systems**: Emergency shutdown, leak detection, fire suppression
- **Communication Systems**: Dedicated radio frequency for fueling operations
- **Support Equipment**: Cryogenic PPE, leak detectors, safety barriers

### 4.2 Operational Parameters

| Parameter | Specification | Tolerance | Safety Limit |
|-----------|--------------|-----------|--------------|
| **LH₂ Temperature** | -253°C (-423°F) | ±2°C | -250°C to -255°C |
| **Transfer Pressure** | 0.3-1.0 MPa (45-145 psi) | ±0.05 MPa | 1.5 MPa maximum |
| **Flow Rate** | 500-1000 kg/hour | ±50 kg/hour | 1200 kg/hour maximum |
| **Purity** | ≥99.99% | -0.01% | ≥99.95% minimum |
| **Boil-off Rate** | <2% during transfer | +0.5% | 3% maximum |
| **Fill Time (typical)** | 30-45 minutes | ±10 minutes | 60 minutes maximum |

### 4.3 Environmental Conditions

#### 4.3.1 Operating Limits

| Condition | Operating Range | Restricted Operations | Prohibited |
|-----------|----------------|----------------------|------------|
| **Ambient Temperature** | -20°C to +45°C | <-10°C or >40°C | <-25°C or >50°C |
| **Wind Speed** | <25 km/h (15 mph) | 25-40 km/h | >40 km/h |
| **Precipitation** | None or light rain | Moderate rain | Heavy rain or snow |
| **Visibility** | >1000 m | 500-1000 m | <500 m |
| **Lightning** | >15 km (9 miles) | 10-15 km | <10 km |
| **Relative Humidity** | No limit | >90% (monitor condensation) | N/A |

### 4.4 Pre-Fueling Procedures

#### 4.4.1 Safety Zone Establishment

**Exclusion Zones:**

| Zone | Radius | Access Restriction |
|------|--------|-------------------|
| **Inner Safety Zone** | 15 meters from fueling point | Essential personnel only (max 3) |
| **Outer Safety Zone** | 30 meters from fueling point | Authorized personnel with PPE |
| **No-Vehicle Zone** | 50 meters from fueling point | No vehicles except fueling equipment |
| **No-Smoking Zone** | 100 meters from fueling point | Absolutely no ignition sources |

**Zone Marking:**
- High-visibility cones and tape
- Bilingual safety signs (English + local language)
- Flashing warning lights during fueling
- Dedicated safety observer

#### 4.4.2 Equipment Inspection Checklist

```markdown
PRE-FUELING INSPECTION — LH₂ FUELING UNIT

Date: __________ Time: __________ Inspector: __________

FUELING VEHICLE:
☐ External inspection (no visible damage, leaks, or ice buildup)
☐ Pressure gauges functional and calibrated (within last 6 months)
☐ Temperature sensors functional
☐ LH₂ level indicator operational
☐ Emergency shutdown system tested (weekly test completed)
☐ Fire suppression system charged and ready
☐ Leak detection system operational and calibrated
☐ Ground connection verified (bonding cable intact)
☐ Communication radio functional (battery >50%)
☐ Emergency lighting operational

FUELING HOSES AND CONNECTIONS:
☐ Hoses inspected for damage, wear, cracks
☐ Cryogenic insulation intact (no exposed metal)
☐ Breakaway coupling functional (tested monthly)
☐ Adapter compatibility confirmed with aircraft
☐ Dust caps removed and connections clean
☐ No ice buildup on connections

SAFETY EQUIPMENT:
☐ Fire extinguishers accessible (CO₂ and dry chemical)
☐ Emergency shower/eyewash station operational
☐ First aid kit complete and accessible
☐ H₂ gas detectors calibrated and operational (4 units minimum)
☐ Wind direction indicators in place
☐ Safety barriers and cones positioned
☐ Communication equipment tested

PERSONNEL PPE:
☐ All operators wearing full cryogenic PPE
☐ Insulated gloves (minimum -250°C rating)
☐ Face shields or safety goggles
☐ Insulated coveralls or protective suits
☐ Steel-toe safety boots
☐ No synthetic clothing (static risk)

ENVIRONMENTAL CONDITIONS:
☐ Weather within operational limits (see 4.3.1)
☐ Wind speed <25 km/h
☐ No lightning within 15 km
☐ Visibility >1000 m
☐ Ambient temperature within range

COMMUNICATION AND COORDINATION:
☐ Aircraft crew contacted and ready
☐ Airport operations notified
☐ Fire department on standby notification sent
☐ Safety observer assigned and briefed
☐ Emergency procedures reviewed with all personnel

Inspector Signature: _________________ Date/Time: _________________
Supervisor Approval: _________________ Date/Time: _________________
```

### 4.5 Fueling Procedures

#### 4.5.1 Connection Procedure

**Step-by-Step Process:**

1. **Position Fueling Vehicle**
   - Approach from downwind direction
   - Stop at designated distance (5-7 meters from aircraft)
   - Set parking brake and chock wheels
   - Shutdown engine (if applicable)
   - Deploy outriggers for stability

2. **Establish Electrical Bonding**
   - Connect grounding cable from fueling unit to aircraft first
   - Verify continuity with multimeter (<1 ohm resistance)
   - Do not proceed without proper grounding

3. **Connect H₂ Gas Detectors**
   - Position 4 detectors around fueling area:
     - At ground level near connection point
     - At intermediate height (1.5 m)
     - Under aircraft (H₂ rises, monitor accumulation)
     - Downwind of fueling point
   - Verify all detectors reading 0% LEL (Lower Explosive Limit)

4. **Pre-Cool Fueling Line (if required)**
   - Open vent valves
   - Slowly introduce small amount of LH₂ to cool lines
   - Monitor boil-off (expected during cooldown)
   - Continue until venting reduces (indicates lines cold)
   - Close vent valves

5. **Connect Fueling Hose**
   - Remove dust cap from aircraft receptacle
   - Inspect receptacle for ice, debris, or damage
   - Align fueling nozzle carefully (avoid cross-threading)
   - Connect and hand-tighten
   - Torque to specification (typically 40-50 Nm)
   - Verify coupling is fully engaged (visual and mechanical check)

6. **Pre-Transfer Checks**
   - Verify all valves in correct position
   - Confirm fuel quantity indication from aircraft
   - Establish communication with aircraft crew
   - Set flow rate limiter (start low, typically 300 kg/hour)
   - Arm emergency shutdown system

#### 4.5.2 Fuel Transfer Procedure

**Transfer Phases:**

**Phase 1: Initiation (0-5 minutes)**
```markdown
☐ Open main transfer valve slowly
☐ Monitor pressure rise (should be gradual)
☐ Verify flow initiation on flowmeter
☐ Check for leaks at all connections (visual and H₂ detector)
☐ Monitor aircraft fuel tank pressure and temperature
☐ Confirm no abnormal venting or boil-off
☐ Establish stable flow rate (start at 300-500 kg/hour)
```

**Phase 2: Bulk Transfer (5-40 minutes)**
```markdown
☐ Gradually increase flow rate to optimal (700-1000 kg/hour)
☐ Continuous monitoring of:
   - Flow rate (recorded every 5 minutes)
   - Transfer pressure (0.3-1.0 MPa)
   - LH₂ temperature (-253°C ±2°C)
   - H₂ gas detectors (must remain <10% LEL)
   - Aircraft tank level indication
   - Boil-off venting (should stabilize <2%)
☐ Maintain communication with aircraft crew
☐ Adjust flow rate if pressure or temperature deviate
☐ Watch for ice formation (indicates leak or cooling issue)
☐ Monitor ambient conditions (wind, weather changes)
```

**Phase 3: Top-Off (40-45 minutes)**
```markdown
☐ Reduce flow rate when tank 95% full
☐ Slow fill to 300 kg/hour for final 5%
☐ Monitor tank pressure closely (avoid overpressure)
☐ Coordinate with aircraft crew for target quantity
☐ Confirm target quantity reached
☐ Close main transfer valve slowly
☐ Allow pressure equalization (1-2 minutes)
```

#### 4.5.3 Disconnection Procedure

**Safe Disconnection Steps:**

1. **Verify Transfer Complete**
   - Confirm final fuel quantity with aircraft crew
   - Ensure all valves closed on fueling unit
   - Allow 2 minutes for pressure equalization

2. **Depressurize Connection**
   - Open vent valve to release residual pressure
   - Monitor pressure gauge (must reach <0.1 MPa)
   - Close vent valve

3. **Disconnect Hose**
   - **WARNING**: Hose will be extremely cold (-253°C)
   - Ensure full cryogenic PPE worn
   - Loosen coupling slowly to release any residual pressure
   - Remove coupling carefully (expect some venting)
   - Immediately install dust cap on aircraft receptacle
   - Secure fueling nozzle in storage position on fueling unit

4. **Disconnect Grounding**
   - Remove bonding cable from aircraft
   - Store cable on fueling unit

5. **Remove H₂ Detectors**
   - Verify detectors reading 0% LEL before removal
   - Return detectors to fueling unit

6. **Clear Safety Zone**
   - Remove barriers and cones
   - Perform final visual inspection of fueling area
   - Ensure no ice patches or debris left

### 4.6 Post-Fueling Operations

#### 4.6.1 Post-Fueling Inspection

```markdown
POST-FUELING INSPECTION

☐ Fueling unit external inspection (no new damage or leaks)
☐ Hose and connection inspection (no wear or damage)
☐ Ground area inspection (no spills, ice, or foreign objects)
☐ Aircraft fuel receptacle area inspection (properly sealed)
☐ All safety equipment accounted for and returned
☐ H₂ detectors reading 0% LEL
☐ Safety zone cleared of personnel and equipment

Inspector Signature: _________________ Date/Time: _________________
```

#### 4.6.2 Documentation Requirements

**Fueling Log Entry:**

| Data Field | Entry Required |
|------------|----------------|
| **Date and Time** | Start and end time of fueling |
| **Aircraft Registration** | Aircraft tail number |
| **Aircraft Type** | AMPEL360 BWB H₂ Hy-E |
| **Fueling Location** | Airport and stand/gate |
| **LH₂ Quantity** | Starting quantity, amount transferred, final quantity |
| **Fueling Duration** | Total time from connection to disconnection |
| **Fueling Personnel** | Names and certifications of all operators |
| **Weather Conditions** | Temperature, wind, visibility at start of fueling |
| **Equipment Used** | Fueling unit ID, hose ID |
| **Incidents/Anomalies** | Any deviations, issues, or near-misses |
| **Fuel Quality** | Batch number, purity certificate reference |
| **H₂ Detector Readings** | Max reading during fueling (should be <10% LEL) |

### 4.7 Special Procedures

#### 4.7.1 First Fill Procedure

For aircraft that have been defueled or are new:

1. **Extended Pre-Cool**: Allow 2x normal cooldown time for fuel system
2. **Reduced Flow Rate**: Limit to 300 kg/hour initially
3. **Continuous Monitoring**: Watch for thermal stresses on aircraft fuel system
4. **Graduated Fill**: Fill to 50%, pause 10 minutes, then complete
5. **Extended Inspection**: Full post-fill inspection including aircraft fuel system

#### 4.7.2 Defueling Procedure

When defueling is required:

1. **Safety Zone**: Establish 50-meter safety zone (larger than fueling)
2. **Defuel Equipment**: Use dedicated defueling pump (lower pressure)
3. **Flow Control**: Maximum 500 kg/hour defuel rate
4. **Venting**: Monitor and manage increased boil-off during defueling
5. **Fuel Disposition**: LH₂ transferred to approved storage or safely vented per regulations

#### 4.7.3 Emergency Disconnection

In case of emergency requiring immediate disconnection:

1. **Activate Emergency Shutdown**: Press E-stop button on fueling unit
2. **Close Valves**: Emergency valve closure system engages automatically
3. **Breakaway Coupling**: If time critical, pull breakaway coupling (will self-seal)
4. **Evacuate**: All personnel evacuate to safe distance (minimum 100 meters)
5. **Alert**: Notify fire department and airport emergency services immediately

## 5. Performance Metrics

### 5.1 Fueling Operations KPIs

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| **Average Fueling Time** | 30-45 minutes | Per operation | Fueling Operations Manager |
| **On-Time Fueling Start** | ≥98% | Daily | Dispatch Coordinator |
| **Fueling Accuracy** | ±1% of target quantity | Per operation | Fueling Operator |
| **Zero Spills/Leaks** | 0 incidents | Monthly | Safety Manager |
| **H₂ Detector Alarms** | 0 alarms >10% LEL | Monthly | Safety Manager |
| **Equipment Availability** | ≥99% | Daily | Maintenance Manager |
| **Emergency Shutdown Activations** | 0 (except drills) | Monthly | Operations Manager |
| **Fueling Personnel Certification** | 100% current | Continuous | Training Manager |

### 5.2 Quality Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| **LH₂ Purity** | ≥99.99% | Batch testing + certificates |
| **Temperature Control** | -253°C ±2°C | Continuous monitoring |
| **Pressure Control** | 0.3-1.0 MPa ±0.05 MPa | Continuous monitoring |
| **Documentation Completeness** | 100% | Log audits |

## 6. Training and Certification

### 6.1 Personnel Requirements

| Role | Training Duration | Recurrency | Prerequisites |
|------|-------------------|------------|---------------|
| **LH₂ Fueling Operator** | 40 hours initial + 40 hours OJT | Semi-annual (every 6 months) | GSE operator certification, H₂ safety training |
| **Fueling Supervisor** | 60 hours | Semi-annual | 2 years fueling experience, supervisor training |
| **Safety Observer** | 16 hours | Annual | H₂ safety training, emergency response |

### 6.2 Competency Requirements

Operators must demonstrate:
- Knowledge of H₂ properties and hazards
- Proficiency in fueling procedures
- Ability to respond to emergencies
- Understanding of cryogenic safety
- Effective communication skills

## 7. Cross-References

### 7.1 Related ATA Chapters

- **[ATA 28 — Fuel](../../../../../ATA_28-FUEL/)**: Aircraft fuel system
- **[ATA 85 — Infrastructure](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/)**: H2 infrastructure

### 7.2 Parent and Sibling Documents

- **Parent Document**: [03-00-14_Ops_Std_Sustain](../)
- **Cryogenic Operations**: [03-00-14-02-02A_Cryogenic_Ops_Standards.md](./03-00-14-02-02A_Cryogenic_Ops_Standards.md)
- **H2 Safety**: [03-00-14-02-03A_H2_Safety_Ops_Standards.md](./03-00-14-02-03A_H2_Safety_Ops_Standards.md)
- **Emergency Procedures**: [03-00-14-02-04A_H2_Emergency_Ops_Standards.md](./03-00-14-02-04A_H2_Emergency_Ops_Standards.md)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Hydrogen Operations Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-14-02-01A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use — Safety Critical
- **Owner**: AMPEL360 Hydrogen Ground Operations WG

---
