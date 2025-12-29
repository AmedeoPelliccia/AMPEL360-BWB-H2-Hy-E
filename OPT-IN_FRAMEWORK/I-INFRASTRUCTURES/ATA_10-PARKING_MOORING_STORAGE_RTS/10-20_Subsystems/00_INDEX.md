# Index: I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/10-20_Subsystems

> **Last Update:** 2025-12-11
> **Total Documents:** 42 specifications + 4 templates + 1 schema
> **Status:** Active - Under Development

## 📂 Directory Contents

### Core Documentation
- [README.md](README.md) - Subsystems overview and methodology
- [subsystems-metadata.schema.json](subsystems-metadata.schema.json) - Metadata schema

### Templates
- [subsystems-templates/](subsystems-templates/)
  - [subsystem-spec-template.md](subsystems-templates/subsystem-spec-template.md)
  - [interface-spec-template.md](subsystems-templates/interface-spec-template.md)
  - [component-spec-template.md](subsystems-templates/component-spec-template.md)
  - [verification-matrix-template.md](subsystems-templates/verification-matrix-template.md)

---

## 🔧 Tiedown Subsystem (01-09)

Secure aircraft restraint during parking and storage operations.

| Doc Number | Title | Status | Description |
|------------|-------|--------|-------------|
| [10-20-01A](tiedown-subsystem/10-20-01A_Tiedown_System_Spec.md) | Tiedown System Specification | DRAFT | System-level specification for tiedown |
| [10-20-02A](tiedown-subsystem/10-20-02A_Tiedown_Points_Design.md) | Tiedown Points Design | DRAFT | Design of structural attachment points |
| [10-20-03A](tiedown-subsystem/10-20-03A_Tiedown_Fittings.md) | Tiedown Fittings | DRAFT | Quick-release fittings specification |
| [10-20-04A](tiedown-subsystem/10-20-04A_Load_Distribution.md) | Load Distribution | DRAFT | Load distribution analysis and design |
| [10-20-05A](tiedown-subsystem/10-20-05A_BWB_Tiedown_Adaptation.md) | BWB Tiedown Adaptation | DRAFT | BWB-specific tiedown adaptations |

**Key Features:**
- 8-point tiedown pattern for BWB geometry
- Non-sparking materials for H2 safety
- Quick-release capability (<2 minutes per point)
- 50 kN ultimate load per point
- Wind resistance up to 70 kt (storm config)

---

## ⚓ Mooring Subsystem (10-19)

Extended parking and severe weather protection.

| Doc Number | Title | Status | Description |
|------------|-------|--------|-------------|
| [10-20-10A](mooring-subsystem/10-20-10A_Mooring_System_Spec.md) | Mooring System Specification | DRAFT | System-level specification for mooring |
| [10-20-11A](mooring-subsystem/10-20-11A_Mooring_Points_Design.md) | Mooring Points Design | DRAFT | Mooring attachment point design |
| [10-20-12A](mooring-subsystem/10-20-12A_Mooring_Equipment.md) | Mooring Equipment | DRAFT | Lines, anchors, and equipment |
| [10-20-13A](mooring-subsystem/10-20-13A_Storm_Mooring_System.md) | Storm Mooring System | DRAFT | Enhanced system for severe weather |
| [10-20-14A](mooring-subsystem/10-20-14A_BWB_Mooring_Adaptation.md) | BWB Mooring Adaptation | DRAFT | BWB-specific mooring design |

**Key Features:**
- Normal and storm configurations
- Compatible with MIL-STD-209 ground infrastructure
- BWB-optimized mooring pattern
- Enhanced weather protection (>70 kt winds)

---

## 🔒 Ground Lock Subsystem (20-29)

Locking devices for steering, control surfaces, and landing gear.

| Doc Number | Title | Status | Description |
|------------|-------|--------|-------------|
| [10-20-20A](ground-lock-subsystem/10-20-20A_Ground_Lock_System_Spec.md) | Ground Lock System Specification | DRAFT | System-level specification |
| [10-20-21A](ground-lock-subsystem/10-20-21A_Steering_Lock.md) | Steering Lock | DRAFT | Nose gear steering lock |
| [10-20-22A](ground-lock-subsystem/10-20-22A_Control_Surface_Locks.md) | Control Surface Locks | DRAFT | Locks for flight control surfaces |
| [10-20-23A](ground-lock-subsystem/10-20-23A_Landing_Gear_Locks.md) | Landing Gear Locks | DRAFT | Landing gear lock pins and safety devices |

