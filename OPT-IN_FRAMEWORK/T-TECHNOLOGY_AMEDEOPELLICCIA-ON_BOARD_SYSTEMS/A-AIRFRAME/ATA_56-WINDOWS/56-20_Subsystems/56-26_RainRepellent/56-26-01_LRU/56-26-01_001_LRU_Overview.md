# LRU_56-26-01 — Rain Repellent System Overview

## Document Information

- **Document ID**: LRU_56-26-01_001_Overview
- **Title**: Rain Repellent System Line Replaceable Unit Overview
- **ATA Chapter**: 56 – Windows
- **Subsystem Code**: 56-26-01
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Introduction

### 1.1 Purpose

This document provides a comprehensive overview of the **Rain Repellent System** Line Replaceable Unit (LRU), providing improved visibility during rain conditions.

### 1.2 Scope

This LRU encompasses:

- **Functional Description**: Hydrophobic coating application
- **Component Inventory**: Fluid delivery system components
- **Interface Summary**: Connections to windshields and controls
- **Maintenance Philosophy**: Fluid replenishment and component servicing

---

## 2. LRU Definition

### 2.1 Identification

| Attribute | Value |
|-----------|-------|
| **LRU Part Number** | PN-56-26-01-001 |
| **Nomenclature** | Rain Repellent System |
| **ATA Chapter** | 56 |
| **Subsystem** | 26 (Rain Repellent) |
| **Sequence** | 01 |

### 2.2 Physical Characteristics

| Parameter | Value |
|-----------|-------|
| **Reservoir Capacity** | 1.0 liters |
| **Operating Pressure** | 25-35 psi |
| **Pump Type** | 28VDC electric |

---

## 3. Component Breakdown — LRI Summary

| LRI ID | Component Name | Qty | Description |
|--------|----------------|-----|-------------|
| LRI_01 | Fluid Reservoir | 1 | Rain repellent fluid storage |
| LRI_02 | Pump Assembly | 1 | Pressurized fluid delivery |
| LRI_03 | Spray Nozzles | 2 | Windshield application nozzles |
| LRI_04 | Control Valve | 1 | Fluid flow control |
| LRI_05 | Fluid Level Sensor | 1 | Quantity indication |

---

## 4. Interface Summary

| Interface ID | Connected System | ATA | Type | Description |
|--------------|------------------|-----|------|-------------|
| IF-56-26-001 | Windshields | 56-21 | Mechanical | Nozzle mounting |
| IF-56-26-002 | Electrical Power | 24 | Electrical | 28VDC supply |
| IF-56-26-003 | EICAS | 31 | Data | Fluid level |
| IF-56-26-004 | Cockpit Panel | - | Electrical | Activation switch |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
