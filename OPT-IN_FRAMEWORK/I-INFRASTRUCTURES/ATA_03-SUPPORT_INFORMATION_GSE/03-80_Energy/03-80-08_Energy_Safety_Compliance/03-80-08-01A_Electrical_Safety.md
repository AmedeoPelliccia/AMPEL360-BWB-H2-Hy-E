# 03-80-08-01A - Electrical Safety

## 1. Purpose
This document specifies electrical safety requirements for Ground Support Equipment (GSE) energy systems to protect personnel, equipment, and facilities from electrical hazards.

## 2. Scope
This specification covers:
- Electrical hazard identification and risk assessment
- Electrical safety standards and codes
- Protection systems and devices
- Safe work practices
- Training and qualification requirements

## 3. Applicable Documents
- NFPA 70 (National Electrical Code)
- NFPA 70E (Electrical Safety in the Workplace)
- IEC 60364 (Low-Voltage Electrical Installations)
- IEC 61140 (Protection Against Electric Shock)
- IEEE 1584 (Arc Flash Hazard Calculation)
- ISO 45001 (Occupational Health and Safety Management)

## 4. Energy System Description

### 4.1 Overview
Electrical safety encompasses all measures to prevent electrical injuries, equipment damage, and fires in GSE energy operations, including design, installation, operation, and maintenance activities.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Maximum Touch Voltage | 50V AC, 120V DC | Safe limits for personnel |
| Ground Fault Protection | ≤30 mA (personnel), ≤300 mA (equipment) | RCD trip current |
| Arc Flash PPE Category | Determined by incident energy (cal/cm²) | Per NFPA 70E |
| Electrical Safety Training | Annual refresher | For qualified workers |
| Insulation Resistance | >1 MΩ minimum | System integrity |

### 4.3 Performance Requirements

**Electrical Hazard Prevention**:
- Eliminate or minimize electrical shock hazards
- Prevent arc flash incidents
- Protect against electrical fires
- Ensure proper grounding and bonding

**Safety Compliance**:
- Meet or exceed applicable electrical codes and standards
- Regular inspections and testing
- Documented safety procedures

### 4.4 Electrical Hazards

#### 4.4.1 Electric Shock
**Causes**:
- Contact with energized conductors
- Insulation failure
- Improper grounding
- Faults in equipment

**Prevention**:
- Proper insulation and guarding
- Ground Fault Circuit Interrupters (GFCI) / Residual Current Devices (RCD)
- Lockout/Tagout (LOTO) procedures
- Personal Protective Equipment (PPE)

#### 4.4.2 Arc Flash
**Causes**:
- Short circuits
- Equipment failure
- Improper operation

**Severity**: Can cause severe burns, hearing loss, vision damage, blast injuries

**Prevention**:
- Arc flash hazard analysis per IEEE 1584
- Arc-resistant switchgear for high-energy equipment
- Arc flash labels indicating hazard level and required PPE
- Safe work procedures and proper PPE

#### 4.4.3 Electrical Fires
**Causes**:
- Overcurrent (short circuit, overload)
- Poor connections (arcing, overheating)
- Insulation failure

**Prevention**:
- Proper overcurrent protection (fuses, circuit breakers)
- Regular thermal imaging inspections
- Proper cable sizing and installation
- Fire detection and suppression systems

### 4.5 Protection Systems

#### 4.5.1 Grounding and Bonding
- **System Grounding**: Connect neutral or one phase to earth
- **Equipment Grounding**: Connect exposed conductive parts to ground
- **Bonding**: Ensure electrical continuity between conductive parts
- **Ground Resistance**: <5 Ω (preferred <1 Ω for sensitive equipment)

#### 4.5.2 Overcurrent Protection
- **Fuses and Circuit Breakers**: Interrupt excessive current
- **Selective Coordination**: Upstream devices slower than downstream
- **Overload Protection**: Thermal or electronic overload relays for motors

#### 4.5.3 Ground Fault Protection
- **RCD/GFCI**: Detect ground fault current and interrupt supply
- **Sensitivity**: 30 mA for personnel protection, 300 mA for equipment
- **Type A or Type B**: For DC and variable frequency applications

#### 4.5.4 Arc Flash Protection
- **Arc-Resistant Switchgear**: Redirect arc energy away from personnel
- **Arc Flash Relays**: Detect arc flash and trip breaker rapidly (<100 ms)
- **Current Limiting Devices**: Reduce peak fault current and incident energy

### 4.6 Safe Work Practices

#### 4.6.1 Lockout/Tagout (LOTO)
- **Purpose**: Ensure energy sources are isolated before work
- **Procedure**: Lock and tag disconnecting means in "off" position
- **Verification**: Test to confirm de-energization
- **Multi-Lock**: Multiple workers use individual locks

#### 4.6.2 Working on Energized Equipment
- **Justification**: Only when de-energization is infeasible and approved
- **Risk Assessment**: Identify hazards, determine PPE category
- **Qualified Workers**: Trained and authorized personnel only
- **PPE**: Arc-rated clothing, face shield, insulated gloves, etc.
- **Barriers**: Use insulating barriers and mats

#### 4.6.3 Personal Protective Equipment (PPE)
- **Arc Flash PPE**: Arc-rated clothing, face shield, hard hat, safety glasses
- **Electrical Gloves**: Insulated rubber gloves with leather protectors
- **Footwear**: Dielectric boots or overshoes (if required)
- **PPE Category**: Determined by arc flash hazard analysis (NFPA 70E)

### 4.7 Training and Qualification

**Qualified Electrical Worker**:
- Training on electrical hazards and safety procedures
- Demonstrated skills and knowledge
- Authorization to work on electrical systems
- Annual refresher training

**Training Topics**:
- Electrical hazards (shock, arc flash, fire)
- Safe work practices (LOTO, testing, PPE)
- Emergency response (first aid, CPR, electrical shock treatment)
- Applicable standards (NFPA 70E, local codes)

### 4.8 Inspection and Testing

**Regular Inspections**:
- Visual inspection of equipment for damage, wear, overheating
- Thermal imaging to detect hot spots
- Frequency: Monthly for critical equipment, annually for general equipment

**Electrical Testing**:
- Insulation resistance testing (Megger test)
- Ground resistance testing
- RCD/GFCI testing (trip time, sensitivity)
- Protective relay testing
- Frequency: Annually or per manufacturer recommendations

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Electrical Installation | NFPA 70, IEC 60364 | Design, installation per codes |
| Electrical Safety in Workplace | NFPA 70E, IEC 61140 | Safe work practices, PPE |
| Arc Flash Analysis | IEEE 1584 | Hazard calculation, labeling |
| Occupational Safety | ISO 45001, OSHA | Safety management system |
| Equipment Testing | IEC 61557, IEC 60364-6 | Periodic testing and inspection |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Grid Power Supply: 03-80-03-01A_Grid_Power_Supply
- Power Distribution: 03-80-03-03A_Power_Distribution
- Battery Safety: 03-80-05_Battery_Energy_Systems
- H2 Safety: 03-80-08-02A_H2_Energy_Safety

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
