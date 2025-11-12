# 03-80-01-001A - LH₂ Cryogenic Refueler - Purpose & Scope

**ATA Chapter:** 03 - Support Information GSE  
**System Code:** 03-80-01  
**System Name:** LH₂ Cryogenic Refueler  
**Document Type:** Overview - Purpose & Scope  
**Document Code:** 03-80-01-001A  
**Version:** 1.0.0  
**Status:** Active  
**Date:** 2025-11-12

---

## 1. Purpose

This document defines the purpose, scope, and boundaries for the **LH₂ Cryogenic Refueler** Ground Support Equipment (GSE) system used with the AMPEL360 BWB H₂ Hy-E Q100 aircraft.

The LH₂ Cryogenic Refueler is a specialized energy GSE (origin: **80-xx = Engines/Energy**) designed to safely transfer liquid hydrogen from ground storage to the aircraft's onboard fuel system at cryogenic temperatures.

---

## 2. System Overview

### 2.1 System Identity

| Parameter | Value |
|-----------|-------|
| **ATA Code** | 03-80-01 |
| **Origin Rule** | 80 = Auxiliary Energy / Ground Energy Equipment |
| **Category** | Energy GSE - Cryogenic Refueling |
| **Primary Function** | LH₂ fuel transfer from ground storage to aircraft |
| **Secondary Function** | Fuel quality monitoring and safety system |

### 2.2 Key Specifications

| Specification | Value | Unit |
|---------------|-------|------|
| **Fuel Type** | Liquid Hydrogen (LH₂) | - |
| **Storage Capacity** | 500 | kg |
| **Operating Temperature** | 20 | K (-253°C) |
| **Operating Pressure** | 10 | bar |
| **Transfer Rate** | 100 | kg/hr |
| **Transfer Time (full)** | ~5 | hours |
| **Purity Required** | >99.99 | % |
| **Insulation Type** | Vacuum-insulated, multi-layer | - |
| **Mobility** | Road-mobile trailer | - |
| **Power Supply** | 400V 3-phase, 50 Hz | - |

---

## 3. Scope

### 3.1 In Scope

This document and the 03-80-01 system documentation cover:

#### 3.1.1 Equipment and Systems
- ✅ LH₂ storage tank (500 kg capacity)
- ✅ Cryogenic transfer lines and hoses
- ✅ Vacuum-insulated piping system
- ✅ Transfer pumps (cryogenic-rated)
- ✅ Flow control and metering system
- ✅ Temperature and pressure monitoring
- ✅ Emergency shutdown system (ESD)
- ✅ Hydrogen leak detection system
- ✅ Static bonding and grounding equipment
- ✅ Mobile trailer chassis and stabilization system
- ✅ Operator control station
- ✅ Communication system (aircraft interface)

#### 3.1.2 Operations
- ✅ Pre-refueling preparation and checks
- ✅ Aircraft-GSE connection procedures
- ✅ LH₂ transfer operations
- ✅ Quality control and purity verification
- ✅ Post-refueling disconnect and purge
- ✅ Emergency procedures and shutdown
- ✅ System monitoring and alarms
- ✅ Refueling abort procedures

#### 3.1.3 Safety Systems
- ✅ Hydrogen leak detection (acoustic, thermal, optical)
- ✅ Fire detection and suppression
- ✅ Pressure relief and venting
- ✅ Emergency shutdown controls
- ✅ Cold burn protection
- ✅ Static discharge prevention
- ✅ Exclusion zone management
- ✅ Personal protective equipment (PPE)

#### 3.1.4 Maintenance and Support
- ✅ Scheduled maintenance procedures
- ✅ Calibration and testing
- ✅ Spare parts management (linked to 03-90-11)
- ✅ System diagnostics
- ✅ Troubleshooting guides
- ✅ Component replacement procedures

#### 3.1.5 Documentation
- ✅ Operating manuals
- ✅ Maintenance manuals
- ✅ Safety procedures (linked to 03-90-02)
- ✅ Training materials (linked to 03-90-01)
- ✅ Certification documents
- ✅ Interface Control Documents (ICDs)

### 3.2 Out of Scope

The following are **NOT** covered in 03-80-01 documentation:

#### 3.2.1 Aircraft Systems
- ❌ On-board LH₂ fuel system (see **ATA 28-10-00**)
- ❌ Aircraft fuel cell propulsion system (see **ATA 71**)
- ❌ Aircraft fuel tanks design (see **ATA 28-10-00**)
- ❌ Aircraft refueling receptacle (interface only)

#### 3.2.2 Ground Infrastructure
- ❌ Airport LH₂ storage facility (see **ATA 02**)
- ❌ LH₂ production and liquefaction (off-site)
- ❌ LH₂ transportation to airport (tanker trucks)
- ❌ Airport fueling infrastructure design

