# 95-00-11-00-003: EIS Versioning Taxonomy

**Document ID:** 95-00-11-00-003  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Owner:** AMPEL360 Configuration Management Team  

---

## 1. Purpose

Define a comprehensive taxonomy for all versioned entities within the AMPEL360 EIS ecosystem, ensuring consistent naming, classification, and relationships across all configuration items.

---

## 2. Taxonomy Structure

### 2.1 Primary Entities

#### A. **Aircraft Configuration Version**
- **Format**: `AMPEL360-BWB-H2-v{MAJOR}.{MINOR}.{PATCH}`
- **Example**: `AMPEL360-BWB-H2-v2.3.1`
- **Description**: Top-level aircraft configuration baseline
- **Scope**: Entire aircraft system integration

#### B. **System Version**
- **Format**: `{ATA_CHAPTER}-v{MAJOR}.{MINOR}.{PATCH}`
- **Example**: `ATA28-FuelSystem-v1.5.2`
- **Description**: Individual system baseline per ATA chapter
- **Scope**: Single aircraft system

#### C. **Neural Network Model Version**
- **Format**: `{MODEL_NAME}-v{MAJOR}.{MINOR}.{PATCH}-build{BUILD_ID}`
- **Example**: `FlightControlNN-v2.1.0-build3421`
- **Description**: Trained AI/ML model with specific weights
- **Scope**: Individual neural network

#### D. **Training Dataset Version**
- **Format**: `{DATASET_NAME}-v{YEAR}.{MONTH}.{SEQUENCE}`
- **Example**: `FlightTestData-v2025.11.003`
- **Description**: Versioned training/validation dataset
- **Scope**: ML training data

#### E. **Software/Firmware Version**
- **Format**: `{COMPONENT}-SW-v{MAJOR}.{MINOR}.{PATCH}`
- **Example**: `FCC-PrimaryFW-v4.2.1`
- **Description**: Software or firmware for avionics components
- **Scope**: Individual LRU or software module

#### F. **DPP Entry Version**
- **Format**: `DPP-{AIRCRAFT_ID}-{TIMESTAMP}-{SEQUENCE}`
- **Example**: `DPP-AC001-20251117T143000Z-00042`
- **Description**: Digital Product Passport immutable entry
- **Scope**: Single blockchain-anchored record

#### G. **Documentation Version**
- **Format**: `{DOC_TYPE}-{DOC_ID}-Rev{REVISION}`
- **Example**: `AFM-95-00-11-RevC`
- **Description**: Technical publications and manuals
- **Scope**: Individual document

---

## 3. Version Component Definitions

### 3.1 Semantic Version Components

#### MAJOR Version
Increment when:
- Incompatible changes requiring recertification
- Breaking API or interface changes
- Structural modifications to aircraft
- New flight envelope or operational capabilities
- Regulatory basis change

**Impact**: Full recertification cycle, operator training, flight test campaign

#### MINOR Version
Increment when:
- New features added (backward compatible)
- Performance improvements
- Additional operational modes
- Enhanced monitoring capabilities
- Non-breaking interface extensions

**Impact**: Partial validation, updated documentation, potential training

#### PATCH Version
Increment when:
- Bug fixes with no functional change
- Security patches
- Documentation corrections
- Configuration tweaks within approved ranges
- Performance optimizations (no behavior change)

**Impact**: Minimal validation, service bulletin, rapid deployment

---

## 4. Entity Relationships

```
Aircraft Configuration v2.3.1
├── Hardware BOM v2.3
│   ├── Wing Assembly v1.2.4
│   ├── Fuselage v1.1.8
│   └── Landing Gear v2.0.3
├── Software Baseline v2.3.1
│   ├── Flight Control SW v4.1.0
│   ├── FMS Software v3.2.1
│   └── CAOS Platform v2.3.0
├── Neural Networks v2.3
│   ├── FlightControlNN v2.1.0-build3421
│   ├── EnergyMgmtNN v1.8.2-build2987
│   └── PredMaintNN v1.5.1-build3102
├── Training Datasets
│   ├── FlightTestData v2025.11.003
│   ├── SimulationData v2025.10.012
│   └── OperationalData v2025.11.001
└── Documentation Set v2.3
    ├── AFM RevC
    ├── AMM RevB
    └── Training Manual v2.3
```

---

## 5. Classification Schemes

### 5.1 By Criticality Level

| Level | Definition | Examples | Change Control |
|-------|------------|----------|----------------|
| **Flight-Critical** | Failure causes catastrophic consequences (DAL A) | Flight control NN, primary FCC | CCB + Authorities |
| **Mission-Critical** | Failure prevents mission completion (DAL B/C) | Navigation system, fuel management | CCB Required |
| **Operational** | Failure reduces efficiency (DAL D/E) | Passenger entertainment, route optimization | Engineering Review |
| **Support** | Development/test only | Simulators, ground test equipment | PM Approval |

### 5.2 By Deployment Phase

