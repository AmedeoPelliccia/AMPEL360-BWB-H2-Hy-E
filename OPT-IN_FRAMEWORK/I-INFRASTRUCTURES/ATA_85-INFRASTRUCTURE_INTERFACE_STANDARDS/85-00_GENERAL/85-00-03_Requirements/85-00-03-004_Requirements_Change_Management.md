# 85-00-03-004 — Requirements Change Management

## 1. Purpose

This document defines the **change management framework** for infrastructure interface requirements of the AMPEL360 BWB H₂ Hy-E aircraft. It establishes procedures, governance, and controls for proposing, reviewing, approving, and implementing changes to infrastructure interface requirements throughout the aircraft lifecycle.

## 2. Change Management Objectives

Effective requirements change management ensures:

- **Controlled Evolution**: Requirements evolve in a controlled, traceable manner
- **Impact Transparency**: Stakeholders understand the implications of changes
- **Safety Integrity**: Safety-critical requirements are protected from unauthorized changes
- **Certification Continuity**: Changes maintain regulatory compliance and certification validity
- **Stakeholder Alignment**: External partners (airports, suppliers) are informed of changes
- **Configuration Control**: Requirements remain consistent with aircraft configuration

## 3. Change Management Governance

### 3.1 Roles and Responsibilities

| Role | Responsibilities | Authority |
|------|-----------------|-----------|
| **Configuration Control Board (CCB)** | Review and approve/reject requirement changes | Approves all changes |
| **Requirements Owner** | Maintain requirements, initiate changes, coordinate reviews | Propose changes, recommend approval |
| **Systems Engineering Lead** | Impact assessment, traceability analysis | Approve minor changes |
| **Chief Engineer** | Technical oversight, safety impact assessment | Veto authority on safety-critical changes |
| **Certification Manager** | Regulatory compliance assessment | Approve changes affecting certification basis |
| **Stakeholder Representatives** | Provide input on changes affecting their domains | Advisory (non-voting) |
| **Change Initiator** | Any team member who identifies need for requirement change | Propose changes |

### 3.2 Configuration Control Board (CCB)

The **CCB** is the governing body for all infrastructure interface requirement changes.

**CCB Composition**:
- Chair: Chief Engineer or Systems Engineering Lead
- Members:
  - Requirements Owner
  - Certification Manager
  - Safety Manager
  - Relevant Domain Experts (propulsion, structures, avionics, operations)
  - Stakeholder Representatives (as needed)

**CCB Meeting Frequency**:
- Regular meetings: Bi-weekly
- Emergency meetings: As needed for critical changes

**CCB Decision Authority**:
- **Approve**: Change is authorized for implementation
- **Reject**: Change is not authorized; requirement remains as-is
- **Defer**: Insufficient information; return to initiator for additional analysis
- **Conditional Approval**: Approved subject to specific conditions or further analysis

---

## 4. Change Request Process

### 4.1 Change Request Workflow

```
┌──────────────────────────────────────────────────────────────────┐
│ 1. INITIATE                                                      │
│    Change Initiator identifies need for requirement change       │
│    → Submit Change Request (CR) with justification               │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 2. ASSESS                                                        │
│    Requirements Owner performs initial impact assessment         │
│    → Identify affected requirements, design, verification, cert  │
│    → Assign priority and classification                          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 3. REVIEW                                                        │
│    Affected teams review change and provide input               │
│    → Design teams assess implementation impact                   │
│    → V&V teams assess verification impact                        │
│    → Certification team assesses regulatory impact               │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 4. CCB DECISION                                                  │
│    CCB reviews change request and all input                     │
│    → Approve / Reject / Defer / Conditional Approval             │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                     ┌───────┴────────┐
                     │ APPROVED       │ REJECTED → Closed
                     ▼                │
┌──────────────────────────────────────────────────────────────────┐
│ 5. IMPLEMENT                                                     │
│    Requirements Owner updates requirement documentation          │
│    → Update traceability links                                   │
│    → Update verification plans if needed                         │
│    → Notify stakeholders                                         │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 6. VERIFY                                                        │
│    V&V team confirms requirement change is properly verified     │
│    → Re-run affected test cases                                  │
│    → Update verification evidence                                │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 7. CLOSE                                                         │
│    Requirements Owner confirms all actions complete              │
│    → Update certification evidence if needed                     │
│    → Archive change request                                      │
└──────────────────────────────────────────────────────────────────┘
```