#### 3.2.3 Other GSE
- ❌ General handling equipment (see **03-20-00**)
- ❌ Structural support frames (see **03-50-01**)
- ❌ Ground power unit (see **03-80-02**)
- ❌ Towing and positioning equipment (see **ATA 09**)

#### 3.2.4 Maintenance Systems
- ❌ Refueler maintenance program (see **03-20-11**)
- ❌ Fleet spares program (see **03-90-10**)
- ❌ Operator training program (see **03-90-01**)

---

## 4. System Context

### 4.1 Law of Origin Classification

Per **NUMBERING_RULES.md**, this system is classified as:

**Origin: 80-xx = Engines / Propulsion / Energy (Auxiliary)**

**Rationale:**
- Primary function: Energy transfer (LH₂ fuel)
- Supports propulsion system (fuel cell powerplant)
- Ground-based auxiliary energy equipment
- Not a structure (50-xx)
- Not a functional maintenance system (20-xx)
- Not meta-information/documentation (90-xx)

Therefore: **03-80-01** (Infrastructure domain 03, Energy origin 80, Refueler 01)

### 4.2 Position in OPT-IN Framework

```
OPT-IN_FRAMEWORK/
└── I-INFRASTRUCTURES/
    └── ATA_03-SUPPORT_INFORMATION_GSE/
        └── 03-80_ENERGY_GSE/
            └── 03-80-01_LH2_CRYOGENIC_REFUELER/  ← THIS SYSTEM
                ├── 01_OVERVIEW/                  ← THIS DOCUMENT
                ├── 02_SAFETY/
                ├── 03_REQUIREMENTS/
                ├── 04_DESIGN/
                ├── 05_INTERFACES/
                ├── 06_ENGINEERING/
                ├── 07_V_AND_V/
                ├── 08_PROTOTYPING/
                ├── 09_PRODUCTION_PLANNING/
                ├── 10_CERTIFICATION/
                ├── 11_OPERATIONS_MAINTENANCE/
                ├── 12_ASSETS_MANAGEMENT/
                ├── 13_SUBSYSTEMS_COMPONENTS/
                └── 14_META_GOVERNANCE/
```

### 4.3 Related Systems

| System Code | System Name | Relationship |
|-------------|-------------|--------------|
| **ATA 28-10-00** | H₂ Storage Tanks (Aircraft) | Target system for fuel transfer |
| **ATA 71** | Power Plant (Fuel Cells) | End user of transferred fuel |
| **03-80-00** | General Energy GSE | Parent system standards |
| **03-20-11** | LH₂ Refueler Maintenance | Maintenance program for this GSE |
| **03-50-01** | LH₂ Support Frames | Structural support during refueling |
| **03-90-01** | Training Materials | Operator training for this GSE |
| **03-90-02** | Safety Data Sheets | LH₂ safety information |
| **03-90-11** | LH₂ Refueler Parts | Spare parts catalogue |
| **ATA 02-32-00** | H₂ Refueling Procedures | Operational procedures |

---

## 5. Operational Context

### 5.1 Typical Refueling Scenario

1. **Pre-Positioning** (20 min)
   - Refueler positioned in designated zone
   - Stabilization and grounding
   - Pre-flight checks and system readiness

2. **Connection** (15 min)
   - Aircraft-GSE electrical bonding
   - Cryogenic hose connection to aircraft receptacle
   - Communication link establishment
   - Safety zone establishment

3. **Pre-Transfer** (10 min)
   - Line purge and cool-down
   - System leak checks
   - Final safety verification
   - Operator authorization

4. **Transfer** (5 hours for 500 kg)
   - Automated LH₂ transfer at 100 kg/hr
   - Continuous monitoring (T, P, flow, purity)
   - Real-time safety system surveillance
   - Operator supervision

5. **Post-Transfer** (15 min)
   - Transfer completion verification
   - Line purge and disconnect
   - System shutdown and securing
   - Documentation and logging

6. **Departure** (10 min)
   - Refueler repositioning
   - Safety zone clearance
   - Post-operation inspection

**Total Time:** ~6 hours (5h transfer + 1h setup/teardown)

### 5.2 Key Performance Indicators (KPIs)

| KPI | Target | Measurement |
|-----|--------|-------------|
| **Transfer Efficiency** | >95% | (Fuel delivered / Fuel capacity) |
| **Purity Maintained** | >99.99% | Post-transfer sampling |
| **Safety Incidents** | 0 | Per 1,000 refuelings |
| **Unscheduled Downtime** | <2% | Annual availability |
| **Transfer Time Compliance** | >90% | Within 5±0.5 hours |
| **Leak Detection Response** | <5 sec | Alarm to ESD activation |

---

## 6. Regulatory and Standards Compliance

### 6.1 Applicable Standards

