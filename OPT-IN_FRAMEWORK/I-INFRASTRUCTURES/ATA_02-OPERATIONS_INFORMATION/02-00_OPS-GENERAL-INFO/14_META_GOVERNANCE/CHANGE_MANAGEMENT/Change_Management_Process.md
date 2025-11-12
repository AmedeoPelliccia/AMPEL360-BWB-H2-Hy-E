# Change Management Process

**Document ID:** AMPEL360-02-00-00-META-CMP  
**Version:** 1.0.0  
**Effective Date:** 2025-09-01

## Purpose

This document establishes the change management process for all ATA 02-00-00 documentation to ensure controlled, traceable, and approved modifications.

## Scope

All baselined documentation requires formal change management through this process.

## Change Classification

| Class | Impact Level | Examples | Approval |
|-------|-------------|----------|----------|
| **Class A (Critical)** | Safety, regulatory, certification | H₂ safety procedures, regulatory requirements | CCB mandatory |
| **Class B (Major)** | System interfaces, procedures | CAOS integration, procedure updates | CCB mandatory |
| **Class C (Minor)** | Editorial, formatting | Typos, formatting, clarifications | Document Control |

## Change Request (CR) Process

### Step 1: Initiate Change Request

**Who can initiate**: Any personnel
**How**: Complete Change_Request_Template.md
**Submit to**: Documentation Manager

**Required Information**:
- Proposed change description
- Justification/rationale
- Affected documents
- Classification (A/B/C)
- Requested implementation date

### Step 2: Initial Review

**Owner**: Documentation Manager
**Timeline**: 2 business days

**Activities**:
- Verify CR completeness
- Assign CR number
- Classify change (confirm/adjust)
- Route for impact assessment

### Step 3: Impact Assessment

**Owner**: Document Owner + relevant SMEs
**Timeline**: 5 business days
**Tool**: Change_Impact_Assessment_Template.md

**Assess**:
- Technical impact
- Safety impact
- Interface changes
- Traceability updates needed
- Resource requirements
- Implementation timeline

### Step 4: CCB Review (Class A & B only)

**When**: At scheduled CCB meeting (bi-weekly)
**Who attends**: CCB members
**Timeline**: 1 business day for decision documentation

**CCB Reviews**:
- Change Request
- Impact Assessment
- Recommendations

**CCB Decisions**:
- **Approved**: Proceed to implementation
- **Approved with Modifications**: Revise and re-submit
- **Deferred**: Needs more analysis or later timing
- **Rejected**: Change not approved

**Vote**: Simple majority of voting members

### Step 5: Implementation

**Owner**: Assigned implementer (often original requestor)
**Timeline**: Per approved schedule

**Activities**:
1. Make changes to documents
2. Update traceability
3. Update affected interfaces
4. Verify completeness
5. Submit for review

### Step 6: Verification

**Owner**: Quality/Document Control
**Timeline**: 2 business days

**Verify**:
- All approved changes implemented
- No unauthorized changes
- Traceability updated
- Version numbers correct
- Metadata complete

### Step 7: Approval and Release

**Owner**: Approval Authority
**Timeline**: 3 business days

**Activities**:
- Final review
- Approve new version
- Release to repository
- Notify stakeholders
- Close CR

### Step 8: Post-Implementation Review

**Owner**: CCB (for Class A & B)
**Timeline**: 30 days after implementation

**Review**:
- Was change effective?
- Any issues discovered?
- Lessons learned

## Change Request Numbering

Format: **CR-ATA-SECTION-SEQUENCE**

Example: `CR-02-00-001`

Assigned by Documentation Manager upon initial review.

## Change Tracking

All changes tracked in:
- **Active_Changes_Log.csv**: Changes in progress
- **Approved_Changes_Log.csv**: Completed changes
- **Changes_to_Documents.csv** (in TRACEABILITY/): Full change history

## Emergency Changes

For critical safety or operational issues:

1. **Identify**: Critical issue requiring immediate fix
2. **Notify**: CCB Chair and Safety Manager immediately
3. **Assess**: Rapid impact assessment (1-4 hours)
4. **Approve**: Emergency CCB meeting (24-hour notice) or Chair approval
5. **Implement**: Immediate implementation
6. **Document**: Full CR documentation completed within 5 days
7. **Review**: Post-implementation review mandatory

## Quality Gates

Before CCB review (Class A & B):
- ✅ Impact assessment complete
- ✅ Technical review completed
- ✅ Safety review (if safety-related)
- ✅ Resource availability confirmed
- ✅ Implementation plan defined

Before release:
- ✅ All approved changes implemented
- ✅ Verification passed
- ✅ Traceability updated
- ✅ Approval obtained
- ✅ Stakeholders notified

## Metrics

Track:
- Number of CRs by class
- CR cycle time (submission to closure)
- CCB approval rate
- Implementation timeline adherence
- Post-implementation issues

Target: 
- Class A/B: ≤30 days
- Class C: ≤14 days

## References

- Configuration Control Board Charter
- Change_Request_Template.md
- Change_Impact_Assessment_Template.md

---

**Document Control:**
- Document ID: AMPEL360-02-00-00-META-CMP
- Version: 1.0.0
- Status: Released
- Owner: Documentation Manager
