---
document_id: "54-00-02-80-001"
ata: "54"
ata_title: "Nacelles / Pylons"
node: "54-00-02-80_REQUIREMENTS_LINKS"
title: "Cert Basis References"
project: "AMPEL360"
program: "AIR-T"
family: "Q100"
variant: "BWB"
phase: "LC02"
knot: "K07"
aor_owner: "STK_CERT"
aor_contributors: ["STK_SAF","STK_SE","STK_CM"]
status: "DRAFT"
issue_rev: "I01-R01"
last_updated: "2026-01-01"
classification: "INTERNAL"
---

# 54-00-02-80-001 — Cert Basis References (ATA 54)

## 1. Purpose

Document the **certification basis references** applicable to **ATA 54 (Nacelles / Pylons)** safety activities for AMPEL360 AIR-T. This document establishes the regulatory framework and applicable standards.

## 2. Certification Basis

### 2.1 Primary Regulations

| Regulation | Authority | Applicability | Amendment |
|------------|-----------|---------------|-----------|
| [CS-25](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) | EASA | Large Aeroplanes | TBD |
| [14 CFR Part 25](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25) | FAA | Transport Category | TBD |

### 2.2 Safety-Relevant CS-25 / Part 25 Paragraphs

| Paragraph | Title | Relevance to ATA 54 |
|-----------|-------|---------------------|
| 25.571 | Damage Tolerance and Fatigue | Nacelle/pylon structural integrity |
| 25.581 | Lightning Protection | Nacelle lightning protection |
| 25.601 | Design | General structural design |
| 25.603 | Materials | Material properties and approvals |
| 25.609 | Protection of Structure | Corrosion, wear, foreign object damage |
| 25.901 | Installation | Powerplant installation |
| 25.903 | Engines | Engine mounting requirements |
| 25.1309 | Equipment, Systems, Installations | System safety assessment |

### 2.3 Applicable Standards

| Standard | Title | Application |
|----------|-------|-------------|
| [ARP4754A](https://www.sae.org/standards/content/arp4754a/) / ED-79A | Development of Civil Aircraft and Systems | System development process |
| [ARP4761](https://www.sae.org/standards/content/arp4761/) / ED-135 | Safety Assessment Process | Safety assessment methodology |
| [DO-178C](https://www.rtca.org/wp-content/uploads/2020/03/DO-178C-2011.pdf) / ED-12C | Software Considerations | Software safety (if applicable) |
| [DO-254](https://www.rtca.org/wp-content/uploads/2020/03/DO-254-2000.pdf) / ED-80 | Hardware Considerations | Complex hardware (if applicable) |

## 3. Means of Compliance

| Requirement | MoC Type | Description |
|-------------|----------|-------------|
| Structural integrity | Analysis + Test | Stress analysis, fatigue/damage tolerance, static test |
| System safety | Analysis | FHA, SSA, FTA per ARP4761 |
| Fire protection | Analysis + Test | Fire zone definition, fire testing |
| Lightning | Analysis + Test | Zoning analysis, test |

## 4. Special Conditions

| ID | Description | Status |
|----|-------------|--------|
| SC-54-001 | Novel propulsion integration (if applicable) | TBD |
| SC-54-002 | Hydrogen fuel system interfaces (if applicable) | TBD |

## 5. Open Items / TODO

- [TODO] Confirm CS-25/Part 25 amendment applicable to program.
- [TODO] Confirm special conditions with certification authority.
- [TODO] Complete means of compliance matrix.
