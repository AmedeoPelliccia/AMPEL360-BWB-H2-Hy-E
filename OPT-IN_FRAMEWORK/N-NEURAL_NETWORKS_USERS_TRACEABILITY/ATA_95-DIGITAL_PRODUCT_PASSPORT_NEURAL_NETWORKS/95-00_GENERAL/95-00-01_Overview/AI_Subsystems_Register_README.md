# AI-Based Systems Register for DS.AI Compliance

## Purpose

This register serves as the **single source of truth** for all AI-based subsystems within the AMPEL360 BWB H₂ Hy-E aircraft program, providing comprehensive classification and traceability for DS.AI (EASA AI Safety Guideline) compliance.

## Document ID

**Document ID**: 95-00-01-010  
**Version**: 1.0  
**Status**: DRAFT  
**Last Updated**: 2025-11-23

## Scope

The AI Subsystems Register catalogs all systems incorporating artificial intelligence, machine learning, or neural network technologies across:

- **Airborne Systems**: On-board neural networks and AI components
- **Ground Systems**: Ground operations, maintenance, and support systems with AI
- **Enterprise Systems**: Development, documentation, and certification tools with AI assistance

## Register Structure

The register (`AI_Subsystems_Register.csv`) contains the following columns:

### Identification and Classification

- **AI_ID**: Unique short identifier (e.g., `NN-ECS`, `OPS-GOPS`, `DOC-META-ENF`)
- **Name**: Human-readable subsystem name
- **ATA_Chapter**: Primary ATA chapter allocation
- **Domain**: `AIRBORNE` / `GROUND` / `ENTERPRISE` / `MIXED`
- **Location**: Physical or logical deployment location

### Functional Description

- **Primary_Function**: Core AI capability and purpose
- **End_User**: Primary users or consumers of the AI system
- **AI_Tech**: AI technology classification
  - `Supervised`: Supervised learning models
  - `Unsupervised`: Unsupervised learning (clustering, anomaly detection)
  - `Reinforcement`: Reinforcement learning
  - `Hybrid`: Combination of techniques
  - `LLM-assist`: Large Language Model assistance
  - `Rule-based`: Rule-based AI
  - `Platform`: Infrastructure/runtime platform

### Safety and Regulatory Classification

- **Safety_Component**: `YES` / `NO` - Meets EU AI Act "safety component" definition
- **Hazard_Contribution**: Hazard classification per typical aerospace FHA
  - `H1`: Catastrophic (loss of aircraft, multiple fatalities)
  - `H2`: Hazardous (large reduction in safety margins, serious injuries)
  - `H3`: Major (significant reduction in safety margins, passenger discomfort)
  - `H4`: Minor (slight reduction in safety margins, inconvenience)
  - `H5`: No safety effect (administrative, business impact only)

### DS.AI Classification

- **AI_Level_DS.AI**: AI system level per DS.AI guideline
  - `1A`: AI-assisted tools (development/verification)
  - `1B`: AI-based decision support systems
  - `2A`: AI constituent contributing to non-catastrophic hazards
  - `2B`: AI constituent contributing to potential catastrophic hazards (but mitigated)
  - Note: `3A/3B` (catastrophic unmitigated) are OUT of DS.AI scope

- **DS.AI_Scope**: `IN` / `OUT` with rationale
  - `IN`: Within DS.AI scope - follow DS.AI guidance
  - `OUT`: Outside DS.AI scope with reason (e.g., "catastrophic → DO-178C Level A", "business only")

- **AL_TQL**: Assurance Level (AL) and Test Quality Level (TQL) per DS.AI Tables 3, 4, 5
  - Format: `ALx / TQLx` or range (e.g., `AL2-AL3 / TQL2-TQL3`)
  - Higher levels = more stringent assurance requirements

### Operational Context

- **OD**: Operational Domain of the **system** (where it operates)
- **ODD**: Operational Design Domain of the **AI constituent** (trained/validated conditions)

### Traceability

- **Repo_Anchor**: Primary repository path for the subsystem
- **Status**: Development status
  - `Concept`: Initial concept phase
  - `Prototype`: Prototype/proof-of-concept
  - `In design`: Active design and development
  - `In operation`: Operational/deployed
- **Owner**: Responsible domain or team

## Usage Guidelines

### For System Engineers

1. **New AI System**: Add a new row to the register with all required fields
2. **Classification**: Carefully assess safety criticality and hazard contribution
3. **DS.AI Triage**: Determine if system is IN or OUT of DS.AI scope
4. **AL/TQL Allocation**: For IN-scope systems, assign AL/TQL per DS.AI Tables 3-5

### For Certification Engineers

1. **DS.AI Compliance Package**: For each IN-scope system, ensure existence of:
   - ConOps (DS.AI.100)
   - OD/ODD Specification (DS.AI.120)
   - Risk Assessment (DS.AI.130)
   - Ethics Assessment (DS.AI.140)
   - Intended Behaviour & Learning Assurance (DS.AI.150)
   - Continuous Risk Assessment plan (DS.AI.160)
   - Human-Centred Design evidence (DS.AI.170)

2. **Verification**: Verify AL/TQL allocation matches hazard contribution
3. **Traceability**: Ensure linkage between register entries and compliance artifacts

### For Documentation

