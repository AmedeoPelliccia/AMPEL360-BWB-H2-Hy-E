# 85-10-00-004: Operational Roles and Responsibilities

## Document Information

- **Document ID**: 85-10-00-004  
- **Title**: Operational Roles and Responsibilities  
- **Version**: 1.0  
- **Status**: DRAFT  
- **Date**: 2025-11-21  

---

## 1. Purpose

This document defines the **roles and responsibilities (R&R)** for all stakeholders involved in the operation and management of **ATA 85 Infrastructure Interface Standards** for the AMPEL360 BWB aircraft.

It establishes:
- **Clear accountability** for interface operations
- **Coordination mechanisms** between stakeholders
- **Escalation paths** for operational issues
- **Training and competency requirements** for each role

---

## 2. Scope

### 2.1 In Scope

- Roles for **aircraft operators** (flight crew, cabin crew, ground crew)
- Roles for **airport and infrastructure providers**
- Roles for **H₂ and CO₂ service providers**
- Roles for **airline operations center (AOC)** and dispatch
- Roles for **maintenance, engineering, and digital twin teams**
- Coordination and communication protocols between roles

### 2.2 Out of Scope

- Detailed job descriptions (handled by HR and airline policies)
- Technical system design roles (covered in `85-00-04_Design`)
- Certification authority roles (covered in `85-00-10_Certification`)

---

## 3. Stakeholder Overview

### 3.1 Primary Stakeholders

| **Stakeholder Category** | **Organization Type** | **Key Interfaces** |
|-------------------------|----------------------|-------------------|
| **Aircraft Operators** | Airline | All ATA 85 interfaces |
| **Ground Handlers** | Airline/3rd Party | GSE, turnaround coordination |
| **Airport Authority** | Airport | Gate/stand, power, data |
| **H₂ Service Provider** | Energy Company/Airport | H₂ refuelling |
| **CO₂ Service Provider** | Industrial Partner | CO₂ buffer logistics |
| **Airline Operations Center (AOC)** | Airline | Real-time monitoring, dispatch |
| **Maintenance Organization** | Airline/MRO | Interface health, troubleshooting |
| **Digital Twin Team** | Airline/OEM | Predictive analytics, optimization |

---

## 4. Role Definitions

### 4.1 Flight Crew

**Primary Responsibility**: Safe operation of aircraft, including verification of infrastructure interface readiness.

#### 4.1.1 Captain

**Responsibilities**:
- **Pre-flight**: Verify all ATA 85 interface disconnections completed before departure
- **In-flight**: Monitor interface health alerts forwarded to flight deck
- **Post-flight**: Report any interface anomalies to maintenance and operations
- **Authority**: Final decision on accepting or rejecting aircraft for dispatch based on interface status

**Training Requirements**:
- Initial: ATA 85 interface overview, emergency procedures
- Recurrent: Annual refresher on interface safety and contingency procedures

**Cross-Reference**: `85-10-08_Training_and_Simulation_Interfaces/`

#### 4.1.2 First Officer

**Responsibilities**:
- Assist Captain in interface verification procedures
- Monitor EFB (Electronic Flight Bag) for interface status during turnaround
- Coordinate with ground crew via intercom/datalink

**Training Requirements**: Same as Captain

---

### 4.2 Cabin Crew

**Primary Responsibility**: Passenger safety and coordination of passenger interface operations.

#### 4.2.1 Purser / Cabin Manager

**Responsibilities**:
- **Boarding**: Coordinate passenger flow with gate agent and boarding bridge status
- **Safety**: Verify evacuation routes and emergency exits compatible with gate configuration
- **Communication**: Liaise with flight crew and ground operations on passenger-related interface status

**Training Requirements**:
- Initial: BWB layout, passenger flow, evacuation procedures with gate/stand variations
- Recurrent: Annual safety drills including gate-dependent evacuation scenarios

**Cross-Reference**: `85-10-05_Passenger_Flow_and_Evac_Operations/`

---

### 4.3 Ground Operations

**Primary Responsibility**: Turnaround execution and coordination of all ground interface activities.

#### 4.3.1 Turnaround Coordinator

