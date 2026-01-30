# 85-40-00-005 Software Certification Approach

## 1. Purpose

This document defines the certification approach for software systems within the AMPEL360 BWB-H2-Hy-E ground infrastructure. It establishes the strategy, processes, and evidence requirements for demonstrating compliance with aviation regulations and achieving certification approval from relevant authorities.

## 2. Scope

This approach covers:

- Certification strategy and planning
- Regulatory requirements and applicable standards
- Software lifecycle processes per [DO-178C](https://en.wikipedia.org/wiki/DO-178C)
- Evidence collection and management
- Authority engagement and approval
- Configuration management and change control

## 3. Regulatory Context

### 3.1 Certification Authorities

**Primary Authorities**:
- **[EASA](https://www.easa.europa.eu/)** (European Union Aviation Safety Agency)
- **[FAA](https://www.faa.gov/)** (Federal Aviation Administration, USA)

**Type of Approval**:
- Ground support equipment and systems typically require **operational approval** rather than type certification
- Software supporting safety-critical functions requires compliance with [DO-178C](https://en.wikipedia.org/wiki/DO-178C)
- Integration with aircraft systems requires approval under [Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)

### 3.2 Applicable Regulations

- **[CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)** - Equipment, systems, and installations
- **[Part 21](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-7482012)** - Certification of aircraft and related products
- **[Part 145](https://www.easa.europa.eu/en/document-library/regulations/commission-regulation-eu-no-13212014)** - Maintenance organization approvals (for maintenance systems)

### 3.3 Applicable Standards

#### Software Development
- **[DO-178C](https://en.wikipedia.org/wiki/DO-178C)** - Software Considerations in Airborne Systems and Equipment Certification
- **[DO-330](https://en.wikipedia.org/wiki/DO-178C)** - Software Tool Qualification Considerations
- **[DO-278A](https://www.rtca.org/content/standards-guidance-materials)** - Guidelines for Communication, Navigation, Surveillance and Air Traffic Management (CNS/ATM) Systems Software Integrity Assurance

#### Cybersecurity
- **[DO-326A](https://www.rtca.org/content/standards-guidance-materials)** - Airworthiness Security Process Specification
- **[DO-356A](https://www.rtca.org/content/standards-guidance-materials)** - Airworthiness Security Methods and Considerations

#### Hardware
- **[DO-254](https://en.wikipedia.org/wiki/DO-254)** - Design Assurance Guidance for Airborne Electronic Hardware

## 4. Certification Strategy

### 4.1 Phased Certification Approach

**Phase 1: Foundation Systems (Months 1-12)**
- H2 refueling control system (DAL A/B)
- Basic safety monitoring
- Essential ground power management
- Initial aircraft interface

**Phase 2: Operational Systems (Months 13-24)**
- Turnaround management
- Enhanced safety monitoring
- Energy optimization
- Data communications

**Phase 3: Advanced Systems (Months 25-36)**
- Predictive analytics and AI
- Digital twin integration
- Advanced optimization
- Full ecosystem integration

### 4.2 Incremental Certification

**Benefits**:
- Early feedback from authorities
- Reduced certification risk
- Faster time to operational capability
- Manageable scope per phase

**Process**:
1. Scope definition and certification plan
2. Authority engagement and agreement on approach
3. Development with continuous compliance
4. Evidence package preparation
5. Authority review and approval
6. Conditional or full operational approval

## 5. Software Development Assurance

### 5.1 DO-178C Software Levels

Software is classified by Design Assurance Level (DAL) based on failure condition severity:

| DAL | Failure Effect | Objectives | Example Systems |
|-----|----------------|------------|-----------------|
| A | Catastrophic | All + formal methods | H2 emergency shutdown, safety interlocks |
| B | Hazardous | Comprehensive V&V | Fire detection integration, pressure monitoring |
| C | Major | Systematic testing | Energy management, turnaround control |
| D | Minor | Basic testing | Information displays, reporting |
| E | No Effect | Development standards | Training systems, simulators |

### 5.2 DO-178C Objectives

**Planning Process**:
- Software development plan (SDP)
- Software verification plan (SVP)
- Software configuration management plan (SCMP)
- Software quality assurance plan (SQAP)

**Development Process**:
- Requirements development
- Design development
- Coding and integration
- Traceability

**Verification Process**:
- Requirements-based testing
- Design-based testing
- Code-based testing (structural coverage)
- Review of verification results

**Configuration Management**:
- Version control
- Baseline management
- Change control
- Problem reporting

**Quality Assurance**:
- Process audits
- Product audits
- Conformity review

**Certification Liaison**:
- Authority engagement
- Plan approval
- Evidence review
- Approval artifacts

### 5.3 Structural Coverage Requirements

| DAL | Statement Coverage | Decision Coverage | MC/DC Coverage | Additional |
|-----|-------------------|-------------------|----------------|------------|
| A | 100% | 100% | 100% | Data/control coupling |
| B | 100% | 100% | 100% | - |
| C | 100% | 100% | - | - |
| D | 100% | - | - | - |
| E | - | - | - | - |

**Note**: MC/DC = Modified Condition/Decision Coverage

## 6. Safety Assessment

### 6.1 System Safety Assessment Process

Based on [ARP4761](https://www.sae.org/standards/content/arp4761a/) and [ARP4754A](https://www.sae.org/standards/content/arp4754a/):

**Functional Hazard Assessment (FHA)**:
- Identify system functions
- Assess potential failures and effects
- Classify failure conditions by severity
- Allocate safety requirements

**Preliminary System Safety Assessment (PSSA)**:
- Develop system architecture
- Allocate functions to systems
- Perform preliminary fault tree analysis
- Derive safety requirements for subsystems

**System Safety Assessment (SSA)**:
- Verify safety requirements met
- Complete fault tree analysis
- Demonstrate compliance with safety objectives
- Common cause analysis

### 6.2 Failure Condition Classifications

Based on [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes):

| Classification | Effect on Aircraft/Occupants | Probability Requirement |
|----------------|------------------------------|-------------------------|
| Catastrophic | Multiple fatalities, aircraft loss | Extremely Improbable (< 10⁻⁹ per flight hour) |
| Hazardous | Large reduction in safety margins, serious injuries | Extremely Remote (< 10⁻⁷ per flight hour) |
| Major | Significant reduction in safety margins | Remote (< 10⁻⁵ per flight hour) |
| Minor | Slight reduction in safety margins | Probable (< 10⁻³ per flight hour) |
| No Safety Effect | No effect on safety | No probability requirement |

### 6.3 Software Contribution to Failure Conditions

**For ground systems**:
- H2 refueling failures: Potentially Catastrophic (fire, explosion)
- Energy system failures: Major (operational disruption)
- Data system failures: Minor (information loss)

**Safety Requirements**:
- Independent monitoring for critical functions
- Redundancy for safety-critical systems
- Fail-safe defaults
- Emergency manual override capability

## 7. Tool Qualification

### 7.1 DO-330 Tool Qualification

Tools that automate verification processes or generate code/data used in the aircraft system require qualification per [DO-330](https://en.wikipedia.org/wiki/DO-178C).

**Tool Qualification Levels**:

| TQL | Tool Error Impact | Verification Credit |
|-----|-------------------|---------------------|
| TQL-1 | Can insert error; verification credit taken | Maximum |
| TQL-2 | Can fail to detect error; verification credit taken | Moderate |
| TQL-3 | Can fail to detect error; no verification credit | Minimal |
| TQL-4 | No impact on software lifecycle processes | None required |
| TQL-5 | Tool output not in airborne system | None required |

**Qualified Tools Required**:
- Compilers for safety-critical code (C/C++)
- Static analysis tools providing verification credit
- Code coverage analysis tools
- Requirements management tools (if generating verification evidence)

### 7.2 Tool Qualification Process

1. **Tool Operational Requirements (TOR)**: Define tool functions and uses
2. **Tool Qualification Plan (TQP)**: Qualification approach
3. **Tool Verification**: Test tool per TQL requirements
4. **Tool Qualification Data**: Evidence package
5. **Authority Approval**: Certification credit approval

## 8. Requirements Management

### 8.1 Requirements Traceability

**Traceability Links**:
```
System Requirements
    ↓
Software High-Level Requirements (SHLR)
    ↓
Software Low-Level Requirements (SLLR)
    ↓
Source Code
    ↓
Test Cases
    ↓
Test Results
```

**Traceability Matrix**: Bidirectional traceability required for all DAL A-D software

### 8.2 Requirements Standards

**High-Level Requirements (HLR)**:
- Derived from system requirements and safety assessment
- Verifiable and unambiguous
- Consistent and complete
- Traceable to source

**Low-Level Requirements (LLR)**:
- Derived from high-level requirements and design
- Implementable and verifiable
- Compatible with target hardware
- Consistent with HLR

### 8.3 Requirements Verification

**Methods**:
- **Review**: Peer review for completeness and correctness
- **Analysis**: Mathematical or logical demonstration
- **Test**: Execution with expected results
- **Demonstration**: Operational demonstration

## 9. Configuration Management

### 9.1 Configuration Identification

**Baselines**:
- **Functional Baseline**: Requirements specifications
- **Allocated Baseline**: Design specifications
- **Product Baseline**: Released software versions

**Configuration Items**:
- Requirements documents
- Design documents
- Source code
- Test cases and procedures
- Build scripts and tools
- Development environment specifications

### 9.2 Change Control

**Change Process**:
1. Change request submission
2. Impact analysis (safety, cost, schedule)
3. Change review board approval
4. Implementation and verification
5. Baseline update
6. Authority notification (if required)

**Authority Approval Required For**:
- Changes affecting safety-critical functions
- Changes to approved software architecture
- Tool updates affecting qualified tools

### 9.3 Software Configuration Index (SCI)

**Contents**:
- Software identification and version
- Configuration items list
- Build procedures
- Installation instructions
- Known anomalies
- Archive location

## 10. Verification and Validation

### 10.1 Verification Activities

**Requirements-Based Testing**:
- Test cases derived from requirements
- Each requirement verified by at least one test
- Normal and abnormal conditions tested
- Boundary conditions tested

**Design-Based Testing**:
- Test cases derived from design
- Verify design implementation
- Interface testing
- Error handling paths

**Code-Based Testing (Structural Coverage)**:
- Statement coverage (all code executed)
- Decision coverage (all branches taken)
- MC/DC coverage (for DAL A/B)
- Dead code analysis

### 10.2 Validation Activities

**System-Level Validation**:
- End-to-end operational scenarios
- Integration with aircraft systems
- Operational environment testing
- User acceptance testing

**Safety Validation**:
- Failure modes testing
- Emergency procedures verification
- Redundancy and fail-safe verification
- Performance under stress conditions

### 10.3 Independent Verification

**Independent Verification & Validation (IV&V)**:
- Required for DAL A software
- Recommended for DAL B software
- Performed by team independent of development
- Includes requirements review, design review, test review

## 11. Evidence Package

### 11.1 Required Documentation

**Plans**:
- Software Development Plan (SDP)
- Software Verification Plan (SVP)
- Software Configuration Management Plan (SCMP)
- Software Quality Assurance Plan (SQAP)
- Tool Qualification Plan (TQP) - if applicable

**Standards**:
- Requirements Standards
- Design Standards
- Code Standards

**Data**:
- Software Requirements Data
- Design Description Data
- Source Code
- Verification Cases and Procedures
- Verification Results
- Configuration Index
- Software Accomplishment Summary (SAS)

### 11.2 Software Accomplishment Summary (SAS)

**Purpose**: High-level summary for certification authority

**Contents**:
- System overview and software identification
- Certification considerations and software level
- Software lifecycle processes used
- Software lifecycle data (list of deliverables)
- Compliance with DO-178C objectives
- Tool qualification summary
- Known limitations and anomalies
- Approval request

### 11.3 Evidence Review Checklist

Authority reviewers will assess:
- [ ] Compliance with approved plans
- [ ] Completeness of requirements traceability
- [ ] Adequacy of verification coverage
- [ ] Proper configuration management
- [ ] Quality assurance conformity
- [ ] Tool qualification (if applicable)
- [ ] Residual risks acceptable
- [ ] Software accomplishment summary accuracy

## 12. Authority Engagement

### 12.1 Engagement Strategy

**Early Engagement** (Before Development):
- Present certification approach
- Agree on applicable standards
- Confirm software levels
- Establish communication channels

**Periodic Updates** (During Development):
- Milestone reviews
- Process audits
- Evidence sampling
- Issue resolution

**Final Review** (Pre-Approval):
- Complete evidence package review
- Demonstration of capabilities
- Conformity verification
- Approval artifacts preparation

### 12.2 Certification Review Items (CRI)

**Definition**: Aspects requiring authority agreement before proceeding

**Typical CRIs**:
- Software development and verification plans
- Software levels and safety justification
- Tool qualification approach
- Deviations from standard processes
- Novel or complex implementations

### 12.3 Issue Resolution

**Process**:
1. Authority raises issue or concern
2. Applicant investigates and proposes resolution
3. Authority reviews proposed resolution
4. Agreement on resolution approach
5. Implementation and verification
6. Closure confirmation

## 13. Continuous Compliance

### 13.1 Post-Certification Changes

**Change Classification**:
- **Major Change**: Requires authority approval (safety impact)
- **Minor Change**: Notification to authority
- **Administrative Change**: Internal documentation only

**Process**:
1. Change impact assessment
2. Determine change classification
3. Authority engagement if required
4. Implementation with appropriate verification
5. Configuration management update
6. Documentation update

### 13.2 Service Bulletins and Airworthiness Directives

**Monitoring**:
- Track issues affecting similar systems
- Assess applicability to AMPEL360 systems
- Implement corrective actions as needed

**Reporting**:
- Notify authorities of safety-related issues
- Support investigation of incidents
- Issue service bulletins for field corrections

## 14. Artificial Intelligence Certification

### 14.1 AI/ML Considerations

For AI/ML systems per [EASA AI Roadmap](https://www.easa.europa.eu/en/domains/innovation-digitalisation/artificial-intelligence) and [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai):

**Challenges**:
- Non-deterministic behavior
- Training data quality and bias
- Explainability and transparency
- Continuous learning implications

**Approach**:
- Rigorous data management and validation
- Extensive operational scenario testing
- Performance envelope definition
- Human oversight for critical decisions
- Staged deployment with monitoring

**See**: [85-40-06 Predictive Analytics and AI](85-40-06_Predictive_Analytics_and_AI/)

### 14.2 EASA AI Certification Pathway

**Concept Certification** (if applicable):
- Novel AI application approval
- Safety case development
- Operational constraints definition

**Type Certification** (for aircraft systems):
- Compliance with [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) including AI aspects
- Demonstration of safe operation

**Operational Approval** (for ground systems):
- Safety management system integration
- Personnel training and competency
- Monitoring and reporting procedures

## 15. Lessons Learned and Continuous Improvement

### 15.1 Post-Project Review

**Activities**:
- Certification process review
- Identify successes and challenges
- Document lessons learned
- Update processes and standards

### 15.2 Industry Best Practices

**Engagement**:
- Participate in industry working groups
- Share experiences (anonymized)
- Adopt proven practices
- Contribute to standard evolution

## 16. References

### 16.1 Internal Documents

- [85-40-00-001 Software Architecture Overview](85-40-00-001_Software_Architecture_Overview.md)
- [85-40-00-002 Software Development Standards](85-40-00-002_Software_Development_Standards.md)
- [85-40-00-003 Software Integration Strategy](85-40-00-003_Software_Integration_Strategy.md)
- [85-40-00-004 Cybersecurity Framework](85-40-00-004_Cybersecurity_Framework.md)

### 16.2 External Standards and Guidance

- [DO-178C](https://en.wikipedia.org/wiki/DO-178C) - Software Considerations in Airborne Systems
- [DO-330](https://en.wikipedia.org/wiki/DO-178C) - Software Tool Qualification
- [DO-326A](https://www.rtca.org/content/standards-guidance-materials) - Airworthiness Security Process
- [CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Equipment, Systems, and Installations
- [ARP4754A](https://www.sae.org/standards/content/arp4754a/) - Guidelines for Development of Civil Aircraft
- [ARP4761](https://www.sae.org/standards/content/arp4761a/) - Guidelines for Conducting Safety Assessment
- [EASA AI Roadmap](https://www.easa.europa.eu/en/domains/innovation-digitalisation/artificial-intelligence)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-11-22

---
