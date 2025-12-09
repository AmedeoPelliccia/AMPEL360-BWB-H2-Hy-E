---
Title: "GSE Test Resources"
Identifier: "AMPEL360-03-00-07-01-04A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 GSE V&V Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Comprehensive specification of test resources including facilities, equipment, personnel, and instrumentation required for GSE verification."
Keywords: ["ATA 03","GSE","Test Resources","Testing Equipment","Facilities"]
Compliance:
  - "ATA iSpec 2200"
  - "ISO 17025"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../../"
  RelatedDocuments:
    - "../03-00-07-01-01A_GSE_Verification_Strategy.md"
    - "../03-00-07-01-02A_GSE_Test_Plan.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 GSE V&V Team", change: "Initial test resources specification" }
---

# 03-00-07-01-04A — GSE Test Resources

## 1. Purpose

This document defines and specifies all resources required for Ground Support Equipment (GSE) verification and validation activities. It includes test facilities, equipment, instrumentation, personnel qualifications, and support resources necessary for comprehensive GSE testing.

## 2. Scope

This document covers:

- **Test Facilities**: Laboratories, test sites, and operational environments
- **Test Equipment**: Measurement instruments, data acquisition systems, and calibration
- **Personnel**: Qualifications, certifications, and training requirements
- **Support Resources**: Utilities, safety equipment, and logistics
- **Resource Scheduling**: Allocation and availability management

## 3. Applicable Documents

