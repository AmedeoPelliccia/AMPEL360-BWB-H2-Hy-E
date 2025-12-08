# 03-80-08-02A - H2 Energy Safety

## 1. Purpose
This document specifies hydrogen safety requirements for Ground Support Equipment (GSE) energy systems to protect personnel, equipment, and facilities from H2-related hazards.

## 2. Scope
This specification covers:
- H2 hazard identification and risk assessment
- H2 safety standards and codes
- Safety systems (detection, ventilation, suppression)
- Safe work practices and emergency response
- Training and qualification requirements

## 3. Applicable Documents
- NFPA 2 (Hydrogen Technologies Code)
- ISO 19880-1 (Gaseous Hydrogen Fueling Stations - General Requirements)
- SAE AS6968 (Hydrogen Aircraft Refueling Standards)
- ISO 22734-3 (Hydrogen Safety)
- IEC 60079 (Explosive Atmospheres)
- ISO 45001 (Occupational Health and Safety Management)

## 4. Energy System Description

### 4.1 Overview
H2 safety encompasses all measures to prevent and mitigate H2-related incidents including fires, explosions, asphyxiation, and embrittlement, covering design, installation, operation, and maintenance of H2 systems.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| H2 Leak Detection Sensitivity | <1% LEL (400 ppm) | Lower Explosive Limit = 4% by volume |
| Ventilation Rate | Minimum 6 air changes per hour | Enclosed/semi-enclosed spaces |
| Emergency Shutdown Time | <10 seconds | From detection to full isolation |
| Safety Distance (Unprotected) | Per NFPA 2 tables | Depends on H2 quantity and pressure |
| H2 Purity | ≥99.97% | ISO 14687 Type I Grade D |
| Personnel Training | Initial + annual refresher | H2 safety awareness and response |

### 4.3 Performance Requirements

**H2 Hazard Prevention**:
- Minimize leak potential through design and maintenance
- Detect leaks early and respond automatically
- Prevent ignition sources in H2 areas
- Ensure adequate ventilation
- Maintain safe distances and barriers

**Emergency Response**:
- Rapid detection and shutdown
- Safe evacuation procedures
- Fire suppression (cooling, not extinguishing)
- Trained emergency response team

### 4.4 H2 Hazards

#### 4.4.1 Flammability and Explosivity
**Properties**:
- Wide flammability range: 4-75% by volume in air
- Low ignition energy: 0.02 mJ (very easy to ignite)
- Fast flame speed and high flame temperature
- Invisible flame (difficult to see)

**Prevention**:
- Eliminate or control ignition sources (sparks, hot surfaces, static electricity)
- Leak detection and ventilation to prevent accumulation
- Electrical equipment rated for hazardous areas (IEC 60079)
- Bonding and grounding to prevent static discharge

#### 4.4.2 Asphyxiation
**Hazard**: H2 displaces oxygen in enclosed spaces

**Prevention**:
- Adequate ventilation (natural or forced)
- Oxygen deficiency monitors (<19.5% O2 alarm)
- Confined space entry procedures

#### 4.4.3 Embrittlement
**Hazard**: H2 can embrittle certain metals, leading to cracking and failure

**Prevention**:
- Material selection: Use H2-compatible materials (316L stainless steel, aluminum, certain composites)
- Material testing: Per ISO 11114
- Regular inspection of pressure-containing equipment

#### 4.4.4 Physiological Effects
**Low Toxicity**: H2 is non-toxic
**High Pressure Hazards**: Jet release can cause injury, cold burns (Joule-Thomson cooling)

### 4.5 Safety Systems

#### 4.5.1 H2 Leak Detection
**Sensor Types**:
- Catalytic bead sensors
- Electrochemical sensors
- Thermal conductivity sensors

**Placement**:
- High points (H2 rises due to low density)
- Near potential leak sources (valves, connections, equipment)
- Coverage: All enclosed and semi-enclosed areas

**Response**:
- Alarm at 10-25% LEL (visual and audible)
- Automatic shutdown at 25-40% LEL
- Integration with emergency shutdown system (ESD)

#### 4.5.2 Ventilation
**Natural Ventilation** (preferred):
- High-level openings for H2 escape
- Low-level openings for air intake
- Minimum 1% of enclosure area

**Forced Ventilation** (if natural inadequate):
- Continuous or activated by H2 detection
- Air change rate: Minimum 6 air changes per hour
- Exhaust fan: Rated for hazardous area, spark-proof