### 4.2 Change Request Form

All change requests must include:

| Field | Description | Mandatory |
|-------|-------------|-----------|
| **CR ID** | Unique change request identifier | Yes |
| **Date Submitted** | Date of CR submission | Yes |
| **Submitted By** | Name and role of change initiator | Yes |
| **Affected Requirement(s)** | Requirement ID(s) to be changed | Yes |
| **Change Type** | Clarification, Addition, Modification, Deletion | Yes |
| **Justification** | Reason for change (problem statement, opportunity) | Yes |
| **Proposed Change** | Specific wording or content change | Yes |
| **Impact Assessment** | Analysis of impacts on design, verification, certification | Yes (by Requirements Owner) |
| **Priority** | Critical, High, Medium, Low | Yes |
| **External Stakeholder Impact** | Does change affect airports, suppliers, operators? | Yes |
| **Safety Impact** | Does change affect safety-critical requirements? | Yes |
| **Certification Impact** | Does change affect certification basis or MoC? | Yes |
| **Recommended Action** | Approve, Reject, Defer | Yes (by Requirements Owner) |

---

## 5. Change Classification

### 5.1 Change Types

| Change Type | Definition | Approval Authority |
|------------|-----------|-------------------|
| **Clarification** | No functional change; improves clarity or corrects typos | Requirements Owner |
| **Addition** | New requirement added | CCB |
| **Modification** | Functional change to existing requirement | CCB |
| **Deletion** | Requirement removed (obsolete or redundant) | CCB |

### 5.2 Change Priority Levels

| Priority | Definition | Response Time |
|----------|-----------|---------------|
| **Critical** | Safety-critical or blocks program progress | Emergency CCB within 48 hours |
| **High** | Significant impact on schedule, cost, or performance | Next regular CCB meeting |
| **Medium** | Important but not urgent | Within 2 CCB meetings |
| **Low** | Minor improvement or optimization | When convenient |

### 5.3 Change Impact Categories

| Impact Category | Definition | Example |
|----------------|-----------|---------|
| **No Impact** | Clarification only; no downstream changes | Typo correction, formatting improvement |
| **Internal Impact** | Affects design, verification, or documentation only | Interface specification update, test case revision |
| **External Impact** | Affects stakeholders outside AMPEL360 | Airport infrastructure requirement change, supplier specification change |
| **Regulatory Impact** | Affects certification basis, MoC, or regulatory approvals | New safety requirement, changed compliance method |

---

## 6. Impact Assessment Process

### 6.1 Impact Assessment Checklist

For each change request, the Requirements Owner assesses impact on:

**Upstream (Sources)**:
- [ ] Does this change affect the originating system requirement, operational concept, or standard?
- [ ] Are stakeholders who provided input affected?

**Horizontal (Design)**:
- [ ] Does this change require updates to Interface Control Documents (ICDs)?
- [ ] Are design specifications or drawings affected?
- [ ] Does this change affect other infrastructure interface categories?

**Downstream (Verification)**:
- [ ] Does this change require new or modified test cases?
- [ ] Are existing verification activities invalidated?
- [ ] Does this change affect verification schedules or resources?

**Certification**:
- [ ] Does this change affect the certification basis or applicable standards?
- [ ] Does this change require a revised Means of Compliance (MoC)?
- [ ] Does this change require notification to or approval from regulatory authorities (EASA, FAA)?

**External Stakeholders**:
- [ ] Does this change affect airport infrastructure requirements?
- [ ] Does this change affect hydrogen suppliers, ground service providers, or energy system suppliers?
- [ ] Does this change require coordination with external partners?

**Safety**:
- [ ] Does this change introduce new hazards or affect existing safety assessments?
- [ ] Is this change to a safety-critical requirement?
- [ ] Does this change require safety risk assessment or hazard analysis update?

### 6.2 Traceability Impact Analysis

Using the traceability framework defined in [85-00-03-003_Requirements_Traceability_and_Mapping](./85-00-03-003_Requirements_Traceability_and_Mapping.md), identify:

- All **upstream sources** that may be affected
- All **design artifacts** (ICDs, specifications) that must be updated
- All **verification activities** (test cases, analyses) that must be re-performed
- All **certification evidence** that must be revised

