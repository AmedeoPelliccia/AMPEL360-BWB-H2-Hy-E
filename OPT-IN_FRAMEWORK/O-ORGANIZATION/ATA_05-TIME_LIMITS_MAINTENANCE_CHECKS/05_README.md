# ATA 05: Time Limits / Maintenance Checks

**CRITICAL GOVERNANCE NOTE:** This chapter translates the maintenance policies (ATA 01) and airworthiness limitations (ATA 04) into specific, scheduled maintenance tasks with defined intervals. ATA 05 is the operational implementation of continuing airworthiness requirements.

## Regulatory Authority
ATA 05 implements:
- **EASA Part-M.A.302:** Aircraft Maintenance Programme (AMP)
- **FAA AC 120-16F:** Air Carrier Maintenance Programs
- **MSG-3:** Maintenance Steering Group Logic (Revision 2019.1)
- **IATA Maintenance Cost Task Force:** Industry maintenance interval standards
- **EASA Part-145:** Approved Maintenance Organization requirements

## Scope and Structure
This chapter defines:
- **Maintenance Check Packages:** Phased inspection intervals (Letter Checks: A, B, C, D or equivalent)
- **Task Card Index:** Individual maintenance tasks with specific intervals
- **Time Limits:** Calendar time, flight hours, flight cycles, or condition-based thresholds
- **Special Inspections:** Event-driven or conditional maintenance requirements
- **Zonal Inspection Program:** Area-based visual inspections
- **Sampling Programs:** Statistical monitoring for reliability-based adjustments

## The 14-Folder Skeleton
Every 6-digit component represents a specific maintenance task group or check package. Each component is managed through the full lifecycle skeleton to ensure requirements traceability from MSG-3 analysis, task development, verification (mock-up trials), certification approval, and operational implementation.

## Integration with Other Chapters
- **ATA 01 (Maintenance Policy):** Strategic framework governing ATA 05 intervals
- **ATA 04 (Airworthiness Limitations):** Hard limits that ATA 05 tasks must execute
- **ATA 06-09, 12:** Servicing and handling procedures referenced by ATA 05 tasks
- **ATA 20-90 (System Chapters):** Detailed maintenance procedures for each task
- **ATA 45 (OMS/CMS):** Real-time monitoring data informing condition-based tasks
- **ATA 92 (Model-Based Maintenance):** Predictive analytics optimizing ATA 05 intervals

## AMPEL360 Maintenance Program Structure

### Traditional Letter Checks
The AMPEL360 employs a **modified MSG-3 approach** adapted for hydrogen-electric propulsion:

| Check Type | Interval | Duration | Typical Scope |
|------------|----------|----------|---------------|
| **A-Check** | 750 FH or 90 days | 10-20 hours | Visual inspections, servicing, minor component replacement |
| **2A-Check** | 1,500 FH or 180 days | 20-40 hours | Enhanced A-Check with additional systems testing |
| **B-Check** | 4,500 FH or 18 months | 3-5 days | Detailed inspections, NDT sampling, systems functional tests |
| **C-Check** | 9,000 FH or 24 months | 2-3 weeks | Structural inspections, major component overhaul, full systems validation |
| **D-Check** | 36,000 FH or 10 years | 2-3 months | Heavy maintenance, full aircraft disassembly/inspection, refurbishment |

### Hydrogen-Specific Adaptations
- **H2-Supplemental Checks (HS-Checks):** Additional cryogenic system inspections at 300 FH intervals
- **Thermal Cycle Monitoring:** Independent tracking of LH₂ fill/drain events (not purely FH-based)
- **Fuel Cell Performance Validation:** 600 FH impedance spectroscopy testing
- **Vacuum Integrity Verification:** 1,200 FH pressure decay tests

### BWB Composite Structure Inspections
- **Impact Damage Surveys:** Enhanced visual/tap-test inspections every 1,500 FH
- **Thermographic Inspections:** IR scanning of composite panels every 9,000 FH
- **Ultrasonic Thickness Surveys:** Full wing skin UT mapping every 18,000 FH

## Task Numbering Convention
ATA 05 uses a hierarchical task numbering system:

```
05-XX-YY-ZZZ-TTT
│  │  │  │   │
│  │  │  │   └─ Task Type (001-999)
│  │  │  └───── Task Group (e.g., 100=Visual Inspection, 400=Functional Test)
│  │  └──────── Subject (e.g., 01=LH2 Tank, 02=Fuel Cells)
│  └─────────── Section (e.g., 10=Check Packages, 20=Task Cards)
└────────────── Chapter 05
```

