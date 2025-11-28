# OFEC Protocol Overview

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-23-95-60-60-OV-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |
| **Classification** | INTERNAL |

---

## 1. Introduction

The OFEC Protocol (60-60) defines the transport layer for Operational Flight Envelope Channel data within the FAirCCC architecture. This is the L2-LINKS component that handles how envelope data is transmitted from aircraft to ground systems.

### 1.1 Purpose

- Transport envelope analytics data from aircraft to ground
- Provide phase-aware publishing rates
- Ensure secure and reliable data transmission
- Support regional aggregation and fleet analytics

### 1.2 Relationship to N-Axis

| N-Axis (97-40-40) | L2-LINKS (60-60) |
|-------------------|------------------|
| What data means | How to transmit |
| Margin calculations | Message encoding |
| Advisory logic | Transport security |
| Envelope models | Publishing rates |

---

## 2. Protocol Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    OFEC PROTOCOL (60-60)                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │              AIRCRAFT PUBLISHER (60-60-10)            │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐  │ │
│  │  │  Envelope   │  │   Message   │  │ Phase-Aware  │  │ │
│  │  │  Sampler    │─▶│   Builder   │─▶│  Publisher   │  │ │
│  │  └─────────────┘  └─────────────┘  └──────────────┘  │ │
│  └───────────────────────────────────────────────────────┘ │
│                            │                                │
│                            │ mTLS 1.3 / CBOR                │
│                            ▼                                │
│  ┌───────────────────────────────────────────────────────┐ │
│  │               GROUND RECEIVER (60-60-20)              │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐  │ │
│  │  │   Message   │  │ Validation  │  │   Storage    │  │ │
│  │  │   Decoder   │─▶│   Engine    │─▶│   Handler    │  │ │
│  │  └─────────────┘  └─────────────┘  └──────────────┘  │ │
│  └───────────────────────────────────────────────────────┘ │
│                            │                                │
│                            ▼                                │
│  ┌───────────────────────────────────────────────────────┐ │
│  │            REGIONAL AGGREGATOR (60-60-30)             │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐  │ │
│  │  │ Multi-A/C   │  │   Fleet     │  │   Uplink     │  │ │
│  │  │ Aggregation │─▶│  Analytics  │─▶│  to Core     │  │ │
│  │  └─────────────┘  └─────────────┘  └──────────────┘  │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Key Components

| Component | ATA Reference | Purpose |
|-----------|---------------|---------|
| Aircraft Publisher | 60-60-10 | Sample, encode, publish envelope data |
| Ground Receiver | 60-60-20 | Decode, validate, store, alert |
| Regional Aggregator | 60-60-30 | Multi-aircraft aggregation, fleet analytics |
| Security | 60-60-40 | Authentication, encryption, integrity |
| Schemas | 60-60-90 | Transport message formats |

---

## 4. Transport Characteristics

| Aspect | Specification |
|--------|---------------|
| Protocol | HTTPS/2 over mTLS 1.3 |
| Encoding | CBOR (Concise Binary Object Representation) |
| Rate | 0.1 - 10 Hz (phase-dependent) |
| Message Size | ~500 bytes typical |
| Latency | < 100 ms aircraft-to-ground |
| Reliability | At-least-once delivery |

---

## 5. Phase-Aware Publishing

| Flight Phase | Rate (Hz) | Priority | Preemptible |
|--------------|-----------|----------|-------------|
| GROUND | 0.1 | LOW | Yes |
| TAXI | 0.5 | LOW | Yes |
| TAKEOFF | 10 | HIGH | No |
| CLIMB | 5 | MEDIUM | Yes |
| CRUISE | 1 | LOW | Yes |
| DESCENT | 5 | MEDIUM | Yes |
| APPROACH | 10 | HIGH | No |
| LANDING | 10 | HIGH | No |

---

## 6. Security Model

- **Authentication**: Mutual TLS with TPM-anchored certificates
- **Encryption**: TLS 1.3 (AES-256-GCM)
- **Integrity**: HMAC-SHA256 message signatures
- **Authorization**: Aircraft identity verified against fleet registry

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
