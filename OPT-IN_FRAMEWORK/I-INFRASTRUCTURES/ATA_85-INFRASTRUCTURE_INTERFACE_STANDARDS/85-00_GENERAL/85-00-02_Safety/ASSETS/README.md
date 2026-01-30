# ATA 85-00-02 Safety Assets

## Overview

This directory contains supporting assets for ATA 85-00-02 Safety documentation, including diagrams, templates, and visual materials for interface hazard analysis, safety zones, evacuation scenarios, and risk management.

## Asset List

### 85-00-02-A-001_Interface_Hazard_Map.drawio

**Type**: Diagram source file (draw.io format)

**Purpose**: Main diagram showing BWB infrastructure interfaces with hazard categories overlaid

**Content**:
- BWB aircraft outline (plan view)
- Interface points: H₂ refueling connector, CO₂ battery dock, ground power, doors, GSE areas
- Hazard category zones overlaid with color coding:
  - **Red**: Fire and explosion hazards (H₂, CO₂ battery thermal runaway)
  - **Orange**: Toxic exposure hazards (H₂ asphyxiation, CO₂ venting)
  - **Yellow**: Electrical hazards (ground power, CO₂ battery high voltage)
  - **Blue**: Crowd safety hazards (blocked evacuation routes, GSE conflicts)
- Legend with hazard category definitions

**Editing**: Use draw.io (desktop or web) to edit, export to SVG for documentation

**Status**: To be created by safety engineering team with input from stand design team

---

### 85-00-02-A-002_Interface_Hazard_Map.svg

**Type**: Scalable Vector Graphics (SVG) export

**Purpose**: Publishable version of interface hazard map for inclusion in documentation

**Content**: Same as 85-00-02-A-001 (source file), exported to SVG for web/print use

**Generation**: Auto-exported from draw.io source file

**Status**: To be generated after source file created

---

### 85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg

**Type**: Scalable Vector Graphics (SVG) diagram

**Purpose**: Plan view of a typical BWB stand showing safety zones, separation distances, and operational areas

**Content**:
- **BWB aircraft outline** (plan view, to scale)
- **H₂ safety zones**: Zone 0 (N/A at external interface), Zone 1 (3 m radius, red), Zone 2 (10 m radius, yellow)
- **CO₂ battery safety zones**: Thermal safety distance (5 m, orange), electrical safety distance (2 m, dashed line), access control zone (3 m during charging, purple)
- **Passenger flow paths**: From boarding bridges/stairs to aircraft doors (green arrows)
- **GSE routing lanes**: Catering, baggage, cleaning, etc. (gray arrows with labels)
- **Rescue access lanes**: ARFF vehicle approach routes (blue, ≥6 m wide), clearances around exits (blue hatched zones)
- **Stand boundaries**: Pavement markings, taxiway edge, terminal building
- **Dimensions**: Key separation distances labeled (e.g., "H₂ to passenger door: 12 m")
- **Legend**: Color coding and symbols explained

**Scale**: Approximately 1:500 or 1:1000 (choose for readability)

**Status**: To be created by stand design team with safety engineering input

---

### 85-00-02-A-004_Evacuation_and_Rescue_Scenarios.svg

**Type**: Scalable Vector Graphics (SVG) diagram(s)

**Purpose**: Scenario diagrams showing evacuation paths, rescue vehicle positions, and safety perimeters during emergency events

**Content** (multiple scenarios, each as separate diagram or combined):

#### Scenario 1: Fire on Stand with Evacuation
- BWB aircraft with smoke/fire symbol at aft cargo area
- **Evacuation routes**: Passengers exiting via forward and mid-fuselage doors (aft doors blocked by smoke)
- **Slide deployment**: Slides deployed from usable exits (yellow triangles)
- **ARFF positioning**: Primary vehicle upwind (west), applying foam curtain; secondary vehicle at downwind exits for passenger assistance
- **Wind arrow**: Showing wind from west (driving smoke away from forward exits)
- **Exclusion zone**: 20 m radius around fire source (red circle)

#### Scenario 2: H₂ Leak During Boarding
- BWB aircraft with H₂ dispenser connected
- **Leak location**: Connector (red starburst symbol)
- **Evacuation routes**: Partially boarded passengers exiting via forward doors only (using stairs, no slides)
- **Ex zone**: Zone 1 (3 m, red) and Zone 2 (10 m, yellow) marked around leak
- **Personnel positions**: H₂ crew evacuating upwind (>10 m), ground supervisor at safe observation point
- **ARFF positioning**: Upwind, monitoring H₂ concentration with handheld detector

