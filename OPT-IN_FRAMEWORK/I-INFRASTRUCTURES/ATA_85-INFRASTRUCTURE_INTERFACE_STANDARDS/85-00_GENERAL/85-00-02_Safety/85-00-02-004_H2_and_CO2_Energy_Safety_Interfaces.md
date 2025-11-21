# 85-00-02-004 H₂ and CO₂ Energy Safety Interfaces

## Document Information
- **Document ID**: 85-00-02-004
- **Title**: H₂ and CO₂ Energy Safety Interfaces
- **Version**: 1.0
- **Status**: Draft
- **Last Updated**: 2025-11-21

## Purpose

This document focuses on **safety aspects** of H₂ refueling and CO₂ battery charging/discharging interfaces, including safety interlocks, monitoring systems, emergency shutdown procedures, and handling of abnormal conditions.

## Scope

This document covers:
- **H₂ refueling interface**: Pressure, temperature, flow control, leak detection
- **CO₂ battery interface**: Thermal management, electrical isolation, charge/discharge monitoring
- **Alarm and signaling**: Integration with airport control rooms and energy management systems
- **Emergency response**: Leak detection, overpressure relief, fire detection, emergency shutdown

## H₂ Refueling Interface Safety

### Safety Interlock System

The H₂ refueling interface implements a **multi-layer interlock system** to prevent unsafe refueling operations:

#### Pre-Refueling Interlocks

| **Interlock** | **Condition** | **Purpose** | **Override Allowed?** |
|---------------|---------------|-------------|---------------------|
| H₂ dispenser ready | Dispenser system health check passed | Verify dispenser is operational | No |
| Aircraft H₂ system ready | H₂ tank pressure, temperature, vent status normal | Verify aircraft can safely receive H₂ | No |
| Grounding verified | Bonding cable connected, continuity confirmed | Prevent static discharge ignition | No |
| Ex zone clear | No unauthorized personnel or ignition sources in Zone 1 | Prevent exposure to potential leak | Yes (Emergency override) |
| Weather acceptable | Wind speed <20 knots, no lightning within 5 nm | Prevent dispersion issues, ignition | Yes (with approval) |
| Communication established | Aircraft ↔ dispenser data link active | Enable monitoring and emergency shutdown | No |

**Interlock Logic**: All interlocks must be satisfied (logical AND) before refueling can commence. Overrides require supervisor approval and are logged.

#### During-Refueling Interlocks

| **Interlock** | **Monitoring Parameter** | **Threshold** | **Action on Violation** |
|---------------|--------------------------|---------------|------------------------|
| Pressure limit | H₂ pressure in hose and aircraft tank | <700 bar (max) | Emergency shutdown, vent |
| Temperature limit | H₂ temperature at connector | -40°C to +85°C | Reduce flow rate or shutdown |
| Flow rate limit | H₂ mass flow rate | <10 kg/min (max) | Reduce flow or shutdown |
| Leak detection | H₂ concentration in Zone 1 | <25% LEL | Emergency shutdown, alarm |
| Connector status | Mechanical lock and seal integrity | Continuous verification | Emergency shutdown |
| Dead-man switch | Operator presence confirmation | Every 60 seconds | Emergency shutdown |

**Continuous Monitoring**: All parameters sampled at ≥1 Hz, with automatic emergency shutdown on any threshold violation.

### H₂ Leak Detection System

**Architecture**:
- **Primary sensors**: Catalytic bead H₂ sensors at connector (4 sensors in redundant configuration)
- **Secondary sensors**: Thermal conductivity sensors at vent outlets and in Ex zone perimeter
- **Tertiary detection**: Visual inspection by trained operator (periodic)

**Sensor Placement**:
1. **At connector** (4 sensors): 0.5 m from connector, 120° spacing, height 0.5-1.5 m (captures rising H₂ and potential ground-level leaks)
2. **Ex zone perimeter** (8 sensors): At Zone 1 boundary (3 m radius), 45° spacing
3. **Vent monitoring** (2 sensors): 2 m from aircraft vent outlets

