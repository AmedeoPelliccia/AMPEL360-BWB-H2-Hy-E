# AMPEL360 Documentation Standard

**Version:** 1.1  
**Date:** 2025-11-12  
**Status:** Active

---

## Overview

This document defines the mandatory documentation structure for the AMPEL360-BWB-H₂-Hy-E program. All ATA chapters and systems must comply with this standard to ensure:

- **Coherent documentation** across all systems
- **Certification readiness** with complete traceability
- **Lifecycle coverage** from concept to maintenance
- **Standards compliance** with ATA iSpec 2200, S1000D, and regulatory requirements

---

## Canonical Reference: ATA 95-00-00_GENERAL

The **ATA 95-00-00_GENERAL** (Neural Networks) serves as the canonical reference pattern for all ATA chapter documentation structures. All other ATA chapters must follow this pattern.

**Location:** `/OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95_NEURAL_NETWORKS/95-00-00_GENERAL/`

---

## Mandatory XX-00-00_GENERAL Structure

Every ATA chapter **MUST** include a `XX-00-00_GENERAL` directory (where `XX` is the ATA chapter number) containing the complete 14-folder lifecycle structure.

### Folder Hierarchy

```
ATA_XX-SYSTEM_NAME/
└── XX-00-00_GENERAL/
    ├── XX-00-01_Overview/              # System description and architecture
    ├── XX-00-02_Safety/                # Hazard analysis and safety requirements
    ├── XX-00-03_Requirements/          # Functional and non-functional requirements
    ├── XX-00-04_Design/                # System design and models
    ├── XX-00-05_Interfaces/            # Interface specifications and protocols
    ├── XX-00-06_Engineering/           # Analysis, models, simulations
    ├── XX-00-07_V_and_V/               # Verification and validation
    ├── XX-00-08_Prototyping/           # Proof-of-concept implementations
    ├── XX-00-09_Production_Planning/   # Deployment strategies
    ├── XX-00-10_Certification/         # Regulatory compliance
    ├── XX-00-11_Operations_Maintenance/ # Operational procedures
    ├── XX-00-12_Assets_Management/     # Asset and resource management
    ├── XX-00-13_Subsystems_Components/ # Component specifications
    └── XX-00-14_Meta_Governance/       # Standards and governance
```

---

## 14-Folder Lifecycle Structure

### 01_OVERVIEW
**Purpose:** System description, architecture, purpose, and scope

**Content:**
- System overview and description
- Architecture diagrams
- Scope definition
- Key features and capabilities
- Integration with other systems

**Key Documents:**
- System Architecture Document (SAD)
- Interface diagram
- Stakeholder requirements

---

### 02_SAFETY
**Purpose:** Functional Hazard Assessment (FHA), FMEA, FTA, Common Cause Analysis (CCA), safety cases

**Content:**
- Functional Hazard Assessment (FHA)
- Failure Modes and Effects Analysis (FMEA)
- Fault Tree Analysis (FTA)
- Common Cause Analysis (CCA)
- Safety requirements and objectives
- Safety cases and validation

**Key Documents:**
- Safety Assessment Report
- Hazard Log
- Safety Requirements Specification

**Standards:**
- ARP4754A (Development of Civil Aircraft and Systems)
- ARP4761 (Safety Assessment Process)

---

### 03_REQUIREMENTS
**Purpose:** Functional, non-functional, safety, and data requirements

**Content:**
- Functional requirements
- Non-functional requirements (performance, reliability, maintainability)
- Safety requirements
- Data requirements
- Requirements traceability matrix
- Requirements management and change control

**Key Documents:**
- System Requirements Document (SRD)
- Requirements Traceability Matrix (RTM)
- Requirements Verification Cross-Reference Matrix (RVCRM)

---

### 04_DESIGN
**Purpose:** System design, models, System Architecture Document (SAD), diagrams

**Content:**
- System design documentation
- Design models and diagrams
- System Architecture Document (SAD)
- Design decisions and rationale
- Design verification against requirements

**Key Documents:**
- System Architecture Document (SAD)
- Design Description Document (DDD)
- Trade study reports

---

### 05_INTERFACES
**Purpose:** Interface Control Documents (ICD), data formats, timing, protocols

**Content:**
- Interface Control Documents (ICD)
- Data formats and protocols
- Timing requirements and constraints
- Interface specifications
- API documentation
- Bus specifications (AFDX, CAN, etc.)

