# 61-00-05-03-03A - Discrete Signals Interface

**Document ID:** 61-00-05-03-03A  
**Title:** Discrete Signals Data Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the discrete signal data interface for safety-critical and time-critical propulsor commands and status signals transmitted via data buses (complementing hardware discrete signals defined in 61-00-05-02-02A).

---

## 2. Scope

This specification covers:
- Discrete signal encoding on AFDX/ARINC 429 networks
- Redundancy and cross-channel monitoring
- Latency and determinism requirements
- Fault detection and Built-In Test (BIT)

### 2.1 Applicable Units
- All four Q100 propulsor units

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements |
| 61-00-05-02-02A | Control Signals (Hardware) | Complementary interface |
| [ARINC 429-18](https://www.aviation-ia.com/arinc-429/) | Mark 33 Digital Information Transfer System | Standard |

---

## 4. Interface Description

### 4.1 Discrete Signal Definitions

| Signal Name | Encoding | Bus Type | Update Rate | Criticality |
|-------------|----------|----------|-------------|-------------|
| Propulsor Enable | Boolean | AFDX VL-6101 | 100 Hz | Safety-critical |
| Emergency Shutdown | Boolean | Hardware + AFDX | 100 Hz | Safety-critical |
| Operating Mode | 3-bit enum | AFDX VL-6101 | 50 Hz | Critical |
| Fault Active | Boolean array (32 bits) | AFDX VL-6111 | On change | Critical |
| Health Status | 2-bit enum | AFDX VL-6111 | 10 Hz | Important |
| Maintenance Request | Boolean | ARINC 429 Label 102 | On change | Non-critical |

### 4.2 Encoding Specifications

| Parameter | Value/Spec |
|-----------|------------|
| Boolean True | 0x01 |
| Boolean False | 0x00 |
| Invalid/No Data | 0xFF |
| Operating Mode Values | 0=Off, 1=Idle, 2=Normal, 3=Reverse, 4-7=Reserved |
| Health Status Values | 0=Fail, 1=Degraded, 2=Normal, 3=Test |

### 4.3 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| DIS-61-001 | Maximum latency (safety-critical) | <5 ms | Test |
| DIS-61-002 | Update determinism | ±1 ms jitter | Test |
| DIS-61-003 | Fault detection (data corruption) | 100% via CRC | Design, Test |
| DIS-61-004 | Cross-channel comparison | Mismatch detection <10 ms | Test |

---

## 5. Interface Control

### 5.1 Message Format (AFDX)

Discrete signals embedded in AFDX messages (see 61-00-05-03-02A for full format):
- Bit-packed within message payload
- Each signal occupies minimum bits required
- Reserved bits set to 0

### 5.2 Message Format (ARINC 429)

Discrete signals encoded per ARINC 429 standard:
- Bits 29-11: Discrete data (bit-mapped)
- SSM: Normal Operation (NO) or Fault Warning (FW)

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| DIS-T-001 | Latency measurement | <5 ms for safety-critical | Network analyzer |
| DIS-T-002 | Jitter measurement | ±1 ms | Statistical analysis |
| DIS-T-003 | Fault injection | Detect 100% of corrupted signals | Test |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Signal encoding verification | 100% (First Article) | Automated test |
| Cross-channel comparison | 100% | Automated test |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 27](../../../../F-FLIGHT_CONTROLS/ATA_27-FLIGHT_CONTROLS/README.md) — Flight Controls

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-02-02A — Control Signals (Hardware discrete)
- 61-00-05-03-02A — AFDX Networks

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-03-02A_AFDX_Networks](61-00-05-03-02A_AFDX_Networks.md) · [Next: 61-00-05-03-04A_CAN_Bus_Links](61-00-05-03-04A_CAN_Bus_Links.md) →

---

**AMPEL360 Q100 — OPT-IN Framework Documentation**  
ATA 61 — Propellers and Propulsors — Data Interfaces  

© AMPEL360 Program — All rights reserved.

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
