# 61-00-01-004 Traceability Matrix

## Document Information

- **Document ID**: 61-00-01-004
- **Title**: ATA 61 Traceability Matrix
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Overview / Traceability
- **ATA Chapter**: 61 — Propellers/Propulsors

## Purpose

This document establishes traceability between the ATA 61 Propellers/Propulsors domain and related lifecycle phases, ATA chapters, and AMPEL360 program requirements. It ensures that:

- All ATA 61 requirements can be traced to higher-level aircraft requirements
- Interfaces with related systems are clearly identified
- Lifecycle phase dependencies are documented
- Certification evidence paths are established

## Traceability Overview

### Lifecycle Phase Traceability

Traceability from ATA 61 Overview to subsequent lifecycle phases within the 61-00_GENERAL layer:

```
61-00-01_Overview (This Document)
        │
        ├──→ 61-00-02_Safety
        │         │
        │         ├──→ 61-00-03_Requirements
        │         │         │
        │         │         ├──→ 61-00-04_Design
        │         │         │         │
        │         │         │         ├──→ 61-00-05_Interfaces
        │         │         │         │         │
        │         │         │         │         ├──→ 61-00-06_Engineering
        │         │         │         │         │         │
        │         │         │         │         │         ├──→ 61-00-07_V_AND_V
        │         │         │         │         │         │         │
        │         │         │         │         │         │         └──→ ...
```

| From Phase | To Phase | Relationship | Artifacts |
|------------|----------|--------------|-----------|
| 01 Overview | 02 Safety | Defines scope for hazard analysis | Domain description, architecture |
| 01 Overview | 03 Requirements | Provides context for requirements derivation | Functional boundaries, key concepts |
| 01 Overview | 04 Design | Establishes architectural constraints | Global architecture, interface definitions |
| 01 Overview | 05 Interfaces | Identifies interface boundaries | Interface architecture, boundary definitions |
| 02 Safety | 03 Requirements | Safety requirements derived from FHA | Hazard list, safety objectives |
| 03 Requirements | 04 Design | Requirements allocated to design elements | Requirements trace matrix |
| 04 Design | 07 V&V | Design features verified by test | Design-to-test trace |
| 07 V&V | 10 Certification | Test evidence supports certification | Compliance matrix |

## ATA Chapter Cross-References

### Primary Related Chapters

| Related ATA | Relationship | Interface Type | Reference |
|-------------|--------------|----------------|-----------|
| **ATA 24** — Electrical Power | Power supply to propulsors | Electrical | [ICD TBD] |
| **ATA 28** — Fuel (H₂) | Cryogenic thermal interface, fuel for power generation | Thermal, Fuel | [ICD TBD] |
| **ATA 54** — Nacelles/Pylons | Structural mounting, aerodynamic integration | Structural | [ICD TBD] |
| **ATA 71** — Power Plant | Overall propulsion system integration | System | [ICD TBD] |
| **ATA 76** — Engine Controls | Control system integration, FADEC interface | Control | [ICD TBD] |

### Secondary Related Chapters

| Related ATA | Relationship | Interface Type | Reference |
|-------------|--------------|----------------|-----------|
| **ATA 21** — Air Conditioning | Thermal management (cooling air, LH₂ cold sink) | Thermal | [ICD TBD] |
| **ATA 22** — Autoflight | Flight control system interface for thrust commands | Control | [ICD TBD] |
| **ATA 45** — Onboard Maintenance | Health data, fault reporting | Data | [ICD TBD] |
| **ATA 72** — Engine | Hybrid turbine integration (if applicable) | System | [ICD TBD] |
| **ATA 95** — Digital Product Passport | Configuration, traceability, lifecycle data | Data | [ATA 95 ICD] |

## Requirements Traceability

### Top-Level Aircraft Requirements

Traceability from aircraft-level requirements to ATA 61 domain:

| Aircraft Req ID | Description | ATA 61 Allocation | Status |
|-----------------|-------------|-------------------|--------|
| AMPEL-REQ-PROP-001 | Aircraft shall achieve thrust-to-weight ratio ≥ 0.35 at MTOW | 61-REQ-PERF-001: Total propulsor thrust ≥ 4 × 180 kN | Derived |
| AMPEL-REQ-PROP-002 | Propulsion system shall operate on 100% hydrogen fuel | 61-REQ-INTEG-001: Propulsors powered by H₂-electric power train | Allocated |
| AMPEL-REQ-NOISE-001 | Sideline noise ≤ 85 EPNdB | 61-REQ-NOISE-001: EDF noise contribution ≤ TBD EPNdB | Derived |
| AMPEL-REQ-SAFE-001 | No single failure shall cause loss of aircraft | 61-REQ-SAFE-001: Propulsor redundancy per PSSA | Allocated |
| AMPEL-REQ-OPER-001 | Dispatch reliability ≥ 99.5% | 61-REQ-REL-001: Propulsor MTBF ≥ TBD hours | Derived |

### ATA 61 Requirements Index

| Requirement ID | Title | Category | Source | Verification |
|----------------|-------|----------|--------|--------------|
| 61-REQ-PERF-001 | Thrust Output | Performance | AMPEL-REQ-PROP-001 | Test |
| 61-REQ-PERF-002 | Efficiency | Performance | Derived | Analysis, Test |
| 61-REQ-INTEG-001 | H₂ Power Train Integration | Integration | AMPEL-REQ-PROP-002 | Inspection |
| 61-REQ-NOISE-001 | Noise Emission | Environmental | AMPEL-REQ-NOISE-001 | Test |
| 61-REQ-SAFE-001 | Failure Tolerance | Safety | AMPEL-REQ-SAFE-001 | Analysis |
| 61-REQ-REL-001 | Reliability | Reliability | AMPEL-REQ-OPER-001 | Analysis |
| 61-REQ-MAINT-001 | Maintainability | Supportability | Derived | Demonstration |

> **Note**: Detailed requirements are documented in [61-00-03 Requirements](../61-00-03_Requirements/README.md).

## Safety Traceability

### Functional Hazard Assessment Trace

Link between ATA 61 functions and hazards identified in [61-00-02 Safety](../61-00-02_Safety/README.md):

| Function | Hazard ID | Hazard Description | Severity | DAL |
|----------|-----------|---------------------|----------|-----|
| Thrust Generation | H-61-001 | Loss of all thrust | Catastrophic | A |
| Thrust Generation | H-61-002 | Asymmetric thrust (uncontrolled) | Hazardous | B |
| Thrust Control | H-61-003 | Loss of thrust control | Hazardous | B |
| Overspeed Protection | H-61-004 | Propulsor overspeed | Catastrophic | A |
| Cooling | H-61-005 | Motor overtemperature | Major | C |
| Health Monitoring | H-61-006 | Undetected propulsor degradation | Major | C |

### Safety Requirements Trace

| Safety Req ID | Hazard | Mitigation | Verification Method |
|---------------|--------|------------|---------------------|
| 61-SREQ-001 | H-61-001 | Four independent propulsors; continued flight with 3/4 | Analysis, Test |
| 61-SREQ-002 | H-61-002 | Asymmetric thrust limiting; yaw damping | Analysis, Simulation |
| 61-SREQ-003 | H-61-003 | Dual-redundant PCU | Analysis, Test |
| 61-SREQ-004 | H-61-004 | Dual overspeed sensors; independent shutdown path | Test |
| 61-SREQ-005 | H-61-005 | Temperature sensors; protective shutdown | Test |
| 61-SREQ-006 | H-61-006 | Continuous health monitoring; scheduled inspections | Analysis, Test |

## Subsystem Traceability

Traceability from ATA 61 Overview to subsystems in [61-20 Subsystems](../../61-20_Subsystems/README.md):

| Overview Element | Subsystem | Subsystem ID | Key Artifacts |
|------------------|-----------|--------------|---------------|
| Electric Motor | [Electric Motor](../../61-20_Subsystems/61-20-01_Electric_Motor/) | 61-20-01 | Specifications, LRU definition |
| Ducted Fan | [Ducted Fan](../../61-20_Subsystems/61-20-02_Ducted_Fan/) | 61-20-02 | Aerodynamic design, LRIs |
| Blade System | [Blade System](../../61-20_Subsystems/61-20-03_Blade_System/) | 61-20-03 | Blade design, materials |
| PCU | [Propulsor Control Unit](../../61-20_Subsystems/61-20-04_Propulsor_Control_Unit/) | 61-20-04 | Software, hardware specs |
| Cooling Loop | [Cooling Loop](../../61-20_Subsystems/61-20-05_Cooling_Loop/) | 61-20-05 | Thermal design |
| Health Sensing | [Health Sensing](../../61-20_Subsystems/61-20-06_Health_Sensing/) | 61-20-06 | Sensor specifications |

