# Configuration Management Plan

**Document ID:** CM-PLAN-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## 1. Introduction

### 1.1 Purpose

This Configuration Management Plan (CMP) establishes the policies, procedures, and responsibilities for managing configuration changes to the AMPEL360 BWB H₂ Hy-E operational equipment and systems under ATA 02-00-00 GENERAL.

### 1.2 Scope

This plan applies to all:
- Operations equipment (H₂ refueling, GSE, emergency)
- CAOS system components (hardware and software)
- Documentation systems (EFB, publications)
- Training equipment (simulators, training devices)
- Associated documentation and data

### 1.3 Objectives

- Maintain accurate configuration baselines
- Control changes systematically
- Ensure traceability throughout lifecycle
- Support certification and compliance
- Enable effective communication of changes

## 2. Configuration Management Organization

### 2.1 Roles and Responsibilities

**Configuration Control Board (CCB)**
- **Chair:** Chief Engineer
- **Members:** Systems Engineering Lead, Quality Manager, Certification Manager, Operations Manager
- **Responsibilities:**
  - Review and approve Engineering Change Orders (ECOs)
  - Resolve configuration conflicts
  - Approve deviations and waivers
  - Review configuration audits
- **Meetings:** Weekly (or as needed for urgent changes)

**Configuration Manager**
- Maintain Master Part Number Registry
- Process ECOs and track status
- Manage configuration baselines
- Conduct configuration audits
- Generate configuration reports

**Engineering Change Coordinator**
- Facilitate ECO process
- Coordinate impact assessments
- Support CCB meetings
- Communicate decisions

**Data Management Team**
- Maintain PLM/PDM systems
- Manage document repositories
- Archive configuration data
- Support configuration queries

### 2.2 Configuration Management Tools

**Primary Systems:**
- **PLM System:** Siemens Teamcenter (product data management)
- **ERP System:** SAP S/4HANA (material master, BOM)
- **Version Control:** Git (documentation, software)
- **ECO System:** Jira with custom workflows
- **CSDB:** S1000D-compliant database

## 3. Configuration Identification

### 3.1 Configuration Items (CIs)

Configuration items are identified using the Part Number Reference (PNR) system:

| CI Level | Description | Example |
|----------|-------------|---------|
| **Level 1** | System | ATA 02-00-00 GENERAL |
| **Level 2** | Subsystem | H₂ Refueling Equipment (02-32) |
| **Level 3** | Assembly | Refueling Panel Assembly (PNR-02-32-001) |
| **Level 4** | Component | Panel Door (PNR-02-32-001-01) |
| **Level 5** | Part | Door Hinge (PNR-02-32-001-01A) |

### 3.2 Configuration Baselines

**Functional Baseline**
- Established at: Requirements Review
- Contents: System requirements, functional specifications
- Approval: Chief Engineer
- Document: Requirements Specification Document (RSD)

**Allocated Baseline**
- Established at: Preliminary Design Review (PDR)
- Contents: Design requirements allocated to subsystems
- Approval: Systems Engineering Lead
- Document: System Design Description (SDD)

**Product Baseline**
- Established at: Critical Design Review (CDR)
- Contents: Detailed design, drawings, specifications
- Approval: Configuration Control Board
- Documents: Engineering drawings, part specifications, BOM

**Operational Baseline**
- Established at: Type Certification
- Contents: As-built configuration, operational procedures
- Approval: Certification Manager
- Documents: Type Certificate Data Sheet (TCDS), Maintenance Manual

### 3.3 Baseline Documentation

Each baseline includes:
- Part numbers and descriptions
- Engineering drawings (PDF/A format)
- Specifications and standards
- Test reports and certification data
- Supplier data and CAGE codes
- Interchangeability data
- Spares recommendations

## 4. Configuration Control

### 4.1 Engineering Change Order (ECO) Process

**ECO Workflow:**
```
[Initiate ECO] → [Impact Assessment] → [CCB Review] → [Approval/Reject]
       │                                     │
       └──────────────────────────────────→ [Implement] → [Verify] → [Close]
```

**ECO Types:**

| Type | Description | Approval Level | Processing Time |
|------|-------------|---------------|-----------------|
| **Class 1** | Safety-critical, airworthiness | CCB + Certification | 5-10 days |
| **Class 2** | Performance, major cost impact | CCB | 3-5 days |
| **Class 3** | Minor improvements, clarifications | Configuration Manager | 1-2 days |
| **Urgent** | Fleet safety, grounding issue | Emergency CCB | <24 hours |

**ECO Numbering:**
- Format: `ECO-YY-NNN`
- YY = Year (25 for 2025)
- NNN = Sequential number (001-999)
- Example: ECO-25-042

