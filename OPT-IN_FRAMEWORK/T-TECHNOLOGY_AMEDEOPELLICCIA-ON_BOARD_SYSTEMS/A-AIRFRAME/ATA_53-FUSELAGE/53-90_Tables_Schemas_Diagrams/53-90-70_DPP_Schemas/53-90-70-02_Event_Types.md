# 53-90-70-02 DPP Event Types

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-70-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / DATA |
| **ATA Chapter** | 53-90-70 |

---

## 1. Purpose

This document defines the Digital Product Passport (DPP) event types for tracking the lifecycle of ANCHORS components.

## 2. Event Type Definitions

### 2.1 Lifecycle Events

| Event Type | Code | Description | Trigger |
|------------|------|-------------|---------|
| INSTALLATION | INST | Component installed on aircraft | Physical installation |
| REMOVAL | REMV | Component removed from aircraft | Physical removal |
| SWAP | SWAP | QuickSwap exchange operation | Ground turnaround |
| END_OF_LIFE | EOL | Component retired from service | Disposal decision |

### 2.2 Maintenance Events

| Event Type | Code | Description | Trigger |
|------------|------|-------------|---------|
| INSPECTION | INSP | Scheduled or unscheduled inspection | Maintenance task |
| MAINTENANCE | MNTC | Corrective or preventive action | Work order |
| OVERHAUL | OVHL | Major overhaul activity | Time limit |
| MODIFICATION | MOD | Design modification applied | Engineering order |

### 2.3 Operational Events

| Event Type | Code | Description | Trigger |
|------------|------|-------------|---------|
| FAULT | FALT | Fault condition detected | BITE/monitoring |
| CALIBRATION | CALB | Sensor calibration performed | Maintenance |
| SOFTWARE_UPDATE | SWUP | Software version changed | Update procedure |
| CONFIGURATION | CONF | Parameter configuration changed | Maintenance |

## 3. Event Data Requirements

### 3.1 Common Fields (All Events)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| event_id | UUID | Yes | Unique event identifier |
| event_type | Enum | Yes | Event type code |
| timestamp | ISO 8601 | Yes | Event occurrence time |
| component_id | String | Yes | Component identifier |
| operator_id | String | No | Personnel identifier |
| work_order | String | No | Associated work order |
| signature | String | No | Digital signature |

### 3.2 Event-Specific Fields

#### INSTALLATION

| Field | Required | Description |
|-------|----------|-------------|
| msn | Yes | Aircraft serial number |
| location.zone | Yes | Installation zone |
| location.position | Yes | Specific position |
| previous_msn | No | Previous aircraft if transferred |

#### REMOVAL

| Field | Required | Description |
|-------|----------|-------------|
| reason | Yes | Removal reason code |
| condition | Yes | Component condition (SERVICEABLE, REPAIRABLE, SCRAP) |
| destination | No | Where component is going |

#### FAULT

| Field | Required | Description |
|-------|----------|-------------|
| fault_code | Yes | Fault identifier |
| severity | Yes | Fault severity (INFO, WARNING, CAUTION, FAULT) |
| description | No | Fault description |
| flight_phase | No | Phase when detected |

#### SWAP

| Field | Required | Description |
|-------|----------|-------------|
| old_component_id | Yes | Removed component |
| new_component_id | Yes | Installed component |
| swap_reason | No | Reason for swap |
| swap_time_min | No | Swap duration |

#### SOFTWARE_UPDATE

| Field | Required | Description |
|-------|----------|-------------|
| old_version | Yes | Previous software version |
| new_version | Yes | New software version |
| update_source | No | Update source (OEM, SB, etc.) |

## 4. Event Workflow

### 4.1 Event Generation

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   TRIGGER   │────▶│   CAPTURE   │────▶│   VALIDATE  │
│  (Physical/ │     │  (System/   │     │  (Schema    │
│   Digital)  │     │   Manual)   │     │   Check)    │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                    ┌─────────────┐     ┌──────▼──────┐
                    │   ARCHIVE   │◀────│    STORE    │
                    │  (Long-term │     │  (DPP       │
                    │   Storage)  │     │   Database) │
                    └─────────────┘     └─────────────┘
```

### 4.2 Event Validation

| Check | Description | Action on Fail |
|-------|-------------|----------------|
| Schema | Validate against JSON schema | Reject |
| Component | Verify component exists | Reject |
| Sequence | Check event sequence valid | Flag |
| Signature | Verify digital signature | Flag |
| Timestamp | Check timestamp reasonable | Flag |

## 5. Event Retention

| Event Category | Active Period | Archive Period | Total |
|----------------|---------------|----------------|-------|
| Safety Events | 5 years | 25 years | 30 years |
| Maintenance | 3 years | 20 years | 23 years |
| Operational | 2 years | 10 years | 12 years |
| Informational | 1 year | 5 years | 6 years |

## 6. Integration Points

### 6.1 System Interfaces

| System | Direction | Events | Format |
|--------|-----------|--------|--------|
| CMC | Inbound | FAULT, MNTC | AFDX JSON |
| MRO System | Bidirectional | All maintenance | API REST |
| Ground Support | Inbound | SWAP | CAN/USB |
| OEM System | Outbound | INST, REMV, EOL | S1000D |
| Regulatory | Outbound | Safety events | XML |

### 6.2 Notification Rules

| Event Type | Notification | Recipients |
|------------|--------------|------------|
| FAULT (Critical) | Immediate | Operations, Engineering |
| INSTALLATION | Same day | Asset Management |
| OVERHAUL | Weekly digest | Maintenance Planning |
| EOL | As occurs | Sustainability, Procurement |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
