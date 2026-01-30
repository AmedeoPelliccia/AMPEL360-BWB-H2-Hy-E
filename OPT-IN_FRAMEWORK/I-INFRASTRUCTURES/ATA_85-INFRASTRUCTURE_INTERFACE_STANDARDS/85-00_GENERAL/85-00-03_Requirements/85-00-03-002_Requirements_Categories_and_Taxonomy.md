# 85-00-03-002 — Requirements Categories and Taxonomy

## 1. Purpose

This document defines the **taxonomy and categorization scheme** for infrastructure interface requirements of the AMPEL360 BWB H₂ Hy-E aircraft. It establishes a standardized framework for organizing, classifying, and managing requirements across all infrastructure interface domains.

## 2. Taxonomy Structure

### 2.1 Primary Category Hierarchy

The infrastructure interface requirements are organized into **seven primary categories**, each addressing a distinct aspect of ground infrastructure compatibility:

```
Infrastructure Interface Requirements (85-00-03)
│
├── GEN — General Airport Infrastructure Compatibility
├── H2 — Hydrogen Refuelling Infrastructure
├── CO2BAT — CO₂ Battery and Hybrid Storage Interface
├── ELEC — Electrical Ground Power and Environmental Services
├── PAX — Passenger Boarding, Turnaround, and Evacuation
├── DATA — Data Communications and Operational Integration
└── EMERG — Emergency, Rescue, and Safety Services
```

### 2.2 Category Code Scheme

Each category is assigned a unique alphanumeric code used in requirement IDs:

| Category Code | Full Name | Primary Focus |
|--------------|-----------|---------------|
| **GEN** | General Airport Infrastructure Compatibility | Runways, taxiways, stands, general airport operations |
| **H2** | Hydrogen Refuelling Infrastructure | H₂ storage, delivery, refuelling interfaces, safety zones |
| **CO2BAT** | CO₂ Battery and Hybrid Storage Interface | CO₂ battery charging, hybrid storage, CO₂ off-loading |
| **ELEC** | Electrical Ground Power and Environmental Services | Ground power, power quality, environmental control services |
| **PAX** | Passenger Boarding, Turnaround, and Evacuation | Boarding bridges, ground services, evacuation routes |
| **DATA** | Data Communications and Operational Integration | Data links, operational platforms, DPP integration |
| **EMERG** | Emergency, Rescue, and Safety Services | Fire rescue, emergency response, safety corridors |

## 3. Category Definitions and Scope

### 3.1 GEN — General Airport Infrastructure Compatibility

**Definition**: Requirements defining the physical compatibility of the AMPEL360 aircraft with standard airport infrastructure, including movement areas, parking stands, and general operational facilities.

**Scope Includes**:
- Runway length, width, and strength requirements
- Taxiway and apron clearances
- Aircraft parking stand dimensions and markings
- Airport category and infrastructure classification (Code C/D/E/F per [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx))
- Ground movement procedures and constraints
- Pavement loading and bearing strength
- Navigation aid compatibility

**Typical Requirement Types**:
- Physical dimensions and clearances
- Pavement strength and loading
- Operational procedures and constraints
- Compatibility with airport reference codes

**Example Requirements**:
- `RQ-85-00-03-GEN-001`: Airport runway length and strength requirements
- `RQ-85-00-03-GEN-002`: Taxiway width and clearance requirements
- `RQ-85-00-03-GEN-003`: Aircraft stand dimensions and operational constraints

---

### 3.2 H2 — Hydrogen Refuelling Infrastructure

**Definition**: Requirements for hydrogen fuel storage, delivery, and refuelling interface systems required to service the AMPEL360 aircraft's hydrogen propulsion system.

