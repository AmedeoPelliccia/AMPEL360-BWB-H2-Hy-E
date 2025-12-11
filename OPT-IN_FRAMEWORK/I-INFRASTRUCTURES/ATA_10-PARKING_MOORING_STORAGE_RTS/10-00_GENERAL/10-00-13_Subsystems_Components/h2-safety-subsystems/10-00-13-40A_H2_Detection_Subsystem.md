# 10-00-13-40A — H2 Detection Subsystem

## 1. Document Information

| Field | Value |
|-------|-------|
| **Document ID** | 10-00-13-40A |
| **Document Number** | 10-00-13-40A_H2_Detection_Subsystem |
| **Title** | H2 Detection Subsystem |
| **Revision** | A |
| **Status** | DRAFT |
| **Date** | 2025-12-11 |
| **Subsystem Type** | h2-safety |
| **Subsystem ID** | H2-DETECT-001 |
| **Parent System** | H2 Safety System (10-00-13-05A) |
| **Safety Critical** | Yes |
| **DAL Level** | B |

## 2. Purpose

The H2 Detection Subsystem provides continuous monitoring and detection of hydrogen gas concentrations in designated zones around the AMPEL360-BWB-H2 aircraft during ground operations. It is a **safety-critical subsystem** designed to detect hydrogen leaks before they reach hazardous concentrations, enabling timely activation of alarms and emergency shutdown systems.

## 3. Scope

### 3.1 In Scope

- Fixed H2 gas detection sensors at strategic locations
- Portable H2 detection equipment for mobile monitoring
- Sensor signal processing and concentration calculation
- Integration with H2 Alarm Subsystem (10-00-13-42A)
- Integration with H2 Emergency Shutdown Subsystem (10-00-13-43A)
- Self-diagnostics and sensor health monitoring
- Detection zone definition and coverage verification

### 3.2 Out of Scope

- Fire detection (covered by ATA 26 Fire Protection)
- Oxygen concentration monitoring (covered by facility systems)
- Hydrocarbon fuel detection (conventional fuel systems)
- Post-event forensic analysis (covered by incident investigation procedures)

## 4. Functional Description

### 4.1 Primary Functions

1. **Continuous H2 Monitoring** - 24/7 monitoring of designated H2 hazard zones
2. **Multi-Level Detection** - Staged alarm thresholds (25% LEL, 50% LEL, 75% LEL)
3. **Redundant Sensing** - Multiple sensors per zone with voting logic
4. **Rapid Response** - Detection and alarm within 2 seconds of threshold exceedance
5. **Self-Diagnostics** - Continuous sensor health checks and fault detection
6. **Data Logging** - Historical concentration data for trend analysis

### 4.2 Operational Modes

| Mode | Description | Active Sensors |
|------|-------------|----------------|
| **Normal** | Standard monitoring during routine operations | All zone sensors |
| **Fueling** | Enhanced sensitivity during H2 fueling | All sensors + portable |
| **Maintenance** | Selective sensor operation during maintenance | Zone-specific |
| **Standby** | Reduced monitoring when aircraft secured | Critical zones only |
| **Test** | Sensor calibration and functional test | Test target sensors |

## 5. Architecture

### 5.1 System Components

```
H2 Detection Subsystem
├── Detection Zones
│   ├── Zone 1: Fueling Interface Area
│   ├── Zone 2: Aft Fuselage LH2 Tank Access
│   ├── Zone 3: Forward Fuselage LH2 Tank Access
│   ├── Zone 4: Vent System Outlet
│   └── Zone 5: Ground Equipment Staging
│
├── Sensor Arrays
│   ├── Catalytic Bead Sensors (CBS)
│   ├── Electrochemical Sensors (EC)
│   └── Thermal Conductivity Sensors (TCD)
│
├── Signal Processing
│   ├── Sensor Signal Conditioning
│   ├── Concentration Calculation
│   ├── Multi-Sensor Voting Logic
│   └── Fault Detection and Isolation
│
└── Interfaces
    ├── H2 Alarm Subsystem (10-00-13-42A)
    ├── H2 Emergency Shutdown (10-00-13-43A)
    ├── H2 Monitoring Subsystem (10-00-13-44A)
    └── Ground Control Station
```

### 5.2 Detection Zones

| Zone | Location | Sensor Count | Redundancy | LEL Threshold |
|------|----------|--------------|------------|---------------|
| Zone 1 | Fueling interface (aft fuselage) | 4 | 2-of-3 voting | 25% LEL |
| Zone 2 | Aft LH2 tank access | 3 | 2-of-3 voting | 25% LEL |
| Zone 3 | Forward LH2 tank access | 3 | 2-of-3 voting | 25% LEL |
| Zone 4 | Vent system outlet (above fuselage) | 2 | Redundant | 50% LEL |
| Zone 5 | Ground equipment staging area | 2 | Redundant | 25% LEL |

**Total Fixed Sensors:** 14  
**Portable Sensors:** 4 (operator-carried during fueling)

## 6. Sensor Types and Specifications

### 6.1 Catalytic Bead Sensors (CBS)

