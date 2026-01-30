# Product Bill of Materials (BOM) Template

## Product: [Product Number] - [Product Title]

**Document**: [10-BOM-XX-nnn]  
**Revision**: [A]  
**Date**: [YYYY-MM-DD]  
**Status**: [ACTIVE]

---

## 1. Product Summary

| Parameter | Value |
|-----------|-------|
| Product Number | [10-PRD-XX-nnn] |
| Product Title | [Full title] |
| BOM Revision | [A] |
| Effective Date | [YYYY-MM-DD] |
| Kit Type | [standard / heavy-duty / emergency / bwb-specific / h2-specific] |
| Total Kit Weight | [XXX kg] |
| Total Kit Value | [€ XXX,XXX] |

---

## 2. Complete Bill of Materials

### 2.1 Primary Components

| Item | Level | Part Number | Description | Qty | UoM | Unit Weight (kg) | Unit Cost (€) | Total Cost (€) | Supplier | Lead Time (days) |
|------|-------|-------------|-------------|-----|-----|------------------|---------------|----------------|----------|------------------|
| 1 | 1 | [10-PART-XX-nnn] | [Description] | [X] | EA | [X.X] | [XXX] | [XXX] | [Supplier] | [XX] |
| 2 | 1 | [10-PART-XX-nnn] | [Description] | [X] | EA | [X.X] | [XXX] | [XXX] | [Supplier] | [XX] |
| 3 | 1 | [10-PART-XX-nnn] | [Description] | [X] | EA | [X.X] | [XXX] | [XXX] | [Supplier] | [XX] |

**Level Key:**
- Level 1: Top-level components (included in kit)
- Level 2: Sub-components (part of Level 1 assemblies)

### 2.2 Consumable Items

| Item | Part Number | Description | Qty | UoM | Shelf Life | Replacement Interval | Unit Cost (€) |
|------|-------------|-------------|-----|-----|------------|---------------------|---------------|
| 1 | [10-PART-XX-nnn] | [Description] | [X] | EA | [XX months] | [As needed] | [XXX] |

### 2.3 Documentation & Accessories

| Item | Document/Part Number | Description | Qty | Format |
|------|---------------------|-------------|-----|--------|
| 1 | [10-INST-XX-nnn] | Installation manual | 1 | PDF + Printed |
| 2 | [10-INSP-XX-nnn] | Inspection checklist | 1 | PDF + Printed |
| 3 | [10-PART-XX-nnn] | Storage container | 1 | Physical |

### 2.4 Optional Components

| Item | Part Number | Description | Qty | UoM | Notes |
|------|-------------|-------------|-----|-----|-------|
| 1 | [10-PART-XX-nnn] | [Optional component] | [X] | EA | [When to include] |

---

## 3. BOM Totals

| Category | Items | Total Weight (kg) | Total Cost (€) |
|----------|-------|-------------------|----------------|
| Primary Components | [X] | [XXX.X] | [X,XXX] |
| Consumables | [X] | [XX.X] | [XXX] |
| Documentation | [X] | [X.X] | [XX] |
| Packaging | 1 | [XX.X] | [XXX] |
| **TOTAL** | **[XX]** | **[XXX.X]** | **[X,XXX]** |

---

## 4. Sourcing Information

### 4.1 Primary Suppliers

| Supplier | Supplier Code | Parts Supplied | Lead Time | Payment Terms |
|----------|--------------|----------------|-----------|---------------|
| [Supplier 1] | [SUP-XXX] | [List of part numbers] | [XX days] | [Terms] |
| [Supplier 2] | [SUP-XXX] | [List of part numbers] | [XX days] | [Terms] |

### 4.2 Alternative Suppliers (Approved)

| Part Number | Primary Supplier | Alternative Supplier(s) | Notes |
|-------------|-----------------|------------------------|-------|
| [10-PART-XX-nnn] | [Supplier] | [Alt Supplier 1, Alt Supplier 2] | [Qualification notes] |

---

## 5. Part Specifications

### 5.1 Critical Parts (Require Incoming Inspection)

| Part Number | Description | Critical Parameter | Inspection Requirement |
|-------------|-------------|-------------------|------------------------|
| [10-PART-XX-nnn] | [Description] | [Parameter] | [Inspection procedure] |

### 5.2 Long Lead Items (>90 days)

| Part Number | Description | Lead Time | Reorder Point | Notes |
|-------------|-------------|-----------|---------------|-------|
| [10-PART-XX-nnn] | [Description] | [XXX days] | [When to reorder] | [Planning notes] |

---

## 6. Packaging & Shipping

### 6.1 Packaging Specification

| Level | Container Type | Dimensions (L×W×H mm) | Weight Capacity (kg) | Quantity |
|-------|---------------|----------------------|---------------------|----------|
| Primary | [Container type] | [XXX×XXX×XXX] | [XXX] | 1 |
| Secondary | [Shipping box] | [XXX×XXX×XXX] | [XXX] | 1 |

### 6.2 Packaging Materials

