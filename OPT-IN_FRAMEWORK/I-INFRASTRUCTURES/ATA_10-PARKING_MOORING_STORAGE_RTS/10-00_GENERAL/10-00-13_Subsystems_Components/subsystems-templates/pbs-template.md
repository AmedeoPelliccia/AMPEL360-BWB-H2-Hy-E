# [Document ID] — Product Breakdown Structure (PBS)

## 1. Document Information

| Field | Value |
|-------|-------|
| **Document ID** | [10-00-13-7XA] |
| **Document Number** | [10-00-13-7XA_Component_Category_PBS] |
| **Title** | [Category] Product Breakdown Structure |
| **Revision** | [A] |
| **Status** | [DRAFT / FOR_REVIEW / APPROVED] |
| **Date** | [YYYY-MM-DD] |
| **Scope** | [All / Parking / Mooring / Storage / H2 / Cryo / BWB] Components |

## 2. Purpose

This document provides the hierarchical Product Breakdown Structure (PBS) for **[Category]** components within ATA 10 - Parking, Mooring, Storage & RTS systems for the AMPEL360-BWB-H2-Hy-E aircraft.

The PBS follows **MIL-STD-881** (Work Breakdown Structures) and **ATA iSpec 2200** guidance to organize components by function, subsystem, and physical/logical grouping.

## 3. Scope

### 3.1 In Scope

[Define what components are covered by this PBS]
- [Subsystem category 1]
- [Subsystem category 2]
- [Component types included]

### 3.2 Out of Scope

[Define what is NOT covered by this PBS]
- [Components covered in other PBS documents]
- [Reference to other ATA chapters]

## 4. PBS Hierarchy

### 4.1 PBS Structure

The PBS follows a hierarchical structure with the following levels:

```
Level 1: ATA Chapter (10)
    └── Level 2: System (10-00-13)
        └── Level 3: Subsystem Group ([Category])
            └── Level 4: Subsystem (Individual subsystems)
                └── Level 5: Assembly (Major assemblies within subsystem)
                    └── Level 6: Component (Individual components)
                        └── Level 7: Part (Lowest-level parts)
```

### 4.2 Numbering Convention

| Level | Format | Example | Description |
|-------|--------|---------|-------------|
| 1 | ATA-XX | ATA-10 | ATA Chapter |
| 2 | ATA-XX-YY-ZZ | 10-00-13 | Subsection |
| 3 | [CAT]-XXX | [CAT]-XXX | Subsystem group |
| 4 | [CAT]-XXX-SS | [CAT]-XXX-10 | Individual subsystem |
| 5 | [CAT]-XXX-SS-AA | [CAT]-XXX-10-01 | Assembly |
| 6 | [CAT]-XXX-SS-AA-CC | [CAT]-XXX-10-01-001 | Component |
| 7 | P/N | [Actual Part Number] | Manufacturer part number |

## 5. Product Breakdown Structure

### 5.1 Level 1-2: ATA Chapter and Subsection

```
10 - Parking, Mooring, Storage & RTS
    └── 10-00-13 - Subsystems & Components
```

### 5.2 Level 3: Subsystem Groups

[List all subsystem groups in this category]

```
10-00-13 - Subsystems & Components
    ├── [Group 1] ([Code]-XXX)
    ├── [Group 2] ([Code]-YYY)
    ├── [Group 3] ([Code]-ZZZ)
    └── ...
```

### 5.3 Level 4-7: Detailed PBS

[Provide detailed breakdown for each subsystem group]

#### 5.3.1 [Subsystem Group Name]

**Subsystem ID:** [ID]  
**Document Reference:** [10-00-13-NNA]

```
[SUBSYSTEM-ID]
├── [SUBSYSTEM-ID]-ASM-01 - [Assembly 1 Name]
│   ├── [SUBSYSTEM-ID]-ASM-01-001 - [Component Name]
│   │   ├── P/N: [Manufacturer Part Number]
│   │   ├── Qty: [Quantity]
│   │   └── Critical: [Yes/No]
│   │
│   ├── [SUBSYSTEM-ID]-ASM-01-002 - [Component Name]
│   │   ├── P/N: [Part Number]
│   │   ├── Qty: [Quantity]
│   │   └── Critical: [Yes/No]
│   │
│   └── [Continue...]
│
├── [SUBSYSTEM-ID]-ASM-02 - [Assembly 2 Name]
│   └── [Components...]
│
└── [Continue...]
```

## 6. Complete Component List (Tabular Format)

[Provide a complete flat list of all components for easy reference]

