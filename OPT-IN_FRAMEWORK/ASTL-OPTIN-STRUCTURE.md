# AST-L OPT-IN Structure — Master Mapping

**Version:** 1.0  
**Date:** 2025-11-27  
**Status:** Draft  
**Related Standard:** AMPEL360-ASTL-SPEC-001

---

## Purpose

This document provides the master mapping for **AST-L (Air SynTech Language)** — the native language of the intelligent aircraft. AST-L unifies ATA, OPT-IN, CAOS, ANCHORS, DPP, AI/NN, federated learning, and aeronautical protocols in a common, computable, certifiable grammar.

---

## Language Overview

| Attribute | Value |
|-----------|-------|
| **Name** | AST-L (Air SynTech Language) |
| **Location** | ATA 23-96 (L2-LINKS) |
| **Purpose** | Technical language for intelligent aircraft |
| **Relation** | Speaks through 23-95 COMM_NN protocols |

---

## Core Syntax

```astl
<entity> : <predicate> : <value> @<context> #<lifecycle>
```

### Syntax Elements

| Element | Description | Examples |
|---------|-------------|----------|
| `<entity>` | Subject identifier | `53-30-21_CO2Separator`, `FAirCCC.A.Node4321` |
| `<predicate>` | Relationship/property | `flow_in`, `sends`, `severity` |
| `<value>` | Object/value | `Air(kg/s=0.84)`, `HIGH` |
| `@<context>` | Contextual modifier | `@CRUISE`, `@eps=0.3`, `@INFLIGHT` |
| `#<lifecycle>` | OPT-IN lifecycle phase | `#L06_ENGINEERING`, `#L07_VV` |

### Examples

```astl
53-30-21_CO2Separator : flow_in : Air(kg/s=0.84) @CRUISE #L06_ENGINEERING
FAirCCC.A.Node4321 : sends : GradientEnvelope(v4) @eps=0.3 #L09_ML
CAOS.Event.SHMA.RivetF12 : severity : HIGH @INFLIGHT #L07_VV
DPP.Battery.0021 : carbon_origin : ANCHORS.CO2.Solid #L11_OPERATIONS
```

---

## Directory Structure

```
OPT-IN_FRAMEWORK/
└── T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/
    └── L2-LINKS/
        └── ATA_23-COMMUNICATIONS/
            └── 23-96_AIR_SYNTECH_LANGUAGE/
                ├── 23-96-00_GENERAL/         # 14 lifecycle folders
                ├── 23-96-10_SEMANTICS/       # Entity types, ontologies
                ├── 23-96-20_SYNTAX/          # Grammar, statements
                │   ├── 20-10_Core_Grammar/
                │   ├── 20-20_Statement_Types/
                │   └── 20-30_Expressions/
                ├── 23-96-30_SYNOPSIS/        # XAI, narratives
                ├── 23-96-40_TECHNOLOGY/      # Data types, protocols
                ├── 23-96-50_PROTOCOL_BINDINGS/
                │   ├── 50-10_ARINC_429/
                │   ├── 50-20_AFDX/
                │   ├── 50-30_CAN/
                │   └── 50-40_ETHERNET/
                ├── 23-96-60_ONTOLOGY/        # OWL/RDF, SPARQL
                ├── 23-96-70_CERTIFICATION/   # Formal verification
                ├── 23-96-80_TOOLS/           # Parser, validator
                └── 23-96-90_SCHEMAS/         # JSON/XML schemas
```

---

## Bucket Descriptions

| Bucket | Purpose |
|--------|---------|
| `23-96-00_GENERAL` | Lifecycle governance (14 folders) |
| `23-96-10_SEMANTICS` | Entity types, domain ontologies, type system |
| `23-96-20_SYNTAX` | EBNF grammar, statement types, expressions |
| `23-96-30_SYNOPSIS` | XAI integration, narrative generation |
| `23-96-40_TECHNOLOGY` | Data types, formats, runtime |
| `23-96-50_PROTOCOL_BINDINGS` | Aeronautical protocol mappings |
| `23-96-60_ONTOLOGY` | OWL/RDF representation, SPARQL |
| `23-96-70_CERTIFICATION` | Formal verification, DO-178C |
| `23-96-80_TOOLS` | Parser, validator, CLI, IDE |
| `23-96-90_SCHEMAS` | JSON/XML schema definitions |

---

## Relationship: 23-95 vs 23-96

| Aspect | 23-95 COMM_NN | 23-96 AST-L |
|--------|---------------|-------------|
| **Focus** | What is transmitted | How to express it |
| **Content** | Gradients, models, envelopes | Semantics, syntax, synopsis |
| **Role** | Transport protocols | Technical language |
| **Analogy** | TCP/IP, HTTP | JSON, XML, Protobuf |

**23-95** defines the **pipes** (CFLF-GRAD, CUC, etc.)  
**23-96** defines the **language** the aircraft speaks through those pipes.

---

## Integration Matrix

| System | AST-L Entity Prefix | Example |
|--------|---------------------|---------|
| **ATA Chapters** | `XX-YY-ZZ_Name` | `53-30-21_CO2Separator` |
| **CAOS Events** | `CAOS.Event.*` | `CAOS.Event.SHMA.RivetF12` |
| **ANCHORS** | `ANCHORS.*` | `ANCHORS.CO2.Solid` |
| **DPP** | `DPP.*` | `DPP.Battery.0021` |
| **FAirCCC** | `FAirCCC.*` | `FAirCCC.A.Node4321` |
| **NN Models** | `NN.*` | `NN.Model.ECS.v4` |

---

## N-Axis / L2-LINKS Integration

| N-Axis (97-40) | L2-LINKS (23-*) | Purpose |
|----------------|-----------------|---------|
| **97-40-20** Federated Learning | **23-95-60-10** CFLF-GRAD | Upstream gradients |
| **97-40-30** Model Deployment | **23-95-60-50** CUC | Downstream updates |
| — | **23-96** AST-L | Technical language |

---

## Key Documents

| Document | Location |
|----------|----------|
| [23-96 README](T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-96_AIR_SYNTECH_LANGUAGE/README.md) | AST-L main |
| [ASTL-GRAMMAR.md](T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-96_AIR_SYNTECH_LANGUAGE/23-96-20_SYNTAX/20-10_Core_Grammar/ASTL-GRAMMAR.md) | Syntax |
| [astl_statement.schema.json](T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-96_AIR_SYNTECH_LANGUAGE/23-96-90_SCHEMAS/astl_statement.schema.json) | Schemas |
| [23-95 README](T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/L2-LINKS/ATA_23-COMMUNICATIONS/23-95_COMM_NN/README.md) | COMM_NN |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
