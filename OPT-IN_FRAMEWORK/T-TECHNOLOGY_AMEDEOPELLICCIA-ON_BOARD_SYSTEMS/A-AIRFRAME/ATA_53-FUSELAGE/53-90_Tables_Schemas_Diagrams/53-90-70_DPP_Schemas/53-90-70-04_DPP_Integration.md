# 53-90-70-04 DPP Integration

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-70-04 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / INTEGRATION |
| **ATA Chapter** | 53-90-70 |

---

## 1. Purpose

This document defines the integration architecture for the ANCHORS Digital Product Passport (DPP) system, including interfaces to aircraft systems, ground systems, and external stakeholders.

## 2. DPP Architecture Overview

### 2.1 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     ANCHORS DPP ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   AIRCRAFT SYSTEMS                        │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐     │  │
│  │  │   BMS   │  │   TMS   │  │  CO2C   │  │   EMS   │     │  │
│  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘     │  │
│  │       │            │            │            │           │  │
│  │       └────────────┴────────────┴────────────┘           │  │
│  │                         │                                 │  │
│  │  ┌──────────────────────▼──────────────────────┐         │  │
│  │  │              DPP AGGREGATOR                  │         │  │
│  │  │  - Event Collection    - Data Validation    │         │  │
│  │  │  - Local Storage       - Compression        │         │  │
│  │  └──────────────────────┬──────────────────────┘         │  │
│  └─────────────────────────┼────────────────────────────────┘  │
│                            │                                    │
│  ┌─────────────────────────▼────────────────────────────────┐  │
│  │                   GROUND SYSTEMS                          │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐     │  │
│  │  │   CMC   │  │   GSE   │  │   MRO   │  │  CLOUD  │     │  │
│  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘     │  │
│  │       └────────────┴────────────┴────────────┘           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Data Flow

| Flow | Source | Destination | Protocol | Frequency |
|------|--------|-------------|----------|-----------|
| Telemetry | Aircraft LRUs | DPP Aggregator | AFDX | Continuous |
| Events | DPP Aggregator | Ground Storage | WiFi/LTE | On event |
| Bulk Data | Aircraft | Ground | USB | End of flight |
| Queries | MRO/OEM | Cloud | REST API | On demand |
| Reports | Cloud | Regulators | S1000D/XML | Periodic |

## 3. Interface Specifications

### 3.1 Aircraft Interfaces

#### AFDX Interface

| Parameter | Value |
|-----------|-------|
| VL ID | VL_5313 |
| BAG | 1000 ms |
| MTU | 256 bytes |
| Format | JSON |

#### CAN Interface

| Parameter | Value |
|-----------|-------|
| Bus | CAN B (Maintenance) |
| ID Range | 0x700-0x7FF |
| Data Rate | 500 kbps |
| Format | Binary |

### 3.2 Ground Interfaces

#### REST API

```
Base URL: https://dpp.ampel360.aero/api/v1

Endpoints:
  GET  /components/{id}           - Get component record
  GET  /components/{id}/events    - Get component events
  POST /components/{id}/events    - Add new event
  GET  /components/{id}/metrics   - Get circular metrics
  GET  /fleet/{msn}/components    - List aircraft components
  GET  /reports/sustainability    - Get sustainability report
```

#### Authentication

| Method | Use Case |
|--------|----------|
| OAuth 2.0 | External API access |
| mTLS | System-to-system |
| API Key | Internal services |

### 3.3 Data Formats

| Interface | Format | Schema |
|-----------|--------|--------|
| Aircraft → Aggregator | Binary | `53-90-30-03_Message_Structures.h` |
| Aggregator → Ground | JSON | `53-90-40-03_DPP_Event_Schema.json` |
| API Responses | JSON | OpenAPI 3.0 |
| Regulatory | XML | S1000D / ED-324 |

## 4. Security Requirements

### 4.1 Data Protection

| Layer | Protection | Standard |
|-------|------------|----------|
| Transport | TLS 1.3 | RFC 8446 |
| Storage | AES-256 | FIPS 197 |
| Signature | ECDSA | FIPS 186-4 |
| Authentication | OAuth 2.0 | RFC 6749 |

### 4.2 Access Control

| Role | Read | Write | Admin |
|------|------|-------|-------|
| Operator | Fleet | Events | No |
| MRO | Assigned A/C | Events | No |
| OEM | All | Design data | Components |
| Regulator | Safety data | No | No |
| Recycler | EOL components | EOL events | No |

## 5. Implementation

### 5.1 Aircraft Components

| Component | Function | Location |
|-----------|----------|----------|
| DPP Aggregator | Data collection and storage | IMA Cabinet |
| RFID Reader | Component identification | QuickSwap Bay |
| Wireless Module | Ground upload | Avionics Bay |

### 5.2 Ground Components

| Component | Function | Location |
|-----------|----------|----------|
| Edge Gateway | Data reception | Airport |
| Cloud Platform | Central storage | Data Center |
| API Gateway | External access | Cloud |
| Analytics Engine | Reporting | Cloud |

### 5.3 Data Storage

| Tier | Data Type | Retention | Storage |
|------|-----------|-----------|---------|
| Hot | Recent events | 30 days | SSD |
| Warm | Historical | 2 years | HDD |
| Cold | Archive | 30 years | Object Storage |

## 6. Certification Considerations

### 6.1 DO-178C Compliance

| Aspect | DAL | Evidence |
|--------|-----|----------|
| DPP Aggregator SW | D | SAS, Test Results |
| Data Integrity | D | Checksum verification |
| Ground Systems | N/A | Non-airborne |

### 6.2 Data Integrity

| Check | Method | Frequency |
|-------|--------|-----------|
| Event Integrity | CRC-32 | Per event |
| Component Linking | Hash chain | On update |
| Archive Integrity | SHA-256 | Daily |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---
