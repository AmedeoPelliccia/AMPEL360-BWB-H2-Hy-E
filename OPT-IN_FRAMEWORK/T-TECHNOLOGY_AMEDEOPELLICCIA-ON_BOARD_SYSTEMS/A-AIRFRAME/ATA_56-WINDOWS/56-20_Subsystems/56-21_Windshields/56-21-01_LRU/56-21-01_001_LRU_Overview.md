# LRU_56-21-01 — Forward Windshield Assembly Overview

## Document Information

- **Document ID**: LRU_56-21-01_001_Overview
- **Title**: Forward Windshield Assembly Line Replaceable Unit Overview
- **ATA Chapter**: 56 – Windows
- **Subsystem Code**: 56-21-01
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Introduction

### 1.1 Purpose

This document provides a comprehensive overview of the **Forward Windshield Assembly** Line Replaceable Unit (LRU) as part of ATA Chapter 56 – Windows. It defines the functional scope, component breakdown, interfaces, and maintenance philosophy for the primary cockpit windshield system of the AMPEL360 BWB aircraft.

### 1.2 Scope

This LRU encompasses:

- **Functional Description**: Primary forward vision system for flight crew
- **Component Inventory**: Summary of Line Replaceable Items (LRIs) contained within the LRU
- **Interface Summary**: Key interfaces with other ATA systems
- **Maintenance Philosophy**: Approach to line maintenance, shop repair, and overhaul

---

## 2. LRU Definition

### 2.1 Identification

| Attribute | Value |
|-----------|-------|
| **LRU Part Number** | PN-56-21-01-001 |
| **Nomenclature** | Forward Windshield Assembly |
| **ATA Chapter** | 56 |
| **Subsystem** | 21 (Windshields) |
| **Sequence** | 01 |
| **Manufacturer** | [TBD] |
| **Cage Code** | [TBD] |

### 2.2 Physical Characteristics

| Parameter | Value |
|-----------|-------|
| **Weight (dry)** | [TBD] kg |
| **Dimensions (L×W×H)** | [TBD] × [TBD] × [TBD] mm |
| **Environmental Rating** | DO-160G, Categories A2/B2/C3/D2/F3/H3 |
| **Operating Temp. Range** | -55°C to +70°C |
| **Bird Strike Rating** | FAR 25.775, 1.8 kg at Vc |

### 2.3 BWB-Specific Features

The AMPEL360 BWB configuration introduces unique requirements:

- **Center Panel**: Additional center windshield panel for wider cockpit geometry
- **Curved Optics**: Optimized for reduced distortion across blended body contours
- **Enhanced Structural Integration**: Direct mounting to BWB integrated fuselage-wing structure

---

## 3. Component Breakdown — LRI Summary

| LRI ID | Component Name | Qty | Description | Location |
|--------|----------------|-----|-------------|----------|
| LRI_01 | Left Windshield Panel | 1 | Captain-side forward view panel | Left cockpit frame |
| LRI_02 | Right Windshield Panel | 1 | First Officer-side forward view panel | Right cockpit frame |
| LRI_03 | Center Windshield Panel | 1 | BWB-specific center view panel | Center cockpit frame |
| LRI_04 | Heating Elements | 3 | Integrated anti-ice/anti-fog heating film | Embedded in panels |
| LRI_05 | Frame Retention System | 1 | Structural attachment, seals, and fasteners | Perimeter of all panels |

**Detailed LRI Documentation**:

- [LRI_01_LeftWindshieldPanel Design](./LRI/LRI_01_LeftWindshieldPanel/56-21-01_01_001_LeftPanel_Design.md)
- [LRI_02_RightWindshieldPanel Design](./LRI/LRI_02_RightWindshieldPanel/56-21-01_02_001_RightPanel_Design.md)
- [LRI_03_CenterWindshieldPanel Design](./LRI/LRI_03_CenterWindshieldPanel/56-21-01_03_001_CenterPanel_Design.md)
- [LRI_04_HeatingElements Design](./LRI/LRI_04_HeatingElements/56-21-01_04_001_HeatingElements_Design.md)
- [LRI_05_FrameRetentionSystem Design](./LRI/LRI_05_FrameRetentionSystem/56-21-01_05_001_FrameRetention_Design.md)

---

## 4. Interface Summary

| Interface ID | Connected System | ATA | Type | Description |
|--------------|------------------|-----|------|-------------|
| IF-56-21-001 | Window Heating Controller | 56-25 | Electrical | Heating power and temperature control |
| IF-56-21-002 | Electrical Power Distribution | 24 | Electrical | 115VAC/28VDC power supply |
| IF-56-21-003 | Rain Repellent System | 56-26 | Fluid/Mechanical | Spray nozzle mounting |
| IF-56-21-004 | Wiper Systems | 56-27 | Mechanical | Wiper arm interface |
| IF-56-21-005 | Flight Deck Structure | 53 | Structural | Frame mounting points |
| IF-56-21-006 | Avionics (EICAS) | 31 | Data | Heating system status |
| IF-56-21-007 | Ice/Rain Protection | 30 | Control | Anti-ice control signals |

---

## 5. Maintenance Philosophy

### 5.1 Line Maintenance Parts (LMP)

| Part Number | Description | Qty/LRU | Criticality | Lead Time |
|-------------|-------------|---------|-------------|-----------|
| PN-56-21-01-S01 | Windshield Seal Kit | 1 | Standard | 5 days |
| PN-56-21-01-S02 | Heating Element Connector | 2 | Critical | 3 days |
| PN-56-21-01-S03 | Frame Fastener Set | 1 | Standard | 2 days |

### 5.2 Removal/Installation

- **Typical Removal Time**: 4.0 hours (single panel)
- **Typical Installation Time**: 5.0 hours (single panel, including leak test)
- **Special Tools Required**: Windshield handling fixture, torque wrench set
- **Personnel Required**: 2 certified technicians minimum

### 5.3 Overhaul Interval

| Component | Overhaul Interval | Life Limit |
|-----------|-------------------|------------|
| Glass Panels | On-condition | None |
| Heating Elements | On-condition | 40,000 flight hours |
| Seals | 5,000 flight hours | 10,000 flight hours |

**Full BOM/LMP details**: See individual LRI folders.

---

## 6. Configuration Item References (CIR)

**Location**: `../../../56-90_Tables_Schemas_Diagrams/ATA_56-90_CIR/`

| CIR ID | Type | Description | File |
|--------|------|-------------|------|
| 56-90-21_56-21-FIG_001 | Figure (SVG) | Windshield Assembly Overview | [Link](../../../56-90_Tables_Schemas_Diagrams/ATA_56-90_CIR/56-90-21_56-21-FIG_001-WindshieldAssembly.svg) |
| 56-90-21_56-21-TABLE_001 | Table (CSV) | Windshield Specifications | [Link](../../../56-90_Tables_Schemas_Diagrams/ATA_56-90_CIR/56-90-21_56-21-TABLE_001-WindshieldSpecs.csv) |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
