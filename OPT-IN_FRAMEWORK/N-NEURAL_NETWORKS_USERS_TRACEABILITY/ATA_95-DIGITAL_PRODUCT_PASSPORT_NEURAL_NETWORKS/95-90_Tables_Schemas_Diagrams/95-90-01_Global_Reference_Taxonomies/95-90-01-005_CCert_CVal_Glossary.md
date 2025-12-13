# 95-90-01-005 — CCert/CVal Glossary and Acronyms

## 1. Purpose

This document provides a comprehensive glossary and acronyms reference for the **Continuous Certification (CCert)** and **Continuous Validation (CVal)** framework within the AMPEL360 BWB H₂ Hy-E program. It defines the ontological lifecycle from static design (AM) through predictive passport (DPP) to operational reality (OM) and validation (OAV), culminating in the Digital Twin (DT) and continuous loops.

## 2. Table of Principal Acronyms

| Acronym    | Full Name                                                   | Layer / Domain         | Brief Definition                                                                                                                                                          |
|------------|-------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AM**     | Aircraft Manual / At-Rest Model                             | Design (static)        | Describes what the system is at rest: architecture, configuration, maintainability, limits. It is the static ontology.                                                     |
| **DV**     | Design Validation                                           | Design validation      | Process that validates the AM and converts it into a coherent, complete, and certifiable design. It is the filter that enables creating a reliable DPP.                    |
| **DPP**    | Digital Product Passport                                    | Identity + prediction  | Sovereign digital passport: identifies the product (physical/digital), establishes its capabilities, limits, and expected behavior. It is the predictive ontology.         |
| **OM**     | Ontological Mission                                         | Operation              | System behavior during real mission. It is the enacted ontology: what the system is when operating in its real context.                                                   |
| **OAV**    | On-Aircraft Validation                                      | On-aircraft validation | Validation that the real OM (on aircraft, in operation) matches what the DPP predicted. Empirical truth.                                                                   |
| **DT**     | Digital Twin (Ontogenetic)                                  | Digital twin           | Digital twin built not only from design but from operational ontogenesis (OM + OAV). Dynamic identity of the system.                                                      |
| **CCert**  | Continuous Certification                                    | Certification loop     | Continuous loop AM→DV→DPP→OM→OAV→DT→AM' that keeps the system permanently certifiable.                                                                                    |
| **CVal**   | Continuous Validation                                       | Validation loop        | Continuous validation from operational evidence (OM + OAV) that feeds DT and future versions of AM/DPP.                                                                    |
| **ATA 95** | Digital Product Passport & Neural Networks                  | ATA Chapter            | ATA chapter created to house DPP, NN, traceability, and all digital/AI grammar within the ATA framework.                                                                  |
| **UTCS**   | Universal Traceability & Circularity Standard               | Traceability           | Backbone standard for traceability, states, tokens, and connections between AM, DPP, OM, OAV, DT, and lifecycles.                                                         |

## 3. Extended Glossary

### 3.1 AM — Aircraft Manual / At-Rest Model

**Document / model describing the system at rest:**

- Physical and logical architecture
- Interfaces, configurations, LRUs (Line Replaceable Units)
- Maintainability, inspections, substitutions
- Design limits and constraints

**AM is the static ontology**: "what I am" before operating.

The AM defines the baseline from which all other artifacts derive. It captures the design intent, engineering specifications, and structural composition of the system in its non-operational state.

---

### 3.2 DV — Design Validation

**Layer of validation by design:**

- Verifies that AM is coherent, complete, and certifiable
- Checks requirements, interfaces, limits, architecture
- Guarantees that the design can generate consistent predictions

**DV transforms AM → DPP.**
It is the "ontological compiler" of design.

Design Validation ensures that before a system moves to operational prediction, its foundational design has been rigorously validated against requirements, standards (e.g., CS-25, DO-178C), and architectural constraints.

---

### 3.3 DPP — Digital Product Passport

**Sovereign passport of the product:**

- Unique identity (UUID, name, version)
- Capabilities, restrictions, ODD (Operational Design Domain) / conditions
- Interfaces, dependencies, datasets, SBOM (Software Bill of Materials), CMM (Configuration Management Matrix), etc.
- Certification status and traceability

**DPP is the predictive ontology:**
**The DPP predicts how the operational behavior (OM) will be.**

The DPP serves as the authoritative digital identity and capability declaration for a system or component. It bridges static design and dynamic operation by establishing expectations that can be validated in real-world use.

**References:**
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206) (Digital identity and transparency requirements)
- [ATA 95 Framework](../) (Digital Product Passport structure)

---

### 3.4 OM — Ontological Mission

**Layer of ontological mission:**

- Describes how the system actually manifests in operation
- Modes, transitions, behaviors, degradations
- Interactions with context (environment, crew, other systems)