**Tools**: Use automated traceability reports to identify affected artifacts.

---

## 7. Change Approval Criteria

### 7.1 Approval Considerations

The CCB evaluates each change request based on:

| Criterion | Considerations |
|-----------|---------------|
| **Technical Merit** | Is the change technically sound? Does it solve the stated problem? |
| **Safety** | Does the change maintain or improve safety? Are safety risks acceptable? |
| **Certification** | Can the change be certified? Is regulatory approval likely? |
| **Cost & Schedule** | What are the cost and schedule impacts? Are they acceptable? |
| **Stakeholder Alignment** | Are external stakeholders (airports, suppliers) willing and able to accommodate the change? |
| **Alternatives** | Have alternatives been considered? Is this the best solution? |
| **Risk** | What are the technical, programmatic, and business risks? Are they manageable? |

### 7.2 Rejection Criteria

A change request may be rejected if:

- Insufficient justification or unclear problem statement
- Introduces unacceptable safety risks
- Not feasible to certify or conflicts with certification basis
- Cost or schedule impact is prohibitive
- External stakeholders cannot accommodate the change
- Better alternative solutions exist
- Change conflicts with program objectives or strategy

---

## 8. Change Implementation

### 8.1 Implementation Steps

Once a change is **approved by the CCB**, the Requirements Owner executes the following steps:

1. **Update Requirement Documentation**:
   - Revise the affected requirement file(s)
   - Update requirement metadata (version, status, approval date)
   - Document the change in the requirement's change history

2. **Update Traceability Links**:
   - Verify and update all upstream and downstream traceability links
   - Update Requirements Traceability Matrix (RTM)
   - Update Verification Cross-Reference Matrix (VCRM)

3. **Notify Affected Teams**:
   - Design teams: Update ICDs and specifications
   - V&V teams: Update verification plans and test cases
   - Certification team: Update compliance matrices and MoCs
   - External stakeholders: Formal notification of change

4. **Update Supporting Documentation**:
   - Revise overview documents if needed
   - Update category index and taxonomy documents
   - Update ASSETS (traceability matrices, diagrams)

5. **Archive Change Request**:
   - Record CCB decision and rationale
   - Link change request to updated requirement(s)
   - Store in change request log

### 8.2 Version Control

All requirement changes are tracked in **Git version control**:

- Each change is committed with a descriptive message
- Commit message references the Change Request ID (e.g., "Update RQ-85-00-03-H2-001 per CR-85-2025-042")
- Git history provides complete audit trail of all requirement changes

### 8.3 Change Notification

Stakeholders are notified of approved changes via:

- **Internal**: Email notification, CCB meeting minutes, project status reports
- **External**: Formal change notification letters, coordination meetings, updated ICDs

---

## 9. Verification of Changed Requirements

### 9.1 Re-Verification Requirements

Changed requirements must be **re-verified** to ensure:

- The change has been correctly implemented
- The requirement still satisfies its original intent (unless intent changed)
- No unintended side effects or regressions introduced
- Traceability to verification evidence is maintained

### 9.2 Verification Status After Change

| Change Type | Verification Status After Change | Action Required |
|------------|----------------------------------|-----------------|
| **Clarification** | Verification status unchanged | Update verification documentation (if needed) |
| **Addition** | New requirement → Not Verified | New verification activities required |
| **Modification** | Verified → Not Verified | Re-verification required |
| **Deletion** | Verified → Obsolete | Archive verification evidence |

---

## 10. Emergency Changes

### 10.1 Emergency Change Criteria

An **emergency change** is required when:

- A safety-critical issue is discovered that requires immediate corrective action
- A regulatory authority issues a mandate or special condition
- A program-critical issue blocks flight test or certification
- A discovered error could lead to non-compliance or safety hazard if not corrected immediately

### 10.2 Emergency Change Process

For emergency changes:

1. **Immediate Notification**: Requirements Owner notifies CCB Chair and Chief Engineer
2. **Emergency CCB Meeting**: Convened within 48 hours (or immediately if safety-critical)
3. **Expedited Review**: Streamlined review focusing on safety and compliance
4. **Provisional Approval**: CCB may grant provisional approval pending full impact assessment
5. **Formal Approval**: Full CCB review within 2 weeks to confirm provisional decision
6. **Notification**: External stakeholders notified immediately