**Alarm Thresholds**:
- **Pre-alarm** (10% LEL): Visual and audible warning, log event, continue refueling with caution
- **Alarm** (25% LEL): Emergency shutdown initiated, ARFF notified, personnel evacuate Ex zone
- **Danger** (50% LEL): Full site alarm, emergency services mobilized, area evacuation

**Sensor Testing**: Daily functional test (exposure to test gas), monthly calibration, annual replacement.

### Emergency Shutdown System

**Trigger Conditions**:
- Leak detection alarm (≥25% LEL)
- Overpressure (>700 bar)
- Temperature excursion (<-40°C or >+85°C)
- Connector unlock or loss of seal
- Dead-man switch timeout
- Manual activation (operator or remote)

**Shutdown Sequence** (automatic, completes in <3 seconds):
1. **Close dispenser outlet valve** (0.5 seconds)
2. **Close aircraft inlet valve** (0.5 seconds)
3. **Depressurize hose** (vent to atmosphere or recovery system, 2 seconds)
4. **Sound alarm** (immediate)
5. **Notify control room and ARFF** (immediate, automatic message)
6. **Log event** (timestamp, parameters, reason for shutdown)

**Manual Reset Required**: After emergency shutdown, system cannot restart until:
- Cause of shutdown investigated and resolved
- All interlocks verified satisfied
- Supervisor approval logged

### H₂ Vent and Pressure Relief

**Purpose**: Safely discharge H₂ in case of overpressure or emergency depressurization

**Vent System Design**:
- **Primary vent**: Aircraft H₂ tank relief valves (set pressure 800 bar, flow capacity >50 kg/min H₂)
- **Secondary vent**: Dispenser hose depressurization port (controlled, flow capacity 10 kg/min)
- **Vent discharge location**: >5 m above stand level, directed away from aircraft and buildings

**Safety Requirements**:
- Vent outlets monitored for H₂ concentration (detect vent activation or leak)
- Vent discharge zone (3 m radius around outlet) marked and kept clear of ignition sources
- Vent flow capacity verified by annual testing

### Cross-Reference to ATA 28 and ATA 70

Interface safety requirements integrate with on-board systems:
- **[ATA 28 Fuel/H₂](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CARBON_NEUTRAL_FUEL_SYSTEMS/ATA_28-FUEL/)**: H₂ tank pressure/temperature monitoring, leak detection on aircraft
- **[ATA 70 Propulsion](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/ATA_70-STANDARD_PRACTICES_ENGINES/)**: Fuel cell system status during refueling (must be isolated)

## CO₂ Battery Docking Interface Safety

### Safety Interlock System

The CO₂ battery docking interface implements **electrical, thermal, and mechanical interlocks**:

#### Pre-Docking Interlocks

| **Interlock** | **Condition** | **Purpose** | **Override Allowed?** |
|---------------|---------------|-------------|---------------------|
| Container health check | Battery management system (BMS) reports normal status | Verify battery is safe to connect | No |
| Thermal status | Battery temperature 10-40°C | Prevent connection if battery is too hot/cold | No |
| Electrical isolation | High-voltage contactors open, no voltage at interface | Prevent arc during connection | No |
| Mechanical alignment | Container position within ±50 mm of dock centerline | Ensure proper connector engagement | No |
| Cooling system ready | Thermal management active, coolant flow verified | Prevent thermal runaway during charging | No |
| Communication established | BMS ↔ dock controller data link active | Enable monitoring and emergency disconnect | No |

#### During Charging/Discharging Interlocks

| **Interlock** | **Monitoring Parameter** | **Threshold** | **Action on Violation** |
|---------------|--------------------------|---------------|------------------------|
| Voltage limit | Battery pack voltage | 800-1500 VDC (operational range) | Stop charge/discharge, alarm |
| Current limit | Charge/discharge current | <500 A (max) | Reduce current or stop |
| Temperature limit | Battery cell temperature (max) | <60°C | Stop charging, activate cooling |
| Temperature gradient | Max temperature difference between cells | <10°C | Reduce current, active balancing |
| Insulation resistance | Resistance between HV+ and chassis | >100 kΩ/V | Immediate disconnect, alarm |
| Thermal runaway detection | Rapid temperature rise (>5°C/min) | Detected by BMS | Emergency disconnect, fire suppression |

