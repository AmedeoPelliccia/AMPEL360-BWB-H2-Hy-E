# OFEC Channel Specification

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-23-95-67-00-CS-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Channel Definition

| Attribute | Value |
|-----------|-------|
| Channel ID | OFEC |
| Full Name | Operational Flight Envelope Channel |
| Direction | Aircraft → Ground/Regional |
| Classification | Telemetry |
| Safety Level | Advisory (non-safety-critical) |

---

## 2. Message Flow

```
Aircraft                    Ground                     Regional
   │                          │                           │
   │  envelope_state_msg      │                           │
   │─────────────────────────▶│                           │
   │                          │  validated_record         │
   │                          │──────────────────────────▶│
   │                          │                           │
   │                          │  alert (if triggered)     │
   │                          │──────────────────────────▶│
   │                          │                           │
   │                          │         aggregated_summary│
   │                          │◀──────────────────────────│
```

---

## 3. Message Types

| Message | Direction | Purpose |
|---------|-----------|---------|
| EnvelopeState | A→G | Primary telemetry message |
| AdvisoryEvent | A→G | Advisory state changes |
| Acknowledgment | G→A | Optional delivery confirmation |
| SummaryReport | G→R | Aggregated flight data |

---

## 4. Endpoints

### 4.1 Aircraft Publisher

```
POST /ofec/v1/envelope
Content-Type: application/cbor
Authorization: Bearer <jwt>
```

### 4.2 Ground Receiver

```
URL: wss://ground.faircc.aero/ofec/v1/stream
Protocol: WebSocket over mTLS
```

### 4.3 Regional Aggregator

```
URL: https://regional.faircc.aero/ofec/v1/aggregate
Method: POST
```

---

## 5. Quality of Service

| Aspect | Specification |
|--------|---------------|
| Delivery | At-least-once |
| Ordering | Best-effort (timestamps for reordering) |
| Buffering | Up to 1000 messages during connectivity loss |
| Retry | Exponential backoff (1s, 2s, 4s, max 30s) |

---

## 6. Rate Limiting

| Context | Limit |
|---------|-------|
| Per aircraft | 100 msg/sec max |
| Per ground station | 10,000 msg/sec |
| Per regional hub | 100,000 msg/sec |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