**Technology:** Catalytic oxidation of H2 on heated platinum bead

| Parameter | Specification |
|-----------|---------------|
| Detection Range | 0 - 100% LEL |
| Accuracy | ±5% LEL |
| Response Time | < 10 seconds (T90) |
| Operating Temp | -40°C to +60°C |
| Lifespan | 3 years (typical) |
| Calibration Interval | 6 months |

**Locations:** Zones 1, 2, 3, 5 (primary detection)

### 6.2 Electrochemical Sensors (EC)

**Technology:** Electrochemical cell with H2-specific electrolyte

| Parameter | Specification |
|-----------|---------------|
| Detection Range | 0 - 1000 ppm |
| Accuracy | ±10 ppm or ±5% reading |
| Response Time | < 15 seconds (T90) |
| Operating Temp | -20°C to +50°C |
| Lifespan | 2 years (typical) |
| Calibration Interval | 6 months |

**Locations:** All zones (backup/verification)

### 6.3 Thermal Conductivity Detectors (TCD)

**Technology:** Thermal conductivity differential measurement

| Parameter | Specification |
|-----------|---------------|
| Detection Range | 0 - 100% volume |
| Accuracy | ±2% volume |
| Response Time | < 5 seconds (T90) |
| Operating Temp | -40°C to +80°C |
| Lifespan | 5 years (typical) |
| Calibration Interval | 12 months |

**Locations:** Zone 4 (vent outlet - high concentration possible)

## 7. Detection Thresholds and Response

### 7.1 Alarm Levels

| Level | Concentration | Response Time | Actions Triggered |
|-------|--------------|---------------|-------------------|
| **Level 1 (Caution)** | 25% LEL (1% vol) | < 2 seconds | • Visual alarm<br>• Log event<br>• Alert operator |
| **Level 2 (Warning)** | 50% LEL (2% vol) | < 2 seconds | • Audio + visual alarm<br>• Alert supervisor<br>• Activate ventilation |
| **Level 3 (Danger)** | 75% LEL (3% vol) | < 1 second | • Evacuation alarm<br>• Emergency shutdown (ESD)<br>• Isolate H2 sources |

**LEL (Lower Explosive Limit) for H2 in air:** 4% by volume  
**UEL (Upper Explosive Limit) for H2 in air:** 75% by volume

### 7.2 Voting Logic

For zones with 3+ sensors, **2-of-3 voting** is used:
- If 2 or more sensors detect ≥ threshold → Alarm triggered
- If 1 sensor detects → Verify with backup sensor, log anomaly
- If sensor disagrees significantly → Flag sensor fault

## 8. Component List

| Component ID | Component Name | Part Number | Qty | Criticality |
|--------------|----------------|-------------|-----|-------------|
| H2-DETECT-CBS-01 | Catalytic Bead Sensor | CBS-H2-LEL-100 | 10 | Critical |
| H2-DETECT-EC-01 | Electrochemical Sensor | EC-H2-1000PPM | 6 | Essential |
| H2-DETECT-TCD-01 | Thermal Conductivity Detector | TCD-H2-100VOL | 2 | Important |
| H2-DETECT-PORT-01 | Portable H2 Detector | PORT-H2-MULTI | 4 | Essential |
| H2-DETECT-CTRL-01 | Detection Controller (PLC) | PLC-H2-DETECT | 2 | Critical |
| H2-DETECT-PWR-01 | Power Supply (24VDC UPS) | PSU-24V-UPS-20A | 2 | Critical |
| H2-DETECT-CABLE-01 | Sensor Cable (shielded) | CAB-SHIELD-4C-50M | 1 spool | Standard |
| H2-DETECT-JB-01 | Junction Box (ATEX rated) | JB-ATEX-IP67 | 5 | Important |

## 9. Interfaces

### 9.1 Input Interfaces

| Interface ID | Source | Type | Description |
|--------------|--------|------|-------------|
| IF-H2D-001 | CBS Sensors | Analog | 4-20 mA current loop (% LEL) |
| IF-H2D-002 | EC Sensors | Analog | 0-10 VDC (ppm) |
| IF-H2D-003 | TCD Sensors | Analog | 4-20 mA current loop (% vol) |
| IF-H2D-004 | Power Supply | Electrical | 24 VDC ±10%, battery-backed |

### 9.2 Output Interfaces

| Interface ID | Destination | Type | Description |
|--------------|-------------|------|-------------|
| IF-H2D-101 | H2 Alarm (10-00-13-42A) | Digital | Alarm level signals (relay contacts) |
| IF-H2D-102 | H2 ESD (10-00-13-43A) | Digital | Emergency shutdown trigger (relay) |
| IF-H2D-103 | H2 Monitor (10-00-13-44A) | Data | Concentration data (Modbus TCP) |
| IF-H2D-104 | Ground Control Station | Data | HMI display and data logging (Ethernet) |

## 10. Safety Features

### 10.1 Redundancy

- **Sensor Redundancy:** Multiple sensors per zone with voting logic
- **Power Redundancy:** Dual power supplies with automatic failover
- **Controller Redundancy:** Hot-standby PLC configuration
- **Communication Redundancy:** Dual Ethernet paths for critical signals