#### 4.5.3 Fire Suppression
**H2 Fires**:
- Allow to burn in controlled manner if safe to do so
- Do NOT attempt to extinguish (risk of explosion if H2 accumulates)
- Use water for cooling adjacent equipment and structures
- Shut off H2 supply if possible

**Fire Detection**:
- Flame detectors (UV/IR)
- Heat detectors
- Early warning for emergency response

#### 4.5.4 Emergency Shutdown System (ESD)
**Activation**:
- Automatic: High H2 concentration, fire detection, high pressure
- Manual: Emergency stop buttons at strategic locations

**Actions**:
- Close isolation valves to stop H2 flow
- Shut down compressors and other equipment
- Activate ventilation (if forced)
- Alarm and notification

### 4.6 Hazardous Area Classification

**Purpose**: Define zones where explosive atmospheres may exist, determine equipment requirements

**Classification** (per IEC 60079):
- **Zone 0**: Explosive atmosphere present continuously or for long periods
- **Zone 1**: Explosive atmosphere likely to occur in normal operation occasionally
- **Zone 2**: Explosive atmosphere not likely to occur in normal operation, or if it does, only briefly

**Equipment Requirements**:
- Electrical equipment: Explosion-proof (Ex d), intrinsically safe (Ex i), or other certified types
- Lighting, motors, switches, sensors: Rated for applicable zone
- Marking: Equipment labeled with Ex marking and zone suitability

### 4.7 Safe Work Practices

**Permit to Work**:
- Required for work on H2 systems
- Review hazards, mitigation measures, PPE, emergency procedures
- Authorized by competent person

**Hot Work**:
- Strictly controlled near H2 systems
- Purge and inert H2 systems before hot work
- Gas test to confirm no H2 present
- Fire watch during and after hot work

**Lockout/Tagout**:
- Isolate H2 supply before maintenance
- Depressurize and purge H2 from equipment
- Lock and tag isolation valves
- Test to confirm isolation

**Personal Protective Equipment**:
- Flame-resistant clothing
- Safety glasses or face shield
- Hearing protection (high-pressure releases are loud)
- Cryogenic gloves and apron (if handling liquid H2)

### 4.8 Emergency Response

**Emergency Procedures**:
- Evacuation routes and assembly points
- Emergency shutdown procedures
- Communication and notification (emergency services, management)
- Fire and H2 leak response procedures

**Training and Drills**:
- All personnel trained on emergency procedures
- Regular emergency drills (at least annually)
- Coordination with local fire department

**Fire Response**:
- Evacuate and call emergency services
- Activate ESD if safe to do so
- Do NOT attempt to extinguish H2 fire (let it burn safely)
- Cool adjacent structures with water

**Leak Response**:
- Evacuate immediate area
- Activate ESD if safe to do so
- Eliminate ignition sources
- Ventilate area
- Monitor H2 concentration
- Investigate and repair leak after H2 dissipated

### 4.9 Training and Qualification

**H2 Safety Awareness** (all personnel):
- H2 properties and hazards
- Safety systems and alarms
- Emergency procedures
- Frequency: Initial + annual refresher

**H2 Operations Training** (operators and technicians):
- H2 system operation and maintenance
- Safe work practices
- Permit to work procedures
- Emergency response
- Frequency: Initial + annual refresher + requalification for new equipment

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| H2 Safety | NFPA 2, ISO 19880-1, SAE AS6968 | Design, operation, maintenance |
| Electrical Equipment (Hazardous Areas) | IEC 60079, NFPA 70 Article 500 | Equipment selection and installation |
| Pressure Equipment | ASME BPVC Section VIII, ISO 11119 | Design, testing, inspection |
| Fire Protection | NFPA 2, ISO 22734-3 | Detection, suppression, emergency response |
| Occupational Safety | ISO 45001 | Safety management system |
| Materials Compatibility | ISO 11114 | Material selection and testing |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- H2 Infrastructure: 03-80-02-01A_H2_Energy_Infrastructure
- H2 Production: 03-80-02-02A_Green_H2_Production
- H2 Distribution: 03-80-02-03A_H2_Distribution_Systems
- Electrical Safety: 03-80-08-01A_Electrical_Safety
- Energy Regulations: 03-80-08-03A_Energy_Regulations

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 GSE Energy WG | Initial release |

---

## Document Control

- **Status**: DRAFT – Subject to review and approval
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Energy Working Group
- **Next Review**: 2026-03-08
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-08

---