**ECO Contents:**
- Change description and justification
- Affected part numbers and documents
- Technical impact assessment
- Cost and schedule impact
- Certification impact (if applicable)
- Implementation plan
- Verification criteria

### 4.2 Deviation and Waiver Process

**Deviation:** Authorization to depart from requirements before production  
**Waiver:** Authorization to accept product that doesn't meet requirements

**Process:**
1. Request submitted with justification
2. Engineering evaluates acceptability
3. Quality assesses risk
4. CCB approves or rejects
5. If approved, deviation/waiver number assigned
6. Tracked until closure

**Numbering:**
- Deviation: `DEV-YY-NNN`
- Waiver: `WAV-YY-NNN`

**Tracking:**
- All deviations/waivers logged in Deviation_Log.csv
- Quarterly review for closure
- Annual summary report to management

### 4.3 Supersession Management

**Process:**
When a part is superseded:
1. New part number assigned (or revision suffix)
2. Interchangeability type determined:
   - Direct replacement (no changes needed)
   - Form-fit-function (minor procedure updates)
   - Conditional (requires modifications)
3. Cross-reference added to Interchangeability_Matrix.csv
4. Old part status changed to "Superseded"
5. Superseded_By field populated with new PNR
6. Effectivity specified (date, serial number, or both)

**Example:**
```
Old: PNR-02-EFB-001 (Superseded)
New: PNR-02-EFB-001B (Active)
Type: Form-Fit-Function
Effectivity: S/N 101 and subsequent, or after 2026-01-01
```

## 5. Configuration Status Accounting

### 5.1 Configuration Data Repository

**Master Part Number Registry**
- Location: Master_Part_Number_Registry.csv (PLM system is system of record)
- Update frequency: Real-time (on ECO closure)
- Backup: Daily automated backup
- Access: Read (all), Write (Configuration Manager only)

**Configuration Reports:**

| Report | Frequency | Distribution |
|--------|-----------|--------------|
| Part Status Report | Weekly | Engineering, Procurement |
| ECO Status Report | Weekly | CCB members |
| Baseline Comparison | Monthly | Systems Engineering |
| As-Built Configuration | Per aircraft | Maintenance, Operators |
| Obsolescence Report | Quarterly | Supply Chain, Engineering |

### 5.2 Traceability

**Upward Traceability:**
- Part → Assembly → Subsystem → System → Aircraft
- Supported by Component_Breakdown_Structure.md
- Automated BOM explosion in PLM system

**Downward Traceability:**
- Requirement → Design → Part → Serial Number
- Requirement IDs linked to part numbers
- Serial number tracking in As_Built_Configuration/

**Horizontal Traceability:**
- Part → Drawing → Specification → Test Report → Certification
- Document links maintained in PLM metadata

### 5.3 Effectivity Management

**Types of Effectivity:**
1. **Date Effectivity:** Change effective after specific date
2. **Serial Number Effectivity:** Change effective starting at S/N
3. **Flight Hour Effectivity:** Change at next scheduled maintenance after XXX FH
4. **Retrofit:** Change applied to existing units

**Effectivity Matrix:**
- Stored in: As_Built_Configuration/Effectivity_Matrix.csv
- Tracks which configuration is installed on which aircraft
- Updated at each maintenance event
- Critical for airworthiness directives (ADs)

## 6. Configuration Audits

### 6.1 Audit Types

**Physical Configuration Audit (PCA)**
- **Purpose:** Verify as-built matches design
- **Frequency:** At major milestones (first article, type certification)
- **Scope:** Physical inspection of all configuration items
- **Outcome:** PCA report, discrepancy list, corrective actions

**Functional Configuration Audit (FCA)**
- **Purpose:** Verify product meets requirements
- **Frequency:** At completion of qualification testing
- **Scope:** All performance tests, environmental tests
- **Outcome:** FCA report, test evidence, compliance matrix

**Configuration Management Audit**
- **Purpose:** Verify CM processes are followed
- **Frequency:** Semi-annual
- **Scope:** ECO process, documentation, traceability
- **Outcome:** Audit findings, improvement actions

### 6.2 Audit Procedures

1. **Audit Planning**
   - Define scope and objectives
   - Assemble audit team
   - Schedule with stakeholders
   - Prepare checklists

2. **Audit Execution**
   - Review documentation
   - Interview personnel
   - Inspect physical items
   - Verify data accuracy

3. **Audit Reporting**
   - Document findings
   - Classify by severity (critical, major, minor, observation)
   - Recommend corrective actions
   - Present to management

4. **Corrective Actions**
   - Assign ownership
   - Set due dates
   - Track to closure
   - Verify effectiveness

## 7. Interface Management

### 7.1 Internal Interfaces

