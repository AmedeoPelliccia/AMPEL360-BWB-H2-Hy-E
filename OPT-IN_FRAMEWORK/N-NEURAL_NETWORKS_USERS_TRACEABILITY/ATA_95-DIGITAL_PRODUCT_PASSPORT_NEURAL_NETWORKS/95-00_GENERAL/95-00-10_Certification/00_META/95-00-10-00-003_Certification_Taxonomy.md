# 95-00-10-00-003 Certification Taxonomy

## Document Information
- **Document ID**: 95-00-10-00-003
- **Title**: Certification Taxonomy
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Purpose

This document establishes a comprehensive taxonomy for organizing and categorizing all certification-related artifacts, evidence, and documentation for the AMPEL360 BWB H₂ Hy-E Q100 aircraft program. The taxonomy ensures consistent naming, classification, and retrieval of certification materials throughout the lifecycle.

## Taxonomy Dimensions

The certification taxonomy is organized along five primary dimensions:

### 1. Lifecycle Phase Dimension
- **00**: META (Cross-cutting governance)
- **01**: Regulatory Frameworks
- **02**: Certification Basis
- **03**: Compliance Strategy
- **04**: Evidence and Traceability
- **05**: Safety Cases and AI Assurance
- **06**: SW/HW Certification
- **07**: ML and Data Specific
- **08**: Tests and Qualification
- **09**: Audits and Findings
- **10**: Authority Interfaces
- **11**: Continuing Airworthiness
- **12**: Change Control
- **13**: DPP and Blockchain
- **14**: Packaging and Archival

### 2. System/Subsystem Dimension (ATA Chapters)
Certification artifacts are tagged with relevant ATA chapters:
- **ATA 20-49**: Airframe and systems (e.g., flight controls, hydraulics, electrical)
- **ATA 70-80**: Propulsion (hydrogen fuel cell systems)
- **ATA 31, 42, 45**: Avionics and AI systems (CAOS, neural networks)
- **ATA 95**: Digital Product Passport and traceability

### 3. Artifact Type Dimension
- **DOC**: Documents (strategies, plans, reports)
- **PLAN**: Plans (certification plans, test plans)
- **PROC**: Procedures (compliance demonstration procedures)
- **SPEC**: Specifications (requirements, design specs)
- **EVID**: Evidence (test results, analysis reports, inspection records)
- **TRACE**: Traceability artifacts (matrices, links)
- **SUBMIT**: Submission packages (dossiers, briefings)
- **ASSET**: Supporting assets (diagrams, spreadsheets, templates)

### 4. Authority/Standard Dimension
- **EASA**: EASA-specific artifacts
- **FAA**: FAA-specific artifacts
- **DUAL**: Harmonized EASA/FAA artifacts
- **DO178**: DO-178C related
- **DO254**: DO-254 related
- **AI-RD**: EASA AI Roadmap related
- **AI-AF**: FAA AI Assurance Framework related
- **EU-AI**: EU AI Act related

### 5. Status/Maturity Dimension
- **DRAFT**: Work in progress
- **REVIEW**: Under internal review
- **APPROVED**: Internally approved
- **SUBMITTED**: Submitted to authorities
- **ACCEPTED**: Accepted by authorities
- **CLOSED**: Compliance demonstrated and closed
- **ARCHIVED**: Archived for long-term retention

## Naming Convention

### Document Naming Pattern
```
{Phase}-{Category}-{Subcategory}-{Sequence}_{Title}.{ext}
```

**Example**:
```
95-00-10-05-001_Safety_Case_Concept_for_NN.md
│  │  │  │  │   └─ Descriptive Title
│  │  │  │  └───── Sequential number
│  │  │  └──────── Subcategory (05 = Safety Cases)
│  │  └─────────── Category (10 = Certification)
│  └────────────── ATA Chapter level 2 (00 = General)
└───────────────── ATA Chapter level 1 (95 = DPP/NN)
```

### Asset Naming Pattern
```
{Phase}-{Category}-{Subcategory}-A-{Sequence}_{Title}.{ext}
```

**Example**:
```
95-00-10-05-A-001_Safety_Case_Template.md
                │  └─ Indicates ASSET type
```

## Classification Schemes

### Certification Evidence Classes
1. **Class A: Regulatory Compliance Evidence**
   - Direct demonstration of regulatory requirement compliance
   - Subject to authority audit and approval
   - Examples: Compliance demonstration reports, type certificate application

2. **Class B: Safety Case Evidence**
   - Supports safety arguments and claims
   - Subject to safety assessment review
   - Examples: Hazard analysis reports, safety test results

3. **Class C: Process Compliance Evidence**
   - Demonstrates process adherence (DO-178C, DO-254)
   - Subject to quality and process audits
   - Examples: Review records, tool qualification data

4. **Class D: Supporting Evidence**
   - Background information and rationale
   - Not directly submitted but available for audit
   - Examples: Design trade studies, internal analyses

