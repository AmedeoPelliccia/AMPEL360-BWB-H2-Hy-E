# BOM/LMP — LRI_01 ComponentA

## Document Information

- **Document ID**: 61-20-XX-LRI_01_BOM_LMP
- **LRI ID**: LRI_01
- **Component**: ComponentA
- **Part Number**: PN-61-20-XX-01A
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Introduction

This document contains the **Bill of Materials (BOM)** and **Line Maintenance Parts (LMP)** for LRI_01 ComponentA.

### 1.1 Purpose

- Provide complete parts hierarchy for manufacturing and procurement
- Identify line-replaceable components for maintenance planning
- Support spares provisioning and logistics

### 1.2 Applicability

| Aircraft | Effectivity | Configuration |
|----------|-------------|---------------|
| AMPEL360 | All | Standard |

---

## 2. Bill of Materials (BOM)

### 2.1 BOM Structure

```text
PN-61-20-XX-01A (ComponentA)
├── PN-61-20-XX-01A-100 (Housing Assembly)
│   ├── PN-61-20-XX-01A-101 (Main Housing)
│   ├── PN-61-20-XX-01A-102 (Cover Plate)
│   └── PN-61-20-XX-01A-103 (Gasket Set)
├── PN-61-20-XX-01A-200 (Electronics Module)
│   ├── PN-61-20-XX-01A-201 (PCB Assembly)
│   ├── PN-61-20-XX-01A-202 (Connector Assembly)
│   └── PN-61-20-XX-01A-203 (Wiring Harness)
└── PN-61-20-XX-01A-300 (Mounting Kit)
    ├── PN-61-20-XX-01A-301 (Mounting Bracket)
    ├── PN-61-20-XX-01A-302 (Fastener Set)
    └── PN-61-20-XX-01A-303 (Vibration Isolators)
```

### 2.2 BOM Table

| Level | Part Number | Nomenclature | Qty | Unit | Make/Buy | Source |
|-------|-------------|--------------|-----|------|----------|--------|
| 0 | PN-61-20-XX-01A | ComponentA | 1 | EA | Make | — |
| 1 | PN-61-20-XX-01A-100 | Housing Assembly | 1 | EA | Make | — |
| 2 | PN-61-20-XX-01A-101 | Main Housing | 1 | EA | Make | — |
| 2 | PN-61-20-XX-01A-102 | Cover Plate | 1 | EA | Make | — |
| 2 | PN-61-20-XX-01A-103 | Gasket Set | 1 | SET | Buy | [Vendor TBD] |
| 1 | PN-61-20-XX-01A-200 | Electronics Module | 1 | EA | Make | — |
| 2 | PN-61-20-XX-01A-201 | PCB Assembly | 1 | EA | Make | — |
| 2 | PN-61-20-XX-01A-202 | Connector Assembly | 2 | EA | Buy | [Vendor TBD] |
| 2 | PN-61-20-XX-01A-203 | Wiring Harness | 1 | EA | Make | — |
| 1 | PN-61-20-XX-01A-300 | Mounting Kit | 1 | KIT | Make | — |
| 2 | PN-61-20-XX-01A-301 | Mounting Bracket | 2 | EA | Make | — |
| 2 | PN-61-20-XX-01A-302 | Fastener Set | 1 | SET | Buy | [Vendor TBD] |
| 2 | PN-61-20-XX-01A-303 | Vibration Isolators | 4 | EA | Buy | [Vendor TBD] |

---

## 3. Line Maintenance Parts (LMP)

### 3.1 LMP Summary

Line Maintenance Parts are components that can be replaced at the line station level without requiring shop-level repair.

| Category | Description |
|----------|-------------|
| **Critical** | Parts whose failure causes system inoperability |
| **High** | Parts whose failure degrades system performance |
| **Standard** | Parts consumed during routine maintenance |

### 3.2 LMP List

| Part Number | Nomenclature | Qty/LRU | Category | MTTR (min) | Spares Ratio |
|-------------|--------------|---------|----------|------------|--------------|
| PN-61-20-XX-01A-103 | Gasket Set | 1 | Standard | 30 | 2:1 |
| PN-61-20-XX-01A-202 | Connector Assembly | 2 | High | 45 | 1:1 |
| PN-61-20-XX-01A-302 | Fastener Set | 1 | Standard | 15 | 3:1 |
| PN-61-20-XX-01A-303 | Vibration Isolators | 4 | Standard | 20 | 2:1 |

### 3.3 Critical Spares

Components requiring immediate availability for dispatch reliability:

| Part Number | Nomenclature | Min Stock | Lead Time | Location |
|-------------|--------------|-----------|-----------|----------|
| PN-61-20-XX-01A | ComponentA (Complete) | 1 | [TBD] days | Line Station |
| PN-61-20-XX-01A-200 | Electronics Module | 1 | [TBD] days | Hub |

---

## 4. Maintenance Information

### 4.1 Replacement Procedures

| Part | AMM Reference | Est. Time | Access |
|------|---------------|-----------|--------|
| ComponentA (Complete) | AMM 61-20-XX-400 | 45 min | Panel [TBD] |
| Gasket Set | AMM 61-20-XX-401 | 30 min | Panel [TBD] |
| Connector Assembly | AMM 61-20-XX-402 | 45 min | Panel [TBD] |

### 4.2 Special Tools

| Tool P/N | Description | Requirement |
|----------|-------------|-------------|
| [TBD] | [Tool description] | Optional |

### 4.3 Consumables

| Part Number | Description | Specification | Qty/Task |
|-------------|-------------|---------------|----------|
| [TBD] | Sealant | [Spec] | As required |
| [TBD] | Lubricant | [Spec] | As required |
| [TBD] | Lockwire | [Spec] | As required |

---

## 5. Vendor Information

### 5.1 Approved Vendors

| Part Category | Vendor | Cage Code | Contact |
|---------------|--------|-----------|---------|
| Gaskets | [TBD] | [TBD] | [TBD] |
| Connectors | [TBD] | [TBD] | [TBD] |
| Fasteners | [TBD] | [TBD] | [TBD] |
| Isolators | [TBD] | [TBD] | [TBD] |

### 5.2 Lead Times

| Part Category | Standard | Expedited | AOG |
|---------------|----------|-----------|-----|
| Manufactured Parts | [X] weeks | [X] weeks | [X] days |
| Buy Parts | [X] weeks | [X] weeks | [X] days |

---

## 6. Interchangeability

### 6.1 Interchangeable Parts

| Original P/N | Alternate P/N | Notes |
|--------------|---------------|-------|
| [TBD] | [TBD] | [Conditions] |

### 6.2 Non-Interchangeable Parts

Parts requiring specific configuration or serial number tracking:

| Part Number | Reason | Tracking |
|-------------|--------|----------|
| [TBD] | [Reason] | Serial |

---

## 7. Traceability

### 7.1 Certification Requirements

| Part | Cert. Requirement | Evidence |
|------|-------------------|----------|
| Electronics Module | [DO-254](https://www.rtca.org/) | COC |
| Structural Parts | [CS-E](https://www.easa.europa.eu/) | COC/CofA |

### 7.2 Related Documents

- [61-20-XX Design](./61-20-XX_Design.md)
- [CIR Links](./CIR_LINKS.md)
- [LRU Overview](../../LRU_61-20-XX_Overview.md)
- [IPC Section 61-20-XX](../../../../61-90_Tables_Schemas_Diagrams/README.md)

---

## 8. Revision History

| Rev | Date | Description | Author |
|-----|------|-------------|--------|
| 1.0 | 2025-12-01 | Initial release | AMPEL360 Documentation WG |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
