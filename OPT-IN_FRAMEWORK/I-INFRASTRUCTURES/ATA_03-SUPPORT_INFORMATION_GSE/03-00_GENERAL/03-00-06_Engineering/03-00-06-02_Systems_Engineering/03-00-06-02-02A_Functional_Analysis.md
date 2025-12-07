# 03-00-06-02-02A - Functional Analysis

## 1. Purpose
Define the approach for conducting functional analysis of the AMPEL360 BWB-H2-Hy-E aircraft systems, decomposing high-level functions into detailed functional architectures that support system design, integration, and verification activities.

## 2. Scope
This document covers:
- Functional decomposition methodology
- Functional flow modeling and representation
- Functional requirements allocation
- Functional architecture development
- Interface functional analysis
- Functional hazard assessment integration
- Trade studies based on functional alternatives

## 3. Applicable Documents
- [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/) - Guidelines for Development of Civil Aircraft and Systems
- [SAE ARP4761](https://www.sae.org/standards/content/arp4761a/) - Guidelines and Methods for Conducting the Safety Assessment Process
- [INCOSE Systems Engineering Handbook](https://www.incose.org/products-and-publications/se-handbook) - Functional Analysis Methods
- [ISO/IEC/IEEE 15288](https://www.iso.org/standard/63711.html) - Systems and Software Engineering - System Life Cycle Processes

## 4. Description

### 4.1 Overview
Functional analysis establishes what the aircraft and its systems must accomplish to meet stakeholder requirements. For the BWB-H2-Hy-E, this includes conventional aircraft functions (flight control, navigation, communication) as well as novel functions related to hydrogen storage and distribution, electric propulsion management, and the unique aerodynamic control requirements of the blended-wing-body configuration.

### 4.2 Requirements
**Functional Analysis Requirements:**
- Functions shall be derived from system requirements
- Functional decomposition shall proceed from top-level to component level
- Each function shall have defined inputs, outputs, and performance criteria
- Functional flows shall be modeled for nominal and off-nominal scenarios
- Interface functions shall be explicitly identified
- Functions shall be allocated to physical system elements
- Functional hazard assessment shall identify safety-critical functions
- Functional redundancy and backup modes shall be defined

**Analysis Deliverables:**
- Functional hierarchy diagrams
- Functional flow block diagrams (FFBDs)
- N² diagrams for interface functions
- Functional requirements allocation sheets (FRAS)
- Functional architecture models

### 4.3 Methodology
**Functional Analysis Process:**

1. **Top-Level Functional Definition**
   - Identify primary aircraft missions and phases
   - Define top-level functions (e.g., "Provide Propulsion", "Control Flight")
   - Establish functional performance requirements

2. **Functional Decomposition**
   - Decompose functions hierarchically (3-5 levels typical)
   - Define sub-functions with clear boundaries
   - Identify function triggering events and sequences
   - Model nominal and contingency functional flows

3. **Functional Architecture Development**
   - Map functions to physical system architecture
   - Define functional interfaces and data flows
   - Identify shared and common functions
   - Establish functional redundancy strategy

4. **Functional Requirements Allocation**
   - Allocate requirements to functions
   - Derive functional performance specifications
   - Define verification methods for each function
   - Trace functions to design elements

5. **Functional Hazard Assessment (FHA)**
   - Identify failure conditions for each function
   - Assess functional failure effects
   - Classify hazard severity
   - Define safety requirements and mitigations

**Modeling Techniques:**
- SysML Activity Diagrams
- Functional Flow Block Diagrams (FFBDs)
- IDEF0 Functional Models
- Use Case Diagrams
- State Machine Diagrams

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Functional Analysis Plan | Markdown/PDF | Systems Engineering | Project start |
| Functional Architecture Document | Markdown/SysML | Systems Engineering | PDR |
| Functional Flow Diagrams | SVG/SysML | Systems Engineering | PDR |
| Functional Hazard Assessment | Markdown/CSV | Safety Engineering | PDR |
| Functional Requirements Allocation | CSV/Excel | Systems Engineering | PDR |
| Interface Control Documents (ICDs) | Markdown | Systems Engineering | CDR |

## 6. Verification & Validation
**Acceptance Criteria:**
- Functional decomposition complete to appropriate level
- All system requirements allocated to functions
- Functional flows model all operational scenarios
- Interface functions fully defined with ICDs
- Functional hazards identified and mitigated
- Functional architecture reviewed and approved
- Traceability established to physical architecture

**Verification Methods:**
- Peer review of functional models
- Functional architecture walkthrough
- Requirements allocation audit
- Interface compatibility analysis
- Safety assessment review
- Customer/stakeholder validation

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 05](https://en.wikipedia.org/wiki/ATA_100) - Time Limits/Maintenance Checks
  - [ATA 24](https://en.wikipedia.org/wiki/ATA_100) - Electrical Power
  - [ATA 28](https://en.wikipedia.org/wiki/ATA_100) - Fuel System
  - [ATA 61](https://en.wikipedia.org/wiki/ATA_100) - Propellers/Propulsors
  - [ATA 73](https://en.wikipedia.org/wiki/ATA_100) - Engine Fuel and Control
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-02-01A Requirements Management](./03-00-06-02-01A_Requirements_Management.md)
  - [03-00-06-02-03A Interface Definition](./03-00-06-02-03A_Interface_Definition.md)
  - [03-00-06-06-01A Hazard Analysis](../03-00-06-06_Safety_Engineering/03-00-06-06-01A_Hazard_Analysis.md)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AI (GitHub Copilot) | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-07.

---
