# ATA 04: Airworthiness Limitations - Navigation Guide

## Quick Access

### Priority Documents (Start Here)
1. **[04_README.md](./04_README.md)** - Chapter overview and regulatory framework
2. **[INDEX.meta.yaml](./INDEX.meta.yaml)** - Chapter metadata and structure
3. **[04-50-01 Example](./04-50_FUEL_AND_ENERGY_STORAGE_LIMITS/04-50-01_LH2_Tank_Inner_Vessel_Life_Limit/)** - Fully populated component

### Section Overviews
| Section | Title | Components | README |
|---------|-------|------------|--------|
| 04-10 | Structural Life Limits | 7 | [README](./04-10_STRUCTURAL_LIFE_LIMITS/README.md) |
| 04-20 | Damage Tolerance Inspections | 8 | [README](./04-20_DAMAGE_TOLERANCE_INSPECTIONS/) |
| 04-30 | Certification Maintenance Requirements | 8 | [README](./04-30_CERTIFICATION_MAINTENANCE_REQUIREMENTS/) |
| 04-40 | Propulsion System Limits | 6 | [README](./04-40_PROPULSION_SYSTEM_LIMITS/) |
| 04-50 | Fuel and Energy Storage Limits | 6 | [README](./04-50_FUEL_AND_ENERGY_STORAGE_LIMITS/README.md) ⭐ |
| 04-60 | EWIS Aging Limitations | 6 | [README](./04-60_EWIS_AGING_LIMITATIONS/) |
| 04-70 | Systems Component Life Limits | 6 | [README](./04-70_SYSTEMS_COMPONENT_LIFE_LIMITS/) |
| 04-80 | Special Inspections | 7 | [README](./04-80_SPECIAL_INSPECTIONS/) |
| 04-90 | Limitations Management | 6 | [README](./04-90_LIMITATIONS_MANAGEMENT/) |

⭐ = Section README available

## Structure Overview