| Phase | Code | Description | Stability | Deployment |
|-------|------|-------------|-----------|------------|
| **Development** | DEV | Active development | Unstable | Dev environment only |
| **Integration** | INT | System integration | Stabilizing | Integration test |
| **Validation** | VAL | V&V in progress | Stable | Test aircraft |
| **Certification** | CERT | Authority review | Frozen | Certification campaign |
| **Production** | PROD | Certified, operational | Stable | Fleet deployment |
| **Maintenance** | MAINT | Hotfix/patch applied | Stable | Targeted aircraft |
| **Deprecated** | DEP | Obsolete | N/A | Decommissioned |

### 5.3 By Change Type

| Type | Abbreviation | Regulatory Impact | Example |
|------|--------------|-------------------|---------|
| **Major Modification** | MM | Type Certificate Amendment | New propulsion system |
| **Minor Change** | MC | EASA Form 1 or equivalent | Software update with new features |
| **Repair** | REP | Approved data only | Component replacement |
| **Service Bulletin** | SB | Optional or mandatory | Performance improvement |
| **Airworthiness Directive** | AD | Mandatory compliance | Safety-critical fix |
| **Emergency Directive** | ED | Immediate action | Grounding issue resolution |

---

## 6. Naming Conventions

### 6.1 Aircraft Tail Number Mapping
```
Physical Aircraft: N360HY-001
  └── DPP ID: AMPEL-BWB-H2-AC001
      └── Configuration: AMPEL360-BWB-H2-v2.3.1
          └── Deployed: 2025-11-20T10:00:00Z
```

### 6.2 Environment Identifiers
- **DEV**: Development (developers' workstations)
- **CI**: Continuous Integration (automated testing)
- **SIM**: Simulator environments
- **HIL**: Hardware-in-the-loop test rigs
- **FT**: Flight test aircraft
- **PROD**: Production fleet

### 6.3 Operator/Fleet Tags
```
{OPERATOR_CODE}-{FLEET_ID}-{AIRCRAFT_SEQ}
Examples:
  - LA-001-AC003  # Launch Airline, Fleet 1, Aircraft 3
  - EU-ALP-AC012  # European Alps Operator, Aircraft 12
```

---

## 7. Metadata Schema

Every versioned entity includes:

```yaml
entity:
  id: "FlightControlNN-v2.1.0-build3421"
  type: "NeuralNetwork"
  category: "FlightCritical"
  criticality: "DAL_A"
  version:
    major: 2
    minor: 1
    patch: 0
    build: 3421
  lifecycle:
    created: "2025-11-10T08:30:00Z"
    validated: "2025-11-15T14:00:00Z"
    certified: "2025-11-18T10:00:00Z"
    deployed: "2025-11-20T10:00:00Z"
  relationships:
    depends_on:
      - "TrainingData-v2025.11.003"
      - "InferenceEngine-v1.4.2"
    used_by:
      - "FlightControlSystem-v4.1.0"
    supersedes: "FlightControlNN-v2.0.5-build3204"
  certification:
    basis: "CS-25.1309, DO-178C DAL A"
    evidence: "95-00-10-02-043"
    authority: "EASA"
    date: "2025-11-18"
  dpp:
    blockchain_anchor: "0x7f3a2b9c4e1d..."
    ipfs_hash: "Qm... (detailed artifacts)"
```

---

## 8. Version Comparison Rules

### 8.1 Compatibility Matrix

| From Version | To Version | Compatibility | Action Required |
|--------------|------------|---------------|------------------|
| v2.3.1 | v2.3.2 | Fully compatible | Drop-in replacement |
| v2.3.x | v2.4.0 | Backward compatible | Validation testing |
| v2.x.x | v3.0.0 | Breaking change | Recertification |
| v2.3.1 | v2.3.0 | Rollback | Regression testing |

### 8.2 Dependency Resolution
- **Hard Dependency**: Exact version required
- **Soft Dependency**: Version range acceptable (e.g., `>= 2.3.0, < 3.0.0`)
- **Conflicting Dependencies**: Resolved by CCB

---

## 9. Taxonomy Governance

- **Owner**: Configuration Management Office
- **Review Cycle**: Quarterly
- **Change Process**: Taxonomy Change Request (TCR) to CCB
- **Tool Support**: Automated validation in CI/CD pipeline

---

## 10. Cross-References

- **95-00-11-00-001**: EIS and Versioning Strategy (parent document)
- **95-00-11-00-004**: Version Traceability Matrix (usage)
- **95-00-11-01-003**: Semantic Versioning Rules (detailed rules)
- **95-00-11-02-001**: Tagging Conventions (Git integration)
- **95-00-11-08-001**: DPP Versioning Model (DPP specifics)

---

## 11. Document Control

| Revision | Date | Author | Changes |
|----------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 CM Team | Initial taxonomy definition |

---

**Document Classification:** Internal Use  
**Next Review Date:** 2026-02-17  
**Contact:** taxonomy@ampel360.aero
