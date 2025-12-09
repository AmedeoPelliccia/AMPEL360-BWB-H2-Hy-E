---
Title: "GSE Operations Procedures"
Identifier: "AMPEL360-03-00-14-01-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Ground Support Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES GSE Operations Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Standard operating procedures for Ground Support Equipment operations."
Keywords: ["ATA 03","GSE","Operations","Procedures","Ground Support","Standards"]
Compliance:
  - "ATA iSpec 2200"
  - "IATA Airport Handling Manual (AHM)"
  - "IATA Ground Operations Manual (IGOM)"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../../"
  Siblings:
    - "./03-00-14-01-02A_GSE_Ops_Safety_Standards.md"
    - "./03-00-14-01-03A_GSE_Ops_Performance_Std.md"
    - "./03-00-14-01-04A_GSE_Ops_Quality_Standards.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-00-14-01-01A — GSE Operations Procedures

## 1. Purpose

This document establishes **standard operating procedures (SOPs)** for Ground Support Equipment (GSE) operations supporting the AMPEL360 BWB H₂ Hy-E aircraft. It defines operational workflows, safety protocols, and procedural requirements to ensure safe, efficient, and compliant GSE operations across all ground handling scenarios.

## 2. Scope

### 2.1 Coverage

This document covers operational procedures for:

1. **Pre-Operations Planning**
   - Equipment selection and preparation
   - Safety briefings and crew qualifications
   - Weather and environmental condition assessment
   - Coordination with aircraft operations

2. **Standard GSE Operations**
   - Ground power unit connections
   - Aircraft towing and pushback
   - Maintenance platform positioning
   - Environmental control service operations
   - Cargo and passenger loading equipment

3. **Hydrogen-Specific Operations**
   - LH₂ fueling operations (detailed in [03-00-14-02](../03-00-14-02_H2_GSE_Operations_Standards/))
   - Cryogenic equipment handling
   - Hydrogen safety zone establishment

4. **Post-Operations**
   - Equipment disconnection and securing
   - Inspection and reporting
   - Equipment return and storage

### 2.2 Out of Scope

- Aircraft-specific maintenance procedures (covered under [ATA 03-30_ANCHORS](../../../03-30_ANCHORS/))
- Airport infrastructure operations (covered under [ATA 85](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/))
- Emergency response procedures (addressed in safety standards)

## 3. Applicable Documents

### 3.1 External Standards

