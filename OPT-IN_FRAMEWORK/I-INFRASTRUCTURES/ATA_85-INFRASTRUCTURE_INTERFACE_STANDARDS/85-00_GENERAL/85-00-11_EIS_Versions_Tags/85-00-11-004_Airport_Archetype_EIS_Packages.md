# 85-00-11-004: Airport Archetype EIS Packages

## Purpose

This document defines the **EIS package structure** for different **airport archetypes**, specifying minimum infrastructure requirements, configuration variants, and readiness criteria for BWB aircraft operations at each archetype level.

---

## Scope

### In Scope

- Definition of airport archetypes (A, B, C, etc.)
- Minimum infrastructure requirements per archetype
- Configuration variants (H₂ only, H₂ + CO₂, etc.)
- EIS readiness criteria and validation checklists
- Dependencies on regional regulations and standards

### Out of Scope

- Detailed infrastructure design (covered in [85-00-04_Design](../85-00-04_Design/README.md))
- Operational procedures (covered in [85-00-12_Services](../85-00-12_Services/README.md))
- Certification processes (covered in [85-00-10_Certification](../85-00-10_Certification/README.md))

---

## Airport Archetype Classification

### Archetype A: Large International Hubs

**Characteristics**:
- **Passenger Volume**: > 50M PAX/year
- **H₂ Infrastructure**: Centralized production/storage (on-site electrolysis or pipeline)
- **CO₂ Battery Infrastructure**: Available (if applicable to aircraft variant)
- **GSE Automation Level**: High (automated refuelling, power, data)
- **PAX Boarding**: Advanced multi-aisle jetways, automated boarding gates

**Example Airports**: FRA (Frankfurt), AMS (Amsterdam), LHR (London Heathrow), LAX (Los Angeles), DXB (Dubai)

**EIS Priority**: **HIGH** (Phase 1-2 focus per [85-00-11-001](./85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md))

---

### Archetype B: Medium Regional Hubs

**Characteristics**:
- **Passenger Volume**: 10-50M PAX/year
- **H₂ Infrastructure**: Distributed (on-site production or trucked-in supply)
- **CO₂ Battery Infrastructure**: Optional
- **GSE Automation Level**: Moderate (semi-automated)
- **PAX Boarding**: Standard dual-aisle jetways

