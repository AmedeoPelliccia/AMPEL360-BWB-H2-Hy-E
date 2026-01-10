# DML Directory

## Purpose

Contains **Data Module Lists** - lists referencing data modules.

DMLs act as the **contract layer** between:
* **Back (SSOT / structured DMs, ICNs, BREX)**
* **Front (AMM PMs, IETP builds, actor-to-actor delivery)**

They:
* Define *what exists*
* Control *what is published*
* Enable *variant/applicability filtering*
* Are **mandatory for certification-grade traceability**

## Available DMLs

This directory contains the following S1000D-compliant Data Module Lists for ATA 31-00-00:

### 1. Master DML
**File:** `DML-AMPEL360AT-31-00-00001_EN-US_001-00.XML`  
**Purpose:** Single source of truth for all AMM DMs under 31-00-00  
**Contains:** All 040A / 52xx / 72xx / 73xx / 94xx DMs

### 2. Descriptive DML
**File:** `DML-AMPEL360AT-31-00-040A_EN-US_001-00.XML`  
**Purpose:** Conceptual understanding & training views  
**Contains:** General system description, architecture, signal flow, HMI concepts

### 3. Maintenance Task DML
**File:** `DML-AMPEL360AT-31-00-520X_EN-US_001-00.XML`  
**Purpose:** Operational maintenance filtering  
**Contains:** Removal/installation, operational tests, servicing actions (520A/520B/520C, 720A)

### 4. Fault Isolation DML
**File:** `DML-AMPEL360AT-31-00-730A_EN-US_001-00.XML`  
**Purpose:** Troubleshooting & diagnostics  
**Contains:** Fault isolation procedures, built-in test references, decision logic

### 5. Software & Configuration DML
**File:** `DML-AMPEL360AT-31-00-940A_EN-US_001-00.XML`  
**Purpose:** Controlled exposure of software actions  
**Contains:** Software loading, configuration data handling, post-load verification  
**Note:** Procedure-only, no binary ownership or parameter definition

### 6. Illustration Cross-Reference DML
**File:** `DML-AMPEL360AT-31-00-ICN_EN-US_001-00.XML`  
**Purpose:** IETP optimization and validation  
**Contains:** All DMs that reference ICNs (Illustration Control Numbers)  
**Enables:** Broken graphic detection, graphic reuse analysis

## Naming Convention

Data Module List format: `DML-AMPEL360AT-31-00-NNNN_EN-US_001-00.XML`

Where:
* `AMPEL360AT` = Model ID
* `31` = ATA Chapter
* `00` = General sub-chapter for ATA 31-00-00
* `NNNN` = Either a sequence number (`00001`–`00006`) or an info code (`040A`, `520X`, `730A`, `940A`, `ICN`)
* `EN-US` = Language code (English-US)
* `001-00` = Issue number and in-work status

## Compliance Notes

* **Standard:** S1000D Issue 5.0
* **Numbering:** ATA iSpec 2200
* Language split via DML (not PM)
* Applicability handled via:
  * `<applicRef>` in DM
  * Cross-DML filtering in PM/IETP

## Relationship to PM and IETP

* **PM** = structure / navigation
* **DML** = controlled content set
* **IETP** = rendered, filtered, interactive view

Key insight:
* PDF / HTML = **IETP outputs**
* The "IETP image" is effectively the **runtime front-liner**
* DMLs are the **gatekeepers** between back and front

## Document Control

- **Directory**: DML
- **Subject**: 31-00-00-general
- **Publication**: AMM
- **Standard**: S1000D Issue 5.0
- **Status**: Active
- **Last Update**: 2026-01-10
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