### Thermal Management and Monitoring

**Cooling System Architecture**:
- **Liquid cooling**: Glycol/water mix circulated through battery container and dock heat exchanger
- **Cooling capacity**: 150 kW (sufficient for 500 A charge/discharge)
- **Redundancy**: Dual cooling pumps (1 primary, 1 standby)

**Temperature Monitoring**:
- **Cell-level sensors**: 1 sensor per 10 cells (typical 200 sensors per container)
- **Coolant sensors**: Inlet and outlet temperature, flow rate
- **Ambient sensors**: 4 sensors around container exterior

**Thermal Alarm Thresholds**:
- **Pre-alarm** (50°C max cell temp): Reduce charge current by 50%
- **Alarm** (60°C max cell temp): Stop charging, maintain cooling
- **Danger** (70°C max cell temp or >5°C/min rise rate): Emergency disconnect, activate fire suppression

### Fire Detection and Suppression

**Fire Detection**:
- **Thermal detection**: Heat sensors at 8 locations in container (alarm at 90°C)
- **Smoke detection**: Optical smoke detectors at container vents (early warning)
- **Gas detection**: CO₂ concentration sensors (detect venting or thermal decomposition)

**Fire Suppression System** (at dock):
- **Suppression agent**: Inert gas (CO₂ or N₂) for electrical fires, water mist for thermal cooling
- **Activation**: Automatic on fire detection, manual activation by operator or ARFF
- **Coverage**: Full container volume, discharge time <10 seconds
- **Venting**: Container vents open automatically during suppression to prevent overpressure

**Fire Suppression Sequence**:
1. **Detect fire** (thermal, smoke, or gas sensors)
2. **Emergency disconnect** (isolate electrical power, <1 second)
3. **Sound alarm** (local and control room)
4. **Activate suppression** (discharge inert gas or water mist)
5. **Notify ARFF** (automatic message with container location and status)
6. **Monitor temperature** (continue cooling after suppression if safe)

### Electrical Isolation and Emergency Disconnect

**Normal Disconnect Sequence** (end of charging):
1. Ramp down current to zero (10 seconds)
2. Open high-voltage contactors (0.5 seconds)
3. Verify zero voltage at interface (1 second)
4. Disengage mechanical connector (manual or automatic)
5. Confirm isolation (test voltage with multimeter)

**Emergency Disconnect Sequence** (thermal runaway, fire, electrical fault):
1. **Immediate**: Open high-voltage contactors (<0.1 seconds)
2. **Immediate**: Sound alarm, notify ARFF
3. **Immediate**: Activate fire suppression (if fire detected)
4. **Within 5 seconds**: Disengage mechanical connector (explosive bolts if required)
5. **Within 10 seconds**: Move container away from dock (automatic or manual)

**Explosive Bolt Disconnect**: If container cannot be mechanically disconnected normally (e.g., thermal expansion has seized connector), explosive bolts sever electrical cables and release mechanical lock. Bolts tested annually.

### Cross-Reference to ATA 80 and ATA 99

Interface safety requirements integrate with on-board systems:
- **[ATA 80 Energy](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_80-STARTING/)**: Energy storage monitoring, charge management
- **[ATA 99 Carbon](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C1-CARBON_NEUTRAL_CIRCULARITY/ATA_99-CARBON/)**: CO₂ battery system safety, BMS integration

## Alarm and Signaling Interfaces

### Signal Exchange Between Aircraft and Infrastructure

**H₂ Refueling Signals** (aircraft → infrastructure):
- Tank pressure, temperature (continuous, 1 Hz)
- Vent valve status (open/closed, change-of-state)
- Leak detection alarm status (normal/pre-alarm/alarm)
- Refueling authorization (permit/deny)

**H₂ Refueling Signals** (infrastructure → aircraft):
- Dispenser status (ready/fueling/shutdown/fault)
- H₂ flow rate, delivered mass (continuous, 1 Hz)
- Emergency shutdown command (immediate action)
- Ex zone status (clear/restricted/unsafe)

