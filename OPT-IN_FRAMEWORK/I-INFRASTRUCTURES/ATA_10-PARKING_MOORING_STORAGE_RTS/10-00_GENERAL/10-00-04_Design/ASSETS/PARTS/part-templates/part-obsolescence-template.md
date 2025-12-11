# Part Obsolescence Management — [Part ID]

## Purpose

This document manages the obsolescence process for parts in the ATA 10 PARTS library, ensuring proper transition, documentation, and traceability when parts are superseded or declared obsolete.

---

## Part Information

| Field | Value |
|-------|-------|
| **Part ID** | [10-PRT-XX-NNN] |
| **Part Title** | [Part title] |
| **Current Status** | [ACTIVE / SUPERSEDED / OBSOLETE] |
| **Category** | [Category] |
| **Initiated By** | [Name / Role] |
| **Initiation Date** | [YYYY-MM-DD] |

---

## Section 1: Obsolescence Type

Select the type of obsolescence:

- [ ] **Superseded** - Part is being replaced by a new/improved part
- [ ] **Obsolete** - Part is no longer needed (no replacement)
- [ ] **End of Life** - Supplier/manufacturer discontinuing part

---

## Section 2: Reason for Obsolescence

### 2.1 Primary Reason

Select primary reason:

- [ ] Design improvement available
- [ ] Supplier discontinuation
- [ ] Material no longer available
- [ ] Performance issues
- [ ] Cost optimization
- [ ] Safety enhancement
- [ ] Regulatory/compliance requirements
- [ ] Technology obsolescence
- [ ] Other: _______________________

### 2.2 Detailed Justification

[Provide detailed explanation of why part is being obsoleted or superseded]

---

## Section 3: Superseding Part Information

**Note:** Complete this section only if part is being SUPERSEDED. If part is becoming OBSOLETE with no replacement, skip to Section 4.

### 3.1 Replacement Part

| Field | Value |
|-------|-------|
| **New Part ID** | [10-PRT-XX-NNN] |
| **New Part Title** | [Title] |
| **New Part Number** | [P/N] |
| **New Part Status** | [Should be ACTIVE or IN_DEVELOPMENT] |

### 3.2 Comparison

| Aspect | Old Part | New Part | Notes |
|--------|----------|----------|-------|
| **Form** | [Description] | [Description] | [Identical / Similar / Different] |
| **Fit** | [Description] | [Description] | [Identical / Similar / Different] |
| **Function** | [Description] | [Description] | [Identical / Enhanced / Different] |
| **Performance** | [Specs] | [Specs] | [Notes] |
| **Cost** | [Category] | [Category] | [Notes] |
| **Lead Time** | [Days] | [Days] | [Notes] |

### 3.3 Improvements

List improvements in new part:

1. [Improvement 1]
2. [Improvement 2]
3. [Improvement 3]

### 3.4 Backward Compatibility

- [ ] New part is **fully backward compatible** (drop-in replacement)
- [ ] New part requires **minor modifications** for compatibility
- [ ] New part requires **significant design changes** for compatibility

**Compatibility Notes:**

[Describe any modifications, rework, or design changes needed to use new part]

---

## Section 4: Impact Assessment

### 4.1 Current Usage

| Aspect | Details |
|--------|---------|
| **Assemblies Using Part** | [List assembly IDs or count] |
| **Drawings Referencing Part** | [List drawing IDs or count] |
| **Current Inventory** | [Quantity on hand] |
| **Pending Orders** | [Quantity on order] |
| **Annual Usage** | [Estimated annual usage] |

### 4.2 Impact on Systems

- [ ] **No impact** - Part not currently used
- [ ] **Low impact** - Used in non-critical applications, easy substitution
- [ ] **Medium impact** - Used in multiple assemblies, moderate effort to change
- [ ] **High impact** - Critical part, significant effort required for transition

**Impact Description:**

[Describe the impact of obsoleting/superseding this part on aircraft systems, assemblies, and operations]

### 4.3 Affected Stakeholders

List affected teams/individuals:

- [ ] Engineering team
- [ ] Procurement team
- [ ] Manufacturing team
- [ ] Quality assurance
- [ ] Maintenance team
- [ ] Certification authority
- [ ] Suppliers
- [ ] Other: ____________________

---

## Section 5: Transition Plan

### 5.1 Timeline

| Milestone | Target Date | Status | Notes |
|-----------|-------------|--------|-------|
| Obsolescence decision | [Date] | [ ] Complete | |
| New part qualification (if superseded) | [Date] | [ ] Complete | |
| Engineering change order issued | [Date] | [ ] Complete | |
| Drawing updates complete | [Date] | [ ] Complete | |
| BOM updates complete | [Date] | [ ] Complete | |
| Inventory depleted or disposed | [Date] | [ ] Complete | |
| Documentation updated | [Date] | [ ] Complete | |
| Obsolescence effective date | [Date] | [ ] Complete | |

### 5.2 Inventory Management

**Current Inventory Disposition:**

- [ ] **Use up** - Deplete existing inventory before transition
- [ ] **Return to supplier** - Return unused inventory
- [ ] **Scrap** - Dispose of inventory
- [ ] **Archive** - Store for legacy support
- [ ] **Other**: _______________________

**Inventory Count:** [Number of units]

**Estimated Depletion Date:** [Date]

### 5.3 Pending Orders

- [ ] No pending orders
- [ ] Cancel pending orders
- [ ] Allow pending orders to complete
- [ ] Replace pending orders with new part

