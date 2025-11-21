# 85-00-02-008 Regulatory Compliance and Safety Standards Map

## Document Information
- **Document ID**: 85-00-02-008
- **Title**: Regulatory Compliance and Safety Standards Map for Infrastructure Interfaces
- **Version**: 1.0
- **Status**: Draft
- **Last Updated**: 2025-11-21

## Purpose

This document maps **regulations and standards** to BWB infrastructure safety interfaces, establishing compliance requirements for each interface type. It defines how interface safety requirements support regulatory compliance and identifies evidence owners across aircraft manufacturer, airport operator, and infrastructure providers.

## Scope

This document covers:
- **EASA/FAA regulations**: Aircraft certification requirements
- **H₂ infrastructure codes**: ISO, NFPA, EN standards for hydrogen
- **Energy storage codes**: UL, IEC standards for battery systems
- **Airport/building codes**: Fire protection, electrical, structural
- **Compliance matrix**: Interface → Hazard → Standard → Evidence
- **Evidence collection**: Operations logs, tests, drills, inspections

## Regulatory Framework Overview

### Jurisdictional Responsibilities

Interface safety compliance is **shared** across multiple authorities:

| **Domain** | **Authority** | **Jurisdiction** | **Key Regulations** |
|------------|---------------|------------------|-------------------|
| Aircraft systems | EASA (Europe), FAA (USA) | Aircraft design, manufacture, airworthiness | CS-25, Part 25, Part 21 |
| Airport infrastructure | National CAA (Civil Aviation Authority) | Aerodrome design, operations, emergency response | ICAO Annex 14, national airport regulations |
| H₂ infrastructure | National safety authority (e.g., HSE in UK, OSHA in USA) | H₂ production, storage, distribution, dispensing | NFPA 2, ISO 22734, EN 1473, local H₂ codes |
| Energy storage (CO₂ batteries) | Electrical safety authority, fire marshal | Battery installation, fire protection, grid connection | UL 9540, IEC 62619, NFPA 855, local electrical codes |
| Building/fire protection | Local authority (city, county) | Stand structures, fire suppression, evacuation routes | IBC (International Building Code), NFPA 1, local fire codes |

**Key Challenge**: Interface safety must satisfy **all applicable authorities**, requiring coordination and joint approval.

## Aircraft Regulatory Compliance

### EASA Certification Specifications for Large Aeroplanes (CS-25)

**Applicable Sections for Interface Safety**:

#### [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-28) Equipment, Systems, and Installations

**Requirement**: Systems must be designed such that:
- Single failures do not result in catastrophic effects
- Probability of catastrophic failure conditions is extremely improbable (<10⁻⁹ per flight hour)

**Interface Safety Application**:
- **H₂ leak with fire/explosion**: Catastrophic hazard → multiple mitigations (leak detection, emergency shutdown, Ex zone enforcement) ensure extremely improbable occurrence
- **CO₂ battery thermal runaway**: Catastrophic hazard → detection, suppression, containment reduce risk to acceptable level

**Evidence**:
- Functional Hazard Assessment (FHA) including interface hazards (see [85-00-02-002](85-00-02-002_Hazard_Analysis_at_Interface_Level.md))
- System Safety Assessment (SSA) demonstrating compliance with probability targets
- Fault tree analysis (FTA) and Failure Modes and Effects Analysis (FMEA) for interface systems

**Responsible Party**: Aircraft manufacturer (with support from airport/infrastructure for shared hazards)

#### [CS-25.803](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-28) Emergency Evacuation

**Requirement**: Demonstrate 90-second evacuation of maximum capacity (all passengers + crew) using 50% of available exits

**Interface Safety Application**:
- BWB evacuation routes must integrate with airport rescue infrastructure
- Stand layout must not impede slide deployment or rescue access
- Joint evacuation drills validate 90-second performance (see [85-00-02-005](85-00-02-005_Passenger_Evacuation_and_Rescue_Safety_Interfaces.md))

**Evidence**:
- Full-scale evacuation demonstration (certification test)
- Joint drills at operational airports (recurring validation)
- Stand layout approval by airport authority

