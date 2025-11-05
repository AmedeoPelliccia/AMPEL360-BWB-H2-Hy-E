# ATA 02 - Operations Information
## Revision Control Procedures

**Document ID:** AMPEL360-02-00-00-OVR-RC  
**Version:** 1.0.0  
**Date:** 2025-11-04  
**Classification:** Operations Critical

---

## 1. PURPOSE

This document establishes procedures for managing revisions to AMPEL360 operational documentation, ensuring controlled, traceable, and effective change management.

**Related Documents:**
- [Document_Conventions.md](Document_Conventions.md) - Formatting and revision marking standards
- [Document_Organization.md](Document_Organization.md) - Overall documentation structure

---

## 2. VERSION NUMBERING

### 2.1 Version Format

**Format:** `Major.Minor.Patch` (e.g., 1.0.0)

### 2.2 Version Increments

**Major Version (X.0.0):**
- Significant operational changes
- New systems or procedures
- Regulatory requirement changes
- Structural reorganization
- **Requires:** Training for affected personnel

**Minor Version (X.Y.0):**
- Improvements and enhancements
- Clarifications and additional detail
- Non-critical procedure changes
- Additional data or examples
- **Requires:** Briefing recommended

**Patch Version (X.Y.Z):**
- Corrections and typos
- Formatting improvements
- Minor clarifications
- Cross-reference updates
- **Requires:** Information only

### 2.3 Version Examples

```
1.0.0 → Initial release
1.0.1 → Typo corrections
1.1.0 → Added winter operations data
1.2.0 → Enhanced CAOS procedures
2.0.0 → New H2 emergency procedures (major change)
```

---

## 3. REVISION PROCESS

### 3.1 Process Flow

```
Step 1: IDENTIFY NEED FOR CHANGE
    ↓
Step 2: SUBMIT CHANGE REQUEST
    ↓
Step 3: EVALUATE CHANGE
    ↓
Step 4: APPROVE/REJECT
    ↓
Step 5: DRAFT REVISION
    ↓
Step 6: TECHNICAL REVIEW
    ↓
Step 7: OPERATIONAL REVIEW
    ↓
Step 8: SAFETY REVIEW
    ↓
Step 9: REGULATORY REVIEW (if required)
    ↓
Step 10: FINAL APPROVAL
    ↓
Step 11: CONFIGURATION CONTROL BOARD
    ↓
Step 12: RELEASE
    ↓
Step 13: DISTRIBUTION & NOTIFICATION
    ↓
Step 14: TRAINING (if required)
    ↓
Step 15: EFFECTIVENESS MONITORING
```

### 3.2 Timeline Targets

| Change Type | Target Timeline |
|-------------|-----------------|
| Patch | 7-14 days |
| Minor | 30-60 days |
| Major | 60-90 days |
| Safety-Critical | 7-14 days (expedited) |
| Emergency | 24-48 hours (urgent) |

---

## 4. CHANGE REQUEST

### 4.1 Who Can Submit

- Flight crew
- Cabin crew
- Dispatch
- Ground operations
- Maintenance
- Training
- Management
- Regulatory authorities
- CAOS anomaly detection

### 4.2 Submission Method

**Online Form:** docs.ampel360.aero/change-request  
**Email:** doc-changes@ampel360.aero  
**Phone:** +34 91 XXX XXXX (urgent only)

### 4.3 Required Information

- Document ID and current version
- Section affected
- Description of issue or proposed change
- Rationale/justification
- Safety impact (if any)
- Operational impact
- Proposed solution (if known)
- Submitter contact information

### 4.4 Change Request Example

```
CHANGE REQUEST CR-02-2025-045

Document: AMPEL360-02-32-03-PRO-001
Version: 1.2.0
Section: 3.4 H2 Pressure Monitoring

Issue: Pressure monitoring step ambiguous regarding 
       which gauge to monitor (tank vs line pressure)

Rationale: Two refueling crews interpreted differently,
           causing delay and confusion

Safety Impact: Low (procedural clarity)

Proposed Fix: Add specific gauge reference: 
              "Monitor TANK PRESSURE gauge on panel P5"

Submitted by: John Smith, Ground Operations Supervisor
Date: 2025-11-04
```

---

## 5. CHANGE EVALUATION

### 5.1 Evaluation Criteria

- **Safety:** Impact on flight safety
- **Operational:** Impact on operations
- **Regulatory:** Compliance requirements
- **Technical:** Technical accuracy
- **Training:** Training requirements
- **Cost:** Implementation cost
- **Schedule:** Implementation timeline

### 5.2 Priority Assignment

**Priority 1 (Urgent):**
- Safety-critical
- Regulatory mandate
- Operational show-stopper
- Timeline: 24-48 hours

**Priority 2 (High):**
- Significant safety improvement
- Major operational improvement
- Regulatory recommendation
- Timeline: 7-14 days

**Priority 3 (Normal):**
- Operational enhancement
- Clarification needed
- User feedback
- Timeline: 30-60 days

**Priority 4 (Low):**
- Minor improvement
- Cosmetic change
- Nice-to-have
- Timeline: Next scheduled update

---

