# 23-97-60-010 — MMIP ⇄ FAirCCC Integration

**Document ID:** 23-97-60-010_MMIP_FAIRCCC_Integration  
**Chapter:** ATA 23-97-60 INHERITANCE  
**Version:** 0.1  
**Status:** DRAFT  

---

## 1. Purpose

Define how **MMIP Memory Envelopes** are transported over the **FAirCCC /
CFLF** communication fabric so that:

- Memory inheritance is **transport-agnostic but real-time capable**.
- CAOS agents exchange context via a **standard payload format**.
- FAirCCC channels handle QoS, while MMIP handles semantic memory.

---

## 2. Roles

- **MMIP**: Defines capsule/thread/package/envelope formats and inheritance
  semantics.
- **FAirCCC / CFLF**: Provides transport channels and QoS profiles:
  - `CFLF-GRAD` — gradient envelopes / model updates
  - `CFLF-MODEL` — model artefacts
  - `CFLF-TELEM` — telemetry
  - `CFLF-SAFETY` — safety-critical alerts
  - `CFLF-MMIP` — proposed **dedicated channel class** for MMIP envelopes

---

## 3. Envelope on the Wire

Canonical representation for FAirCCC payload:

```json
{
  "protocol": "MMIP",
  "version": "0.1",
  "envelope": {
    "mmip_version": "0.1",
    "context_id": "ctx_9876",
    "thread_id": "thr_CAOS_MISSION_001",
    "producer": {
      "id": "CAOS_SHM",
      "role": "agent",
      "type": "agent",
      "version": "1.0.0"
    },
    "policies": { "...": "..." },
    "capsules": [ /* see capsule.json */ ],
    "integrity": {
      "hash": "sha256:...",
      "signature": "..."
    }
  },
  "transport_meta": {
    "channel": "CFLF-MMIP",
    "priority": "MEDIUM",
    "ttl_ms": 5000
  }
}
```

- MMIP remains **agnostic** of FAirCCC specifics.
- FAirCCC treats the `envelope` as an opaque payload with integrity hints.

---

## 4. Channel Binding

### 4.1 Dedicated MMIP Channel

Define `CFLF-MMIP` as:

- Class: **control / cognitive context**
- Priority: medium (below safety, above bulk logs)
- Reliability: at-least-once for safety-related threads, best-effort allowed for
  non-critical contexts.

### 4.2 Existing Channels

For tightly coupled contexts:

- Safety-critical memory envelopes MAY be duplicated on `CFLF-SAFETY`.
- Bulk historical context MAY be offloaded to storage and referenced via
  `external_refs` in the envelope instead of inlining all capsules.

---

## 5. Inheritance on Node Boundaries

At each FAirCCC node (e.g., agent, digital twin service):

1. Receive MMIP envelope over FAirCCC channel.
2. Validate envelope integrity and policies.
3. Attach capsules to local thread via `ATTACH_MEMORY`.
4. On subsequent model/agent calls, use `INHERIT_CONTEXT` locally.

This pattern ensures **local MMIP continuity** even if transport is intermittent.

---

## 6. Failure Handling

- If envelope fails integrity verification:
  - MUST NOT be used as context.
  - MAY be stored as corrupted artefact for forensic analysis.
- If capsule policies forbid cross-boundary export:
  - MMIP engine MUST strip or redact before sending over FAirCCC.
  - Such transformations MUST be recorded in `provenance.transformations`.

---

## 7. References

- [MMIP v0.1 Specification](../../../../../../mmip-standard/spec/mmip-v0.1.md)
- [MMIP Envelope Schema](../../../../../../mmip-standard/schemas/envelope.json)
- [23-95 COMM_NN (FAirCCC)](../../23-95_COMM_NN/)

---

## 8. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-28.

---
