# LRU_56-25-01 — Windshield Heating Controller Overview

## Document Information

- **Document ID**: LRU_56-25-01_001_Overview
- **Title**: Windshield Heating Controller Line Replaceable Unit Overview
- **ATA Chapter**: 56 – Windows
- **Subsystem Code**: 56-25-01
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Introduction

### 1.1 Purpose

This document provides a comprehensive overview of the **Windshield Heating Controller** Line Replaceable Unit (LRU), the central controller for all cockpit window heating functions.

### 1.2 Scope

This LRU encompasses:

- **Functional Description**: Anti-ice and anti-fog heating control
- **Component Inventory**: Power control and monitoring equipment
- **Interface Summary**: Connections to heating elements and avionics
- **Safety Features**: Overheat protection and fault monitoring

---

## 2. LRU Definition

### 2.1 Identification

| Attribute | Value |
|-----------|-------|
| **LRU Part Number** | PN-56-25-01-001 |
| **Nomenclature** | Windshield Heating Controller |
| **ATA Chapter** | 56 |
| **Subsystem** | 25 (Window Heating) |
| **Sequence** | 01 |
| **TSO** | TSO-C16a |

### 2.2 Physical Characteristics

| Parameter | Value |
|-----------|-------|
| **Weight (dry)** | [TBD] kg |
| **Dimensions** | [TBD] × [TBD] × [TBD] mm |
| **Environmental Rating** | DO-160G |
| **Power Input** | 115VAC, 400Hz |
| **Power Output** | Up to 5 kW per channel |

---

## 3. Component Breakdown — LRI Summary

| LRI ID | Component Name | Qty | Description |
|--------|----------------|-----|-------------|
| LRI_01 | Power Controller | 1 | Main power regulation unit |
| LRI_02 | Temperature Sensors | 6 | Panel temperature monitoring (2 per panel) |
| LRI_03 | Current Monitoring | 1 | Power consumption tracking |
| LRI_04 | Overheat Protection | 1 | Thermal runaway prevention circuit |
| LRI_05 | Diagnostic Interface | 1 | BITE and ARINC 429 interface |

---

## 4. Operating Modes

| Mode | Description | Power Level |
|------|-------------|-------------|
| OFF | Heating disabled | 0% |
| LOW | Anti-fog / light icing | 25-50% |
| NORMAL | Standard operation | 50-75% |
| HIGH | Heavy icing conditions | 75-100% |
| AUTO | Temperature-controlled | Variable |

---

## 5. Interface Summary

| Interface ID | Connected System | ATA | Type | Description |
|--------------|------------------|-----|------|-------------|
| IF-56-25-001 | Windshields | 56-21 | Electrical | Heating power output |
| IF-56-25-002 | Side Windows | 56-22 | Electrical | Heating power output |
| IF-56-25-003 | Electrical Power | 24 | Electrical | 115VAC input |
| IF-56-25-004 | Ice Protection | 30 | Data | System coordination |
| IF-56-25-005 | EICAS | 31 | Data | ARINC 429 status |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