**Order Details:**

[Describe any pending procurement orders and their disposition]

---

## Section 6: Documentation Updates Required

### 6.1 Part Documents

- [ ] Update old part document status to OBSOLETE or SUPERSEDED
- [ ] Add "superseded_by" field in old part document (if applicable)
- [ ] Update new part document with supersession info (if applicable)
- [ ] Update revision history in both documents

### 6.2 Index & Catalogs

- [ ] Update 00_INDEX.md
- [ ] Update part metadata files
- [ ] Update any parts catalogs or databases

### 6.3 Drawings

List drawings requiring updates:

- [Drawing ID 1] - [Description]
- [Drawing ID 2] - [Description]
- [Drawing ID 3] - [Description]

### 6.4 Bills of Material (BOMs)

List BOMs requiring updates:

- [BOM ID 1] - [Description]
- [BOM ID 2] - [Description]
- [BOM ID 3] - [Description]

### 6.5 Assemblies

List assemblies requiring updates:

- [Assembly ID 1] - [Description]
- [Assembly ID 2] - [Description]
- [Assembly ID 3] - [Description]

---

## Section 7: Change Control

### 7.1 Engineering Change Order (ECO)

- [ ] ECO created
- [ ] ECO number: ____________________
- [ ] ECO approved
- [ ] ECO implemented

### 7.2 Configuration Management

- [ ] Configuration baseline updated
- [ ] Version/tag created for transition
- [ ] Change log updated
- [ ] Traceability matrix updated

---

## Section 8: Communication Plan

### 8.1 Notifications

- [ ] Engineering team notified
- [ ] Procurement team notified
- [ ] Manufacturing team notified
- [ ] Quality team notified
- [ ] Maintenance team notified
- [ ] Suppliers notified
- [ ] Customers notified (if applicable)

### 8.2 Communication Date

**Notification Sent:** [YYYY-MM-DD]

**Notification Method:**

- [ ] Email
- [ ] Meeting
- [ ] Formal letter
- [ ] ECO distribution
- [ ] Other: ____________________

---

## Section 9: Supplier Coordination

### 9.1 Old Part Supplier

- [ ] Supplier notified of discontinuation
- [ ] Remaining inventory disposition coordinated
- [ ] Pending orders resolved
- [ ] Contract closure initiated (if applicable)

### 9.2 New Part Supplier (If Superseded)

- [ ] New supplier qualified
- [ ] Purchase agreement established
- [ ] Quality requirements communicated
- [ ] Lead times confirmed

---

## Section 10: Legacy Support

### 10.1 Legacy Aircraft/Systems

Are there legacy aircraft or systems still requiring this part?

- [ ] **No** - No legacy support needed
- [ ] **Yes** - Legacy support plan required

**If Yes, Legacy Support Plan:**

- [ ] Maintain inventory for legacy support
- [ ] Establish alternate sourcing
- [ ] Develop modification kit for new part
- [ ] Document legacy part as custom/special order

**Legacy Support Duration:** [Specify duration or "Indefinite"]

### 10.2 Documentation Archival

- [ ] Old part document moved to archive (if full obsolescence)
- [ ] Old part document retained with OBSOLETE/SUPERSEDED status
- [ ] Drawings archived or marked superseded
- [ ] Historical records maintained

---

## Section 11: Verification & Closeout

### 11.1 Verification Checklist

- [ ] All drawings updated and released
- [ ] All BOMs updated and released
- [ ] All assemblies updated and released
- [ ] Old part inventory depleted or disposed
- [ ] New part (if applicable) in active inventory
- [ ] All documentation updated
- [ ] All stakeholders notified
- [ ] ECO closed
- [ ] Configuration management updated

### 11.2 Lessons Learned

[Document any lessons learned during the obsolescence process that could improve future transitions]

---

## Section 12: Approval

### 12.1 Technical Approval

**Approved By:**

- **Name**: ___________________________
- **Role**: ___________________________
- **Date**: ___________________________
- **Signature**: ___________________________

### 12.2 Quality Approval

**Approved By:**

- **Name**: ___________________________
- **Role**: ___________________________
- **Date**: ___________________________
- **Signature**: ___________________________

### 12.3 Management Approval

**Approved By:**

- **Name**: ___________________________
- **Role**: ___________________________
- **Date**: ___________________________
- **Signature**: ___________________________

---

## Section 13: Closeout

### 13.1 Obsolescence Status

- [ ] **Complete** - Part obsolescence/supersession fully implemented
- [ ] **In Progress** - Transition ongoing
- [ ] **Cancelled** - Obsolescence decision reversed

**Effective Date:** [YYYY-MM-DD]

**Closeout Date:** [YYYY-MM-DD]

### 13.2 Final Notes

[Any final notes, follow-up actions, or special considerations]

---

## Document Control

- **Template Version**: 1.0
- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**
- **Status**: TEMPLATE
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last Updated**: 2025-12-09
- **Owner**: AMPEL360 Documentation WG

---

## Usage Instructions

1. **Create a copy** of this template when obsoleting or superseding a part
2. **Fill in** all applicable sections
3. **Complete** transition plan and timeline
4. **Coordinate** with all affected stakeholders
5. **Update** all related documentation
6. **Obtain** required approvals
7. **File** completed document with part records
8. **Monitor** transition to completion

### When to Use:

- Replacing a part with an improved design (supersession)
- Discontinuing a part with no replacement (obsolescence)
- Managing supplier end-of-life notifications
- Coordinating engineering changes affecting parts
