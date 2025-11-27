# 53-40-20-02 — Fault Catalog

| Field | Value |
|-------|-------|
| **Document ID** | 53-40-20-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | SOFTWARE / DIAGNOSTICS |

---

## 1. Purpose

This document provides the fault catalog for ANCHORS systems, defining all fault codes, descriptions, and recommended maintenance actions.

## 2. Fault Code Format

### 2.1 Code Structure

```
53-40-XX-YYY-Z
│  │  │  │   └── Severity (1=Warning, 2=Caution, 3=Fault, 4=Failure)
│  │  │  └────── Fault sequence (001-999)
│  │  └───────── Subsystem band (10, 20, 30, etc.)
│  └──────────── Software bucket
└─────────────── ATA chapter
```

## 3. Fault Catalog

### 3.1 Control Logic Faults (Band 10)

| Code | Name | Description | Severity | Action |
|------|------|-------------|----------|--------|
| 53-40-10-001-3 | MODE_TRANS_FAIL | Mode transition failure | Fault | Reset system |
| 53-40-10-002-2 | CO2_CTRL_DEGRADE | CO₂ controller degraded | Caution | Monitor |
| 53-40-10-003-4 | BAT_TMS_FAIL | Battery TMS failure | Failure | Isolate battery |
| 53-40-10-004-1 | H2O_LOW_FLOW | Water flow below minimum | Warning | Check filters |

### 3.2 Diagnostics Faults (Band 20)

| Code | Name | Description | Severity | Action |
|------|------|-------------|----------|--------|
| 53-40-20-001-2 | BITE_FAIL | BITE system failure | Caution | Ground service |
| 53-40-20-002-1 | SENSOR_MISMATCH | Sensor cross-check fail | Warning | Verify sensors |
| 53-40-20-003-3 | HEALTH_DEGRADE | System health degraded | Fault | Dispatch check |

### 3.3 Interface Faults (Band 30)

| Code | Name | Description | Severity | Action |
|------|------|-------------|----------|--------|
| 53-40-30-001-3 | AFDX_LOSS | AFDX communication loss | Fault | Check network |
| 53-40-30-002-2 | CAN_BUS_ERR | CAN bus error | Caution | Check wiring |
| 53-40-30-003-4 | COMM_TOTAL_LOSS | Total comm failure | Failure | Emergency proc |

### 3.4 Safety Faults (Band 50)

| Code | Name | Description | Severity | Action |
|------|------|-------------|----------|--------|
| 53-40-50-001-4 | BATT_OVERHEAT | Battery overheat | Failure | Isolate + cool |
| 53-40-50-002-3 | LIMIT_EXCEED | Safety limit exceeded | Fault | Investigate |
| 53-40-50-003-2 | FALLBACK_ACTIVE | Fallback mode active | Caution | Monitor |

### 3.5 NN Integration Faults (Band 95)

| Code | Name | Description | Severity | Action |
|------|------|-------------|----------|--------|
| 53-40-95-001-2 | NN_TIMEOUT | NN execution timeout | Caution | Using fallback |
| 53-40-95-002-3 | NN_ENV_VIOLATION | NN envelope violation | Fault | Using fallback |
| 53-40-95-003-1 | NN_LOW_CONF | NN low confidence | Warning | Monitor output |

## 4. Maintenance Actions

### 4.1 Action Codes

| Code | Description | Location |
|------|-------------|----------|
| A1 | Reset system | Flight deck |
| A2 | Monitor and log | Flight deck |
| A3 | Ground service required | Line maintenance |
| A4 | Component replacement | Base maintenance |
| A5 | Emergency procedure | Flight deck |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-40-20-02 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Author** | AMPEL360 Diagnostics Team |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*