**Responsibilities**:
- **Planning**: Create turnaround plan based on gate/stand capabilities and interface availability
- **Execution**: Coordinate sequence and timing of all ATA 85 interface connections/disconnections
- **Monitoring**: Track turnaround progress via dashboard, escalate delays
- **Communication**: Central point of contact for all ground operations stakeholders
- **Documentation**: Record turnaround events, interface performance, anomalies

**Authority**: Direct ground crew and GSE operators during turnaround

**Training Requirements**:
- Initial: ATA 85 interface overview, turnaround procedures, dashboard operation
- Recurrent: Quarterly updates on procedures and system changes

**Cross-Reference**: 
- `85-10-01_Turnaround_Interface_Management/`
- [ATA 02-20-14 Ground Operations](../../ATA_02-OPERATIONS_INFORMATION/)

#### 4.3.2 Ground Crew / Ramp Agent

**Responsibilities**:
- Physical connection/disconnection of gate/stand interfaces (power, data, GSE)
- Visual inspection of interface hardware
- Safety verification (chocks, cones, grounding)
- Report status to Turnaround Coordinator

**Training Requirements**:
- Initial: BWB-specific GSE positioning, interface connection procedures, safety protocols
- Recurrent: Annual refresher, competency check

**Cross-Reference**: `85-10-04_Airport_Gate_and_Stand_Operations/`

---

### 4.4 H₂ Service Provider

**Primary Responsibility**: Safe and efficient H₂ refuelling operations.

#### 4.4.1 H₂ Refuelling Operator

**Responsibilities**:
- **Pre-refuel**: Perform safety checks (grounding, leak detection, pressure verification)
- **Refuelling**: Execute refuelling sequence per `85-10-02_H2_Ground_Operations/` procedures
- **Monitoring**: Continuously monitor refuelling parameters (flow, pressure, temperature)
- **Safety**: Immediately abort operation if safety thresholds exceeded
- **Documentation**: Record refuel quantities, times, anomalies

**Authority**: Stop refuelling operation at any time for safety reasons

**Certification**: 
- H₂ handling certification (e.g., ISO/IEC 17024 equivalent)
- Aircraft-specific H₂ interface training

**Training Requirements**:
- Initial: H₂ safety, AMPEL360 BWB H₂ system, interface procedures, emergency response
- Recurrent: Semi-annual refresher, annual competency check

**Cross-Reference**: 
- `85-10-02_H2_Ground_Operations/85-10-02-001_H2_Refuelling_Operations_Overview.md`
- `85-10-07_Operational_Contingencies_and_Degraded_Modes/`

#### 4.4.2 H₂ Service Supervisor

**Responsibilities**:
- Oversee multiple refuelling operations
- Coordinate with airport authority on H₂ infrastructure availability
- Investigate and resolve H₂ interface anomalies
- Liaise with airline operations on scheduling and availability

**Training Requirements**: Same as H₂ Refuelling Operator plus supervisory training

---

### 4.5 CO₂ Service Provider

**Primary Responsibility**: CO₂ battery buffer exchange and closed-loop logistics.

#### 4.5.1 CO₂ Buffer Technician

**Responsibilities**:
- **Assessment**: Check CO₂ buffer status via aircraft interface
- **Exchange**: Remove depleted buffer, install charged buffer per procedure
- **Verification**: Confirm buffer integration and system health
- **Logistics**: Update buffer tracking system (location, status, carbon credits)

**Certification**: CO₂ handling, pressure vessel safety

**Training Requirements**:
- Initial: CO₂ system overview, buffer exchange procedures, safety protocols
- Recurrent: Annual refresher

**Cross-Reference**: `85-10-03_CO2_Battery_Ground_Operations/85-10-03-002_CO2_Buffer_Exchange_and_Recharge_Procedures.md`

#### 4.5.2 CO₂ Logistics Coordinator

**Responsibilities**:
- Plan buffer exchange schedules based on aircraft utilization
- Coordinate buffer recharge at centralized facilities
- Track buffer lifecycle and carbon credit allocation
- Interface with [ATA 99 – Circularity & Carbon](../ATA_99-CIRCULARITY_CARBON/) system

