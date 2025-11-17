# 95-60-00-002 Storage Taxonomy and Scope

**Document ID:** 95-60-00-002  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE

---

## 1. Purpose

This document defines the comprehensive taxonomy for all storage systems in the AMPEL360 BWB H₂ Hy-E aircraft, establishing classification criteria, naming conventions, and scope boundaries.

---

## 2. Storage Taxonomy Structure

### 2.1 Primary Classification by Function

```
AMPEL360 Storage Systems
│
├── ENERGY_STORAGE
│   ├── Electrical (Batteries, Supercapacitors)
│   ├── Chemical (Hydrogen, Fuel)
│   ├── Mechanical (Flywheels, Springs, Accumulators)
│   ├── Thermal (Phase Change Materials, Thermal Buffers)
│   └── Hybrid (CO₂ Battery, Multi-mode Systems)
│
├── FLUID_STORAGE
│   ├── Cryogenic (LH₂, LN₂, LOX)
│   ├── Hydraulic (Fluid Reservoirs, Accumulators)
│   ├── Pneumatic (Compressed Air, Gas Bottles)
│   └── Service Fluids (Water, Waste, Oil)
│
├── DATA_STORAGE
│   ├── Flight Critical (FDR, CVR, QAR)
│   ├── Operational (Data Hubs, Buffers)
│   ├── Archive (Cold Storage, Backups)
│   └── Digital Infrastructure (Data Lakes, Registries)
│
└── PROPULSION_STORAGE
    ├── Primary Fuel (H₂ Tanks)
    ├── Auxiliary Fuel (APU)
    ├── Thermal Buffers (Propulsion Cooling)
    └── Energy Buffers (Spool Inertia, Mechanical)
```

---

## 3. Classification Criteria

### 3.1 By Physical State

| Class | Description | Examples | ATA |
|-------|-------------|----------|-----|
| **LIQUID** | Liquid-state storage | Hydraulic fluid, water, waste | 29, 38 |
| **GAS** | Gaseous storage | Compressed air, pneumatic | 36 |
| **CRYOGENIC** | Cryogenic liquid storage | LH₂, LN₂, LOX | 28 |
| **SOLID** | Solid-state storage | Batteries, thermal PCM | 24, 21 |
| **DIGITAL** | Electronic/magnetic storage | FDR, data hubs, cloud | 31, 46 |

### 3.2 By Criticality

| Level | Definition | Failure Impact | Examples |
|-------|-----------|----------------|----------|
| **CRITICAL** | Flight safety-critical | Loss of control, immediate hazard | H₂ tanks, FDR, hydraulic accumulators |
| **ESSENTIAL** | Mission-essential | Degraded operation | Battery packs, thermal buffers |
| **IMPORTANT** | Comfort/efficiency | Reduced performance | Water tanks, data buffers |
| **AUXILIARY** | Support functions | Minor inconvenience | APU fuel, grey water |

### 3.3 By Operational Profile

| Profile | Duty Cycle | Monitoring Frequency | Examples |
|---------|-----------|---------------------|----------|
| **CONTINUOUS** | Always active | Real-time | H₂ tanks, batteries, FDR |
| **MISSION** | Active during flight | Per-flight | Hydraulic reservoirs, thermal buffers |
| **INTERMITTENT** | Periodic use | Daily/weekly | APU fuel, water tanks |
| **STANDBY** | Emergency/backup | Monthly | Emergency systems, backup power |

---

## 4. Capacity and Sizing Bands

### 4.1 Energy Storage Capacity Bands

| Band | Capacity Range | Typical Application | Examples |
|------|---------------|---------------------|----------|
| **MICRO** | < 1 kWh | Local buffers, sensors | Supercaps for avionics |
| **SMALL** | 1-10 kWh | Subsystem backup | Emergency battery packs |
| **MEDIUM** | 10-100 kWh | System-level buffering | APU start batteries |
| **LARGE** | 100-500 kWh | Primary backup power | Main battery banks |
| **MEGA** | > 500 kWh | Primary propulsion/energy | CO₂ battery, H₂ storage |

### 4.2 Fluid Storage Volume Bands

| Band | Volume Range | Typical Application | Examples |
|------|-------------|---------------------|----------|
| **MICRO** | < 1 L | Sight glasses, samples | Oil level indicators |
| **SMALL** | 1-10 L | Component reservoirs | Hydraulic accumulators |
| **MEDIUM** | 10-100 L | System reservoirs | Hydraulic main reservoir |
| **LARGE** | 100-1000 L | Service tanks | Water tanks, waste tanks |
| **MEGA** | > 1000 L (or kg) | Primary fuel storage | LH₂ main tanks |

