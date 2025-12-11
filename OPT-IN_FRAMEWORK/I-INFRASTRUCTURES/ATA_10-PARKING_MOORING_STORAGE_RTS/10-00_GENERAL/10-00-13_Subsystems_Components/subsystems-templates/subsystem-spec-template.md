# [Document ID] — [Subsystem Title]

## 1. Document Information

| Field | Value |
|-------|-------|
| **Document ID** | [10-00-13-NNA] |
| **Document Number** | [10-00-13-NNA_Subsystem_Name] |
| **Title** | [Subsystem Title] |
| **Revision** | [A] |
| **Status** | [DRAFT / FOR_REVIEW / APPROVED] |
| **Date** | [YYYY-MM-DD] |
| **Subsystem Type** | [architecture / parking / mooring / storage / h2-safety / cryo / bwb / component-breakdown] |
| **Subsystem ID** | [SUBSYS-ID-XXX] |
| **Parent System** | [Parent System Name (Doc ID)] |
| **Safety Critical** | [Yes / No] |
| **DAL Level** | [A / B / C / D / E / N/A] |

## 2. Purpose

[Provide a clear, concise statement of the subsystem's purpose. Explain what the subsystem does, why it exists, and its role within the overall ATA 10 system. Include specific mention of H2/LH2 aspects if applicable, and BWB configuration adaptations if relevant.]

[Example: "The [Subsystem Name] provides [key function] for the AMPEL360-BWB-H2-Hy-E aircraft during [operational context]. It is designed to [primary objective] while ensuring [safety/performance goal]."]

## 3. Scope

### 3.1 In Scope

[List all functions, components, and activities that are part of this subsystem]
- [Function or component 1]
- [Function or component 2]
- [Function or component 3]
- [Interface to System X]
- [Safety feature Y]

### 3.2 Out of Scope

[List related functions or components that are explicitly NOT part of this subsystem, with references to where they are covered]
- [Function covered in another subsystem] (see [Doc ID])
- [Component covered in another ATA chapter] (see ATA XX)
- [Operational procedure] (see 10-10_Operations)

## 4. Functional Description

### 4.1 Primary Functions

[Numbered list of the key functions performed by this subsystem]

1. **[Function 1 Name]** - [Description of function 1]
2. **[Function 2 Name]** - [Description of function 2]
3. **[Function 3 Name]** - [Description of function 3]
4. **[Function 4 Name]** - [Description of function 4]

### 4.2 Operational Modes

[Table describing different operational modes if applicable]

| Mode | Description | Active Components | Typical Use Case |
|------|-------------|-------------------|------------------|
| **[Mode 1]** | [Description] | [Component list] | [When used] |
| **[Mode 2]** | [Description] | [Component list] | [When used] |
| **[Mode 3]** | [Description] | [Component list] | [When used] |

## 5. Architecture

### 5.1 System Components

[Provide a hierarchical breakdown of subsystem components using text or diagram notation]

```
[Subsystem Name]
├── [Component Group 1]
│   ├── [Component 1.1]
│   ├── [Component 1.2]
│   └── [Component 1.3]
│
├── [Component Group 2]
│   ├── [Component 2.1]
│   └── [Component 2.2]
│
└── Interfaces
    ├── [Interface to System A]
    ├── [Interface to System B]
    └── [Interface to System C]
```

### 5.2 [Specific Architecture Aspect]

[Provide additional architectural details specific to this subsystem type]
[For H2 systems: sensor layouts, detection zones]
[For mechanical systems: structural load paths]
[For BWB systems: geometry-specific adaptations]

## 6. Component List

[Comprehensive list of all components within this subsystem]

| Component ID | Component Name | Part Number | Qty | Criticality |
|--------------|----------------|-------------|-----|-------------|
| [ID-001] | [Component name] | [P/N] | [#] | [Critical / Essential / Important / Standard] |
| [ID-002] | [Component name] | [P/N] | [#] | [Criticality] |
| [ID-003] | [Component name] | [P/N] | [#] | [Criticality] |
| [ID-004] | [Component name] | [P/N] | [#] | [Criticality] |

**Criticality Definitions:**
- **Critical:** Failure directly impacts safety or mission success
- **Essential:** Required for primary function, but redundancy/backup exists
- **Important:** Supports primary function, degraded operation possible without it
- **Standard:** Supportive role, minimal impact if unavailable

## 7. Interfaces

### 7.1 Input Interfaces

[Table of all inputs to this subsystem]

| Interface ID | Source | Type | Description |
|--------------|--------|------|-------------|
| IF-[XXX]-001 | [Source system/subsystem] | [Mechanical / Electrical / H2-gas / LH2-liquid / Data / Thermal] | [Interface description] |
| IF-[XXX]-002 | [Source] | [Type] | [Description] |

### 7.2 Output Interfaces

[Table of all outputs from this subsystem]

| Interface ID | Destination | Type | Description |
|--------------|-------------|------|-------------|
| IF-[XXX]-101 | [Destination system/subsystem] | [Mechanical / Electrical / H2-gas / LH2-liquid / Data / Thermal] | [Interface description] |
| IF-[XXX]-102 | [Destination] | [Type] | [Description] |

## 8. Safety Features

[For safety-critical subsystems, detail all safety features. For non-safety-critical, provide safety considerations.]

### 8.1 Redundancy

[If applicable, describe redundant elements]
- **[System/Component]:** [Redundancy approach and level]
- **[System/Component]:** [Redundancy approach and level]

### 8.2 Fail-Safe Design

[Describe fail-safe features]
- **[Component/Function]:** [Fail-safe behavior]
- **[Component/Function]:** [Fail-safe behavior]

### 8.3 Self-Diagnostics

[If applicable, describe built-in test capabilities]
- **[Diagnostic function 1]**
- **[Diagnostic function 2]**

## 9. Requirements Traceability

[Table linking this subsystem to parent requirements]

| Requirement ID | Requirement Description | Verification Method |
|---------------|-------------------------|---------------------|
| REQ-10-[XXX]-001 | [Requirement text] | [Test / Analysis / Inspection / Demonstration] |
| REQ-10-[XXX]-002 | [Requirement text] | [Verification method] |
| REQ-10-[XXX]-003 | [Requirement text] | [Verification method] |

[Reference to requirements database: See `10-00-03_Requirements/` for complete requirements]

## 10. Hazard Mitigation

[Table showing which hazards this subsystem helps mitigate]

| Hazard ID | Hazard Description | Mitigation by this Subsystem |
|-----------|-------------------|------------------------------|
| H-10-[XXX] | [Hazard description] | [How this subsystem mitigates the hazard] |
| H-10-[YYY] | [Hazard description] | [Mitigation approach] |

[Reference to safety analysis: See `10-00-02_Safety/` for complete hazard analysis]

## 11. Operational Domain

[Table of environmental and operational limits]

| Parameter | Min | Typical | Max | Unit | Notes |
|-----------|-----|---------|-----|------|-------|
| Ambient Temperature | [value] | [value] | [value] | °C | [Operational notes] |
| Relative Humidity | [value] | [value] | [value] | % RH | [Notes] |
| [Parameter] | [value] | [value] | [value] | [unit] | [Notes] |

## 12. H2/Cryo Specific Considerations

[Complete this section for H2-related or cryogenic subsystems. Otherwise mark as "N/A - Not H2/Cryo related"]

### 12.1 H2 Compatibility

[If applicable]
- **H2 Service Type:** [Gaseous H2 / Liquid H2 (LH2) / Both / N/A]
- **H2 Pressure Rating:** [value bar/psi / N/A]
- **Material Qualification:** [ISO 11114-4 qualified / SAE AS6968 compliant / N/A]

### 12.2 Cryogenic Requirements

[If applicable]
- **Cryo Rated:** [Yes / No]
- **Operating Temperature Range:** [min to max °C]
- **Insulation Type:** [MLI / Aerogel / Vacuum / Foam / None / N/A]
- **Cryo Standard Compliance:** [ASTM E1450 / ISO 20421 / N/A]

### 12.3 ATEX/IECEx Classification

[If operating in explosive atmospheres]
- **ATEX/IECEx Certified:** [Yes / No / N/A]
- **Zone Rating:** [Zone 0/1/2/20/21/22 / N/A]
- **Equipment Group:** [IIC / IIB / IIA / N/A]

## 13. BWB-Specific Considerations

[Complete this section for BWB-specific subsystems. Otherwise mark as "N/A - Not BWB-specific"]

### 13.1 BWB Geometric Adaptations

[If applicable, describe how BWB geometry influences this subsystem]
- [Adaptation 1]
- [Adaptation 2]

### 13.2 BWB Load Distribution

[If applicable, describe BWB-specific load considerations]

## 14. Maintenance Requirements

[Describe maintenance approach for this subsystem]

### 14.1 Preventive Maintenance Schedule

| Interval | Task | Responsible Party | Estimated Duration |
|----------|------|------------------|-------------------|
| [Daily / Weekly / Monthly / Quarterly / Annual] | [Task description] | [Role] | [Hours] |
| [Interval] | [Task] | [Role] | [Duration] |

### 14.2 Calibration Requirements

[If applicable]

| Component | Interval | Calibration Standard | Acceptance Criteria |
|-----------|----------|---------------------|---------------------|
| [Component name] | [Interval] | [Standard] | [Criteria] |

### 14.3 Replacement Schedule

[List components with defined replacement intervals]

| Component | Replacement Interval | Replacement Trigger |
|-----------|---------------------|---------------------|
| [Component] | [Interval or hours] | [Trigger condition] |

## 15. Applicable Standards

[List all standards applicable to this subsystem]

### 15.1 General Standards

- **ATA iSpec 2200** - [Specific section if applicable]
- **ATA 100** - Chapter 10 [Specific section]
- **SAE ARP4754A** - [Applicable clauses]
- **[Other standard]** - [Description]

### 15.2 H2/Cryogenic Standards

[If applicable]
- **SAE AS6968** - [Section]
- **NFPA 2** - [Section]
- **ISO 11114-4** - [Description]
- **ISO 13984** - [Description]
- **ISO 20421-1** - [Description]

### 15.3 Safety & Certification Standards

[If safety-critical]
- **DO-178C** - [If software is involved]
- **DO-254** - [If complex electronics are involved]
- **IEC 61508** - [If safety-instrumented system]
- **ATEX 2014/34/EU** - [If explosive atmosphere]
- **IECEx** - [If explosive atmosphere]

## 16. Related Documentation

[List all related documents with hyperlinks if available]

- [Parent System Architecture Document] - [Link]
- [Related Subsystem 1] - [Link]
- [Related Subsystem 2] - [Link]
- [Interface Control Document] - [Link to 10-00-05_Interfaces]
- [Safety Analysis] - [Link to 10-00-02_Safety]
- [Requirements] - [Link to 10-00-03_Requirements]

## 17. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | [YYYY-MM-DD] | [Author name] | Initial release |
| [B] | [YYYY-MM-DD] | [Author] | [Description of changes] |

## 18. Document Control

| Field | Value |
|-------|-------|
| **Status** | [DRAFT / FOR_REVIEW / APPROVED / OBSOLETE] |
| **Owner** | [Responsible Working Group or Individual] |
| **Approver** | _[to be completed]_ |
| **Classification** | [Public / Internal Use / Confidential] |
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

1. **Copy this template** to create a new subsystem specification
2. **Replace all bracketed placeholders** `[...]` with actual content
3. **Remove sections** that are not applicable (or mark as "N/A")
4. **Follow naming convention:** `10-00-13-NNA_Subsystem_Name.md`
5. **Maintain consistency** with numbering ranges per subsystem category
6. **Add to index** `00_INDEX.md` after creation
7. **Link from parent** system architecture document

---

*End of Template*
