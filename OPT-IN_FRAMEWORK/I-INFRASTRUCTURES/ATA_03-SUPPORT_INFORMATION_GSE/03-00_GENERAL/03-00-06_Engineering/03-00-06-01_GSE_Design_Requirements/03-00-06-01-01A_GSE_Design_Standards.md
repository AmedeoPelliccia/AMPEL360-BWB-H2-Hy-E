---
Title: "GSE Design Standards — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-06-01-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Design standards and guidelines for Ground Support Equipment (GSE) applicable to AMPEL360 BWB H2 aircraft operations."
Keywords: ["ATA 03","GSE","Design Standards","Engineering","Ground Support"]
Compliance:
  - "ATA iSpec 2200"
  - "SAE ARP1796"
  - "ISO 9001"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  Parent: "../00_INDEX.md"
  Related: "./03-00-06-01-02A_GSE_Specifications.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-00-06-01-01A — GSE Design Standards

## 1. Purpose

This document defines the **design standards and guidelines** for Ground Support Equipment (GSE) used in servicing the AMPEL360 BWB H2-powered aircraft. These standards ensure that all GSE is designed to meet safety, reliability, maintainability, and operational requirements.

## 2. Scope

This document covers:

- **General GSE design principles** applicable to all equipment types
- **Design standards** for mechanical, electrical, and software components
- **Interface standards** between GSE and aircraft
- **Environmental and ergonomic requirements**
- **Special requirements** for hydrogen-compatible GSE

This document applies to all GSE used for:
- Aircraft servicing (refueling, electrical power, air conditioning)
- Ground handling (towing, lifting, loading)
- Maintenance operations (platforms, tooling, test equipment)

## 3. Applicable Documents

### 3.1 Regulatory and Industry Standards

