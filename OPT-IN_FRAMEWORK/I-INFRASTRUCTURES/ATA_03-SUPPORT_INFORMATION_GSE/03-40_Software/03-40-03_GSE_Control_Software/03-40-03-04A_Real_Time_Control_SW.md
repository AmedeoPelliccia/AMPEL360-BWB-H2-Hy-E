# 03-40-03-04A - Real-Time Control Software

**Document ID:** 03-40-03-04A  
**Title:** Real-Time Control Software for GSE  
**ATA Chapter:** 03 — Support Information/GSE  
**Version:** A  
**Status:** DRAFT

---

## 1. Purpose

Defines requirements for real-time control software in GSE systems requiring deterministic response times.

---

## 2. Scope

Covers real-time operating systems (RTOS), control algorithms, and timing requirements for safety-critical GSE control.

---

## 3. Applicable Documents

| Document ID | Title | Reference |
|-------------|-------|-----------|
| [IEC 61508](https://www.iec.ch/functional-safety) | Functional Safety | RTOS certification |
| [POSIX.1](https://pubs.opengroup.org/onlinepubs/9699919799/) | Real-Time Extensions | RTOS API |
| [DO-178C](https://www.rtca.org/) | Software Considerations (reference) | Airborne (adapted) |

---

## 4. Software Description

### 4.1 RTOS Platforms

| RTOS | Certification | Usage | Typical Hardware |
|------|--------------|-------|------------------|
| VxWorks | DO-178B/C, IEC 61508 | Safety-critical control | PowerPC, ARM |
| QNX Neutrino | IEC 61508 | High-reliability | x86, ARM |
| Linux RT (PREEMPT_RT) | Not certified (non-safety) | Non-critical apps | x86, ARM |
| FreeRTOS | Optional certification | Low-cost controllers | ARM Cortex-M |

### 4.2 Timing Requirements

| Control Loop | Cycle Time | Jitter | Priority |
|--------------|------------|--------|----------|
| Safety Shutdown | <10 ms | <1 ms | Highest |
| Valve Control | 100 ms | <10 ms | High |
| PID Control | 100-500 ms | <50 ms | Medium |
| Data Logging | 1 sec | <100 ms | Low |

### 4.3 Control Algorithms

**PID Control**: Temperature, pressure, flow
- Tuning methods: Ziegler-Nichols, Cohen-Coon
- Anti-windup mechanisms
- Bumpless transfer

**State Machines**: Sequential control
- Clearly defined states and transitions
- Timeout handling
- Error recovery

**Safety Logic**: Emergency response
- Fail-safe design
- Redundant sensing
- Independent verification

### 4.4 Interfaces

- Real-time I/O hardware
- Inter-process communication (IPC)
- Shared memory (for high-speed data)
- Network time protocol (NTP) for synchronization

---

## 5. Safety and Security Requirements

| Requirement ID | Requirement | Standard |
|----------------|-------------|----------|
| RT-SAF-001 | Safety functions shall meet deterministic timing | IEC 61508 |
| RT-SAF-002 | Watchdog timer shall detect CPU failures | IEC 61508 |
| RT-SEC-001 | RTOS shall have memory protection | POSIX |
| RT-QA-001 | Worst-case execution time (WCET) shall be analyzed | DO-178C practice |

---

## 6. Cross-References

- 03-40-03-01A — PLC Programming
- 03-40-06-01A — Safety Critical SW

---

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---