**Responsible Party**: Aircraft manufacturer (evacuation demonstration) + Airport operator (stand layout)

#### [CS-25.1351](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-28) Electrical Systems and Equipment

**Requirement**: Electrical systems designed to prevent ignition of flammable fluids/vapors, protect against electrical shocks

**Interface Safety Application**:
- Ground power connection must not create ignition source in H₂ Ex zone
- CO₂ battery high-voltage interface must protect ground personnel from electrical shock
- Bonding/grounding prevents static discharge during H₂ refueling

**Evidence**:
- Electrical safety analysis (arc flash, fault propagation)
- Ex zone classification and ignition source control (see [85-00-02-003](85-00-02-003_Safety_Zones_and_Separation_Criteria.md))
- High-voltage safety testing per IEC 60364-4-41

**Responsible Party**: Aircraft manufacturer (on-board systems) + Infrastructure provider (ground power, H₂/CO₂ equipment)

### FAA Federal Aviation Regulations (FAR)

**FAR Part 25**: Airworthiness Standards: Transport Category Airplanes (equivalent to CS-25, similar requirements)

**FAR Part 21**: Certification Procedures for Products and Articles
- Subpart H: Airworthiness Certificates
- Aircraft manufacturer must demonstrate compliance with Part 25 for Type Certificate (TC)
- Interface safety assessments are part of TC application

### EASA Part 21 Certification Procedures

**Part 21.A.15**: Type Certificates — Applicability
- Type certificate application must include safety assessment for novel technologies (H₂, CO₂ batteries)
- Interface hazards with external systems documented in TC dossier

## H₂ Infrastructure Regulatory Compliance

### ISO 22734 Hydrogen Fuel — Quality Specifications

**Requirement**: H₂ purity, moisture content, contaminants specified for fuel cell and combustion applications

**Interface Safety Application**:
- H₂ delivered to aircraft must meet purity specification (prevents fuel cell poisoning, ensures safe combustion)
- Airport H₂ infrastructure includes quality monitoring (on-line sensors or periodic sampling)

**Evidence**:
- H₂ quality certificates from supplier
- Periodic sampling and lab analysis
- On-line monitoring logs (if available)

**Responsible Party**: H₂ supplier + Airport H₂ infrastructure operator

### NFPA 2 Hydrogen Technologies Code

**Chapter 7: Hydrogen Fueling**

**Requirements**:
- Ex zone classification (Zone 0, 1, 2) based on anticipated H₂ release scenarios
- Separation distances between H₂ equipment and ignition sources, public areas
- Leak detection and emergency shutdown systems
- Personnel training and procedures

**Interface Safety Application**:
- H₂ refueling interface design follows NFPA 2 Chapter 7 (see [85-00-02-003](85-00-02-003_Safety_Zones_and_Separation_Criteria.md) for zones, [85-00-02-004](85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md) for shutdown)
- Ground crew training per NFPA 2 requirements (see [85-00-02-006](85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md))

**Evidence**:
- H₂ dispenser design approval (certified by authority having jurisdiction, AHJ)
- Ex zone documentation (drawings, calculations, inspection reports)
- Training records (ground crew, H₂ technicians)
- Operational logs (refueling events, leak detections, shutdowns)

**Responsible Party**: Airport H₂ infrastructure operator (primary) + Aircraft manufacturer (interface compatibility)

### EN 1473 Installation and Equipment for Liquefied Natural Gas / Hydrogen

**Scope**: Design, construction, operation of LNG/H₂ installations (primarily European standard)

**Requirements**:
- Safety systems (pressure relief, leak detection, fire protection)
- Materials selection (compatible with cryogenic H₂ or high-pressure gas)
- Inspection and testing (pressure tests, leak tests)

**Interface Safety Application**:
- If BWB uses liquid H₂ (LH₂) instead of compressed gas → EN 1473 applicable
- Cryogenic safety considerations (frostbite, material embrittlement, rapid vaporization)

**Evidence**:
- LH₂ system design approval (if applicable)
- Cryogenic safety procedures and PPE (personal protective equipment)
- Material compatibility certification

