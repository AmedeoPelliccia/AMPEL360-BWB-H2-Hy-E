# 02-70-00-004 — Interface Not Applicable Statement

## Document Information

- **Document ID**: 02-70-00-004
- **Title**: Interface Not Applicable Statement Template
- **Subsystem**: ATA 02-70 Propulsion
- **Version**: 1.0
- **Status**: DRAFT
- **Date**: 2025-11-21

## Purpose

This document provides a template for documenting interfaces that are deliberately out of scope for ATA 02-70 Propulsion Operations Information, ensuring traceability and avoiding perceived gaps in the documentation structure.

## Usage

Use this template when an interface or data flow that might be expected to exist is intentionally not implemented or not applicable to the AMPEL360 BWB H₂ Hybrid-Electric propulsion system.

## Template

---

### Interface N/A Statement

**Interface ID**: [e.g., 02-70-XX-YYY]

**Interface Description**: [Brief description of the interface that does not apply]

**Reason for Non-Applicability**:

Select one or more:
- [ ] **System Design**: The AMPEL360 propulsion architecture does not include this component/subsystem
- [ ] **Technology Choice**: The H₂ hybrid-electric technology does not require this interface
- [ ] **Operational Concept**: The CONOPS does not include this operational scenario
- [ ] **Certification Approach**: Certification basis does not require this interface
- [ ] **Out of Scope**: This interface is managed by another ATA chapter or external system

**Detailed Explanation**:

[Provide detailed rationale for why this interface is not applicable. Include:
- Technical reasons
- Architectural decisions
- References to design documents
- Alternative approaches used instead]

**Traceability**:

- **Related Requirements**: [List any requirements that might have implied this interface and how they are satisfied alternatively]
- **Stakeholder Approval**: [Note stakeholders who have reviewed and approved this N/A statement]
- **Review Date**: [Date of last review]
- **Next Review Date**: [Scheduled re-evaluation date]

**References**:

- [Link to relevant design documents, requirements, or architectural decisions]

---

## Examples

### Example 1: Traditional Turbine Engine Interfaces

**Interface ID**: 02-70-XX-001-NA

**Interface Description**: Turbine engine exhaust gas temperature (EGT) monitoring

**Reason for Non-Applicability**:
- [x] **Technology Choice**: The H₂ hybrid-electric technology does not require this interface

**Detailed Explanation**:

The AMPEL360 propulsion system uses fuel cells and electric motors rather than traditional gas turbines. Fuel cells operate at much lower temperatures (60-80°C) than turbine engines (>1000°C EGT), and the relevant temperature monitoring is handled through:

- Fuel cell stack temperature monitoring ([ATA 73](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/ATA_73-ENGINE_FUEL_CONTROL/))
- Electric motor winding temperature ([ATA 72](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/ATA_72-ENGINE/))
- Thermal management system ([ATA 21](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E1-ENVIRONMENT/ATA_21-AIR_CONDITIONING_PRESSURIZATION/))

See [02-70-02_Engine_Performance_Data](./02-70-02_Engine_Performance_Data/) for the applicable thermal monitoring interfaces.

**Traceability**:
- **Related Requirements**: RQ-02-70-TEMP-001 "Propulsion system temperature monitoring" is satisfied by fuel cell and motor temperature sensors
- **Stakeholder Approval**: Propulsion engineering, flight operations (2025-11-15)
- **Review Date**: 2025-11-21
- **Next Review Date**: 2026-11-21 (annual review)

**References**:
- [AMPEL360 Propulsion System Architecture](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/)
- [02-70-02_Engine_Performance_Data](./02-70-02_Engine_Performance_Data/)

---

### Example 2: Jet Fuel Quality Monitoring

**Interface ID**: 02-70-XX-002-NA

**Interface Description**: Jet fuel contamination and quality monitoring

**Reason for Non-Applicability**:
- [x] **Technology Choice**: The H₂ hybrid-electric technology does not require this interface
- [x] **System Design**: The AMPEL360 propulsion architecture does not include this component/subsystem

**Detailed Explanation**:

The AMPEL360 uses cryogenic hydrogen fuel (H₂) stored at low temperatures (<-253°C) rather than traditional jet fuel (Jet A/Jet A-1). Hydrogen fuel quality concerns are fundamentally different:

**Not applicable**:
- Water contamination (jet fuel concern)
- Microbial growth (jet fuel concern)
- Particulate filtering (jet fuel concern)

**Applicable instead** (covered under [ATA 28](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/)):
- H₂ purity monitoring (minimum 99.97% purity required)
- Moisture ingress detection
- Air contamination monitoring
- Boiloff gas management

See [02-70-01_Fuel_Performance_Interfaces](./02-70-01_Fuel_Performance_Interfaces/) for H₂-specific fuel quality and performance monitoring.

**Traceability**:
- **Related Requirements**: RQ-02-70-FUEL-001 "Fuel quality monitoring" is satisfied by H₂ purity sensors in ATA 28
- **Stakeholder Approval**: Fuel systems engineering, operations (2025-11-15)
- **Review Date**: 2025-11-21
- **Next Review Date**: 2026-11-21

**References**:
- [ISO 14687:2019](https://www.iso.org/standard/69539.html) - Hydrogen fuel quality for PEM fuel cells
- [ATA 28 H₂ Fuel System](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/)

---

### Example 3: Traditional APU for Engine Start

**Interface ID**: 02-70-XX-003-NA

**Interface Description**: APU-provided compressed air for engine start

**Reason for Non-Applicability**:
- [x] **System Design**: The AMPEL360 propulsion architecture does not include this component/subsystem
- [x] **Technology Choice**: The H₂ hybrid-electric technology does not require this interface

**Detailed Explanation**:

Electric motors used in the AMPEL360 do not require compressed air for starting (unlike turbine engines). Motor starting is accomplished through:

1. **Power Electronics**: Direct electrical start from battery or APU generator
2. **Control System**: Sequential energization of motor phases
3. **No mechanical/pneumatic starting system required**

If an APU is present ([ATA 49](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_49-AIRBORNE_AUXILIARY_POWER/)), it provides electrical power only, not pneumatic power for engine start.

**Traceability**:
- **Related Requirements**: RQ-02-70-START-001 "Propulsion system starting" is satisfied by electrical starting system in ATA 72/24
- **Stakeholder Approval**: Propulsion engineering, systems engineering (2025-11-15)
- **Review Date**: 2025-11-21
- **Next Review Date**: 2026-11-21

**References**:
- [ATA 72 Engine (Electric Motors)](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/ATA_72-ENGINE/)
- [ATA 80 Starting](../../../T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/E2-ENERGY/ATA_80-STARTING/)

---

## Governance

### When to Create an N/A Statement

Create an interface N/A statement when:

1. **Expected Interface**: An interface might reasonably be expected based on traditional aircraft or ATA structure
2. **Deliberate Decision**: A conscious architectural or design decision has been made to exclude it
3. **Traceability Need**: Stakeholders or certification authorities might question its absence
4. **Prevent Confusion**: Future reviewers might perceive a gap in documentation

### Review and Approval

All N/A statements must be:

- **Technically Reviewed**: By subject matter experts in propulsion and relevant interfacing systems
- **Operations Reviewed**: By flight operations and maintenance to ensure no operational gaps
- **Certification Reviewed**: By certification team to ensure compliance is not affected
- **Periodically Re-evaluated**: At least annually, or when system design changes

### Documentation Location

N/A statements should be:

- **Indexed**: In the main [02-70 README](./README.md)
- **Cross-Referenced**: From any documents that might reference the N/A interface
- **Version Controlled**: Like all other documentation
- **Audit Trail**: Changes to N/A statements logged and justified

## References

### Internal Documents
- [02-70-00-001 Propulsion Ops Integration Overview](./02-70-00-001_Propulsion_Ops_Integration_Overview.md)
- [02-70-00-002 Cross-ATA Propulsion Data Map](./02-70-00-002_Cross_ATA_Propulsion_Data_Map.md)

### External Standards
- **[CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27)**: Certification Specifications (defines required systems)
- **[Part 21](https://www.easa.europa.eu/document-library/regulations/commission-regulation-eu-no-7482012)**: Design Organization Approval requirements

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---