#### Scenario 3: Normal Evacuation (All Exits Available)
- BWB aircraft, no hazards
- **Evacuation routes**: All exits in use (forward, mid, aft), slides deployed
- **ARFF positioning**: Multiple vehicles at forward, mid, and aft positions (both sides)
- **Passenger flow**: Arrows showing evacuation direction and convergence at assembly points
- **Rescue access lanes**: Clear and accessible (green)

**Status**: To be created by safety engineering team in coordination with ARFF

---

### 85-00-02-A-005_Interface_Risk_Register_Template.xlsx

**Type**: Microsoft Excel spreadsheet template

**Purpose**: Template risk register for documenting and tracking interface-level hazards

**Content** (columns):

1. **Interface Hazard ID**: Unique identifier (e.g., IFH-H2-001, IFH-CO2-001, IFH-EVAC-001)
2. **Interface**: Which interface (H₂ refueling, CO₂ battery, evacuation, ground power, GSE)
3. **Hazard Description**: Brief description of hazard (e.g., "H₂ leak at dispenser connector")
4. **Cause(s)**: What can cause this hazard (e.g., "Connector seal degradation, overpressure, improper connection")
5. **Effect(s)**: Consequences if hazard occurs (e.g., "Flammable atmosphere, potential fire/explosion")
6. **Initial Likelihood**: Before mitigations (Frequent, Probable, Remote, Extremely Remote, Extremely Improbable)
7. **Initial Severity**: Before mitigations (No Safety Effect, Minor, Major, Hazardous, Catastrophic)
8. **Initial Risk**: Combination of likelihood and severity (Unacceptable, Acceptable with Review, Acceptable)
9. **Mitigation(s)**: List of mitigations (e.g., "Leak-proof connector design, automatic leak detection, emergency shutdown, Ex zone enforcement")
10. **Mitigation Owner(s)**: Who implements each mitigation (Aircraft, Infrastructure, Procedures, or combinations)
11. **Residual Likelihood**: After mitigations
12. **Residual Severity**: After mitigations (typically same as initial)
13. **Residual Risk**: Combination of residual likelihood and severity
14. **ATA Owner**: Which ATA chapter owns on-board mitigation (e.g., ATA 28 for H₂ system)
15. **Infrastructure Owner**: Which organization owns infrastructure mitigation (e.g., H₂ infrastructure operator)
16. **Status**: Open, Mitigations in Progress, Closed (mitigations implemented and verified)
17. **Verification Method**: How mitigation effectiveness is verified (Test, Analysis, Inspection, Demonstration)
18. **Verification Status**: Not Started, In Progress, Complete
19. **Notes**: Any additional information, cross-references, assumptions

**Conditional Formatting**:
- **Initial Risk**: Red = Unacceptable, Yellow = Acceptable with Review, Green = Acceptable
- **Residual Risk**: Same color coding
- **Status**: Red = Open, Yellow = In Progress, Green = Closed

**Sample Rows**: Include 2-3 example hazards as templates (e.g., IFH-H2-001 H₂ leak, IFH-CO2-001 thermal runaway, IFH-EVAC-001 blocked rescue access)

**Status**: Template to be created by safety engineering team, populated during hazard analysis workshops

---

## File Naming Convention

All asset files follow the naming pattern:
```
85-00-02-A-[SequenceNumber]_[Descriptive_Name].[extension]
```

Where:
- **85-00-02**: Document section (Safety)
- **A**: Asset type
- **SequenceNumber**: 001, 002, 003, etc.
- **Descriptive_Name**: Brief name with underscores
- **extension**: .drawio, .svg, .xlsx, .png, etc.

## Usage in Documentation

Assets are referenced in safety documents using relative links:

```markdown
See [ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg](ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg)
```

For inline images (if supported by documentation system):

```markdown
![Safety Zones and Stand Layout](ASSETS/85-00-02-A-003_Safety_Zones_and_Stand_Layout.svg)
```

## Maintenance

**Review Frequency**: Assets reviewed quarterly along with parent safety documents

**Update Triggers**:
- Stand layout design changes
- New hazards identified
- Mitigation strategies updated
- Regulatory requirements change

**Version Control**: All assets tracked in git repository, commit messages describe changes

## Document Control

- **Owner**: AMPEL360 Safety & Certification Team
- **Repository**: AMPEL360-BWB-H2-Hy-E
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **DRAFT** – Subject to human review and approval
- Human approver: _[to be completed]_
- Last AI update: 2025-11-21