### AI/ML Certification Categories
1. **ML-DATA**: Dataset and data pipeline certification
   - Data provenance
   - Dataset quality metrics
   - Bias and fairness assessments

2. **ML-MODEL**: Neural network model certification
   - Model architecture specifications
   - Training and validation results
   - Performance and robustness evidence

3. **ML-RUNTIME**: Runtime assurance and monitoring
   - Runtime monitoring specifications
   - Out-of-distribution detection
   - Degradation management

4. **ML-UPDATE**: Model update and retraining
   - Retraining procedures
   - Change impact assessments
   - Version control evidence

### Special Conditions Categories
- **SC-BWB**: BWB configuration special conditions
- **SC-H2**: Hydrogen propulsion special conditions
- **SC-AI**: AI/ML system special conditions
- **SC-DPP**: Digital Product Passport special conditions

## Traceability Tags

### Requirement Traceability
All certification documents include tags linking to:
- **REQ-ID**: Requirements from 95-00-03 (Requirements folder)
- **VV-ID**: V&V activities from 95-00-07 (V&V folder)
- **HAZARD-ID**: Hazards from 95-00-02 (Safety folder)
- **DESIGN-ID**: Design elements from 95-00-04 (Design folder)

### Cross-Reference Tags
- **@EASA[regulation/section]**: Reference to EASA regulations (e.g., @EASA[CS-25.1309])
- **@FAA[regulation/section]**: Reference to FAA regulations (e.g., @FAA[25.1309])
- **@DO178C[objective]**: Reference to DO-178C objectives (e.g., @DO178C[A-1])
- **@AI-RD[section]**: Reference to EASA AI Roadmap (e.g., @AI-RD[3.2])

## Metadata Schema

Each certification artifact includes structured metadata:

```yaml
document_id: "95-00-10-XX-XXX"
title: "Document Title"
version: "1.0"
status: "DRAFT | REVIEW | APPROVED | SUBMITTED | ACCEPTED | CLOSED"
date: "YYYY-MM-DD"
author: "Name"
approver: "Name"
ata_chapter: ["31", "95"]
artifact_type: "DOC | PLAN | PROC | SPEC | EVID | TRACE | SUBMIT | ASSET"
authority: ["EASA", "FAA"]
classification: "Class A | Class B | Class C | Class D"
related_documents: ["95-00-10-XX-XXX", ...]
traceability:
  requirements: ["REQ-ID-XXX", ...]
  hazards: ["HAZARD-ID-XXX", ...]
  vv_activities: ["VV-ID-XXX", ...]
keywords: ["keyword1", "keyword2", ...]
```

## Search and Retrieval

### Search Facets
Users can search certification artifacts using:
- Lifecycle phase
- ATA chapter
- Artifact type
- Authority/standard
- Status
- Keywords
- Date range
- Author

### Common Search Queries
1. "All EASA-submitted safety case evidence for neural networks"
   - Filter: Authority=EASA, Type=EVID, Phase=05, Keywords=neural network, Status=SUBMITTED

2. "Open findings from authority audits"
   - Filter: Phase=09, Type=EVID, Status=REVIEW

3. "DO-178C compliance evidence for CAOS software"
   - Filter: Standard=DO178, ATA=42, Type=EVID

## Versioning and Configuration Management

### Version Numbering
- **Major.Minor.Patch** (e.g., 1.2.3)
- **Major**: Significant content change, re-approval required
- **Minor**: Moderate updates, review required
- **Patch**: Editorial corrections, no re-approval needed

### Configuration Baselines
- **CB-01**: Certification Basis Baseline (Month 6)
- **CB-02**: Safety Case Baseline (Month 18)
- **CB-03**: Compliance Demonstration Baseline (Month 30)
- **CB-04**: Type Certificate Baseline (Month 36)

Each baseline locks configuration of relevant artifacts.

## Integration with CAOS and DPP

### CAOS Certification Hooks
CAOS AI system interfaces with certification taxonomy via:
- Automated metadata extraction
- Traceability link validation
- Evidence completeness checking
- Status tracking and alerting

### DPP Blockchain Integration
Certification artifacts stored in DPP include:
- Document hash (SHA-256)
- Timestamp of creation/approval
- Author and approver digital signatures
- Traceability links (hashed)
- Version history (immutable log)

## Governance

### Taxonomy Owner
- **Primary**: Certification Manager
- **Deputy**: Configuration Manager

### Change Control
- Taxonomy changes require Certification Review Board approval
- Impact assessment for all taxonomy changes
- Communication to all stakeholders

### Review and Updates
- **Frequency**: Quarterly or upon major program milestone
- **Next Review**: 2026-02-17

## References

- 95-00-10-00-001 Certification Strategy
- 95-00-10-00-002 Certification Lifecycle Overview
- 95-00-10-00-004 Certification Traceability Matrix
- AMPEL360 Configuration Management Plan
- ATA iSpec 2200 (Numbering system)

---
*This document is part of the AMPEL360 OPT-IN Framework certification package.*