| PBS ID | Component Name | P/N | Qty | Subsystem | Criticality | H2-Related | Cryo | ATEX |
|--------|----------------|-----|-----|-----------|-------------|------------|------|------|
| [ID]-001 | [Component] | [P/N] | [#] | [Subsystem] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| [ID]-002 | [Component] | [P/N] | [#] | [Subsystem] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| [ID]-003 | [Component] | [P/N] | [#] | [Subsystem] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Total Component Count:** [Number]

## 7. Component Statistics

### 7.1 Component Count by Subsystem

| Subsystem | Total Components | Critical | Essential | Important | Standard |
|-----------|-----------------|----------|-----------|-----------|----------|
| [Subsystem 1] | [#] | [#] | [#] | [#] | [#] |
| [Subsystem 2] | [#] | [#] | [#] | [#] | [#] |
| **TOTAL** | [#] | [#] | [#] | [#] | [#] |

### 7.2 Component Count by Type

| Component Type | Count | % of Total |
|----------------|-------|------------|
| [Mechanical] | [#] | [%] |
| [Electrical] | [#] | [%] |
| [Sensor] | [#] | [%] |
| [Valve] | [#] | [%] |
| [Controller] | [#] | [%] |
| [Other] | [#] | [%] |
| **TOTAL** | [#] | 100% |

### 7.3 H2/Cryo Component Summary

| Category | Count | Notes |
|----------|-------|-------|
| H2-Related Components | [#] | [Components exposed to H2] |
| Cryo-Related Components | [#] | [Components in cryogenic service] |
| ATEX-Certified Components | [#] | [Components in hazardous areas] |

## 8. Supplier Analysis

### 8.1 Primary Suppliers

| Supplier | CAGE Code | Component Count | % of Total | Lead Time (avg) |
|----------|-----------|----------------|------------|-----------------|
| [Supplier 1] | [CAGE] | [#] | [%] | [Days] |
| [Supplier 2] | [CAGE] | [#] | [%] | [Days] |
| [Supplier 3] | [CAGE] | [#] | [%] | [Days] |
| **TOTAL** | - | [#] | 100% | - |

### 8.2 Single-Source Components

[List components with only one qualified supplier - potential supply chain risk]

| Component ID | Component Name | Single Supplier | Risk Mitigation |
|--------------|----------------|----------------|-----------------|
| [ID] | [Name] | [Supplier] | [Mitigation plan] |
| [ID] | [Name] | [Supplier] | [Mitigation plan] |

## 9. Cost Analysis

### 9.1 Component Cost Summary

| Category | Total Cost ([Currency]) | % of Total | Notes |
|----------|------------------------|------------|-------|
| [Category 1] | [Cost] | [%] | [Notes] |
| [Category 2] | [Cost] | [%] | [Notes] |
| **TOTAL** | [Cost] | 100% | - |

### 9.2 High-Value Components

[List top 10 most expensive components]

| Rank | Component ID | Component Name | Unit Cost | Qty | Total Cost |
|------|--------------|----------------|-----------|-----|------------|
| 1 | [ID] | [Name] | [Cost] | [#] | [Total] |
| 2 | [ID] | [Name] | [Cost] | [#] | [Total] |
| ... | ... | ... | ... | ... | ... |

## 10. Maintenance Impact Analysis

### 10.1 Consumable Components

[Components with defined replacement intervals]

| Component ID | Component Name | Replacement Interval | Annual Consumption | Unit Cost |
|--------------|----------------|---------------------|-------------------|-----------|
| [ID] | [Name] | [Interval] | [Qty/year] | [Cost] |
| [ID] | [Name] | [Interval] | [Qty/year] | [Cost] |

### 10.2 Calibration-Required Components

| Component ID | Component Name | Calibration Interval | Calibration Cost | Notes |
|--------------|----------------|---------------------|------------------|-------|
| [ID] | [Name] | [Interval] | [Cost] | [Notes] |
| [ID] | [Name] | [Interval] | [Cost] | [Notes] |

## 11. Cross-References

### 11.1 Related PBS Documents

- [10-00-13-70A - Complete PBS](./10-00-13-70A_PBS_Product_Breakdown_Structure.md)
- [10-00-13-71A - Parking Components PBS] (if different document)
- [10-00-13-72A - H2 Components PBS] (if different document)

### 11.2 Subsystem Documents

- [10-00-13-XXA - Subsystem 1](../[category]/10-00-13-XXA_Subsystem.md)
- [10-00-13-YYA - Subsystem 2](../[category]/10-00-13-YYA_Subsystem.md)

### 11.3 Design Documentation

- [10-00-04_Design](../../10-00-04_Design/) - Detailed design specifications
- [10-00-09_Production_Planning](../../10-00-09_Production_Planning/) - Manufacturing plans

## 12. Change Management

### 12.1 PBS Change Control

All changes to this PBS must follow the configuration management process:

1. **Proposed Change:** Submit change request with justification
2. **Impact Analysis:** Assess impact on cost, schedule, interfaces
3. **Approval:** Obtain approval from PBS owner and affected subsystem owners
4. **Update PBS:** Update this document and increment revision
5. **Notify Stakeholders:** Inform all affected parties of the change

### 12.2 Pending Changes

| Change ID | Description | Proposer | Status | Target Rev |
|-----------|-------------|----------|--------|------------|
| [CHG-001] | [Description] | [Name] | [Proposed/Approved/Rejected] | [Rev] |

## 13. Applicable Standards

- **MIL-STD-881** - Work Breakdown Structures for Defense Materiel Items
- **ATA iSpec 2200** - Information Standards for Aviation Maintenance
- **SAE ARP4754A** - Guidelines for Development of Civil Aircraft and Systems
- **ISO 10007** - Quality management - Guidelines for configuration management

## 14. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | [YYYY-MM-DD] | [Name] | Initial PBS release |
| B | [YYYY-MM-DD] | [Name] | [Description of changes] |

## 15. Document Control

| Field | Value |
|-------|-------|
| **Status** | [DRAFT / FOR_REVIEW / APPROVED] |
| **Owner** | AMPEL360 Configuration Management WG |
| **Approver** | _[to be completed]_ |
| **Classification** | Internal Use |
| **Next Review** | [YYYY-MM-DD] |

---

**AI Generation Note:**

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: [YYYY-MM-DD]

---

**Template Usage Instructions:**

1. **Copy this template** to create PBS documents
2. **Replace category placeholders** with specific category (Parking, H2, Cryo, etc.)
3. **Build PBS hierarchy** starting from subsystem groups
4. **Populate component tables** with actual part numbers and data
5. **Calculate statistics** for component counts, costs, suppliers
6. **Cross-reference** all subsystem specification documents
7. **Maintain** this PBS as a living document through change control

---

*End of Template*