**Training Requirements**:
- Initial: CO₂ closed-loop logistics, system training
- Recurrent: Annual

---

### 4.6 Airport Authority

**Primary Responsibility**: Provide and maintain airport infrastructure interfaces.

#### 4.6.1 Gate/Stand Manager

**Responsibilities**:
- Allocate gates/stands compatible with BWB geometry and interface requirements
- Ensure availability of power, data, and GSE connections
- Coordinate maintenance of airport-side interface equipment
- Provide performance data to airline operations

**Training Requirements**:
- Initial: BWB interface requirements, stand compatibility rules
- Recurrent: As needed for new equipment or procedures

**Cross-Reference**: `85-10-04_Airport_Gate_and_Stand_Operations/85-10-04-003_Stand_Compatibility_and_Allocation_Rules.md`

#### 4.6.2 Airport Operations Center (APOC)

**Responsibilities**:
- Monitor real-time status of all infrastructure interfaces
- Coordinate with AOC on gate/stand availability and issues
- Dispatch maintenance for airport-side interface faults
- Provide situational awareness during contingencies

**Training Requirements**:
- Initial: ATA 85 interface overview, monitoring dashboard
- Recurrent: Annual

---

### 4.7 Airline Operations Center (AOC)

**Primary Responsibility**: Real-time monitoring, decision support, and dispatch coordination.

#### 4.7.1 Flight Dispatcher

**Responsibilities**:
- Monitor interface status for all flights in operation
- Coordinate with ground operations on turnaround issues
- Make dispatch decisions based on interface readiness
- Coordinate contingency planning (e.g., alternate H₂ sources, route changes)

**Authority**: 
- Delay or cancel flights if interface issues impact safety or regulatory compliance
- Co-authority with Captain on dispatch decisions

**Training Requirements**:
- Initial: ATA 85 interface overview, dispatch procedures, contingency planning
- Recurrent: Annual, plus updates when procedures change

**Cross-Reference**: 
- `85-10-06_Real_Time_Monitoring_and_Alerts/`
- `85-10-07_Operational_Contingencies_and_Degraded_Modes/`

#### 4.7.2 Operations Controller

**Responsibilities**:
- Oversee network-wide operations, including infrastructure interface performance
- Coordinate with airport authorities and service providers on systemic issues
- Drive continuous improvement initiatives based on operational data

**Training Requirements**:
- Initial: ATA 85 operations overview, cross-ATA integration
- Recurrent: Quarterly

---

### 4.8 Maintenance Organization

**Primary Responsibility**: Interface health monitoring, troubleshooting, and corrective maintenance.

#### 4.8.1 Line Maintenance Technician

**Responsibilities**:
- Respond to interface faults reported during turnaround
- Perform troubleshooting using diagnostics and digital twin insights
- Execute corrective actions (reset, recalibration, component swap)
- Document maintenance actions in CMMS (Computerized Maintenance Management System)

**Certification**: Licensed aircraft maintenance technician (AMT/EASA Part-66)

**Training Requirements**:
- Initial: ATA 85 interface systems, troubleshooting procedures, digital twin interface
- Recurrent: Annual, plus updates for system changes

**Cross-Reference**: 
- ATA 01/03 (Maintenance policies and procedures)
- [ATA 95 – Digital Product Passport & Neural Networks](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)

#### 4.8.2 Maintenance Control Center (MCC)

**Responsibilities**:
- Monitor interface health across fleet via digital twin dashboards
- Coordinate maintenance resources for interface faults
- Escalate recurring issues to engineering
- Track interface performance metrics and reliability

**Training Requirements**:
- Initial: ATA 85 overview, digital twin monitoring, dispatch coordination
- Recurrent: Annual

---

### 4.9 Engineering and Digital Twin Team

**Primary Responsibility**: Interface performance analysis, predictive maintenance, and continuous improvement.

#### 4.9.1 Interface Systems Engineer

**Responsibilities**:
- Analyze interface performance data from digital twin
- Investigate recurring or novel interface faults
- Develop and validate interface improvements and modifications
- Support certification of interface changes