**OM = the ontogenesis of the system:**
It is the moment when it "becomes" what it is, in the real world.

The Ontological Mission represents the system's lived experience—its behavior under actual operational conditions, environmental influences, and real-world constraints. It is where theory meets practice.

---

### 3.5 OAV — On-Aircraft Validation

**Validation on real aircraft:**

- Flight tests, data campaigns, controlled real operation
- Compares real OM with what the DPP predicted
- Generates the "verifiable truth" of the system

**Only the uniqueness of the operational context can validate the prediction of the DPP.**
That is OAV.

On-Aircraft Validation provides empirical evidence that the system performs as predicted. It closes the loop between design prediction (DPP) and operational reality (OM), producing data that confirms or refines the model.

**References:**
- [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) (System design and analysis)
- [EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012) (Certification procedures)

---

### 3.6 DT — Digital Twin (Ontogenetic)

**Digital twin built from:**

- Design (AM, DPP)
- Operational evidence (OM + OAV)

**Not just a static model + telemetry:**
It is the **ontogenetic accumulation** of everything the system has been in operation.

**DT = living synthesis of design + validated operation.**

The Digital Twin is a continuously evolving representation that integrates design baseline, operational history, validation data, and predictive models. It enables predictive maintenance, performance optimization, and informed decision-making throughout the system lifecycle.

---

### 3.7 CCert — Continuous Certification

**Continuous certification loop:**

> AM → DV → DPP → OM → OAV → DT → AM'

Each cycle of the loop:

- Reaffirms the design
- Corrects the prediction
- Integrates new evidence
- Updates the AM
- Produces a new DPP

Certification ceases to be a one-time event and becomes a **living, cyclical, and ontological process.**

Continuous Certification aligns with modern regulatory trends toward continuous airworthiness and evidence-based certification. It enables incremental improvements and rapid incorporation of operational learnings.

