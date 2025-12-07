# 03-00-06-05-02A - Software Development

## 1. Purpose
Establish the software development processes and standards for avionics software on the AMPEL360 BWB-H2-Hy-E aircraft, ensuring compliance with [DO-178C](https://www.rtca.org/content/standards-guidance-materials) guidelines and achieving the required Design Assurance Level (DAL) for safety-critical software.

## 2. Scope
This document covers:
- Software development lifecycle per DO-178C
- Software requirements, design, coding, and testing
- Configuration management and quality assurance
- Tool qualification
- Safety assessment and certification compliance
- Hydrogen system and electric propulsion software considerations

## 3. Applicable Documents
- [DO-178C](https://www.rtca.org/content/standards-guidance-materials) - Software Considerations in Airborne Systems and Equipment Certification
- [DO-330](https://www.rtca.org/content/standards-guidance-materials) - Software Tool Qualification Considerations
- [DO-332](https://www.rtca.org/content/standards-guidance-materials) - Object-Oriented Technology and Related Techniques Supplement to DO-178C
- [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/) - Guidelines for Development of Civil Aircraft and Systems

## 4. Description

### 4.1 Overview
Avionics software for the BWB-H2-Hy-E must meet stringent safety and reliability requirements. Software for flight-critical functions (flight control, navigation, propulsion management) requires DO-178C DAL A certification, while less critical software may be developed to DAL B, C, or D.

### 4.2 Requirements
**Design Assurance Levels (DAL):**
- **DAL A (Catastrophic):** Flight control software, critical propulsion management
- **DAL B (Hazardous):** Navigation, crew alerting
- **DAL C (Major):** Communication, non-critical displays
- **DAL D (Minor):** Entertainment, administrative functions
- **DAL E (No Effect):** Non-essential features

**DO-178C Objectives:**
- Requirements are developed and verified
- Software architecture is defined and verified
- Source code is developed, reviewed, and verified against requirements
- Testing demonstrates software correctness
- Configuration management maintains integrity
- Quality assurance ensures process compliance

### 4.3 Methodology
**Software Development Lifecycle:**
1. **Software Planning** - Plan for Software Aspects of Certification (PSAC), Software Development Plan (SDP), Software Verification Plan (SVP)
2. **Software Requirements** - Derive from system requirements, document in SRS
3. **Software Design** - High-level and low-level design, documented in SDD
4. **Software Coding** - Implement design in code, follow coding standards
5. **Software Integration** - Integrate software components
6. **Software Verification** - Reviews, analysis, testing per SVP
7. **Configuration Management** - Version control, baselines, change control
8. **Quality Assurance** - Audits, process compliance checks
9. **Certification Liaison** - Coordinate with certification authority

**Verification Activities (per DAL):**
- **Reviews:** Requirements review, design review, code review
- **Analysis:** Worst-case execution time (WCET), stack usage, data/control flow
- **Testing:** Unit testing, integration testing, requirements-based testing
- **Structural Coverage:** Statement coverage (DAL C), decision coverage (DAL B), MC/DC (DAL A)

## 5. Deliverables
| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Plan for Software Aspects of Certification (PSAC) | PDF | Software Lead | Project start |
| Software Development Plan (SDP) | PDF | Software Lead | Project start |
| Software Requirements Specification (SRS) | DOORS/Markdown | Software Engineer | PDR |
| Software Design Description (SDD) | Markdown/PDF | Software Engineer | CDR |
| Source Code | C/C++/Ada | Software Developer | Implementation |
| Software Verification Plan (SVP) | PDF | Software QA | PDR |
| Software Verification Report | PDF | Software QA | Pre-certification |
| Software Configuration Management Plan (SCMP) | PDF | Configuration Mgmt | Project start |

## 6. Verification & Validation
**Acceptance Criteria:**
- All DO-178C objectives satisfied for applicable DAL
- Software requirements traced to system requirements
- All requirements verified through review, analysis, or test
- Structural coverage achieved (MC/DC for DAL A)
- Configuration management controls established
- Certification authority accepts software life cycle data

## 7. Cross-References
- Related ATA Chapters:
  - [ATA 22](https://en.wikipedia.org/wiki/ATA_100) - Auto Flight (autopilot software)
  - [ATA 31](https://en.wikipedia.org/wiki/ATA_100) - Instruments (display software)
  - [ATA 34](https://en.wikipedia.org/wiki/ATA_100) - Navigation (FMS software)
- Parent Document: [03-00-06_Engineering](../README.md)
- Related Documents:
  - [03-00-06-05-01A Avionics Architecture](./03-00-06-05-01A_Avionics_Architecture.md)
  - [03-00-06-05-04A Certification Compliance](./03-00-06-05-04A_Certification_Compliance.md)

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