**Responsible Party**: H₂ infrastructure operator (if LH₂) or Aircraft manufacturer (if on-board LH₂ system)

## Energy Storage (CO₂ Battery) Regulatory Compliance

### UL 9540 Energy Storage Systems and Equipment

**Scope**: Safety of stationary and mobile energy storage systems (batteries, capacitors)

**Requirements**:
- Fire testing (thermal runaway propagation, see UL 9540A test method)
- Electrical safety (isolation, fault protection)
- Environmental testing (temperature, humidity, vibration)
- Safety certifications for BMS, enclosures

**Interface Safety Application**:
- CO₂ battery containers must be UL 9540 listed or equivalent certification
- Fire propagation testing demonstrates thermal runaway in one container does not cascade to adjacent containers (validates 5 m separation, see [85-00-02-003](85-00-02-003_Safety_Zones_and_Separation_Criteria.md))

**Evidence**:
- UL 9540 certification for CO₂ battery containers
- UL 9540A test reports (thermal runaway fire propagation)
- BMS safety certification (UL 1973 or equivalent)

**Responsible Party**: Battery manufacturer + Airport energy infrastructure operator (installation and operation)

### IEC 62619 Secondary Cells and Batteries Containing Alkaline or Other Non-Acid Electrolytes — Safety Requirements

**Scope**: Safety testing for lithium-ion and other battery chemistries (if CO₂ battery contains lithium-ion cells in addition to CO₂ storage)

**Requirements**:
- Overcharge, over-discharge, short circuit testing
- Thermal abuse testing (heating to thermal runaway)
- Mechanical abuse testing (crush, nail penetration)

**Interface Safety Application**:
- Battery cells within CO₂ container must meet IEC 62619 (ensures cells do not fail unsafely under abuse conditions)

**Evidence**:
- IEC 62619 test reports for battery cells
- BMS prevents abuse conditions (overcharge, over-discharge, over-temperature)

**Responsible Party**: Battery cell manufacturer + Container integrator

### NFPA 855 Standard for the Installation of Stationary Energy Storage Systems

**Scope**: Installation requirements for large-scale battery systems (>50 kWh)

**Requirements**:
- Separation distances from buildings, property lines
- Fire protection systems (detection, suppression)
- Ventilation (prevent accumulation of flammable gases from venting)
- Emergency response planning

**Interface Safety Application**:
- CO₂ battery docking stations meet NFPA 855 requirements (fire suppression, ventilation, separation)
- Stand layout accounts for NFPA 855 separation distances (see [85-00-02-003](85-00-02-003_Safety_Zones_and_Separation_Criteria.md))

**Evidence**:
- Fire protection system design approval (fire marshal or AHJ)
- Stand layout approval showing compliance with separation distances
- Emergency response plan (coordinated with ARFF)

**Responsible Party**: Airport energy infrastructure operator + ARFF

## Airport and Building Code Compliance

### ICAO Annex 14 Aerodromes — Volume I: Aerodrome Design and Operations

**Chapter 9: Aerodrome Operational Services — Rescue and Fire Fighting**

**Requirements**:
- ARFF response time: Category 1-3 minutes (depending on airport category)
- ARFF equipment capable of reaching all parts of aircraft
- Emergency access roads maintained clear

**Interface Safety Application**:
- Stand layout ensures ARFF vehicles reach BWB exits within 3 minutes (see [85-00-02-003](85-00-02-003_Safety_Zones_and_Separation_Criteria.md))
- Rescue access lanes maintained clear of GSE, energy equipment

**Evidence**:
- Stand layout approval by airport authority
- ARFF response time verification (drills, simulations)
- Periodic inspections of rescue access lanes

**Responsible Party**: Airport operator

### ICAO Doc 9137 Airport Services Manual — Part 1: Rescue and Fire Fighting

**Guidance**: Detailed procedures for ARFF operations, equipment, training

**Interface Safety Application**:
- ARFF training includes BWB-specific procedures (exit locations, H₂/CO₂ hazards)
- Joint drills validate ARFF effectiveness (see [85-00-02-005](85-00-02-005_Passenger_Evacuation_and_Rescue_Safety_Interfaces.md))

