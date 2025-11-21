# 85-00-02-007 Safety Monitoring and Alerting Interfaces

## Document Information
- **Document ID**: 85-00-02-007
- **Title**: Safety Monitoring and Alerting Interfaces
- **Version**: 1.0
- **Status**: Draft
- **Last Updated**: 2025-11-21

## Purpose

This document describes **monitoring and alerting** interfaces for safety at BWB infrastructure interfaces. It defines signals exchanged between aircraft systems and airport monitoring systems, data points for safety dashboards, alert prioritization and escalation, and cybersecurity requirements for safety-related interface data.

## Scope

This document covers:
- **Signal exchange**: Aircraft ↔ infrastructure data interfaces
- **Safety dashboards**: Control room and mobile displays
- **Alert prioritization**: Categorization and escalation logic
- **Data integrity**: Cybersecurity and validation requirements
- **Performance monitoring**: KPIs and trending

## Signal Exchange Between Aircraft and Infrastructure

### Data Interface Architecture

**Communication Layers**:
1. **Physical layer**: Ethernet (wired at gate) or LTE/5G (wireless backup)
2. **Network layer**: IP-based, segregated VLAN for safety-critical data
3. **Application layer**: Custom protocol or industry standard (e.g., ARINC 834 for ground ↔ aircraft data)

**Redundancy**:
- **Primary link**: Wired Ethernet connection (established when aircraft on stand)
- **Backup link**: Wireless (LTE/5G) for pre-arrival coordination and backup during ground ops
- **Failover**: Automatic switchover if primary link fails (<2 seconds)

### H₂ Refueling Interface Signals

#### Aircraft → Infrastructure (Continuous, 1 Hz)

| **Signal** | **Data Type** | **Range/Values** | **Purpose** |
|------------|--------------|-----------------|------------|
| H₂ tank pressure | Float (bar) | 0-800 bar | Monitor fill level, detect overpressure |
| H₂ tank temperature | Float (°C) | -40 to +85°C | Monitor thermal status, detect anomalies |
| Leak detection status | Enum | NORMAL / PRE-ALARM / ALARM | Aircraft-side leak detection |
| Vent valve status | Boolean | OPEN / CLOSED | Detect venting events |
| Refuel authorization | Boolean | AUTHORIZED / DENIED | Aircraft authorizes/denies refueling start |
| Aircraft H₂ system health | Enum | READY / NOT_READY / FAULT | Overall system status |

#### Infrastructure → Aircraft (Continuous, 1 Hz)

| **Signal** | **Data Type** | **Range/Values** | **Purpose** |
|------------|--------------|-----------------|------------|
| Dispenser status | Enum | READY / FUELING / SHUTDOWN / FAULT | Dispenser operational state |
| H₂ flow rate | Float (kg/min) | 0-10 kg/min | Current refuel rate |
| Delivered H₂ mass | Float (kg) | 0-300 kg | Cumulative mass delivered |
| Ex zone H₂ concentration | Float (% LEL) | 0-100% LEL | Safety monitoring |
| Emergency shutdown command | Boolean | NORMAL / SHUTDOWN | Command aircraft valve closure |
| Stand safety state | Enum | SAFE / RESTRICTED / UNSAFE | Overall stand status |

#### Event-Based Signals (Change-of-State)

- **Refuel start**: Timestamp, operator ID, aircraft/dispenser ID
- **Refuel complete**: Timestamp, total delivered mass, end pressure
- **Leak alarm**: Timestamp, location, H₂ concentration
- **Emergency shutdown**: Timestamp, trigger reason, operator/auto

### CO₂ Battery Docking Interface Signals

#### Container/Aircraft → Dock (High-Rate, 10 Hz for Control Signals)

