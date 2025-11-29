# Envelope Sampler Specification

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-23-95-67-11-SPEC-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Overview

The Envelope Sampler acquires envelope analytics data from the N-Axis component (97-40-40) at the rate required by the current flight phase.

---

## 2. Input Interface

| Source | Data | Rate |
|--------|------|------|
| Margin Calculator | All margin values | On-demand |
| Advisory Engine | Advisory state | On-demand |
| Flight Phase | Current phase | 1 Hz |

---

## 3. Sampling Strategy

- **Synchronous**: Sample at phase-determined rate
- **Event-driven**: Immediate sample on advisory change
- **Buffered**: Queue samples during rate transitions

---

## 4. Data Quality

| Check | Action |
|-------|--------|
| Timestamp validation | Reject stale data (> 100ms) |
| Range check | Flag out-of-range values |
| Consistency | Cross-check redundant sources |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.
