# 53-80-60-01 — Electrical Protection Coordination

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-60-01 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / PROTECTION |

---

## 1. Purpose

This document defines the electrical protection coordination strategy for the ANCHORS HVDC distribution system.

## 2. Protection Hierarchy

| Level | Device | Location | Trip Time |
|-------|--------|----------|-----------|
| 1 | Load SSCB | Load input | < 1 ms |
| 2 | Channel SSCB | SPDA output | < 10 ms |
| 3 | GFI | Channel | < 50 ms |
| 4 | Bus MCCB | Bus section | < 100 ms |
| 5 | Source contactor | Source output | < 200 ms |

## 3. Selectivity Coordination

### 3.1 Time Grading

| Level | Nominal Time | Maximum Time | Margin |
|-------|--------------|--------------|--------|
| 1 → 2 | 1 ms → 10 ms | — | 10:1 |
| 2 → 3 | 10 ms → 50 ms | — | 5:1 |
| 3 → 4 | 50 ms → 100 ms | — | 2:1 |
| 4 → 5 | 100 ms → 200 ms | — | 2:1 |

### 3.2 Current Grading

| Protection | Pickup | Setting |
|------------|--------|---------|
| Load SSCB | 120% rated | Per load |
| Channel SSCB | 110% channel | Sum of loads |
| Bus MCCB | 100% bus | Full capacity |

## 4. Fault Types and Response

| Fault | Detection | Primary | Backup |
|-------|-----------|---------|--------|
| Overload | Current | Load SSCB | Channel SSCB |
| Short circuit | dI/dt | Load SSCB | Channel SSCB |
| Ground fault | GFI | GFI trip | Bus MCCB |
| Arc fault | Arc signature | SSCB | MCCB |

## 5. Protection Devices

### 5.1 SSCB Specifications

| Parameter | Value |
|-----------|-------|
| Voltage rating | 1000 VDC |
| Current ratings | 20-100 A |
| Trip time | < 1 ms |
| Reset | Remote electronic |
| Status | Digital output |

### 5.2 MCCB Specifications

| Parameter | Value |
|-----------|-------|
| Voltage rating | 1000 VDC |
| Current rating | 300 A |
| Interrupting capacity | 50 kA |
| Reset | Manual |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-60-01 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*