| **Signal** | **Data Type** | **Range/Values** | **Purpose** |
|------------|--------------|-----------------|------------|
| Battery voltage | Float (VDC) | 0-1500 VDC | Monitor charge state |
| Battery current | Float (A) | -500 to +500 A | Monitor charge/discharge rate (+ = charging) |
| State of Charge (SOC) | Float (%) | 0-100% | Capacity status |
| Max cell temperature | Float (°C) | -20 to +80°C | Thermal safety monitoring |
| Temperature gradient | Float (°C) | 0-20°C | Detect cell imbalance |
| Insulation resistance | Float (kΩ) | 0-10,000 kΩ | Electrical isolation monitoring |
| BMS status | Enum | NORMAL / WARNING / FAULT / EMERGENCY | Battery management system health |
| Thermal runaway alarm | Boolean | NORMAL / ALARM | Critical safety alarm |

#### Dock → Container/Aircraft (Control Signals, 10 Hz)

| **Signal** | **Data Type** | **Range/Values** | **Purpose** |
|------------|--------------|-----------------|------------|
| Charge current setpoint | Float (A) | 0-500 A | Commanded charge rate |
| Cooling flow rate | Float (L/min) | 0-100 L/min | Thermal management |
| Coolant temperature (inlet) | Float (°C) | 10-40°C | Cooling system status |
| Fire suppression status | Enum | ARMED / ACTIVATED / FAULT | Safety system status |
| Emergency disconnect command | Boolean | NORMAL / DISCONNECT | Command immediate isolation |
| Dock operational status | Enum | READY / CHARGING / FAULT | Dock health |

### Ground Power and Data Interface Signals

**Aircraft ↔ Ground Power Unit**:
- Voltage, current, frequency (for AC ground power)
- Voltage, current (for DC ground power)
- Ground power available/connected status
- Isolation fault detection

**Aircraft ↔ Control Room** (General):
- Aircraft ID, flight number, parking stand
- Doors status (open/closed, armed/disarmed)
- Fire detection status (zone-by-zone)
- Evacuation status (in progress, complete)
- Passenger count (estimated on board)

## Safety Dashboard Architecture

### Control Room Master Display

**Layout**:
- **Stand overview map**: Graphical representation of all stands with aircraft icons, color-coded by safety state
- **Active alerts panel**: List of all current alarms and pre-alarms (scrolling list, prioritized)
- **Detail view**: Drill-down for selected stand showing all interface signals, trends, and status

**Stand Icon Color Coding**:
- **Green**: SAFE state, all operations normal
- **Yellow**: RESTRICTED state, limited operations
- **Red**: UNSAFE state, emergency response active
- **Gray**: Stand vacant or out of service

**Alert Indicators**:
- **Count badges**: Number of active alarms per stand (e.g., "3" in red circle = 3 alarms)
- **Flashing**: Stand icon flashes for new alarms (until acknowledged by operator)
- **Sound**: Audible alert for new alarms (tone distinguishes pre-alarm vs alarm vs emergency)

### Stand Detail View

**H₂ Interface Section**:
- H₂ tank pressure gauge (dial or bar chart, with limits marked)
- H₂ flow rate (real-time trend, last 5 minutes)
- Ex zone H₂ concentration (multi-sensor display, heat map showing highest concentration)
- Refuel status (idle, in progress, complete, shutdown)
- Leak detection alarm status (color-coded indicator for each sensor)

**CO₂ Battery Interface Section**:
- Battery voltage, current, SOC (gauges)
- Max cell temperature (gauge + trend chart)
- Cooling system status (flow rate, temperature)
- Charge/discharge status (in progress, complete, fault)
- Fire suppression status (armed, activated, fault)

**Evacuation Interface Section**:
- Door positions (schematic of aircraft with door icons, color-coded: closed, open, slide deployed)
- Passenger count on board (estimate)
- ARFF vehicle positions (map overlay)
- Evacuation timer (if evacuation declared, shows elapsed time since declaration)

### Mobile Dashboard (ARFF Tablet)

**Optimized for Field Use**:
- **Large fonts and icons**: Readable in bright sunlight
- **Touch interface**: Simple tap to acknowledge alarms, request info
- **GPS integration**: Show user's position relative to aircraft on stand map
- **Offline mode**: Last known data cached if wireless link lost

