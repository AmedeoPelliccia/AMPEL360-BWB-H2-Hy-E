# 53-80-50-01 — ATA 24 Electrical Interface

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-50-01 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / INTERFACE |

---

## 1. Purpose

This document defines the interface between ANCHORS Energy (53-80) and the Aircraft Electrical Power System (ATA 24).

## 2. Interface Overview

| Interface | Type | Direction | Content |
|-----------|------|-----------|---------|
| ICD-24-001 | Power | Bidirectional | HVDC 750 VDC |
| ICD-24-002 | Signal | Bidirectional | AFDX control/status |
| ICD-24-003 | Discrete | Output | Status discretes |

## 3. Power Interface

| Parameter | Value | Tolerance |
|-----------|-------|-----------|
| Voltage | 750 VDC | ±100 VDC |
| Current (max) | 267 A | — |
| Power allocation | 200 kW | — |
| Emergency backup | 50 kW | — |

## 4. Signal Interface

### 4.1 To ATA 24

| Signal | Type | Range |
|--------|------|-------|
| ANCHORS_PWR_REQ | Power | 0-250 kW |
| ANCHORS_SOC | Percentage | 0-100% |
| ANCHORS_STATUS | Bitmap | — |
| EMERG_PWR_AVAIL | Power | 0-50 kW |

### 4.2 From ATA 24

| Signal | Type | Range |
|--------|------|-------|
| HVDC_BUS_V | Voltage | 0-1000 VDC |
| HVDC_AVAIL | Power | 0-500 kW |
| LOAD_SHED_CMD | Level | 0-5 |

## 5. Operating Procedures

| Condition | 53-80 Action | ATA 24 Response |
|-----------|--------------|-----------------|
| Normal | Request power | Provide allocation |
| Low SOC | Request increased | Prioritize if available |
| Emergency | Provide backup | Accept backup power |

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-50-01 |
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