**Example:**
- **05-20-01-100-001:** A-Check, LH₂ Tank, Visual Inspection, External Surface Inspection
- **05-20-01-400-005:** C-Check, LH₂ Tank, Functional Test, Vacuum Pressure Decay Test

## Maintenance Task Intervals

### Interval Types
1. **Flight Hours (FH):** Hobbs meter / ACMS recorded hours
2. **Flight Cycles (FC):** Takeoff/landing count
3. **Calendar Time (CY/MO/DY):** Elapsed time since manufacture or last compliance
4. **Thermal Cycles (TC):** Cryogenic fill/drain events (H₂-specific)
5. **On-Condition (OC):** Finding-based, no fixed interval
6. **Condition Monitoring (CM):** Real-time sensor data thresholds

### Escalation Factors
ATA 05 tasks incorporate **tolerance bands** to enable maintenance planning flexibility:
- **Early Compliance:** Tasks may be performed up to 10% early without reset of interval
- **Late Compliance:** NOT permitted for CMR tasks; ±5% for non-critical tasks with engineering approval

## Compliance Tracking
All ATA 05 tasks are tracked via:
- **Aircraft Maintenance Tracking System (AMTS):** Digital work package generation
- **Electronic Logbook:** Part-M.A.305/306 compliant records
- **ACMS Integration:** Automated FH/FC tracking via ATA 45 systems
- **QR Code Task Cards:** S1000D digital maintenance procedures with NFC tags

## Special Considerations for AMPEL360

### Hydrogen Safety
- **Pre-Maintenance Purging:** All H₂ system work requires GN₂ purge per AMM 28-00-00
- **Leak Testing:** Mandatory post-maintenance pressure test for any H₂ system opening
- **Personnel Qualification:** Cryogenic systems require Type Rating + H₂ Safety Course

### BWB Access Challenges
- **Limited Access Panels:** BWB structure requires specialized tooling for internal access
- **Non-Destructive Inspection (NDI):** Heavy reliance on advanced NDT due to composite design
- **Mock-Up Trials:** All new tasks validated on full-scale mockup before fleet introduction

### Environmental Conditions
- **Cold Soak Requirements:** Post-flight inspections must account for cryogenic cold zones
- **Thermal Stabilization:** Structure must reach ambient temperature before composite repairs
- **Humidity Control:** Fuel cell and battery compartments require <30% RH during maintenance

## Reliability Program Integration
ATA 05 intervals are subject to continuous optimization via:
- **Fleet Reliability Monitoring:** ATA 01-10-05 Reliability Program
- **Service Difficulty Reporting (SDR):** FAA/EASA mandatory reporting
- **Operator Feedback:** AMPEL360 Maintenance Steering Committee (quarterly reviews)
- **Predictive Analytics:** ATA 92 Model-Based Maintenance AI interval recommendations

## Revision Control
Changes to ATA 05 intervals require:
1. **MSG-3 Re-Analysis:** Documented justification for interval change
2. **Reliability Data Review:** Minimum 50,000 FH fleet experience (unless safety-driven)
3. **Regulatory Approval:** EASA Part-M approval for AMP amendment
4. **Service Bulletin (SB):** Formal notification to all operators
5. **Maintenance Planning Document (MPD) Revision:** Updated task intervals published

## Directory Structure

