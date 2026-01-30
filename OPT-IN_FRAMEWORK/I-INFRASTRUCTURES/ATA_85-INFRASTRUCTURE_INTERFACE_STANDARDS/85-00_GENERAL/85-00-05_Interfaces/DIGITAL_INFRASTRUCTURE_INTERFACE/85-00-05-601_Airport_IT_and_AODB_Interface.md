# 85-00-05-601: Airport IT and AODB Interface

## 1. Introduction
This document defines the interface between the aircraft's information systems and the Airport Operational Database (AODB).

## 2. Data Exchange
*   **Protocol:** [AIDX](https://www.iata.org/en/programs/passenger/aidx/) (Aviation Information Data Exchange) XML/JSON.
*   **Transport:** 4G/5G, Wi-Fi (Gatelink).
*   **Data Points:** ETA, ETD, Pax Count, Baggage Status.

## 3. Requirements
*   **REQ-D-001:** The aircraft shall automatically connect to the secure airport network upon block-on.
*   **REQ-D-002:** Data transmission shall be encrypted (TLS 1.3).


---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
