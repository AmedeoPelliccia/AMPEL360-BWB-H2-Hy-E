# 95-00-09-00-003: Production Planning Taxonomy

**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** ACTIVE  
**Document ID:** 95-00-09-00-003

---

## 1. Purpose

This document defines the taxonomy and classification system for all production planning artifacts, processes, and documentation within the AMPEL360 BWB H2 Hy-E neural network systems.

---

## 2. Scope

This taxonomy covers:
- Production planning document classification
- Artifact categorization
- Process classification
- Traceability relationships
- Metadata standards

---

## 3. Document Classification

### 3.1 Document Types

| Type Code | Type Name | Description | Example |
|-----------|-----------|-------------|---------|
| STRT | Strategy | High-level strategic documents | 95-00-09-00-001 |
| CRIT | Criteria | Acceptance and readiness criteria | 95-00-09-00-002 |
| TAXO | Taxonomy | Classification and structure documents | 95-00-09-00-003 |
| PROC | Process | Process definitions and procedures | 95-00-09-01-001 |
| PLAN | Plan | Detailed planning documents | 95-00-09-02-001 |
| SPEC | Specification | Technical specifications | 95-00-09-03-003 |
| GUID | Guideline | Best practices and guidelines | 95-00-09-04-001 |
| TMPL | Template | Document or data templates | 95-00-09-10-A-001 |
| REPT | Report | Assessment and analysis reports | 95-00-09-07-002 |
| MATR | Matrix | Traceability and mapping matrices | 95-00-09-00-004 |
| REGR | Registry | Catalogs and inventories | 95-00-09-00-005 |
| RISK | Risk Document | Risk registers and assessments | 95-00-09-00-006 |
| CHKL | Checklist | Validation and verification checklists | 95-00-09-01-005 |

### 3.2 Document Hierarchy

```
95-00-09: Production Planning (Root)
├── 95-00-09-00-XXX: Core Strategy and Meta (00_META)
├── 95-00-09-01-XXX: Model Freeze and Baselines (01)
├── 95-00-09-02-XXX: Data Production Pipelines (02)
├── 95-00-09-03-XXX: MLOps Production (03)
├── 95-00-09-04-XXX: SW/HW Industrialization (04)
├── 95-00-09-05-XXX: AI Supply Chain (05)
├── 95-00-09-06-XXX: DPP and Blockchain Production (06)
├── 95-00-09-07-XXX: Verification in Production (07)
├── 95-00-09-08-XXX: Monitoring and Support (08)
├── 95-00-09-09-XXX: Flight Operations and EIS (09)
├── 95-00-09-10-XXX: Documentation and Deliverables (10)
└── 95-00-09-11-XXX: Certification and Audit (11)
```

### 3.3 Asset Numbering

Assets follow the pattern: `95-00-09-XX-A-YYY_<Category>_<Name>.<ext>`

Where:
- **XX**: Subdirectory number (00-11)
- **A**: Asset indicator
- **YYY**: Asset sequence number (001-999)
- **Category**: Asset category code (see Section 4)

---

## 4. Asset Categories

### 4.1 Asset Category Codes

| Category | Code | Description | Typical Formats |
|----------|------|-------------|-----------------|
| Diagrams | DIAG | Architecture, flow, sequence diagrams | .drawio, .mmd, .svg |
| Flowcharts | FLOW | Process flowcharts | .drawio, .svg |
| Tables | TABL | Data tables and matrices | .csv, .xlsx |
| Configurations | CONF | Configuration files | .yaml, .json, .xml |
| Templates | TMPL | Document and data templates | .md, .xlsx, .json |
| Specifications | SPEC | Technical specifications | .json, .yaml, .md |
| Schemas | SCHM | Data schemas and structures | .json, .xsd, .yaml |
| Reports | REPT | Generated or template reports | .md, .pdf |
| Scripts | SCPT | Automation scripts | .py, .sh, .js |
| Manifests | MNFT | Deployment manifests | .yaml, .json |

### 4.2 Asset ID Ranges by Category

