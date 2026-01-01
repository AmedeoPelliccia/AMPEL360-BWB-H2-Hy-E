---
document_id: "54-00-02-20-003"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-20_FHA"
title: "FHA Methodology"
project: "AMPEL360"
program: "AIR-T"
family: "Q100"
variant: "BWB"
phase: "LC02"
knot: "K07"
aor_owner: "STK_SAF"
aor_contributors: ["STK_SE","STK_CERT","STK_TEST","STK_CM","STK_MRO","STK_OPS"]
status: "DRAFT"
issue_rev: "I01-R01"
last_updated: "2026-01-01"
classification: "INTERNAL"
---

# 54-00-02-20-003 — FHA Methodology (ATA 54)

## 1. Purpose

Define the **Functional Hazard Assessment (FHA) methodology** applied to **ATA 54 (Nacelles / Pylons)** for AMPEL360 AIR-T. This document:
- describes the FHA process steps and analysis criteria,
- defines the severity classification scheme,
- establishes the hazard identification and documentation rules,
- ensures alignment with certification requirements and industry standards.

## 2. Scope

This methodology applies to:
- all functional hazards within the ATA 54 boundary,
- interface hazards with coupled ATA chapters (24/26/28/30/51/71/72),
- both normal and abnormal operating conditions,
- all flight phases and ground operations.

## 3. Regulatory and Standards Framework

### 3.1 Primary References

This FHA methodology is aligned with:

| Standard | Title | Application |
|----------|-------|-------------|
| [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | Equipment, Systems, and Installations | Certification requirements |
| [ARP4754A](https://www.sae.org/standards/content/arp4754a/) | Guidelines for Development of Civil Aircraft and Systems | Development assurance |
| [ARP4761](https://www.sae.org/standards/content/arp4761/) | Guidelines and Methods for Conducting the Safety Assessment Process | Safety assessment methods |
| AC 25.1309-1A | System Design and Analysis | FAA guidance material |

### 3.2 Program-Specific Adaptations

Program-specific adaptations to the standard FHA methodology SHALL be documented in:
- [`../54-00-02-00_SAFETY_OVERVIEW/54-00-02-00-001_Safety_Framework.md`](../54-00-02-00_SAFETY_OVERVIEW/54-00-02-00-001_Safety_Framework.md)

## 4. FHA Process Overview

The FHA process for ATA 54 follows these steps:

```
┌─────────────────────────────────────────────────────────────────────┐
│  Step 1: Functional Decomposition                                   │
│  - Identify ATA 54 functions and boundaries                         │
│  - Define normal and abnormal operating conditions                  │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Step 2: Failure Condition Identification                          │
│  - Identify potential loss or malfunction of each function         │
│  - Consider single and combined failures                           │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Step 3: Effect Analysis                                           │
│  - Determine effects on aircraft, crew, and passengers             │
│  - Consider all flight phases                                      │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Step 4: Severity Classification                                   │
│  - Assign severity per classification scheme (Section 5)           │
│  - Document rationale and assumptions                              │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Step 5: Requirements Derivation                                   │
│  - Derive safety requirements for critical failure conditions      │
│  - Establish probability targets per severity                      │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Step 6: Documentation and Traceability                            │
│  - Record in FHA case list and hazard log                          │
│  - Link to SSA/FTA for further analysis                            │
└─────────────────────────────────────────────────────────────────────┘
```

## 5. Severity Classification Scheme

### 5.1 Severity Definitions

Severity classifications are assigned per ARP4761 / [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) AMC:

| Severity | Definition | Probability Target |
|----------|------------|-------------------|
| **Catastrophic** | Failure conditions which would prevent continued safe flight and landing | ≤ 10⁻⁹ per flight hour |
| **Hazardous** | Failure conditions which would reduce aircraft capability or crew ability to cope with adverse operating conditions to the extent that there would be: (a) large reduction in safety margins or functional capabilities; (b) physical distress or excessive workload such that crew cannot be relied upon to perform tasks accurately or completely; or (c) serious or fatal injury to a relatively small number of occupants | ≤ 10⁻⁷ per flight hour |
| **Major** | Failure conditions which would reduce aircraft capability or crew ability to cope with adverse operating conditions to the extent that there would be: (a) significant reduction in safety margins or functional capabilities; (b) significant increase in crew workload or degraded crew efficiency; or (c) discomfort to occupants, possibly including injuries | ≤ 10⁻⁵ per flight hour |
| **Minor** | Failure conditions which would not significantly reduce aircraft safety and involve crew actions well within their capabilities. May include: (a) slight reduction in safety margins or functional capabilities; (b) slight increase in crew workload; or (c) minor physical discomfort to occupants | No quantitative requirement |
| **No Safety Effect** | Failure conditions which have no effect on safety | No requirement |

### 5.2 Severity Classification Criteria for ATA 54

For ATA 54 (Nacelles / Pylons), the following guidance applies:

| Failure Type | Typical Severity | Rationale |
|--------------|-----------------|-----------|
| Nacelle/pylon separation | Catastrophic | Loss of propulsion integration, asymmetric thrust, potential aircraft control issues |
| Partial attachment failure (arrested) | Hazardous | Reduced margins, secondary damage potential |
| Structural degradation (detectable) | Major | Requires maintenance action, reduced dispatch capability |
| Minor cosmetic damage | Minor | No flight safety impact |

## 6. Flight Phase Considerations

FHA SHALL consider all applicable flight phases:

| Phase | Duration Assumption | Special Considerations |
|-------|---------------------|----------------------|
| Taxi | Variable | Ground loads, foreign object damage |
| Takeoff | ~2 min | Maximum thrust, critical phase |
| Climb | ~20 min | High thrust, changing environment |
| Cruise | Variable | Sustained loads, fatigue |
| Descent | ~20 min | Thermal transients |
| Approach | ~5 min | Critical phase |
| Landing | ~2 min | Impact loads, critical phase |
| Go-around | ~2 min | Maximum thrust, critical phase |

## 7. Interface Hazard Analysis

### 7.1 Coupled Systems

FHA SHALL consider interface hazards with:
- ATA 71/72 (Powerplant/Propulsor) — mounting, thrust loads, vibration
- ATA 28 (Fuel / H₂) — fluid routing, leak potential
- ATA 26 (Fire Protection) — zone fire risks
- ATA 24 (Electrical Power) — wiring, arcing potential
- ATA 51 (Structures) — load paths, attachment points
- ATA 30 (Ice & Rain Protection) — thermal loads

### 7.2 Interface Hazard Documentation

Interface hazards SHALL be documented in:
- [`../54-00-02-70_INTERFACES_SAFETY/`](../54-00-02-70_INTERFACES_SAFETY/00_INDEX.md)

## 8. FHA Worksheet Format

Each FHA case SHALL be documented with the following minimum content:

| Field | Description |
|-------|-------------|
| Case ID | Unique FHA case identifier (FHA-54-XXX) |
| Hazard ID | Link to functional hazard (ATA54-FH-XXX) |
| Function | Affected ATA 54 function |
| Failure Condition | Description of the functional failure |
| Phase(s) | Applicable flight phases |
| Local Effects | Effects at component/subsystem level |
| Aircraft Effects | Effects at aircraft level |
| Crew Effects | Crew workload, awareness, actions required |
| Passenger Effects | Passenger safety and comfort impacts |
| Severity | Classification per Section 5 |
| Rationale | Justification for severity assignment |
| Derived Requirements | Safety requirements generated |
| Verification | How requirements will be verified |
| Status | Analysis status (Not Started / In Progress / Complete) |

## 9. Assumptions and Limitations

### 9.1 Key Assumptions

1. Crew training and procedures are adequate for normal and abnormal operations.
2. Aircraft is operated within approved flight envelope.
3. Maintenance is performed per approved procedures and intervals.
4. Design complies with applicable structural requirements (CS-25 Subpart C).

### 9.2 Limitations

1. FHA is a preliminary analysis; SSA/FTA provides detailed quantitative assessment.
2. FHA severity may be refined as design matures.
3. FHA assumes single failure conditions unless otherwise noted.

## 10. Open Items / TODO

- [TODO] Confirm program-specific probability targets with certification authority
- [TODO] Define combined failure condition analysis approach
- [TODO] Establish FHA review and approval workflow
- [TODO] Add FHA worksheet template as appendix or separate file

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-AIR-T`
- Last AI update: _2026-01-01_.

---