| Item | Part Number | Description | Qty | Purpose |
|------|-------------|-------------|-----|---------|
| 1 | [PKG-XXX] | [Padding material] | [X] | [Protection] |
| 2 | [PKG-XXX] | [Desiccant] | [X] | [Moisture control] |

### 6.3 Shipping Classification

- **UN/IATA Classification**: [If applicable]
- **Dangerous Goods**: [Yes/No]
- **Special Handling**: [Requirements]

---

## 7. Quality Control

### 7.1 Inspection Points

| Stage | Inspection Type | Procedure Reference | Accept/Reject Criteria |
|-------|----------------|-------------------|----------------------|
| Incoming | [Type] | [10-QC-XX-nnn] | [Criteria] |
| Assembly | [Type] | [10-QC-XX-nnn] | [Criteria] |
| Final | [Type] | [10-QC-XX-nnn] | [Criteria] |

### 7.2 Quality Records

- Incoming inspection records
- Assembly checklist
- Final inspection certificate
- Test reports (if applicable)

---

## 8. Configuration Management

### 8.1 Interchangeability

| Part Number | Interchangeable With | Notes |
|-------------|---------------------|-------|
| [10-PART-XX-nnn] | [Alt part number] | [Conditions for interchange] |

### 8.2 Configuration Control

- BOM changes require engineering approval
- Part substitutions must be documented
- Effectivity dates tracked per BOM revision

---

## 9. Special Requirements

### 9.1 H2-Specific Requirements (if H2 product)

- Non-sparking materials required: [List parts]
- Anti-static treatment required: [List parts]
- Explosion-proof rating: [Class/Division]
- Special certifications: [List]

### 9.2 BWB-Specific Requirements (if BWB product)

- Custom geometry parts: [List]
- BWB-specific tooling required: [List]
- Special handling: [Requirements]

### 9.3 Cryo-Rated Requirements (if cryo-rated)

- Cryo-rated materials (-253°C): [List parts]
- Special testing required: [List]

---

## 10. Cost Breakdown

### 10.1 Cost Analysis

| Category | Subtotal (€) | % of Total |
|----------|-------------|------------|
| Materials | [X,XXX] | [XX%] |
| Labor (Assembly) | [XXX] | [X%] |
| Packaging | [XXX] | [X%] |
| Documentation | [XX] | [X%] |
| Overhead | [XXX] | [X%] |
| **Total** | **[X,XXX]** | **100%** |

### 10.2 Price Points

| Quantity | Unit Price (€) | Discount | Notes |
|----------|---------------|----------|-------|
| 1-5 | [X,XXX] | 0% | Standard pricing |
| 6-20 | [X,XXX] | [X%] | Volume discount |
| 21+ | [X,XXX] | [X%] | Large order discount |

---

## 11. Revision History

### 11.1 BOM Changes

| Rev | Date | ECN Number | Description of Changes | Approved By |
|-----|------|------------|----------------------|-------------|
| A | YYYY-MM-DD | [ECN-XXXX] | Initial release | [Name] |
| B | YYYY-MM-DD | [ECN-XXXX] | [Change description] | [Name] |

### 11.2 Effectivity

| Rev | Effective Date | Serial Numbers Affected | Notes |
|-----|---------------|------------------------|-------|
| A | YYYY-MM-DD | All | Initial release |
| B | YYYY-MM-DD | [S/N XXXX and up] | [Change notes] |

---

## 12. Assembly Instructions Summary

### 12.1 Assembly Sequence

1. [Step 1 - Assembly stage]
2. [Step 2 - Assembly stage]
3. [Step 3 - Assembly stage]
4. [Continue as needed]

**Detailed assembly instructions**: See [10-INST-XX-nnn]

### 12.2 Special Tools Required

| Tool | Tool Number | Description | Supplier |
|------|-------------|-------------|----------|
| [Tool 1] | [TOOL-XXX] | [Description] | [Supplier] |

---

## Document Control

- **Document Number**: [10-BOM-XX-nnn]
- **Status**: ACTIVE
- **Revision**: [A]
- **Date**: YYYY-MM-DD
- **Generated with assistance from**: AI (GitHub Copilot), prompted by Amedeo Pelliccia
- **Approver**: [To be completed by Product Engineering]
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Path**: `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_10-PARKING_MOORING_STORAGE_RTS/10-00_GENERAL/10-00-04_Design/ASSETS/PRODUCTS/`

---

## Notes for BOM Template Users

**Instructions:**
1. Replace all [bracketed] placeholders with actual data
2. Add/remove rows as needed to accommodate your BOM
3. Ensure all part numbers follow AMPEL360 numbering convention
4. Include complete supplier information
5. Document all quality inspection requirements
6. Track configuration management carefully
7. Maintain revision history for all BOM changes
8. Cost data may be marked confidential if needed

**BOM Management:**
- Update BOM when parts change
- Issue Engineering Change Notice (ECN) for revisions
- Track effectivity by serial number or date
- Maintain approved vendor list (AVL)
- Document part interchangeability

**Quality Assurance:**
- All BOMs require engineering approval
- Changes require change control process
- Inspection requirements must be defined
- Test data referenced where applicable

---
