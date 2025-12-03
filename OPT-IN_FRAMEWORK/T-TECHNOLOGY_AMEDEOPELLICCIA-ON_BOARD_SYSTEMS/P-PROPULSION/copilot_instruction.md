# Copilot Instructions — P-PROPULSION

**Axis:** T — Technology (On-board Systems & Powerplant)  
**Domain:** Propulsion (hybrid hydrogen–electric, SAF backup)  
**Owner:** Propulsion Engineering / AMPEL360 Documentation Steward

These instructions tell GitHub Copilot (and similar AI assistants) how to behave when generating or editing content inside:

`OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/P-PROPULSION/`

---

## 1. Purpose of this folder

This folder contains documentation, diagrams, data schemas, and helper scripts related to the **propulsion system** of the AMPEL360 BWB program, including:

- Hybrid **hydrogen–electric** architecture
- **Distributed electric propulsion (DEP)**: e.g. 4 × 4 MW ducted electric fans
- **Energy storage**: LH₂ tanks, batteries, SAF backup
- **Power conversion**: fuel cells, DC/DC, inverters, HVDC distribution
- Cross-links to **ATA 70–79**, **ATA 24**, **ATA 28**, **ATA 88**, **ATA 89**, **ATA 95–98**

Copilot must help maintain **consistent, traceable, certification-aligned** documentation.

---

## 2. General behaviour for Copilot

When operating in this folder, Copilot should:

1. **Prefer editing over rewriting**
   - Preserve existing structure, headings, and numbering.
   - When updating, modify the minimal necessary section.

2. **Stay consistent with program baselines**
   - Default propulsion concept (unless explicitly changed in the file being edited):
     - 4 × 4 MW electric motors / ducted fans (16 MW total installed propulsive power).
     - LH₂ storage: 3,000 kg (nominal).
     - Fuel cell system: 20 MW PEM.
     - Battery system: 5 MWh Li-ion.
     - Backup fuel: 500 L SAF.
   - If you change any of these values, clearly **call out the change** in the text and, if relevant, add a “TBD / subject to trade study” note.

3. **Write in engineering / certification language**
   - Use clear, technical English suitable for:
     - Propulsion engineers
     - Systems / safety engineers
     - Certification and performance engineers
   - Avoid marketing language. No slogans, no hype.

4. **Preserve traceability**
   - Maintain or add a **Document Control** section at the end of each document.
   - Whenever you introduce a new concept (unit, interface, requirement), consider:
     - A reference to the relevant **ATA chapter(s)**.
     - A note about which **lifecycle layer** (`XX-00-0x`) it belongs to.

---

## 3. File types and expectations

### 3.1 Markdown documents (`*.md`)

Copilot should:

- Use this basic structure unless the file explicitly follows another template:

  ```markdown
  # <Document Title>

  | Field           | Value                      |
  |----------------|----------------------------|
  | Document ID    | <ID>                       |
  | Version        | <x.y>                      |
  | Date           | YYYY-MM-DD                 |
  | Status         | DRAFT / REVIEW / RELEASED  |
  | Classification | TECHNICAL / INTERNAL / ... |
  | Owner          | Propulsion Engineering     |

  ---

  ## 1. Overview

  (Short, clear description of the purpose and scope.)

  ---

  ## 2. System Description

  (Architecture, main components, interfaces.)

  ---

  ## 3. Cross-References

  (Relevant ATA chapters, other docs, data schemas.)

  ---

  ## 4. Document Control

  - Generated with the assistance of AI (GitHub Copilot), prompted by: <Name>
  - Status: DRAFT – Subject to human review and approval.
  - Human approver: _[to be completed]_
  - Repository: `AMPEL360-BWB-H2-Hy-E`
  - Last AI update: YYYY-MM-DD