**Example Airports**: MUC (Munich), BCN (Barcelona), ORD (Chicago O'Hare), SIN (Singapore)

**EIS Priority**: **MEDIUM** (Phase 3 focus)

---

### Archetype C: Small Regional Airports

**Characteristics**:
- **Passenger Volume**: < 10M PAX/year
- **H₂ Infrastructure**: Minimal (trucked-in, limited capacity)
- **CO₂ Battery Infrastructure**: Not available
- **GSE Automation Level**: Low (manual operations)
- **PAX Boarding**: Basic jetways or ground boarding

**Example Airports**: Regional airports in Europe, North America, Asia

**EIS Priority**: **LOW** (Phase 4 and beyond)

---

## EIS Package Structure

### Package Naming Convention

```
PKG-85-ARCH-{X}-{YYY}
```

**Components**:
- **PKG**: Package identifier
- **85**: ATA chapter
- **ARCH**: Archetype indicator
- **{X}**: Archetype level (A, B, C)
- **{YYY}**: Sequential package number

**Examples**:
- `PKG-85-ARCH-A-001`: Archetype A, H₂ standard configuration
- `PKG-85-ARCH-A-002`: Archetype A, H₂ + CO₂ battery configuration
- `PKG-85-ARCH-B-001`: Archetype B, H₂ standard configuration

---

## Package Content

Each EIS package MUST include:

1. **Baseline Reference**
   - Link to configuration baseline (per [85-00-11-003](./85-00-11-003_Interface_Configuration_Baselines.md))
   - Example: `BL-85-00-11-004`

2. **Archetype Specification**
   - Airport category (A, B, or C)
   - Minimum infrastructure requirements
   - Optional infrastructure features

3. **Configuration Variant**
   - H₂ only
   - H₂ + CO₂ battery
   - H₂ + advanced GSE automation

4. **Installation Procedures**
   - Infrastructure setup and validation steps
   - Interface connection procedures
   - Safety checks and interlocks

5. **Readiness Checklist**
   - Per [85-00-11-A-202_EIS_Readiness_Checklist.xlsx](./ASSETS/EIS_Packages/85-00-11-A-202_EIS_Readiness_Checklist.xlsx)
   - Covers infrastructure, documentation, training, regulatory approvals

6. **Training Materials**
   - Ground crew training modules
   - Maintenance personnel training
   - Emergency procedures training

7. **Rollback Plan**
   - Per [85-00-11-A-203_Reversibility_Rollback_Plan_Template.md](./ASSETS/EIS_Packages/85-00-11-A-203_Reversibility_Rollback_Plan_Template.md)
   - Contingency procedures if EIS deployment fails validation

---

## Archetype A EIS Packages

### PKG-85-ARCH-A-001: H₂ Standard Configuration

**Baseline**: `BL-85-00-11-004`  
**Configuration**: H₂ refuelling (standard rate), GSE power/data (automated), PAX boarding (triple-aisle jetways)

**Minimum Infrastructure Requirements**:
- **H₂ Refuelling**:
  - Refuelling rate: 500 kg/h minimum
  - Storage capacity: 10,000 kg on-site
  - Pressure: 350 bar or 700 bar (per aircraft variant)
  - Safety: Compliance with [ISO 19880-1](https://www.iso.org/standard/71940.html) (Gaseous hydrogen — Fuelling stations)
- **GSE Power**:
  - 400 Hz AC power, 115V, 400A per aircraft
  - Automated connection/disconnection
- **GSE Data**:
  - Ethernet 1000BASE-T, redundant links
  - ARINC 429 compatibility (legacy systems)
- **PAX Boarding**:
  - Triple-aisle jetways (compatible with BWB cabin layout)
  - Automated door alignment systems

**Readiness Criteria**:
- [ ] Infrastructure installed and commissioned
- [ ] Passed [85-00-07_V_AND_V](../85-00-07_V_AND_V/README.md) validation tests
- [ ] Ground crew trained and certified
- [ ] Regulatory approval obtained (EASA/FAA/local authority)
- [ ] Emergency procedures in place and drilled

---

### PKG-85-ARCH-A-002: H₂ + CO₂ Battery Configuration

**Baseline**: `BL-85-00-11-006`  
**Configuration**: H₂ refuelling + CO₂ battery charging, GSE power/data (automated), PAX boarding (triple-aisle jetways)

**Additional Requirements** (beyond PKG-85-ARCH-A-001):
- **CO₂ Battery Charging**:
  - DC fast charging: 350 kW minimum
  - Charging connector: CCS2 or aviation-specific variant
  - Safety: Compliance with [IEC 62368-1](https://webstore.iec.ch/publication/6793) and aviation extensions
- **Cooling Systems**:
  - Active cooling for battery charging (if required)

**Readiness Criteria**: Same as PKG-85-ARCH-A-001, plus:
- [ ] CO₂ battery charging infrastructure validated
- [ ] Electrical safety certifications obtained

---

## Archetype B EIS Packages

### PKG-85-ARCH-B-001: H₂ Standard Configuration

**Baseline**: `BL-85-00-11-005`  
**Configuration**: H₂ refuelling (reduced rate), GSE power/data (semi-automated), PAX boarding (dual-aisle jetways)

**Minimum Infrastructure Requirements**:
- **H₂ Refuelling**:
  - Refuelling rate: 250 kg/h minimum
  - Storage capacity: 5,000 kg on-site or trucked-in
  - Pressure: 350 bar or 700 bar
- **GSE Power**:
  - 400 Hz AC power, 115V, 200A per aircraft (reduced capacity)
  - Semi-automated or manual connection
- **GSE Data**:
  - Ethernet 100BASE-T minimum
- **PAX Boarding**:
  - Dual-aisle jetways (standard commercial)

**Readiness Criteria**: Similar to Archetype A, with reduced infrastructure requirements

---

## Archetype C EIS Packages

### PKG-85-ARCH-C-001: H₂ Minimal Configuration

**Baseline**: `BL-85-00-11-007`  
**Configuration**: H₂ refuelling (minimal rate), GSE power/data (manual), PAX boarding (basic jetways or ground boarding)

**Minimum Infrastructure Requirements**:
- **H₂ Refuelling**:
  - Refuelling rate: 100 kg/h minimum
  - Storage: Trucked-in supply, minimal on-site storage
  - Pressure: 350 bar
- **GSE Power**:
  - 400 Hz AC power, 115V, 100A per aircraft (minimal capacity)
  - Manual connection only
- **GSE Data**:
  - Basic Ethernet or legacy systems
- **PAX Boarding**:
  - Single jetway or ground boarding (bus + stairs)

**Readiness Criteria**: Minimal validation, suitable for low-frequency operations

---

## Regional Variants

### European Variant

- Compliance with [EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- Additional safety requirements per EU regulations
- Integration with EU DPP Regulation

### North American Variant

- Compliance with [FAA FAR-25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25)
- TSA security considerations for ground infrastructure
- Integration with US DOT data reporting

### Asia-Pacific Variant

- Compliance with CAAC (China), CASA (Australia), etc.
- Regional H₂ infrastructure standards (e.g., Japanese hydrogen strategy)

---

## EIS Package Lifecycle

1. **Development**: Baseline + archetype-specific adaptations
2. **Validation**: Per [85-00-07_V_AND_V](../85-00-07_V_AND_V/README.md)
3. **Approval**: CCB + regulatory authorities
4. **Deployment**: Per [85-00-11-001](./85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md)
5. **Monitoring**: Post-EIS field data collection per [85-00-11-A-303_Field_Feedback_Summary_Template.md](./ASSETS/Reports/85-00-11-A-303_Field_Feedback_Summary_Template.md)
6. **Refinement**: Iterative improvements based on operational experience

---

## References

- [ISO 19880-1 – Gaseous hydrogen — Fuelling stations — Part 1: General requirements](https://www.iso.org/standard/71940.html)
- [IEC 62368-1 – Audio/video, information and communication technology equipment – Safety requirements](https://webstore.iec.ch/publication/6793)
- [EASA CS-25 – Certification Specifications for Large Aeroplanes](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [FAA FAR-25 – Airworthiness Standards: Transport Category Airplanes](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25)
- [85-00-04_Design](../85-00-04_Design/README.md)
- [85-00-07_V_AND_V](../85-00-07_V_AND_V/README.md)
- [85-00-10_Certification](../85-00-10_Certification/README.md)
- [85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md](./85-00-11-001_EIS_Strategy_Infrastructure_Interfaces.md)
- [85-00-11-003_Interface_Configuration_Baselines.md](./85-00-11-003_Interface_Configuration_Baselines.md)
- [85-00-12_Services](../85-00-12_Services/README.md)

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (A-LIVE-GP, ATA 85 pattern)
- **Document ID**: 85-00-11-004
- **Version**: 1.0 (DRAFT)
- **Last Updated**: 2025-11-21
- **Next Review**: 2026-02-21
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.