- **A001-A099**: Flowcharts and process diagrams
- **A100-A199**: Architecture diagrams
- **A200-A299**: Tables and matrices (CSV, Excel)
- **A300-A399**: Configuration files (YAML, JSON)
- **A400-A499**: Templates (documents, data)
- **A500-A599**: Specifications and schemas
- **A600-A699**: Reports and analysis outputs
- **A700-A799**: Scripts and automation
- **A800-A899**: Manifests and deployment configs
- **A900-A999**: Miscellaneous and exports

---

## 5. Process Classification

### 5.1 Process Types

| Process Type | Code | Description | Trigger |
|--------------|------|-------------|---------|
| Model Freeze | MFRZ | Freezing model for production | Completion of V&V |
| Baseline Management | BASL | Managing production baselines | Model freeze |
| Data Pipeline | DPIP | Data production workflows | Scheduled/event-driven |
| ETL Process | ETLP | Extract, Transform, Load | Data source updates |
| CI/CD Pipeline | CICD | Continuous integration/deployment | Code commit |
| Model Deployment | MDPL | Deploying models to production | Release approval |
| Hardware Qualification | HWQL | Qualifying hardware targets | New hardware intro |
| Verification | VRFY | Production verification activities | Pre-release gate |
| Validation | VALD | Production validation activities | Post-deployment |
| Monitoring | MNTR | Health and performance monitoring | Continuous |
| Incident Response | INCR | Responding to production incidents | Incident detection |
| Audit | AUDT | Compliance and quality audits | Scheduled/triggered |

### 5.2 Process States

| State | Code | Description |
|-------|------|-------------|
| Planned | PLAN | Process is defined but not initiated |
| In Progress | INPR | Process is currently executing |
| Blocked | BLCK | Process is blocked awaiting input |
| Review | REVW | Process output under review |
| Approved | APRV | Process output approved |
| Deployed | DPLY | Process is operational |
| Deprecated | DEPR | Process is no longer used |

---

## 6. Traceability Relationships

### 6.1 Relationship Types

| Relationship | Code | Direction | Description |
|--------------|------|-----------|-------------|
| Derives From | DRVF | Forward | Target derives from source |
| Refines | REFN | Forward | Target refines source |
| Implements | IMPL | Forward | Target implements source |
| Validates | VALD | Forward | Target validates source |
| Depends On | DEPO | Forward | Target depends on source |
| Parent Of | PRNT | Hierarchical | Source is parent of target |
| References | REFS | Associative | Source references target |
| Supersedes | SUPR | Temporal | Source supersedes target |

### 6.2 Traceability Metadata

Each traced item must include:
- **Source ID**: Unique identifier of source artifact
- **Target ID**: Unique identifier of target artifact
- **Relationship Type**: Type code from 6.1
- **Rationale**: Reason for relationship
- **Status**: Current status of relationship
- **Last Verified**: Date of last verification

---

## 7. Lifecycle Stage Classification

### 7.1 Production Planning Stages

| Stage | Code | Description | Entry Criteria | Exit Criteria |
|-------|------|-------------|----------------|---------------|
| Planning | PLNG | Initial production planning | V&V completion | Plan approval |
| Preparation | PREP | Production infrastructure setup | Plan approval | Infrastructure ready |
| Freeze | FREZ | Model and data freeze | Preparation complete | Freeze approval |
| Industrialization | INDZ | Full industrialization | Freeze approval | PRR pass |
| Validation | VALD | Production validation | Industrialization complete | Validation pass |
| Release | RELS | Production release | Validation pass | Release authorization |
| Support | SUPT | Production support and monitoring | Release authorization | EIS transition |

---

## 8. Risk Classification

### 8.1 Risk Categories

| Category | Code | Description |
|----------|------|-------------|
| Technical | TECH | Technical implementation risks |
| Schedule | SCHD | Timeline and deadline risks |
| Resource | RSRC | Resource availability risks |
| Quality | QUAL | Quality and performance risks |
| Safety | SAFE | Safety-related risks |
| Security | SECU | Security and cyber risks |
| Regulatory | REGU | Compliance and certification risks |
| Supply Chain | SUPC | External dependency risks |

### 8.2 Risk Severity Levels