**Key Features:**
- Prevents inadvertent movement
- Visual engagement indicators
- Standardized lock pin designs
- Integrated with maintenance procedures

---

## ⚠️ H2 Safety Subsystem (30-39)

**CRITICAL**: Hydrogen safety systems for ground operations.

| Doc Number | Title | Status | Description |
|------------|-------|--------|-------------|
| [10-20-30A](h2-safety-subsystem/10-20-30A_H2_Safety_System_Spec.md) | H2 Safety System Specification | DRAFT | System-level H2 safety specification |
| [10-20-31A](h2-safety-subsystem/10-20-31A_H2_Detection_System.md) | H2 Detection System | DRAFT | H2 detection sensors and logic |
| [10-20-32A](h2-safety-subsystem/10-20-32A_H2_Venting_System.md) | H2 Venting System | DRAFT | Safe H2 venting provisions |
| [10-20-33A](h2-safety-subsystem/10-20-33A_H2_Alarm_System.md) | H2 Alarm System | DRAFT | Visual and audible alarms |
| [10-20-34A](h2-safety-subsystem/10-20-34A_H2_ESD_System.md) | H2 ESD System | DRAFT | Emergency shutdown system |
| [10-20-35A](h2-safety-subsystem/10-20-35A_H2_Monitoring_System.md) | H2 Monitoring System | DRAFT | Continuous H2 monitoring |

**Key Features:**
- Detection at 25% LEL within 1 second
- Redundant sensors at critical locations
- Automatic ESD at 60% LEL
- Visual and audible alarms
- Integration with ground H2 infrastructure

**Applicable Standards:**
- SAE AS6968 (Hydrogen Aircraft Systems)
- ISO 13984 (Liquid Hydrogen)
- NFPA 2 (Hydrogen Technologies Code)

---

## ❄️ Cryogenic Subsystem (40-49)

**CRITICAL**: LH2 handling and thermal management at -253°C.

| Doc Number | Title | Status | Description |
|------------|-------|--------|-------------|
| [10-20-40A](cryo-subsystem/10-20-40A_Cryo_System_Spec.md) | Cryogenic System Specification | DRAFT | System-level cryo specification |
| [10-20-41A](cryo-subsystem/10-20-41A_LH2_Tank_Interface.md) | LH2 Tank Interface | DRAFT | Tank connection interfaces |
| [10-20-42A](cryo-subsystem/10-20-42A_Cryo_Insulation_System.md) | Cryo Insulation System | DRAFT | Thermal insulation system |
| [10-20-43A](cryo-subsystem/10-20-43A_Cryo_Valve_System.md) | Cryo Valve System | DRAFT | Cryogenic valves and controls |
| [10-20-44A](cryo-subsystem/10-20-44A_Boiloff_Management_System.md) | Boiloff Management System | DRAFT | Boil-off control and venting |
| [10-20-45A](cryo-subsystem/10-20-45A_Thermal_Protection_System.md) | Thermal Protection System | DRAFT | Personnel and equipment protection |

**Key Features:**
- Operating temperature: -253°C (20K)
- Boil-off management ≤2% per day
- Vacuum insulation systems
- Cryogenic-qualified materials
- Fill/drain/vent interfaces

**Applicable Standards:**
- ISO 13984 (Liquid Hydrogen)
- SAE AS6968 (H2 Aircraft Systems)
- ASME B31.12 (Hydrogen Piping)

---

## 🛡️ Preservation Subsystem (50-59)

Aircraft preservation during storage.

| Doc Number | Title | Status | Description |
|------------|-------|--------|-------------|
| [10-20-50A](preservation-subsystem/10-20-50A_Preservation_System_Spec.md) | Preservation System Specification | DRAFT | System-level preservation spec |
| [10-20-51A](preservation-subsystem/10-20-51A_Dehumidification_System.md) | Dehumidification System | DRAFT | Moisture control system |
| [10-20-52A](preservation-subsystem/10-20-52A_Corrosion_Prevention.md) | Corrosion Prevention | DRAFT | Corrosion prevention measures |
| [10-20-53A](preservation-subsystem/10-20-53A_H2_System_Preservation.md) | H2 System Preservation | DRAFT | H2-specific preservation |
| [10-20-54A](preservation-subsystem/10-20-54A_Cryo_System_Preservation.md) | Cryo System Preservation | DRAFT | Cryogenic system preservation |

