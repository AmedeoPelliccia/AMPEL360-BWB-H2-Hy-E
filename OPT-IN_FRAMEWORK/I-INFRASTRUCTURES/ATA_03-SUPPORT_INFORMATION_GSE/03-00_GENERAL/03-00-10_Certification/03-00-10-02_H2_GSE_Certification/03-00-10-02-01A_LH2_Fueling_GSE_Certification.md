---
Title: "LH2 Fueling GSE Certification — ATA 03 Support Information GSE"
Identifier: "AMPEL360-03-00-10-02-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Certification requirements and evidence for liquid hydrogen (LH2) fueling Ground Support Equipment."
Keywords: ["ATA 03","GSE","LH2","Hydrogen","Fueling","Certification"]
Compliance:
  - "SAE AS6968"
  - "ISO 19880-8"
  - "IEC 60079"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentH2: "./"
  Siblings:
    - "03-00-10-02-02A_Cryogenic_GSE_Approval.md"
    - "03-00-10-02-03A_H2_Safety_GSE_Certification.md"
    - "03-00-10-02-04A_H2_GSE_Special_Conditions.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial LH2 fueling GSE certification document" }
---

# 03-00-10-02-01A - LH2 Fueling GSE Certification

## 1. Purpose

This document defines the **certification requirements and process** for Liquid Hydrogen (LH2) fueling Ground Support Equipment (GSE) used to refuel the AMPEL360 BWB H₂ Hy-E aircraft. It addresses the unique challenges of cryogenic hydrogen handling at -253°C and ensures safe, reliable fueling operations.

## 2. Scope

### 2.1 Covered Equipment

- LH2 fuel trucks and mobile refuelers
- LH2 hydrant fueling systems
- Cryogenic fuel hoses and connectors
- Pressure management systems
- Leak detection and safety systems
- Control and monitoring systems

### 2.2 Out of Scope

- Aircraft fuel system (covered under ATA 28)
- Hydrogen production and storage facilities (airport infrastructure)
- Ground crew training (covered in operational approval)

## 3. Applicable Documents

