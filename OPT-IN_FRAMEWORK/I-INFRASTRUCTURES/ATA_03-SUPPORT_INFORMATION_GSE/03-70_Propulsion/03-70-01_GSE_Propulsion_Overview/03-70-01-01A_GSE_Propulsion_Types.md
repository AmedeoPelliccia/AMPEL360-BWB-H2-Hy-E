---
Title: "GSE Propulsion Types — ATA 03-70"
Identifier: "AMPEL360-03-70-01-01A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-08"
ModifiedAt: "2025-12-08"
Abstract: "Classification and overview of propulsion system types for Ground Support Equipment (GSE) in AMPEL360 operations."
Keywords: ["ATA 03","GSE","Propulsion Types","H2 Fuel Cell","Electric","Hybrid","Ground Support"]
Compliance:
  - "ATA iSpec 2200"
  - "ISO 23273"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentSection: "../"
  RelatedATASections:
    - "../../03-30_ANCHORS/"
    - "../../03-50_Structures/"
    - "../../03-60_Storages/"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-08", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-70-01-01A - GSE Propulsion Types

## 1. Purpose

This document provides a comprehensive classification and overview of **propulsion system types** deployed in Ground Support Equipment (GSE) for the AMPEL360 BWB H₂ Hy-E aircraft operations. It establishes the framework for understanding different propulsion technologies, their applications, and strategic selection criteria.

## 2. Scope

### 2.1 Coverage

This document covers:
- Zero-emission propulsion systems (H₂ fuel cell, battery electric)
- Hybrid propulsion systems (H₂-electric, diesel-electric)
- Conventional propulsion systems (diesel, gasoline, LPG/CNG)
- Propulsion system selection criteria
- Performance characteristics and operational envelopes
- Integration requirements with GSE platforms

### 2.2 Exclusions

This document does **NOT** cover:
- Aircraft propulsion systems (see ATA 70-79 aircraft chapters)
- Stationary power generation equipment (see ATA 03-80 Energy)
- Non-propulsive GSE systems

## 3. Applicable Documents