Configuration management interfaces with:
- **Engineering:** Design changes, drawing release
- **Quality:** Nonconformances, corrective actions
- **Manufacturing:** As-built data, process changes
- **Procurement:** Supplier changes, part sourcing
- **Maintenance:** Modification instructions, service bulletins
- **Certification:** Compliance documentation, approvals

### 7.2 External Interfaces

Configuration data exchanged with:
- **Suppliers:** Part specifications, change notifications
- **Customers:** Configuration of delivered aircraft
- **Regulatory Authorities:** Type design, amendments
- **Maintenance Organizations:** Effectivity, procedures

### 7.3 Data Exchange Standards

- **STEP AP242:** 3D CAD data exchange
- **S1000D:** Technical publication data
- **ATA Spec 2300:** Electronic transfer of maintenance data
- **JASC Codes:** Part identification in maintenance systems

## 8. Training and Competency

### 8.1 Training Requirements

| Role | Initial Training | Recertification | Content |
|------|-----------------|-----------------|---------|
| Configuration Manager | 40 hours | Annual | CM processes, tools, standards |
| Engineers | 8 hours | Biennial | ECO process, PNR system |
| Procurement | 4 hours | Biennial | Part status, sourcing |
| Quality Auditors | 16 hours | Annual | CM audits, standards |

### 8.2 Competency Assessment

- Written exam (80% passing score)
- Practical exercise (ECO processing)
- Audit observation (for auditors)
- Annual performance review

## 9. Metrics and KPIs

### 9.1 Process Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| ECO Processing Time (Class 3) | <2 days | Average days from submission to closure |
| ECO Approval Rate (first submission) | >90% | Approved / Total submitted |
| Configuration Accuracy | >99.5% | Audit findings / Total items |
| Baseline Deviation Rate | <1% | Unauthorized changes / Total items |
| Data Quality (completeness) | >95% | Required fields populated |

### 9.2 Performance Reporting

- Monthly metrics dashboard
- Quarterly trend analysis
- Annual management review
- Continuous improvement initiatives

## 10. Tools and Systems

### 10.1 Software Tools

| Tool | Purpose | Users |
|------|---------|-------|
| Siemens Teamcenter | PLM/PDM | Engineering, Quality, Procurement |
| SAP S/4HANA | ERP, BOM | Manufacturing, Supply Chain |
| Jira | ECO workflow | All engineering |
| Git/GitHub | Version control | Documentation, Software |
| S1000D CSDB | Tech pubs | Publications, Maintenance |

### 10.2 System Integration

- Teamcenter ↔ SAP: BOM synchronization (daily)
- Jira ↔ Teamcenter: ECO data (real-time)
- Git ↔ Teamcenter: Document links (on commit)
- CSDB ↔ Teamcenter: Part data (on demand)

## 11. Records Management

### 11.1 Record Types

| Record Type | Retention Period | Storage Location |
|------------|------------------|------------------|
| ECOs | Life of aircraft + 10 years | PLM system + archive |
| Configuration Baselines | Permanent | PLM system + archive |
| Audit Reports | 10 years | Quality system |
| Part Specifications | Life of part type + 10 years | PLM system |
| As-Built Configs | Life of aircraft + 10 years | Aircraft records |

### 11.2 Archive and Retrieval

- Electronic records: PLM system (primary), offsite backup (secondary)
- Critical records: PDF/A format for long-term preservation
- Retrieval SLA: <24 hours for any record
- Annual archive audit for completeness

## 12. Compliance and Standards

### 12.1 Applicable Standards

- **ISO 10007:2017:** Configuration management guidelines
- **EIA-649-B:** Configuration management standard
- **GEIA-HB-649:** Configuration management handbook
- **EASA Part-21:** Design organization requirements
- **AS9100D:** Aerospace quality management (clause 8.3.6)

### 12.2 Regulatory Compliance

- EASA type design change approval process
- FAA equivalency compliance
- Export control (ITAR, EAR) for configuration data
- Cybersecurity requirements (DO-326A) for software

## 13. Continuous Improvement

### 13.1 Improvement Initiatives

- Quarterly process review (CCB)
- User feedback collection (surveys)
- Benchmarking (industry best practices)
- Technology updates (tools, automation)

### 13.2 Lessons Learned

- Capture lessons from each major milestone
- Share across organization (knowledge base)
- Incorporate into process updates
- Annual lessons learned report

## 14. Related Documents

- Part_Number_Management_System.md
- Component_Breakdown_Structure.md
- Master_Part_Number_Registry.csv
- Engineering_Change_Orders/ECO_Log.csv
- As_Built_Configuration/Configuration_Baselines.csv

---

**Document Control:**
- **Version:** 1.0
- **Status:** Active
- **Approved By:** Chief Engineer & Quality Manager
- **Next Review Date:** 2026-05-05
- **Owner:** Configuration Management