- [ATA iSpec 2200](https://www.ata.org/resources/specifications) — Information Standards for Aviation Maintenance
- [SAE ARP1796](https://www.sae.org/standards/content/arp1796/) — Aerospace Ground Equipment Design Requirements
- [ISO 9001](https://www.iso.org/iso-9001-quality-management.html) — Quality Management Systems
- [SAE AS6968](https://www.sae.org/standards/content/as6968/) — Hydrogen Aircraft Ground Support Equipment (Refueling)
- [ISO 19880-8](https://www.iso.org/standard/71940.html) — Gaseous Hydrogen Fueling Stations (Airport Applications)

### 3.2 Related Documents

- [03-00-06-01-02A_GSE_Specifications](./03-00-06-01-02A_GSE_Specifications.md) — GSE Technical Specifications
- [03-00-06-01-03A_Environmental_Requirements](./03-00-06-01-03A_Environmental_Requirements.md) — Environmental Requirements
- [03-00-06-01-04A_Ergonomic_Requirements](./03-00-06-01-04A_Ergonomic_Requirements.md) — Ergonomic Requirements
- [03-00-05_Interfaces](../../03-00-05_Interfaces/) — GSE-Aircraft Interface Requirements
- [03-00-02_Safety](../../03-00-02_Safety/) — GSE Safety Requirements

## 4. General Design Principles

### 4.1 Safety-First Design

| Principle | Description | Verification |
|-----------|-------------|--------------|
| Fail-Safe Design | GSE shall be designed to fail in a safe state without causing harm to personnel, aircraft, or environment | FMEA, Testing |
| Redundancy | Critical safety functions shall have redundant design features | Design Review |
| Emergency Shutoff | All GSE shall have clearly marked emergency shutoff controls accessible within 3 seconds | Inspection, Test |
| Hazard Mitigation | Identified hazards shall be eliminated by design or mitigated through engineering controls | Safety Assessment |

### 4.2 Human Factors Integration

| Principle | Description | Verification |
|-----------|-------------|--------------|
| Intuitive Operation | Controls and displays shall be intuitive and require minimal training | Usability Testing |
| Error Prevention | Design shall prevent common operator errors through interlocks and warnings | Design Review, Test |
| Visibility | All operational areas shall be visible to the operator or monitored by sensors | Inspection |
| Accessibility | Controls shall be accessible from normal operating positions | Ergonomic Assessment |

### 4.3 Maintainability

| Principle | Description | Verification |
|-----------|-------------|--------------|
| Modular Design | GSE shall use modular components for easy replacement and maintenance | Design Review |
| Diagnostic Capability | GSE shall include built-in test equipment (BITE) for fault diagnosis | Testing |
| Access for Maintenance | Maintenance points shall be accessible without removal of major assemblies | Inspection |
| Standard Parts | Use industry-standard parts where possible to reduce spares inventory | Parts List Review |

### 4.4 Reliability and Durability

| Principle | Description | Verification |
|-----------|-------------|--------------|
| Design Life | GSE shall be designed for minimum 20-year service life | Analysis, Testing |
| Environmental Protection | GSE shall withstand environmental conditions per specifications | Environmental Testing |
| Material Selection | Materials shall be selected for corrosion resistance and durability | Materials Review |
| Fatigue Resistance | Structural components shall be designed for cyclic loading | Fatigue Analysis |

## 5. Design Standards by Discipline

### 5.1 Mechanical Design Standards

| Standard | Requirement | Reference |
|----------|-------------|-----------|
| **Structural Integrity** | All load-bearing structures shall meet minimum safety factor of 1.5 for static loads and 3.0 for dynamic loads | SAE ARP1796 |
| **Corrosion Protection** | All metal surfaces shall be protected against corrosion per MIL-STD-889 | MIL-STD-889 |
| **Fasteners** | Use of standard aerospace fasteners (NAS, MS, AN series) preferred | AS standards |
| **Welding** | Welding shall comply with AWS D1.1 (structural steel) or AWS D17.1 (aircraft) | AWS standards |
| **Hydraulic Systems** | Hydraulic components shall meet SAE J1065 and operate at pressures ≤ 3000 psi | SAE J1065 |
| **Pneumatic Systems** | Pneumatic systems shall comply with ISO 4414 | ISO 4414 |

### 5.2 Electrical Design Standards

| Standard | Requirement | Reference |
|----------|-------------|-----------|
| **Voltage Standards** | Power systems: 115/200 VAC 400Hz (aircraft), 28 VDC, 208/480 VAC 60Hz (ground) | MIL-STD-704 |
| **EMI/EMC** | Electromagnetic compatibility per DO-160 Category M (ground equipment) | RTCA DO-160 |
| **Grounding** | All equipment shall have protective earth grounding per NEC Article 250 | NEC 2020 |
| **Circuit Protection** | All circuits shall have overcurrent protection (fuses or circuit breakers) | NEC 2020 |
| **Wiring** | Wiring shall meet MIL-W-5088 (general purpose) or MIL-W-81381 (lightweight) | MIL-STD-5088 |
| **Connectors** | Use hermetically sealed connectors in wet/corrosive environments | MIL-C-38999 |

### 5.3 Software and Control System Standards

| Standard | Requirement | Reference |
|----------|-------------|-----------|
| **Software Development** | Safety-critical software shall follow DO-178C Level C or higher | RTCA DO-178C |
| **PLC Programming** | Programmable logic controllers shall follow IEC 61131-3 | IEC 61131-3 |
| **HMI Design** | Human-machine interfaces shall follow ISO 9241 usability guidelines | ISO 9241 |
| **Cybersecurity** | Networked GSE shall implement security measures per IEC 62443 | IEC 62443 |
| **Communication Protocols** | Use standardized protocols (Modbus, OPC UA, Ethernet/IP) | Industry standards |

### 5.4 Hydrogen-Compatible Design Standards

| Standard | Requirement | Reference |
|----------|-------------|-----------|
| **Material Compatibility** | Materials in contact with hydrogen shall resist hydrogen embrittlement | NASA-STD-8719.17 |
| **Leak Detection** | Hydrogen systems shall have continuous leak detection with alarm | ISO 19880-8 |
| **Ventilation** | Enclosed spaces with hydrogen equipment require forced ventilation | NFPA 2 |
| **Ignition Source Control** | Eliminate ignition sources within 3m of hydrogen vents/connections | ISO 19880-8 |
| **Pressure Relief** | All hydrogen pressure vessels require pressure relief devices | ASME Section VIII |
| **Bonding and Grounding** | All hydrogen equipment shall be bonded and grounded to prevent static discharge | NFPA 77 |

## 6. Interface Design Standards

### 6.1 Mechanical Interfaces

| Interface Type | Standard | Notes |
|----------------|----------|-------|
| **Fueling Connections** | SAE AS6968 (LH2), SAE AS1833 (Jet A) | BWB-specific adapters may be required |
| **Electrical Connectors** | MIL-C-38999 (power), MIL-C-26482 (signal) | Standardize connector types across GSE |
| **Hydraulic Couplings** | ISO 7241-1 (quick disconnect) | Use dry-break couplings to minimize spillage |
| **Pneumatic Couplings** | ISO 6150 (quick disconnect) | Include safety lockout features |
| **Towing Attachments** | SAE AS25420 | Verify compatibility with BWB nose gear |
| **Lifting Points** | Aircraft-specific per AFM | Document all approved lifting points |

### 6.2 Electrical Interfaces

| Interface Type | Voltage/Signal | Standard | Notes |
|----------------|----------------|----------|-------|
| **GPU Power Output** | 115/200 VAC 400Hz, 28 VDC | MIL-STD-704F | Monitor voltage, frequency, and THD |
| **Data Communication** | ARINC 429, CAN bus, Ethernet | Aircraft-specific | Define communication protocol early |
| **Interlock Signals** | 28 VDC discrete | — | Use for safety interlocks (e.g., fuel connected) |

### 6.3 Software Interfaces

| Interface | Protocol | Application |
|-----------|----------|-------------|
| **GSE-to-Aircraft Data Link** | ARINC 615A (data load), TBD (fuel/power monitoring) | Coordinate with avionics team |
| **GSE Fleet Management** | OPC UA, MQTT | Central monitoring and dispatch system |
| **Maintenance Diagnostics** | IADS (Integrated Aircraft Diagnostics System) | Enable remote troubleshooting |

## 7. Environmental and Operational Requirements

### 7.1 Environmental Conditions

GSE shall operate in the following environmental conditions per [03-00-06-01-03A_Environmental_Requirements](./03-00-06-01-03A_Environmental_Requirements.md):

| Parameter | Operating Range | Storage Range | Notes |
|-----------|----------------|---------------|-------|
| **Temperature** | -40°C to +55°C | -55°C to +70°C | LH2 GSE requires cryogenic capability |
| **Humidity** | 0-95% RH (non-condensing) | 0-95% RH | |
| **Altitude** | Sea level to 3000m (10,000 ft) | — | Airport elevation consideration |
| **Wind** | Operation up to 25 knots | Secure above 25 knots | Wind loading per ASCE 7 |
| **Precipitation** | Rain, snow, ice operation | — | IP65 rating minimum for outdoor GSE |
| **Solar Radiation** | Up to 1120 W/m² | — | Consider thermal effects on electronics |

### 7.2 Mobility and Portability

| Requirement | Specification | Verification |
|-------------|---------------|--------------|
| **Towing Speed** | Towable equipment: max 40 km/h (25 mph) | Test |
| **Self-Propelled Speed** | Self-propelled equipment: max 25 km/h (15 mph) | Test |
| **Ground Clearance** | Minimum 100mm (4 inches) for outdoor GSE | Inspection |
| **Turning Radius** | Maximum 10m for standard ramp GSE | Dimensional check |
| **Ramp Loading** | Equipment weight shall not exceed 500 kg/m² on apron | Structural analysis |

## 8. Quality and Configuration Management

### 8.1 Design Documentation Requirements

| Document | Description | Approval |
|----------|-------------|----------|
| **Design Specification** | Detailed technical requirements | Chief Engineer |
| **Design Drawings** | Mechanical, electrical, and software architecture | Design Review Board |
| **Interface Control Documents (ICD)** | GSE-aircraft interface definitions | Systems Integration Lead |
| **Failure Modes and Effects Analysis (FMEA)** | Safety and reliability analysis | Safety Manager |
| **Test Plans** | Verification and validation test procedures | V&V Lead |

### 8.2 Configuration Control

| Requirement | Description | Reference |
|-------------|-------------|-----------|
| **Design Baseline** | All designs shall be placed under configuration control after Critical Design Review (CDR) | ISO 9001 |
| **Change Management** | Design changes require Engineering Change Request (ECR) and approval | Configuration Management Plan |
| **As-Built Records** | Maintain as-built drawings and deviations from design | Quality procedures |
| **Serialization** | All GSE units shall have unique serial numbers traceable to build records | Traceability requirements |

## 9. Verification and Validation

### 9.1 Design Verification

| Activity | Method | Acceptance Criteria |
|----------|--------|---------------------|
| **Design Review** | Peer review by independent engineers | No open critical issues |
| **Analysis** | Structural, thermal, electrical analysis | Margins meet requirements |
| **Inspection** | Dimensional and workmanship inspection | Per drawing tolerances |
| **Testing** | Functional, environmental, safety testing | All requirements verified |

### 9.2 Validation

| Activity | Description | Success Criteria |
|----------|-------------|------------------|
| **Operational Testing** | Test GSE with actual aircraft or high-fidelity mockup | Successful operations per procedures |
| **Usability Testing** | Evaluate ease of use with representative operators | <5% error rate, positive feedback |
| **Reliability Testing** | Accelerated life testing or fleet data analysis | Meets MTBF targets |

## 10. Certification and Compliance

### 10.1 Type Approval Requirements

| GSE Category | Certification | Authority | Notes |
|--------------|---------------|-----------|-------|
| **Hydrogen Refueling GSE** | Type approval per national regulations | Local authority (e.g., BAM in Germany) | Required before first use |
| **Pressure Equipment** | PED 2014/68/EU (Europe) or ASME BPVC (USA) | Notified Body / ASME AI | Applies to pressure vessels and piping |
| **Lifting Equipment** | LOLER (UK), DGUV (Germany), OSHA (USA) | HSE, BG, OSHA | Annual inspections required |
| **Electrical Equipment** | Low Voltage Directive 2014/35/EU, NEC (USA) | CE marking, UL listing | Electromagnetic compatibility also required |

### 10.2 Periodic Inspections

| Equipment Type | Inspection Frequency | Inspector Qualification |
|----------------|----------------------|-------------------------|
| **Hydrogen Systems** | 6 months | Certified pressure equipment inspector |
| **Lifting Equipment** | 12 months (or per local regulation) | Competent person per regulations |
| **Electrical Systems** | 12 months | Licensed electrician |
| **Pressure Vessels** | Per code (typically 5 years) | Authorized inspector (AI) |

## 11. Cross-References

### 11.1 Related ATA Chapters

- **ATA 03-00-02** — Safety requirements for GSE
- **ATA 03-00-03** — GSE functional and performance requirements
- **ATA 03-00-04** — GSE design documentation
- **ATA 03-00-05** — GSE-aircraft interface specifications
- **ATA 03-00-07** — Verification and validation of GSE
- **ATA 03-10** — GSE operational procedures
- **ATA 03-20** — GSE subsystem details

### 11.2 External Standards

- [SAE ARP1796](https://www.sae.org/standards/content/arp1796/) — GSE Design Requirements
- [SAE AS6968](https://www.sae.org/standards/content/as6968/) — Hydrogen Aircraft GSE
- [ISO 19880-8](https://www.iso.org/standard/71940.html) — Gaseous Hydrogen Fueling Stations
- [RTCA DO-178C](https://www.rtca.org/content/standards-guidance-materials) — Software Considerations in Airborne Systems
- [NASA-STD-8719.17](https://standards.nasa.gov/) — Hydrogen Safety Standard

## 12. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-06-01-01A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Engineering & Certification WG

---
