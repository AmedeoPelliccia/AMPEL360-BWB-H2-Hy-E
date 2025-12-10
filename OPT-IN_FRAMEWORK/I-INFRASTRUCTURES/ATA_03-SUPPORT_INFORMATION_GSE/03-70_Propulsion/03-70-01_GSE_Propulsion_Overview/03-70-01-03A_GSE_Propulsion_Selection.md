---
Title: "GSE Propulsion Selection Criteria — ATA 03-70"
Identifier: "AMPEL360-03-70-01-03A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES Chapter Authority"
Language: "en"
CreatedAt: "2025-12-08"
ModifiedAt: "2025-12-08"
Abstract: "Decision framework and criteria for selecting appropriate propulsion systems for Ground Support Equipment."
Keywords: ["ATA 03","GSE","Propulsion Selection","Decision Criteria","Cost Analysis"]
Compliance:
  - "ATA iSpec 2200"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentSection: "../"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-08", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-70-01-03A - GSE Propulsion Selection Criteria

## 1. Purpose

This document establishes a **decision framework** for selecting the most appropriate propulsion technology for Ground Support Equipment (GSE) procurements and retrofits. It provides technical, operational, economic, and environmental criteria to guide propulsion system selection aligned with AMPEL360's zero-emission objectives.

## 2. Scope

### 2.1 Coverage

This document covers:
- Technical selection criteria (power, range, duty cycle)
- Operational requirements assessment
- Total cost of ownership (TCO) analysis framework
- Environmental impact evaluation
- Infrastructure readiness assessment
- Risk and technology maturity considerations

### 2.2 Applicability

Applies to:
- New GSE procurement decisions
- Existing GSE propulsion retrofit evaluations
- Fleet planning and optimization
- Third-party GSE contractor requirements

## 3. Applicable Documents

- **ATA iSpec 2200** — Information Standards for Aviation Maintenance
- **[03-70-01-01A — GSE Propulsion Types](./03-70-01-01A_GSE_Propulsion_Types.md)**
- **[03-70-01-02A — GSE Propulsion Standards](./03-70-01-02A_GSE_Propulsion_Standards.md)**
- **[03-70-01-04A — Zero Emission Strategy](./03-70-01-04A_Zero_Emission_Strategy.md)**

## 4. Selection Framework Overview

### 4.1 Multi-Criteria Decision Process

The propulsion selection process follows a structured multi-stage evaluation:

```
Stage 1: Requirements Definition
   ↓
Stage 2: Technology Screening
   ↓
Stage 3: Technical Assessment
   ↓
Stage 4: Economic Analysis (TCO)
   ↓
Stage 5: Infrastructure Assessment
   ↓
Stage 6: Risk and Maturity Evaluation
   ↓
Stage 7: Decision and Approval
```

## 5. Stage 1: Requirements Definition

### 5.1 GSE Operational Requirements

| **Parameter** | **Description** | **Typical Values** | **Impact on Selection** |
|---------------|-----------------|--------------------|-----------------------|
| **Power Requirement** | Peak and continuous power needed | 20 kW - 400 kW | Determines propulsion system sizing |
| **Duty Cycle** | Operating hours per day/shift | 2-20 hours/day | Impacts energy storage capacity |
| **Range / Endurance** | Operating time before refuel/recharge | 4-16 hours | Battery vs. H₂ FC consideration |
| **Refuel/Recharge Frequency** | Acceptable downtime for energy replenishment | 1-3 times/day | Fast refuel (H₂) vs. slow charge (battery) |
| **Operating Environment** | Indoor/outdoor, temperature range | -20°C to +45°C | Cold start capability, thermal management |
| **Maneuverability** | Turning radius, acceleration | Application specific | Weight and power distribution |

### 5.2 Operational Constraints

- **Emission Zones:** Are zero-emission operations required in specific areas?
- **Noise Restrictions:** Are there noise limits (dB levels) to comply with?
- **Maintenance Windows:** Available maintenance downtime and intervals
- **Operator Training:** Skill level and training requirements

## 6. Stage 2: Technology Screening

### 6.1 Propulsion Technology Screening Matrix

| **GSE Type** | **Power Range** | **Duty Cycle** | **Recommended Technologies** | **Not Recommended** |
|--------------|-----------------|----------------|------------------------------|---------------------|
| **Heavy-Duty Tractor** | 150-300 kW | High (12-20 h/day) | H₂ FC, H₂-Electric Hybrid | Battery Electric (insufficient range) |
| **Pushback Tug** | 100-200 kW | Medium (8-12 h/day) | H₂ FC, H₂-Electric Hybrid, Battery Electric | Diesel (emissions) |
| **Cargo Loader** | 50-150 kW | Medium (6-12 h/day) | Battery Electric, H₂ FC | Diesel (phase-out) |
| **Belt Loader** | 30-80 kW | Medium (6-10 h/day) | Battery Electric | Diesel, H₂ FC (oversized) |
| **Ground Power Unit (GPU)** | 50-100 kW | Low-Medium (4-8 h/day) | Battery Electric, H₂ FC | Diesel (emissions) |
| **Service Vehicles (Light)** | 20-50 kW | Low (2-6 h/day) | Battery Electric | All others (overkill) |