**Training Requirements**:
- Initial: ATA 85 design and operations, digital twin analytics
- Recurrent: As needed for new technologies

**Cross-Reference**: 
- `85-00-04_Design/`
- `85-00-06_Engineering/`

#### 4.9.2 Digital Twin Analyst

**Responsibilities**:
- Configure digital twin models for ATA 85 interfaces
- Develop and tune predictive maintenance algorithms
- Generate reports on interface health trends and anomalies
- Provide predictive alerts to AOC and maintenance

**Training Requirements**:
- Initial: Digital twin platform, ATA 85 interface data schemas, ML/analytics techniques
- Recurrent: Quarterly, plus ongoing skill development

**Cross-Reference**: 
- `85-10-06_Real_Time_Monitoring_and_Alerts/85-10-06-001_Real_Time_Interface_Monitoring_Concept.md`
- [ATA 95 – Digital Product Passport & Neural Networks](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/)

---

## 5. Responsibility Assignment Matrix (RACI)

### 5.1 RACI Legend

- **R** = Responsible (performs the work)
- **A** = Accountable (final approval/authority)
- **C** = Consulted (input sought)
- **I** = Informed (kept updated)

### 5.2 Interface Operations RACI Matrix

| **Activity** | **Captain** | **Turnaround Coord** | **Ground Crew** | **H₂ Operator** | **CO₂ Tech** | **AOC Dispatcher** | **MCC** | **Engineer** |
|--------------|-------------|---------------------|----------------|----------------|-------------|-------------------|---------|-------------|
| **Pre-flight interface verification** | A | C | R | I | I | I | I | - |
| **Turnaround planning** | I | A | C | C | C | C | I | - |
| **Gate interface connection** | I | A | R | I | I | I | I | - |
| **H₂ refuelling operation** | C | C | I | R/A | - | I | I | - |
| **CO₂ buffer exchange** | I | C | I | - | R/A | I | I | - |
| **Real-time monitoring** | I | C | I | I | I | A | R | C |
| **Interface fault response** | C | C | R | C | C | A | R | C |
| **Predictive maintenance planning** | I | I | - | I | I | C | A | R |
| **Dispatch decision (interface issue)** | A | C | I | C | C | A | C | C |
| **Contingency execution** | A | R | R | R | R | A | C | C |
| **Performance analysis** | I | C | I | I | I | C | C | R/A |
| **Continuous improvement** | I | C | I | C | C | C | C | R/A |

---

## 6. Communication and Coordination Protocols

### 6.1 Normal Operations

**Primary Channel**: 
- Ground Crew ↔ Turnaround Coordinator: Radio (dedicated channel)
- Turnaround Coordinator ↔ AOC: Data link + voice backup
- Flight Crew ↔ Ground Crew: Intercom + hand signals

**Secondary Channel**: Mobile phone, backup radio

**Data Systems**: 
- Turnaround dashboard (real-time interface status)
- AOC monitoring system
- Digital twin alerts

### 6.2 Contingency Operations

**Escalation Path** (Interface Fault):
1. **Ground Crew/Operator** detects fault → Reports to **Turnaround Coordinator**
2. **Turnaround Coordinator** assesses severity → Informs **AOC Dispatcher** + **MCC**
3. **MCC** provides diagnostic support (digital twin insights)
4. **AOC Dispatcher** coordinates with **Captain** on dispatch implications
5. **Captain** makes final dispatch decision
6. If unresolved: **Engineer** engaged for root cause analysis

**Critical Alert Protocol** (Safety Issue):
- Immediate voice communication (all channels)
- Operations suspended until safety confirmed
- Incident command structure activated if needed

**Cross-Reference**: `85-10-07_Operational_Contingencies_and_Degraded_Modes/85-10-07-002_Contingency_Scenarios_and_Playbooks.md`

---

## 7. Training and Competency Management

### 7.1 Training Strategy

All roles interfacing with ATA 85 systems require:

1. **Initial Training**: 
   - Classroom: Theory, procedures, safety
   - Simulator/Mock-up: Hands-on practice
   - On-the-Job Training (OJT): Supervised real-world operations

