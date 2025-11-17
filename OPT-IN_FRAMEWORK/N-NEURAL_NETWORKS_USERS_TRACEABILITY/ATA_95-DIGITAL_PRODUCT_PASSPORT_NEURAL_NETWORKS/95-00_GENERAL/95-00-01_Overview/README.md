# 95-00-01_Overview

## Purpose

This folder provides a comprehensive overview of the Digital Product Passport (DPP) framework for neural networks and AI systems in the AMPEL360 BWB H₂ Hy-E Q100 aircraft program. It establishes the foundation, context, and governance structure for all DPP activities within ATA Chapter 95.

## Scope

This folder is part of the **95-00_GENERAL** layer, which provides governance and lifecycle management for ATA Chapter 95 — Digital Product Passport Neural Networks.

The Overview section covers:
- DPP purpose, objectives, and strategic alignment
- Regulatory and standards context
- Key concepts, terminology, and definitions
- Lifecycle coverage across all 14 GENERAL folders
- Organizational roles and responsibilities
- Data model, identifiers, and information architecture
- Scope boundaries, limitations, and exclusions

## Contents

### Documentation

This folder contains eight comprehensive documents that establish the DPP framework:

1. **[95-00-01-001_DPP_Purpose_and_Scope.md](95-00-01-001_DPP_Purpose_and_Scope.md)**
   - Purpose of the Digital Product Passport for neural networks
   - Systems coverage (flight control, predictive maintenance, energy orchestration, etc.)
   - Lifecycle phases addressed
   - Intended users and stakeholders
   - Relationship to aircraft-level passport

2. **[95-00-01-002_Regulatory_and_Standards_Context.md](95-00-01-002_Regulatory_and_Standards_Context.md)**
   - EU Digital Product Passport framework (ESPR, Battery Regulation, AI Act)
   - Aviation certification standards (EASA CS-25, FAA 14 CFR Part 25)
   - AI/ML lifecycle standards (ISO/IEC 5338, 23053, 24029)
   - Safety standards (ARP 4754A, ARP 4761)
   - Data exchange and cybersecurity standards
   - AMPEL360 compliance strategy

3. **[95-00-01-003_DPP_Key_Concepts_and_Definitions.md](95-00-01-003_DPP_Key_Concepts_and_Definitions.md)**
   - Core terminology (DPP, neural network, ML model)
   - AI/ML system concepts (training data, validation, inference)
   - Lifecycle concepts (versioning, lineage, ODD, model drift)
   - Safety and assurance concepts (explainability, robustness, certification credit)
   - Data and information concepts (data modules, digital twins, traceability)
   - Environmental concepts (carbon footprint, transfer learning, model retirement)
   - Comprehensive acronyms and abbreviations

4. **[95-00-01-004_DPP_Objectives_for_Neural_Networks.md](95-00-01-004_DPP_Objectives_for_Neural_Networks.md)**
   - Strategic objectives (regulatory approval, accelerated development, operational safety)
   - Technical objectives (traceability, reproducibility, knowledge transfer, interoperability)
   - Business objectives (cost reduction, competitive differentiation, supply chain collaboration)
   - Sustainability objectives (environmental footprint, circular economy, ethical AI)
   - Compliance objectives and KPIs
   - Implementation roadmap and phasing

5. **[95-00-01-005_DPP_Lifecycle_Coverage.md](95-00-01-005_DPP_Lifecycle_Coverage.md)**
   - Mapping to 14-folder GENERAL structure (95-00-01 through 95-00-14)
   - Detailed coverage for each lifecycle stage
   - Entry/exit criteria for each phase
   - DPP state transitions
   - Cross-cutting activities (documentation, traceability, stakeholder engagement)
   - Example lifecycle evolution for a flight control neural network

6. **[95-00-01-006_DPP_Roles_and_Responsibilities.md](95-00-01-006_DPP_Roles_and_Responsibilities.md)**
   - Executive leadership roles (Chief AI Officer, CTO, Program Manager)
   - AI/ML engineering roles (Lead AI Engineer, ML Engineer, Data Engineer, MLOps Engineer)
   - Safety and assurance roles (AI Safety Engineer, V&V Engineer, AI Ethics Officer)
   - Certification and regulatory roles (Certification Manager, Regulatory Affairs Specialist)
   - Configuration and quality management roles
   - Operational roles (Aircraft Operator, MRO)
   - Governance bodies (AI Steering Committee, Change Control Board, Safety Board, Ethics Board)
   - RACI matrix and training requirements