## Certification Traceability

### Applicable Regulations

| Regulation | Applicable Paragraphs | Compliance Method | Evidence Location |
|------------|----------------------|-------------------|-------------------|
| [CS-25 Subpart E](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) | CS 25.901–25.1001 | Test, Analysis | [61-00-10 Certification](../61-00-10_Certification/) |
| [CS-E](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-e-amendment-6) | TBD | Test, Analysis | TBD |
| [CS-P](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-p-amendment-1) | TBD | Test, Analysis | TBD |
| [FAR Part 25 Subpart E](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25/subpart-E) | 25.901–25.1001 | Test, Analysis | TBD |
| [DO-178C](https://www.rtca.org/content/do-178c-software-considerations-airborne-systems-and-equipment-certification) | All | Review, Test | 61-40 Software |
| [DO-254](https://www.rtca.org/content/do-254-design-assurance-guidance-airborne-electronic-hardware) | All | Review, Test | 61-20-04 PCU |

### Compliance Matrix Summary

| CS-25 Paragraph | Title | Applicability | Compliance Status |
|-----------------|-------|---------------|-------------------|
| 25.901 | Installation | Applicable | In Progress |
| 25.903 | Engines | Partially Applicable | In Progress |
| 25.905 | Propellers | Applicable (adapted) | In Progress |
| 25.925 | Propeller Clearance | Applicable | TBD |
| 25.929 | Propeller De-icing | TBD | TBD |
| 25.933 | Reversing Systems | Applicable if VP | TBD |
| 25.934 | Turbojet Engine Thrust Reverser | Not Applicable | – |

## Document Cross-Reference Matrix

| Document | 001 Domain | 002 Architecture | 003 Glossary | 004 Traceability |
|----------|------------|------------------|--------------|-------------------|
| 61-00-01-001 | – | ✓ | ✓ | ✓ |
| 61-00-01-002 | ✓ | – | ✓ | ✓ |
| 61-00-01-003 | ✓ | ✓ | – | ✓ |
| 61-00-01-004 | ✓ | ✓ | ✓ | – |
| 61-00-02 Safety | ✓ | ✓ | – | ✓ |
| 61-00-03 Requirements | ✓ | ✓ | – | ✓ |
| 61-00-04 Design | ✓ | ✓ | ✓ | ✓ |
| 61-20 Subsystems | ✓ | ✓ | ✓ | ✓ |

## Open Items

| Item | Description | Owner | Target Date | Status |
|------|-------------|-------|-------------|--------|
| TRC-001 | Complete ICD references for all ATA interfaces | Systems Team | TBD | Open |
| TRC-002 | Derive detailed ATA 61 requirements from aircraft-level | Requirements Team | TBD | Open |
| TRC-003 | Complete FHA and link hazards to safety requirements | Safety Team | TBD | Open |
| TRC-004 | Establish CS-25/FAR 25 compliance matrix | Certification Team | TBD | Open |

## References

### Internal References

- [61-00-01-001 ATA 61 Domain Description](61-00-01-001_ATA_61_Domain_Description.md)
- [61-00-01-002 Global Architecture](61-00-01-002_Global_Architecture.md)
- [61-00-01-003 Terminology Glossary](61-00-01-003_Terminology_Glossary.md)
- [61-00-02 Safety](../61-00-02_Safety/README.md)
- [61-00-03 Requirements](../61-00-03_Requirements/README.md)
- [61-00-04 Design](../61-00-04_Design/README.md)
- [61-00-10 Certification](../61-00-10_Certification/README.md)
- [61-20 Subsystems](../../61-20_Subsystems/README.md)

### External References

- [EASA CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) — Certification Specifications for Large Aeroplanes
- [FAA 14 CFR Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) — Airworthiness Standards: Transport Category Airplanes
- SAE ARP4754A — Guidelines for Development of Civil Aircraft and Systems
- SAE ARP4761 — Guidelines and Methods for Conducting the Safety Assessment Process

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---