**Prioritized Information**:
1. **Stand safety state** (SAFE/RESTRICTED/UNSAFE) — most prominent
2. **Active hazards**: H₂ leak, fire, thermal runaway (concise text + icon)
3. **Exit availability**: Which doors/slides available for rescue access
4. **Aircraft H₂/CO₂ system status**: Safe to approach or hazard present

## Alert Prioritization and Escalation

### Alert Categories

#### Category 1: Emergency (Immediate Action Required)

**Characteristics**:
- Immediate threat to life or aircraft
- Requires instant response (ARFF, emergency shutdown)
- Automatically escalates to all stakeholders

**Examples**:
- H₂ alarm (≥25% LEL)
- CO₂ battery thermal runaway
- Fire detected (aircraft or ground equipment)
- Evacuation declared

**Alerting**:
- **Control room**: Red flashing banner, loud audible alarm (continuous tone), "Emergency" text
- **ARFF**: Automatic dispatch message (pager, radio, mobile app), location and hazard type
- **Ground supervisor**: Radio alert + SMS/text message
- **OCC**: Automatic notification to operations control center

**Acknowledgment**: Operator must acknowledge within 30 seconds; if no ack, alert escalates to duty manager + backup operator

#### Category 2: Alarm (Urgent, Time-Sensitive)

**Characteristics**:
- Out-of-limits condition requiring prompt action
- May escalate to emergency if not addressed
- Requires operator response within 2-5 minutes

**Examples**:
- H₂ pre-alarm (10-25% LEL, sustained >30 seconds)
- CO₂ battery temperature >60°C
- Insulation resistance <threshold
- Weather exceeding limits (wind, lightning)

**Alerting**:
- **Control room**: Yellow flashing banner, moderate audible alarm (intermittent tone)
- **Ground supervisor**: Radio alert
- **Duty manager**: Email + dashboard notification (no immediate phone/SMS unless unacknowledged >5 minutes)

**Acknowledgment**: Operator must acknowledge within 2 minutes; if no ack, alert escalates to duty manager

#### Category 3: Pre-Alarm (Advisory, Monitoring Required)

**Characteristics**:
- Condition approaching limits but not immediately hazardous
- Provides early warning to prevent escalation
- Operator monitors and may take preventive action

**Examples**:
- H₂ concentration 5-10% LEL (below pre-alarm threshold, but elevated)
- CO₂ battery temperature 50-55°C (warm but not alarm level)
- Weather deteriorating (approaching limits)
- Sensor fault (redundant sensors available)

**Alerting**:
- **Control room**: Blue banner (not flashing), soft audible alert (single chime)
- **Log entry**: Recorded for trending and analysis

**Acknowledgment**: No immediate acknowledgment required; alert clears automatically when condition returns to normal

#### Category 4: Information (Status Change, No Action Required)

**Characteristics**:
- Normal operational events
- Logged for record-keeping and post-ops analysis

**Examples**:
- Refuel start/complete
- Battery docking/undocking
- Stand state change (SAFE ↔ RESTRICTED, if due to planned maintenance)
- Sensor calibration completed

**Alerting**:
- **Control room**: Green notification (bottom of dashboard), no audible alert
- **Log entry**: Recorded with timestamp

### Escalation Logic

**Time-Based Escalation**:
- **Category 1 (Emergency)**: If unacknowledged for 30 seconds → escalate to duty manager + backup control room operator
- **Category 2 (Alarm)**: If unacknowledged for 2 minutes → escalate to duty manager; if unacknowledged for 5 minutes → escalate to airport operations director
- **Category 3 (Pre-Alarm)**: No automatic escalation; if condition worsens → automatic upgrade to Category 2

**Condition-Based Escalation**:
- **Repeat alarms**: If same alarm recurs >3 times in 1 hour → escalate to maintenance team + safety manager
- **Multiple alarms**: If >5 alarms active simultaneously on one stand → escalate to duty manager (potential systemic issue)
- **Cross-stand patterns**: If similar alarms on multiple stands → escalate to infrastructure maintenance (e.g., all H₂ sensors reading high = potential sensor calibration issue or actual area-wide leak)

