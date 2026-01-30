# ASSETS — GSE Safety Documentation Visual Artefacts

## Purpose

This folder contains visual artefacts (diagrams, templates, checklists) that support the safety documentation in the parent folder `03-00-02_Safety` for Ground Support Equipment (GSE) operations under [ATA 03 – Support Information GSE](https://www.ata.org/resources/specifications/ispec2200).

---

## Current Contents

### 03-00-02-A-001_Safety_Architecture_GSE.drawio

**Status:** PLACEHOLDER

**Description:** This diagram will show the high-level architecture of GSE safety controls, including:

- **Technical Controls**: H₂ leak detection, emergency shutdown systems, fire suppression, collision avoidance
- **Procedural Controls**: Safety rules, work permits, pre-operation checks, exclusion zones
- **Organizational Controls**: Safety management framework, roles and responsibilities, training and competency, audits and inspections
- **Interfaces**: Integration with flight operations, maintenance, airport authority, fire/rescue services
- **Data Flow**: Safety data collection, analysis, reporting, and continuous improvement loop

**To be developed by:** GSE Safety Manager / Systems Engineering team using draw.io or similar diagramming tool

**Referenced in:** [03-00-02-001_Safety_Management_Framework.md](../03-00-02-001_Safety_Management_Framework.md)

---

### 03-00-02-A-002_Safety_Architecture_GSE.svg

**Status:** PLACEHOLDER

**Description:** SVG export of the GSE safety architecture diagram (03-00-02-A-001) for quick reference and embedding in other documents.

**To be developed by:** Automatically exported from 03-00-02-A-001_Safety_Architecture_GSE.drawio

**Referenced in:** [03-00-02-001_Safety_Management_Framework.md](../03-00-02-001_Safety_Management_Framework.md)

---

### 03-00-02-A-003_BowTie_Analysis_H2_Refuelling.svg

**Status:** PLACEHOLDER

**Description:** Bow-tie diagram for H₂ refuelling hazards showing:

- **Central Hazard**: H₂ leak during refuelling operation
- **Threats (Left Side - Causes)**:
  - Connection failure (improper coupling, damaged hose)
  - Overpressure (pressure regulator failure, blocked vent)
  - Equipment damage (impact damage, corrosion, fatigue)
  - Human error (incorrect procedure, inadequate training)
  - External factors (lightning strike, vehicle collision)
- **Preventive Barriers (Between Threats and Hazard)**:
  - Regular equipment inspections
  - Pressure relief devices (PRDs)
  - Breakaway coupling
  - Pre-refuelling checks
  - H₂ safety training
  - Exclusion zones and barriers
  - Lightning protection
- **Consequences (Right Side - Outcomes)**:
  - Fire / explosion
  - Asphyxiation
  - Cryogenic burns
  - Equipment damage
  - Operational disruption
- **Mitigative Barriers (Between Hazard and Consequences)**:
  - H₂ leak detection and alarms
  - Emergency shutdown systems
  - Fire suppression systems
  - Emergency response procedures
  - Personal Protective Equipment (PPE)
  - Evacuation procedures
  - Fire/rescue response

**To be developed by:** H₂ Safety Specialist / Safety Engineering team using bow-tie analysis software or drawing tool

**Referenced in:** [03-00-02-002_Hazard_Identification_and_Risk_Assessment.md](../03-00-02-002_Hazard_Identification_and_Risk_Assessment.md), [03-00-02-004_H2_Specific_Safety_Considerations.md](../03-00-02-004_H2_Specific_Safety_Considerations.md)

---

### 03-00-02-A-004_FMEA_Template.xlsx

**Status:** PLACEHOLDER

**Description:** Failure Modes and Effects Analysis (FMEA) template tailored for GSE components and operations, including:

**Columns:**
- **Component/System**: GSE equipment or subsystem being analyzed
- **Function**: Intended function of the component
- **Failure Mode**: How the component could fail
- **Effect of Failure**: Consequences if failure occurs (local, system, end effect)
- **Severity (S)**: Rating 1-10 (10 = catastrophic)
- **Cause(s)**: Root causes of the failure mode
- **Occurrence (O)**: Rating 1-10 (10 = very frequent)
- **Current Controls**: Existing controls to prevent or detect failure
- **Detectability (D)**: Rating 1-10 (10 = cannot detect)
- **Risk Priority Number (RPN)**: S × O × D
- **Recommended Actions**: Corrective or preventive actions to reduce RPN
- **Responsibility**: Person responsible for implementing action
- **Actions Taken**: Description of completed actions
- **Resulting RPN**: RPN after actions implemented

**Example Entries:**
- H₂ refuelling hose connection leak
- Tow tractor brake system failure
- High loader hydraulic cylinder failure
- GSE battery fire

**To be developed by:** GSE Safety Manager / Reliability Engineering team using Microsoft Excel or similar

**Referenced in:** [03-00-02-002_Hazard_Identification_and_Risk_Assessment.md](../03-00-02-002_Hazard_Identification_and_Risk_Assessment.md)

---

### 03-00-02-A-005_Risk_Register_Template.xlsx

**Status:** PLACEHOLDER

**Description:** Risk register template for tracking identified GSE risks, owners, mitigations, and status, including:

**Columns:**
- **Risk ID**: Unique identifier (e.g., GSE-RISK-001)
- **Date Identified**: Date risk was first identified
- **Identified By**: Person or process that identified the risk
- **Hazard Description**: Brief description of the hazard
- **Risk Scenario**: What could happen if hazard materializes
- **Category**: Type of risk (collision, fire, H₂ safety, injury, equipment failure, etc.)
- **Likelihood (Initial)**: Rating 1-5 before controls
- **Severity (Initial)**: Rating 1-5 before controls
- **Initial Risk Level**: Likelihood × Severity (with color coding: green/yellow/orange/red)
- **Existing Controls**: Current risk control measures in place
- **Likelihood (Residual)**: Rating 1-5 after controls
- **Severity (Residual)**: Rating 1-5 after controls
- **Residual Risk Level**: Likelihood × Severity after controls
- **Additional Actions Required**: Further actions needed to reduce risk
- **Action Owner**: Person responsible for implementing actions
- **Target Completion Date**: When actions should be completed
- **Status**: Open / In Progress / Closed
- **Review Date**: Date of last risk review
- **Next Review Date**: When risk should be reviewed next

**To be developed by:** GSE Safety Manager using Microsoft Excel or similar

**Referenced in:** [03-00-02-002_Hazard_Identification_and_Risk_Assessment.md](../03-00-02-002_Hazard_Identification_and_Risk_Assessment.md)

---

### 03-00-02-A-006_Safety_Checklist_GSE_Operations.pdf

**Status:** PLACEHOLDER

**Description:** Operational safety checklists for daily start-up, shift handover, and pre-task GSE checks, including:

**Checklists:**

1. **Daily Pre-Operation Checklist** (for GSE operators)
   - General inspection (damage, tires, lights, mirrors)
   - Safety systems (brakes, steering, horn, emergency stop)
   - Fluids and leaks (fuel, oil, coolant, hydraulic)
   - Fire extinguisher and first aid kit
   - H₂ refuelling bowser specific checks (leak detection, PRDs, emergency shutdown)

2. **Shift Handover Checklist** (for supervisors)
   - Shift briefing conducted (hazards, special operations, weather)
   - Equipment status review (serviceable, defects, unserviceable)
   - Personnel status (training current, fitness for duty)
   - Safety incidents/near-misses from previous shift
   - Outstanding corrective actions reviewed

3. **Pre-Task Safety Checklist** (for complex operations like H₂ refuelling, aircraft towing)
   - Task description and sequence understood
   - Roles and responsibilities assigned
   - Hazards identified and control measures in place
   - Communication methods established
   - Emergency procedures reviewed
   - PPE checked and donned
   - Equipment inspected and functional
   - Work area secured (exclusion zones, signage, barriers)

4. **Post-Operation Checklist** (for GSE operators)
   - Equipment secured (parked, braked, chocked, locked)
   - Area cleaned and FOD-free
   - Defects reported
   - Fuel/fluid levels checked
   - Equipment log updated

**To be developed by:** GSE Safety Manager / Ground Operations Manager using PDF format with fillable form fields (if possible)

**Referenced in:** [03-00-02-003_Operational_Safety_Rules_GSE.md](../03-00-02-003_Operational_Safety_Rules_GSE.md), [03-00-02-008_Safety_Audits_and_Inspections.md](../03-00-02-008_Safety_Audits_and_Inspections.md)

---

## Development Guidelines

When creating these artefacts:

1. **Consistency**: Follow the [AMPEL360 Assets Standard](../../../../../../AMPEL360_ASSETS_STANDARD.md) and AMPEL360 visual style guide
2. **Clarity**: Ensure diagrams and templates are understandable by both technical and non-technical stakeholders
3. **Traceability**: Each artefact should reference relevant sections in the parent documentation files
4. **Version Control**: Use formats that support version control (draw.io, SVG, Excel with change tracking)
5. **Export Formats**: Provide both editable source files and rendered formats (PDF, PNG) for documentation embedding
6. **Accessibility**: Ensure checklists are available in both electronic (PDF, Excel) and printed formats
7. **Regulatory Compliance**: Ensure templates align with [IATA ISAGO](https://www.iata.org/en/programs/safety/audit/isago/), [ICAO](https://www.icao.int/), and other relevant standards

---

## File Naming Convention

All asset files follow the naming convention:

```
03-00-02-A-XXX_Description.extension
```

Where:
- `03-00-02`: Parent folder (Safety)
- `A`: Asset type
- `XXX`: Sequential number (001, 002, 003, etc.)
- `Description`: Brief descriptive name (use underscores, not spaces)
- `extension`: File type (drawio, svg, xlsx, pdf, png, etc.)

---

## Asset Types by Extension

| Extension | Type | Purpose |
|---|---|---|
| `.drawio` | Diagram source | Editable diagrams (use draw.io / diagrams.net) |
| `.svg` | Vector graphic | Scalable diagrams for embedding in documents |
| `.png` | Raster graphic | Screenshots, photos, rendered diagrams |
| `.pdf` | Document | Checklists, forms, reports (final output) |
| `.xlsx` | Spreadsheet | Templates, data analysis (editable) |
| `.csv` | Data | Data exchange, imports |

---

## References

- Parent folder: [../](../) (03-00-02_Safety)
- AMPEL360 Assets Standard: [../../../../../../AMPEL360_ASSETS_STANDARD.md](../../../../../../AMPEL360_ASSETS_STANDARD.md)
- AMPEL360 Documentation Standard: [../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md](../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md)

---

## Document Control

- **Status**: `DRAFT` – Subject to human review and approval
- **Owner**: GSE Safety Manager
- **Last Updated**: 2025-11-21
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Notes: Placeholder files created as part of initial safety structure setup. Actual artefacts to be developed by subject matter experts.

---