2. **Recurrent Training**: 
   - Frequency: Annual minimum (more frequent for critical roles)
   - Content: Refresher, updates, lessons learned

3. **Competency Validation**: 
   - Method: Scenario-based evaluation, written/practical exams
   - Frequency: Annually or after significant procedure changes
   - Records: Maintained in training management system

**Cross-Reference**: `85-10-08_Training_and_Simulation_Interfaces/85-10-08-001_Training_Strategy_for_Infra_Interfaces.md`

### 7.2 Competency Matrix

| **Role** | **Initial Training (hours)** | **Recurrent (hours/year)** | **Certification Required** |
|---------|------------------------------|----------------------------|---------------------------|
| **Captain** | 4 | 2 | Type rating + ATA 85 endorsement |
| **Purser** | 2 | 1 | Cabin crew license |
| **Turnaround Coordinator** | 16 | 8 | Company certification |
| **Ground Crew** | 8 | 4 | Company certification |
| **H₂ Refuelling Operator** | 40 | 16 | H₂ handling + aircraft-specific |
| **CO₂ Buffer Technician** | 16 | 8 | CO₂ handling + aircraft-specific |
| **AOC Dispatcher** | 8 | 4 | Dispatcher license + ATA 85 |
| **Line Maintenance Technician** | 24 | 12 | AMT/Part-66 + ATA 85 |
| **Digital Twin Analyst** | 40 | 16 | Platform-specific + ATA 85 |

---

## 8. Performance Metrics and Accountability

### 8.1 Key Performance Indicators (KPIs)

**Interface Operations**:
- **Turnaround On-Time Performance**: % of turnarounds completed without interface delays
- **Interface Fault Rate**: Faults per 1000 operations
- **H₂ Refuelling Efficiency**: Average refuel time vs. target
- **CO₂ Buffer Exchange Time**: Average exchange time vs. target

**Safety**:
- **Interface Safety Incidents**: Count (target: zero)
- **Near-Miss Reporting Rate**: Indicator of safety culture

**Training**:
- **Training Completion Rate**: % of personnel current on training
- **Competency Pass Rate**: % passing competency checks on first attempt

### 8.2 Accountability and Review

- **Quarterly**: Operations review meeting (all stakeholder leads)
  - Review KPIs, discuss issues, identify improvements
- **Annually**: R&R matrix review and update
  - Adjust responsibilities based on operational experience
- **Post-Incident**: Root cause analysis with all involved roles
  - Update procedures and training as needed

---

## 9. Cross-References

### 9.1 Internal (ATA 85)

- `85-10-00-001_Operations_Interface_Overview.md` – Operational ConOps
- `85-10-00-002_Cross_ATA_Operations_Interface_Map.md` – Cross-ATA coordination
- `85-10-01_Turnaround_Interface_Management/` – Turnaround roles
- `85-10-02_H2_Ground_Operations/` – H₂ refuelling roles
- `85-10-06_Real_Time_Monitoring_and_Alerts/` – Monitoring roles
- `85-10-08_Training_and_Simulation_Interfaces/` – Training requirements

### 9.2 External (Other ATAs)

- [ATA 02 – Operations Information](../../ATA_02-OPERATIONS_INFORMATION/) – AOC and dispatch procedures
- ATA 03 – Support Information GSE – GSE operator roles
- [ATA 95 – Digital Product Passport & Neural Networks](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/) – Digital twin roles

### 9.3 Regulatory

- [CS-25.1309](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) – Equipment, systems, and installations
- [EASA Part-66](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-13212014) – Aircraft maintenance licensing

---

## 10. Status and Next Steps

### 10.1 Current Status

- **Phase**: R&R definition (SKELETON)
- **Next Phase**: 
  - Detailed job descriptions and procedures
  - Training curriculum development
  - Competency management system setup

### 10.2 Planned Deliverables

1. Detailed Standard Operating Procedures (SOPs) for each role
2. Training packages (classroom materials, simulator scenarios)
3. Competency evaluation checklists
4. Communication protocols and escalation matrices

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21.

---

**End of Document**