- **Markdown Generation**: Generate tables from CSV for inclusion in documentation
- **Dashboard Updates**: Update project dashboards with register statistics
- **Gap Analysis**: Identify systems needing DS.AI compliance packages

## DS.AI Scope Decision Criteria

### IN Scope (DS.AI Applicable)

✅ AI Level 1A (AI-assisted tools)
✅ AI Level 1B (Decision support systems)
✅ AI Level 2A (AI constituent, non-catastrophic hazards)
✅ AI Level 2B (AI constituent, mitigated catastrophic potential)

### OUT of Scope (Alternative Guidance Required)

❌ **Catastrophic Unmitigated**: AI contributing directly to H1 catastrophic hazards without sufficient mitigation
   - → Apply DO-178C Level A + dedicated AI safety guidance (future standards)
   - Examples: `NN-FCTL` (flight controls), `NN-PROP` (propulsion)

❌ **Business-Only**: No safety component, purely commercial
   - → Not subject to safety-related AI regulation under DS.AI
   - Examples: `OPS-PAX` (passenger experience), `OPS-PRED` (network planning - strategic only)

## Key Statistics (Current Register)

- **Total AI Systems**: 31
- **Airborne**: 13 (neural network subsystems)
- **Ground**: 11 (operations and infrastructure)
- **Enterprise**: 4 (tools and assistants)
- **Mixed Domain**: 3 (airborne+ground hybrid)

### By DS.AI Scope
- **IN Scope**: 23 systems (primary classification)
- **OUT Scope**: 5 systems (2 catastrophic, 2 business-only, 1 conditional)
- **Mixed/Split**: 3 systems (context-dependent classification)

### By Safety Classification
- **Safety Components**: 21 systems
- **Non-Safety/Advisory**: 12 systems

### By AI Level
- **1A (Tools)**: 5 systems
- **1B (Decision Support)**: 8 systems
- **2A (Non-Catastrophic)**: 14 systems
- **2B (Mitigated Catastrophic)**: 6 systems

## Maintenance and Updates

- **Review Frequency**: Quarterly or upon addition of new AI systems
- **Owner**: NN Platform & Integration Domain (primary) + Domain owners (respective systems)
- **Approval**: Chief Engineer + Certification Manager for DS.AI scope changes

## Related Documents

- [EASA First Usable Guidance for Level 1 & 2 Machine Learning Applications](https://www.easa.europa.eu/en/document-library/general-publications/easa-concept-paper-first-usable-guidance-level-1-machine) - EASA AI Guidance
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) - Official EU legislation
- `95-00-01-002_Regulatory_and_Standards_Context.md` - Regulatory framework overview
- `95-00-01-004_DPP_Objectives_for_Neural_Networks.md` - DPP objectives
- Individual subsystem documentation under respective `95-20-XX_*` and `02-20-XX_*` directories

## Next Steps

For each IN-scope system requiring DS.AI compliance package:

1. **ConOps Development**: Define concept of operations per DS.AI.100
2. **OD/ODD Specification**: Document operational domain and design domain per DS.AI.120
3. **FHA & Risk Assessment**: Complete functional hazard assessment per DS.AI.130
4. **AL/TQL Allocation**: Formalize assurance and test quality levels
5. **Ethics Review**: Complete ethics assessment per DS.AI.140
6. **Learning Assurance Plan**: Define ML-specific V&V approach per DS.AI.150
7. **Continuous Monitoring**: Establish continuous risk assessment per DS.AI.160
8. **HCD Evidence**: Document human-centered design considerations per DS.AI.170

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval by Chief Engineer and Certification Manager.
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-23

---

## Appendix A: DS.AI AL/TQL Quick Reference

### From DS.AI Table 3 (AI Level 1A - Tools)

| AL | TQL | Description |
|----|-----|-------------|
| AL1-AL6 | TQL1-TQL6 | Varies by tool criticality and usage context |

Typical: **TQL5-TQL6** for development/documentation tools

### From DS.AI Table 4 (AI Level 1B - Decision Support)

| Hazard | AL | TQL |
|--------|----|----|
| H3-H5 | AL4-AL6 | TQL4-TQL6 |

### From DS.AI Table 5 (AI Level 2A/2B - AI Constituents)

| Hazard | AI Level | AL | TQL |
|--------|----------|----|----|
| H3 | 2A | AL3 | TQL3 |
| H2 | 2A/2B | AL2-AL3 | TQL2-TQL3 |
| H1 (mitigated to H2) | 2B | AL2 | TQL2 |

**Note**: H1 catastrophic without mitigation → OUT of DS.AI scope

## Appendix B: Hazard Classification Criteria

### H1 - Catastrophic
- Loss of aircraft
- Multiple fatalities
- Examples: Loss of flight control, uncontained engine failure, structural failure

### H2 - Hazardous  
- Large reduction in safety margins or functional capabilities
- Serious or fatal injury to small number of persons
- Examples: Emergency landing required, multiple system failures

### H3 - Major
- Significant reduction in safety margins or functional capabilities
- Physical discomfort to passengers/crew
- Examples: Single system failure with degraded operation, passenger discomfort

### H4 - Minor
- Slight reduction in safety margins
- Physical inconvenience
- Examples: Increased crew workload, passenger inconvenience

### H5 - No Safety Effect
- No impact on safety
- Examples: Administrative burden, business efficiency only