**Key Documents:**
- Interface Control Document (ICD)
- Data Dictionary
- Protocol Specifications

---

### 06_ENGINEERING
**Purpose:** Analysis, models, simulations, trade-off studies

**Content:**
- Engineering analysis
- Models and simulations
- Trade-off studies
- Performance analysis
- Optimization studies
- Computational models

**Key Documents:**
- Analysis Reports
- Simulation Results
- Trade Study Documents

**Tools:**
- CAD (Computer-Aided Design)
- CAE (Computer-Aided Engineering)
- CAM (Computer-Aided Manufacturing)
- CAOS (Computer-Aided Operations & Services)

---

### 07_V_AND_V
**Purpose:** Verification and Validation plans and results

**Content:**
- Verification plans and procedures
- Validation plans and strategies
- Test procedures and scripts
- Test results and reports
- Verification coverage analysis
- Requirements verification matrix

**Key Documents:**
- Verification Plan
- Validation Plan
- Test Procedures
- Test Reports
- Requirements Verification Matrix

**Standards:**
- DO-178C (Software)
- DO-254 (Hardware)
- DO-160 (Environmental Conditions)

---

### 08_PROTOTYPING
**Purpose:** Mockups, test benches, experiments, proof-of-concept

**Content:**
- Proof-of-concept implementations
- Mockups and prototypes
- Test benches and rigs
- Experimental results
- Lessons learned
- Technology demonstrations

**Key Documents:**
- Prototype Test Reports
- Lessons Learned Documents
- Technology Readiness Level (TRL) Assessments

---

### 09_PRODUCTION_PLANNING
**Purpose:** Industrialization, deployment, ramp-up strategies

**Content:**
- Industrialization strategy
- Deployment plans
- Manufacturing considerations
- Ramp-up planning
- Supply chain management
- Quality assurance plans

**Key Documents:**
- Production Plan
- Manufacturing Plan
- Quality Assurance Plan
- Supply Chain Strategy

---

### 10_CERTIFICATION
**Purpose:** Regulatory requirements mapping, Means of Compliance (MoC), evidence

**Content:**
- Regulatory requirements mapping
- Means of Compliance (MoC)
- Certification evidence
- Authority liaison records
- Compliance documentation
- Certification plans

**Key Documents:**
- Certification Plan
- Compliance Matrix
- Means of Compliance Documents
- Certification Evidence

**Regulatory Bodies:**
- EASA (European Union Aviation Safety Agency)
- FAA (Federal Aviation Administration)
- Transport Canada
- Other national authorities

**Key Regulations:**
- CS-25 (Large Aeroplanes)
- CS-E (Engines)
- CS-APU (Auxiliary Power Units)

---

### 11_OPERATIONS_MAINTENANCE
**Purpose:** In-service operation, maintenance procedures, troubleshooting

**Content:**
- Operating procedures
- Maintenance procedures
- Troubleshooting guides
- Service bulletins
- Operational limitations
- Maintenance planning

**Key Documents:**
- Aircraft Maintenance Manual (AMM)
- Fault Isolation Manual (FIM)
- Illustrated Parts Catalog (IPC)
- Service Bulletins

**Standards:**
- ATA iSpec 2200
- S1000D

---

### 12_ASSETS_MANAGEMENT
**Purpose:** Spare parts, tooling, datasets, model versions

**Content:**
- Spare parts management
- Tooling and equipment
- Datasets and databases
- Version control
- Configuration management
- Digital assets (models, datasets, software)

**Key Documents:**
- Configuration Management Plan
- Asset Register
- Version Control Logs

---

### 13_SUBSYSTEMS_COMPONENTS
**Purpose:** Hierarchical decomposition of subsystems and components

**Content:**
- Subsystem decomposition
- Component specifications
- Hierarchical breakdown structure
- Dependencies mapping
- Integration points
- Component interfaces

**Key Documents:**
- System Breakdown Structure
- Component Specifications
- Integration Plan

---

### 14_META_GOVERNANCE
**Purpose:** Schemas, CI rules, metadata, traceability framework

**Content:**
- Documentation schemas
- CI/CD rules and pipelines
- Metadata standards
- Traceability framework
- Governance policies
- Quality gates
- Documentation standards

**Key Documents:**
- Documentation Standards
- Governance Framework
- Traceability Matrix
- CI/CD Configuration

---

## Naming Conventions

