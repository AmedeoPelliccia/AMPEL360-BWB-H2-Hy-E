# AI Subsystems Quick Reference

**Document ID**: 95-00-01-011  
**Version**: 1.0  
**Status**: DRAFT  
**Last Updated**: 2025-11-23

## Purpose

This document provides a quick reference view of the AI Subsystems Register, organized by domain and DS.AI scope for rapid navigation and decision-making.

## Summary Statistics

- **Total AI Systems**: 31
- **DS.AI IN Scope**: 23 systems (primary classification)
- **DS.AI OUT Scope**: 5 systems (catastrophic or business-only)
- **Mixed/Split Scope**: 3 systems (context-dependent)

## Systems by Domain

### Airborne Neural Networks (ATA 95-20-XX)

| AI_ID | Name | Safety | Hazard | DS.AI | AL/TQL | Status |
|-------|------|--------|--------|-------|--------|--------|
| NN-CORE | Core Platform | YES | H2 | IN | AL2-AL3 / TQL2-TQL3 | In design |
| NN-DPP | Digital Product Passport | NO | H4-H5 | IN | TQL5-TQL6 | Prototype |
| NN-ECS | Environmental Control System | YES | H2-H3 | IN | AL2-AL3 / TQL2-TQL3 | In design |
| NN-FCTL | Flight Controls | YES | H1 | **OUT** | DO-178C Level A | Concept |
| NN-FUEL | Fuel System (H2) | YES | H2 | IN | AL2-AL3 / TQL2-TQL3 | Concept |
| NN-REC | Recording Systems | NO | H4-H5 | IN | AL4-AL5 / TQL4-TQL5 | Concept |
| NN-IMA | IMA Integration | YES | H2 | IN | AL2-AL3 / TQL2-TQL3 | In design |
| NN-MX | Maintenance (Predictive) | NO/Limited | H3-H4 | IN | AL3-AL4 / TQL3-TQL4 | Concept |
| NN-APU | APU | YES | H3 | IN | AL3 / TQL3 | Concept |
| NN-STRUCT | Structures (Health Mon.) | YES | H2-H3 | IN | AL2-AL3 / TQL2-TQL3 | Concept |
| NN-WING | Wing Systems | YES | H2 | IN | AL2-AL3 / TQL2-TQL3 | Concept |
| NN-PROP | Propulsion | YES | H1-H2 | **OUT** | DO-178C Level A | Concept |
| NN-ENERGY | Energy Systems | YES | H2 | IN | AL2-AL3 / TQL2-TQL3 | Concept |

**Key Observations:**
- 2 systems OUT of DS.AI scope due to catastrophic hazard potential (NN-FCTL, NN-PROP)
- 11 systems IN scope requiring DS.AI compliance packages
- Most IN-scope systems at AL2-AL3 / TQL2-TQL3 (H2-H3 hazards)

### Ground & Airborne Operations (ATA 02-20-XX)

| AI_ID | Name | Safety | Hazard | DS.AI | AL/TQL | Status |
|-------|------|--------|--------|-------|--------|--------|
| OPS-DIGITAL | Digital Ops Platform | Depends | H2-H4 | Mixed | Per component | In design |
| OPS-EFB | Electronic Flight Bag | Depends | H2-H4 | Split | AL3-AL5 / TQL3-TQL5 | Concept |
| OPS-WB | Weight & Balance | YES | H1-H2 | IN | AL2-AL3 / TQL2-TQL3 | Concept |
| OPS-PERF | Performance Computer | YES | H1-H2 | IN/OUT | AL2-AL3 / TQL2-TQL3 | Concept |
| OPS-GOPS | Ground Ops Management | YES | H2-H3 | IN | AL3 / TQL3 | Prototype |
| OPS-FP | Flight Planning | NO | H3-H4 | IN | AL4-AL5 / TQL4-TQL5 | Concept |
| OPS-DISPATCH | Dispatch System | NO | H3-H4 | IN | AL4-AL5 / TQL4-TQL5 | Concept |
| OPS-WX | Weather Information | NO | H3-H4 | IN | AL4-AL5 / TQL4-TQL5 | Concept |
| OPS-ODR | Operational Data Rec. | NO | H4-H5 | IN | AL5 / TQL5 | Concept |
| OPS-CRM | Crew Resource Mgmt | NO | H4-H5 | IN | AL5-AL6 / TQL5-TQL6 | Concept |
| OPS-H2 | H2 Operations | YES | H2-H3 | IN | AL2-AL3 / TQL2-TQL3 | Concept |
| OPS-PAX | Passenger Experience | NO | H4-H5 | **OUT** | Business only | Concept |
| OPS-PRED | Predictive Operations | NO | H4-H5 | **OUT** | Business only | Concept |

**Key Observations:**
- 2 systems OUT of scope (business-only, non-safety: OPS-PAX, OPS-PRED)
- Wide range of AL/TQL levels (AL2 to AL6) reflecting diverse functions
- OPS-WB and OPS-PERF have H1-H2 hazards but with different mitigation approaches

### Infrastructure & Circularity (ATA 85)

