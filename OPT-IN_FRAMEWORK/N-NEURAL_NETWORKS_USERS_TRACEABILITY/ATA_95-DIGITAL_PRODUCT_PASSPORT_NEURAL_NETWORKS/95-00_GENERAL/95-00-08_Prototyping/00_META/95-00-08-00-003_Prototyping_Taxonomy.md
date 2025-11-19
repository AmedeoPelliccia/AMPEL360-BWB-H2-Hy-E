# 95-00-08-00-003_Prototyping_Taxonomy

## Document Information

- **Document ID**: 95-00-08-00-003
- **Title**: Prototyping Taxonomy
- **Version**: 1.0
- **Status**: Active
- **Date**: 2025-11-17
- **Author**: AMPEL360 Documentation WG
- **Related Documents**: 
  - 95-00-08-00-001_Prototyping_Strategy
  - 95-00-08-00-005_Prototype_Registry

---

## 1. Purpose

This document defines a standardized taxonomy for classifying and categorizing prototypes within the ATA Chapter 95 Digital Product Passport Neural Networks framework. It ensures consistent nomenclature, facilitates traceability, and enables effective communication across teams and lifecycle stages.

---

## 2. Prototype Classification Dimensions

Prototypes are classified along multiple dimensions:

### 2.1 By Development Stage

| Stage | Description | Typical Duration |
|-------|-------------|------------------|
| **Concept** | Initial exploration, proof-of-concept | 1-2 weeks |
| **Alpha** | Basic functionality, internal testing | 2-4 weeks |
| **Beta** | Advanced functionality, broader testing | 4-8 weeks |
| **Release Candidate** | Production-ready, final validation | 2-4 weeks |

### 2.2 By Prototype Type

| Type | Code | Description | Example |
|------|------|-------------|---------|
| **Model Prototype** | MP | Neural network architectures, algorithms | CNN for image recognition |
| **Data Prototype** | DP | Synthetic data, preprocessing pipelines | Data augmentation pipeline |
| **Runtime Prototype** | RP | Execution environments, sandboxes | Docker-based sandbox |
| **Integration Prototype** | IP | System interfaces, API prototypes | ATA 31 interface |
| **HMI Prototype** | HP | User interfaces, dashboards | Pilot alerting dashboard |
| **DPP Prototype** | BP | Blockchain, smart contracts | On-chain traceability |
| **Hardware Prototype** | HW | Test rigs, HIL setups | Sensor test rig |
| **Demo Prototype** | DM | Lab and ground demonstrations | Customer showcase |
| **Operational Prototype** | OP | Flight trials, operational testing | Pre-certification trial |
| **Tooling Prototype** | TP | Automation, CI/CD, notebooks | Auto-documentation tool |

### 2.3 By Maturity Level

(See 95-00-08-00-006_Prototype_Maturity_Levels for detailed definitions)

| Level | Name | Description |
|-------|------|-------------|
| **ML0** | Concept | Initial idea, no implementation |
| **ML1** | Proof-of-Concept | Basic functionality demonstrated |
| **ML2** | Functional Prototype | Core features working |
| **ML3** | Integration Prototype | Interfaces with other systems |
| **ML4** | Production-Ready | Meets engineering criteria |
| **ML5** | Certified | Passes V&V and certification |

### 2.4 By ATA System Integration

Prototypes are tagged with the ATA systems they interface with:

| ATA Code | Description | Example Prototype |
|----------|-------------|-------------------|
| **ATA 02** | Weight and Balance | Weight optimization NN |
| **ATA 28** | Fuel Systems | Fuel consumption prediction |
| **ATA 31** | Indicating/Recording | FDR data analysis |
| **ATA 42** | IMA Governance | Partitioning compliance |
| **ATA 45** | Central Maintenance | Predictive maintenance |
| **ATA 95** | Digital Product Passport | DPP blockchain |

### 2.5 By Safety Criticality

| Level | Description | Example |
|-------|-------------|---------|
| **DAL A** | Catastrophic | Flight control NN |
| **DAL B** | Hazardous | Engine health monitoring |
| **DAL C** | Major | Cabin environment control |
| **DAL D** | Minor | Passenger entertainment |
| **DAL E** | No Safety Effect | Documentation tools |

---

## 3. Prototype Naming Convention

### 3.1 Standard Format

```
<Type>-<Stage>-<ATA>-<Seq>-<Version>
```

**Example**: `MP-ALPHA-ATA95-001-v0.3`