## 6. REVIEW PROCESS

### 6.1 Technical Review

**Reviewer:** Subject Matter Expert (SME)  
**Focus:** Technical accuracy, completeness  
**Deliverable:** Technical review sign-off

**Checklist:**
- [ ] Technically accurate
- [ ] Consistent with system design
- [ ] Data verified
- [ ] References correct
- [ ] Calculations checked

### 6.2 Operational Review

**Reviewer:** Check Pilot or Operations Manager  
**Focus:** Operational practicality, safety  
**Deliverable:** Operational review sign-off

**Checklist:**
- [ ] Operationally practical
- [ ] Clear and understandable
- [ ] Follows standard procedures
- [ ] Safe to implement
- [ ] Crew workload acceptable

### 6.3 Safety Review

**Reviewer:** Safety Manager  
**Focus:** Safety impact assessment  
**Deliverable:** Safety assessment report

**Checklist:**
- [ ] Safety impact assessed
- [ ] Hazards identified and mitigated
- [ ] Complies with SMS
- [ ] Risk acceptable
- [ ] Safety reporting considered

### 6.4 Regulatory Review (if required)

**When Required:**
- Changes to AFM
- Changes to MEL
- Changes to approved procedures
- New operational capabilities

**Authority:** EASA/FAA or delegated representative  
**Deliverable:** Regulatory approval letter

---

## 7. APPROVAL AUTHORITY

### 7.1 Approval Levels

| Change Type | Approver |
|-------------|----------|
| Patch (X.Y.Z) | Technical Publications Manager |
| Minor (X.Y.0) | Operations Manager |
| Major (X.0.0) | Chief Pilot + Operations Manager |
| Safety-Critical | Safety Manager + Chief Pilot |
| Regulatory | Regulatory Affairs + Authority |

### 7.2 Configuration Control Board (CCB)

**Membership:**
- Chief Pilot (Chair)
- Operations Manager
- Safety Manager
- Technical Publications Manager
- Regulatory Affairs Representative

**Meetings:** Monthly (routine), ad-hoc (urgent)

**Responsibilities:**
- Final approval of major changes
- Coordinate related changes
- Ensure consistency across documents
- Manage version control
- Authorize release

---

## 8. DOCUMENTATION OF CHANGES

### 8.1 Revision Log

**Location:** At end of document or separate file

**Format:**
```
| Version | Date | Description | Author | Approver |
|---------|------|-------------|--------|----------|
| 1.0.0 | 2025-01-01 | Initial release | J. Smith | M. Jones |
| 1.0.1 | 2025-02-15 | Typo corrections | J. Smith | T. Pubs Mgr |
| 1.1.0 | 2025-06-01 | Added winter ops | K. Brown | Ops Mgr |
```

### 8.2 Change Summary

**For each version, include:**
- Version number
- Effective date
- Supersedes statement
- List of changes (by section)
- Reason for change
- Impact assessment

**Example:**
```
VERSION 1.1.0 - CHANGE SUMMARY

Effective Date: 2025-06-01
Supersedes: Version 1.0.1 dated 2025-02-15

Changes:
1. Section 3.2: Added cold weather H2 refueling procedures
2. Section 4.5: Enhanced leak detection monitoring
3. Section 7.1: Updated emergency defueling procedure

Reason: Operational experience from first winter season
Impact: Training required for ground operations personnel
```

---

## 9. REVISION MARKING

### 9.1 Visual Indicators

**Black Triangle (▶):** New or changed content

**Placement:**
- Left margin of changed paragraphs
- Before/after inline changes
- On changed figures/tables

**Example:**
```
▶ 3.2 Cold Weather Refueling

▶ When ambient temperature is below -10°C:
  1. Pre-heat refueling equipment ▶ per manufacturer instructions ◀
  2. Monitor for ice formation
  ▶ 3. Increase monitoring frequency to every 5 minutes ◀
```

### 9.2 Revision Bars

**Alternative:** Vertical bar in margin

```
| This entire paragraph has been revised to include
| new procedures for cold weather operations. The
| change includes enhanced monitoring requirements.
```

### 9.3 Color Coding (Electronic Only)

- **Green highlight:** New content
- **Yellow highlight:** Changed content
- **Red strikethrough:** Deleted content (shown in draft)

---

## 10. TEMPORARY REVISIONS

### 10.1 When to Issue

- Urgent operational change needed
- Permanent revision in progress
- Trial procedure implementation
- Immediate safety improvement

### 10.2 Temporary Revision Format

**Header:**
```
TEMPORARY REVISION TR-02-2025-012

Document: AMPEL360-02-32-03-PRO-001
Version: 1.2.0
Effective: 2025-11-04
Expires: 2026-02-04 (90 days maximum)
Status: TEMPORARY - Must be incorporated or withdrawn
```

### 10.3 Limitations

- **Maximum Duration:** 90 days
- **Action Required:** Incorporate into permanent revision or withdraw
- **Tracking:** All temporary revisions tracked by CCB
- **Notification:** All affected personnel notified

### 10.4 Incorporation

**Before Expiration:**
- Evaluate effectiveness
- Incorporate into permanent revision, OR
- Withdraw if ineffective
- Update training materials
- Close temporary revision