## Data Integrity and Cybersecurity

### Threat Model for Safety Data

**Threats**:
1. **Data injection**: Attacker sends false alarm or shutdown command
2. **Data spoofing**: Attacker modifies sensor readings to hide hazard (e.g., false "H₂ concentration normal" during actual leak)
3. **Denial of service**: Attacker floods communication channel, preventing real alarms from reaching control room
4. **Replay attack**: Attacker records and replays old "normal" status messages to hide current hazard

### Security Measures

#### Authentication and Encryption

**Cryptographic Protection**:
- **All safety-critical signals** use HMAC (Hash-based Message Authentication Code) with SHA-256
- **Symmetric key**: Pre-shared key between aircraft and infrastructure (updated periodically, e.g., monthly)

**Mutual Authentication**:
- Aircraft and infrastructure exchange certificates (X.509) at connection establishment
- TLS 1.3 for data encryption (prevents eavesdropping)

#### Anomaly Detection

**Signal Validation**:
- **Range checks**: Reject out-of-range values (e.g., H₂ pressure >1000 bar = physically impossible)
- **Rate-of-change limits**: Reject implausible rapid changes (e.g., H₂ concentration 0% to 50% in 1 second = likely spoofed)
- **Redundancy checks**: Compare redundant sensors (e.g., 4 H₂ sensors at connector); alarm if one deviates significantly from others
- **Timestamp validation**: Reject old messages (timestamp >10 seconds in past = likely replay attack)
- **Sequence numbers**: Detect missing or duplicate messages

**Intrusion Detection System (IDS)**:
- Monitor communication patterns for anomalies (e.g., unusual message frequency, unexpected source IP)
- Detect port scanning or unauthorized connection attempts
- Log all rejected messages for forensic analysis

#### Fail-Safe on Cyber Attack

**If attack detected or suspected**:
1. **Isolate compromised system**: Disconnect affected aircraft or infrastructure from network
2. **Default to safe state**: Declare stand UNSAFE, initiate emergency shutdown of energy systems
3. **Manual mode**: Operators rely on local displays and direct observation (no network data)
4. **Investigate**: Cybersecurity team investigates, restores system only after verification

**Graceful Degradation**:
- If data link fails (legitimate or attack), local safety systems continue to operate autonomously
- Local leak detectors, fire detectors, and emergency shutdown systems do not depend on network

### Compliance with DO-326A / ED-202A