- **MP**: Model Prototype
- **ALPHA**: Alpha stage
- **ATA95**: ATA Chapter 95
- **001**: Sequential number
- **v0.3**: Version 0.3

### 3.2 Naming Rules

1. **Type Code**: Use 2-letter code from Section 2.2
2. **Stage**: One of {CONCEPT, ALPHA, BETA, RC}
3. **ATA Code**: Use standard ATA chapter notation
4. **Sequential Number**: 3-digit zero-padded number
5. **Version**: Semantic versioning (vX.Y.Z)

---

## 4. Prototype Tags

In addition to the naming convention, prototypes are tagged with metadata:

### 4.1 Required Tags

| Tag | Description | Example Values |
|-----|-------------|----------------|
| **domain** | Application domain | prediction, classification, optimization |
| **ml_framework** | ML framework used | TensorFlow, PyTorch, Scikit-learn |
| **deployment_target** | Intended deployment | edge, cloud, on-board |
| **data_source** | Primary data source | synthetic, flight_data, simulation |
| **safety_critical** | Safety criticality | true, false |

### 4.2 Optional Tags

| Tag | Description | Example Values |
|-----|-------------|----------------|
| **author** | Prototype owner | john.doe@ampel360.com |
| **sponsor** | Business sponsor | Chief AI Officer |
| **regulatory_scope** | Regulatory requirement | EASA AI.25, FAA AC 20-115D |
| **certification_phase** | Certification stage | pre-cert, cert-prep, certified |

---

## 5. Prototype Categories

### 5.1 By Business Impact

| Category | Description | Priority |
|----------|-------------|----------|
| **Strategic** | High business value, competitive advantage | High |
| **Operational** | Improves efficiency, reduces cost | Medium |
| **Experimental** | Research, long-term innovation | Low |
| **Regulatory** | Required for compliance | High |

### 5.2 By Technology Readiness Level (TRL)

| TRL | Description | Prototype Stage |
|-----|-------------|-----------------|
| **TRL 1-3** | Basic research, proof-of-concept | Concept, Alpha |
| **TRL 4-6** | Lab testing, integration | Beta, RC |
| **TRL 7-8** | System demonstration, qualification | Operational |
| **TRL 9** | Proven in operational environment | Certified |

---

## 6. Taxonomy Usage

### 6.1 In Prototype Registry

All prototypes in the **Prototype Registry** (95-00-08-00-005) must use this taxonomy for:
- Naming
- Tagging
- Classification
- Search and filtering

### 6.2 In Documentation

All prototype documentation must include:
- Prototype name (per naming convention)
- All required tags
- Maturity level
- ATA system integration
- Safety criticality

### 6.3 In Reporting

Reports and dashboards must use this taxonomy to:
- Group prototypes by type, stage, maturity
- Track progress across lifecycle stages
- Analyze resource allocation
- Communicate with stakeholders

---

## 7. Taxonomy Evolution

### 7.1 Change Process

Changes to the taxonomy require:
1. Proposal submitted to Prototype Review Board
2. Impact assessment on existing prototypes
3. PRB approval
4. Update to Prototype Registry
5. Communication to all teams

### 7.2 Version Control

This taxonomy document is version-controlled. All changes must be documented in the version history.

---

## 8. Examples

### 8.1 Model Prototype Example

```yaml
name: MP-ALPHA-ATA95-001-v0.3
type: Model Prototype
stage: Alpha
ata_system: ATA 95
sequence: 001
version: v0.3
maturity_level: ML1
tags:
  domain: classification
  ml_framework: TensorFlow
  deployment_target: cloud
  data_source: synthetic
  safety_critical: false
  author: alice.smith@ampel360.com
category: Experimental
trl: 4
```

### 8.2 Integration Prototype Example

```yaml
name: IP-BETA-ATA31-005-v1.2
type: Integration Prototype
stage: Beta
ata_system: ATA 31
sequence: 005
version: v1.2
maturity_level: ML3
tags:
  domain: data_acquisition
  ml_framework: N/A
  deployment_target: on-board
  data_source: flight_data
  safety_critical: true
  author: bob.jones@ampel360.com
  regulatory_scope: EASA AI.25
category: Regulatory
trl: 6
```

---

## 9. References

- **95-00-08-00-001**: Prototyping Strategy
- **95-00-08-00-005**: Prototype Registry
- **95-00-08-00-006**: Prototype Maturity Levels

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial version |

---

**End of Document**
