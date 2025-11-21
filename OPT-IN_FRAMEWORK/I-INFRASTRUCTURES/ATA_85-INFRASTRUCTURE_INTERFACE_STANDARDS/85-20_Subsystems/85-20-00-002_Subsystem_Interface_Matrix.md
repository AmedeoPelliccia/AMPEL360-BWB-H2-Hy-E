# 85-20-00-002 — Subsystem Interface Matrix

## Document Metadata

```yaml
document_id: "85-20-00-002"
title: "Subsystem Interface Matrix"
parent_ata: "ATA 85"
category: "Infrastructure Interface Standards"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

This document defines the interface relationships between the nine ground-aircraft subsystems defined in [ATA 85-20](./85-20-00-001_Subsystems_Overview_and_Architecture.md). It provides a comprehensive matrix of mechanical, electrical, data, and operational interfaces to support integrated ground operations and system design.

## Interface Categories

Interfaces are categorized into four primary types:

### 1. Mechanical Interfaces (M)

Physical connections, mounting points, structural loads, and geometric constraints.

**Examples:**
- H2 coupling mechanical connection
- Jetway docking alignment
- Cargo loader positioning

### 2. Electrical Interfaces (E)

Power distribution, grounding, circuit protection, and electrical compatibility.

**Examples:**
- Ground power connection
- Battery charging circuits
- Sensor power distribution

### 3. Data Interfaces (D)

Communication protocols, data exchange formats, and information flows.

**Examples:**
- Refueling status data
- Safety monitoring alerts
- Maintenance data download

### 4. Operational Interfaces (O)

Procedural coordination, timing dependencies, and operational constraints.

**Examples:**
- Simultaneous refueling and boarding restrictions
- Emergency evacuation priorities
- Turnaround sequence coordination

## Subsystem Interface Matrix

### Matrix Legend

- **●** — Direct interface (critical dependency)
- **◐** — Indirect interface (coordination required)
- **○** — No direct interface
- **Priority:** 1=Critical, 2=Important, 3=Informational

### Full Interface Matrix

| From ↓ / To → | 85-20-01 H2 | 85-20-02 Power | 85-20-03 Board | 85-20-04 Evac | 85-20-05 Cargo | 85-20-06 Data | 85-20-07 Stand | 85-20-08 Safety | 85-20-09 Battery |
|---------------|-------------|----------------|----------------|---------------|----------------|---------------|----------------|-----------------|------------------|
| **85-20-01 H2 Refueling** | — | ◐ (E,D) | ○ | ● (O) P1 | ○ | ● (D) P1 | ◐ (O) | ● (M,E,D) P1 | ◐ (E,D) |
| **85-20-02 Electrical Power** | ◐ (E,D) | — | ◐ (E) | ◐ (E) | ◐ (E) | ● (E,D) P2 | ◐ (E) | ◐ (E) | ● (E,D) P1 |
| **85-20-03 Passenger Boarding** | ○ | ◐ (E) | — | ● (M,O) P1 | ○ | ◐ (D) | ● (M,D,O) P1 | ◐ (O) | ○ |
| **85-20-04 Evacuation** | ● (O) P1 | ◐ (E) | ● (M,O) P1 | — | ◐ (O) | ● (D) P1 | ● (M,O) P1 | ● (D,O) P1 | ○ |
| **85-20-05 Cargo** | ○ | ◐ (E) | ○ | ◐ (O) | — | ◐ (D) | ● (M,O) P2 | ◐ (O) | ○ |
| **85-20-06 Data Comms** | ● (D) P1 | ● (E,D) P2 | ◐ (D) | ● (D) P1 | ◐ (D) | — | ● (D) P2 | ● (D) P1 | ● (D) P2 |
| **85-20-07 Stand/Gate** | ◐ (O) | ◐ (E) | ● (M,D,O) P1 | ● (M,O) P1 | ● (M,O) P2 | ● (D) P2 | — | ◐ (D) | ◐ (M) |
| **85-20-08 Safety Monitor** | ● (M,E,D) P1 | ◐ (E) | ◐ (O) | ● (D,O) P1 | ◐ (O) | ● (D) P1 | ◐ (D) | — | ◐ (D) |
| **85-20-09 CO2 Battery** | ◐ (E,D) | ● (E,D) P1 | ○ | ○ | ○ | ● (D) P2 | ◐ (M) | ◐ (D) | — |

## Detailed Interface Descriptions

### 85-20-01 ↔ 85-20-08: H2 Refueling ↔ Safety Monitoring

**Interface Type:** Mechanical, Electrical, Data (Priority 1 — Critical)

**Description:**
Safety monitoring is integral to H2 refueling operations. Gas detection sensors must be active before, during, and after refueling.

**Interface Elements:**
- **M:** H2 sensor mounting points on refueling infrastructure
- **E:** Sensor power from safety monitoring system
- **D:** Real-time H2 concentration data, leak detection alerts

**Requirements:**
- Safety monitoring must confirm safe conditions before refueling authorization
- H2 concentration above 0.4% triggers automatic refueling shutdown
- Data latency < 500ms for safety-critical alerts

**Related Documents:**
- [85-20-01-003_H2_Safety_Monitoring_Subsystem.md](./85-20-01_H2_Refueling_Interface_Subsystem/85-20-01-003_H2_Safety_Monitoring_Subsystem.md)
- [85-20-08-002_H2_Gas_Detection_System.md](./85-20-08_Safety_and_Monitoring_Subsystem/85-20-08-002_H2_Gas_Detection_System.md)

### 85-20-01 ↔ 85-20-06: H2 Refueling ↔ Data Communications

**Interface Type:** Data (Priority 1 — Critical)

**Description:**
Refueling system status, flow rates, and completion data must be communicated to aircraft systems and ground operations.

**Interface Elements:**
- **D:** Refueling status (idle, connecting, fueling, complete, fault)
- **D:** Flow rate and total quantity transferred
- **D:** Safety interlocks status
- **D:** Maintenance and diagnostic data

**Protocol:** ARINC 615A data loader protocol or equivalent secure ground data link

**Requirements:**
- Bidirectional data exchange for authorization and status
- Encryption for security-sensitive refueling data
- Logging of all refueling transactions for audit trail

**Related Documents:**
- [85-20-01-005_H2_Data_Interface_and_Communications.md](./85-20-01_H2_Refueling_Interface_Subsystem/85-20-01-005_H2_Data_Interface_and_Communications.md)
- [85-20-06-004_Operations_Data_Exchange_System.md](./85-20-06_Data_and_Communications_Interface_Subsystem/85-20-06-004_Operations_Data_Exchange_System.md)

### 85-20-02 ↔ 85-20-09: Electrical Power ↔ CO2 Battery

**Interface Type:** Electrical, Data (Priority 1 — Critical)

**Description:**
Ground electrical power infrastructure charges the CO2 battery containers through high-power DC charging interfaces.

**Interface Elements:**
- **E:** High-voltage DC charging bus (800V nominal)
- **E:** Current limiting and protection circuits
- **E:** Grounding and bonding
- **D:** Battery state of charge (SOC), temperature, BMS data
- **D:** Charging control commands

**Requirements:**
- Charging power up to 350 kW per battery container
- CCS2 or MCS (Megawatt Charging System) compatible connectors
- Thermal management coordination with battery BMS
- Emergency disconnect capability

**Related Documents:**
- [85-20-02-003_Battery_Charging_Interface.md](./85-20-02_Electrical_Power_Interface_Subsystem/85-20-02-003_Battery_Charging_Interface.md)
- [85-20-09-003_Charging_and_Thermal_Management_Interface.md](./85-20-09_CO2_Battery_Interface_Subsystem/85-20-09-003_Charging_and_Thermal_Management_Interface.md)

### 85-20-03 ↔ 85-20-04: Passenger Boarding ↔ Evacuation

**Interface Type:** Mechanical, Operational (Priority 1 — Critical)

**Description:**
Boarding and evacuation interfaces share common door systems. Emergency egress must override boarding operations.

**Interface Elements:**
- **M:** Door mechanisms, jetway interface points
- **O:** Door mode selection (boarding vs. armed for evacuation)
- **O:** Emergency evacuation activation and override logic

**Requirements:**
- Evacuation mode disables normal boarding interlocks
- ARFF must have independent access to door controls
- Visual and audible indication of door mode (boarding/armed)

**Related Documents:**
- [85-20-03-003_Door_Interface_Sensors_and_Controls.md](./85-20-03_Passenger_Boarding_Interface_Subsystem/85-20-03-003_Door_Interface_Sensors_and_Controls.md)
- [85-20-04-002_Emergency_Exit_Interface_System.md](./85-20-04_Evacuation_and_Rescue_Interface_Subsystem/85-20-04-002_Emergency_Exit_Interface_System.md)

### 85-20-03 ↔ 85-20-07: Passenger Boarding ↔ Stand Infrastructure

**Interface Type:** Mechanical, Data, Operational (Priority 1 — Critical)

**Description:**
Jetway/boarding bridge positioning and aircraft door alignment require precise coordination with stand infrastructure.

**Interface Elements:**
- **M:** Jetway docking mechanism, alignment guides
- **D:** Aircraft position data, door height and location
- **D:** Jetway position feedback
- **O:** Boarding sequence coordination with pushback/towing

**Requirements:**
- Positioning accuracy: ±25mm lateral, ±50mm vertical
- Visual guidance system active during positioning
- Automated jetway docking where available
- Manual override capability

**Related Documents:**
- [85-20-03-002_Jetway_Docking_System.md](./85-20-03_Passenger_Boarding_Interface_Subsystem/85-20-03-002_Jetway_Docking_System.md)
- [85-20-07-002_Aircraft_Positioning_System.md](./85-20-07_Stand_and_Gate_Infrastructure_Subsystem/85-20-07-002_Aircraft_Positioning_System.md)

### 85-20-06 ↔ All Subsystems: Data Communications

**Interface Type:** Data (Priority 1-2)

**Description:**
Data communications subsystem provides centralized data exchange for all ground-aircraft interfaces.

**Interface Elements:**
- **D:** Ethernet backbone (1 Gbps minimum)
- **D:** WiFi 6E access for wireless ground systems
- **D:** Secure VPN tunnels for sensitive data
- **D:** Time synchronization (NTP or PTP)

**Requirements:**
- Redundant communication paths for critical data
- Quality of Service (QoS) prioritization for safety-critical messages
- Cybersecurity per [DO-326A](https://www.rtca.org/content/standards-guidance-materials) / [ED-202A](https://eshop.eurocae.net/eurocae-documents-and-reports/ed-202a/)
- Logging and audit trail for all transactions

**Related Documents:**
- [85-20-06-002_Ground_Data_Link_System.md](./85-20-06_Data_and_Communications_Interface_Subsystem/85-20-06-002_Ground_Data_Link_System.md)

### 85-20-08 ↔ Critical Subsystems: Safety Monitoring

**Interface Type:** Data, Operational (Priority 1)

**Description:**
Safety monitoring provides environmental and hazard detection for critical operations including H2 refueling, evacuation, and battery charging.

**Interface Elements:**
- **D:** Gas concentration data (H2, O2, CO, CO2)
- **D:** Fire detection alerts
- **D:** Safety zone intrusion detection
- **O:** Safety permit status for hazardous operations

**Requirements:**
- Continuous monitoring during all ground operations
- Safety alerts broadcast to all relevant subsystems
- Automatic inhibit of incompatible operations (e.g., refueling + welding)
- Integration with airport fire/rescue services

**Related Documents:**
- [85-20-08-001_Safety_Monitoring_Architecture.md](./85-20-08_Safety_and_Monitoring_Subsystem/85-20-08-001_Safety_Monitoring_Architecture.md)

## Cross-ATA Interface Traceability

### On-Board Systems (ATA Chapters)

**ATA 28 (Fuel) ↔ 85-20-01 (H2 Refueling):**
- H2 tank fill/vent valve control
- H2 quantity indication
- Fueling interlock signals

**ATA 24 (Electrical Power) ↔ 85-20-02 (Electrical Power Interface):**
- Ground power contactor control
- Battery charge management
- Bus voltage monitoring

**ATA 52 (Doors) ↔ 85-20-03/04/05 (Boarding/Evacuation/Cargo):**
- Door position sensors
- Lock/unlock commands
- Emergency egress signals

For complete on-board to ground interface mapping, see:
- [ASSETS/Cross_Subsystem_Integration/85-20-A-003_Data_Flow_Diagram.svg](./ASSETS/Cross_Subsystem_Integration/85-20-A-003_Data_Flow_Diagram.svg)

## Interface Management

### Design Responsibility

- **Aircraft OEM (AMPEL360):** On-board interface equipment, connectors, mounting provisions
- **Ground Infrastructure Provider:** Ground-side equipment, mounting, utilities
- **Interface Control Document (ICD):** Joint responsibility, maintained in this repository

### Configuration Control

All interface changes require:
1. Impact assessment across affected subsystems
2. Update to this interface matrix
3. Revision of affected subsystem documents
4. Validation testing of modified interfaces

### Standards Compliance

Interfaces shall comply with:
- [ISO 19880-5](https://www.iso.org/standard/71975.html) (H2 refueling)
- [SAE ARP 599](https://www.sae.org/standards/content/arp599/) (Ground support equipment)
- [ARINC 628](https://www.aviation-ia.com/standards-library/arinc-standards) (Ground systems)
- Airport-specific interface standards where applicable

## Change Log

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-21 | Initial interface matrix | AI (GitHub Copilot) / Amedeo Pelliccia |

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21

---

*Reference: [OPT-IN Framework Documentation Standard](../../../../AMPEL360_DOCUMENTATION_STANDARD.md)*