### 6.2 Preliminary Exclusion Criteria

Technologies are excluded if:
- They do not meet mandatory emission requirements
- Power capabilities are insufficient or grossly oversized
- Infrastructure is not feasible within project timeline
- Technology maturity is too low for mission-critical applications

## 7. Stage 3: Technical Assessment

### 7.1 Performance Evaluation

#### 7.1.1 Power and Energy Capacity

| **Metric** | **H₂ Fuel Cell** | **Battery Electric** | **H₂-Electric Hybrid** |
|------------|------------------|----------------------|------------------------|
| **Power Density** | 0.5-1.5 kW/kg | 0.1-0.3 kW/kg | 0.3-0.8 kW/kg |
| **Energy Density** | 1-2 kWh/kg (H₂ system) | 0.15-0.25 kWh/kg | 0.5-1.2 kWh/kg |
| **Refuel/Recharge Time** | 3-10 minutes | 30 minutes - 8 hours | 3-10 minutes (H₂) + opportunity charging |
| **Cold Start Capability** | Down to -20°C (with thermal management) | Down to -20°C (reduced capacity) | Down to -20°C |
| **Efficiency (Well-to-Wheel)** | 25-40% | 60-80% | 40-60% |

#### 7.1.2 Operational Reliability

- **Mean Time Between Failures (MTBF):**
  - H₂ FC: 5,000 - 10,000 hours (stack life)
  - Battery Electric: 2,000 - 4,000 cycles (battery life)
  - Hybrid: Dependent on component with lowest MTBF

- **Maintenance Intervals:**
  - H₂ FC: Annual inspections, stack replacement at 10,000-20,000 hours
  - Battery Electric: Minimal routine maintenance, battery health monitoring
  - Hybrid: Combined maintenance of both systems

### 7.2 Weight and Packaging Constraints

| **System** | **Weight Impact** | **Packaging Considerations** |
|------------|-------------------|-------------------------------|
| **H₂ FC + H₂ Tanks** | Moderate (lightweight H₂, but pressure vessels add weight) | Requires dedicated space for fuel cell and H₂ tanks |
| **Battery Electric** | High (battery packs are heavy) | Distributed battery placement for weight balance |
| **H₂-Electric Hybrid** | Moderate to High | Requires space for both fuel cell and battery |

## 8. Stage 4: Economic Analysis (Total Cost of Ownership)

### 8.1 TCO Framework

Total Cost of Ownership (TCO) over a typical 10-15 year lifecycle includes:

```
TCO = Capital Cost + Operating Cost + Maintenance Cost + End-of-Life Cost - Residual Value
```

### 8.2 Capital Cost Comparison (Indicative, per unit)

| **Propulsion System** | **Relative Capital Cost** | **Notes** |
|-----------------------|---------------------------|-----------|
| **Diesel (baseline)** | 1.0x | Legacy technology, lowest upfront cost |
| **Battery Electric** | 1.3-1.8x | Battery cost declining, subsidies available |
| **H₂ Fuel Cell** | 2.0-3.0x | High initial cost, decreasing with scale |
| **H₂-Electric Hybrid** | 2.2-3.2x | Combined system cost |
| **Diesel-Electric Hybrid** | 1.5-2.0x | Transitional technology |

**Note:** Subsidies, grants, and incentives can significantly reduce net capital cost for zero-emission technologies.

### 8.3 Operating Cost (Energy) Comparison

| **Propulsion System** | **Energy Cost** | **Notes** |
|-----------------------|-----------------|-----------|
| **Diesel** | €0.10-0.15 / kWh equivalent | Fuel price volatile |
| **Battery Electric** | €0.05-0.10 / kWh | Grid electricity cost |
| **H₂ Fuel Cell** | €0.08-0.15 / kWh | H₂ production method dependent (green H₂ preferred) |
| **Hybrid** | Varies | Depends on energy split strategy |

### 8.4 Maintenance Cost Comparison

| **Propulsion System** | **Annual Maintenance Cost** | **Major Overhaul** |
|-----------------------|-----------------------------|---------------------|
| **Diesel** | €3,000 - €6,000 | Engine overhaul every 5-8 years |
| **Battery Electric** | €500 - €1,500 | Battery replacement at 8-12 years |
| **H₂ Fuel Cell** | €1,500 - €3,000 | FC stack replacement at 10,000-20,000 hours |
| **Hybrid** | €2,000 - €4,500 | Combined maintenance requirements |

### 8.5 TCO Example (Heavy-Duty Tractor, 15-year lifecycle)

| **Cost Component** | **Diesel** | **Battery Electric** | **H₂ Fuel Cell** |
|--------------------|-----------|----------------------|------------------|
| **Capital Cost** | €150,000 | €220,000 | €350,000 |
| **Operating Cost (Energy)** | €180,000 | €90,000 | €120,000 |
| **Maintenance Cost** | €75,000 | €25,000 | €40,000 |
| **End-of-Life Cost** | €10,000 | €5,000 (battery recycling) | €8,000 |
| **Residual Value** | -€20,000 | -€30,000 | -€40,000 |
| **Total TCO** | **€395,000** | **€310,000** | **€478,000** |