**References:**
- [DO-178C](https://www.rtca.org/content/standards-guidance-materials) (Software considerations in airborne systems)
- [DO-254](https://www.rtca.org/content/standards-guidance-materials) (Hardware considerations)
- [EASA AI Roadmap 2.0](https://www.easa.europa.eu/en/domains/innovation-digital/artificial-intelligence/easa-ai-roadmap) (Continuous certification concepts)

---

### 3.8 CVal — Continuous Validation

**Dimension of continuous validation within the loop:**

- OM and OAV provide real evidence
- DT consolidates that evidence
- That evidence feeds the next version of AM and DV

**CVal = continuous flow of verifiable truth** that sustains CCert.

Continuous Validation ensures that the certification loop is grounded in empirical data. It transforms operational experience into validated knowledge that informs future design iterations.

---

### 3.9 ATA 95 — Digital Product Passport & Neural Networks

**ATA chapter that defines:**

- Primary home of DPP
- Registration and governance of NN models
- Integration with other ATA chapters (27 Flight Controls, 31 Recording, 70 Propulsion, etc.)
- Buckets 95-20/30/40/50/60/70/80/90 for subsystems, circulars, software, structures, energy, tables, schemas…

**ATA 95 becomes the official domain of intelligence and certifiable digital identity** of the system.

This chapter establishes the organizational structure for all digital product passport information, neural network documentation, and AI/ML system traceability within the ATA framework.

**References:**
- [ATA iSpec 2200](https://www.ata.org/resources/specifications) (Standard numbering system)
- [ATA 95 Documentation](../) (Internal framework)

---

### 3.10 UTCS — Universal Traceability & Circularity Standard

**Framework for:**

- Universal traceability (model, data, energy, materials)
- Circularity (closed loops, CO₂, H₂, energy, DPP)
- Tokens / states / events (CADET, QAUDIT, etc.)

**UTCS is the mesh** that connects AM, DPP, OM, OAV, DT, CCert, and CVal.

The Universal Traceability & Circularity Standard provides the underlying infrastructure for tracking, auditing, and managing all aspects of the system lifecycle—from materials and energy flows to data provenance and model versions.

---

## 4. The Axiom Principle

> **AM defines the DPP.**
> **The DPP predicts the OM.**
> **Only the uniqueness of the operational context (OAV) can validate that prediction.**
> **DT accumulates that truth and the CCert/CVal loop updates the AM again.**

This axiom encapsulates the complete lifecycle philosophy:

1. **Design foundation** (AM) → establishes what the system is
2. **Validated design** (DV) → confirms design integrity
3. **Predictive identity** (DPP) → declares expected behavior
4. **Operational reality** (OM) → manifests actual behavior
5. **Empirical validation** (OAV) → verifies prediction against reality
6. **Accumulated knowledge** (DT) → synthesizes design and operation
7. **Continuous improvement** (CCert/CVal) → closes the loop for next iteration

---

## 5. Lifecycle Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                   CONTINUOUS CERTIFICATION LOOP                  │
└─────────────────────────────────────────────────────────────────┘

    ┌──────┐
    │  AM  │  Aircraft Manual / At-Rest Model
    │      │  (Static Ontology)
    └───┬──┘
        │
        ↓
    ┌───┴──┐
    │  DV  │  Design Validation
    │      │  (Ontological Compiler)
    └───┬──┘
        │
        ↓
    ┌───┴──┐
    │ DPP  │  Digital Product Passport
    │      │  (Predictive Ontology)
    └───┬──┘
        │
        ↓
    ┌───┴──┐
    │  OM  │  Ontological Mission
    │      │  (Enacted Ontology)
    └───┬──┘
        │
        ↓
    ┌───┴──┐
    │ OAV  │  On-Aircraft Validation
    │      │  (Empirical Truth)
    └───┬──┘
        │
        ↓
    ┌───┴──┐
    │  DT  │  Digital Twin (Ontogenetic)
    │      │  (Living Synthesis)
    └───┬──┘
        │
        ↓
    ┌───┴──┐
    │ AM'  │  Updated Aircraft Manual
    │      │  (Next Iteration)
    └───┬──┘
        │
        └──────→ (Loop continues)

        ┌─────────────────────────────┐
        │  Supported by CVal & UTCS   │
        │  Governed by ATA 95         │
        └─────────────────────────────┘
```

---

## 6. Cross-References

### 6.1 Related ATA 95 Documents

- [95-00-00 — ATA 95 Overview](../../95-00_General/)
- [95-20 — Subsystems and Neural Networks](../../95-20_Subsystems/)
- [95-40 — Software and AI Lifecycle](../../95-40_Software/)
- [95-90-02 — Global Data Schemas](../95-90-02_Global_Data_Schemas/)
- [95-90-04 — Global Traceability Tables](../95-90-04_Global_Traceability_Tables/)

### 6.2 External Standards References

- **CS-25** (Certification Specifications for Large Aeroplanes): [EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
- **DO-178C** (Software Considerations in Airborne Systems): [RTCA DO-178C](https://www.rtca.org/content/standards-guidance-materials)
- **DO-254** (Design Assurance Guidance for Airborne Electronic Hardware): [RTCA DO-254](https://www.rtca.org/content/standards-guidance-materials)
- **EU AI Act**: [EU Regulation on AI](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)
- **EASA AI Roadmap 2.0**: [EASA AI Certification](https://www.easa.europa.eu/en/domains/innovation-digital/artificial-intelligence/easa-ai-roadmap)
- **EASA Part 21** (Certification Procedures): [EASA Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)

### 6.3 Internal Framework References

- [AM_Q100.json](../../../../../../examples/am_aircraft_model/AM_Q100.json) — Example Aircraft Manual for Q100
- [OPT-IN Framework Overview](../../../../)
- [UTCS Documentation](../95-90-04_Global_Traceability_Tables/)

---

## 7. Usage Guidelines

### 7.1 For System Designers

When creating new system documentation:

1. Start with **AM** — Define the static architecture and constraints
2. Apply **DV** — Validate design completeness and certification readiness
3. Create **DPP** — Generate the predictive passport with expected behaviors
4. Reference this glossary for consistent terminology

### 7.2 For Certification Engineers

When preparing certification evidence:

1. Use **CCert** framework to structure continuous certification approach
2. Ensure **OAV** data is captured during flight tests
3. Link evidence to **DPP** predictions and **OM** actuals
4. Feed learnings back through **CVal** process

### 7.3 For Operations and Maintenance

When managing operational systems:

1. Consult **DPP** for authorized operating conditions and limits
2. Report **OM** deviations for **CVal** analysis
3. Utilize **DT** for predictive maintenance insights
4. Support **CCert** loop with operational data

---

## 8. Version History

| Version | Date       | Author              | Changes                          |
|---------|------------|---------------------|----------------------------------|
| 1.0     | 2025-12-13 | GitHub Copilot      | Initial glossary creation        |

---

## 9. Document Control

- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by [Approver]
- **Status**: DRAFT – Subject to human review and approval.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Standard**: OPT-IN Framework v1.2
- **ATA Chapter**: 95 (Digital Product Passport and Neural Networks)
- **Bucket**: 90_Tables_Schemas_Diagrams
- **Sub-bucket**: 01_Global_Reference_Taxonomies
- **Document ID**: 95-90-01-005
- **Last AI update**: 2025-12-13

---

## 10. Notes

This glossary is a living document that will evolve as the CCert/CVal framework matures through operational experience. It serves as the authoritative reference for terminology across all AMPEL360 documentation and should be consulted when ambiguity arises regarding the ontological lifecycle of systems and components.

For questions or clarifications, contact the AMPEL360 Data Architecture Working Group.

---

**End of Document**
