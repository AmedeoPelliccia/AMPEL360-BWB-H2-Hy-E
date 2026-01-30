# 03-80-06-03A - Peak Shaving Systems

## 1. Purpose
This document specifies peak shaving systems for Ground Support Equipment (GSE) operations to reduce maximum electrical demand and associated utility charges.

## 2. Scope
This specification covers:
- Peak shaving strategies and technologies
- Battery energy storage for peak shaving
- On-site generation integration
- Control algorithms and optimization
- Economic analysis and benefits

## 3. Applicable Documents
- ISO 50001 (Energy Management Systems)
- IEC 62933 (Electrical Energy Storage Systems)
- IEEE 1547 (Interconnection of Distributed Energy Resources)
- IEEE 2030.7 (Microgrid Controllers)

## 4. Energy System Description

### 4.1 Overview
Peak shaving reduces maximum electrical demand from the grid by using energy storage, on-site generation, or load management to "shave" demand peaks, thereby reducing utility demand charges.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Peak Reduction Target | 20-40% of baseline peak demand | Depends on economics |
| Battery Storage Capacity | 1-4 hours at peak reduction power | Typical sizing |
| Response Time | <1 second | Battery systems |
| System Efficiency | >85% round-trip | Battery charge-discharge |
| Payback Period | 3-7 years | Depends on demand charges |

### 4.3 Performance Requirements

**Peak Shaving Effectiveness**:
- Consistently reduce peak demand below target threshold
- Avoid creating new peaks (rebound effect)
- Maintain adequate energy reserve for operational needs

**Economic Performance**:
- Positive return on investment (ROI)
- Demand charge savings exceed system costs over lifetime

### 4.4 Peak Shaving Technologies

#### 4.4.1 Battery Energy Storage
- Most common and flexible solution
- Fast response, high cycling capability
- Can also provide other services (backup power, renewable integration)

#### 4.4.2 On-Site Generation
- Diesel, natural gas, or H2 generators
- Operate during peak demand periods
- Higher emissions than batteries (unless H2)

#### 4.4.3 Load Management
- Defer flexible loads during peak periods
- Complementary to storage/generation
- See 03-80-06-02A_Load_Management

### 4.5 Control Strategies

**Threshold-Based Control**:
- Discharge battery when grid demand exceeds threshold
- Simple, predictable, but not optimal

**Predictive Control**:
- Forecast demand and optimize battery operation
- Model Predictive Control (MPC) algorithms
- Maximize savings while maintaining operational constraints

**Machine Learning**:
- Learn demand patterns over time
- Adapt control strategy automatically
- Improve performance with experience

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Energy Management | ISO 50001 | EnMS, demand management |
| Energy Storage Safety | IEC 62933, NFPA 855 | Battery system design and operation |
| Grid Interconnection | IEEE 1547 | If providing grid services |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Battery Energy Systems: 03-80-05_Battery_Energy_Systems
- Load Management: 03-80-06-02A_Load_Management
- Energy Monitoring: 03-80-06-01A_Energy_Monitoring

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 GSE Energy WG | Initial release |

---

## Document Control

- **Status**: DRAFT – Subject to review and approval
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Energy Working Group
- **Next Review**: 2026-03-08
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-08

---