```
/O-ORGANIZATION
└── /ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS
    ├── 05_README.md
    ├── INDEX.meta.yaml
    │
    ├── /05-10_MAINTENANCE_CHECK_PACKAGES
    │   ├── /05-10-01_A_Check_Package
    │   ├── /05-10-02_2A_Check_Package
    │   ├── /05-10-03_B_Check_Package
    │   ├── /05-10-04_C_Check_Package
    │   ├── /05-10-05_D_Check_Package
    │   ├── /05-10-06_HS_Check_H2_Supplemental
    │   └── /05-10-07_Check_Interval_Optimization
    │
    ├── /05-20_TASK_CARD_INDEX
    │   ├── /05-20-01_LH2_System_Tasks
    │   ├── /05-20-02_Fuel_Cell_System_Tasks
    │   ├── /05-20-03_CO2_Capture_System_Tasks
    │   ├── /05-20-04_BWB_Structure_Tasks
    │   ├── /05-20-05_Propulsion_System_Tasks
    │   ├── /05-20-06_Flight_Control_System_Tasks
    │   ├── /05-20-07_Electrical_Power_System_Tasks
    │   ├── /05-20-08_Environmental_Control_System_Tasks
    │   ├── /05-20-09_Landing_Gear_Tasks
    │   └── /05-20-10_Avionics_System_Tasks
    │
    ├── /05-30_STRUCTURAL_INSPECTION_PROGRAM
    │   ├── /05-30-01_Zonal_Inspection_Schedule
    │   ├── /05-30-02_Supplemental_Structural_Inspection_Program_SSIP
    │   ├── /05-30-03_Corrosion_Prevention_Control_Program_CPCP
    │   ├── /05-30-04_BWB_Composite_Inspection_Program
    │   ├── /05-30-05_Cryogenic_Cold_Zone_Inspection
    │   ├── /05-30-06_Damage_Tolerance_Inspection_Intervals
    │   └── /05-30-07_NDT_Inspection_Schedule
    │
    ├── /05-40_POWERPLANT_TIME_LIMITS
    │   ├── /05-40-01_Turbine_Engine_Shop_Visit_Intervals
    │   ├── /05-40-02_Propulsor_Overhaul_Intervals
    │   ├── /05-40-03_Fuel_Cell_Stack_Replacement_Schedule
    │   ├── /05-40-04_Electric_Motor_Bearing_Inspection_Intervals
    │   ├── /05-40-05_Gearbox_Inspection_Intervals
    │   └── /05-40-06_H2_Fuel_System_Component_Intervals
    │
    ├── /05-50_SYSTEMS_COMPONENT_TIME_LIMITS
    │   ├── /05-50-01_Hydraulic_Component_Overhaul_Intervals
    │   ├── /05-50-02_Flight_Control_Actuator_Intervals
    │   ├── /05-50-03_Landing_Gear_Overhaul_Intervals
    │   ├── /05-50-04_Oxygen_System_Component_Intervals
    │   ├── /05-50-05_Fire_Extinguisher_Replacement_Intervals
    │   ├── /05-50-06_Emergency_Equipment_Inspection_Intervals
    │   ├── /05-50-07_CO2_Battery_Module_Replacement
    │   └── /05-50-08_High_Voltage_System_Component_Intervals
    │
    ├── /05-60_LIFE_LIMITED_PARTS_REPLACEMENT
    │   ├── /05-60-01_Life_Limited_Parts_Index
    │   ├── /05-60-02_LH2_Tank_Replacement_Schedule
    │   ├── /05-60-03_Turbine_Disc_Replacement
    │   ├── /05-60-04_Landing_Gear_Life_Limited_Parts
    │   ├── /05-60-05_Flight_Control_Life_Limited_Parts
    │   └── /05-60-06_Cryogenic_Line_Flexible_Joint_Replacement
    │
    ├── /05-70_SAMPLING_PROGRAMS
    │   ├── /05-70-01_Engine_Oil_Analysis_Program
    │   ├── /05-70-02_Hydraulic_Fluid_Analysis_Program
    │   ├── /05-70-03_Fuel_Cell_Coolant_Analysis_Program
    │   ├── /05-70-04_Composite_Material_Moisture_Sampling
    │   ├── /05-70-05_EWIS_Connector_Sampling_Program
    │   └── /05-70-06_H2_Purity_Analysis_Program
    │
    ├── /05-80_CONDITION_BASED_MAINTENANCE
    │   ├── /05-80-01_On_Condition_Task_Index
    │   ├── /05-80-02_Condition_Monitoring_Thresholds
    │   ├── /05-80-03_Real_Time_Health_Monitoring_Integration
    │   ├── /05-80-04_Predictive_Maintenance_Task_Triggers
    │   ├── /05-80-05_Fuel_Cell_Performance_Monitoring
    │   └── /05-80-06_Battery_State_of_Health_Monitoring
    │
    └── /05-90_SPECIAL_INSPECTIONS
        ├── /05-90-01_Post_Heavy_Landing_Inspection_Tasks
        ├── /05-90-02_Lightning_Strike_Inspection_Tasks
        ├── /05-90-03_Overweight_Landing_Inspection_Tasks
        ├── /05-90-04_Cryogenic_System_Leak_Event_Tasks
        ├── /05-90-05_Fuel_Cell_Failure_Inspection_Tasks
        └── /05-90-06_Thermal_Exceedance_Inspection_Tasks
```

Each component contains the full 14-folder lifecycle skeleton:
1. `01_OVERVIEW`
2. `02_SAFETY`
3. `03_REQUIREMENTS`
4. `04_DESIGN`
5. `05_INTERFACES`
6. `06_ENGINEERING`
7. `07_V_AND_V`
8. `08_PROTOTYPING`
9. `09_PRODUCTION_PLANNING`
10. `10_CERTIFICATION`
11. `11_OPERATIONS_AND_MAINTENANCE`
12. `12_ASSETS_MANAGEMENT`
13. `13_SUBSYSTEMS_AND_COMPONENTS`
14. `14_META_GOVERNANCE`