Safety monitoring system cybersecurity follows **[DO-326A/ED-202A](https://www.rtca.org/)** (Airworthiness Security Process Specification):
- Security risk assessment for monitoring data interfaces
- Security requirements derived from safety requirements (e.g., "Prevent false H₂ alarm" → "Authenticate all alarm messages")
- Security testing (penetration testing, fuzzing, code review)
- Continuous monitoring and incident response plan

## Performance Monitoring and KPIs

### Safety KPIs (Key Performance Indicators)

**Tracked Monthly**:

| **KPI** | **Target** | **Purpose** |
|---------|-----------|------------|
| H₂ pre-alarms (10-25% LEL) | <5 per month (all stands) | Monitor leak detection sensitivity and H₂ handling procedures |
| H₂ alarms (≥25% LEL) | 0 per month | Verify safety systems effective (any alarm = incident investigation) |
| CO₂ battery temperature excursions (>60°C) | <2 per month | Monitor thermal management effectiveness |
| Thermal runaway events | 0 per month | Ultimate safety metric (any event = major investigation) |
| Emergency shutdowns (H₂ or CO₂) | <3 per month | Distinguish real vs. false alarms; minimize nuisance shutdowns |
| Stand UNSAFE declarations | <5 per month | Monitor overall stand safety (excluding planned maintenance) |
| Sensor faults (H₂, CO₂, fire detection) | <10% of sensors faulted | Maintain sensor availability (redundancy ensures no single point of failure) |
| Data link failures (>10 seconds) | <1 per week | Monitor communication reliability |

**Trending and Analysis**:
- Monthly safety dashboard review (safety manager, ground ops, maintenance)
- Identify trends (e.g., increasing H₂ pre-alarms = potential equipment degradation or procedure drift)
- Implement corrective actions (e.g., retrain ground crews, replace aging sensors, adjust alarm thresholds)

### Predictive Maintenance

**Sensor Health Monitoring**:
- Track sensor performance (response time, noise, drift)
- Predictive alerts (e.g., "H₂ sensor 3 response time increasing, replace within 30 days")
- Proactive replacement before sensor fails (reduces false alarms, maintains safety)

**Equipment Condition Monitoring**:
- H₂ dispenser valve cycling counts (valves have finite lifecycle, e.g., 10,000 cycles)
- CO₂ battery contactor arcing events (each arc reduces contactor life)
- Predictive maintenance scheduling (replace before failure during planned downtime)

## Integration with Airport and Energy Management Systems

### Airport Operations Control Center (OCC)

**Data Provided to OCC**:
- Stand safety states (real-time, all stands)
- Active alarms and emergencies (filtered for OCC relevance)
- ARFF dispatch status
- Weather impacting stand operations

**OCC Use Cases**:
- **Flight planning**: Delay departures if stand UNSAFE (e.g., H₂ leak response in progress)
- **Resource allocation**: Divert aircraft to alternate stand if primary stand UNSAFE
- **Emergency coordination**: Liaise with ARFF, external emergency services, regulatory authorities

### Energy Management System (EMS)

**Data Provided to EMS**:
- H₂ inventory and consumption rate (all dispensers)
- CO₂ battery SOC and availability (all containers)
- Charging/discharging load (aggregate MW for grid coordination)

**EMS Use Cases**:
- **H₂ supply planning**: Predict H₂ demand based on flight schedule, trigger H₂ delivery or production
- **Grid load management**: Schedule CO₂ battery charging during off-peak hours (lower electricity cost)
- **Vehicle-to-Grid (V2G)**: Use parked aircraft with charged CO₂ batteries to provide grid frequency regulation (if supported)

### ARFF Command and Control

**Data Provided to ARFF**:
- Real-time stand safety state and active alarms
- Aircraft exit availability (during emergency)
- H₂/CO₂ system status (safe to approach or hazard present)
- Weather (wind direction for smoke dispersion, rescue vehicle positioning)

**ARFF Use Cases**:
- **Pre-planning**: ARFF reviews stand layouts and BWB exits during training
- **Response**: Tablet displays guide ARFF to correct exits, highlight hazards (H₂, CO₂)
- **Situational awareness**: Aircraft fire detection status helps ARFF assess fire location and severity

## Related Documents

- [85-00-02-001_Safety_Concepts_and_Objectives.md](85-00-02-001_Safety_Concepts_and_Objectives.md) - Safety objectives
- [85-00-02-002_Hazard_Analysis_at_Interface_Level.md](85-00-02-002_Hazard_Analysis_at_Interface_Level.md) - Interface hazards
- [85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md](85-00-02-004_H2_and_CO2_Energy_Safety_Interfaces.md) - Technical interface details
- [85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md](85-00-02-006_Operational_Safety_Procedures_at_Interfaces.md) - Operational procedures
- [ATA 42 IMA Governance](../../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/O-OPERATING_SYSTEMS/ATA_42-IMA_GOVERNANCE/) - On-board data systems

## References

- **ARINC 834**: Aircraft Data Interface Function (potential standard for ground ↔ aircraft data)
- **[DO-326A/ED-202A](https://www.rtca.org/)**: Airworthiness Security Process Specification
- **IEC 62443**: Industrial communication networks — IT security
- **ISO/IEC 27001**: Information security management systems
- **NIST Cybersecurity Framework**: Identify, Protect, Detect, Respond, Recover

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
