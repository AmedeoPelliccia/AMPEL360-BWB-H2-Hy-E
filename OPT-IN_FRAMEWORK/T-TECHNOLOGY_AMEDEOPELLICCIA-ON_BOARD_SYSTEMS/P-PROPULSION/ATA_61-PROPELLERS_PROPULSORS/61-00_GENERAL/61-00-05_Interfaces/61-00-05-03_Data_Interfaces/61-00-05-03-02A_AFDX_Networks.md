# 61-00-05-03-02A - AFDX Networks Interface

**Document ID:** 61-00-05-03-02A  
**Title:** AFDX Networks Interface Specification  
**ATA Chapter:** 61 — Propellers and Propulsors  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

This document defines the Avionics Full-Duplex Switched Ethernet (AFDX) network interface for high-speed, deterministic data communication between the Q100 propulsor control units and the aircraft flight control and health management systems.

---

## 2. Scope

This specification covers:
- AFDX physical layer (ARINC 664 Part 7)
- Virtual Link (VL) definitions and bandwidth allocation
- End system requirements
- Network redundancy and fault tolerance
- Quality of Service (QoS) requirements

### 2.1 Applicable Units
- All four Q100 propulsor units
- Dual redundant AFDX networks (A/B)

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| 61-00-03-004 | Interface Requirements | Parent requirements document |
| [ARINC 664 Part 7](https://www.aviation-ia.com/arinc-664/) | Aircraft Data Network | Industry standard |
| [DO-178C](https://www.rtca.org/content/standards-guidance-materials) | Software Considerations in Airborne Systems | Software development |
| [IEEE 802.3](https://standards.ieee.org/standard/802_3-2018.html) | Ethernet Standards | Physical layer |

---

## 4. Interface Description

### 4.1 Physical Characteristics

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Physical Layer | 100BASE-TX | — | Fast Ethernet |
| Data Rate | 100 | Mbps | Full-duplex |
| Cable Type | Quad shielded twisted pair | — | ARINC 664 compliant |
| Connector Type | RJ-45 or M12 D-coded | — | Per aircraft standard |
| Number of Networks | 2 (A/B) | — | Redundant |
| Maximum Frame Size | 1,518 | bytes | Standard Ethernet |
| Bandwidth Allocation Gap (BAG) | 2-128 | ms | Per virtual link |

### 4.2 Virtual Link (VL) Definitions

#### 4.2.1 Critical Control Data (Propulsor ← Flight Control)

| VL ID | Source | Destination | BAG | Max Frame Size | Bandwidth | Priority |
|-------|--------|-------------|-----|----------------|-----------|----------|
| VL-6101 | Flight Control Computer A | Propulsor 1-4 PCU | 4 ms | 256 bytes | 512 kbps | High |
| VL-6102 | Flight Control Computer B | Propulsor 1-4 PCU | 4 ms | 256 bytes | 512 kbps | High |

#### 4.2.2 Propulsor Status and Feedback (Propulsor → Flight Control)

| VL ID | Source | Destination | BAG | Max Frame Size | Bandwidth | Priority |
|-------|--------|-------------|-----|----------------|-----------|----------|
| VL-6111 | Propulsor 1 PCU | Flight Control Computers | 8 ms | 512 bytes | 512 kbps | High |
| VL-6112 | Propulsor 2 PCU | Flight Control Computers | 8 ms | 512 bytes | 512 kbps | High |
| VL-6113 | Propulsor 3 PCU | Flight Control Computers | 8 ms | 512 bytes | 512 kbps | High |
| VL-6114 | Propulsor 4 PCU | Flight Control Computers | 8 ms | 512 bytes | 512 kbps | High |

#### 4.2.3 Health Monitoring Data (Propulsor → Health Monitoring)

| VL ID | Source | Destination | BAG | Max Frame Size | Bandwidth | Priority |
|-------|--------|-------------|-----|----------------|-----------|----------|
| VL-6121 | Propulsor 1-4 PCU | Health Monitoring Computer | 32 ms | 1,024 bytes | 256 kbps | Medium |

#### 4.2.4 Maintenance Data (Propulsor → CMC)

| VL ID | Source | Destination | BAG | Max Frame Size | Bandwidth | Priority |
|-------|--------|-------------|-----|----------------|-----------|----------|
| VL-6131 | Propulsor 1-4 PCU | Central Maintenance Computer | 128 ms | 1,024 bytes | 64 kbps | Low |

### 4.3 Functional Requirements

| Requirement ID | Requirement | Value/Spec | Verification |
|----------------|-------------|------------|--------------|
| AFDX-61-001 | End-to-end latency (critical control) | <10 ms (99.9th percentile) | Test |
| AFDX-61-002 | Frame loss rate | <10⁻⁷ | Test |
| AFDX-61-003 | Network switching time (redundancy) | <100 ms | Test |
| AFDX-61-004 | Bandwidth utilization | <70% per network | Analysis |
| AFDX-61-005 | Virtual link jitter | <1 ms | Measurement |
| AFDX-61-006 | Message integrity check | CRC-32 | Design |
| AFDX-61-007 | Time synchronization accuracy | ±1 ms | Test |

### 4.4 Environmental Constraints

| Parameter | Operating Range | Unit | Notes |
|-----------|----------------|------|-------|
| Temperature | -40 to +85 | °C | Per DO-160G |
| Vibration | 10g RMS | g | Per DO-160G Category T |
| EMI Immunity | Per DO-160G Category M | — | High intensity fields |

---

## 5. Interface Control

### 5.1 AFDX Message Formats

#### 5.1.1 Thrust Command Message (VL-6101/6102)

| Field | Size (bytes) | Description |
|-------|--------------|-------------|
| Message ID | 2 | 0x6101 |
| Timestamp | 4 | System time (ms) |
| Propulsor 1 Thrust Command | 4 | Float (0.0-1.0, normalized) |
| Propulsor 2 Thrust Command | 4 | Float (0.0-1.0) |
| Propulsor 3 Thrust Command | 4 | Float (0.0-1.0) |
| Propulsor 4 Thrust Command | 4 | Float (0.0-1.0) |
| Mode Command | 2 | Bit field (normal/reverse/idle) |
| CRC | 2 | Message integrity |

#### 5.1.2 Propulsor Status Message (VL-6111-6114)

| Field | Size (bytes) | Description |
|-------|--------------|-------------|
| Message ID | 2 | 0x6111-0x6114 |
| Timestamp | 4 | System time (ms) |
| RPM | 4 | Uint32 (0-4,095 rpm) |
| Motor Current (A/B/C) | 12 | 3× Float (A) |
| Bus Voltage | 4 | Float (VDC) |
| Thrust Estimate | 4 | Float (kN) |
| Temperature (Max) | 4 | Float (°C) |
| Fault Status | 4 | Bit field |
| Health Status | 2 | Enumeration |
| CRC | 2 | Message integrity |

### 5.2 Connector Pinout (M12 D-coded)

| Pin | Signal | Function |
|-----|--------|----------|
| 1 | TX+ | Transmit positive |
| 2 | RX+ | Receive positive |
| 3 | TX- | Transmit negative |
| 4 | RX- | Receive negative |
| Shell | Shield | Chassis ground |

---

## 6. Verification Requirements

### 6.1 Design Verification

| Test ID | Test Description | Acceptance Criteria | Method |
|---------|------------------|---------------------|--------|
| AFDX-T-001 | Physical layer compliance | Per IEEE 802.3 100BASE-TX | Bit error rate test |
| AFDX-T-002 | End-to-end latency | <10 ms for critical VLs | Network analyzer |
| AFDX-T-003 | Frame loss rate | <10⁻⁷ | Long-duration test |
| AFDX-T-004 | BAG compliance | Frames within BAG window | Protocol analyzer |
| AFDX-T-005 | Redundancy switching | <100 ms failover | Fault injection |
| AFDX-T-006 | Bandwidth utilization | <70% per network | Analysis, measurement |
| AFDX-T-007 | Message integrity | No CRC errors | Protocol analyzer |

### 6.2 Production Verification

| Inspection | Frequency | Method |
|------------|-----------|--------|
| Cable continuity | 100% | Network tester |
| Link establishment | 100% | Automated test |
| Frame transmission/reception | 100% | Loopback test |
| Bandwidth allocation verification | 10% (sampling) | Protocol analyzer |

---

## 7. Cross-References

### 7.1 Related ATA Chapters
- [ATA 42](../../../../ATA_42-INTEGRATED_MODULAR_AVIONICS/README.md) — Integrated Modular Avionics (AFDX switches)
- [ATA 27](../../../../F-FLIGHT_CONTROLS/ATA_27-FLIGHT_CONTROLS/README.md) — Flight Controls (data source/consumer)
- [ATA 45](../../../../ATA_45-CENTRAL_MAINTENANCE_SYSTEM/README.md) — Central Maintenance System

### 7.2 Parent Document
- [61-00-05_Interfaces](../README.md) — Interface specifications overview

### 7.3 Related Documents
- 61-00-05-03-01A — ARINC 429 Buses
- 61-00-05-02-02A — Control Signals

---

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

← [Previous: 61-00-05-03-01A_ARINC_429_Buses](61-00-05-03-01A_ARINC_429_Buses.md) · [Next: 61-00-05-03-03A_Discrete_Signals](61-00-05-03-03A_Discrete_Signals.md) →

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
