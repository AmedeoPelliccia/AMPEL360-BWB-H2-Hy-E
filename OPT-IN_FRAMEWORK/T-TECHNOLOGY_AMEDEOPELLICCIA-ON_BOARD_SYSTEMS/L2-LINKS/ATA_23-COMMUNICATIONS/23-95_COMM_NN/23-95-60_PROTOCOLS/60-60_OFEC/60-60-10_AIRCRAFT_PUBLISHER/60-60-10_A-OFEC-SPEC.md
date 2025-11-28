# Aircraft OFEC Publisher Specification

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-60-60-10-SPEC-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Overview

The Aircraft OFEC Publisher (A-OFEC) is responsible for sampling envelope analytics data, encoding it, and publishing to ground stations with phase-aware rate control.

---

## 2. Components

| Component | Purpose |
|-----------|---------|
| Envelope Sampler | Acquire data from Envelope Analytics (97-40-40) |
| Message Builder | Construct OFEC messages |
| Phase-Aware Publisher | Control publish rate based on flight phase |

---

## 3. Data Flow

```
┌──────────────────────────────────────────────────────────┐
│                  AIRCRAFT PUBLISHER                      │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌─────────────┐ │
│  │   Envelope   │   │   Message    │   │   Phase     │ │
│  │   Sampler    │──▶│   Builder    │──▶│   Aware     │ │
│  │              │   │              │   │  Publisher  │ │
│  └──────────────┘   └──────────────┘   └─────────────┘ │
│        ▲                   ▲                  │         │
│        │                   │                  │         │
│   97-40-40             Schemas           mTLS/CBOR     │
│   Interface              90                   │         │
│                                               ▼         │
│                                         Ground Rx       │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 4. Phase-Aware Publishing

The publisher adjusts transmission rate based on current flight phase:

| Phase | Rate | Rationale |
|-------|------|-----------|
| TAKEOFF | 10 Hz | Critical phase, high margin sensitivity |
| LANDING | 10 Hz | Critical phase, high margin sensitivity |
| APPROACH | 10 Hz | Critical phase, margin monitoring important |
| CLIMB | 5 Hz | Dynamic phase, frequent updates needed |
| DESCENT | 5 Hz | Dynamic phase, frequent updates needed |
| CRUISE | 1 Hz | Stable phase, lower rate sufficient |
| TAXI | 0.5 Hz | Ground ops, minimal updates |
| GROUND | 0.1 Hz | Parked, very low rate |

---

## 5. Message Encoding

- Primary encoding: CBOR (RFC 8949)
- Fallback: JSON (for debugging/testing)
- Compression: Optional LZ4 for large messages

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
