# 85-00-11-005: H₂, CO₂, and GSE EIS Packages

## Purpose

This document defines **aggregated EIS packages** for specific infrastructure subsystems:
- **Hydrogen (H₂) refuelling systems**
- **CO₂ battery ground infrastructure**
- **Ground Support Equipment (GSE) power and data interface packs**

These packages can be deployed independently or combined based on airport archetype and aircraft configuration requirements.

---

## Scope

### In Scope

- H₂ refuelling interface packages (pressure levels, flow rates, connectors)
- CO₂ battery charging interface packages (power levels, connector types, cooling systems)
- GSE power/data interface packages (electrical, data protocols, automation levels)
- Safety and certification requirements per subsystem
- Compatibility matrices across subsystems

### Out of Scope

- Aircraft-side systems (covered in respective ATA chapters)
- Detailed ground infrastructure design (covered in [85-00-04_Design](../85-00-04_Design/README.md))
- Operational procedures (covered in [85-00-12_Services](../85-00-12_Services/README.md))

---

## H₂ Refuelling EIS Packages

### PKG-85-H2-001: Standard H₂ Refuelling (350 bar)

**Baseline**: `BL-85-00-11-010`  
**Configuration**: 350 bar gaseous hydrogen refuelling

**Technical Specifications**:
- **Pressure**: 350 bar (nominal)
- **Flow Rate**: 500 kg/h (Archetype A), 250 kg/h (Archetype B), 100 kg/h (Archetype C)
- **Connector**: SAE J2601 compatible (or aviation-specific variant)
- **Purity**: 99.97% minimum (ISO 14687:2019 Grade D)
- **Temperature**: -40°C to +85°C ambient operating range