**Key Insight:** Battery electric has the lowest TCO for suitable applications, but H₂ fuel cell becomes competitive for heavy-duty, high-utilization scenarios when considering operational flexibility and range.

## 9. Stage 5: Infrastructure Assessment

### 9.1 Infrastructure Readiness Checklist

| **Infrastructure Element** | **Battery Electric** | **H₂ Fuel Cell** | **Hybrid** |
|----------------------------|----------------------|------------------|------------|
| **Energy Supply** | Grid electricity (upgrades may be needed) | H₂ production/delivery | Both |
| **Refueling/Charging Stations** | Charging stations (AC/DC) | H₂ refueling stations | Both types |
| **Maintenance Facilities** | Standard electrical shop | Specialized H₂ and HV training | Combined capabilities |
| **Safety Systems** | HV safety, fire suppression | H₂ detection, ventilation, fire suppression | Combined safety systems |
| **Training Programs** | HV certification | H₂ handling certification | Combined training |

### 9.2 Infrastructure Investment Requirements

Estimate costs for:
- Installation of charging infrastructure (€50,000 - €200,000 per DC fast charger)
- Installation of H₂ refueling station (€500,000 - €2,000,000 depending on capacity)
- Facility modifications (ventilation, detection, safety systems)
- Training and certification programs

### 9.3 Timeline Considerations

- **Battery Electric:** 6-12 months for infrastructure deployment
- **H₂ Fuel Cell:** 12-24 months for H₂ infrastructure deployment
- **Hybrid:** Longest timeline (combination of both)

## 10. Stage 6: Risk and Technology Maturity Evaluation

### 10.1 Technology Readiness Level (TRL)

| **Propulsion Technology** | **TRL** | **Maturity Assessment** |
|---------------------------|---------|-------------------------|
| **Battery Electric** | TRL 9 | Fully mature, widely deployed |
| **H₂ Fuel Cell (PEM)** | TRL 8-9 | Proven in transit buses and trucks, emerging in GSE |
| **H₂-Electric Hybrid** | TRL 7-8 | Demonstrated in commercial applications, limited GSE deployment |
| **Diesel-Electric Hybrid** | TRL 9 | Mature technology, but transitional only |

### 10.2 Risk Assessment

| **Risk Category** | **Battery Electric** | **H₂ Fuel Cell** | **Hybrid** |
|-------------------|----------------------|------------------|------------|
| **Technology Risk** | Low | Medium | Medium |
| **Supply Chain Risk** | Medium (battery materials) | Medium-High (H₂ supply) | Medium-High |
| **Infrastructure Risk** | Low | High | High |
| **Regulatory Risk** | Low | Low-Medium | Low-Medium |
| **Operational Risk** | Low | Medium | Medium |

### 10.3 Mitigation Strategies

- **Technology Risk:** Pilot programs before full fleet conversion
- **Supply Chain Risk:** Long-term supplier agreements, dual sourcing
- **Infrastructure Risk:** Phased infrastructure deployment
- **Regulatory Risk:** Engage with authorities early in design phase
- **Operational Risk:** Comprehensive training, backup conventional units during transition

## 11. Stage 7: Decision and Approval

### 11.1 Decision Criteria Weighting

Recommended weighting for decision scoring (adjustable per stakeholder priorities):

| **Criterion** | **Weight** | **Notes** |
|---------------|-----------|-----------|
| **Zero-Emission Compliance** | 25% | Mandatory strategic objective |
| **Technical Suitability** | 20% | Must meet performance requirements |
| **Total Cost of Ownership** | 20% | Economic viability |
| **Infrastructure Feasibility** | 15% | Can it be implemented in required timeline? |
| **Technology Maturity / Risk** | 10% | Lower risk preferred |
| **Operational Flexibility** | 10% | Adaptability to changing requirements |

### 11.2 Approval Process

1. **Technical Review:** Engineering assessment of selected propulsion system
2. **Financial Approval:** Budget allocation and TCO validation
3. **Safety Approval:** Compliance with safety standards and risk acceptance
4. **Executive Approval:** Strategic alignment and final authorization

## 12. Cross-References

- **Related ATA Chapters:**
  - ATA 03-00-03 — Requirements (operational requirements)
  - ATA 03-00-09 — Production Planning (fleet planning)
  - ATA 03-80 — Energy (infrastructure planning)

- **Parent Document:** [03-70_Propulsion](../)

- **Related Documents:**
  - [03-70-01-01A — GSE Propulsion Types](./03-70-01-01A_GSE_Propulsion_Types.md)
  - [03-70-01-04A — Zero Emission Strategy](./03-70-01-04A_Zero_Emission_Strategy.md)
  - [03-70-02 — H2 Fuel Cell Propulsion](../03-70-02_H2_Fuel_Cell_Propulsion/)
  - [03-70-03 — Electric Propulsion GSE](../03-70-03_Electric_Propulsion_GSE/)

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_.
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-08.

---