**Evidence**:
- ARFF training curriculum (BWB module)
- Drill reports (annual full-scale drills, quarterly desktop exercises)

**Responsible Party**: Airport ARFF + Aircraft manufacturer (provide training materials)

### International Building Code (IBC) and Local Fire Codes

**Requirements**:
- Fire-rated construction for structures housing energy storage
- Fire suppression systems (sprinklers, gas suppression)
- Electrical code compliance (NEC or local equivalent)

**Interface Safety Application**:
- CO₂ battery containers or enclosures meet building code fire resistance ratings
- H₂ infrastructure buildings (if any on airport) meet explosion-resistant construction requirements

**Evidence**:
- Building permits and inspections
- Fire protection system testing and commissioning reports

**Responsible Party**: Airport infrastructure owner + Local building authority

## Compliance Matrix: Interface → Hazard → Standard → Evidence

### H₂ Refueling Interface

| **Hazard** | **Hazard ID** | **Applicable Standards** | **Compliance Evidence** | **Evidence Owner** |
|------------|--------------|-------------------------|------------------------|-------------------|
| H₂ leak with fire/explosion | IFH-H2-001 | CS-25.1309, NFPA 2, ISO 22734 | FHA/SSA, Ex zone documentation, leak detection test reports | Aircraft mfr + H₂ infrastructure operator |
| Overpressure during refueling | IFH-H2-002 | CS-25.1309, NFPA 2, EN 1473 | Pressure relief valve tests, dispenser control validation | H₂ infrastructure operator |
| Ignition source in Ex zone | IFH-H2-005 | CS-25.1351, NFPA 2, IEC 60079 | Ex zone classification, ignition source control audit, bonding/grounding tests | Airport operator + H₂ infrastructure operator |
| Personnel exposure (toxic, asphyxiation) | IFH-H2-006 | OSHA (or local OSH), NFPA 2 | Ventilation design, H₂ monitoring, PPE requirements, training records | Airport operator |

### CO₂ Battery Docking Interface

| **Hazard** | **Hazard ID** | **Applicable Standards** | **Compliance Evidence** | **Evidence Owner** |
|------------|--------------|-------------------------|------------------------|-------------------|
| Thermal runaway with fire | IFH-CO2-001 | CS-25.1309, UL 9540/9540A, NFPA 855 | FHA/SSA, UL 9540A test report, fire suppression validation | Aircraft mfr + Battery operator |
| Electrical isolation failure (arc flash) | IFH-CO2-003 | CS-25.1351, IEC 60364-4-41, NFPA 70E | High-voltage safety analysis, isolation resistance tests, arc flash study | Battery operator |
| Toxic gas release (venting failure) | IFH-CO2-002 | UL 9540, NFPA 855, OSHA | Ventilation design, gas detection, PPE, emergency procedures | Battery operator + Airport ARFF |
| Grid back-feed (during discharge) | IFH-PWR-001 | CS-25.1351, IEC 61727, local grid code | Anti-islanding protection, grid interconnection approval | Battery operator + Utility |

### Evacuation and Rescue Interface

| **Hazard** | **Hazard ID** | **Applicable Standards** | **Compliance Evidence** | **Evidence Owner** |
|------------|--------------|-------------------------|------------------------|-------------------|
| Blocked rescue access (delayed evacuation) | IFH-EVAC-001 | CS-25.803, ICAO Annex 14, Doc 9137 | 90-second evacuation demo, stand layout approval, ARFF drill reports | Aircraft mfr + Airport operator |
| Smoke obscuring evacuation routes | IFH-EVAC-002 | CS-25.803, CS-25.851 (fire protection), ICAO Doc 9137 | Fire detection and suppression validation, ARFF response procedures | Aircraft mfr + Airport ARFF |
| Inadequate ARFF equipment reach | IFH-EVAC-003 | ICAO Annex 14, Doc 9137 | ARFF vehicle capability assessment, reach verification (drills) | Airport ARFF |

## Evidence Collection and Management

### Operations Logs