### 10.2 Fail-Safe Design

- **Sensor Failure:** Triggers alarm condition (fail-safe high)
- **Power Loss:** Battery backup maintains operation for 4 hours
- **Communication Loss:** Local alarm activation (hardwired relays)
- **Controller Failure:** Watchdog triggers failover to standby controller

### 10.3 Self-Diagnostics

- **Sensor Health Checks:** Continuous monitoring of sensor status
- **Calibration Drift Detection:** Automatic comparison with reference
- **Circuit Continuity:** Wire break detection for all sensor loops
- **Power Quality Monitoring:** Voltage and current monitoring

## 11. Requirements Traceability

| Requirement ID | Requirement Description | Verification Method |
|---------------|-------------------------|---------------------|
| REQ-10-H2D-001 | Detect H2 ≥ 25% LEL within 2 seconds | Test with calibration gas |
| REQ-10-H2D-002 | Provide redundant sensing in critical zones | Design review + inspection |
| REQ-10-H2D-003 | Operate in temperature range -40°C to +60°C | Environmental testing |
| REQ-10-H2D-004 | Maintain operation on battery for 4 hours | Endurance test |
| REQ-10-H2D-005 | Interface with alarm and ESD systems | Integration testing |
| REQ-10-H2D-006 | Self-diagnostic capability for all sensors | Functional test |

## 12. Hazard Mitigation

| Hazard ID | Hazard Description | Mitigation by this Subsystem |
|-----------|-------------------|------------------------------|
| H-10-001 | H2 leak during fueling undetected | Multi-sensor detection in Zone 1 |
| H-10-002 | LH2 vaporization creating H2 cloud | Zone 2/3 sensors detect vapor |
| H-10-004 | Slow H2 leak during long-term parking | Continuous monitoring in standby mode |
| H-10-012 | Sensor failure masks actual leak | Redundant sensors with voting logic |

## 13. Operational Domain

| Parameter | Min | Typical | Max | Unit |
|-----------|-----|---------|-----|------|
| Ambient Temperature | -40 | +20 | +60 | °C |
| Relative Humidity | 0 | 60 | 95 | % RH (non-condensing) |
| Atmospheric Pressure | 800 | 1013 | 1100 | mbar |
| Wind Speed | 0 | - | 50 | kt (sensor calibration limits) |

## 14. Calibration and Maintenance

### 14.1 Calibration Schedule

| Sensor Type | Interval | Calibration Gas | Acceptance Criteria |
|-------------|----------|-----------------|---------------------|
| CBS | 6 months | 50% LEL H2 in air | ±5% LEL |
| EC | 6 months | 500 ppm H2 in N2 | ±10 ppm |
| TCD | 12 months | 10% H2 in N2 | ±2% vol |

### 14.2 Preventive Maintenance

- **Monthly:** Visual inspection of sensors and wiring
- **Quarterly:** Functional test with calibration gas
- **Semi-Annually:** Full calibration and performance verification
- **Annually:** Sensor replacement (CBS, EC) or as needed

## 15. Applicable Standards

- **NFPA 2** - Hydrogen Technologies Code (Section 7.4 Detection)
- **EN 60079-29-1** - Gas detectors - Performance requirements (Ex equipment)
- **IEC 60079-29-1** - Explosive atmospheres - Gas detectors (Part 1: Performance requirements)
- **SAE AS6968** - Hydrogen Aircraft GSE (Appendix C: Detection Systems)
- **ISO 26142** - Hydrogen detection apparatus - Stationary applications
- **ATEX 2014/34/EU** - Equipment in potentially explosive atmospheres
- **IECEx** - International Electrotechnical Commission Ex certification

## 16. Related Documentation

- [10-00-13-05A - H2 Safety System Architecture](10-00-13-05A_H2_Safety_System_Architecture.md)
- [10-00-13-41A - H2 Venting Subsystem](10-00-13-41A_H2_Venting_Subsystem.md)
- [10-00-13-42A - H2 Alarm Subsystem](10-00-13-42A_H2_Alarm_Subsystem.md)
- [10-00-13-43A - H2 Emergency Shutdown Subsystem](10-00-13-43A_H2_Emergency_Shutdown_Subsystem.md)
- [10-00-13-44A - H2 Monitoring Subsystem](10-00-13-44A_H2_Monitoring_Subsystem.md)
- [10-00-02-005-A - LH2 Properties and Hazards](../../10-00-02_Safety/10-00-02-005_H2_Specific_Safety/10-00-02-005-A_LH2_Properties_Hazards.md)

## 17. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-11 | AI/Copilot (Amedeo Pelliccia) | Initial subsystem specification |

## 18. Document Control

| Field | Value |
|-------|-------|
| **Status** | DRAFT |
| **Owner** | AMPEL360 H2 Safety Engineering WG |
| **Approver** | _[to be completed]_ |
| **Classification** | Internal Use |
| **Next Review** | 2026-03-11 |

---

**AI Generation Note:**

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-11

---

*End of Document*
