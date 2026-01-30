# 85-20-01-005 — H2 Data Interface and Communications

## Document Metadata

```yaml
document_id: "85-20-01-005"
title: "H2 Data Interface and Communications"
parent_system: "85-20-01 H2 Refueling Interface Subsystem"
category: "Component Specification"
status: "DRAFT"
version: "1.0"
last_updated: "2025-11-21"
```

## Purpose

This document specifies the data interfaces and communication protocols that enable refueling authorization, real-time status exchange, and audit logging between the ground refueling system, aircraft, and operations infrastructure.

## Communication Architecture

### Data Flow Overview

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   Aircraft   │◄───────►│  H2 Ground   │◄───────►│  Operations  │
│  (ATA 28)    │  Local  │  Refueling   │  Network│    Center    │
│              │  Link   │   System     │         │  (85-20-06)  │
└──────────────┘         └──────────────┘         └──────────────┘
       │                        │
       │                        │
       ▼                        ▼
  [Aircraft H2          [Refueling Data
   Tank System]          Controller PLC]
```

### Communication Layers

**Layer 1: Aircraft-Ground Local Link**
- Physical: Coupling electrical contacts OR wireless (WiFi, Bluetooth)
- Purpose: Direct aircraft-to-refueling system data exchange

**Layer 2: Ground System Network**
- Physical: Ethernet (wired) or WiFi 6E
- Purpose: Refueling system to airport operations network

**Layer 3: Operations Data**
- Integration with 85-20-06 Data and Communications Subsystem
- Purpose: Central operations monitoring, billing, maintenance

## Aircraft-Ground Data Interface

### Physical Interface Options

**Option A: Electrical Contacts in Coupling (Preferred)**
- **Advantage:** Reliable, no wireless interference
- **Contacts:** 4-8 pins (power, ground, data+, data-, spare)
- **Protection:** Sealed, corrosion-resistant (gold-plated)

**Option B: Wireless (WiFi or Bluetooth)**
- **Advantage:** No additional physical connection
- **Frequency:** 2.4 GHz or 5 GHz (WiFi), 2.4 GHz (Bluetooth)
- **Range:** 5-10 meters (sufficient for refueling area)
- **Security:** WPA3 encryption (WiFi) or pairing (Bluetooth)

**Option C: Hybrid (Wired Primary, Wireless Backup)**
- **Advantage:** Redundancy for reliability

### Communication Protocol

**Preferred: Modbus RTU (for serial/wired) or Modbus TCP (for Ethernet/WiFi)**

**Alternative: OPC UA (Open Platform Communications Unified Architecture)**
- Advantage: More robust, secure, industrial standard
- Disadvantage: More complex implementation

**Data Rate:** Low bandwidth required (1-10 kbps sufficient for status and control)

**Latency:** <500ms for normal data, <100ms for safety-critical interlocks

## Refueling Authorization

### Pre-Refueling Data Exchange

**Aircraft → Ground:**
```yaml
aircraft_id: "N123AM"                  # Aircraft registration
aircraft_type: "AMPEL360-BWB"          # Aircraft model
tank_capacity_kg: 500                  # H2 tank total capacity
current_quantity_kg: 50                # Current H2 on board
target_pressure_bar: 700               # Maximum tank pressure
fuel_type: "GH2"                       # Gaseous H2 (vs. LH2 liquid)
authorization_code: "AUTH987654321"    # Security token
```

**Ground → Aircraft:**
```yaml
authorization_status: "APPROVED"       # or "DENIED" with reason
estimated_duration_min: 15             # Estimated refueling time
dispenser_id: "H2-DISP-03"            # Refueling dispenser identifier
ground_operator_id: "OPS-JD-42"       # Operator badge number
```

### Authorization Validation

**Checks by Ground System:**
1. Aircraft ID valid and in database
2. Authorization code valid (cryptographic verification)
3. Requested H2 type matches ground supply (GH2 vs. LH2)
4. Target pressure within ground system capability
5. Safety interlocks satisfied (from 85-20-01-003)

**Approval:** If all checks pass, authorization granted

**Denial:** If any check fails, refueling inhibited, reason code sent to aircraft

## Real-Time Status Reporting

### During Refueling (1 Hz Update Rate)

**Ground → Aircraft:**
```yaml
timestamp: "2025-11-21T14:35:22Z"
refueling_phase: "BULK_FILL"          # or INITIAL, TOPPING, COMPLETE
flow_rate_kg_per_min: 1.8
total_quantity_transferred_kg: 237.5
tank_pressure_bar: 620
estimated_time_remaining_min: 8
safety_status: "NORMAL"               # or WARNING, CRITICAL
```

**Aircraft → Ground:**
```yaml
timestamp: "2025-11-21T14:35:22Z"
tank_temperature_C: 45
tank_pressure_bar: 618                # Independent measurement
quantity_on_board_kg: 287.5           # Aircraft gauge (may differ slightly)
valves_status: "OPEN"                 # Fill valve status
```

### Alarm and Event Reporting

**Ground → Aircraft (and Operations Center):**
```yaml
alarm_code: "H2_LEAK_DETECTED"
severity: "CRITICAL"
description: "H2 concentration 1.2% at sensor S3"
action_taken: "EMERGENCY_SHUTDOWN"
timestamp: "2025-11-21T14:37:05Z"
```

**Aircraft → Ground:**
```yaml
alert_code: "TANK_OVERPRESSURE"
severity: "WARNING"
description: "Tank pressure 715 bar, near limit 720 bar"
action_requested: "REDUCE_FLOW_RATE"
timestamp: "2025-11-21T14:38:12Z"
```

## Refueling Completion Data

### Completion Record

**Ground → Aircraft and Operations Center:**
```yaml
refueling_id: "RF-20251121-143522-N123AM"
aircraft_id: "N123AM"
start_time: "2025-11-21T14:35:22Z"
end_time: "2025-11-21T14:48:15Z"
duration_min: 12.9
quantity_transferred_kg: 450.2
initial_tank_pressure_bar: 150
final_tank_pressure_bar: 698
average_flow_rate_kg_per_min: 1.75
safety_events: 0                      # Number of alarms during refueling
dispenser_id: "H2-DISP-03"
operator_id: "OPS-JD-42"
billing_amount_USD: 3150.00           # If commercial (450 kg × $7/kg)
signature_hash: "a3f9c2..."           # Cryptographic hash for audit
```

**Aircraft Acknowledgment:**
```yaml
refueling_id: "RF-20251121-143522-N123AM"
acknowledged: true
final_quantity_on_board_kg: 500.5     # Aircraft gauge reading
discrepancy_kg: 0.3                   # Within tolerance
signature_hash: "b7e1d4..."
```

## Audit and Logging

### Ground System Logs

**Refueling Transaction Log:**
- All refueling operations (successful and aborted)
- Complete data record per transaction (as above)
- Retention: 7 years (regulatory requirement)

**Event Log:**
- All alarms, warnings, operator actions
- Timestamp, event code, description, value
- Retention: 3 years

**Maintenance Log:**
- Sensor calibrations, component replacements, functional tests
- Timestamp, activity, technician ID, results
- Retention: Lifetime of equipment

**Data Storage:** Local (on refueling controller) + remote backup (via 85-20-06 to operations center)

### Operations Center Access

**Real-Time Monitoring:**
- Dashboard showing all active refueling operations
- Live data from all H2 dispensers at airport
- Alarm summary and escalation

**Historical Analysis:**
- Query refueling transactions by aircraft, date, dispenser
- Generate reports for billing, safety analysis, maintenance planning
- Export data for regulatory compliance (e.g., H2 usage reporting)

## Cybersecurity

### Threat Model

**Threats:**
1. **Unauthorized Refueling:** Attacker gains authorization code, refuels without paying
2. **Data Tampering:** Attacker modifies quantity data for billing fraud
3. **Denial of Service:** Attacker disrupts communication, prevents refueling
4. **Malware Injection:** Attacker uploads malicious code to refueling controller

### Security Measures

**Authentication:**
- Aircraft authorization code (cryptographic token, rotated daily)
- Operator badge authentication (RFID or biometric)

**Encryption:**
- TLS 1.3 for network communication (ground system ↔ operations center)
- AES-256 for stored data (logs, transaction records)

**Integrity:**
- Digital signatures on refueling completion records (prevent tampering)
- Hash verification on software updates (prevent malware)

**Availability:**
- Redundant communication paths (wired + wireless)
- Offline mode (refueling can proceed if operations center link lost, with local logging)

**Compliance:** Per [DO-326A / ED-202A](https://www.rtca.org/content/standards-guidance-materials) (Airworthiness Security Process Specification)

### Access Control

**Operator Interface (HMI):**
- Login required (username/password or badge)
- Role-based access (Operator: start refueling; Supervisor: override alarms; Maintenance: calibrate sensors)

**Remote Access:**
- VPN required for remote diagnostics
- Two-factor authentication
- Audit log of all remote sessions

## Integration with 85-20-06 Data and Communications

### Data Exchange

**85-20-01 (H2 Refueling) → 85-20-06 (Data/Comms):**
- Real-time refueling status (for operations monitoring)
- Completed transaction records (for billing and audit)
- Maintenance alerts (for predictive maintenance)

**85-20-06 (Data/Comms) → 85-20-01 (H2 Refueling):**
- Aircraft arrival notification (prepare for refueling)
- Authorization updates (revoke if aircraft status changes)
- Weather data (wind, lightning, for safety interlocks)

**Protocol:** RESTful API over HTTPS or MQTT for publish/subscribe

**Data Format:** JSON or XML

### Example API Call (RESTful)

**Refueling Authorization Request:**
```http
POST /api/v1/refueling/authorize
Content-Type: application/json
Authorization: Bearer <API_TOKEN>

{
  "aircraft_id": "N123AM",
  "requested_quantity_kg": 450,
  "authorization_code": "AUTH987654321"
}
```

**Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "authorization_status": "APPROVED",
  "refueling_id": "RF-20251121-143522-N123AM",
  "estimated_duration_min": 15
}
```

## Performance Requirements

| Parameter | Value | Notes |
|-----------|-------|-------|
| Data Latency (Normal) | <500 ms | For status updates |
| Data Latency (Safety-Critical) | <100 ms | For emergency shutdown |
| Message Loss Rate | <0.1% | Acceptable packet loss |
| Communication Range (Wireless) | 10 m | Minimum |
| Data Encryption | AES-256 | For sensitive data |
| Log Retention | 7 years | Transaction logs |

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-21

---

*Reference: [85-20-01 H2 Refueling Interface Subsystem README](./README.md)*