### Directory Names
- Format: `XX-YY-ZZ_DESCRIPTIVE_NAME`
- `XX`: ATA chapter number (e.g., 22, 95, 115)
- `YY`: Section number (00 for GENERAL layer)
- `ZZ`: Subsection number (01-14 for lifecycle folders)
- Use underscores for multi-word names
- Use UPPERCASE for descriptive parts

**Examples:**
- `22-00-00_GENERAL`
- `95-00-01_Overview`
- `24-00-11_Operations_Maintenance`

### File Names
- Use descriptive names with context
- Include ATA reference code
- Use hyphens or underscores consistently
- End with appropriate extension (.md, .pdf, .xlsx, etc.)

**Examples:**
- `22-00-01-001A_System_Overview.md`
- `95-00-02-005A_Fault_Tree_Analysis.md`
- `24-00-03-REQ_Requirements_Matrix.xlsx`

---

## ATA Code Numbering Convention (Law of Origin)

This section defines the **fundamental numbering blocks** that serve as the origin for all ATA codes across the AMPEL360 program. This "law of origin" ensures consistent, predictable code structure.

### Numbering Blocks

#### 20-xx → SYSTEMS (Functional/Operational)
All **functional systems** and **operational processes** originate from block **20**.

**Scope:**
- Operational systems (handling, processing, management)
- Fleet maintenance programs
- Support system operations
- Functional procedures and workflows

**Examples:**
- `20-00-00_STANDARD_PRACTICES_AIRFRAME` - Base airframe practices
- `03-20-00_GENERAL_HANDLING` - GSE handling systems
- `03-20-01_STORAGE_SHIPPING` - Storage/shipping systems
- `03-20-10_FLEET_MAINTENANCE_PROGRAM` - Fleet-level maintenance
- `03-20-11_LH2_CRYO_REFUELER_MAINT` - LH₂ refueler maintenance system

#### 50-xx → STRUCTURES (Physical/Airframe)
All **physical structures**, **airframe components**, and **structural support** originate from block **50**.

**Scope:**
- Airframe structures (fuselage, wings, stabilizers)
- GSE structural equipment (frames, stands, docks)
- Physical support structures
- Structural mounting and attachment points

**Examples:**
- `50-00-00_CARGO_AND_ACCESSORY_COMPARTMENTS` - Cargo structures
- `53-00-00_FUSELAGE` - Fuselage structure
- `03-50-00_GENERAL_STRUCTURAL_GSE` - GSE structural equipment
- `03-50-01_LH2_SUPPORT_FRAMES` - LH₂ support frames and structures

#### 70-xx / 80-xx → ENGINES / PROPULSION / ENERGY
All **powerplant**, **propulsion systems**, **energy systems**, and **auxiliary power** originate from blocks **70** and **80**.

**Scope:**
- **70-xx**: Primary powerplant, engines, propulsion systems, H₂ fuel cells
- **80-xx**: Auxiliary power (APU, GPU, starting systems), ground energy systems

**Examples:**
- `70-00-00_STANDARD_PRACTICES_ENGINE` - Engine practices
- `71-00-00_POWER_PLANT` - Main powerplant
- `72-00-00_ENGINE` - Engine systems
- `80-00-00_STARTING` - Starting systems
- `03-80-00_GENERAL_ENERGY_GSE` - GSE energy systems
- `03-80-01_LH2_CRYOGENIC_REFUELER` - LH₂ refueling energy system
- `03-80-02_HV_GROUND_POWER_UNIT` - High-voltage ground power

#### 90-xx → SCHEMAS / META / CATALOGS / TRAINING
All **schemas**, **metadata**, **catalogs**, **registries**, **training materials**, and **safety data** originate from block **90**.

**Scope:**
- Documentation schemas and templates
- Part catalogs (IPL/IPC)
- In-service registries
- Training materials and programs
- Safety Data Sheets (SDS)
- Configuration management
- Meta-governance documents

**Examples:**
- `91-00-00_CHARTS_FLIGHT_OPERATIONS` - Operational charts
- `92-00-00_MODEL_BASED_MAINTENANCE` - Maintenance models
- `93-00-00_ONBOARD_DATA_LOAD` - Data loading schemas
- `03-90-00_IN-SERVICE_REGISTRY` - GSE service registry
- `03-90-01_TRAINING_MATERIALS` - GSE training content
- `03-90-02_SAFETY_DATA_SHEETS` - SDS documents
- `03-90-10_FLEET_SPARES_PROGRAM` - Spares catalog/program
- `03-90-11_LH2_CRYO_REFUELER_PARTS` - LH₂ refueler parts catalog

