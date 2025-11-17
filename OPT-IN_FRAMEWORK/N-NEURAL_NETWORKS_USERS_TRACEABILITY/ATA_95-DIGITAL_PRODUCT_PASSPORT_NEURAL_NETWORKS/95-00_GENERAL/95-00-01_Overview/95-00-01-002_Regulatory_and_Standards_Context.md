# 95-00-01-002 — Regulatory and Standards Context

**Document ID**: 95-00-01-002  
**Version**: 1.0  
**Date**: 2025-11-17  
**Status**: Active

---

## 1. Introduction

This document establishes the regulatory and standards landscape governing Digital Product Passports for neural networks and AI systems in the AMPEL360 program. It provides a comprehensive mapping of applicable requirements and guidance material.

---

## 2. EU Digital Product Passport Framework

### 2.1 Core Regulations

**Ecodesign for Sustainable Products Regulation (ESPR)** — (EU) 2023/1781
- Establishes mandatory DPP requirements for products placed on EU market
- Requires digital traceability of materials, components, and lifecycle data
- Mandates information sharing across supply chain
- **AMPEL360 Application**: Neural network models treated as digital "products" requiring lifecycle transparency

**Battery Regulation** — (EU) 2023/1542
- Sets precedent for digital passport structure and data elements
- Requires carbon footprint declaration, sourcing transparency, circularity information
- **AMPEL360 Application**: Template for AI model energy consumption tracking and computational resource lifecycle

**AI Act** — (EU) 2024/1689 (Proposed)
- Classifies AI systems by risk level (unacceptable, high, limited, minimal)
- Mandates conformity assessment for high-risk AI in aviation
- Requires technical documentation, logging, human oversight, robustness testing
- **AMPEL360 Application**: Flight control and safety-critical neural networks fall under high-risk category

### 2.2 Implementing Acts & Delegated Regulations

- **Product-Specific DPP Specifications**: Awaiting aviation-specific implementing acts
- **Data Carrier Standards**: QR codes, NFC tags, digital twins for information access
- **Interoperability Requirements**: Data schema, API standards, cross-border data exchange

---

## 3. Aviation Certification Standards

### 3.1 EASA Regulations

**CS-25 (Large Aeroplanes)**
- Certification Specifications for transport category aircraft
- Amendment 28 introduces AI considerations in system safety assessment
- **Relevant Sections**: CS 25.1309 (Equipment, systems and installations), AMC 25.1309

**EASA AI Roadmap 2.0** (2023)
- Phased approach to AI certification
- Emphasis on explainability, robustness, continuous learning constraints
- Concept Paper: "Artificial Intelligence in Aviation"

**Proposed Special Condition: AI/ML Systems in Flight-Critical Applications**
- Additional means of compliance beyond DO-178C
- Requirements for training data validation, model interpretability, runtime monitoring
- **AMPEL360 Application**: Direct applicability to ATA 22, 27 neural network functions

### 3.2 FAA Regulations

**14 CFR Part 25** (Airworthiness Standards)
- Equivalent to EASA CS-25
- Policy Statement: "Software Approval Guidelines" (PS-ACE100-2001-004)

**FAA Order 8110.114** — Compliance Findings for AI/ML-Based Systems (Draft)
- Guidance for applicants and FAA engineers
- Issue papers on neural network verification, validation, and assurance

### 3.3 DO-178C & DO-254 (AI Extensions)

**DO-178C** (Software Considerations in Airborne Systems)
- Baseline for software certification (Design Assurance Level A-D)
- **Gaps for AI**: Non-determinism, emergent behavior, data-driven development
- **Supplement in Development**: RTCA SC-147 / EUROCAE WG-114 AI Assurance Guidance

**DO-254** (Hardware Design Assurance)
- Applicable to AI accelerators, neural processing units
- Hardware-software co-design considerations for AI inference engines

---

## 4. AI/ML Lifecycle Standards

### 4.1 ISO/IEC Standards

**ISO/IEC 5338:2023** — AI System Lifecycle Process
- Framework for AI system development from concept to retirement
- Aligns with AMPEL360 14-folder lifecycle structure (95-00-01 through 95-00-14)

**ISO/IEC 23053:2022** — Framework for AI System Using ML
- Requirements for data quality, model validation, performance monitoring

**ISO/IEC 24029-1:2021** — Assessment of Neural Network Robustness
- Test methodologies for adversarial robustness, input perturbations, edge cases

**ISO/IEC 42001** — AI Management System (under development)
- Organizational governance framework for AI deployment

### 4.2 Safety & Risk Standards

**ARP 4754A** — Development of Civil Aircraft Systems
- System-level safety process
- **Extension for AI**: Hazard analysis considering ML model failure modes

**ARP 4761** — Safety Assessment Process
- Fault tree analysis (FTA), failure modes and effects analysis (FMEA)
- **AI Adaptation**: Probabilistic model behavior, out-of-distribution detection

**ISO 26262** (Automotive) / IEC 61508 (Industrial)
- Cross-industry lessons for safety-critical AI
- ASIL/SIL decomposition approaches applicable to aviation

---

## 5. Data & Information Standards

