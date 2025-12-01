# BOM/LMP — LRI_03 ComponentC

## Document Information

- **Document ID**: 61-20-XX-LRI_03_BOM_LMP
- **LRI ID**: LRI_03
- **Component**: ComponentC
- **Part Number**: PN-61-20-XX-03C
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Introduction

This document contains the **Bill of Materials (BOM)** and **Line Maintenance Parts (LMP)** for LRI_03 ComponentC.

---

## 2. Bill of Materials (BOM)

### 2.1 BOM Structure

```text
PN-61-20-XX-03C (ComponentC)
├── PN-61-20-XX-03C-100 (Body Assembly)
│   ├── PN-61-20-XX-03C-101 (Main Body)
│   ├── PN-61-20-XX-03C-102 (End Cap)
│   └── PN-61-20-XX-03C-103 (O-Ring Kit)
├── PN-61-20-XX-03C-200 (Sensor Module)
│   ├── PN-61-20-XX-03C-201 (Sensor Element)
│   └── PN-61-20-XX-03C-202 (Signal Conditioner)
└── PN-61-20-XX-03C-300 (Install Kit)
    ├── PN-61-20-XX-03C-301 (Mounting Plate)
    └── PN-61-20-XX-03C-302 (Hardware Set)
```

### 2.2 BOM Table

| Level | Part Number | Nomenclature | Qty | Unit | Make/Buy |
|-------|-------------|--------------|-----|------|----------|
| 0 | PN-61-20-XX-03C | ComponentC | 1 | EA | Make |
| 1 | PN-61-20-XX-03C-100 | Body Assembly | 1 | EA | Make |
| 2 | PN-61-20-XX-03C-101 | Main Body | 1 | EA | Make |
| 2 | PN-61-20-XX-03C-102 | End Cap | 1 | EA | Make |
| 2 | PN-61-20-XX-03C-103 | O-Ring Kit | 1 | SET | Buy |
| 1 | PN-61-20-XX-03C-200 | Sensor Module | 1 | EA | Make |
| 2 | PN-61-20-XX-03C-201 | Sensor Element | 1 | EA | Buy |
| 2 | PN-61-20-XX-03C-202 | Signal Conditioner | 1 | EA | Make |
| 1 | PN-61-20-XX-03C-300 | Install Kit | 1 | KIT | Make |
| 2 | PN-61-20-XX-03C-301 | Mounting Plate | 1 | EA | Make |
| 2 | PN-61-20-XX-03C-302 | Hardware Set | 1 | SET | Buy |

---

## 3. Line Maintenance Parts (LMP)

### 3.1 LMP List

| Part Number | Nomenclature | Qty/LRU | Category | MTTR (min) |
|-------------|--------------|---------|----------|------------|
| PN-61-20-XX-03C-103 | O-Ring Kit | 1 | Standard | 15 |
| PN-61-20-XX-03C-201 | Sensor Element | 1 | Critical | 40 |
| PN-61-20-XX-03C-302 | Hardware Set | 1 | Standard | 10 |

---

## 4. Related Documents

- [61-20-XX Design](./61-20-XX_Design.md)
- [CIR Links](./CIR_LINKS.md)
- [LRU Overview](../../LRU_61-20-XX_Overview.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-01_.

---