---

## 11. Baseline Management

### 11.1 Requirement Baselines

Infrastructure interface requirements are **baselined** at key program milestones:

| Baseline | Milestone | Requirements Status | Change Authority |
|----------|-----------|---------------------|------------------|
| **Preliminary Baseline** | Conceptual Design Review (CDR) | Draft requirements approved for design | CCB |
| **Allocated Baseline** | Preliminary Design Review (PDR) | Requirements allocated to subsystems | CCB |
| **Functional Baseline** | Critical Design Review (CDR) | Requirements frozen for implementation | CCB + Chief Engineer |
| **Product Baseline** | Type Certificate Issuance | Requirements certified and released | CCB + Regulatory Authority |

### 11.2 Baseline Change Control

Changes to **baselined requirements** are subject to stricter control:

- **Pre-Baseline**: Changes approved by Requirements Owner or Systems Engineering Lead
- **Post-Baseline**: All changes require CCB approval
- **Post-Certification**: Changes require CCB approval + regulatory authority notification/approval

---

## 12. Change Metrics and Reporting

### 12.1 Change Metrics

The following metrics are tracked and reported:

| Metric | Definition | Target |
|--------|-----------|--------|
| **Change Request Rate** | Number of CRs submitted per month | Decreasing trend over time |
| **Change Approval Rate** | % of CRs approved by CCB | ≥ 70% (indicates good quality CRs) |
| **Average CR Cycle Time** | Days from submission to closure | ≤ 30 days (non-emergency) |
| **Emergency Change Rate** | % of CRs classified as emergency | ≤ 5% (indicates mature requirements) |
| **Stakeholder Impact Rate** | % of CRs affecting external stakeholders | Monitored for stakeholder communication |

### 12.2 Change Reporting

Change management reports are provided:

| Report | Frequency | Audience |
|--------|-----------|----------|
| **CCB Meeting Minutes** | After each CCB meeting | All stakeholders |
| **Change Request Log** | Ongoing (living document) | Requirements team, PM |
| **Change Metrics Dashboard** | Monthly | PM, Chief Engineer, Leadership |
| **Stakeholder Change Summary** | Quarterly | External stakeholders (airports, suppliers) |

---

## 13. Integration with ATA 95 (Digital Product Passport)

Requirement changes are recorded in the **Digital Product Passport (DPP)** system under [ATA Chapter 95](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/):

### 13.1 DPP Change Tracking

Each requirement change is logged in the DPP with:

- Requirement ID and title
- Change Request ID
- Change date and author
- Change type and justification
- CCB decision and approval date
- Impact summary (design, verification, certification)

### 13.2 Configuration Management via DPP

The DPP provides:

- **Version History**: Complete history of all requirement changes
- **Traceability**: Links to affected design, test, and certification artifacts
- **Audit Trail**: Immutable record of who changed what and when
- **Compliance Tracking**: Status of certification evidence after changes

---

## 14. Related Documents

- [85-00-03-001_Infrastructure_Interface_Requirements_Overview](./85-00-03-001_Infrastructure_Interface_Requirements_Overview.md) — High-level overview
- [85-00-03-002_Requirements_Categories_and_Taxonomy](./85-00-03-002_Requirements_Categories_and_Taxonomy.md) — Requirements taxonomy
- [85-00-03-003_Requirements_Traceability_and_Mapping](./85-00-03-003_Requirements_Traceability_and_Mapping.md) — Traceability framework
- [ASSETS/85-00-03-A-001_Requirements_Traceability_Matrix.xlsx](./ASSETS/85-00-03-A-001_Requirements_Traceability_Matrix.xlsx) — RTM (includes change tracking)
- [95-00-03_Requirements](../../../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/95-00_GENERAL/95-00-03_Requirements/) — DPP Requirements (for integration reference)

---

## Document Control

- **Document ID**: 85-00-03-004
- **Version**: 1.0
- **Status**: DRAFT — Subject to human review and approval
- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-21
- **Classification**: Internal Use
- **Owner**: AMPEL360 Configuration Control Board (CCB) & Requirements WG

---

**For questions or to submit a change request, contact: requirements@ampel360.aero**