```
ATA_04-AIRWORTHINESS_LIMITATIONS/
├── 04_README.md                          ← Chapter overview
├── INDEX.meta.yaml                       ← Metadata
├── NAVIGATION.md                         ← This file
│
├── 04-10_STRUCTURAL_LIFE_LIMITS/         ← Safe-life components
│   ├── README.md                         ← Section overview
│   ├── 04-10-01_Safe_Life_Components/
│   │   ├── 01_OVERVIEW/
│   │   ├── 02_SAFETY/
│   │   ├── 03_REQUIREMENTS/
│   │   ├── 04_DESIGN/
│   │   ├── 05_INTERFACES/
│   │   ├── 06_ENGINEERING/
│   │   ├── 07_V_AND_V/
│   │   ├── 08_PROTOTYPING/
│   │   ├── 09_PRODUCTION_PLANNING/
│   │   ├── 10_CERTIFICATION/
│   │   ├── 11_OPERATIONS_AND_MAINTENANCE/
│   │   ├── 12_ASSETS_MANAGEMENT/
│   │   ├── 13_SUBSYSTEMS_AND_COMPONENTS/
│   │   └── 14_META_GOVERNANCE/
│   ├── 04-10-02_Landing_Gear_Life_Limits/
│   ├── 04-10-03_Flight_Control_Actuator_Limits/
│   ├── 04-10-04_Engine_Mount_Life_Limits/
│   ├── 04-10-05_BWB_Center_Body_Life_Limit/
│   ├── 04-10-06_Wing_Root_Attachment_Limit/
│   └── 04-10-07_Cryogenic_Tank_Support_Structure/
│
├── 04-20_DAMAGE_TOLERANCE_INSPECTIONS/   ← Inspection thresholds
│   ├── 04-20-01_Principal_Structural_Elements_PSE/
│   ├── 04-20-02_Composite_Structure_Inspection_Thresholds/
│   ├── 04-20-03_Metallic_Fatigue_Critical_Structure/
│   ├── 04-20-04_Widespread_Fatigue_Damage_WFD/
│   ├── 04-20-05_Corrosion_Prevention_Limits/
│   ├── 04-20-06_BWB_Skin_Panel_Inspection_Intervals/
│   ├── 04-20-07_Pressurization_Cycle_Tracking/
│   └── 04-20-08_Hydrogen_Cold_Zone_Structure_Monitoring/
│
├── 04-30_CERTIFICATION_MAINTENANCE_REQUIREMENTS/  ← CMRs
│   ├── 04-30-01_CMR_Task_Definitions/
│   ├── 04-30-02_Flight_Control_System_CMRs/
│   ├── 04-30-03_Fuel_System_CMRs/
│   ├── 04-30-04_Fire_Protection_CMRs/
│   ├── 04-30-05_Emergency_Systems_CMRs/
│   ├── 04-30-06_H2_Leak_Detection_CMR/
│   ├── 04-30-07_CO2_Capture_System_CMR/
│   └── 04-30-08_High_Voltage_Isolation_CMR/
│
├── 04-40_PROPULSION_SYSTEM_LIMITS/       ← Engine/motor limits
│   ├── 04-40-01_Turbine_Disc_Life_Limits/
│   ├── 04-40-02_Propulsor_Blade_Retirement_Limits/
│   ├── 04-40-03_Gearbox_Component_Life_Limits/
│   ├── 04-40-04_Fuel_Cell_Stack_Life_Limit/
│   ├── 04-40-05_H2_Fuel_Pump_Seal_Life_Limit/
│   └── 04-40-06_Electric_Motor_Bearing_Life_Limit/
│
├── 04-50_FUEL_AND_ENERGY_STORAGE_LIMITS/ ← H₂ tanks, batteries
│   ├── README.md                         ← Section overview ⭐
│   ├── 04-50-01_LH2_Tank_Inner_Vessel_Life_Limit/  ← DETAILED EXAMPLE ⭐⭐⭐
│   │   ├── 01_OVERVIEW/README.md         ← Limitation statement
│   │   ├── 02_SAFETY/README.md           ← FTA/FMEA
│   │   ├── 03_REQUIREMENTS/REQUIREMENTS.yaml  ← Requirements traceability
│   │   ├── 04_DESIGN/DESIGN_DETAILS.md   ← Engineering design
│   │   ├── 06_ENGINEERING/ANALYSIS_REPORTS.md  ← Analysis substantiation
│   │   ├── 10_CERTIFICATION/CERT_ARTIFACTS.md  ← Regulatory approval
│   │   └── 11_OPERATIONS_AND_MAINTENANCE/MAINTENANCE_PROCEDURES.md
│   ├── 04-50-02_Vacuum_Insulation_Integrity_Threshold/
│   ├── 04-50-03_Cryogenic_Line_Flexible_Joint_Limit/
│   ├── 04-50-04_Solid_CO2_Battery_Module_Retirement/
│   ├── 04-50-05_High_Voltage_Battery_Capacity_Threshold/
│   └── 04-50-06_Thermal_Cycling_Accumulated_Limit/
│
├── 04-60_EWIS_AGING_LIMITATIONS/         ← Wiring system limits
│   ├── 04-60-01_Wire_Bundle_Age_Limits/
│   ├── 04-60-02_Connector_Replacement_Intervals/
│   ├── 04-60-03_High_Temperature_Zone_EWIS_Limits/
│   ├── 04-60-04_Cryogenic_Zone_EWIS_Limits/
│   ├── 04-60-05_High_Voltage_Insulation_Resistance_Minimum/
│   └── 04-60-06_EWIS_Zonal_Inspection_Thresholds/
│
├── 04-70_SYSTEMS_COMPONENT_LIFE_LIMITS/  ← Various systems
│   ├── 04-70-01_Hydraulic_Component_Life_Limits/
│   ├── 04-70-02_Pneumatic_System_Component_Limits/
│   ├── 04-70-03_Flight_Control_Computer_Life_Limit/
│   ├── 04-70-04_Air_Data_Sensor_Calibration_Limit/
│   ├── 04-70-05_Oxygen_System_Component_Limits/
│   └── 04-70-06_Fire_Extinguisher_Service_Life/
│
├── 04-80_SPECIAL_INSPECTIONS/            ← Event-driven inspections
│   ├── 04-80-01_Post_Heavy_Landing_Inspection/
│   ├── 04-80-02_Lightning_Strike_Inspection_Requirements/
│   ├── 04-80-03_Bird_Strike_Inspection_Thresholds/
│   ├── 04-80-04_Overweight_Landing_Inspection/
│   ├── 04-80-05_Hail_Damage_Inspection_Requirements/
│   ├── 04-80-06_Cryogenic_System_Leak_Event_Inspection/
│   └── 04-80-07_Thermal_Exceedance_Inspection/
│
└── 04-90_LIMITATIONS_MANAGEMENT/         ← Document control
    ├── 04-90-01_ALS_Document_Control/
    ├── 04-90-02_Revision_and_Amendment_Process/
    ├── 04-90-03_Compliance_Tracking_System/
    ├── 04-90-04_Fleet_Leader_Program_Integration/
    ├── 04-90-05_Service_Bulletin_Mandatory_Compliance/
    └── 04-90-06_Airworthiness_Directive_Compliance/
```

## The 14-Folder Skeleton

Every component follows the same lifecycle structure:

| Folder | Content | Purpose |
|--------|---------|---------|
| 01_OVERVIEW | Executive summary | High-level limitation statement |
| 02_SAFETY | Safety assessment | FTA, FMEA, hazard analysis |
| 03_REQUIREMENTS | Requirements | Traceable requirements (YAML) |
| 04_DESIGN | Design specifications | Engineering drawings, specs |
| 05_INTERFACES | Interface definitions | System boundaries |
| 06_ENGINEERING | Analysis reports | FEA, fatigue, thermal analysis |
| 07_V_AND_V | Verification & validation | Test plans and reports |
| 08_PROTOTYPING | Prototype testing | Hardware qualification |
| 09_PRODUCTION_PLANNING | Manufacturing | Production processes |
| 10_CERTIFICATION | Regulatory approval | TC amendments, ALS entries |
| 11_OPERATIONS_AND_MAINTENANCE | Operator procedures | Maintenance tasks |
| 12_ASSETS_MANAGEMENT | Spares and logistics | Supply chain |
| 13_SUBSYSTEMS_AND_COMPONENTS | Sub-tier items | Decomposition |
| 14_META_GOVERNANCE | Metadata | Schemas, CI rules |

