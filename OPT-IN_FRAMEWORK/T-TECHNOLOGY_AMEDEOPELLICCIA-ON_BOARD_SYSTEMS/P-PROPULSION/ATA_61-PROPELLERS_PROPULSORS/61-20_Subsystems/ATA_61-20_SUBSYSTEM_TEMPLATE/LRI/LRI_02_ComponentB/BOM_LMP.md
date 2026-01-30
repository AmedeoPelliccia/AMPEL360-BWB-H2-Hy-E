# BOM/LMP — LRI_02 ComponentB

## Document Information

- **Document ID**: 61-20-XX-LRI_02_BOM_LMP
- **LRI ID**: LRI_02
- **Component**: ComponentB
- **Part Number**: PN-61-20-XX-02B
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-12-01

---

## 1. Introduction

This document contains the **Bill of Materials (BOM)** and **Line Maintenance Parts (LMP)** for LRI_02 ComponentB.

---

## 2. Bill of Materials (BOM)

### 2.1 BOM Structure

```text
PN-61-20-XX-02B (ComponentB)
├── PN-61-20-XX-02B-100 (Main Assembly)
│   ├── PN-61-20-XX-02B-101 (Frame)
│   ├── PN-61-20-XX-02B-102 (Cover)
│   └── PN-61-20-XX-02B-103 (Seal Kit)
├── PN-61-20-XX-02B-200 (Control Unit)
│   ├── PN-61-20-XX-02B-201 (Controller PCB)
│   ├── PN-61-20-XX-02B-202 (Connector Set)
│   └── PN-61-20-XX-02B-203 (Cable Assembly)
└── PN-61-20-XX-02B-300 (Hardware Kit)
    ├── PN-61-20-XX-02B-301 (Bracket)
    └── PN-61-20-XX-02B-302 (Fasteners)
```

### 2.2 BOM Table

| Level | Part Number | Nomenclature | Qty | Unit | Make/Buy |
|-------|-------------|--------------|-----|------|----------|
| 0 | PN-61-20-XX-02B | ComponentB | 1 | EA | Make |
| 1 | PN-61-20-XX-02B-100 | Main Assembly | 1 | EA | Make |
| 2 | PN-61-20-XX-02B-101 | Frame | 1 | EA | Make |
| 2 | PN-61-20-XX-02B-102 | Cover | 1 | EA | Make |
| 2 | PN-61-20-XX-02B-103 | Seal Kit | 1 | SET | Buy |
| 1 | PN-61-20-XX-02B-200 | Control Unit | 1 | EA | Make |
| 2 | PN-61-20-XX-02B-201 | Controller PCB | 1 | EA | Make |
| 2 | PN-61-20-XX-02B-202 | Connector Set | 1 | SET | Buy |
| 2 | PN-61-20-XX-02B-203 | Cable Assembly | 1 | EA | Make |
| 1 | PN-61-20-XX-02B-300 | Hardware Kit | 1 | KIT | Buy |
| 2 | PN-61-20-XX-02B-301 | Bracket | 1 | EA | Make |
| 2 | PN-61-20-XX-02B-302 | Fasteners | 1 | SET | Buy |

---

## 3. Line Maintenance Parts (LMP)

### 3.1 LMP List

| Part Number | Nomenclature | Qty/LRU | Category | MTTR (min) |
|-------------|--------------|---------|----------|------------|
| PN-61-20-XX-02B-103 | Seal Kit | 1 | Standard | 20 |
| PN-61-20-XX-02B-202 | Connector Set | 1 | High | 35 |
| PN-61-20-XX-02B-302 | Fasteners | 1 | Standard | 10 |

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