### 4.3 Data Storage Capacity Bands

| Band | Capacity Range | Typical Application | Examples |
|------|---------------|---------------------|----------|
| **SMALL** | < 1 GB | Real-time buffers | Sensor data streams |
| **MEDIUM** | 1-100 GB | Flight recorders | FDR, CVR |
| **LARGE** | 100 GB - 10 TB | Onboard data hubs | Mission data storage |
| **MEGA** | > 10 TB | Digital infrastructure | Data lakes, warehouses |

---

## 5. Scope Boundaries

### 5.1 Included in 95-60 Storages

- All tanks, vessels, reservoirs with **defined capacity**
- Accumulators and buffers with **energy/fluid storage function**
- Data storage systems with **retention policies**
- Digital storage infrastructure with **defined SLOs**

### 5.2 Excluded from 95-60 Storages

- Active processing systems (e.g., fuel cells, pumps) → Covered in respective ATA chapters
- Transient flow through pipes/ducts → Covered in distribution systems
- Structural volumes without storage function → Covered in 95-50 Structures
- Empty equipment bays → Covered in 95-50 Structures

### 5.3 Grey Areas (Case-by-Case)

- **Embedded thermal mass**: Included if designed for thermal buffering
- **Pipe dead volume**: Excluded unless specifically sized for buffering
- **Software cache/RAM**: Included if persistent or mission-critical
- **Fuel cell reactant volumes**: Cross-referenced between ATA 80 and 95-60-28

---

## 6. Storage Lifecycle Phases

Storage systems are documented across lifecycle phases:

```
01_Concept       → Initial sizing, trade studies
02_Requirements  → Capacity, safety, performance specs
03_Architecture  → Integration, interfaces, location
04_Design        → Detailed design, materials, sensors
05_Analysis      → Thermal, structural, safety analysis
06_Simulation    → Digital twin, operational modeling
07_Test          → Qualification testing, validation
08_Integration   → Installation, commissioning
09_Certification → Compliance demonstration
10_Maintenance   → Inspection, servicing, refurbishment
11_Obsolescence  → Decommissioning, disposal, recycling
12_Lessons       → Performance review, improvements
```

---

## 7. Cross-References

### 7.1 To Physical ATA Chapters

- **ATA 21**: ECS thermal storages
- **ATA 24**: Electrical energy storages
- **ATA 28**: Hydrogen and cryogenic storages
- **ATA 29**: Hydraulic reservoirs and accumulators
- **ATA 31**: Data recorders and buffers
- **ATA 38**: Water and waste storages
- **ATA 46**: Digital and cloud storages
- **ATA 49**: APU and auxiliary storages
- **ATA 70**: Propulsion energy buffers
- **ATA 80**: CO₂ battery and hybrid energy storages

### 7.2 To Digital Product Passport Chapters

- **95-20**: Subsystem component details
- **95-30**: Circularity and lifecycle management
- **95-40**: Software monitoring and control
- **95-50**: Structural integration and mounting
- **95-90**: Schemas, tables, and diagrams

---

## 8. Naming and Numbering

### 8.1 Document Numbering

```
95-60-{ATA}-{SEQ}_{Description}
```

- `95-60`: Storage chapter identifier
- `{ATA}`: Two-digit ATA chapter (00 for meta, 21, 24, 28, etc.)
- `{SEQ}`: Three-digit sequence (001, 002, 003, ...)
- `{Description}`: PascalCase description

### 8.2 Asset Numbering

```
95-60-{ATA}-A{nnn}_{CATEGORY}_{ShortName}.{ext}
```

Following AMPEL360_ASSETS_STANDARD.md

---

## 9. Related Documents

- **[95-60-00-001](95-60-00-001_Storages_Overview.md)**: Overview of all storage systems
- **[95-60-00-003](95-60-00-003_Cross_ATA_Storages_Map.csv)**: Cross-ATA mapping matrix
- **[95-60-00-004](00_META/95-60-00-004_Storage_Classes_and_Capacity_Bands.md)**: Detailed classification
- **[95-60-00-006](00_META/95-60-00-006_Storages_Registry.json)**: Authoritative storage registry

---

## 10. Maintenance and Updates

This taxonomy is reviewed quarterly and updated as new storage systems are added or existing systems evolve.

**Last Review:** 2025-11-17  
**Next Review:** 2026-02-17  
**Owner:** AMPEL360 Systems Architecture

---

**Document Control**
- **Standard**: OPT-IN Framework v1.5
- **Classification**: Technical Documentation
- **Distribution**: Unrestricted (Open Source)