### 5.1 Technical Publications

**S1000D** — International specification for technical publications
- Issue 6.0 includes provisions for dynamic content and digital twins
- **AMPEL360 Application**: DPP data modules structured per S1000D conventions

**ATA iSpec 2200** — Information Standards for Aviation Maintenance
- ATA chapter numbering system (basis for ATA 95)
- Data module code structure

### 5.2 Data Exchange & Interoperability

**ARINC 653** — Avionics Application Software Standard Interface
- Partitioning for AI applications in Integrated Modular Avionics (IMA)

**AFDX / ARINC 664** — Avionics Full-Duplex Switched Ethernet
- Network infrastructure for AI inference data distribution

**IEEE 1451** — Smart Transducer Interface Standards
- Sensor data ingestion for AI/ML models

---

## 6. Cybersecurity & Data Protection

### 6.1 Cybersecurity Standards

**ED-202A / DO-326A** — Airworthiness Security Process Specification
- Security threat analysis for AI systems
- Protection against adversarial attacks on neural networks

**ED-203A / DO-356A** — Airworthiness Security Methods
- Secure coding, penetration testing, vulnerability management

### 6.2 Data Privacy

**GDPR** — General Data Protection Regulation (EU) 2016/679
- Constraints on use of personal data in AI training
- Right to explanation for automated decisions
- **AMPEL360 Application**: Anonymization of maintenance logs, flight data used for model training

---

## 7. Environmental & Sustainability Standards

### 7.1 Carbon Accounting

**GHG Protocol Product Standard** — Greenhouse Gas Accounting
- Scope 1, 2, 3 emissions for AI model training and inference
- **AMPEL360 Application**: Energy consumption tracking for neural network operations

**ISO 14067** — Carbon Footprint of Products
- Lifecycle carbon assessment methodology

### 7.2 Circular Economy

**ISO 59020** — Circular Economy Principles
- Model reuse, transfer learning, knowledge distillation as circularity strategies

---

## 8. Industry Best Practices & Guidelines

### 8.1 Aviation Industry Working Groups

**RTCA SC-147 / EUROCAE WG-114** — AI in Aviation
- Joint RTCA/EUROCAE working group developing AI assurance guidance
- Expected publication: 2025-2026

**SAE G-34** — Artificial Intelligence in Aviation
- Standards development for AI testing, validation, certification

### 8.2 Cross-Industry AI Governance

**OECD AI Principles** — Responsible AI stewardship
**IEEE Ethically Aligned Design** — AI ethics framework
**NIST AI Risk Management Framework** — Trustworthy AI characteristics

---

## 9. AMPEL360 Compliance Strategy

The AMPEL360 program adopts a **proactive compliance posture**:

1. **Monitor Regulatory Evolution**: Continuous tracking of EASA, FAA guidance development
2. **Early Engagement**: Pre-application meetings with authorities on AI certification approach
3. **Conservative Design**: Emphasize explainability, determinism, runtime monitoring
4. **Comprehensive Documentation**: DPP as single source of truth for AI compliance artifacts
5. **Cross-Reference Traceability**: Explicit links between DPP elements and certification requirements

---

## 10. Standards Gap Analysis

### 10.1 Identified Gaps

| Gap Area                           | Current Standards       | AMPEL360 Approach                          |
| ---------------------------------- | ----------------------- | ------------------------------------------ |
| Continuous learning in flight      | Not addressed           | Prohibit in-flight learning (frozen models)|
| Neural network formal verification | Emerging (ISO 24029)    | Hybrid: formal + extensive testing         |
| Adversarial robustness             | Limited guidance        | Implement input validation, anomaly detect |
| Model lifecycle management         | Generic IT practices    | Adapt DO-178C config mgmt to AI models    |
| Carbon footprint of AI training    | No aviation-specific std| Use GHG Protocol + internal tracking      |

### 10.2 Industry Leadership Opportunities

AMPEL360's comprehensive DPP framework positions the program to:

- **Contribute to standards development** (RTCA, EUROCAE, ISO working groups)
- **Pilot novel compliance methods** (shadow mode testing, digital twin validation)
- **Share lessons learned** (open-source portions of DPP tooling)

---

## 11. Document Control

| Version | Date       | Author                 | Changes                                    |
| ------- | ---------- | ---------------------- | ------------------------------------------ |
| 1.0     | 2025-11-17 | AMPEL360 Documentation | Initial release — Regulatory & Standards   |

---

### Document Metadata

- **Originator**: AI prompted by Amedeo Pelliccia
- **Toolchain**: GitHub Copilot + AMPEL360 Documentation Standards
- **Status**: `WORKING`
- **Notes**: This document was generated with AI assistance and must be reviewed and approved by a designated human checker/approver before being used as an official baseline.

---

**Previous Document**: [95-00-01-001_DPP_Purpose_and_Scope.md](95-00-01-001_DPP_Purpose_and_Scope.md)

**Next Document**: [95-00-01-003_DPP_Key_Concepts_and_Definitions.md](95-00-01-003_DPP_Key_Concepts_and_Definitions.md)

**Parent**: [95-00-01_Overview README](README.md)
