# 03-00-12-03-02A - Battery Charging Service

## 1. Purpose
This document specifies battery charging services for AMPEL360 aircraft, including main propulsion batteries for the hybrid-electric system and auxiliary battery systems.

## 2. Scope
This service specification covers:
- High-voltage battery charging for hybrid propulsion system
- Auxiliary battery charging (28VDC systems)
- Battery management system interface
- Charging rate control and monitoring
- Battery health assessment during charging

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- SAE J1772 (Electric Vehicle Conductive Charge Coupler)
- IEC 62196 (Plugs, Socket-Outlets, Vehicle Connectors)
- UL 2202 (Electric Vehicle Charging System Equipment)
- ATA 24 (Electrical Power)

## 4. Service Description

### 4.1 Overview
Battery Charging Service provides safe, efficient charging for aircraft battery systems, with specialized capabilities for high-voltage propulsion batteries and standard auxiliary batteries.

### 4.2 Service Specifications
| Parameter | Specification | SLA Target |
|-----------|---------------|------------|
| HV Battery Charging Power | Up to 350 kW | Fast-charging capability |
| HV Battery Voltage Range | 400-800 VDC | Compatible with aircraft BMS |
| Auxiliary Battery Charging | 28 VDC, 200A | Standard aviation battery systems |
| Charging Efficiency | ≥95% | Energy conversion efficiency |
| Connection Time | ≤ 10 minutes | From aircraft arrival |
| Full Charge Time (HV) | 45-90 minutes | Dependent on state of charge |
| Battery Health Monitoring | Real-time | BMS integration |

### 4.3 Service Delivery Process
1. **Pre-Charge Assessment**: Battery state of charge verification, BMS communication check
2. **Connection**: High-voltage interlocks verification, charging cable connection
3. **Charging Initiation**: BMS handshake, charging profile selection, power ramp-up
4. **Active Charging**: Continuous monitoring of voltage, current, temperature, cell balance
5. **Charging Completion**: Controlled power ramp-down, final battery conditioning
6. **Disconnection**: Safe high-voltage disconnect procedures, cable removal
7. **Post-Charge Report**: Battery health summary, charging efficiency metrics

## 5. Service Level Agreement
| Metric | Target | Measurement |
|--------|--------|-------------|
| Service Availability | 99% | Charging system uptime |
| Charging Success Rate | 98% | Successful charge completions |
| Charging Efficiency | ≥95% | Energy delivered vs. consumed |
| Battery Health Monitoring | 100% | All parameters logged |
| Safety Incident Rate | Zero | Charging-related safety events |
| Equipment Reliability | 98% | Charger uptime |

## 6. Safety Requirements
- High-voltage safety interlocks mandatory
- Emergency disconnect systems (manual and automatic)
- Continuous battery temperature monitoring
- Thermal runaway detection and suppression
- Ground Fault Protection (GFP) active during all charging
- Personnel must complete HV electrical safety training
- Minimum 3-meter safety zone during HV charging operations
- Fire suppression systems active and tested

## 7. Cross-References
- Related ATA Chapters: ATA 24 (Electrical Power), ATA 49 (APU - Battery systems)
- Parent Document: [03-00-12_Services](../)
- Related Services: [03-00-12-03-01A_Ground_Power_Service.md](./03-00-12-03-01A_Ground_Power_Service.md)
- Electrical Testing: [03-00-12-03-03A_Electrical_Testing_Service.md](./03-00-12-03-03A_Electrical_Testing_Service.md)
- Maintenance: [03-00-12-05_GSE_Maintenance_Services](../03-00-12-05_GSE_Maintenance_Services/)
- Training: [03-00-12-06_GSE_Training_Services](../03-00-12-06_GSE_Training_Services/)

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
