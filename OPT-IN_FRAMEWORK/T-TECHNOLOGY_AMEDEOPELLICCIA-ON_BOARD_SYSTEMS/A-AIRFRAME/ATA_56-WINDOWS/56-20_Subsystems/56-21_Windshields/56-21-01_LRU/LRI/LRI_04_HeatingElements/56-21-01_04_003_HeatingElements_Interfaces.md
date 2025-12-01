# 56-21-01_04_003 — Heating Elements Interfaces

## Document Information

- **Document ID**: 56-21-01_04_003
- **Title**: Windshield Heating Elements Interfaces
- **ATA Chapter**: 56 – Windows
- **LRI Code**: 56-21-01_04 (LRI_04)
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Purpose

This document defines the interfaces for the Windshield Heating Elements.

---

## 2. Electrical Interfaces

| Interface ID | Connected Component | Description |
|--------------|---------------------|-------------|
| IF-56-21-04-E01 | Window Heating Controller (56-25) | 115VAC power input |
| IF-56-21-04-E02 | Left Panel (LRI_01) | Embedded heating connection |
| IF-56-21-04-E03 | Right Panel (LRI_02) | Embedded heating connection |
| IF-56-21-04-E04 | Center Panel (LRI_03) | Embedded heating connection |

---

## 3. Sensor Interfaces

| Interface ID | Connected Component | Description |
|--------------|---------------------|-------------|
| IF-56-21-04-S01 | Temperature Sensors | RTD feedback to controller |
| IF-56-21-04-S02 | Current Monitors | Power consumption monitoring |
| IF-56-21-04-S03 | EICAS | Status indication via ATA 31 |

---

## 4. Control Interfaces

| Interface ID | Connected Component | Description |
|--------------|---------------------|-------------|
| IF-56-21-04-C01 | Cockpit Control Panel | Manual ON/OFF and mode selection |
| IF-56-21-04-C02 | Ice/Rain Protection System (ATA 30) | Automatic activation signals |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
