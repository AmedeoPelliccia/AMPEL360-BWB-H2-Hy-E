# 03-00-12-03-01A - Ground Power Service

## 1. Purpose
This document specifies ground electrical power services for AMPEL360 aircraft during ground operations, including AC and DC power supply for aircraft systems while engines are not running.

## 2. Scope
This service specification covers:
- AC ground power supply (115V/200V 400Hz)
- DC ground power supply (28VDC)
- High-voltage DC systems for hybrid-electric propulsion
- Power quality monitoring and conditioning
- Connection/disconnection procedures
- Emergency backup power systems

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- IATA Airport Handling Manual (AHM)
- SAE AS50881 (Wiring, Aerospace Vehicle)
- MIL-STD-704 (Aircraft Electric Power Characteristics)
- ISO 6858 (Aircraft Ground Support Equipment - Electrical Supplies)

## 4. Service Description

### 4.1 Overview
Ground Power Service provides reliable electrical power to aircraft during ground operations, supporting avionics, cabin systems, auxiliary equipment, and battery charging for the hybrid-electric propulsion system.

### 4.2 Service Specifications
| Parameter | Specification | SLA Target |
|-----------|---------------|------------|
| AC Power Output | 90 kVA @ 115/200V 400Hz | ±5% voltage, ±0.5% frequency |
| DC Power Output | 1500A @ 28VDC | ±2% voltage |
| HV-DC Output (Hybrid System) | 50 kW @ 540VDC | ±3% voltage |
| Connection Time | ≤ 5 minutes | From aircraft arrival |
| Power Quality (THD) | <5% | Total Harmonic Distortion |
| Availability | 99.5% | Operational readiness |
| Load Response Time | <100ms | Load change to stabilization |

### 4.3 Service Delivery Process
1. **Pre-Connection**: Equipment positioning, safety verification, aircraft electrical system verification
2. **Connection**: Grounding establishment, power cable connection, load verification
3. **Power Transfer**: Gradual load application, aircraft systems activation monitoring
4. **Monitoring**: Continuous power quality and load monitoring during service
5. **Disconnection**: Load reduction, cable removal, equipment securing
6. **Post-Service**: Documentation and equipment status verification

## 5. Service Level Agreement
| Metric | Target | Measurement |
|--------|--------|-------------|
| Service Availability | 99.5% | Monthly uptime |
| Power Quality Compliance | 100% | Within MIL-STD-704 limits |
| Connection Success Rate | 99% | First-attempt connections |
| Response Time | ≤ 10 minutes | Emergency power requests |
| Equipment Reliability | 95% MTBF | Mean time between failures >500 hours |
| Safety Incident Rate | Zero | Electrical incidents per 10,000 connections |

## 6. Safety Requirements
- Mandatory grounding before power connection
- Interlocks prevent connection with aircraft systems energized
- Ground Fault Circuit Interrupter (GFCI) protection
- Emergency disconnect capability (manual and automatic)
- Personnel must maintain safe distance during connection/disconnection
- Regular electrical safety testing and equipment inspection
- Arc flash protection and PPE requirements enforced

## 7. Cross-References
- Related ATA Chapters: ATA 24 (Electrical Power), ATA 03-10 (Operations)
- Parent Document: [03-00-12_Services](../)
- Related Services: [03-00-12-03-02A_Battery_Charging_Service.md](./03-00-12-03-02A_Battery_Charging_Service.md)
- Electrical Testing: [03-00-12-03-03A_Electrical_Testing_Service.md](./03-00-12-03-03A_Electrical_Testing_Service.md)
- Maintenance: [03-00-12-05_GSE_Maintenance_Services](../03-00-12-05_GSE_Maintenance_Services/)

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