---

## 11. DISTRIBUTION AND NOTIFICATION

### 11.1 Distribution Methods

**Electronic:**
- EFB automatic update
- Web portal update
- Email notification
- CAOS system message

**Paper:**
- Controlled distribution to holders
- Replacement of superseded pages
- Acknowledgment of receipt

### 11.2 Notification Content

**Email Template:**
```
Subject: ATA 02 Document Revision - [Document ID] v[X.Y.Z]

Document: [Title]
Document ID: [AMPEL360-XX-YY-ZZ-AAA]
New Version: [X.Y.Z]
Previous Version: [X.Y.Z]
Effective Date: [YYYY-MM-DD]

Change Summary:
- [Brief description of changes]

Impact:
- [Training required / Briefing recommended / Information only]

Action Required:
- [Specific actions for personnel]

Access: docs.ampel360.aero or EFB automatic update

Questions: tech-pubs@ampel360.aero or +34 91 XXX XXXX
```

### 11.3 Acknowledgment

**Required for:**
- Major revisions
- Safety-critical changes
- Procedure changes

**Method:**
- Electronic acknowledgment in portal
- Signed paper form
- Training completion certificate

---

## 12. TRAINING REQUIREMENTS

### 12.1 Training Triggers

| Change Type | Training Required |
|-------------|-------------------|
| Major (X.0.0) | Yes - Formal training |
| Minor (X.Y.0) | Maybe - Briefing recommended |
| Patch (X.Y.Z) | No - Information only |
| Safety-Critical | Yes - Immediate briefing |

### 12.2 Training Methods

**Formal Training:**
- Classroom session
- Simulator session
- CBT module
- Assessment required

**Briefing:**
- Email briefing
- Crew briefing
- Self-study
- No assessment

**Information:**
- Email notification
- Document available
- Self-review

### 12.3 Training Records

**Maintain:**
- Who trained
- What version
- When trained
- Assessment results (if applicable)
- Training effectiveness

---

## 13. EFFECTIVENESS MONITORING

### 13.1 Monitoring Methods

- User feedback surveys
- Incident/error reports
- CAOS anomaly detection
- Operational audits
- Safety reviews

### 13.2 Success Criteria

- Reduction in errors/confusion
- Positive user feedback
- No safety incidents related to change
- Operational improvement achieved
- Regulatory compliance maintained

### 13.3 Continuous Improvement

**Feedback Loop:**
```
Release Change
    ↓
Monitor Effectiveness
    ↓
Collect Feedback
    ↓
Analyze Data
    ↓
Identify Improvements
    ↓
Submit New Change Request
    ↓
(Repeat Process)
```

---

## 14. ARCHIVE AND RECORDS

### 14.1 Document Retention

**Active Documents:**
- Current version: Indefinite
- Immediate predecessor: 5 years

**Superseded Documents:**
- Retention period: 10 years minimum
- Accessible for historical reference
- Not for operational use (clearly marked)

### 14.2 Change Records

**Retain Permanently:**
- Change requests
- Review records
- Approval records
- Effectiveness reports
- Training records

### 14.3 Archive System

**Electronic Archive:**
- Version control system (Git)
- Document management system
- Backup and recovery
- Audit trail maintained

---

## 15. SPECIAL PROCEDURES

### 15.1 Emergency Changes

**When Required:**
- Immediate safety threat
- Regulatory mandate (AD)
- Critical operational issue

**Process:**
1. Identify emergency
2. Draft change immediately
3. Expedited review (SME + Safety + Chief Pilot)
4. Emergency CCB approval (phone/email)
5. Immediate release
6. Notification within 4 hours
7. Full review within 30 days

**Timeline:** 24-48 hours maximum

### 15.2 Regulatory-Mandated Changes

**Process:**
- Review regulatory requirement
- Assess impact
- Draft compliance change
- Expedited review
- Submit to authority (if required)
- Implement upon approval

**Timeline:** Per regulatory requirement

---

## 16. ROLES AND RESPONSIBILITIES

### 16.1 Key Roles

**Technical Publications Manager:**
- Manage revision process
- Coordinate reviews
- Maintain version control
- Ensure quality

**Operations Manager:**
- Approve operational changes
- Assess operational impact
- Ensure crew notification

**Chief Pilot:**
- Final approval authority
- Safety oversight
- Training coordination

**Safety Manager:**
- Safety impact assessment
- Risk evaluation
- SMS integration

**Configuration Manager:**
- CCB coordination
- Version synchronization
- Archive management

### 16.2 Contact Information

**Technical Publications:**
- Email: tech-pubs@ampel360.aero
- Phone: +34 91 XXX XXXX (24/7)

**Configuration Control:**
- Email: config-control@ampel360.aero
- Phone: +34 91 XXX XXXX (office hours)

**Change Requests:**
- Email: doc-changes@ampel360.aero
- Online: docs.ampel360.aero/change-request

---

**Document Status:** ✅ RELEASED
**Effective Date:** 2029-01-01
**Next Review:** 2026-11-04
**Configuration Control:** Git SHA-256: [hash]