**CO₂ Battery Signals** (aircraft/container → dock):
- Battery voltage, current, SOC (State of Charge), temperature (continuous, 10 Hz)
- BMS status (normal/warning/fault/emergency)
- Isolation resistance, insulation status (1 Hz)
- Thermal runaway alarm (immediate)

**CO₂ Battery Signals** (dock → aircraft/container):
- Charge/discharge command (current setpoint, 10 Hz)
- Cooling system status (flow rate, temperature, 1 Hz)
- Fire suppression status (armed/activated)
- Emergency disconnect command (immediate action)

### Integration with Airport Control Room

**Safety Dashboard**:
- Real-time display of all H₂ and CO₂ interface status (stand-by-stand view)
- Alarm summary (color-coded: green=normal, yellow=pre-alarm, red=alarm, flashing red=emergency)
- Stand safety state (SAFE / RESTRICTED / UNSAFE — see [85-00-02-006](85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md))

**Alarm Escalation**:
1. **Pre-alarm**: Display on dashboard, log event (no immediate action)
2. **Alarm**: Audible alert in control room, notify duty manager and ground supervisor
3. **Emergency**: Full site alarm, automatic notification to ARFF, OCC (Operations Control Center), and energy operators

### Integration with Energy Management Systems

**H₂ Infrastructure**:
- H₂ storage pressure and inventory (real-time, 1 Hz)
- Dispenser availability and status (all stands)
- H₂ quality monitoring (purity, moisture content, daily updates)

**CO₂ Battery Systems**:
- Container SOC and availability (all containers on airport)
- Charging/discharging schedule (predictive load for grid connection)
- Thermal status and cooling demand (aggregate, 1 Hz)

**Grid Integration**:
- CO₂ battery charging load (MW, continuous)
- Grid frequency and voltage stability (monitoring for V2G support)
- Demand response signals (reduce charging during peak demand)

## Cybersecurity and Integrity of Safety Data

### Threat Model

Safety-critical interface signals are vulnerable to:
- **Data injection**: Malicious false alarms or shutdown commands
- **Data spoofing**: False sensor readings (e.g., fake "normal" status during actual leak)
- **Denial of service**: Disruption of communication preventing emergency shutdown
- **Man-in-the-middle**: Interception and modification of control commands

### Security Measures

**Authentication and Encryption**:
- All safety-critical signals use **cryptographic authentication** (HMAC or digital signature)
- Control commands (e.g., emergency shutdown) use **mutual authentication** (aircraft ↔ infrastructure)
- Encryption (AES-256) for all interface communication (prevents eavesdropping)

**Intrusion Detection**:
- **Anomaly detection**: Monitor signal patterns for unusual behavior (e.g., sudden sensor dropout, implausible values)
- **Rate limiting**: Prevent flooding attacks on communication channels
- **Logging**: All interface commands and alarms logged with tamper-evident timestamps

**Physical Security**:
- Interface control systems in **locked cabinets** with access control
- Network connections protected by **firewalls** (separate VLAN for safety systems)
- Regular security audits and penetration testing

**Fail-Safe on Cyber Attack**:
- If authentication fails or intrusion detected → **default to safe state** (emergency shutdown, alarms activated)
- Safety systems can operate in **degraded mode** (local control only) if network compromised

### Compliance with DO-326A and ED-202A