7. **[95-00-01-007_DPP_Data_Model_and_Identifiers.md](95-00-01-007_DPP_Data_Model_and_Identifiers.md)**
   - UUID-based identification scheme
   - Semantic versioning (MAJOR.MINOR.PATCH)
   - Comprehensive JSON data model schema (metadata, architecture, training, validation, certification, operations)
   - Data formats (JSON, XML, YAML, Protobuf)
   - Database storage (relational and graph databases)
   - RESTful and GraphQL APIs
   - Data integrity, security, and version control
   - Data retention and archival policies

8. **[95-00-01-008_DPP_Scope_Limitations_and_Exclusions.md](95-00-01-008_DPP_Scope_Limitations_and_Exclusions.md)**
   - Systems included in DPP scope
   - Systems explicitly excluded (conventional software, COTS AI tools, simple statistical models)
   - Lifecycle stages with partial coverage
   - Data elements not included (raw training data, model weights, proprietary algorithms)
   - Functional limitations (not real-time monitoring, not automated updates)
   - Geographic and temporal limitations
   - Known gaps and future enhancements
   - Stakeholder communication and escalation process

### Visual Assets

The **ASSETS/** folder contains diagrams and visual aids:

- **95-00-01-OVW-001_DPP_Overview_Diagram.png** (placeholder)
  - Comprehensive overview of DPP framework
  - Lifecycle stages and stakeholder interactions
  - Data flows and integration points

- **95-00-01-OVW-002_DPP_Entity_Relationship.svg** (placeholder)
  - Entity-relationship diagram for DPP data model
  - Core entities and their relationships
  - Traceability structure

> **Note**: Visual assets are currently placeholders. Final diagrams to be created by technical illustrators following AMPEL360 documentation standards.

## Navigation

### Reading Order

For first-time readers, we recommend reading the documents in sequence:

1. Start with **Purpose and Scope** to understand the "why"
2. Review **Regulatory Context** to understand compliance drivers
3. Study **Key Concepts** to establish common vocabulary
4. Read **Objectives** to understand strategic goals
5. Explore **Lifecycle Coverage** to see end-to-end process
6. Review **Roles and Responsibilities** to understand organizational structure
7. Study **Data Model** to understand technical implementation
8. Finally, review **Limitations and Exclusions** to understand boundaries

### Quick Reference

- **For Executives**: Read 95-00-01-001 (Purpose) and 95-00-01-004 (Objectives)
- **For Certification Authorities**: Read 95-00-01-002 (Regulatory Context) and 95-00-01-005 (Lifecycle Coverage)
- **For ML Engineers**: Read 95-00-01-003 (Concepts), 95-00-01-006 (Roles), and 95-00-01-007 (Data Model)
- **For Safety Engineers**: Read 95-00-01-002 (Regulatory), 95-00-01-003 (Concepts), and 95-00-01-005 (Lifecycle)
- **For Auditors**: Read 95-00-01-008 (Scope Limitations) and 95-00-01-007 (Data Model)

## Status

- **Phase**: Overview
- **Lifecycle Position**: 01 of 14
- **Status**: Active
- **Completeness**: 100% (all 8 documents complete, visual assets pending)
- **Last Updated**: 2025-11-17

## Related Folders

Part of the canonical 14-folder lifecycle:

1. **Overview** (this folder) → 2. Safety → 3. Requirements → 4. Design → 5. Interfaces → 6. Engineering → 7. V&V → 8. Prototyping → 9. Production Planning → 10. Certification → 11. EIS/Versions/Tags → 12. Services → 13. Subsystems/Components → 14. Ops/Std/Sustain

Each subsequent folder builds upon the foundation established in this Overview section.

## Key Takeaways

The Overview section establishes that:

✅ **Digital Product Passports are mandatory** for all neural networks and AI systems in AMPEL360 aircraft  
✅ **Regulatory compliance is paramount** — DPP framework aligns with EU DPP Regulation, AI Act, and aviation standards  
✅ **Full lifecycle coverage** from concept through retirement across all 14 GENERAL folders  
✅ **Clear roles and governance** with executive oversight, engineering ownership, and board-level governance  
✅ **Structured data model** using UUIDs, semantic versioning, and comprehensive JSON schema  
✅ **Balanced transparency** with clear scope boundaries respecting IP and privacy  

## Document Control

- **Standard**: OPT-IN Framework v1.1 (ATA 95 canonical template)
- **Owner**: AMPEL360 Documentation WG
- **Contributors**: AI Team, Certification Team, Safety Board, Regulatory Affairs
- **Approvers**: Chief AI Officer, Configuration Management Authority
- **Version**: 1.0
- **Date**: 2025-11-17