**Key Features:**
- Dehumidification for corrosion prevention
- H2 system purging and preservation
- Cryogenic system conditioning
- Long-term storage preparations

---

## 📊 Monitoring Subsystem (60-69)

Continuous monitoring during ground operations.

| Doc Number | Title | Status | Description |
|------------|-------|--------|-------------|
| [10-20-60A](monitoring-subsystem/10-20-60A_Monitoring_System_Spec.md) | Monitoring System Specification | DRAFT | System-level monitoring spec |
| [10-20-61A](monitoring-subsystem/10-20-61A_Environmental_Monitoring.md) | Environmental Monitoring | DRAFT | Temperature, humidity, pressure |
| [10-20-62A](monitoring-subsystem/10-20-62A_Structural_Monitoring.md) | Structural Monitoring | DRAFT | Structural health monitoring |
| [10-20-63A](monitoring-subsystem/10-20-63A_H2_Status_Monitoring.md) | H2 Status Monitoring | DRAFT | H2 system status and data logging |
| [10-20-64A](monitoring-subsystem/10-20-64A_Remote_Monitoring.md) | Remote Monitoring | DRAFT | Off-site surveillance capabilities |

**Key Features:**
- Real-time environmental monitoring
- Structural health monitoring
- H2 system status tracking
- Remote access capabilities
- Data logging and trending

---

## ✈️ BWB-Specific Subsystems (70-79)

Subsystems adapted for BWB configuration.

| Doc Number | Title | Status | Description |
|------------|-------|--------|-------------|
| [10-20-70A](bwb-specific-subsystems/10-20-70A_BWB_Subsystems_Overview.md) | BWB Subsystems Overview | DRAFT | Overview of BWB-specific systems |
| [10-20-71A](bwb-specific-subsystems/10-20-71A_BWB_Jacking_System.md) | BWB Jacking System | DRAFT | 6-point jacking system |
| [10-20-72A](bwb-specific-subsystems/10-20-72A_BWB_Towing_Interface.md) | BWB Towing Interface | DRAFT | Towing connection and steering |
| [10-20-73A](bwb-specific-subsystems/10-20-73A_BWB_Lifting_System.md) | BWB Lifting System | DRAFT | Hoist points and lifting procedures |
| [10-20-74A](bwb-specific-subsystems/10-20-74A_BWB_Clearance_System.md) | BWB Clearance System | DRAFT | Wingtip clearance detection |

**Key Features:**
- 40m wingspan accommodation
- BWB center of gravity considerations
- 2m wingtip ground clearance management
- Distributed load paths through wing-body structure
- Integrated with other BWB systems

---

## 📈 Statistics

| Category | Count | Status |
|----------|-------|--------|
| **Tiedown Subsystem** | 5 docs | DRAFT |
| **Mooring Subsystem** | 5 docs | DRAFT |
| **Ground Lock Subsystem** | 4 docs | DRAFT |
| **H2 Safety Subsystem** | 6 docs | DRAFT |
| **Cryogenic Subsystem** | 6 docs | DRAFT |
| **Preservation Subsystem** | 5 docs | DRAFT |
| **Monitoring Subsystem** | 5 docs | DRAFT |
| **BWB-Specific Subsystems** | 5 docs | DRAFT |
| **Templates** | 4 docs | ACTIVE |
| **TOTAL** | **45 files** | - |

---

## 🔗 Related Documentation

### Internal References
- [../README.md](../README.md) - ATA 10 Overview
- [../10-00_GENERAL/](../10-00_GENERAL/) - General information
- [../10-10_Operations/](../10-10_Operations/) - Operational procedures
- [../10-90_Tables_Schemas_Diagrams/](../10-90_Tables_Schemas_Diagrams/) - Supporting data

### External ATA Chapters
- **ATA 28**: Fuel Systems (H2 system design)
- **ATA 53**: Fuselage/Wing Structure
- **ATA 32**: Landing Gear
- **ATA 27**: Flight Controls
- **ATA 20**: Standard Practices

---

## Document Control

- **Generated with assistance from**: AI (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last Updated**: 2025-12-11
- **Next Review**: 2026-01-11
- **Status**: DRAFT - Under Active Development
- **Repository**: `AMPEL360-BWB-H2-Hy-E`

---
