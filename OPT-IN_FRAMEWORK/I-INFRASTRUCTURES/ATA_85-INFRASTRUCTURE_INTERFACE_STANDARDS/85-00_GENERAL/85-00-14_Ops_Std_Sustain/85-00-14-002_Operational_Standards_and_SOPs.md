# 85-00-14-002 — Operational Standards and SOPs

## 1. Purpose

This document defines the **global operational standards** and baseline structure for **Standard Operating Procedures (SOPs)** applicable to all [ATA 85 – Infrastructure Interface Standards](https://www.ata.org/resources/specifications) for the AMPEL360 BWB H₂ Hy-E aircraft.

It establishes minimum content requirements, interaction rules, and references to domain-specific SOPs maintained in subdomain folders.

---

## 2. Scope

### 2.1 Applicable Infrastructure Domains

This document covers operational standards for:

1. **H₂ Infrastructure** — Hydrogen refuelling, storage, and safety interfaces
2. **CO₂ Battery Interface** — CO₂ battery charging and servicing
3. **Airport Interface** — Gates, bridges, ground power, data communications
4. **Ground Services Interface** — GSE connections, towing, de-icing
5. **Passenger Boarding & Evacuation** — Boarding bridges, emergency egress

### 2.2 SOP Hierarchy

- **Global SOPs** (this document) — Cross-domain standards and baseline templates
- **Domain-Specific SOPs** — Detailed procedures in subdomain folders:
  - [H2_INFRASTRUCTURE/](./H2_INFRASTRUCTURE/)
  - [CO2_BATTERY_INTERFACE/](./CO2_BATTERY_INTERFACE/)
  - [AIRPORT_INTERFACE/](./AIRPORT_INTERFACE/)
  - [GROUND_SERVICES_INTERFACE/](./GROUND_SERVICES_INTERFACE/)
  - [PAX_BOARDING_EVAC_INTERFACE/](./PAX_BOARDING_EVAC_INTERFACE/)
- **Airport-Specific Adaptations** — Local procedures aligned with airport operations

---

## 3. Global Operational Standards

### 3.1 Safety-First Principle

All infrastructure interface operations must prioritize:

1. **Personnel safety** — Ground crew, flight crew, passengers, and airport staff
2. **Aircraft integrity** — Prevention of damage to aircraft systems
3. **Infrastructure protection** — Safe operation of ground equipment
4. **Environmental safety** — H₂/CO₂ handling and emission controls

Reference: [85-00-02_Safety](../85-00-02_Safety) for risk assessments.

### 3.2 Pre-Operation Readiness

Before any interface connection:

- **Infrastructure readiness check** — Equipment functional and positioned correctly
- **Aircraft readiness check** — Systems powered and configured for ground operations
- **Personnel qualification** — Crew trained and certified for specific interface type
- **Communication established** — Ground crew ↔ flight crew ↔ airport operations

### 3.3 Connection Sequence Standards

All interface connections follow a standardized sequence:

1. **Visual inspection** — Check connectors, hoses, cables for damage
2. **Safety lockout** — Ensure aircraft systems in safe state
3. **Physical connection** — Mate connectors per interface specifications
4. **Verification** — Confirm secure connection and system status
5. **System activation** — Enable data/power/fluid flow as applicable
6. **Continuous monitoring** — Monitor interface status during operations

### 3.4 Disconnection Sequence Standards

1. **System deactivation** — Stop data/power/fluid flow
2. **Pressure relief** — For H₂/CO₂ interfaces, safely depressurize
3. **Physical disconnection** — Unmating per interface specifications
4. **Post-disconnect inspection** — Check for leaks, damage, or debris
5. **Equipment stowage** — Return ground equipment to safe storage
6. **Documentation** — Log operation completion and any anomalies

---

## 4. SOP Baseline Structure

### 4.1 Minimum SOP Content

All domain-specific SOPs must include:

#### Section 1: Purpose and Scope
- Objective of the procedure
- Applicable interface types and configurations

#### Section 2: Prerequisites
- Required personnel qualifications
- Required equipment and tools
- Aircraft and infrastructure state requirements

#### Section 3: Safety Precautions
- Hazards and risks
- Personal protective equipment (PPE) requirements
- Emergency procedures and escape routes

#### Section 4: Step-by-Step Procedure
- Numbered steps with clear actions
- Decision points and conditional branches
- Expected system responses and confirmations

#### Section 5: Verification and Completion
- Success criteria
- Documentation and logging requirements
- Handover to next phase of operations

#### Section 6: Troubleshooting
- Common issues and solutions
- Escalation procedures
- Contact points for technical support

#### Section 7: References
- Applicable standards and regulations
- Related SOPs and checklists
- Interface design specifications

### 4.2 SOP Version Control

- SOPs must be version-controlled with change history
- Updates triggered by incidents, equipment changes, or regulatory updates
- Approval required from Infrastructure Interfaces CCB (I-CCB-85)

See [85-00-14-005_Lifecycle_Change_and_Upgrade_Management.md](./85-00-14-005_Lifecycle_Change_and_Upgrade_Management.md).

---

## 5. Interaction Rules

### 5.1 Flight Crew ↔ Ground Crew

- **Pre-connection communication** — Ground crew confirms aircraft ready for interface
- **During operation** — Continuous monitoring and status updates
- **Abnormal situations** — Immediate notification and coordinated response
- **Post-operation** — Confirmation of safe disconnection

### 5.2 Ground Crew ↔ Airport Infrastructure Operators

- **Coordination of equipment positioning** — Gates, bridges, fuelling vehicles
- **Shared situational awareness** — Weather, aircraft status, operational constraints
- **Incident reporting** — Unified reporting to airport operations and airline

### 5.3 Interface with Training and Competency

- All personnel must complete **type-specific training** before performing interface operations
- **Refresher training** required annually or after significant procedure updates
- **Competency assessment** documented and maintained per [ATA 02 (Operations Information)](../../../../I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION)

---

## 6. Domain-Specific SOP References

### 6.1 H₂ Infrastructure

See [H2_INFRASTRUCTURE/85-00-14-H2-001_H2_Infrastructure_Ops_Standards.md](./H2_INFRASTRUCTURE/85-00-14-H2-001_H2_Infrastructure_Ops_Standards.md) for:

- Hydrogen refuelling procedures
- Safety perimeter management
- Emergency response for H₂ leaks

### 6.2 CO₂ Battery Interface

See [CO2_BATTERY_INTERFACE/85-00-14-CO2-001_CO2_Battery_Ops_Standards.md](./CO2_BATTERY_INTERFACE/85-00-14-CO2-001_CO2_Battery_Ops_Standards.md) for:

- CO₂ battery charging and servicing
- Closed-loop CO₂ handling
- Thermal management during ground operations

### 6.3 Airport Interface

See [AIRPORT_INTERFACE/85-00-14-AI-001_Airport_Interface_Ops_Standards.md](./AIRPORT_INTERFACE/85-00-14-AI-001_Airport_Interface_Ops_Standards.md) for:

- Gate compatibility checks
- Boarding bridge connection sequences
- Ground power and data interface operations

### 6.4 Ground Services Interface

See [GROUND_SERVICES_INTERFACE/85-00-14-GSE-001_GSE_Interface_Ops_Standards.md](./GROUND_SERVICES_INTERFACE/85-00-14-GSE-001_GSE_Interface_Ops_Standards.md) for:

- GSE positioning and connection
- Towing and pushback procedures
- De-icing equipment interface

### 6.5 Passenger Boarding & Evacuation

See [PAX_BOARDING_EVAC_INTERFACE/85-00-14-PAX-001_Pax_Boarding_Evac_Ops_Standards.md](./PAX_BOARDING_EVAC_INTERFACE/85-00-14-PAX-001_Pax_Boarding_Evac_Ops_Standards.md) for:

- Boarding bridge safety checks
- Passenger flow management
- Emergency evacuation coordination with airport rescue services

---

## 7. Related Standards and Regulations

### 7.1 Aviation Authorities

- [EASA CS-25](https://www.easa.europa.eu/document-library/certification-specifications/cs-25-amendment-27) — Large aeroplanes (ground handling aspects)
- [FAA Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) — Airworthiness standards
- [ICAO Annex 14](https://www.icao.int/safety/airnavigation/nationalitymarks/annexes_booklet_en.pdf) — Aerodromes (ground operations)

### 7.2 Industry Standards

- [ISO 13985](https://www.iso.org/standard/54560.html) — Liquid hydrogen land vehicle fuelling
- [SAE AS50881](https://www.sae.org/standards/content/as50881/) — Wiring aerospace vehicle
- [IATA Ground Operations Manual (IGOM)](https://www.iata.org/en/publications/manuals/ground-operations-manual/) — Ground handling standards

### 7.3 Internal References

- [85-00-03_Requirements](../85-00-03_Requirements) — Infrastructure interface requirements
- [85-00-04_Design](../85-00-04_Design) — Interface design specifications
- [85-00-06_Engineering](../85-00-06_Engineering) — Engineering change management

---

## 8. Status

- **Phase**: Operational Standards Development (A-LIVE-GP Stage 14)
- **Maturity**: `DRAFT` — Content to be validated with operational trials
- **Last Updated**: 2025-11-21

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-21.

---

**End of Document**