Interface cybersecurity follows **[DO-326A/ED-202A](https://www.rtca.org/)** (Airworthiness Security Process Specification):
- Risk assessment for interface cyber threats
- Security requirements derived from safety requirements
- Security testing and validation
- Continuous security monitoring and incident response

## Handling of Abnormal Conditions

### H₂ Leak During Refueling

**Detection**: H₂ sensors alarm at ≥25% LEL

**Immediate Actions** (automatic):
1. Emergency shutdown (close valves, depressurize hose)
2. Sound alarm, notify ARFF
3. Evacuate Ex zone (all personnel >10 m from leak source)

**Follow-Up Actions** (manual):
1. ARFF assesses leak severity (H₂ concentration, dispersion)
2. If leak stops and concentration drops <10% LEL → safe to approach (after 5 minutes)
3. Inspect connector and seals, repair or replace as needed
4. Leak test before resuming refueling

### CO₂ Battery Thermal Runaway

**Detection**: BMS detects rapid temperature rise (>5°C/min) or temperature >70°C

**Immediate Actions** (automatic):
1. Emergency disconnect (isolate electrical power)
2. Activate fire suppression (inert gas flood)
3. Sound alarm, notify ARFF and hazmat team
4. Continue cooling if safe (to slow thermal propagation)

**Follow-Up Actions** (manual):
1. ARFF establishes exclusion zone (10 m radius, toxic gas hazard)
2. Monitor temperature remotely (thermal imaging)
3. If safe, move container to designated hazmat area (>50 m from aircraft and buildings)
4. Allow container to cool naturally (may take 24-48 hours)
5. Hazmat team disposes of damaged container per regulations

### Overpressure Event (H₂ or CO₂)

**H₂ Overpressure**:
- **Cause**: Dispenser control failure, blocked vent, temperature rise
- **Response**: Pressure relief valves open automatically (800 bar setpoint), venting H₂ safely upward
- **Action**: Emergency shutdown, inspect relief valve and vent system

**CO₂ Battery Overpressure** (container venting):
- **Cause**: Thermal runaway producing gas, blocked vent
- **Response**: Container vents open (pressure relief at 1.5 bar), CO₂ gas discharge
- **Action**: Emergency disconnect, activate fire suppression, monitor CO₂ concentration

### Fire at Interface

**Detection**: Thermal sensors, smoke detectors, visual observation

**Immediate Actions** (automatic where applicable):
1. Emergency shutdown/disconnect (isolate fuel/energy source)
2. Activate fire suppression (water mist for H₂, inert gas for CO₂ battery electrical fire)
3. Sound alarm, notify ARFF
4. Evacuate personnel from immediate area

**ARFF Response**:
1. Assess fire type and severity
2. Deploy appropriate suppression (foam for H₂ fire if leak stopped, water for cooling)
3. Establish exclusion zone
4. Monitor for re-ignition or secondary hazards

## Related Documents

- [85-00-02-001_Safety_Concepts_and_Objectives.md](85-00-02-001_Safety_Concepts_and_Objectives.md) - Safety objectives
- [85-00-02-002_Hazard_Analysis_at_Interface_Level.md](85-00-02-002_Hazard_Analysis_at_Interface_Level.md) - Interface hazards
- [85-00-02-003_Safety_Zones_and_Separation_Criteria.md](85-00-02-003_Safety_Zones_and_Separation_Criteria.md) - Safety zones
- [85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md](85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md) - Operational procedures
- [85-00-02-007_Safety_Monitoring_and_Alerting_Interfaces.md](85-00-02-007_Safety_Monitoring_and_Alerting_Interfaces.md) - Monitoring systems
- [ATA 28 Fuel/H₂](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CARBON_NEUTRAL_FUEL_SYSTEMS/ATA_28-FUEL/)
- [ATA 80 Energy](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_80-STARTING/)

## References

- **ISO 22734**: Hydrogen fuel — Quality specifications
- **NFPA 2**: Hydrogen Technologies Code (Chapter 7: Fueling Operations)
- **UL 9540A**: Test Method for Evaluating Thermal Runaway Fire Propagation in Battery Energy Storage Systems
- **IEC 62443**: Industrial communication networks — IT security for networks and systems
- **[DO-326A/ED-202A](https://www.rtca.org/)**: Airworthiness Security Process Specification
- **EN 1473**: Installation and equipment for liquefied natural gas/hydrogen

## Document Control

- **Owner**: AMPEL360 Safety & Certification Team
- **Approver**: Chief Safety Officer
- **Review Frequency**: Quarterly
- **Next Review**: 2026-02-21
- **Repository**: AMPEL360-BWB-H2-Hy-E
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **DRAFT** – Subject to human review and approval
- Human approver: _[to be completed]_
- Last AI update: 2025-11-21

---
*This document is part of the AMPEL360 OPT-IN Framework certification package.*