## How to Use This Chapter

### For Operators
1. Start with **04_README.md** to understand mandatory compliance requirements
2. Review each section README for overview of applicable limitations
3. For each component in your aircraft:
   - Read **01_OVERVIEW** for the limitation statement
   - Review **11_OPERATIONS_AND_MAINTENANCE** for compliance procedures
4. Implement cycle tracking per **04-90-03** (Compliance Tracking System)

### For Maintenance Organizations
1. Understand limitations from **01_OVERVIEW** of each component
2. Follow procedures in **11_OPERATIONS_AND_MAINTENANCE**
3. Record removals and installations per **04-90-01** (Document Control)
4. Report non-compliances per **04-90-06** (Airworthiness Directives)

### For Engineering/Certification
1. Review **03_REQUIREMENTS** for requirements traceability
2. Study **04_DESIGN** and **06_ENGINEERING** for technical substantiation
3. Examine **10_CERTIFICATION** for regulatory approval documentation
4. Use **14_META_GOVERNANCE** for change control and configuration management

### For Auditors/Inspectors
1. Verify operator compliance tracking systems (**04-90-03**)
2. Check logbook entries against ALS requirements (**04-90-01**)
3. Audit cycle counts for accuracy (**11_OPERATIONS_AND_MAINTENANCE**)
4. Confirm Service Bulletin compliance (**04-90-05**)

## AMPEL360-Specific Technologies

### Hydrogen Systems (NEW)
- **04-50-01:** LH₂ tank life limit (cryogenic fatigue)
- **04-50-02:** Vacuum insulation monitoring
- **04-50-03:** Cryogenic piping flexible joints
- **04-40-04:** Fuel cell stack degradation
- **04-40-05:** H₂ pump seal life (embrittlement)
- **04-30-06:** H₂ leak detection CMR

### BWB Composite Structure (NEW)
- **04-10-05:** BWB center body life limit
- **04-10-06:** Wing root attachment (non-redundant load path)
- **04-20-02:** Composite inspection thresholds
- **04-20-06:** BWB skin panel inspection intervals
- **04-20-08:** Cold zone structure monitoring (near H₂ tank)

### High-Voltage Systems (NEW)
- **04-50-04:** Solid CO₂ battery retirement
- **04-50-05:** HV battery capacity threshold
- **04-60-05:** 800V DC insulation resistance
- **04-30-08:** HV isolation verification CMR
- **04-40-06:** Electric motor bearing life

## Regulatory Framework

### EASA Compliance
- **Part-26:** Mandatory Continuing Airworthiness Information (MCAI)
- **CS-25.571:** Damage Tolerance and Fatigue Evaluation
- **CS-25.1529:** Instructions for Continued Airworthiness
- **SC-Hydrogen:** Special Conditions for hydrogen fuel systems

### FAA Compliance
- **14 CFR §25.1529:** Instructions for Continued Airworthiness
- **AC 120-93:** Airworthiness Limitations Section
- **AC 23.573-1C:** Fatigue Test Development

### Industry Standards
- **SAE ARP4761:** Guidelines for Conducting SSA
- **SAE AIR7396:** Fuel Cell Systems for Aviation
- **ISO 14687:** Hydrogen Fuel Quality
- **SAE AS50881:** Wiring Aerospace Vehicle

## Non-Compliance Consequences

**CRITICAL:** All limitations in this chapter are **MANDATORY**.

**Immediate Effects:**
- Certificate of Airworthiness: **REVOKED**
- Aircraft: **GROUNDED**
- Operator certificate: **SUSPENDED**

**Penalties:**
- **EASA:** Up to €4,000 per day of violation
- **FAA:** Up to $50,000 per violation
- **Criminal:** Possible imprisonment if results in accident

## Support and Contact

**Technical Questions:**
- **OEM Support:** cert@ampel360.aero
- **24/7 Hotline:** +XX XXX XXX XXXX

**Regulatory Questions:**
- **EASA:** Specific certification authority contact
- **FAA:** Local FSDO (Flight Standards District Office)

**Emergency Reporting:**
- **Safety Issues:** safety@ampel360.aero (mandatory within 24 hours)
- **Limit Exceedance:** Report to authority immediately

## Document Version Control
- **Version:** 1.0.0
- **Last Updated:** 2024-10-31
- **Next Review:** 2025-10-31 (annual)
- **Change Control:** Per AMPEL-PROC-CM-001

---

**END OF NAVIGATION GUIDE**