### Application Rules

#### Rule 1: Domain-Specific Numbering
When creating subsystems within an ATA domain (e.g., ATA 03 Infrastructure), apply the origin blocks as **second-level codes**:

- `03-20-xx` for **systems** within infrastructure
- `03-50-xx` for **structures** within infrastructure
- `03-80-xx` for **energy/propulsion** within infrastructure
- `03-90-xx` for **schemas/catalogs** within infrastructure

#### Rule 2: Consistency Across Domains
The same origin blocks apply across **all OPT-IN axes** (O, P, T, I, N):

- **Organization (O)**: May use 20 (policies/systems), 90 (governance schemas)
- **Program (P)**: May use 20 (program systems), 50 (geometry/structures)
- **Technology (T)**: Full use of 20, 50, 70/80, 90 based on technology type
- **Infrastructures (I)**: As shown above (03-20, 03-50, 03-80, 03-90)
- **Neural Networks (N)**: May use 20 (AI systems), 90 (model catalogs/schemas)

#### Rule 3: No Random Numbering
**Do not** create intermediate blocks (10-xx, 30-xx, 40-xx, 60-xx) unless explicitly justified by:
1. An existing ATA standard requirement
2. A specific regulatory mandate
3. Documented program decision with traceability

**Always** map new codes to one of the four origin blocks (20, 50, 70/80, 90).

### Decision Tree for New Codes

When creating a new ATA code, ask:

1. **Is it a functional system or operational process?** → Use **20-xx**
2. **Is it a physical structure or airframe component?** → Use **50-xx**
3. **Is it related to engines, propulsion, or energy?** → Use **70-xx** or **80-xx**
4. **Is it a schema, catalog, training, or meta-document?** → Use **90-xx**

If multiple categories apply, prioritize based on **primary function**:
- If it's primarily structural with energy aspects → **50-xx** (structure is primary)
- If it's primarily energy with structural supports → **70/80-xx** (energy is primary)
- If it's documentation/training about a system → **90-xx** (meta is primary)

### Examples of Correct Mapping

| Item | Wrong Code | Correct Code | Reason |
|------|-----------|--------------|---------|
| Fleet maintenance program | `03-40-00` | `03-20-10` | It's a system (20), not random 40 |
| LH₂ refueler parts catalog | `03-40-01` | `03-90-11` | It's a catalog/IPC (90), not 40 |
| GSE support frame | `03-30-01` | `03-50-01` | It's a structure (50), not 30 |
| Ground power unit | `03-60-01` | `03-80-02` | It's energy equipment (80), not 60 |
| Training materials | `03-10-00` | `03-90-01` | It's training/meta (90), not 10 |

---

## Content Requirements

### Every Folder Must Have
1. **README.md** - Folder overview and contents
2. **Status indicator** - Development, Draft, Active, Deprecated
3. **Related documents** - Links to parent/child/sibling documentation
4. **Standards references** - Applicable ATA, EASA, FAA standards

### Pending Content
If content is not yet developed:
- ✅ **DO** create the folder structure
- ✅ **DO** add a README.md with placeholder text
- ✅ **DO** mark status as "Pending Development"
- ✅ **DO** describe what should be in the folder
- ❌ **DON'T** leave folders empty without README
- ❌ **DON'T** skip mandatory folders

---

## OPT-IN Framework Integration

The XX-00-00_GENERAL structure integrates with the OPT-IN framework axes:

### O - Organization
ATA chapters: 00-05, 100-series
- Policies, certification, governance, maintenance

### P - Program
ATA chapters: 06-12
- Geometry, mission, configuration, performance

### T - Technology
ATA chapters: 20-99 (following A-M-E-D-E-O-P-E-L-I-C-C-I₂-A₂ taxonomy)
- On-board systems and technologies

### I - Infrastructures
ATA chapters: 02, 03, 10, 13, 85-90, 115-116
- Airports, supply chain, GSE, data centers

### N - Neural Networks
ATA chapters: 40, 92, 95
- AI, machine learning, CAOS, Digital Product Passport

---

## CAOS Integration

All systems should consider CAOS (Computer-Aided Operations & Services) integration:

- **Product-as-Intelligent-Service (PaaSI)** approach
- **Digital Product Passport (DPP)** data collection
- **Service Twin / Digital Twin** simulation
- **Federated Learning** for fleet intelligence
- **Predictive maintenance** capabilities
- **Real-time optimization** strategies

---

## Standards Compliance