**H₂ Refueling Logs**:
- Each refueling event logged: date/time, aircraft, operator, delivered mass, anomalies
- Leak detection events (pre-alarms, alarms) logged with response actions
- Retention: 5 years (regulatory requirement for safety-critical operations)

**CO₂ Battery Operations Logs**:
- Docking/undocking events: date/time, aircraft, container ID, charge/discharge energy (kWh)
- Temperature excursions, fire suppression activations
- Retention: 5 years

**Responsible Party**: Airport infrastructure operator (maintain logs), provide to authorities on request

### Tests and Inspections

**Periodic Testing**:
- **H₂ leak detectors**: Daily function test, monthly calibration, annual replacement
- **CO₂ battery fire suppression**: Annual discharge test (one zone or full system)
- **Pressure relief valves (H₂)**: Annual proof test (verify setpoint, seal tight below setpoint)
- **Emergency shutdown systems**: Quarterly functional test (simulate alarm, verify shutdown sequence)

**Inspection Reports**:
- Stand layout inspections: Quarterly (verify rescue access lanes clear, Ex zones marked, signage legible)
- H₂ dispenser inspections: Monthly (visual check for damage, leaks, corrosion)
- CO₂ battery container inspections: Monthly (thermal imaging scan for hot spots, visual check for damage)

**Retention**: 3 years for test reports, 5 years for safety-critical system tests

**Responsible Party**: Infrastructure operator (conduct tests) + Maintenance provider (if contracted)

### Drills and Exercises

**Full-Scale Evacuation Drill**:
- Frequency: Annual (required for aircraft type certification)
- Participants: Flight crew, ARFF, ground staff, passengers (volunteers or mannequins)
- Report: Evacuation time, issues encountered, corrective actions
- Retention: Permanent (part of certification dossier)

**Desktop Exercises** (tabletop simulation):
- Frequency: Quarterly
- Scenarios: H₂ leak, CO₂ battery fire, evacuation, etc.
- Report: Lessons learned, procedure updates
- Retention: 3 years

**ARFF Familiarization**:
- Frequency: Twice annually (or when ARFF personnel change)
- Activities: Walk around BWB aircraft (or mockup), practice rescue access, review hazards
- Report: Attendance, feedback
- Retention: 3 years

**Responsible Party**: Airport ARFF (organize drills) + Aircraft manufacturer (support, provide aircraft/mockup)

### Compliance Audits

**Internal Audits**:
- Frequency: Quarterly (by airport safety department)
- Scope: Verify procedures followed, logs complete, tests current, Ex zones maintained
- Report: Non-conformances, corrective actions, due dates

**External Audits**:
- Frequency: Annual (by regulatory authority or third-party auditor)
- Scope: Comprehensive review of compliance with all applicable regulations/standards
- Report: Findings, corrective action plan, follow-up verification

**Responsible Party**: Airport operator (subject of audit) + Regulatory authority (conduct external audit)

## Cross-ATA Compliance Traceability

Interface safety compliance integrates with on-board system compliance:

**Example Traceability Chain**:
1. **CS-25.1309** requires catastrophic hazards be extremely improbable (<10⁻⁹ per flight hour)
2. **Interface hazard IFH-H2-001** (H₂ leak with fire) is classified as catastrophic
3. **Mitigations allocated**:
   - On-board: Aircraft H₂ leak detection (ATA 28), emergency shutoff valve (ATA 28)
   - Infrastructure: Ex zone enforcement (ATA 85), dispenser leak detection (ATA 85), emergency shutdown (ATA 85)
   - Procedures: Ground crew training (ATA 85), refueling checklist (ATA 85)
4. **SSA demonstrates** combined effectiveness of mitigations → hazard probability <10⁻⁹
5. **Evidence**: ATA 28 SSA (on-board systems) + ATA 85 interface safety assessment + operational logs (refueling events, leak detection activations)
6. **Responsible parties**: Aircraft manufacturer (ATA 28 SSA) + Airport/H₂ operator (ATA 85 interface assessment, operational logs)