**Scope Includes**:
- Hydrogen refuelling interface connectors and protocols
- H₂ supply pressure and flow rate requirements (up to 700 bar)
- Hydrogen storage and delivery system specifications
- Safety zones and exclusion perimeters during refuelling
- Refuelling operational procedures and timelines
- Hydrogen quality and purity standards per [ISO 14687](https://www.iso.org/standard/69539.html)
- Emergency shutdown and isolation procedures

**Typical Requirement Types**:
- Physical interface specifications
- Performance requirements (pressure, flow rate, purity)
- Safety and operational constraints
- Compatibility with hydrogen fuelling standards (e.g., [SAE J2601](https://www.sae.org/standards/content/j2601/))

**Example Requirements**:
- `RQ-85-00-03-H2-001`: H₂ refuelling connector interface standard
- `RQ-85-00-03-H2-002`: H₂ supply pressure and flow rate requirements
- `RQ-85-00-03-H2-003`: H₂ refuelling safety zone and operational constraints

---

### 3.3 CO2BAT — CO₂ Battery and Hybrid Storage Interface

**Definition**: Requirements for ground-based charging and servicing interfaces for the aircraft's CO₂ capture battery system and hybrid energy storage.

**Scope Includes**:
- CO₂ battery charging interface (electrical and thermal)
- Hybrid energy storage charging protocols
- CO₂ off-loading and transfer systems (captured CO₂ from aircraft to ground storage)
- Thermal management during charging and servicing
- Battery health monitoring and diagnostics interfaces
- Safety protocols for CO₂ battery incidents
- Containment and handling of captured CO₂

**Typical Requirement Types**:
- Electrical interface specifications (voltage, current, power)
- Thermal management requirements
- Safety and containment protocols
- CO₂ handling and transfer procedures

**Example Requirements**:
- `RQ-85-00-03-CO2BAT-001`: CO₂ battery charging interface electrical specifications
- `RQ-85-00-03-CO2BAT-002`: Hybrid storage operational interface requirements
- `RQ-85-00-03-CO2BAT-003`: CO₂ battery safety and containment protocols

---

### 3.4 ELEC — Electrical Ground Power and Environmental Services

**Definition**: Requirements for electrical ground power supply, power quality, and environmental control services (air conditioning, heating) provided by airport infrastructure.

**Scope Includes**:
- Ground power interface connectors (400 Hz AC and/or DC)
- Voltage, frequency, and power quality specifications
- Harmonic distortion limits
- Ground power capacity and loading
- Environmental control services (preconditioned air, heating)
- Electromagnetic compatibility (EMC) and grounding
- Power supply reliability and backup systems

**Typical Requirement Types**:
- Electrical specifications (voltage, frequency, power, harmonics)
- Interface standards and connector types
- Power quality and reliability requirements
- Environmental control service specifications

**Example Requirements**:
- `RQ-85-00-03-ELEC-001`: Ground power interface voltage and frequency requirements
- `RQ-85-00-03-ELEC-002`: Power quality and harmonic distortion limits
- `RQ-85-00-03-ELEC-003`: Environmental control services interface requirements

---

### 3.5 PAX — Passenger Boarding, Turnaround, and Evacuation

**Definition**: Requirements for passenger boarding infrastructure, ground service equipment, and emergency evacuation access compatible with the BWB configuration.

**Scope Includes**:
- Passenger boarding bridge compatibility (door heights, locations, access angles)
- Ground service vehicle access and positioning
- Turnaround time objectives and ground service sequencing
- Catering, cleaning, and cargo loading access
- Emergency evacuation routes and ground rescue vehicle access
- Passenger mobility assistance (wheelchair lifts, accessibility)
- Novel BWB-specific boarding and evacuation considerations

**Typical Requirement Types**:
- Physical access requirements (heights, angles, clearances)
- Operational timing and sequencing
- Safety and emergency access
- Compatibility with ground service equipment

**Example Requirements**:
- `RQ-85-00-03-PAX-001`: Passenger boarding bridge door height and angle compatibility
- `RQ-85-00-03-PAX-002`: Turnaround time and ground service interface requirements
- `RQ-85-00-03-PAX-003`: Evacuation routes and ground rescue access requirements

---

### 3.6 DATA — Data Communications and Operational Integration

**Definition**: Requirements for data communication interfaces between the aircraft and airport operational systems, including operational data exchange, DPP integration, and cybersecurity.

**Scope Includes**:
- Airport operational data exchange (turnaround status, fuel/energy status, maintenance alerts)
- Aircraft Communications Addressing and Reporting System (ACARS) and datalink
- Digital Product Passport (DPP) integration with airport systems
- Surveillance and ATC data interfaces (ADS-B, Mode S)
- CAOS (AI-powered operations) data requirements
- Cybersecurity protocols per [DO-326A](https://www.rtca.org/content/standards-documents)
- Wi-Fi and high-bandwidth data links for maintenance and diagnostics

**Typical Requirement Types**:
- Data interface protocols and formats
- Bandwidth and latency requirements
- Cybersecurity and encryption standards
- Integration with airport operational platforms

**Example Requirements**:
- `RQ-85-00-03-DATA-001`: Airport operational data interface protocol requirements
- `RQ-85-00-03-DATA-002`: Surveillance and ATC data interface specifications
- `RQ-85-00-03-DATA-003`: DPP and operational platform data exchange requirements

---

### 3.7 EMERG — Emergency, Rescue, and Safety Services

**Definition**: Requirements for emergency response infrastructure, including fire rescue, H₂ emergency procedures, and safety access routes compatible with the aircraft design.

**Scope Includes**:
- Fire and rescue vehicle access routes and positioning
- H₂ emergency response procedures and equipment (specialized firefighting foam, ventilation)
- CO₂ battery emergency procedures (thermal runaway, containment)
- Emergency safety corridors and exclusion zones
- Emergency communication and coordination protocols
- Airport Rescue and Firefighting (ARFF) category requirements per [ICAO Annex 14](https://www.icao.int/safety/pages/annex-14.aspx)
- Novel BWB-specific emergency access considerations

**Typical Requirement Types**:
- Access routes and clearances for emergency vehicles
- Emergency response procedures and equipment
- Safety zones and exclusion perimeters
- Coordination and communication protocols

**Example Requirements**:
- `RQ-85-00-03-EMERG-001`: Fire and rescue vehicle access and positioning requirements
- `RQ-85-00-03-EMERG-002`: H₂ and energy system emergency response procedures
- `RQ-85-00-03-EMERG-003`: Emergency safety corridors and access route requirements

---

## 4. Cross-Category Taxonomy

### 4.1 Requirement Types (Cross-Category)

In addition to category-specific classification, requirements are also classified by **type**:

| Requirement Type | Description | Typical Keywords |
|-----------------|-------------|------------------|
| **Physical** | Dimensional, spatial, and geometric requirements | Dimensions, clearances, heights, widths, angles |
| **Performance** | Functional performance specifications | Flow rates, pressures, power, capacity, timing |
| **Safety** | Safety-critical requirements and constraints | Safety zones, hazards, emergency procedures, risk mitigation |
| **Operational** | Operational procedures and constraints | Turnaround, sequencing, coordination, scheduling |
| **Interface** | Electrical, mechanical, or data interface standards | Connectors, protocols, formats, compatibility |
| **Quality** | Quality attributes (reliability, availability, maintainability) | Uptime, failure rates, harmonics, purity |
| **Regulatory** | Compliance with regulations and standards | EASA, FAA, ICAO, ISO, SAE compliance |

### 4.2 Lifecycle Phase Mapping

Requirements are mapped to specific lifecycle phases:

| Lifecycle Phase | Applicability | Traceability Link |
|----------------|---------------|-------------------|
| **Concept** | High-level infrastructure compatibility assessments | [85-00-01_Overview](../../85-00-01_Overview/) |
| **Safety** | Hazard identification and safety requirements | [85-00-02_Safety](../../85-00-02_Safety/) |
| **Requirements** | Detailed infrastructure interface requirements | [85-00-03_Requirements](./) (this phase) |
| **Design** | Infrastructure interface design specifications | [85-00-04_Design](../../85-00-04_Design/) |
| **V&V** | Verification and validation of infrastructure compatibility | [85-00-07_V_AND_V](../../85-00-07_V_AND_V/) |
| **Certification** | Regulatory approval and certification evidence | [85-00-10_Certification](../../85-00-10_Certification/) |
| **Operations** | Operational procedures and turnaround protocols | [85-10_Operations](../../../85-10_Operations/) |

### 4.3 Stakeholder Mapping

Requirements are also categorized by primary stakeholder:

| Stakeholder | Primary Categories | Typical Interests |
|------------|-------------------|-------------------|
| **Airport Operators** | GEN, PAX, DATA, EMERG | Airport compatibility, turnaround efficiency, safety |
| **Hydrogen Suppliers** | H2 | Refuelling infrastructure, supply chain, safety |
| **Ground Service Providers** | PAX, ELEC, GEN | Ground handling equipment, power supply, turnaround |
| **Energy System Suppliers** | CO2BAT, ELEC | Battery charging, power quality, thermal management |
| **Emergency Services** | EMERG, H2 | Fire rescue, emergency response, safety equipment |
| **Regulatory Authorities** | All categories | Safety, certification, regulatory compliance |
| **Maintenance Organizations** | DATA, ELEC, GEN | Diagnostics, data access, maintenance procedures |

---

## 5. Requirement Attributes and Metadata

Each infrastructure interface requirement includes standardized **metadata attributes**:

| Attribute | Description | Example Values |
|-----------|-------------|----------------|
| **Requirement ID** | Unique identifier | `RQ-85-00-03-H2-001` |
| **Title** | Short descriptive title | "H₂ Refuelling Interface Requirements" |
| **Category** | Primary category code | `H2` |
| **Type** | Requirement type | `Physical`, `Performance`, `Safety`, etc. |
| **Priority** | Implementation priority | `Critical`, `High`, `Medium`, `Low` |
| **Status** | Lifecycle status | `DRAFT`, `FOR_REVIEW`, `APPROVED`, `IMPLEMENTED` |
| **Source** | Originating document or standard | `CS-25.1309`, `ISO 19880-8`, stakeholder input |
| **Owner** | Responsible team or individual | `Propulsion Team`, `Systems Engineering` |
| **Verification Method** | How requirement will be verified | `Analysis`, `Test`, `Inspection`, `Demonstration` |
| **Traceability** | Links to design, test, certification | Design doc ID, test case ID, MoC ID |

---

## 6. Requirement Prioritization Scheme

Requirements are prioritized based on **criticality and implementation urgency**:

### 6.1 Priority Levels

| Priority | Definition | Criteria |
|----------|-----------|----------|
| **Critical** | Must be satisfied for aircraft to operate | Safety-critical, regulatory mandated, no workarounds |
| **High** | Essential for normal operations | Significant operational impact if not satisfied |
| **Medium** | Important but not essential | Operational workarounds exist, future capability |
| **Low** | Desirable but not required | Convenience features, optimization opportunities |

### 6.2 Priority Assignment Examples

- **Critical**: H₂ refuelling safety zones, emergency evacuation access
- **High**: Passenger boarding bridge compatibility, ground power capacity
- **Medium**: Advanced data link bandwidth, optimized turnaround sequencing
- **Low**: Enhanced Wi-Fi coverage, advanced diagnostics interfaces

---

## 7. Requirement Traceability Framework

### 7.1 Upstream Traceability (Sources)

Infrastructure interface requirements trace **upstream** to:

- **Aircraft System Requirements**: Propulsion, energy, structures, avionics
- **Operational Concepts**: Mission profiles, turnaround scenarios, flight operations
- **Regulatory Requirements**: EASA CS-25, FAA Part 25, ICAO Annex 14
- **Industry Standards**: ISO, SAE, RTCA, EUROCAE standards
- **Stakeholder Inputs**: Airport operators, ground service providers

### 7.2 Downstream Traceability (Verification)

Infrastructure interface requirements trace **downstream** to:

- **Design Specifications**: Interface control documents (ICDs), detailed designs
- **Test Cases**: Verification test procedures, acceptance criteria
- **Certification Evidence**: Means of Compliance (MoC), compliance matrices
- **Operational Procedures**: Standard Operating Procedures (SOPs), turnaround checklists

---

## 8. Integration with Other ATA Chapters

Infrastructure interface requirements integrate with multiple ATA chapters:

| ATA Chapter | Integration Point | Example Interfaces |
|------------|-------------------|-------------------|
| **ATA 28** | Hydrogen fuel systems | Refuelling interfaces, fuel quality monitoring |
| **ATA 24** | Electrical power | Ground power interfaces, power distribution |
| **ATA 52** | Doors | Passenger boarding door locations and types |
| **ATA 95** | Digital Product Passport | DPP data exchange, operational integration |
| **ATA 05** | Time limits and maintenance | Turnaround time requirements, scheduled services |

---

## 9. Related Documents

- [85-00-03-001_Infrastructure_Interface_Requirements_Overview](./85-00-03-001_Infrastructure_Interface_Requirements_Overview.md) — High-level overview
- [85-00-03-003_Requirements_Traceability_and_Mapping](./85-00-03-003_Requirements_Traceability_and_Mapping.md) — Traceability matrices
- [85-00-03-004_Requirements_Change_Management](./85-00-03-004_Requirements_Change_Management.md) — Change control procedures
- [ASSETS/85-00-03-A-002_Category_Index.csv](./ASSETS/85-00-03-A-002_Category_Index.csv) — Complete category index

---

## Document Control

- **Document ID**: 85-00-03-002
- **Version**: 1.0
- **Status**: DRAFT — Subject to human review and approval
- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21
- **Classification**: Internal Use
- **Owner**: AMPEL360 Systems Engineering & Requirements WG

---

**For questions or collaboration opportunities, contact: requirements@ampel360.aero**