- **[ATA iSpec 2200](https://www.ata.org/resources/specifications)** — Information Standards for Aviation Maintenance
- **[SAE J2601](https://www.sae.org/standards/content/j2601/)** — Hydrogen Fueling Protocol
- **[ISO 14687](https://www.iso.org/standard/69539.html)** — Hydrogen Fuel Quality
- **[ISO 23273](https://www.iso.org/standard/75154.html)** — Fuel Cell Road Vehicles Safety
- **[IEC 62282](https://webstore.iec.ch/publication/6751)** — Fuel Cell Technologies
- **[SAE J2578](https://www.sae.org/standards/content/j2578/)** — Fuel Cell Vehicle Safety
- **[UN ECE R100](https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-100-119)** — Electric Vehicle Safety
- **[NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2)** — Hydrogen Technologies Code

## 4. GSE Propulsion System Types

### 4.1 Zero-Emission Propulsion Systems

#### 4.1.1 Hydrogen Fuel Cell Propulsion

Proton Exchange Membrane (PEM) fuel cell systems converting H₂ into electrical energy for electric motor propulsion.

| **Parameter** | **Specification** | **Notes** |
|---------------|-------------------|-----------|
| **Technology** | PEM Fuel Cell + Electric Motor | Primary zero-emission solution |
| **Power Range** | 20 kW - 300 kW | Varies by GSE type |
| **Fuel** | Compressed H₂ (350-700 bar) or LH₂ | Site infrastructure dependent |
| **Efficiency** | 40-60% (system level) | Higher than conventional engines |
| **Emissions** | Water vapor only | True zero emissions |
| **Refueling Time** | 3-10 minutes | Comparable to diesel |
| **Typical Applications** | Tractors, pushback tugs, cargo loaders | Heavy-duty GSE |

**Key Advantages:**
- Zero local emissions
- Fast refueling
- High power density
- Quiet operation

**Key Challenges:**
- H₂ infrastructure requirements
- Higher capital costs
- Balance of Plant (BoP) complexity
- Cold-start performance in extreme conditions

#### 4.1.2 Battery Electric Propulsion

Pure battery electric systems with electric motors powered by lithium-ion or advanced battery packs.

| **Parameter** | **Specification** | **Notes** |
|---------------|-------------------|-----------|
| **Technology** | Li-ion Battery + Electric Motor | Mature technology |
| **Power Range** | 10 kW - 200 kW | Limited by battery weight |
| **Energy Storage** | 50-500 kWh | Application dependent |
| **Efficiency** | 70-90% (well-to-wheel) | Highest efficiency |
| **Emissions** | Zero (operational) | Grid-dependent overall footprint |
| **Charging Time** | 30 min - 8 hours | Depends on charger power |
| **Typical Applications** | Belt loaders, GPUs, light tractors | Light to medium-duty GSE |

**Key Advantages:**
- Proven technology
- Simple drivetrain
- Low maintenance
- Excellent for short-range operations

**Key Challenges:**
- Long charging times (standard charging)
- Battery weight vs. capacity trade-off
- Range limitations for heavy-duty applications
- Battery degradation over time

### 4.2 Hybrid Propulsion Systems

#### 4.2.1 H₂ Fuel Cell + Battery Hybrid

Combined fuel cell and battery system, allowing optimized energy management.

| **Parameter** | **Specification** | **Notes** |
|---------------|-------------------|-----------|
| **Primary Source** | H₂ Fuel Cell (30-100 kW) | Base load power |
| **Secondary Source** | Battery Pack (20-100 kWh) | Peak power and regeneration |
| **Control Strategy** | Power split / Series hybrid | Configurable |
| **Typical Applications** | Heavy-duty tractors, mobile GPUs | Extended range + high power |

**Key Advantages:**
- Extended range vs. pure battery
- Peak power capability
- Regenerative braking energy recovery
- Downsized fuel cell (lower cost)

#### 4.2.2 Diesel-Electric Hybrid

Diesel engine + electric motor/generator + battery storage (transition technology).

| **Parameter** | **Specification** | **Notes** |
|---------------|-------------------|-----------|
| **Primary Source** | Diesel Engine (50-200 kW) | Conventional ICE |
| **Secondary Source** | Battery Pack (10-50 kWh) | Electric-only mode capability |
| **Emissions** | Reduced vs. pure diesel | Step toward zero emissions |
| **Typical Applications** | Large tugs, cargo loaders | Bridge to zero-emission |

**Key Advantages:**
- Reduced fuel consumption (20-40%)
- Lower emissions than pure diesel
- Electric-only operation in sensitive zones
- Existing refueling infrastructure

**Key Challenges:**
- Still produces emissions
- Complexity of dual powertrain
- Maintenance of ICE + electric systems

### 4.3 Conventional Propulsion Systems

#### 4.3.1 Diesel Engine Systems

Traditional compression-ignition internal combustion engines.

| **Parameter** | **Specification** | **Notes** |
|---------------|-------------------|-----------|
| **Technology** | Diesel ICE | Legacy systems |
| **Power Range** | 30 kW - 400 kW | Wide application range |
| **Fuel** | Diesel (EN 590) | Widely available |
| **Emissions** | CO₂, NOx, PM | Regulated by emissions standards |
| **Typical Applications** | All GSE types | Phase-out planned |

**Status:** Actively being phased out in favor of zero-emission alternatives.

#### 4.3.2 Gasoline, LPG, CNG Systems

Alternative fossil fuel systems with lower emissions than diesel.

**Status:** Limited use; transitional technologies only.

## 5. GSE Propulsion Selection Criteria

### 5.1 Decision Matrix

| **Criterion** | **H₂ Fuel Cell** | **Battery Electric** | **H₂-Electric Hybrid** | **Diesel-Electric Hybrid** |
|---------------|------------------|----------------------|------------------------|----------------------------|
| **Zero Emissions** | ✅ Yes | ✅ Yes | ✅ Yes | ⚠️ Reduced |
| **Range / Endurance** | ✅ High | ⚠️ Limited | ✅ High | ✅ High |
| **Refuel/Recharge Time** | ✅ Fast (3-10 min) | ⚠️ Slow (30+ min) | ✅ Fast | ✅ Fast |
| **Infrastructure** | ⚠️ H₂ required | ✅ Grid power | ⚠️ H₂ required | ✅ Diesel available |
| **Capital Cost** | ⚠️ High | ✅ Moderate | ⚠️ High | ⚠️ Moderate |
| **Operating Cost** | ✅ Low (H₂ fuel) | ✅ Very Low | ✅ Low | ⚠️ Moderate (fuel) |
| **Maintenance** | ✅ Low | ✅ Very Low | ⚠️ Moderate | ⚠️ Moderate to High |
| **Proven Maturity** | ⚠️ Emerging | ✅ Mature | ⚠️ Emerging | ✅ Mature |

### 5.2 Application-Based Recommendations

#### Heavy-Duty GSE (Tractors, Pushback Tugs)
- **Primary Recommendation:** H₂ Fuel Cell or H₂-Electric Hybrid
- **Rationale:** High power requirements, extended operating hours, fast refueling needed

#### Medium-Duty GSE (Cargo Loaders, Belt Loaders)
- **Primary Recommendation:** Battery Electric or H₂ Fuel Cell (depending on range)
- **Rationale:** Moderate power, duty cycles suit battery charging windows

#### Light-Duty GSE (Ground Power Units, Light Service Vehicles)
- **Primary Recommendation:** Battery Electric
- **Rationale:** Lower power requirements, shorter operating cycles, simple charging infrastructure

## 6. Safety Requirements

| **Requirement** | **Standard** | **Implementation** |
|-----------------|--------------|---------------------|
| H₂ system safety | ISO 23273, SAE J2578 | Leak detection, ventilation, shutdown systems |
| High-voltage safety | UN ECE R100 | Isolation monitoring, HV interlock circuits |
| Battery safety | UN ECE R100 | Thermal management, BMS, crash protection |
| Emergency response | NFPA 2 | Site-specific emergency procedures |
| Operator training | Internal standard | Competency verification for each propulsion type |

## 7. Cross-References

- **Related ATA Chapters:**
  - ATA 03-30 — ANCHORS (physical mounting and interfaces)
  - ATA 03-50 — Structures (GSE structural integration)
  - ATA 03-60 — Storages (H₂ tanks, battery enclosures)
  - ATA 03-80 — Energy (charging, refueling infrastructure)

- **Parent Document:** [03-70_Propulsion](../)

- **Related Documents:**
  - [03-70-01-02A — GSE Propulsion Standards](./03-70-01-02A_GSE_Propulsion_Standards.md)
  - [03-70-01-04A — Zero Emission Strategy](./03-70-01-04A_Zero_Emission_Strategy.md)
  - [03-70-02 — H2 Fuel Cell Propulsion](../03-70-02_H2_Fuel_Cell_Propulsion/)
  - [03-70-03 — Electric Propulsion GSE](../03-70-03_Electric_Propulsion_GSE/)
  - [03-70-04 — Hybrid Propulsion GSE](../03-70-04_Hybrid_Propulsion_GSE/)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-08.

---
