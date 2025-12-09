# 03-00-12-03-04A - Power Quality Service

## 1. Purpose
This document specifies power quality monitoring and management services for AMPEL360 aircraft and ground support equipment electrical systems.

## 2. Scope
This service specification covers:
- Real-time power quality monitoring
- Harmonic analysis and mitigation
- Voltage regulation and stabilization
- Power factor correction
- Transient suppression
- Load balancing for ground power systems

## 3. Applicable Documents
- MIL-STD-704 (Aircraft Electric Power Characteristics)
- IEEE 519 (Recommended Practices for Harmonic Control)
- IEC 61000 (Electromagnetic Compatibility)
- SAE AS50881 (Wiring, Aerospace Vehicle)
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)

## 4. Service Description

### 4.1 Overview
Power Quality Service ensures that electrical power supplied to aircraft meets stringent quality requirements, protecting sensitive avionics and propulsion systems from power disturbances.

### 4.2 Service Specifications
| Parameter | Specification | SLA Target |
|-----------|---------------|------------|
| Voltage Regulation | ±5% nominal | 115V ±5.75V, 28V ±1.4V |
| Frequency Stability (AC) | 400 Hz ±0.5% | ±2 Hz maximum deviation |
| Total Harmonic Distortion (THD) | <5% | Per MIL-STD-704 |
| Power Factor | ≥0.95 | With active correction |
| Transient Suppression | <50V peak | Overvoltage protection |
| Monitoring Sample Rate | 10 kHz | Real-time data capture |
| Response to Power Quality Event | <100ms | Automatic correction |

### 4.3 Service Delivery Process
1. **Baseline Monitoring**: Continuous power quality monitoring during all ground operations
2. **Analysis**: Real-time analysis of voltage, current, frequency, harmonics
3. **Event Detection**: Identification of power quality excursions
4. **Automatic Correction**: Active power conditioning and regulation
5. **Alert Generation**: Notification of persistent or severe power quality issues
6. **Reporting**: Daily/weekly power quality summaries and trend analysis
7. **Corrective Action**: Recommendations and implementation of power quality improvements

## 5. Service Level Agreement
| Metric | Target | Measurement |
|--------|--------|-------------|
| Monitoring Uptime | 99.9% | Continuous monitoring availability |
| Voltage Compliance | 99% | Time within specified limits |
| Frequency Compliance (AC) | 99.5% | Time within ±0.5% of nominal |
| THD Compliance | 95% | Time within <5% THD |
| Power Factor | ≥0.95 | Average monthly power factor |
| Response Time to Events | <100ms | Automatic correction activation |
| Monthly Reporting | 100% | On-time delivery of quality reports |

## 6. Safety Requirements
- Power quality monitoring systems have backup power supplies
- Automatic disconnection on critical power quality failures
- Voltage surge protection on all power connections
- Regular calibration of monitoring equipment
- Alert systems for out-of-tolerance conditions
- Emergency power backup for critical aircraft systems during power quality events

## 7. Cross-References
- Related ATA Chapters: ATA 24 (Electrical Power), MIL-STD-704 compliance
- Parent Document: [03-00-12_Services](../)
- Related Services:
  - [03-00-12-03-01A_Ground_Power_Service.md](./03-00-12-03-01A_Ground_Power_Service.md)
  - [03-00-12-03-02A_Battery_Charging_Service.md](./03-00-12-03-02A_Battery_Charging_Service.md)
  - [03-00-12-03-03A_Electrical_Testing_Service.md](./03-00-12-03-03A_Electrical_Testing_Service.md)
- Maintenance: [03-00-12-05_GSE_Maintenance_Services](../03-00-12-05_GSE_Maintenance_Services/)
- Technical Support: [03-00-12-07_GSE_Technical_Support](../03-00-12-07_GSE_Technical_Support/)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Status:** DRAFT – Subject to human review and approval
- **Generated with assistance from:** GitHub Copilot, prompted by Amedeo Pelliccia
- **Repository:** AMPEL360-BWB-H2-Hy-E
- **Last AI update:** 2025-12-07