- [ISO 17025](https://www.iso.org/standard/66912.html) — Testing and Calibration Laboratories
- [NIST Handbook 150](https://www.nist.gov/topics/laboratory-accreditation/nist-handbook-150) — Calibration requirements
- [ATEX Directive 2014/34/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0034) — Explosive atmospheres equipment
- [03-00-07-01-02A_GSE_Test_Plan.md](./03-00-07-01-02A_GSE_Test_Plan.md) — Test plan

## 4. Test Facilities

### 4.1 H₂ Test Facility

**Required Capabilities:**

| Capability | Specification | Justification |
|------------|---------------|---------------|
| **Cryogenic Testing** | -270°C to +50°C | LH₂ system testing at -253°C |
| **Pressure Testing** | 0-500 bar | High-pressure H₂ systems |
| **Leak Testing** | Detection to 1×10⁻⁹ mbar·L/s | Ultra-sensitive leak detection |
| **Ventilation** | ≥6 air changes/hour | H₂ safety |
| **H₂ Detection** | 0-1000 ppm, response < 1s | Continuous safety monitoring |
| **Area Classification** | ATEX Zone 1 | Explosive atmosphere protection |
| **Fire Suppression** | Automatic detection + suppression | H₂ fire safety |

**Certifications Required:**
- ISO 17025 accreditation
- ATEX Zone 1 certification
- Local fire marshal approval
- Environmental permits for H₂ venting

**Location Options:**
1. Certified cryogenic test facility (preferred)
2. Dedicated H₂ testing site with appropriate certifications
3. Manufacturer facility with required certifications (subject to audit)

### 4.2 Electrical Test Laboratory

**Required Capabilities:**

| Capability | Specification | Justification |
|------------|---------------|---------------|
| **Power Supply** | 3-phase 400V/200A | High-power GSE testing |
| **Power Quality** | THD measurement, harmonics analysis | Power quality verification |
| **EMC Testing** | MIL-STD-461, IEC 61000 | EMC compliance |
| **Load Bank** | 0-200 kVA programmable | GPU load testing |
| **Oscilloscopes** | 4-channel, 100 MHz, 1 GS/s | Waveform analysis |
| **Environmental Control** | 20°C ±2°C, 50% RH ±10% | Stable test conditions |

**Certifications Required:**
- ISO 17025 accreditation for electrical testing
- EMC test site accreditation (if performing EMC tests)
- Electrical safety inspections current

### 4.3 Mechanical Test Facility

**Required Capabilities:**

| Capability | Specification | Justification |
|------------|---------------|---------------|
| **Structural Testing** | Load capacity ≥200 tons | Towing equipment testing |
| **Fatigue Testing** | Cyclic loading, 1-100 Hz | Durability verification |
| **Environmental Chamber** | -40°C to +85°C, humidity control | Environmental qualification |
| **Vibration Test** | Electrodynamic shaker, 20 kN | MIL-STD-810 compliance |
| **Tensile/Compression** | Universal testing machine, 500 kN | Material/component testing |
| **Non-Destructive Testing** | Ultrasonic, X-ray, dye penetrant | Structural integrity verification |

**Certifications Required:**
- ISO 17025 accreditation for mechanical testing
- Load test equipment annual certification
- NDT personnel Level II certification

### 4.4 Integration Test Site

**Required Capabilities:**

| Capability | Specification | Justification |
|------------|---------------|---------------|
| **Aircraft Mockup/Test Article** | Full-scale BWB interfaces | Interface verification |
| **Apron Space** | ≥5000 m² | Multi-GSE integration |
| **Utilities** | Power, compressed air, water | GSE operations support |
| **Weather Protection** | Hangar or covered area (optional) | All-weather testing capability |
| **Data Infrastructure** | Network, data acquisition | Real-time monitoring |
| **Safety Infrastructure** | Emergency equipment, fire systems | Safety compliance |

**Location Requirements:**
- Airport or dedicated test facility
- Appropriate clearances for GSE operations
- Access to H₂ supply (for H₂ GSE testing)
- Emergency response coordination

### 4.5 Operational Test Site

**Required Capabilities:**

- Fully operational airport with AMPEL360-compatible infrastructure
- Hydrogen refueling infrastructure (operational or test)
- Standard GSE support equipment
- Trained ground handling personnel
- Regulatory authority oversight (as required)

## 5. Test Equipment and Instrumentation

### 5.1 H₂ Testing Equipment

| Equipment | Specification | Quantity | Calibration | Traceability |
|-----------|---------------|----------|-------------|--------------|
| **H₂ Gas Detectors** | 0-1000 ppm, ±1% | 10 | Annual | NIST |
| **Helium Leak Detector** | 1×10⁻⁹ mbar·L/s | 2 | Annual | NIST |
| **Cryogenic Thermocouples** | Type T, -270°C to +400°C, ±0.5°C | 50 | Semi-annual | NIST |
| **Pressure Transducers** | 0-500 bar, ±0.1% FS | 30 | Annual | NIST |
| **Mass Flow Meters** | 0-1000 kg/h LH₂, ±0.5% | 5 | Annual | NIST |
| **Liquid Level Sensors** | 0-100%, cryogenic-rated | 10 | Annual | NIST |
| **Purity Analyzer** | H₂ purity 99.9-100% | 2 | Quarterly | NIST |

### 5.2 Electrical Testing Equipment

| Equipment | Specification | Quantity | Calibration | Traceability |
|-----------|---------------|----------|-------------|--------------|
| **Power Analyzer** | 3-phase, THD, harmonics, PF | 5 | Annual | NIST |
| **Digital Multimeter** | 6½ digit, 0.0035% accuracy | 10 | Annual | NIST |
| **Oscilloscope** | 4-ch, 100 MHz, 1 GS/s | 5 | Bi-annual | NIST |
| **Ground Resistance Tester** | 0.01-2000Ω, ±2% | 5 | Annual | NIST |
| **Insulation Tester** | 50V-5kV, 200GΩ | 5 | Annual | NIST |
| **Programmable Load Bank** | 0-200 kVA, PF 0.8-1.0 | 2 | Annual | NIST |
| **Current Clamp** | 1-3000A AC/DC, ±1% | 10 | Annual | NIST |
| **EMC Test Equipment** | Per MIL-STD-461 | 1 set | Annual | NIST |

### 5.3 Mechanical Testing Equipment

| Equipment | Specification | Quantity | Calibration | Traceability |
|-----------|---------------|----------|-------------|--------------|
| **Load Cells** | 0-50 ton, ±0.05% FS | 10 | Semi-annual | NIST |
| **Torque Transducer** | 0-10,000 Nm, ±0.1% | 5 | Annual | NIST |
| **Displacement Sensors** | LVDT, ±0.01 mm | 20 | Annual | NIST |
| **Strain Gauges** | 350Ω, gauge factor 2.0±1% | 100 | Pre-use check | Manufacturer |
| **Accelerometers** | Piezoelectric, 10-5000 Hz | 10 | Bi-annual | NIST |
| **Vibration Shaker** | 20 kN, 5-2000 Hz | 1 | Annual | Manufacturer |
| **Pressure Gauges** | 0-1000 bar, ±0.25% | 20 | Annual | NIST |

### 5.4 Data Acquisition Systems

| System Component | Specification | Quantity | Calibration |
|------------------|---------------|----------|-------------|
| **DAQ Chassis** | 8-slot, PXI/PXIe | 5 | Annual |
| **Analog Input Module** | 16-ch, 24-bit, 100 kS/s | 20 | Annual |
| **Digital I/O Module** | 32-ch, isolated | 10 | Annual |
| **Thermocouple Module** | 32-ch, CJC, ±0.5°C | 10 | Annual |
| **Strain Gauge Module** | 8-ch, quarter/half/full bridge | 5 | Annual |
| **High-Speed DAQ** | 100 kHz/ch, 16-bit | 2 | Annual |
| **Data Server** | Redundant storage, RAID | 2 | N/A |

### 5.5 Calibration and Traceability

**Calibration Requirements:**

- All measurement equipment calibrated before use
- Calibration traceable to NIST or national metrology institute
- Calibration certificates maintained in test records
- Out-of-tolerance equipment immediately removed from service
- Calibration recall system to prevent use of expired calibrations

**Calibration Schedule:**

| Frequency | Equipment Type | Method |
|-----------|----------------|--------|
| Pre-use | One-time use sensors (strain gauges) | Factory calibration certificate |
| Quarterly | H₂ purity analyzers | Certified gas standards |
| Semi-annual | Cryogenic sensors, load cells | External calibration lab |
| Annual | Most electrical and mechanical instruments | External calibration lab |
| Bi-annual | Oscilloscopes, high-accuracy equipment | External calibration lab |

## 6. Personnel Resources

### 6.1 Personnel Requirements

| Role | Quantity | Key Qualifications | Certifications Required |
|------|----------|-------------------|------------------------|
| **Test Manager** | 1 | Engineering degree, 10+ years GSE experience | PMP (preferred) |
| **Lead Test Engineer** | 2 | Engineering degree, 5+ years test experience | Engineering license |
| **H₂ Test Engineer** | 3 | Engineering degree, H₂ systems knowledge | H₂ safety certification |
| **Electrical Test Engineer** | 3 | Electrical engineering degree | EMC certification (if performing EMC tests) |
| **Mechanical Test Engineer** | 3 | Mechanical engineering degree | NDT Level II (at least 1) |
| **Test Technicians** | 10 | Technical diploma, 2+ years experience | Relevant technical certifications |
| **Safety Officer** | 2 | Safety engineering background | CSP, H₂ safety certification |
| **Quality Inspector** | 2 | Quality engineering background | ASQ CQE or CQI |
| **Data Analyst** | 2 | Engineering/statistics degree | Data analysis software proficiency |

### 6.2 Training Requirements

**Mandatory Training for All Personnel:**

- GSE overview and safety
- Test facility safety procedures
- Emergency response procedures
- Data handling and security
- Quality management system

**Role-Specific Training:**

| Role | Additional Training |
|------|-------------------|
| **H₂ Test Personnel** | Hydrogen safety (8 hours), Cryogenic systems (4 hours), ATEX awareness (4 hours) |
| **Electrical Test Personnel** | High-voltage safety (4 hours), EMC fundamentals (if applicable, 8 hours) |
| **Mechanical Test Personnel** | Structural test safety (4 hours), NDT procedures (if applicable, 40+ hours) |
| **Safety Officers** | H₂ incident response (16 hours), First aid/CPR (8 hours), HAZMAT awareness (8 hours) |

### 6.3 Personnel Certification Tracking

- Training and certification records maintained for all personnel
- Expiration tracking system with automatic alerts
- Retraining scheduled before certification expiration
- Competency assessments documented

## 7. Support Resources

### 7.1 Utilities

| Utility | Specification | Purpose |
|---------|---------------|---------|
| **Electrical Power** | 3-phase 400V, 500 kVA | Test equipment, GSE operation |
| **Compressed Air** | 7 bar, oil-free, -40°C dewpoint | Pneumatic systems, purging |
| **Nitrogen** | GN₂, 99.9% purity, 200 bar | Purging, inerting |
| **Helium** | 99.999% purity (for leak testing) | Leak detection |
| **Water** | Potable, 4 bar | Cooling, safety showers |
| **HVAC** | Temperature/humidity control | Environmental control |

### 7.2 Safety Equipment

| Equipment | Specification | Quantity | Location |
|-----------|---------------|----------|----------|
| **H₂ Detectors (portable)** | 0-1000 ppm, alarm at 25% LEL | 10 | H₂ test areas |
| **O₂ Monitors** | 0-25%, alarm <19.5% | 10 | Confined spaces, H₂ areas |
| **Fire Extinguishers** | Class D (for metal fires), BC | 20 | Per fire code |
| **Emergency Eyewash/Shower** | ANSI Z358.1 compliant | 5 | All test areas |
| **Cryogenic PPE** | Face shield, gloves, apron | 20 sets | Cryogenic areas |
| **First Aid Kits** | Industrial, ANSI Type III | 5 | All test areas |
| **Emergency Stop Buttons** | Hardwired, redundant | As needed | Throughout test areas |
| **Spill Containment** | Appropriate for all fluids used | As needed | Storage areas |

### 7.3 Logistics Support

- **Parts and Consumables**: Stock of common replacement parts, sensors, consumables
- **Transportation**: Capability to transport GSE and test equipment
- **Storage**: Secure storage for GSE, test equipment, and test articles
- **Waste Disposal**: Contracts for hazardous waste disposal (H₂ venting, cryogenic fluids, etc.)
- **Documentation**: Document management system for test records and reports

## 8. Resource Scheduling and Allocation

### 8.1 Scheduling Process

1. **Test Planning**: Identify resource requirements in test procedures
2. **Resource Check**: Verify availability of facilities, equipment, personnel
3. **Reservation**: Reserve resources through central scheduling system
4. **Confirmation**: Confirm reservation 2 weeks prior to test
5. **Pre-Test Check**: Verify resource readiness 1 day before test
6. **Post-Test**: Release resources, note any issues for maintenance

### 8.2 Resource Conflicts

- Central scheduling system to prevent double-booking
- Priority system for resource allocation (certification tests highest priority)
- Escalation process for unresolved conflicts
- Advance notice (4 weeks minimum) for major test activities

### 8.3 Resource Maintenance

| Resource Type | Maintenance Schedule | Responsible Party |
|---------------|---------------------|-------------------|
| **Test Facilities** | Per facility maintenance plan | Facility manager |
| **Test Equipment** | Per equipment maintenance plan + calibration schedule | Equipment custodian |
| **Safety Equipment** | Monthly inspection, annual certification | Safety officer |
| **Data Systems** | Daily backup, quarterly validation | IT support |

## 9. Acceptance Criteria

Test resources are acceptable when:

- ✅ Facilities hold required certifications (ISO 17025, ATEX, etc.)
- ✅ Equipment calibrated and within specification
- ✅ Personnel trained and certified per requirements
- ✅ Safety equipment inspected and functional
- ✅ Resource availability confirmed for test schedule
- ✅ Utilities available and meet specifications

## 10. Safety Considerations

- All resources must meet applicable safety standards
- H₂ testing resources must be ATEX certified
- Personnel must complete required safety training before testing
- Safety equipment must be inspected and functional
- Emergency response procedures must be in place and tested
- Insurance coverage must be appropriate for testing activities

## 11. Cross-References

### 11.1 Related Documents

- Parent Document: [03-00-07_V_AND_V](../)
- Verification Strategy: [03-00-07-01-01A_GSE_Verification_Strategy.md](./03-00-07-01-01A_GSE_Verification_Strategy.md)
- Test Plan: [03-00-07-01-02A_GSE_Test_Plan.md](./03-00-07-01-02A_GSE_Test_Plan.md)
- Verification Matrix: [03-00-07-01-03A_GSE_Verification_Matrix.md](./03-00-07-01-03A_GSE_Verification_Matrix.md)

### 11.2 External Standards

- [ISO 17025](https://www.iso.org/standard/66912.html) — Laboratory accreditation
- [NIST Handbook 150](https://www.nist.gov/topics/laboratory-accreditation/nist-handbook-150) — Calibration
- [ATEX Directive 2014/34/EU](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0034) — Explosive atmospheres

## 12. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 GSE V&V Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-07-01-04A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Verification & Validation Team

---