| AI_ID | Name | Safety | Hazard | DS.AI | AL/TQL | Status |
|-------|------|--------|--------|-------|--------|--------|
| CIRC-CO2 | CO2 Capture Controller | YES | H2-H3 | IN | AL3 / TQL3 | Prototype |

**Key Observations:**
- Industrial safety focus, not direct flight safety
- IN scope for DS.AI as safety component in plant operations

### Enterprise Tools (Development & Documentation)

| AI_ID | Name | Safety | Hazard | DS.AI | AL/TQL | Status |
|-------|------|--------|--------|-------|--------|--------|
| DOC-META-ENF | doc-meta-enforcer MCP | Tool | H4-H5 | IN | TQL5-TQL6 | Prototype |
| GEOM-WATCH | Geometry & Mass Watchdog | Tool | H4-H5 | IN | TQL5-TQL6 | Prototype |
| GEN-CCC | GenCCC Cross-Reference | Tool | H4-H5 | IN | TQL5-TQL6 | Concept |
| CAOS-CHAT | CAOS AI Assistants | Depends | H2-H5 | Split | AL2-AL6 | Concept |

**Key Observations:**
- All development tools IN scope as AI Level 1A
- CAOS-CHAT has split classification based on usage context
- Generally lower safety impact (H4-H5) with higher TQL requirements (TQL5-TQL6)

## DS.AI Scope Decision Summary

### ✅ IN Scope (24 systems)

**High Assurance (AL2-AL3)** - 11 systems
- Critical safety functions with H2-H3 hazards
- Examples: NN-ECS, NN-FUEL, NN-CORE, NN-IMA, NN-ENERGY, NN-WING, NN-STRUCT, OPS-WB, OPS-H2

**Medium Assurance (AL3-AL5)** - 7 systems
- Decision support and advisory functions
- Examples: NN-APU, NN-MX, OPS-GOPS, OPS-FP, OPS-DISPATCH, OPS-WX, OPS-ODR

**Tool Assurance (TQL5-TQL6)** - 6 systems
- Development and verification tools
- Examples: NN-DPP, DOC-META-ENF, GEOM-WATCH, GEN-CCC, NN-REC, OPS-CRM

### ❌ OUT of Scope (5 primary + 2 split)

**Catastrophic Hazards** (2 systems)
- NN-FCTL (Flight Controls) - H1 loss of control
- NN-PROP (Propulsion) - H1-H2 propulsion failure
- → Require DO-178C Level A + future AI-specific catastrophic guidance

**Business-Only** (2 systems)
- OPS-PAX (Passenger Experience) - No safety impact
- OPS-PRED (Predictive Operations) - Strategic planning only

**Context-Dependent** (3 systems - split classification)
- OPS-PERF: IN if non-catastrophic use, OUT if catastrophic scenarios
- OPS-DIGITAL: Mixed - evaluate per component
- CAOS-CHAT: IN if safety-related, OUT if pure knowledge tool

## Priority Actions by System

### Immediate DS.AI Package Required (AL2-AL3)

1. **NN-ECS** (In design - Priority 1)
   - Full DS.AI compliance package
   - ConOps, OD/ODD, Risk Assessment, Ethics, Learning Assurance
   
2. **NN-CORE** (In design - Priority 1)
   - Platform-level DS.AI compliance
   - Affects all dependent NN subsystems

3. **NN-IMA** (In design - Priority 2)
   - Integration layer compliance
   - Critical for NN deployment

4. **OPS-GOPS** (Prototype - Priority 2)
   - Already in prototype phase
   - Ground safety implications

5. **OPS-WB** (Concept - Priority 3)
   - H1-H2 hazard level
   - High priority once design starts

### Medium-Term DS.AI Packages (AL3-AL5)

- NN-APU, NN-MX, OPS-FP, OPS-DISPATCH, OPS-WX, OPS-ODR
- Advisory and decision support functions
- Lower immediate priority

### Tool Verification (TQL5-TQL6)

- DOC-META-ENF (Prototype - verify ML components)
- GEOM-WATCH, GEN-CCC (if ML-based - assess)
- NN-DPP (traceability verification)

### Out of Scope - Alternative Approach

- **NN-FCTL, NN-PROP**: Monitor for future AI safety standards beyond DS.AI
- **OPS-PAX, OPS-PRED**: Standard software development (non-safety)

## Next Steps

1. **For NN-ECS** (example detailed package):
   - Generate ConOps per DS.AI.100
   - Define OD/ODD per DS.AI.120
   - Complete FHA per DS.AI.130
   - Ethics assessment per DS.AI.140
   - Learning assurance plan per DS.AI.150

2. **For all IN-scope systems**:
   - Verify AL/TQL allocation against DS.AI tables
   - Ensure repository structure supports compliance artifacts
   - Link to master register for traceability

3. **For OUT-of-scope systems**:
   - Document rationale in safety case
   - Apply appropriate alternative standards (DO-178C, etc.)

---

## Document Control

- **Generated with the assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-23

---

## References

- [AI_Subsystems_Register.csv](./AI_Subsystems_Register.csv) - Full register data
- [AI_Subsystems_Register_README.md](./AI_Subsystems_Register_README.md) - Detailed documentation
- DS.AI Guideline - EASA (official guidance)
- EU AI Act - Official EU legislation
