# 03-80-05-03A - Charging Infrastructure

## 1. Purpose
This document specifies charging infrastructure for battery-electric Ground Support Equipment (GSE), including charging stations, power management, and operational requirements.

## 2. Scope
This specification covers:
- Charging levels and standards
- Charging station design and deployment
- Power distribution for charging
- Smart charging and load management
- User interface and operation

## 3. Applicable Documents
- IEC 61851 (Electric Vehicle Conductive Charging System)
- SAE J1772 (EV Conductive Charge Coupler)
- ISO 15118 (Road Vehicles - Vehicle to Grid Communication Interface)
- IEC 62196 (Plugs, Socket-outlets, Vehicle Connectors and Vehicle Inlets)
- NFPA 70 (National Electrical Code)

## 4. Energy System Description

### 4.1 Overview
Charging infrastructure provides the means to recharge battery-electric GSE, including charging stations, power distribution, control systems, and communication networks.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Level 2 AC Charging | 7-22 kW per port | 400V three-phase |
| DC Fast Charging | 50-350 kW per station | High-power charging |
| Connector Types | IEC 62196 Type 2, CCS | Standard connectors |
| Charging Efficiency | >90% | AC to battery |
| Communication | ISO 15118, OCPP | Smart charging |
| Availability | 98% per charging station | Operational target |

### 4.3 Performance Requirements

#### 4.3.1 Charging Speed and Capacity
- **Level 2 AC**: 2-8 hours charging time (depends on battery size)
- **DC Fast Charging**: 15-60 minutes to 80% SOC
- **Throughput**: Support daily charging demand for GSE fleet

#### 4.3.2 User Experience
- **Ease of Use**: Simple plug-in operation
- **Display**: Charging status, time remaining, energy delivered
- **Payment/Access**: RFID or app-based authentication (if required)
- **Availability**: Real-time status information (available, occupied, faulted)

### 4.4 Charging Station Types

#### 4.4.1 Level 2 AC Charging Stations
**Configuration**:
- Wall-mounted or pedestal-mounted
- Single or dual port (2 vehicles simultaneously)
- 7-22 kW per port

**Applications**:
- Overnight charging for light-duty GSE
- Opportunity charging during extended breaks
- Lower infrastructure cost

#### 4.4.2 DC Fast Charging Stations
**Configuration**:
- Pedestal-mounted, floor-standing
- Single or dual port (sequential or simultaneous charging)
- 50-350 kW per station

**Applications**:
- Rapid charging during operational breaks
- Heavy-duty GSE with large battery packs
- High-utilization equipment

### 4.5 Smart Charging and Load Management

**Smart Charging Features**:
- **Scheduled Charging**: Charge during off-peak hours or high renewable generation
- **Load Balancing**: Distribute available power among multiple vehicles
- **Demand Response**: Reduce charging during grid peak demand
- **V2G (Vehicle-to-Grid)**: Use vehicle batteries for grid services (future capability)

**Communication Protocols**:
- **ISO 15118**: Vehicle-to-charger communication
- **OCPP (Open Charge Point Protocol)**: Charger-to-management system communication
- **Modbus/CAN**: Integration with energy management system

### 4.6 Deployment Planning

**Site Selection**:
- Proximity to GSE parking/staging areas
- Access to electrical infrastructure
- Space for equipment maneuvering
- Future expansion provisions

**Capacity Planning**:
- Number of charging ports = (Fleet size × Charging frequency) / (Availability × Throughput)
- Consider peak demand, utilization patterns, charger availability

**Power Supply**:
- Dedicated distribution transformer and feeder for large charging installations
- Load calculation: Sum of all charging stations (with diversity factor)

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Charging Safety | IEC 61851, SAE J1772 | Design and installation |
| Electrical Safety | NFPA 70, IEC 60364 | Wiring, grounding, protection |
| User Safety | IEC 61851-22 | User interface and operation |
| EMC | CISPR 11, CISPR 22 | Electromagnetic compatibility |
| Environmental | ISO 14001 | EMS compliance |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Battery Technology: 03-80-05-01A_Battery_Technology
- Battery Management Systems: 03-80-05-02A_Battery_Management_Systems
- Power Distribution: 03-80-03-03A_Power_Distribution
- Energy Management Systems: 03-80-06_Energy_Management_Systems

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 GSE Energy WG | Initial release |

---

## Document Control

- **Status**: DRAFT – Subject to review and approval
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Energy Working Group
- **Next Review**: 2026-03-08
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-08

---
