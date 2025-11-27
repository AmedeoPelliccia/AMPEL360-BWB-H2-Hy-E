# AST-L Core Grammar — EBNF Specification

**Version:** 1.0  
**Date:** 2025-11-27  
**Status:** Draft  
**Related Standard:** AMPEL360-ASTL-SPEC-001 §3

---

## Purpose

This document defines the formal grammar for **AST-L (Air SynTech Language)** in Extended Backus-Naur Form (EBNF). AST-L is the native language of the AMPEL360 intelligent aircraft.

---

## Core Syntax Pattern

```astl
<entity> : <predicate> : <value> @<context> #<lifecycle>
```

---

## EBNF Grammar

```ebnf
(* AST-L Core Grammar v1.0 *)

statement       = entity , ":" , predicate , ":" , value 
                  [ context_list ] [ lifecycle ] ;

entity          = entity_prefix , "." , entity_path
                | ata_reference ;

entity_prefix   = "CAOS" | "ANCHORS" | "DPP" | "FAirCCC" | "NN" | "CI" ;

entity_path     = identifier , { "." , identifier } ;

ata_reference   = ata_chapter , "-" , ata_section , "-" , ata_item 
                  [ "_" , description ] ;

ata_chapter     = digit , digit ;
ata_section     = digit , digit ;
ata_item        = digit , digit ;

predicate       = identifier ;

value           = literal
                | typed_value
                | entity ;

typed_value     = type_name , "(" , parameter_list , ")" ;

type_name       = identifier ;

parameter_list  = parameter , { "," , parameter } ;

parameter       = identifier , "=" , literal ;

literal         = string_literal
                | number_literal
                | boolean_literal
                | enum_literal ;

string_literal  = '"' , { character } , '"' ;

number_literal  = [ "-" ] , digits , [ "." , digits ] , [ unit ] ;

unit            = identifier , [ "/" , identifier ] ;

boolean_literal = "true" | "false" | "TRUE" | "FALSE" ;

enum_literal    = "HIGH" | "MEDIUM" | "LOW" | "CRITICAL" 
                | "NORMAL" | "DEGRADED" | "FAILED" ;

context_list    = context , { context } ;

context         = "@" , context_value ;

context_value   = identifier , [ "=" , literal ] ;

lifecycle       = "#" , lifecycle_phase ;

lifecycle_phase = "L" , digit , digit , "_" , identifier ;

identifier      = letter , { letter | digit | "_" } ;

description     = identifier , { identifier } ;

letter          = "A" | "B" | ... | "Z" | "a" | "b" | ... | "z" ;

digit           = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

digits          = digit , { digit } ;

character       = letter | digit | special ;

special         = " " | "." | "-" | "_" | "/" | "(" | ")" ;
```

---

## Lifecycle Phases

| Code | Phase | Description |
|------|-------|-------------|
| `#L01_OVERVIEW` | Overview | System overview |
| `#L02_SAFETY` | Safety | Safety analysis |
| `#L03_REQUIREMENTS` | Requirements | Requirements definition |
| `#L04_DESIGN` | Design | Design specification |
| `#L05_INTERFACES` | Interfaces | Interface control |
| `#L06_ENGINEERING` | Engineering | Engineering analysis |
| `#L07_VV` | V&V | Verification & Validation |
| `#L08_PROTOTYPING` | Prototyping | Prototype development |
| `#L09_PRODUCTION` | Production | Production planning |
| `#L10_CERTIFICATION` | Certification | Certification evidence |
| `#L11_EIS` | EIS | Entry into service |
| `#L12_SERVICES` | Services | Maintenance & service |
| `#L13_SUBSYSTEMS` | Subsystems | Component breakdown |
| `#L14_OPERATIONS` | Operations | Operational standards |

---

## Entity Prefixes

| Prefix | Domain | Examples |
|--------|--------|----------|
| `CAOS` | Operational awareness | `CAOS.Event.SHMA.RivetF12` |
| `ANCHORS` | Sustainability | `ANCHORS.CO2.Solid` |
| `DPP` | Digital Product Passport | `DPP.Battery.0021` |
| `FAirCCC` | Federated learning | `FAirCCC.A.Node4321` |
| `NN` | Neural networks | `NN.Model.ECS.v4` |
| `CI` | Configuration items | `CI.53-30-21.Separator` |

---

## Context Modifiers

| Context | Description | Examples |
|---------|-------------|----------|
| `@CRUISE` | Flight phase | Cruise conditions |
| `@TAKEOFF` | Flight phase | Takeoff conditions |
| `@LANDING` | Flight phase | Landing conditions |
| `@GROUND` | Flight phase | Ground operations |
| `@INFLIGHT` | Flight phase | Any airborne phase |
| `@eps=X` | Privacy budget | Differential privacy epsilon |
| `@delta=X` | Privacy budget | Differential privacy delta |
| `@temp=X` | Environment | Temperature condition |
| `@alt=X` | Environment | Altitude condition |

---

## Statement Examples

### ATA System Statement
```astl
53-30-21_CO2Separator : flow_in : Air(kg/s=0.84) @CRUISE #L06_ENGINEERING
```

### FAirCCC Gradient Statement
```astl
FAirCCC.A.Node4321 : sends : GradientEnvelope(version=4, sparse=true) @eps=0.3 #L09_PRODUCTION
```

### CAOS Event Statement
```astl
CAOS.Event.SHMA.RivetF12 : severity : HIGH @INFLIGHT #L07_VV
```

### DPP Traceability Statement
```astl
DPP.Battery.0021 : carbon_origin : ANCHORS.CO2.Solid #L11_EIS
```

### NN Model Statement
```astl
NN.Model.ECS.TempPredictor : accuracy : 0.97 @validation #L10_CERTIFICATION
```

---

## Type System

### Primitive Types
- `String` — Text values
- `Number` — Numeric values with optional units
- `Boolean` — true/false
- `Enum` — Predefined value sets

### Composite Types
- `Air(kg/s, temp, pressure)` — Air flow parameters
- `GradientEnvelope(version, sparse, model_id)` — FL gradient
- `ModelBundle(version, hash, signature)` — Model package
- `SafetyCase(level, evidence)` — Safety argument

---

## Validation Rules

1. **Entity Format:** Must match valid prefix or ATA reference
2. **Predicate:** Must be a valid identifier
3. **Value:** Must be a valid literal or typed value
4. **Context:** Optional, must start with `@`
5. **Lifecycle:** Optional, must match `#LXX_PHASE` format

---

## Related Documents

* [AST-L README](../../README.md)
* [Statement Types](../20-20_Statement_Types/README.md)
* [astl_statement.schema.json](../../23-96-90_SCHEMAS/astl_statement.schema.json)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27.

---