| Level | Code | Description | Response Required |
|-------|------|-------------|-------------------|
| Critical | CRIT | Immediate threat to safety or program | Immediate action |
| High | HIGH | Significant impact on timeline or quality | Action within 48h |
| Medium | MEDM | Moderate impact, manageable | Action within 1 week |
| Low | LOWW | Minor impact, monitoring sufficient | Action as resources allow |

---

## 9. Data Classification

### 9.1 Data Sensitivity Levels

| Level | Code | Access Control | Examples |
|-------|------|----------------|----------|
| Public | PUBL | No restriction | Published documentation |
| Internal | INTL | Company-wide | General production docs |
| Restricted | REST | Need-to-know | Detailed technical specs |
| Confidential | CONF | Authorized only | Proprietary algorithms |
| Regulated | REGL | Compliance-controlled | Certification evidence |

### 9.2 Data Types

| Type | Code | Description | Format |
|------|------|-------------|--------|
| Training Data | TRDA | Neural network training datasets | HDF5, TFRecord, Parquet |
| Validation Data | VLDA | Validation datasets | Same as training |
| Configuration | CNFG | System configurations | YAML, JSON |
| Model Artifacts | MDLA | Trained model files | ONNX, SavedModel, PTH |
| Metadata | META | Descriptive metadata | JSON, YAML |
| Logs | LOGS | System and application logs | Text, JSON |
| Metrics | METR | Performance and health metrics | Time-series DB |

---

## 10. Integration with Standards

### 10.1 Alignment with External Standards

This taxonomy aligns with:
- **[ISO/IEC 15288](https://www.iso.org/standard/63711.html)**: Systems lifecycle processes
- **[ARP4754A](https://www.sae.org/standards/content/arp4754a/)**: Development of civil aircraft systems
- **[DO-178C](https://www.rtca.org/content/standards-guidance-materials)**: Software considerations in airborne systems
- **[ISO 9001](https://www.iso.org/iso-9001-quality-management.html)**: Quality management systems
- **[EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)**: Certification specifications

### 10.2 Digital Product Passport (DPP) Integration

All production artifacts are classified for DPP inclusion:
- **DPP_REQUIRED**: Must be included in DPP
- **DPP_OPTIONAL**: May be included if relevant
- **DPP_EXCLUDED**: Not for DPP inclusion

---

## 11. Metadata Standards

### 11.1 Required Metadata Fields

All production artifacts must include:
```yaml
artifact_id: "95-00-09-XX-YYY"
title: "Descriptive title"
type: "Document type code"
version: "X.Y"
date: "YYYY-MM-DD"
status: "DRAFT | REVIEW | ACTIVE | DEPRECATED"
owner: "Role or person responsible"
classification: "Sensitivity level code"
dpp_inclusion: "REQUIRED | OPTIONAL | EXCLUDED"
```

### 11.2 Optional Metadata Fields

```yaml
approver: "Approving authority"
review_cycle: "Review frequency"
next_review: "YYYY-MM-DD"
related_documents: ["ID1", "ID2", ...]
keywords: ["tag1", "tag2", ...]
change_history: [...]
```

---

## 12. Version Control Convention

### 12.1 Version Numbering

Format: **MAJOR.MINOR.PATCH**

- **MAJOR**: Incompatible changes, major restructuring
- **MINOR**: Backward-compatible additions or changes
- **PATCH**: Minor corrections, clarifications

### 12.2 Version States

- **0.x.x**: Draft, under development
- **1.0.0**: First approved release
- **x.x.x-RC**: Release candidate
- **x.x.x-DEPRECATED**: No longer maintained

---

## 13. Document Control

- **Owner**: Production Planning Board
- **Approver**: Chief Engineer, AI Systems
- **Review Cycle**: Annually or upon major taxonomy change
- **Next Review**: 2026-11-17
- **Related Documents**:
  - [95-00-09-00-001: Production Planning Strategy](../95-00-09-00-001_Production_Planning_Strategy.md)
  - [95-00-09-00-004: Production Traceability Matrix](./95-00-09-00-004_Production_Traceability_Matrix.csv)
  - [AMPEL360_DOCUMENTATION_STANDARD.md](../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)

---

**Document Control Information:**
- **Status**: ACTIVE
- **Classification**: Internal - Production
- **Distribution**: All Production Planning Team Members