### Regulatory Standards
- **EASA CS-25** - Certification Specifications for Large Aeroplanes
- **FAA 14 CFR Part 25** - Airworthiness Standards
- **DO-178C** - Software Considerations in Airborne Systems
- **DO-254** - Design Assurance Guidance for Airborne Electronic Hardware
- **DO-160** - Environmental Conditions and Test Procedures
- **ARP4754A** - Guidelines for Development of Civil Aircraft and Systems
- **ARP4761** - Guidelines and Methods for Conducting Safety Assessment Process

### Documentation Standards
- **ATA iSpec 2200** - Information Standards for Aviation Maintenance
- **S1000D** - International specification for technical publications
- **ATA 100** - Specification for Manufacturers' Technical Data

### AI/ML Standards (for ATA 95 and related systems)
- **ISO/IEC 5338** - AI System Lifecycle Processes
- **ISO/IEC 23894** - AI Risk Management
- **IEEE P2863** - Recommended Practice for Organizational Governance of AI
- **EUROCAE ED-202A** - Guidelines for Approval of AI in Aviation

---

## Traceability Requirements

All documentation must maintain traceability:

1. **Upward Traceability** - Requirements to stakeholder needs
2. **Downward Traceability** - Requirements to design, implementation, tests
3. **Horizontal Traceability** - Between related systems and interfaces
4. **Bidirectional Traceability** - Change impact analysis

### Traceability Matrix
Each system should maintain:
- Requirements Traceability Matrix (RTM)
- Verification Cross-Reference Matrix (VCRM)
- Safety Requirements Traceability
- Interface Dependencies Map

---

## Implementation Checklist

When implementing XX-00-00_GENERAL for a new ATA chapter:

- [ ] Create `XX-00-00_GENERAL` directory
- [ ] Create main `README.md` with system overview
- [ ] Create all 14 mandatory subfolders (01-14)
- [ ] Add `README.md` to each subfolder with purpose and placeholder content
- [ ] Document folder structure in main README
- [ ] List applicable standards and compliance requirements
- [ ] Add integration points with other ATA chapters
- [ ] Link to OPT-IN framework axis
- [ ] Reference CAOS components (if applicable)
- [ ] Set development status indicators
- [ ] Create initial traceability links
- [ ] Review against ATA 95-00-00 canonical pattern

---

## Automation and Tools

### Implementation Script
Location: `/tmp/implement_general_structure.py`

This script automatically creates the XX-00-00_GENERAL structure for ATA chapters. Use it to ensure consistency.

### Validation
Future tools will validate:
- Folder structure completeness
- Naming convention compliance
- README presence in all folders
- Traceability link integrity
- Standards reference completeness

---

## Continuous Improvement

This standard is a living document. Updates should be:

1. **Proposed** through issue or pull request
2. **Reviewed** by documentation working group
3. **Approved** by technical authority
4. **Implemented** across all affected ATA chapters
5. **Version controlled** with clear change log

---

## References

### Primary References
- [ATA 95-00-00_GENERAL](./OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95_NEURAL_NETWORKS/95-00-00_GENERAL/) - Canonical reference pattern
- [OPT-IN Framework](./OPT-IN_FRAMEWORK/README.md) - Program structure
- [CAOS Manifesto](./CAOS/CAOS_MANIFESTO.md) - Operations framework

### Standards Documents
- ATA iSpec 2200 - Available from ATA Spec 2200
- S1000D - Available from S1000D website
- DO-178C, DO-254, DO-160 - Available from RTCA
- CS-25 - Available from EASA
- 14 CFR Part 25 - Available from FAA

---

## Document Control

| Version | Date       | Author                  | Changes                            |
|---------|------------|-------------------------|------------------------------------|
| 1.1     | 2025-11-12 | AMPEL360 Implementation | Added ATA Code Numbering Convention (Law of Origin) - defines 20/50/70-80/90 blocks |
| 1.0     | 2025-11-12 | AMPEL360 Implementation | Initial documentation standard     |

---

## Contact

For questions, clarifications, or suggestions regarding this documentation standard:

- **Technical Lead:** AMPEL360 Program Documentation Team
- **Repository:** [AMPEL360-BWB-H2-Hy-E](https://github.com/AmedeoPelliccia/AMPEL360-BWB-H2-Hy-E)
- **Issues:** Use GitHub Issues for documentation standard questions

---

*This document is part of the AMPEL360-BWB-H₂-Hy-E program documentation.*