**Cross-ATA References**:
- [ATA 26 Fire Protection](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E1-ENVIRONMENT/ATA_26-FIRE_PROTECTION/)
- [ATA 28 Fuel/H₂](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CARBON_NEUTRAL_FUEL_SYSTEMS/ATA_28-FUEL/)
- [ATA 52 Doors](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/A-AIRFRAME/ATA_52-DOORS/)
- [ATA 70 Propulsion](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/ATA_70-STANDARD_PRACTICES_ENGINES/)
- [ATA 80 Energy](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_80-STARTING/)
- [ATA 99 Carbon](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C1-CARBON_NEUTRAL_CIRCULARITY/ATA_99-CARBON/)

## Summary: Regulatory Strategy for Interface Safety

**Key Principles**:
1. **Shared responsibility**: Aircraft manufacturer, airport operator, infrastructure providers each own compliance for their domain, with joint responsibility at interfaces
2. **Early engagement**: Involve regulatory authorities (EASA, FAA, local safety authorities) early in design to align on compliance approach
3. **Joint safety cases**: Develop coordinated safety assessments (aircraft + infrastructure) demonstrating overall system safety
4. **Evidence trail**: Maintain clear traceability from hazard → requirement → standard → evidence → responsible party
5. **Continuous compliance**: Operational logs, periodic tests, drills provide ongoing evidence of continued compliance (beyond initial certification)

## Related Documents

- [85-00-02-001_Safety_Concepts_and_Objectives.md](85-00-02-001_Safety_Concepts_and_Objectives.md) - Safety objectives
- [85-00-02-002_Hazard_Analysis_at_Interface_Level.md](85-00-02-002_Hazard_Analysis_at_Interface_Level.md) - Interface hazards and traceability
- [85-00-02-003_Safety_Zones_and_Separation_Criteria.md](85-00-02-003_Safety_Zones_and_Separation_Criteria.md) - Separation requirements
- [85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md](85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md) - Energy interface safety details
- [85-00-02-005_Passenger_Evacuation_and_Rescue_Safety_Interfaces.md](85-00-02-005_Passenger_Evacuation_and_Rescue_Safety_Interfaces.md) - Evacuation compliance
- [85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md](85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md) - Operational procedures
- [../85-00-10_Certification/](../85-00-10_Certification/) - Certification strategy and planning

## References

### Aircraft Regulations
- **[EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-28)**: Certification Specifications for Large Aeroplanes
- **[EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)**: Certification Procedures for Aircraft and Related Products
- **FAA Part 25**: Airworthiness Standards: Transport Category Airplanes
- **FAA Part 21**: Certification Procedures for Products and Articles

### H₂ Infrastructure Standards
- **ISO 22734**: Hydrogen fuel — Quality specifications
- **[NFPA 2](https://www.nfpa.org/codes-and-standards/2/hydrogen-technologies-code)**: Hydrogen Technologies Code
- **EN 1473**: Installation and equipment for liquefied natural gas/hydrogen
- **IEC 60079-10-1**: Explosive atmospheres — Classification of areas — Explosive gas atmospheres

### Energy Storage Standards
- **UL 9540**: Energy Storage Systems and Equipment
- **UL 9540A**: Test Method for Evaluating Thermal Runaway Fire Propagation in Battery Energy Storage Systems
- **IEC 62619**: Secondary cells and batteries containing alkaline or other non-acid electrolytes — Safety requirements
- **NFPA 855**: Standard for the Installation of Stationary Energy Storage Systems
- **IEC 60364-4-41**: Low-voltage electrical installations — Protection against electric shock

### Airport and Emergency Response
- **[ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx)**: Aerodromes — Volume I: Aerodrome Design and Operations
- **ICAO Doc 9137**: Airport Services Manual — Part 1: Rescue and Fire Fighting
- **International Building Code (IBC)**
- **NFPA 1**: Fire Code

## Document Control

- **Owner**: AMPEL360 Safety & Certification Team
- **Approver**: Chief Safety Officer
- **Review Frequency**: Quarterly
- **Next Review**: 2026-02-21
- **Repository**: AMPEL360-BWB-H2-Hy-E
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **DRAFT** – Subject to human review and approval
- Human approver: _[to be completed]_
- Last AI update: 2025-11-21

---
*This document is part of the AMPEL360 OPT-IN Framework certification package.*
