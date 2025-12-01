# ATA 56-90 CIR — Central Illustration Repository

## Overview

This folder contains **Central Illustration Repository (CIR)** assets for ATA Chapter 56 (Windows) subsystems. CIR assets include figures (SVG), tables (CSV), Bill of Materials (BOM), and schemas referenced by LRU and LRI documentation.

## Naming Convention

### Figures (FIG)

```text
56-90-XX_56-YY-FIG_NNN-[Description].svg
```

Where:
- `XX` = Subsystem code (21=Windshields, 22=SideWindows, etc.)
- `YY` = LRI sequence
- `NNN` = Figure sequence number

### Tables (TABLE)

```text
56-90-XX_56-YY-TABLE_NNN-[Description].csv
```

### Bill of Materials / Line Maintenance Parts (BOM_LMP)

```text
56-90-XX_56-YY-ZZ-BOM_LMP.csv
```

Where:
- `XX` = Subsystem code
- `YY-ZZ` = LRU identifier

## BOM_LMP Column Definitions

| Column | Description |
|--------|-------------|
| Line | Sequential line number |
| LRU_PN | Parent LRU Part Number |
| LRI_ID | Line Replaceable Item identifier |
| Part_Number | NATO PNR format part number |
| NSN | NATO Stock Number (placeholder format) |
| CAGE | Commercial and Government Entity code |
| Nomenclature | Part description |
| Qty | Quantity per assembly |
| UoM | Unit of Measure (EA, SET, KIT) |
| ICC | Interchangeability Code (1=Identical, 2=Interchangeable, 3=Not interchangeable) |
| LMP | Line Maintenance Part (Y/N) |
| MTTR_min | Mean Time To Replace in minutes |
| Criticality | Critical/Standard classification |
| Lead_Time_Days | Procurement lead time |
| Make_Buy | Manufacturing source |
| Spec_Std | Applicable specification/standard |
| Shelf_Life_Months | Storage shelf life (UNL=Unlimited) |
| Recyclability | End-of-life recyclability code and note |
| Notes | Additional information |

## Recyclability Codes

| Code | Description |
|------|-------------|
| R1 | Direct material recycling (metals, glass) |
| R2 | Separation required before recycling |
| R3 | Precious/specialty material recovery |
| R4 | Thermal recovery or controlled disposal |
| R5 | Hazardous material disposal required |

## Asset Index

### 56-21 Windshields

| CIR ID | Type | Description | Status |
|--------|------|-------------|--------|
| 56-90-21_56-21-FIG_001 | Figure | Windshield Assembly Overview | Placeholder |
| 56-90-21_56-21-TABLE_001 | Table | Windshield Specifications | Placeholder |
| 56-90-21_56-21-01-BOM_LMP | BOM | Forward Windshield Assembly BOM/LMP | Active |

### 56-22 Side Windows

| CIR ID | Type | Description | Status |
|--------|------|-------------|--------|
| 56-90-22_56-22-FIG_001 | Figure | Side Window Assembly | Placeholder |
| 56-90-22_56-22-01-BOM_LMP | BOM | Captain Side Window BOM/LMP | Active |

### 56-23 Cabin Windows

| CIR ID | Type | Description | Status |
|--------|------|-------------|--------|
| 56-90-23_56-23-FIG_001 | Figure | Cabin Window Assembly | Placeholder |
| 56-90-23_56-23-01-BOM_LMP | BOM | Standard Cabin Window BOM/LMP | Active |
| 56-90-23_56-23-02-BOM_LMP | BOM | Overwing Emergency Exit BOM/LMP | Active |

### 56-24 Observation Windows

| CIR ID | Type | Description | Status |
|--------|------|-------------|--------|
| 56-90-24_56-24-01-BOM_LMP | BOM | Panoramic Window BOM/LMP | Active |

### 56-25 Window Heating

| CIR ID | Type | Description | Status |
|--------|------|-------------|--------|
| 56-90-25_56-25-TABLE_001 | Table | Heating Load Profiles | Placeholder |
| 56-90-25_56-25-01-BOM_LMP | BOM | Heating Controller BOM/LMP | Active |

### 56-26 Rain Repellent

| CIR ID | Type | Description | Status |
|--------|------|-------------|--------|
| 56-90-26_56-26-FIG_001 | Figure | Rain Repellent Schematic | Placeholder |
| 56-90-26_56-26-01-BOM_LMP | BOM | Rain Repellent System BOM/LMP | Active |

### 56-27 Wiper Systems

| CIR ID | Type | Description | Status |
|--------|------|-------------|--------|
| 56-90-27_56-27-01-BOM_LMP | BOM | Wiper Drive Unit BOM/LMP | Active |

### 56-28 Smart Glass

| CIR ID | Type | Description | Status |
|--------|------|-------------|--------|
| 56-90-28_56-28-01-BOM_LMP | BOM | Smart Glass Control Unit BOM/LMP | Active |

## Legacy/Template Assets

| CIR ID | LRI | Type | Description | Status |
|--------|-----|------|-------------|--------|
| 56-90-20_56-02-FIG_001 | LRI_01 | Figure | ComponentA Assembly | Template |
| 56-90-20_56-02-TABLE_001 | LRI_01 | Table | ComponentA Specs | Template |
| 56-90-20_56-03-FIG_002 | LRI_02 | Figure | ComponentB Assembly | Template |
| 56-90-20_56-03-TABLE_002 | LRI_02 | Table | ComponentB Specs | Template |
| 56-90-20_56-04-FIG_003 | LRI_03 | Figure | ComponentC Assembly | Template |
| 56-90-20_56-04-TABLE_003 | LRI_03 | Table | ComponentC Specs | Template |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT**
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