| Standard | Title | Application |
|----------|-------|-------------|
| **[IATA AHM](https://www.iata.org/en/publications/manuals/airport-handling-manual/)** | Airport Handling Manual | Ground handling procedures |
| **[IATA IGOM](https://www.iata.org/en/publications/manuals/ground-operations-manual/)** | Ground Operations Manual | GSE operational standards |
| **[ATA iSpec 2200](https://www.ata.org/resources/specifications)** | Information Standards for Aviation Maintenance | Technical publication standards |
| **[ISO 9001](https://www.iso.org/standard/62085.html)** | Quality Management Systems | Quality procedures |
| **[SAE ARP4761](https://www.sae.org/standards/content/arp4761/)** | Safety Assessment Process | Safety procedure development |

### 3.2 Internal References

- [03-00-01_Overview](../../03-00-01_Overview/) — ATA 03 overview
- [03-00-02_Safety](../../03-00-02_Safety/) — GSE safety assessments
- [03-00-05_Interfaces](../../03-00-05_Interfaces/) — Aircraft-GSE interfaces
- [03-00-12_Services](../../03-00-12_Services/) — GSE service specifications
- [03-10_Operations](../../../03-10_Operations/) — Operational guidelines

## 4. Operations/Sustainment Requirements

### 4.1 Overview

GSE operations must adhere to structured procedures ensuring:

- **Safety**: Zero tolerance for safety deviations
- **Efficiency**: Minimized turnaround times
- **Quality**: Consistent service delivery
- **Compliance**: Adherence to regulatory and company standards
- **Traceability**: Complete documentation of all operations

### 4.2 Pre-Operations Requirements

#### 4.2.1 Equipment Selection Criteria

| Criteria | Requirement | Verification Method |
|----------|-------------|---------------------|
| **Certification** | Valid equipment certification | Documentation review |
| **Inspection** | Pre-operation inspection completed | Inspection log |
| **Compatibility** | Confirmed compatible with aircraft | Interface checklist |
| **Availability** | Equipment ready and available | Status check |
| **Personnel** | Qualified operators assigned | Training records |

#### 4.2.2 Pre-Operations Checklist

```markdown
☐ Equipment inspection completed (daily/pre-use)
☐ Fluid levels checked (hydraulic, fuel, coolant as applicable)
☐ Safety devices tested (emergency stops, alarms)
☐ Communication systems operational
☐ Weather conditions assessed and acceptable
☐ Safety briefing conducted with all personnel
☐ Aircraft status confirmed (ready for GSE operations)
☐ Ground clearances obtained
☐ Safety zones established and marked
```

### 4.3 Standard Operating Procedures

#### 4.3.1 Ground Power Unit (GPU) Operations

**Procedure:**

1. **Preparation**
   - Position GPU within specified distance (typically 3-5 meters from aircraft)
   - Verify voltage/frequency compatibility (115V/400Hz for AMPEL360)
   - Ensure proper grounding connections

2. **Connection**
   - Establish communication with aircraft systems
   - Connect ground cables following sequence:
     - Ground connection first
     - Power connection second
   - Verify connection integrity

3. **Power-Up**
   - Start GPU and allow stabilization period (30 seconds minimum)
   - Monitor voltage, frequency, and current parameters
   - Confirm aircraft systems receiving power

4. **Monitoring**
   - Continuous monitoring during operation
   - Log any anomalies or deviations
   - Maintain communication with aircraft crew

5. **Disconnection**
   - Coordinate with aircraft crew before disconnection
   - Shutdown sequence (reverse of connection)
   - Remove cables and secure equipment

#### 4.3.2 Aircraft Towing Operations

**Procedure:**

1. **Pre-Tow Checks**
   ```markdown
   ☐ Aircraft brakes released
   ☐ Landing gear pins installed (if required)
   ☐ Towbar compatible and in good condition
   ☐ Tow vehicle inspected and operational
   ☐ Communication established with aircraft and ground control
   ☐ Tow path clear and approved
   ```

2. **Towbar Connection**
   - Align tow vehicle with nose gear
   - Connect towbar per manufacturer specifications
   - Verify secure connection (visual and mechanical check)
   - Install safety pins

3. **Towing Operation**
   - Maximum speed: 5 km/h (3 mph) or per airport regulations
   - Maintain constant communication
   - Use wing walkers for clearance monitoring
   - Follow designated taxiway/tow paths only

4. **Parking and Disconnection**
   - Position aircraft precisely at designated spot
   - Engage aircraft brakes (coordinate with crew)
   - Disconnect towbar
   - Install wheel chocks
   - Complete tow log

#### 4.3.3 Maintenance Platform Operations

**Procedure:**

1. **Platform Setup**
   - Select appropriate platform height for BWB configuration
   - Position on stable, level ground
   - Deploy outriggers and verify stability
   - Establish safety perimeter

2. **Access Operations**
   - Verify platform load limits
   - Ensure personnel wearing fall protection (if required)
   - Maintain 3-point contact during access
   - Secure tools and equipment

3. **Platform Monitoring**
   - Periodic stability checks
   - Weather monitoring (wind speed limits: 40 km/h / 25 mph)
   - Communication with ground personnel

4. **Platform Removal**
   - Clear all personnel and equipment
   - Retract platform in controlled manner
   - Store in designated area

### 4.4 Hydrogen-Specific Procedure References

For LH₂ fueling and hydrogen-related GSE operations, refer to:

- [03-00-14-02-01A_LH2_Fueling_Ops_Standards.md](../03-00-14-02_H2_GSE_Operations_Standards/03-00-14-02-01A_LH2_Fueling_Ops_Standards.md)
- [03-00-14-02-03A_H2_Safety_Ops_Standards.md](../03-00-14-02_H2_GSE_Operations_Standards/03-00-14-02-03A_H2_Safety_Ops_Standards.md)
- [03-00-14-02-04A_H2_Emergency_Ops_Standards.md](../03-00-14-02_H2_GSE_Operations_Standards/03-00-14-02-04A_H2_Emergency_Ops_Standards.md)

### 4.5 Post-Operations Requirements

#### 4.5.1 Equipment Shutdown and Securing

| Action | Requirement | Documentation |
|--------|-------------|---------------|
| **Disconnection** | All connections removed per procedure | Operation log |
| **Inspection** | Post-operation inspection completed | Inspection checklist |
| **Defects** | Any defects reported immediately | Defect report |
| **Cleaning** | Equipment cleaned per schedule | Cleaning log |
| **Storage** | Equipment stored in designated area | Storage log |
| **Fueling** | Equipment refueled if below 25% (if applicable) | Fuel log |

#### 4.5.2 Documentation Requirements

All GSE operations must be documented with:

- **Operation Log**: Date, time, aircraft, equipment used, personnel
- **Inspection Records**: Pre- and post-operation inspections
- **Defect Reports**: Any anomalies or equipment issues
- **Incident Reports**: Any safety incidents or near-misses
- **Performance Data**: Turnaround times, fuel consumption (if applicable)

## 5. Performance Metrics

### 5.1 Operational KPIs

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| **On-Time Equipment Availability** | ≥99% | Daily | GSE Operations Manager |
| **Procedure Compliance Rate** | 100% | Per operation | Ground Service Supervisor |
| **Average Turnaround Time** | ≤45 minutes | Per aircraft turnaround | Operations Coordinator |
| **Equipment Utilization Rate** | 70-85% | Weekly | Fleet Manager |
| **Pre-Operation Inspection Completion** | 100% | Per operation | Equipment Operator |
| **Incident Rate** | 0 incidents/1000 operations | Monthly | Safety Manager |

### 5.2 Quality Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| **Procedure Adherence** | 100% | Audit observations |
| **Documentation Completeness** | 100% | Record review |
| **Personnel Qualification** | 100% certified | Training records |
| **Equipment Condition** | ≥95% serviceable | Inspection reports |

## 6. Training and Qualification

### 6.1 Personnel Requirements

| Role | Training Required | Recurrency |
|------|-------------------|------------|
| **GSE Operator** | Equipment-specific certification | Annual |
| **Ground Service Supervisor** | Supervisor training + equipment familiarization | Annual |
| **Safety Observer** | Safety procedures training | Annual |
| **Maintenance Technician** | Equipment maintenance training | Bi-annual |

### 6.2 Competency Assessment

Personnel must demonstrate:

- Knowledge of procedures
- Proficiency in equipment operation
- Understanding of safety protocols
- Ability to respond to abnormal situations
- Effective communication skills

## 7. Cross-References

### 7.1 Related ATA Chapters

- **[ATA 02 — Operations Information](../../../../ATA_02-OPERATIONS_INFORMATION/)**: Flight operations coordination
- **[ATA 03-10 — Operations](../../../03-10_Operations/)**: GSE operational guidelines
- **[ATA 03-30 — Anchors](../../../03-30_ANCHORS/)**: Maintenance procedures
- **[ATA 85 — Infrastructure Interface Standards](../../../../../ATA_85-INFRASTRUCTURE_INTERFACE_STANDARDS/)**: Airport interface requirements

### 7.2 Parent and Sibling Documents

- **Parent Document**: [03-00-14_Ops_Std_Sustain](../)
- **Related GSE Services**: [03-00-12_Services](../../03-00-12_Services/)
- **Safety Standards**: [03-00-14-01-02A_GSE_Ops_Safety_Standards.md](./03-00-14-01-02A_GSE_Ops_Safety_Standards.md)
- **Performance Standards**: [03-00-14-01-03A_GSE_Ops_Performance_Std.md](./03-00-14-01-03A_GSE_Ops_Performance_Std.md)
- **Quality Standards**: [03-00-14-01-04A_GSE_Ops_Quality_Standards.md](./03-00-14-01-04A_GSE_Ops_Quality_Standards.md)

## 8. Continuous Improvement

### 8.1 Procedure Review

Procedures are reviewed:

- **Annually**: Scheduled review of all procedures
- **Post-Incident**: After any safety incident or near-miss
- **Technology Change**: When new equipment or technology is introduced
- **Regulatory Update**: When regulations or standards change

### 8.2 Feedback Mechanisms

- **Operator Feedback**: Regular input from GSE operators
- **Safety Observations**: Safety committee review
- **Performance Data**: Analysis of operational metrics
- **Audit Findings**: Internal and external audit recommendations

For continuous improvement program details, see [03-00-14-07_GSE_Continuous_Improvement](../03-00-14-07_GSE_Continuous_Improvement/).

## 9. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Ground Support Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-14-01-01A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 Ground Support Operations WG

---
