# 03-00-12-02-01A - LH2 Fueling Service

## 1. Purpose
This document specifies the service requirements and procedures for Liquid Hydrogen (LH2) fueling operations supporting AMPEL360 BWB H2-Hybrid Electric aircraft.

## 2. Scope
This service specification covers:
- LH2 refueling procedures and protocols
- Cryogenic fuel handling requirements
- Safety procedures and emergency response
- Equipment specifications and maintenance
- Personnel qualification and training requirements

## 3. Applicable Documents
- SAE AS6968 (Hydrogen Aircraft Refueling)
- ISO 19880-8 (Gaseous Hydrogen - Fueling Stations - Part 8: Fuel Quality Control)
- NFPA 2 (Hydrogen Technologies Code)
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- EASA/FAA Hydrogen Safety Guidelines
- IATA Airport Handling Manual (AHM) - Hydrogen Operations Addendum

## 4. Service Description

### 4.1 Overview
LH2 fueling service provides safe and efficient transfer of liquid hydrogen fuel from ground storage systems to aircraft fuel tanks. The service requires specialized cryogenic equipment, highly trained personnel, and stringent safety protocols.

### 4.2 Service Specifications
| Parameter | Specification | SLA Target |
|-----------|---------------|------------|
| Fuel Temperature | -253°C (-423°F) | ±2°C control |
| Fuel Purity | ≥99.99% | Verified per ISO 19880-8 |
| Fill Rate | 500-1500 kg/hour | Variable by aircraft configuration |
| Fuel Transfer Pressure | 2-5 bar | Monitored continuously |
| Connection Time | ≤ 10 minutes | From arrival to ready-to-fuel |
| Disconnection Time | ≤ 5 minutes | After fueling complete |
| Ambient Condition Limits | -20°C to +45°C | Service availability range |

### 4.3 Service Delivery Process
1. **Pre-Arrival Preparation**: Fuel quantity calculation, equipment positioning, safety zone establishment
2. **Aircraft Arrival**: Ground crew positioning, safety verification, communication establishment
3. **Connection Phase**: Bonding, coupling attachment, leak testing (mandatory)
4. **Fueling Phase**: Automated transfer with continuous monitoring, temperature/pressure tracking
5. **Completion Phase**: System purge, coupling disconnection, safety verification
6. **Post-Service**: Equipment securing, documentation, quality records

## 5. Service Level Agreement
| Metric | Target | Measurement |
|--------|--------|-------------|
| Service Availability | 99.9% | 24/7/365 operational readiness |
| Response Time (Scheduled) | ≤ 5 minutes | From aircraft arrival to service start |
| Response Time (Unscheduled) | ≤ 15 minutes | Emergency fueling capability |
| Fuel Quality Compliance | 100% | ISO 19880-8 verification |
| Safety Incident Rate | Zero tolerance | Per 10,000 fueling operations |
| Equipment Reliability | 99.5% | Mean time between failures |
| Personnel Certification | 100% | All operators SAE AS6968 certified |

## 6. Safety Requirements

### 6.1 Critical Safety Protocols
- **Exclusion Zone**: 50-meter minimum clearance during fueling operations
- **Fire Suppression**: Automated fire detection and suppression systems active
- **Grounding/Bonding**: Mandatory electrical bonding before connection
- **Leak Detection**: Continuous hydrogen gas monitoring (≥4 sensors per fueling point)
- **Emergency Shutdown**: Automated system with manual override capability
- **Personnel Protection**: Cryogenic-rated PPE mandatory for all fueling personnel

### 6.2 Emergency Response Requirements
- Emergency Response Team (ERT) on-site during all fueling operations
- Emergency shutdown capability within 2 seconds
- Immediate notification to airport fire services
- Post-incident lockout until safety clearance obtained
- Incident investigation within 24 hours

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 03-10 (Operations)
  - ATA 12 (Servicing - Aircraft fuel systems)
  - ATA 28 (Fuel - Aircraft systems)
- Parent Document: [03-00-12_Services](../)
- Related H2 Services: 
  - [03-00-12-02-02A_Cryogenic_Support_Service.md](./03-00-12-02-02A_Cryogenic_Support_Service.md)
  - [03-00-12-02-03A_H2_Safety_Monitoring_Service.md](./03-00-12-02-03A_H2_Safety_Monitoring_Service.md)
  - [03-00-12-02-04A_H2_Emergency_Response_Service.md](./03-00-12-02-04A_H2_Emergency_Response_Service.md)
- Training Requirements: [03-00-12-06-03A_H2_GSE_Safety_Training.md](../03-00-12-06_GSE_Training_Services/03-00-12-06-03A_H2_GSE_Safety_Training.md)
- H2 Energy Systems: [03-80_Energy](../../../03-80_Energy/)

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