**Safety Requirements**:
- Compliance with [ISO 19880-1](https://www.iso.org/standard/71940.html) (Gaseous hydrogen fuelling stations)
- Leak detection systems (< 1% LEL sensitivity)
- Emergency shutdown systems (< 2 seconds response time)
- Grounding and bonding per aviation electrical safety standards

**Certification**:
- EASA/FAA approval per [85-00-10_Certification](../85-00-10_Certification/README.md)
- Local fire authority approval
- Compliance with [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (Equipment, systems, and installations)

**Compatibility**:
- Aircraft variants: All H₂-powered BWB variants
- Airport archetypes: A, B, C (with flow rate variations)

---

### PKG-85-H2-002: High-Pressure H₂ Refuelling (700 bar)

**Baseline**: `BL-85-00-11-011`  
**Configuration**: 700 bar gaseous hydrogen refuelling (for extended-range aircraft)

**Technical Specifications**:
- **Pressure**: 700 bar (nominal)
- **Flow Rate**: 500 kg/h (Archetype A), 250 kg/h (Archetype B)
- **Connector**: SAE J2601 Type B3 or aviation-specific
- **Purity**: 99.97% minimum (ISO 14687:2019 Grade D)
- **Pre-cooling**: Required (-40°C target temperature)

**Safety Requirements**: Enhanced beyond PKG-85-H2-001 for higher pressure
- Burst pressure: > 1,500 bar
- Enhanced leak detection and containment
- Automated refuelling with reduced human intervention

**Certification**: As per PKG-85-H2-001, with additional pressure vessel certifications

**Compatibility**:
- Aircraft variants: Extended-range BWB variants only
- Airport archetypes: A, B (not suitable for Archetype C due to infrastructure complexity)

---

### PKG-85-H2-003: Liquid H₂ Refuelling (Future)

**Baseline**: `BL-85-00-11-012` (PLANNED)  
**Configuration**: Liquid hydrogen refuelling (for ultra-long-range aircraft, future capability)

**Status**: **PLANNED** (not currently available; requires future technology maturation)

**Technical Specifications** (Preliminary):
- **Temperature**: -253°C (20 K)
- **Flow Rate**: TBD based on aircraft requirements
- **Connector**: Vacuum-insulated transfer line (aviation-specific)
- **Purity**: 99.99% minimum

**Safety Requirements**: Cryogenic safety per [CGA P-12](https://www.cganet.com/) (Safe Handling of Cryogenic Liquids)

**Compatibility**: Future BWB variants with liquid H₂ tanks

---

## CO₂ Battery Charging EIS Packages

### PKG-85-CO2-001: Standard CO₂ Battery Charging (350 kW)

**Baseline**: `BL-85-00-11-020`  
**Configuration**: DC fast charging for CO₂ battery ground infrastructure

**Technical Specifications**:
- **Charging Power**: 350 kW (nominal), 400 kW (peak)
- **Voltage Range**: 200-800 VDC
- **Connector**: CCS2 (Combined Charging System) or aviation-specific variant
- **Charging Protocol**: ISO 15118 (Vehicle-to-Grid communication)
- **Cooling**: Active liquid cooling (if required by battery system)

**Safety Requirements**:
- Compliance with [IEC 62368-1](https://webstore.iec.ch/publication/6793) (Safety requirements for electrical equipment)
- Ground fault detection: < 30 mA leakage current
- Insulation resistance: > 500 MΩ
- Emergency disconnect: < 1 second response time

**Certification**:
- EASA/FAA approval per [85-00-10_Certification](../85-00-10_Certification/README.md)
- Electrical safety certifications per local regulations
- Compliance with CS-25 electrical system requirements

**Compatibility**:
- Aircraft variants: BWB variants equipped with CO₂ battery systems
- Airport archetypes: A, B (Archetype C typically does not have CO₂ battery infrastructure)

---

### PKG-85-CO2-002: High-Power CO₂ Battery Charging (800 kW)

**Baseline**: `BL-85-00-11-021`  
**Configuration**: Ultra-fast charging for large CO₂ battery packs

**Technical Specifications**:
- **Charging Power**: 800 kW (nominal), 1,000 kW (peak)
- **Voltage Range**: 400-1,000 VDC
- **Connector**: Aviation-specific high-power connector
- **Charging Protocol**: ISO 15118 with extensions for aviation
- **Cooling**: Mandatory active liquid cooling

**Safety Requirements**: Enhanced beyond PKG-85-CO2-001 for higher power
- Arc flash protection
- Thermal runaway detection and mitigation

**Certification**: As per PKG-85-CO2-001, with additional high-power electrical certifications

**Compatibility**:
- Aircraft variants: Large BWB variants with extended-range CO₂ battery systems
- Airport archetypes: A only (due to infrastructure complexity and cost)

---

## GSE Power and Data EIS Packages

### PKG-85-GSE-001: Standard GSE Power and Data

**Baseline**: `BL-85-00-11-030`  
**Configuration**: 400 Hz AC power + Ethernet data

**Technical Specifications**:
- **AC Power**:
  - Frequency: 400 Hz
  - Voltage: 115V AC (3-phase)
  - Current: 400A per aircraft (Archetype A), 200A (Archetype B), 100A (Archetype C)
  - Connector: MIL-STD-704 compatible
- **Data**:
  - Ethernet: 1000BASE-T (Archetype A/B), 100BASE-T (Archetype C)
  - Redundancy: Dual links (Archetype A), single link (Archetype B/C)
  - Protocols: TCP/IP, SNMP, custom aircraft protocols

**Safety Requirements**:
- Ground fault protection
- Over-current protection
- Data encryption (TLS 1.3 minimum)

**Certification**: EASA/FAA approval per [85-00-10_Certification](../85-00-10_Certification/README.md)

**Compatibility**:
- Aircraft variants: All BWB variants
- Airport archetypes: A, B, C (with power/data capacity variations)

---

### PKG-85-GSE-002: Advanced GSE with Automation

**Baseline**: `BL-85-00-11-031`  
**Configuration**: Automated connection/disconnection, advanced data protocols

**Technical Specifications**: As per PKG-85-GSE-001, plus:
- **Automation**:
  - Robotic connector alignment and mating
  - Automated power sequencing and health checks
  - Predictive maintenance via [ATA 92 Model-Based Maintenance](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/ATA_92-MODEL_BASED_MAINTENANCE/README.md)
- **Advanced Data**:
  - 10GBASE-T Ethernet (Archetype A)
  - ARINC 429 backward compatibility
  - Real-time monitoring and diagnostics

**Safety Requirements**: Enhanced automation safety (fail-safe design, redundant sensors)

**Certification**: As per PKG-85-GSE-001, with additional automation safety certifications

**Compatibility**:
- Aircraft variants: All BWB variants
- Airport archetypes: A (full automation), B (partial automation)

---

## Integrated EIS Packages

### PKG-85-INTEGRATED-001: Full Infrastructure Package (Archetype A)

**Baseline**: `BL-85-00-11-040`  
**Configuration**: H₂ (350 bar or 700 bar) + CO₂ battery (350 kW) + Advanced GSE

**Components**:
- PKG-85-H2-001 or PKG-85-H2-002
- PKG-85-CO2-001
- PKG-85-GSE-002

**Use Case**: Large international hubs with full infrastructure support

---

### PKG-85-INTEGRATED-002: H₂-Only Package (Archetype B)

**Baseline**: `BL-85-00-11-041`  
**Configuration**: H₂ (350 bar) + Standard GSE (no CO₂ battery)

**Components**:
- PKG-85-H2-001
- PKG-85-GSE-001

**Use Case**: Medium regional hubs without CO₂ battery infrastructure

---

### PKG-85-INTEGRATED-003: Minimal Package (Archetype C)

**Baseline**: `BL-85-00-11-042`  
**Configuration**: H₂ (350 bar, reduced flow) + Minimal GSE

**Components**:
- PKG-85-H2-001 (reduced flow rate)
- PKG-85-GSE-001 (minimal capacity)

**Use Case**: Small regional airports with limited infrastructure

---

## Compatibility Matrix

| Aircraft Variant | H₂ Package | CO₂ Package | GSE Package | Airport Archetype |
|------------------|------------|-------------|-------------|-------------------|
| BWB-H2-STD | PKG-85-H2-001 | - | PKG-85-GSE-001 | A, B, C |
| BWB-H2-CO2 | PKG-85-H2-001 | PKG-85-CO2-001 | PKG-85-GSE-001 | A, B |
| BWB-H2-EXTENDED | PKG-85-H2-002 | PKG-85-CO2-002 | PKG-85-GSE-002 | A |

---

## References

- [ISO 19880-1 – Gaseous hydrogen — Fuelling stations — Part 1: General requirements](https://www.iso.org/standard/71940.html)
- [ISO 14687:2019 – Hydrogen fuel quality — Product specification](https://www.iso.org/standard/69539.html)
- [IEC 62368-1 – Audio/video, information and communication technology equipment – Safety requirements](https://webstore.iec.ch/publication/6793)
- [ISO 15118 – Road vehicles — Vehicle to grid communication interface](https://www.iso.org/standard/55366.html)
- [SAE J2601 – Fueling Protocols for Light Duty Gaseous Hydrogen Surface Vehicles](https://www.sae.org/standards/content/j2601_201612/)
- [MIL-STD-704 – Aircraft Electric Power Characteristics](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35789)
- [CS-25.1309 – Equipment, systems, and installations](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- [85-00-04_Design](../85-00-04_Design/README.md)
- [85-00-10_Certification](../85-00-10_Certification/README.md)
- [85-00-11-004_Airport_Archetype_EIS_Packages.md](./85-00-11-004_Airport_Archetype_EIS_Packages.md)
- [85-00-12_Services](../85-00-12_Services/README.md)
- [ATA 92 – Model-Based Maintenance](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/ATA_92-MODEL_BASED_MAINTENANCE/README.md)

---

## Document Control

- **Standard**: OPT-IN Framework v1.1 (A-LIVE-GP, ATA 85 pattern)
- **Document ID**: 85-00-11-005
- **Version**: 1.0 (DRAFT)
- **Last Updated**: 2025-11-21
- **Next Review**: 2026-02-21
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.