| Standard | Title | Applicability |
|----------|-------|---------------|
| **[SAE AS6968](https://www.sae.org/standards/content/as6968/)** | Hydrogen Aircraft Refueling | Primary design and operational standard |
| **[ISO 19880-8](https://www.iso.org/standard/71940.html)** | Gaseous hydrogen fueling stations | Safety and purity requirements |
| **[IEC 60079](https://webstore.iec.ch/publication/632)** | Explosive atmospheres (ATEX) | Electrical system design in H2 zones |
| **[SAE J2719](https://www.sae.org/standards/content/j2719/)** | Hydrogen fuel quality | Fuel purity specifications |
| **[ASME BPVC](https://www.asme.org/codes-standards/find-codes-standards/bpvc-section-viii)** | Boiler and Pressure Vessel Code | Pressure vessel design and certification |
| **[UN TPED](https://unece.org/transportdangerous-goods)** | Transport of Dangerous Goods | Portable pressure equipment |

## 4. Certification Requirements

### 4.1 Overview

LH2 fueling GSE certification requires demonstration of:

1. **Design compliance** with SAE AS6968 and ISO 19880-8
2. **Safety assurance** through hazard analysis and testing
3. **Operational suitability** via trials and validation
4. **Material compatibility** with cryogenic hydrogen
5. **ATEX compliance** for explosive atmosphere protection

### 4.2 Regulatory Basis

**SAE AS6968 Requirements**:

| Section | Requirement | Compliance Method |
|---------|-------------|-------------------|
| 4.1 | Safety philosophy (fail-safe design) | Design review, FMEA |
| 4.2.1 | Cryogenic containment | Thermal analysis, insulation testing |
| 4.2.2 | Pressure management | Pressure testing, relief valve verification |
| 4.2.3 | Leak detection | Sensitivity testing (10 ppm H2) |
| 4.2.4 | Emergency shutdown | Functional testing, response time measurement |
| 4.3 | Material selection | Material testing, hydrogen embrittlement assessment |
| 4.4 | Fueling procedures | Procedure validation, operational trials |

**ISO 19880-8 Requirements**:

| Requirement | Specification | Verification |
|-------------|---------------|--------------|
| H2 purity | ≥ 99.97% per SAE J2719 | Gas chromatography analysis |
| Leak rate | < 10 ppm detection sensitivity | Calibrated leak testing |
| Pressure vessel | ASME BPVC Section VIII certified | Certificate review, inspection |
| Grounding | < 10Ω to aircraft | Resistance measurement |
| Interlocks | Fail-safe automatic shutdown | Functional testing |

### 4.3 Compliance Methods

| Requirement Category | Method | Evidence |
|----------------------|--------|----------|
| Design compliance | Analysis, review, similarity | Design reports, calculations, comparisons |
| Material compatibility | Testing, certification | Material test reports, certificates |
| Structural integrity | Pressure testing, NDT | Test reports, inspection records |
| Safety systems | Functional testing, FMEA | Test data, failure analysis |
| Operational suitability | Operational trials | Trial reports, operator feedback |

## 5. Certification Evidence

### 5.1 Design Evidence

**Required Documentation**:

- P&ID (Piping and Instrumentation Diagrams)
- Cryogenic system design specifications
- Material selection rationale and certifications
- Pressure vessel design calculations (ASME)
- Thermal insulation analysis
- Leak detection system specification
- ATEX zone classification drawings
- Electrical system design (intrinsically safe)

**Design Reviews**:

- Preliminary Design Review (PDR) at 30% design
- Critical Design Review (CDR) at 90% design
- Safety Design Review (SDR) before prototype build

### 5.2 Testing Evidence

**Type Testing Requirements**:

| Test | Standard | Acceptance Criteria | Evidence |
|------|----------|---------------------|----------|
| **Pressure test** | ASME BPVC | 1.5× design pressure, no leaks | Pressure test report |
| **Thermal performance** | SAE AS6968 | Boil-off < 2% per day | Thermal test data |
| **Leak detection** | ISO 19880-8 | 10 ppm H2 sensitivity | Calibration certificate |
| **Flow rate** | SAE AS6968 | Per aircraft requirement (TBD kg/min) | Flow measurement report |
| **Emergency shutdown** | SAE AS6968 | < 2 seconds response time | Functional test report |
| **Cryogenic cycling** | Internal spec | 1000 cycles without degradation | Fatigue test report |
| **ATEX certification** | IEC 60079 | Zone 1 equipment compliance | ATEX certificate |

**Interface Testing**:

- Compatibility with aircraft fuel receptacle
- Electrical bonding verification (< 10Ω)
- Pressure and flow control verification
- Data interface validation (if applicable)

### 5.3 Operational Evidence

**Operational Trials**:

- Minimum 50 successful fueling operations
- Includes normal, abnormal, and emergency scenarios
- Ground crew evaluation and feedback
- Performance data collection

**Operational Documentation**:

- Fueling procedures manual
- Emergency response procedures
- Pre-fueling inspection checklist
- Maintenance procedures
- Training materials

## 6. Safety Requirements

### 6.1 Hazard Analysis

**Identified Hazards** (from FHA):

| Hazard ID | Hazard | Severity | Probability Target | Mitigation |
|-----------|--------|----------|-------------------|------------|
| H2-F-01 | LH2 leak during fueling | Hazardous | < 10⁻⁵ | Leak detection, auto-shutdown, ventilation |
| H2-F-02 | Overpressure in fuel tank | Catastrophic | < 10⁻⁷ | Pressure relief, interlock, monitoring |
| H2-F-03 | Cryogenic burn to personnel | Major | < 10⁻⁵ | PPE, safety interlocks, training |
| H2-F-04 | Ignition source in H2 zone | Hazardous | < 10⁻⁵ | ATEX equipment, bonding, hot work permit |
| H2-F-05 | Fuel contamination | Major | < 10⁻⁵ | Purity monitoring, filter systems |

### 6.2 Safety Systems

**Mandatory Safety Features**:

- Automatic leak detection (10 ppm sensitivity)
- Automatic emergency shutdown on leak detection
- Overpressure protection (relief valves, burst discs)
- Deadman switch on fueling nozzle
- Aircraft-GSE electrical bonding
- Personnel safety interlocks
- Fire suppression system integration
- Emergency stop buttons (accessible from all sides)

### 6.3 ATEX Compliance

**Zone Classification**:

- **Zone 1**: Within 3m of fueling connection during operation
- **Zone 2**: 3-10m from fueling connection

**Equipment Requirements**:

- Electrical: Ex d IIC T1 (explosion-proof, hydrogen, 450°C max)
- Intrinsically safe circuits: Ex ia IIC T1
- Temperature monitoring: Non-sparking, certified for cryogenic service

## 7. Cross-References

### 7.1 Related ATA 03 Documents

- [03-00-10-02-02A_Cryogenic_GSE_Approval](./03-00-10-02-02A_Cryogenic_GSE_Approval.md) — Cryogenic GSE requirements
- [03-00-10-02-03A_H2_Safety_GSE_Certification](./03-00-10-02-03A_H2_Safety_GSE_Certification.md) — H2 safety systems
- [03-00-10-02-04A_H2_GSE_Special_Conditions](./03-00-10-02-04A_H2_GSE_Special_Conditions.md) — Special conditions
- [03-00-10-04_GSE_Safety_Certification](../03-00-10-04_GSE_Safety_Certification/) — Safety certification framework
- [03-00-10-06-03A_GSE_Test_Evidence](../03-00-10-06_GSE_Compliance_Documentation/03-00-10-06-03A_GSE_Test_Evidence.md) — Test evidence compilation

### 7.2 Cross-ATA References

- [ATA 28 — Fuel System](../../../ATA_28-FUEL_SYSTEM/) — Aircraft fuel system interface
- [ATA 02 — Operations Information](../../ATA_02-OPERATIONS_INFORMATION/) — Fueling procedures

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-10-02-01A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Certification Team

---
