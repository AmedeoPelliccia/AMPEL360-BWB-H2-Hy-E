# 23-96_AIR_SYNTECH_LANGUAGE — AST-L Technical Language

**Version:** 1.0  
**Date:** 2025-11-27  
**Status:** Draft  
**Related Standard:** AMPEL360-ASTL-SPEC-001

---

## Purpose

**AST-L (Air SynTech Language)** is the **native language of the intelligent aircraft** — a unified, computable, certifiable, and federated grammar that connects:

- ATA chapter systems
- OPT-IN Framework structure
- CAOS operational awareness
- ANCHORS sustainability metrics
- Digital Product Passport (DPP)
- AI/NN federated learning
- Aeronautical protocols

---

## Core Syntax

```astl
<entity> : <predicate> : <value> @<context> #<lifecycle>
```

### Examples

```astl
53-30-21_CO2Separator : flow_in : Air(kg/s=0.84) @CRUISE #L06_ENGINEERING
FAirCCC.A.Node4321 : sends : GradientEnvelope(v4) @eps=0.3 #L09_ML
CAOS.Event.SHMA.RivetF12 : severity : HIGH @INFLIGHT #L07_VV
DPP.Battery.0021 : carbon_origin : ANCHORS.CO2.Solid #L11_OPERATIONS
```

---

## Bucket Structure

```
23-96_AIR_SYNTECH_LANGUAGE/
├── 23-96-00_GENERAL/             # 14 lifecycle folders
│   ├── 23-96-00-01_Overview/
│   ├── 23-96-00-02_Safety/
│   ├── 23-96-00-03_Requirements/
│   ├── 23-96-00-04_Design/
│   ├── 23-96-00-05_Interfaces/
│   ├── 23-96-00-06_Engineering/
│   ├── 23-96-00-07_V_AND_V/
│   ├── 23-96-00-08_Prototyping/
│   ├── 23-96-00-09_Production_Planning/
│   ├── 23-96-00-10_Certification/
│   ├── 23-96-00-11_EIS_Versions_Tags/
│   ├── 23-96-00-12_Services/
│   ├── 23-96-00-13_Subsystems_Components/
│   └── 23-96-00-14_Ops_Std_Sustain/
├── 23-96-10_SEMANTICS/           # Entity types, domain ontologies
├── 23-96-20_SYNTAX/              # Grammar (EBNF), statement types
│   ├── 20-10_Core_Grammar/
│   ├── 20-20_Statement_Types/
│   └── 20-30_Expressions/
├── 23-96-30_SYNOPSIS/            # XAI, narrative engine
├── 23-96-40_TECHNOLOGY/          # Data types, protocols
├── 23-96-50_PROTOCOL_BINDINGS/   # ARINC 429, AFDX, CAN, Ethernet
│   ├── 50-10_ARINC_429/
│   ├── 50-20_AFDX/
│   ├── 50-30_CAN/
│   └── 50-40_ETHERNET/
├── 23-96-60_ONTOLOGY/            # OWL/RDF, SPARQL
├── 23-96-70_CERTIFICATION/       # Formal verification
├── 23-96-80_TOOLS/               # Parser, validator, CLI
└── 23-96-90_SCHEMAS/             # JSON/XML schemas
```

---

## Relationship with 23-95 COMM_NN

| Aspect | 23-95 COMM_NN | 23-96 AST-L |
|--------|---------------|-------------|
| **Focus** | What is transmitted | How to express it |
| **Content** | Gradients, models, envelopes | Semantics, syntax, synopsis |
| **Role** | Transport protocols | Technical language |
| **Analogy** | TCP/IP, HTTP | JSON, XML, Protobuf |

**23-95** defines the **pipes** (CFLF-GRAD, CUC, etc.)  
**23-96** defines the **language** the aircraft speaks through those pipes.

---

## Language Components

### Semantics (23-96-10)
- Entity types (CI, NN, CAOS, DPP, ANCHORS)
- Domain ontologies per ATA chapter
- Type system and validation rules

### Syntax (23-96-20)
- Core grammar (EBNF specification)
- Statement types (assertion, query, command)
- Expression language

### Synopsis (23-96-30)
- Explainable AI (XAI) integration
- Narrative generation engine
- Human-readable summaries

### Technology (23-96-40)
- Data types and formats
- Protocol integration
- Runtime representation

### Protocol Bindings (23-96-50)
- ARINC 429 encoding
- AFDX/ARINC 664 mapping
- CAN bus integration
- Ethernet/IP transport

### Ontology (23-96-60)
- OWL/RDF representation
- SPARQL query support
- Semantic reasoning

### Certification (23-96-70)
- Formal verification methods
- [DO-178C](https://www.rtca.org/) compliance
- Safety-critical language subset

### Tools (23-96-80)
- AST-L parser/lexer
- Validator
- CLI tools
- IDE integration

---

## Integration Points

| System | AST-L Integration |
|--------|-------------------|
| **CAOS** | Event descriptions, severity, context |
| **ANCHORS** | Carbon tracking, sustainability metrics |
| **DPP** | Product passport assertions |
| **FAirCCC** | Gradient envelopes, model metadata |
| **ATA Systems** | Configuration items, interfaces |

---

## The Complete Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AMPEL360 INTELLIGENT AIRCRAFT                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                         AST-L (23-96)                               │  │
│   │           "The native language of the intelligent aircraft"        │  │
│   │                                                                     │  │
│   │   Semantics │ Syntax │ Synopsis │ Technology │ Ontology │ Tools   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                    │                                        │
│                                    │ speaks through                         │
│                                    ▼                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                       COMM_NN (23-95)                               │  │
│   │                    FAirCCC Transport Protocols                      │  │
│   │                                                                     │  │
│   │   CFLF-GRAD │ CFLF-MODEL │ CFLF-TELEM │ CFLF-SAFETY │ CUC         │  │
│   │   (A→F)     │ (F→A)      │ (A→F)      │ (F→A)       │ (F→A)       │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                    │                                        │
│                                    │ connects to                            │
│                                    ▼                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                 CAOS │ ANCHORS │ DPP │ NN (95/97)                   │  │
│   │                    Systems that consume AST-L                       │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documents

* [23-95_COMM_NN README](../23-95_COMM_NN/README.md)
* [CFLF-GRAD OPT-IN Structure](../../../../CFLF-GRAD-OPTIN-STRUCTURE.md)
* [CUC OPT-IN Structure](../../../../CUC-OPTIN-STRUCTURE.md)
* [AST-L OPT-IN Structure](../../../../ASTL-OPTIN-STRUCTURE.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