| Standard | Title | Application |
|----------|-------|-------------|
| **ISO 19881** | Gaseous hydrogen — Land vehicle fuel containers | LH₂ storage design |
| **SAE J2601** | Fueling protocols for hydrogen vehicles | Transfer protocols |
| **NFPA 2** | Hydrogen Technologies Code | Fire safety |
| **ISO 13984** | Liquid hydrogen — Land vehicle fuel tanks | Cryogenic tank design |
| **EN 1473** | Installation and equipment for LNG | Cryogenic systems |
| **ASME B31.12** | Hydrogen Piping and Pipelines | Piping design |
| **IEC 60079** | Explosive atmospheres | Electrical equipment |

### 6.2 Certification Requirements

- ✅ Pressure Equipment Directive (PED) 2014/68/EU
- ✅ ATEX Directive 2014/34/EU (explosive atmospheres)
- ✅ Machinery Directive 2006/42/EC
- ✅ EMC Directive 2014/30/EU
- ✅ National hydrogen vehicle regulations (varies by jurisdiction)
- ✅ AMPEL360 Engineering Authority approval

---

## 7. Lifecycle Overview

This system follows the **14-folder lifecycle skeleton**:

| Folder | Phase | Key Deliverables |
|--------|-------|------------------|
| **01_OVERVIEW** | Concept | Purpose, scope, context (this document) |
| **02_SAFETY** | Analysis | FMEA, FHA, HAZOP, safety case |
| **03_REQUIREMENTS** | Specification | Functional, performance, safety requirements |
| **04_DESIGN** | Design | Mechanical, electrical, control system design |
| **05_INTERFACES** | Integration | ICDs with aircraft and infrastructure |
| **06_ENGINEERING** | Analysis | Thermal, structural, flow analysis |
| **07_V_AND_V** | Validation | Test plans, test reports, qualification |
| **08_PROTOTYPING** | Development | Prototype build and testing |
| **09_PRODUCTION_PLANNING** | Manufacturing | Production processes and tooling |
| **10_CERTIFICATION** | Compliance | Certification documentation |
| **11_OPERATIONS_MAINTENANCE** | Operations | Operating and maintenance manuals |
| **12_ASSETS_MANAGEMENT** | Lifecycle | Asset tracking, configuration management |
| **13_SUBSYSTEMS_COMPONENTS** | Breakdown | Detailed component specifications |
| **14_META_GOVERNANCE** | Control | Document control, change management |

---

## 8. Document Control

### 8.1 Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Author** | GSE Engineering Team | [Digital] | 2025-11-12 |
| **Reviewer** | Safety Engineering | [Pending] | - |
| **Approver** | Program Office | [Pending] | - |

### 8.2 Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-11-12 | Program Office | Initial release per Law of Origin |

### 8.3 Related Documents

| Code | Title | Relationship |
|------|-------|--------------|
| **NUMBERING_RULES.md** | ATA Numbering System Rules | Defines origin-based coding |
| **03-80-01-002A** | System Architecture | Next document in series |
| **03-80-01-003A** | Key Stakeholders | Stakeholder identification |
| **ATA_03/00_README.md** | ATA 03 Overview | Parent chapter overview |
| **ATA_03/INDEX.meta.yaml** | ATA 03 Index | Chapter metadata |

---

## 9. Glossary

| Term | Definition |
|------|------------|
| **LH₂** | Liquid Hydrogen at cryogenic temperature (20K / -253°C) |
| **GSE** | Ground Support Equipment |
| **ESD** | Emergency Shutdown |
| **ICD** | Interface Control Document |
| **PPE** | Personal Protective Equipment |
| **FMEA** | Failure Mode and Effects Analysis |
| **FHA** | Functional Hazard Analysis |
| **HAZOP** | Hazard and Operability Study |
| **KPI** | Key Performance Indicator |

---

## 10. Summary

The **03-80-01 LH₂ Cryogenic Refueler** is a critical energy GSE system (origin: 80-xx) that enables safe, efficient transfer of liquid hydrogen fuel from ground storage to the AMPEL360 aircraft. This document establishes the purpose, scope, and context for all subsequent documentation in the 14-folder lifecycle structure.

**Key Takeaways:**
- ✅ Classified as Energy GSE per Law of Origin (80-xx = Engines/Energy)
- ✅ Capacity: 500 kg LH₂, transfer rate 100 kg/hr
- ✅ Safety-critical system with comprehensive monitoring and ESD
- ✅ Full lifecycle documentation across 14 folders
- ✅ Complies with international hydrogen and cryogenic standards

---

**Next Steps:**
1. Review and approve this document
2. Proceed to **02_SAFETY** folder for hazard analysis
3. Develop detailed requirements in **03_REQUIREMENTS**
4. Begin preliminary design in **04_DESIGN**

---

**© 2024-2025 AMPEL360 Project | All Rights Reserved**
